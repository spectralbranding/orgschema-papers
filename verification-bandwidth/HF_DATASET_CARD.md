---
license: cc-by-4.0
language:
  - en
tags:
  - verification
  - effective-sample-size
  - design-effect
  - evaluator-panels
  - correlated-errors
  - organizational-design
  - reproducibility
pretty_name: Verification Bandwidth Under Correlated Evaluators — derived results
size_categories:
  - n<1K
configs:
  - config_name: table1_bracket_width_vs_union_bound
    default: true
    data_files:
      - split: train
        path: tables/table1_bracket_width_vs_union_bound.csv
  - config_name: table3_reported_neff_vs_formula
    data_files:
      - split: train
        path: tables/table3_reported_neff_vs_formula.csv
  - config_name: table4_bracket_surviving
    data_files:
      - split: train
        path: tables/table4_bracket_surviving.csv
  - config_name: table5_dimensional_ceiling_typical
    data_files:
      - split: train
        path: tables/table5_dimensional_ceiling_typical.csv
  - config_name: table6_transferable_share
    data_files:
      - split: train
        path: tables/table6_transferable_share.csv
---

# Verification Bandwidth Under Correlated Evaluators — derived results

Derived numerical results for the paper **Verification Bandwidth Under Correlated Evaluators: What an Effective-Sample-Size Statistic Measures in an Acceptance Cascade**.

- Paper concept DOI: [10.5281/zenodo.21891435](https://doi.org/10.5281/zenodo.21891435)
- Paper version DOI (v1.0.0): [10.5281/zenodo.21891436](https://doi.org/10.5281/zenodo.21891436)
- Code: [github.com/spectralbranding/orgschema-papers/tree/main/verification-bandwidth/code](https://github.com/spectralbranding/orgschema-papers/tree/main/verification-bandwidth/code)
- This dataset's DOI: [10.57967/hf/9953](https://doi.org/10.57967/hf/9953)

## What this is, and what it is not

**This is not an observational dataset, and it should not be cited as evidence.** The paper collected no data. It is a theory-and-computation paper whose reported figures come from two places: arithmetic on summary statistics another study published, and seeded simulation of a stated model. This record is the *output* of that computation — the tables the paper prints, plus the captured stdout of every script that produced them.

Its purpose is auditability rather than reuse. A reader who wants to check a number in the paper against the code that produced it can diff this record instead of re-running anything; a reader who wants to re-run it can, from the repository above, with no network access and no key.

## Contents

| File | What it holds |
|---|---|
| `tables/table1_bracket_width_vs_union_bound.csv` | Exact bracket width against its union bound across the correlation range, with the looseness factor and whether the bound is informative at all |
| `tables/table3_reported_neff_vs_formula.csv` | The published nine-judge panel's reported effective sample sizes beside the design-effect formula evaluated at its own reported error correlations |
| `tables/table4_bracket_surviving.csv` | Percentage of the zero-correlation bracket width surviving at that panel's error correlations, bracketed over three marginal error rates |
| `tables/table5_dimensional_ceiling_typical.csv` | The typical-case dimensional ceiling: exact limit and its square-root asymptotic, by state-space dimension |
| `tables/table6_transferable_share.csv` | Transferable share and accountable-signatory residual under a correlated receiving panel |
| `logs/*.log` | Captured stdout of all six scripts, including the seeded Monte Carlo tables (paper Tables 2 and A1) that are deliberately not re-derived as CSV |
| `figures/*.png` | The map from inspection geometry to error correlation, and geometric against error correlation |

## Provenance and how to reproduce

Every value is produced by `reproduce.sh` in the repository above, which runs six scripts in dependency order. All fix `SEED = 20260811` at file top and exit nonzero if any internal check fails. The whole pipeline runs in well under a minute and requires only Python 3.12 with `numpy`, `scipy` and `matplotlib`.

```
git clone https://github.com/spectralbranding/orgschema-papers
cd orgschema-papers/verification-bandwidth
./reproduce.sh
```

Tables 2 and A1 and the worst-case block of Table 5 are seeded Monte Carlo. They appear here only as captured stdout, not as CSV, because emitting them would require a second implementation of a seeded simulation — the exact drift the paper's reproducibility standard exists to prevent. The script is the ground truth for any value the paper calls computed.

## Known limits of what these numbers mean

- **Table 3 is arithmetic on another study's published figures, not a re-analysis of its panel.** No raw judgements were obtained; the agreement it reports is between a formula and a published number.
- **Table 4 is model-dependent and directional.** The point inversion needs a marginal error rate the published record does not carry, so it is bracketed over three values rather than fixed, and no shared-difficulty correction is applied.
- **Table 6 rows are illustrative combinations**, not measurements of any organization, and are computed under one-dimensional inspection subspaces.
- The simulations assume isotropic deviations, rank-one inspection, and a miss-only error model with no false-alarm arm. Each is a stated scope condition of the paper, not a defect of this record.

## Citation

Cite the paper, not this record:

> Zharnikov, Dmitry (2026), *Verification Bandwidth Under Correlated Evaluators: What an Effective-Sample-Size Statistic Measures in an Acceptance Cascade.* Working Paper v1.0.0. DOI: 10.5281/zenodo.21891435

## License

CC BY 4.0. The code that produced these results is MIT, at the repository above.
