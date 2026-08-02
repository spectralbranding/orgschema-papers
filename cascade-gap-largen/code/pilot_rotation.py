#!/usr/bin/env python3
"""Pre-registered per-construct coder-rotation assignment for the cascade-gap pilot.

Registered-before-data artifact (PILOT_PREREGISTRATION.md §4, v1.2.0). Generates the
seeded disjoint-pair rotation that fixes, for each of the 10 pilot case-slots, which
disjoint pair of models codes the STRUCTURAL construct (the gap) and which codes the
OUTCOME construct (the pathway) -- so that no model codes both constructs for the same
case, while every model codes both constructs across different cases (balanced).

Coder pool (4 models, pinned):
    claude  -> claude-opus-4-8
    gemini  -> gemini-3.1-pro-preview
    grok    -> grok-4.3
    openai  -> gpt-5.4-2026-03-05   (the 4th coder, added for genuine rotation)

The assignment is a function of the fixed SEED only (independent of which real deal
fills which slot) -- so it is a genuine pre-registration: committed BEFORE the EDGAR
draw and BEFORE any coding call. Deterministic; re-running reproduces the same file.

Run:
    uv run python research/cascade-gap-largen/pilot_rotation.py --write
    uv run python research/cascade-gap-largen/pilot_rotation.py --verify
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "pilot_rotation.json"

SEED = 20260729  # fixed pre-registration seed
N_SLOTS = 10

# operator name -> pinned model id (recorded in the assignment for provenance)
MODELS: dict[str, str] = {
    "claude": "claude-opus-4-8",
    "gemini": "gemini-3.1-pro-preview",
    "grok": "grok-4.3",
    "openai": "gpt-5.4-2026-03-05",
}
CODERS = tuple(MODELS)  # ("claude", "gemini", "grok", "openai")


def disjoint_partitions() -> list[tuple[tuple[str, str], tuple[str, str]]]:
    """The 3 ways to split 4 coders into two disjoint unordered pairs."""
    a = CODERS[0]
    parts = []
    for combo in itertools.combinations(CODERS[1:], 1):
        partner = combo[0]
        pair1 = (a, partner)
        pair2 = tuple(m for m in CODERS if m not in pair1)
        parts.append((pair1, pair2))  # type: ignore[arg-type]
    return parts  # 3 partitions


def build_rotation() -> list[dict]:
    """Seeded, balanced disjoint-pair rotation over N_SLOTS case-slots.

    Each slot fixes a disjoint partition + an orientation (which pair codes the
    structural construct). Balance-by-construction for N_SLOTS=10:
      - the 6 base configs = all 3 partitions x both orientations. Over these, every
        model is structural 3x and outcome 3x (each model is in a pair in all 3
        partitions, so both orientations balance it).
      - 4 balancing configs = 2 seed-chosen partitions x both orientations. Both
        orientations of a partition add exactly +1 structural and +1 outcome to each of
        that partition's 4 members; every model is in both chosen partitions, so each
        gets +2 structural / +2 outcome -> 5/5 overall, independent of which 2 are
        chosen. The order of all 10 slots is then seed-shuffled (order does not affect
        the per-model role balance).
    """
    rng = random.Random(SEED)
    partitions = disjoint_partitions()  # 3
    both = [
        (p1, p2)
        for (p1, p2) in (
            [(a, b) for (a, b) in partitions] + [(b, a) for (a, b) in partitions]
        )
    ]  # 6 base configs
    extra_partitions = rng.sample(partitions, 2)
    extra = [
        (p1, p2) for (a, b) in extra_partitions for (p1, p2) in ((a, b), (b, a))
    ]  # 4 balancing configs
    configs = both + extra  # 10
    rng.shuffle(configs)
    rotation: list[dict] = []
    for slot, (struct_pair, outcome_pair) in enumerate(configs, start=1):
        rotation.append(
            {
                "slot": slot,
                "structural_pair": sorted(struct_pair),
                "outcome_pair": sorted(outcome_pair),
            }
        )
    return rotation


def role_counts(rotation: list[dict]) -> dict[str, dict[str, int]]:
    counts = {m: {"structural": 0, "outcome": 0} for m in CODERS}
    for r in rotation:
        for m in r["structural_pair"]:
            counts[m]["structural"] += 1
        for m in r["outcome_pair"]:
            counts[m]["outcome"] += 1
    return counts


def verify(rotation: list[dict]) -> list[str]:
    """Return a list of problems (empty = OK)."""
    problems: list[str] = []
    for r in rotation:
        sp = set(r["structural_pair"])
        op = set(r["outcome_pair"])
        if len(sp) != 2 or len(op) != 2:
            problems.append(f"slot {r['slot']}: a pair is not size 2")
        if sp & op:
            problems.append(f"slot {r['slot']}: pairs not disjoint ({sp & op})")
        if sp | op != set(CODERS):
            problems.append(f"slot {r['slot']}: pairs do not cover all 4 coders")
    # Balance: no model's structural (or outcome) count deviates from the mean by > 1.
    counts = role_counts(rotation)
    for role in ("structural", "outcome"):
        vals = [counts[m][role] for m in CODERS]
        if max(vals) - min(vals) > 1:
            problems.append(f"{role} role imbalance across coders: {counts}")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument(
        "--write", action="store_true", help="generate + write pilot_rotation.json"
    )
    g.add_argument(
        "--verify", action="store_true", help="regenerate + verify (no write)"
    )
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()

    rotation = build_rotation()
    problems = verify(rotation)
    counts = role_counts(rotation)

    print(f"seed={SEED}  slots={N_SLOTS}  coders={list(CODERS)}")
    for r in rotation:
        print(
            f"  slot {r['slot']:>2}: gap<-{r['structural_pair']}  "
            f"pathway<-{r['outcome_pair']}"
        )
    print("role balance (structural/outcome):")
    for m in CODERS:
        print(f"  {m:<7} {counts[m]['structural']}/{counts[m]['outcome']}")

    if problems:
        print("VERIFY FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print(
        "VERIFY OK: every slot has disjoint pairs covering all 4 coders; roles balanced."
    )

    if args.write:
        payload = {
            "seed": SEED,
            "n_slots": N_SLOTS,
            "models": MODELS,
            "design": "disjoint-pair per-construct rotation (PILOT_PREREGISTRATION.md §4 v1.2.0)",
            "rotation": rotation,
            "role_counts": counts,
        }
        Path(args.out).write_text(json.dumps(payload, indent=2) + "\n")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
