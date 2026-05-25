"""monte_carlo_simulation.py — Comparative-statics Monte Carlo for the
capability-as-projection formalism.

Companion computation script for:

    Zharnikov, D. (2026). Capability as Projection of an Append-Only Organizational Log: Toward an
    Event-Sourced Theory of Organizational Capability. Working paper.

Implements the comparative-statics simulation for Sections 5 and 6
of the paper ("elevate the formalism"):

    Vary conflict density d in {0.0, 0.1, 0.2, 0.5, 0.9} and decay
    parameter lambda in {0.0, 0.05, 0.1, 0.5} across N = 500 trials.
    For each trial, generate two synthetic logs L_A and L_B of size
    200 events each with target conflict density, compute the merged
    log L_M under (i) acquirer-supreme conflict-resolution policy
    (snapshot-import failure mode -- relevant to P2) and (ii)
    negotiated conflict-resolution (clean merge -- relevant to P1).
    Track post-merge projection continuity and simulated writedown
    magnitude.

Outputs (under ``code/plots/`` and ``code/``):

    plots/plot_projection_continuity_vs_kappa.png
    plots/plot_writedown_vs_conflict_density.png
    monte_carlo_results.csv

Reproducibility:

    Fixed RNG seed = 42.
    Run command (from the paper directory):

        uv run python code/monte_carlo_simulation.py

    Total runtime on a 2024 Apple Silicon Mac: < 30 seconds.

Scope caveat: synthetic-data simulation is a numerical-coherence check
for the formalism, not an empirical confirmation in real firms. See
``PRE_EXPERIMENT_REPORT.md`` and ``POST_EXPERIMENT_REPORT.md``.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

RANDOM_SEED: int = 42

N_TRIALS: int = 500
LOG_SIZE: int = 200
CONFLICT_DENSITIES: tuple[float, ...] = (0.0, 0.1, 0.2, 0.5, 0.9)
LAMBDAS: tuple[float, ...] = (0.0, 0.05, 0.1, 0.5)
RESOLUTION_POLICIES: tuple[str, ...] = ("negotiated", "acquirer_supreme")

# Event-type weights for the simulated "scaling capability" query
WEIGHT_MAP: dict[str, float] = {
    "DECISION": 1.0,
    "POLICY": 1.0,
    "ARTIFACT": 0.5,
    "FAILURE": -1.0,
    "PERSONNEL": 0.0,
}
EVENT_TYPES: tuple[str, ...] = tuple(WEIGHT_MAP.keys())

# Tolerance band for "continuity" (post-merge pi within +/- TOL of pre-merge)
CONTINUITY_TOL: float = 0.10

OUT_DIR = Path(__file__).resolve().parent
PLOT_DIR = OUT_DIR / "plots"
CSV_PATH = OUT_DIR / "monte_carlo_results.csv"


# --------------------------------------------------------------------------
# Synthetic log generation
# --------------------------------------------------------------------------


@dataclass
class SyntheticLog:
    """A lightweight numpy-backed log for fast Monte Carlo iteration."""

    times: np.ndarray  # shape (n,), in years since t0
    weights: np.ndarray  # shape (n,)
    is_policy: np.ndarray  # shape (n,) bool — flags POLICY/PERSONNEL events
    policy_ids: np.ndarray  # shape (n,) int — conflict-eligible policy ids

    def size(self) -> int:
        return int(self.times.size)


def generate_log(
    rng: np.random.Generator,
    n: int,
    horizon_years: float = 5.0,
    n_policy_ids: int = 20,
) -> SyntheticLog:
    """Generate a single synthetic log of size n.

    Event times are drawn uniformly over [0, horizon_years]. Event
    types are drawn from EVENT_TYPES with empirically reasonable
    proportions (DECISION 0.30, POLICY 0.20, ARTIFACT 0.25, FAILURE
    0.10, PERSONNEL 0.15). Each POLICY or PERSONNEL event is assigned
    a policy_id in [0, n_policy_ids); conflicts between two logs are
    defined as POLICY/PERSONNEL events sharing a policy_id.
    """
    times = rng.uniform(0.0, horizon_years, size=n)
    times.sort()

    type_probs = np.array([0.30, 0.10, 0.20, 0.15, 0.25])  # matches EVENT_TYPES order
    type_idx = rng.choice(len(EVENT_TYPES), size=n, p=type_probs)
    type_names = np.array(EVENT_TYPES)[type_idx]

    weights = np.array([WEIGHT_MAP[name] for name in type_names])
    is_policy = np.isin(type_names, ("POLICY", "PERSONNEL"))

    # Assign policy_ids only to policy-bearing events; others get -1
    policy_ids = np.full(n, -1, dtype=int)
    n_policy = int(is_policy.sum())
    if n_policy > 0:
        policy_ids[is_policy] = rng.integers(0, n_policy_ids, size=n_policy)

    return SyntheticLog(times=times, weights=weights, is_policy=is_policy,
                        policy_ids=policy_ids)


def inject_conflicts(
    log_b: SyntheticLog,
    log_a: SyntheticLog,
    rng: np.random.Generator,
    target_density: float,
) -> SyntheticLog:
    """Mutate ``log_b`` so that roughly ``target_density`` fraction of
    its policy-bearing events share a policy_id with at least one of
    log_a's policy-bearing events.

    Returns a new SyntheticLog (does not mutate input).
    """
    new_policy_ids = log_b.policy_ids.copy()
    a_policy_pool = log_a.policy_ids[log_a.is_policy]
    if a_policy_pool.size == 0:
        return SyntheticLog(log_b.times, log_b.weights, log_b.is_policy,
                            new_policy_ids)
    a_unique = np.unique(a_policy_pool)

    b_policy_positions = np.where(log_b.is_policy)[0]
    n_b_policy = b_policy_positions.size
    if n_b_policy == 0:
        return SyntheticLog(log_b.times, log_b.weights, log_b.is_policy,
                            new_policy_ids)

    n_conflict_target = int(round(target_density * n_b_policy))
    if n_conflict_target == 0:
        # Force NO conflicts: relabel any b policy_id that collides with
        # a_unique to a value outside that set.
        max_id = int(max(a_unique.max(), new_policy_ids.max(initial=0))) + 1
        safe_id_pool = np.arange(max_id + 1, max_id + 1 + 50)
        collide_mask = np.isin(new_policy_ids[b_policy_positions], a_unique)
        n_collisions = int(collide_mask.sum())
        if n_collisions > 0:
            replacement = rng.choice(safe_id_pool, size=n_collisions, replace=True)
            new_policy_ids[b_policy_positions[collide_mask]] = replacement
        return SyntheticLog(log_b.times, log_b.weights, log_b.is_policy,
                            new_policy_ids)

    # Otherwise: first scrub all collisions, then plant exactly the
    # target number of fresh collisions with a_unique policy ids.
    max_id = int(max(a_unique.max(), new_policy_ids.max(initial=0))) + 1
    safe_id_pool = np.arange(max_id + 1, max_id + 1 + 50)
    collide_mask = np.isin(new_policy_ids[b_policy_positions], a_unique)
    n_collisions = int(collide_mask.sum())
    if n_collisions > 0:
        replacement = rng.choice(safe_id_pool, size=n_collisions, replace=True)
        new_policy_ids[b_policy_positions[collide_mask]] = replacement

    # Plant the target conflicts
    conflict_positions = rng.choice(b_policy_positions,
                                    size=min(n_conflict_target, n_b_policy),
                                    replace=False)
    planted_ids = rng.choice(a_unique, size=conflict_positions.size, replace=True)
    new_policy_ids[conflict_positions] = planted_ids

    return SyntheticLog(log_b.times, log_b.weights, log_b.is_policy,
                        new_policy_ids)


# --------------------------------------------------------------------------
# Projection + compatibility (numpy-vectorized)
# --------------------------------------------------------------------------


def pi_lambda_log(log: SyntheticLog, render_t: float, lam: float) -> float:
    """Vectorized weighted prefix sum with exponential decay."""
    mask = log.times <= render_t
    if not mask.any():
        return 0.0
    dt = render_t - log.times[mask]
    return float(np.sum(log.weights[mask] * np.exp(-lam * dt)))


def kappa_logs(log_a: SyntheticLog, log_b: SyntheticLog) -> float:
    """kappa(L_A, L_B) using policy_id collisions as conflicts.

    Each policy-bearing event whose policy_id appears in the other log's
    policy_id set is counted as implicated.
    """
    n_total = log_a.size() + log_b.size()
    if n_total == 0:
        return 1.0
    a_pol = log_a.policy_ids[log_a.is_policy]
    b_pol = log_b.policy_ids[log_b.is_policy]
    if a_pol.size == 0 or b_pol.size == 0:
        return 1.0
    a_set = set(a_pol.tolist())
    b_set = set(b_pol.tolist())
    shared = a_set & b_set
    if not shared:
        return 1.0
    implicated_a = int(np.isin(log_a.policy_ids, list(shared)).sum())
    implicated_b = int(np.isin(log_b.policy_ids, list(shared)).sum())
    return 1.0 - (implicated_a + implicated_b) / n_total


# --------------------------------------------------------------------------
# Merge policies
# --------------------------------------------------------------------------


def merge_negotiated(log_a: SyntheticLog, log_b: SyntheticLog) -> SyntheticLog:
    """Clean merge: union of events; on conflict (shared policy_id) the
    *later* of the two events wins (last-write-wins per CRDT
    convention), but BOTH events stay on the log (the loser's weight is
    halved to model the negotiation cost / partial preservation).
    """
    a_pol = log_a.policy_ids[log_a.is_policy]
    b_pol = log_b.policy_ids[log_b.is_policy]
    shared = set(a_pol.tolist()) & set(b_pol.tolist())

    a_weights = log_a.weights.copy()
    b_weights = log_b.weights.copy()

    for pid in shared:
        a_idx = np.where((log_a.policy_ids == pid) & log_a.is_policy)[0]
        b_idx = np.where((log_b.policy_ids == pid) & log_b.is_policy)[0]
        if a_idx.size == 0 or b_idx.size == 0:
            continue
        # The later event wins; loser's weight halved (negotiation cost).
        a_max_t = log_a.times[a_idx].max()
        b_max_t = log_b.times[b_idx].max()
        if a_max_t >= b_max_t:
            b_weights[b_idx] *= 0.5
        else:
            a_weights[a_idx] *= 0.5

    return SyntheticLog(
        times=np.concatenate([log_a.times, log_b.times]),
        weights=np.concatenate([a_weights, b_weights]),
        is_policy=np.concatenate([log_a.is_policy, log_b.is_policy]),
        policy_ids=np.concatenate([log_a.policy_ids, log_b.policy_ids]),
    )


def merge_acquirer_supreme(log_a: SyntheticLog,
                           log_b: SyntheticLog) -> SyntheticLog:
    """Acquirer-supreme: L_A retained in full; L_B contributes only
    non-policy-conflicting events, AND policy-bearing events from L_B
    that DO conflict are dropped entirely (snapshot-import failure
    mode -- the target's policy-substrate is discarded).
    """
    a_pol = log_a.policy_ids[log_a.is_policy]
    a_set = set(a_pol.tolist())
    conflict_mask = np.isin(log_b.policy_ids, list(a_set)) & log_b.is_policy
    keep_mask = ~conflict_mask

    return SyntheticLog(
        times=np.concatenate([log_a.times, log_b.times[keep_mask]]),
        weights=np.concatenate([log_a.weights, log_b.weights[keep_mask]]),
        is_policy=np.concatenate([log_a.is_policy, log_b.is_policy[keep_mask]]),
        policy_ids=np.concatenate([log_a.policy_ids,
                                   log_b.policy_ids[keep_mask]]),
    )


# --------------------------------------------------------------------------
# Trial + aggregation
# --------------------------------------------------------------------------


@dataclass
class TrialResult:
    conflict_density: float
    lam: float
    policy: str
    kappa: float
    pi_pre_merge_a: float
    pi_post_merge: float
    continuity_ratio: float
    writedown: float


def run_trial(rng: np.random.Generator, density: float, lam: float,
              policy: str) -> TrialResult:
    """One Monte Carlo trial."""
    log_a = generate_log(rng, LOG_SIZE)
    log_b_raw = generate_log(rng, LOG_SIZE)
    log_b = inject_conflicts(log_b_raw, log_a, rng, density)

    horizon = max(log_a.times.max(), log_b.times.max())
    render_t = horizon + 1.0  # render 1 year after the last event

    if policy == "negotiated":
        log_m = merge_negotiated(log_a, log_b)
    elif policy == "acquirer_supreme":
        log_m = merge_acquirer_supreme(log_a, log_b)
    else:
        raise ValueError(policy)

    pi_a = pi_lambda_log(log_a, render_t, lam)
    pi_m = pi_lambda_log(log_m, render_t, lam)

    # Continuity ratio: post-merge pi / expected pi if both logs
    # contributed fully (pi_a + pi_b). Acquirer-supreme drops the
    # target's policy-bearing events, so this ratio falls below 1.
    pi_b = pi_lambda_log(log_b, render_t, lam)
    denom = pi_a + pi_b
    if abs(denom) < 1e-9:
        continuity = 1.0
    else:
        continuity = pi_m / denom

    kappa = kappa_logs(log_a, log_b)

    # Simulated writedown: under acquirer-supreme, the lost capability
    # is (pi_a + pi_b) - pi_m; under negotiated it's the negotiation
    # cost (the 0.5x weighting on superseded policy events). We
    # normalize by (pi_a + pi_b) when meaningful and clamp at [0, 1].
    if abs(denom) < 1e-9:
        writedown = 0.0
    else:
        writedown = max(0.0, (denom - pi_m) / denom)
        writedown = min(writedown, 1.0)

    return TrialResult(
        conflict_density=density,
        lam=lam,
        policy=policy,
        kappa=kappa,
        pi_pre_merge_a=pi_a,
        pi_post_merge=pi_m,
        continuity_ratio=continuity,
        writedown=writedown,
    )


def aggregate(results: list[TrialResult]) -> list[dict[str, float]]:
    """Aggregate trial results by (conflict_density, lam, policy)."""
    keys: set[tuple[float, float, str]] = set(
        (r.conflict_density, r.lam, r.policy) for r in results
    )
    rows: list[dict[str, float]] = []
    for d, lam, policy in sorted(keys):
        bucket = [r for r in results
                  if r.conflict_density == d and r.lam == lam
                  and r.policy == policy]
        n = len(bucket)
        kappas = np.array([r.kappa for r in bucket])
        conts = np.array([r.continuity_ratio for r in bucket])
        writedowns = np.array([r.writedown for r in bucket])
        rows.append({
            "conflict_density": d,
            "lambda": lam,
            "policy": policy,
            "n_trials": n,
            "kappa_mean": float(kappas.mean()),
            "kappa_stderr": float(kappas.std(ddof=1) / math.sqrt(n)),
            "continuity_mean": float(conts.mean()),
            "continuity_stderr": float(conts.std(ddof=1) / math.sqrt(n)),
            "writedown_mean": float(writedowns.mean()),
            "writedown_stderr": float(writedowns.std(ddof=1) / math.sqrt(n)),
        })
    return rows


# --------------------------------------------------------------------------
# Plotting
# --------------------------------------------------------------------------


def plot_continuity_vs_kappa(rows: list[dict[str, float]],
                             out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    markers = {"negotiated": "o", "acquirer_supreme": "s"}
    colors = {0.0: "#1f77b4", 0.05: "#2ca02c", 0.1: "#ff7f0e", 0.5: "#d62728"}

    for policy in RESOLUTION_POLICIES:
        for lam in LAMBDAS:
            xs = [r["kappa_mean"] for r in rows
                  if r["lambda"] == lam and r["policy"] == policy]
            ys = [r["continuity_mean"] for r in rows
                  if r["lambda"] == lam and r["policy"] == policy]
            yerr = [r["continuity_stderr"] for r in rows
                    if r["lambda"] == lam and r["policy"] == policy]
            order = np.argsort(xs)
            xs = np.array(xs)[order]
            ys = np.array(ys)[order]
            yerr = np.array(yerr)[order]
            ax.errorbar(
                xs, ys, yerr=yerr,
                marker=markers[policy], color=colors[lam],
                linestyle="-" if policy == "negotiated" else "--",
                linewidth=1.4, markersize=6, capsize=3,
                label=f"{policy}, lambda={lam}",
            )

    ax.set_xlabel("Compatibility kappa(L_A, L_B)")
    ax.set_ylabel("Projection continuity ratio pi(L_M) / (pi(L_A) + pi(L_B))")
    ax.set_title(
        "Projection continuity vs log compatibility\n"
        f"({N_TRIALS} trials per cell, log size {LOG_SIZE} each)"
    )
    ax.axhline(1.0, color="gray", linewidth=0.6, linestyle=":")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7, loc="lower right", ncol=2)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_writedown_vs_conflict(rows: list[dict[str, float]],
                               out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    markers = {"negotiated": "o", "acquirer_supreme": "s"}
    colors = {0.0: "#1f77b4", 0.05: "#2ca02c", 0.1: "#ff7f0e", 0.5: "#d62728"}

    for policy in RESOLUTION_POLICIES:
        for lam in LAMBDAS:
            bucket = [r for r in rows
                      if r["lambda"] == lam and r["policy"] == policy]
            xs = np.array([1.0 - r["kappa_mean"] for r in bucket])
            ys = np.array([r["writedown_mean"] for r in bucket])
            yerr = np.array([r["writedown_stderr"] for r in bucket])
            order = np.argsort(xs)
            xs = xs[order]
            ys = ys[order]
            yerr = yerr[order]
            ax.errorbar(
                xs, ys, yerr=yerr,
                marker=markers[policy], color=colors[lam],
                linestyle="-" if policy == "negotiated" else "--",
                linewidth=1.4, markersize=6, capsize=3,
                label=f"{policy}, lambda={lam}",
            )

    ax.set_xlabel("Conflict density 1 - kappa(L_A, L_B)")
    ax.set_ylabel("Simulated writedown magnitude (fraction of pre-merge pi lost)")
    ax.set_title(
        "Writedown magnitude vs conflict density (P3 visualization)\n"
        f"({N_TRIALS} trials per cell, log size {LOG_SIZE} each)"
    )
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7, loc="upper left", ncol=2)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def run() -> None:
    print("monte_carlo_simulation.py — Firm-as-Event-Log comparative statics")
    print("=" * 72)
    print(f"RANDOM_SEED = {RANDOM_SEED}")
    print(f"N_TRIALS    = {N_TRIALS}")
    print(f"LOG_SIZE    = {LOG_SIZE} events per log")
    print(f"densities   = {CONFLICT_DENSITIES}")
    print(f"lambdas     = {LAMBDAS}")
    print(f"policies    = {RESOLUTION_POLICIES}")
    print()

    rng = np.random.default_rng(RANDOM_SEED)
    results: list[TrialResult] = []
    n_cells = (len(CONFLICT_DENSITIES) * len(LAMBDAS)
               * len(RESOLUTION_POLICIES))
    print(f"Total cells = {n_cells}; trials per cell = {N_TRIALS}; "
          f"total trials = {n_cells * N_TRIALS}")

    for density in CONFLICT_DENSITIES:
        for lam in LAMBDAS:
            for policy in RESOLUTION_POLICIES:
                for _ in range(N_TRIALS):
                    results.append(run_trial(rng, density, lam, policy))
    print(f"Trials completed: {len(results)}")
    print()

    rows = aggregate(results)

    # Write CSV
    fieldnames = [
        "conflict_density", "lambda", "policy", "n_trials",
        "kappa_mean", "kappa_stderr",
        "continuity_mean", "continuity_stderr",
        "writedown_mean", "writedown_stderr",
    ]
    with CSV_PATH.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r[k] for k in fieldnames})
    print(f"Wrote aggregated results: {CSV_PATH}")

    # Print summary table
    print()
    print("Aggregated results (one row per (density, lambda, policy)):")
    print("-" * 72)
    hdr = (f"{'dens':>5} {'lam':>5} {'policy':>17} "
           f"{'kappa':>7} {'continuity':>11} {'writedown':>10}")
    print(hdr)
    for r in rows:
        print(f"{r['conflict_density']:>5.2f} {r['lambda']:>5.2f} "
              f"{r['policy']:>17s} {r['kappa_mean']:>7.4f} "
              f"{r['continuity_mean']:>11.4f} {r['writedown_mean']:>10.4f}")
    print()

    # Plots
    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    p1 = PLOT_DIR / "plot_projection_continuity_vs_kappa.png"
    p2 = PLOT_DIR / "plot_writedown_vs_conflict_density.png"
    plot_continuity_vs_kappa(rows, p1)
    plot_writedown_vs_conflict(rows, p2)
    print(f"Wrote plot: {p1}")
    print(f"Wrote plot: {p2}")
    print()
    print("OK — monte_carlo_simulation.py completed.")


if __name__ == "__main__":
    run()
