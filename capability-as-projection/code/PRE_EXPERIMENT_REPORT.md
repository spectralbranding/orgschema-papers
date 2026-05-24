---
title: "Pre-experiment Report: Firm-as-Event-Log Companion Computation"
paper_slug: capability_as_projection_paper
date: 2026-05-24
status: PRE-REGISTERED before execution
---

# Pre-experiment Report

Written before the companion simulation is run. This document fixes the
hypotheses, parameters, success criteria, and analysis plan in advance,
so that the post-experiment report can report results against
pre-registered predictions rather than post-hoc rationalizations.

## Scope and what this simulation is NOT

The synthetic Monte Carlo simulation specified here is a
**numerical-coherence check** for the formalism in
`FORMALISM_v0.md`. It tests whether the propositions P1, P2, P3 are
numerically internally consistent given the projection operator
`pi_lambda` and compatibility function `kappa`. It is **not** an
empirical confirmation of those propositions in real firms. Real-firm
confirmation requires the process-traced case-coding outputs in the
empirical companion (Disney-Pixar, Microsoft-Nokia, Toyota TPS) per
`METHODS_APPENDIX_event_coding_protocol.md`.

This caveat is critical for the post-experiment report. A "PASS"
on every check below does NOT permit the paper to claim empirical
confirmation; it only permits the claim that the formalism is
numerically coherent under the parameterizations tested.

## Hypotheses

From `FORMALISM_v0.md` Section 3 (P1, P2, P3) plus comparative-static
predictions derived from the formalism:

**H1 (P1 numerical-coherence).** Under the negotiated merge policy
(clean merge preserving both logs with last-write-wins on
policy conflicts), projection continuity ratio
`pi(L_M) / (pi(L_A) + pi(L_B))` should be close to 1.0 across all
conflict densities, deviating only by the negotiation cost (the
0.5x weighting on superseded policy events).

**H2 (P2 numerical-coherence).** Under the acquirer-supreme merge
policy (snapshot-import failure mode: target policy-bearing events
discarded on conflict), projection continuity ratio should fall
**monotonically** as conflict density increases. At conflict density
= 0, the two policies should be indistinguishable (no policy events
discarded under acquirer-supreme); at conflict density = 0.9, the
acquirer-supreme continuity ratio should fall well below the
negotiated ratio.

**H3 (P3 numerical-coherence).** Simulated writedown magnitude (the
fraction of `pi(L_A) + pi(L_B)` lost by the merger) should be
**monotonically increasing** in `1 - kappa` (conflict density) for
the acquirer-supreme policy. For the negotiated policy, writedown
should be small at all conflict densities (the formalism predicts
zero writedown for clean merges; the simulation predicts a small
positive value due to the negotiation-cost halving).

**H4 (decay parameter independence).** The lambda parameter rescales
absolute projection magnitudes but should NOT alter the qualitative
ordering of continuity_acquirer_supreme vs continuity_negotiated
at any given conflict density. (The mechanism in P1-P3 operates on
the log substrate, not on the decay weighting.)

## Parameters

| Parameter | Value |
|---|---|
| `RANDOM_SEED` | 42 |
| `N_TRIALS` per cell | 500 |
| `LOG_SIZE` | 200 events per log |
| Conflict densities tested | {0.0, 0.1, 0.2, 0.5, 0.9} |
| Decay parameters lambda tested | {0.0, 0.05, 0.1, 0.5} |
| Resolution policies | {negotiated, acquirer_supreme} |
| Event types | DECISION, FAILURE, POLICY, PERSONNEL, ARTIFACT |
| Event-type proportions | 0.30, 0.10, 0.20, 0.15, 0.25 |
| Event-type weights w_q | +1.0, -1.0, +1.0, 0.0, +0.5 |
| Time horizon | 5.0 years |
| Render time t | (max event time) + 1 year |
| Continuity tolerance band (descriptive only) | 0.10 |
| Total trials | 5 x 4 x 2 x 500 = 20,000 |

## Pre-registered analysis plan

1. **Aggregate** trial results by `(conflict_density, lambda, policy)`.
   Compute mean and standard error of `kappa`, `continuity_ratio`,
   `writedown` per cell. Write to `monte_carlo_results.csv`.

2. **Plot 1** (`plot_projection_continuity_vs_kappa.png`):
   continuity_ratio (y) vs kappa_mean (x), one line per
   `(policy, lambda)` pair, with stderr bars. Visualizes P1 + P2.

3. **Plot 2** (`plot_writedown_vs_conflict_density.png`):
   writedown_mean (y) vs `1 - kappa_mean` (x), one line per
   `(policy, lambda)` pair, with stderr bars. Visualizes P3.

4. **Numerical-coherence checks** (each evaluated post-hoc against the
   CSV):
   - **C1**: at conflict_density = 0.0, continuity ratio under
     BOTH policies should be within 0.02 of each other (no conflicts
     means no policy-resolution difference).
   - **C2**: at conflict_density = 0.9, continuity ratio under
     acquirer_supreme should be at least 0.10 below the negotiated
     ratio (the mechanism produces a meaningful gap).
   - **C3**: writedown_mean under acquirer_supreme should be
     monotonically non-decreasing in conflict_density (allowing for
     small Monte Carlo noise, defined as one violation of monotonicity
     by at most 0.01 across the 5-cell sequence).
   - **C4**: writedown_mean under negotiated should remain below
     0.30 at conflict_density = 0.9 (negotiation cost is bounded).
   - **C5**: at any fixed conflict_density, the sign of
     `continuity_acquirer_supreme - continuity_negotiated` should be
     the same across all four lambda values (H4 — lambda does not
     flip the qualitative ordering).

5. Each check produces a PASS / FAIL string in
   `POST_EXPERIMENT_REPORT.md` Section "Comparison to predictions",
   along with the underlying numerical values.

## Success criteria

The simulation is considered numerically coherent with the formalism
if **at least 4 of 5** of C1-C5 pass. Failure of one check is
acceptable (the formalism is a stylized model and the synthetic data
is parameter-sensitive); failure of two or more indicates a numerical
inconsistency that the post-experiment report must surface and the
formalism authors must address before paper submission.

A coherent result here does NOT confirm the propositions empirically;
an incoherent result here DOES indicate that the formalism contains
a numerical bug, a parameter-space gap, or a definitional ambiguity
that must be fixed.

## What would falsify each proposition

Even within the synthetic-coherence frame, the following patterns
would force a re-examination of the formalism (not the simulation):

- **Falsifies P1 numerical-coherence**: negotiated continuity ratio
  falls below 0.80 at any conflict density >= 0 (would indicate that
  the clean-merge policy itself destroys capability, contradicting the
  Disney-Pixar archetype).

- **Falsifies P2 numerical-coherence**: acquirer-supreme continuity
  ratio fails to fall as conflict density rises, OR remains
  indistinguishable from negotiated at high conflict density (would
  indicate that the snapshot-import failure mode is not captured by
  the formalism as written).

- **Falsifies P3 numerical-coherence**: writedown under
  acquirer-supreme is NOT monotonically increasing in conflict density
  (would indicate that the formalism's writedown prediction is
  non-monotonic in a way the propositions do not allow).

## Post-hoc protections

Decisions that are explicitly NOT permitted post-hoc:

- Changing `RANDOM_SEED` to obtain a more favorable plot.
- Changing the event-type proportions, weights, or LOG_SIZE.
- Dropping any conflict_density or lambda value from the reporting
  set.
- Filtering trials based on outlier criteria not specified here.

Decisions that ARE permitted post-hoc:

- Adding diagnostic sub-plots (small-multiples per lambda, sensitivity
  to LOG_SIZE) provided the four pre-registered outputs above are
  reported alongside.
- Reporting additional summary statistics beyond mean and stderr
  (e.g., median, IQR) provided the pre-registered means are reported.

## Files produced by execution

- `code/monte_carlo_results.csv`
- `code/plots/plot_projection_continuity_vs_kappa.png`
- `code/plots/plot_writedown_vs_conflict_density.png`
- `code/logs/projection_demo_output.txt`
- `code/logs/monte_carlo_run_output.txt`

The post-experiment report references these files by relative path.
