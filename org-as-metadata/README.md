[![MIT License](https://img.shields.io/badge/Code-MIT-blue.svg)](../LICENSE)
[![CC-BY 4.0](https://img.shields.io/badge/Data-CC--BY_4.0-lightgrey.svg)](../LICENSE-data)
![Last Updated](https://img.shields.io/badge/updated-2026--05--29-success)

# Organizational Metamerism: When Distinct Configurations Produce Equivalent Outputs

**Status**: Working paper v1.0.0 (April 2026) | **DOI**: [10.5281/zenodo.19869871](https://doi.org/10.5281/zenodo.19869871)

## Paper

Zharnikov, D. (2026). Organizational Metamerism: When Distinct Configurations Produce Equivalent Outputs. Working Paper.

## Abstract

This paper introduces organizational metamerism — the condition under which structurally distinct organizational configurations produce functionally equivalent value outputs as observed by a particular evaluative observer. Metamerism extends the equifinality literature from path-equivalence (different sequences reach the same end state) to state-equivalence (different configurations are simultaneously equivalent for a given observer). The framework rests on a temporal stability ordering — value output specifications change least often, process specifications change at intermediate frequencies, and organizational configurations change most often — explained mechanistically by the migration of coordination work into process specifications, which renders organizational form the lowest-stability layer of a multi-layered specification stack.

The paper engages organizational routines (Pentland and Feldman 2005), configurational equifinality (Gresov and Drazin 1997; Fiss 2011), pace layering (Beane and Leonardi 2025), and combinatorial configuration (Puranam, Alexy, and Reitzig 2014) as the closest precedents, distinguishing metamerism from each. Four propositions follow with explicit confirming and refuting evidence criteria. The framework predicts a decoupling of organizational restructuring frequency from process change frequency in AI-era organizations, with tacit knowledge intensity as a boundary condition.

## Propositions

| ID | Statement | Status |
|----|-----------|--------|
| P1 | Stability ordering: value > process > organizational form | Proposed |
| P2 | Metamerism set size increases with coordination embedding, decreases with tacit knowledge intensity | Proposed |
| P3 | AI-era decoupling: restructuring frequency rises while process change frequency remains stable | Proposed |
| P4 | Tacit knowledge boundary: high-tacit organizations have narrow metamerism sets regardless of coordination embedding | Proposed |

## Companion papers

- **Spectral metamerism in brand perception** (Zharnikov 2026e) — formal observer-relativity argument grounding the organizational extension. [DOI](https://doi.org/10.5281/zenodo.18945352)
- **Specification impossibility in organizational design** (Zharnikov 2026h) — establishes that complete specifications are unattainable, motivating the metamerism set framing. [DOI](https://doi.org/10.5281/zenodo.18945591)
- **The Organizational Schema Theory** (Zharnikov 2026i) — shared metadata-style framing of organizational specification. [DOI](https://doi.org/10.5281/zenodo.18946043)

---

## 1 | Project Layout

```
org-as-metadata/
├── README.md              # this file
├── CITATION.cff           # machine-readable citation
├── paper.md               # full manuscript
├── paper.yaml             # paper specification
├── code/                  # companion computation scripts
│   └── metamerism_set_simulation.py
├── CONTRIBUTORS.yaml
└── PROVENANCE.yaml
```

## 2 | Companion Computation Script

`code/metamerism_set_simulation.py` — illustrative simulation of metamerism set size as a function of coordination embedding and tacit knowledge intensity. Run command and dependencies documented in the script docstring.

## 3 | Dependencies

Python 3.12+. See script docstring in `code/metamerism_set_simulation.py` for any specific package requirements.

## 4 | Citation

Verbatim title (per `paper.yaml`):

> Zharnikov, D. (2026). Organizational Metamerism: Observer-Relative State Equivalence in Organizational Configurations. Working Paper v1.1.0. DOI: [10.5281/zenodo.19869871](https://doi.org/10.5281/zenodo.19869871).

See [CITATION.cff](CITATION.cff) for machine-readable citation. GitHub and Zenodo render this natively via the "Cite this repository" affordance.

## 5 | Licence

Code (if any): MIT — see hub-level [../LICENSE](../LICENSE). Data, figures, tables: CC BY 4.0 — see hub-level [../LICENSE-data](../LICENSE-data). Paper text: CC BY-NC-ND 4.0 (matches published Zenodo PDF; see [CITATION.cff](CITATION.cff)).

---

*Last updated: 2026-05-29*
