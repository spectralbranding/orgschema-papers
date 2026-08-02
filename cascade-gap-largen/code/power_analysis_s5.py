#!/usr/bin/env python3
"""S5 full-draw power / precision analysis -> the exact registered N.

Sizes the Stage-S5 case-control replication (PREREGISTRATION_V2.md Amendment 2) on
the NECESSARY-CONDITION / SAFE-HARBOR effect -- NOT on the sufficiency odds ratio
(Locked Decision 3: sufficiency is the fragile direction and is never headlined).

Two pre-registered precision targets drive N:

  (T1) SAFE-HARBOR precision. With inclusion by closing-time deal STRUCTURE (blind to
       outcome), the "no gap" cell is populated by the matched going-concern controls
       plus the gap-prone deals that carry no coded gap. The confirmatory quantity is
       P(fail | no gap) with an exact (Clopper-Pearson) upper 95% bound. Target: the
       expected exact upper bound <= .05 (a "<1-in-20 no-gap deals fail on this mode"
       safe harbor), achieved with high probability across the plausible necessity-leak
       range.

  (T2) NECESSITY / NCA precision. The gap cell must be populated enough to estimate
       necessity consistency P(gap | fail) and the NCA ceiling. Target: 60-80 coded gap
       cases (the S5 pre-draft's sizing note), achieved with high probability.

Method: a fixed-seed Monte Carlo over the case-control draw. For a candidate design
(N_gap_prone gap-prone + N_control matched controls, 1:1) each replication draws the
coded gap indicator per stratum, then draws failures conditional on gap, then computes
the realized (T1) exact upper bound and (T2) gap count. We report, per candidate N, the
probability each target is met and the median realized upper bound, and recommend the
smallest N meeting both targets with probability >= .90 across the parameter grid.

Two distinct questions are kept separate (an earlier draft wrongly folded them):
  - T1 sizes PRECISION under the world where necessity HOLDS (leak ~ 0). There the
    safe harbor is real and we size n_nogap to certify it (exact upper 95% CI <= .05).
    Including a large "leak" in T1's worst case is a category error: at a true 4% leak
    the safe harbor genuinely does not hold and no feasible N drives the upper CI to
    <= .05 (it converges to .04 from ABOVE) -- that is a detection question, not a
    precision one.
  - T3 (reported, not a sizing veto) is the mirror: under a real necessity VIOLATION
    (leak .03-.05) what is the power to REJECT a false safe harbor (exact lower 95% CI
    on P(fail|no gap) > 0)? Larger n_nogap helps here too.

Parameter ranges (pilot-informed, deliberately conservative):
  p_gap | gap-prone stratum : .40 - .55  (pilot: carve-outs carried gaps; roll-ups split)
  p_gap | control stratum   : .02 - .06  (whole-company + acquirer-reporting screen makes
                                          a coded gap rare; residual RMT-like leakage only)
  P(fail | gap)             : .25 - .45  (the populated tail)
  P(fail | no gap) T1 (holds): .000 - .010  (necessity holds / near-holds -- sizes T1)
  P(fail | no gap) T3 (viol.): .03, .05     (necessity violated -- reported detection power)

Nothing here is a coded datum: this is a design-time simulation. Registered-before-data
is intact (no draw, no dossier, no coding call is performed by this script).

Run (fixed seed, reproducible; PAQS 37):
    uv run --with scipy python research/cascade-gap-largen/power_analysis_s5.py
    uv run --with scipy python research/cascade-gap-largen/power_analysis_s5.py --fixture
"""

from __future__ import annotations

import argparse
import sys

import numpy as np

try:
    from scipy.stats import beta as _beta
except Exception:  # pragma: no cover - scipy is provided via `uv run --with scipy`
    _beta = None

SEED = 20260729
N_REPS = 20000

# Pre-registered precision targets.
SAFE_HARBOR_UPPER_MAX = 0.05  # T1: exact upper 95% bound on P(fail | no gap)
GAP_CASES_MIN = 60  # T2 lower
GAP_CASES_MAX = 80  # T2 nominal upper (informational; not a veto)
TARGET_PROB = 0.90  # a design must meet each target with >= this probability

# Parameter grid (pilot-informed; conservative corners are what the design must survive).
P_GAP_PRONE = (0.40, 0.475, 0.55)
P_GAP_CONTROL = (0.02, 0.04, 0.06)
P_FAIL_GAP = (0.25, 0.35, 0.45)
P_FAIL_NOGAP_HOLDS = (0.000, 0.005, 0.010)  # T1 precision: necessity holds / near-holds
P_FAIL_NOGAP_VIOL = (0.03, 0.05)  # T3 detection: necessity violated (reported)

# Candidate designs: gap-prone count per arm (controls matched 1:1), so N = 2 * N_gp.
CANDIDATE_N_GAP_PRONE = (100, 120, 140, 150, 160, 175)


def clopper_pearson_upper(k: int, n: int, alpha: float = 0.05) -> float:
    """Exact one-sided (upper) Clopper-Pearson bound on a binomial proportion.

    Upper bound = BetaInv(1 - alpha; k + 1, n - k). At k = 0 this reduces to the
    familiar 1 - alpha**(1/n) ("rule of three" at alpha = .05).
    """
    if n == 0:
        return 1.0
    if k >= n:
        return 1.0
    if _beta is not None:
        return float(_beta.ppf(1.0 - alpha, k + 1, n - k))
    # Fallback for the k = 0 case only (exact), used if scipy is unavailable.
    if k == 0:
        return 1.0 - alpha ** (1.0 / n)
    raise RuntimeError("scipy required for Clopper-Pearson at k > 0")


def cp_upper_vec(k: np.ndarray, n: np.ndarray, alpha: float = 0.05) -> np.ndarray:
    """Vectorised Clopper-Pearson upper bound over arrays of (k, n).

    upper = BetaInv(1 - alpha; k + 1, n - k), with the k >= n and n == 0 edges set to 1.
    """
    if _beta is None:  # pragma: no cover - scipy provided via `uv run --with scipy`
        return np.array([clopper_pearson_upper(int(a), int(b)) for a, b in zip(k, n)])
    k = np.asarray(k)
    n = np.asarray(n)
    out = _beta.ppf(1.0 - alpha, k + 1, np.maximum(n - k, 1))
    out = np.where(n == 0, 1.0, out)
    out = np.where(k >= n, 1.0, out)
    return out


def cp_lower_vec(k: np.ndarray, n: np.ndarray, alpha: float = 0.05) -> np.ndarray:
    """Vectorised Clopper-Pearson LOWER bound over arrays of (k, n).

    lower = BetaInv(alpha; k, n - k + 1), with k == 0 -> 0 and n == 0 -> 0.
    Used for T3: a lower bound > 0 rejects the safe harbor.
    """
    if _beta is None:  # pragma: no cover
        raise RuntimeError("scipy required for the vectorised lower bound")
    k = np.asarray(k)
    n = np.asarray(n)
    out = _beta.ppf(alpha, np.maximum(k, 1), n - k + 1)
    out = np.where(k == 0, 0.0, out)
    out = np.where(n == 0, 0.0, out)
    return out


def simulate_point(
    n_gap_prone: int,
    n_control: int,
    p_gap_prone: float,
    p_gap_control: float,
    p_fail_nogap: float,
    rng: np.random.Generator,
    n_reps: int = N_REPS,
) -> dict:
    """Monte-Carlo one design at one parameter point (vectorised).

    Draws the coded-gap counts per stratum and the no-gap-cell failures, then computes
    the realized exact upper AND lower 95% CI on P(fail | no gap) and the gap count.
    (P(fail|gap) does not affect T1/T2/T3, so it is not drawn here.)
    """
    gaps_prone = rng.binomial(n_gap_prone, p_gap_prone, size=n_reps)
    gaps_control = rng.binomial(n_control, p_gap_control, size=n_reps)
    n_gap = gaps_prone + gaps_control
    n_total = n_gap_prone + n_control
    n_nogap = n_total - n_gap
    fail_nogap = rng.binomial(n_nogap, p_fail_nogap)

    uppers = cp_upper_vec(fail_nogap, n_nogap)
    lowers = cp_lower_vec(fail_nogap, n_nogap)
    return {
        "prob_upper_ok": float(np.mean(uppers <= SAFE_HARBOR_UPPER_MAX)),
        "prob_reject_sh": float(np.mean(lowers > 0.0)),  # T3: lower bound excludes 0
        "prob_gaps_ok": float(np.mean(n_gap >= GAP_CASES_MIN)),
        "median_upper": float(np.median(uppers)),
        "median_gaps": float(np.median(n_gap)),
        "p10_gaps": float(np.percentile(n_gap, 10)),
    }


def evaluate_candidate(n_gap_prone: int, rng: np.random.Generator) -> dict:
    """Worst-case-over-grid evaluation of one candidate N (controls matched 1:1).

    T1 (precision) is worst-cased over the necessity-HOLDS leak grid; T2 (gap count)
    over the gap-prevalence grid; T3 (detection) is the worst-case power to reject a
    false safe harbor over the necessity-VIOLATED leak grid.
    """
    n_control = n_gap_prone  # 1:1 matched design
    worst_t1 = 1.0
    worst_t2 = 1.0
    max_upper = 0.0
    min_p10_gaps = 1e9
    worst_t3 = 1.0
    for pgp in P_GAP_PRONE:
        for pgc in P_GAP_CONTROL:
            # T1 precision + T2 gap count under necessity-holds.
            for pfn in P_FAIL_NOGAP_HOLDS:
                r = simulate_point(n_gap_prone, n_control, pgp, pgc, pfn, rng)
                worst_t1 = min(worst_t1, r["prob_upper_ok"])
                worst_t2 = min(worst_t2, r["prob_gaps_ok"])
                max_upper = max(max_upper, r["median_upper"])
                min_p10_gaps = min(min_p10_gaps, r["p10_gaps"])
            # T3 detection under necessity-violated.
            for pfn in P_FAIL_NOGAP_VIOL:
                r = simulate_point(n_gap_prone, n_control, pgp, pgc, pfn, rng)
                worst_t3 = min(worst_t3, r["prob_reject_sh"])
    return {
        "n_gap_prone": n_gap_prone,
        "n_control": n_control,
        "N": n_gap_prone + n_control,
        "worst_prob_t1": worst_t1,
        "worst_prob_t2": worst_t2,
        "max_median_upper": max_upper,
        "min_p10_gaps": min_p10_gaps,
        "worst_prob_t3": worst_t3,
    }


def run() -> int:
    rng = np.random.default_rng(SEED)
    print(
        "S5 full-draw power / precision analysis (seed %d, %d reps/point)"
        % (SEED, N_REPS)
    )
    print(
        "Targets: T1 exact upper 95%% CI on P(fail|no gap) <= %.2f (necessity holds); "
        "T2 gap cases >= %d; each met w.p. >= %.2f (worst case over grid).\n"
        "T3 (reported): power to REJECT a false safe harbor at a true .03-.05 leak.\n"
        % (SAFE_HARBOR_UPPER_MAX, GAP_CASES_MIN, TARGET_PROB)
    )
    header = (
        "N_gp",
        "N_ctrl",
        "N",
        "P(T1)",
        "P(T2)",
        "T3 pow",
        "max med.upper",
        "p10 gaps",
    )
    print("%-6s %-7s %-5s %-7s %-7s %-7s %-14s %-9s" % header)
    recommended = None
    for n_gp in CANDIDATE_N_GAP_PRONE:
        r = evaluate_candidate(n_gp, rng)
        print(
            "%-6d %-7d %-5d %-7.3f %-7.3f %-7.3f %-14.4f %-9.0f"
            % (
                r["n_gap_prone"],
                r["n_control"],
                r["N"],
                r["worst_prob_t1"],
                r["worst_prob_t2"],
                r["worst_prob_t3"],
                r["max_median_upper"],
                r["min_p10_gaps"],
            )
        )
        if (
            recommended is None
            and r["worst_prob_t1"] >= TARGET_PROB
            and r["worst_prob_t2"] >= TARGET_PROB
        ):
            recommended = r

    print()
    if recommended is None:
        print(
            "No candidate met both targets at p >= %.2f across the grid; widen N."
            % TARGET_PROB
        )
        return 1
    print(
        "RECOMMENDED registered design: N = %d (%d gap-prone + %d matched controls, 1:1)."
        % (recommended["N"], recommended["n_gap_prone"], recommended["n_control"])
    )
    print(
        "  - T1 safe-harbor precision: exact upper 95%% CI on P(fail|no gap) <= %.2f met "
        "w.p. >= %.2f (necessity holds); worst-grid median upper ~ %.3f."
        % (
            SAFE_HARBOR_UPPER_MAX,
            recommended["worst_prob_t1"],
            recommended["max_median_upper"],
        )
    )
    print(
        "  - T2 gap cases >= %d met w.p. >= %.2f; worst-grid 10th pct gap count ~ %.0f "
        "(nominal band %d-%d)."
        % (
            GAP_CASES_MIN,
            recommended["worst_prob_t2"],
            recommended["min_p10_gaps"],
            GAP_CASES_MIN,
            GAP_CASES_MAX,
        )
    )
    print(
        "  - T3 detection: power to reject a false safe harbor at a true .03-.05 leak "
        ">= %.2f (worst grid)." % recommended["worst_prob_t3"]
    )
    print(
        "  - Coding load: N x 2 sub-dossiers x 3 raters/construct "
        "= %d structural + %d outcome calls = %d coding calls."
        % (recommended["N"] * 3, recommended["N"] * 3, recommended["N"] * 6)
    )
    return 0


def fixture() -> int:
    """Self-check the two math kernels against known values."""
    ok = True
    # Clopper-Pearson at k=0: upper = 1 - .05**(1/n). Known: n=60 -> ~.0487; n=100 -> ~.0295.
    for n, want in ((60, 0.0487), (100, 0.0295)):
        got = clopper_pearson_upper(0, n)
        if abs(got - want) > 5e-3:
            print("FAIL CP(0,%d) = %.4f, want ~%.4f" % (n, got, want))
            ok = False
        else:
            print("ok  CP(0,%d) = %.4f (~%.4f)" % (n, got, want))
    # CP is monotone increasing in k for fixed n.
    seq = [clopper_pearson_upper(k, 100) for k in range(0, 6)]
    if seq != sorted(seq):
        print("FAIL CP not monotone in k:", [round(x, 4) for x in seq])
        ok = False
    else:
        print("ok  CP monotone in k:", [round(x, 4) for x in seq])
    # Vectorised CP upper matches the scalar version.
    kk = np.array([0, 1, 3, 10])
    nn = np.array([100, 100, 150, 200])
    vec = cp_upper_vec(kk, nn)
    for i, (a, b) in enumerate(zip(kk, nn)):
        scal = clopper_pearson_upper(int(a), int(b))
        if abs(vec[i] - scal) > 1e-9:
            print("FAIL cp_upper_vec[%d]=%.6f != scalar %.6f" % (i, vec[i], scal))
            ok = False
    print("ok  cp_upper_vec matches scalar on", list(zip(kk.tolist(), nn.tolist())))
    # Lower bound: 0 at k=0, > 0 at k>0.
    low = cp_lower_vec(np.array([0, 5]), np.array([200, 200]))
    if not (low[0] == 0.0 and low[1] > 0.0):
        print("FAIL cp_lower_vec:", low)
        ok = False
    else:
        print(
            "ok  cp_lower_vec: k=0 ->", low[0], " k=5/200 ->", round(float(low[1]), 4)
        )
    # A tiny simulation runs and returns sane probabilities.
    rng = np.random.default_rng(1)
    r = simulate_point(150, 150, 0.475, 0.04, 0.005, rng, n_reps=2000)
    for key in (
        "prob_upper_ok",
        "prob_gaps_ok",
        "prob_reject_sh",
        "median_upper",
        "median_gaps",
    ):
        v = r[key]
        if not (0.0 <= v <= 300.0):
            print("FAIL sim %s out of range: %s" % (key, v))
            ok = False
    print(
        "ok  sim @ N=300 (leak .005): P(upper_ok)=%.3f P(gaps_ok)=%.3f median_upper=%.4f "
        "median_gaps=%.0f"
        % (r["prob_upper_ok"], r["prob_gaps_ok"], r["median_upper"], r["median_gaps"])
    )
    print("FIXTURE", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--fixture", action="store_true", help="self-check the math kernels"
    )
    args = ap.parse_args()
    if args.fixture:
        return fixture()
    return run()


if __name__ == "__main__":
    sys.exit(main())
