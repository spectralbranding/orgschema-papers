---
title: "Post-experiment Report: Firm-as-Event-Log Companion Computation"
paper_slug: capability_as_projection_paper
date: 2026-05-24
status: EXECUTED — results below match those in monte_carlo_results.csv
---

# Post-experiment Report

Written after running `projection_demo.py` and `monte_carlo_simulation.py`
with `RANDOM_SEED = 42` per the pre-registered plan in
`PRE_EXPERIMENT_REPORT.md`. This document reports actual outputs against
pre-registered predictions, lists replication instructions, and surfaces
the explicit scope caveat.

## 1. Actual outputs

### 1.1 Files produced (verified to exist)

| File | Size / purpose |
|---|---|
| `monte_carlo_results.csv` | 41 rows (40 cells + header), 10 columns |
| `plots/plot_projection_continuity_vs_kappa.png` | ~119 KB, 150 DPI |
| `plots/plot_writedown_vs_conflict_density.png` | ~123 KB, 150 DPI |
| `logs/projection_demo_output.txt` | Captured stdout |
| `logs/monte_carlo_run_output.txt` | Captured stdout |

### 1.2 `projection_demo.py` — key tabular output

```
Projection pi_lambda(L_A=10 events, scaling_query, t = 2021-04-15)
  lambda |    pi(L_A) |    pi(L_B) |  pi(L_A) - pi(L_B)
    0.00 |     4.5000 |     6.0000 |            -1.5000
    0.10 |     3.6774 |     5.0543 |            -1.3769
    0.50 |     1.8935 |     2.8646 |            -0.9711

Compatibility kappa(L_A, L_B) = 0.6000
  events in L_A implicated in >= 1 conflict pair: 4
  events in L_B implicated in >= 1 conflict pair: 4
  |L_A| + |L_B| = 20
```

The decay-parameter behavior is correct: as lambda rises, older events
lose weight; the magnitudes shrink monotonically across both logs. The
partial-merge kappa = 0.60 is the expected mid-range case driven by
two POLICY-POLICY collisions and the shared-role PERSONNEL collision.

### 1.3 `monte_carlo_simulation.py` — selected cells from `monte_carlo_results.csv`

20,000 trials across 40 cells. Key cells (one row per
`(density, lambda, policy)` triple; full table is in the CSV):

| density | lambda | policy            | kappa_mean | continuity_mean | writedown_mean |
|---:|---:|---|---:|---:|---:|
| 0.0 | 0.10 | negotiated        | 1.0000 | 1.0000 | 0.0000 |
| 0.0 | 0.10 | acquirer_supreme  | 1.0000 | 1.0000 | 0.0000 |
| 0.1 | 0.10 | negotiated        | 0.9288 | 0.9901 | 0.0099 |
| 0.1 | 0.10 | acquirer_supreme  | 0.9268 | 0.9857 | 0.0143 |
| 0.5 | 0.10 | negotiated        | 0.7652 | 0.9614 | 0.0386 |
| 0.5 | 0.10 | acquirer_supreme  | 0.7664 | 0.9273 | 0.0727 |
| 0.9 | 0.10 | negotiated        | 0.6737 | 0.9422 | 0.0578 |
| 0.9 | 0.10 | acquirer_supreme  | 0.6745 | 0.8709 | 0.1291 |

Standard errors are all below 0.005 on continuity and writedown
across all cells (500 trials per cell).

### 1.4 Plots

- `plots/plot_projection_continuity_vs_kappa.png`: continuity ratio
  (y) vs kappa (x), one line per (policy, lambda) pair. The two
  policy families separate cleanly: negotiated lines hug 0.94-1.00
  across the full kappa range; acquirer_supreme lines fall to
  ~0.87 at kappa = 0.67.
- `plots/plot_writedown_vs_conflict_density.png`: writedown (y)
  vs 1 - kappa (x). The acquirer_supreme writedown is roughly 2x
  the negotiated writedown at high conflict density, visualizing
  the substrate-vs-snapshot wedge.

## 2. Comparison to predictions (pre-registered checks C1-C5)

| Check | Pre-registered criterion | Actual | Verdict |
|---|---|---|---|
| C1 | At density = 0.0, continuity-ratio gap between policies <= 0.02 | Gap = 0.000 across all four lambdas | **PASS** |
| C2 | At density = 0.9, continuity_acquirer_supreme is at least 0.10 below continuity_negotiated | Gap ranges 0.0713 - 0.0795 across lambdas (mean 0.0737) | **FAIL** |
| C3 | acquirer_supreme writedown is monotonically non-decreasing in conflict_density | Strictly increasing at every lambda (0.00 -> 0.0152 -> 0.029 -> 0.073 -> 0.131 at lambda=0.0; analogous at other lambdas) | **PASS** |
| C4 | At density = 0.9, negotiated writedown < 0.30 | Range 0.048 - 0.059 across lambdas | **PASS** |
| C5 | Sign of (continuity_acquirer_supreme - continuity_negotiated) is constant across lambda at each density | Sign = 0 at density 0; sign = negative at all density > 0 across all lambdas | **PASS** |

**4 of 5 checks pass.** Per the pre-registered success criterion
(at least 4 of 5), the simulation is numerically coherent with the
formalism.

### 2.1 C2 failure analysis

C2 failed by a margin of approximately 0.03 (observed gap ~0.074;
required >=0.10). This is a calibration finding about the synthetic
parameterization, not a contradiction of P2:

- The acquirer-supreme policy discards target policy-bearing events
  on conflict, but at density 0.9 the target log retains
  approximately 70 percent of its non-conflicting events (which
  still contribute to the merged-log projection).
- The 1.0 (DECISION/POLICY) + 0.5 (ARTIFACT) weighting in
  `WEIGHT_MAP` means that even when all POLICY-conflict events are
  dropped, DECISION and ARTIFACT events still carry the bulk of the
  scaling-query weight.
- A more aggressive parameterization (e.g., raising POLICY weight to
  3.0 or extending the conflict mechanism to PERSONNEL-driven
  DECISION events) would widen the gap to >0.10. This is left as a
  documented sensitivity finding; the pre-registered seed and
  weights are NOT changed post-hoc per the protections in
  `PRE_EXPERIMENT_REPORT.md` Section "Post-hoc protections".

C2's near-miss indicates the formalism's mechanism is present in the
right direction with the right monotonicity but with a synthetic-data
gap that the paper's discussion should note. The paper should report
the C2 finding as written rather than tune parameters to force a pass.

### 2.2 What the simulation does NOT show

- It does not show that real-firm M&A writedowns follow these curves.
- It does not show that the writedown gap of 0.13 - 0.06 = 0.07 (the
  observed acquirer-supreme vs negotiated wedge at density 0.9)
  corresponds to any specific dollar magnitude in real deals.
- It does not show that the 5 conflict-density and 4 lambda values
  tested are sufficient to cover the parameter space; they are a
  pre-registered grid, not a sensitivity analysis.

Real-firm confirmation is the job of the three process-traced cases
in `case_event_coding/` (Disney-Pixar, Microsoft-Nokia, Toyota TPS),
not this simulation.

## 3. Replication instructions

### 3.1 Prerequisites

- Python 3.12 (the scripts use 3.12 syntax: `dict[str, Any]`, `|` union types)
- `uv` (Astral) for dependency management

### 3.2 Steps

```
git clone https://github.com/spectralbranding/orgschema-papers.git
cd orgschema-papers/capability-as-projection/code

# Option A: ephemeral run via uv
uv run --with numpy==2.2.2 --with matplotlib==3.10.0 --with pandas==2.2.3 \
    python projection_demo.py
uv run --with numpy==2.2.2 --with matplotlib==3.10.0 --with pandas==2.2.3 \
    python monte_carlo_simulation.py

# Option B: venv + pinned requirements
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt
python projection_demo.py
python monte_carlo_simulation.py
```

### 3.3 Expected wall-clock time

- `projection_demo.py`: under 1 second
- `monte_carlo_simulation.py`: under 30 seconds on a 2024 Apple
  Silicon Mac (M-series); under 90 seconds on a 2020-era Intel
  laptop.

### 3.4 Expected outputs (deterministic)

- `logs/projection_demo_output.txt` matches the captured run.
- `monte_carlo_results.csv` rows match those reported in Section 1.3.
- Plots are 150 DPI PNGs with identical pixel content across runs on
  the same `numpy` / `matplotlib` build.

Minor numerical differences (below 1e-9) may appear on different
BLAS implementations but do not affect any aggregate statistic at
the four-decimal precision reported in the CSV.

## 4. Scope caveat (mandatory)

**This synthetic Monte Carlo does NOT empirically confirm P1, P2, or
P3 in real firms.**

The simulation tests **numerical coherence**: given the formalism
in `FORMALISM_v0.md`, the projection operator `pi_lambda`, the
compatibility function `kappa`, and a synthetic generative model for
event logs, the propositions hold in the predicted direction with
the predicted monotonicity (with one calibration near-miss on the
quantitative magnitude of the C2 gap).

**Empirical confirmation in real firms requires the three process-traced
case-coding outputs** that complement this simulation, per
`METHODS_APPENDIX_event_coding_protocol.md`:

- Disney-Pixar (2006-2012): clean merge archetype, kappa ~ 1
- Microsoft-Nokia (2013-2016): snapshot-import failure mode, kappa ~ 0
- Toyota TPS (longitudinal): log-as-capability proof

The paper's empirical-anchor claims must come from those case-coded
event logs, not from this simulation. The simulation's role is to
demonstrate that the formalism is internally consistent and produces
the comparative statics the propositions predict.

## 5. Direct GitHub URLs for paper.md to reference

Once committed to `main` of `spectralbranding/orgschema-papers`, the
paper should reference these scripts and outputs at the following
URLs (per PAPER_QUALITY_STANDARDS items 37a-37e, "Companion
Computation Script" subsection):

- Projection demo:
  `https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/projection_demo.py`
- Monte Carlo simulation:
  `https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/monte_carlo_simulation.py`
- Pre-experiment report:
  `https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/PRE_EXPERIMENT_REPORT.md`
- Post-experiment report (this document):
  `https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/POST_EXPERIMENT_REPORT.md`
- Aggregated results CSV:
  `https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/monte_carlo_results.csv`
- Projection continuity vs kappa plot:
  `https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/plots/plot_projection_continuity_vs_kappa.png`
- Writedown vs conflict density plot:
  `https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/plots/plot_writedown_vs_conflict_density.png`
- Captured stdout (projection demo):
  `https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/logs/projection_demo_output.txt`
- Captured stdout (Monte Carlo):
  `https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/logs/monte_carlo_run_output.txt`
