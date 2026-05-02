"""
Simulation: Information Loss in Rank-1 Audit vs. Full-Rank Cascade Projection
==============================================================================
Models organizational states as 6-dimensional vectors (L0-L5 cascade dimensions).

The key question: how much of the CLEAN TRUE SIGNAL is preserved by each
verification architecture?

- Rank-1 audit: can only detect deviations on the single compliance axis (dim 0).
  It discards all information about dims 1-5. A deviation that lives entirely in
  dims 1-5 is INVISIBLE to rank-1 audit, no matter how large.

- Full-rank cascade: independently projects each dimension, detecting deviations
  across all 6 specification levels. The cascade localizes failures by level.

We model this as follows:
  - x_true: the true organizational state (clean, known specification target)
  - x_obs = x_true + noise: the observed state with Gaussian noise sigma
  - Deviation d = x_obs - x_true: what the verifier is trying to detect

Rank-1 audit detects only d[0] (compliance axis).
Full-rank cascade detects the full deviation vector d = (d[0], ..., d[5]).

Information loss = fraction of total deviation MISSED by the verifier.
  - Rank-1 audit misses d[1..5] entirely.
  - Full-rank cascade misses nothing (detects all 6 dims independently).

We also compute the Frobenius residual: ||d - detected_d||, i.e.,
how much deviation propagates undetected past each verifier.
"""

import numpy as np
import json

np.random.seed(42)

N_TRIALS = 1000
DIMS = 6  # L0-L5 OST cascade levels
SIGMA_VALUES = [0.1, 0.5, 1.0, 2.0]

results = {}

for sigma in SIGMA_VALUES:
    # Per-trial: undetected deviation norm for audit vs cascade
    undetected_audit_norms = []
    undetected_cascade_norms = []
    total_deviation_norms = []

    for _ in range(N_TRIALS):
        # True clean specification target (arbitrary unit-norm vector)
        x_true = np.random.randn(DIMS)
        x_true = x_true / np.linalg.norm(x_true)

        # Observed state: true state + isotropic noise
        noise = np.random.randn(DIMS) * sigma
        x_obs = x_true + noise

        # Total deviation from spec
        d = x_obs - x_true  # = noise (since x_true is the spec target)

        # Rank-1 audit detects only d[0] (compliance axis)
        detected_audit = np.zeros(DIMS)
        detected_audit[0] = d[0]
        undetected_audit = d - detected_audit  # undetected deviation = d[1..5]

        # Full-rank cascade detects all 6 dimensions independently
        detected_cascade = d.copy()  # detects everything
        undetected_cascade = d - detected_cascade  # = zero vector

        undetected_audit_norms.append(np.linalg.norm(undetected_audit))
        undetected_cascade_norms.append(np.linalg.norm(undetected_cascade))
        total_deviation_norms.append(np.linalg.norm(d))

    mean_undetected_audit = float(np.mean(undetected_audit_norms))
    mean_undetected_cascade = float(np.mean(undetected_cascade_norms))
    mean_total_deviation = float(np.mean(total_deviation_norms))
    std_undetected_audit = float(np.std(undetected_audit_norms))
    std_total = float(np.std(total_deviation_norms))

    # Information loss ratio: fraction of deviation that goes undetected
    pct_missed_audit = 100.0 * mean_undetected_audit / mean_total_deviation
    pct_missed_cascade = 100.0 * mean_undetected_cascade / mean_total_deviation

    results[f"sigma_{sigma}"] = {
        "sigma": sigma,
        "n_trials": N_TRIALS,
        "mean_total_deviation": round(mean_total_deviation, 4),
        "rank1_audit": {
            "mean_undetected_deviation": round(mean_undetected_audit, 4),
            "std_undetected_deviation": round(std_undetected_audit, 4),
            "pct_deviation_missed": round(pct_missed_audit, 1),
        },
        "full_rank_cascade": {
            "mean_undetected_deviation": round(mean_undetected_cascade, 4),
            "std_undetected_deviation": 0.0,
            "pct_deviation_missed": round(pct_missed_cascade, 1),
        },
        "ratio_audit_undetected_to_cascade": (
            round(mean_undetected_audit / max(mean_undetected_cascade, 1e-10), 2)
            if mean_undetected_cascade < 1e-10
            else round(mean_undetected_audit / mean_undetected_cascade, 2)
        ),
    }

# Print summary
print("=" * 75)
print("Simulation: Undetected Deviation — Rank-1 Audit vs. Full-Rank Cascade")
print(f"Dimensions: {DIMS} (L0-L5 OST cascade), Trials: {N_TRIALS}")
print("=" * 75)
print(f"{'Sigma':>6} | {'Total Dev':>10} | {'Audit Missed':>14} | "
      f"{'Cascade Missed':>15} | {'% Missed (Audit)':>17}")
print("-" * 75)
for sigma in SIGMA_VALUES:
    r = results[f"sigma_{sigma}"]
    print(f"{sigma:>6.1f} | {r['mean_total_deviation']:>10.4f} | "
          f"{r['rank1_audit']['mean_undetected_deviation']:>14.4f} | "
          f"{r['full_rank_cascade']['mean_undetected_deviation']:>15.4f} | "
          f"{r['rank1_audit']['pct_deviation_missed']:>16.1f}%")
print("=" * 75)

# Also compute information-theoretic measure: fraction of variance detected
# Audit detects E[d_0^2] / E[||d||^2] = 1/6 of total variance (isotropic noise)
print(f"\nNote: Under isotropic Gaussian noise, rank-1 audit detects exactly")
print(f"      1/{DIMS} = {100/DIMS:.1f}% of total deviation variance (dim 0 only).")
print(f"      Full-rank cascade detects 100% across all {DIMS} dimensions.")

# Analytic prediction for undetected audit norm (dims 1..5)
# E[||noise_{1..5}||^2] = 5 * sigma^2, so E[||noise_{1..5}||] ~ sqrt(5)*sigma
print(f"\nAnalytic predictions (undetected audit norm ~ sqrt({DIMS-1}) * sigma):")
for sigma in SIGMA_VALUES:
    analytic = np.sqrt(DIMS - 1) * sigma
    simulated = results[f"sigma_{sigma}"]["rank1_audit"]["mean_undetected_deviation"]
    print(f"  sigma={sigma}: analytic={analytic:.4f}, simulated={simulated:.4f}")

# Save to JSON (alongside this script)
import os
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "simulation_results.json")
with open(output_path, "w") as f:
    json.dump(results, f, indent=2)

print(f"\nResults saved to: {output_path}")
