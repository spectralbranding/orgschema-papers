# Companion computation scripts -- Zharnikov 2026am

Companion code for:

> Zharnikov, D. (2026). *Specification Readiness and Endogenous Friction:
> An Information-Theoretic Theory of Multi-Interface Organizational
> Architecture*. Working paper 2026am.

**Scope note**: This repository serves two papers. It is the primary
numerical-coherence reference for the pure-theory paper 2026am (Specification
Readiness and Endogenous Friction). The operational empirical hypotheses
derived from that theory are developed in companion empirical work (in
preparation), which will reference this repository as its primary
computational instrument.

Per PAPER_QUALITY_STANDARDS items 37a-37e, every computed numerical value
cited in the paper must be reproducible from a script in this directory
with a fixed seed and a documented run command.

---

## Files in this directory

| File | Purpose |
|---|---|
| `friction_tax_montecarlo.py` | Section A: Monte Carlo simulation of friction-tax dynamics under push and pull regimes |
| `push_pull_regression_sim.py` | Section B: Regression identification simulation for propositions P1-P5 |
| `PRE_EXPERIMENT_NOTES.md` | Anti-HARKing artifact: verbatim copy of pre-registered hypotheses, effect sizes, and decision rules -- committed before any execution |
| `POST_EXPERIMENT_REPORT.md` | Actual results vs pre-registered expectations: PASS/FAIL per criterion, deviations recorded |
| `monte_carlo_summary.csv` | Aggregated Monte Carlo results (one row per parameter cell) |
| `regression_simulation_summary.csv` | Aggregated regression simulation results (one row per proposition x condition x specification) |
| `plots/friction_distribution_push_vs_pull.png` | Push vs pull friction-tax density at baseline parameters |
| `plots/phase_shift_alpha.png` | F(alpha)/F(0) vs alpha for multiple sigma values |
| `plots/sensitivity_misalignment.png` | Push/pull ratio vs sigma (log-scale y-axis) |
| `plots/functional_form_comparison.png` | Cohen's d vs sigma across three functional forms |
| `plots/power_curve_P1.png` -- `plots/power_curve_P5.png` | Power curves for each proposition |
| `plots/null_distribution_qq.png` | QQ plots of t-statistics under H0 vs N(0,1) |
| `plots/effect_size_sensitivity.png` | Point estimates and 95% CIs under H1 vs pre-registered expectations |
| `logs/monte_carlo_run_<YYYYMMDD>.log` | Verbatim stdout from Monte Carlo run |
| `logs/regression_simulation_run_<YYYYMMDD>.log` | Verbatim stdout from regression simulation run |

---

## Quickstart

```
uv run --with numpy==2.2.2 --with scipy==1.14.0 --with statsmodels==0.14.4 \
       --with matplotlib==3.10.0 --with pandas==2.2.3 \
       python friction_tax_montecarlo.py

uv run --with numpy==2.2.2 --with scipy==1.14.0 --with statsmodels==0.14.4 \
       --with matplotlib==3.10.0 --with pandas==2.2.3 \
       python push_pull_regression_sim.py
```

Both scripts are fully self-contained: no network calls, no external data,
no API keys. All inputs are generated from the fixed seed.

---

## Required dependencies (pinned)

```
numpy==2.2.2
scipy==1.14.0
statsmodels==0.14.4
matplotlib==3.10.0
pandas==2.2.3
```

Python version: 3.12 (required).

---

## Reproduction recipe

1. Confirm Python 3.12 is active.
2. Run `friction_tax_montecarlo.py` with the exact command above (fixed seed
   `np.random.seed(20260525)` is set at module top).
3. Run `push_pull_regression_sim.py` with the exact command above (same seed).
4. Outputs are deterministic; minor floating-point differences across platforms
   (order 1e-9) do not affect aggregate statistics.
5. Compare output CSVs to the versions committed alongside the Zenodo v1 upload.

Expected runtimes on a 2024 Apple Silicon Mac:
- `friction_tax_montecarlo.py`: 8-12 minutes (4,320,000 individual measurements)
- `push_pull_regression_sim.py`: 15-20 minutes (5 propositions x 2 conditions x
  1,000 simulated datasets)
- Total: under 35 minutes

---

## Output artifact inventory

**Monte Carlo outputs** (from `friction_tax_montecarlo.py`):

- `monte_carlo_summary.csv`: 432 rows (6 sigma x 4 N x 6 alpha x 3 functional
  forms) x 3 sigma_query multipliers = 1,296 rows total. Columns: sigma, N,
  alpha, functional_form, sigma_query_mult, mu_push_mean, mu_push_sd,
  mu_push_p25, mu_push_p975, mu_pull_mean, mu_pull_sd, mu_pull_p25,
  mu_pull_p975, mu_alpha_mean, cohens_d, ratio_push_pull, n_trials.
- `plots/friction_distribution_push_vs_pull.png`
- `plots/phase_shift_alpha.png`
- `plots/sensitivity_misalignment.png`
- `plots/functional_form_comparison.png`

**Regression simulation outputs** (from `push_pull_regression_sim.py`):

- `regression_simulation_summary.csv`: 10 rows (5 propositions x 2
  specifications: primary + no-FE alternative). Columns: proposition,
  condition, specification, power, type1_error, mean_point_estimate,
  sd_point_estimate, pct_in_plausible_range, pct_correct_sign_h1,
  pre_reg_beta, pre_reg_cohens_d.
- `plots/power_curve_P1.png` through `plots/power_curve_P5.png`
- `plots/null_distribution_qq.png`
- `plots/effect_size_sensitivity.png`

---

## Pre-registration and anti-HARKing

- `PRE_EXPERIMENT_NOTES.md` was committed before any simulation execution.
  It records the verbatim pre-registered hypotheses, effect sizes, and
  decision rules from `METHODS_APPENDIX.md`.
- `POST_EXPERIMENT_REPORT.md` was written after execution and records the
  actual results vs pre-registered expectations, with explicit PASS/FAIL
  verdicts and any deviations from the pre-registration.
- The fixed seed `np.random.seed(20260525)` may not be changed to obtain
  more favorable results. Any post-execution modification requires a dated
  changelog entry in `METHODS_APPENDIX.md`.

---

## Companion script subsection in the paper

The paper body "Companion Computation Script" subsection references this
directory at:

```
https://github.com/spectralbranding/orgschema-papers/tree/main/specification-readiness/code/
```

(URL confirmed at Zenodo v1 upload time; placeholder until then.)

Run command as it will appear in the paper:

```
uv run --with numpy==2.2.2 --with scipy==1.14.0 --with statsmodels==0.14.4 \
       --with matplotlib==3.10.0 --with pandas==2.2.3 \
       python friction_tax_montecarlo.py && python push_pull_regression_sim.py
```

---

## Scope

These simulations are numerical-coherence checks for the formalism developed
in the paper. They demonstrate that the formal model is internally consistent
across the specified parameter space. They do not constitute empirical
confirmation in real firms. Real-firm confirmation requires the archival panel
study described in the paper's empirical strategy section.

---

## License

MIT. Open-source under MIT license, matching the paper's public mirror license.
