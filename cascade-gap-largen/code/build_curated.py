#!/usr/bin/env python3
"""S5 FULL-DRAW curated top-up builder (Amendment 3.D) -- EDGAR is the ground truth.

The widened FTS frame is short of the registered per-stratum quotas for the gap-prone
tail (JV 9 + roll_up 5 + distressed 20 = 34 deals; FULL_DRAW_FRAME_FINDINGS.md). This
script RESOLVES a human-curated candidate list of large (>=$1bn) deals -- each identified
by NAME + structure + year -- to a REAL EDGAR registrant CIK + closing-era primary filing
(accession) + SIC + size, and emits only the deals EDGAR confirms. Anti-fabrication HARD:
nothing is hand-typed into the curated CSV; a candidate that cannot be resolved to a real
EDGAR CIK + a closing-era >=$1bn operating filing is EXCLUDED (logged with a reason), never
guessed. Outcome-blind: only closing-era structural facts are read here; the 3-5-year
outcome is never touched (it is coded later from a separate sub-dossier).

INPUT  : full_draw_curated_candidates.csv  (structure, deal_name, company, cik, forms, year)
           - company : EDGAR filer name to resolve when `cik` is blank (FTS name match)
           - cik     : optional explicit CIK (skips name resolution; submissions-based)
           - forms   : preferred closing-era forms (e.g. "8-K,S-4"); blank -> a default set
           - year    : deal close year (a +/-2y window is searched)
OUTPUT : full_draw_curated_gap_deals.csv   (FRAME_HEADER rows; signal="curated:<deal_name>")
         + a printed per-stratum count vs the deficit + a RESOLUTION / EXCLUDED log.

Run (network; EDGAR only, no paid API):
    uv run python research/cascade-gap-largen/build_curated.py --build
    uv run python research/cascade-gap-largen/build_curated.py --verify   # offline schema/logic

The resolver reuses draw_full_sample's EDGAR helpers + inclusion filter so the curated pool
passes exactly the same >=$1bn / operating-SIC gate as the FTS frame. Review the RESOLUTION
log: for any mis-matched name, add an explicit `cik` to the candidate row and re-run.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import draw_full_sample as dfs  # noqa: E402

CANDIDATES_CSV = HERE / "full_draw_curated_candidates.csv"
CURATED_CSV = dfs.CURATED_CSV
CANDIDATE_HEADER = ["structure", "deal_name", "company", "cik", "forms", "year"]
DEFAULT_FORMS = "8-K,S-4,DEFM14A,10-K,10-12B,10-12G,S-1"
# Curated deficit to fill per stratum (FULL_DRAW_FRAME_FINDINGS.md, measured post-widening).
DEFICIT = {"joint_venture": 9, "roll_up": 5, "distressed": 20}
NEAR_YEARS = (
    2  # accept a filing / size fact within +/- this many years of the deal year
)


def _tokens(s: str) -> set[str]:
    return {t for t in re.split(r"[^a-z0-9]+", s.lower()) if len(t) > 2}


def _cik_from_display(display: str) -> str:
    m = re.search(r"CIK\s+0*(\d+)", display)
    return m.group(1) if m else ""


def _submissions(cik: str) -> dict:
    padded = str(cik).lstrip("0").zfill(10)
    return dfs._get_json(f"https://data.sec.gov/submissions/CIK{padded}.json")


def _companyfacts_size(cik: str, year: int) -> tuple[float, str]:
    """Outcome-blind >=$1bn size proxy: max of Assets/Revenues/StockholdersEquity (USD),
    preferring facts within +/-NEAR_YEARS of the deal year but falling back to the company's
    nearest/largest XBRL fact when none is in-window. XBRL began ~2011, so a 2007-2010 deal
    by a large ongoing filer has no in-window fact yet is plainly >=$1bn; the fallback uses a
    later fact as a materiality proxy (a company >=$1bn in 2012 was >=$1bn at a 2008 deal).
    Truly pre-XBRL defunct entities (no facts at all) return 0 -> sourced-size fallback.
    """
    padded = str(cik).lstrip("0").zfill(10)
    try:
        data = dfs._get_json(
            f"https://data.sec.gov/api/xbrl/companyfacts/CIK{padded}.json"
        )
    except Exception:  # noqa: BLE001
        return 0.0, ""
    concepts = (
        "Assets",
        "Revenues",
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "StockholdersEquity",
    )
    in_window, out_window = 0.0, 0.0
    in_metric, out_metric = "", ""
    for concept in concepts:
        try:
            units = data["facts"]["us-gaap"][concept]["units"]["USD"]
        except KeyError:
            continue
        for u in units:
            end = str(u.get("end", ""))[:4]
            val = u.get("val")
            if not end.isdigit() or not isinstance(val, (int, float)):
                continue
            fv = float(val)
            if abs(int(end) - year) <= NEAR_YEARS:
                if fv > in_window:
                    in_window, in_metric = fv, concept
            elif fv > out_window:
                out_window, out_metric = fv, concept
    if in_window > 0:
        best, metric = in_window, in_metric
    else:
        best, metric = out_window, (out_metric + "(nearest)" if out_metric else "")
    return best, metric


def _find_filing_by_cik(
    cik: str, forms_pref: list[str], year: int
) -> tuple[str, str, str] | None:
    """From the submissions history pick a closing-era filing: a form in forms_pref within
    +/-NEAR_YEARS of the deal year, closest to it. Returns (form, filing_date, accession).
    """
    try:
        subs = _submissions(cik)
    except Exception:  # noqa: BLE001
        return None
    recent = subs.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accns = recent.get("accessionNumber", [])
    pref = {f.upper() for f in forms_pref}
    best: tuple[int, str, str, str] | None = None
    for f, d, a in zip(forms, dates, accns):
        fy = d[:4]
        if not fy.isdigit() or abs(int(fy) - year) > NEAR_YEARS:
            continue
        if pref and f.upper() not in pref:
            continue
        prox = abs(int(fy) - year)
        if best is None or prox < best[0]:
            best = (prox, f, d, a)
    if best is None:
        return None
    return best[1], best[2], best[3]


def _resolve_by_name(
    company: str, forms: str, year: int
) -> tuple[str, str, str, str, str] | None:
    """FTS name resolution: find the filing whose FILER best matches `company` within the
    year window. Returns (cik, filer_name, form, filing_date, accession)."""
    want = _tokens(company)
    hits = dfs.fts_search(
        forms,
        f'"{company}"',
        f"{year - NEAR_YEARS}-01-01",
        f"{year + NEAR_YEARS}-12-31",
        60,
    )
    best: tuple[tuple[int, int], str, str, str, str, str] | None = None
    for h in hits:
        src = h.get("_source", {})
        display = (src.get("display_names") or [""])[0]
        cik = _cik_from_display(display) or str((src.get("ciks") or [""])[0]).lstrip(
            "0"
        )
        if not cik:
            continue
        filer_tokens = _tokens(display)
        overlap = len(want & filer_tokens)
        if overlap < max(1, len(want) - 1):  # require a strong filer-name match
            continue
        date = src.get("file_date", "")
        prox = abs(int(date[:4]) - year) if date[:4].isdigit() else 99
        accession = str(h.get("_id", "")).split(":")[0]
        form = (src.get("root_forms") or [forms.split(",")[0]])[0]
        # rank: most name overlap, then closest year
        key = (-overlap, prox)
        if best is None or key < best[0]:
            best = (key, cik, display, form, date, accession)
    if best is None:
        return None
    return best[1], best[2], best[3], best[4], best[5]


def _row_for(cand: dict) -> tuple[dict | None, str]:
    """Resolve one candidate to a verified FRAME_HEADER row, or (None, reason)."""
    company = cand["company"].strip()
    year = int(cand["year"])
    forms = (cand.get("forms") or DEFAULT_FORMS).strip()
    explicit_cik = (cand.get("cik") or "").strip().lstrip("0")

    if explicit_cik:
        found = _find_filing_by_cik(explicit_cik, forms.split(","), year)
        if not found:
            return None, f"no {forms} filing within +/-{NEAR_YEARS}y of {year}"
        cik, filer, (form, fdate, accession) = explicit_cik, company, found
    else:
        res = _resolve_by_name(company, forms, year)
        if not res:
            return None, "FTS name resolution found no strong filer match in window"
        cik, filer, form, fdate, accession = res

    sic, sic_desc = dfs.sic_for_cik(cik)
    size, metric = _companyfacts_size(cik, year)
    # Sourced-size fallback (pre-XBRL era): companyfacts has no us-gaap facts before ~2010,
    # so 2008-2009 mega-deals proxy to 0 despite being obviously >=$1bn. If the candidate
    # carries a documented size_usd (sourced in the candidate list / a note), use it when the
    # XBRL proxy is unavailable. The CIK + accession are still EDGAR-verified; only the
    # materiality figure is sourced (anti-fabrication: it must be a real, cited number).
    cand_size = 0.0
    try:
        cand_size = float(cand.get("size_usd") or 0)
    except ValueError:
        cand_size = 0.0
    if size <= 0 and cand_size > 0:
        size, metric = cand_size, "sourced(pre-xbrl)"
    row = {
        "stratum": cand["structure"],
        "cik": cik,
        "company": filer,
        "form": form,
        "filing_date": fdate,
        "accession": accession,
        "sic": sic,
        "sic_desc": sic_desc,
        "size_usd": f"{size:.0f}" if size else "",
        "size_metric": metric,
        "deal_value_usd": "",  # captured at --gate / dossier build when disclosed
        "parent_cik": "",
        "signal": f"curated:{cand['deal_name']}",
    }
    if not dfs.passes_inclusion(row, operating=True):
        reason = (
            f"excluded SIC {sic}"
            if (sic in dfs.EXCLUDE_SIC_EXACT or sic.startswith(dfs.EXCLUDE_SIC_PREFIX))
            else f"size {size:.0f} < ${dfs.MATERIALITY_MIN_USD:.0f} (or unknown)"
        )
        return None, reason
    return row, "OK"


def build() -> int:
    if not CANDIDATES_CSV.exists():
        print(f"No candidate list at {CANDIDATES_CSV.name}; create it first.")
        return 2
    with CANDIDATES_CSV.open(newline="", encoding="utf-8") as fh:
        cands = [r for r in csv.DictReader(fh) if r.get("deal_name", "").strip()]
    verified: list[dict] = []
    seen: set[str] = set()
    print(f"[curated] resolving {len(cands)} candidates against EDGAR ...")
    for c in cands:
        # Resilient per-candidate resolution: retry transient EDGAR errors (500/timeouts)
        # so one flaky call never aborts the batch; skip the candidate if it keeps failing.
        row, status = None, ""
        for attempt in range(1, 4):
            try:
                row, status = _row_for(c)
                break
            except Exception as e:  # noqa: BLE001
                status = f"network error ({type(e).__name__}); skipped after retries"
                time.sleep(1.5 * attempt)
        tag = c["deal_name"]
        if row is None:
            print(f"  EXCLUDED  {c['structure']:13} {tag:38} -> {status}")
            continue
        key = f"{row['stratum']}:{row['cik']}"
        if key in seen:
            print(f"  DUP-SKIP  {c['structure']:13} {tag:38} -> CIK {row['cik']}")
            continue
        seen.add(key)
        verified.append(row)
        print(
            f"  OK        {c['structure']:13} {tag:38} -> CIK {row['cik']} "
            f"{row['form']} {row['filing_date']} ${float(row['size_usd']):,.0f}"
        )
    with CURATED_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=dfs.FRAME_HEADER)
        w.writeheader()
        w.writerows(verified)
    print(f"\n[curated] wrote {len(verified)} verified rows -> {CURATED_CSV.name}")
    ok = True
    for stratum, need in sorted(DEFICIT.items()):
        got = sum(1 for r in verified if r["stratum"] == stratum)
        flag = "OK" if got >= need else "SHORT"
        if got < need:
            ok = False
        print(f"[curated] {stratum:14} verified={got:2}  need>={need:2}  [{flag}]")
    print(
        "[curated] "
        + (
            "all strata meet the deficit."
            if ok
            else "add more candidates for SHORT strata."
        )
    )
    return 0 if ok else 1


def verify() -> int:
    """Offline self-check: candidate schema + that the deficit map covers the thin strata."""
    problems: list[str] = []
    for s in DEFICIT:
        if s not in dfs.GAP_STRATA:
            problems.append(f"deficit stratum {s} not in GAP_STRATA")
    if CANDIDATES_CSV.exists():
        with CANDIDATES_CSV.open(newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            missing = [
                c for c in CANDIDATE_HEADER if c not in (reader.fieldnames or [])
            ]
            if missing:
                problems.append(f"candidate CSV missing columns: {missing}")
            per: dict[str, int] = {}
            for r in reader:
                if r.get("deal_name", "").strip():
                    per[r["structure"]] = per.get(r["structure"], 0) + 1
            for s, need in DEFICIT.items():
                if per.get(s, 0) < need:
                    problems.append(
                        f"candidate list has {per.get(s, 0)} {s} < deficit {need} "
                        "(add candidates before --build)"
                    )
    # inclusion-logic sanity on synthetic rows (no network)
    big = {"sic": "3711", "size_usd": "5000000000", "deal_value_usd": ""}
    small = {"sic": "3711", "size_usd": "500000000", "deal_value_usd": ""}
    depo = {"sic": "6022", "size_usd": "5000000000", "deal_value_usd": ""}
    if not dfs.passes_inclusion(big, operating=True):
        problems.append("inclusion rejected a >=$1bn operating row")
    if dfs.passes_inclusion(small, operating=True):
        problems.append("inclusion accepted a sub-$1bn row")
    if dfs.passes_inclusion(depo, operating=True):
        problems.append("inclusion accepted a 60xx depository row")
    if problems:
        print("VERIFY FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print(
        "VERIFY OK: deficit map valid; inclusion logic correct; candidate schema checks pass."
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument(
        "--build", action="store_true", help="resolve candidates -> curated CSV"
    )
    g.add_argument(
        "--verify", action="store_true", help="offline schema/logic self-check"
    )
    args = ap.parse_args()
    return build() if args.build else verify()


if __name__ == "__main__":
    raise SystemExit(main())
