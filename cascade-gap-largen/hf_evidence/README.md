---
license: cc-by-4.0
pretty_name: "Cascade-Gap Large-N Study — evidence corpus and coding logs"
tags:
  - mergers-and-acquisitions
  - inter-rater-reliability
  - llm-coding
  - organization-theory
configs:
  - config_name: coded_dataset
    data_files: full_draw_dataset.csv
    default: true
---

# Cascade-Gap Large-N Study — evidence corpus and coding logs

Companion **dataset** for the working paper *A Large-N Confirmatory Necessary-Condition Test of Closing-Time Structural Gaps in Acquisition Integration Failure* (Zharnikov, 2026). Concept DOI [10.5281/zenodo.21755969](https://doi.org/10.5281/zenodo.21755969). Dataset DOI [10.57967/hf/9805](https://doi.org/10.57967/hf/9805).

Code, paper, and reproduction pipeline: https://github.com/spectralbranding/orgschema-papers/tree/main/cascade-gap-largen

## Dataset viewer

The **viewer shows `full_draw_dataset.csv`** — the analysis dataset of record: **350 completed transactions**, one row per case, with the per-construct codes (structural gap, outcome pathway), the outcome status, the deal-structure stratum, and the rotated coder assignment. This is the single table the paper's results are computed from.

The bulky **raw evidence and logs** are archival files under the *Files and versions* tab (they are not a train/validation split — the auto-inferred split view does not apply to them):

| Path | Description |
|---|---|
| `full_draw_dataset.csv` | The 350-case coded dataset (the viewer table). |
| `full_draw_dossiers/` | 700 blinded per-case evidence dossiers (350 structural + 350 outcome), built from public SEC EDGAR filings — the coder-facing evidence base. |
| `full_draw_code_out/` | 700 per-case coded records (structural + outcome JSON per case) plus reliability outputs. |
| `logs_fulldraw/` | 700 JSONL model-call logs — every rater call with full prompt, parameters, and response (secrets-clean). |

## Provenance

Four large language models served as independent blinded raters under a pre-registered 3-of-4 per-construct rotation (seed 20260729): Claude (Opus 4.8), Gemini (3.1 Pro), Grok (4.5), GPT (5.6). All source documents are public SEC EDGAR filings. License: CC BY 4.0.
