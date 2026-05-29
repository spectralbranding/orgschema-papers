[![MIT License](https://img.shields.io/badge/Code-MIT-blue.svg)](../LICENSE)
[![CC-BY 4.0](https://img.shields.io/badge/Data-CC--BY_4.0-lightgrey.svg)](../LICENSE-data)
![Last Updated](https://img.shields.io/badge/updated-2026--05--29-success)

# Dual Hierarchies of Organizational Transferability (2026ag)

**Title**: Dual Hierarchies of Organizational Transferability: A Six-Tier Ontology and Theory of Acquisition Failure Propagation

**Author**: Dmitry Zharnikov ([ORCID 0009-0000-6893-9231](https://orcid.org/0009-0000-6893-9231))

**Citation key**: 2026ag

**Status**: Working paper v1.1.0 prepared for Zenodo re-upload 2026-05-29 (clean reference-list pass + 3 added references: Barney 1991, Teece-Pisano-Shuen 1997, Zharnikov 2026m back-cite; substantive Smeulders 2023 citation correction). v1.0.0 originally published 2026-04-29. Target venue: Academy of Management Review.

**DOI**: [10.5281/zenodo.19895813](https://doi.org/10.5281/zenodo.19895813) (concept) | [10.5281/zenodo.19895814](https://doi.org/10.5281/zenodo.19895814) (v1)

## What this paper does

Develops a six-tier ontology of the acquisition target — Owner Intent, Business Model, Business Entity, Product, Process, and Organization — each defined by a unique governor, specification surface, and transferability mode across ownership boundaries. The tiers form dual overlapping hierarchies (service running upward; constraint running downward) that jointly determine integration sequencing and generate seven falsifiable propositions on cross-tier failure cascades. The framework applies across for-profit, NGO, cooperative, and state-owned organizational forms through explicit substitution rules. The Six-Tier Separability Diagnostic (STSD) profiles each tier as Fused / Partial / Independent for pre-close M&A risk assessment.

## Three contributions

1. The first unified transferability ontology covering all six tiers from Owner Intent through Organization.
2. Formal derivation of bidirectional cross-tier propagation pathways, generating P1 through P7.
3. The Six-Tier Separability Diagnostic (STSD) — a structured pre-close instrument profiling each tier ordinally.

## Files

- `paper.md` — full paper (~12,500 words body; 53 references; 4 tables; 1 Mermaid figure; 7 sections)
- `paper.yaml` — paper-spec schema (citation key, propositions, falsification criteria, dependencies, AI disclosure)
- `CITATION.cff` — citation file (CITATION File Format 1.2.0)
- `CONTRIBUTORS.yaml` — verified contributor attribution
- `PROVENANCE.yaml` — version history and review records

## Related work

This paper is a bridge contribution between Spectral Brand Theory (SBT) and Organizational Schema Theory (OST):

- The Tier 4 Product specification surface uses the SBT eight-dimension framework as one example precision instrument: [Zharnikov (2026a) Spectral Brand Theory](https://doi.org/10.5281/zenodo.18945912).
- The P4 Product-Process Disruption mechanism anchors on the formal impossibility of fully specifying Product requirements: [Zharnikov (2026h) Specification Impossibility in Organizational Design (R5)](https://doi.org/10.5281/zenodo.18945591).
- The Tier 5 Process and Tier 6 Organization tiers nest the OST cascade L0-L5 inside the broader six-tier structure: [Zharnikov (2026i) Organizational Schema Theory](https://doi.org/10.5281/zenodo.18946043).
- The paper continues the cross-paper organizational specification thread from [Zharnikov (2026af) Organizational Metamerism](https://doi.org/10.5281/zenodo.19869871), which studies state-equivalence on the same Tier 5-6 stack from a different theoretical axis.

## License

Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).

## How to cite

```
Zharnikov, Dmitry (2026), "Dual Hierarchies of Organizational Transferability: A Six-Tier Ontology and Theory of Acquisition Failure Propagation," Working Paper v1.1.0, Zenodo, doi:10.5281/zenodo.19895813.
```

---

## 1 | Paper

[paper.md](paper.md) — version 1.1.0. Zenodo versioned DOI: [10.5281/zenodo.19895814](https://doi.org/10.5281/zenodo.19895814). Concept DOI (always resolves to latest): [10.5281/zenodo.19895813](https://doi.org/10.5281/zenodo.19895813).

## 2 | Companion Data

No companion dataset for this paper.

## 3 | Reproduction

The [`code/`](code/) directory contains the Six-Tier Separability Diagnostic (STSD) scoring utility derived in the paper:

- `code/stsd_scorer.py` — STSD ordinal scorer (Fused / Partial / Independent per tier).
- `code/sample_output.txt` — reference output from the scorer.
- `code/README.md` — usage notes and invocation.

Run from the slug root: `python code/stsd_scorer.py`.

## 4 | Citation

```bibtex
@article{zharnikov2026sixtier,
  author  = {Zharnikov, Dmitry},
  title   = {Dual Hierarchies of Organizational Transferability: A Six-Tier Ontology and Theory of Acquisition Failure Propagation},
  year    = {2026},
  doi     = {10.5281/zenodo.19895814}
}
```

Machine-readable: [CITATION.cff](CITATION.cff).

## 5 | Licence

Code (if any): MIT — see hub-level [../LICENSE](../LICENSE). Data, figures, tables: CC BY 4.0 — see hub-level [../LICENSE-data](../LICENSE-data). Paper text: CC BY-NC-ND 4.0 (matches published Zenodo PDF; see [CITATION.cff](CITATION.cff)).

---

*Last updated: 2026-05-29*
