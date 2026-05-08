# AI Tier Penetration (2026ak)

**Title**: AI Tier Penetration: A Theory of Substrate-Dependent Competitive Advantage

**Author**: Dmitry Zharnikov ([ORCID 0009-0000-6893-9231](https://orcid.org/0009-0000-6893-9231))

**Citation key**: 2026ak

**Status**: Working paper v1.0.0 published on Zenodo 2026-05-08. Target venue: Strategic Management Journal (primary); Management Information Systems Quarterly and Academy of Management Review as alternates.

**DOI**: [10.5281/zenodo.20087036](https://doi.org/10.5281/zenodo.20087036) (concept) | [10.5281/zenodo.20087037](https://doi.org/10.5281/zenodo.20087037) (v1)

## What this paper does

Two firms operating in the same sector announce equal-magnitude AI investments in the same fiscal year. Each commits an identical fraction of operating budget to large-language-model deployment. Each reports comparable contemporaneous productivity gains in the same earnings cycle. Three years later, one firm trades at a forward multiple roughly twice the other's, and acquirers in the sector treat the two firms as structurally non-comparable in due diligence. No standard AI-and-strategy framework predicts this divergence.

This paper formalizes why. AI output either accumulates as durable organizational substrate or is consumed as accelerated flow. The difference is governed by the tier of deployment within a six-tier architecture ordered by transferability under M&A separation. The paper extends the tiered capital-allocation model of Zharnikov (2026aj) with per-tier cost shocks (γ_t) and durability shocks (Δ_t), yielding the generalized closed-form share rule:

**w_t*(r; γ, Δ) = α_t / [γ_t · (δ_t^eff + r)]**

where δ_t^eff = δ_t^0 − Δ_t is the effective decay rate under AI-driven durability improvement.

## Three contributions

1. **The Tier-6 Over-Allocation Paradox (P1).** Surface-tier (Tier 6) cost reductions raise short-run earnings yet lower long-run M&A multiples by shifting optimal allocation toward the lowest-persistence tier. The diagnostic signature: positive contemporaneous EBIT shifts alongside negative 36-month forward M&A-multiple shifts, in firms deploying AI exclusively at Tier 6.

2. **The Substrate-Building Threshold at Tier 4 (P2).** Durable value creation requires crossing a discrete threshold from API-rented capacity (Δ_4 = 0) to proprietary or strongly embedded configurations (Δ_4 > 0). The threshold produces a level shift in M&A multiples rather than a continuous slope shift — structurally distinct from continuous-intangibles specifications in the existing literature.

3. **The Horizon-Conditional Sign Flip (P3).** AI's net value effect flips sign with the principal's effective discount rate. Deep-tier deployments that codify tacit knowledge extend founder horizon (lower r) and reinforce substrate accumulation; surface deployments compressed by algorithmic-feedback loops raise r and erode substrate. The mechanism formally connects to the automation-augmentation paradox of Raisch and Krakowski (2021).

The AI Tier Penetration Curve (Stage 0 pre-deployment through Stage 5 asymptotic ceiling) translates the cross-sectional comparative statics of P1-P3 into a temporal stage trajectory, serving as the surface-to-deep temporal counterpart to the Tier-Rotation Curve (Zharnikov 2026ai).

## Files

- `paper.md` -- full paper (~13,100 words body; ~58 references; 3 propositions; 4 tables; Appendix A self-contained re-derivation)
- `supplement.md` -- Online Supplement S1-S5 (Lagrangian derivation, CES robustness, alpha calibration sensitivity, identification strategy, companion-script documentation)
- `paper.yaml` -- paper-spec schema (citation key, propositions, falsification criteria, dependencies, AI disclosure, review history)
- `CITATION.cff` -- citation file (CITATION File Format 1.2.0)
- `CONTRIBUTORS.yaml` -- verified contributor attribution
- `PROVENANCE.yaml` -- version history and submission records
- `code/tier_penetration_simulation.py` -- companion computation script (deterministic; reproduces all numerical values; run: `uv run python tier_penetration_simulation.py`)

## Related work

This paper is part of the SBT-OST cross-cutting series on organizational tier structure, capital allocation, and competitive advantage:

- The generalized share rule w_t*(r; γ, Δ) extends the base model in: [Zharnikov (2026aj) Where to Invest Within the Firm](https://doi.org/10.5281/zenodo.20072288).
- The six-tier ontology and architectural-transferability cut-point criterion inherited from: [Zharnikov (2026ag) Dual Hierarchies of Organizational Transferability](https://doi.org/10.5281/zenodo.19895813).
- The Tier-Rotation Curve as temporal companion to the AI Tier Penetration Curve: [Zharnikov (2026ai) The Tier-Rotation Curve](https://doi.org/10.5281/zenodo.20069605).
- Brand-as-Tier-4 projection establishing the Tier-4 substrate-accumulation pattern: [Zharnikov (2026ah) Brand as Tier-4 Projection](https://doi.org/10.5281/zenodo.19930157).

## How to cite

```
Zharnikov, Dmitry (2026), "AI Tier Penetration: A Theory of Substrate-Dependent Competitive Advantage," Working Paper v1.0.0, Zenodo, doi:10.5281/zenodo.20087036.
```

## License

Creative Commons Attribution 4.0 International (CC BY 4.0).
