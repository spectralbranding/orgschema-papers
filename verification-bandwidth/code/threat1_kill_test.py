"""Is the intersection view reconcilable with the bandwidth view?

2026ae (multi-evaluator boundary condition) says the effective invariant subspace
becomes the INTERSECTION of evaluators' subspaces, and cascade rank "may be LOWER
than any single evaluator's". The bandwidth intuition says more diverse evaluators
check MORE dimensions, so rank should be HIGHER. If these are trivially identical
or trivially unrelated, there is nothing to reconcile.

FORMAL CLAIM UNDER TEST
-----------------------
They are neither. They are two different AGGREGATION RULES and they move in
OPPOSITE directions as evaluator diversity rises:

  evaluator e checks subspace C_e; it detects deviation d iff |<v_e, d>| > tau
  (an audit sees only the component lying in what it inspects).

  * DISJUNCTIVE panel (any evaluator may raise a flag): blind spot is
    intersection_e ker(P_e) = (sum_e C_e)^perp  -> SHRINKS with diversity.
  * UNANIMOUS panel (all evaluators must agree to flag): blind spot is
    union_e ker(P_e)                            -> GROWS with diversity.

  Every monotone aggregation rule f (AND <= f <= OR) is bracketed between them.
  Bracket WIDTH is governed by inter-evaluator correlation: as correlation -> 1
  the two blind spots coincide and the aggregation rule stops mattering at all.

PREDICTIONS (falsifiable; this script tests each)
  P1  OR-rule detection DECREASES as correlation rises.
  P2  AND-rule detection INCREASES as correlation rises.
  P3  MAJORITY lies strictly between them at low correlation.
  P4  All three converge as correlation -> 1 (bracket collapses).
  P5  Effective rank k/lambda_max falls from ~k to ~1 as correlation rises,
      and matches the Kish n_eff = k/(1+(k-1)*phi) under exchangeability.

If P1 and P2 have the SAME sign, the two views are not distinct -> paper DROPS.

ADDENDUM — the two phi's, side by side
------------------------------------------------------
The verdict above is unchanged; this file now ALSO emits, per condition, the
second correlation the paper needs. phi_geom is the mean absolute inner product
between evaluator directions (what this test always measured). phi_err is the
mean pairwise PHI COEFFICIENT on the binary miss indicators — Kohli's quantity,
computed on the SAME simulated panel. phi_pred is what `phi_mapping.py` predicts
phi_err should be, from phi_geom and the observed miss rate.

This is the end-to-end check: `phi_mapping.py` derives the map under
GAUSSIAN isotropic deviations and pairwise, whereas this test draws UNIT-NORM
deviations in n = 10 and runs a k = 9 panel. Agreement means the map survives
both the distributional change and the move from a pair to a panel.

All new columns are computed from arrays the original code already drew, so no
RNG draw is added or reordered and the recorded P1-P5 table reproduces exactly.

Run: uv run --with numpy --with scipy --with matplotlib python threat1_kill_test.py
"""

from __future__ import annotations

import os

import numpy as np

SEED = 20260811
N_DIM = 10  # ambient organizational state space
K = 9  # evaluators (matches Kohli's panel size)
TAU = 0.30  # detection threshold on the inspected component
N_DEV = 200_000  # random unit deviations per condition
RHOS = [0.0, 0.1, 0.2, 0.3, 0.391, 0.5, 0.7, 0.9, 0.99]


def evaluator_directions(rng, k, n, rho):
    """k unit vectors with expected pairwise correlation ~rho (shared-factor model)."""
    shared = rng.normal(size=n)
    shared /= np.linalg.norm(shared)
    idio = rng.normal(size=(k, n))
    idio /= np.linalg.norm(idio, axis=1, keepdims=True)
    v = np.sqrt(rho) * shared + np.sqrt(1.0 - rho) * idio
    v /= np.linalg.norm(v, axis=1, keepdims=True)
    return v


def run(rho, rng):
    v = evaluator_directions(rng, K, N_DIM, rho)

    # realised mean pairwise |correlation| among evaluator directions
    g = v @ v.T
    iu = np.triu_indices(K, 1)
    phi_bar = float(np.mean(np.abs(g[iu])))

    # effective rank of the evaluator set (Kohli's eigenvalue n_eff = k / lambda_max)
    lam_max = float(np.linalg.eigvalsh(g)[-1])
    n_eff_eigen = K / lam_max
    n_eff_kish = K / (1.0 + (K - 1) * phi_bar)

    # random unit deviations; evaluator e detects iff |<v_e, d>| > TAU
    d = rng.normal(size=(N_DEV, N_DIM))
    d /= np.linalg.norm(d, axis=1, keepdims=True)
    seen = np.abs(d @ v.T) > TAU  # (N_DEV, K) boolean
    n_seen = seen.sum(axis=1)

    # --- addendum: the error-vector phi on the SAME panel -----------------
    # every drawn deviation is genuine, so a non-detection IS an error (miss).
    miss = (~seen).astype(np.float64)  # (N_DEV, K) binary error indicators
    q = miss.mean(axis=0)  # per-evaluator marginal miss rate
    joint = (miss.T @ miss) / N_DEV  # (K, K) joint miss probabilities
    denom = np.sqrt(np.outer(q * (1 - q), q * (1 - q)))
    phi_mat = (joint - np.outer(q, q)) / denom
    phi_err = float(np.mean(phi_mat[iu]))

    return {
        "rho": rho,
        "phi_bar": phi_bar,
        "phi_err": phi_err,
        "rho_ij": np.abs(g[iu]),  # pairwise geometric correlations, for the map
        "miss_rate": float(q.mean()),
        "n_eff_eigen": n_eff_eigen,
        "n_eff_kish": n_eff_kish,
        "n_eff_err": K / (1.0 + (K - 1) * phi_err),
        "or_rate": float((n_seen >= 1).mean()),
        "maj_rate": float((n_seen > K / 2).mean()),
        "and_rate": float((n_seen == K).mean()),
        "single_rate": float(seen[:, 0].mean()),
    }


def main():
    rng = np.random.default_rng(SEED)
    rows = [run(r, rng) for r in RHOS]

    print(f"n_dim={N_DIM}  k={K}  tau={TAU}  deviations={N_DEV:,}  seed={SEED}\n")
    hdr = (
        f"{'rho':>6} {'phi_bar':>8} {'n_eff_eig':>10} {'n_eff_kish':>11} "
        f"{'OR':>7} {'MAJ':>7} {'AND':>7} {'single':>7} {'bracket':>8}"
    )
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        print(
            f"{r['rho']:>6.3f} {r['phi_bar']:>8.3f} {r['n_eff_eigen']:>10.2f} "
            f"{r['n_eff_kish']:>11.2f} {r['or_rate']:>7.3f} {r['maj_rate']:>7.3f} "
            f"{r['and_rate']:>7.3f} {r['single_rate']:>7.3f} "
            f"{r['or_rate'] - r['and_rate']:>8.3f}"
        )

    print("\nVERDICT")
    or_trend = rows[-1]["or_rate"] - rows[0]["or_rate"]
    and_trend = rows[-1]["and_rate"] - rows[0]["and_rate"]
    print(f"  P1 OR trend over rho:  {or_trend:+.3f}  (predicted NEGATIVE)")
    print(f"  P2 AND trend over rho: {and_trend:+.3f}  (predicted POSITIVE)")
    same_sign = (or_trend > 0) == (and_trend > 0)
    print(f"  P1/P2 opposite signs:  {not same_sign}")
    lo, hi = rows[0], rows[-1]
    print(
        f"  P3 MAJ strictly inside at rho=0: "
        f"{lo['and_rate'] < lo['maj_rate'] < lo['or_rate']}"
    )
    print(
        f"  P4 bracket collapses: width {lo['or_rate'] - lo['and_rate']:.3f} "
        f"-> {hi['or_rate'] - hi['and_rate']:.3f}"
    )
    print(
        f"  P5 eff. rank {lo['n_eff_eigen']:.2f} -> {hi['n_eff_eigen']:.2f} "
        f"(k={K}); eigen vs Kish max abs diff "
        f"{max(abs(r['n_eff_eigen'] - r['n_eff_kish']) for r in rows):.2f}"
    )
    print(
        "\n  => "
        + (
            "SURVIVES: the two views are distinct regimes, not one quantity."
            if not same_sign
            else "DROP: the two views move together; no reconciliation to make."
        )
    )

    phi_report(rows)


def phi_report(rows):
    """Addendum: geometric phi vs error phi on this panel, against the map."""
    from phi_mapping import kish, phi_from_rho, t_of_q

    print("\n\nADDENDUM — the two correlations on the same panel")
    print("  phi_geom: mean |<v_e, v_f>|      (geometric, what this test measured)")
    print("  phi_err : mean pairwise phi on binary miss indicators   (Kohli's)")
    print("  mapOfMean: phi_from_rho(phi_geom, t)   — the map applied to the average")
    print("  meanOfMap: mean_ij phi_from_rho(|rho_ij|, t)  — the map applied PAIRWISE")
    print("  The two differ because the map is convex at low rho (M4). meanOfMap is")
    print("  correct; mapOfMean understates. t is taken from the observed miss rate.\n")
    hdr = (
        f"{'rho':>6} {'miss':>7} {'phi_geom':>9} {'phi_err':>8} {'mapOfMean':>10} "
        f"{'meanOfMap':>10} {'err-moM':>8} {'n_eff_geom':>11} {'n_eff_err':>10}"
    )
    print(hdr)
    print("-" * len(hdr))
    worst = 0.0
    for r in rows:
        t = t_of_q(r["miss_rate"])
        map_of_mean = phi_from_rho(r["phi_bar"], t)
        mean_of_map = float(np.mean([phi_from_rho(x, t) for x in r["rho_ij"]]))
        worst = max(worst, abs(r["phi_err"] - mean_of_map))
        print(
            f"{r['rho']:>6.3f} {r['miss_rate']:>7.3f} {r['phi_bar']:>9.3f} "
            f"{r['phi_err']:>8.3f} {map_of_mean:>10.3f} {mean_of_map:>10.3f} "
            f"{r['phi_err'] - mean_of_map:>+8.3f} "
            f"{r['n_eff_kish']:>11.2f} {r['n_eff_err']:>10.2f}"
        )
    print(f"\n  max |phi_err - meanOfMap| = {worst:.3f}")
    print(
        "  NOTE: this panel draws UNIT-NORM deviations, so a negative radial term\n"
        "  (the counterpart of shared item difficulty, R1) sits on top of the map.\n"
        "  Under the map's own Gaussian model the residual falls to < .001 —\n"
        "  see phi_mapping.check_panel_recovery()."
    )
    print(
        "  attenuation holds on every row: "
        f"{all(r['phi_err'] < r['phi_bar'] for r in rows)}"
    )
    print(
        "  n_eff from error vectors >= n_eff from geometry on every row: "
        f"{all(r['n_eff_err'] >= r['n_eff_kish'] - 1e-9 for r in rows)}"
    )

    _phi_plot(rows, kish, phi_from_rho, t_of_q)


def _phi_plot(rows, kish, phi_from_rho, t_of_q):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    t_bar = t_of_q(float(np.mean([r["miss_rate"] for r in rows])))
    grid = np.linspace(0.0, 0.999, 200)

    fig, ax = plt.subplots(figsize=(6.2, 5.0))
    ax.plot([0, 1], [0, 1], color="0.6", lw=1.0, ls="--", label="identity")
    ax.plot(
        grid,
        [phi_from_rho(g, t_bar) for g in grid],
        color="C0",
        lw=1.8,
        label="closed-form map (t from mean miss rate)",
    )
    ax.scatter(
        [r["phi_bar"] for r in rows],
        [r["phi_err"] for r in rows],
        s=42,
        color="C3",
        zorder=5,
        label=f"simulated panel (n={N_DIM}, k={K}, unit-norm deviations)",
    )
    ax.set_xlabel(r"$\bar\phi_{geom}$ — mean $|\langle v_e, v_f\rangle|$")
    ax.set_ylabel(r"$\bar\phi_{err}$ — mean phi coefficient on miss indicators")
    ax.set_title("Geometric correlation vs error correlation")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend(fontsize=7.5, loc="upper left")
    ax.grid(alpha=0.25)
    fig.tight_layout()

    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "..", "output", "figures", "phi_geom_vs_phi_err.png")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, dpi=170)
    print(f"\n  figure -> output/figures/{os.path.basename(path)}")


if __name__ == "__main__":
    main()
