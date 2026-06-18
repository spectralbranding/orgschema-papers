# Tier-Allocation R-paper — Companion Computation Script

Companion script for:

> Zharnikov, D. (2026). *Tier-Allocation of Capital: A Theory of Investment-Tier Choice and Long-Run Firm Value.* Working Paper. https://doi.org/10.5281/zenodo.20072288

## What this reproduces

`back_of_envelope.py` reproduces every computed numerical value in the paper:

- **Section 4.2 Two-Tier Minimal Illustration** — Profile A/B/C V_LR multipliers and the Profile B/A multiple ratio.
- **Appendix A2 Sensitivity of V_LR Multiple Gap to r** — V_LR(A), V_LR(B), and the B/A ratio across r ∈ {.10, .15, .20}, computed under both the *bare* Cobb-Douglas (r-invariant; the published §3 specification) and a *discounted* Cobb-Douglas variant (the only specification that produces the slight r-variation reported in the published Appendix A2).
- **Appendix A3 Alternative α_t Calibrations** — baseline, conservative, and concentrated-stock specifications.

## How to run

```
uv run python back_of_envelope.py
```

(plain CPython 3.10+ also works — no external dependencies)

## Reproducibility

Fully deterministic. No RNG used. No external data files. All parameters (decay rates δ_t, separability factors m_t, output elasticities α_t, profile w-vectors) are hard-coded constants matching Table 1 + Section 3.2 + Section 4.2 of the paper.

## Discrepancies surfaced by this script

Running the script as of paper internal version v1.0.0 surfaces several discrepancies between the paper's reported numbers and the script's computed values. Each is a downstream consequence of the formal-model integrity question tracked as item C-r3-2 in `audit/reviews/REVIEW_PAPER_2026aj_r3.md`. They will be resolved in the next paper revision pass:

- **Profile C V_LR**: paper §4.2 reports 1.135; script computes 1.209 (rounding-chain artifact in the manual derivation).
- **B/C and C/A multiple ratios**: paper §4.2 reports 1.20× and 1.62×; script computes 1.122× and 1.721×.
- **Appendix A2 r-variation**: paper reports slight r-variation (.703 → .702 → .700 for Profile A across r ∈ {.10, .15, .20}); script confirms the bare Cobb-Douglas is r-invariant (.702 at all r). The paper's reported variation is consistent with an implicit discounted-Cobb-Douglas formulation that has not yet been formally derived in the body. Both specifications are tabulated in the script output.
- **Appendix A3 alternative α calibrations**: paper reports baseline 1.93× / conservative 1.48× / concentrated-stock 2.74×; script computes 1.93× / 1.55× / 2.39×. Conservative and concentrated cells differ by ~5-15%.

These discrepancies are precisely the value of publishing companion computation scripts: they convert opaque manual arithmetic into reproducible code that any reader (or referee) can re-run.

## File listing

- `back_of_envelope.py` — main script (deterministic, all reproductions)
- `README.md` — this file

## License

Public domain (CC0). Re-use without attribution is permitted; citation of the paper is appreciated.
