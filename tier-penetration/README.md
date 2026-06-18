# AI Tier Penetration (2026ak)

[![MIT License](https://img.shields.io/badge/Code-MIT-blue.svg)](../LICENSE)
[![CC-BY 4.0](https://img.shields.io/badge/Data-CC--BY_4.0-lightgrey.svg)](../LICENSE-data)
![Last Updated](https://img.shields.io/badge/updated-2026--05--29-success)

**Title**: AI Tier Penetration: A Theory of Substrate-Dependent Competitive Advantage

**Author**: Dmitry Zharnikov ([ORCID 0009-0000-6893-9231](https://orcid.org/0009-0000-6893-9231))

**Citation key**: 2026ak

**Status**: Working paper v1.0.0 published on Zenodo 2026-05-08.

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

## Related work

This paper is part of the Organizational Schema Theory (OST) cross-cutting series on organizational tier structure, capital allocation, and competitive advantage:

- The generalized share rule w_t*(r; γ, Δ) extends the base model in: [Zharnikov (2026aj) Where to Invest Within the Firm](https://doi.org/10.5281/zenodo.20072288).
- The six-tier ontology and architectural-transferability cut-point criterion inherited from: [Zharnikov (2026ag) Dual Hierarchies of Organizational Transferability](https://doi.org/10.5281/zenodo.19895813).
- The Tier-Rotation Curve as temporal companion to the AI Tier Penetration Curve: [Zharnikov (2026ai) The Tier-Rotation Curve](https://doi.org/10.5281/zenodo.20069605).
- Brand-as-Tier-4 projection establishing the Tier-4 substrate-accumulation pattern: [Zharnikov (2026ah) Brand as Tier-4 Projection](https://doi.org/10.5281/zenodo.19930157).

---

## 1 | Getting Started

This slug holds a theory paper with a companion deterministic simulation script. Python 3.12+ with [`uv`](https://docs.astral.sh/uv/) is the supported environment. Hub-level anchors (`pyproject.toml`, `LICENSE`, `LICENSE-data`, `.gitignore`) are inherited from `orgschema-papers/` root.

## 2 | Project Layout

```
tier-penetration/
├── README.md                    # this file
├── paper.md                     # full paper (~13,100 words; 3 propositions; 4 tables)
├── supplement.md                # Online Supplement S1-S5
├── paper.yaml                   # paper-spec schema (citation key, propositions, dependencies)
├── CITATION.cff                 # machine-readable citation (CFF 1.2.0)
├── CONTRIBUTORS.yaml            # verified contributor attribution
├── PROVENANCE.yaml              # version history and submission records
├── code/
│   └── tier_penetration_simulation.py   # deterministic companion script
└── figures/                     # generated figures (gitkeep placeholder)
```

## 3 | Quick Start

Reproduce all numerical anchors in the paper (P1 paradox magnitude, CES B/A robustness across σ ∈ {.5, 1.0, 1.5}, P3 horizon comparative statics):

```bash
uv run python code/tier_penetration_simulation.py
```

Key anchor values reproduced by the script (per `paper.yaml § verification`):

- S3 Baseline: dollar_share_6*(γ_6=.8) = .065; B/A = 1.93; paradox_mag = .076
- S3 Conservative: dollar_share_6*(γ_6=.8) = .112; B/A = 1.55; paradox_mag = .124
- S3 Concentrated: dollar_share_6*(γ_6=.8) = .027; B/A = 2.39; paradox_mag = .033
- CES B/A at σ=.5 = 1.22; σ=1.0 = 1.93; σ=1.5 = 2.17
- P3 ordering dollar_share_6*(r=.10) < (r=.15) < (r=.20) confirmed

## 4 | Dependencies

- Python ≥ 3.12
- numpy, scipy (standard scientific stack; resolved automatically by `uv run`)

The script is deterministic with no external data inputs; outputs are reproducible from the closed-form derivations in Online Supplement S1.

## 5 | Citation

```
Zharnikov, Dmitry (2026), "AI Tier Penetration: A Theory of Substrate-Dependent Competitive Advantage," Working Paper v1.0.0, Zenodo, doi:10.5281/zenodo.20087036.
```

Machine-readable citation in [CITATION.cff](CITATION.cff).

## 6 | Licence

Code (if any): MIT — see hub-level [../LICENSE](../LICENSE). Data, figures, tables: CC BY 4.0 — see hub-level [../LICENSE-data](../LICENSE-data). Paper text: CC BY 4.0 (see [CITATION.cff](CITATION.cff)).

---

*Last updated: 2026-05-29*
