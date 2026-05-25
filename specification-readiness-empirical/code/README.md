# Companion Code — Paper 2026an

This paper (Zharnikov 2026an) reuses the Monte Carlo and regression-identification simulation infrastructure of its foundational theoretical companion, [Zharnikov (2026am) Specification Readiness and Endogenous Friction](https://doi.org/10.5281/zenodo.20379981).

The five hypotheses H1–H5 share the underlying theoretical mechanism with the five comparative-statics propositions P1–P5 in 2026am, so the simulation infrastructure is reused without duplication.

## Where the code lives

Full code companion: [orgschema-papers/specification-readiness/code/](https://github.com/spectralbranding/orgschema-papers/tree/main/specification-readiness/code/)

## What the code does

- `friction_tax_montecarlo.py` — 12.96 million trials under fixed seed 20260525 confirming the friction-tax phase shift at α* ≈ .91; μ_push/μ_pull ≈ 19,993; Cohen's d ≈ 88.4.
- `push_pull_regression_sim.py` — pre-registered regression-identification simulation with 1,000 datasets per condition under H₀ and H₁; all H1–H5 power ≥ .80 at pre-registered effect sizes.
- `render_figure1.py` — matplotlib hub-and-spoke rendering of the Multi-Interface Specification Model diagram (shared between 2026am and 2026an).
- `PRE_EXPERIMENT_NOTES.md` / `POST_EXPERIMENT_REPORT.md` — anti-HARKing register + honest documentation of one post-hoc deviation in the cluster-robust SE specification.
- `plots/` — 12 plots (friction distribution; phase shift; sensitivity; functional-form comparison; H1–H5 power curves; null distribution QQ; effect-size sensitivity).
- `logs/` — verbatim stdout from both simulation runs (date-stamped).

## Run command

```
cd specification-readiness/code
bws run -- uv run python friction_tax_montecarlo.py
bws run -- uv run python push_pull_regression_sim.py
```

Expected outputs documented in the present paper's §Mechanism Tests section and in the foundational paper 2026am's §Mechanism Confirmation section.

## Reproducibility

Fixed seed 20260525. Python 3.12 + uv. Dependencies pinned in the parent `specification-readiness/code/` repository.

## Future archival code companion

When the archival panel implementation completes (future work; companion paper v2.0 / Paper C), the empirical-analysis code (Compustat / SEC EDGAR / Glassdoor / Burning Glass extraction; Callaway-Sant'Anna and Goodman-Bacon estimation; Oster δ-bound computation) will be added in a separate code directory for that follow-up paper.
