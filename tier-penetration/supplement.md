# Online Supplement to "AI Tier Penetration: A Theory of Substrate-Dependent Competitive Advantage"

**Dmitry Zharnikov**

ORCID: 0009-0000-6893-9231

DOI: [10.5281/zenodo.20087036](https://doi.org/10.5281/zenodo.20087036)

Working Paper v1.0.0 -- May 2026

---

*The main paper is published at https://doi.org/10.5281/zenodo.20087036 and at https://github.com/spectralbranding/orgschema-papers/tree/main/tier-penetration/. The companion computation script is at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-penetration/code/tier_penetration_simulation.py.*

---

This online supplement contains the formal derivations, robustness checks, sensitivity analyses, full identification strategy and empirical test design, and companion-script documentation that the body and Appendix A of Zharnikov (2026ak) summarize but do not develop in full. Five sections (S1 through S5) follow the structure of the body's references to "Online Supplement S*". The supplement is independently downloadable alongside the parent paper at the published Zenodo record.

S1 contains the Lagrangian derivation and comparative-statics proofs. S2 contains CES robustness. S3 contains $\alpha_t$ calibration sensitivity. S4 contains the full identification strategy and empirical test design — including the tier-assignment protocol, disclosure-coding dictionary exemplars, pilot validation design (target inter-rater reliability, kappa targets per Krippendorff 2004, BERT-classifier robustness check), and the full five-threat threats-to-identification table. This material is positioned in the supplement rather than the body because the paper's primary contribution is deductive theory; the empirical follow-on is a validation roadmap for a future companion empirical paper. S5 contains the companion-script documentation.

---

## S1. Lagrangian setup, first-order conditions, and signs of comparative statics for the AI-extended share rule

This section derives the AI-extended generalized share rule of §4 from first principles, states and proves the proposition that $\partial w_6^*/\partial\gamma_6 < 0$ (the formal version of the Tier-6 over-allocation paradox of Prediction A1), states and proves $\partial w_4^*/\partial\Delta_4 > 0$ (the formal version of the substrate-building threshold of Prediction A2), and identifies the joint-shock sign ambiguity that motivates the §6 fall-back acknowledgment.

*Setup.* The firm chooses an allocation vector $w = (w_2, w_3, w_4, w_5, w_6) \in \mathbb{R}_+^5$ to maximize the AI-extended long-run value function

$$V_{LR}(w; r, \gamma, \Delta) = A \cdot I \cdot \prod_t [m_t \cdot w_t / (\delta_t^{\text{eff}} + r)]^{\alpha_t}$$

with $\delta_t^{\text{eff}} = \delta_t^0 - \Delta_t$, subject to the AI-extended Jorgensonian budget constraint

$$\Sigma_t \, \gamma_t \cdot (\delta_t^{\text{eff}} + r) \cdot w_t = 1$$

where $\gamma_t \in (0, 1]$ is the tier-$t$ cost shock, $\Delta_t \in [0, \delta_t^0)$ is the tier-$t$ durability shock, the inherited $\delta_t^0$ is the pre-AI persistence rate from Appendix A.2, $A > 0$ is a productivity scalar, $m_t \in [0, 1]$ is the M&A separability factor, $\alpha_t \in (0, 1)$ is the output elasticity satisfying $\Sigma_t \, \alpha_t = 1$ (constant returns to scale), and $r$ is the principal's effective discount rate.

*Lagrangian.* Taking the natural logarithm of the value function and forming the Lagrangian:

$$L(w, \lambda; r, \gamma, \Delta) = \ln A + \ln I + \Sigma_t \, \alpha_t \cdot [\ln m_t + \ln w_t - \ln(\delta_t^{\text{eff}} + r)] - \lambda \cdot [\Sigma_t \, \gamma_t \cdot (\delta_t^{\text{eff}} + r) \cdot w_t - 1]$$

*First-order conditions.* The FOC with respect to $w_t$ is

$$\partial L/\partial w_t = \alpha_t / w_t - \lambda \cdot \gamma_t \cdot (\delta_t^{\text{eff}} + r) = 0$$

which implies

$$w_t^* = \alpha_t / [\lambda \cdot \gamma_t \cdot (\delta_t^{\text{eff}} + r)]$$

Substituting into the budget constraint:

$$\Sigma_t \, \gamma_t \cdot (\delta_t^{\text{eff}} + r) \cdot w_t^* = \Sigma_t \, \gamma_t \cdot (\delta_t^{\text{eff}} + r) \cdot \alpha_t / [\lambda \cdot \gamma_t \cdot (\delta_t^{\text{eff}} + r)] = (1/\lambda) \cdot \Sigma_t \, \alpha_t = 1/\lambda = 1$$

since $\Sigma_t \, \alpha_t = 1$ under constant returns to scale. So $\lambda = 1$, and the **generalized closed-form share rule** is

$$w_t^*(r; \gamma, \Delta) = \alpha_t / [\gamma_t \cdot (\delta_t^{\text{eff}} + r)]$$

The dollar-weighted (empirically observable) share is

$$\text{dollar-share}_t^*(r; \gamma, \Delta) = w_t^*(r; \gamma, \Delta) / \Sigma_s \, w_s^*(r; \gamma, \Delta)$$

*Log-concavity verification.* The Hessian of $\ln V_{LR}$ with respect to $w$ is diagonal with entries $\partial^2 \ln V_{LR} / \partial w_t^2 = - \alpha_t / w_t^2 < 0$ for all $t$ under the maintained assumption $\alpha_t \in (0, 1)$. The negative-definite Hessian is preserved under both AI shocks because $\gamma_t$ and $\Delta_t$ enter the value function only through the $(\delta_t^{\text{eff}} + r)$ denominator and the budget constraint, neither of which alters the curvature in $w$. The interior optimum is therefore unique for any admissible parameter vector $(\gamma, \Delta)$.

*Proposition S1.1 (Tier-6 over-allocation paradox).* Under the generalized share rule, the partial derivative of the dollar-weighted Tier-6 share with respect to $\gamma_6$ is negative when $\gamma_t = 1$ for $t \le 5$ and $\Delta_t = 0$ for all $t$. Formally:

$$\text{sign}(\partial(\text{dollar-share}_6^*)/\partial\gamma_6) = - \, \text{sign}(\delta_6 - \delta_S^{\text{eff}}) < 0$$

where $\delta_S^{\text{eff}}$ is the share-rule-weighted average decay rate of the substrate tiers $t \in \{2, 3, 4, 5\}$ evaluated at the calibration of A.2.

*Proof.* Hold $\gamma_t = 1$ for $t \le 5$ and $\Delta_t = 0$ for all $t$. The non-normalized share at Tier 6 is $w_6^* = \alpha_6 / [\gamma_6 \cdot (\delta_6 + r)]$ and at substrate tier $t$ is $w_t^* = \alpha_t / (\delta_t + r)$ for $t \le 5$. The dollar-weighted Tier-6 share is

$$\text{dollar-share}_6^* = w_6^* / [w_6^* + \Sigma_{t \le 5} \, w_t^*]$$

Differentiating with respect to $\gamma_6$ and applying the quotient rule, after simplification:

$$\partial(\text{dollar-share}_6^*)/\partial\gamma_6 = - [\alpha_6 / (\gamma_6^2 \cdot (\delta_6 + r))] \cdot [\Sigma_{t \le 5} \, w_t^* / (\Sigma_t \, w_t^*)^2] < 0$$

since all terms inside the bracket are positive. The dollar-weighted Tier-6 share is monotonically decreasing in $\gamma_6$: as AI cheapens the surface tier ($\gamma_6$ falls), the optimal share at Tier 6 rises. The structural source of the sign is the large value of $\delta_6 = .50$ relative to the substrate-tier average $\delta_S = .119$: the relative-price reduction at Tier 6 is amplified by the high baseline rental rate at Tier 6, so the substitution toward Tier 6 dominates the income effect. QED.

*Proposition S1.2 (substrate-building threshold).* Under the generalized share rule with $\gamma_4 \le 1$ fixed, the partial derivative of the long-run Tier-4 stock with respect to $\Delta_4$ is positive:

$$\partial S_4^*/\partial\Delta_4 = \partial(w_4^* \cdot I / \delta_4^{\text{eff}})/\partial\Delta_4 > 0$$

*Proof.* Substitute $w_4^*(r; \gamma, \Delta) = \alpha_4 / [\gamma_4 \cdot (\delta_4^{\text{eff}} + r)]$ into $S_4^* = w_4^* \cdot I / \delta_4^{\text{eff}}$:

$$S_4^* = (\alpha_4 \cdot I) / [\gamma_4 \cdot \delta_4^{\text{eff}} \cdot (\delta_4^{\text{eff}} + r)]$$

Let $f(\delta_4^{\text{eff}}) = \delta_4^{\text{eff}} \cdot (\delta_4^{\text{eff}} + r) = (\delta_4^{\text{eff}})^2 + r \cdot \delta_4^{\text{eff}}$. Differentiating with respect to $\Delta_4$ (recalling $\delta_4^{\text{eff}} = \delta_4^0 - \Delta_4$):

$$\partial f/\partial\Delta_4 = (\partial f/\partial\delta_4^{\text{eff}}) \cdot (\partial\delta_4^{\text{eff}}/\partial\Delta_4) = - [2 \cdot \delta_4^{\text{eff}} + r] < 0$$

Hence $\partial S_4^*/\partial\Delta_4 = - (\alpha_4 \cdot I) \cdot [- (2 \cdot \delta_4^{\text{eff}} + r)] / [\gamma_4 \cdot f(\delta_4^{\text{eff}})^2] > 0$ since the numerator's effective sign is positive after the chain-rule cancellation, and the denominator is strictly positive. The long-run Tier-4 stock is monotonically increasing in $\Delta_4$, confirming the substrate-building threshold result. The discontinuity that A2 predicts is structural rather than algebraic: at $\Delta_4 = 0$ the AI deployment reduces to a $\gamma$-only cost shock with no substrate accumulation, and at $\Delta_4 > 0$ (proprietary fine-tune or owned-weights configuration) the substrate-building component becomes admissible. QED.

*Proposition S1.3 (joint-shock sign ambiguity).* When $\gamma_t$ and $\Delta_t$ move jointly at the same tier, the sign of the cross-partial $\partial^2 w_t^*/\partial\gamma_t\,\partial\Delta_t$ can be positive or negative depending on the magnitudes of the individual shocks.

*Proof sketch.* Differentiate $w_t^* = \alpha_t / [\gamma_t \cdot (\delta_t^{\text{eff}} + r)] = \alpha_t / [\gamma_t \cdot (\delta_t^0 - \Delta_t + r)]$ with respect to both $\gamma_t$ and $\Delta_t$:

$$\partial^2 w_t^*/\partial\gamma_t\,\partial\Delta_t = \alpha_t \cdot [\gamma_t \cdot \partial(\delta_t^{\text{eff}} + r)/\partial\Delta_t - (\delta_t^{\text{eff}} + r) \cdot \partial\gamma_t/\partial\Delta_t] / [\gamma_t^2 \cdot (\delta_t^{\text{eff}} + r)^2]$$

The expression depends on the joint movement pattern. Under a measurement model where empirical disclosure language correlates $\gamma_t$ and $\Delta_t$ (e.g., a 10-K passage describing "a proprietary fine-tune that has reduced our customer-service operating cost while building a defensible asset" reflects both $\gamma_5$ reduction and $\Delta_5$ increase), the cross-partial term carries opposing components and the sign is ambiguous in finite samples. This ambiguity motivates the §6 fall-back acknowledgment that clean separate identification of $\gamma_t$ versus $\Delta_t$ with public data may be infeasible and that joint identification of $(\gamma_t, \Delta_t)$ at the tier level may be the operational empirical specification. QED.

The three propositions S1.1, S1.2, and S1.3 together formalize the comparative-statics machinery that drives the body's Predictions A1, A2, and the §6/§9 fall-back acknowledgment, respectively. The remaining body predictions (A3 Tier-2 moat asymmetry, A4 penetration-depth ordering, A5 horizon-conditional sign flip, A6 rotation acceleration) follow from analogous derivations applied to the generalized share rule under tier-specific shock patterns; the derivations are verbal-formal in the body §5 and reproduce numerically in the companion script (S5).

---

## S2. CES robustness for the AI-extended share rule

The Cobb-Douglas ($\sigma = 1$) specification is maintained throughout the body. This section reports a constant-elasticity-of-substitution robustness check at $\sigma \in \{.5, 1.0, 1.5\}$ for the AI-extended share rule, parallel in structure to the 2026aj Online Supplement S4 robustness check for the inherited base model.

*Setup.* Replace the inner Cobb-Douglas aggregator with a CES aggregator of degree $\sigma$:

$$V_{LR}(w; r, \gamma, \Delta; \sigma) = A \cdot I \cdot [\Sigma_t \, \alpha_t \cdot (m_t \cdot w_t / (\delta_t^{\text{eff}} + r))^{(\sigma-1)/\sigma}]^{\sigma/(\sigma-1)}$$

The Cobb-Douglas case is recovered as $\sigma \to 1$ by L'Hôpital-style limit. The optimization problem is the same as in S1 — maximize $V_{LR}$ subject to the AI-extended budget constraint $\Sigma_t \, \gamma_t \cdot (\delta_t^{\text{eff}} + r) \cdot w_t = 1$ — and the FOC structure parallels S1 with the share rule generalizing to

$$w_t^*(r; \gamma, \Delta; \sigma) = K(\sigma) \cdot \frac{[\alpha_t \cdot (m_t / (\delta_t^{\text{eff}} + r))^{(\sigma-1)/\sigma}]^{\sigma}}{[\gamma_t \cdot (\delta_t^{\text{eff}} + r)]^{\sigma}}$$

where $K(\sigma)$ is the budget-normalization constant. The closed form of S1 ($\sigma = 1$) recovers under the limit and the central qualitative result extends.

*Tier-6 paradox at $\sigma \in \{.5, 1.0, 1.5\}$.* The companion script of S5 evaluates $\partial(\text{dollar-share}_6^*)/\partial\gamma_6$ at $\sigma \in \{.5, 1.0, 1.5\}$ under the calibration of A.2. The qualitative ordering — $\text{dollar-share}_6^*$ monotonically decreasing in $\gamma_6$ — survives at $\sigma = 1.0$ (the maintained Cobb-Douglas case) and at $\sigma = 1.5$ (the gross-substitutes case, where allocations across tiers become more responsive to relative-price changes). At $\sigma = .5$ (the gross-complements case, where allocations become less responsive), the sign of the comparative static can become ambiguous in two-tier reductions, paralleling the boundary-case finding in 2026aj Online Supplement S4. Numerical evaluation of the full five-tier model at $\sigma = .5$ with the calibrated parameters preserves the directional sign of A1 at the calibrated values but the magnitude attenuates by approximately 35% relative to $\sigma = 1.0$.

*B/A multiple ordering at $\sigma \in \{.5, 1.0, 1.5\}$.* Comparing two stylized firm profiles — Profile A (Tier-6-heavy, $w_6 = .70$) versus Profile B (Tier-4/5-heavy, $w_{4\text{-}5} = .65$) — the long-run value ratio $V_{LR}(B) / V_{LR}(A)$ is computed at each $\sigma$. The ratio is 1.93 at $\sigma = 1.0$ (the maintained Cobb-Douglas case from 2026aj), 2.17 at $\sigma = 1.5$ (gross substitutes), and 1.22 at $\sigma = .5$ (gross complements). The qualitative ordering $V_{LR}(B) > V_{LR}(A)$ — Tier-4/5-heavy beats Tier-6-heavy — survives all three elasticity values; the magnitude is sensitive to $\sigma$ but the direction is not.

*Tier-6 paradox under joint $\gamma_6$ and $\Delta_t$ shocks.* When AI deployment includes $\gamma_6 < 1$ at the surface tier and $\Delta_t > 0$ at deeper tiers (the configuration that distinguishes substrate-building deployments from surface-only deployments), the qualitative directional signs of A1 ($\partial(\text{dollar-share}_6^*)/\partial\gamma_6 < 0$) and A2 ($\partial S_4^*/\partial\Delta_4 > 0$) survive at $\sigma \in \{1.0, 1.5\}$. Under $\sigma = .5$, the two effects can partially cancel in the dollar-weighted share-rule decomposition, and the interpretation of the sign becomes a matter of whether the gross-complementary regime applies to the firm's specific tier-deployment configuration; the body maintains $\sigma = 1$ throughout and the CES robustness is reported as a parameter sensitivity rather than a structural claim about the firm's production technology.

*Practical implication.* The Cobb-Douglas maintained specification of §4 is a conservative middle-ground choice that preserves the framework's directional predictions in the gross-substitutes case (where the predictions are stronger than under Cobb-Douglas) and in the modal case $\sigma = 1.0$; the gross-complements case $\sigma = .5$ represents a boundary regime in which the framework's directional predictions hold only with attenuation. Empirical work that recovers $\sigma$ from firm-level production-function estimation can sharpen the prediction set; the framework's structural claims do not depend on $\sigma$ being recovered exactly.

---

## S3. Sensitivity to alternative $\alpha_t$ calibrations

The output-elasticity vector $\alpha_t$ enters the share rule directly: $w_t^* = \alpha_t / [\gamma_t \cdot (\delta_t^{\text{eff}} + r)]$. The body uses a baseline calibration $\alpha_6 = .12$, $\alpha_4 = \alpha_5 = .24$, $\alpha_2 = \alpha_3 = .20$ derived proportional to the M&A separability factors $m_t$. This section reports the sensitivity of the framework's headline predictions to two alternative calibrations. Supplement S3 was reconciled to companion-script outputs at v1.0.0; see `tier_penetration_simulation.py::alpha_calibration_sensitivity()` for the implementation.

*Scenario 1 — Baseline ($m_t$-proportional).* $\alpha_6 = .12$, $\alpha_4 = \alpha_5 = .24$, $\alpha_2 = \alpha_3 = .20$. The dollar-share at Tier 6 evaluated at $r = .15$, $\gamma_6 = .8$, all other $\gamma_t = 1$, all $\Delta_t = 0$ is .065. The B/A multiple ratio (Profile A Tier-6-heavy versus Profile B Tier-4/5-heavy at the same parameters) is 1.93. The Tier-6 paradox magnitude — $\partial(\text{dollar-share}_6^*)/\partial\gamma_6$ — is .076 at $\gamma_6 = .8$ evaluation point.

*Scenario 2 — Conservative (uniform).* $\alpha_t = .20$ for all $t$. The dollar-share at Tier 6 at the same evaluation point is .112. The B/A multiple ratio attenuates to 1.55 because the elasticity at Tier 6 rises to .20 from .12, increasing the surface tier's contribution to total value. The Tier-6 paradox magnitude rises to .124.

*Scenario 3 — Concentrated-stock.* $\alpha_6 = .05$, $\alpha_4 = \alpha_5 = .30$, $\alpha_2 = \alpha_3 = .175$. The dollar-share at Tier 6 falls to .027 because the surface-tier elasticity is sharply reduced; the substrate tiers (especially Tier-4 and Tier-5) absorb a larger share of the planner's optimal allocation. The B/A multiple ratio rises to 2.39 because the concentrated-stock calibration places higher elasticity on the substrate tiers and the Tier-4/5-heavy Profile B exploits the calibration's weighting more efficiently. The Tier-6 paradox magnitude is .033 at $\gamma_6 = .8$.

*Cross-scenario invariants.* The directional sign of the Tier-6 paradox — $\partial(\text{dollar-share}_6^*)/\partial\gamma_6 < 0$ — holds across all three calibrations. The B/A multiple ranges from 1.55 (conservative) to 2.39 (concentrated), a 1.54× spread driven by the relative weighting of Tier-6 versus substrate-tier elasticities. The framework's directional prediction A1 is robust to $\alpha_t$ mis-calibration; the magnitude of the predicted M&A-multiple effect is sensitive and should be re-estimated alongside any panel that recovers $\alpha_t$ from firm-level data.

The three-scenario sensitivity check parallels the analogous exercise in 2026aj's calibration appendix and confirms that the framework's structural claims do not depend on the specific $\alpha_t$ calibration; they depend on the architectural-structural ordering $m_6 < m_2 = m_3 < m_4 = m_5$, which the calibration preserves across the three scenarios.

---

## S4. Identification Strategy and Empirical Test Design

This section develops the full identification strategy for testing Propositions P1-P3, including the tier-assignment protocol, disclosure-coding pilot design, and the complete five-threat threats-to-identification table. The body's "Implications for Empirical Testing" section sketches these elements qualitatively; this section provides the operational detail needed to implement the empirical follow-on. The material is positioned here rather than in the body because the paper's primary contribution is deductive theory; empirical test design is a roadmap for a future companion empirical paper.

*Tier-assignment protocol.* The unit of tier assignment is the AI-deployment artifact, not the project. A single project commonly produces multiple artifacts at different tiers; treating the project as the assignment unit collapses the architectural decomposition the framework requires. Each artifact is assigned by asking: where does the durable artifact reside in the six-tier stack? The four boundary-object cases illustrate per-artifact decomposition. Klarna's chatbot deployment produces a transient Tier-6 customer interaction, a Tier-5 chatbot configuration, and a Tier-3 disclosure footprint; Spotify's recommendation system produces a Tier-6 served recommendation, a Tier-2 user-behavior model (the data flywheel), and a Tier-4 platform specification; BloombergGPT produces a Tier-5 fine-tune and Tier-4 terminal-embedded outputs; Stripe Radar produces a Tier-2 fraud-decisioning AI and a Tier-6 merchant-facing output.

*Disclosure-coding pilot design.* The pilot hand-codes 100 AI-related disclosures from a stratified S&P 1500 sample across the 2023-2026 window. Target inter-rater reliability is Cohen's kappa $\ge .65$ for tier assignment, following Krippendorff (2004) content-analysis methodology and matching the .60-.75 range Hassan, Hollander, van Lent, and Tahoun (2019) achieve on analogous text-based political-risk topic classification. Two independent coders, third-coder adjudication, both pairwise and three-way kappas reported. The pilot also validates tier-depth scores against Babina, Fedyk, He, and Hodson (2024) aggregate AI-investment measures via two pre-committed correlation tests (sum-correlation $\ge .40$; per-tier collinearity $\le .85$). A BERT-based or LLM-classifier robustness check is pre-committed.

*Disclosure-coding dictionary exemplars.* Tier-6 positive exemplars: "generative marketing copy," "AI customer-service chatbot," "programmatic-bidding optimization." Tier-5 positive exemplars: "proprietary fine-tune," "owned model weights," "AI workflow automation agent." Tier-4 positive exemplars: "AI-as-product," "embedding-context switching cost," "AI-codified product specification." Tier-2 positive exemplars: "data flywheel," "recommendation engine constitutive of product," "AI fraud-decisioning." Tier-3 positive exemplars: "AI contract drafting," "AI compliance monitoring." Tier-1: smaller dictionary; hard ceilings make positive exemplars rare in current disclosure data. Negative exemplars (artifacts that look like tier indicators but are not): generic mentions of "AI strategy," "evaluating AI vendors," "AI pilot program" (unassigned); "AI-powered analytics dashboard" (requires artifact-level decomposition).

*Threats-to-identification table (full).* The body §6 sketches three first-order threats. This section expands each into prose discussion across four columns — severity, proposed mitigation, residual risk, and robustness checks — and adds two further threats (measurement error in the tier-depth disclosure measure; attrition due to acquisition during the panel).

*Threat 1: Selection on unobservables.* Severity HIGH. Firms that were ready for Tier-4 AI deployment in 2022, at the GPT-3-to-GPT-4 transition, were systematically firms with superior pre-existing data infrastructure, specification-quality discipline, and ML-engineering capacity. The pre-existing infrastructure differential is correlated with subsequent firm-level outcomes through channels other than the AI deployment itself, so naive cross-sectional comparisons of Tier-4 deployers versus non-deployers conflate the deployment effect with the selection effect. *Proposed mitigations:* (a) pre-trends test on intangible-intensity series prior to the AI-deployment event, demonstrating that pre-treatment firm-level outcomes do not differ between deployers and non-deployers; (b) firm fixed effects in the difference-in-differences specification, absorbing time-invariant firm-level heterogeneity; (c) entropy-balancing or Coarsened Exact Matching on observable pre-shock characteristics — size, intangible intensity, prior R&D spend, sector AIOE per Felten, Raj, and Seamans (2021), and pre-treatment earnings-call AI-mention frequency. *Residual risk:* time-varying unobservables remain — firms whose data infrastructure was improving at the moment of AI deployment cannot be matched on the time-varying improvement, and the residual selection-on-time-varying-unobservables cannot be eliminated by the proposed mitigations. *Robustness checks:* (a) Oster (2019) bounding-the-effect-of-unobservables coefficient-stability test; (b) sub-sample analysis restricted to firms with ex-ante similar data-infrastructure scores constructed from prior-year disclosure language.

*Threat 2: Parallel-trends violation.* Severity MEDIUM. The GPT-3 → GPT-4 → GPT-5 capability-frontier shocks are common shocks correlated with broader tech-sector time trends, so the difference-in-differences identification assumption that treated and control firms would have followed parallel trends absent treatment is contestable in any tech-sector-heavy panel. *Proposed mitigations:* (a) pre-trends test on intangible-intensity series demonstrating parallel pre-treatment trajectories; (b) placebo difference-in-differences on capital-light service-sector firms (legal services, accounting, financial services excluding fintech) where Tier-4 AI deployment is implausible at the relevant horizon, providing a parallel-trends placebo; (c) sector-by-time fixed effects to absorb common sector-time shocks; (d) Callaway and Sant'Anna (2021) staggered-adoption difference-in-differences estimator if treatment timing is heterogeneous across firms. *Residual risk:* heterogeneous treatment effects within the tech sector remain — firms with different pre-existing AI exposure may respond differentially to the same capability-frontier shock, and the heterogeneous-treatment-effect bias cannot be eliminated by the proposed mitigations. *Robustness checks:* (a) De Chaisemartin and D'Haultfœuille (2020) bounds on heterogeneous treatment effects; (b) leave-one-out sub-sample analysis to assess whether estimates are driven by specific tech-sector sub-industries.

*Threat 3: Founder-horizon endogeneity.* Severity MEDIUM. Founder-CEO status, family-firm governance structure, and ownership concentration are themselves outcomes of past performance and past strategic decisions, so the founder-horizon proxies that A5 requires for its sign-flip test are endogenous to the firm-value outcomes the framework attempts to explain. *Proposed mitigations:* (a) gender-of-first-born instrument from Bennedsen, Nielsen, Pérez-González, and Wolfenzon (2007) for family-firm horizon, exploiting the documented relationship between first-born-child characteristics and family-firm CEO succession; (b) CEO-founder tenure interacted with industry-shock indicators to identify within-firm variation in effective horizon; (c) institutional-concentration measures as alternative horizon proxies that are at least partially exogenous to firm-level performance. *Residual risk:* instrument validity is contestable in the post-2010 governance environment — the first-born-gender instrument has weakened in predictive power over time as gender-neutral succession norms have spread, and the residual instrument-validity uncertainty cannot be eliminated. *Robustness checks:* (a) overidentification test combining the Bennedsen et al. (2007) instrument with the alternative founder-tenure-by-industry-shock instrument; (b) sub-sample analysis restricted to family firms with first-born children of identifiable gender pre-2000.

*Threat 4: Measurement error in the tier-depth disclosure measure.* Severity LOW-MEDIUM. The tier-depth measure is constructed from text-based dictionary-coding of 10-K Item 1A, Item 7, and earnings-call transcript language, following the Hassan, Hollander, van Lent, and Tahoun (2019) text-based political-risk measurement template. Classical measurement error attenuates regression coefficients toward zero. *Proposed mitigations:* (a) inter-rater reliability check at the pilot stage with target Cohen's kappa $\ge .65$ per Krippendorff (2004); (b) BERT-based or LLM-classifier validation pass against the human-coded sample with agreement-rate reported as secondary validation; (c) split-sample replication. *Residual risk:* non-classical measurement error — tier-depth measures may be more accurately coded for firms with verbose disclosure language than for firms with concise disclosure language, and the disclosure-verbosity correlation with firm size is a confounder. *Robustness checks:* (a) firm-size sub-sample stratification; (b) controls for total disclosure length in the regression specification.

*Threat 5: Attrition due to acquisition during the panel.* Severity LOW-MEDIUM. The framework's empirical predictions concern M&A-multiple effects, but observation of M&A multiples requires that firms in the panel are acquired (or remain on the market in a way that allows multiple computation). Firms that become target firms during the panel are non-randomly selected — they are systematically more likely to be successful Tier-4 deployers or systematically less likely to be Tier-6-only deployers. *Proposed mitigations:* (a) Heckman (1979) two-stage selection-correction model with the first stage modeling the probability of acquisition; (b) sub-sample analysis restricted to acquired firms with an explicit selection-correction adjustment; (c) inverse-probability weighting on the propensity-to-be-acquired score. *Residual risk:* the exclusion restriction in Heckman correction is contestable — instruments that affect acquisition probability without affecting M&A multiple conditional on acquisition are scarce. *Robustness checks:* (a) bound-the-treatment-effect approach following Lee (2009); (b) sensitivity analysis to the exclusion-restriction assumption.

The full threats-to-identification structure makes explicit that even under the cleanest mitigation set, residual identification challenges remain — particularly time-varying unobservables and instrument-validity contestability. The framework's empirical implementation should be positioned as a validation roadmap that progressively narrows the identified effect rather than as a single test that delivers the framework's predictions in one regression specification. The §6 fall-back to deductive theory plus calibrated comparative-statics simulation, in which the body §6 explicitly acknowledges that the empirical implementation may settle for joint identification of $(\gamma_t, \Delta_t)$ at the tier level rather than separate identification of each parameter, is the methodological end-point at which the framework remains testable even when full panel identification is infeasible.

---

## S5. Companion script docstring, run command, and parameter table

This section documents the companion computation script that reproduces every numerical value reported in the main paper and this supplement.

*Script location.* `tier_penetration_simulation.py`, published at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-penetration/code/tier_penetration_simulation.py.

*Run command.* `uv run python tier_penetration_simulation.py`

*Python version and dependencies.* Python $\ge$ 3.10. Required packages: numpy $\ge$ 1.24, scipy $\ge$ 1.10. No plotting dependencies (the parent paper has no figures; tabular output to stdout). Random seed: numpy.random.seed(42) set at module load for structural consistency with the corpus pattern; the script is fully deterministic and uses no stochastic operations.

*Function inventory.*

`effective_delta(delta_0, Delta)` — returns $\delta_t^{\text{eff}} = \delta_t^0 - \Delta_t$ with assertion $\Delta_t < \delta_t^0$. Inputs: delta_0 is a dict mapping tier to baseline decay rate; Delta is a dict mapping tier to durability shock. Returns: dict mapping tier to effective decay rate.

`share_rule(alpha, delta_eff, gamma, r)` — returns the un-normalized $w_t^*$ vector under the generalized AI-extended share rule $w_t^* = \alpha_t / [\gamma_t \cdot (\delta_t^{\text{eff}} + r)]$. Inputs: alpha is a dict of $\alpha_t$ values (default the baseline calibration $\alpha_6 = .12$, $\alpha_4 = \alpha_5 = .24$, $\alpha_2 = \alpha_3 = .20$); delta_eff is a dict of $\delta_t^{\text{eff}}$ values; gamma is a dict of $\gamma_t$ values (default all $\gamma_t = 1.0$ corresponding to no AI shock); r is the principal's effective discount rate (default $r = .15$). Returns: dict mapping tier to un-normalized rental-share value.

`dollar_shares(w_star)` — normalizes the un-normalized share dict to dollar-weighted shares summing to 1. Returns: dict mapping tier to dollar-weighted share.

`proposition_1_tier6_paradox()` — replicates body §5 Proposition 1 by sweeping $\gamma_6 \in \{.5, .7, .9, 1.0\}$ under the baseline calibration and reporting the sign of $\partial(\text{dollar-share}_6^*)/\partial\gamma_6$ at each point. Returns: dict with keys "gamma_6_grid", "dollar_share_6", "paradox_magnitude", "sign".

`proposition_2_tier4_threshold()` — replicates body §5 Proposition 2 by computing the Tier-4 stock $S_4^*$ across the $\Delta_4 = 0$ vs $\Delta_4 > 0$ threshold, demonstrating the level-shift interpretation. Returns: dict with keys "delta_4_eff_grid", "S_4_star", "level_shift_at_threshold".

`proposition_3_horizon_flip()` — replicates body §5 Proposition 3 by computing $\text{dollar-share}_6^*(r)$ across $r \in \{.10, .15, .20\}$ under the maintained Cobb-Douglas ($\sigma = 1$) and demonstrating $\partial w_6^*/\partial r > 0$. Returns: dict with keys "r_grid", "dollar_share_6", "sign", "scope_condition".

`ces_robustness(sigma_values=[.5, 1.0, 1.5])` — replicates Online Supplement S2 by evaluating the Tier-6 paradox sign and the Profile B / Profile A multiple ratio at each $\sigma \in$ sigma_values. Returns: dict with keys "sigma", "tier6_paradox_sign", "B_over_A_multiple", "tier6_paradox_magnitude_at_gamma_6_eq_pt8".

`alpha_calibration_sensitivity()` — replicates Online Supplement S3 under three scenarios ($m_t$-proportional baseline, conservative-uniform, concentrated-stock); reports $\text{dollar-share}_6^*$, B/A multiple ratio, and Tier-6 paradox magnitude per scenario. Returns: dict mapping scenario name to result dict.

`boundary_object_cases()` — replicates body §6 by computing the implied $(\gamma_t, \Delta_t)$ vector and the long-run M&A-multiple direction for each of the four illustrative cases (Klarna, Spotify, BloombergGPT, Stripe Radar). Returns: list of BoundaryCase namedtuples.

`main()` — top-level driver invoked by the run command `uv run python tier_penetration_simulation.py`. Calls each of the eight simulation functions above in sequence, prints structured tabular output with section headers, and runs the verification check that script-computed values match the paper-stated values reconciled at v1.0.0.

*Parameter table.* The script's hard-coded baseline calibration is:

| Parameter | Value | Source |
|---|---|---|
| $\alpha_6$ | .12 | Appendix A.3 ($m_t$-proportional) |
| $\alpha_4 = \alpha_5$ | .24 | Appendix A.3 |
| $\alpha_2 = \alpha_3$ | .20 | Appendix A.3 |
| $m_6$ | .25 | Appendix A.1 |
| $m_4 = m_5$ | 1.0 | Appendix A.1 |
| $m_2 = m_3$ | .6 | Appendix A.1 |
| $\delta_6$ | .50 | Belo, Lin, and Vitorino (2014) |
| $\delta_5$ | .175 | Eisfeldt and Papanikolaou (2013); Corrado, Hulten, and Sichel (2009) |
| $\delta_4$ | .15 | Lev and Sougiannis (1996); Hall, Jaffe, and Trajtenberg (2005) |
| $\delta_2 = \delta_3$ | .075 | Wiggins and Ruefli (2002) extrapolation |
| $r$ (default) | .15 | Principal's effective discount rate; sensitivity analysis at $r \in \{.10, .15, .20\}$ |
| $\gamma_t$ (default no-shock) | 1.0 | Pre-AI baseline |
| $\Delta_t$ (default no-shock) | 0 | Pre-AI baseline |
| Random seed | 42 | numpy.random.seed |

*Reproducibility statement.* Every numerical value in the body and in this supplement that is not directly traceable to an external published source is reproducible from `tier_penetration_simulation.py` under the run command above. The script has no external data dependencies — all calibrated parameters are hard-coded — and produces deterministic output across runs. The script will be published at the public mirror at the URL above once Zenodo upload completes.

---

*End of Online Supplement.*
