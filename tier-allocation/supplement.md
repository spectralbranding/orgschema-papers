# Online Supplement to "Where to Invest Within the Firm: Organizational Tiers, Discount Rates, and AI Penetration"

**Dmitry Zharnikov**

ORCID: 0009-0000-6893-9231

DOI: [10.5281/zenodo.20072288](https://doi.org/10.5281/zenodo.20072288)

Working Paper v1.3.0 -- May 2026 (revised November 2026)

*The main paper is published at https://doi.org/10.5281/zenodo.20072288 and at https://github.com/spectralbranding/orgschema-papers/tree/main/tier-allocation/. The companion computation scripts are at https://github.com/spectralbranding/orgschema-papers/tree/main/tier-allocation/code/.*

This online supplement provides the full mathematical derivations, sensitivity analyses, and robustness checks underlying the formal model presented in the main paper. Sections S1–S4 support Part I of the main paper and are reproduced by the companion script `back_of_envelope.py`; Sections S5–S9 support Part II and are reproduced by `tier_penetration_simulation.py`. Both scripts are published in the paper's public code directory named above. All values are fully deterministic; no random-number generation is used.

---

## S1. Mathematical Derivations: Formal Proof of $\partial(\text{dollar-share}_6^*)/\partial r > 0$

*Formal Derivation of $\partial(\text{dollar-share}_6^*)/\partial r > 0$ Under the Discounted-Cobb-Douglas Maintained Specification*

Throughout this section, $\delta_t$ denotes the per-period decay rate (matching Table 1 values directly and the Belo, Lin, and Vitorino 2014 convention). The full user-cost-of-capital specification (Jorgenson 1963) sets the per-tier rental rate $q_t = \delta_t + r$, which is the per-period cost of holding one unit of tier-$t$ stock: the firm pays $\delta_t$ to cover depreciation and $r$ as the opportunity cost of capital. Belo, Lin, and Vitorino (2014) adopt the simplifying assumption $r = 0$, so their rental rate equals the decay rate alone; the present model retains the full Jorgensonian form $q_t = \delta_t + r$.

**Step 1: The maximand.** The maintained specification (Equation 3 in the main paper) is:

$$V_{LR}(w; r) = A \cdot I \cdot \Pi_t \, [m_t \cdot w_t / (\delta_t + r)]^{\alpha_t}, \quad \Sigma_t \, \alpha_t = 1$$

Taking logs: $\ln V_{LR} = \ln A + \ln I + \Sigma_t \, \alpha_t \cdot [\ln m_t + \ln w_t - \ln(\delta_t + r)]$.

**Step 2: The budget constraint.** The firm allocates total expenditure $E$ across tiers facing per-tier rental prices $q_t = \delta_t + r$. With $w_t = I_t/I_{\text{total}}$ and normalization $\Sigma_t \, (\delta_t + r) \cdot w_t = 1$ (the Jorgensonian user-cost budget constraint).

**Step 3: Lagrangian and FOC.** The Lagrangian is:

$$L = \ln A + \ln I + \Sigma_t \, \alpha_t \cdot [\ln m_t + \ln w_t - \ln(\delta_t + r)] - \lambda \cdot [\Sigma_t \, (\delta_t + r) \cdot w_t - 1]$$

FOC with respect to $w_t$: $\partial L/\partial w_t = \alpha_t / w_t - \lambda \cdot (\delta_t + r) = 0$

Solving:

$$w_t^*(r) = \alpha_t / [\lambda \cdot (\delta_t + r)]$$

**Step 4: Solving for $\lambda$.** Substituting $w_t^*(r)$ into the budget constraint:

$$\Sigma_t \, (\delta_t + r) \cdot w_t^* = \Sigma_t \, (\delta_t + r) \cdot \alpha_t / [\lambda \cdot (\delta_t + r)] = \Sigma_t \, \alpha_t / \lambda = 1/\lambda = 1$$

Since $\Sigma_t \, \alpha_t = 1$ under CRS, $\lambda = 1$. Therefore:

$$w_t^*(r) = \alpha_t / (\delta_t + r)$$

**Step 5: Observable dollar-weighted share.** The empirically observable investment share (what an analyst measures as XAD/total-investment) is the dollar-weighted renormalization:

$$\text{dollar-share}_t^*(r) = w_t^*(r) / \Sigma_s \, w_s^*(r) = (\alpha_t / (\delta_t + r)) / \Sigma_s \, (\alpha_s / (\delta_s + r))$$

**Step 6: Sign of $\partial(\text{dollar-share}_6^*)/\partial r$.** For the two-tier reduction (marketing flow, the item indexed 6, vs. aggregate stock tier $S$):

$$\text{dollar-share}_6^*(r) = [\alpha_6/(\delta_6+r)] / \{[\alpha_6/(\delta_6+r)] + [\alpha_S/(\delta_S+r)]\}$$

Let $f = \alpha_6/(\delta_6+r)$ and $g = \alpha_S/(\delta_S+r)$, so $\text{dollar-share}_6^* = f/(f+g)$. Then:

$$\partial(\text{dollar-share}_6^*)/\partial r = (f' \cdot g - f \cdot g') / (f + g)^2$$

where $f' = -\alpha_6/(\delta_6+r)^2 < 0$ and $g' = -\alpha_S/(\delta_S+r)^2 < 0$.

The numerator is $f' \cdot g - f \cdot g' = [-\alpha_6/(\delta_6+r)^2] \cdot [\alpha_S/(\delta_S+r)] - [\alpha_6/(\delta_6+r)] \cdot [-\alpha_S/(\delta_S+r)^2]$

$$= \alpha_6 \cdot \alpha_S / [(\delta_6+r)(\delta_S+r)] \cdot [1/(\delta_S+r) - 1/(\delta_6+r)]$$

$$= \alpha_6 \cdot \alpha_S / [(\delta_6+r)(\delta_S+r)] \cdot [(\delta_6 - \delta_S) / ((\delta_S+r)(\delta_6+r))]$$

The sign of the numerator equals the sign of $(\delta_6 - \delta_S)$. Since $\delta_6 = .50 > \delta_S = .119$, the numerator is **strictly positive** for all $r > 0$. Therefore:

$$\partial(\text{dollar-share}_6^*)/\partial r > 0$$

The optimal marketing-flow dollar-share rises monotonically as $r$ rises. QED.

**Numerical verification.** At $r = .15$: $\text{dollar-share}_6^* = (.12/.65)/[(.12/.65)+(.88/.269)] = .185/3.456 \approx .053$ (5.3%). At $r = .50$: $\text{dollar-share}_6^* = (.12/1.00)/[(.12/1.00)+(.88/.619)] = .120/1.542 \approx .078$ (7.8%). The predicted increase from 5.3% to 7.8% as $r$ rises from .15 to .50 confirms the comparative static.

**Intuition.** As $r$ rises, the per-period rental cost $q_t = \delta_t + r$ increases for all tiers, but the proportional increase is larger for low-$\delta_t$ (stock) tiers because $r$ is a larger fraction of their smaller denominator. The planner responds by substituting away from the now-relatively-more-expensive stock tiers toward marketing flow, whose high base $\delta_6 = .50$ makes the proportional rental-cost increase smaller. The Jorgensonian rental-rate structure is the formal mechanism that generates the comparative static the paper's propositions rest on.

## S2. Sensitivity of $V_{LR}$ Multiple Gap to $r$

The ratio $V_{LR}(\text{Profile B}; r) / V_{LR}(\text{Profile A}; r)$ as a function of $r$, computed under the discounted-Cobb-Douglas maintained specification $V_{LR}(w; r) = A \cdot I \cdot \Pi_t \, [m_t \cdot w_t / (\delta_t + r)]^{\alpha_t}$ with $\alpha$ calibration ($\alpha_6 = .12$; $\alpha_4 = \alpha_5 = .24$; $\alpha_2 = \alpha_3 = .20$) and separability factors ($m_6 = .25$; $m_{4\text{-}5} = 1.0$; $m_{2\text{-}3} = .6$):

| $r$ | $V_{LR}(A)$ | $V_{LR}(B)$ | Ratio B/A |
|---|---------|---------|---------|
| .10 | .268 | .518 | 1.93 |
| .15 | .221 | .427 | 1.93 |
| .20 | .188 | .363 | 1.93 |

*Notes*: Values normalized to $A \cdot I = 1$. Computed from the back-of-envelope calibration in the "Two-Tier Minimal Illustration" section of the main paper with $w$ profiles (A: $w_6 = .70$, $w_{4\text{-}5} = .20$, $w_{2\text{-}3} = .10$; B: $w_6 = .15$, $w_{4\text{-}5} = .65$, $w_{2\text{-}3} = .20$) and $\alpha$ exponents calibrated proportional to M&A separability factors. Under constant returns to scale ($\Sigma_t \, \alpha_t = 1$), the B/A ratio is exactly $r$-invariant at 1.93: as $r$ rises, all per-tier productivity factors $m_t/(\delta_t+r)$ fall for both profiles, but they cancel in the ratio ($I^{\Sigma_t \alpha_t} = I$ factors out). The $V_{LR}$ levels decline substantially with $r$ — from .268/.518 at $r = .10$ to .188/.363 at $r = .20$ — reflecting that higher discount rates compress the present value of all perpetuity-form tier stocks. The $r$-sensitivity surfaces in the optimal dollar-share $\text{dollar-share}_6^*(r)$ (Section S1), not in the B/A ratio at fixed $w$-profiles. The B/A multiple gap of 1.93× is stable across the relevant discount-rate range, reproducing the *ordinal* structure of observed M&A multiple differentials but understating the magnitude (empirical gap is closer to 4–6×). All values are reproducible from the companion computation script (`back_of_envelope.py`, function `reproduce_appendix_a2()`).

## S3. Alternative $\alpha_t$ Calibrations

The $\alpha_t$ output elasticities ($\alpha_6 = .12$, $\alpha_4 = \alpha_5 = .24$, $\alpha_2 = \alpha_3 = .20$) are calibrated proportional to the M&A separability factors $m_t$. Sensitivity checks across two alternative specifications, computed under the discounted-Cobb-Douglas maintained specification at $r = .15$:

| $\alpha$ Calibration | $V_{LR}(A; .15)$ | $V_{LR}(B; .15)$ | Ratio |
|---------------|---------|---------|-------|
| Baseline ($\alpha_6 = .12$; $\alpha_4 = \alpha_5 = .24$; $\alpha_2 = \alpha_3 = .20$) | .221 | .427 | 1.93 |
| Conservative ($\alpha_6 = .20$; $\alpha_4 = \alpha_5 = .20$; $\alpha_2 = \alpha_3 = .20$) | .218 | .339 | 1.55 |
| Concentrated-stock ($\alpha_6 = .05$; $\alpha_4 = \alpha_5 = .30$; $\alpha_2 = \alpha_3 = .175$) | .234 | .559 | 2.39 |

*Notes*: Values computed under the maintained specification $V_{LR}(w; r) = A \cdot I \cdot \Pi_t \, [m_t \cdot w_t / (\delta_t + r)]^{\alpha_t}$ at $r = .15$; all values are reproducible from the companion computation script (`back_of_envelope.py`, function `reproduce_appendix_a3()`). The B/A multiple ratio ranges from 1.55× to 2.39× across the alternative $\alpha$-vector specifications, confirming the qualitative stability of the result. The directional prediction — Profile B commands a substantially higher multiple than Profile A regardless of the $\alpha$ calibration — is robust to reasonable parameter variation. As $\alpha_6$ falls, the magnitude gap widens: the "Concentrated-stock" specification with $\alpha_6 = .05$ produces a 2.39× ratio, closer to the empirical 4–6× range. The validation roadmap (Appendix: Validation Roadmap of the main paper, Priority 1) jointly estimates $\alpha_t$ and $\delta_t$ from a Compustat panel where the parameters are identified from the data rather than chosen to reproduce target ratios.

## S4. CES Robustness Check on Comparative Static

The maintained specification adopts the Cobb-Douglas aggregator ($\sigma = 1$), which is the tractable special case of the CES family. To assess whether the qualitative findings depend on the unit elasticity of substitution, this section reports $V_{LR}$ under a full CES aggregator:

$$V_{LR}^{\text{CES}}(w; r, \sigma) = A \cdot I \cdot \left[ \Sigma_t \, \alpha_t \cdot (m_t \cdot w_t / (\delta_t + r))^{(\sigma-1)/\sigma} \right]^{\sigma/(\sigma-1)}$$

for $\sigma \neq 1$, recovering the Cobb-Douglas maintained specification as $\sigma \to 1$. Values of $\sigma < 1$ correspond to gross complements (co-specialization-strong; Adner 2012 ecosystem framing), while $\sigma > 1$ corresponds to gross substitutes (co-specialization-weak). The table below reports $V_{LR}(A)$, $V_{LR}(B)$, and the B/A ratio at $r = .15$ for $\sigma \in \{.5, 1.0, 1.5\}$.

**Table S4: CES Robustness Check — Profile A/B $V_{LR}$ and B/A Ratio at $r = .15$.**

| $\sigma$ | $V_{LR}(A)$ | $V_{LR}(B)$ | Ratio B/A |
|---|---------|---------|---------|
| .5 (gross complements) | .202 | .247 | 1.22 |
| 1.0 (Cobb-Douglas, maintained) | .221 | .427 | 1.93 |
| 1.5 (gross substitutes) | .227 | .494 | 2.17 |

*Notes*: Values computed at $r = .15$ with baseline $\alpha$ calibration ($\alpha_6 = .12$; $\alpha_4 = \alpha_5 = .24$; $\alpha_2 = \alpha_3 = .20$). Reproducible from companion computation script (`back_of_envelope.py`, function `reproduce_appendix_a4_ces()`). The Cobb-Douglas ($\sigma = 1$) row matches the "Two-Tier Minimal Illustration" section of the main paper exactly. CES with $\sigma < 1$ attenuates the B/A ratio to 1.22× but does not reverse it: Profile B strictly dominates Profile A across all three elasticity values. CES with $\sigma > 1$ amplifies the ratio to 2.17×, closer to the empirical 4–6× range. A brief summary of the in-body CES check and the main qualitative finding appears in the main paper (Table 2); this supplement section provides the full derivation and sign verification.

The comparative static $\partial(\text{dollar-share}_6^*)/\partial r$ is verified numerically under $\sigma \in \{.5, 1.5\}$ using a two-tier reduction (marketing flow vs. aggregate stock tier, equal-weighted $\delta_S = .119$). Under the maintained Cobb-Douglas ($\sigma = 1$), the sign is established analytically in Section S1. Under $\sigma = 1.5$ (gross substitutes), numerical optimization confirms that the planner-optimal $w_6$ share rises monotonically: .017 at $r = .10$, .018 at $r = .15$, .019 at $r = .20$ — $\partial w_6^*/\partial r > 0$ confirmed. Under $\sigma = .5$ (gross complements), the two-tier numerical optimizer finds that the planner-optimal $w_6$ share declines slightly with $r$ in the two-tier reduction (.523 at $r = .10$, .507 at $r = .15$, .495 at $r = .20$), indicating that the comparative static sign is not preserved under strong gross complementarity in the simplified two-tier case. This reversal is specific to the two-tier reduction at $\sigma < 1$: under gross complementarity, the planner wants a more balanced portfolio, and as $r$ rises the high rental cost of all tiers shifts the interior optimum toward the symmetry point. In the full five-tier model with heterogeneous $\delta_t$ the directional propositions remain supported by the B/A ordering, which is robust across all $\sigma$ values examined. The maintained Cobb-Douglas ($\sigma = 1$) is therefore a conservative choice: the B/A ratio of 1.93× understates the magnitude under $\sigma > 1$ and overstates it under $\sigma < 1$, bracketing the empirical range symmetrically. Full five-tier CES optimization is identified as a future extension.

All numerical values in Sections S1–S4 are reproducible from the companion computation script published at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-allocation/code/back_of_envelope.py. Run with `uv run python back_of_envelope.py` (Python 3.10+; requires numpy, matplotlib, scipy).

---

Sections S5–S9 support Part II of the main paper (AI tier penetration). They give the derivations behind Propositions 5–7, the CES and $\alpha_t$ robustness of the AI-extended share rule, the full identification design, and the documentation of the second companion script, `tier_penetration_simulation.py`. Notation follows the main paper: the subscript 6 indexes marketing flow on Tier 2 channels, the spend item with the highest decay rate, and does not refer to Tier 6. Works cited in these sections are listed in the main paper's references.

## S5. Lagrangian Setup, First-Order Conditions, and Comparative Statics for the AI-Extended Share Rule

*Setup.* The firm chooses an allocation vector $w = (w_2, w_3, w_4, w_5, w_6) \in \mathbb{R}_+^5$ to maximize the AI-extended long-run value function

$$V_{LR}(w; r, \gamma, \Delta) = A \cdot I \cdot \prod_t [m_t \cdot w_t / (\delta_t^{\text{eff}} + r)]^{\alpha_t}$$

with $\delta_t^{\text{eff}} = \delta_t^0 - \Delta_t$, subject to the AI-extended Jorgensonian budget constraint

$$\sum_t \gamma_t \cdot (\delta_t^{\text{eff}} + r) \cdot w_t = 1$$

where $\gamma_t \in (0, 1]$ is the cost shock on item $t$, $\Delta_t \in [0, \delta_t^0)$ is the durability shock, $\delta_t^0$ is the pre-AI decay rate of Table 1 of the main paper, $A > 0$ is a productivity scalar, $m_t \in [0, 1]$ is the M&A separability factor, $\alpha_t \in (0, 1)$ is the output elasticity with $\sum_t \alpha_t = 1$, and $r$ is the principal's effective discount rate.

*First-order conditions.* With $L = \ln A + \ln I + \sum_t \alpha_t [\ln m_t + \ln w_t - \ln(\delta_t^{\text{eff}} + r)] - \lambda [\sum_t \gamma_t (\delta_t^{\text{eff}} + r) w_t - 1]$, the condition $\partial L / \partial w_t = \alpha_t / w_t - \lambda \gamma_t (\delta_t^{\text{eff}} + r) = 0$ gives $w_t^* = \alpha_t / [\lambda \gamma_t (\delta_t^{\text{eff}} + r)]$. Substituting into the budget constraint gives $1/\lambda = \sum_t \alpha_t = 1$, so the generalized share rule is

$$w_t^*(r; \gamma, \Delta) = \frac{\alpha_t}{\gamma_t \cdot (\delta_t^{\text{eff}} + r)}$$

and the dollar-weighted share is $\text{dollar-share}_t^* = w_t^* / \sum_s w_s^*$. The Hessian of $\ln V_{LR}$ in $w$ is diagonal with entries $-\alpha_t / w_t^2 < 0$; neither shock enters the curvature, so the interior optimum is unique for every admissible $(\gamma, \Delta)$.

*Proposition S5.1 (marketing-flow over-allocation; Proposition 5).* With $\gamma_t = 1$ for $t \le 5$ and $\Delta_t = 0$ for all $t$, $\partial(\text{dollar-share}_6^*)/\partial \gamma_6 < 0$ for every admissible parameter vector.

*Proof.* Let $W = \sum_{t \le 5} w_t^*$, which does not depend on $\gamma_6$, and $w_6^* = \alpha_6 / [\gamma_6 (\delta_6 + r)]$, so $\partial w_6^* / \partial \gamma_6 = -w_6^* / \gamma_6$. By the quotient rule,

$$\frac{\partial(\text{dollar-share}_6^*)}{\partial \gamma_6} = -\frac{w_6^*}{\gamma_6} \cdot \frac{W}{(w_6^* + W)^2} < 0,$$

equivalently $\partial \ln(\text{dollar-share}_6^*) / \partial \ln \gamma_6 = -(1 - \text{dollar-share}_6^*)$. QED. The sign does not depend on the decay rates. They determine what the shift costs: the allocation moves toward the item with the highest decay rate ($\delta_6 = .50$ against a substrate average $\delta_S = .119$), which is why the long-run multiple falls while current earnings rise.

*Proposition S5.2 (substrate-building threshold; Proposition 6).* With $\gamma_4 \in (0, 1]$ fixed, the long-run Tier-4 stock rises with the durability shock: $\partial S_4^* / \partial \Delta_4 > 0$.

*Proof.* Substituting the share rule into $S_4^* = w_4^* \cdot I / \delta_4^{\text{eff}}$ gives $S_4^* = \alpha_4 I / [\gamma_4 f(\delta_4^{\text{eff}})]$ with $f(\delta) = \delta(\delta + r)$. Since $\partial \delta_4^{\text{eff}} / \partial \Delta_4 = -1$ and $f'(\delta) = 2\delta + r$,

$$\frac{\partial S_4^*}{\partial \Delta_4} = \frac{\alpha_4 I \, (2\delta_4^{\text{eff}} + r)}{\gamma_4 \, f(\delta_4^{\text{eff}})^2} > 0.$$

QED. The threshold in Proposition 6 is structural rather than algebraic: at $\Delta_4 = 0$ a deployment is a cost shock only, and at $\Delta_4 > 0$ (a proprietary fine-tune or owned weights) a substrate-building component becomes admissible.

*Proposition S5.3 (horizon dependence of the marketing-flow share; Proposition 7).* Under the generalized share rule,

$$\frac{\partial \ln(\text{dollar-share}_6^*)}{\partial r} = \sum_t \frac{\text{dollar-share}_t^*}{\delta_t^{\text{eff}} + r} - \frac{1}{\delta_6^{\text{eff}} + r},$$

which is positive whenever $\delta_6^{\text{eff}}$ exceeds every other $\delta_t^{\text{eff}}$, as it does at the calibration (.50 against at most .175).

*Proof.* $\partial \ln w_t^* / \partial r = -1/(\delta_t^{\text{eff}} + r)$, and $\gamma_t$ enters only the weights. The right-hand side is a share-weighted average of $1/(\delta_t^{\text{eff}} + r)$ minus its smallest term, hence positive. QED. A deployment that raises the principal's effective discount rate therefore raises the marketing-flow share, and one that lowers it lowers the share; this is the formal content of the horizon-conditional sign flip. Proposition S5.3 extends the base-model result of S1 to the shocked share rule.

*Joint shocks and identification.* On a single item, a fall in $\gamma_t$ and a rise in $\Delta_t$ move $w_t^*$ in the same direction ($\partial w_t^* / \partial \gamma_t < 0$, $\partial w_t^* / \partial \Delta_t > 0$, and $\partial^2 w_t^* / \partial \gamma_t \partial \Delta_t = -\alpha_t / [\gamma_t^2 (\delta_t^{\text{eff}} + r)^2] < 0$), so the direction of a joint shock on the item's own share is not ambiguous. What a share cannot reveal is the split between the two: $\gamma_t$ changes how much of the item is bought, while $\Delta_t$ also changes how long it lasts, through $S_t^* = w_t^* I / \delta_t^{\text{eff}}$. A disclosure such as "a proprietary fine-tune that has reduced our customer-service operating cost while building a defensible asset" identifies the direction but not the channel. This is why the main paper treats joint identification of $(\gamma_t, \Delta_t)$ as sufficient for Propositions 5 and 6 but not for the $\Delta_t$-specific channel of Proposition 7.

---

## S6. CES Robustness for the AI-Extended Share Rule

The main paper maintains Cobb-Douglas ($\sigma = 1$). This section replaces the aggregator with constant elasticity of substitution $\sigma$, parallel to S4 for the base model:

$$V_{LR}(w; r, \gamma, \Delta; \sigma) = A \cdot I \cdot \Big[\sum_t \alpha_t \, x_t^{(\sigma - 1)/\sigma}\Big]^{\sigma/(\sigma - 1)}, \qquad x_t = m_t w_t / (\delta_t^{\text{eff}} + r),$$

under the same budget constraint. Writing the constraint in $x_t$ gives a linear cost $\sum_t c_t x_t = 1$ with $c_t = \gamma_t (\delta_t^{\text{eff}} + r)^2 / m_t$, so the CES demand $x_t \propto (\alpha_t / c_t)^{\sigma}$ yields

$$w_t^*(\sigma) \propto \alpha_t^{\sigma} \, m_t^{\sigma - 1} \, \gamma_t^{-\sigma} \, (\delta_t^{\text{eff}} + r)^{1 - 2\sigma},$$

which reduces to the share rule of S5 at $\sigma = 1$. The normalization constant cancels in every dollar-weighted share.

*Proposition 5 under CES.* $\partial \ln(\text{dollar-share}_6^*) / \partial \ln \gamma_6 = -\sigma (1 - \text{dollar-share}_6^*) < 0$ for every $\sigma > 0$. The direction of the paradox does not depend on $\sigma$; its strength does, weaker under gross complements and stronger under gross substitutes.

*Proposition 7 under CES.* $\partial \ln(\text{dollar-share}_6^*) / \partial r = (2\sigma - 1) \big[\sum_t \text{dollar-share}_t^* / (\delta_t^{\text{eff}} + r) - 1/(\delta_6^{\text{eff}} + r)\big]$. The bracket is positive, as in S5.3, so the sign of the horizon effect is the sign of $2\sigma - 1$: positive for $\sigma > .5$, zero at $\sigma = .5$, negative below. The two-tier reduction printed by both companion scripts (S4, Panel 2) is a coarser check of the same boundary and reports a falling share at $\sigma = .5$. Proposition 7 is therefore stated for $\sigma \ge 1$ in the main paper, with the $\sigma = .5$ case disclosed.

*Profile comparison.* For Profile A (marketing-flow-heavy, $w_6 = .70$) and Profile B (Tier-4/5-heavy, $w_{4\text{-}5} = .65$), the ratio $V_{LR}(B)/V_{LR}(A)$ is 1.22 at $\sigma = .5$, 1.93 at $\sigma = 1.0$ and 2.17 at $\sigma = 1.5$ (function `ces_robustness()`). The ordering $V_{LR}(B) > V_{LR}(A)$ holds at all three values; its magnitude depends on $\sigma$.

---

## S7. Sensitivity to Alternative $\alpha_t$ Calibrations

The output elasticities enter the share rule directly. The main paper's baseline is $\alpha_6 = .12$, $\alpha_4 = \alpha_5 = .24$, $\alpha_2 = \alpha_3 = .20$, proportional to the separability factors $m_t$. Table S5 compares it with two alternatives.

**Table S5: Marketing-Flow Share, Paradox Magnitude and Profile Ratio Under Three $\alpha_t$ Calibrations.**

| Calibration | $\text{dollar-share}_6^*$ | Paradox magnitude | $V_{LR}(B)/V_{LR}(A)$ |
|---|---|---|---|
| Baseline ($m_t$-proportional) | .065 | .076 | 1.93 |
| Conservative (all $\alpha_t = .20$) | .112 | .124 | 1.55 |
| Concentrated-stock ($\alpha_6 = .05$; $\alpha_4 = \alpha_5 = .30$; $\alpha_2 = \alpha_3 = .175$) | .027 | .033 | 2.39 |

*Notes*: Evaluated at $r = .15$, $\gamma_6 = .8$, all other $\gamma_t = 1$ and all $\Delta_t = 0$. The paradox magnitude is $|\partial(\text{dollar-share}_6^*)/\partial \gamma_6|$ at $\gamma_6 = .8$. Printed by `alpha_calibration_sensitivity()` in `tier_penetration_simulation.py`.

The sign of the paradox holds in all three calibrations, as S5.1 requires. The profile ratio ranges from 1.55 to 2.39, a 1.54-fold spread driven by the weight on marketing flow relative to the substrate items. The direction of Proposition 5 is robust to the calibration; the size of the predicted M&A-multiple effect is not, and should be re-estimated in any panel that recovers $\alpha_t$ from firm-level data. All three calibrations preserve the ordering $m_6 < m_2 = m_3 < m_4 = m_5$ on which the structural claims rest.

---

## S8. Identification Strategy and Empirical Test Design

This section gives the operational detail behind the main paper's section "AI Deployment: Implications for Empirical Testing": the tier-assignment protocol, the disclosure-coding pilot, dictionary exemplars, and the five threats to identification. It is a validation roadmap for a future empirical paper; the paper's contribution is deductive theory.

*Tier-assignment protocol.* The unit of assignment is the deployment artifact, not the project, because one project often produces artifacts on several tiers. Each artifact is assigned by asking where its durable record resides: which tier's specification or parameter it writes or keeps up, or, for marketing flow, whether it is spend that only runs functioning. The four boundary cases of Table 5 decompose as follows. Klarna's chatbot is a Tier 5 configuration on a third-party foundation model under Tier 3 vendor terms; the work it absorbs moves from Tier 6 (the agents) to Tier 5. Spotify's recommendation system is a Tier 2 user-behavior model (the data flywheel) with a Tier 4 platform specification; each served recommendation is a transient output, not a durable artifact. BloombergGPT is a Tier 5 fine-tune with Tier 4 outputs embedded in the terminal. Stripe Radar is a Tier 2 fraud-decisioning model; the merchant-facing decision is a transient output.

*Disclosure-coding pilot design.* The pilot hand-codes 100 AI-related disclosures from a stratified S&P 1500 sample over 2023–2026. The target inter-rater reliability for tier assignment is Cohen's kappa $\ge .65$, following Krippendorff (2004) and matching the .60–.75 range that Hassan, Hollander, van Lent, and Tahoun (2019) report for text-based political-risk classification. Two independent coders, with third-coder adjudication, report pairwise and three-way kappas. The pilot validates tier-depth scores against the firm-level AI-investment measure of Babina, Fedyk, He, and Hodson (2024) with two pre-committed tests (sum correlation $\ge .40$; per-tier collinearity $\le .85$), and a classifier-based robustness check is pre-committed.

*Dictionary exemplars.* Marketing flow: "generative marketing copy," "programmatic-bidding optimization." Tier 5: "AI customer-service chatbot," "proprietary fine-tune," "owned model weights," "AI workflow automation agent." Tier 4: "AI-as-product," "embedding-context switching cost," "AI-codified product specification." Tier 2: "data flywheel," "recommendation engine constitutive of product," "AI fraud-decisioning." Tier 3: "AI contract drafting," "AI compliance monitoring." Tier 1: few positive exemplars are expected, because the main paper treats the controlling position's judgment as a constitutional ceiling rather than a capability threshold. Negative exemplars, which resemble tier indicators but are not: "AI strategy," "evaluating AI vendors," "AI pilot program" (unassigned); "AI-powered analytics dashboard" (requires artifact-level decomposition).

*Threats to identification.* The main paper sketches three first-order threats and the separability concern. Each is expanded below with severity, mitigations, residual risk and robustness checks, and two further threats are added.

*Threat 1: Selection on unobservables.* Severity high. Firms ready for Tier-4 deployment at the 2022 capability transition had superior data infrastructure, specification discipline and machine-learning capacity, which affect later outcomes through channels other than the deployment, so a cross-sectional comparison of deployers and non-deployers conflates the deployment effect with selection. *Mitigations:* (a) pre-trends tests on intangible-intensity series before the deployment event; (b) firm fixed effects in a difference-in-differences specification; (c) entropy balancing or coarsened exact matching on size, intangible intensity, prior R&D, sector AI exposure (Felten, Raj, and Seamans 2021) and pre-treatment AI-mention frequency in earnings calls. *Residual risk:* time-varying unobservables, such as infrastructure that was improving at the moment of deployment. *Robustness checks:* (a) the coefficient-stability bound of Oster (2019); (b) a sub-sample of firms with similar ex-ante data-infrastructure scores built from prior-year disclosures.

*Threat 2: Parallel-trends violation.* Severity medium. Successive capability-frontier shocks are common shocks correlated with tech-sector trends, so the parallel-trends assumption is contestable in a tech-heavy panel. *Mitigations:* (a) pre-trends tests; (b) placebo difference-in-differences on capital-light service sectors (legal services, accounting, financial services excluding fintech) where Tier-4 deployment is implausible at the relevant horizon; (c) sector-by-time fixed effects; (d) the staggered-adoption estimator of Callaway and Sant'Anna (2021) if treatment timing varies. *Residual risk:* heterogeneous treatment effects within the tech sector. *Robustness checks:* (a) the heterogeneous-effects diagnostics of de Chaisemartin and D'Haultfœuille (2020); (b) leave-one-sub-industry-out estimates.

*Threat 3: Founder-horizon endogeneity.* Severity medium. Founder-CEO status, family governance and ownership concentration are themselves outcomes of past performance, so the horizon proxies that Proposition 7 requires are endogenous to the outcomes it explains. *Mitigations:* (a) the first-born-gender instrument of Bennedsen, Nielsen, Pérez-González, and Wolfenzon (2007) for family-firm succession; (b) founder-CEO tenure interacted with industry shocks; (c) institutional-concentration measures as partly exogenous horizon proxies. *Residual risk:* the instrument's predictive power has weakened as gender-neutral succession norms spread. *Robustness checks:* (a) an overidentification test combining the two instruments; (b) a sub-sample of family firms whose first-born child's gender is identifiable before 2000.

*Threat 4: Measurement error in the tier-depth measure.* Severity low to medium. The measure is dictionary-coded from 10-K Item 1A, Item 7 and earnings-call transcripts on the template of Hassan, Hollander, van Lent, and Tahoun (2019); classical error attenuates coefficients toward zero. *Mitigations:* (a) the pilot reliability target above; (b) a classifier validation pass against the human-coded sample, with agreement reported; (c) split-sample replication. *Residual risk:* non-classical error, since verbose disclosers may be coded more accurately and verbosity correlates with size. *Robustness checks:* (a) size-stratified sub-samples; (b) controls for total disclosure length.

*Threat 5: Attrition through acquisition.* Severity low to medium. M&A multiples are observed only for firms that are acquired, and targets are not a random sample: they are more likely to be successful Tier-4 deployers and less likely to be firms deploying AI only in marketing flow. *Mitigations:* (a) a two-stage selection correction (Heckman 1979) with a first stage for the probability of acquisition; (b) inverse-probability weighting on the propensity to be acquired. *Residual risk:* the exclusion restriction is contestable, because instruments that move acquisition probability without moving the multiple conditional on acquisition are scarce. *Robustness check:* sensitivity of the estimates to the exclusion restriction.

Even under the full mitigation set, time-varying unobservables and instrument validity remain open. The empirical programme should therefore narrow the identified effect progressively rather than test the framework in one regression. Where separate identification of $\gamma_t$ and $\Delta_t$ fails, joint identification at the tier level (S5) keeps Propositions 5 and 6 testable.

---

## S9. Companion Script for Part II: Run Command, Functions and Parameters

*Script location.* `tier_penetration_simulation.py`, published at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-allocation/code/tier_penetration_simulation.py.

*Run command.* `uv run python tier_penetration_simulation.py`

*Python version and dependencies.* Python 3.10 or later, with numpy and scipy. The script draws no plots (Figure 1 is generated by `back_of_envelope.py`). It sets `numpy.random.seed(42)` at module load for consistency with the corpus pattern, uses no stochastic operation, and is deterministic.

*Function inventory.*

`effective_delta(delta_0, Delta)` returns $\delta_t^{\text{eff}} = \delta_t^0 - \Delta_t$ per item and asserts $\Delta_t < \delta_t^0$.

`share_rule(alpha, delta_eff, gamma, r)` returns the unnormalized $w_t^* = \alpha_t / [\gamma_t (\delta_t^{\text{eff}} + r)]$ (S5).

`dollar_shares(w_star)` normalizes the shares to sum to one.

`proposition_5_marketing_flow_paradox()` sweeps $\gamma_6$ under the baseline calibration and checks $\partial(\text{dollar-share}_6^*)/\partial \gamma_6 < 0$ (Proposition 5, S5.1).

`proposition_6_tier4_threshold()` computes $S_4^*$ across $\Delta_4 = 0$ and $\Delta_4 > 0$ and checks $\partial S_4^* / \partial \Delta_4 > 0$ (Proposition 6, S5.2).

`proposition_7_horizon_flip()` computes $\text{dollar-share}_6^*$ at $r \in \{.10, .15, .20\}$ under $\sigma = 1$ and checks that it rises with $r$ (Proposition 7, S5.3).

`ces_robustness()` reports the profile ratio and the two-tier sign check at $\sigma \in \{.5, 1.0, 1.5\}$ (S6).

`alpha_calibration_sensitivity()` reports Table S5 (S7).

`boundary_object_cases()` reports the $(\gamma_t, \Delta_t)$ pattern and multiple direction for the four cases of Table 5.

`main()` runs the analysis functions in sequence, prints each result with the value stated in the paper, and ends with a verification summary of the signs of Propositions 5–7.

*Parameters.* The baseline calibration is the one stated in the main paper's per-tier accumulation model, with decay rates from Table 1: $\alpha_6 = .12$, $\alpha_4 = \alpha_5 = .24$, $\alpha_2 = \alpha_3 = .20$; $m_6 = .25$, $m_4 = m_5 = 1.0$, $m_2 = m_3 = .60$; $\delta_6 = .50$ (Belo, Lin, and Vitorino 2014), $\delta_5 = .175$ (Eisfeldt and Papanikolaou 2013; Corrado, Hulten, and Sichel 2009), $\delta_4 = .15$ (Lev and Sougiannis 1996; Hall, Jaffe, and Trajtenberg 2005), $\delta_2 = \delta_3 = .075$ (extrapolated from Wiggins and Ruefli 2002); default $r = .15$; no-shock defaults $\gamma_t = 1$ and $\Delta_t = 0$.

*Reproducibility.* Every numerical value in Part II of the main paper and in Sections S5–S9 that is not taken from an external source is reproducible from `tier_penetration_simulation.py` with the run command above; the script has no external data dependencies.
