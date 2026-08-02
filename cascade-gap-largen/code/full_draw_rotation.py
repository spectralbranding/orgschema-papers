#!/usr/bin/env python3
"""Pre-registered per-construct coder-rotation for the cascade-gap FULL DRAW (N=350).

Registered-before-data artifact (FULL_DRAW_PREREGISTRATION.md §4; PREREGISTRATION_V2.md
Amendment 2.D). Generalizes the pilot's 4-coder DISJOINT-PAIR rotation (2 raters/construct)
to the full draw's **3 raters per construct**: for each case, 3 of the 4 pinned models code
the STRUCTURAL construct and 3 code the OUTCOME construct, with the two triples NOT identical
(a different model is omitted from each construct). Rotating which model is omitted from each
construct across the 350 case-slots keeps per-construct coding as separated as a 4-model pool
allows and balances every model's structural/outcome load and its coded-both/coded-one mix.

With 4 models, a 3-model triple is fixed by the ONE model it omits. So a case-slot config is
an ordered pair (struct_omit, outcome_omit) with struct_omit != outcome_omit -> 12 distinct
configs. N=350 = 12 * 29 + 2: each config appears 29 times + 2 seed-chosen extras; the slot
order is then seed-shuffled (order does not affect per-model balance).

Coder pool (4 models, pinned) -- each provider's current frontier reasoning model
(pre-DATA refresh 2026-08-01; grok/openai upgraded to newer flagships, registered
before any coding call):
    claude -> claude-opus-4-8 ; gemini -> gemini-3.1-pro-preview
    grok   -> grok-4.5        ; openai -> gpt-5.6-sol

The assignment is a function of the fixed SEED only (independent of which real deal fills
which slot) -- a genuine pre-registration, committed BEFORE the draw and BEFORE any coding
call. Deterministic; re-running reproduces the same file.

Run:
    uv run python research/cascade-gap-largen/full_draw_rotation.py --verify
    uv run python research/cascade-gap-largen/full_draw_rotation.py --write
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "full_draw_rotation.json"

SEED = (
    20260729  # fixed pre-registration seed (same family as the pilot / power analysis)
)
N_SLOTS = 350

MODELS: dict[str, str] = {
    "claude": "claude-opus-4-8",
    "gemini": "gemini-3.1-pro-preview",
    "grok": "grok-4.5",
    "openai": "gpt-5.6-sol",
}
CODERS = tuple(MODELS)  # ("claude", "gemini", "grok", "openai")


def all_configs() -> list[tuple[str, str]]:
    """The 12 ordered (struct_omit, outcome_omit) configs with struct_omit != outcome_omit."""
    return [(a, b) for a, b in itertools.product(CODERS, CODERS) if a != b]


def triple(omit: str) -> list[str]:
    """The 3-model construct triple = all coders except the omitted one."""
    return sorted(m for m in CODERS if m != omit)


def build_rotation() -> list[dict]:
    """Seeded, balanced 3-of-4 per-construct rotation over N_SLOTS case-slots."""
    rng = random.Random(SEED)
    configs = all_configs()  # 12
    base_reps, remainder = divmod(N_SLOTS, len(configs))  # 29, 2
    pool = configs * base_reps + rng.sample(configs, remainder)
    rng.shuffle(pool)
    rotation: list[dict] = []
    for slot, (struct_omit, outcome_omit) in enumerate(pool, start=1):
        rotation.append(
            {
                "slot": slot,
                "structural_triple": triple(struct_omit),
                "outcome_triple": triple(outcome_omit),
                "structural_omit": struct_omit,
                "outcome_omit": outcome_omit,
            }
        )
    return rotation


def role_counts(rotation: list[dict]) -> dict[str, dict[str, int]]:
    counts = {
        m: {"structural": 0, "outcome": 0, "omit_struct": 0, "omit_outcome": 0}
        for m in CODERS
    }
    for r in rotation:
        for m in r["structural_triple"]:
            counts[m]["structural"] += 1
        for m in r["outcome_triple"]:
            counts[m]["outcome"] += 1
        counts[r["structural_omit"]]["omit_struct"] += 1
        counts[r["outcome_omit"]]["omit_outcome"] += 1
    return counts


def verify(rotation: list[dict]) -> list[str]:
    """Return a list of problems (empty = OK)."""
    problems: list[str] = []
    if len(rotation) != N_SLOTS:
        problems.append(f"expected {N_SLOTS} slots, got {len(rotation)}")
    for r in rotation:
        st = set(r["structural_triple"])
        ot = set(r["outcome_triple"])
        if len(st) != 3 or len(ot) != 3:
            problems.append(f"slot {r['slot']}: a triple is not size 3")
        if st == ot:
            problems.append(
                f"slot {r['slot']}: structural and outcome triples identical"
            )
        if r["structural_omit"] == r["outcome_omit"]:
            problems.append(
                f"slot {r['slot']}: same model omitted from both constructs"
            )
    # Balance: each model's structural / outcome load within +/- 1 of the mean.
    counts = role_counts(rotation)
    for role in ("structural", "outcome"):
        vals = [counts[m][role] for m in CODERS]
        # each model is in 3 of the 4 triples' complement -> expect ~ 3/4 * N per role
        if max(vals) - min(vals) > 2:
            problems.append(
                f"{role} role imbalance > 2 across coders: "
                f"{{{', '.join(f'{m}:{counts[m][role]}' for m in CODERS)}}}"
            )
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument(
        "--write", action="store_true", help="generate + write full_draw_rotation.json"
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
    print("role balance (structural / outcome ; omit_struct / omit_outcome):")
    for m in CODERS:
        c = counts[m]
        print(
            f"  {m:<7} {c['structural']:>3}/{c['outcome']:>3}   "
            f"omit {c['omit_struct']:>3}/{c['omit_outcome']:>3}"
        )

    if problems:
        print("VERIFY FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print(
        "VERIFY OK: every slot has two distinct size-3 triples; per-construct load balanced."
    )

    if args.write:
        payload = {
            "seed": SEED,
            "n_slots": N_SLOTS,
            "models": MODELS,
            "design": "3-of-4 per-construct rotation (FULL_DRAW_PREREGISTRATION.md §4; "
            "PREREGISTRATION_V2.md Amendment 2.D)",
            "rotation": rotation,
            "role_counts": counts,
        }
        Path(args.out).write_text(json.dumps(payload, indent=2) + "\n")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
