# Computation scripts

Companion code for **Verification Bandwidth Under Correlated Evaluators: What an Effective-Sample-Size Statistic Measures in an Acceptance Cascade**.

Concept DOI: [10.5281/zenodo.21891435](https://doi.org/10.5281/zenodo.21891435) · version v1.0.0: [10.5281/zenodo.21891436](https://doi.org/10.5281/zenodo.21891436)

Every numerical value the paper reports is produced here. The paper collected no dataset: its figures are either arithmetic on another study's published summary statistics or seeded simulation, so reproduction needs no network access, no provider key and no data download.

**Run everything from the paper root:**

```
./reproduce.sh
```

That runs the scripts in the order below, captures each one's stdout to `../output/logs/`, and writes the machine-readable tables to `../output/tables/` and the figures to `../output/figures/`. Every script fixes `SEED = 20260811` at file top and exits nonzero if any of its internal checks fails, so the orchestrator cannot pass on a silent numerical regression.

## What each script reproduces

| Script | Reproduces | Run command |
|---|---|---|
| `reported_neff_check.py` | **Table 3.** That the published nine-judge panel's reported effective sample sizes are the design-effect formula evaluated at its own reported error correlations, to three decimals in all four conditions, and that its independence ratio is that value over the panel size. Deterministic; no RNG. | `uv run --with numpy --with scipy python reported_neff_check.py` |
| `phi_mapping.py` | **Table 2** and both figures. The closed-form map from inspection geometry to error correlation; its evenness, monotonicity, endpoints, quadratic behaviour at the origin and attenuation; the shared-item-difficulty decomposition; and panel recovery to within .0008. | `uv run --with numpy --with scipy --with matplotlib python phi_mapping.py` |
| `p2_exact.py` | **Table 1** and **Table 4.** The exact single-factor bracket width by dense fixed-grid quadrature, checked against Monte Carlo to within .0021, the union bound's looseness factor, and the cross-check against `phi_mapping.py`'s independent implementation to 2.5 × 10⁻¹⁴. | `uv run --with numpy --with scipy python p2_exact.py` |
| `formal_model_checks.py` | The proposition checks, and the worst-case block of **Table 5.** Random-rule checks on the bracket over all 2⁵ input vectors for 400 rules; the correlation sweep; the exact and typical dimensional ceilings. | `uv run --with numpy --with scipy python formal_model_checks.py` |
| `threat1_kill_test.py` | **Table A1.** The bracket simulation: detection rates for the disjunctive, majority, unanimous and single-evaluator rules across the correlation range, at 200,000 deviations per row. | `uv run --with numpy python threat1_kill_test.py` |
| `emit_paper_tables.py` | A CSV projection of the deterministic tables (1, 3, 4, 5-typical, 6), so the paper can be diffed against its own derivations mechanically. Computes nothing itself — every value comes from the function in the script that owns it. | `uv run --with numpy --with scipy python emit_paper_tables.py` |

Tables 2 and A1 and the worst-case block of Table 5 are seeded Monte Carlo and are deliberately **not** re-derived by the CSV emitter: a second implementation of a seeded simulation is exactly the drift that standard exists to prevent. Their record is the captured stdout in `../output/logs/`.

## Two notes that affect reproduction

**The quadrature is a dense fixed grid, deliberately.** The one-dimensional integrals in `p2_exact.py` are evaluated on a fixed grid over ±12σ rather than by Gauss–Hermite quadrature, which is unstable at the node counts this integrand wants and can return NaN weights without raising. The Monte Carlo comparison in that script's first check is what certifies the grid; a substitution back to Gauss–Hermite will not reproduce the published tables.

**`reported_neff_check.py` is a boundary guard, not a result.** It checks that the published nine-judge panel's reported effective sample sizes are the design-effect formula at its own reported error correlations. The paper therefore cites that estimator rather than claiming it, and this script is what keeps that boundary checkable rather than asserted.

## Environment

Python 3.12; `numpy`, `scipy`, and `matplotlib` for the figures only. `uv` resolves dependencies per script, so nothing is installed globally; any Python 3.12 environment carrying those three packages will also run each script directly.

## License

Code in this directory is MIT (see `LICENSE` at the repository root). Generated tables, figures and logs under `../output/` are CC BY 4.0 (see `LICENSE-data`).
