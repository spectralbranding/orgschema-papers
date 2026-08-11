"""The map between GEOMETRIC evaluator correlation and the PHI coefficient on errors.

THE PROBLEM
-----------
`threat1_kill_test.py` measures phi_bar as a GEOMETRIC correlation: the mean
absolute inner product between the unit directions v_e that evaluators inspect.
Kohli (2026) measures phi as a PHI COEFFICIENT on binary error indicators —
Pearson correlation of two judges' 0/1 error vectors against gold labels.

Reading the design effect n_eff = k / (1 + (k-1) phi_bar) as an estimator of
verification bandwidth stands or falls on the link between the two. If the map
is non-monotone, or distribution-dependent in a way that leaves n_eff
uninterpretable as a rank, the reading degrades to an analogy.

THE MODEL
---------
Ambient organizational state space R^n. Evaluator e inspects the unit direction
v_e and flags a deviation d iff |<v_e, d>| > tau: an audit sees only the
component of a deviation that lies in what it inspects. Every d drawn is a
genuine deviation, so a non-flag IS an error (a miss), and

    E_e = 1[|<v_e, d>| <= tau]

is the binary error indicator whose pairwise Pearson correlation is Kohli's phi.

Take d ~ N(0, sigma^2 I_n) (isotropic deviations; the spherical case is the
same after conditioning, see the RADIAL section). Then

    (X, Y) = (<v_e, d>, <v_f, d>)

is bivariate normal with correlation EXACTLY rho = <v_e, v_f>. So the geometric
correlation IS the correlation of the inspected components, and the whole
question reduces to: what does a symmetric two-sided dichotomization at
+/- tau do to a bivariate normal correlation?

THE RESULT (derived here, verified numerically below)
-----------------------------------------------------
Write t = tau/sigma, q_e = P(|X| <= t_e) = 2 Phi(t_e) - 1 for the marginal
error (miss) rate. Inclusion-exclusion on the bivariate normal CDF, plus the
reflection identities, gives the exact joint miss probability

    P11(rho) = 2 Phi2(t_e, t_f; rho) + 2 Phi2(t_e, t_f; -rho)
               - 2 Phi(t_e) - 2 Phi(t_f) + 1                          (1)

    phi(rho) = [P11(rho) - q_e q_f] / sqrt(q_e (1-q_e) q_f (1-q_f))   (2)

Five properties follow, and each is checked numerically in main():

  M1 EVEN.       (1) is invariant under rho -> -rho. The folded rule |<v,d>|
                 cannot see the sign of a direction, so phi depends on |rho|.
                 This justifies the use of the MEAN
                 ABSOLUTE inner product as its geometric correlation.

  M2 MONOTONE.   By Plackett's identity d/drho Phi2(h,k;rho) = phi2(h,k;rho),

                     dP11/drho = 2 phi2(t_e,t_f;rho) - 2 phi2(t_e,t_f;-rho)

                 and phi2(h,k;rho) > phi2(h,k;-rho) iff rho*h*k > 0. With
                 t_e, t_f > 0 the derivative is STRICTLY POSITIVE for all
                 rho in (0,1) — including heterogeneous thresholds. In the
                 homogeneous case it simplifies to

                     dP11/drho = [exp(-t^2/(1+rho)) - exp(-t^2/(1-rho))]
                                 / (pi sqrt(1-rho^2))                  (3)

  M3 FIXED ENDS. phi(0) = 0 and phi(1) = 1 for every t. The map is a strictly
                 increasing bijection of [0,1] onto itself — hence INVERTIBLE
                 given the marginal error rate q, which is observable in any
                 panel with gold labels.

  M4 QUADRATIC AT THE ORIGIN. dP11/drho = 0 at rho = 0, so the map is tangent
                 to zero and expands as

                     phi(rho) ~ [t^2 exp(-t^2) / (pi q (1-q))] rho^2    (4)

                 Error correlation is SECOND-ORDER small in geometric
                 correlation near independence.

  M5 ATTENUATION. phi(rho) < rho strictly on (0,1) for every t (verified on a
                 dense (rho, t) grid, homogeneous and heterogeneous). This is
                 the property that matters most, because it is DISTRIBUTION-
                 FREE in the only sense the paper needs:

                     n_eff_rank = Kish(rho_bar) <= Kish(phi_bar) = n_eff_vote

                 The Kish design effect computed on ERROR vectors is an UPPER
                 BOUND on verification bandwidth. Kohli's "two effective votes"
                 does not need correcting to be safe — correcting it only makes
                 the finding more pessimistic.

RADIAL / SHARED ITEM DIFFICULTY
-------------------------------
If deviations carry a random common magnitude R (equivalently: items differ in
difficulty), then conditional on R the model above holds with a common random
threshold T = tau/R, and the law of total covariance splits phi exactly:

    phi = E_T[Cov(E_e,E_f | T)] / (q(1-q))   +   Var_T(q(T)) / (q(1-q))

into a GEOMETRIC term (the first, which is what bandwidth means) and a
DIFFICULTY term (the second). So phi(rho=0) = Var_T(q(T)) / (q(1-q)) > 0:
geometrically ORTHOGONAL evaluators still show correlated errors purely because
items share difficulty. That term is a nuisance for bandwidth — it is not
shared inspection direction — so it must be netted out before the map is
inverted, or the recovered rho is biased upward.

Kohli reports a shared-item-difficulty component on his panel, which is the
same mechanism qualitatively. Do NOT assume his 6.8% figure is this term: as
reported it is the share of the CONDORCET GAP attributable to shared
difficulty, not a decomposition of phi. Confirming what exactly he decomposes,
and whether it can be reused as the difficulty correction here, is an open
action item, not something this script establishes.

WHAT THIS SCRIPT DOES NOT SETTLE
--------------------------------
One-dimensional inspection subspaces; misses as the only error type (no false
alarms, since a deviation is present by construction); Gaussian/spherical
isotropic deviations; and a shared-factor correlation structure. Multi-
dimensional inspection subspaces and a false-alarm arm are open.

Run: uv run --with numpy --with scipy --with matplotlib python phi_mapping.py
Seed 20260811 (matches threat1_kill_test.py). Runtime ~30 s.
Writes ../output/figures/phi_mapping.png
"""

from __future__ import annotations

import os

import numpy as np
from scipy.optimize import brentq
from scipy.stats import multivariate_normal as mvn
from scipy.stats import norm

SEED = 20260811
K_KOHLI = 9  # Kohli's panel size, for the n_eff columns
N_GL = 400  # Gauss-Legendre nodes for the P11 quadrature
RHO_CAP = 1.0 - 1e-9

# Kohli (2026), arXiv 2605.29800v1 — mean pairwise phi on binary error vectors.
KOHLI_PHI = {
    "MNLI": 0.391,
    "SNLI": 0.354,
    "AlphaNLI": 0.328,
    "MNLI (chain-of-thought)": 0.456,
}

_GL_X, _GL_W = np.polynomial.legendre.leggauss(N_GL)


# --------------------------------------------------------------------------
# the map
# --------------------------------------------------------------------------
def q_of_t(t):
    """Marginal error (miss) rate P(|X| <= t) for standard normal X."""
    return 2.0 * norm.cdf(t) - 1.0


def t_of_q(q):
    """Inverse of q_of_t: the threshold implied by an observed miss rate."""
    return norm.ppf((q + 1.0) / 2.0)


def p11(rho, t_e, t_f=None):
    """P(|X| <= t_e, |Y| <= t_f) for standard bivariate normal, corr rho.

    Computed by Gauss-Legendre quadrature on the conditional-normal form
    rather than by (1), which needs a bivariate CDF; main() checks the two
    against each other and against Monte Carlo.
    """
    t_f = t_e if t_f is None else t_f
    r = float(np.clip(abs(rho), 0.0, RHO_CAP))
    s = np.sqrt(1.0 - r * r)
    x = t_e * _GL_X  # map [-1,1] -> [-t_e, t_e]
    inner = norm.cdf((t_f - r * x) / s) - norm.cdf((-t_f - r * x) / s)
    return float(t_e * np.sum(_GL_W * norm.pdf(x) * inner))


def p11_via_cdf(rho, t_e, t_f=None):
    """P11 by the closed form (1), using scipy's bivariate normal CDF."""
    t_f = t_e if t_f is None else t_f
    r = float(np.clip(rho, -RHO_CAP, RHO_CAP))

    def cdf2(sign):
        cov = [[1.0, sign * r], [sign * r, 1.0]]
        return float(mvn(mean=[0.0, 0.0], cov=cov).cdf([t_e, t_f]))

    return 2 * cdf2(1) + 2 * cdf2(-1) - 2 * norm.cdf(t_e) - 2 * norm.cdf(t_f) + 1.0


def phi_from_rho(rho, t_e, t_f=None):
    """Kohli-style phi coefficient induced by geometric correlation rho."""
    t_f = t_e if t_f is None else t_f
    q_e, q_f = q_of_t(t_e), q_of_t(t_f)
    denom = np.sqrt(q_e * (1 - q_e) * q_f * (1 - q_f))
    return (p11(rho, t_e, t_f) - q_e * q_f) / denom


def dp11_drho(rho, t_e, t_f=None):
    """Analytic derivative via Plackett's identity (see M2)."""
    t_f = t_e if t_f is None else t_f
    r = float(np.clip(rho, -RHO_CAP, RHO_CAP))

    def dens(sgn):
        num = t_e**2 + t_f**2 - 2.0 * sgn * r * t_e * t_f
        return np.exp(-num / (2.0 * (1 - r * r))) / (2 * np.pi * np.sqrt(1 - r * r))

    return 2.0 * dens(1) - 2.0 * dens(-1)


def rho_from_phi(phi, t_e, t_f=None):
    """Invert the map: the geometric correlation implied by an observed phi."""
    if phi <= 0.0:
        return 0.0
    return brentq(lambda r: phi_from_rho(r, t_e, t_f) - phi, 1e-12, RHO_CAP, xtol=1e-12)


def kish(k, phi_bar):
    """Kish effective sample size / design effect."""
    return k / (1.0 + (k - 1) * phi_bar)


# --------------------------------------------------------------------------
# checks
# --------------------------------------------------------------------------
def check_quadrature(rng):
    """C1: the quadrature, the closed form (1), and Monte Carlo must agree."""
    print("C1  QUADRATURE vs CLOSED FORM (1) vs MONTE CARLO")
    print(f"    {'t':>6} {'rho':>7} {'P11 quad':>10} {'P11 cdf':>10} {'P11 mc':>10}")
    worst_cdf = worst_mc = 0.0
    for t in (0.30, 0.674, 1.00, 1.96):
        for rho in (0.0, 0.391, 0.70, 0.90):
            a = p11(rho, t)
            b = p11_via_cdf(rho, t)
            chol = np.linalg.cholesky([[1.0, rho], [rho, 1.0]])
            z = rng.normal(size=(2_000_000, 2)) @ chol.T
            c = float(((np.abs(z[:, 0]) <= t) & (np.abs(z[:, 1]) <= t)).mean())
            worst_cdf = max(worst_cdf, abs(a - b))
            worst_mc = max(worst_mc, abs(a - c))
            print(f"    {t:>6.3f} {rho:>7.3f} {a:>10.6f} {b:>10.6f} {c:>10.6f}")
    print(f"    max |quad - cdf| = {worst_cdf:.2e}   max |quad - mc| = {worst_mc:.2e}")
    return worst_cdf < 1e-6 and worst_mc < 2e-3


def check_even():
    """M1: the map is even in rho."""
    worst = max(
        abs(p11_via_cdf(r, t) - p11_via_cdf(-r, t))
        for t in (0.3, 0.674, 1.0, 1.96)
        for r in (0.2, 0.5, 0.9)
    )
    print(f"\nM1  EVEN in rho: max |P11(rho) - P11(-rho)| = {worst:.2e}")
    return worst < 1e-9


def check_monotone():
    """M2: derivative strictly positive; analytic form matches numeric."""
    ts = np.linspace(0.05, 3.50, 40)
    rs = np.linspace(0.001, 0.995, 60)
    d_min, at = np.inf, None
    for t in ts:
        for r in rs:
            d = dp11_drho(r, t)
            if d < d_min:
                d_min, at = d, (t, r)
    print(
        f"\nM2  MONOTONE: min dP11/drho over grid = {d_min:+.3e} at t={at[0]:.3f} rho={at[1]:.3f}"
    )

    worst = 0.0
    for t, r in ((0.674, 0.40), (1.00, 0.70), (0.30, 0.20), (1.96, 0.90)):
        h = 1e-5
        num = (p11_via_cdf(r + h, t) - p11_via_cdf(r - h, t)) / (2 * h)
        worst = max(worst, abs(dp11_drho(r, t) - num))
    print(f"    analytic vs numeric derivative: max abs diff = {worst:.2e}")

    # heterogeneous thresholds
    het_min = np.inf
    for t_e in np.linspace(0.1, 2.5, 15):
        for t_f in np.linspace(0.1, 2.5, 15):
            for r in np.linspace(0.05, 0.99, 25):
                het_min = min(het_min, dp11_drho(r, t_e, t_f))
    print(f"    heterogeneous (t_e != t_f): min derivative = {het_min:+.3e}")
    return d_min > 0 and het_min > 0 and worst < 1e-8


def check_endpoints():
    """M3: phi(0) = 0 and phi(rho) -> 1 as rho -> 1, for every t.

    The upper endpoint is approached like 1 - O(sqrt(1-rho)), not attained at
    any finite grid point, so the test is a convergence test: the residual must
    shrink monotonically and be below 1e-3 by rho = 1 - 1e-9.
    """
    print("\nM3  FIXED ENDPOINTS: phi(0) = 0 and phi(rho) -> 1")
    eps = (1e-2, 1e-4, 1e-6, 1e-9)
    print(
        f"    {'t':>6} {'q':>7} {'phi(0)':>10} "
        + " ".join(f"{'1-phi@' + f'{e:.0e}':>13}" for e in eps)
    )
    ok = True
    for t in (0.15, 0.30, 0.674, 1.00, 1.96, 3.00):
        lo = phi_from_rho(0.0, t)
        resid = [1.0 - phi_from_rho(1.0 - e, t) for e in eps]
        ok &= abs(lo) < 1e-9
        ok &= all(a > b for a, b in zip(resid, resid[1:]))  # monotone shrink
        ok &= resid[-1] < 1e-3
        print(
            f"    {t:>6.3f} {q_of_t(t):>7.4f} {lo:>10.2e} "
            + " ".join(f"{r:>13.2e}" for r in resid)
        )
    return ok


def check_quadratic():
    """M4: leading coefficient of the small-rho expansion (4)."""
    print("\nM4  QUADRATIC AT THE ORIGIN: phi ~ c rho^2, c = t^2 e^-t^2 / (pi q(1-q))")
    worst = 0.0
    for t in (0.30, 0.674, 1.00, 1.96):
        q = q_of_t(t)
        c_ana = t**2 * np.exp(-(t**2)) / (np.pi * q * (1 - q))
        c_num = phi_from_rho(0.02, t) / 0.02**2
        worst = max(worst, abs(c_ana - c_num) / c_ana)
        print(f"    t={t:>5.3f}  c analytic={c_ana:.5f}  c numeric={c_num:.5f}")
    print(f"    max relative discrepancy = {worst:.2e}")
    return worst < 1e-3


def check_attenuation():
    """M5: phi(rho) < rho strictly, homogeneous and heterogeneous."""
    print("\nM5  ATTENUATION: phi(rho) < rho ?")
    worst, at = -np.inf, None
    for t in np.linspace(0.05, 3.50, 40):
        for r in np.linspace(0.01, 0.999, 60):
            d = phi_from_rho(r, t) - r
            if d > worst:
                worst, at = d, (t, r)
    print(
        f"    homogeneous:   max (phi - rho) = {worst:+.6f} at t={at[0]:.3f} rho={at[1]:.3f}"
    )

    worst_h, at_h = -np.inf, None
    for t_e in np.linspace(0.1, 2.5, 12):
        for t_f in np.linspace(0.1, 2.5, 12):
            for r in np.linspace(0.05, 0.99, 20):
                d = phi_from_rho(r, t_e, t_f) - r
                if d > worst_h:
                    worst_h, at_h = d, (t_e, t_f, r)
    print(
        f"    heterogeneous: max (phi - rho) = {worst_h:+.6f} "
        f"at t_e={at_h[0]:.2f} t_f={at_h[1]:.2f} rho={at_h[2]:.2f}"
    )
    return worst < 0 and worst_h < 0


def check_difficulty(rng):
    """RADIAL: shared item difficulty puts a positive floor under phi at rho=0."""
    print("\nR1  SHARED ITEM DIFFICULTY: phi(rho=0) = Var_T(q(T)) / (q(1-q))")
    print(f"    {'spread':>8} {'q_bar':>8} {'phi(0) direct':>15} {'Var/q(1-q)':>12}")
    ok = True
    for spread in (0.0, 0.10, 0.25, 0.50):
        ts = 0.674 * np.exp(rng.normal(0.0, spread, size=200_000))
        qs = q_of_t(ts)
        q_bar = float(qs.mean())
        direct = float((qs**2).mean() - q_bar**2) / (q_bar * (1 - q_bar))
        decomp = float(qs.var()) / (q_bar * (1 - q_bar))
        ok &= abs(direct - decomp) < 1e-9 and (spread == 0.0 or direct > 0)
        print(f"    {spread:>8.2f} {q_bar:>8.4f} {direct:>15.6f} {decomp:>12.6f}")
    return ok


def check_panel_recovery(rng):
    """PANEL: does the pairwise map reproduce a k-evaluator panel's error phi?

    The checks above are pairwise and analytic. This one simulates a whole
    k = 9 panel under the map's own model (Gaussian isotropic deviations),
    measures phi on the binary miss indicators exactly as Kohli does, and
    compares against the map applied PAIRWISE and then averaged.

    It also reports the map applied to the AVERAGE correlation, which is the
    tempting shortcut and is wrong: by M4 the map is convex at low rho, so
    Jensen makes map-of-mean understate mean-of-map. The estimator must map
    each pair and then average.
    """
    print("\nP1  PANEL RECOVERY under the map's own model (Gaussian deviations)")
    print(
        f"    {'n':>4} {'rho':>5} {'phi_geom':>9} {'phi_err':>9} "
        f"{'mapOfMean':>10} {'meanOfMap':>10} {'resid':>8}"
    )
    k, n_dev, tau = K_KOHLI, 400_000, 0.30
    worst_resid, worst_jensen = 0.0, 0.0
    for n_dim in (10, 40):
        for rho in (0.0, 0.2, 0.5, 0.9):
            shared = rng.normal(size=n_dim)
            shared /= np.linalg.norm(shared)
            idio = rng.normal(size=(k, n_dim))
            idio /= np.linalg.norm(idio, axis=1, keepdims=True)
            v = np.sqrt(rho) * shared + np.sqrt(1 - rho) * idio
            v /= np.linalg.norm(v, axis=1, keepdims=True)

            iu = np.triu_indices(k, 1)
            rho_ij = np.abs((v @ v.T)[iu])

            d = rng.normal(size=(n_dev, n_dim)) / np.sqrt(n_dim)
            miss = (np.abs(d @ v.T) <= tau * np.sqrt(10.0 / n_dim)).astype(np.float64)
            q = miss.mean(axis=0)
            joint = (miss.T @ miss) / n_dev
            phi_mat = (joint - np.outer(q, q)) / np.sqrt(
                np.outer(q * (1 - q), q * (1 - q))
            )
            phi_err = float(np.mean(phi_mat[iu]))

            t = t_of_q(float(q.mean()))
            map_of_mean = phi_from_rho(float(rho_ij.mean()), t)
            mean_of_map = float(np.mean([phi_from_rho(x, t) for x in rho_ij]))
            worst_resid = max(worst_resid, abs(phi_err - mean_of_map))
            worst_jensen = max(worst_jensen, abs(mean_of_map - map_of_mean))
            print(
                f"    {n_dim:>4} {rho:>5.2f} {rho_ij.mean():>9.3f} {phi_err:>9.4f} "
                f"{map_of_mean:>10.4f} {mean_of_map:>10.4f} "
                f"{phi_err - mean_of_map:>+8.4f}"
            )
    print(f"    max |phi_err - meanOfMap| = {worst_resid:.4f}   (map is exact)")
    print(
        f"    max |meanOfMap - mapOfMean| = {worst_jensen:.4f}   (Jensen; map pairwise)"
    )
    return worst_resid < 2e-3


# --------------------------------------------------------------------------
# what the map does to Kohli's numbers
# --------------------------------------------------------------------------
def kohli_inversion():
    """The consequence: n_eff on error vectors bounds verification bandwidth."""
    print("\nINVERSION — geometric correlation implied by Kohli's reported phi")
    print(
        "  (q = the panel's marginal error rate; observable, so the map is identified)"
    )
    hdr = (
        f"    {'condition':<24} {'phi':>6} {'q':>6} {'rho':>7} "
        f"{'n_eff_vote':>11} {'n_eff_rank':>11}"
    )
    print(hdr)
    print("    " + "-" * (len(hdr) - 4))
    rows = []
    for label, phi in KOHLI_PHI.items():
        n_vote = kish(K_KOHLI, phi)
        for q in (0.10, 0.25, 0.50, 0.68):
            rho = rho_from_phi(phi, t_of_q(q))
            n_rank = kish(K_KOHLI, rho)
            rows.append((label, phi, q, rho, n_vote, n_rank))
            shown = label if q == 0.10 else ""
            print(
                f"    {shown:<24} {phi if q == 0.10 else float('nan'):>6.3f} "
                f"{q:>6.2f} {rho:>7.4f} {n_vote:>11.2f} {n_rank:>11.2f}".replace(
                    "   nan", "     "
                )
            )
    return rows


# --------------------------------------------------------------------------
# figure
# --------------------------------------------------------------------------
def make_figure(path):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    rhos = np.linspace(0.0, 0.999, 220)
    qs = (0.10, 0.25, 0.50, 0.68)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.6))

    ax1.plot([0, 1], [0, 1], color="0.6", lw=1.0, ls="--", label="identity")
    for q in qs:
        t = t_of_q(q)
        ax1.plot(rhos, [phi_from_rho(r, t) for r in rhos], lw=1.8, label=f"q = {q:.2f}")
    ax1.set_xlabel(r"geometric correlation $\rho = |\langle v_e, v_f \rangle|$")
    ax1.set_ylabel(r"induced error correlation $\phi$")
    ax1.set_title("The map is strictly increasing and strictly attenuating")
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.legend(fontsize=8, loc="upper left")
    ax1.grid(alpha=0.25)

    for q in qs:
        t = t_of_q(q)
        ax2.plot(
            [kish(K_KOHLI, phi_from_rho(r, t)) for r in rhos],
            [kish(K_KOHLI, r) for r in rhos],
            lw=1.8,
            label=f"q = {q:.2f}",
        )
    ax2.plot([1, K_KOHLI], [1, K_KOHLI], color="0.6", lw=1.0, ls="--", label="identity")
    n_obs = [kish(K_KOHLI, p) for p in KOHLI_PHI.values()]
    ax2.axvspan(
        min(n_obs),
        max(n_obs),
        color="0.5",
        alpha=0.18,
        lw=0,
        label=f"Kohli's reported range ({min(n_obs):.2f}-{max(n_obs):.2f})",
    )
    ax2.set_xlabel(r"$n_{eff}$ from error vectors (Kohli's estimator)")
    ax2.set_ylabel(r"$n_{eff}$ from inspection directions (bandwidth)")
    ax2.set_title(f"Measured $n_{{eff}}$ bounds bandwidth from above ($k = {K_KOHLI}$)")
    ax2.set_xlim(1, K_KOHLI)
    ax2.set_ylim(1, K_KOHLI)
    ax2.legend(fontsize=8, loc="upper left")
    ax2.grid(alpha=0.25)

    fig.tight_layout()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, dpi=170)
    print(f"\nfigure -> output/figures/{os.path.basename(path)}")


def main():
    rng = np.random.default_rng(SEED)
    print(f"phi mapping.  seed={SEED}  GL nodes={N_GL}\n")

    results = {
        "C1 quadrature": check_quadrature(rng),
        "M1 even": check_even(),
        "M2 monotone": check_monotone(),
        "M3 endpoints": check_endpoints(),
        "M4 quadratic": check_quadratic(),
        "M5 attenuation": check_attenuation(),
        "R1 difficulty": check_difficulty(rng),
        "P1 panel recovery": check_panel_recovery(rng),
    }
    kohli_inversion()

    here = os.path.dirname(os.path.abspath(__file__))
    make_figure(os.path.join(here, "..", "output", "figures", "phi_mapping.png"))

    print("\nVERDICT")
    for name, ok in results.items():
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    all_ok = all(results.values())
    print(
        "\n  => "
        + (
            "SURVIVES: the map is exact, even in rho, strictly monotone, and\n"
            "     strictly attenuating, with fixed endpoints — so it is invertible\n"
            "     given the observed marginal error rate, and Kish n_eff on error\n"
            "     vectors is an upper bound on verification bandwidth regardless.\n"
            "     The design-effect reading holds."
            if all_ok
            else "CHECK FAILED — see above."
        )
    )
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
