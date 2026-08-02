# S5 pilot results + pre-registered go/no-go read

Run 2026-07-29 on branch `feature/tba-s5-largen-2026bi`. Descriptive
feasibility/pipeline-validation pilot (NOT confirmatory) per `PILOT_PREREGISTRATION.md`
(v1.3.0). Ten deals, separated-from-the-start sub-dossiers from SEC EDGAR primary
filings, 4-coder disjoint-pair per-construct rotation (40 coding calls). This document
reports the pre-registered go/no-go and its interpretation; frame findings are in
`PILOT_FRAME_FINDINGS.md`. **The full N≈300 draw decision is the user's.**

## 1. Pre-registered go/no-go table (PILOT_PREREGISTRATION.md §6)

| Criterion | Result | Threshold | Verdict |
|---|---|---|---|
| Reliability — structural κ | .687 | ≥ .60 | **PASS** |
| Reliability — outcome κ | .419 | ≥ .70 | **COARSE-LOW** (see §3) |
| Porosity (clean structural slices) | 10/10 | ≥ 9/10 | **PASS** |
| Feasibility (built + coded end-to-end) | 10/10 | 10/10 | **PASS** (with caveats, §4) |
| Pipeline (draw→dossier→rotated coding→assemble→analyze) | end-to-end | runs | **PASS** |

Pooled 2-rater Fleiss' κ (coarse signal at N=10, as pre-registered). All 40 rater-slots
present after recovering 2 Gemini calls (§5).

## 2. Descriptive necessary-condition 2×2 (description only — pilot not powered)

`gap_any × p45_any` over the 10 deals:

| | outcome pathway | no pathway |
|---|---|---|
| **structural gap** | n11 = 1 (P03 Adient) | n10 = 2 (P02 JBT, P08 Wabtec) |
| **no structural gap** | n01 = 1 (P05 Colony/BrightSpire) | n00 = 6 (P01, P04, P06, P07, P09, P10) |

Per-case reading:
- **P03 Adient** (gap + fail): the one cleanly-drawn genuine carve-out; structural product↔shared-services
  gap AND a realized product/process pathway (SS&M impairments). The anchor pattern.
- **P02 JBT** (gap + ok): genuine carve-out with a structural gap that was contractually
  mitigated (gap_mitigated = yes) and did not realize a pathway — a gap-prone-but-successful case.
- **P08 Wabtec** (gap + ok): a "control" that is structurally an RMT carve-out (coded gap_56); no realized pathway.
- **P05 Colony/BrightSpire** (no-gap + fail — the necessity-breaking cell): structural coders read no
  closing gap (externally-managed roll-up), but outcome coders read a process/organization pathway. This is
  exactly the case type to examine at scale — either a genuine necessity-breaker or a struct/outcome
  measurement boundary case.
- **n00 (6 cases)**: includes the two mis-draws (P01 uplisting, no separation) and the two go-private
  controls (P07, P09) whose "no pathway" is an ABSENCE OF OUTCOME DATA, not observed no-failure (§4).

The pilot makes no confirmatory claim from this table (no CI/p; not powered — the
confirmatory necessary-condition test is the full S5 draw).

## 3. Interpreting the outcome-κ "COARSE-LOW" (the key reliability nuance)

The outcome κ = .419 is **substantially a low-base-rate artifact, not a coding-quality
failure**:
- **Raw agreement is high**: observed agreement P̄ = .825 (82.5% of rater-slots agree), only
  3/10 cases carry any outcome flag.
- **Base rate is extreme**: category proportions are 0 = .825, 1 = .050, uncertain = .125 —
  pathways are rare events, so chance agreement Pₑ = .699 is high and deflates κ (the classic
  Fleiss-κ prevalence paradox: high agreement, low κ).
- The **structural** construct is better balanced (0 = .80, 1 = .20, uncertain = 0; P̄ = .90) so
  its κ = .687 is not prevalence-deflated and clears the bar.

Implications for the full draw (do NOT treat outcome κ as a design veto):
1. The **case-control design deliberately over-samples gap-prone structures**, which should raise
   the pathway base rate and stabilize outcome κ (the pilot's control-heavy 5/10 + go-private 0s
   depress it here).
2. Report a **prevalence-adjusted statistic** (e.g. PABAK / Gwet's AC1) alongside κ for the rare
   pathway cells, and keep raw agreement in view.
3. Consider a **3rd rater per construct** for the full draw (the pilot's 2-rater disjoint design
   trades precision for a cleaner IV/DV separation; on rare cells the extra rater helps most).
4. Tighten the outcome codebook's "no pathway documented" vs "cannot determine" boundary so
   go-private/no-record cases resolve to *uncertain*, not 0 (§4).

## 4. Feasibility: the mechanics PASS, but the frame is not yet fit to scale

The pipeline ran end-to-end on real primary filings and porosity closed 10/10 — the
separated-from-the-start construction removed the residual retrospective leak S4's slicer
could not. But build-time verification surfaced sampling-frame problems that gate the full
draw (full detail in `PILOT_FRAME_FINDINGS.md`):
- **Carve-out draw by form-type is unreliable**: 2 of 3 drawn "carve-outs" are not carve-outs
  (P01 Bank First = a Nasdaq uplisting registration; P02 JBT drawn accession = a rights-plan
  amendment, rebuilt from JBT's genuine 2008 FMC spin-off, era outside frame). Only P03 was
  cleanly drawn. The full-draw frame needs a positive spin-off/divestiture signal (parent Item-2.01
  disposition 8-K / distribution-ratio disclosure / curated spin-off list) + a build-time gate.
- **Control pool needs a whole-company + acquirer-still-reporting screen**: 2 of 5 controls went
  private (P07 VeriFone, P09 Gramercy) → no public 3–5yr outcome (coded 0 for absence of data, which
  biases n00); P08 (Wabtec/GE Transportation) is itself an RMT carve-out, not a whole-company control.
- **Roll-ups discriminated as intended** (a good sign): P04 internalized management (no gap) vs P05
  stayed externally managed (candidate gap → the necessity-breaking case).
- Carry-forward: the ≥$1bn size gate skews the pool to asset-heavy financials (`DRAW_QUALITY_FINDING.md`).

## 5. Pipeline-robustness finding + fix (Gemini structured-JSON)

The `gemini-3.1-pro-preview` coder deterministically failed on 2/40 calls: it requires
thinking mode (budget 0 → 400 INVALID_ARGUMENT), and its mandatory thinking trace consumed
the output allowance, so the structured JSON dropped its trailing `}` (or, on the no-cost API quota,
appended a stray `)."` tail). Fixes applied to `recode_separated_passes.py` and verified before
re-run: (a) raised `max_output_tokens` to 16384 with `thinking_budget=512`; (b) switched the
Gemini key preference to the paid `GOOGLE_API_KEY`; (c) added a `_lenient_json` fallback that
recovers both malformed shapes (the last schema field `rationale` is a non-scored text field, so
truncation never touches a coded cell). After the fix the 2 calls recovered cleanly (full 40/40
coverage). **For the full draw:** keep the robust parser + retry logic; expect ~5% raw Gemini
formatting failures without it.

## 6. Net read

- The **coding pipeline is validated**: it runs end-to-end, porosity closes, structural
  reliability is acceptable, and the outcome-reliability shortfall is largely a rare-event
  prevalence artifact with concrete mitigations (§3), not a coding-quality failure.
- The **sampling frame is NOT yet fit to scale**: the carve-out draw and the control screen both
  need redesign (§4) before spending the full N≈300.
- Recommended sequencing for a full-draw GO (the decision is the user's): (1) fix the frame
  (positive spin-off signal + whole-company/acquirer-reporting control screen + cascade-relevant
  SIC scoping), (2) add a 3rd rater per construct and a prevalence-adjusted reliability statistic,
  (3) tighten the outcome "no-record → uncertain" boundary, then (4) run the registered full draw.

The pilot did its job: for a cost of 40 coding calls it caught a broken sampling frame, a
rare-event reliability nuance, and a pipeline bug BEFORE the ~1,800-call full draw.
