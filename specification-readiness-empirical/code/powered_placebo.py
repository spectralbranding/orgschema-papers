"""Powered re-run (run 2) of the zero-activity-filer placebo for 2026an.

Run 1 (`zero_activity_placebo.py`, 2026-08-09) returned n = 30 against n = 20, primary
d = -.457, Welch p = .065 -- INDETERMINATE by its own pre-registered rule, and in the
OPPOSITE direction to the paper's premise. This run resolves that at power and enters the
two candidate mechanism variables -- document length and boilerplate share -- explicitly.

EVERYTHING here is fixed in advance by `PRE_EXPERIMENT_NOTES_POWERED.md`. Read it before
changing anything. In particular:

  * The MEASURE is unchanged and may not be tuned. This module IMPORTS the embedding,
    cosine, rescaling, section-extraction and statistics functions from run 1 rather than
    restating them, so "the measure is unchanged" is enforced by the code.
  * MODEL PINNING: pre-registered study code. `bert-base-uncased` is pinned literally
    inside run 1 and must NEVER be resolved through the shared model registry. A newer
    embedding model is a reason to keep this pin, not to change it.
  * Three panel deviations from run 1 (fiscal years 2011+, year-matched pair selection for
    the operating panel, full-index draw across all four quarters of year Y and Y+1) are
    each declared and reasoned in the pre-registration. No fourth deviation is permitted.

Data: SEC EDGAR only. Public, no licence, no authentication. Fair-access rate limit
respected via run 1's `fetch`, with its declared User-Agent, and sharing run 1's on-disk
cache -- so a re-run pays EDGAR only for filings not already fetched.

Run (in order; --build needs no torch, --score needs no network):

    uv run python code/powered_placebo.py --build
    uv run --with torch --with transformers python code/powered_placebo.py --score

Outputs (in `output/powered/`):
    screen/<cik>.json          per-firm XBRL screening extract, so a re-build is free
    panel_zero_powered.csv     the zero-activity panel, one row per firm-year pair
    panel_operating_powered.csv
    build.log / score.log
    results_powered.json       every reported statistic
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
import statistics
import sys
from collections import Counter
from dataclasses import asdict, dataclass, fields
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import zero_activity_placebo as base  # noqa: E402  (path set above)

OUT = HERE / "output"
POW = OUT / "powered"
SCREEN = POW / "screen"

# ---- fixed by PRE_EXPERIMENT_NOTES_POWERED.md -------------------------------------------

SEED2 = 20260815  # operating-panel draw. Run 1's SEED seeds the embedder, inside base.
TARGET_N = 100  # 93% power against run 1's d = .457; 80% against d = .40
POWER_FLOOR_N = 76  # below this per panel, the run reports itself as still underpowered
MIN_FY = date(2011, 1, 1)  # XBRL company-facts coverage is universal from here
BOILERPLATE_DF = 0.05  # a tetragram in >= 5% of union-corpus documents is boilerplate
TETRAGRAM = 4

# Run 1's cross-firm baseline (200 unrelated-firm pairs), for ceiling-relative reporting.
CEILING_BASELINE = {"sci_bert": 0.979, "sci_bow": 0.925}


# --------------------------------------------------------------------------- pairs


@dataclass
class PPair:
    panel: str
    cik: str
    name: str
    sic: str
    fy_t: str
    fy_prev: str
    url_t: str
    url_prev: str
    words_t: int = 0
    words_prev: int = 0
    revenue_t: float | None = None
    revenue_prev: float | None = None
    sci_bert: float | None = None
    sci_bow: float | None = None
    sci_bert_item1: float | None = None
    boilerplate_t: float | None = None
    boilerplate_prev: float | None = None


def _d(x: str) -> date:
    y, m, dd = (int(v) for v in x.split("-"))
    return date(y, m, dd)


def all_consecutive_pairs(filings: list[tuple[str, str, str]], cik: str) -> list[tuple]:
    """Every 10-K pair whose period ends are 330-400 days apart, most recent first.

    Run 1 returned only the most recent such pair. The operating panel needs to be able to
    select the pair that matches a required fiscal year (deviation 2).
    """
    out = []
    for i in range(len(filings) - 1):
        t, prev = filings[i], filings[i + 1]
        if not t[0] or not prev[0]:
            continue
        try:
            gap = (_d(t[0]) - _d(prev[0])).days
        except ValueError:
            continue
        if not (330 <= gap <= 400):
            continue

        def url(f):
            return (
                f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
                f"{f[1].replace('-', '')}/{f[2]}"
            )

        out.append((t[0], prev[0], url(t), url(prev)))
    out.sort(reverse=True)
    return out


def in_window(fy_t: str, fy_prev: str) -> bool:
    """Deviation 1: both fiscal years must end on or after 2011-01-01."""
    try:
        return _d(fy_prev) >= MIN_FY and _d(fy_t) >= MIN_FY
    except ValueError:
        return False


# --------------------------------------------------------------------------- XBRL screen


def _revenue_from_facts(facts: dict, fy_end: str) -> float | None:
    """Run 1's `revenue_for_fy` rule, evaluated against a single companyfacts payload.

    Identical tag list, identical form filter, identical >=300-day duration filter,
    identical max-across-tags rule. Only the TRANSPORT differs: one companyfacts request
    instead of five companyconcept requests per fiscal year. `--build` asserts equivalence
    against run 1's own function on run 1's own firms before it screens anything new; that
    check is free, because every fetch it makes is a cache hit.
    """
    gaap = facts.get("facts", {}).get("us-gaap", {})
    best = None
    for tag in base.REVENUE_TAGS:
        node = gaap.get(tag)
        if not node:
            continue
        for unit_rows in node.get("units", {}).values():
            for row in unit_rows:
                if row.get("end") != fy_end or row.get("form") not in (
                    "10-K",
                    "10-K/A",
                ):
                    continue
                if row.get("start"):
                    try:
                        if (_d(row["end"]) - _d(row["start"])).days < 300:
                            continue
                    except ValueError:
                        pass
                val = row.get("val")
                if isinstance(val, (int, float)):
                    best = val if best is None else max(best, val)
    return best


def _has_assets(facts: dict, fy_end: str) -> bool:
    """Does the firm report a us-gaap Assets fact at this period end, in a 10-K?

    Deviation 1's integrity check. A post-2011 10-K filer reports Assets in XBRL. If it
    does, then "no revenue tag reports a nonzero value" is a REPORTED zero rather than an
    absence of data -- which is exactly the distinction run 1 could not make for its 2006
    and 2010 pairs.
    """
    node = facts.get("facts", {}).get("us-gaap", {}).get("Assets")
    if not node:
        return False
    for unit_rows in node.get("units", {}).values():
        for row in unit_rows:
            if row.get("end") == fy_end and row.get("form") in ("10-K", "10-K/A"):
                return True
    return False


def screen(cik: str, fy_ends: list[str], log) -> dict | None:
    """Cached per-firm screening extract: revenue and Assets-presence at each fy end."""
    sp = SCREEN / f"{cik}.json"
    have = {}
    if sp.exists():
        try:
            have = json.loads(sp.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            have = {}
    if all(fy in have.get("rev", {}) for fy in fy_ends):
        return have
    try:
        body = base.fetch(
            f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json",
            cache=False,
            tolerate_404=True,
        )
    except Exception as exc:
        log(f"    {cik}: companyfacts failed ({type(exc).__name__})")
        return None
    facts = {}
    if body:
        try:
            facts = json.loads(body)
        except json.JSONDecodeError:
            facts = {}
    rec = {"rev": dict(have.get("rev", {})), "assets": dict(have.get("assets", {}))}
    for fy in fy_ends:
        rec["rev"][fy] = _revenue_from_facts(facts, fy)
        rec["assets"][fy] = _has_assets(facts, fy)
    SCREEN.mkdir(parents=True, exist_ok=True)
    sp.write_text(json.dumps(rec), encoding="utf-8")
    return rec


def verify_screen_equivalence(log) -> dict:
    """Assert the transport change is a transport change, on run 1's own firms.

    Every fetch here is a cache hit, so this costs nothing and touches no network.
    """
    checked = agree = 0
    disagreements = []
    for fn in ("panel_zero.csv", "panel_operating.csv"):
        p = OUT / fn
        if not p.exists():
            continue
        lines = p.read_text(encoding="utf-8").strip().splitlines()
        cols = lines[0].split(";")
        for line in lines[1:]:
            row = dict(zip(cols, line.split(";")))
            cik, fy = row["cik"], row["fy_t"]
            old = base.revenue_for_fy(cik, fy)
            rec = screen(cik, [fy], log)
            new = (rec or {}).get("rev", {}).get(fy)
            checked += 1
            if (old or 0) == (new or 0):
                agree += 1
            else:
                disagreements.append({"cik": cik, "fy": fy, "run1": old, "run2": new})
    log(f"  screen equivalence: {agree}/{checked} agree")
    for d0 in disagreements:
        log(f"    DISAGREE {d0}")
    return {"checked": checked, "agree": agree, "disagreements": disagreements}


# --------------------------------------------------------------------------- panels


def build_zero(scan: int, target: int, log) -> list[PPair]:
    log("\n[1/2] zero-activity panel — SIC 6770, no revenue reported, FY 2011+")
    cands = base.blank_check_ciks(scan)
    log(f"  scanned {len(cands)} blank-check CIKs from EDGAR")
    out: list[PPair] = []
    rej = Counter()
    for cik in cands:
        if len(out) >= target:
            break
        try:
            name, sic, filings = base.submission_10ks(cik)
        except Exception as exc:
            rej[f"submissions failed ({type(exc).__name__})"] += 1
            continue
        pairs = [
            p for p in all_consecutive_pairs(filings, cik) if in_window(p[0], p[1])
        ]
        if not pairs:
            rej["no consecutive 10-K pair in window"] += 1
            continue
        fy_t, fy_prev, url_t, url_prev = pairs[0]  # most recent, per run 1
        rec = screen(cik, [fy_t, fy_prev], log)
        if rec is None:
            rej["screen failed"] += 1
            continue
        if not (rec["assets"].get(fy_t) and rec["assets"].get(fy_prev)):
            rej["no XBRL Assets fact — coverage unproven"] += 1
            continue
        if (rec["rev"].get(fy_t) or 0) != 0 or (rec["rev"].get(fy_prev) or 0) != 0:
            rej["reports revenue"] += 1
            continue
        p = PPair(
            panel="zero",
            cik=cik,
            name=name,
            sic=sic,
            fy_t=fy_t,
            fy_prev=fy_prev,
            url_t=url_t,
            url_prev=url_prev,
            revenue_t=rec["rev"].get(fy_t),
            revenue_prev=rec["rev"].get(fy_prev),
        )
        if base.attach_sections(p, log) is None:
            rej["item 7 not extractable / under 200 words"] += 1
            continue
        out.append(p)
        log(
            f"  + {len(out):3d} {p.name[:42]:42} {p.fy_prev} -> {p.fy_t} "
            f"({p.words_prev}/{p.words_t} words)"
        )
    log(f"  zero panel n={len(out)}; rejected {dict(rej)}")
    return out


def index_ciks(years: list[int], log) -> dict[int, list[str]]:
    """Deviation 3: 10-K filers from all four quarters of year Y and Y+1, per needed Y."""
    pool: dict[int, list[str]] = {}
    fetched: dict[int, list[str]] = {}

    def year_ciks(y: int) -> list[str]:
        if y in fetched:
            return fetched[y]
        seen: list[str] = []
        for qtr in (1, 2, 3, 4):
            try:
                body = base.fetch(
                    f"https://www.sec.gov/Archives/edgar/full-index/{y}/QTR{qtr}/form.idx",
                    tolerate_404=True,
                )
            except Exception as exc:
                log(f"    index {y}Q{qtr} failed ({type(exc).__name__})")
                continue
            if not body:
                continue
            for line in body.splitlines():
                if not line.startswith("10-K "):
                    continue
                parts = re.split(r"\s{2,}", line.strip())
                if len(parts) < 4:
                    continue
                c = parts[2].strip()
                if c.isdigit():
                    seen.append(c.zfill(10))
        fetched[y] = list(dict.fromkeys(seen))
        log(f"  index {y}: {len(fetched[y])} distinct 10-K filers")
        return fetched[y]

    for y in sorted(set(years)):
        merged = list(dict.fromkeys(year_ciks(y) + year_ciks(y + 1)))
        pool[y] = merged
    return pool


def build_operating(
    year_need: Counter, target: int, exclude: set[str], scan_per_year: int, log
) -> list[PPair]:
    log(
        "\n[2/2] operating panel — random 10-K filers, matched fiscal years, revenue > $50M"
    )
    rng = random.Random(SEED2)
    pool = index_ciks(list(year_need), log)
    out: list[PPair] = []
    rej = Counter()
    used: set[str] = set(exclude)
    # Fill the scarcest years first: a year with few candidates must not lose its
    # candidates to a year that has plenty.
    for y in sorted(year_need, key=lambda k: (len(pool.get(k, [])), k)):
        need = year_need[y]
        cands = list(pool.get(y, []))
        rng.shuffle(cands)
        got = 0
        for cik in cands[:scan_per_year]:
            if got >= need or len(out) >= target:
                break
            if cik in used:
                continue
            try:
                name, sic, filings = base.submission_10ks(cik)
            except Exception as exc:
                rej[f"submissions failed ({type(exc).__name__})"] += 1
                continue
            pairs = [
                p
                for p in all_consecutive_pairs(filings, cik)
                if in_window(p[0], p[1]) and p[0][:4] == str(y)
            ]
            if not pairs:
                rej["no pair ending in the needed year"] += 1
                continue
            fy_t, fy_prev, url_t, url_prev = pairs[0]
            rec = screen(cik, [fy_t, fy_prev], log)
            if rec is None:
                rej["screen failed"] += 1
                continue
            rt, rp = rec["rev"].get(fy_t), rec["rev"].get(fy_prev)
            if rt is None or rp is None:
                rej["no revenue reported"] += 1
                continue
            if rt < base.OPERATING_MIN_REVENUE or rp < base.OPERATING_MIN_REVENUE:
                rej["revenue below floor"] += 1
                continue
            p = PPair(
                panel="operating",
                cik=cik,
                name=name,
                sic=sic,
                fy_t=fy_t,
                fy_prev=fy_prev,
                url_t=url_t,
                url_prev=url_prev,
                revenue_t=rt,
                revenue_prev=rp,
            )
            if base.attach_sections(p, log) is None:
                rej["item 7 not extractable / under 200 words"] += 1
                continue
            used.add(cik)
            out.append(p)
            got += 1
            log(
                f"  + {len(out):3d} [{y}] {p.name[:36]:36} {p.fy_prev} -> {p.fy_t} "
                f"({p.words_prev}/{p.words_t} words)"
            )
        if got < need:
            log(f"  year {y}: filled {got}/{need}")
    log(f"  operating panel n={len(out)}; rejected {dict(rej)}")
    return out


# --------------------------------------------------------------------------- boilerplate


def _tokens(text: str) -> list[str]:
    return base.WORD_RE.findall(text.lower())


def _tetragram_ids(toks: list[str]) -> list[int]:
    out = []
    for i in range(len(toks) - TETRAGRAM + 1):
        key = " ".join(toks[i : i + TETRAGRAM]).encode()
        out.append(int.from_bytes(hashlib.blake2b(key, digest_size=8).digest(), "big"))
    return out


def boilerplate_shares(docs: dict[str, str], log) -> dict[str, float]:
    """Share of each document's tetragram positions that are boilerplate.

    A tetragram is boilerplate if it occurs in >= BOILERPLATE_DF of the UNION corpus --
    every MD&A from both panels and both fiscal years -- so neither panel sets its own
    threshold. Definition fixed in the pre-registration before any document was read.
    """
    grams = {k: _tetragram_ids(_tokens(v)) for k, v in docs.items()}
    df: Counter = Counter()
    for g in grams.values():
        df.update(set(g))
    cutoff = max(2, math.ceil(BOILERPLATE_DF * len(grams)))
    log(
        f"  boilerplate: {len(grams)} documents, {len(df)} distinct tetragrams, "
        f"cutoff = {cutoff} documents"
    )
    shares = {}
    for k, g in grams.items():
        shares[k] = 0.0 if not g else sum(1 for x in g if df[x] >= cutoff) / len(g)
    return shares


# --------------------------------------------------------------------------- OLS


def ols(y: list[float], X: list[list[float]], names: list[str]) -> dict:
    """Least squares with an intercept, classical standard errors. n x k, k small."""
    n, k = len(y), len(X[0]) + 1
    A = [[1.0] + row for row in X]
    xtx = [
        [sum(A[i][a] * A[i][b] for i in range(n)) for b in range(k)] for a in range(k)
    ]
    xty = [sum(A[i][a] * y[i] for i in range(n)) for a in range(k)]
    inv = _inverse(xtx)
    if inv is None:
        return {"error": "singular design matrix"}
    beta = [sum(inv[a][b] * xty[b] for b in range(k)) for a in range(k)]
    fitted = [sum(beta[a] * A[i][a] for a in range(k)) for i in range(n)]
    resid = [y[i] - fitted[i] for i in range(n)]
    sse = sum(r * r for r in resid)
    ybar = statistics.fmean(y)
    sst = sum((v - ybar) ** 2 for v in y)
    dof = n - k
    s2 = sse / dof
    terms = []
    for a, nm in enumerate(["intercept"] + names):
        se = math.sqrt(max(s2 * inv[a][a], 0.0))
        t = beta[a] / se if se > 0 else 0.0
        terms.append(
            {
                "term": nm,
                "coef": beta[a],
                "se": se,
                "t": t,
                "p": 2.0 * base._t_sf(abs(t), dof) if se > 0 else 1.0,
            }
        )
    return {
        "n": n,
        "df_resid": dof,
        "r2": 0.0 if sst == 0 else 1.0 - sse / sst,
        "terms": terms,
    }


def _inverse(m: list[list[float]]) -> list[list[float]] | None:
    k = len(m)
    a = [row[:] + [1.0 if i == j else 0.0 for j in range(k)] for i, row in enumerate(m)]
    for col in range(k):
        piv = max(range(col, k), key=lambda r: abs(a[r][col]))
        if abs(a[piv][col]) < 1e-14:
            return None
        a[col], a[piv] = a[piv], a[col]
        d = a[col][col]
        a[col] = [v / d for v in a[col]]
        for r in range(k):
            if r == col:
                continue
            f = a[r][col]
            if f:
                a[r] = [v - f * w for v, w in zip(a[r], a[col])]
    return [row[k:] for row in a]


# --------------------------------------------------------------------------- csv io


def write_csv(rows: list[PPair], path: Path) -> None:
    cols = [f.name for f in fields(PPair)]
    lines = [";".join(cols)]
    for p in rows:
        r = asdict(p)
        lines.append(
            ";".join("" if r[c] is None else str(r[c]).replace(";", ",") for c in cols)
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_csv(path: Path) -> list[PPair]:
    lines = path.read_text(encoding="utf-8").strip().splitlines()
    cols = lines[0].split(";")
    types = {f.name: f.type for f in fields(PPair)}
    out = []
    for line in lines[1:]:
        r = dict(zip(cols, line.split(";")))
        kw = {}
        for c in cols:
            v = r.get(c, "")
            if v == "":
                kw[c] = None if "None" in str(types[c]) else 0
            elif "int" in str(types[c]) and "float" not in str(types[c]):
                kw[c] = int(v)
            elif "float" in str(types[c]):
                kw[c] = float(v)
            else:
                kw[c] = v
        out.append(PPair(**kw))
    return out


# --------------------------------------------------------------------------- phases


def phase_build(args, log) -> int:
    log(
        f"seed2={SEED2} target_n={args.target_n} min_fy={MIN_FY} (BUILD, no torch needed)"
    )
    eq = verify_screen_equivalence(log)
    if eq["disagreements"]:
        log(
            "  ABORT: the screening transport is not equivalent to run 1's. Do not proceed."
        )
        return 3
    zero = build_zero(args.scan_blank_check, args.target_n, log)
    if len(zero) < 10:
        log("  ABORT: zero panel too small to report anything.")
        return 2
    years = Counter(int(p.fy_t[:4]) for p in zero)
    log(f"  fiscal-year distribution: {dict(sorted(years.items()))}")
    oper = build_operating(
        years, args.target_n, {p.cik for p in zero}, args.scan_per_year, log
    )
    POW.mkdir(parents=True, exist_ok=True)
    write_csv(zero, POW / "panel_zero_powered.csv")
    write_csv(oper, POW / "panel_operating_powered.csv")
    log(f"\nBUILD DONE: zero n={len(zero)}, operating n={len(oper)} -> {POW}")
    return 0


def phase_score(args, log) -> int:
    zero = read_csv(POW / "panel_zero_powered.csv")
    oper = read_csv(POW / "panel_operating_powered.csv")
    log(f"scoring: zero n={len(zero)}, operating n={len(oper)} (SCORE, cache only)")

    sections: dict[str, dict] = {}
    docs: dict[str, str] = {}
    for p in zero + oper:
        raw_t, raw_prev = base.fetch(p.url_t), base.fetch(p.url_prev)
        txt_t, txt_prev = base.to_text(raw_t), base.to_text(raw_prev)
        s = {
            "item7_t": base.extract_section(txt_t, base.ITEM7_START, base.ITEM7_END),
            "item7_prev": base.extract_section(
                txt_prev, base.ITEM7_START, base.ITEM7_END
            ),
            "item1_t": base.extract_section(txt_t, base.ITEM1_START, base.ITEM1_END),
            "item1_prev": base.extract_section(
                txt_prev, base.ITEM1_START, base.ITEM1_END
            ),
        }
        sections[p.cik] = s
        docs[f"{p.cik}:t"] = s["item7_t"] or ""
        docs[f"{p.cik}:prev"] = s["item7_prev"] or ""

    log("\n[1/4] boilerplate share over the union corpus")
    shares = boilerplate_shares(docs, log)
    for p in zero + oper:
        p.boilerplate_t = shares.get(f"{p.cik}:t")
        p.boilerplate_prev = shares.get(f"{p.cik}:prev")

    log(f"\n[2/4] embedding with {base.BERT_MODEL} (pinned; do not substitute)")
    emb = base.Embedder()

    def score(pairs: list[PPair], label: str) -> None:
        for i, p in enumerate(pairs, 1):
            s = sections[p.cik]
            if s["item7_t"] and s["item7_prev"]:
                et, ep = emb.embed(s["item7_t"]), emb.embed(s["item7_prev"])
                if et is not None and ep is not None:
                    p.sci_bert = base.rescale(emb.cosine(et, ep))
                p.sci_bow = base.rescale(base.bow_cosine(s["item7_t"], s["item7_prev"]))
            if s["item1_t"] and s["item1_prev"]:
                e1t, e1p = emb.embed(s["item1_t"]), emb.embed(s["item1_prev"])
                if e1t is not None and e1p is not None:
                    p.sci_bert_item1 = base.rescale(emb.cosine(e1t, e1p))
            if i % 10 == 0:
                log(f"  {label}: {i}/{len(pairs)}")

    score(zero, "zero-activity")
    score(oper, "operating")

    log("\n[3/4] statistics")
    results: dict = {
        "run": 2,
        "seed_operating_draw": SEED2,
        "seed_embedder": base.SEED,
        "model": base.BERT_MODEL,
        "min_fiscal_year_end": str(MIN_FY),
        "boilerplate_df_threshold": BOILERPLATE_DF,
        "n_zero": len(zero),
        "n_operating": len(oper),
        "target_n": TARGET_N,
        "power_floor_n": POWER_FLOOR_N,
        "underpowered": min(len(zero), len(oper)) < POWER_FLOOR_N,
        "years_zero": dict(sorted(Counter(int(p.fy_t[:4]) for p in zero).items())),
        "years_operating": dict(sorted(Counter(int(p.fy_t[:4]) for p in oper).items())),
    }

    def compare(field_name: str, name: str) -> dict | None:
        a = [getattr(p, field_name) for p in zero if getattr(p, field_name) is not None]
        b = [getattr(p, field_name) for p in oper if getattr(p, field_name) is not None]
        if len(a) < 5 or len(b) < 5:
            return None
        t, df, p_t = base.welch(a, b)
        u, p_u = base.mann_whitney(a, b)
        r = {
            "measure": name,
            "n_zero": len(a),
            "n_operating": len(b),
            "mean_zero": statistics.fmean(a),
            "sd_zero": statistics.stdev(a),
            "median_zero": statistics.median(a),
            "mean_operating": statistics.fmean(b),
            "sd_operating": statistics.stdev(b),
            "median_operating": statistics.median(b),
            "diff": statistics.fmean(a) - statistics.fmean(b),
            "welch_t": t,
            "df": df,
            "p": p_t,
            "cohens_d": base.cohens_d(a, b),
            "mann_whitney_u": u,
            "p_mw": p_u,
        }
        baseline = CEILING_BASELINE.get(field_name)
        if baseline:
            # Ceiling-relative reporting rule: where each panel mean sits in the realized
            # range of the index, whose floor is run 1's unrelated-firm baseline.
            span = 1.0 - baseline
            r["ceiling_baseline"] = baseline
            r["mean_zero_ceiling_relative"] = (r["mean_zero"] - baseline) / span
            r["mean_operating_ceiling_relative"] = (
                r["mean_operating"] - baseline
            ) / span
            r["diff_as_share_of_realized_range"] = r["diff"] / span
        log(
            f"  {name}: zero M={base.fmt(r['mean_zero'])} (SD {base.fmt(r['sd_zero'])}) vs "
            f"operating M={base.fmt(r['mean_operating'])} (SD {base.fmt(r['sd_operating'])}); "
            f"d={base.fmt(r['cohens_d'])}, p {base.fmt_p(p_t)}"
        )
        return r

    results["primary"] = compare("sci_bert", "SCI (BERT, Item 7) — PRIMARY")
    results["bow"] = compare("sci_bow", "SCI (bag-of-words, Item 7)")
    results["item1"] = compare("sci_bert_item1", "SCI (BERT, Item 1)")

    # ---- the mechanism variables, described before they are modelled
    def mech(pairs: list[PPair]) -> dict:
        length = [(p.words_t + p.words_prev) / 2 for p in pairs]
        bp = [
            (p.boilerplate_t + p.boilerplate_prev) / 2
            for p in pairs
            if p.boilerplate_t is not None and p.boilerplate_prev is not None
        ]
        return {
            "length_mean": statistics.fmean(length),
            "length_median": statistics.median(length),
            "length_min": min(length),
            "length_max": max(length),
            "boilerplate_mean": statistics.fmean(bp) if bp else None,
            "boilerplate_median": statistics.median(bp) if bp else None,
        }

    results["mechanism_zero"] = mech(zero)
    results["mechanism_operating"] = mech(oper)
    log(
        f"  length: zero M={results['mechanism_zero']['length_mean']:.0f} words vs "
        f"operating M={results['mechanism_operating']['length_mean']:.0f}"
    )
    log(
        f"  boilerplate share: zero M={base.fmt(results['mechanism_zero']['boilerplate_mean'] or 0)} "
        f"vs operating M={base.fmt(results['mechanism_operating']['boilerplate_mean'] or 0)}"
    )

    # ---- the mechanism model
    log("\n[4/4] mechanism model — SCI ~ zero_panel + log_length + boilerplate_share")
    ys, Xs, X1 = [], [], []
    for p in zero + oper:
        if p.sci_bert is None or p.boilerplate_t is None or p.boilerplate_prev is None:
            continue
        length = (p.words_t + p.words_prev) / 2
        if length <= 0:
            continue
        z = 1.0 if p.panel == "zero" else 0.0
        bp = (p.boilerplate_t + p.boilerplate_prev) / 2
        ys.append(p.sci_bert)
        X1.append([z])
        Xs.append([z, math.log(length), bp])
    if len(ys) >= 20:
        results["model_unadjusted"] = ols(ys, X1, ["zero_panel"])
        results["model_mechanism"] = ols(
            ys, Xs, ["zero_panel", "log_length", "boilerplate_share"]
        )
        results["model_length_only"] = ols(
            ys, [[r[0], r[1]] for r in Xs], ["zero_panel", "log_length"]
        )
        for key in ("model_unadjusted", "model_length_only", "model_mechanism"):
            m = results[key]
            log(f"  {key}: R2={base.fmt(m['r2'])}")
            for term in m["terms"]:
                log(
                    f"    {term['term']:<20} b={term['coef']:+.6f} "
                    f"SE={term['se']:.6f} t={term['t']:+.3f} p {base.fmt_p(term['p'])}"
                )
    else:
        results["model_mechanism"] = None

    # ---- length-stratified arm, as run 1 pre-registered it
    all_len = sorted((p.words_t + p.words_prev) / 2 for p in zero + oper)
    lo, hi = all_len[len(all_len) // 3], all_len[2 * len(all_len) // 3]

    def band(pairs):
        return [
            p.sci_bert
            for p in pairs
            if p.sci_bert is not None and lo <= (p.words_t + p.words_prev) / 2 <= hi
        ]

    zs, os_ = band(zero), band(oper)
    if len(zs) >= 5 and len(os_) >= 5:
        t, df, p_t = base.welch(zs, os_)
        results["length_matched"] = {
            "measure": "SCI (BERT, Item 7) — middle length tercile",
            "n_zero": len(zs),
            "n_operating": len(os_),
            "mean_zero": statistics.fmean(zs),
            "mean_operating": statistics.fmean(os_),
            "welch_t": t,
            "df": df,
            "p": p_t,
            "cohens_d": base.cohens_d(zs, os_),
            "word_band": [lo, hi],
        }
        log(
            f"  length-matched ({lo:.0f}-{hi:.0f} words): d="
            f"{base.fmt(base.cohens_d(zs, os_))}, p {base.fmt_p(p_t)}"
        )
    else:
        results["length_matched"] = None

    # ---- verdict, by the four-outcome rule fixed in the pre-registration
    results["verdict"], results["verdict_reason"] = verdict(results)
    log(f"\nVERDICT: {results['verdict']} — {results['verdict_reason']}")

    write_csv(zero, POW / "panel_zero_powered.csv")
    write_csv(oper, POW / "panel_operating_powered.csv")
    (POW / "results_powered.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8"
    )
    log(f"\nSCORE DONE -> {POW}/results_powered.json")
    return 0


def verdict(results: dict) -> tuple[str, str]:
    pri = results.get("primary")
    if pri is None:
        return (
            "INDETERMINATE",
            "the primary measure could not be computed on enough pairs",
        )
    d, p = pri["cohens_d"], pri["p"]
    under = results["underpowered"]
    if pri["diff"] >= 0 and p < 0.05:
        return (
            "KILL — BY-CONSTRUCTION DIRECTION",
            "the zero-activity panel scores at or above the operating panel, which is the "
            "direction the paper originally asserted and the one that follows trivially from "
            "a similarity measure; the 2026-08-15 correction is reverted and the line closes",
        )
    if pri["diff"] < 0 and p < 0.05:
        mech = results.get("model_mechanism")
        leng = results.get("model_length_only")
        named = False
        for m in (leng, mech):
            if not m or "terms" not in m:
                continue
            for t in m["terms"]:
                if t["term"] == "zero_panel" and t["p"] >= 0.05:
                    named = True
        if named:
            return (
                "PROCEED — INVERSION, MECHANISM NAMED",
                "the inversion holds at power and entering document length removes the panel "
                "effect; what the index reads as readiness is substantially a length artifact",
            )
        return (
            "PROCEED WITH CAUTION — INVERSION, MECHANISM NOT NAMED",
            "the inversion holds at power and survives both covariates; real and unexplained, "
            "which licenses no mechanism claim",
        )
    if abs(d) < 0.2 and not under:
        return (
            "KILL — POWERED NULL",
            "no separation and no inversion at adequate power; the surviving claim is the one "
            "run 1 already licenses, that no instrument abstains",
        )
    return (
        "INDETERMINATE",
        "still underpowered or between the thresholds; an underpowered null is not evidence "
        "of absence and is not written as one",
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--build", action="store_true", help="panels only; network, no torch"
    )
    ap.add_argument(
        "--score", action="store_true", help="measure + statistics; no network"
    )
    ap.add_argument("--scan-blank-check", type=int, default=3000)
    ap.add_argument("--scan-per-year", type=int, default=900)
    ap.add_argument("--target-n", type=int, default=TARGET_N)
    args = ap.parse_args()
    if not (args.build or args.score):
        ap.error("choose --build or --score")

    POW.mkdir(parents=True, exist_ok=True)
    SCREEN.mkdir(parents=True, exist_ok=True)
    base.OUT.mkdir(exist_ok=True)
    base.CACHE.mkdir(exist_ok=True)
    lines: list[str] = []

    def log(msg: str) -> None:
        print(msg, flush=True)
        lines.append(msg)

    rc = 0
    try:
        if args.build:
            rc = phase_build(args, log)
            (POW / "build.log").write_text("\n".join(lines) + "\n", encoding="utf-8")
        if rc == 0 and args.score:
            lines.clear()
            rc = phase_score(args, log)
            (POW / "score.log").write_text("\n".join(lines) + "\n", encoding="utf-8")
    finally:
        pass
    return rc


if __name__ == "__main__":
    sys.exit(main())
