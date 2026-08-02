[![MIT License](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)
[![CC-BY 4.0](https://img.shields.io/badge/Data-CC--BY_4.0-lightgrey.svg)](LICENSE-data)
![Last Updated](https://img.shields.io/badge/updated-2026--08--02-success)

# A Blinded Multi-LLM Content-Coding Instrument

> **Companion code and data** for a reproducible, registered-before-data instrument in which several large language models independently code the same organizational evidence dossiers under blinding, with inter-coder reliability validation.

Companion repository for *A Blinded Multi-LLM Content-Coding Instrument: Protocol Specification and Inter-Coder Reliability Validation on an Organizational Corpus* (Zharnikov, 2026). Concept DOI [`10.5281/zenodo.21756063`](https://doi.org/10.5281/zenodo.21756063); v1.0.0 version DOI [`10.5281/zenodo.21756064`](https://doi.org/10.5281/zenodo.21756064).

This is a **working paper (v1.0.0)**. The contribution is the *instrument* — a blinded multi-coder pipeline with per-call logging, majority-vote-or-flag adjudication, and reliability validation (Fleiss' κ = .838 on the n = 30 demonstration corpus). Reliability is not validity; a held-out human-coding validation is declared future work.

---

## 1 | Getting Started

```bash
git clone https://github.com/spectralbranding/orgschema-papers.git
cd orgschema-papers/multi-llm-coding-instrument
uv sync
```

The demonstration corpus is small and fully vendored in `data/` — no external download is required to reproduce the reported reliability statistics.

---

## 2 | Project Layout

```
.
├── code/                       # Pipeline scripts (self-contained)
│   ├── triple_code_dossiers.py     # blinded multi-coder harness + JSONL logging
│   ├── assemble_coded_dataset.py   # deterministic assembler (codes + adjudication)
│   ├── analyze_study_n30.py        # reliability + analysis, with fixture self-check
│   ├── draw_extension_sample.py    # seeded sampling of the extension corpus
│   └── llm_call_logger.py          # canonical JSONL model-call logger
├── data/
│   ├── coded_dataset_n30.csv       # the coded dataset (majority-vote)
│   ├── coded_dataset_n30_full.csv  # per-coder long form
│   ├── ADJUDICATION.csv            # the adjudication ledger
│   ├── dossiers/                   # 30 blinded per-case evidence dossiers
│   └── coding_raw/                 # per-coder raw model responses (call records)
├── protocols/CODING_RESULTS.md     # reliability results + honest reading
├── output/{figures,tables,logs}/   # Generated artifacts
├── SPINE.yaml · ONTOLOGY.yaml · GLOSSARY.md
├── paper.md · paper.yaml
├── README · CITATION.cff · LICENSE · LICENSE-data · pyproject.toml · reproduce.sh
```

---

## 3 | Quick Start

```bash
./reproduce.sh                 # recompute reliability from the vendored dataset
./reproduce.sh --check-only    # verify dependencies only
```

Re-running the coding from scratch (LLM calls) is optional and needs API keys; it is not required to reproduce the reported statistics.

---

## 4 | Dependencies

- **Python ≥ 3.12** — pinned in `pyproject.toml`; install with `uv sync`.
- **LLM API access** — only to re-run coding. Keys via `.env` (see `.env.example`); every call is logged in JSONL via `code/llm_call_logger.py`. The three blinded coders were Claude (Opus 4.8), Gemini (3.1 Pro), and Grok (4.3).

---

## 5 | Script Map

| Block | Script | Inputs | Outputs |
|-------|--------|--------|---------|
| Coding | `code/triple_code_dossiers.py` | `data/dossiers/` | per-coder codes + JSONL logs |
| Assemble | `code/assemble_coded_dataset.py` | per-coder codes + `data/ADJUDICATION.csv` | `data/coded_dataset_n30.csv` |
| Analysis | `code/analyze_study_n30.py --data data/coded_dataset_n30.csv` | coded dataset | Fleiss' κ, reliability tables |

`analyze_study_n30.py --fixture` self-checks the analysis kernels against a known value.

---

## 6 | Citation

> Dmitry Zharnikov (2026). "A Blinded Multi-LLM Content-Coding Instrument: Protocol Specification and Inter-Coder Reliability Validation on an Organizational Corpus." Working Paper v1.0.0. DOI [`10.5281/zenodo.21756063`](https://doi.org/10.5281/zenodo.21756063).

Machine-readable citation: [`CITATION.cff`](CITATION.cff).

---

## 7 | Licence

- **Code** — © Dmitry Zharnikov, 2026. [MIT Licence](LICENSE).
- **Data, figures, tables** — © Dmitry Zharnikov, 2026. [CC BY 4.0](LICENSE-data).

---

*Last updated: 2026-08-02.*
