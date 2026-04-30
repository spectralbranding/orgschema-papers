# PENDING_UPDATES — Organizational Schema Theory (2026i)

Pending updates queued while paper.md is under journal review.

## Phase 1 alignment audit (2026-04-30)

Status: queued — not applied because paper is under TQM Journal review.

### Dimension order in §SBT-as-test-specification

**Issue**: the OST passage describing "SBT as test specification language" enumerates the eight SBT dimensions as `experiential, semiotic, temporal, ideological, narrative, cultural, social, economic`. This is the only place in the 35-paper SBT/OST corpus where the dimensions are listed in non-canonical order.

**Canonical order** per `CLAUDE.md` (project root) and the other 24 dimension-bearing corpus papers:

> Semiotic, Narrative, Ideological, Experiential, Social, Economic, Cultural, Temporal

**Recommended fix on next revision**: reorder the dimension list to canonical order. No theoretical claim depends on the order — the passage is purely descriptive.

**Source**: `audit/reports/01_alignment_2026i.md` in spectral-branding repo.

## Phase 2 Audit Findings (2026-04-30)

Status: queued — not applied because paper is under TQM Journal review.

### Tables missing `*Notes*:` italic block

Per `PAPER_QUALITY_STANDARDS.md` (in spectral-branding repo), every table must carry an italic `*Notes*:` block immediately below it. Phase 2 mechanical audit found 8 of 10 tables in `paper.md` missing this block. Only Table 4 (typst-rendered) currently complies.

| Caption | Line | Action |
|---|---|---|
| Table 1: The TDD-to-Orgschema Parallel | 39 | Add `*Notes*:` block below |
| Table 2: Forward Design vs. Reverse Design | 56 | Add `*Notes*:` block below |
| Table 3: Framework Lineage and Orgschema's Contribution | 90 | Add `*Notes*:` block below |
| Table 5: CI/CD Validation Levels | 283 | Add `*Notes*:` block below |
| Table 6: Six-Level Orgschema Maturity Model | 298 | Add `*Notes*:` block below |
| Table 7: LLM Impact on Orgschema Feasibility (Theoretical Comparison) | 319 | Add `*Notes*:` block below |
| Table 8: Executor Swap Impact Analysis (Illustrative Scenario) | 383 | Add `*Notes*:` block below |
| Table 9: Orgschema to Viable System Model Mapping | 446 | Add `*Notes*:` block below |
| Table 10: Three Fork Types | 491 | Add `*Notes*:` block below |

(Table 4 is typst-rendered and already complies; Table 7 is correctly counted above for a total of 9 missing-Notes tables — the Phase 2 batch-2 subagent flagged 8 in its initial pass; the comprehensive list here supersedes it.)

**Source**: `audit/reports/02_mechanical_2026i.md` and `audit/reports/02_mechanical_report.md` (M5) in spectral-branding repo.
