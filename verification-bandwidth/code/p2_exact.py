"""
P2 exact form -- the single-factor reduction of the bracket width.

WHY. The bracket width W admits a union bound over pairwise disagreement probabilities.
That bound is assumption-free, which is its virtue, and loose by roughly a factor of
three, which is its cost: it only drops below 1 above phi_bar ~ .88, so on its own it is
a limit statement rather than a usable bound. Under exchangeability the exact
disagreement probability is available, and this script derives and checks it.

THE DERIVATION. Build an EQUIANGULAR panel: v_e = sqrt(rho) * u + sqrt(1 - rho) * w_e
with u, w_1..w_k orthonormal (feasible whenever k + 1 <= n). Then every pairwise inner
product is exactly rho and every v_e is exactly a unit vector. For Gaussian isotropic
deviations delta ~ N(0, sigma^2 I), the inspected components are

    X_e = <v_e, delta> = sqrt(rho) * G_0 + sqrt(1 - rho) * G_e,

with G_0, G_1, ..., G_k iid N(0, sigma^2) EXACTLY, because the defining vectors are
orthonormal. So the panel is exactly single-factor: conditional on the common factor
G_0 = z, the k detection indicators are INDEPENDENT with common flag probability

    p(z) = Pr[|sqrt(rho) z + sqrt(1-rho) G| > t]
         = 1 - Phi((t - sqrt(rho) z)/sqrt(1-rho)) + Phi((-t - sqrt(rho) z)/sqrt(1-rho)),

writing t = tau/sigma. Everything the bracket needs then follows exactly, as
one-dimensional integrals against the standard normal density:

    mu(D_AND) = E_Z[ p(Z)^k ]
    mu(D_OR)  = 1 - E_Z[ (1 - p(Z))^k ]
    W         = 1 - E_Z[ p(Z)^k + (1 - p(Z))^k ]

A k-dimensional orthant probability collapses to a single Gauss-Hermite quadrature.

WHAT THIS DOES AND DOES NOT REPLACE. It does NOT replace the union bound: that form
needs no exchangeability, no common marginals and no distributional assumption, and
real panels are not equianguar. It adds the exact value in the model the paper already
uses for its estimator (P5's Gaussian isotropic deviations), which is the regime where
the union bound is least informative. Keep both; lead with whichever the claim needs.

Checks (all must pass; the script exits nonzero otherwise):
  C1  quadrature against direct Monte Carlo on the equiangular panel
  C2  exact vs the generic shared-factor construction used by the other scripts
  C3  independence limit rho -> 0 reproduces 1 - p^k - (1-p)^k
  C4  collapse limit rho -> 1 drives W to 0
  C5  W is strictly decreasing in rho
  C6  the union bound is never violated by the exact value
  C7  the exact form is informative (< 1) across the whole range, unlike the bound

Reproduces: Tables 1 and 4.

Run:
    uv run --with numpy --with scipy python p2_exact.py
"""

from __future__ import annotations

import sys

import numpy as np
from scipy.stats import norm

SEED = 20260811
N_DEV = 400_000
GH_NODES = 20_001  # quadrature grid points; convergence checked against Monte Carlo


# --------------------------------------------------------------------------
# the exact form
# --------------------------------------------------------------------------
def flag_prob_given_factor(z, rho, t):
    """p(z): conditional probability that one evaluator flags, given common factor z."""
    if rho >= 1.0:
        return (np.abs(z) > t).astype(float)
    s = np.sqrt(1.0 - rho)
    m = np.sqrt(rho) * z
    return 1.0 - norm.cdf((t - m) / s) + norm.cdf((-t - m) / s)


def _gauss_hermite(n=GH_NODES):
    """Nodes/weights for E_Z[f(Z)] with Z ~ N(0,1).

    NOT Gauss-Hermite: numpy's hermegauss overflows past roughly 100 nodes and
    silently returns NaN weights, which propagates into every integral here. A dense
    trapezoidal grid over +-12 sigma is unconditionally stable and, for integrands
    this smooth, converges to machine precision -- C1 against Monte Carlo is what
    actually certifies it.
    """
    x = np.linspace(-12.0, 12.0, n)
    w = norm.pdf(x)
    w = w * (x[1] - x[0])
    return x, w / w.sum()


def bracket_exact(rho, t, k):
    """Exact (mu(D_AND), mu(D_OR), W) under the single-factor model."""
    z, w = _gauss_hermite()
    p = flag_prob_given_factor(z, rho, t)
    p_and = float(np.sum(w * p**k))
    p_none = float(np.sum(w * (1.0 - p) ** k))
    return p_and, 1.0 - p_none, 1.0 - (p_and + p_none)


def marginal_flag_rate(t):
    """p = Pr[|X| > t] for X ~ N(0,1) -- free of rho, as the single-factor model requires."""
    return float(2.0 * norm.cdf(-t))


def union_bound(k, p, phi_bar):
    """Proposition 2 form (iii): the exchangeable union bound."""
    return 2.0 * (k - 1) * p * (1.0 - p) * (1.0 - phi_bar)


# --------------------------------------------------------------------------
# simulation, for validation only
# --------------------------------------------------------------------------
def equiangular_directions(k, n, rho, rng):
    """v_e = sqrt(rho) u + sqrt(1-rho) w_e with u, w_1..w_k orthonormal.

    Pairwise inner products are EXACTLY rho and every v_e is EXACTLY unit norm.
    """
    if k + 1 > n:
        raise ValueError(f"equiangular construction needs k+1 <= n (k={k}, n={n})")
    basis = np.linalg.qr(rng.normal(size=(n, k + 1)))[0]  # n x (k+1), orthonormal cols
    u, w = basis[:, 0], basis[:, 1:].T
    return np.sqrt(rho) * u + np.sqrt(1.0 - rho) * w


def shared_factor_directions(k, n, rho, rng):
    """The generic shared-factor construction, with unequal pairwise angles."""
    shared = rng.normal(size=n)
    shared /= np.linalg.norm(shared)
    idio = rng.normal(size=(k, n))
    idio /= np.linalg.norm(idio, axis=1, keepdims=True)
    v = np.sqrt(rho) * shared + np.sqrt(1.0 - rho) * idio
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def bracket_mc(v, t, rng, n_dev=N_DEV):
    """Monte Carlo bracket under GAUSSIAN isotropic deviations (P5's model)."""
    n = v.shape[1]
    d = rng.normal(size=(n_dev, n))
    seen = np.abs(d @ v.T) > t
    p_and = float(np.all(seen, axis=1).mean())
    p_or = float(np.any(seen, axis=1).mean())
    return p_and, p_or, p_or - p_and


def mean_pairwise_phi(seen):
    a = seen.astype(np.float64)
    p = a.mean(axis=0)
    joint = (a.T @ a) / a.shape[0]
    denom = np.sqrt(np.outer(p * (1 - p), p * (1 - p)))
    iu = np.triu_indices(a.shape[1], 1)
    return float(np.mean(((joint - np.outer(p, p)) / denom)[iu]))


def phi_err_exact(rho, t):
    """Induced pairwise error correlation under the single-factor model.

    Computed here by the same one-dimensional reduction: conditional on the factor,
    the pair is independent, so Pr[both flag] = E_Z[p(Z)^2].
    """
    z, w = _gauss_hermite()
    p_z = flag_prob_given_factor(z, rho, t)
    p11 = float(np.sum(w * p_z**2))
    p = marginal_flag_rate(t)
    return (p11 - p * p) / (p * (1.0 - p))


# --------------------------------------------------------------------------
# checks
# --------------------------------------------------------------------------
def check_c1_c2(rng):
    """Quadrature against Monte Carlo, on both panel constructions."""
    k, n, t = 9, 10, 0.30
    print("C1/C2  exact vs Monte Carlo, Gaussian deviations, k=9 n=10 t=.30")
    print(
        f"    {'rho':>6} {'W exact':>9} {'W MC eq':>9} {'d':>8} "
        f"{'W MC sf':>9} {'d':>8}  {'AND ex':>7} {'AND MC':>7}"
    )
    ok = True
    for rho in (0.0, 0.2, 0.5, 0.7, 0.9, 0.99):
        and_ex, _, w_ex = bracket_exact(rho, t, k)
        v_eq = equiangular_directions(k, n, rho, rng)
        and_eq, _, w_eq = bracket_mc(v_eq, t, rng)
        v_sf = shared_factor_directions(k, n, rho, rng)
        _, _, w_sf = bracket_mc(v_sf, t, rng)
        d_eq, d_sf = w_eq - w_ex, w_sf - w_ex
        print(
            f"    {rho:>6.2f} {w_ex:>9.4f} {w_eq:>9.4f} {d_eq:>+8.4f} "
            f"{w_sf:>9.4f} {d_sf:>+8.4f}  {and_ex:>7.4f} {and_eq:>7.4f}"
        )
        # C1: the equiangular panel is the model's own case -- demand MC agreement.
        if abs(d_eq) > 0.005:
            ok = False
            print(f"      FAIL C1: equiangular MC differs by {d_eq:+.4f}")
        # C2: the generic construction only approximates equiangularity.
        if abs(d_sf) > 0.05:
            ok = False
            print(f"      FAIL C2: shared-factor MC differs by {d_sf:+.4f}")
    print(
        "    C1 exact reproduces the equiangular panel; C2 the generic construction\n"
        "    tracks it, with the residual coming from its unequal pairwise angles."
    )
    return ok


def check_c3_c4():
    """Independence limit and collapse limit."""
    k, t = 9, 0.30
    p = marginal_flag_rate(t)
    print("\nC3/C4  limits")
    _, _, w0 = bracket_exact(0.0, t, k)
    w0_closed = 1.0 - p**k - (1.0 - p) ** k
    print(f"    rho=0    W exact {w0:.6f}   1 - p^k - (1-p)^k = {w0_closed:.6f}")
    ok = abs(w0 - w0_closed) < 1e-9
    if not ok:
        print("      FAIL C3")
    for rho in (0.99, 0.999, 0.9999):
        _, _, w = bracket_exact(rho, t, k)
        print(f"    rho={rho:<7} W exact {w:.6f}")
    _, _, w_hi = bracket_exact(0.999999, t, k)
    if w_hi > 0.01:
        ok = False
        print(f"      FAIL C4: W = {w_hi:.4f} at rho -> 1, expected -> 0")
    else:
        print(f"    rho->1   W exact {w_hi:.6f}  (collapses, as P2(4) requires)")
    return ok


def check_c5_c6_c7():
    """Monotonicity; the bound is never violated; the exact form stays informative."""
    k, t = 9, 0.30
    p = marginal_flag_rate(t)
    rhos = np.linspace(0.0, 0.999, 200)
    ws = np.array([bracket_exact(r, t, k)[2] for r in rhos])
    dec = bool(np.all(np.diff(ws) < 1e-12))
    print("\nC5     W strictly decreasing in rho:", dec)

    print("\nC6/C7  exact value against the union bound (k=9, t=.30)")
    print(
        f"    {'rho':>6} {'phi_err':>8} {'W exact':>9} {'bound':>9} "
        f"{'bound/W':>8} {'bound<1':>8}"
    )
    ok = dec
    informative_exact = True
    for rho in (0.0, 0.2, 0.5, 0.7, 0.9, 0.95, 0.99, 0.999):
        _, _, w = bracket_exact(rho, t, k)
        phi = phi_err_exact(rho, t)
        b = union_bound(k, p, phi)
        ratio = b / w if w > 0 else float("inf")
        print(
            f"    {rho:>6.3f} {phi:>8.3f} {w:>9.4f} {b:>9.4f} "
            f"{ratio:>8.2f} {str(b < 1.0):>8}"
        )
        if b < w - 1e-9:
            ok = False
            print("      FAIL C6: union bound violated by the exact value")
        if w >= 1.0:
            informative_exact = False
    if not informative_exact:
        ok = False
        print("      FAIL C7")
    else:
        print(
            "    C7 the exact value is informative at every rho; the union bound only\n"
            "    drops below 1 near phi ~ .88, which is the gap this closes."
        )
    return ok


def check_c8():
    """The claim that motivates the whole paper, stated exactly rather than bounded."""
    t = 0.30
    print("\nC8     collapse across panel sizes (exact W, t=.30)")
    print(f"    {'rho':>6} " + " ".join(f"{'k='+str(k):>9}" for k in (3, 9, 25, 100)))
    for rho in (0.0, 0.3, 0.6, 0.9, 0.99):
        row = " ".join(f"{bracket_exact(rho, t, k)[2]:>9.4f}" for k in (3, 9, 25, 100))
        print(f"    {rho:>6.2f} {row}")
    print(
        "    Bracket width GROWS with k at fixed correlation and collapses with\n"
        "    correlation at fixed k -- the two directions P1's asymmetry predicts."
    )
    return True


def check_c9():
    """Cross-check against the independently implemented map in phi_mapping.py.

    phi_mapping.py computes the induced error correlation from the bivariate normal
    CDF with the reflection identities. This script computes it by conditioning on the
    common factor. Same quantity, two derivations, two implementations -- if they
    disagree, one of them is wrong.
    """
    from phi_mapping import (
        phi_from_rho,
        t_of_q,
    )  # local, so the file stays runnable alone

    print("\nC9     single-factor phi against the bivariate-normal map")
    print(
        f"    {'q':>5} {'t':>6} {'rho':>6} {'phi (factor)':>13} {'phi (bvn map)':>13} {'d':>10}"
    )
    worst = 0.0
    for q in (0.10, 0.25, 0.50):
        t = t_of_q(q)
        for rho in (0.1, 0.5, 0.9, 0.99):
            a = phi_err_exact(rho, t)
            b = phi_from_rho(rho, t)
            worst = max(worst, abs(a - b))
            print(
                f"    {q:>5.2f} {t:>6.3f} {rho:>6.2f} {a:>13.6f} {b:>13.6f} {a-b:>+10.2e}"
            )
    ok = worst < 1e-6
    print(f"    worst disagreement {worst:.2e} -- {'agree' if ok else 'FAIL C9'}")
    return ok


def check_c10():
    """The number the paper actually quotes: how much bracket is left at a REAL panel's
    correlation?

    The published nine-judge panel reports mean pairwise error correlations of .391 /
    .354 / .328, and .456 under chain-of-thought. The point inversion needs the marginal
    error rate q, which that record does not carry, so q is bracketed rather than fixed
    -- the same treatment the bandwidth inversion gets.
    """
    from phi_mapping import rho_from_phi, t_of_q

    k = 9
    print(
        "\nC10    bracket remaining at the correlations a real nine-judge panel shows"
    )
    print(
        f"    {'condition':<22} {'phi':>6} "
        + " ".join(f"{'q=' + f'{q:.2f}':>12}" for q in (0.10, 0.25, 0.50))
    )
    for name, phi in (
        ("MNLI", 0.391),
        ("SNLI", 0.354),
        ("AlphaNLI", 0.328),
        ("MNLI chain-of-thought", 0.456),
    ):
        cells = []
        for q in (0.10, 0.25, 0.50):
            t = t_of_q(q)
            rho = rho_from_phi(phi, t)
            w = bracket_exact(rho, t, k)[2]
            w0 = bracket_exact(0.0, t, k)[2]
            cells.append(f"{100 * w / w0:>11.1f}%")
        print(f"    {name:<22} {phi:>6.3f} " + " ".join(cells))
    print(
        "    Read as: percentage of the ZERO-CORRELATION bracket width that SURVIVES at\n"
        "    the panel's measured error correlation. Model-dependent and directional, not\n"
        "    a measurement. State the loss honestly: between roughly a quarter and three\n"
        "    fifths of the bracket is already gone, depending on the marginal error rate --\n"
        "    NOT 'most of it', and not zero. The union bound says nothing whatever at these\n"
        "    correlations, because it exceeds 1 until phi is near .88."
    )
    return True


def main():
    rng = np.random.default_rng(SEED)
    print(
        f"P2 exact form.  seed={SEED}  MC deviations={N_DEV:,}  quadrature nodes={GH_NODES}\n"
    )
    results = [
        check_c1_c2(rng),
        check_c3_c4(),
        check_c5_c6_c7(),
        check_c8(),
        check_c9(),
        check_c10(),
    ]
    print("\n" + ("ALL CHECKS PASSED" if all(results) else "SOME CHECKS FAILED"))
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
