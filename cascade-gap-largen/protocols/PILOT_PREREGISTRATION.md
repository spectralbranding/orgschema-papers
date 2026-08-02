---
title: "Pilot pre-registration — separated-from-the-start dossier + coding pipeline validation for the cascade-gap large-N study"
version: 1.3.0
status: pre-analysis registered (pilot design; no pilot CODED datum yet collected)
registered_at: 2026-07-29
pre_analysis_revision: |
  v1.1.0 (2026-07-29, BEFORE any pilot datum): user scope confirmation narrowed the
  pilot to N=10 (from 20) and locked the deal-selection universe to SEC EDGAR (public
  primary filings). §1 (sample) and §2 (selection) updated.
  v1.2.0 (2026-07-29, BEFORE any pilot datum): user chose to implement genuine
  per-construct coder rotation in the pilot by ADDING A 4TH CODER, so the gap and the
  pathway are coded by DISJOINT model pairs. 4th coder verified against the live API =
  OpenAI gpt-5.4 (pinned gpt-5.4-2026-03-05, the general-purpose flagship; not codex/
  mini). §4 (measurement) rewritten to the 4-coder disjoint-pair rotation; per-construct
  κ is now over 2 rater-slots (§4 + §6 note the precision tradeoff); coding-call count
  → ≈40 (§1). Both are pre-DATA refinements (registered-before-data intact — no deal
  drawn, no dossier built, no coding call); §3, §5, §7 unchanged.
  v1.3.0 (2026-07-29, BEFORE any pilot CODED datum): the first v1.2.0 seeded draw
  (committed, then superseded) showed that pure form-type EDGAR classification is too
  crude — it drew a SIC-6770 blank-check/SPAC as a "control" and a micro-cap shell as a
  "roll-up", and enumeration carried no size signal (DRAW_QUALITY_FINDING.md). Per user
  decision (revise frame + re-draw), §2 gains an OUTCOME-BLIND structural INCLUSION
  FILTER applied at draw time: (a) drop SIC 6770 (Blank Checks / SPACs — definitionally
  not a going-concern deal); (b) require a ≥ $1bn size band via an outcome-blind XBRL
  size proxy (largest of us-gaap Assets / Revenues / equity with a period end near the
  filing date). The frame snapshot still records the FULL unfiltered enumeration for
  transparency; the filter is applied only at selection. This is a pre-CODED-DATA
  refinement of the sampling frame — the blind seeded draw is re-run and the earlier
  (superseded) selection is discarded; NO dossier was built and NO coding call was made
  under either draw. §1, §3–§7 unchanged (design, N=10, rotation, go/no-go all hold).
registered_by: Dmitry Zharnikov
program_stage: "S5 (paper 2026bi), pilot phase — gates the decision on the full N≈300 draw"
parent_design: "research/empirical_cases_v1/PREREGISTRATION_V2.md (the locked S5 blueprint; this pilot is Amendment 1 to it — sequencing only, design unchanged)"
gate_decision: "pilot-first sequencing chosen before any datum; design and N unchanged"
registration_anchor: |
  This document's first-public-commit SHA + timestamp in the spectral-branding
  repository is the verifiable "registered-before-data" anchor for the pilot. The
  pilot pre-registration, the empty pilot schema (pilot_dataset.csv, header only), the
  seeded selection procedure, and the pre-registered per-construct coder-rotation
  assignment are all committed BEFORE any pilot deal is drawn, any sub-dossier is built,
  or any coding call is made. Deviations after this commit are numbered amendments; the
  locked body is not modified.
---

# Pilot pre-registration — pipeline validation before the full cascade-gap draw

This pilot is a **feasibility / pipeline-validation** step, NOT a confirmatory test.
It exists because the user chose REVISE (pilot first) at the rule-0a gate: before
committing to the full N ≈ 300 registered-before-data run (≈600 sub-dossiers, ≈1,800
coding calls), validate on a small structured sample that the three things S4 could not
test — (a) building dossiers **separated from the start** from primary filings (not
slicing a pooled v1 dossier), (b) **per-construct coder rotation**, and (c) coding
**newly collected** deals rather than the anchor corpus — actually work end-to-end and
produce acceptable reliability. The confirmatory necessary-condition test remains the
full S5 draw (`PREREGISTRATION_V2.md` §4).

## 0. What the pilot must answer (go/no-go questions)

1. **Feasibility.** Can separated structural + outcome sub-dossiers be built from public
   primary sources at a per-deal effort compatible with N ≈ 300? (Record wall-clock /
   source-availability per deal.)
2. **Reliability under clean construction.** Is per-construct triple-coder agreement
   acceptable on separated-from-the-start dossiers (i.e. does building the slices from
   disjoint primary sources restore the gap-construct κ that S4's *slicing* of pooled
   dossiers dropped to .620)?
3. **Porosity closure.** Does separated-from-the-start construction remove the residual
   retrospective-phrasing leak (the "processes largely stayed separate" problem
   `PREREGISTRATION_V2.md` §1.4 named) that the S4 slicer could not fully strip?
4. **Coder-rotation stability.** Does per-construct rotation (§1.3 — different model
   codes the gap vs the pathway for a given case) run cleanly and not degrade agreement
   below the acceptance thresholds?

The pilot is **descriptive**: it reports per-construct κ, feasibility notes, a porosity
spot-check, and the descriptive necessary-condition cells — it is NOT powered for a
confirmatory CI on P(fail | no gap) and makes no confirmatory claim.

## 1. Pilot sample (scope-narrowed from the full S5 frame)

Two of the five gap-prone strata, chosen on the S4 evidence, plus matched controls:

- **Stratum A — carve-outs / divestitures.** The canonical `gap_45` generator (product/
  asset separates from the shared services that produced it) with the richest closing
  documentation (S-4 / DEFM14A / Form 10 / 8-K). Best case for exercising the structural
  pass.
- **Stratum B — roll-ups.** The stratum where S4's A05 (funeral-home roll-up) surfaced
  the gap-prone-but-successful case the random frame missed — i.e. the stratum that
  directly validated the case-control frame; it must be in the pilot.
- **Matched going-concern controls.** For each case-stratum deal, one whole-company
  going-concern acquisition matched on industry × size band × era (product, process,
  organization transfer together).

**Pilot N (locked v1.1.0): 10 deals** — **3 carve-outs + 2 roll-ups** (5 gap-prone) +
**5 matched going-concern controls** (one per gap-prone case). 20 sub-dossiers (10
structural + 10 outcome); with the 4-coder **disjoint-pair** rotation (2 coders per
construct per case — see §4), **≈ 40 coding calls** (10 structural × 2 + 10 outcome × 2).
This is the cheapest sample that still exercises
both strata + the matched-control contrast + both coding passes end-to-end; it is a
**pipeline-and-feasibility probe**, and per-construct κ on 10 cases is read as a coarse
signal (a wide CI is expected — a κ point estimate below threshold triggers a design
look, it does not by itself veto the full draw). The full-draw target (N ≈ 300, 60–80
gap cases) is unchanged and is decided AFTER the pilot.

## 2. Selection procedure (pre-registered, seeded, blind to outcome) — SEC EDGAR universe

- **Universe (locked v1.1.0): SEC EDGAR** completed US transactions, so that every coded
  field traces to a **public primary filing** (anti-fabrication + full reproducibility).
- Sampling variable = **deal type** (a closing-time structural property), never the
  outcome. Deal type is classified from **filing type**, blind to the 3–5-year outcome:
  - **Carve-out / divestiture (Stratum A):** a spin-off / equity-carve-out registration
    (Form 10 / 10-12B, or S-1/S-4 for a carve-out IPO) and/or the parent's completion
    8-K (Item 2.01 disposition). The product/asset separates from the shared services
    that produced it — the canonical `gap_45` generator.
  - **Roll-up (Stratum B):** a serial acquirer's repeated completion 8-Ks (Item 2.01) +
    S-4s consolidating multiple operating units onto one platform.
  - **Matched going-concern control:** a whole-company merger (DEFM14A / S-4 + completion
    8-K Item 2.01) where product, process, and organization transfer together, matched to
    a gap-prone case on SIC industry × size band × era.
- **Structural sub-dossier sources:** the closing filings above (S-4 / DEFM14A / Form 10 /
  8-K / proxy) — closing-time only. **Outcome sub-dossier sources:** the coded entity's
  subsequent **10-K / 20-F** at the 3–5-year horizon + reputable press — outcome-time only.
- **Outcome-blind structural inclusion filter (Amendment v1.3.0):** because pure
  form-type classification proved too crude (it admits SPACs and shells and carries no
  size signal — DRAW_QUALITY_FINDING.md), the seeded selection is restricted to frame
  rows that pass two closing-era, outcome-blind checks: (a) SIC ≠ 6770 (exclude
  blank-check / SPAC registrants, which are not going-concern deals); (b) a ≥ $1bn size
  band verified by an outcome-blind XBRL size proxy — the largest of us-gaap Assets,
  Revenues, or StockholdersEquity reported with a period end within ±2 years of the
  filing date. Both signals are structural and blind to the 3–5-year outcome. The frame
  snapshot (`pilot_frame_raw.csv`) records the FULL unfiltered enumeration; the filter is
  applied only when selecting.
- **Seeded, reproducible draw:** the pilot draw script queries EDGAR full-text / filing
  indices by form type + date window, classifies deal type per the above, applies the
  inclusion filter + size/era band, and makes a **seeded** random selection from each
  qualifying set, **blind to outcome** (the draw script prints the selected deals with no
  outcome field). Era window and size proxy are recorded at draw time. Committed with the
  seed BEFORE the draw; residual deal-value/type verification still happens at
  dossier-build.
- The concrete deal list produced by the seeded draw is recorded in `pilot_selection.csv`
  (created at draw time; not part of this pre-analysis commit).

## 3. Dossier construction (separated from the start — the S4 §1.4 requirement)

For each selected deal, two sub-dossiers are built as **separate files**:
- **Structural sub-dossier** — assembled ONLY from closing-time deal documents (merger
  agreement / S-4 / DEFM14A / Form 10 / 8-K / proxy). Contains no post-deal language.
  Codes `gap_45`, `gap_56`, `gap_mitigated`.
- **Outcome sub-dossier** — assembled ONLY from the realized 3–5-year record (subsequent
  10-K / 20-F + reputable press). Contains no deal-structure language. Codes
  `p4_pathway`, `p5_pathway`.
- The transaction whose 3–5-year window is the outcome is fixed at construction (the E06
  lesson — a later downstream deal's impairment is not attributed to the coded deal).
- **Anti-fabrication (HARD):** every coded field traces to a cited public primary source
  recorded in the sub-dossier; unverifiable facts are flagged, never guessed.

## 4. Measurement — 4-coder disjoint-pair rotation

- **Separated two-pass coding** reusing / extending the S4 harness
  (`research/empirical_cases_v1/recode_separated_passes.py`): structural pass sees only
  the structural sub-dossier; outcome pass sees only the outcome sub-dossier.
- **Coder pool (4 models, pinned):** Claude `claude-opus-4-8`, Gemini
  `gemini-3.1-pro-preview`, Grok `grok-4.3`, OpenAI `gpt-5.4-2026-03-05`. The OpenAI
  coder is the 4th model added specifically to make genuine per-construct rotation
  possible (verified against the live API — the general-purpose flagship, not
  codex/mini). A `code_with_openai` operator is added to the harness with the same
  structured-JSON contract + JSONL logging as the existing three.
- **Disjoint-pair per-construct rotation (pre-registered + seeded):** the 4 models are
  split into two disjoint pairs; for each case the **structural pass is coded by one
  pair and the outcome pass by the other**, so no model codes both constructs for the
  same case — removing the same-model shared-method variance evidence-separation alone
  leaves. Which pair codes the gap vs the pathway is **rotated across the 10 cases by a
  fixed seed**, so across the pilot every model codes both constructs on *different*
  cases (balancing model-level effects). The full rotation assignment
  (`pilot_rotation.json`: per case-slot → structural pair, outcome pair) is generated by
  the seed and **committed BEFORE any coding call**.
- **Blinding (HARD):** coders see only the evidence slice — never the hypotheses,
  predicted direction, or case-vs-control status.
- **Aggregation + reliability:** each construct is coded by **2 models** per case
  (the assigned pair) → agree-or-flag per cell (a 2-coder split is flagged as
  uncertain), and **per-construct Fleiss' κ is computed over 2 rater-slots**, pooling all
  cases regardless of which pair coded them. *Precision note:* 2-rater κ is coarser than
  the S4 3-rater κ; the disjointness (a cleaner IV/DV separation) is the deliberate
  trade for it, and at N=10 κ is already a coarse signal (§6). If a construct's flag rate
  is high (many 2-coder splits), that is itself a pilot finding about how many coders per
  construct the full draw needs. Every call JSONL-logged (`code/llm_call_logger.py`).

## 5. Analysis (descriptive — pipeline validation, not confirmatory)

`analyze_pilot.py` (committed with a synthetic `--fixture` self-check BEFORE any datum,
mirroring `analyze_deconfounding.py`) reports:
- per-construct Fleiss' κ (structural, outcome) with item counts;
- feasibility notes (source availability + per-deal effort);
- a porosity spot-check (confirm the structural slices carry no retrospective/outcome
  phrasing — an automated phrase scan like the S4 slicer's disjointness check);
- the **descriptive** necessary-condition 2×2 (`gap_any` × `p45_any`) with per-cell
  counts — reported as description only, no CI-based confirmatory claim.

## 6. Go/no-go criteria for the full N ≈ 300 draw (pre-registered)

Proceed to the full draw iff ALL hold; otherwise revise the design (or stop):
- **Reliability (coarse 2-rater signal at N=10):** per-construct κ ≥ .60 (structural)
  and ≥ .70 (outcome) — the S4 separated-coding baseline. NB the pilot κ is a **2-rater**
  κ (disjoint-pair design, §4) vs S4's 3-rater κ, so it is read as a directional check
  (is separated-from-start construction at least as reliable as slicing?) alongside the
  per-construct flag rate, not as a like-for-like number. At N=10 the κ CI is wide; a point
  estimate *below* threshold triggers a design look (inspect disagreements, tighten the
  coding brief) rather than an automatic veto, and a point estimate *at/above* threshold
  is read as "no reliability red flag," not as a precise estimate.
- **Feasibility:** median per-deal EDGAR construction effort compatible with completing
  N ≈ 300 within the planned program window (recorded, threshold set at draw time).
- **Porosity:** the structural-slice phrase scan is clean (no outcome/retrospective
  leakage) on ≥ 90% of pilot deals (i.e. ≥ 9/10).
- **Pipeline:** the full chain (EDGAR draw → separated dossier → rotated separated coding
  → assemble → analyze) runs end-to-end with logging intact.

A pilot that FAILS a criterion is itself a useful result — it says *what* to fix before
spending the full N ≈ 300 (the whole point of piloting first).

## 7. Discipline carried forward (unchanged)

Registered-before-data · blinded coding · anti-fabrication · LLM-call logging · additive
amendments — all HARD, per `PREREGISTRATION_V2.md` §5.

## Appendix — Files registered at this pilot pre-analysis commit

- `PILOT_PREREGISTRATION.md` — this document.
- `pilot_dataset.csv` — empty pilot schema (header row only), committed before any datum.

Still TO BUILD before any pilot datum (the registered-before-data scaffold this commit
begins; each committed before the step it gates):
- the `code_with_openai` operator (4th coder, `gpt-5.4-2026-03-05`) added to the
  separated-pass harness, with the same structured-JSON contract + JSONL logging as the
  existing three, and the harness generalized from a fixed triple to the 4-coder
  disjoint-pair rotation (2 coders per construct);
- the seeded pilot draw script (EDGAR, blind to outcome);
- the pre-registered rotation-assignment file `pilot_rotation.json` (per case-slot →
  structural pair, outcome pair);
- `analyze_pilot.py` with its `--fixture` self-check (2-rater per-construct κ +
  descriptive NC 2×2 + porosity + feasibility).

The concrete deal draw, the dossier construction, and the ≈40 coding calls happen only
after those are committed.
