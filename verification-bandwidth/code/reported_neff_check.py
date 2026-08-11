"""
Is the published panel's effective sample size the design-effect formula?

WHY THIS EXISTS. The nine-judge evaluation-panel study (arXiv 2605.29800) reports both
its mean pairwise error correlations AND its effective sample sizes, which makes the
question of how the second was computed checkable by arithmetic on its own published
figures rather than a matter to take on trust.

It checks out to three decimals in all four reported conditions, and that study's
"independence ratio" is n_eff / k exactly. The estimator is therefore borrowed and cited
by this paper, not claimed. What this paper contributes is the IDENTIFICATION of that
quantity with the rank of an acceptance projection, plus the map and the bound that
establish it. This script is the standing guard on that boundary.

Reproduces: Table 3.

Run:
    uv run --with numpy --with scipy python reported_neff_check.py
"""

from __future__ import annotations

import sys

# (condition, k, reported mean pairwise phi on error vectors, reported n_eff)
# Source: arXiv 2605.29800, quoted from its own reported summary statistics.
REPORTED = [
    ("MNLI", 9, 0.391, 2.18),
    ("SNLI", 9, 0.354, 2.35),
    ("AlphaNLI", 9, 0.328, 2.48),
    ("MNLI (chain-of-thought)", 9, 0.456, 1.94),
]

# The study also reports an "independence ratio" of 24.2% for the MNLI condition.
REPORTED_INDEPENDENCE_RATIO = 0.242

TOLERANCE = 0.005  # the reported values are given to two decimals


def design_effect_neff(k: int, phi_bar: float) -> float:
    """Kish effective sample size for k units with mean pairwise correlation phi_bar."""
    return k / (1.0 + (k - 1) * phi_bar)


def main() -> int:
    print(
        "Does the reported n_eff equal the design-effect formula at the reported phi?\n"
    )
    print(
        f"    {'condition':<24} {'k':>2} {'phi':>6} {'formula':>9} {'reported':>9} {'diff':>8}"
    )
    ok = True
    for name, k, phi, reported in REPORTED:
        computed = design_effect_neff(k, phi)
        diff = computed - reported
        if abs(diff) > TOLERANCE:
            ok = False
        print(
            f"    {name:<24} {k:>2} {phi:>6.3f} {computed:>9.3f} "
            f"{reported:>9.2f} {diff:>+8.3f}"
        )

    k, _, _, neff = REPORTED[0][1], None, None, REPORTED[0][3]
    ratio = neff / k
    ratio_ok = abs(ratio - REPORTED_INDEPENDENCE_RATIO) < 0.001
    print(
        f"\n    independence ratio: {neff}/{k} = {ratio:.3f} "
        f"against a reported {REPORTED_INDEPENDENCE_RATIO:.3f} -- "
        f"{'matches' if ratio_ok else 'DOES NOT MATCH'}"
    )
    ok = ok and ratio_ok

    print(
        "\n"
        + (
            "CONFIRMED: the reported effective sample sizes ARE the design-effect formula\n"
            "evaluated at the reported error correlations. Cite the estimator; do not claim it."
            if ok
            else "NOT CONFIRMED: the reported values do not follow from the formula.\n"
            "If this ever fails, the attribution in P6 must be revisited."
        )
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
