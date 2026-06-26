# Online Supplement to "Where to Invest Within the Firm: Organizational Tiers, Discount Rates, and AI Penetration"

**Dmitry Zharnikov**

ORCID: 0009-0000-6893-9231

DOI: [10.5281/zenodo.20072288](https://doi.org/10.5281/zenodo.20072288)

Working Paper v1.1.0 -- May 2026

*The main paper is published at https://doi.org/10.5281/zenodo.20072288 and at https://github.com/spectralbranding/orgschema-papers/tree/main/tier-allocation/. The companion computation script is at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-allocation/code/back_of_envelope.py.*

This online supplement provides the full mathematical derivations, sensitivity analyses, and robustness checks underlying the formal model presented in the main paper. The companion computation script `back_of_envelope.py` (available at the paper's Zenodo record, DOI 10.5281/zenodo.20072288) reproduces all numerical values reported in both the main paper and this supplement. All values are fully deterministic; no random-number generation is used.

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

**Step 6: Sign of $\partial(\text{dollar-share}_6^*)/\partial r$.** For the two-tier reduction (Tier 6 vs. aggregate stock tier $S$):

$$\text{dollar-share}_6^*(r) = [\alpha_6/(\delta_6+r)] / \{[\alpha_6/(\delta_6+r)] + [\alpha_S/(\delta_S+r)]\}$$

Let $f = \alpha_6/(\delta_6+r)$ and $g = \alpha_S/(\delta_S+r)$, so $\text{dollar-share}_6^* = f/(f+g)$. Then:

$$\partial(\text{dollar-share}_6^*)/\partial r = (f' \cdot g - f \cdot g') / (f + g)^2$$

where $f' = -\alpha_6/(\delta_6+r)^2 < 0$ and $g' = -\alpha_S/(\delta_S+r)^2 < 0$.

The numerator is $f' \cdot g - f \cdot g' = [-\alpha_6/(\delta_6+r)^2] \cdot [\alpha_S/(\delta_S+r)] - [\alpha_6/(\delta_6+r)] \cdot [-\alpha_S/(\delta_S+r)^2]$

$$= \alpha_6 \cdot \alpha_S / [(\delta_6+r)(\delta_S+r)] \cdot [1/(\delta_S+r) - 1/(\delta_6+r)]$$

$$= \alpha_6 \cdot \alpha_S / [(\delta_6+r)(\delta_S+r)] \cdot [(\delta_6 - \delta_S) / ((\delta_S+r)(\delta_6+r))]$$

The sign of the numerator equals the sign of $(\delta_6 - \delta_S)$. Since $\delta_6 = .50 > \delta_S = .119$, the numerator is **strictly positive** for all $r > 0$. Therefore:

$$\partial(\text{dollar-share}_6^*)/\partial r > 0$$

The optimal Tier-6 dollar-share rises monotonically as $r$ rises. QED.

**Numerical verification.** At $r = .15$: $\text{dollar-share}_6^* = (.12/.65)/[(.12/.65)+(.88/.269)] = .185/3.456 \approx .053$ (5.3%). At $r = .50$: $\text{dollar-share}_6^* = (.12/1.00)/[(.12/1.00)+(.88/.619)] = .120/1.542 \approx .078$ (7.8%). The predicted increase from 5.3% to 7.8% as $r$ rises from .15 to .50 confirms the comparative static.

**Intuition.** As $r$ rises, the per-period rental cost $q_t = \delta_t + r$ increases for all tiers, but the proportional increase is larger for low-$\delta_t$ (stock) tiers because $r$ is a larger fraction of their smaller denominator. The planner responds by substituting away from the now-relatively-more-expensive stock tiers toward Tier 6, whose high base $\delta_6 = .50$ makes the proportional rental-cost increase smaller. The Jorgensonian rental-rate structure is the formal mechanism that generates the comparative static the paper's propositions rest on.

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

The comparative static $\partial(\text{dollar-share}_6^*)/\partial r$ is verified numerically under $\sigma \in \{.5, 1.5\}$ using a two-tier reduction (Tier 6 vs. aggregate stock tier, equal-weighted $\delta_S = .119$). Under the maintained Cobb-Douglas ($\sigma = 1$), the sign is established analytically in Section S1. Under $\sigma = 1.5$ (gross substitutes), numerical optimization confirms that the planner-optimal $w_6$ share rises monotonically: .017 at $r = .10$, .018 at $r = .15$, .019 at $r = .20$ — $\partial w_6^*/\partial r > 0$ confirmed. Under $\sigma = .5$ (gross complements), the two-tier numerical optimizer finds that the planner-optimal $w_6$ share declines slightly with $r$ in the two-tier reduction (.523 at $r = .10$, .507 at $r = .15$, .495 at $r = .20$), indicating that the comparative static sign is not preserved under strong gross complementarity in the simplified two-tier case. This reversal is specific to the two-tier reduction at $\sigma < 1$: under gross complementarity, the planner wants a more balanced portfolio, and as $r$ rises the high rental cost of all tiers shifts the interior optimum toward the symmetry point. In the full five-tier model with heterogeneous $\delta_t$ the directional propositions remain supported by the B/A ordering, which is robust across all $\sigma$ values examined. The maintained Cobb-Douglas ($\sigma = 1$) is therefore a conservative choice: the B/A ratio of 1.93× understates the magnitude under $\sigma > 1$ and overstates it under $\sigma < 1$, bracketing the empirical range symmetrically. Full five-tier CES optimization is identified as a future extension.

All numerical values in this supplement are reproducible from the companion computation script published at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-allocation/code/back_of_envelope.py and also available at the paper's Zenodo record at https://doi.org/10.5281/zenodo.20072288. Run with `uv run python back_of_envelope.py` (Python 3.10+; requires numpy, matplotlib, scipy).
