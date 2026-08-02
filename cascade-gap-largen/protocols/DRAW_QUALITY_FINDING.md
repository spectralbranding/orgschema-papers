# Pilot draw quality finding (2026-07-29) — mechanical EDGAR form-type frame is too crude

**Status:** feasibility finding recorded at the seeded draw step, BEFORE any coding
call. The registered-before-data chain is intact (the draw script `draw_pilot_sample.py`
and the frame snapshot `pilot_frame_raw.csv` were committed before `pilot_selection.csv`;
no dossier built, no coding call made).

## What ran

Per `PILOT_PREREGISTRATION.md` §2 the pilot draw is seeded and blind to outcome, using
**filing/form type** as the deal-type classifier. `draw_pilot_sample.py --enumerate`
snapshotted a 175-registrant frame from EDGAR full-text search (34 carve-out Form 10-12B
+ 41 roll-up S-1/S-4 self-describing a "roll-up" + 100 control DEFM14A), attached each
registrant's SIC, and `--draw` (seed 20260729) produced the 10-deal stratified selection
(`pilot_selection.csv`).

## The finding

Pure form-type FTS classification gives **low stratum fidelity and no size guarantee**.
On manual inspection of the 10 drawn deals, roughly half fail the pre-registered
inclusion intent (US registrant, ≥ $1bn, correct deal *structure*):

| slot | deal | drawn stratum | problem |
|---|---|---|---|
| P05 | Upholstery International, Inc. | roll-up | SIC 7600 micro-cap repair-services shell; not a ≥$1bn platform roll-up |
| P09 | Federal Street Acquisition Corp. | control | SIC 6770 **blank-check / SPAC** — definitionally NOT a going-concern whole-company acquisition |
| P01 | Avaya Holdings Corp. | carve-out | 10-12B was a post-Chapter-11 relisting, not a divestiture carve-out |
| P02 | Epsilon Energy | carve-out | genuine spin-off but ~$150M — below the ≥$1bn band |
| P08 | RadiSys Corp | control | genuine whole-company merger but ~$74M — below the band |

Clean, usable draws in the same sample: P03 John Bean Technologies (real FMC carve-out),
P04 Colony NorthStar Credit RE (real REIT roll-up), P06 athenahealth (~$5.7bn control),
P07 Rowan Companies (~$12bn control), P10 Navigators Group (~$2.1bn control).

So the mechanical frame *works* end-to-end (real filings, real strata, reproducible
seeded draw) but is **too coarse to reliably deliver the intended case-control sample**:
SIC/form type does not separate SPACs and shells from operating carve-outs/roll-ups/
mergers, and enumeration carries no deal-size signal.

## Why this is a decision, not something to silently code through

`PILOT_PREREGISTRATION.md` §2 anticipated **size** failures and specified seeded
replacement at build. It did **not** anticipate **type** misclassification (SPAC-as-
control, shell-as-roll-up). Both the fix (add outcome-blind structural inclusion filters
+ a size gate, i.e. a change to the §2 procedure) and the alternative (code the sample
as-drawn for pipeline-validation only, accepting a noisy κ on degenerate cases) change
what the ≈40 paid coding calls buy and what the pilot's reliability read means. That is a
genuine fork surfaced to the user rather than guessed.

The pipeline itself (harness, 4-coder rotation, EDGAR draw, analysis + fixtures) is built,
committed, and green — this finding is about the sampling *frame*, not the machinery.

## Resolution (2026-07-29, user decision: revise frame + re-draw)

`draw_pilot_sample.py` gained an outcome-blind structural inclusion filter (Amendment
v1.3.0, `PILOT_PREREGISTRATION.md` §2): drop SIC 6770 blank-check/SPAC registrants +
require a ≥ $1bn size band via an outcome-blind XBRL size proxy (largest of us-gaap
Assets / Revenues / equity with a period end within ±2y of the filing). Re-enumeration
snapshotted 335 registrants; the filter dropped 1 blank-check + 186 sub-$1bn/unknown,
leaving qualifying pools carve_out=39 / roll_up=8 / control=101. The same seed (20260729)
re-drew a clean case-control sample (all ≥ $1bn operating registrants): P01 Bank First,
P02 JBT (FMC carve-out), P03 Adient ($13bn Johnson Controls seating carve-out), P04
Griffin REIT II + P05 Colony NorthStar (REIT roll-ups); controls FNB Bancorp, VeriFone,
Wabtec, Gramercy, LaSalle — each SIC-2 + era matched to its gap-prone case.

Residual (noted for dossier-build + the full-draw design): the roll-up qualifying pool is
small and REIT-dominated (both drawn roll-ups are REITs); carve-out P01 (Bank First) is a
bank 10-12B registration whose divestiture character is verified at build. These are frame
limitations to widen for the N≈300 draw, not blockers for the pilot's pipeline check.
