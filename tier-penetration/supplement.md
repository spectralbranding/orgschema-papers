# Online Supplement to "AI Tier Penetration: A Theory of Substrate-Dependent Competitive Advantage"

**Dmitry Zharnikov**

ORCID: 0009-0000-6893-9231

DOI: [10.5281/zenodo.20087036](https://doi.org/10.5281/zenodo.20087036)

Working Paper v1.0.0 -- May 2026

---

*The main paper is published at https://doi.org/10.5281/zenodo.20087036 and at https://github.com/spectralbranding/orgschema-papers/tree/main/tier-penetration/. The companion computation script is at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-penetration/code/tier_penetration_simulation.py.*

---

This online supplement contains the formal derivations, robustness checks, sensitivity analyses, full identification strategy and empirical test design, and companion-script documentation that the body and Appendix A of Zharnikov (2026ak) summarize but do not develop in full. Five sections (S1 through S5) follow the structure of the body's references to "Online Supplement S*". The supplement is independently downloadable alongside the parent paper at the published Zenodo record.

S1 contains the Lagrangian derivation and comparative-statics proofs. S2 contains CES robustness. S3 contains α_t calibration sensitivity. S4 contains the full identification strategy and empirical test design — including the tier-assignment protocol, disclosure-coding dictionary exemplars, pilot validation design (target inter-rater reliability, kappa targets per Krippendorff 2004, BERT-classifier robustness check), and the full five-threat threats-to-identification table. This material is positioned in the supplement rather than the body because the paper's primary contribution is deductive theory; the empirical follow-on is a validation roadmap for a future companion empirical paper. S5 contains the companion-script documentation.

---

## S1. Lagrangian setup, first-order conditions, and signs of comparative statics for the AI-extended share rule

This section derives the AI-extended generalized share rule of §4 from first principles, states and proves the proposition that ∂w_6*/∂γ_6 < 0 (the formal version of the Tier-6 over-allocation paradox of Prediction A1), states and proves ∂w_4*/∂Δ_4 > 0 (the formal version of the substrate-building threshold of Prediction A2), and identifies the joint-shock sign ambiguity that motivates the §6 fall-back acknowledgment.

*Setup.* The firm chooses an allocation vector w = (w_2, w_3, w_4, w_5, w_6) ∈ R^5_+ to maximize the AI-extended long-run value function

V_LR(w; r, γ, Δ) = A · I · ∏_t [m_t · w_t / (δ_t^eff + r)]^{α_t}

with δ_t^eff = δ_t^0 − Δ_t, subject to the AI-extended Jorgensonian budget constraint

Σ_t γ_t · (δ_t^eff + r) · w_t = 1

where γ_t ∈ (0, 1] is the tier-t cost shock, Δ_t ∈ [0, δ_t^0) is the tier-t durability shock, the inherited δ_t^0 is the pre-AI persistence rate from Appendix A.2, A > 0 is a productivity scalar, m_t ∈ [0, 1] is the M&A separability factor, α_t ∈ (0, 1) is the output elasticity satisfying Σ_t α_t = 1 (constant returns to scale), and r is the principal's effective discount rate.

*Lagrangian.* Taking the natural logarithm of the value function and forming the Lagrangian:

L(w, λ; r, γ, Δ) = ln A + ln I + Σ_t α_t · [ln m_t + ln w_t − ln(δ_t^eff + r)] − λ · [Σ_t γ_t · (δ_t^eff + r) · w_t − 1]

*First-order conditions.* The FOC with respect to w_t is

∂L/∂w_t = α_t / w_t − λ · γ_t · (δ_t^eff + r) = 0

which implies

w_t* = α_t / [λ · γ_t · (δ_t^eff + r)]

Substituting into the budget constraint:

Σ_t γ_t · (δ_t^eff + r) · w_t* = Σ_t γ_t · (δ_t^eff + r) · α_t / [λ · γ_t · (δ_t^eff + r)] = (1/λ) · Σ_t α_t = 1/λ = 1

since Σ_t α_t = 1 under constant returns to scale. So λ = 1, and the **generalized closed-form share rule** is

**w_t*(r; γ, Δ) = α_t / [γ_t · (δ_t^eff + r)]**

The dollar-weighted (empirically observable) share is

dollar-share_t*(r; γ, Δ) = w_t*(r; γ, Δ) / Σ_s w_s*(r; γ, Δ)

*Log-concavity verification.* The Hessian of ln V_LR with respect to w is diagonal with entries ∂²ln V_LR / ∂w_t² = − α_t / w_t² < 0 for all t under the maintained assumption α_t ∈ (0, 1). The negative-definite Hessian is preserved under both AI shocks because γ_t and Δ_t enter the value function only through the (δ_t^eff + r) denominator and the budget constraint, neither of which alters the curvature in w. The interior optimum is therefore unique for any admissible parameter vector (γ, Δ).

*Proposition S1.1 (Tier-6 over-allocation paradox).* Under the generalized share rule, the partial derivative of the dollar-weighted Tier-6 share with respect to γ_6 is negative when γ_t = 1 for t ≤ 5 and Δ_t = 0 for all t. Formally:

sign(∂(dollar-share_6*)/∂γ_6) = − sign(δ_6 − δ_S^eff) < 0

where δ_S^eff is the share-rule-weighted average decay rate of the substrate tiers t ∈ {2, 3, 4, 5} evaluated at the calibration of A.2.

*Proof.* Hold γ_t = 1 for t ≤ 5 and Δ_t = 0 for all t. The non-normalized share at Tier 6 is w_6* = α_6 / [γ_6 · (δ_6 + r)] and at substrate tier t is w_t* = α_t / (δ_t + r) for t ≤ 5. The dollar-weighted Tier-6 share is

dollar-share_6* = w_6* / [w_6* + Σ_{t≤5} w_t*]

Differentiating with respect to γ_6 and applying the quotient rule, after simplification:

∂(dollar-share_6*)/∂γ_6 = − [α_6 / (γ_6² · (δ_6 + r))] · [Σ_{t≤5} w_t* / (Σ_t w_t*)²] < 0

since all terms inside the bracket are positive. The dollar-weighted Tier-6 share is monotonically decreasing in γ_6: as AI cheapens the surface tier (γ_6 falls), the optimal share at Tier 6 rises. The structural source of the sign is the large value of δ_6 = .50 relative to the substrate-tier average δ_S = .119: the relative-price reduction at Tier 6 is amplified by the high baseline rental rate at Tier 6, so the substitution toward Tier 6 dominates the income effect. QED.

*Proposition S1.2 (substrate-building threshold).* Under the generalized share rule with γ_4 ≤ 1 fixed, the partial derivative of the long-run Tier-4 stock with respect to Δ_4 is positive:

∂S_4*/∂Δ_4 = ∂(w_4* · I / δ_4^eff)/∂Δ_4 > 0

*Proof.* Substitute w_4*(r; γ, Δ) = α_4 / [γ_4 · (δ_4^eff + r)] into S_4* = w_4* · I / δ_4^eff:

S_4* = (α_4 · I) / [γ_4 · δ_4^eff · (δ_4^eff + r)]

Let f(δ_4^eff) = δ_4^eff · (δ_4^eff + r) = (δ_4^eff)² + r · δ_4^eff. Differentiating with respect to Δ_4 (recalling δ_4^eff = δ_4^0 − Δ_4):

∂f/∂Δ_4 = (∂f/∂δ_4^eff) · (∂δ_4^eff/∂Δ_4) = − [2 · δ_4^eff + r] < 0

Hence ∂S_4*/∂Δ_4 = − (α_4 · I) · [− (2 · δ_4^eff + r)] / [γ_4 · f(δ_4^eff)²] > 0 since the numerator's effective sign is positive after the chain-rule cancellation, and the denominator is strictly positive. The long-run Tier-4 stock is monotonically increasing in Δ_4, confirming the substrate-building threshold result. The discontinuity that A2 predicts is structural rather than algebraic: at Δ_4 = 0 the AI deployment reduces to a γ-only cost shock with no substrate accumulation, and at Δ_4 > 0 (proprietary fine-tune or owned-weights configuration) the substrate-building component becomes admissible. QED.

*Proposition S1.3 (joint-shock sign ambiguity).* When γ_t and Δ_t move jointly at the same tier, the sign of the cross-partial ∂²w_t*/∂γ_t∂Δ_t can be positive or negative depending on the magnitudes of the individual shocks.

*Proof sketch.* Differentiate w_t* = α_t / [γ_t · (δ_t^eff + r)] = α_t / [γ_t · (δ_t^0 − Δ_t + r)] with respect to both γ_t and Δ_t:

∂²w_t*/∂γ_t∂Δ_t = α_t · [γ_t · ∂(δ_t^eff + r)/∂Δ_t − (δ_t^eff + r) · ∂γ_t/∂Δ_t] / [γ_t² · (δ_t^eff + r)²]

The expression depends on the joint movement pattern. Under a measurement model where empirical disclosure language correlates γ_t and Δ_t (e.g., a 10-K passage describing "a proprietary fine-tune that has reduced our customer-service operating cost while building a defensible asset" reflects both γ_5 reduction and Δ_5 increase), the cross-partial term carries opposing components and the sign is ambiguous in finite samples. This ambiguity motivates the §6 fall-back acknowledgment that clean separate identification of γ_t versus Δ_t with public data may be infeasible and that joint identification of (γ_t, Δ_t) at the tier level may be the operational empirical specification. QED.

The three propositions S1.1, S1.2, and S1.3 together formalize the comparative-statics machinery that drives the body's Predictions A1, A2, and the §6/§9 fall-back acknowledgment, respectively. The remaining body predictions (A3 Tier-2 moat asymmetry, A4 penetration-depth ordering, A5 horizon-conditional sign flip, A6 rotation acceleration) follow from analogous derivations applied to the generalized share rule under tier-specific shock patterns; the derivations are verbal-formal in the body §5 and reproduce numerically in the companion script (S5).

---

## S2. CES robustness for the AI-extended share rule

The Cobb-Douglas (σ = 1) specification is maintained throughout the body. This section reports a constant-elasticity-of-substitution robustness check at σ ∈ {.5, 1.0, 1.5} for the AI-extended share rule, parallel in structure to the 2026aj Online Supplement S4 robustness check for the inherited base model.

*Setup.* Replace the inner Cobb-Douglas aggregator with a CES aggregator of degree σ:

V_LR(w; r, γ, Δ; σ) = A · I · [Σ_t α_t · (m_t · w_t / (δ_t^eff + r))^{(σ−1)/σ}]^{σ/(σ−1)}

The Cobb-Douglas case is recovered as σ → 1 by L'Hôpital-style limit. The optimization problem is the same as in S1 — maximize V_LR subject to the AI-extended budget constraint Σ_t γ_t · (δ_t^eff + r) · w_t = 1 — and the FOC structure parallels S1 with the share rule generalizing to

w_t*(r; γ, Δ; σ) = [α_t · (m_t / (δ_t^eff + r))^{(σ−1)/σ}]^σ · [γ_t · (δ_t^eff + r)]^{−σ} · K(σ)

where K(σ) is the budget-normalization constant. The closed form of S1 (σ = 1) recovers under the limit and the central qualitative result extends.

*Tier-6 paradox at σ ∈ {.5, 1.0, 1.5}.* The companion script of S5 evaluates ∂(dollar-share_6*)/∂γ_6 at σ ∈ {.5, 1.0, 1.5} under the calibration of A.2. The qualitative ordering — dollar-share_6* monotonically decreasing in γ_6 — survives at σ = 1.0 (the maintained Cobb-Douglas case) and at σ = 1.5 (the gross-substitutes case, where allocations across tiers become more responsive to relative-price changes). At σ = .5 (the gross-complements case, where allocations become less responsive), the sign of the comparative static can become ambiguous in two-tier reductions, paralleling the boundary-case finding in 2026aj Online Supplement S4. Numerical evaluation of the full five-tier model at σ = .5 with the calibrated parameters preserves the directional sign of A1 at the calibrated values but the magnitude attenuates by approximately 35% relative to σ = 1.0.

*B/A multiple ordering at σ ∈ {.5, 1.0, 1.5}.* Comparing two stylized firm profiles — Profile A (Tier-6-heavy, w_6 = .70) versus Profile B (Tier-4/5-heavy, w_4-5 = .65) — the long-run value ratio V_LR(B) / V_LR(A) is computed at each σ. The ratio is 1.93 at σ = 1.0 (the maintained Cobb-Douglas case from 2026aj), 2.17 at σ = 1.5 (gross substitutes), and 1.22 at σ = .5 (gross complements). The qualitative ordering V_LR(B) > V_LR(A) — Tier-4/5-heavy beats Tier-6-heavy — survives all three elasticity values; the magnitude is sensitive to σ but the direction is not.

*Tier-6 paradox under joint γ_6 and Δ_t shocks.* When AI deployment includes γ_6 < 1 at the surface tier and Δ_t > 0 at deeper tiers (the configuration that distinguishes substrate-building deployments from surface-only deployments), the qualitative directional signs of A1 (∂(dollar-share_6*)/∂γ_6 < 0) and A2 (∂S_4*/∂Δ_4 > 0) survive at σ ∈ {1.0, 1.5}. Under σ = .5, the two effects can partially cancel in the dollar-weighted share-rule decomposition, and the interpretation of the sign becomes a matter of whether the gross-complementary regime applies to the firm's specific tier-deployment configuration; the body maintains σ = 1 throughout and the CES robustness is reported as a parameter sensitivity rather than a structural claim about the firm's production technology.

*Practical implication.* The Cobb-Douglas maintained specification of §4 is a conservative middle-ground choice that preserves the framework's directional predictions in the gross-substitutes case (where the predictions are stronger than under Cobb-Douglas) and in the modal case σ = 1.0; the gross-complements case σ = .5 represents a boundary regime in which the framework's directional predictions hold only with attenuation. Empirical work that recovers σ from firm-level production-function estimation can sharpen the prediction set; the framework's structural claims do not depend on σ being recovered exactly.

---

## S3. Sensitivity to alternative α_t calibrations

The output-elasticity vector α_t enters the share rule directly: w_t* = α_t / [γ_t · (δ_t^eff + r)]. The body uses a baseline calibration α_6 = .12, α_4 = α_5 = .24, α_2 = α_3 = .20 derived proportional to the M&A separability factors m_t. This section reports the sensitivity of the framework's headline predictions to two alternative calibrations. Supplement S3 was reconciled to companion-script outputs at v1.0.0; see `tier_penetration_simulation.py::alpha_calibration_sensitivity()` for the implementation.

*Scenario 1 — Baseline (m_t-proportional).* α_6 = .12, α_4 = α_5 = .24, α_2 = α_3 = .20. The dollar-share at Tier 6 evaluated at r = .15, γ_6 = .8, all other γ_t = 1, all Δ_t = 0 is .065. The B/A multiple ratio (Profile A Tier-6-heavy versus Profile B Tier-4/5-heavy at the same parameters) is 1.93. The Tier-6 paradox magnitude — ∂(dollar-share_6*)/∂γ_6 — is .076 at γ_6 = .8 evaluation point.

*Scenario 2 — Conservative (uniform).* α_t = .20 for all t. The dollar-share at Tier 6 at the same evaluation point is .112. The B/A multiple ratio attenuates to 1.55 because the elasticity at Tier 6 rises to .20 from .12, increasing the surface tier's contribution to total value. The Tier-6 paradox magnitude rises to .124.

*Scenario 3 — Concentrated-stock.* α_6 = .05, α_4 = α_5 = .30, α_2 = α_3 = .175. The dollar-share at Tier 6 falls to .027 because the surface-tier elasticity is sharply reduced; the substrate tiers (especially Tier-4 and Tier-5) absorb a larger share of the planner's optimal allocation. The B/A multiple ratio rises to 2.39 because the concentrated-stock calibration places higher elasticity on the substrate tiers and the Tier-4/5-heavy Profile B exploits the calibration's weighting more efficiently. The Tier-6 paradox magnitude is .033 at γ_6 = .8.

*Cross-scenario invariants.* The directional sign of the Tier-6 paradox — ∂(dollar-share_6*)/∂γ_6 < 0 — holds across all three calibrations. The B/A multiple ranges from 1.55 (conservative) to 2.39 (concentrated), a 1.54× spread driven by the relative weighting of Tier-6 versus substrate-tier elasticities. The framework's directional prediction A1 is robust to α_t mis-calibration; the magnitude of the predicted M&A-multiple effect is sensitive and should be re-estimated alongside any panel that recovers α_t from firm-level data.

The three-scenario sensitivity check parallels the analogous exercise in 2026aj's calibration appendix and confirms that the framework's structural claims do not depend on the specific α_t calibration; they depend on the architectural-structural ordering m_6 < m_2 = m_3 < m_4 = m_5, which the calibration preserves across the three scenarios.

---

## S4. Identification Strategy and Empirical Test Design

This section develops the full identification strategy for testing Propositions P1-P3, including the tier-assignment protocol, disclosure-coding pilot design, and the complete five-threat threats-to-identification table. The body's "Implications for Empirical Testing" section sketches these elements qualitatively; this section provides the operational detail needed to implement the empirical follow-on. The material is positioned here rather than in the body because the paper's primary contribution is deductive theory; empirical test design is a roadmap for a future companion empirical paper.

*Tier-assignment protocol.* The unit of tier assignment is the AI-deployment artifact, not the project. A single project commonly produces multiple artifacts at different tiers; treating the project as the assignment unit collapses the architectural decomposition the framework requires. Each artifact is assigned by asking: where does the durable artifact reside in the six-tier stack? The four boundary-object cases illustrate per-artifact decomposition. Klarna's chatbot deployment produces a transient Tier-6 customer interaction, a Tier-5 chatbot configuration, and a Tier-3 disclosure footprint; Spotify's recommendation system produces a Tier-6 served recommendation, a Tier-2 user-behavior model (the data flywheel), and a Tier-4 platform specification; BloombergGPT produces a Tier-5 fine-tune and Tier-4 terminal-embedded outputs; Stripe Radar produces a Tier-2 fraud-decisioning AI and a Tier-6 merchant-facing output.

*Disclosure-coding pilot design.* The pilot hand-codes 100 AI-related disclosures from a stratified S&P 1500 sample across the 2023-2026 window. Target inter-rater reliability is Cohen's kappa ≥ .65 for tier assignment, following Krippendorff (2004) content-analysis methodology and matching the .60-.75 range Hassan, Hollander, van Lent, and Tahoun (2019) achieve on analogous text-based political-risk topic classification. Two independent coders, third-coder adjudication, both pairwise and three-way kappas reported. The pilot also validates tier-depth scores against Babina, Fedyk, He, and Hodson (2024) aggregate AI-investment measures via two pre-committed correlation tests (sum-correlation ≥ .40; per-tier collinearity ≤ .85). A BERT-based or LLM-classifier robustness check is pre-committed.

*Disclosure-coding dictionary exemplars.* Tier-6 positive exemplars: "generative marketing copy," "AI customer-service chatbot," "programmatic-bidding optimization." Tier-5 positive exemplars: "proprietary fine-tune," "owned model weights," "AI workflow automation agent." Tier-4 positive exemplars: "AI-as-product," "embedding-context switching cost," "AI-codified product specification." Tier-2 positive exemplars: "data flywheel," "recommendation engine constitutive of product," "AI fraud-decisioning." Tier-3 positive exemplars: "AI contract drafting," "AI compliance monitoring." Tier-1: smaller dictionary; hard ceilings make positive exemplars rare in current disclosure data. Negative exemplars (artifacts that look like tier indicators but are not): generic mentions of "AI strategy," "evaluating AI vendors," "AI pilot program" (unassigned); "AI-powered analytics dashboard" (requires artifact-level decomposition).

*Threats-to-identification table (full).* The body §6 sketches three first-order threats. This section expands each into prose discussion across four columns — severity, proposed mitigation, residual risk, and robustness checks — and adds two further threats (measurement error in the tier-depth disclosure measure; attrition due to acquisition during the panel).

*Threat 1: Selection on unobservables.* Severity HIGH. Firms that were ready for Tier-4 AI deployment in 2022, at the GPT-3-to-GPT-4 transition, were systematically firms with superior pre-existing data infrastructure, specification-quality discipline, and ML-engineering capacity. The pre-existing infrastructure differential is correlated with subsequent firm-level outcomes through channels other than the AI deployment itself, so naive cross-sectional comparisons of Tier-4 deployers versus non-deployers conflate the deployment effect with the selection effect. *Proposed mitigations:* (a) pre-trends test on intangible-intensity series prior to the AI-deployment event, demonstrating that pre-treatment firm-level outcomes do not differ between deployers and non-deployers; (b) firm fixed effects in the difference-in-differences specification, absorbing time-invariant firm-level heterogeneity; (c) entropy-balancing or Coarsened Exact Matching on observable pre-shock characteristics — size, intangible intensity, prior R&D spend, sector AIOE per Felten, Raj, and Seamans (2021), and pre-treatment earnings-call AI-mention frequency. *Residual risk:* time-varying unobservables remain — firms whose data infrastructure was improving at the moment of AI deployment cannot be matched on the time-varying improvement, and the residual selection-on-time-varying-unobservables cannot be eliminated by the proposed mitigations. *Robustness checks:* (a) Oster (2019) bounding-the-effect-of-unobservables coefficient-stability test; (b) sub-sample analysis restricted to firms with ex-ante similar data-infrastructure scores constructed from prior-year disclosure language.

*Threat 2: Parallel-trends violation.* Severity MEDIUM. The GPT-3 → GPT-4 → GPT-5 capability-frontier shocks are common shocks correlated with broader tech-sector time trends, so the difference-in-differences identification assumption that treated and control firms would have followed parallel trends absent treatment is contestable in any tech-sector-heavy panel. *Proposed mitigations:* (a) pre-trends test on intangible-intensity series demonstrating parallel pre-treatment trajectories; (b) placebo difference-in-differences on capital-light service-sector firms (legal services, accounting, financial services excluding fintech) where Tier-4 AI deployment is implausible at the relevant horizon, providing a parallel-trends placebo; (c) sector-by-time fixed effects to absorb common sector-time shocks; (d) Callaway and Sant'Anna (2021) staggered-adoption difference-in-differences estimator if treatment timing is heterogeneous across firms. *Residual risk:* heterogeneous treatment effects within the tech sector remain — firms with different pre-existing AI exposure may respond differentially to the same capability-frontier shock, and the heterogeneous-treatment-effect bias cannot be eliminated by the proposed mitigations. *Robustness checks:* (a) De Chaisemartin and D'Haultfœuille (2020) bounds on heterogeneous treatment effects; (b) leave-one-out sub-sample analysis to assess whether estimates are driven by specific tech-sector sub-industries.

*Threat 3: Founder-horizon endogeneity.* Severity MEDIUM. Founder-CEO status, family-firm governance structure, and ownership concentration are themselves outcomes of past performance and past strategic decisions, so the founder-horizon proxies that A5 requires for its sign-flip test are endogenous to the firm-value outcomes the framework attempts to explain. *Proposed mitigations:* (a) gender-of-first-born instrument from Bennedsen, Nielsen, Pérez-González, and Wolfenzon (2007) for family-firm horizon, exploiting the documented relationship between first-born-child characteristics and family-firm CEO succession; (b) CEO-founder tenure interacted with industry-shock indicators to identify within-firm variation in effective horizon; (c) institutional-concentration measures as alternative horizon proxies that are at least partially exogenous to firm-level performance. *Residual risk:* instrument validity is contestable in the post-2010 governance environment — the first-born-gender instrument has weakened in predictive power over time as gender-neutral succession norms have spread, and the residual instrument-validity uncertainty cannot be eliminated. *Robustness checks:* (a) overidentification test combining the Bennedsen et al. (2007) instrument with the alternative founder-tenure-by-industry-shock instrument; (b) sub-sample analysis restricted to family firms with first-born children of identifiable gender pre-2000.

*Threat 4: Measurement error in the tier-depth disclosure measure.* Severity LOW-MEDIUM. The tier-depth measure is constructed from text-based dictionary-coding of 10-K Item 1A, Item 7, and earnings-call transcript language, following the Hassan, Hollander, van Lent, and Tahoun (2019) text-based political-risk measurement template. Classical measurement error attenuates regression coefficients toward zero. *Proposed mitigations:* (a) inter-rater reliability check at the pilot stage with target Cohen's kappa ≥ .65 per Krippendorff (2004); (b) BERT-based or LLM-classifier validation pass against the human-coded sample with agreement-rate reported as secondary validation; (c) split-sample replication. *Residual risk:* non-classical measurement error — tier-depth measures may be more accurately coded for firms with verbose disclosure language than for firms with concise disclosure language, and the disclosure-verbosity correlation with firm size is a confounder. *Robustness checks:* (a) firm-size sub-sample stratification; (b) controls for total disclosure length in the regression specification.

*Threat 5: Attrition due to acquisition during the panel.* Severity LOW-MEDIUM. The framework's empirical predictions concern M&A-multiple effects, but observation of M&A multiples requires that firms in the panel are acquired (or remain on the market in a way that allows multiple computation). Firms that become target firms during the panel are non-randomly selected — they are systematically more likely to be successful Tier-4 deployers or systematically less likely to be Tier-6-only deployers. *Proposed mitigations:* (a) Heckman (1979) two-stage selection-correction model with the first stage modeling the probability of acquisition; (b) sub-sample analysis restricted to acquired firms with an explicit selection-correction adjustment; (c) inverse-probability weighting on the propensity-to-be-acquired score. *Residual risk:* the exclusion restriction in Heckman correction is contestable — instruments that affect acquisition probability without affecting M&A multiple conditional on acquisition are scarce. *Robustness checks:* (a) bound-the-treatment-effect approach following Lee (2009); (b) sensitivity analysis to the exclusion-restriction assumption.

The full threats-to-identification structure makes explicit that even under the cleanest mitigation set, residual identification challenges remain — particularly time-varying unobservables and instrument-validity contestability. The framework's empirical implementation should be positioned as a validation roadmap that progressively narrows the identified effect rather than as a single test that delivers the framework's predictions in one regression specification. The §6 fall-back to deductive theory plus calibrated comparative-statics simulation, in which the body §6 explicitly acknowledges that the empirical implementation may settle for joint identification of (γ_t, Δ_t) at the tier level rather than separate identification of each parameter, is the methodological end-point at which the framework remains testable even when full panel identification is infeasible.

---

## S5. Companion script docstring, run command, and parameter table

This section documents the companion computation script that reproduces every numerical value reported in the main paper and this supplement.

*Script location.* `tier_penetration_simulation.py`, published at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-penetration/code/tier_penetration_simulation.py.

*Run command.* `uv run python tier_penetration_simulation.py`

*Python version and dependencies.* Python ≥ 3.10. Required packages: numpy ≥ 1.24, scipy ≥ 1.10. No plotting dependencies (the parent paper has no figures; tabular output to stdout). Random seed: numpy.random.seed(42) set at module load for structural consistency with the corpus pattern; the script is fully deterministic and uses no stochastic operations.

*Function inventory.*

`effective_delta(delta_0, Delta)` — returns δ_t^eff = δ_t^0 − Δ_t with assertion Δ_t < δ_t^0. Inputs: delta_0 is a dict mapping tier to baseline decay rate; Delta is a dict mapping tier to durability shock. Returns: dict mapping tier to effective decay rate.

`share_rule(alpha, delta_eff, gamma, r)` — returns the un-normalized w_t* vector under the generalized AI-extended share rule w_t* = α_t / [γ_t · (δ_t^eff + r)]. Inputs: alpha is a dict of α_t values (default the baseline calibration α_6 = .12, α_4 = α_5 = .24, α_2 = α_3 = .20); delta_eff is a dict of δ_t^eff values; gamma is a dict of γ_t values (default all γ_t = 1.0 corresponding to no AI shock); r is the principal's effective discount rate (default r = .15). Returns: dict mapping tier to un-normalized rental-share value.

`dollar_shares(w_star)` — normalizes the un-normalized share dict to dollar-weighted shares summing to 1. Returns: dict mapping tier to dollar-weighted share.

`proposition_1_tier6_paradox()` — replicates body §5 Proposition 1 by sweeping γ_6 ∈ {.5, .7, .9, 1.0} under the baseline calibration and reporting the sign of ∂(dollar-share_6*)/∂γ_6 at each point. Returns: dict with keys "gamma_6_grid", "dollar_share_6", "paradox_magnitude", "sign".

`proposition_2_tier4_threshold()` — replicates body §5 Proposition 2 by computing the Tier-4 stock S_4* across the Δ_4 = 0 vs Δ_4 > 0 threshold, demonstrating the level-shift interpretation. Returns: dict with keys "delta_4_eff_grid", "S_4_star", "level_shift_at_threshold".

`proposition_3_horizon_flip()` — replicates body §5 Proposition 3 by computing dollar-share_6*(r) across r ∈ {.10, .15, .20} under the maintained Cobb-Douglas (σ = 1) and demonstrating ∂w_6*/∂r > 0. Returns: dict with keys "r_grid", "dollar_share_6", "sign", "scope_condition".

`ces_robustness(sigma_values=[.5, 1.0, 1.5])` — replicates Online Supplement S2 by evaluating the Tier-6 paradox sign and the Profile B / Profile A multiple ratio at each σ ∈ sigma_values. Returns: dict with keys "sigma", "tier6_paradox_sign", "B_over_A_multiple", "tier6_paradox_magnitude_at_gamma_6_eq_pt8".

`alpha_calibration_sensitivity()` — replicates Online Supplement S3 under three scenarios (m_t-proportional baseline, conservative-uniform, concentrated-stock); reports dollar-share_6*, B/A multiple ratio, and Tier-6 paradox magnitude per scenario. Returns: dict mapping scenario name to result dict.

`boundary_object_cases()` — replicates body §6 by computing the implied (γ_t, Δ_t) vector and the long-run M&A-multiple direction for each of the four illustrative cases (Klarna, Spotify, BloombergGPT, Stripe Radar). Returns: list of BoundaryCase namedtuples.

`main()` — top-level driver invoked by the run command `uv run python tier_penetration_simulation.py`. Calls each of the eight simulation functions above in sequence, prints structured tabular output with section headers, and runs the verification check that script-computed values match the paper-stated values reconciled at v1.0.0.

*Parameter table.* The script's hard-coded baseline calibration is:

| Parameter | Value | Source |
|---|---|---|
| α_6 | .12 | Appendix A.3 (m_t-proportional) |
| α_4 = α_5 | .24 | Appendix A.3 |
| α_2 = α_3 | .20 | Appendix A.3 |
| m_6 | .25 | Appendix A.1 |
| m_4 = m_5 | 1.0 | Appendix A.1 |
| m_2 = m_3 | .6 | Appendix A.1 |
| δ_6 | .50 | Belo, Lin, and Vitorino (2014) |
| δ_5 | .175 | Eisfeldt and Papanikolaou (2013); Corrado, Hulten, and Sichel (2009) |
| δ_4 | .15 | Lev and Sougiannis (1996); Hall, Jaffe, and Trajtenberg (2005) |
| δ_2 = δ_3 | .075 | Wiggins and Ruefli (2002) extrapolation |
| r (default) | .15 | Principal's effective discount rate; sensitivity analysis at r ∈ {.10, .15, .20} |
| γ_t (default no-shock) | 1.0 | Pre-AI baseline |
| Δ_t (default no-shock) | 0 | Pre-AI baseline |
| Random seed | 42 | numpy.random.seed |

*Reproducibility statement.* Every numerical value in the body and in this supplement that is not directly traceable to an external published source is reproducible from `tier_penetration_simulation.py` under the run command above. The script has no external data dependencies — all calibrated parameters are hard-coded — and produces deterministic output across runs. The script will be published at the public mirror at the URL above once Zenodo upload completes.

---

*End of Online Supplement.*
