[![MIT License](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)
[![CC-BY 4.0](https://img.shields.io/badge/Data-CC--BY_4.0-lightgrey.svg)](LICENSE-data)
![Last Updated](https://img.shields.io/badge/updated-2026--07--03-success)

# Organizational Schema Theory -- Research Papers

Research publications on Organizational Schema Theory (orgschema), a reverse-design TDD methodology for business operations. Businesses are designed backward from desired customer experience through testable, version-controlled specifications where each operational layer validates the layer above it.

## Papers

| Paper | Status |
|-------|--------|
| [The Organizational Schema Theory: Test-Driven Business Design](organizational-schema-theory/paper.md) | Working paper v1.3.0, Apr 2026 — [DOI](https://doi.org/10.5281/zenodo.18946043) |
| [The OrgSchema Audit: A Six-Level Diagnostic for Specification-Driven Organizations](orgschema-audit/paper.md) | Working paper v1.0.0, Apr 2026 — [DOI](https://doi.org/10.5281/zenodo.19555201) |
| [The Projection Cascade: Why Reorganizations Fail When the Specification Cascade Doesn't](projection-paper/paper.md) | Working paper — [DOI](https://doi.org/10.5281/zenodo.19145205) |
| [Verification as Operator: Spectral Projection, Rank Deficiencies, and the Persistence of the Audit Society](verification-as-operator/paper.md) | Preprint v1.1.0, May 2026 — [DOI](https://doi.org/10.5281/zenodo.19778588) |
| [Organizational Metamerism: Observer-Relative State Equivalence in Organizational Configurations](org-as-metadata/paper.md) | Preprint v1.1.0, May 2026 — [DOI](https://doi.org/10.5281/zenodo.19869871) |
| [Dual Hierarchies of Organizational Transferability: A Six-Tier Ontology and Theory of Acquisition Failure Propagation](six-tier-ontology/paper.md) | Preprint v1.1.0 on Zenodo, May 2026 — [DOI](https://doi.org/10.5281/zenodo.19895813) |
| [Brand as a Modular Layer: Tiered Organizational Architecture, Separability, and Firm Performance in Multi-Brand Strategies](brand-as-modular-layer/paper.md) | Preprint v1.1.0 on Zenodo, May 2026 — [DOI](https://doi.org/10.5281/zenodo.19930157) |
| [The Tier-Rotation Curve: A Theory of Brand-Substrate Decoupling and Its M&A-Value Geometry](tier-rotation/paper.md) | Preprint v1.0.0 on Zenodo, May 2026 — [DOI](https://doi.org/10.5281/zenodo.20069605) |
| [Where to Invest Within the Firm: Organizational Tiers, Discount Rates, and AI Penetration](tier-allocation/paper.md) | Preprint v1.0.0 on Zenodo 2026-05-07 — [DOI](https://doi.org/10.5281/zenodo.20072288) |
| [AI Tier Penetration: A Theory of Substrate-Dependent Competitive Advantage](tier-penetration/paper.md) | [SUPERSEDED] Working paper — [DOI](https://doi.org/10.5281/zenodo.20087036) |
| [Capability as Projection of an Append-Only Organizational Log: An Event-Sourced Substrate Theory of Organizational Capability and Transfer Failure](capability-as-projection/paper.md) | Working paper v1.0.0 — [DOI](https://doi.org/10.5281/zenodo.20367459) |
| [Specification Readiness and Endogenous Friction: An Information-Theoretic Model of Multi-Interface Organizational Architecture](specification-readiness/paper.md) | Working paper v1.0.0 — [DOI](https://doi.org/10.5281/zenodo.20379981) |
| [Specification Readiness: Measuring an Architectural Antecedent of Functional Friction and AI Returns](specification-readiness-empirical/paper.md) | Working paper v1.0.0 — [DOI](https://doi.org/10.5281/zenodo.20384084) |

### The Tier-Rotation Curve (Zharnikov 2026ai)

Formalizes brand-substrate decoupling as a continuous, logistic-form model governing how brand signal migrates from a founder-bound substrate (Tier 1) to an institutionally separable product-brand substrate (Tier 4) through deliberate knowledge-externalization effort over time. M&A value at exit is derived as a piecewise function of Tier-4 share at deal time, with a separability threshold above which brand assets become acquirable independently of the originating principal. Extends the Tier-Rotation Valuation Dynamics subsection of Zharnikov (2026ah) into a complete continuous model. Five falsifiable propositions; four illustrative boundary objects (Yeezy/Adidas, Casamigos/Diageo, Tom Ford/Estée Lauder, Kongō Gumi).

**Keywords**: brand assets, founder exit, intangible-asset separability, M&A valuation, organizational architecture, resource separability, tier rotation

- [Read on GitHub](tier-rotation/paper.md)
- [Preprint (DOI)](https://doi.org/10.5281/zenodo.20069605)

### Where to Invest Within the Firm (Zharnikov 2026aj)

Formalizes the cross-tier capital allocation problem using a vector w spanning five operating tiers that differ in asset durability. Each tier accumulates stock with tier-specific decay rates calibrated from Belo, Lin, and Vitorino (2014), ranging from .50/year at the organizational surface (Tier 6: advertising, paid media) to .05-.10/year at foundational layers (Tiers 2-3). Long-run value is a discounted Cobb-Douglas aggregator with Jorgensonian user costs; optimizing subject to the per-tier rental-rate budget constraint yields the closed-form rule w_t*(r) = alpha_t / (delta_t + r) and the comparative static d(w_6*)/dr > 0. Four falsifiable propositions link pre-deal surface-tier intensity, governance horizon, cost-of-capital shocks, and capability-rotation stage to M&A outcomes and capability persistence. Companion computation script and Figure 1 contour plot published alongside the paper.

**Keywords**: capital allocation, dynamic capabilities, brand capital, goodwill impairment, portfolio choice, organizational architecture, tier allocation, intangible capital, resource orchestration, corporate governance

- [Read on GitHub](tier-allocation/paper.md)
- [Preprint (DOI)](https://doi.org/10.5281/zenodo.20072288)

### Brand as a Modular Layer (Zharnikov 2026ah)

Extends the six-tier business architecture from Zharnikov (2026ag) into the brand-portfolio domain. Argues that brand IS Tier 4 — the Product specification surface — projected through an observer perceptual filter into observed brand-perception space. Three downstream phenomena unify under this single structural identity: multi-brand capacity is the firm's tier-level separability profile; failed-brand recovery is tier-level salvage of brand-agnostic infrastructure under brand-bound failure; and marketing, advertising, and branding are Tier-6 organizational functions that create, operate, and retire Tier-4 instances. Seven falsifiable propositions are derived (P1-P7), including the operationalization of the Aaker-Joachimsthaler Brand Relationship Spectrum as a measurable Tier-3-visibility-in-Tier-4 parameter (P7). Two diagnostic instruments — the Multi-Brand Capacity Diagnostic and the Recovery Salvage Matrix — are sketched for empirical validation.

**Keywords**: brand portfolio architecture, multi-brand strategy, corporate rebranding, brand failure recovery, tier-level decomposition, brand-business separability, marketing organization, cross-brand function

- [Read on GitHub](brand-as-modular-layer/paper.md)
- [Preprint (DOI)](https://doi.org/10.5281/zenodo.19930157)

### A Six-Tier Ontology of Acquisition-Target Transferability (Zharnikov 2026ag)

Develops a six-tier ontology of the acquisition target — Owner Intent, Business Model, Business Entity, Product, Process, and Organization — each defined by a unique governor, specification surface, and transferability mode. The tiers form dual overlapping hierarchies (service running upward; constraint running downward) that jointly determine integration sequencing and generate seven falsifiable propositions on cross-tier failure cascades. The framework applies across for-profit, NGO, cooperative, and state-owned organizational forms through explicit substitution rules. The Six-Tier Separability Diagnostic (STSD) profiles each tier as Fused / Partial / Independent for pre-close M&A risk assessment. Bridge contribution: the OST cascade L0-L5 nests inside Tiers 4-6 of the broader six-tier ontology.

**Keywords**: mergers and acquisitions, organizational ontology, transferability, business model, integration failure, form-invariance, separability diagnostic, dual hierarchy, failure cascade

- [Read on GitHub](six-tier-ontology/paper.md)
- [Preprint (DOI)](https://doi.org/10.5281/zenodo.19895813)

### The Organizational Schema Theory (Zharnikov 2026c)

Introduces the orgschema methodology: a six-level TDD cascade (customer experience contracts, signal requirements, process contracts, procedures, input specifications, sourcing requirements) where each level functions as the acceptance test for the level below it. Demonstrated through a complete specialty coffee operation (Spectra Coffee) specified across all six levels. Evaluated by five independent expert reviewers. Discusses implications for franchise models, organizational openness, and cross-industry perception transplant.

**Keywords**: test-driven development, business design, configuration management, design science research, declarative process management, organizational specification

- [Read on GitHub](organizational-schema-theory/paper.md)
- [Preprint (DOI)](https://doi.org/10.5281/zenodo.18946043)

### Verification as Operator (Zharnikov 2026ae)

Provides the first explicit algebraic identification of organizational acceptance testing as a spectral projection operator. Conventional audit (per Power 1997) is shown to be a degenerate rank-1 projection that discards all dimensions of organizational performance orthogonal to the compliance axis; OST's six-level cascade is full-rank, preserving dimensional structure across the specification hierarchy. The paper synthesizes three convergent lineages — organizational cybernetics (Beer 1972; Beer 1984), behavioral organization theory (March and Simon 1958; Argyris and Schön 1978), and software engineering verification (Beck 2002) — and shows that all three implicitly rely on the projection identity without naming it. Three formal propositions establish the rank inequality, cascade-consistency condition, and bandwidth bound. A Python simulation in Appendix B confirms that rank-1 audit misses ~90% of total organizational deviation across all noise levels.

**Keywords**: organizational verification, spectral projection, acceptance testing, audit society, viable system model, test-driven development, organizational learning, information-processing design

- [Read on GitHub](verification-as-operator/paper.md)
- [Preprint (DOI)](https://doi.org/10.5281/zenodo.19778588)

### The OrgSchema Audit (Zharnikov 2026)

Introduces a structured diagnostic protocol that evaluates organizational specification maturity across six cascading levels. Each audit level defines what to examine, what a healthy specification looks like, what failure modes indicate, and what corrective actions restore specification integrity. Demonstrates the full protocol through a worked example using a specialty coffee operation. Advances two propositions: cascade-position prioritization and bidirectional traceability completeness.

**Keywords**: organizational specification, test-driven business design, operational audit, specification maturity, six-level cascade, experience contracts, organizational schema theory, AI-assisted diagnostics

- [Read on GitHub](orgschema-audit/paper.md)
- [Preprint (DOI)](https://doi.org/10.5281/zenodo.19555201)

## How to Cite

```bibtex
@article{zharnikov2026ost,
  title={The Organizational Schema Theory: Test-Driven Business Design},
  author={Zharnikov, Dmitry},
  year={2026},
  url={https://github.com/spectralbranding/orgschema-papers}
}
```

Machine-readable citation: [CITATION.cff](organizational-schema-theory/CITATION.cff)

## Companion Repositories

| Repository | Description |
|-----------|-------------|
| [orgschema-framework](https://github.com/spectralbranding/orgschema-framework) | Python validator + JSON Schema for orgschema specifications |
| [orgschema-demo](https://github.com/spectralbranding/orgschema-demo) | Spectra Coffee reference implementation -- 25 YAML files, CI/CD pipeline |
| [sbt-framework](https://github.com/spectralbranding/sbt-framework) | Spectral Brand Theory -- the perception specification language used for L0-L1 |
| [sbt-papers](https://github.com/spectralbranding/sbt-papers) | SBT research papers (sibling framework) |

## Related Work

Orgschema is a sibling framework to Spectral Brand Theory (SBT). Both emerge from specification-first epistemology but target different domains:

- **SBT** models how brands are perceived (observer-dependent, 8 dimensions)
- **Orgschema** uses SBT as the test specification language for L0-L1 (desired perception determines required signals)

See [Zharnikov 2026a](https://github.com/spectralbranding/sbt-papers) for the SBT paper.

### Cross-Cutting Methodology Papers (in sbt-papers)

Several papers in the [sbt-papers](https://github.com/spectralbranding/sbt-papers) repo are cross-cutting methodology pieces that apply equally to SBT, Orgschema, and the broader specification-first research program. They live in sbt-papers for historical reasons (originated there before the orgschema-papers split) but are conceptually shared between the two frameworks:

| Key | Paper | DOI | Relevance to Orgschema |
|-----|-------|-----|------------------------|
| R13 | [Paper as Specification: A Machine-Readable Standard for Scientific Claims](https://github.com/spectralbranding/sbt-papers/tree/main/r13-paper-as-specification) | [10.5281/zenodo.19210037](https://doi.org/10.5281/zenodo.19210037) | Applies the orgschema test-driven cascade pattern to scientific publishing — papers as testable specifications. |
| R14 | [Research as Repository: A Git-Native Protocol for Scientific Knowledge Production](https://github.com/spectralbranding/sbt-papers/tree/main/r14-paper-as-repository) | [10.5281/zenodo.19294864](https://doi.org/10.5281/zenodo.19294864) | Extends orgschema's "git as system of record" architecture to scientific knowledge production. |
| 2026l | [The Rendering Problem: From Genetic Expression to Brand Perception](https://github.com/spectralbranding/sbt-papers/tree/main/rendering-problem) | [10.5281/zenodo.19064426](https://doi.org/10.5281/zenodo.19064426) | Cross-domain formalization of the specification-rendering gap that orgschema's L1-L5 cascade addresses operationally. |

These papers' Zenodo DOIs and GitHub paths remain in sbt-papers; this repo points to them rather than duplicating.

## Author

**Dmitry Zharnikov** -- dmitry@spectralbranding.com

Creator of Organizational Schema Theory and Spectral Brand Theory. Background in financial systems engineering and applied epistemology.

## License

All papers are released under [MIT License](LICENSE). Use, cite, and build upon this work freely with attribution.

## Trademarks

"Organizational Schema Theory" and "orgschema" are trademarks of Dmitry Zharnikov. The MIT license applies to the source code and text only and does not grant permission to use the project trademarks.

---

## 1 | Getting Started

This repository is the hub index for the Organizational Schema Theory (OST) research corpus. Each subdirectory is a paper-slug (for example, `organizational-schema-theory/`, `six-tier-ontology/`, `tier-rotation/`) containing the paper source, supporting computation, and per-paper `README.md`, `CITATION.cff`, and reproduction artifacts.

Clone the hub:

```bash
git clone https://github.com/spectralbranding/orgschema-papers.git
cd orgschema-papers
```

To work on a specific paper, change into its subdirectory and read that paper's `README.md`:

```bash
cd six-tier-ontology
cat README.md
```

The project anchor at the hub root is `pyproject.toml` (`name = "orgschema-papers-hub"`). Individual papers may declare their own `pyproject.toml` for paper-specific dependencies.

## 2 | Project Layout

```
orgschema-papers/
|-- README.md                          <- this file (hub index)
|-- CITATION.cff                       <- machine-readable hub citation
|-- LICENSE                            <- MIT (code, text)
|-- LICENSE-data                       <- CC BY 4.0 (figures, tables, data)
|-- pyproject.toml                     <- hub project anchor
|-- reproduce.sh                       <- hub orchestrator (iterates paper subdirs)
|-- .gitignore
|-- output/
|   |-- figures/.gitkeep
|   |-- tables/.gitkeep
|   `-- logs/.gitkeep                  <- hub_run.log lands here
|-- organizational-schema-theory/      <- Zharnikov 2026c
|-- orgschema-audit/                   <- Zharnikov 2026
|-- verification-as-operator/          <- Zharnikov 2026ae
|-- org-as-metadata/                   <- organizational metamerism
|-- six-tier-ontology/                 <- Zharnikov 2026ag
|-- brand-as-modular-layer/            <- Zharnikov 2026ah
|-- tier-rotation/                     <- Zharnikov 2026ai
|-- tier-allocation/                   <- Zharnikov 2026aj
|-- capability-as-projection/
|-- projection-paper/
|-- specification-readiness/
|-- specification-readiness-empirical/
|-- tier-penetration/
`-- ...                                <- additional paper-slugs
```

Each paper-slug subdirectory follows the per-paper layout defined in `PUBLIC_MIRROR_STANDARD.md` v1.0.0.

## 3 | Quick Start

Each paper that ships a reproduction pipeline carries its own `reproduce.sh`. The hub-level orchestrator iterates paper-slug subdirectories and invokes each per-paper `reproduce.sh` in turn:

```bash
./reproduce.sh                  # iterate all paper-slug subdirs, run each reproduce.sh
./reproduce.sh --check-only     # verify dependencies only
./reproduce.sh --fast           # skip expensive blocks (power analyses, LLM calls)
```

Run logs land in `output/logs/hub_run.log`. To reproduce a single paper directly:

```bash
cd six-tier-ontology
./reproduce.sh
```

## 4 | Dependencies

- Python `>=3.12`
- `uv` package manager ([install](https://docs.astral.sh/uv/getting-started/installation/))
- `git` (history-tracking; SHA recorded in run logs)

Per-paper subdirectories may declare additional dependencies (LLM API SDKs, scientific computing libraries) via their own `pyproject.toml`. The hub anchor at root scopes only the orchestration layer.

## 6 | Citation

To cite the hub repository:

> Zharnikov D. *Organizational Schema Theory -- Research Papers.* GitHub repository, 2026. https://github.com/spectralbranding/orgschema-papers

Machine-readable form: [`CITATION.cff`](CITATION.cff). GitHub renders a "Cite this repository" widget from that file.

For individual papers, cite the concept DOI listed in the paper table at the top of this README, or use the per-paper `CITATION.cff`. Selected concept DOIs:

- Organizational Schema Theory (Zharnikov 2026c): [10.5281/zenodo.18946043](https://doi.org/10.5281/zenodo.18946043)
- OrgSchema Audit: [10.5281/zenodo.19555201](https://doi.org/10.5281/zenodo.19555201)
- Verification as Operator (2026ae): [10.5281/zenodo.19778588](https://doi.org/10.5281/zenodo.19778588)
- Organizational Metamerism: [10.5281/zenodo.19869871](https://doi.org/10.5281/zenodo.19869871)
- Six-Tier Ontology (2026ag): [10.5281/zenodo.19895813](https://doi.org/10.5281/zenodo.19895813)
- Brand as Tier-4 Projection (2026ah): [10.5281/zenodo.19930157](https://doi.org/10.5281/zenodo.19930157)
- Tier-Rotation Curve (2026ai): [10.5281/zenodo.20069605](https://doi.org/10.5281/zenodo.20069605)
- Where to Invest Within the Firm (2026aj): [10.5281/zenodo.20072288](https://doi.org/10.5281/zenodo.20072288)

## 7 | Licence

This hub adopts the dual-licence discipline defined in `PUBLIC_MIRROR_STANDARD.md`:

- **Code** (scripts, configs, computational artifacts) -- MIT, see [`LICENSE`](LICENSE)
- **Data, figures, tables, paper text, rendered artifacts** -- Creative Commons Attribution 4.0 International (CC BY 4.0), see [`LICENSE-data`](LICENSE-data)

Per-paper subdirectories inherit this licence pairing unless they declare otherwise.

*Last updated: 2026-07-03*
