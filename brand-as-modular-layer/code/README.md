# Companion Computation Scripts — Brand as a Modular Layer (2026ah)

Reproducibility scripts for:

> Zharnikov, D. (2026). *Brand as a Modular Layer: Tiered Organizational Architecture, Separability, and Firm Performance in Multi-Brand Strategies*. Working Paper. https://doi.org/10.5281/zenodo.19930157

## Contents

- `v_parameter.py` — Computes the V parameter (Tier-3-visibility-in-Tier-4) for a set of Tier-4 brand instances. Worked examples for Virgin (branded house), Toyota/Lexus (sub-brand), Marriott (endorsed), and P&G (house of brands).
- `mbcd_scorer.py` — Multi-Brand Capacity Diagnostic scorer. Inputs are per-tier separability scores (1-5) plus V; output is predicted multi-brand capacity. Six worked firm audits.

## Run

```bash
uv run python v_parameter.py
uv run python mbcd_scorer.py
```

Plain CPython 3.10+ also works; no third-party dependencies.

## Output (sample)

`v_parameter.py` produces V = 1.000 (Virgin), V ≈ 0.467 (Toyota), V ≈ 0.333 (Marriott), V = 0.000 (P&G), and assigns each to the corresponding architecture class threshold.

`mbcd_scorer.py` produces capacity headroom estimates, e.g., +94 brands for P&G at current high separability, BLOCKED for a founder-led firm with Tier-1 bound to a single brand.

## Limitations

The composite formulas (V weights, MBCD geometric-mean rescaling, λ_V tuning) are illustrative defaults. Empirical recalibration on a multi-firm panel is part of the validation roadmap (P1, P3, P7 in the paper).

## License

Code: MIT (matches Zenodo deposit). Paper: CC BY 4.0.
