---
title: "Full-draw pre-registration — the registered N=350 case-control replication of the cascade-gap necessary-condition"
version: 1.0.0
status: pre-analysis registered (full-draw design; NO full-draw datum collected)
registered_at: 2026-07-29
registered_by: Dmitry Zharnikov
program_stage: "S5 (paper 2026bi), full draw — after the pilot go/no-go + user fix-the-frame-then-GO"
parent_design: "research/empirical_cases_v1/PREREGISTRATION_V2.md (the locked S5 blueprint) + its Amendment 2 (the post-pilot frame + reliability redesign)"
supersedes: "the pilot phase (research/cascade-gap-largen/PILOT_PREREGISTRATION.md) — the pilot validated the pipeline; this document registers the full confirmatory draw"
registration_anchor: |
  This document's first-public-commit SHA + timestamp in the spectral-branding repo is
  the verifiable registered-before-data anchor for the FULL DRAW. The full-draw draw
  script, the build-time confirmation gate, the 3-rater rotation assignment, the analysis
  pipeline (with prevalence-adjusted reliability), and the empty full-draw schema are all
  committed BEFORE any full-draw deal is drawn, any sub-dossier is built, or any coding
  call is made. Deviations after this commit are numbered amendments; the locked body is
  not modified.
---

# Full-draw pre-registration — the registered N=350 confirmatory replication

This document freezes the OPERATIONAL protocol for the confirmatory Stage-S5 large-N
draw. The DESIGN lives in `PREREGISTRATION_V2.md` (§1 construct separation, §2
case-control frame, §4 analysis plan) as amended by its **Amendment 2** (the post-pilot
frame + reliability redesign — carve-out positive-signal + build-time gate, whole-company
control screen, wider SIC scoping, 3-rater/construct + Gwet's AC1, tightened no-record
boundary, and the power-finalized N). This file is the single registered anchor that ties
those to concrete, seeded, reproducible procedures and to the files committed before any
datum. It is confirmatory (unlike the pilot): the necessary-condition / safe-harbor claim
is pre-registered here (Locked Decision 3).

## 1. Sample (registered)

- **N = 350**, 1:1 case-control: **175 gap-prone case deals + 175 matched whole-company
  going-concern controls** — finalized by `power_analysis_s5.py` (seed 20260729),
  `POWER_ANALYSIS_RESULTS.md`. Sizing target: exact upper 95% CI on P(fail | no gap) ≤ .05
  (safe-harbor precision) AND ≥ 60 coded gap cases (nominal band 60-80) under the
  pilot-observed conservative gap prevalence (.40 among gap-prone).
- **Case strata (gap-prone, per `PREREGISTRATION_V2.md` §2.1):** carve-outs/divestitures,
  acqui-hires, roll-ups, joint ventures, distressed/asset-only deals — spread across the
  five strata with a per-SIC-2 cap so no single industry dominates (Amendment 2.C).
- **Control stratum:** whole-company going-concern acquisitions whose acquirer keeps
  public reporting through the outcome window, matched on structure + SIC-2 × size band ×
  era (Amendment 2.B).
- **Budget-capped fallback (registered):** if capped, N = 300 (150 + 150) conditional on
  the frame fixes lifting gap prevalence to ≥ .475, with a stop-rule drawing gap-prone
  deals until ≥ 60 coded gaps are reached.

## 2. Draw (registered, seeded, outcome-blind)

- **Universe:** SEC EDGAR completed US transactions (every coded field traces to a public
  primary filing — anti-fabrication + reproducibility), as in the pilot.
- **Carve-out/divestiture case selection — POSITIVE signal (Amendment 2.A):** a parent
  Item-2.01 disposition-completion 8-K + a distribution-ratio / former-parent information
  statement + a separation/TSA/tax-matters agreement, OR a curated divestiture list
  cross-checked against EDGAR. **NOT** filing-form-type alone.
- **Build-time confirmation gate (HARD, Amendment 2.A):** before a drawn deal enters the
  sample, verify from primary filings (a) a divesting parent, (b) a separation/TSA/tax
  agreement, (c) a product/asset↔shared-services separation. A deal that fails is replaced
  by the next seeded draw, logged with the failure reason; it is never coded.
- **Control selection screen (HARD, Amendment 2.B):** whole-company going-concern +
  acquirer-still-reporting; screen out RMT/carve-out-into-acquirer + going-private exits
  (or explicitly budget a retained going-private control as press-only → *uncertain*).
- **Size / SIC scoping (Amendment 2.C):** deal-value size measure + cascade-relevant /
  operating-company SIC; per-SIC-2 cap; exclude SIC 60xx/6770 from the operating strata.
- **Seed:** the full-draw seed is recorded in the draw script at the registration commit;
  the full unfiltered enumeration snapshot is retained for transparency; the filter +
  gate are applied only at selection/build.

## 3. Dossier construction (separated from the start — unchanged from V2 §1.4 / pilot §3)

Two sub-dossiers per deal, stored as separate files: a **structural** sub-dossier from
closing-time deal documents only (merger agreement / S-4 / DEFM14A / Form 10 / 8-K /
proxy), and an **outcome** sub-dossier from the realized 3–5-year record only (subsequent
10-K/20-F + reputable press). Anti-fabrication HARD: every coded field cites a public
primary source; unverifiable facts flagged `[UNVERIFIED]`, never guessed. The coded
transaction's outcome window is fixed at construction (the E06 lesson).

## 4. Measurement — 3 raters per construct (Amendment 2.D)

- Coder pool: Claude `claude-opus-4-8`, Gemini `gemini-3.1-pro-preview`, Grok `grok-4.5`,
  OpenAI `gpt-5.6-sol` — each provider's current frontier reasoning model. For each case,
  **3 of the 4 code the structural construct and 3 code the outcome construct, rotated so
  the two triples differ** (max per-construct coder separation a 4-model pool allows),
  seed-fixed in `full_draw_rotation.json`.
  - **Amendment 5 (coder-pool refresh, pre-DATA 2026-08-01, registered before any coding
    call):** Grok `grok-4.3`→`grok-4.5` (xAI frontier, 2026-07; reasoning-only + cheaper)
    and OpenAI `gpt-5.4-2026-03-05`→`gpt-5.6-sol` (GPT-5.6 frontier reasoning) upgraded to
    each provider's newest flagship — quality-first, not cost-driven. Claude Opus 4.8 kept
    (Anthropic's frontier *reasoning* tier; Fable 5 is a higher long-horizon-agentic tier
    and overshoots per-dossier classification). Gemini 3.1 Pro (Preview) kept (Gemini 3.5
    *Pro* has not shipped — only 3.5 Flash; 3.1 Pro is the live flagship Pro). The seed,
    N=350, and 3-of-4 rotation structure are UNCHANGED (rotation regenerated identical).
    Registered-before-data intact: no coding call has run. The run session MUST smoke-test
    one call per model against the live API before the full 2,100 (reasoning models: grok
    and gpt-5.6-sol are default-only on sampling; both backends updated accordingly).
- Structural pass sees only the structural sub-dossier; outcome pass only the outcome
  sub-dossier. Blinding HARD (no hypotheses / predicted direction / case-vs-control status).
- Reliability: per-construct Fleiss' κ over 3 rater-slots **AND Gwet's AC1** (prevalence-
  adjusted; Gwet 2008) + raw agreement. AC1 is the primary read for the rare outcome cell.
- Every call JSONL-logged (`code/llm_call_logger.py`); the Gemini robustness fix
  (max_output_tokens=16384, paid `GOOGLE_API_KEY`, `_lenient_json`) is carried forward.

## 5. Analysis (confirmatory — `PREREGISTRATION_V2.md` §4 + Amendment 2.F)

- **Primary (pre-registered confirmatory):** P(fail | no gap) with an exact binomial
  (Clopper-Pearson) upper 95% CI — the safe-harbor / empty-cell test; necessity
  consistency P(gap | fail); NCA ceiling effect (Dul 2016), CE-FDH + CR-FDH lines +
  bottleneck table.
- **Secondary (robustness section, NOT a second headline):** discrete-time survival
  (Allison 1982) of the outcome pathway on the structural gap + controls (industry, deal
  size, era, relatedness, acquirer experience); matching justification (Rosenbaum & Rubin
  1983).
- **Sufficiency reported, never headlined** (selection-on-the-IV constraint, Amendment 2.F).
- **Robustness:** 10% human-coded IRR subsample; drop-one-stratum sensitivity.

## 6. Go criteria are already met (this is the confirmatory run, not another gate)

The pilot's go/no-go (κ / porosity / feasibility / pipeline) is passed; the user issued
fix-the-frame-then-GO. This draw executes the confirmatory test. Its result — whatever the
direction — is reported honestly (a weakening of the safe harbor is a finding, not smoothed
away), consistent with the V2 §3 interpretation rule carried to the confirmatory scale.

## 7. Discipline carried forward (all HARD, unchanged)

Registered-before-data · blinded coding · anti-fabrication (Crossref-verify every new
citation before the substrate) · LLM-call JSONL logging · additive amendments — per
`PREREGISTRATION_V2.md` §5.

## 8. Amendment 3 (2026-07-29 — frame-readiness fix; ADDITIVE, registered before any datum)

The seeded full-draw enumeration + `--draw` (committed `75c0d9fe`;
`FULL_DRAW_FRAME_FINDINGS.md`) surfaced that the ≥$1bn EDGAR-FTS positive-signal frame
cannot supply the registered 175 balanced gap-prone cases: it yielded 116 gap-prone
(< the ≥60-coded-gap power floor at the pilot's .40 gap prevalence). This amendment fixes
the **frame** only; the N=350 target, the size threshold (≥$1bn), the construct-separated
measurement, the 3-of-4 rotation, and the confirmatory analysis are all **unchanged**.
The user chose the hybrid remedy (rebalance + curated top-up) after the finding was
surfaced. Registered BEFORE the corrected draw; no coded datum exists.

- **3.A — Drop the acqui_hire stratum (documented structural absence).** Only 6 acqui-hire
  deals exist in all of EDGAR full-text over 2006-2018, 3 of them ≥$1bn; billion-dollar
  acqui-hires essentially do not exist, so the stratum cannot be balanced at the registered
  size. It is removed from the design and reported as a scope finding (not a failure).
- **3.B — Rebalance the 175 gap-prone across the four remaining structure types** via
  per-stratum quotas `carve_out=44, joint_venture=44, roll_up=44, distressed=43` (equal as
  possible; sum 175). Controls stay 175 (matched). N=350 unchanged.
- **3.C — Widened FTS queries** for the two thinnest strata (outcome-blind, closing-era text
  only): `roll_up` adds forms 8-K/10-K + the PE buy-and-build vocabulary
  ("buy-and-build" / "platform acquisition" / "add-on acquisition" / "roll up strategy");
  `distressed` adds forms S-4/DEFM14A + distressed-M&A vocabulary ("stalking horse" /
  "debtor-in-possession" / "chapter 11 plan"). These lift the qualifying ≥$1bn pool before
  any curation.
- **3.D — Curated ≥$1bn top-up (Amendment 2.A curated-list option), for the residual
  deficit after 3.C.** Where a stratum's widened-FTS qualifying pool is still short of its
  quota, it is topped up from a curated list of ≥$1bn deals **of that structure**, subject
  to the same size/SIC inclusion filter and the same build-time `--gate`. **Sourcing
  (anti-fabrication HARD):** curated candidates are identified from reputable public deal
  records (major-press M&A coverage; for distressed, court/bankruptcy dockets; company IR),
  and **every** curated deal must resolve to a real EDGAR registrant CIK **and** a
  closing-era primary filing (accession) before it enters `full_draw_curated_gap_deals.csv`;
  a candidate that cannot be resolved to EDGAR is excluded, never guessed. The curated list
  is outcome-blind (closing-era structural facts only) and committed before the corrected
  `--draw`. It is NOT form-type-only selection; it is a name-level positive identification
  cross-checked against primary filings.
- **3.E — Draw preference order:** each stratum is filled from its qualifying FTS pool first
  (per-SIC-2 capped), then topped up from the curated pool (deduped by CIK); the seeded,
  deterministic draw and the per-SIC-2 dominance cap are unchanged.

Implemented in `draw_full_sample.py` (GAP_STRATA/GAP_QUOTAS/widened STRATUM_QUERIES +
`load_curated`/`CURATED_CSV`; `--fixture` PASS; black/flake8/mypy clean) and
`full_draw_curated_gap_deals.csv` (empty header scaffold, populated in the curated build
before the corrected draw).

## 9. Amendment 4 (2026-07-30 — control-screen operationalization; ADDITIVE, before any datum)

The build-time `--gate` (run on the N=350 selection; `FULL_DRAW_FRAME_FINDINGS.md`) failed
156/175 controls on "Form 15 deregistration after the deal." This is a mis-operationalization
of the Amendment-2.B control screen, not real deal failure: controls are drawn target-side
(DEFM14A merger proxy), and a target that COMPLETES a whole-company acquisition always files
a Form 15 to stop reporting — so a post-deal Form 15 is EXPECTED and confirms the merger
closed, not a disqualifier. Amendment 2.B's real intent (an observable 3-5-year outcome;
screen out going-private / no-public-successor deals) concerns the ACQUIRER, whose CIK the
target-side frame does not capture. User decision (2026-07-30): **defer the acquirer check to
dossier-build** (over re-keying controls acquirer-side). Registered before any coded datum.

- **4.A — Control gate no longer fails on the target's post-deal Form 15.** `gate_control`
  PASSes controls at build time; the acquirer-reporting / going-private / outcome-observability
  determination moves to dossier-build, where the acquirer is identified and, if no public
  3-5-year outcome exists, the case is coded *uncertain* (the already-registered no-record
  rule, V2 §4 / Amendment 2.D). The target-keyed control frame is unchanged.
- **4.B — `_has_form` scans the FULL submissions history** (the `recent` block PLUS the
  paginated `files` archives), not just the ~1000-filing recent window. This fixes false
  carve_out gate failures where a pre-2011 Form-10 information statement (required at
  enumeration) was invisible to a recent-only scan.

Implemented in `draw_full_sample.py` (`gate_control` revised; `_all_forms`/`_has_form`
paged; `--fixture` PASS; black/flake8/mypy clean). The gate is re-run on the canonical
seeded N=350 selection; `full_draw_gate_log.csv` records every verdict.

## Appendix — Files registered at this full-draw pre-analysis commit

- `FULL_DRAW_PREREGISTRATION.md` — this document.
- `PREREGISTRATION_V2.md` Amendment 2 — the design change this operationalizes.
- `power_analysis_s5.py` + `POWER_ANALYSIS_RESULTS.md` — the N=350 derivation (seed 20260729).
- `DR_PHASE2_VERIFICATION.md` — the Crossref verification of every new anchor.
- `full_draw_dataset.csv` — empty full-draw schema (header row only), committed before any datum.

Still TO BUILD before any full-draw datum (each committed before the step it gates):
- the full-draw draw script (positive divestiture signal + build-time gate + control
  screen + deal-value/SIC scoping; seeded, outcome-blind);
- `full_draw_rotation.json` (per case → structural triple, outcome triple; seed-fixed);
- the 3-rater coding harness (generalize the pilot's 4-coder disjoint-pair runner to
  3-of-4 per construct) + the analysis pipeline emitting κ AND Gwet's AC1, with a
  `--fixture` self-check.

The concrete draw, the ~700 sub-dossiers, and the 2,100 coding calls happen only after
those are committed.
