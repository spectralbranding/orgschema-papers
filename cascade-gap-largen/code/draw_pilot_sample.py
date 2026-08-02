#!/usr/bin/env python3
"""Seeded, blind-to-outcome pilot draw over SEC EDGAR (PILOT_PREREGISTRATION.md §2).

Two phases, so the seeded selection is deterministic and reproducible even though the
live EDGAR index moves (same pattern as draw_extension_sample.py: enumerate a frame
snapshot -> commit -> deterministic seeded draw on the snapshot):

  --enumerate : query EDGAR full-text search (efts.sec.gov, 2001+ index) for each
      stratum's canonical FORM TYPE within a fixed era window, dedup to the registrant
      (CIK), attach the registrant's SIC from the EDGAR submissions API, and write the
      committed frame snapshot pilot_frame_raw.csv. This step reads ONLY closing-time
      structural signals (form type, filing date, registrant, SIC) -- it never looks at
      the 3-5-year OUTCOME, so the frame is blind to outcome. Requires network.

  --draw : deterministic seeded stratified draw on the committed snapshot (NO network).
      Applies the Amendment v1.3.0 outcome-blind structural INCLUSION filter first (drop
      SIC 6770 blank-check/SPAC registrants + anything below the >= $1bn size band), then
      draws 3 carve-outs (Form 10-12B) + 2 roll-ups (S-1/S-4 self-describing a roll-up) =
      5 gap-prone cases + 5 matched going-concern controls (DEFM14A whole-company
      mergers), each matched to a gap-prone case on 2-digit SIC (nearest) + era (+/-2y),
      seeded. Writes pilot_selection.csv (slot -> deal, stratum, role, matched_to,
      size, source accessions) with NO outcome field.

Stratum <-> filing type (PILOT_PREREGISTRATION.md §2), all classified BLIND to outcome:
  - carve-out / divestiture  -> Form 10-12B (spin-off / carve-out registration)
  - roll-up                  -> S-1 / S-4 whose text describes a roll-up/consolidation
  - matched control          -> DEFM14A (definitive whole-company merger proxy)

Era window (fixed): FY2006-2018 completed transactions, so a >=3-5-year realized-
outcome window has elapsed by the 2026 coding date. Size band (>= $1bn): enumeration
attaches an outcome-blind size PROXY (largest of us-gaap Assets/Revenues/equity with a
period end near the filing date) and the draw applies a >= $1bn gate (Amendment
v1.3.0); residual deal-value/type verification still happens at dossier-build.

Reproducibility (PAQS 37a-e): deterministic given the committed pilot_frame_raw.csv;
draw seed 20260729 (Python random.Random / MT19937). Standard library only.

Run (from repo root):
    # phase 1 (network; writes the committed frame snapshot, blind to outcome):
    uv run python research/cascade-gap-largen/draw_pilot_sample.py --enumerate
    # phase 2 (deterministic; writes pilot_selection.csv):
    uv run python research/cascade-gap-largen/draw_pilot_sample.py --draw
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRAME_CSV = HERE / "pilot_frame_raw.csv"
SELECTION_CSV = HERE / "pilot_selection.csv"

DRAW_SEED = 20260729
UA = "Spectral Branding Research dmitry@spectralbranding.com"

ERA_START = "2006-01-01"
ERA_END = "2018-12-31"

N_CARVEOUT = 3
N_ROLLUP = 2
N_CONTROL = 5
PER_STRATUM_ENUM = 200  # top hits pulled per stratum query before dedup

# Fixed, committed per-stratum queries (form type is the structural classifier).
STRATUM_QUERIES = {
    "carve_out": {"forms": "10-12B", "q": ""},
    "roll_up": {"forms": "S-1,S-4", "q": '"roll-up"'},
    "control": {"forms": "DEFM14A", "q": ""},
}

# Outcome-blind structural inclusion filters (PILOT_PREREGISTRATION.md §2, Amendment
# v1.3.0 — added after the v1.2.0 draw showed pure form-type classification is too
# crude). Applied at DRAW time on the committed frame snapshot (the snapshot keeps the
# full unfiltered enumeration for transparency). All signals are closing-era / blind to
# the 3-5-year outcome.
EXCLUDE_SIC = {"6770"}  # "Blank Checks" = SPAC/blank-check; not a going-concern deal
SIZE_MIN_USD = 1_000_000_000.0  # >= $1bn size band (Assets|Revenues proxy, blind)
# us-gaap size concepts tried in order for the >= $1bn proxy (nearest fact <= filing).
SIZE_CONCEPTS = ["Assets", "Revenues", "StockholdersEquity"]

FRAME_HEADER = [
    "stratum",
    "cik",
    "company",
    "form",
    "filing_date",
    "accession",
    "sic",
    "sic_desc",
    "size_usd",
    "size_metric",
]


# ---------------------------------------------------------------------------
# EDGAR access (stdlib urllib; polite 0.2s spacing under the 10 req/s limit)
# ---------------------------------------------------------------------------
def _get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310 (trusted host)
        data = json.loads(resp.read().decode("utf-8"))
    time.sleep(0.2)
    return data


def fts_search(forms: str, q: str, start: str, end: str, want: int) -> list[dict]:
    """EDGAR full-text search; returns up to `want` hits (paged by 'from')."""
    base = "https://efts.sec.gov/LATEST/search-index"
    hits: list[dict] = []
    frm = 0
    while len(hits) < want:
        params = {"forms": forms, "startdt": start, "enddt": end, "from": frm}
        if q:
            params["q"] = q
        url = base + "?" + urllib.parse.urlencode(params)
        data = _get_json(url)
        page = data.get("hits", {}).get("hits", [])
        if not page:
            break
        hits.extend(page)
        frm += len(page)
        if frm >= data.get("hits", {}).get("total", {}).get("value", 0):
            break
    return hits[:want]


def sic_for_cik(cik: str) -> tuple[str, str]:
    padded = str(cik).lstrip("0").zfill(10)
    try:
        data = _get_json(f"https://data.sec.gov/submissions/CIK{padded}.json")
        return str(data.get("sic", "") or ""), str(data.get("sicDescription", "") or "")
    except Exception:  # noqa: BLE001
        return "", ""


def size_for_cik(cik: str, filing_date: str) -> tuple[float, str]:
    """A >= $1bn size PROXY blind to outcome: the largest us-gaap size concept
    (Assets, then Revenues, then equity) reported with a period end on/around the
    filing date. Returns (usd, metric) or (0.0, '') if none found."""
    padded = str(cik).lstrip("0").zfill(10)
    year = filing_date[:4] if filing_date else "9999"
    for concept in SIZE_CONCEPTS:
        url = (
            f"https://data.sec.gov/api/xbrl/companyconcept/"
            f"CIK{padded}/us-gaap/{concept}.json"
        )
        try:
            data = _get_json(url)
        except Exception:  # noqa: BLE001
            continue
        facts = data.get("units", {}).get("USD", []) or []
        # Prefer a fact whose period end is within +/- 2 years of the filing year.
        best_val, best_gap = 0.0, 10**9
        for f in facts:
            end = str(f.get("end", ""))[:4]
            try:
                gap = abs(int(end) - int(year))
            except ValueError:
                continue
            val = f.get("val")
            if isinstance(val, (int, float)) and gap <= 2 and gap < best_gap:
                best_val, best_gap = float(val), gap
        if best_val > 0:
            return best_val, concept
    return 0.0, ""


def enumerate_frame() -> int:
    rows: list[dict] = []
    for stratum, spec in STRATUM_QUERIES.items():
        print(f"[enumerate] {stratum}: forms={spec['forms']} q={spec['q']!r}")
        hits = fts_search(
            spec["forms"], spec["q"], ERA_START, ERA_END, PER_STRATUM_ENUM
        )
        seen_cik: set[str] = set()
        for h in hits:
            src = h.get("_source", {})
            ciks = src.get("ciks") or []
            if not ciks:
                continue
            cik = str(ciks[0]).lstrip("0")
            if cik in seen_cik:
                continue  # dedup to the registrant (one row per CIK per stratum)
            seen_cik.add(cik)
            names = src.get("display_names") or [""]
            accession = str(h.get("_id", "")).split(":")[0]
            rows.append(
                {
                    "stratum": stratum,
                    "cik": cik,
                    "company": names[0],
                    "form": (
                        src.get("root_forms", [spec["forms"]])[0]
                        if isinstance(src.get("root_forms"), list)
                        else spec["forms"]
                    ),
                    "filing_date": src.get("file_date", ""),
                    "accession": accession,
                    "sic": "",
                    "sic_desc": "",
                    "size_usd": "",
                    "size_metric": "",
                }
            )
        print(f"           -> {len(seen_cik)} unique registrants")
    print(f"[enumerate] attaching SIC + size proxy for {len(rows)} registrants ...")
    for r in rows:
        r["sic"], r["sic_desc"] = sic_for_cik(r["cik"])
        size, metric = size_for_cik(r["cik"], r["filing_date"])
        r["size_usd"] = f"{size:.0f}" if size else ""
        r["size_metric"] = metric
    with FRAME_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FRAME_HEADER)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"[enumerate] wrote {len(rows)} rows -> {FRAME_CSV.name} (blind to outcome)")
    return 0


# ---------------------------------------------------------------------------
# Deterministic seeded stratified draw on the committed snapshot
# ---------------------------------------------------------------------------
def passes_inclusion(row: dict) -> bool:
    """Outcome-blind structural inclusion (Amendment v1.3.0): drop blank-check/SPAC
    registrants and anything below the >= $1bn size band. Blind to the outcome."""
    if (row.get("sic") or "") in EXCLUDE_SIC:
        return False
    try:
        size = float(row.get("size_usd") or 0)
    except ValueError:
        size = 0.0
    return size >= SIZE_MIN_USD


def load_frame(apply_filter: bool = True) -> dict[str, list[dict]]:
    by_stratum: dict[str, list[dict]] = {}
    dropped = {"sic": 0, "size": 0}
    with FRAME_CSV.open(newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if apply_filter and not passes_inclusion(r):
                if (r.get("sic") or "") in EXCLUDE_SIC:
                    dropped["sic"] += 1
                else:
                    dropped["size"] += 1
                continue
            by_stratum.setdefault(r["stratum"], []).append(r)
    # stable order for reproducibility (accession is unique + monotone-ish)
    for s in by_stratum:
        by_stratum[s].sort(key=lambda r: (r["filing_date"], r["accession"]))
    if apply_filter:
        print(
            f"[draw] inclusion filter dropped {dropped['sic']} blank-check + "
            f"{dropped['size']} sub-$1bn/unknown-size registrants"
        )
        print(
            "[draw] qualifying pool per stratum: "
            + ", ".join(f"{s}={len(rows)}" for s, rows in sorted(by_stratum.items()))
        )
    return by_stratum


def _sic2(row: dict) -> str:
    return (row.get("sic") or "")[:2]


def _era(row: dict) -> int:
    d = row.get("filing_date") or "0000"
    try:
        return int(d[:4])
    except ValueError:
        return 0


def match_control(case: dict, controls: list[dict], used: set[str], rng) -> dict | None:
    """Nearest control by 2-digit SIC then era; seeded tie-break; not-yet-used."""
    pool = [c for c in controls if c["cik"] not in used]
    if not pool:
        return None
    case_sic2, case_era = _sic2(case), _era(case)

    def score(c: dict) -> tuple[int, int]:
        sic_match = 0 if _sic2(c) and _sic2(c) == case_sic2 else 1
        return (sic_match, abs(_era(c) - case_era))

    best = min(score(c) for c in pool)
    tied = [c for c in pool if score(c) == best]
    return rng.choice(sorted(tied, key=lambda c: c["accession"]))


def draw() -> int:
    if not FRAME_CSV.exists():
        print(f"No frame snapshot at {FRAME_CSV.name}; run --enumerate first.")
        return 2
    frame = load_frame()
    rng = random.Random(DRAW_SEED)

    def pick(stratum: str, n: int) -> list[dict]:
        pool = list(frame.get(stratum, []))
        rng.shuffle(pool)
        return pool[:n]

    carveouts = pick("carve_out", N_CARVEOUT)
    rollups = pick("roll_up", N_ROLLUP)
    gap_cases = carveouts + rollups

    controls_pool = list(frame.get("control", []))
    used: set[str] = set()
    matched: list[tuple[dict, dict]] = []
    for case in gap_cases:
        ctl = match_control(case, controls_pool, used, rng)
        if ctl is None:
            print(f"[warn] no control available to match {case['company']}")
            continue
        used.add(ctl["cik"])
        matched.append((case, ctl))

    # Slot assignment (deterministic + transparent): 1-3 carve-outs, 4-5 roll-ups,
    # 6-10 the matched controls in the same order as their gap-prone case.
    selection: list[dict] = []
    slot = 1
    for case in gap_cases:
        stratum = case["stratum"]
        selection.append(
            {
                "slot": slot,
                "case_id": f"P{slot:02d}",
                "deal": case["company"],
                "stratum": stratum,
                "role": "gap_prone",
                "matched_to": "",
                "cik": case["cik"],
                "form": case["form"],
                "filing_date": case["filing_date"],
                "accession": case["accession"],
                "sic": case["sic"],
                "sic_desc": case["sic_desc"],
                "size_usd": case.get("size_usd", ""),
                "size_metric": case.get("size_metric", ""),
            }
        )
        slot += 1
    for case, ctl in matched:
        case_slot = next(s["slot"] for s in selection if s["cik"] == case["cik"])
        selection.append(
            {
                "slot": slot,
                "case_id": f"P{slot:02d}",
                "deal": ctl["company"],
                "stratum": "control",
                "role": "control",
                "matched_to": f"P{case_slot:02d}",
                "cik": ctl["cik"],
                "form": ctl["form"],
                "filing_date": ctl["filing_date"],
                "accession": ctl["accession"],
                "sic": ctl["sic"],
                "sic_desc": ctl["sic_desc"],
                "size_usd": ctl.get("size_usd", ""),
                "size_metric": ctl.get("size_metric", ""),
            }
        )
        slot += 1

    header = [
        "slot",
        "case_id",
        "deal",
        "stratum",
        "role",
        "matched_to",
        "cik",
        "form",
        "filing_date",
        "accession",
        "sic",
        "sic_desc",
        "size_usd",
        "size_metric",
    ]
    with SELECTION_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=header)
        w.writeheader()
        for r in selection:
            w.writerow(r)

    print(
        f"Seeded draw (seed {DRAW_SEED}); wrote {len(selection)} rows -> "
        f"{SELECTION_CSV.name} (NO outcome field)"
    )
    for r in selection:
        print(
            f"  {r['case_id']} [{r['stratum']}/{r['role']}"
            + (f"->{r['matched_to']}" if r["matched_to"] else "")
            + f"]  {r['deal']}  SIC {r['sic']}  "
            + (f"${float(r['size_usd'])/1e9:.1f}bn " if r.get("size_usd") else "")
            + f"{r['filing_date']}  {r['accession']}"
        )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--enumerate", action="store_true", help="query EDGAR -> frame CSV")
    g.add_argument("--draw", action="store_true", help="deterministic seeded draw")
    args = ap.parse_args()
    if args.enumerate:
        return enumerate_frame()
    return draw()


if __name__ == "__main__":
    raise SystemExit(main())
