---
title: "PRE_EXPERIMENT_NOTES -- Anti-HARKing Artifact"
paper: "Toward a Thermodynamic Theory of Organizational Coupling (Zharnikov 2026am)"
status: "Created before any simulation execution. Modifications after first run require a dated changelog entry."
date: 2026-05-25
---

# Pre-Experiment Notes

This document is an anti-HARKing artifact. It records, verbatim from
`METHODS_APPENDIX.md`, the hypotheses, pre-registered effect sizes, decision
rules, alternative-explanations register, and identification threats BEFORE
any simulation code is executed. Modifying this document after execution to
make results appear pre-registered is prohibited.

Source document: `[internal path removed]` v0.1.0
(2026-05-25). This file excerpts Sections A.4, A.5, B.3, B.4, and B.6 verbatim.

---

## Section A.4 -- Pre-Registered Expected Results (Monte Carlo)

All values below are stated before the simulation runs. They constitute the
pre-registered success criteria for `friction_tax_montecarlo.py`.

**Primary effect -- push vs pull friction asymmetry at baseline parameters
(sigma = .3, N = 1,000, alpha = 0, quadratic norm)**:

- mu_push approximately 2 * sigma^2 * d = 2 * .09 * 8 = 1.44 (analytic expectation
  from the quadratic distance between two independent N(0, sigma^2 I) vectors
  in d dimensions).
- mu_pull approximately (.01)^2 * sigma^2 * d = .0000072 (negligible under the
  codified-specification assumption).
- Expected Cohen's d >= 1.0 (large effect). The push distribution is far wider
  than the pull distribution.
- Expected mu_push / mu_pull >= 200. This ratio encodes the paper's core claim
  that the push friction tax is not marginal.

**Effect of misalignment variance sigma**:

- F_push / F_pull should increase monotonically in sigma because push friction
  scales as sigma^2 while pull friction scales as (sigma_query)^2 = (.01*sigma)^2
  = .0001*sigma^2, yielding a ratio of approximately 10,000 in the limit. At low
  sigma the absolute magnitude of both is small; the ratio is still large.

**Effect of population size N**:

- The population size N should not substantially affect the push-vs-pull ratio at
  fixed sigma (N is a sample-size parameter for the mean; the ratio is a
  distributional property). This controls for the alternative explanation that
  "smaller N drives the effect."

**Phase-shift threshold alpha***:

- At sigma = .3, N = 1,000: the expected threshold alpha* at which F(alpha) falls
  below .10 * F(0) is in the range [.85, .95] at sigma = .3. Derivation: F(alpha) =
  (1 - alpha) * 1.44 + alpha * .0000072; setting F(alpha) = .144 gives
  1 - alpha* = .144 / 1.44 = .10, so alpha* = .90. The reported threshold will
  differ because the simulation uses non-zero pull friction.

**Falsification condition for H_A**:

H_A is falsified if mu_push / mu_pull < 2.0 at any tested sigma value under
baseline parameters (N = 1,000, alpha = 0, quadratic norm). A ratio below 2
would indicate that the friction-tax mechanism fails to produce a meaningful
push-pull asymmetry and that the formalism does not support the paper's core claim.

**Robustness**:

The push-vs-pull asymmetry must hold under all three functional forms (quadratic,
L1, log-quadratic). The specific Cohen's d values will differ across forms, but
the qualitative ordering -- mu_push >> mu_pull -- must be consistent.

---

## Section A.5 -- Alternative Explanations Register (Anti-HARKing)

The following alternative explanations could, in principle, produce a push >
pull friction asymmetry without the friction-tax mechanism the paper proposes.
Each is stated before the simulation runs, and each has a design control.

**Alternative 1 -- Dimensionality drives the effect, not the push-pull regime**

The argument: in high-dimensional specification space, any guessing error is
amplified. The push-vs-pull difference is an artifact of d = 8, not a structural
property of push regimes.

Control: The simulation fixes d = 8 throughout. The robustness check varies d in
{2, 4, 8, 16} to confirm that the push-vs-pull ratio is stable across
dimensionalities. If the ratio collapses at d = 2, the effect is
dimensionality-driven; if it persists, the mechanism holds across dimensions.

**Alternative 2 -- The pull-friction floor is artificially low**

The argument: the codified-specification assumption (sigma_query = .01 * sigma)
sets pull friction near zero by construction. The asymmetry is an assumption,
not a finding.

Control: The simulation runs pull-friction at three sigma_query multipliers: .01
(baseline), .10, and .30. The paper's claim is that pull friction is substantially
lower than push friction; it does not require zero pull friction. The falsification
condition (push/pull ratio < 2) remains binding even at sigma_query = .30 * sigma.

**Alternative 3 -- The specific friction functional form is rigged toward large
push values**

The argument: the quadratic norm amplifies large deviations. Using a different
distance measure would produce a smaller asymmetry.

Control: The simulation tests three functional forms (quadratic, L1, log-quadratic).
Consistency of qualitative ordering across all three is required for the result to
count as robust.

**Alternative 4 -- The AI-mediation interpolation model is linear and unrealistically
smooth**

The argument: the linear interpolation F(alpha) = (1 - alpha) * F_push + alpha *
F_pull imposes a smooth phase shift by construction. A non-linear model might
produce a different phase-shift threshold or no threshold at all.

Control: The alpha sweep is descriptive, not a test of the phase-shift threshold's
location. The paper's qualitative prediction is that increasing alpha reduces F;
the simulation confirms this direction. The linear interpolation is the simplest
model that captures partial AI adoption; the paper does not claim that the
transition is literally linear in real organizations.

**Alternative 5 -- The effect vanishes at firm-relevant scales (large N)**

The argument: large firms have large recipient populations, and the law of large
numbers smooths out individual misalignment events. The aggregate friction tax per
recipient is small at N = 5,000.

Control: The simulation sweeps N in {100, 500, 1,000, 5,000}. The per-recipient
friction F / N is scale-invariant by construction; the total friction F is what
scales with N. The paper's economic claim concerns per-recipient friction cost and
its aggregate across the total interface-maintenance budget. Both are reported.

---

## Section B.3 -- Pre-Registered Simulation Design (Regression)

Fixed seed: np.random.seed(20260525) at module top.

Panel structure: N_firms = 1,000 firms x T = 10 years = 10,000 firm-year
observations for P1, P2, P4, P5. For P3 (event study): N_events = 200
spend-cessation events x window of 5 years each = 1,000 event-year observations.

Number of Monte Carlo draws: 1,000 simulated datasets per condition per proposition
(H0 and H1 separately). Power = fraction of H1 draws where |t-stat| > 1.96
(two-sided alpha = .05). Type I error = fraction of H0 draws where |t-stat| > 1.96.

---

## Section B.4 -- Pre-Registered Effect Sizes Under H1

All effect sizes are stated before the simulation runs. They represent the minimum
plausible effect consistent with the paper's theoretical claims.

| Proposition | Effect metric | Assumed effect size | Cohen's d | Direction |
|---|---|---|---|---|
| P1 | beta (SCI -> functional spend / revenue) | -.08 | .5 | Negative |
| P2 | beta (delta log functional headcount -> brand-capital net growth) | -.12 | .3 | Negative |
| P3 | CAR in [0, +1 year] for high-push vs low-push firms | -.15 | .7 | Negative for high-push |
| P4 | beta (contradiction index -> cross-stakeholder dispersion) | +.10 | .4 | Positive |
| P5 | beta (SCI at t -> AI-ROI at t+2) | +.15 | .5 | Positive |

Note: Cohen's d is computed as the standardized regression coefficient at the assumed
beta values relative to the DGP residual variance. Effect sizes are set
conservatively; the paper's theoretical argument would predict larger effects.

---

## Section B.5 -- Threats to Identification

### P1 -- Interface coherence and function spend

Threat 1 -- Omitted firm-quality bias: High-specification-coherence firms may be
high-quality on dimensions not captured by fixed effects.
Mitigation: Firm fixed effects + difference-in-differences around codification events.

Threat 2 -- Reverse causality: Low functional spend makes codification-investment
affordable.
Mitigation: Lead-lag structure; ISO certification as partial instrument.

Threat 3 -- SCI measurement error: Binary-component SCI is noisy; informal
effective codification misclassified as low-SCI.
Mitigation: Sensitivity analysis with alternative SCI operationalizations.

### P2 -- Function headcount and brand-capital accumulation

Threat 1 -- LinkedIn headcount data quality: Inconsistent job-title taxonomies.
Mitigation: Capital IQ functional-expense data as robustness check.

Threat 2 -- Brand-capital stock measurement: Belo-Lin-Vitorino (2014) model with
delta_6 = .50/year is stylized; understates investment for luxury/professional
services brands.
Mitigation: Restrict primary sample to consumer-goods firms (Fama-French sector 2).

Threat 3 -- Simultaneity: Firms achieving brand-capital growth may require less
functional headcount (reverse causality).
Mitigation: Regulatory-compliance IV; lead-lag structure.

### P3 -- Push-dependence and spend-cessation revaluation

Threat 1 -- Event-selection bias: Cessation events correlate with management
quality problems, competitive deterioration, or financial distress.
Mitigation: Exclude distress-year events (Altman Z-score < 1.81); exclude events
coinciding with CEO departure or bankruptcy filing.

Threat 2 -- Confounding by macroeconomic conditions: Recession-year cessation
produces negative CARs regardless of push-dependence.
Mitigation: Year fixed effects; separate recession vs non-recession analysis per
NBER business cycle chronology.

Threat 3 -- Category-level push norms: High XAD/SALE is an industry norm in some
categories; cessation effects differ by category.
Mitigation: Fama-French 48-industry x year cells as within-group comparison unit.

### P4 -- Inter-interface contradiction and stakeholder dispersion

Threat 1 -- NLP embedding quality: Cosine-similarity contradiction score may
capture style differences (formal vs conversational register) rather than
substantive logical contradictions.
Mitigation: Validate against human-coded subsample with known contradictory cases
(e.g., firms with SEC enforcement actions alleging misleading disclosures).

Threat 2 -- Reverse causality: High-dispersion firms attract contradictory
stakeholder constituencies, which itself generates interface contradictions.
Mitigation: Lagged independent variable (contradiction index at t-1 predicts
dispersion at t); cross-lagged panel model.

Threat 3 -- Missing stakeholder-perception data: Consumer NPS from YouGov
BrandIndex available only for large-cap consumer-facing firms.
Mitigation: Restrict primary sample to firms covered by at least two of three
perception-data sources.

### P5 -- Specification-readiness and AI-ROI realization

Threat 1 -- AI-ROI measurement is not standardized: No single accounting variable
captures AI return at the firm level; headcount-change proxy assumes Substrate-AI
realizations appear as headcount efficiency gains.
Mitigation: Two alternative dependent variables (revenue-per-AI-dollar and
headcount-change-per-AI-dollar) reported side by side.

Threat 2 -- CEO-transition IV exclusion restriction: CEO transitions may affect
AI-ROI directly through CEO tenure effects.
Mitigation: Control for CEO tenure directly; robustness analysis excluding firms
where new CEO had prior AI-intensive firm experience.

Threat 3 -- AI-adoption timing is endogenous: Firms with strong specifications
may adopt AI earlier because they have the substrate already in place.
Mitigation: Use SCI at t-3 (three years before AI adoption) as the
specification-readiness measure.

---

## Section B.6 -- Pre-Registered Decision Rules

The following decision rules are fixed before the simulation runs. Any deviation
in the post-experiment report must be flagged explicitly and justified.

**Statistical power threshold**: If power < .80 under H1 at the assumed effect
size for any proposition, that proposition's proxy operationalization is declared
underpowered in the simulation. The post-experiment report must propose an
alternative operationalization or a larger N before the empirical study proceeds.

**Type I error threshold**: If Type I error rate > .05 under H0 for any
specification, the regression specification is declared mis-specified. The source
of inflation must be identified and corrected before the empirical study proceeds.

**Effect-size plausibility check**: If the H1 simulation produces point estimates
outside the interval [.5 * expected_effect, 2.0 * expected_effect], the proxy
operationalization is flagged as potentially mis-specified. The interval is
deliberately wide; estimates outside this range indicate a non-trivial discrepancy
between the DGP and the theoretical model.

**Robustness reporting obligation**: For each proposition, the simulation must be
run with at least two alternative specifications (different fixed-effects structure,
alternative control set, alternative DV operationalization). If the primary
specification shows adequate power but an alternative shows power < .60, this must
be reported as a specification-sensitivity finding.

**Null-result reporting**: If any proposition fails the power threshold or shows a
directionally inconsistent result under H1, this is reported transparently. No
proposition is dropped from the paper based on simulation results; null or
inconclusive simulation results are reported alongside the theory.

---

*This document was committed to version control before any simulation execution.
Version: v0.1.0. Date: 2026-05-25. Source: METHODS_APPENDIX.md v0.1.0.*
