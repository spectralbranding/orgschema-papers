#!/usr/bin/env python3
"""Wave QC for the step-4 dossier grind (PROGRAM_PLAN S5).

Runs the three NEXT_SESSION QC checks over a set of case ids and prints ONE terse
line per case (PASS / FAIL: <reasons>), so a grinding session spends minimal context
per wave. Read-only.

Checks per case P###:
  1. existence   -- both P###_struct.md and P###_outcome.md exist and are non-trivial.
  2. tag cover   -- in each file, bullet lines ('- ') <= source tags ('[SRC:'/'[UNVERIFIED').
  3. blinding    -- no study-meta / construct / stratum labels in either file.
  4. porosity    -- no acquirer realized-outcome scalar leaks into the _struct file
                    (seller/target bankruptcy in a 363-deal struct is allowed context).

Usage (from repo root):
  uv run python research/cascade-gap-largen/qc_wave.py P014 P015 ...
  uv run python research/cascade-gap-largen/qc_wave.py --all      # every built case
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOSSIERS = HERE / "full_draw_dossiers"

BULLET = re.compile(r"^\s*-\s")
TAG = re.compile(r"\[SRC:|\[UNVERIFIED")
BLINDING = re.compile(
    r"\b(gap_45|gap_56|p4_pathway|p5_pathway|t1_archetype|t2_model|gap_prone|"
    r"gap-prone|hypothes|stratum|case-control|safe harbor|necessary condition|"
    r"cascade gap|re-collapse)\b",
    re.IGNORECASE,
)
# Acquirer realized-outcome scalars that must live only in the _outcome file. Seller/
# target bankruptcy in a 363-deal struct is a closing-time structural feature (allowed),
# so plain "bankrupt"/"chapter 11" is intentionally NOT flagged here.
POROSITY = re.compile(
    r"net (loss|income) of|goodwill impair|impairment (of|charge|loss)|delist|"
    r"going concern doubt|write-down|writedown|years after (clos|the deal)",
    re.IGNORECASE,
)


def check_file(path: Path) -> list[str]:
    problems: list[str] = []
    if not path.exists():
        return [f"{path.name} MISSING"]
    text = path.read_text()
    lines = text.splitlines()
    if len(lines) < 10:
        problems.append(f"{path.name} too short ({len(lines)} lines)")
    bullets = sum(1 for line in lines if BULLET.match(line))
    tags = len(TAG.findall(text))
    if bullets > tags:
        problems.append(f"{path.name} tags<bullets ({bullets}>{tags})")
    blind = [str(i + 1) for i, line in enumerate(lines) if BLINDING.search(line)]
    if blind:
        problems.append(f"{path.name} blinding@{','.join(blind)}")
    return problems


def check_case(case_id: str) -> tuple[bool, str]:
    struct = DOSSIERS / f"{case_id}_struct.md"
    outcome = DOSSIERS / f"{case_id}_outcome.md"
    problems = check_file(struct) + check_file(outcome)
    if struct.exists():
        por = [
            str(i + 1)
            for i, line in enumerate(struct.read_text().splitlines())
            if POROSITY.search(line)
        ]
        if por:
            problems.append(f"{struct.name} porosity@{','.join(por)}")
    if problems:
        return False, "FAIL: " + "; ".join(problems)
    return True, "PASS"


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args == ["--all"]:
        ids = sorted({p.name[:4] for p in DOSSIERS.glob("P[0-9][0-9][0-9]_struct.md")})
    else:
        ids = args
    n_pass = 0
    for cid in ids:
        ok, msg = check_case(cid)
        n_pass += ok
        print(f"{cid} {msg}")
    print(f"--- {n_pass}/{len(ids)} PASS ---")
    return 0 if n_pass == len(ids) else 1


if __name__ == "__main__":
    raise SystemExit(main())
