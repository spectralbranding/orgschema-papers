[![MIT License](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)
[![CC-BY 4.0](https://img.shields.io/badge/Data-CC--BY_4.0-lightgrey.svg)](LICENSE-data)
![Last Updated](https://img.shields.io/badge/updated-2026--08--02-success)

# Cascade-Gap Large-N Study

> **Companion code and data** for a large-N confirmatory necessary-condition test of whether a closing-time *cascade gap* — a product–process or process–organization mismatch created when an asset or process crosses the ownership boundary without its adjacent producing or governing tier — is necessary for a cascade-type acquisition-integration failure.

Companion repository for *A Large-N Confirmatory Necessary-Condition Test of Closing-Time Structural Gaps in Acquisition Integration Failure* (Zharnikov, 2026). Concept DOI [`10.5281/zenodo.21755969`](https://doi.org/10.5281/zenodo.21755969); v1.0.0 version DOI [`10.5281/zenodo.21755970`](https://doi.org/10.5281/zenodo.21755970).

This is a **working paper (v1.0.0)**. The headline result is honest rather than triumphal: at N = 350 the structural safe harbor is real but **bounded** — conditional on no detected gap the cascade-type failure rate is `.073` (exact upper 95% bound `.112`), not zero, and only about half of failures carried a gap (necessity consistency `.517`).

---

## 1 | Getting Started

```bash
git clone https://github.com/spectralbranding/orgschema-papers.git
cd orgschema-papers/cascade-gap-largen
uv sync
```

The bulky evidence corpus (blinded case dossiers, per-case coded records, and full model-call logs) is **not vendored in git** — it lives as a companion dataset on Hugging Face. `reproduce.sh` downloads it. The small analysis inputs (the 350-case coded dataset, the selection and gate logs) are in `data/`.

---

## 2 | Project Layout

```
.
├── code/                       # Analysis + pipeline scripts (self-contained)
│   ├── analyze_full_draw.py    # confirmatory 2x2, exact CI, NCA, reliability
│   ├── power_analysis_s5.py    # registered N derivation (seed 20260729)
│   ├── full_draw_code.py       # the coding runner (3-of-4 rotation)
│   ├── full_draw_rotation.py   # deterministic per-construct rotation map
│   ├── draw_full_sample.py     # case-control draw on deal structure
│   ├── build_curated.py        # EDGAR ground-truth curated top-up resolver
│   ├── fetch_filing.py         # SEC EDGAR fetch/strip helper
│   ├── recode_separated_passes.py  # blinded separated-pass coding backend
│   ├── llm_call_logger.py      # canonical JSONL model-call logger
│   └── ...                     # pilot + QC utilities
├── data/                       # Small analysis inputs (CC BY 4.0)
│   ├── full_draw_dataset.csv       # 350 cases: per-construct codes + outcome
│   ├── full_draw_selection.csv     # the gated case-control sample of record
│   ├── full_draw_gate_log.csv      # build-time gate decisions
│   └── full_draw_curated_gap_deals.csv
├── protocols/                  # Pre-registration + frame-precision findings
│   ├── FULL_DRAW_PREREGISTRATION.md
│   ├── PILOT_PREREGISTRATION.md
│   ├── POWER_ANALYSIS_RESULTS.md
│   ├── FULL_DRAW_FRAME_FINDINGS.md
│   └── ...
├── output/{figures,tables,logs}/   # Generated artifacts
├── SPINE.yaml                  # Claim / dependency / evidence graph
├── ONTOLOGY.yaml               # Term-ownership module
├── GLOSSARY.md                 # Rendered term glossary
├── paper.md                    # The manuscript (SSOT)
├── paper.yaml                  # Machine-readable paper record
├── DATA_MANIFEST.yaml          # Hugging Face dataset pointers
├── CITATION.cff · LICENSE · LICENSE-data · pyproject.toml · reproduce.sh
```

---

## 3 | Quick Start

Reproduce the reported quantities (the 2×2, the exact Clopper–Pearson bound, necessity consistency, reliability, and the registered sample size) from the released dataset:

```bash
./reproduce.sh                 # download HF evidence + run full pipeline
./reproduce.sh --check-only    # verify dependencies only
./reproduce.sh --fast          # analysis only, skip the HF download
```

The pipeline is deterministic: the draw and rotation use fixed seed `20260729`.

---

## 4 | Dependencies

- **Python ≥ 3.12** — pinned in `pyproject.toml`; install with `uv sync`.
- **`huggingface_hub`** — used by `reproduce.sh` to fetch the evidence dataset.
- **LLM API access** — only needed to *re-run coding from scratch* (not to reproduce the reported statistics from the released dataset). Keys via `.env` (see `.env.example`); every call is logged in JSONL via `code/llm_call_logger.py`. The four blinded raters were Claude (Opus 4.8), Gemini (3.1 Pro), Grok (4.5), and GPT (5.6).

---

## 5 | Script Map

| Block | Script | Inputs | Outputs |
|-------|--------|--------|---------|
| Power / N | `code/power_analysis_s5.py` | — (seed 20260729) | registered N = 350 |
| Draw | `code/draw_full_sample.py` | SEC EDGAR frames | `data/full_draw_selection.csv` |
| Coding | `code/full_draw_code.py` | dossiers (HF) + `full_draw_rotation.json` | per-case coded records (HF), JSONL logs (HF) |
| Analysis | `code/analyze_full_draw.py` | `data/full_draw_dataset.csv` | 2×2, exact CI, necessity, AC1/κ |

Reliability primary read is Gwet's AC1 (the rare-cell-robust statistic), reported alongside Fleiss' κ.

---

## 6 | Data Availability

- **Small inputs** (this repo, `data/`) — the 350-case coded dataset and selection/gate logs, CC BY 4.0.
- **Evidence corpus** (Hugging Face, [`spectralbranding/tba-cascade-gap-largen`](https://huggingface.co/datasets/spectralbranding/tba-cascade-gap-largen), DOI [10.57967/hf/9805](https://doi.org/10.57967/hf/9805)) — 700 blinded case dossiers built from public SEC EDGAR filings, 700 per-case coded records, and the complete per-call model-interaction logs. See `DATA_MANIFEST.yaml` for the file map and DOI.

All underlying source documents are public SEC EDGAR filings; nothing here depends on licensed or redistributable-restricted data.

---

## 7 | Citation

> Dmitry Zharnikov (2026). "A Large-N Confirmatory Necessary-Condition Test of Closing-Time Structural Gaps in Acquisition Integration Failure." Working Paper v1.0.0. DOI [`10.5281/zenodo.21755969`](https://doi.org/10.5281/zenodo.21755969).

Machine-readable citation: [`CITATION.cff`](CITATION.cff).

---

## 8 | Licence

- **Code** — © Dmitry Zharnikov, 2026. [MIT Licence](LICENSE).
- **Data, figures, tables** — © Dmitry Zharnikov, 2026. [CC BY 4.0](LICENSE-data).

---

*Last updated: 2026-08-02.*
