---
title: "Methods Appendix — Pre-Registration Record for Monte Carlo and Regression-Simulation Companions"
paper: "Toward a Thermodynamic Theory of Organizational Coupling: Push, Pull, and the Multi-Interface Architecture of the Firm Under AI Mediation"
working_paper_key: 2026am
version: v0.1.0
date: 2026-05-25
status: Pre-registered before simulations run. Anti-HARKing discipline enforced. Modifications after first execution require an explicit changelog entry with date and reason.
---

# Methods Appendix

## Purpose

This document is the pre-registration record for the two companion computational experiments that accompany Zharnikov (2026am). It is written before any simulation code is executed. Its function is to fix, in advance and with precision, the hypotheses, formal models, parameter ranges, expected effect sizes, identification strategy, alternative-explanation register, and decision rules that will be evaluated once the code runs. Modifying this document after execution to make results appear pre-registered is prohibited; any post-execution modification requires a dated changelog entry stating the reason.

The appendix covers two independent experiments:

- **Section A** — Monte Carlo simulation of friction-tax dynamics under push and pull regimes.
- **Section B** — Regression identification simulation for propositions P1–P5.

Both experiments are numerical-coherence checks for the formalism developed in the paper. They demonstrate that the formal model is internally consistent across the specified parameter space; they do not constitute empirical confirmation in real firms. Real-firm confirmation requires the archival panel study described in the paper's empirical strategy section.

Reproducibility follows the corpus computational-reproducibility standard: fixed seeds, documented run commands, public-mirror publication before Zenodo v1 upload.

---

## A. Monte Carlo Simulation: Friction-Tax Dynamics Under Push and Pull

### A.1 Hypothesis

The central prediction of the paper's push-pull energy formalization is that push regimes incur structural energy dissipation proportional to the misalignment between the sender's guessed recipient-need profile and the recipient's actual need profile, while pull regimes incur near-zero energy dissipation because the recipient draws from a codified substrate rather than receiving guessed output.

Stated formally:

**H_A**: The mean friction-tax cost under a push regime (μ_push) will exceed the mean friction-tax cost under a pull regime (μ_pull) by a factor of at least 10 across all tested values of misalignment variance σ ∈ {.1, .2, .3, .5, .7, 1.0}. The ratio μ_push / μ_pull will increase monotonically in σ under constant recipient-population size N and constant AI-mediation factor α = 0. Under full AI mediation (α = 1), the pull-regime friction cost will approach zero regardless of σ.

The Shannon (1948) information-entropy structural analog licenses the formalization. In the push regime, the sender's guessed distribution over recipient needs has cross-entropy H(p_actual, p_guessed) relative to the actual distribution; friction cost is proportional to this cross-entropy times volume times time. In the pull regime, H(p_actual, p_pulled) → 0 as the recipient self-queries, because the query is the need itself — there is no guessing step.

**Pre-registered effect-size expectation**: Cohen's d comparing push-regime and pull-regime friction distributions ≥ 1.0 at σ = .3 under N = 1,000, α = 0. This expectation derives from the theoretical position that the structural energy loss in push systems is large, not marginal.

**Falsification condition for H_A**: H_A is falsified if μ_push / μ_pull < 2.0 at any tested σ value. A ratio below 2 would indicate that the friction-tax mechanism fails to produce a meaningful push-pull asymmetry and that the formalism does not support the paper's core claim.

### A.2 Formal Model

**Variables and definitions**:

- **Specification vector s** ∈ ℝ^d: the firm's organizational specification, where d = 8 (corresponding to the eight-dimensional SBT specification structure: Semiotic, Narrative, Ideological, Experiential, Social, Economic, Cultural, Temporal).
- **Recipient need vector n_i** for recipient i, drawn from a distribution centered on s with misalignment noise: n_i = s + ε_i, where ε_i ~ N(0, σ²I).
- **Guessed need vector g_i** (push regime only): the sender's forecast of n_i, drawn from a distribution centered on s with guessing noise: g_i = s + η_i, where η_i ~ N(0, σ²I), independent of ε_i.
- **Push friction for recipient i**: f_push(i) = ‖n_i – g_i‖² = ‖ε_i – η_i‖², i.e., the squared distance between the actual need and the guessed output. The Euclidean norm is used throughout.
- **Pull friction for recipient i**: f_pull(i) = ‖n_i – n_i‖² = 0 under the codified-specification assumption, because the recipient queries and retrieves their exact need from the substrate. In practice, f_pull(i) = ‖ε_query‖² where ε_query ~ N(0, σ²_query I) with σ_query << σ. The baseline simulation sets σ_query = .01 × σ.
- **AI-mediation factor α** ∈ [0, 1]: interpolates between push (α = 0) and pull (α = 1) behavior. At α ∈ (0, 1), friction is f(i, α) = (1 – α) × f_push(i) + α × f_pull(i). This parameterization models partial AI adoption at the consumption layer.
- **Aggregate friction-tax cost for a population of N recipients**: F(α) = (1/N) Σ_i f(i, α).
- **Units**: friction cost is reported in squared specification-distance units (unitless). No calibration to dollar values is required for the numerical-coherence check.

**Functional form for friction**: The baseline simulation uses the squared Euclidean distance (quadratic misalignment cost), consistent with the Grok-recommended quadratic misalignment-cost model (PREDRAFT_REVIEW_SUMMARY.md, High-priority 2). Two alternative functional forms are tested as robustness checks:

- *Linear norm*: f_push_alt1(i) = ‖n_i – g_i‖₁ (L1 distance).
- *Log penalty*: f_push_alt2(i) = –log(1 / (1 + ‖n_i – g_i‖²)) (log-quadratic).

The qualitative ordering — push friction substantially exceeds pull friction — must hold across all three functional forms for the result to be robust.

**Cross-entropy interpretation**: The friction-tax cost under the push regime is structurally equivalent to the cross-entropy H(p_actual, p_guessed) in Shannon's (1948) information-entropy framework. When the guessing distribution matches the actual distribution perfectly (σ_guess = σ_actual), cross-entropy equals entropy and the inefficiency is minimal. When the two distributions diverge, cross-entropy exceeds entropy, and the excess is the friction. This equivalence is stated in the paper's Section 5 licensing paragraph and confirmed numerically by the simulation.

### A.3 Simulation Design

**Fixed seed**: `np.random.seed(20260525)` at module top. This seed is fixed before execution and may not be changed to obtain more favorable results.

**Trial count**: 10,000 trials per parameter cell. At 10,000 trials, the standard error on the friction-cost mean is small enough (< 2% of the mean at σ = .3) to report Cohen's d to two decimal places reliably.

**Parameter grid** (full factorial, all combinations run):

| Parameter | Values tested |
|---|---|
| Misalignment variance σ | .1, .2, .3, .5, .7, 1.0 |
| Recipient population N | 100, 500, 1,000, 5,000 |
| AI-mediation factor α | 0, .2, .4, .6, .8, 1.0 |
| Specification dimensionality d | 8 (fixed) |
| Friction functional form | Quadratic (primary); L1, log-quadratic (robustness) |

Total cells: 6 × 4 × 6 × 3 = 432 parameter cells × 10,000 trials = 4,320,000 individual friction measurements.

**Per-trial procedure**:

1. Draw specification vector s ~ Uniform([0, 10]^d) once per trial.
2. Draw N recipient-need vectors n_i = s + ε_i.
3. Draw N guessed-need vectors g_i = s + η_i (push regime).
4. Draw N queried-need vectors q_i = n_i + δ_i where δ_i ~ N(0, (.01σ)²I) (pull regime).
5. Compute f_push(i), f_pull(i) for each recipient.
6. Compute aggregate F_push, F_pull for the trial.
7. Interpolate at each α value: F(α) = (1 – α) × F_push + α × F_pull.
8. Record all values.

**Aggregation**: Across 10,000 trials per cell, compute mean, standard deviation, 2.5th and 97.5th percentile, and Cohen's d = (μ_push – μ_pull) / σ_pooled.

**Phase-shift curve**: For each σ value at N = 1,000, plot F(α) against α across α ∈ [0, 1] to identify the phase-shift threshold α* at which F(α) falls below .10 × F(0). The paper's qualitative argument predicts α* in the range [.5, .7] for σ ∈ [.2, .5].

### A.4 Expected Results (Pre-Registered)

All values below are stated before the simulation runs. They constitute the pre-registered success criteria.

**Primary effect — push vs pull friction asymmetry at baseline parameters (σ = .3, N = 1,000, α = 0, quadratic norm)**:

- μ_push ≈ 2 × σ² × d = 2 × .09 × 8 = 1.44 (analytic expectation from the quadratic distance between two independent N(0, σ²I) vectors in d dimensions).
- μ_pull ≈ (.01)² × σ² × d ≈ .0000072 (negligible under the codified-specification assumption).
- Expected Cohen's d ≥ 1.0 (large effect). The push distribution is far wider than the pull distribution.
- Expected μ_push / μ_pull ≥ 200. This ratio encodes the paper's core claim that the push friction tax is not marginal.

**Effect of misalignment variance σ**:

- F_push / F_pull should increase monotonically in σ because push friction scales as σ² while pull friction scales as (σ_query)² = (.01σ)² = .0001σ², yielding a ratio of approximately .0001^–1 = 10,000 in the limit. At low σ the absolute magnitude of both is small; the ratio is still large.

**Effect of population size N**:

- The population-size N should not substantially affect the push-vs-pull ratio at fixed σ (N is a sample-size parameter for the mean; the ratio is a distributional property). This controls for the alternative explanation that "smaller N drives the effect."

**Phase-shift threshold α***:

- At σ = .3, N = 1,000: the expected threshold α* at which F(α) < .10 × F(0) is approximately .55. This value is derived analytically from the linear interpolation model: F(α) = (1 – α) × 1.44 + α × .0000072. Setting F(α) = .144 gives 1 – α* = .144 / 1.44 = .10, so α* = .90. The reported threshold will differ from this because the simulation uses non-zero pull friction; the pre-registered range is α* ∈ [.85, .95] at σ = .3.

**Robustness to functional form**:

- The push-vs-pull asymmetry must hold under all three functional forms (quadratic, L1, log-quadratic). The specific Cohen's d values will differ across forms, but the qualitative ordering — μ_push >> μ_pull — must be consistent.

### A.5 Alternative Explanations Register (Anti-HARKing)

The following alternative explanations could, in principle, produce a push > pull friction asymmetry without the friction-tax mechanism the paper proposes. Each is stated before the simulation runs, and each has a design control.

**Alternative 1 — Dimensionality drives the effect, not the push-pull regime**

The argument: in high-dimensional specification space, any guessing error is amplified. The push-vs-pull difference is an artifact of d = 8, not a structural property of push regimes.

*Control*: The simulation fixes d = 8 throughout (matching the SBT specification structure). The robustness check varies d ∈ {2, 4, 8, 16} to confirm that the push-vs-pull ratio is stable across dimensionalities. If the ratio collapses at d = 2, the effect is dimensionality-driven; if it persists, the mechanism holds across dimensions.

**Alternative 2 — The pull-friction floor is artificially low**

The argument: the codified-specification assumption (σ_query = .01 × σ) sets pull friction near zero by construction. The asymmetry is an assumption, not a finding.

*Control*: The simulation runs pull-friction at three σ_query multipliers: .01 (baseline), .10, and .30. The paper's claim is that pull friction is substantially lower than push friction; it does not require zero pull friction. The falsification condition (push/pull ratio < 2) remains binding even at σ_query = .30 × σ.

**Alternative 3 — The specific friction functional form is rigged toward large push values**

The argument: the quadratic norm amplifies large deviations. Using a different distance measure would produce a smaller asymmetry.

*Control*: The simulation tests three functional forms (quadratic, L1, log-quadratic). Consistency of qualitative ordering across all three is required for the result to count as robust.

**Alternative 4 — The AI-mediation interpolation model is linear and unrealistically smooth**

The argument: the linear interpolation F(α) = (1 – α) × F_push + α × F_pull imposes a smooth phase shift by construction. A non-linear model might produce a different phase-shift threshold or no threshold at all.

*Control*: The α ∈ [0, 1] sweep is descriptive, not a test of the phase-shift threshold's location. The paper's qualitative prediction is that increasing α reduces F; the simulation confirms this direction. The linear interpolation is the simplest model that captures partial AI adoption; the paper does not claim that the transition is literally linear in real organizations.

**Alternative 5 — The effect vanishes at firm-relevant scales (large N)**

The argument: large firms have large recipient populations, and the law of large numbers smooths out individual misalignment events. The aggregate friction tax per recipient is small at N = 5,000.

*Control*: The simulation sweeps N ∈ {100, 500, 1,000, 5,000}. The per-recipient friction F / N is scale-invariant by construction; the total friction F is what scales with N. The paper's economic claim concerns per-recipient friction cost and its aggregate across the total interface-maintenance budget. Both are reported.

### A.6 Output Artifacts

**Plots** (saved to `code/plots/`):

- `friction_distribution_push_vs_pull.png` — overlapping density plots of push-regime and pull-regime per-trial friction at baseline parameters (σ = .3, N = 1,000, α = 0). Annotated with μ_push, μ_pull, and Cohen's d.
- `phase_shift_alpha.png` — F(α) vs α for σ ∈ {.1, .3, .7, 1.0} at N = 1,000. One curve per σ value; y-axis normalized to F(0) = 1 for comparability.
- `sensitivity_misalignment.png` — μ_push / μ_pull ratio vs σ for N ∈ {100, 1,000, 5,000}. Log-scale y-axis.
- `functional_form_comparison.png` — Cohen's d vs σ for all three functional forms at N = 1,000, α = 0. Robustness check visualization.

**Summary CSV** (`code/monte_carlo_summary.csv`): one row per parameter cell, columns: σ, N, α, functional_form, μ_push_mean, μ_push_sd, μ_pull_mean, μ_pull_sd, cohens_d, ratio_push_pull, n_trials.

**Log file** (`code/logs/monte_carlo_run_<YYYYMMDD>.log`): verbatim stdout/stderr from execution, including elapsed time, random seed confirmation, and row counts.

---

## B. Regression Simulation: P1–P5 Propositional Identification

### B.1 Hypotheses: Propositions P1–P5 (Verbatim from Phase-0 Thesis Section 7)

**P1 (Interface coherence and function-layer spending).** Firms with codified, coherent specifications have lower aggregate spending on interface-maintaining functions — marketing, investor relations, human resources, legal, procurement, and communications combined as a percentage of revenue — than firms with implicit or contradictory specifications, controlling for industry, firm size, and competitive intensity.

**P2 (Function-as-friction-tax and substrate accumulation).** Conditional on revenue cohort, increases in Tier-6 functional headcount or budget share correlate negatively with brand-capital growth net of depreciation, measured using the Belo, Lin, and Vitorino (2014) perpetual-inventory model applied to Compustat XAD.

**P3 (Push-dependence collapse under spend cessation).** Firms whose consumer-interface demand is push-dependent — high advertising-to-revenue ratio — exhibit faster public-market revaluation declines following spend-cessation events than firms whose demand is pull-dependent, controlling for category, firm size, and macroeconomic conditions.

**P4 (Interface inconsistency and stakeholder valuation dispersion).** Firms with documented inter-interface contradictions — cases where the consumer-facing specification and the regulatory-facing specification make incompatible claims — exhibit higher dispersion in cross-stakeholder valuation metrics than coherent-specification firms.

**P5 (Specification-readiness and AI-ROI realization).** Firms that codify function-specific specifications — versioned, machine-readable artifacts — before AI deployment exhibit higher AI-ROI realization than firms that deploy AI without prior specification codification, controlling for AI spend, industry, and firm size.

Each proposition is a directional prediction with a sign. The regression simulation tests whether the specified proxy-variable operationalization has adequate statistical power to detect the hypothesized effect at the assumed effect size, and whether the specification produces acceptable Type I error under the null.

### B.2 Proxy-Variable Operationalization

**P1 — Interface coherence and aggregate function spend**

*Independent variable — Specification Codification Index (SCI)*:

A continuous composite constructed from four binary components: (a) employee handbook publicly published (binary, 1 if the firm has a publicly accessible handbook per systematic web search, e.g., GitLab, Valve, Netflix); (b) ISO 9001 or equivalent quality-management certification as of the year-end (binary, from ISO certification database); (c) design-system public release (binary, 1 if the firm published a publicly accessible design system per GitHub or firm website); (d) investor-day specification overhaul event (binary, 1 if an investor-day event included a structured strategy overhaul presentation in that year, per Factiva or Capital IQ events). SCI = (a + b + c + d) / 4, range [0, 1]. Firms with SCI ≥ .75 are classified as high-codification.

*Dependent variable*: (Marketing expense + IR function estimate + HR function expense + Legal expense + Procurement overhead + Comms expense) / Revenue. For firms that do not report functional expense decomposition below SG&A, the SG&A-to-revenue ratio is used as a proxy with a control for SG&A composition.

*Controls*: industry × year fixed effects (Fama-French 48-industry classification), log(total assets), log(firm age in years), Herfindahl-Hirschman Index for competitive intensity.

*Identification*: Two-way fixed effects panel regression (firm and year). Difference-in-differences around specification-codification events (the year of handbook publication or ISO certification event, relative to a matched control group of firms in the same Fama-French industry-year cell that did not experience a codification event in the same window).

**P2 — Function headcount and brand-capital accumulation**

*Independent variable*: Δ log(functional headcount) as a fraction of total headcount. Functional headcount measured from LinkedIn Economic Graph data for marketing, HR, legal, and comms job titles. Alternatively, Δ log(SG&A) decomposed using BvD Orbis or Capital IQ segment-level expense data where available.

*Dependent variable*: Brand-capital stock growth, net of depreciation. Computed via the Belo, Lin, and Vitorino (2014) perpetual-inventory method: Brand_Capital_{t} = (1 – δ₆) × Brand_Capital_{t–1} + XAD_t, where δ₆ = .50/year is the calibrated brand-capital depreciation rate from Belo, Lin, and Vitorino (2014), and XAD is Compustat advertising expenditure. Net growth = Brand_Capital_t – Brand_Capital_{t–1}. Normalized by lagged total assets.

*Controls*: industry × year fixed effects, log(revenue), log(total assets).

*Identification*: Instrumental variable — exogenous increases in compliance-mandated legal or HR headcount triggered by regulatory changes (e.g., Sarbanes-Oxley compliance year for legal function; EEOC reporting mandate years for HR function). These events expand Tier-6 headcount for regulatory reasons independent of specification quality, providing exogenous variation in the independent variable.

**P3 — Push-dependence and revaluation under spend cessation**

*Independent variable*: Push intensity — XAD / SALE (advertising-to-revenue ratio, Compustat), computed as the three-year average prior to the cessation event, quintile-ranked within Fama-French industry × year cells.

*Dependent variable*: Cumulative abnormal returns (CAR) in the [–1, +3 year] window around spend-cessation events. CARs computed using the Fama-French three-factor model, estimated on the [–5, –2 year] pre-event window.

*Spend-cessation event identification*: A firm-year qualifies as a cessation event if XAD falls by > 30% from the prior year and total assets do not decline by > 10% (to exclude distress-driven cessations). Additional exclusion: cessation events that coincide with mergers, acquisitions, or material divestitures within the [–1, +1 year] window.

*Controls*: Fama-French three-factor loadings (beta, SMB, HML), log(market cap at event date), macroeconomic condition indicator (NBER recession dummy for the event year).

*Identification*: The event-study design uses near-exogenous spend reductions. The instrument for exogenous cessation is platform-policy changes that forced spend reductions (e.g., changes to digital advertising auction mechanics that raised CPM substantially in specific years) and CMO transitions (exogenous CEO-driven CMO replacement events per ExecuComp). Difference-in-differences contrast: high-push-intensity firms (top quintile of XAD/SALE) vs low-push-intensity firms (bottom quintile) in the same Fama-French × year cell, where the cessation event is the treated condition.

**P4 — Inter-interface contradiction and stakeholder valuation dispersion**

*Independent variable — cross-interface contradiction index*:

NLP-based composite. Three pairwise comparisons: (a) consumer-interface language (brand-tone from 10-K business-description section, Item 1) vs investor-interface language (MD&A forward-looking statements, Item 7); (b) employer-brand language (Glassdoor employer profile, scraped annually) vs investor-interface language (10-K Item 7); (c) regulatory-positioning language (SEC comment letters and response filings) vs consumer-interface language (10-K Item 1). Contradiction score for each pair computed as 1 – cosine_similarity(embedding_pair). Composite = mean of three pairwise contradiction scores. Embeddings from a sentence-transformer model applied to standardized 200-word excerpts from each interface.

*Dependent variable — cross-stakeholder valuation dispersion*:

Composite of three components, each normalized within Fama-French × year cells: (i) consumer NPS variance across brand-tracker survey cohorts (YouGov BrandIndex or equivalent); (ii) employee Glassdoor rating standard deviation within firm-year; (iii) analyst 12-month price-target dispersion (standard deviation of analyst consensus, from I/B/E/S). Cross-stakeholder dispersion = geometric mean of the three normalized components.

*Controls*: industry × year fixed effects, log(total assets), log(firm age), institutional ownership fraction (from 13F filings).

*Identification*: Two-way fixed effects panel regression. Lagged independent variable (contradiction index at t–1 predicts dispersion at t) to address reverse causality.

**P5 — Specification-readiness and AI-ROI realization**

*Independent variable*: SCI (same construction as P1), measured at year t, where t is the year of first AI deployment (defined as the year in which the firm's AI-adoption score crosses a firm-specific threshold per Alekseeva et al. (2026) AI-adoption measure or equivalent NLP-based adoption index from job postings and earnings call transcripts).

*Dependent variable — AI-ROI proxy*: Two alternative operationalizations: (a) ΔRevenue per $1 AI spend in the [t+1, t+2] window; (b) functional-headcount change in interface-maintaining roles in [t+1, t+2] relative to AI spend — the paper's theoretical position is that Substrate-AI converts function-layer headcount to monitoring roles, so high-ROI AI deployment should show flat or declining functional headcount alongside increasing AI spend.

*Controls*: log(AI spend), industry × year fixed effects, log(total assets), log(firm age).

*Identification*: Instrument for pre-deployment specification codification — CEO transition in [t–3, t–1] (an exogenous event that is associated with strategic-reset behavior, including handbook publication and process-codification initiatives, but that predates the AI deployment decision). This instrument is valid under the exclusion restriction that CEO transitions affect AI-ROI only through their effect on specification codification, not directly. The restriction is plausible but must be tested with standard over-identification or placebo tests.

### B.3 Simulation Design

The regression simulation generates synthetic panel data under H₀ (no effect) and H₁ (effect at the pre-registered magnitude) for each proposition, runs the specified regression, and reports Type I error rate (false-positive rate under H₀) and statistical power (true-positive rate under H₁).

**Fixed seed**: `np.random.seed(20260525)` at module top.

**Panel structure**: N_firms = 1,000 firms × T = 10 years = 10,000 firm-year observations for P1, P2, P4, P5. For P3 (event study), N_events = 200 spend-cessation events × window of 5 years each = 1,000 event-year observations.

**Data-generating process under H₁**:

- The independent variable X is drawn from a mixture distribution calibrated to match expected Compustat distributions (SCI uniform on [0, 1]; XAD/SALE log-normal with mean .05 and sd .04 for the consumer-goods sector; functional headcount fraction beta-distributed with mode at .15).
- The dependent variable Y is generated as: Y = β_true × X + γ × Controls + ε, where β_true is set at the pre-registered effect size (below), Controls are drawn from independent normal distributions, and ε ~ N(0, σ_ε²) with σ_ε² calibrated to produce the assumed R² (R² ≈ .15 for P1, .10 for P2, .20 for P3, .12 for P4, .18 for P5).
- Industry and year fixed effects are included as block-random effects in the DGP.

**Data-generating process under H₀**: As above but β_true = 0.

**Number of Monte Carlo draws**: 1,000 simulated datasets per condition per proposition (H₀ and H₁ separately). Power = fraction of H₁ draws where |t-stat| > 1.96 (two-sided α = .05). Type I error = fraction of H₀ draws where |t-stat| > 1.96.

### B.4 Pre-Registered Effect Sizes Under H₁

All effect sizes are stated before the simulation runs. They represent the minimum plausible effect consistent with the paper's theoretical claims.

| Proposition | Effect metric | Assumed effect size | Cohen's d | Directional prediction |
|---|---|---|---|---|
| P1 | β (SCI → functional spend / revenue) | –.08 (8 pp reduction per unit SCI) | d = 0.5 | Negative (higher SCI, lower functional spend share) |
| P2 | β (Δ log functional headcount → brand-capital net growth) | –.12 | d = 0.3 | Negative (more functional headcount, less brand-capital accumulation) |
| P3 | CAR in [0, +1 year] for high-push vs low-push firms | –15 pp for high-push firms | d = 0.7 | Negative for high-push; near-zero for low-push |
| P4 | β (contradiction index → cross-stakeholder dispersion) | +.10 | d = 0.4 | Positive (more inter-interface contradiction, more valuation dispersion) |
| P5 | β (SCI at t → AI-ROI at t+2) | +.15 | d = 0.5 | Positive (higher pre-deployment codification, higher AI-ROI) |

*Notes*: Cohen's d is computed as the standardized regression coefficient at the assumed β values relative to the DGP residual variance. Effect sizes are set conservatively; the paper's theoretical argument would predict larger effects. If the simulation shows adequate power at these conservative sizes, the real-world signal should be detectable even if effect sizes are smaller than the theoretical maximum.

### B.5 Threats to Identification

**P1 — Interface coherence and function spend**

*Threat 1 — Omitted firm-quality bias*: High-specification-coherence firms are likely high-quality firms on dimensions not captured by industry × year fixed effects (management quality, governance quality, financial slack). Any of these could simultaneously cause low functional-spend ratios and high SCI scores, confounding the proposed causal direction.
*Mitigation*: Include firm fixed effects in the main specification to absorb stable heterogeneity. Supplement with a difference-in-differences design exploiting within-firm variation in codification events.

*Threat 2 — Reverse causality*: Low functional spend makes codification-investment affordable; firms save functional-spend money and redirect it to specification-building. The correlation goes in the correct direction but the causal direction is inverted.
*Mitigation*: Lead–lag structure (SCI at t–2 predicts functional spend at t). Instrument: ISO certification is partially exogenous (industry adoption waves driven by supply-chain partners, not by the firm's marketing budget level).

*Threat 3 — SCI measurement error*: The binary-component SCI is noisy. Firms with informal but effective codification practices are misclassified as low-SCI.
*Mitigation*: Sensitivity analysis with alternative SCI operationalizations (handbook word count as continuous measure; number of ISO certifications held; structured brand-spec publication per web-scraping). Report attenuation bounds.

**P2 — Function headcount and brand-capital accumulation**

*Threat 1 — LinkedIn headcount data quality*: Functional headcount from LinkedIn is subject to inconsistent job-title taxonomies. Marketing operations and brand management titles are sometimes classified as HR functions; legal operations roles span legal and operations categories.
*Mitigation*: Use Capital IQ functional-expense segment data as a robustness check where available. Report main results with LinkedIn and robustness check with Capital IQ side by side.

*Threat 2 — Brand-capital stock measurement*: The Belo, Lin, and Vitorino (2014) perpetual-inventory model calibrated at δ₆ = .50/year is a stylized approximation. For firms with non-advertising-intensive brand strategies (Hermès, luxury, professional services), XAD may understate brand-capital investment.
*Mitigation*: Restrict the primary sample to consumer-goods firms (Fama-French sector 2, Nondurables + Durables) where XAD is the dominant brand-capital investment channel. Report sensitivity analysis for the full-sample specification.

*Threat 3 — Simultaneity*: Firms that achieve brand-capital growth may have less need for functional headcount expansion (reverse causality).
*Mitigation*: Regulatory-compliance IV (see B.2 above). Lead–lag structure.

**P3 — Push-dependence and spend-cessation revaluation**

*Threat 1 — Event-selection bias*: Spend-cessation events are not random. They are disproportionately associated with management-quality problems, competitive deterioration, or financial distress. The valuation effect following cessation may reflect distress, not push-dependence.
*Mitigation*: Exclude firm-years where Z-score (Altman) is in the distress range (< 1.81) in the event year or the prior year. Exclude events that coincide with CEO departures, material divestitures, or pending bankruptcy within the [–1, +2 year] window. Report the exclusion counts transparently.

*Threat 2 — Confounding by macroeconomic conditions*: Spend-cessation events during recessions will produce more negative CARs regardless of push-dependence, because macroeconomic deterioration simultaneously depresses consumer demand and firm valuations.
*Mitigation*: Year fixed effects in the CAR model. Separate analysis for recession-year versus non-recession-year cessation events per the NBER business cycle chronology.

*Threat 3 — Category-level push norms*: In some categories (FMCG, consumer staples), high XAD/SALE ratios are industry norms, and cessation is unusual; in others (B2B, luxury), they are rare. The industry × year fixed effects and within-quintile comparison are designed to control for this, but residual category-level confounders may remain.
*Mitigation*: Fama-French 48-industry × year cells as the within-group comparison unit. Sensitivity analysis excluding industries where XAD/SALE variance is below the 10th percentile.

**P4 — Inter-interface contradiction and stakeholder dispersion**

*Threat 1 — NLP embedding quality for contradiction detection*: The cosine-similarity-based contradiction score may capture style differences rather than substantive contradictions. Formal investor-relations language in MD&A will always embed differently from conversational brand-perception copy; the embedding distance may reflect linguistic register, not logical inconsistency.
*Mitigation*: Validate the NLP contradiction score against human-coded subsample of known contradictory cases (e.g., firms with documented SEC enforcement actions alleging misleading public disclosures relative to internal practices). Report the calibration subsample's inter-rater reliability and correlation with the automated index.

*Threat 2 — Reverse causality in the dispersion relationship*: High-dispersion firms may attract incompatible stakeholder constituencies (activist investors + mass-market consumer base), which itself generates interface contradictions, rather than the other way around.
*Mitigation*: Lagged independent variable (contradiction index at t–1 → dispersion at t) as the primary specification. Cross-lagged panel model to test the direction of causality.

*Threat 3 — Missing stakeholder-perception data*: Consumer NPS data from YouGov BrandIndex or equivalent is available for large-cap consumer-facing firms but not for B2B-intensive or private-sector firms. The sample is biased toward large consumer-brand firms.
*Mitigation*: Restrict the primary sample to the set of firms covered by at least two of the three perception-data sources. Report coverage counts in the descriptive statistics table.

**P5 — Specification-readiness and AI-ROI realization**

*Threat 1 — AI-ROI measurement is not standardized*: No single accounting variable captures AI return on investment at the firm level. The proxy (functional headcount change relative to AI spend) assumes that Substrate-AI realizations manifest as headcount efficiency gains. Surface-AI deployments may produce revenue gains without headcount reduction, making the proxy noisy.
*Mitigation*: Two alternative dependent variables (revenue-per-AI-dollar and headcount-change-per-AI-dollar) reported side by side. Identify firms with documented AI ROI disclosures in earnings calls using NLP coding as a validation subsample.

*Threat 2 — CEO-transition IV exclusion restriction*: The CEO-transition instrument may violate the exclusion restriction if CEO transitions affect AI-ROI directly through CEO tenure effects (experienced CEOs deploy AI more effectively regardless of specification codification).
*Mitigation*: Control for CEO tenure directly. Report robustness analysis excluding firms where the new CEO had prior AI-intensive firm experience.

*Threat 3 — AI-adoption timing is endogenous*: Firms with strong specifications may adopt AI earlier because they have the substrate already in place. The pre-deployment SCI at time t is partly endogenous to the AI-adoption timing decision.
*Mitigation*: Use SCI at t–3 (three years before AI adoption) as the specification-readiness measure, ensuring that the codification level predates the AI-adoption decision by enough time to be plausibly exogenous.

### B.6 Pre-Registered Decision Rules

The following decision rules are fixed before the simulation runs. Any deviation from these rules in the post-experiment report must be flagged explicitly and justified.

**Statistical power threshold**: If statistical power < .80 under H₁ at the assumed effect size for any proposition, that proposition's proxy operationalization is declared underpowered in the simulation. The post-experiment report must propose an alternative operationalization or a larger N before the empirical study proceeds.

**Type I error threshold**: If the Type I error rate > .05 under H₀ for any specification, the regression specification is declared mis-specified. The source of inflation (heteroskedasticity, serial correlation, cluster-robust SE specification) must be identified and corrected before the empirical study proceeds.

**Effect-size plausibility check**: If the H₁ simulation produces point estimates outside the interval [.5 × expected_effect, 2.0 × expected_effect], the proxy operationalization is flagged as potentially mis-specified. The interval is deliberately wide to avoid over-sensitivity to DGP assumptions; estimates outside this range indicate a non-trivial discrepancy between the DGP and the theoretical model.

**Robustness reporting obligation**: For each proposition, the simulation must be run with at least two alternative specifications (different fixed-effects structure, alternative control set, alternative DV operationalization). If the primary specification shows adequate power but an alternative shows power < .60, this must be reported as a specification-sensitivity finding and included in the paper's limitations section.

**Null-result reporting**: If any proposition fails the power threshold or shows a directionally inconsistent result under H₁ (i.e., the DGP produces the correct-sign effect but the regression recovers the wrong sign due to confounders in the simulation), this is reported transparently in the post-experiment report. No proposition is dropped from the paper based on simulation results; null or inconclusive simulation results are reported alongside the theory.

### B.7 Output Artifacts

**Plots** (saved to `code/plots/`):

- `power_curve_P1.png` through `power_curve_P5.png` — statistical power (y) vs assumed effect size (x, ranging from .25d to 2.0d in increments of .25d) for each proposition. Reference line at power = .80.
- `null_distribution_qq.png` — QQ plot of t-statistics under H₀ against theoretical N(0, 1) for each proposition, confirming correct Type I error calibration.
- `effect_size_sensitivity.png` — point estimates and 95% CIs under H₁ across 1,000 simulated datasets for each proposition, plotted against the pre-registered effect-size expectation.

**Summary CSV** (`code/regression_simulation_summary.csv`): one row per proposition × condition (H₀ / H₁) × specification (primary / alternative), columns: proposition, condition, specification, power, type1_error, mean_point_estimate, sd_point_estimate, pct_in_plausible_range.

**Log file** (`code/logs/regression_simulation_run_<YYYYMMDD>.log`): verbatim stdout/stderr from execution, including random seed confirmation, sample-size parameters, and completion time.

---

## C. Reproducibility

**Random seeds**: Both experiments use `np.random.seed(20260525)` fixed at the top of each script. The seed reflects the date the experiments were pre-registered. It may not be changed post-execution to improve results.

**Dependencies** (pinned versions):

```
numpy==2.2.2
scipy==1.14.0
statsmodels==0.14.4
matplotlib==3.10.0
pandas==2.2.3
```

**Python version**: 3.12 (required; all scripts must run under Python 3.12 without modification).

**uv-based invocation** (preferred):

```
uv run --with numpy==2.2.2 --with scipy==1.14.0 --with statsmodels==0.14.4 \
       --with matplotlib==3.10.0 --with pandas==2.2.3 \
       python code/friction_tax_montecarlo.py

uv run --with numpy==2.2.2 --with scipy==1.14.0 --with statsmodels==0.14.4 \
       --with matplotlib==3.10.0 --with pandas==2.2.3 \
       python code/push_pull_regression_sim.py
```

**Expected runtime**: friction_tax_montecarlo.py — approximately 8–12 minutes on a 2024 Apple Silicon Mac (4.32M individual friction measurements). push_pull_regression_sim.py — approximately 15–20 minutes (5 propositions × 2 conditions × 1,000 simulated datasets each with N = 10,000 firm-year observations). Total expected runtime under 35 minutes.

**No network calls**: Both scripts are fully self-contained. No external data is required, no API keys, no downloads. All inputs are generated from the fixed seed.

**Companion script paths**:

- `code/friction_tax_montecarlo.py` — Section A experiment
- `code/push_pull_regression_sim.py` — Section B experiment
- `code/PRE_EXPERIMENT_NOTES.md` — verbatim copy of Section A.5 (alternative-explanations register) and Section B.5 (identification threats); committed before any execution
- `code/POST_EXPERIMENT_REPORT.md` — results vs pre-registered expectations, Cohen's d values, PASS/FAIL against each pre-registered criterion, honest report of null or unexpected results; drafted after execution
- `code/logs/` — date-stamped run logs from every execution
- `code/README.md` — invocation instructions, file inventory, provenance note linking back to paper DOI

---

## D. Code Companion Publication Plan

Per the corpus computational-reproducibility standard, the `code/` directory must be mirrored to the public companion repository before the Zenodo v1 upload. The companion script subsection in the paper body names the public URL and run command verbatim.

**Final public-mirror path**: TBD at Zenodo upload time. Anticipated path: `sbt-papers/specification-readiness/code/` or equivalent depending on public-repo naming convention confirmed at upload. Placeholder for paper body:

```
https://github.com/spectralbranding/sbt-papers/tree/main/specification-readiness/code/
```

**Run command for paper body** (to appear in the "Companion Computation Script" subsection):

```
uv run --with numpy==2.2.2 --with scipy==1.14.0 --with statsmodels==0.14.4 \
       --with matplotlib==3.10.0 --with pandas==2.2.3 \
       python friction_tax_montecarlo.py && python push_pull_regression_sim.py
```

**Publication sequence** (hard rule):

1. Run both simulations locally; confirm outputs match pre-registered expectations.
2. Write `POST_EXPERIMENT_REPORT.md` with honest PASS/FAIL evaluation.
3. Mirror `code/` directory (including all plots, CSVs, log files, README, PRE_EXPERIMENT_NOTES.md, POST_EXPERIMENT_REPORT.md) to public repo.
4. Confirm public URL is live.
5. Update paper body "Companion Computation Script" subsection with confirmed public URL.
6. Proceed to Zenodo v1 upload.

The `code/` directory must never be in a state where the scripts and the paper's cited figures are out of sync. If any paper revision changes a simulated value, the corresponding script must be updated before re-mirroring.

---

## References

Belo, Frederico, Xiaoji Lin, and Maria Ana Vitorino (2014), "Brand Capital and Firm Value," *Review of Economic Dynamics*, 17 (1), 150–169. doi:10.1016/j.red.2013.05.001.

Shannon, Claude E. (1948), "A Mathematical Theory of Communication," *Bell System Technical Journal*, 27 (3), 379–423.

---

## Version

v0.1.0 (2026-05-25): Initial pre-registered version. Committed before any simulation code is executed. Updates require an explicit changelog entry in this document with date, reason, and whether the update occurred before or after execution.
