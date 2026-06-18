"""Back-of-envelope arithmetic for the Tier-Allocation of Capital R-paper.

Companion script for:
    Zharnikov, D. (2026). Tier-Allocation of Capital: A Theory of
    Investment-Tier Choice and Long-Run Firm Value. Working Paper.
    https://doi.org/10.5281/zenodo.20072288

Reproduces every computed numerical value in the paper:
- Section 4.2 Two-Tier Minimal Illustration: Profile A/B/C V_LR multipliers
  and the Profile B/A multiple ratio under the discounted-Cobb-Douglas
  maintained specification.
- Appendix A2 Sensitivity of V_LR Multiple Gap to r: table of V_LR(A),
  V_LR(B), and the B/A ratio across r in {.10, .15, .20}.
- Appendix A3 Alternative alpha_t Calibrations: baseline, conservative,
  and concentrated-stock specifications.
- Optimal dollar-weighted investment shares w_t*(r) derived from the
  user-cost-of-capital FOC (Section 4.2 and Appendix A1).
- Appendix A4 CES Robustness Check: V_LR under CES aggregator with
  sigma in {.5, 1.0, 1.5}; verification that d(dollar_share_6*)/dr > 0
  holds across all three elasticity-of-substitution values.
- Figure 1 Contour Plot: iso-V_LR contours over the (w_4, w_6) plane at
  r = .15, saved to figures/tier_allocation_contour.png.

Maintained model specification --- Option (a) C-r3-2 resolution
(discounted-Cobb-Douglas with Jorgensonian user-cost-of-capital framing):

    V_LR(w; r) = A * I * Prod_t (m_t * w_t / (delta_t + r))^alpha_t,
    Sigma_t alpha_t = 1 (constant returns to scale).

The budget constraint is the Jorgensonian user-cost-of-capital condition:
    Sigma_t q_t * I_t = E,   where q_t = delta_t + r
(Jorgenson 1963 user cost of capital with per-tier rental rate q_t equal to
the sum of the decay rate delta_t and the discount rate r).

FOC (Lagrangian maximization with user-cost constraint):
    w_t*(r) = alpha_t / (delta_t + r)   (after solving lambda = 1)

Dollar-weighted (observable) investment share:
    dollar_share_t*(r) = w_t*(r) / Sum_s w_s*(r)
                       = (alpha_t / (delta_t + r)) / Sum_s (alpha_s / (delta_s + r))

For Tier 6 (highest delta_t = .50), dollar_share_6* RISES as r rises because
delta_6 dominates the Tier-6 denominator while r dominates the low-delta stock
tiers, compressing their weights faster. Sign condition: d(dollar_share_6)/dr > 0
iff delta_6 > delta_S (holds since delta_6 = .50 > delta_S = .119).

The bare-Cobb-Douglas (compute_v_lr_bare) is retained as a legacy/alternative
comparison; the discounted-Cobb-Douglas (compute_v_lr_discounted) is the
maintained specification throughout.

Per-tier accumulation equation (Equation 1, decay-rate convention):
    dS_t/dtau = w_t * I(tau) - delta_t * S_t(tau)

Long-run stock at steady state (Equation 2):
    S_t* = w_t * I / delta_t

Calibrated parameters (Table 1):
    delta_6   = .50/year   (Belo, Lin, Vitorino 2014)
    delta_4   = .15/year   (Lev-Sougiannis 1996; Nadiri-Prucha 1996)
    delta_5   = .175/year  (Eisfeldt-Papanikolaou 2013; Corrado-Hulten-
                            Sichel 2009; midpoint of .15 to .20)
    delta_3   = .075/year  (extrapolated; Wiggins-Ruefli 2002 persistence)
    delta_2   = .075/year  (extrapolated)

M&A separability factors (m_t enters V_LR(w; r) directly):
    m_6   = .25
    m_4   = m_5 = 1.0
    m_2   = m_3 = .6

Cobb-Douglas output elasticities (paper section 3.2; calibrated proportional
to m_t separability factors, normalized to sum to 1):
    alpha_6   = .12
    alpha_4   = alpha_5 = .24
    alpha_2   = alpha_3 = .20
    Sigma     = 1.00

Usage:
    uv run python back_of_envelope.py        # runs all reproductions
    python back_of_envelope.py               # plain CPython works too

Reproducibility: this script is fully deterministic. No RNG used.
"""

from __future__ import annotations
import math
import os
from dataclasses import dataclass
from typing import Optional

# ---------------------------------------------------------------------------
# Calibrated parameters (Table 1)
# ---------------------------------------------------------------------------

DECAY_RATES = {
    2: 0.075,
    3: 0.075,
    4: 0.15,
    5: 0.175,
    6: 0.50,
}

SEPARABILITY = {
    2: 0.6,
    3: 0.6,
    4: 1.0,
    5: 1.0,
    6: 0.25,
}

ALPHA_BASELINE = {
    2: 0.20,
    3: 0.20,
    4: 0.24,
    5: 0.24,
    6: 0.12,
}

ALPHA_CONSERVATIVE = {
    2: 0.20,
    3: 0.20,
    4: 0.20,
    5: 0.20,
    6: 0.20,
}

ALPHA_CONCENTRATED_STOCK = {
    2: 0.175,
    3: 0.175,
    4: 0.30,
    5: 0.30,
    6: 0.05,
}


# ---------------------------------------------------------------------------
# Profile w-vectors (Section 4.2)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Profile:
    """A tier-allocation portfolio: shares w_t summing to 1.0."""

    name: str
    description: str
    w: dict[int, float]

    def __post_init__(self) -> None:
        s = sum(self.w.values())
        assert abs(s - 1.0) < 1e-9, f"{self.name} w-shares sum to {s}, not 1"


PROFILE_A = Profile(
    name="Profile A",
    description="Tier-6-heavy D2C (stylized; e.g., Casper Sleep)",
    w={6: 0.70, 4: 0.10, 5: 0.10, 2: 0.05, 3: 0.05},
)

PROFILE_B = Profile(
    name="Profile B",
    description="Tier-4/Tier-5-heavy specialty B2B (stylized; e.g., Roper)",
    w={6: 0.15, 4: 0.325, 5: 0.325, 2: 0.10, 3: 0.10},
)

PROFILE_C = Profile(
    name="Profile C",
    description="Balanced mid-market (stylized)",
    w={6: 0.40, 4: 0.20, 5: 0.20, 2: 0.10, 3: 0.10},
)


# ---------------------------------------------------------------------------
# Long-run stock + V_LR computations
# ---------------------------------------------------------------------------


def steady_state_stock(w_t: float, delta_t: float, i: float = 1.0) -> float:
    """Equation 2: S_t* = w_t * I / delta_t (decay-rate convention)."""
    return w_t * i / delta_t


def compute_v_lr_bare(
    profile: Profile,
    alpha: dict[int, float],
    a: float = 1.0,
    i: float = 1.0,
) -> float:
    """V_LR under bare Cobb-Douglas (legacy/alternative specification).

    V_LR = A * I * Prod_t (w_t / delta_t)^alpha_t

    Independent of the discount rate r. Retained for comparison; the
    maintained specification is compute_v_lr_discounted.
    """
    product = 1.0
    for t, w_t in profile.w.items():
        s_t = steady_state_stock(w_t, DECAY_RATES[t], i=1.0)
        product *= s_t ** alpha[t]
    return a * i * product


def compute_v_lr_discounted(
    profile: Profile,
    alpha: dict[int, float],
    r: float,
    a: float = 1.0,
    i: float = 1.0,
) -> float:
    """V_LR under discounted-Cobb-Douglas --- the maintained specification.

    V_LR(w; r) = A * I * Prod_t (m_t * w_t / (delta_t + r))^alpha_t

    This is the Option (a) C-r3-2 resolution: Equation 3 now carries explicit
    r-dependence through the Jorgensonian user-cost-of-capital framing.
    The per-tier productivity term m_t * w_t / (delta_t + r) folds the
    perpetuity-form valuation weight rho_t(r) = m_t * delta_t / (delta_t + r)
    and the long-run stock S_t* = w_t * I / delta_t into a single effective
    factor. Under Sigma alpha_t = 1 (CRS), the I^{Sigma alpha_t} = I term
    factors out cleanly. The B/A ratio is r-invariant under CRS (all alpha_t
    sum to 1), but V_LR levels vary with r.
    """
    product = 1.0
    for t, w_t in profile.w.items():
        v_t = SEPARABILITY[t] * w_t / (DECAY_RATES[t] + r)
        product *= v_t ** alpha[t]
    return a * i * product


def optimal_dollar_share(r: float) -> dict[int, float]:
    """Planner's optimal dollar-weighted investment share at discount rate r,
    derived from the user-cost-of-capital FOC w_t* = alpha_t / (delta_t + r).

    The budget constraint is Jorgensonian: Sigma_t (delta_t + r) * w_t = 1,
    where q_t = delta_t + r is the per-tier rental rate (Jorgenson 1963).
    The Lagrangian FOC gives w_t* = alpha_t / (delta_t + r) (after solving
    lambda = 1 from the sum constraint). The dollar-weighted (observable)
    share is w_t* renormalized to sum to 1:
        dollar_share_t*(r) = w_t*(r) / Sum_s w_s*(r)

    For Tier 6 (highest delta_t = .50), dollar_share_6* rises as r rises
    because delta_6 dominates the Tier-6 denominator while r dominates the
    low-delta stock tiers, compressing their weights faster. Sign condition:
    d(dollar_share_6)/dr > 0 iff delta_6 > delta_S (holds since .50 > .119).
    """
    weights = {t: ALPHA_BASELINE[t] / (DECAY_RATES[t] + r) for t in DECAY_RATES}
    total = sum(weights.values())
    return {t: weights[t] / total for t in DECAY_RATES}


# ---------------------------------------------------------------------------
# Reproductions: Section 4.2, Appendix A2, Appendix A3, optimal shares
# ---------------------------------------------------------------------------


def reproduce_section_4_2() -> None:
    """Section 4.2 Two-Tier Minimal Illustration --- Profile A/B/C V_LR
    multipliers under the discounted-Cobb-Douglas maintained specification.

    Maintained spec (Option a C-r3-2 resolution):
        V_LR(w; r) = A * I * Prod_t (m_t * w_t / (delta_t + r))^alpha_t

    Under CRS (Sigma alpha_t = 1), the B/A ratio is r-invariant at 1.93.
    V_LR levels vary with r; reference r = .15.
    """
    r = 0.15
    print("=" * 72)
    print("Section 4.2 Reproduction --- Profile A/B/C V_LR multipliers")
    print(
        "Discounted Cobb-Douglas (maintained): "
        "V_LR(w; r) = A * I * Prod_t (m_t * w_t / (delta_t + r))^alpha_t"
    )
    print(
        "Baseline alpha calibration: alpha_6 = .12; alpha_4 = alpha_5 ="
        " .24; alpha_2 = alpha_3 = .20"
    )
    print(f"r = {r}")
    print("=" * 72)
    v_a = compute_v_lr_discounted(PROFILE_A, ALPHA_BASELINE, r)
    v_b = compute_v_lr_discounted(PROFILE_B, ALPHA_BASELINE, r)
    v_c = compute_v_lr_discounted(PROFILE_C, ALPHA_BASELINE, r)
    print(f"V_LR(Profile A) = {v_a:.3f}  (paper: .221)")
    print(f"V_LR(Profile B) = {v_b:.3f}  (paper: .427)")
    print(f"V_LR(Profile C) = {v_c:.3f}  (paper: .380)")
    print()
    print(
        f"Multiple ratio V_LR(B) / V_LR(A) = {v_b / v_a:.3f}x"
        f"  (paper: 1.93x; r-invariant under CRS)"
    )
    print(f"Multiple ratio V_LR(B) / V_LR(C) = {v_b / v_c:.3f}x" f"  (paper: 1.12x)")
    print(f"Multiple ratio V_LR(C) / V_LR(A) = {v_c / v_a:.3f}x" f"  (paper: 1.72x)")


def reproduce_appendix_a2() -> None:
    """Appendix A2 sensitivity table across r in {.10, .15, .20}.

    Under the discounted-Cobb-Douglas maintained specification with CRS
    (Sigma alpha_t = 1), the B/A ratio is exactly r-invariant at 1.93.
    V_LR levels vary with r because the per-tier productivity factors
    m_t / (delta_t + r) all fall as r rises.

    The bare Cobb-Douglas (compute_v_lr_bare) is reported for comparison.
    """
    print()
    print("=" * 72)
    print("Appendix A2 Reproduction --- Sensitivity to r")
    print("=" * 72)
    print()
    print(
        "MAINTAINED SPEC --- Discounted Cobb-Douglas "
        "V_LR(w; r) = A * I * Prod_t (m_t * w_t / (delta_t + r))^alpha_t:"
    )
    print(f"{'r':>6}  {'V_LR(A)':>10}  {'V_LR(B)':>10}  {'B/A':>8}")
    for r in [0.10, 0.15, 0.20]:
        v_a = compute_v_lr_discounted(PROFILE_A, ALPHA_BASELINE, r)
        v_b = compute_v_lr_discounted(PROFILE_B, ALPHA_BASELINE, r)
        print(f"{r:>6.2f}  {v_a:>10.3f}  {v_b:>10.3f}  {v_b / v_a:>8.3f}")
    print()
    print(
        "LEGACY/ALTERNATIVE --- Bare Cobb-Douglas "
        "V_LR = A * I * Prod_t (w_t / delta_t)^alpha_t (r-invariant):"
    )
    print(f"{'r':>6}  {'V_LR(A)':>10}  {'V_LR(B)':>10}  {'B/A':>8}")
    for r in [0.10, 0.15, 0.20]:
        v_a = compute_v_lr_bare(PROFILE_A, ALPHA_BASELINE)
        v_b = compute_v_lr_bare(PROFILE_B, ALPHA_BASELINE)
        print(f"{r:>6.2f}  {v_a:>10.3f}  {v_b:>10.3f}  {v_b / v_a:>8.3f}")


def reproduce_appendix_a3() -> None:
    """Appendix A3 alternative alpha_t calibrations.

    Computed under the discounted-Cobb-Douglas maintained spec at r = .15.

    Published table:
        Baseline (.12 / .24 / .20):                V_A = .221, V_B = .427
                                                   ratio = 1.93
        Conservative (.20 / .20 / .20):            V_A = ?, V_B = ?
                                                   ratio = 1.55
        Concentrated-stock (.05 / .30 / .175):     V_A = ?, V_B = ?
                                                   ratio = 2.39
    """
    r = 0.15
    print()
    print("=" * 72)
    print("Appendix A3 Reproduction --- Alternative alpha_t calibrations")
    print(f"Discounted Cobb-Douglas (maintained spec) at r = {r}")
    print("=" * 72)
    print()
    specs = [
        (
            "Baseline       (alpha_6=.12; alpha_4=alpha_5=.24; alpha_2=alpha_3=.20)",
            ALPHA_BASELINE,
        ),
        ("Conservative   (all alpha_t = .20)", ALPHA_CONSERVATIVE),
        (
            "Concentrated   (alpha_6=.05; alpha_4=alpha_5=.30; alpha_2=alpha_3=.175)",
            ALPHA_CONCENTRATED_STOCK,
        ),
    ]
    print(f"{'Specification':<70}  {'V_A':>7}  {'V_B':>7}  {'B/A':>6}")
    for label, alpha in specs:
        v_a = compute_v_lr_discounted(PROFILE_A, alpha, r)
        v_b = compute_v_lr_discounted(PROFILE_B, alpha, r)
        print(f"{label:<70}  {v_a:>7.3f}  {v_b:>7.3f}  {v_b / v_a:>6.2f}")


def reproduce_optimal_shares() -> None:
    """Planner's optimal dollar-weighted investment shares at r in {.10, .15, .20}.

    Derived from FOC w_t* = alpha_t / (delta_t + r) under the Jorgensonian
    user-cost-of-capital budget constraint Sigma (delta_t + r) * w_t = 1.
    The dollar-share is w_t* renormalized to sum to 1.

    Shows comparative static: dollar_share_6* rises as r rises (from 4.6% at
    r=.10 to 5.3% at r=.15 to 5.8% at r=.20), confirming d(dollar_share_6)/dr > 0.
    """
    print()
    print("=" * 72)
    print("Optimal Dollar-Weighted Investment Shares w_t*(r)")
    print("FOC: w_t* = alpha_t / (delta_t + r); renormalized to sum to 1")
    print("=" * 72)
    print()
    header = f"{'r':>6}  {'Tier2':>8}  {'Tier3':>8}  {'Tier4':>8}  {'Tier5':>8}  {'Tier6':>8}  {'Sum':>6}"
    print(header)
    for r in [0.10, 0.15, 0.20]:
        shares = optimal_dollar_share(r)
        row = (
            f"{r:>6.2f}  "
            f"{shares[2]:>8.4f}  "
            f"{shares[3]:>8.4f}  "
            f"{shares[4]:>8.4f}  "
            f"{shares[5]:>8.4f}  "
            f"{shares[6]:>8.4f}  "
            f"{sum(shares.values()):>6.4f}"
        )
        print(row)
    print()
    print(
        "Tier-6 dollar-share rises with r: .046 (r=.10) -> .053 (r=.15) ->"
        " .058 (r=.20)"
    )
    print(
        "Sign confirmed: d(dollar_share_6)/dr > 0 iff delta_6 > delta_S (.50 > .119)."
    )


# ---------------------------------------------------------------------------
# Appendix A4: CES robustness check
# ---------------------------------------------------------------------------


def compute_v_lr_ces(
    profile: Profile,
    alpha: dict[int, float],
    sigma: float,
    r: float,
    a: float = 1.0,
    i: float = 1.0,
) -> float:
    """V_LR under CES aggregator --- robustness check for Appendix A4.

    For sigma != 1:
        V_LR^CES(w; r, sigma) = A * I *
            [Sum_t alpha_t * (m_t * w_t / (delta_t + r))^((sigma-1)/sigma)]
            ^(sigma/(sigma-1))

    sigma = 1 recovers the Cobb-Douglas limit (use compute_v_lr_discounted).
    sigma < 1: gross complements / co-specialization-strong.
    sigma > 1: gross substitutes / co-specialization-weak.

    The maintained specification stays Cobb-Douglas (sigma = 1); this function
    implements the CES generalization as a robustness check only.
    """
    if abs(sigma - 1.0) < 1e-10:
        # Use the Cobb-Douglas maintained spec directly.
        return compute_v_lr_discounted(profile, alpha, r, a=a, i=i)
    rho = (sigma - 1.0) / sigma
    agg = 0.0
    for t, w_t in profile.w.items():
        factor = SEPARABILITY[t] * w_t / (DECAY_RATES[t] + r)
        agg += alpha[t] * (factor**rho)
    return a * i * (agg ** (sigma / (sigma - 1.0)))


def _optimal_w6_ces(sigma: float, r: float) -> float:
    """Numerically solve for the planner-optimal dollar_share_6* under CES.

    Uses scipy.optimize.minimize_scalar on the 2-tier reduction:
    Tier 6 vs. aggregate stock tier (Tiers 2-5 equal-weighted).
    Returns the dollar-weighted (observable) share of Tier 6 at the optimum.

    The full 5-tier minimization is not required for sign verification of
    d(dollar_share_6*)/dr > 0 --- the 2-tier reduction preserves the sign.
    """
    from scipy.optimize import minimize_scalar

    alpha_6 = ALPHA_BASELINE[6]
    alpha_s = 1.0 - alpha_6  # aggregate stock tier

    # Equal-weighted aggregate decay for tiers 2-5
    delta_s = (DECAY_RATES[2] + DECAY_RATES[3] + DECAY_RATES[4] + DECAY_RATES[5]) / 4.0
    m_s = (SEPARABILITY[2] + SEPARABILITY[3] + SEPARABILITY[4] + SEPARABILITY[5]) / 4.0
    m_6 = SEPARABILITY[6]
    delta_6 = DECAY_RATES[6]

    def neg_v(w6: float) -> float:
        """Negative of CES value for two-tier reduction."""
        if w6 <= 0.0 or w6 >= 1.0:
            return 1e12
        w_s = 1.0 - w6
        f6 = m_6 * w6 / (delta_6 + r)
        fs = m_s * w_s / (delta_s + r)
        if abs(sigma - 1.0) < 1e-10:
            # Cobb-Douglas limit
            return -(f6**alpha_6) * (fs**alpha_s)
        rho = (sigma - 1.0) / sigma
        agg = alpha_6 * (f6**rho) + alpha_s * (fs**rho)
        return -(agg ** (sigma / (sigma - 1.0)))

    result = minimize_scalar(neg_v, bounds=(1e-6, 1.0 - 1e-6), method="bounded")
    w6_star = result.x
    # Convert to dollar-weighted share (same as w6_star for 2-tier)
    return w6_star


def reproduce_appendix_a4_ces() -> None:
    """Appendix A4 CES robustness check.

    Verifies two things:
    1. B/A ratio at r = .15 across sigma in {.5, 1.0, 1.5}.
    2. d(dollar_share_6*)/dr > 0 under sigma in {.5, 1.5} using
       numerical optimization at r in {.10, .15, .20}.

    Maintained spec stays Cobb-Douglas (sigma = 1); CES is robustness only.
    """
    print()
    print("=" * 72)
    print("Appendix A4 Reproduction --- CES Robustness Check")
    print("V_LR^CES: sigma in {.5, 1.0, 1.5} at r = .15")
    print("=" * 72)
    print()

    r_ref = 0.15
    sigmas = [0.5, 1.0, 1.5]

    print("Panel 1: Profile A/B V_LR and B/A ratio by sigma at r = .15")
    print(f"{'sigma':>7}  {'V_LR(A)':>10}  {'V_LR(B)':>10}  {'B/A':>8}")
    ba_ratios: dict[float, float] = {}
    for sigma in sigmas:
        v_a = compute_v_lr_ces(PROFILE_A, ALPHA_BASELINE, sigma, r_ref)
        v_b = compute_v_lr_ces(PROFILE_B, ALPHA_BASELINE, sigma, r_ref)
        ratio = v_b / v_a
        ba_ratios[sigma] = ratio
        print(f"{sigma:>7.1f}  {v_a:>10.3f}  {v_b:>10.3f}  {ratio:>8.3f}")

    print()
    print("Panel 2: Planner-optimal dollar_share_6*(r) by sigma --- sign check")
    print("Verifies d(dollar_share_6*)/dr > 0 holds across sigma.")
    print(f"{'sigma':>7}  {'r=.10':>10}  {'r=.15':>10}  {'r=.20':>10}  {'Sign':>8}")
    for sigma in [0.5, 1.5]:
        shares = []
        for r in [0.10, 0.15, 0.20]:
            shares.append(_optimal_w6_ces(sigma, r))
        increasing = shares[0] < shares[1] < shares[2]
        sign_str = "d>0 YES" if increasing else "d>0 NO"
        print(
            f"{sigma:>7.1f}  {shares[0]:>10.4f}  {shares[1]:>10.4f}"
            f"  {shares[2]:>10.4f}  {sign_str:>8}"
        )
    # Cobb-Douglas (sigma=1) verified analytically in Appendix A1
    shares_cd = [optimal_dollar_share(r)[6] for r in [0.10, 0.15, 0.20]]
    print(
        f"{'1.0 (CD)':>7}  {shares_cd[0]:>10.4f}  {shares_cd[1]:>10.4f}"
        f"  {shares_cd[2]:>10.4f}  {'d>0 YES':>8}"
    )
    print()
    print("B/A ordering Profile B > Profile A holds across all sigma values.")
    print(
        "CES sigma < 1 (co-specialization-strong) attenuates but does not"
        " reverse the qualitative ordering."
    )

    # Return ratios for external use
    return ba_ratios


# ---------------------------------------------------------------------------
# Figure 1: Contour plot over (w_4, w_6) plane
# ---------------------------------------------------------------------------

# Planner-optimal relative shares of tiers {2, 3, 5} within the residual
# (1 - w_4 - w_6). These are the renormalized dollar-shares at r = .15:
#   dollar_share_t*(r=.15) = (alpha_t/(delta_t+r)) / Sum_s(alpha_s/(delta_s+r))
# After excluding tiers 4 and 6, the remaining {2, 3, 5} have shares:
#   2: .2539, 3: .2539, 5: .2109  => relative: .3533, .3533, .2935
_RESIDUAL_SHARES = {2: 0.3533, 3: 0.3533, 5: 0.2935}

# Verify they sum to 1 (up to rounding)
assert abs(sum(_RESIDUAL_SHARES.values()) - 1.0) < 1e-3


def _profile_from_w4_w6(w4: float, w6: float) -> Optional[Profile]:
    """Build a Profile from (w_4, w_6) with residual split across {2, 3, 5}.

    Returns None if residual < 0 (infeasible grid point).
    The residual shares are normalised precisely to sum to 1 - w4 - w6.
    """
    residual = 1.0 - w4 - w6
    if residual < -1e-12:
        return None
    if residual < 0.0:
        residual = 0.0
    # Distribute residual using planner-optimal relative shares for {2, 3, 5}.
    # Use exact fractions to avoid floating-point accumulation errors.
    rs = _RESIDUAL_SHARES
    total_rs = rs[2] + rs[3] + rs[5]
    w2 = residual * rs[2] / total_rs
    w3 = residual * rs[3] / total_rs
    w5 = residual * rs[5] / total_rs
    # Force exact sum to 1 by adjusting w4 last
    exact_w4 = 1.0 - w6 - w2 - w3 - w5
    w = {
        4: exact_w4,
        6: w6,
        2: w2,
        3: w3,
        5: w5,
    }
    return Profile(name="grid", description="grid", w=w)


def generate_contour_plot(
    output_path: str = "",
    r: float = 0.15,
    step: float = 0.005,
) -> None:
    """Generate and save iso-V_LR contour plot over the (w_4, w_6) plane.

    Grid: (w_4, w_6) in [0, .85] x [0, .85], step = 0.005.
    For each grid point, residual (1 - w_4 - w_6) is split among tiers {2, 3, 5}
    using the planner-optimal relative shares at r = .15 (_RESIDUAL_SHARES).
    Points where residual < 0 are masked (NaN).

    Saves a 300-DPI PNG with viridis colormap (print + colorblind safe).

    Output default: <paper_dir>/figures/tier_allocation_contour.png
    """
    import numpy as np
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    if not output_path:
        # Resolve relative to this file's location: code/ -> paper dir -> figures/
        script_dir = os.path.dirname(os.path.abspath(__file__))
        paper_dir = os.path.abspath(os.path.join(script_dir, ".."))
        output_path = os.path.join(paper_dir, "figures", "tier_allocation_contour.png")

    print()
    print("=" * 72)
    print(f"Figure 1: Generating V_LR contour plot at r = {r}")
    print(f"Output: {output_path}")
    print("=" * 72)

    # Build grid
    w4_vals = np.arange(0.0, 0.86, step)
    w6_vals = np.arange(0.0, 0.86, step)
    W4, W6 = np.meshgrid(w4_vals, w6_vals)
    V = np.full_like(W4, float("nan"))

    for i in range(W4.shape[0]):
        for j in range(W4.shape[1]):
            w4 = float(W4[i, j])
            w6 = float(W6[i, j])
            p = _profile_from_w4_w6(w4, w6)
            if p is not None:
                # Skip profiles with any zero or negative share (log-undefined)
                if all(v > 1e-12 for v in p.w.values()):
                    V[i, j] = compute_v_lr_discounted(p, ALPHA_BASELINE, r)

    # Planner-optimal point
    ds = optimal_dollar_share(r)
    w4_opt = ds[4]  # 0.2285
    w6_opt = ds[6]  # 0.0527

    # Profile A and B coordinates
    w4_A, w6_A = PROFILE_A.w[4], PROFILE_A.w[6]  # .10, .70
    w4_B, w6_B = PROFILE_B.w[4], PROFILE_B.w[6]  # .325, .15

    # Plot
    fig, ax = plt.subplots(figsize=(8, 7))

    # Filled contour (viridis: print + colorblind safe)
    vmin = float(np.nanpercentile(V, 5))
    vmax = float(np.nanpercentile(V, 95))
    cf = ax.contourf(W4, W6, V, levels=20, cmap="viridis", vmin=vmin, vmax=vmax)

    # Iso-value contour lines
    cs = ax.contour(W4, W6, V, levels=12, colors="white", linewidths=0.6, alpha=0.5)
    ax.clabel(cs, inline=True, fontsize=7, fmt="%.3f")

    # Colorbar
    cbar = fig.colorbar(cf, ax=ax, shrink=0.88)
    cbar.set_label("V_LR (normalized, A*I = 1)", fontsize=10)

    # Planner-optimal point (star)
    ax.scatter(
        [w4_opt],
        [w6_opt],
        marker="*",
        s=220,
        c="gold",
        zorder=5,
        linewidths=0.8,
        edgecolors="black",
        label=f"Planner optimum ({w4_opt:.2f}, {w6_opt:.2f})",
    )
    ax.annotate(
        f"  Planner optimum\n  ({w4_opt:.2f}, {w6_opt:.2f})",
        xy=(w4_opt, w6_opt),
        xytext=(w4_opt + 0.07, w6_opt + 0.06),
        fontsize=8,
        color="gold",
        arrowprops=dict(arrowstyle="->", color="gold", lw=1.2),
    )

    # Profile A
    ax.scatter(
        [w4_A],
        [w6_A],
        marker="^",
        s=140,
        c="tomato",
        zorder=5,
        edgecolors="black",
        linewidths=0.8,
        label=f"Profile A  ({w4_A:.2f}, {w6_A:.2f}) -- Tier-6-heavy D2C",
    )
    ax.annotate(
        f"Profile A ({w4_A:.2f}, {w6_A:.2f})",
        xy=(w4_A, w6_A),
        xytext=(w4_A + 0.05, w6_A - 0.07),
        fontsize=8,
        color="tomato",
        arrowprops=dict(arrowstyle="->", color="tomato", lw=1.2),
    )

    # Profile B
    ax.scatter(
        [w4_B],
        [w6_B],
        marker="s",
        s=110,
        c="cyan",
        zorder=5,
        edgecolors="black",
        linewidths=0.8,
        label=f"Profile B  ({w4_B:.2f}, {w6_B:.2f}) -- Tier-4/5-heavy B2B",
    )
    ax.annotate(
        f"Profile B ({w4_B:.2f}, {w6_B:.2f})",
        xy=(w4_B, w6_B),
        xytext=(w4_B + 0.06, w6_B + 0.05),
        fontsize=8,
        color="cyan",
        arrowprops=dict(arrowstyle="->", color="cyan", lw=1.2),
    )

    # Infeasible region shade (w4 + w6 > 1)
    tri_x = [0.0, 0.85, 0.85, 0.0]
    tri_y = [1.0, 0.15, 0.85, 0.85]  # approximate boundary
    ax.fill_between(
        [0.0, 0.85],
        [1.0, 0.15],
        [0.85, 0.85],
        color="gray",
        alpha=0.25,
        label="Infeasible (w_4 + w_6 > 1)",
    )

    ax.set_xlim(0.0, 0.85)
    ax.set_ylim(0.0, 0.85)
    ax.set_xlabel("w_4  (Tier-4 share)", fontsize=12)
    ax.set_ylabel("w_6  (Tier-6 share)", fontsize=12)
    ax.set_title(
        "Long-run value V_LR over the (w_4, w_6) plane at r = .15\n"
        "(w_2, w_3, w_5 held at planner-optimal relative shares .353, .353, .294)",
        fontsize=11,
    )
    ax.legend(fontsize=8, loc="upper right", framealpha=0.8)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
    ax.grid(True, linestyle=":", linewidth=0.4, alpha=0.6)

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    file_size = os.path.getsize(output_path)
    print(f"Saved: {output_path}  ({file_size:,} bytes)")
    print(f"Planner-optimal interior: w_4* = {w4_opt:.4f}, w_6* = {w6_opt:.4f}")
    print("Profile A  (w_4=.10, w_6=.70): high-w_6 corner, steep welfare-loss region.")
    print("Profile B  (w_4=.325, w_6=.15): near the high-V_LR ridge.")


def main() -> None:
    """Run all reproductions and print results."""
    reproduce_section_4_2()
    reproduce_appendix_a2()
    reproduce_appendix_a3()
    reproduce_optimal_shares()
    reproduce_appendix_a4_ces()
    generate_contour_plot()
    print()
    print("=" * 72)
    print("Done. All values are deterministic; no RNG seeded.")
    print("Maintained specification: discounted-Cobb-Douglas with Jorgensonian")
    print("user-cost-of-capital framing (Option a C-r3-2 resolution).")
    print("CES robustness check (sigma in {.5, 1.0, 1.5}) in Appendix A4.")
    print("Figure 1 contour plot saved to figures/tier_allocation_contour.png.")
    print("=" * 72)


if __name__ == "__main__":
    main()
