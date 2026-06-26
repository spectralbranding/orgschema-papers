# Online Supplement to "Where to Invest Within the Firm: Organizational Tiers, Discount Rates, and Long-Run Firm Value"

**Dmitry Zharnikov**

ORCID: 0009-0000-6893-9231

DOI: [10.5281/zenodo.20072288](https://doi.org/10.5281/zenodo.20072288)

Working Paper v1.1.0 -- May 2026

*The main paper is published at https://doi.org/10.5281/zenodo.20072288 and at https://github.com/spectralbranding/orgschema-papers/tree/main/tier-allocation/. The companion computation script is at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-allocation/code/back_of_envelope.py.*

This online supplement provides the full mathematical derivations, sensitivity analyses, and robustness checks underlying the formal model presented in the main paper. The companion computation script `back_of_envelope.py` (available at the paper's Zenodo record, DOI 10.5281/zenodo.20072288) reproduces all numerical values reported in both the main paper and this supplement. All values are fully deterministic; no random-number generation is used.

---

## S1. Mathematical Derivations: Formal Proof of ∂(dollar-share_6*)/∂r > 0

*Formal Derivation of ∂(dollar-share_6*)/∂r > 0 Under the Discounted-Cobb-Douglas Maintained Specification*

Throughout this section, δ_t denotes the per-period decay rate (matching Table 1 values directly and the Belo, Lin, and Vitorino 2014 convention). The full user-cost-of-capital specification (Jorgenson 1963) sets the per-tier rental rate q_t = δ_t + r, which is the per-period cost of holding one unit of tier-t stock: the firm pays δ_t to cover depreciation and r as the opportunity cost of capital. Belo, Lin, and Vitorino (2014) adopt the simplifying assumption r = 0, so their rental rate equals the decay rate alone; the present model retains the full Jorgensonian form q_t = δ_t + r.

**Step 1: The maximand.** The maintained specification (Equation 3 in the main paper) is:

V_LR(w; r) = A · I · Π_t [m_t · w_t / (δ_t + r)]^{α_t},   Σ_t α_t = 1

Taking logs: ln V_LR = ln A + ln I + Σ_t α_t · [ln m_t + ln w_t − ln(δ_t + r)].

**Step 2: The budget constraint.** The firm allocates total expenditure E across tiers facing per-tier rental prices q_t = δ_t + r. With w_t = I_t/I_total and normalization Σ_t (δ_t + r) · w_t = 1 (the Jorgensonian user-cost budget constraint).

**Step 3: Lagrangian and FOC.** The Lagrangian is:

L = ln A + ln I + Σ_t α_t · [ln m_t + ln w_t − ln(δ_t + r)] − λ · [Σ_t (δ_t + r) · w_t − 1]

FOC with respect to w_t: ∂L/∂w_t = α_t / w_t − λ · (δ_t + r) = 0

Solving: **w_t*(r) = α_t / [λ · (δ_t + r)]**

**Step 4: Solving for λ.** Substituting w_t*(r) into the budget constraint:

Σ_t (δ_t + r) · w_t* = Σ_t (δ_t + r) · α_t / [λ · (δ_t + r)] = Σ_t α_t / λ = 1/λ = 1

Since Σ_t α_t = 1 under CRS, λ = 1. Therefore: **w_t*(r) = α_t / (δ_t + r)**

**Step 5: Observable dollar-weighted share.** The empirically observable investment share (what an analyst measures as XAD/total-investment) is the dollar-weighted renormalization:

**dollar-share_t*(r) = w_t*(r) / Σ_s w_s*(r) = (α_t / (δ_t + r)) / Σ_s (α_s / (δ_s + r))**

**Step 6: Sign of ∂(dollar-share_6*)/∂r.** For the two-tier reduction (Tier 6 vs. aggregate stock tier S):

dollar-share_6*(r) = [α_6/(δ_6+r)] / {[α_6/(δ_6+r)] + [α_S/(δ_S+r)]}

Let f = α_6/(δ_6+r) and g = α_S/(δ_S+r), so dollar-share_6* = f/(f+g). Then:

∂(dollar-share_6*)/∂r = (f' · g − f · g') / (f + g)²

where f' = −α_6/(δ_6+r)² < 0 and g' = −α_S/(δ_S+r)² < 0.

The numerator is f'·g − f·g' = [−α_6/(δ_6+r)²] · [α_S/(δ_S+r)] − [α_6/(δ_6+r)] · [−α_S/(δ_S+r)²]

= α_6 · α_S / [(δ_6+r)(δ_S+r)] · [1/(δ_S+r) − 1/(δ_6+r)]

= α_6 · α_S / [(δ_6+r)(δ_S+r)] · [(δ_6 − δ_S) / ((δ_S+r)(δ_6+r))]

The sign of the numerator equals the sign of (δ_6 − δ_S). Since δ_6 = .50 > δ_S = .119, the numerator is **strictly positive** for all r > 0. Therefore:

**∂(dollar-share_6*)/∂r > 0**

The optimal Tier-6 dollar-share rises monotonically as r rises. QED.

**Numerical verification.** At r = .15: dollar-share_6* = (.12/.65)/[(.12/.65)+(.88/.269)] = .185/3.456 ≈ .053 (5.3%). At r = .50: dollar-share_6* = (.12/1.00)/[(.12/1.00)+(.88/.619)] = .120/1.542 ≈ .078 (7.8%). The predicted increase from 5.3% to 7.8% as r rises from .15 to .50 confirms the comparative static.

**Intuition.** As r rises, the per-period rental cost q_t = δ_t + r increases for all tiers, but the proportional increase is larger for low-δ_t (stock) tiers because r is a larger fraction of their smaller denominator. The planner responds by substituting away from the now-relatively-more-expensive stock tiers toward Tier 6, whose high base δ_6 = .50 makes the proportional rental-cost increase smaller. The Jorgensonian rental-rate structure is the formal mechanism that generates the comparative static the paper's propositions rest on.

## S2. Sensitivity of V_LR Multiple Gap to r

The ratio V_LR(Profile B; r) / V_LR(Profile A; r) as a function of r, computed under the discounted-Cobb-Douglas maintained specification V_LR(w; r) = A · I · Π_t [m_t · w_t / (δ_t + r)]^{α_t} with α calibration (α_6 = .12; α_4 = α_5 = .24; α_2 = α_3 = .20) and separability factors (m_6 = .25; m₄₋₅ = 1.0; m₂₋₃ = .6):

| r | V_LR(A) | V_LR(B) | Ratio B/A |
|---|---------|---------|---------|
| .10 | .268 | .518 | 1.93 |
| .15 | .221 | .427 | 1.93 |
| .20 | .188 | .363 | 1.93 |

*Notes*: Values normalized to A · I = 1. Computed from the back-of-envelope calibration in the "Two-Tier Minimal Illustration" section of the main paper with w profiles (A: w₆ = .70, w₄₋₅ = .20, w₂₋₃ = .10; B: w₆ = .15, w₄₋₅ = .65, w₂₋₃ = .20) and α exponents calibrated proportional to M&A separability factors. Under constant returns to scale (Σ_t α_t = 1), the B/A ratio is exactly r-invariant at 1.93: as r rises, all per-tier productivity factors m_t/(δ_t+r) fall for both profiles, but they cancel in the ratio (I^{Σα_t} = I factors out). The V_LR levels decline substantially with r — from .268/.518 at r = .10 to .188/.363 at r = .20 — reflecting that higher discount rates compress the present value of all perpetuity-form tier stocks. The r-sensitivity surfaces in the optimal dollar-share dollar-share_6*(r) (Section S1), not in the B/A ratio at fixed w-profiles. The B/A multiple gap of 1.93× is stable across the relevant discount-rate range, reproducing the *ordinal* structure of observed M&A multiple differentials but understating the magnitude (empirical gap is closer to 4–6×). All values are reproducible from the companion computation script (`back_of_envelope.py`, function `reproduce_appendix_a2()`).

## S3. Alternative α_t Calibrations

The α_t output elasticities (α_6 = .12, α_4 = α_5 = .24, α_2 = α_3 = .20) are calibrated proportional to the M&A separability factors m_t. Sensitivity checks across two alternative specifications, computed under the discounted-Cobb-Douglas maintained specification at r = .15:

| α Calibration | V_LR(A; .15) | V_LR(B; .15) | Ratio |
|---------------|---------|---------|-------|
| Baseline (α_6 = .12; α_4 = α_5 = .24; α_2 = α_3 = .20) | .221 | .427 | 1.93 |
| Conservative (α_6 = .20; α_4 = α_5 = .20; α_2 = α_3 = .20) | .218 | .339 | 1.55 |
| Concentrated-stock (α_6 = .05; α_4 = α_5 = .30; α_2 = α_3 = .175) | .234 | .559 | 2.39 |

*Notes*: Values computed under the maintained specification V_LR(w; r) = A · I · Π_t [m_t · w_t / (δ_t + r)]^{α_t} at r = .15; all values are reproducible from the companion computation script (`back_of_envelope.py`, function `reproduce_appendix_a3()`). The B/A multiple ratio ranges from 1.55× to 2.39× across the alternative α-vector specifications, confirming the qualitative stability of the result. The directional prediction — Profile B commands a substantially higher multiple than Profile A regardless of the α calibration — is robust to reasonable parameter variation. As α_6 falls, the magnitude gap widens: the "Concentrated-stock" specification with α_6 = .05 produces a 2.39× ratio, closer to the empirical 4–6× range. The validation roadmap (Appendix: Validation Roadmap of the main paper, Priority 1) jointly estimates α_t and δ_t from a Compustat panel where the parameters are identified from the data rather than chosen to reproduce target ratios.

## S4. CES Robustness Check on Comparative Static

The maintained specification adopts the Cobb-Douglas aggregator (σ = 1), which is the tractable special case of the CES family. To assess whether the qualitative findings depend on the unit elasticity of substitution, this section reports V_LR under a full CES aggregator:

V_LR^{CES}(w; r, σ) = A · I · [ Σ_t α_t · (m_t · w_t / (δ_t + r))^{(σ−1)/σ} ]^{σ/(σ−1)}

for σ ≠ 1, recovering the Cobb-Douglas maintained specification as σ → 1. Values of σ < 1 correspond to gross complements (co-specialization-strong; Adner 2012 ecosystem framing), while σ > 1 corresponds to gross substitutes (co-specialization-weak). The table below reports V_LR(A), V_LR(B), and the B/A ratio at r = .15 for σ ∈ {.5, 1.0, 1.5}.

**Table S4: CES Robustness Check — Profile A/B V_LR and B/A Ratio at r = .15.**

| σ | V_LR(A) | V_LR(B) | Ratio B/A |
|---|---------|---------|---------|
| .5 (gross complements) | .202 | .247 | 1.22 |
| 1.0 (Cobb-Douglas, maintained) | .221 | .427 | 1.93 |
| 1.5 (gross substitutes) | .227 | .494 | 2.17 |

*Notes*: Values computed at r = .15 with baseline α calibration (α_6 = .12; α_4 = α_5 = .24; α_2 = α_3 = .20). Reproducible from companion computation script (`back_of_envelope.py`, function `reproduce_appendix_a4_ces()`). The Cobb-Douglas (σ = 1) row matches the "Two-Tier Minimal Illustration" section of the main paper exactly. CES with σ < 1 attenuates the B/A ratio to 1.22× but does not reverse it: Profile B strictly dominates Profile A across all three elasticity values. CES with σ > 1 amplifies the ratio to 2.17×, closer to the empirical 4–6× range. A brief summary of the in-body CES check and the main qualitative finding appears in the main paper (Table 2); this supplement section provides the full derivation and sign verification.

The comparative static ∂(dollar-share_6*)/∂r is verified numerically under σ ∈ {.5, 1.5} using a two-tier reduction (Tier 6 vs. aggregate stock tier, equal-weighted δ_S = .119). Under the maintained Cobb-Douglas (σ = 1), the sign is established analytically in Section S1. Under σ = 1.5 (gross substitutes), numerical optimization confirms that the planner-optimal w_6 share rises monotonically: .017 at r = .10, .018 at r = .15, .019 at r = .20 — ∂w_6*/∂r > 0 confirmed. Under σ = .5 (gross complements), the two-tier numerical optimizer finds that the planner-optimal w_6 share declines slightly with r in the two-tier reduction (.523 at r = .10, .507 at r = .15, .495 at r = .20), indicating that the comparative static sign is not preserved under strong gross complementarity in the simplified two-tier case. This reversal is specific to the two-tier reduction at σ < 1: under gross complementarity, the planner wants a more balanced portfolio, and as r rises the high rental cost of all tiers shifts the interior optimum toward the symmetry point. In the full five-tier model with heterogeneous δ_t the directional propositions remain supported by the B/A ordering, which is robust across all σ values examined. The maintained Cobb-Douglas (σ = 1) is therefore a conservative choice: the B/A ratio of 1.93× understates the magnitude under σ > 1 and overstates it under σ < 1, bracketing the empirical range symmetrically. Full five-tier CES optimization is identified as a future extension.

All numerical values in this supplement are reproducible from the companion computation script published at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-allocation/code/back_of_envelope.py and also available at the paper's Zenodo record at https://doi.org/10.5281/zenodo.20072288. Run with `uv run python back_of_envelope.py` (Python 3.10+; requires numpy, matplotlib, scipy).
