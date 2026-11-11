# Where to Invest Within the Firm — Companion Computation Scripts

Companion scripts for:

> Zharnikov, D. (2026). *Where to Invest Within the Firm: Organizational Tiers, Discount Rates, and AI Penetration.* Working Paper. https://doi.org/10.5281/zenodo.20072288

## What this reproduces

`back_of_envelope.py` reproduces every computed value in Part I (tier allocation):

- **Two-Tier Minimal Illustration** — Profile A/B/C $V_{LR}$ multipliers and the B/A, B/C and C/A multiple ratios under the maintained discounted Cobb-Douglas specification.
- **Sensitivity to r** — $V_{LR}(A)$, $V_{LR}(B)$ and the B/A ratio across r ∈ {.10, .15, .20}.
- **Alternative α_t calibrations** — baseline, conservative and concentrated-stock specifications.
- **Optimal dollar-weighted investment shares** $w_t^*(r) = \alpha_t / (\delta_t + r)$ and the comparative static for marketing flow.
- **CES robustness** at σ ∈ {.5, 1.0, 1.5}.
- **Figure 1** — iso-$V_{LR}$ contours over the ($w_4$, $w_6$) plane at r = .15, written to `../figures/tier_allocation_contour.png`.

`tier_penetration_simulation.py` reproduces every computed value in Part II (AI tier penetration): the AI-extended share rule with per-tier cost shocks $\gamma_t$ and durability shocks $\Delta_t$, the sign checks for Propositions 5–7, CES robustness, the α_t calibration sensitivity, and the boundary-object cases.

## How to run

```
uv run python back_of_envelope.py
uv run python tier_penetration_simulation.py
```

Python 3.10+. `back_of_envelope.py` needs scipy for the CES check and numpy + matplotlib for Figure 1; the other reproductions use the standard library only. `tier_penetration_simulation.py` needs numpy and scipy.

## Reproducibility

Both scripts are deterministic and read no external data files. `tier_penetration_simulation.py` sets `numpy.random.seed(42)` at module load. All parameters (decay rates δ_t, separability factors m_t, output elasticities α_t, profile w-vectors, AI shock vectors) are hard-coded constants matching the paper's calibration tables.

## File listing

- `back_of_envelope.py` — Part I reproductions and Figure 1
- `tier_penetration_simulation.py` — Part II reproductions
- `README.md` — this file

## License

MIT (see `LICENSE` at the repository root).
