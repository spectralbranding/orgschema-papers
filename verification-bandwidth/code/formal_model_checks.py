"""Numerical checks on the paper's formal propositions.

The propositions are stated and proved in the paper. This script does not prove
anything; it checks that each proved statement is not contradicted by simulation,
and supplies the numbers the paper quotes. A FAIL here means a proof is wrong,
not that the simulation is.

  P1  BRACKET.     For any panel rule f with f(0..0)=0 and f(1..1)=1,
                   AND <= f <= OR pointwise, hence in detection probability for
                   every deviation distribution. Checked against random
                   weighted-threshold rules and random general monotone rules.

  P2  COLLAPSE.    Bracket width W = P(OR) - P(AND) = P(the panel disagrees),
                   and W <= 2(k-1) p(1-p) (1 - phibar_err), which vanishes as
                   phibar_err -> 1. Checked on a correlation sweep; the bound is
                   informative (below 1) only in the collapse regime, which is
                   where the claim lives.

  P3  CEILING.     n_eff <= min(k, n) EXACTLY, for every configuration of unit
                   inspection directions, via a Frobenius bound on the frame
                   operator. Typical case is far tighter: randomly oriented
                   evaluators saturate at 1/E|<u,v>| = sqrt(pi) Gamma((n+1)/2) /
                   Gamma(n/2) ~ sqrt(pi n / 2), not at n.

  P4  TRANSFER.    Transferable share of an r-condition acceptance contract is
                   at most min(n_eff, r)/r. Illustrated, not tested: it is a
                   definition plus P3.

  P5  ESTIMATOR.   Proved and checked in phi_mapping.py (8 checks); not
                   repeated here.

Run: uv run --with numpy --with scipy python formal_model_checks.py
Seed 20260811. Runtime ~40 s.
"""

from __future__ import annotations

import itertools

import numpy as np
from scipy.special import gammaln

SEED = 20260811
N_DEV = 200_000


# --------------------------------------------------------------------------
# shared panel machinery (same model as threat1_kill_test.py)
# --------------------------------------------------------------------------
def evaluator_directions(rng, k, n, rho):
    """k unit vectors with expected pairwise correlation ~rho (shared factor)."""
    shared = rng.normal(size=n)
    shared /= np.linalg.norm(shared)
    idio = rng.normal(size=(k, n))
    idio /= np.linalg.norm(idio, axis=1, keepdims=True)
    v = np.sqrt(rho) * shared + np.sqrt(1.0 - rho) * idio
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def panel_detections(rng, v, tau, n_dev=N_DEV):
    """Boolean (n_dev, k): evaluator e detects deviation d iff |<v_e,d>| > tau."""
    n = v.shape[1]
    d = rng.normal(size=(n_dev, n))
    d /= np.linalg.norm(d, axis=1, keepdims=True)
    return np.abs(d @ v.T) > tau


def mean_pairwise_phi(indicator):
    """Mean pairwise phi coefficient across columns of a boolean array."""
    k = indicator.shape[1]
    a = indicator.astype(np.float64)
    p = a.mean(axis=0)
    joint = (a.T @ a) / a.shape[0]
    denom = np.sqrt(np.outer(p * (1 - p), p * (1 - p)))
    iu = np.triu_indices(k, 1)
    return float(np.mean(((joint - np.outer(p, p)) / denom)[iu])), float(p.mean())


def kish(k, phi_bar):
    return k / (1.0 + (k - 1) * phi_bar)


# --------------------------------------------------------------------------
# P1 — the bracket
# --------------------------------------------------------------------------
def random_threshold_rule(rng, k):
    """A random weighted-threshold (hence monotone) rule; AND/OR/MAJ are cases."""
    w = rng.uniform(0.1, 1.0, size=k)
    theta = rng.uniform(0.05, 0.95) * w.sum()
    return lambda s: (s @ w) > theta


def random_monotone_rule(rng, k):
    """A random general monotone rule: upward closure of a random seed set.

    Both boundary conditions are enforced, and they do real work. f(1..1)=1
    needs a seed (the all-ones row). f(0..0)=0 needs EVERY seed to be non-empty:
    an all-zeros seed would make f identically 1, which is monotone but violates
    P1's hypothesis -- and the bracket genuinely fails for such a rule. An
    earlier version of this generator omitted that filter and P1 failed its own
    check, which is the intended behaviour of the check.
    """
    n_seed = int(rng.integers(1, 5))
    seeds = rng.integers(0, 2, size=(n_seed, k)).astype(bool)
    empty = ~seeds.any(axis=1)
    if empty.any():  # repair all-zero seeds by lighting one random coordinate
        seeds[empty, rng.integers(0, k, size=int(empty.sum()))] = True
    seeds[0] = True  # guarantees f(1..1) = 1
    return lambda s: np.any(np.all(s[:, None, :] >= seeds[None, :, :], axis=2), axis=1)


def check_p1(rng):
    """AND <= f <= OR, pointwise on all 2^k inputs and in detection probability."""
    print("P1  BRACKET")
    k = 5
    all_inputs = np.array(list(itertools.product([False, True], repeat=k)))
    pointwise_ok = True
    for _ in range(400):
        f = (
            random_threshold_rule(rng, k)
            if rng.random() < 0.5
            else random_monotone_rule(rng, k)
        )
        out = np.asarray(f(all_inputs), dtype=bool)
        and_v = all_inputs.all(axis=1)
        or_v = all_inputs.any(axis=1)
        if not (out[and_v].all() and not out[~or_v].any()):
            pointwise_ok = False
        pointwise_ok &= bool(np.all(out >= and_v) and np.all(out <= or_v))
    print(
        f"    pointwise AND <= f <= OR over 400 random rules, all 2^{k} inputs: {pointwise_ok}"
    )

    print(
        f"    {'rho':>6} {'P(AND)':>8} {'min f':>8} {'max f':>8} {'P(OR)':>8} {'inside':>8}"
    )
    prob_ok = True
    for rho in (0.0, 0.4, 0.8):
        v = evaluator_directions(rng, k, 10, rho)
        seen = panel_detections(rng, v, 0.30)
        p_and = float(seen.all(axis=1).mean())
        p_or = float(seen.any(axis=1).mean())
        rates = []
        for _ in range(60):
            f = (
                random_threshold_rule(rng, k)
                if rng.random() < 0.5
                else random_monotone_rule(rng, k)
            )
            rates.append(float(np.asarray(f(seen), dtype=bool).mean()))
        lo, hi = min(rates), max(rates)
        inside = (lo >= p_and - 1e-12) and (hi <= p_or + 1e-12)
        prob_ok &= inside
        print(
            f"    {rho:>6.2f} {p_and:>8.3f} {lo:>8.3f} {hi:>8.3f} {p_or:>8.3f} {str(inside):>8}"
        )
    return pointwise_ok and prob_ok


# --------------------------------------------------------------------------
# P2 — the collapse and its bound
# --------------------------------------------------------------------------
def check_p2(rng):
    """W = P(disagree) <= 2(k-1) p(1-p) (1 - phibar_err); W -> 0 as phi -> 1."""
    print("\nP2  COLLAPSE")
    k, n, tau = 9, 10, 0.30
    print(
        f"    {'rho':>6} {'phi_err':>8} {'p':>6} {'W obs':>7} {'bound':>8} "
        f"{'holds':>6} {'useful':>7}"
    )
    ok = True
    widths = []
    for rho in (0.0, 0.2, 0.5, 0.7, 0.9, 0.99, 0.999):
        v = evaluator_directions(rng, k, n, rho)
        seen = panel_detections(rng, v, tau)
        phi_err, p = mean_pairwise_phi(seen)
        w = float(seen.any(axis=1).mean() - seen.all(axis=1).mean())
        bound = 2 * (k - 1) * p * (1 - p) * (1 - phi_err)
        holds = w <= bound + 1e-9
        ok &= holds
        widths.append(w)
        print(
            f"    {rho:>6.3f} {phi_err:>8.3f} {p:>6.3f} {w:>7.3f} {bound:>8.3f} "
            f"{str(holds):>6} {str(bound < 1.0):>7}"
        )
    print(
        f"    bracket width falls {widths[0]:.3f} -> {widths[-1]:.3f}: {widths[-1] < widths[0]}"
    )

    # exact endpoint: perfectly correlated evaluators have zero bracket
    v = np.repeat(evaluator_directions(rng, 1, n, 0.0), k, axis=0)
    seen = panel_detections(rng, v, tau)
    w_exact = float(seen.any(axis=1).mean() - seen.all(axis=1).mean())
    print(f"    identical evaluators (phi = 1): W = {w_exact:.6f}  (exactly 0)")
    return ok and w_exact == 0.0


# --------------------------------------------------------------------------
# P3 — the dimensional ceiling
# --------------------------------------------------------------------------
def expected_abs_inner(n):
    """E|<u,v>| for independent uniform unit vectors: Gamma(n/2)/(sqrt(pi)Gamma((n+1)/2))."""
    return float(np.exp(gammaln(n / 2) - 0.5 * np.log(np.pi) - gammaln((n + 1) / 2)))


def check_p3(rng):
    """n_eff <= min(k, n) exactly; typical case saturates near sqrt(pi n / 2)."""
    print("\nP3  DIMENSIONAL CEILING")
    print("    hard bound: n_eff <= min(k, n) for EVERY configuration")
    print(
        f"    {'n':>4} {'k':>5} {'phibar':>8} {'n_eff':>7} {'min(k,n)':>9} {'holds':>6}"
    )
    ok = True
    for n, k in ((10, 5), (10, 9), (10, 40), (10, 200), (4, 50), (25, 200)):
        worst, worst_phi = -np.inf, np.nan
        for _ in range(30):
            # sweep configurations: random, near-orthogonal, and clustered
            mode = rng.integers(0, 3)
            if mode == 0:
                v = evaluator_directions(rng, k, n, 0.0)
            elif mode == 1:
                base = np.linalg.qr(rng.normal(size=(n, n)))[0]
                v = base[rng.integers(0, n, size=k)]
                v = v + 0.02 * rng.normal(size=(k, n))
                v /= np.linalg.norm(v, axis=1, keepdims=True)
            else:
                v = evaluator_directions(rng, k, n, float(rng.uniform(0, 0.9)))
            iu = np.triu_indices(k, 1)
            phi = float(np.mean(np.abs((v @ v.T)[iu])))
            if kish(k, phi) > worst:
                worst, worst_phi = kish(k, phi), phi
        holds = worst <= min(k, n) + 1e-9
        ok &= holds
        print(
            f"    {n:>4} {k:>5} {worst_phi:>8.3f} {worst:>7.3f} {min(k, n):>9} {str(holds):>6}"
        )

    print("\n    typical case: randomly oriented evaluators, k -> infinity")
    print(
        f"    {'n':>4} {'E|<u,v>|':>10} {'exact lim':>10} {'sqrt(pi n/2)':>13} {'n_eff k=200':>12}"
    )
    for n in (4, 10, 25, 48, 100):
        e_abs = expected_abs_inner(n)
        v = evaluator_directions(rng, 200, n, 0.0)
        iu = np.triu_indices(200, 1)
        phi = float(np.mean(np.abs((v @ v.T)[iu])))
        print(
            f"    {n:>4} {e_abs:>10.4f} {1/e_abs:>10.3f} {np.sqrt(np.pi*n/2):>13.3f} "
            f"{kish(200, phi):>12.3f}"
        )
    return ok


# --------------------------------------------------------------------------
# P4 — the executor-invariance ceiling
# --------------------------------------------------------------------------
def check_p4():
    """Transferable share of an r-condition contract is at most min(n_eff, r)/r."""
    print(
        "\nP4  EXECUTOR-INVARIANCE CEILING (illustration; P4 is a definition plus P3)"
    )
    print("    OST cascade L0-L2 contract on the 8x6 = 48-dim specification space.")
    print(
        f"    {'r':>4} {'k':>5} {'phibar':>8} {'n_eff':>7} {'transferable':>13} {'residual':>9}"
    )
    for r, k, phi in (
        (6, 3, 0.35),
        (6, 9, 0.39),
        (16, 9, 0.39),
        (16, 40, 0.39),
        (48, 200, 0.25),
    ):
        ne = kish(k, phi)
        share = min(ne, r) / r
        print(
            f"    {r:>4} {k:>5} {phi:>8.2f} {ne:>7.2f} {share:>12.1%} {1 - share:>8.1%}"
        )
    print("    The residual column is the share of the stated contract that the")
    print("    receiving panel cannot independently check -- the signatory's remit.")
    return True


def main():
    rng = np.random.default_rng(SEED)
    print(f"formal-model checks.  seed={SEED}  deviations per panel={N_DEV:,}\n")
    results = {
        "P1 bracket": check_p1(rng),
        "P2 collapse": check_p2(rng),
        "P3 ceiling": check_p3(rng),
        "P4 transfer": check_p4(),
    }
    print("\nVERDICT")
    for name, ok in results.items():
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    print("  ----  P5 estimator: proved and checked in phi_mapping.py")
    all_ok = all(results.values())
    print(
        "\n  => "
        + (
            "No proposition is contradicted by simulation."
            if all_ok
            else "A PROOF IS WRONG -- a proposition failed its own check."
        )
    )
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
