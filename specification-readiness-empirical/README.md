# Specification Readiness: Measuring an Architectural Antecedent (2026an)

**Title**: Specification Readiness: Measuring an Architectural Antecedent of Functional Friction and AI Returns

**Author**: Dmitry Zharnikov ([ORCID 0009-0000-6893-9231](https://orcid.org/0009-0000-6893-9231))

**Citation key**: 2026an

**Status**: Working paper v1.0.0 (May 2026).

**Concept DOI**: [10.5281/zenodo.20384084](https://doi.org/10.5281/zenodo.20384084)
**v1.0.0 DOI**: [10.5281/zenodo.20384085](https://doi.org/10.5281/zenodo.20384085)

## What this paper does

This paper introduces *specification readiness* — the degree to which a firm's commitments are codified in versioned, machine-readable, queryable form — as a new strategic construct and supplies a scalable archival operationalization. The construct is conceptually prior to existing measures of organization capital (Eisfeldt and Papanikolaou 2013), brand capital (Belo, Lin, and Vitorino 2014), and disclosure readability (Loughran and McDonald 2011, 2014).

Three contributions follow. First, a continuous Specification Coherence Index (SCI) built from year-over-year cosine similarity of 10-K narrative embeddings supplies the first firm-year measure observable across the Compustat universe of US public firms 2010–2025. Second, a multi-arm pre-registered identification template pairs within-firm linguistic-coherence shifts with staggered codification events (handbook publication, ISO 9001 certification, design-system release, investor-day specification overhaul), regulatory instruments (Sarbanes-Oxley Section 404; EEOC reporting), and event studies around advertising-spend cessation, with Oster (2019) bounds. The template is designed for reuse across upstream architectural variables. Third, pre-registered Monte Carlo mechanism tests and regression-identification power simulations confirm that the theoretical mechanism is internally consistent and that the design has the statistical power to detect the pre-registered effect sizes.

This is the empirical companion to Zharnikov (2026am) Specification Readiness and Endogenous Friction, which develops the underlying information-theoretic model. The five hypotheses H1–H5 in this paper are empirical readings of the five comparative-statics propositions P1–P5 in the foundational theory paper.

## Five hypotheses

- **H1 (Specification Readiness Reduces Functional Friction Tax)**: within firms, a one-SD increase in SCI is associated with approximately one percentage point reduction in interface-maintaining SG&A composition / total revenue (pre-registered Cohen's d ≈ .5; β ≈ −.08).
- **H2 (Specification Readiness Accelerates Brand-Capital Accumulation)**: within firms, higher SCI predicts faster Belo-Lin-Vitorino brand-capital stock accumulation per dollar of advertising spend (Cohen's d ≈ .3).
- **H3 (Multi-Interface Incoherence Raises Cross-Stakeholder Valuation Dispersion)**: within firms, higher cross-interface linguistic contradiction predicts greater cross-stakeholder valuation dispersion (Cohen's d ≈ .4).
- **H4 (Substrate Readiness Conditions AI Deployment ROI)**: within firms, pre-deployment SCI moderates the effect of AI deployment on firm productivity (Cohen's d ≈ .5).
- **H5 (Pull Architecture Shrinks Function-as-Friction-Tax)**: event-study analysis of advertising-cessation events shows sharper negative CARs for low-SCI firms than high-SCI firms (Cohen's d ≈ .7).

## Files

- `paper.md` — full paper (body ≈ 10,780 words; 48 references; 3 appendices)
- `paper.yaml` — paper-spec schema (citation key, hypotheses, falsification criteria, dependencies, AI disclosure)
- `CITATION.cff` — citation file (CFF 1.2.0)
- `CONTRIBUTORS.yaml` — contributor attribution (CRediT taxonomy; Form A AI disclosure)
- `PROVENANCE.yaml` — version history and related-work record
- `code/` — pointer to the shared code companion with paper 2026am (see `code/README.md`)

## Companion theoretical work

Foundational theory: [Zharnikov (2026am)](https://doi.org/10.5281/zenodo.20379981) Specification Readiness and Endogenous Friction — develops the information-theoretic model whose five propositions P1–P5 this paper operationalizes empirically.

## Companion code

Monte Carlo friction-tax simulation and regression-identification power simulation are shared with paper 2026am at [specification-readiness/code/](https://github.com/spectralbranding/orgschema-papers/tree/main/specification-readiness/code/). Run under fixed seed 20260525.

## Companion articles (practitioner expression)

The architectural construct and its empirical implications are developed in plain-English form across the SBT and OST Substack series, including The Log Is the Brand, The Business Is a Repository, Your Company Already Forks-Merges-and-Tags, and Capability Is Not What You Have. See `paper.yaml` `companion_articles` for the full list with URLs.

## Future archival implementation

The pre-registered design specified in this paper is in execution as future work (companion paper v2.0 / Paper C). When the archival panel results are available, the empirical estimates with confidence intervals, first-stage F-statistics, Oster δ-bounds, and economic magnitudes in dollars of SG&A savings will be reported in that follow-up paper.

## License

Creative Commons Attribution 4.0 International (CC BY 4.0) for the paper text; MIT License for the companion computation code.

## How to cite

```
Zharnikov, Dmitry (2026), "Specification Readiness: Measuring an Architectural Antecedent of Functional Friction and AI Returns," Working Paper v1.0.0, Zenodo, https://doi.org/10.5281/zenodo.20384084.
```
