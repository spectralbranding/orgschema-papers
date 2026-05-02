"""Companion computation script for:
Zharnikov (2026af) — Organizational Metamerism: Observer-Relative State
Equivalence in Organizational Configurations

Reproduces the illustrative set-size dynamics underlying Table 2 and
Appendix A (Figure A1 in standalone outputs). Specifically:

    - |M(P,O)| growth as coordination-cost burden c(P) falls (P2 prediction)
    - |M(P,O)| contraction as tacit-knowledge intensity τ(P) rises (P4 boundary)
    - Observer-relativity: M(P,O1) vs M(P,O2) for two observer types

Run command:
    uv run --with numpy,matplotlib python metamerism_set_simulation.py

Outputs:
    stdout — three tables matching the directional claims in Appendix A
    metamerism_set_growth.png — Figure A1 (optional; requires matplotlib)

Seeds:
    SEED = 42
"""

import math
import sys

SEED = 42

# ---------------------------------------------------------------------------
# Core model
# ---------------------------------------------------------------------------

def metamerism_set_size(codifiability: float,
                        coord_cost: float,
                        tacit_intensity: float,
                        scale: float = 100.0) -> float:
    """Schematic set-size function from Appendix A.

    |M(P,O)| = scale * codifiability / (coord_cost * (1 + tacit_intensity))

    Parameters
    ----------
    codifiability : float in [0, 1]
        Fraction of process steps with explicit specifications.
    coord_cost : float > 0
        Coordination cost per coordinating relation (lower = AI-era).
    tacit_intensity : float in [0, 1]
        Proportion of P's coordinating work requiring uncodifiable knowledge.
    scale : float
        Normalizing constant; sets the maximum observable set size.

    Returns
    -------
    float
        Theoretical cardinality of M(P, O) (continuous approximation).
    """
    if coord_cost <= 0:
        raise ValueError("coord_cost must be positive")
    raw = scale * codifiability / (coord_cost * (1.0 + tacit_intensity))
    return round(raw, 2)


# ---------------------------------------------------------------------------
# Simulation 1: Set expansion as coordination cost falls (P2 / P3)
# ---------------------------------------------------------------------------

def sim_coord_cost_sweep():
    """Table A1 — |M| as c(P) falls from 1.0 (high-cost) to 0.05 (AI-era).

    Fixed: codifiability = 0.8, tacit_intensity = 0.1
    Prediction: set grows monotonically.
    """
    codifiability = 0.8
    tacit = 0.1
    costs = [1.0, 0.8, 0.5, 0.3, 0.2, 0.1, 0.05]

    print("Table A1: Set expansion as coordination cost falls")
    print("  (codifiability=0.80, tacit_intensity=0.10)")
    print(f"  {'c(P)':>8}  {'|M(P,O)|':>10}")
    print("  " + "-" * 22)
    for c in costs:
        size = metamerism_set_size(codifiability, c, tacit)
        print(f"  {c:>8.2f}  {size:>10.1f}")
    print()


# ---------------------------------------------------------------------------
# Simulation 2: Tacit boundary (P4)
# ---------------------------------------------------------------------------

def sim_tacit_boundary():
    """Table A2 — |M| across tacit intensity levels at low vs high coord cost.

    Fixed: codifiability = 0.8
    Two coord-cost regimes: c=1.0 (pre-AI), c=0.1 (AI-era).
    Prediction: high-tacit narrows the set in both regimes;
                the floor is tighter in the AI era but never reaches zero.
    """
    codifiability = 0.8
    tacit_values = [0.0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0]
    c_high = 1.0
    c_low  = 0.1

    print("Table A2: Tacit knowledge boundary on set expansion (P4)")
    print("  (codifiability=0.80)")
    print(f"  {'τ(P)':>8}  {'|M| c=1.0':>12}  {'|M| c=0.1':>12}")
    print("  " + "-" * 36)
    for tau in tacit_values:
        hi = metamerism_set_size(codifiability, c_high, tau)
        lo = metamerism_set_size(codifiability, c_low, tau)
        print(f"  {tau:>8.2f}  {hi:>12.1f}  {lo:>12.1f}")
    print()


# ---------------------------------------------------------------------------
# Simulation 3: Observer-relativity — M(P,O1) ≠ M(P,O2)
# ---------------------------------------------------------------------------

def sim_observer_relativity():
    """Table A3 — Two observer types across the same process portfolio.

    Observer O1: technically oriented buyer (only evaluates output quality)
        → high effective codifiability weighting, low form sensitivity
    Observer O2: institutional actor (evaluates form for legitimacy signals)
        → lower effective codifiability weight (form matters independently)

    Modeled by a form-sensitivity discount on codifiability for O2:
        effective_codifiability = codifiability * (1 - form_sensitivity)

    Prediction: |M(P,O1)| > |M(P,O2)| across all process types.
    """
    processes = [
        ("API-first software",     0.95, 0.05),
        ("Agile development",       0.70, 0.20),
        ("Legal services",          0.40, 0.60),
        ("Strategic consulting",    0.25, 0.80),
        ("Scientific R&D",          0.20, 0.85),
    ]
    c = 0.3           # moderate AI-era coordination cost
    form_sensitivity_O2 = 0.5   # O2 discounts 50% of codifiability via form norms

    print("Table A3: Observer-relativity — M(P,O1) vs M(P,O2)")
    print("  (coord_cost=0.30; O1=technical buyer; O2=institutional actor)")
    print(f"  {'Process':28}  {'|M(P,O1)|':>10}  {'|M(P,O2)|':>10}  {'Ratio O1/O2':>12}")
    print("  " + "-" * 66)
    for name, cod, tau in processes:
        o1 = metamerism_set_size(cod, c, tau)
        cod_o2 = cod * (1.0 - form_sensitivity_O2)
        o2 = metamerism_set_size(cod_o2, c, tau)
        ratio = round(o1 / o2, 2) if o2 > 0 else float("inf")
        print(f"  {name:28}  {o1:>10.1f}  {o2:>10.1f}  {ratio:>12.2f}")
    print()


# ---------------------------------------------------------------------------
# Optional: matplotlib figure (skipped gracefully if not installed)
# ---------------------------------------------------------------------------

def plot_if_available():
    try:
        import numpy as np
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        costs = np.linspace(1.0, 0.01, 200)
        tau_values = [0.0, 0.2, 0.5, 0.8]
        cod = 0.8

        fig, ax = plt.subplots(figsize=(7, 4))
        for tau in tau_values:
            sizes = [metamerism_set_size(cod, c, tau) for c in costs]
            ax.plot(costs, sizes, label=f"τ = {tau:.1f}")

        ax.set_xlabel("Coordination cost c(P)")
        ax.set_ylabel("|M(P,O)| — metamerism set size")
        ax.set_title("Figure A1: Set expansion as coordination cost falls\n"
                     "(codifiability = 0.80; curves by tacit intensity τ)")
        ax.invert_xaxis()
        ax.legend(title="Tacit intensity τ(P)")
        plt.tight_layout()
        plt.savefig("metamerism_set_growth.png", dpi=150)
        print("Figure saved: metamerism_set_growth.png")
    except ImportError:
        print("matplotlib/numpy not available — skipping figure output.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 68)
    print("Organizational Metamerism — Companion Computation Script")
    print("Zharnikov (2026af) | DOI: 10.5281/zenodo.19869871")
    print("=" * 68)
    print()
    sim_coord_cost_sweep()
    sim_tacit_boundary()
    sim_observer_relativity()
    plot_if_available()
    print("Done. All tables reproduced successfully.")
