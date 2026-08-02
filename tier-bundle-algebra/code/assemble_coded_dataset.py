#!/usr/bin/env python3
"""Assemble the coded datasets from the triple-coder output + adjudication log.

Consumes:
  - coding_raw/<case_id>_codes.json     (per triple_code_dossiers.py: per-model
                                          codes, majority vote, per-cell flags)
  - ADJUDICATION.csv                     (author resolution of FLAGGED cells and of
                                          any H6-relevant cell whose majority is
                                          "uncertain"; columns: case_id,cell,value,
                                          rationale). Optional; missing -> no overrides.

Produces:
  - coded_dataset_n30.csv        H6-ELIGIBLE cases only, binary schema the analysis
                                 pipeline (analyze_study_n30.py) expects:
                                 case_id,case,gap_45,p4_pathway,gap_56,p5_pathway,
                                 gap_any,p45_any,gap_mitigated
  - coded_dataset_n30_full.csv   ALL coded cases incl. H6-excluded, with per-coder
                                 codes, majority, D (performance) and E (collapse),
                                 flags, and eligibility.

H6 exclusions (PREREGISTRATION_V1.md sec.2): intra-business pivot (A08 Netflix),
redomiciliation (A09 Medtronic-Covidien), sole-proprietor/founder wind-down
(A10 elBulli). All extension (E*) cases are going-concern acquisitions and are
H6-eligible.

Deterministic; no network, no RNG. Run:
    uv run python code/assemble_coded_dataset.py
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW_DIR = HERE / "coding_raw"
ADJUDICATION = HERE / "ADJUDICATION.csv"

# H6-excluded case_ids (pre-registration sec.2). By case-class, not by outcome.
H6_EXCLUDED = {
    "A08": "intra-business pivot (no ownership-boundary crossing)",
    "A09": "redomiciliation (pure Tier-3 swap; cascade vacuous)",
    "A10": "sole-proprietor/founder wind-down (admissibility fires before cascade)",
}

H6_CELLS = ["gap_45", "gap_56", "p4_pathway", "p5_pathway"]
PER_CODER_CELLS = [
    "sigma_T1",
    "sigma_T2",
    "sigma_T3",
    "sigma_T4",
    "sigma_T5",
    "sigma_T6",
    "collapse_state",
    "gap_45",
    "gap_56",
    "p4_pathway",
    "p5_pathway",
    "t1_archetype",
    "t2_model",
    "gap_mitigated",
]


def load_adjudication() -> dict[tuple[str, str], str]:
    overrides: dict[tuple[str, str], str] = {}
    if not ADJUDICATION.exists():
        return overrides
    with ADJUDICATION.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            overrides[(row["case_id"].strip(), row["cell"].strip())] = row[
                "value"
            ].strip()
    return overrides


def resolved(rec: dict, cell: str, overrides: dict[tuple[str, str], str]) -> str:
    """Adjudicated value if present, else the majority value."""
    key = (rec["case_id"], cell)
    if key in overrides:
        return overrides[key]
    return rec["majority"].get(cell, "uncertain")


def main() -> int:
    records = []
    for p in sorted(RAW_DIR.glob("*_codes.json")):
        records.append(json.loads(p.read_text(encoding="utf-8")))
    if not records:
        print(
            "No coded cases in coding_raw/. Run triple_code_dossiers.py first.",
            file=sys.stderr,
        )
        return 2
    overrides = load_adjudication()

    # ---- full record (all cases) ----
    full_path = HERE / "coded_dataset_n30_full.csv"
    full_fields = ["case_id", "case", "h6_eligible", "h6_exclusion_reason", "n_flags"]
    for cell in PER_CODER_CELLS:
        full_fields.append(f"maj_{cell}")
    for coder in ("claude", "gemini", "grok"):
        for cell in PER_CODER_CELLS:
            full_fields.append(f"{coder}_{cell}")
    full_fields += ["performance_metric_majority_note", "flagged_cells"]

    with full_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=full_fields)
        w.writeheader()
        for rec in records:
            cid = rec["case_id"]
            row = {
                "case_id": cid,
                "case": rec["case"],
                "h6_eligible": "no" if cid in H6_EXCLUDED else "yes",
                "h6_exclusion_reason": H6_EXCLUDED.get(cid, ""),
                "n_flags": rec.get("n_flags", 0),
                "flagged_cells": ";".join(
                    c for c, f in rec.get("flags", {}).items() if f
                ),
            }
            for cell in PER_CODER_CELLS:
                row[f"maj_{cell}"] = resolved(rec, cell, overrides)
            for coder in ("claude", "gemini", "grok"):
                pm = rec["per_model"].get(coder)
                for cell in PER_CODER_CELLS:
                    row[f"{coder}_{cell}"] = pm.get(cell) if pm else "MISSING"
            # Performance metric: report each coder's phrase (no vote on free text).
            perf = {
                coder: (rec["per_model"].get(coder) or {}).get("performance_metric", "")
                for coder in ("claude", "gemini", "grok")
            }
            row["performance_metric_majority_note"] = " | ".join(
                f"{k}:{v}" for k, v in perf.items() if v
            )
            w.writerow(row)
    print(f"wrote {full_path.name} ({len(records)} cases)")

    # ---- H6-eligible binary dataset ----
    h6_path = HERE / "coded_dataset_n30.csv"
    unresolved = []
    eligible_rows = []
    for rec in records:
        cid = rec["case_id"]
        if cid in H6_EXCLUDED:
            continue
        vals = {cell: resolved(rec, cell, overrides) for cell in H6_CELLS}
        gm = resolved(rec, "gap_mitigated", overrides)
        # Every H6 cell must be binary (0/1) for the eligible set.
        bad = [c for c in H6_CELLS if vals[c] not in ("0", "1")]
        if bad:
            unresolved.append((cid, bad, {c: vals[c] for c in bad}))
            continue
        gap_any = "1" if (vals["gap_45"] == "1" or vals["gap_56"] == "1") else "0"
        p45_any = (
            "1" if (vals["p4_pathway"] == "1" or vals["p5_pathway"] == "1") else "0"
        )
        eligible_rows.append(
            {
                "case_id": cid,
                "case": rec["case"],
                "gap_45": vals["gap_45"],
                "p4_pathway": vals["p4_pathway"],
                "gap_56": vals["gap_56"],
                "p5_pathway": vals["p5_pathway"],
                "gap_any": gap_any,
                "p45_any": p45_any,
                "gap_mitigated": gm if gm in ("yes", "no", "NA") else "NA",
            }
        )

    if unresolved:
        print(
            "\nUNRESOLVED H6 cells (need adjudication in ADJUDICATION.csv):",
            file=sys.stderr,
        )
        for cid, bad, vals in unresolved:
            print(f"  {cid}: {vals}", file=sys.stderr)
        print(
            "\nAdd rows (case_id,cell,value,rationale) to ADJUDICATION.csv resolving "
            "each to 0/1, then re-run.",
            file=sys.stderr,
        )

    fields = [
        "case_id",
        "case",
        "gap_45",
        "p4_pathway",
        "gap_56",
        "p5_pathway",
        "gap_any",
        "p45_any",
        "gap_mitigated",
    ]
    with h6_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for row in eligible_rows:
            w.writerow(row)
    print(f"wrote {h6_path.name} ({len(eligible_rows)} H6-eligible cases)")
    if unresolved:
        print(
            f"WARNING: {len(unresolved)} case(s) excluded from H6 dataset pending adjudication."
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
