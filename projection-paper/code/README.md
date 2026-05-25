# Projection Cascade Paper — Companion Computation Script

## What this reproduces

`cascade_numerical_example.py` reproduces all numerical values cited in §3.5 (Numerical Illustration of Theorem 1) of:

> Zharnikov, D. (2026). The Projection Cascade: Why Reorganizations Fail When the Specification Cascade Doesn't. Working Paper v2.0.0.

Specifically:

- **Table 2** (per-junction cascade statistics): d_i, d_{i+1}, rank(Pi_{i->i+1}), r_i, kappa_i, L_i, iteration counts, ||x_{i+1}^* - x_{i+1}^{(0)}|| for i = 1..5.
- **Sub-additivity verification of Corollary 1**: r_total = 2, sum_i r_i = 3, strict-inequality status (gap = 1).
- **Cascade Lipschitz bound of Theorem 1**: product_{j=1}^{5} L_j / (1 - kappa_j) = 3056.11.
- **Maximum fixed-point residual** across the cascade: 2.38e-11 (tolerance 1e-10).

## Run commands

```
uv run --with numpy python code/cascade_numerical_example.py
```

For the §4.6 comparative-statics experiment (cascade vs. Galbraith / Williamson / Mintzberg / Puranam restrictions):

```
uv run --with numpy python code/cascade_numerical_example.py --compare
```

Requires: Python 3.12+, numpy. No proprietary data. Fixed seed `SEED = 2026`.

## Zenodo DOI

Paper v1 (preserved): [10.5281/zenodo.19145205](https://doi.org/10.5281/zenodo.19145205).
Paper v2.0.0 concept DOI: [10.5281/zenodo.19145205](https://doi.org/10.5281/zenodo.19145205).
Public mirror: https://github.com/spectralbranding/orgschema-papers/tree/main/projection-paper/

## Method

Six-tier cascade with dimensions (4, 4, 3, 3, 2, 2). Pi_{i->i+1} matrices are deterministic draws from `numpy.random.default_rng(2026)`; Pi_{1->2} is constructed rank-deficient (rank 3, not 4) to demonstrate Corollary 1's strict-inequality scenario. Each A_{i+1->i} is rescaled so that ||Pi composed with A||_op equals a target kappa_i in {.30, .40, .50, .35, .45}, satisfying Theorem 1 condition (C_i). Per-junction parameter-Lipschitz constants L_i are derived analytically as ||(I - Pi composed with A) composed with Pi||_op, satisfying (C_i'). The cascade is iterated junction-by-junction from a normalized x_1 in B_1 with tolerance 1e-10 on successive-iterate distance.

The `--compare` flag builds the five design-theory restrictions (Full cascade, Galbraith-restricted, Williamson-restricted, Mintzberg-restricted, Puranam-restricted) on the same seed-2026 cascade and prints the comparative-statics table from §4.6, showing that no single restriction simultaneously achieves the full cascade's P3 amplification product and P4 strict-inequality regime.
