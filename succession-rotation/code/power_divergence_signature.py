"""Monte Carlo power for the succession/exit divergence signature.

The signature under test is a CROSSOVER, not a main effect. Two pre-transition
investments are measured on the same instrument in both arms:

    X_cod  process documentation coverage   (converts person-carried residual
                                             into artifact)
    X_exp  successor exposure               (moves person-carried residual into
                                             a specific person)

Two arms, each with its own outcome, standardised within arm:

    Arm A (exit / removal)         Y_A = realised sale price
    Arm B (succession/replacement) Y_B = low operating disruption

The derivation predicts the two investments load on DIFFERENT outcomes: X_cod
on Y_A, X_exp on Y_B. The null the paper must beat is NOT "no association" --
it is "one portfolio raises both", i.e. no crossover. So the estimand is a
difference-in-differences of standardised regression coefficients,

    delta = (b_cod,A - b_exp,A) - (b_cod,B - b_exp,B)

tested against zero. Under the derivation delta = 2*beta; under the rival
single-portfolio account delta = 0.

The run establishes an identity worth stating, because the intuition runs the
other way: at rho = 0 the crossover test has EXACTLY the power of a single
standardised slope at the same per-arm n (.352 vs .349 at n = 40, .719 vs .720
at n = 100). Delta is twice the effect but carries four coefficient variances,
and the two cancel. So the crossover costs nothing per arm -- the factor of two
is in the TOTAL, because there are two arms. A target N stated as a total is
therefore half the design it appears to be, which is the specific error this
script exists to prevent.

Two structural features of the population are varied because neither is known:

  rho   correlation between the two investments. The budget constraint pushes
        it NEGATIVE (they compete for one person's time); owner conscientiousness
        and managerial slack push it POSITIVE. Both are run.
  beta  the per-arm standardised effect of the matching investment.

Run (from the paper directory):
    uv run python code/power_divergence_signature.py

Seed is fixed at 20260810, so the output is deterministic and reproduces the
paper's Table 2 exactly. A recorded run is kept alongside at
code/output/power_divergence_signature.txt.
"""

from __future__ import annotations

import numpy as np

SEED = 20260810
N_SIMS = 20000
ALPHA = 0.05
Z_CRIT = 1.959963984540054  # two-sided .05

# per-arm sample sizes. The design's original target was 80-120 transitions;
# both the "total" and the "per arm" readings of that target are covered.
N_PER_ARM = (40, 50, 60, 75, 100, 125, 150, 200, 300, 400)
BETAS = (0.25, 0.35, 0.45)
RHOS = (-0.30, 0.0, 0.30)


def _arm_contrast(
    rng: np.random.Generator, sims: int, n: int, beta: float, rho: float, loaded: int
) -> tuple[np.ndarray, np.ndarray]:
    """Simulate one arm `sims` times.

    `loaded` is the index (0 = documentation coverage, 1 = successor exposure)
    of the investment that actually drives this arm's outcome. Returns the
    within-arm contrast b_cod - b_exp and its standard error, per replication.
    """
    chol = np.linalg.cholesky(np.array([[1.0, rho], [rho, 1.0]]))
    x = rng.standard_normal((sims, n, 2)) @ chol.T
    noise = rng.standard_normal((sims, n)) * np.sqrt(1.0 - beta**2)
    y = beta * x[:, :, loaded] + noise

    design = np.concatenate([np.ones((sims, n, 1)), x], axis=2)  # (S, n, 3)
    xtx = np.einsum("sni,snj->sij", design, design)
    xty = np.einsum("sni,sn->si", design, y)
    xtx_inv = np.linalg.inv(xtx)
    coef = np.einsum("sij,sj->si", xtx_inv, xty)

    resid = y - np.einsum("sni,si->sn", design, coef)
    sigma2 = np.einsum("sn,sn->s", resid, resid) / (n - 3)

    # Var(b1 - b2) = sigma2 * (C11 + C22 - 2*C12) with C = (X'X)^-1
    var_contrast = sigma2 * (xtx_inv[:, 1, 1] + xtx_inv[:, 2, 2] - 2 * xtx_inv[:, 1, 2])
    return coef[:, 1] - coef[:, 2], var_contrast


def power(
    n: int, beta: float, rho: float, rng: np.random.Generator, sims: int = N_SIMS
) -> float:
    """Fraction of replications rejecting H0: delta = 0."""
    # Arm A's outcome is driven by documentation coverage (index 0),
    # arm B's by successor exposure (index 1).
    contrast_a, var_a = _arm_contrast(rng, sims, n, beta, rho, loaded=0)
    contrast_b, var_b = _arm_contrast(rng, sims, n, beta, rho, loaded=1)
    delta = contrast_a - contrast_b
    se = np.sqrt(var_a + var_b)
    return float(np.mean(np.abs(delta / se) > Z_CRIT))


def main() -> None:
    rng = np.random.default_rng(SEED)
    grid: dict[tuple[float, float, int], float] = {}

    print(
        f"Monte Carlo power, crossover divergence signature. sims={N_SIMS}, alpha={ALPHA}"
    )
    print("delta = (b_cod,A - b_exp,A) - (b_cod,B - b_exp,B); H0: delta = 0\n")
    for rho in RHOS:
        print(f"--- correlation between the two investments: rho = {rho:+.2f} ---")
        header = "  n/arm |" + "".join(f"   beta={b:.2f}" for b in BETAS)
        print(header)
        print("  " + "-" * (len(header) - 2))
        for n in N_PER_ARM:
            cells = []
            for b in BETAS:
                p = power(n, b, rho, rng)
                grid[(rho, b, n)] = p
                cells.append(f"    {p:>7.3f}")
            print(f"  {n:>5}  |" + "".join(cells))
        print()

    print("Smallest n/arm reaching power >= .80 on this grid:")
    for rho in RHOS:
        for b in BETAS:
            reached = next((n for n in N_PER_ARM if grid[(rho, b, n)] >= 0.80), None)
            label = f"{reached:>3} per arm" if reached else f">{N_PER_ARM[-1]} per arm"
            print(f"  rho={rho:+.2f}  beta={b:.2f}  ->  {label}")

    print("\nFor comparison -- the single-arm MAIN effect (b_cod in arm A alone),")
    print("which is what a power calculation would report if the crossover were")
    print("mistaken for a main effect:")
    for b in BETAS:
        for n in (40, 60, 100):
            # power of a single standardised slope, two regressors, rho = 0
            se = np.sqrt((1.0 - b**2) / (n - 3))
            ncp = b / se
            p_main = float(
                1.0
                - 0.5 * (1 + _erf((Z_CRIT - ncp) / np.sqrt(2)))
                + 0.5 * (1 + _erf((-Z_CRIT - ncp) / np.sqrt(2)))
            )
            print(f"  beta={b:.2f}  n={n:>3}  ->  power {p_main:.3f}")


def _erf(x: float | np.ndarray) -> np.ndarray:
    """Abramowitz-Stegun 7.1.26; adequate to ~1e-7, and avoids a scipy dependency."""
    x = np.asarray(x, dtype=float)
    sign = np.sign(x)
    ax = np.abs(x)
    t = 1.0 / (1.0 + 0.3275911 * ax)
    poly = t * (
        0.254829592
        + t * (-0.284496736 + t * (1.421413741 + t * (-1.453152027 + t * 1.061405429)))
    )
    return sign * (1.0 - poly * np.exp(-ax * ax))


if __name__ == "__main__":
    main()
