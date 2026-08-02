#!/usr/bin/env python3
"""Completion tracker for the N=350 full-draw sub-dossier build (step 4).

Scans ``full_draw_dossiers/`` for each case's two sub-dossiers and reports, per
stratum, how many cases are DONE (both P###_struct.md + P###_outcome.md present and
non-trivial) vs MISSING. Also lists the next MISSING case ids so a session can pick up
the next batch mechanically. Read-only.

Usage (from repo root):
  uv run python research/cascade-gap-largen/dossier_status.py            # summary
  uv run python research/cascade-gap-largen/dossier_status.py --missing  # list missing ids
  uv run python research/cascade-gap-largen/dossier_status.py --next 20  # next 20 missing ids
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SELECTION = HERE / "full_draw_selection.csv"
DOSSIERS = HERE / "full_draw_dossiers"
MIN_CHARS = 400  # a real dossier is well above this; guards against empty stubs


def load() -> list[dict]:
    with open(SELECTION, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def case_done(cid: str) -> bool:
    s = DOSSIERS / f"{cid}_struct.md"
    o = DOSSIERS / f"{cid}_outcome.md"
    return (
        s.exists()
        and o.exists()
        and s.stat().st_size >= MIN_CHARS
        and o.stat().st_size >= MIN_CHARS
    )


def main(argv: list[str]) -> int:
    rows = load()
    done = {r["case_id"]: case_done(r["case_id"]) for r in rows}
    missing = [r["case_id"] for r in rows if not done[r["case_id"]]]
    if "--missing" in argv:
        print("\n".join(missing))
        return 0
    if "--next" in argv:
        n = int(argv[argv.index("--next") + 1])
        print(" ".join(missing[:n]))
        return 0
    by_stratum_total = Counter(r["stratum"] for r in rows)
    by_stratum_done = Counter(r["stratum"] for r in rows if done[r["case_id"]])
    print(f"cases: {len(rows)}  DONE: {sum(done.values())}  MISSING: {len(missing)}")
    for strat in sorted(by_stratum_total):
        print(f"  {strat:14} {by_stratum_done[strat]:>3}/{by_stratum_total[strat]:>3}")
    if missing:
        print(
            f"next missing: {' '.join(missing[:15])}{' ...' if len(missing) > 15 else ''}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
