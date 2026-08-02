#!/usr/bin/env python3
"""S5 pilot descriptive analysis + go/no-go read (PILOT_PREREGISTRATION.md §5-6).

The pilot is FEASIBILITY / PIPELINE-VALIDATION, NOT confirmatory (§0). This script
reports, from the assembled pilot outputs:

  - per-construct pooled 2-rater Fleiss' kappa (structural / outcome), read from the
    kappa_*.json the coding runner wrote (pilot_code.py), with the per-construct flag
    rate alongside (a coarse 2-rater signal at N=10 -- §6);
  - a POROSITY spot-check: an automated retrospective/outcome-phrase scan over each
    structural sub-dossier, confirming the separated-from-the-start structural slice
    carries no post-deal/outcome language (the residual leak S4's slicer could not
    fully strip, PREREGISTRATION_V2.md §1.4);
  - feasibility: how many of the 10 deals were fully built + coded end-to-end;
  - the DESCRIPTIVE necessary-condition 2x2 (gap_any x p45_any) with per-cell counts,
    reported as description only -- NO confirmatory CI / p-value (the pilot is not
    powered; the confirmatory NC test is the full S5 draw).

It then prints the pre-registered go/no-go criteria (§6) with a PASS / COARSE / FAIL
read for each. A failing criterion is a useful result (it says what to fix); the
full-draw decision is the user's.

Modes:
  --fixture : synthetic self-check of the kappa, 2x2, and porosity-scan helpers (the
              only mode that runs until the pilot dataset + kappa files exist).
  (default) : run on pilot_dataset.csv + pilot_code_out/kappa_*.json + pilot_dossiers/.

Run:
    uv run python research/cascade-gap-largen/analyze_pilot.py --fixture
    uv run python research/cascade-gap-largen/analyze_pilot.py
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from pilot_code import pooled_fleiss  # noqa: E402

DATASET = HERE / "pilot_dataset.csv"
KAPPA_STRUCT = HERE / "pilot_code_out" / "kappa_struct.json"
KAPPA_OUTCOME = HERE / "pilot_code_out" / "kappa_outcome.json"
DOSSIER_DIR = HERE / "pilot_dossiers"

N_PILOT = 10
KAPPA_STRUCT_MIN = 0.60
KAPPA_OUTCOME_MIN = 0.70
POROSITY_CLEAN_MIN = 9  # >= 9/10 structural slices clean

# Retrospective / realized-outcome phrasing that must NOT appear in a closing-time
# STRUCTURAL sub-dossier. Substring match, case-insensitive. Kept conservative:
# these are outcome/hindsight markers, not neutral structural vocabulary.
POROSITY_PHRASES = [
    "years later",
    "in hindsight",
    "ultimately failed",
    "ultimately divested",
    "eventually divested",
    "eventually sold",
    "would later",
    "later divested",
    "later sold",
    "later wrote",
    "wrote down",
    "write-down",
    "writedown",
    "goodwill impairment",
    "impairment charge",
    "restructuring charge",
    "failed to integrate",
    "never integrated",
    "stayed separate",
    "remained separate",
    "integration failed",
    "post-merger performance",
    "shareholder value was destroyed",
    "destroyed value",
    "turned out to be",
    "proved to be a failure",
]


def load_rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def nc_2x2(rows: list[dict], gap_col: str, fail_col: str) -> dict:
    n11 = n10 = n01 = n00 = 0
    for r in rows:
        g, f = int(r[gap_col]), int(r[fail_col])
        if g and f:
            n11 += 1
        elif g and not f:
            n10 += 1
        elif not g and f:
            n01 += 1
        else:
            n00 += 1
    return {"n11": n11, "n10": n10, "n01": n01, "n00": n00}


def porosity_scan(dossier_dir: Path) -> dict:
    """Scan each *_struct.md for retrospective/outcome phrasing. Returns per-file hits."""
    results: dict[str, list[str]] = {}
    files = sorted(dossier_dir.glob("P*_struct.md"))
    for f in files:
        text = f.read_text(encoding="utf-8").lower()
        hits = [p for p in POROSITY_PHRASES if p in text]
        results[f.name] = hits
    n_clean = sum(1 for h in results.values() if not h)
    return {"per_file": results, "n_files": len(files), "n_clean": n_clean}


def read_kappa(path: Path) -> dict:
    if not path.exists():
        return {"kappa": None}
    return json.loads(path.read_text()).get("fleiss", {"kappa": None})


def _fmt(k) -> str:
    return f"{k:.3f}" if isinstance(k, float) else "n/a"


def run_report() -> int:
    if not DATASET.exists() or DATASET.read_text().strip().count("\n") < 1:
        print(f"No coded pilot data at {DATASET.name}.", file=sys.stderr)
        print(
            "Run draw_pilot_sample.py -> build sub-dossiers -> pilot_code.py first; "
            "or --fixture to validate this pipeline.",
            file=sys.stderr,
        )
        return 2
    rows = load_rows(DATASET)
    ks = read_kappa(KAPPA_STRUCT)
    ko = read_kappa(KAPPA_OUTCOME)
    por = porosity_scan(DOSSIER_DIR)

    print("S5 pilot descriptive analysis + go/no-go read")
    print("=" * 70)
    print(f"cases coded: {len(rows)} / {N_PILOT}")
    strat = {}
    for r in rows:
        strat[r["stratum"]] = strat.get(r["stratum"], 0) + 1
    print(f"by stratum: {strat}")
    print()

    print("Reliability (pooled 2-rater Fleiss' kappa; coarse signal at N=10):")
    s_flags = sum(1 for r in rows if r.get("struct_flags"))
    o_flags = sum(1 for r in rows if r.get("outcome_flags"))
    print(
        f"  structural kappa = {_fmt(ks.get('kappa'))} over {ks.get('n_items')} "
        f"rater-slot items; cases with a struct flag: {s_flags}/{len(rows)}"
    )
    print(
        f"  outcome    kappa = {_fmt(ko.get('kappa'))} over {ko.get('n_items')} "
        f"rater-slot items; cases with an outcome flag: {o_flags}/{len(rows)}"
    )
    print()

    print("Porosity spot-check (structural slices must carry no outcome phrasing):")
    print(f"  clean structural slices: {por['n_clean']}/{por['n_files']}")
    for name, hits in por["per_file"].items():
        if hits:
            print(f"    [LEAK] {name}: {hits}")
    print()

    print(
        "Descriptive necessary-condition 2x2 (gap_any x p45_any) -- description only:"
    )
    t = nc_2x2(rows, "gap_any", "p45_any")
    print(f"  gap & fail   (n11) = {t['n11']}")
    print(f"  gap & ok     (n10) = {t['n10']}")
    print(f"  no-gap & fail(n01) = {t['n01']}   <- necessity-breaking cell")
    print(f"  no-gap & ok  (n00) = {t['n00']}")
    print("  (no CI / p-value: the pilot is not powered; see PILOT_PREREGISTRATION §5)")
    print()

    print("Go/no-go criteria for the full N~300 draw (PILOT_PREREGISTRATION.md §6):")
    _crit(
        "reliability struct",
        ks.get("kappa"),
        KAPPA_STRUCT_MIN,
        coarse=True,
    )
    _crit("reliability outcome", ko.get("kappa"), KAPPA_OUTCOME_MIN, coarse=True)
    porosity_ok = por["n_clean"] >= POROSITY_CLEAN_MIN
    print(
        f"  porosity        : {por['n_clean']}/{por['n_files']} clean "
        f"(need >= {POROSITY_CLEAN_MIN}/{N_PILOT})  "
        f"-> {'PASS' if porosity_ok else 'FAIL'}"
    )
    feasible = len(rows) >= N_PILOT
    print(
        f"  feasibility     : {len(rows)}/{N_PILOT} deals built + coded end-to-end  "
        f"-> {'PASS' if feasible else 'PARTIAL'}"
    )
    pipeline_ok = (
        ks.get("kappa") is not None and ko.get("kappa") is not None and len(rows) > 0
    )
    print(
        f"  pipeline        : draw->dossier->rotated coding->assemble->analyze  "
        f"-> {'PASS' if pipeline_ok else 'INCOMPLETE'}"
    )
    print()
    print(
        "A failing criterion is a useful result; the full-draw decision is the user's."
    )
    return 0


def _crit(name: str, val, threshold: float, coarse: bool = False) -> None:
    if not isinstance(val, float):
        print(f"  {name:<16}: n/a")
        return
    tag = "PASS" if val >= threshold else ("COARSE-LOW" if coarse else "FAIL")
    note = " (2-rater, N=10 -> read as directional, not a veto)" if coarse else ""
    print(f"  {name:<16}: {val:.3f} (need >= {threshold:.2f}) -> {tag}{note}")


def run_fixture() -> int:
    print("S5 pilot analysis pipeline self-check (synthetic; no study data)")
    print("=" * 70)

    # (a) pooled 2-rater kappa: two items, both raters agree on "1" -> perfect
    #     agreement; expected kappa handles the degenerate all-same case.
    agree_items = [[0, 2, 0], [0, 2, 0], [2, 0, 0]]  # perfect agreement, mixed cats
    split_items = [[1, 1, 0], [1, 1, 0]]  # total disagreement on every item
    k_agree = pooled_fleiss(agree_items)["kappa"]
    k_split = pooled_fleiss(split_items)["kappa"]

    # (b) descriptive 2x2 on a synthetic dataset with a known shape [2,1,0,7].
    synth = (
        [{"gap_any": "1", "p45_any": "1"}] * 2
        + [{"gap_any": "1", "p45_any": "0"}] * 1
        + [{"gap_any": "0", "p45_any": "0"}] * 7
    )
    t = nc_2x2(synth, "gap_any", "p45_any")

    # (c) porosity scanner: a clean structural string vs a dirty one.
    clean = (
        "the merger agreement transfers the product line and the manufacturing plant"
    )
    dirty = (
        "the plant transferred; the acquirer later wrote down the goodwill impairment"
    )
    clean_hits = [p for p in POROSITY_PHRASES if p in clean.lower()]
    dirty_hits = [p for p in POROSITY_PHRASES if p in dirty.lower()]

    ok = (
        isinstance(k_agree, float)
        and k_agree > 0.99
        and isinstance(k_split, float)
        and k_split < 0.0 + 1e-9
        and (t["n11"], t["n10"], t["n01"], t["n00"]) == (2, 1, 0, 7)
        and clean_hits == []
        and len(dirty_hits) >= 2
    )
    print(f"  pooled kappa (agree) = {_fmt(k_agree)} (expect ~1.000)")
    print(f"  pooled kappa (split) = {_fmt(k_split)} (expect <= 0)")
    print(
        f"  2x2 (n11,n10,n01,n00) = {(t['n11'], t['n10'], t['n01'], t['n00'])} "
        f"(expect (2,1,0,7))"
    )
    print(
        f"  porosity clean hits = {clean_hits} (expect []); "
        f"dirty hits = {dirty_hits}"
    )
    print()
    if ok:
        print("SELF-CHECK OK: kappa + 2x2 + porosity-scan helpers agree.")
        return 0
    print("SELF-CHECK FAILED: pilot analysis logic drifted.")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fixture", action="store_true")
    args = ap.parse_args()
    if args.fixture:
        return run_fixture()
    return run_report()


if __name__ == "__main__":
    raise SystemExit(main())
