# Full-draw frame-readiness finding (S5 Phase-B step 3)

**Date:** 2026-07-29. **Branch:** `feature/tba-s5-largen-2026bi`. **Status:** the
outcome-blind enumeration ran; the seeded `--draw` surfaced a frame-quality shortfall
that is a **pre-registered-frame design decision for the user** (a new fork, not covered
by the LOCKED DECISIONS). **No dossier built, no coding call made.** Registered-before-data
intact.

This is the full-draw analogue of the pilot's `DRAW_QUALITY_FINDING.md` /
`PILOT_FRAME_FINDINGS.md`, at N=350 scale.

## What ran

`draw_full_sample.py --enumerate` (SEC EDGAR full-text search + SEC bulk `frames` size
proxy + per-CIK SIC), then `--draw` (seeded 20260729, offline, applies the Amendment-2.C
inclusion filter: drop SIC 60xx/6770 + ≥$1bn deal-value materiality gate + per-SIC-2 cap).

- Enumerated frame: **1,049 outcome-blind registrant rows** →
  `full_draw_frame_raw.csv` (committed for transparency; the full unfiltered snapshot per
  FULL_DRAW_PREREGISTRATION §2).
- Draw output: **232 rows (116 gap-prone + 116 matched controls)** →
  `full_draw_selection.csv` (gate_status=PENDING). **This is UNDER the registered N=350
  target and is NOT the confirmatory sample** — it is the draw that surfaced the finding.

## The shortfall

| stratum | raw FTS hits | qualifying ≥$1bn | drawn (post per-SIC-2 cap) | target |
|---|---|---|---|---|
| carve_out | 95 | 51 | 35 | 35 |
| joint_venture | 219 | 35 | 35 | 35 |
| distressed | 196 | 29 | 26 | 35 |
| roll_up | 140 | 17 | 17 | 35 |
| acqui_hire | 6 | 3 | 3 | 35 |
| **gap-prone total** | | | **116** | **175** |
| control | 393 | 213 | 116 (matched) | 175 |

The inclusion filter dropped 15 excluded-SIC + 689 sub-threshold/unknown-size registrants.

## Why (diagnosed, not guessed)

1. **acqui_hire is structurally incompatible with a ≥$1bn operating-company frame.** Only
   **6 acqui-hire deals exist in EDGAR full-text at all** (across the whole 2006-2018 era),
   3 of them ≥$1bn. Acqui-hires are small talent acquisitions rarely disclosed as material
   in billion-dollar registrant filings. **Query-widening cannot fix this** — the deals
   are not in the universe at this size.
2. **roll_up / distressed are thinned by the ≥$1bn materiality gate AND a large
   unknown-size bucket** (59 roll_up, 84 distressed rows had no size fact in the bulk
   frames). A companyfacts spot-check of 40 unknown-size registrants found them
   **overwhelmingly no-XBRL-at-all** (19/20 roll_up, 17/20 distressed) — foreign/IFRS
   filers, pre-XBRL shells, non-reporting entities — and **zero** of the sampled ones
   were ≥$1bn. So resolving unknown-size does **not** recover the pools.

Net: the ≥$1bn EDGAR FTS positive-signal frame cleanly supplies only **carve_out** and
**joint_venture**; roll_up/distressed are partial; acqui_hire is empty.

## Why this matters for the campaign (why not just proceed)

The registered N=350 power target's binding constraint is **≥60 coded gap cases** at the
pilot-observed .40 gap prevalence among gap-prone. 116 gap-prone × .40 ≈ **46 gaps —
below the 60 floor**. The budget-capped fallback N=300 required gap prevalence ≥.475;
even there 116 × .475 ≈ 55, still short. So the current frame is **under-powered for the
pre-registered confirmatory test**, and spending ~700 dossier-builds + 2,100 paid coding
calls on it would burn real budget on a mis-specified sample.

## Options (for the user — a pre-registered-frame change + real-budget gate)

1. **Curated-list cross-check (Amendment 2.A — the registered remedy).** Hand-build
   curated lists of large (≥$1bn) roll-ups / distressed / carve-out deals from reliable
   sources, cross-check each against EDGAR primary filings, keep the build-time
   confirmation gate. Rigorous, holds ≥$1bn; heaviest to build; introduces (gated)
   curation. Acqui-hire remains near-empty even here.
2. **Rebalance onto the strata the frame supports + formally drop acqui_hire.**
   Concentrate the 175 gap-prone quota on carve_out + joint_venture (both fill) +
   widened roll_up/distressed (broaden their FTS queries/forms), and record acqui_hire as
   structurally absent at ≥$1bn (a finding). Stays fully in EDGAR-FTS method.
3. **Lower the materiality threshold** for gap-prone strata (e.g. ≥$250M or ≥$500M) so
   roll_up/distressed/acqui_hire fill; match controls on the same lower size band.
   Diverges from the pre-registered ≥$1bn; reintroduces smaller-deal heterogeneity.
4. **Two-stratum design at ≥$1bn** (carve_out + joint_venture only) — cleanest, most
   defensible frame; narrows the "gap-prone structure" generality claim.

**Recommendation:** a hybrid of **2 + 1** — rebalance onto carve_out/JV/roll_up/distressed
(drop acqui_hire as a documented structural absence), and use the Amendment-2.A curated
cross-check to top up roll_up/distressed to quota at ≥$1bn. This holds the pre-registered
size threshold, keeps the method reproducible, and hits the ≥60-gap power floor.

## RESOLVED — user chose the hybrid remedy (rebalance + curated top-up); Amendment 3 applied

**User decision (2026-07-29):** option 1 (hybrid). Applied as `FULL_DRAW_PREREGISTRATION.md`
Amendment 3 + `draw_full_sample.py` changes (commit `fb6c1859`), registered before any datum:
drop acqui_hire (documented structural absence); rebalance 175 gap-prone across the 4
remaining strata via GAP_QUOTAS (carve_out/JV/roll_up = 44, distressed = 43); widen
roll_up/distressed FTS queries; curated ≥$1bn top-up cross-checked against real EDGAR
CIK + closing-era accession (anti-fabrication HARD), FTS-first then curated. N=350 and the
≥$1bn threshold unchanged.

### Corrected (widened) enumeration + measured curated deficit

Re-enumerated with the Amendment-3 widened queries → 1,091 outcome-blind rows
(`full_draw_frame_raw.csv`, corrected snapshot). The corrected FTS-only `--draw` yields
**141 gap-prone** (up from 116). Remaining per-stratum curated deficit to reach quota:

| stratum | qualifying ≥$1bn (widened) | quota | curated needed |
|---|---|---|---|
| carve_out | 51 | 44 | 0 |
| joint_venture | 35 | 44 | **9** |
| roll_up | 39 | 44 | **5** |
| distressed | 23 | 43 | **20** |
| control | 213 | 175 | 0 (matched) |

**Total curated top-up needed: 34 ≥$1bn deals** (9 JV + 5 roll-up + 20 distressed), each
resolvable to a real EDGAR registrant CIK + a closing-era primary filing (2006-2018),
outcome-blind, entered into `full_draw_curated_gap_deals.csv`, re-verified at `--gate`.
Large ≥$1bn distressed/363 asset sales and JVs over 2006-2018 are plentiful, so the
deficit is readily fillable without lowering the size threshold.

**Next:** build the 34-deal curated list (anti-fabrication HARD; every deal EDGAR-verified),
then the corrected `--draw` (FTS + curated) → `--gate` → commit `full_draw_selection.csv` at
the registered N=350 → the ~700-dossier + 2,100-call paid campaign.

## Curated build DONE + N=350 draw COMPLETE (2026-07-30)

`build_curated.py` resolved 52 human-curated candidates against EDGAR → **50 verified
≥$1bn rows** (`full_draw_curated_gap_deals.csv`): distressed 27, JV 13, roll_up 10 (all
deficits met with margin), each carrying a real CIK + closing-era accession + SIC +
companyfacts size (anti-fabrication HARD — nothing hand-typed; retry-resilient;
nearest-fact + sourced-size fallbacks for near/pre-XBRL deals). The corrected `--draw`
writes the registered **N=350 exactly**: 175 gap-prone (carve_out/JV/roll_up 44,
distressed 43 = FTS 141 + curated 34: JV 9 + roll_up 5 + distressed 20) + 175 matched
controls. Known characteristic (documented, not blocking): roll_up ~45% SIC-67
(REIT/holding-company roll-ups; the curated top-up adds operating-company roll-ups;
industry is a controlled covariate). Reproducibility: the committed candidate list +
`build_curated.py` are the SSOT; the resolved CSV is the EDGAR projection of record.

## `--gate` exposed a control-screen operationalization issue (DECISION for the user)

The build-time `--gate` FAILed 167/350 (158 unreplaced), which is NOT real deal
failure — it is two fixable gate issues:

1. **Control screen (Amendment 2.B) is mis-operationalized — 156/175 controls FAIL on
   "Form 15 deregistration after the deal."** Controls are drawn from **DEFM14A** (the
   *target's* merger proxy), and a target that completes a whole-company acquisition
   **always files a Form 15** to stop reporting. So the screen penalizes exactly the
   completed acquisitions it should keep. Amendment 2.B's real intent ("acquirer keeps
   public reporting through the outcome window") is about the **acquirer**, whose CIK the
   target-side DEFM14A frame does not capture. Options for the user:
   - **(A, recommended) Defer the acquirer-reporting / going-private screen to
     dossier-build.** Stop failing controls on the target's own post-merger Form 15
     (that is expected + confirms the deal closed); at dossier-build, identify the
     acquirer and assess outcome observability, coding no-observable-outcome →
     *uncertain* (the already-registered no-record rule). Records as an additive
     amendment; keeps the target-keyed control frame.
   - **(B) Re-key controls to the acquirer** (draw the acquirer-side filing; measure the
     outcome on the acquirer/combined entity). Cleaner conceptually but a larger frame
     change (re-enumerate controls acquirer-side + re-match).
2. **`_has_form` technical bug (affects carve_out Form-10 check, 11 FAIL):** it reads only
   `submissions.recent` (~1000 latest filings), missing older Form-10s — but these
   carve-outs were *enumerated by requiring* a 10-12B/10-12G, so they demonstrably have
   one. Fix `_has_form` to page the full submissions history (the `files` array) so older
   filings are seen. (Clear technical fix, applies regardless of the control decision.)

`full_draw_gate_log.csv` holds all 350 verdicts. **No dossier, no coding call.** Awaiting
the control-screen decision; the corrected gate is re-run before dossier-build.
