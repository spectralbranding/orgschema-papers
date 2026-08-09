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

## Zero-activity placebo (added 2026-08-09)

The paper's sixth robustness check, executed rather than pre-registered. Inputs are **public SEC
filings only** — no licence, no authentication — so unlike the simulation companion this run is
reproducible end to end by anyone.

- `PRE_EXPERIMENT_NOTES.md` — written **before** the run and not amended after it. Fixes the measure
  (the published index, unchanged and not tunable), both panel screens, the decision rule in the
  paper's own words, and three robustness arms.
- `zero_activity_placebo.py` — the run. 30 zero-activity filers (blank-cheque classification, no
  revenue reported in either fiscal year) against 20 matched operating filers (revenue above $50M in
  both, same fiscal years). Model pinned literally; a newer embedding model is a reason to keep the
  pin, not to change it.
- `ceiling_diagnostic.py` — **post-hoc**, and labelled so in its own docstring. Asks whether the
  index can separate any two filings, by scoring 200 pairs of unrelated firms.
- `POST_EXPERIMENT_REPORT.md` — the result, the deviation log, and what the run does and does not
  establish.
- `results.json`, `ceiling_diagnostic.json`, `panel_zero.csv`, `panel_operating.csv` — outputs.

**Result in one line**: the predicted direction was not observed — zero-activity filers scored .997
against .999 for matched operating firms, verdict inconclusive against the pre-registered rule — and
the diagnostic that followed found the index's working range to be roughly the top two percent of its
scale.

### Run

```
uv run --with torch --with transformers python zero_activity_placebo.py
uv run --with torch --with transformers python ceiling_diagnostic.py
```

Fixed seed 20260809. The first run is network-bound (it fetches and caches filings); re-runs are not.
The filing cache is git-ignored and rebuilds itself.
