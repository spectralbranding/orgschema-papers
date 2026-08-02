# S5 full-draw power / precision analysis — result + registered N

Run 2026-07-29 (seed 20260729, 20,000 reps/point) by
`research/cascade-gap-largen/power_analysis_s5.py`. Reproduce:

```
uv run --with scipy --with numpy python research/cascade-gap-largen/power_analysis_s5.py
```

This finalizes the exact N the Locked-Decision-14 "N ≈ 300" left to a power analysis
(`PROGRAM_PLAN.md` §3 item 14; `PREREGISTRATION_V2.md` §2.3). Sizing is on the
**necessary-condition / safe-harbor** effect, never the sufficiency odds ratio.

## Targets (pre-registered)

- **T1 (safe-harbor precision).** Exact (Clopper-Pearson) upper 95% CI on P(fail | no
  gap) ≤ .05, met with probability ≥ .90 across the grid, under the world where
  necessity **holds** (leak ∈ {0, .005, .01}).
- **T2 (necessity / NCA precision).** ≥ 60 coded gap cases (nominal band 60-80), met
  with probability ≥ .90 across the gap-prevalence grid.
- **T3 (detection, reported not a veto).** Power to REJECT a false safe harbor (exact
  lower 95% CI on P(fail | no gap) > 0) at a true .03-.05 necessity leak.

## Result table (worst case over the parameter grid)

| N_gap-prone | N_control | N | P(T1) | P(T2) | T3 power | max median upper | 10th-pct gaps |
|---|---|---|---|---|---|---|---|
| 100 | 100 | 200 | .831 | .000 | .984 | .0347 | 35 |
| 120 | 120 | 240 | .906 | .052 | .993 | .0344 | 43 |
| 140 | 140 | 280 | .950 | .448 | .997 | .0315 | 51 |
| 150 | 150 | 300 | .964 | .711 | .998 | .0297 | 55 |
| 160 | 160 | 320 | .975 | .880 | .999 | .0282 | 59 |
| **175** | **175** | **350** | **.986** | **.980** | **.999** | **.0271** | **65** |

## Registered design: N = 350 (175 gap-prone + 175 matched going-concern controls, 1:1)

- **Binding constraint is T2**, not T1. T1 (safe-harbor precision) is comfortably met by
  N ≥ 240 because the no-gap cell is large (controls + no-gap gap-prone). The gap CELL is
  what needs volume: at the conservative gap-prevalence corner (p_gap | gap-prone = .40 —
  **exactly the pilot's observed rate: 2 of 5 gap-prone deals carried a coded gap**), only
  N = 350 delivers ≥ 60 gap cases with probability ≥ .90 (10th-percentile gap count 65).
- **Why not N = 300?** N = 300 delivers the 60-80 band under *expected* gap prevalence
  (median 77 gaps at p = .475) but only P(T2) = .71 at the pilot's pessimistic .40 corner.
  The frame fixes (positive spin-off signal) should raise the gap-prone hit rate above the
  pilot's 40% by removing mis-draws (e.g. the P01 uplisting that diluted the carve-out
  stratum), but the pre-registration sizes for the observed-conservative corner.
- **N = 300 documented fallback.** If the full draw is budget-capped, N = 300 (150 + 150,
  1,800 calls) is adequate *conditional on* the frame fixes lifting gap prevalence to ≥ .475;
  it should then be paired with a stop-rule that keeps drawing gap-prone deals until ≥ 60
  coded gaps are reached.
- **Budget note.** N = 350 → **2 sub-dossiers × 350 × 3 raters/construct = 2,100 coding
  calls** (1,050 structural + 1,050 outcome) + ~700 sub-dossiers. This is +17% over the
  nominal ~1,800-call / ~600-dossier figure the ≈300 target implied — the increment buys
  robustness of the 60-80 gap band against the pilot-observed 40% gap prevalence.

## Reproducibility (PAQS 37)

Fixed seed 20260729; scipy Clopper-Pearson (exact Beta-quantile) for both bounds; the
`--fixture` mode self-checks the CP kernels against known values (CP(0,60) = .0487,
CP(0,100) = .0295) and the vectorised/scalar equivalence. Script published with the
paper's computational artifact at drafting (Phase C).
