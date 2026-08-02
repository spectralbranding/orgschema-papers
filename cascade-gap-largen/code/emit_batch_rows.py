#!/usr/bin/env python3
"""Emit the per-case CASE BLOCK(s) to paste into the generic dossier-build subagent
prompt (SUBAGENT_PROMPT_TEMPLATE.md) during the step-4 scale-up. Read-only.

Given case ids (or a count of the next-missing), prints one blinded CASE BLOCK per case
with exactly the fields a subagent needs: case id, entity + CIK, stratum (so it applies
the right §3 8-K guidance), drawn form + accession + filing date, and the closing year
(for the outcome-window + contemporaneous-primary search). It does NOT print role for
gap_prone vs control beyond what the subagent needs to source (controls need the §4
no-record rule), and never prints hypotheses/constructs.

Usage (from repo root):
  uv run python research/cascade-gap-largen/emit_batch_rows.py P002 P003 P046
  uv run python research/cascade-gap-largen/emit_batch_rows.py --next 8   # next 8 missing
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SELECTION = HERE / "full_draw_selection.csv"
DOSSIERS = HERE / "full_draw_dossiers"


def load() -> dict[str, dict]:
    with open(SELECTION, newline="", encoding="utf-8") as fh:
        return {r["case_id"]: r for r in csv.DictReader(fh)}


def case_done(cid: str) -> bool:
    s = DOSSIERS / f"{cid}_struct.md"
    o = DOSSIERS / f"{cid}_outcome.md"
    return (
        s.exists()
        and o.exists()
        and s.stat().st_size >= 400
        and o.stat().st_size >= 400
    )


def block(r: dict) -> str:
    year = (r["filing_date"] or "")[:4]
    # Entity name: strip trailing ticker/CIK parenthetical noise, keep it readable.
    entity = r["deal"].split("  (")[0].strip() or r["deal"].strip()
    is_control = r["role"] == "control"
    role_note = (
        "This case is a matched whole-company / going-concern acquisition. If the target "
        "is absorbed and deregisters with no separate public 3-5-yr record, apply brief §4 "
        "(outcome UNCERTAIN unless the acquirer separately discloses the business)."
        if is_control
        else (
            "The drawn filing's stratum is an 8-K-drawn structural type; apply brief §3 "
            "if the drawn accession is not itself the deal-terms document."
            if r["form"].upper().startswith("8-K")
            else "The drawn filing is a closing-era deal document; source structure from it."
        )
    )
    return (
        f"CASE {r['case_id']}:\n"
        f"- Entity: {entity} (CIK {r['cik']}); SIC {r['sic']} ({r['sic_desc']}).\n"
        f"- Deal-structure stratum: {r['stratum']}.\n"
        f"- STRUCT drawn source: Form {r['form']}, accession {r['accession']}, "
        f"filed {r['filing_date']} (closing year ~{year}).\n"
        f"- Outcome window: fixed 3-5 years after ~{year}.\n"
        f"- {role_note}\n"
        f"- Replace <CASE_ID>={r['case_id']} and <CIK>={r['cik']} in the sourcing/output "
        f"paths below."
    )


def main(argv: list[str]) -> int:
    rows = load()
    if "--next" in argv:
        n = int(argv[argv.index("--next") + 1])
        ids = [cid for cid in rows if not case_done(cid)][:n]
    else:
        ids = [a for a in argv if a.startswith("P")]
    for cid in ids:
        if cid not in rows:
            print(f"# {cid} NOT IN SELECTION", file=sys.stderr)
            continue
        print(block(rows[cid]))
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
