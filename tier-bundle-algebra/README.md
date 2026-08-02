[![MIT License](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)
[![CC-BY 4.0](https://img.shields.io/badge/Data-CC--BY_4.0-lightgrey.svg)](LICENSE-data)
![Last Updated](https://img.shields.io/badge/updated-2026--08--02-success)

# Tier-Bundle Algebra

> **Companion code and data** for a fork-operation formalism over the six-tier acquisition-target ontology — a compositional grammar for which tiers must co-transfer when an asset crosses an ownership boundary — with a pre-registered n = 30 empirical anchor.

Companion repository for *Tier-Bundle Algebra in Inter-Organizational Resource Transfer: A Fork-Operation Formalism Over the Six-Tier Acquisition-Target Ontology* (Zharnikov, 2026). Concept DOI [`10.5281/zenodo.21756077`](https://doi.org/10.5281/zenodo.21756077); v1.0.0 version DOI [`10.5281/zenodo.21756078`](https://doi.org/10.5281/zenodo.21756078).

This is a **working paper (v1.0.0)**. The paper is primarily formal: it develops a fork operator, the tier-bundle, a directional *cascade rule* across the service hierarchy, and an *admissibility predicate* derived from tier-collapse states. Its empirical anchor is a pre-registered, blindly-coded corpus of thirty documented transactions; that anchor is preliminary (three cascade-gap cases, all anchor deals) and its correctly-scoped necessary-condition reading is developed in the companion large-N study.

---

## 1 | Getting Started

```bash
git clone https://github.com/spectralbranding/orgschema-papers.git
cd orgschema-papers/tier-bundle-algebra
uv sync
```

The coded corpus is small and fully vendored in `data/` — no external download is required.

---

## 2 | Project Layout

```
.
├── code/                       # The empirical-test pipeline (self-contained)
│   ├── analyze_study_n30.py        # pre-registered categorical-association test (fixture self-check)
│   ├── triple_code_dossiers.py     # blinded multi-coder harness + JSONL logging
│   ├── assemble_coded_dataset.py   # deterministic assembler
│   ├── draw_extension_sample.py    # seeded extension-corpus draw
│   └── llm_call_logger.py          # canonical JSONL model-call logger
├── data/
│   ├── coded_dataset_n30.csv       # coded dataset (majority-vote)
│   ├── coded_dataset_n30_full.csv  # per-coder long form
│   ├── ADJUDICATION.csv            # adjudication ledger
│   ├── dossiers/                   # 30 blinded per-case evidence dossiers
│   └── coding_raw/                 # per-coder raw responses + reliability outputs
├── protocols/                  # Pre-registration + coding protocol + results
├── output/{figures,tables,logs}/
├── SPINE.yaml · ONTOLOGY.yaml · GLOSSARY.md
├── paper.md · paper.yaml
├── README · CITATION.cff · LICENSE · LICENSE-data · pyproject.toml · reproduce.sh
```

---

## 3 | Quick Start

```bash
./reproduce.sh                 # reproduce the pre-registered empirical test
./reproduce.sh --check-only    # verify dependencies only
```

`analyze_study_n30.py --fixture` self-checks the analysis kernels against a known textbook value.

---

## 4 | Dependencies

- **Python ≥ 3.12** — pinned in `pyproject.toml`; install with `uv sync`.
- **LLM API access** — only to re-run the blinded coding. Keys via `.env` (see `.env.example`); every call is logged in JSONL via `code/llm_call_logger.py`. The three blinded raters were Claude (Opus 4.8), Gemini (3.1 Pro), and Grok (4.3).

---

## 5 | Script Map

| Block | Script | Inputs | Outputs |
|-------|--------|--------|---------|
| Analysis | `code/analyze_study_n30.py --data data/coded_dataset_n30.csv` | coded dataset | Fisher's exact, Cramér's V, necessary-condition summary |
| Coding | `code/triple_code_dossiers.py` | `data/dossiers/` | per-coder codes + JSONL logs |
| Assemble | `code/assemble_coded_dataset.py` | per-coder codes + adjudication | `data/coded_dataset_n30.csv` |

The empirical test is the paper's anchor, not its headline; the correctly-scoped necessary-condition reading is developed at large N in the companion study.

---

## 6 | Citation

> Dmitry Zharnikov (2026). "Tier-Bundle Algebra in Inter-Organizational Resource Transfer: A Fork-Operation Formalism Over the Six-Tier Acquisition-Target Ontology." Working Paper v1.0.0. DOI [`10.5281/zenodo.21756077`](https://doi.org/10.5281/zenodo.21756077).

Machine-readable citation: [`CITATION.cff`](CITATION.cff).

---

## 7 | Licence

- **Code** — © Dmitry Zharnikov, 2026. [MIT Licence](LICENSE).
- **Data, figures, tables** — © Dmitry Zharnikov, 2026. [CC BY 4.0](LICENSE-data).

---

*Last updated: 2026-08-02.*
