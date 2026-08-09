"""Zero-activity-filer placebo for the Specification Coherence Index (2026an).

The paper's robustness battery specifies this check and has never run it:

    Compute the published index unchanged on a panel of structurally zero-activity filers
    against matched operating firms. If the zero-activity panel scores at or above the
    operating panel, the confound is demonstrated on the paper's own measure; if it does
    not, this whole item is void and should be deleted.

Everything here is fixed in advance by `PRE_EXPERIMENT_NOTES.md`, which was written before
the first run. Read it before changing anything in this file -- the measure is the PUBLISHED
one and may not be tuned, and the decision rule is stated there in the paper's own words.

MODEL PINNING: this is study code for a pre-registered run, so it pins its model literally
(`bert-base-uncased`) and must NEVER resolve it through the shared model registry. A newer
embedding model is a reason to keep this pin, not to change it -- the point of the placebo is
that it runs the index the paper published, not a better one.

Data: SEC EDGAR only. Public, no licence, no authentication. Fair-access rate limit respected
with a declared User-Agent per https://www.sec.gov/os/accessing-edgar-data.

Run:
    uv run --with torch --with transformers python code/zero_activity_placebo.py

Outputs (written to an `output/` directory beside this script):
    cache/            fetched filings + extracted sections, so re-analysis needs no re-fetch
    panel_zero.csv    the zero-activity panel, one row per firm-year pair
    panel_operating.csv
    results.json      every reported statistic
    RESULTS.md        the human-readable result table
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import math
import random
import re
import statistics
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

SEED = 20260809
HERE = Path(__file__).resolve().parent
OUT = HERE / "output"
CACHE = OUT / "cache"

# SEC fair access: declare who is calling and stay well under 10 requests/second.
UA = {"User-Agent": "Spectral Branding Research dmitry@spectralbranding.com"}
SLEEP = 0.16

# The measure, pinned literally. See MODEL PINNING in the module docstring.
BERT_MODEL = "bert-base-uncased"
MAX_TOKENS = 512

# Panel screens, fixed by PRE_EXPERIMENT_NOTES.md.
SIC_BLANK_CHECK = "6770"
OPERATING_MIN_REVENUE = 50_000_000
MIN_SECTION_WORDS = 200
TARGET_N = 30

REVENUE_TAGS = [
    "Revenues",
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "RevenueFromContractWithCustomerIncludingAssessedTax",
    "SalesRevenueNet",
    "SalesRevenueGoodsNet",
]


# --------------------------------------------------------------------------- fetching


def _cache_path(url: str, suffix: str = ".txt") -> Path:
    return CACHE / (hashlib.sha256(url.encode()).hexdigest()[:24] + suffix)


def fetch(url: str, *, cache: bool = True, tolerate_404: bool = False) -> str | None:
    """GET with on-disk caching. Returns None on a tolerated 404."""
    cp = _cache_path(url)
    if cache and cp.exists():
        return cp.read_text(encoding="utf-8")
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=UA)
            body = (
                urllib.request.urlopen(req, timeout=90)
                .read()
                .decode("utf-8", "replace")
            )
            time.sleep(SLEEP)
            if cache:
                cp.write_text(body, encoding="utf-8")
            return body
        except urllib.error.HTTPError as exc:
            if exc.code == 404 and tolerate_404:
                return None
            if exc.code in (403, 429) and attempt < 2:
                time.sleep(2 + 3 * attempt)
                continue
            if attempt == 2:
                raise
        except Exception:
            if attempt == 2:
                raise
            time.sleep(1.5)
    return None


# --------------------------------------------------------------------------- extraction


def to_text(raw_html: str) -> str:
    """Strip a filing to narrative text.

    Tables are removed rather than flattened: the paper's construction strips non-narrative
    content (financial tables, exhibits, references), and a flattened financial table is a
    long run of numerals that would dominate any bag-of-words representation.
    """
    h = re.sub(r"(?is)<(script|style|table)[^>]*>.*?</\1>", " ", raw_html)
    h = re.sub(r"(?is)<[^>]+>", " ", h)
    h = html.unescape(h).replace("\xa0", " ")
    # Normalise typographic punctuation -- SEC filings use curly apostrophes in the very
    # headings the section regexes have to match ("Management's").
    for a, b in (
        ("’", "'"),
        ("‘", "'"),
        ("“", '"'),
        ("”", '"'),
        ("–", "-"),
        ("—", "-"),
    ):
        h = h.replace(a, b)
    return re.sub(r"\s+", " ", h).strip()


ITEM7_START = re.compile(r"item\s*7\s*[\.\:\-]?\s*management'?s\s+discussion", re.I)
ITEM7_END = re.compile(
    r"item\s*(?:7a|8)\s*[\.\:\-]?\s*(?:quantitative|financial\s+statements)", re.I
)
ITEM1_START = re.compile(r"item\s*1\s*[\.\:\-]?\s*business\b", re.I)
ITEM1_END = re.compile(r"item\s*1a\s*[\.\:\-]?\s*risk\s+factors", re.I)


def extract_section(text: str, start_re: re.Pattern, end_re: re.Pattern) -> str | None:
    """Longest start->end span. The longest span skips the table-of-contents hit, whose
    span to the next heading is a line or two."""
    starts = [m.start() for m in start_re.finditer(text)]
    ends = [m.start() for m in end_re.finditer(text)]
    best = None
    for s in starts:
        after = [e for e in ends if e > s]
        if not after:
            continue
        span = text[s : after[0]]
        if best is None or len(span) > len(best):
            best = span
    return best


# --------------------------------------------------------------------------- panels


@dataclass
class Pair:
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


def submission_10ks(cik: str) -> tuple[str, str, list[tuple[str, str, str]]]:
    body = fetch(f"https://data.sec.gov/submissions/CIK{cik}.json")
    s = json.loads(body)
    rec = s["filings"]["recent"]
    out = []
    for i, form in enumerate(rec["form"]):
        if form != "10-K" or not rec["primaryDocument"][i]:
            continue
        out.append(
            (rec["reportDate"][i], rec["accessionNumber"][i], rec["primaryDocument"][i])
        )
    out.sort(reverse=True)
    return s.get("name", ""), str(s.get("sic", "")), out


def consecutive_pair(filings: list[tuple[str, str, str]], cik: str) -> tuple | None:
    """Most recent pair of 10-Ks whose period ends are 330-400 days apart."""
    from datetime import date

    def d(x: str) -> date:
        y, m, dd = (int(v) for v in x.split("-"))
        return date(y, m, dd)

    for i in range(len(filings) - 1):
        t, prev = filings[i], filings[i + 1]
        if not t[0] or not prev[0]:
            continue
        gap = (d(t[0]) - d(prev[0])).days
        if 330 <= gap <= 400:

            def url(f):
                return (
                    f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
                    f"{f[1].replace('-', '')}/{f[2]}"
                )

            return t[0], prev[0], url(t), url(prev)
    return None


def revenue_for_fy(cik: str, fy_end: str) -> float | None:
    """Largest revenue value reported for a period ending at fy_end, across the standard
    tags. None means no tag reported anything for that period."""
    best = None
    for tag in REVENUE_TAGS:
        body = fetch(
            f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/{tag}.json",
            tolerate_404=True,
        )
        if not body:
            continue
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            continue
        for unit_rows in data.get("units", {}).values():
            for row in unit_rows:
                if row.get("end") != fy_end or row.get("form") not in (
                    "10-K",
                    "10-K/A",
                ):
                    continue
                # annual figures only
                if row.get("start"):
                    try:
                        from datetime import date

                        y, m, d0 = (int(v) for v in row["start"].split("-"))
                        y2, m2, d2 = (int(v) for v in row["end"].split("-"))
                        if (date(y2, m2, d2) - date(y, m, d0)).days < 300:
                            continue
                    except Exception:
                        pass
                val = row.get("val")
                if isinstance(val, (int, float)):
                    best = val if best is None else max(best, val)
    return best


def blank_check_ciks(max_scan: int) -> list[str]:
    ciks: list[str] = []
    start = 0
    while len(ciks) < max_scan:
        url = (
            "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany"
            f"&SIC={SIC_BLANK_CHECK}&type=10-K&dateb=&owner=include&count=100"
            f"&start={start}&output=atom"
        )
        body = fetch(url)
        found = list(dict.fromkeys(re.findall(r"CIK=(\d{10})", body or "")))
        if not found:
            break
        for c in found:
            if c not in ciks:
                ciks.append(c)
        start += 100
        if start > 3000:
            break
    return ciks[:max_scan]


def operating_ciks(years: list[int], sample: int, rng: random.Random) -> list[str]:
    """Random 10-K filers from EDGAR's quarterly full index for the relevant years."""
    seen: list[str] = []
    for year in sorted(set(years)):
        for qtr in (1, 2, 3):
            body = fetch(
                f"https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{qtr}/form.idx",
                tolerate_404=True,
            )
            if not body:
                continue
            for line in body.splitlines():
                if not line.startswith("10-K "):
                    continue
                parts = re.split(r"\s{2,}", line.strip())
                if len(parts) < 4:
                    continue
                cik = parts[2].strip()
                if cik.isdigit():
                    padded = cik.zfill(10)
                    if padded not in seen:
                        seen.append(padded)
    rng.shuffle(seen)
    return seen[:sample]


def build_pair(cik: str, *, want_zero: bool, log) -> Pair | None:
    try:
        name, sic, filings = submission_10ks(cik)
    except Exception as exc:
        log(f"    {cik}: submissions failed ({type(exc).__name__})")
        return None
    if len(filings) < 2:
        return None
    cp = consecutive_pair(filings, cik)
    if not cp:
        return None
    fy_t, fy_prev, url_t, url_prev = cp
    try:
        rev_t = revenue_for_fy(cik, fy_t)
        rev_prev = revenue_for_fy(cik, fy_prev)
    except Exception as exc:
        log(f"    {cik}: xbrl failed ({type(exc).__name__})")
        return None

    if want_zero:
        # structurally zero-activity: no revenue tag reports anything nonzero in EITHER year
        if (rev_t or 0) != 0 or (rev_prev or 0) != 0:
            return None
    else:
        if rev_t is None or rev_prev is None:
            return None
        if rev_t < OPERATING_MIN_REVENUE or rev_prev < OPERATING_MIN_REVENUE:
            return None

    return Pair(
        cik=cik,
        name=name,
        sic=sic,
        fy_t=fy_t,
        fy_prev=fy_prev,
        url_t=url_t,
        url_prev=url_prev,
        revenue_t=rev_t,
        revenue_prev=rev_prev,
    )


def attach_sections(p: Pair, log) -> dict | None:
    """Fetch both filings and pull Item 7 (and Item 1 for the pre-registered robustness)."""
    try:
        raw_t = fetch(p.url_t)
        raw_prev = fetch(p.url_prev)
    except Exception as exc:
        log(f"    {p.cik}: filing fetch failed ({type(exc).__name__})")
        return None
    if not raw_t or not raw_prev:
        return None
    txt_t, txt_prev = to_text(raw_t), to_text(raw_prev)
    s7_t = extract_section(txt_t, ITEM7_START, ITEM7_END)
    s7_prev = extract_section(txt_prev, ITEM7_START, ITEM7_END)
    if not s7_t or not s7_prev:
        return None
    if (
        len(s7_t.split()) < MIN_SECTION_WORDS
        or len(s7_prev.split()) < MIN_SECTION_WORDS
    ):
        return None
    p.words_t, p.words_prev = len(s7_t.split()), len(s7_prev.split())
    return {
        "item7_t": s7_t,
        "item7_prev": s7_prev,
        "item1_t": extract_section(txt_t, ITEM1_START, ITEM1_END),
        "item1_prev": extract_section(txt_prev, ITEM1_START, ITEM1_END),
    }


# --------------------------------------------------------------------------- the measure


class Embedder:
    def __init__(self) -> None:
        import torch
        from transformers import AutoModel, AutoTokenizer

        self.torch = torch
        torch.manual_seed(SEED)
        self.tok = AutoTokenizer.from_pretrained(BERT_MODEL)
        self.model = AutoModel.from_pretrained(BERT_MODEL)
        self.model.eval()

    def embed(self, text: str):
        """Mean of mean-pooled non-overlapping 512-token windows. Chunking rule declared in
        PRE_EXPERIMENT_NOTES.md and applied identically to both panels."""
        torch = self.torch
        ids = self.tok(text, add_special_tokens=False)["input_ids"]
        if not ids:
            return None
        body = MAX_TOKENS - 2
        chunks = [ids[i : i + body] for i in range(0, len(ids), body)]
        vecs = []
        with torch.no_grad():
            for ch in chunks:
                inp = torch.tensor(
                    [[self.tok.cls_token_id] + ch + [self.tok.sep_token_id]]
                )
                mask = torch.ones_like(inp)
                out = self.model(input_ids=inp, attention_mask=mask).last_hidden_state
                vecs.append(out.mean(dim=1).squeeze(0))
        return torch.stack(vecs).mean(dim=0)

    def cosine(self, a, b) -> float:
        return float(
            self.torch.nn.functional.cosine_similarity(a.unsqueeze(0), b.unsqueeze(0))
        )


WORD_RE = re.compile(r"[a-z]{2,}")


def bow_cosine(a: str, b: str) -> float:
    ca, cb = Counter(WORD_RE.findall(a.lower())), Counter(WORD_RE.findall(b.lower()))
    keys = set(ca) | set(cb)
    dot = sum(ca[k] * cb[k] for k in keys)
    na = math.sqrt(sum(v * v for v in ca.values()))
    nb = math.sqrt(sum(v * v for v in cb.values()))
    return 0.0 if na == 0 or nb == 0 else dot / (na * nb)


def rescale(c: float) -> float:
    """Published spec: cosine in [-1, 1] rescaled to [0, 1]."""
    return (c + 1.0) / 2.0


# --------------------------------------------------------------------------- statistics


def welch(a: list[float], b: list[float]) -> tuple[float, float, float]:
    """Welch t, df, two-sided p (Student-t survival via continued fraction)."""
    na, nb = len(a), len(b)
    ma, mb = statistics.fmean(a), statistics.fmean(b)
    va, vb = statistics.variance(a), statistics.variance(b)
    se2 = va / na + vb / nb
    if se2 == 0:
        return 0.0, float(na + nb - 2), 1.0
    t = (ma - mb) / math.sqrt(se2)
    df = se2**2 / ((va / na) ** 2 / (na - 1) + (vb / nb) ** 2 / (nb - 1))
    return t, df, 2.0 * _t_sf(abs(t), df)


def _betacf(a: float, b: float, x: float) -> float:
    tiny = 1e-30
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = tiny if abs(d) < tiny else d
    d = 1.0 / d
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = tiny if abs(d) < tiny else d
        c = 1.0 + aa / c
        c = tiny if abs(c) < tiny else c
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = tiny if abs(d) < tiny else d
        c = 1.0 + aa / c
        c = tiny if abs(c) < tiny else c
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 3e-12:
            break
    return h


def _betai(a: float, b: float, x: float) -> float:
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(lbeta + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return front * _betacf(a, b, x) / a
    return 1.0 - front * _betacf(b, a, 1 - x) / b


def _t_sf(t: float, df: float) -> float:
    return 0.5 * _betai(df / 2.0, 0.5, df / (df + t * t))


def cohens_d(a: list[float], b: list[float]) -> float:
    na, nb = len(a), len(b)
    va, vb = statistics.variance(a), statistics.variance(b)
    sp = math.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))
    return 0.0 if sp == 0 else (statistics.fmean(a) - statistics.fmean(b)) / sp


def mann_whitney(a: list[float], b: list[float]) -> tuple[float, float]:
    """U for sample a, plus a normal-approximation two-sided p with tie correction."""
    combined = sorted([(v, 0) for v in a] + [(v, 1) for v in b])
    ranks: list[float] = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[k] = avg
        i = j + 1
    ra = sum(r for r, (_, g) in zip(ranks, combined) if g == 0)
    na, nb = len(a), len(b)
    u = ra - na * (na + 1) / 2.0
    mu = na * nb / 2.0
    tie_groups = Counter(v for v, _ in combined)
    n = na + nb
    tie_term = sum(t**3 - t for t in tie_groups.values())
    sigma = math.sqrt((na * nb / 12.0) * ((n + 1) - tie_term / (n * (n - 1))))
    if sigma == 0:
        return u, 1.0
    z = (u - mu) / sigma
    return u, 2.0 * (1.0 - 0.5 * (1.0 + math.erf(abs(z) / math.sqrt(2))))


def fmt_p(p: float) -> str:
    return "< .001" if p < 0.001 else f"= {p:.3f}".replace("0.", ".")


def fmt(x: float) -> str:
    s = f"{x:.3f}"
    return s.replace("0.", ".", 1) if s.startswith("0.") else s.replace("-0.", "-.", 1)


# --------------------------------------------------------------------------- driver


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--scan-blank-check",
        type=int,
        default=700,
        help="how many SIC-6770 CIKs to scan for a usable 10-K pair",
    )
    ap.add_argument(
        "--scan-operating",
        type=int,
        default=600,
        help="how many random 10-K filers to scan for the operating panel",
    )
    ap.add_argument("--target-n", type=int, default=TARGET_N)
    args = ap.parse_args()

    OUT.mkdir(exist_ok=True)
    CACHE.mkdir(exist_ok=True)
    rng = random.Random(SEED)
    log_lines: list[str] = []

    def log(msg: str) -> None:
        print(msg, flush=True)
        log_lines.append(msg)

    log(f"seed={SEED} model={BERT_MODEL} target_n={args.target_n}")

    # ---- zero-activity panel
    log("\n[1/5] zero-activity panel (SIC 6770 + no revenue reported in either year)")
    cands = blank_check_ciks(args.scan_blank_check)
    log(f"  scanned {len(cands)} blank-check CIKs")
    zero: list[Pair] = []
    zero_sections: dict[str, dict] = {}
    rejected = Counter()
    for cik in cands:
        if len(zero) >= args.target_n:
            break
        p = build_pair(cik, want_zero=True, log=log)
        if not p:
            rejected["no pair / has revenue"] += 1
            continue
        sec = attach_sections(p, log)
        if not sec:
            rejected["item 7 not extractable"] += 1
            continue
        zero.append(p)
        zero_sections[p.cik] = sec
        log(
            f"  + {len(zero):2d} {p.name[:44]:44} {p.fy_prev} -> {p.fy_t}  "
            f"({p.words_prev}/{p.words_t} words)"
        )
    log(f"  zero-activity panel n={len(zero)}; rejected {dict(rejected)}")
    if len(zero) < 10:
        log("  ABORT: panel too small to report anything.")
        return 2

    years = [int(p.fy_t[:4]) for p in zero]
    log(f"  fiscal-year distribution: {dict(sorted(Counter(years).items()))}")

    # ---- operating panel, same filing years
    log(
        "\n[2/5] operating panel (random 10-K filers, same years, revenue > $50M both years)"
    )
    op_c = operating_ciks(years, args.scan_operating, rng)
    log(f"  scanned {len(op_c)} random 10-K filer CIKs")
    year_need = Counter(years)
    oper: list[Pair] = []
    op_sections: dict[str, dict] = {}
    op_rejected = Counter()
    for cik in op_c:
        if len(oper) >= args.target_n:
            break
        p = build_pair(cik, want_zero=False, log=log)
        if not p:
            op_rejected["no pair / revenue below floor"] += 1
            continue
        y = int(p.fy_t[:4])
        if year_need[y] <= 0:
            op_rejected["year already filled"] += 1
            continue
        sec = attach_sections(p, log)
        if not sec:
            op_rejected["item 7 not extractable"] += 1
            continue
        year_need[y] -= 1
        oper.append(p)
        op_sections[p.cik] = sec
        log(
            f"  + {len(oper):2d} {p.name[:44]:44} {p.fy_prev} -> {p.fy_t}  "
            f"({p.words_prev}/{p.words_t} words)"
        )
    log(f"  operating panel n={len(oper)}; rejected {dict(op_rejected)}")
    if len(oper) < 10:
        log("  ABORT: comparison panel too small to report anything.")
        return 2

    # ---- the measure
    log(f"\n[3/5] embedding with {BERT_MODEL} (pinned; do not substitute)")
    emb = Embedder()

    def score(pairs: list[Pair], sections: dict[str, dict], label: str) -> None:
        for i, p in enumerate(pairs, 1):
            s = sections[p.cik]
            et, ep = emb.embed(s["item7_t"]), emb.embed(s["item7_prev"])
            if et is not None and ep is not None:
                p.sci_bert = rescale(emb.cosine(et, ep))
            p.sci_bow = rescale(bow_cosine(s["item7_t"], s["item7_prev"]))
            if s.get("item1_t") and s.get("item1_prev"):
                e1t, e1p = emb.embed(s["item1_t"]), emb.embed(s["item1_prev"])
                if e1t is not None and e1p is not None:
                    p.sci_bert_item1 = rescale(emb.cosine(e1t, e1p))
            if i % 5 == 0:
                log(f"  {label}: {i}/{len(pairs)}")

    score(zero, zero_sections, "zero-activity")
    score(oper, op_sections, "operating")

    # ---- statistics
    log("\n[4/5] statistics")
    results: dict = {
        "seed": SEED,
        "model": BERT_MODEL,
        "n_zero": len(zero),
        "n_operating": len(oper),
        "years_zero": dict(sorted(Counter(years).items())),
        "years_operating": dict(sorted(Counter(int(p.fy_t[:4]) for p in oper).items())),
    }

    def compare(field: str, name: str) -> dict | None:
        a = [getattr(p, field) for p in zero if getattr(p, field) is not None]
        b = [getattr(p, field) for p in oper if getattr(p, field) is not None]
        if len(a) < 5 or len(b) < 5:
            return None
        t, df, p_t = welch(a, b)
        u, p_u = mann_whitney(a, b)
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
            "cohens_d": cohens_d(a, b),
            "mann_whitney_u": u,
            "p_mw": p_u,
        }
        log(
            f"  {name}: zero M={fmt(r['mean_zero'])} (SD {fmt(r['sd_zero'])}) vs "
            f"operating M={fmt(r['mean_operating'])} (SD {fmt(r['sd_operating'])}); "
            f"d={fmt(r['cohens_d'])}, p {fmt_p(p_t)}"
        )
        return r

    results["primary"] = compare("sci_bert", "SCI (BERT, Item 7) — PRIMARY")
    results["bow"] = compare("sci_bow", "SCI (bag-of-words, Item 7)")
    results["item1"] = compare("sci_bert_item1", "SCI (BERT, Item 1)")

    # length-stratified robustness: pairs whose mean MD&A length is in the middle tercile
    all_len = sorted((p.words_t + p.words_prev) / 2 for p in zero + oper)
    lo, hi = all_len[len(all_len) // 3], all_len[2 * len(all_len) // 3]
    zs = [
        p.sci_bert
        for p in zero
        if p.sci_bert is not None and lo <= (p.words_t + p.words_prev) / 2 <= hi
    ]
    os_ = [
        p.sci_bert
        for p in oper
        if p.sci_bert is not None and lo <= (p.words_t + p.words_prev) / 2 <= hi
    ]
    if len(zs) >= 5 and len(os_) >= 5:
        t, df, p_t = welch(zs, os_)
        results["length_matched"] = {
            "measure": "SCI (BERT, Item 7) — middle length tercile",
            "n_zero": len(zs),
            "n_operating": len(os_),
            "mean_zero": statistics.fmean(zs),
            "mean_operating": statistics.fmean(os_),
            "welch_t": t,
            "df": df,
            "p": p_t,
            "cohens_d": cohens_d(zs, os_),
            "word_band": [lo, hi],
        }
        log(
            f"  length-matched (middle tercile, {lo:.0f}-{hi:.0f} words): "
            f"zero M={fmt(statistics.fmean(zs))} vs operating M={fmt(statistics.fmean(os_))}, "
            f"d={fmt(cohens_d(zs, os_))}, p {fmt_p(p_t)}"
        )
    else:
        results["length_matched"] = None

    results["words_zero_mean"] = statistics.fmean(
        [(p.words_t + p.words_prev) / 2 for p in zero]
    )
    results["words_operating_mean"] = statistics.fmean(
        [(p.words_t + p.words_prev) / 2 for p in oper]
    )

    # ---- verdict, by the rule fixed in PRE_EXPERIMENT_NOTES.md
    pri = results["primary"]
    if pri is None:
        verdict, why = (
            "INDETERMINATE",
            "primary measure could not be computed on enough pairs",
        )
    elif pri["diff"] > 0 and pri["p"] < 0.05:
        verdict = "CONFIRMED"
        why = (
            "the zero-activity panel scores ABOVE the operating panel on the published index; "
            "the confound is demonstrated on the measure itself"
        )
    elif pri["diff"] < 0 and pri["p"] < 0.05:
        verdict = "VOID"
        why = (
            "the zero-activity panel scores BELOW the operating panel; by the pre-registered "
            "rule the pending item is deleted and the article's claim must be corrected"
        )
    else:
        verdict = "INDETERMINATE"
        why = "the difference does not reach the pre-registered threshold in either direction"
    results["verdict"] = verdict
    results["verdict_reason"] = why
    log(f"\n[5/5] VERDICT: {verdict} — {why}")

    # ---- write everything
    (OUT / "results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    for pairs, fn in ((zero, "panel_zero.csv"), (oper, "panel_operating.csv")):
        rows = [asdict(p) for p in pairs]
        cols = list(rows[0].keys())
        lines = [";".join(cols)]
        for r in rows:
            lines.append(
                ";".join(
                    "" if r[c] is None else str(r[c]).replace(";", ",") for c in cols
                )
            )
        (OUT / fn).write_text("\n".join(lines) + "\n", encoding="utf-8")
    (OUT / "run.log").write_text("\n".join(log_lines) + "\n", encoding="utf-8")
    log(f"\nwrote {OUT}/results.json, panel_zero.csv, panel_operating.csv, run.log")
    return 0


if __name__ == "__main__":
    sys.exit(main())
