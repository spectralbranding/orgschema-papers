# Companion computation script — Verification as Operator (2026ae)

Companion code for *Verification as Operator: Spectral Projection, Rank Deficiencies, and the Persistence of the Audit Society* (Zharnikov 2026, DOI 10.5281/zenodo.19778588).

## Files

- `projection_simulation.py` — reproduces all numerical values reported in Figure 1, Appendix B Table 1, and the body discussion of the rank-1 versus full-rank cascade contrast.
- `simulation_results.json` — saved output (regenerated each run).

## Run command

```bash
uv run --with numpy python3 projection_simulation.py
```

Output is written to `simulation_results.json` in this directory and a summary is printed to stdout.

## Determinism

`np.random.seed(42)` is set at the top of the script. Output is byte-identical across runs. Tested on Python 3.12 + NumPy 2.x; no other dependencies.

## What the simulation reports

For each of four noise levels (sigma = .1, .5, 1.0, 2.0), N = 1,000 trials in a 6-dimensional state space (corresponding to OST L0–L5 cascade levels):

- mean total deviation `||x_obs − x_true||`
- mean undetected deviation under rank-1 audit (detects only dimension 0)
- mean undetected deviation under full-rank cascade (detects all 6 dimensions)
- percentage of total deviation missed by each architecture

The analytic prediction `sqrt(5) · sigma` for the rank-1 undetected norm is printed alongside the simulated mean for each sigma.

## Expected output (sigma = 1.0)

| Quantity                              | Value     |
|---------------------------------------|-----------|
| Mean total deviation                  | 2.3505    |
| Mean undetected — rank-1 audit        | 2.1247    |
| Mean undetected — full-rank cascade   | .0000     |
| Pct missed by rank-1 audit            | 90.4%     |
| Analytic prediction (sqrt(5) · sigma) | 2.2361    |

The 90% miss rate is geometric: under isotropic Gaussian noise, a rank-1 projection in d = 6 dimensions detects exactly 1/d = 16.7% of total deviation variance. The simulated norm-based ratio sits slightly above the variance ratio because we report `||r||` rather than `||r||²`.
