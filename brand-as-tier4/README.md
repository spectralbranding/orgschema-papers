[![MIT License](https://img.shields.io/badge/Code-MIT-blue.svg)](../LICENSE)
[![CC-BY 4.0](https://img.shields.io/badge/Data-CC--BY_4.0-lightgrey.svg)](../LICENSE-data)
![Last Updated](https://img.shields.io/badge/updated-2026--05--29-success)

# Brand as a Modular Layer: Tiered Organizational Architecture, Separability, and Firm Performance in Multi-Brand Strategies

**Title**: Brand as a Modular Layer: Tiered Organizational Architecture, Separability, and Firm Performance in Multi-Brand Strategies

**Author**: Dmitry Zharnikov ([ORCID 0009-0000-6893-9231](https://orcid.org/0009-0000-6893-9231))

**Citation key**: 2026ah

**Status**: Working paper v1.1.0-pre. v1.0.0 published on Zenodo 2026-04-30 under the prior title "Brand as Tier-4 Projection: A Multi-Brand and Recovery Theory of the Six-Tier Business Architecture." Title, abstract, introduction, and conclusion revised; DOI corrections applied (Snihur & Tarziján 2018 LRP confirmed; Strebinger & Treiblmaier 2018 replaced with Strebinger 2004 ACR + Åsberg & Uggla 2019 JBM); Simon 1962 added to bibliography. Pending v1.1.0 Zenodo re-upload.

**DOI**: [10.5281/zenodo.19930157](https://doi.org/10.5281/zenodo.19930157) (concept) | [10.5281/zenodo.19930158](https://doi.org/10.5281/zenodo.19930158) (v1, 2026-04-30) | v1.1 DOI pending re-upload

## What this paper does

The brand-portfolio architecture literature has produced a mature taxonomy of *relationships between brands* — branded house, sub-brand, endorsed, hybrid, house of brands — but no theory of *which organizational layers carry the brand boundary*. This paper proposes that brand IS Tier 4 — the Product specification surface — of the six-tier business architecture in Zharnikov (2026ag), projected through an observer perceptual filter into observed brand-perception space.

Three downstream phenomena unify under this single structural identity: (1) multi-brand capacity is the firm's tier-level separability profile; (2) failed-brand recovery is tier-level salvage of brand-agnostic infrastructure under brand-bound failure; (3) marketing, advertising, and branding are Tier-6 organizational functions that create, operate, and retire Tier-4 instances. Seven falsifiable propositions are derived, each with explicit confirming and falsifying criteria.

## Three contributions

1. Operationalizes the Aaker–Joachimsthaler (2000) Brand Relationship Spectrum as a measurable Tier-3-visibility-in-Tier-4 parameter (P7), turning a typological dimension into a continuous-valued diagnostic.
2. Supplies a theory of failed-brand recovery as tier-level salvage, explaining the Marques, Vinhas da Silva, Davcik and Tamagnini Faria (2020) "equity transferred not created" finding through the Tier-4 framing (P2, P6) and predicting which substrate is salvageable per recovery pathway.
3. Gives a tier-level account of marketing, advertising, and branding as Tier-6 organizational functions managing a portfolio of Tier-4 configurations (P4), resolving the centralization-versus-decentralization debate as a tier-level separability choice.

## Files

- `paper.md` — full paper (~13,355 words body post-audit + rewrites; ~80 references; 5 tables; 1 Mermaid figure; 8 sections)
- `paper.yaml` — paper-spec schema (citation key, propositions, falsification criteria, dependencies, AI disclosure)
- `CITATION.cff` — citation file (CITATION File Format 1.2.0)
- `CONTRIBUTORS.yaml` — verified contributor attribution
- `PROVENANCE.yaml` — version history

## Related work

This paper extends [Zharnikov (2026ag) A Six-Tier Ontology of Acquisition-Target Transferability](https://doi.org/10.5281/zenodo.19895813) into the brand-portfolio domain. It uses the six-tier framework as its foundation and applies it to brand-business separability questions.

It draws on the perception-side machinery of Spectral Brand Theory:

- The Tier-4 specification surface uses the SBT eight-dimension framework: [Zharnikov (2026a) Spectral Brand Theory](https://doi.org/10.5281/zenodo.18945912).
- The tacit Tier-4 transfer-impossibility argument anchors on [Zharnikov (2026h) Specification Impossibility (R5)](https://doi.org/10.5281/zenodo.18945591).
- The longitudinal Tier-4 evolution claim and P5 Cultural / Ideological transfer prediction anchor on [Zharnikov (2026p) Dimensional Activation and Cohort Divergence (Dove case)](https://doi.org/10.5281/zenodo.19139258).
- The portfolio interference DO/WHAT distinction connects to [Zharnikov (2026ac) Spectral Immunity (R21)](https://doi.org/10.5281/zenodo.19765401).

## License

Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).

## How to cite

```
Zharnikov, Dmitry (2026), "Brand as a Modular Layer: Tiered Organizational Architecture, Separability, and Firm Performance in Multi-Brand Strategies," Working Paper v1.1.0-pre, Zenodo, doi:10.5281/zenodo.19930157.
```

---

## 1 | Paper

- Manuscript: [paper.md](paper.md)
- Version: 1.1.0
- Concept DOI: [10.5281/zenodo.19930157](https://doi.org/10.5281/zenodo.19930157)
- v1 DOI: [10.5281/zenodo.19930158](https://doi.org/10.5281/zenodo.19930158)
- Status: Working paper v1.1.0-pre; v1.1 Zenodo upload pending.

## 2 | Companion Data

No companion dataset for this paper.

## 3 | Reproduction

This paper ships two illustrative diagnostic scripts under [code/](code/):

- `code/v_parameter.py` — Tier-3-visibility-in-Tier-4 parameter V computation (P7).
- `code/mbcd_scorer.py` — Multi-Brand Capacity Diagnostic composite scorer.

Both run on plain CPython 3.10+ with no third-party dependencies:

```
uv run python code/v_parameter.py
uv run python code/mbcd_scorer.py
```

The hub-level orchestrator at [../reproduce.sh](../reproduce.sh) iterates all slugs.

## 4 | Citation

```bibtex
@article{zharnikov2026brandtier4,
  author  = {Zharnikov, Dmitry},
  title   = {Brand as a Modular Layer: Tiered Organizational Architecture, Separability, and Firm Performance in Multi-Brand Strategies},
  year    = {2026},
  doi     = {10.5281/zenodo.19930157}
}
```

Machine-readable: [CITATION.cff](CITATION.cff).

## 5 | Licence

Code (if any): MIT — see hub-level [../LICENSE](../LICENSE). Data, figures, tables: CC BY 4.0 — see hub-level [../LICENSE-data](../LICENSE-data). Paper text: CC BY-NC-ND 4.0 (matches published Zenodo PDF; see [CITATION.cff](CITATION.cff)).

*Last updated: 2026-05-29*
