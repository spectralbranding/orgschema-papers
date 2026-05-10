# Where to Invest Within the Firm: Organizational Tiers, Discount Rates, and Long-Run Firm Value

**Dmitry Zharnikov**

ORCID: 0009-0000-6893-9231

DOI: [10.5281/zenodo.20072288](https://doi.org/10.5281/zenodo.20072288)

Working Paper v1.0.0 -- May 2026

---

**Abstract**

Why do two firms with identical revenues, margins, and aggregate investment generate exit multiples of 2× versus 9× revenue and divergent post-acquisition performance? Capital allocation theory, dynamic capabilities, and marketing-finance literatures have each left the direction of investment within a business implicit. This paper formalizes the cross-tier allocation problem using a vector w spanning five operating tiers that differ in asset durability. Each tier accumulates stock according to a differential equation with tier-specific decay rates δ_t ranging from .50/year at the organizational surface (Tier 6: advertising, paid media) to .05–.10/year at foundational layers (Tiers 2–3: business-model architecture, legal position). Long-run value is a discounted Cobb-Douglas aggregator incorporating Jorgensonian user costs (δ_t + r) and ownership-separability weights. Optimizing subject to the per-tier rental-rate budget constraint yields the closed-form rule w_t*(r) = α_t / (δ_t + r) and the comparative static ∂w₆*/∂r > 0: higher discount rates increase optimal allocation to the high-decay surface tier at the expense of durable substrate.

Four propositions follow: pre-deal surface-tier intensity predicts post-acquisition goodwill impairment; long-horizon governance lowers equilibrium surface-tier share; cost-of-capital shocks shift allocation predictably; and capability-rotation stage moderates returns to codification investment. The framework supplies a missing architectural mechanism that integrates resource-based, dynamic-capability, and internal-capital-market streams, making investment direction — not merely intensity — a consequential strategic choice.

**Keywords**: capital allocation; dynamic capabilities; brand capital; goodwill impairment; portfolio choice; organizational architecture

---

Consider two consumer goods firms — call them Firm A and Firm B — that are identical on every dimension a standard valuation model can observe. Their revenues are equal. Their EBITDA margins are equal. Their aggregate annual investment in the business is equal. Their sectors overlap, their debt structures match, and their management tenure is comparable. At exit, Firm A sells at 2× revenue; Firm B sells at 9× revenue. The acquirer of Firm A writes down goodwill within eighteen months; the acquirer of Firm B does not. The post-close performance divergence between them persists for five years.

Neither internal-capital-markets theory (Stein 1997; Berger and Ofek 1995; Maksimovic and Phillips 2002) nor dynamic-capabilities theory (Teece, Pisano, and Shuen 1997; Teece 2007) nor marketing-finance research (Mizik and Jacobson 2003, 2009) can explain this divergence. All three literatures treat the structural character of investment within a business as given. The internal-capital-markets tradition allocates across divisions but does not encode the architectural composition of investment within a division. Marketing finance distinguishes brand-capital stock from advertising flow without specifying the organizational layer that produces the distinction. Dynamic capabilities treats capability accumulation as a single integrative channel without decomposing direction across architectural tiers.

The resolution lies in a prior architectural question: not how much the firm invested but where, across the organizational hierarchy, the investment was directed. Firm A routed investment predominantly toward Tier 6 — the organizational surface comprising marketing, advertising, and paid media — where expenditure generates current-period output but accumulates minimal transferable substrate. Firm B routed a larger share toward Tiers 4 and 5 — product specification, brand codification, and process infrastructure — where investment compounds into stocks whose value persists across ownership transitions and management changes. This architectural difference is invisible in aggregate financials yet produces order-of-magnitude valuation gaps.

We formalize this cross-tier portfolio choice. Organizational tiers are defined by substrate durability and ownership separability (Table 1), with decay rates grounded in Belo, Lin, and Vitorino (2014), Eisfeldt and Papanikolaou (2013), and Lev and Sougiannis (1996). Each tier t accumulates according to dS_t/dτ = w_t I − δ_t S_t. Long-run value is the Cobb-Douglas aggregator V_LR(w; r) = A · I · Π_t [m_t · w_t / (δ_t+r)]^{α_t} subject to the Jorgensonian constraint Σ_t (δ_t+r) · w_t = 1. The resulting closed-form optimum w_t*(r) = α_t/(δ_t+r) yields ∂w₆*/∂r > 0 as a direct mathematical consequence of the decay-rate differential.

We introduce organizational tier as a new unit of analysis for resource allocation, supplying the missing architectural primitive that converts capability direction into a portfolio variable whose optimization depends on principal discount rates. The framework contributes to strategy by: (1) anchoring multi-asset decay heterogeneity to an architectural ontology — extending Dierickx and Cool (1989) from single-asset to multi-tier settings and grounding the empirical depreciation estimates of Belo, Lin, and Vitorino (2014) in organizational theory; (2) deriving four falsifiable propositions that link pre-deal Tier-6 intensity, governance horizon, cost-of-capital shocks, and rotation stage to M&A outcomes and capability persistence; and (3) providing the mechanism that reconciles Mizik and Jacobson's (2003, 2009) empirical signature with Teece's (2007) dynamic-capabilities framework — the δ₄ ≪ δ₆ decay-rate differential makes brand-capital stock and advertising flow structurally non-fungible.

The paper proceeds as follows. Theoretical foundations situate the contribution within capital allocation, marketing finance, and dynamic capabilities. The per-tier accumulation model is developed formally. A two-tier minimal illustration establishes the core comparative-static result with a back-of-envelope calibration. Cross-tier comparative statics and four propositions follow. Illustrative cases examine the theory's predictions. The Discussion elaborates implications for each literature stream and for practice. A validation roadmap is provided in the Appendix. Mathematical derivations are collected in the Online Supplement.

---

**Theoretical Foundations**

*Capital Allocation Across Business Units and the Missing Architectural Margin*

The internal capital markets literature establishes that capital allocation across divisions is value-relevant and subject to agency distortions. Stein (1997) formalizes headquarters winner-picking logic — allocating capital using soft information about divisional productivity — as the mechanism behind variation in the conglomerate discount. Berger and Ofek (1995) document a 13–15% diversification discount in U.S. firms, establishing the value-relevance of within-firm allocation choices at scale. Maksimovic and Phillips (2002) provide the large-sample empirical counterpart: more productive business units receive larger allocations in efficient multi-business firms. Agency distortions compound this structural problem: Glaser, Lopez-de-Silanes, and Sautner (2013) show that division managers manipulate information to extract favorable allocation outcomes; Scharfstein and Stein (2000) and Rajan, Servaes, and Zingales (2000) document the rent-seeking and cross-divisional competition costs that reverse efficient allocation.

The ICM tradition allocates capital across divisions and treats the within-division composition of investment as a residual. The present paper introduces the within-business architectural tier as the unit of analysis — preserving the portfolio formalism while replacing the divisional unit with the tier unit. The resulting comparative statics are not derivable from divisional ICM models because tiers differ in accumulation dynamics (δ_t), not in expected returns. The frictionless-planner benchmark developed here is the necessary first step; the agency extension (discussed below) predicts equilibrium over-allocation to Tier 6 relative to the planner's optimum, strengthening the directional propositions.

*Marketing Finance: Stock Versus Flow*

Mizik and Jacobson (2003) document that firms face a fundamental trade-off between value creation — accumulating brand-capital stock — and value appropriation — harvesting returns from existing stock through advertising spend and pricing. Firms that shift strategic emphasis toward value appropriation boost current-period earnings at the cost of long-run brand asset value. Mizik and Jacobson (2009) demonstrate that brand-capital stock explains incremental variance in firm valuation multiples beyond accounting variables alone: markets price the stock, not the flow. These are the most direct empirical antecedents of the present theory, which supplies the organizational-layer mechanism that Mizik and Jacobson's empirical signature requires but does not provide: brand-capital stock resides at Tier 4 (product specification and brand codification; δ₄ ≈ .12–.20/year), while advertising and paid media reside at Tier 6 (δ₆ = .50/year). The δ₄ ≪ δ₆ differential is what makes the two investment categories structurally non-fungible from a long-run value perspective — the formalization of the trade-off Mizik and Jacobson document empirically.

Belo, Lin, and Vitorino (2014) provide the empirical anchor for the Tier-6 decay parameter, calibrating δ₆ = .50/year from a perpetual-inventory model on Compustat advertising expenditure. Peters and Taylor (2017) generalize this approach to the full intangible capital stock, with their SG&A-derived organizational capital component depreciating at approximately .20/year — independently corroborating the Tier-5 range in Table 1. Erickson and Jacobson (1992) supply the earliest formal cross-channel return evidence: R&D and advertising generate distinct return profiles across time horizons, the foundational observation that the present framework converts into a portfolio optimization problem. Naik (1999) independently corroborates δ₆ = .50 via meta-estimated advertising half-lives of four to six months across product categories.

*Dynamic Capabilities, RBV Foundations, and the Single-Channel Accumulation Problem*

The resource-based view (Wernerfelt 1984; Barney 1991; Dierickx and Cool 1989) establishes that sustained competitive advantage derives from durable asset stocks accumulated through sustained investment flows, and that structural properties of accumulation — time-compression diseconomies, asset mass efficiencies — differ across asset types. The tier-allocation framework is a formal instantiation of Dierickx and Cool applied to a multi-tier architectural setting: each tier carries a structurally distinct accumulation profile captured by δ_t. Tiers are not resources in the Barney-VRIN sense — they are the architectural locations where resources accumulate, and the structural properties of those locations (substrate durability, ownership separability) determine the sustainability profiles of whatever resources accumulate there.

Teece, Pisano, and Shuen (1997) and Teece (2007) establish dynamic capabilities as the capacity to continuously reconfigure the asset base, treating capability accumulation as a single integrative channel through which the firm repositions itself. The 2007 paper is the most-cited contribution in the tradition; the present paper's core extension is to decompose Teece's single channel into a portfolio variable whose direction — not merely intensity — is theoretically consequential. Helfat and Peteraf (2003) supply the capability-lifecycle frame: capability stocks follow a founding-development-maturity trajectory whose persistence properties correspond directly to the tier-specific δ_t vector. Adner and Helfat (2003) extend this to dynamic managerial capabilities — the capacity of managers to purposively create, extend, and modify the resource base — which provides the governance-level mechanism for P2's long-horizon-principal result: patient-capital allocation is itself a dynamic capability. Eggers and Kaplan (2013) connect executive cognitive-resource allocation across time horizons to which capability investments receive sustained organizational attention, directly linking principal time horizons to the tier-allocation decision.

The post-2015 DC literature closes the mechanism-specification gap this framework targets. Helfat and Peteraf (2015) identify the specific cognitive abilities — search, pattern recognition, adaptive capacity — underlying sensing, seizing, and transforming, grounding the long-horizon-principal result in managerial cognition rather than discount-rate arithmetic alone. Helfat and Martin (2015) review evidence that managerial human capital and social capital systematically affect the direction and quality of strategic change. Teece (2018) extends the 2007 microfoundations to business-model innovation — directly relevant because Tier 2 of the six-tier scaffold is business-model architecture, making tier-allocation decisions at Tier 2 dynamic-capability exercises. Schilke, Hu, and Helfat (2018) supply the definitive content-analytic review, confirming that formalization of cross-capability complementarities and architectural decompositions is a major identified gap — precisely what the per-tier δ_t vector supplies. Fainshmidt, Wenger, Pezeshkan, and Mallon (2019) show that dynamic capabilities yield competitive advantage only when they align with strategic fit — a configurational logic the tier-allocation framework formalizes by specifying which tier portfolio achieves fit with a given discount-rate environment. Sirmon, Hitt, Ireland, and Gilbert (2011) establish resource orchestration as bundling and leveraging across life-cycle stages; the allocation vector w is the portfolio-formal instantiation of those orchestration decisions, with architectural tier identity as the organizing principle. The multiplicative Cobb-Douglas aggregation (Equation 3) captures cross-tier complementarities in reduced form, following the tractable special case of the Milgrom and Roberts (1990, 1995) supermodularity framework.

*Six-Tier Architectural Scaffold*

The tier-allocation formalism requires an organizational decomposition that partitions the firm into layers whose persistence properties differ structurally — not merely empirically. This paper adopts a six-tier hierarchy grounded in published organization theory and developed from first principles here. The foundational insight is Penrose's (1959) characterization of the firm as an administrative organization whose value derives not from individual resources but from the bundle of services those resources yield under the governance structures that hold them together. Galbraith (1973) extends this by treating architectural design as the central unit of organizational decision-making: the structural configuration chosen by the firm determines which decisions can be delegated, which commitments are reversible, and which resource bundles are insulated from market volatility. Mintzberg (1979) identifies durable structural elements — strategic apex, middle line, operating core, technostructure, support staff — whose persistence across personnel transitions is precisely what distinguishes organizational form from individual talent. Galunic and Eisenhardt (1996) establish that modular hierarchy is an evolving architectural primitive: divisional charters and component boundaries migrate as the firm repositions, but the hierarchical layering itself is a stable organizing logic that persists across reconfigurations.

From these foundations, the six-tier ontology used in this paper classifies organizational elements by substrate durability and ownership separability:

| Tier | Architectural Element | Durability / Separability Rationale |
|------|-----------------------|--------------------------------------|
| Tier 1 | Owner intent and personal identity | Non-transferable across ownership; decays with founder departure |
| Tier 2 | Business-model architecture, contractual relations, ownership structure | Contractual — survives as long as legal and relational scaffolding holds; δ₂ ≈ .05–.10/year |
| Tier 3 | Business entity, regulatory position, formal legal structure | Legally embodied in the entity — persists across management change; δ₃ ≈ .05–.10/year |
| Tier 4 | Product specification, brand codification, trademark portfolio | Architecturally recorded and legally owned; persists across personnel transition; δ₄ ≈ .12–.20/year |
| Tier 5 | Process infrastructure, operations, physical capital | Converted into codified routines and PP&E; survives individual departures; δ₅ ≈ .15–.20/year |
| Tier 6 | Organizational surface: advertising, PR, paid media | Constitutionally flow-dependent; requires continuous investment to persist; δ₆ = .50/year |

This six-tier decomposition partitions the firm into layers where substrate durability is architecturally determined — it is a consequence of the persistence mechanism of each layer, not an empirical label. The tier position predicts the numerical range of δ_t, which is what distinguishes this architectural grounding from the ad hoc category assignments of prior multi-asset depreciation studies. For an extended treatment of the dual-hierarchy structure and acquisition-failure propagation, see Zharnikov (2026ag).

A central mechanism linking tier composition to post-acquisition outcomes is what this paper terms the tier-independence overestimation problem: acquirers systematically attribute durable-stock value to targets whose revenue-generating assets are constitutively flow-dependent. When a high-w₆ target's advertising-funded revenue is capitalized at a multiple appropriate for a durable-stock business, the resulting goodwill premium exceeds the present value of the substrate that actually transfers across the ownership transition. The resulting write-down — accounting recognition of this mismatch — is consistent with the finding of Glaum, Landsman, and Wyrwa (2018) that goodwill impairments are concentrated in acquisitions where post-close monitoring of asset quality is weakest, precisely the condition created when intangible value is treated as tier-independent at deal pricing. The P1 derivation (Proposition 1 below) formalizes this mechanism from the tier-allocation model directly.

The Tier-Rotation Curve (Zharnikov 2026ai) addresses the temporal margin of tier composition: how the Tier-1/Tier-4 share evolves across multi-decade ownership horizons as founders externalize tacit brand knowledge into organizational substrates. The present paper addresses the spatial margin: in any given period, where should marginal investment be deployed across the five operating tiers? The two margins are analytically separable — the Tier-Rotation Curve takes w as exogenous; this paper endogenizes w and holds rotation stage fixed as a conditioning variable.

---

**The Per-Tier Accumulation Model**

*Architectural Grounding: Why Tiers Are the Right Unit of Analysis*

Prior asset-stock models (Dierickx and Cool 1989; Lev and Sougiannis 1996; Belo, Lin, and Vitorino 2014) start from observed investment categories and estimate depreciation rates empirically. The resulting estimates are tractable but architecturally under-motivated: they do not explain why R&D decays at a different rate than advertising, or why that difference is stable across sectors. The six-tier ontology (Section "Theoretical Foundations") provides the architectural explanation: tier position determines persistence mechanism, and persistence mechanism determines the numerical range of δ_t. This ground-up motivation is what distinguishes the tier-allocation model from prior multi-asset depreciation frameworks — the δ_t vector carries theoretical content rather than functioning as an empirical label.

The choice of organizational tier as the unit of analysis is a position within the microfoundations debate: Felin, Foss, and Ployhart (2015) establish that the central question is which level of analysis — individual cognition, routines, or organizational architecture — is the correct locus for explaining firm heterogeneity. The tier-allocation framework takes a definite position: the architectural tier, not the individual or the routine, is the right unit because it determines the persistence mechanism. Directional commitment to a high-w_t allocation also inherits the irreversibility logic of Ghemawat (1991): tier-specific stocks resist redirection because their accumulation paths involve sunk organizational investments that cannot be costlessly redeployed. Ghemawat and Levinthal (2008) generalize this in an NK-simulation setting, showing that policy-choice interdependence amplifies the cost of reallocating across strategy positions — directly applicable to cross-tier reallocation where each tier's stock accumulation is partly co-determined by adjacent tiers.

*The Per-Tier Accumulation Equation*

The model specifies each tier t ∈ {2, 3, 4, 5, 6} as carrying a stock S_t(τ) governed by a first-order accumulation equation:

**Equation 1 (Per-Tier Accumulation):**

dS_t/dτ = w_t · I(τ) − δ_t · S_t(τ)

where I(τ) is total investment at time τ, w_t is the allocation share to tier t, δ_t ∈ [0, 1] is the tier-specific *decay rate* (the proportion of the existing stock that depreciates in each period), and the allocation vector satisfies Σ_t w_t = 1 with w_t ≥ 0. This convention matches Belo, Lin, and Vitorino (2014) verbatim: they set the brand-capital depreciation rate δ = 50% annually, so their δ is the decay coefficient, not the persistence fraction. Under this convention, a tier with δ_t = .50 loses half its stock each period in the absence of new investment; a tier with δ_t = .15 loses only 15% of its stock per period and is considerably more durable. Throughout this paper δ_t denotes the per-period decay rate, (1 − δ_t) denotes the per-period survival fraction, and all Table 1 values are reported as decay rates.

At the long-run steady state, dS_t/dτ = 0, and the equilibrium stock is:

**Equation 2 (Long-Run Stock):**

S_t* = w_t · I / δ_t

for δ_t > 0 and I(τ) = I constant. The steady-state derivation assumes constant total investment I(τ) = I and time-invariant allocation share w_t; the comparative statics on r are therefore interpretable as cross-sectional comparisons across firms operating at distinct steady states, with the dynamic adjustment path treated as future work. The long-run stock at each tier is proportional to the allocation share w_t and inversely proportional to the decay rate δ_t — so more durable tiers accumulate larger equilibrium stocks per unit of investment. This is the fundamental stock-versus-flow tension: a firm that allocates entirely to Tier 6 (δ₆ = .50) achieves long-run stock S₆* = 2·I, while a firm that allocates entirely to Tier 4 (δ₄ ≈ .15) achieves long-run stock S₄* ≈ 6.67·I — more than three times the stock per unit of investment. The stock-versus-flow asymmetry is built into the accumulation equation's parameters; the portfolio problem is how to optimally allocate w across tiers given the firm's discount rate and the valuation weights ρ_t(r).

*The δ_t Calibration Table*

The tier-specific decay rates are calibrated from empirical estimates in independent literatures. Table 1 presents the full calibrated δ_t vector with sources. Four key observations follow from the table.

**Table 1: Calibrated Tier-Specific Decay Rates (δ_t Vector).**

| Tier | Asset Type | δ_t (Decay Rate) | Half-Life | Source | Confidence |
|------|-----------|------------------|-----------|--------|------------|
| Tier 6 | Advertising / marketing surface | .50/year | ~1.4 years | Belo, Lin, Vitorino (2014) RED; Naik (1999) | HIGH -- confirmed from paper PDF |
| Tier 5 | Organizational capital / process infrastructure | .15–.20/year | ~3.5–4.3 years | Eisfeldt, Papanikolaou (2013) JF; Corrado, Hulten, Sichel (2009) RIW | HIGH |
| Tier 4 | Product specification / R&D / trademark stock | .12–.20/year | ~3.1–5.4 years | Lev, Sougiannis (1996) JAE; Nadiri, Prucha (1996) EI; Hall, Jaffe, Trajtenberg (2005) RAND | HIGH |
| Tiers 2/3 | Business-model architecture / entity position | .05–.10/year | ~7–14 years | Wiggins, Ruefli (2002) Org Sci (persistence proxy; no direct δ estimate) | MEDIUM -- extrapolation |

*Notes*: δ_t is the per-period decay rate (the fraction of stock that depreciates in one year); (1 − δ_t) is the survival fraction. Half-life computed as ln(.5) / ln(1 − δ_t). This convention matches Belo, Lin, and Vitorino (2014) verbatim: "We use a depreciation rate of δ = 50%… The monthly depreciation rate of brand capital is set at δ_n = 4.16% per month, which corresponds to an annual depreciation rate of 50%." Tier-2/3 estimates are extrapolated from competitive-advantage duration evidence (Wiggins and Ruefli 2002); no direct calibrated depreciation rate exists for business-model architecture or entity-level assets, which constitutes a priority for the validation roadmap (Appendix).

---

First, the Tier-6 parameter δ₆ = .50/year is confirmed directly from the Belo, Lin, and Vitorino (2014) paper: they set the depreciation rate at 50% annually (monthly δ = .0416), calibrated from a perpetual-inventory model applied to Compustat advertising expenditure (XAD). This is not an approximation; it is the paper's stated calibration value. Naik (1999) provides independent corroboration: pooling meta-estimates of advertising carry-over across product categories, he finds half-lives of advertising goodwill in the 4–6 month range, consistent with an annual decay rate of approximately 50%.

Second, the Tier-5 decay rate (δ₅ = .15–.20/year) is anchored to two independent estimates. Eisfeldt and Papanikolaou (2013) construct an organizational capital stock from the non-routine component of SG&A using a perpetual-inventory method and find that the implied depreciation rate is approximately .15/year; Corrado, Hulten, and Sichel (2009) report a range of .15–.20/year for organizational competencies in their intangible-capital accounting framework.

Third, the Tier-4 decay rate (δ₄ = .12–.20/year) is supported by three independent estimates. Lev and Sougiannis (1996) estimate industry-specific R&D amortization rates ranging from 15% to 20% per year; Nadiri and Prucha (1996) estimate R&D capital depreciation at .12/year for U.S. total manufacturing; Hall, Jaffe, and Trajtenberg (2005) document patent citation dynamics consistent with a knowledge-stock depreciation in the same range.

Fourth, the Tier-2/Tier-3 decay rates (δ₂/δ₃ = .05–.10/year) have no direct empirical estimates and are extrapolated from competitive-advantage duration evidence. Wiggins and Ruefli (2002) document that superior economic performance persists for 7–14 years in the median case across industries, implying an annual decay rate of approximately .05–.10 for the capability substrate supporting that performance. The absence of direct depreciation estimates for Tier-2/Tier-3 assets is itself a theoretical contribution: the paper is explicit that the business-model-architecture and entity-level-position tiers lack an empirical depreciation literature, and that establishing calibrated estimates for these tiers is a priority for the companion validation paper (see Appendix).

*The Long-Run Value Function*

The long-run value function aggregates tier stocks via a constant-returns-to-scale Cobb-Douglas production function:

**Equation 3 (Long-Run Value Function):**

V_LR(w; r) = A · I · Π_t [m_t · w_t / (δ_t + r)]^{α_t}

where A > 0 is a productivity scalar, m_t ∈ [0,1] is the M&A separability factor for tier t (the fraction of tier-t stock that transfers across an ownership transition, calibrated from the tier-durability rationale in the Six-Tier Architectural Scaffold above: m_6 = .25 reflecting the flow-dependent character of advertising assets; m₄₋₅ = 1.0 reflecting legally owned, architecturally recorded stocks; m₂₋₃ = .6 reflecting contractual and regulatory positions that are transferable but subject to deal-structure risk), and α_t ∈ (0,1) are the per-tier output elasticities satisfying Σ_t α_t = 1 (constant returns to scale). This maintained specification follows the two-capital Cobb-Douglas production function of Belo, Lin, and Vitorino (2014), who combine brand capital and physical capital multiplicatively to explain the cross-section of firm value. The Cobb-Douglas is the tractable special case of the Milgrom and Roberts (1990, 1995) supermodularity framework: it captures cross-tier complementarities in reduced form while admitting closed-form comparative statics. The constant-returns-to-scale constraint (Σ_t α_t = 1) implies that V_LR scales linearly with total investment I (since I^{Σα_t} = I^1 = I factors out cleanly) but responds non-linearly to the allocation vector w — the central theoretical claim.

The term (δ_t + r) in the denominator of each factor is the Jorgensonian user cost of capital for tier t — the per-period rental rate q_t = δ_t + r that the firm effectively pays to hold one unit of tier-t stock (Jorgenson 1963). The firm allocates total expenditure E across tiers facing per-tier rental prices q_t, so the budget constraint is Σ_t q_t · I_t = E (or equivalently, with shares w_t = I_t/I and total investment normalized to 1: Σ_t (δ_t + r) · w_t = 1). Belo, Lin, and Vitorino (2014) adopt the simplifying assumption that the rental rate equals the decay rate alone (r = 0 special case); the present model retains the full Jorgensonian form, making the rental rate tier-specific and discount-rate-dependent. The effective per-tier productivity factor m_t · w_t / (δ_t + r) folds together the long-run stock S_t* = w_t · I / δ_t, the perpetuity valuation discount, and the M&A separability weight into a single reduced-form term.

The per-tier output elasticities α_t represent the long-run value contribution per unit of effective tier-t stock, calibrated proportional to the M&A separability factors m_t (m_6 = .25; m₄₋₅ = 1.0; m₂₋₃ = .6), normalized to sum to 1. Rounding to two decimal places: α_6 = .12; α_4 = α_5 = .24; α_2 = α_3 = .20 (sum = 1.00). The calibration encodes the structural insight that tiers with higher M&A transferability contribute more elastically to long-run value per unit of effective stock; the observable investment share w_t*, however, depends jointly on α_t and the per-tier rental rate (δ_t + r) — tiers with high rental rates attract smaller observable investment shares even when their output elasticity is held fixed.

The Cobb-Douglas structure has two consequences for the optimization. First, V_LR is strictly log-concave in w, so interior optima exist naturally — without any adjustment-cost augmentation. This eliminates the quadratic adjustment-cost term that the additive formulation required; the organizational-learning costs motivating that term are now captured implicitly by the diminishing marginal returns structure of the Cobb-Douglas. Second, ∂²ln(V_LR)/∂w_t² = −α_t/w_t² < 0: the log-concavity is strict, so the planner's optimum is uniquely interior for all r in the calibrated range. The over-allocation-to-Tier-6 result becomes a statement about the deviation of the observed w₆ from the planner's interior optimum, rather than a corner versus interior comparison. Online Supplement S1 provides the complete formal derivation of the interior optimum and the ∂w₆*/∂r comparative static.

---

**Two-Tier Minimal Illustration**

*The Sethi Template and the Advertising-Stock Tradition*

The clearest route to the core result is the two-tier minimal model, which reduces the full five-tier vector to a single choice: w₆ versus (1 − w₆) allocated to an aggregate stock tier. This structure adopts the asset-stock-vs-flow distinction from the optimal-control tradition established by Sethi (1977) without deploying its full continuous-time control apparatus, which is a natural extension; Sethi's survey of advertising-as-goodwill-stock models formalizes the advertising firm's problem as choosing an investment flow (advertising expenditure) that builds a one-dimensional goodwill stock S(t) subject to geometric depreciation, maximizing the present value of profits net of advertising costs. Sethi's framework treats advertising as the sole control, with all other organizational assets in the residual. The tier-allocation minimal model inverts this architecture: Tier 6 (advertising flow) is the choice variable whose optimal share w₆* is to be determined, and the aggregate stock tier (Tiers 2–5 consolidated) is the competing investment destination. The Doraszelski and Markovich (2007) dynamic model of advertising-as-stock extends Sethi's template to competitive markets; the minimal model below abstracts from competition to isolate the portfolio choice at the firm level.

Mizik and Jacobson (2003) provide the empirical precedent: their value-creation/value-appropriation trade-off is the closest existing operationalization of the Tier-5/Tier-4 versus Tier-6 distinction that the tier-allocation framework formalizes. The present paper describes the Sethi (1977) optimal-control lineage as the formal template and Mizik-Jacobson (2003) as the empirical precedent, distinguishing its contribution as the model that (a) embeds both within a formal tier-indexed accumulation vector and (b) derives discount-rate comparative statics from that vector.

*The Two-Tier Setup*

Let the firm choose w₆ ∈ [0, 1], with the residual w_S = 1 − w₆ allocated to a single aggregate stock tier S_S combining Tiers 2 through 5. The aggregate stock tier has effective decay rate δ_S (the investment-weighted average of the Tier-2 through Tier-5 decay rates). From Table 1: δ₂/₃ ≈ .075 (midpoint of .05–.10); δ₄ ≈ .15 (midpoint of .12–.20); δ₅ ≈ .175 (midpoint of .15–.20). Weighting by relative investment share (assuming uniform initial weights across the four stock tiers as a baseline), the aggregate stock-tier decay rate is:

δ_S ≈ (1/4)(.075) + (1/4)(.075) + (1/4)(.15) + (1/4)(.175) ≈ .119

Using the steady-state stock formula (Equation 2) under the decay-rate convention:

S₆* = w₆ · I / δ₆ = w₆ · I / .50 = 2 · w₆ · I

S_S* = (1 − w₆) · I / δ_S ≈ (1 − w₆) · I / .119 ≈ 8.40 · (1 − w₆) · I

The stock-tier multiplier 8.40 versus the Tier-6 multiplier 2 reflects the decay-rate differential at the center of the model: each unit of investment in the aggregate stock tier generates more than four times the equilibrium stock of an equivalent unit invested at Tier 6.

Under the Cobb-Douglas maintained specification, the two-tier value function reduces to:

V_LR(w₆) = A · S₆*(w₆)^{α₆} · S_S*(1 − w₆)^{1−α₆}
           = A · (2·w₆·I)^{α₆} · (8.40·(1−w₆)·I)^{1−α₆}

where α₆ = .12 (the Tier-6 output elasticity from the maintained calibration) and 1−α₆ = .88 aggregates the stock tiers. The Cobb-Douglas form is log-concave in w₆, so an interior optimum exists for all positive α₆.

*The ∂w₆*/∂r Comparative Static*

The interior optimum w₆* follows from the Lagrangian maximization of ln V_LR(w; r) subject to the Jorgensonian user-cost-of-capital budget constraint Σ_t (δ_t + r) · w_t = 1. This budget constraint captures the per-tier rental rate q_t = δ_t + r: higher-decay-rate tiers carry higher per-period costs, so the firm faces a tier-differentiated price vector when allocating investment.

The Lagrangian is: L = ln A + ln I + Σ_t α_t · [ln m_t + ln w_t − ln(δ_t + r)] − λ · [Σ_t (δ_t + r) · w_t − 1].

The FOC with respect to w_t is: α_t / w_t − λ · (δ_t + r) = 0, giving **w_t*(r) = α_t / [λ · (δ_t + r)]**.

Substituting into the budget constraint: Σ_t (δ_t + r) · w_t* = Σ_t α_t / λ = (1/λ) · Σ_t α_t = 1/λ = 1 (since Σα_t = 1 under CRS), so **λ = 1** and the interior optimum simplifies to:

**w_t*(r) = α_t / (δ_t + r)**

The dollar-weighted (empirically observable) investment share — what an outside observer measures as tier-t investment as a fraction of total investment — is:

**dollar-share_t*(r) = w_t*(r) / Σ_s w_s*(r) = (α_t / (δ_t + r)) / Σ_s (α_s / (δ_s + r))**

The comparative static ∂(dollar-share_6*)/∂r > 0 follows directly from the sign of (δ₆ − δ_S). For the two-tier reduction, differentiating dollar-share_6*(r) = (α_6/(δ_6+r)) / [(α_6/(δ_6+r)) + (α_S/(δ_S+r))] with respect to r, the derivative is positive if and only if δ₆ > δ_S — which holds since δ₆ = .50 > δ_S = .119. The economic intuition: as r rises, the per-period rental cost of stock-tier investment (δ_S + r) increases proportionally more than that of Tier-6 (δ_6 + r), because r is a larger fraction of the smaller-δ denominator for stock tiers. This compresses α_S/(δ_S+r) faster than α_6/(δ_6+r), shifting the optimal dollar-share toward Tier 6.

Numerically, at r = .15: dollar-share_6* = (.12/.65) / [(.12/.65) + (.88/.269)] = .185 / 3.456 ≈ **5.3%**. At r = .50: dollar-share_6* = (.12/1.00) / [(.12/1.00) + (.88/.619)] = .120 / 1.542 ≈ **7.8%**. The optimal Tier-6 dollar-share rises from 5.3% to 7.8% as the discount rate rises from .15 to .50 — the predicted comparative static, with **∂(dollar-share_6*)/∂r > 0** cleanly demonstrated.

High-discount-rate principals therefore optimally hold *lower* stock-tier dollar-shares and *higher* Tier-6 dollar-shares than low-discount-rate principals — the mechanism behind Propositions 1–4. Online Supplement S1 provides the complete formal derivation under the full five-tier vector.

*Back-of-Envelope Calibration of M&A Multiple Gaps*

The formal comparative static becomes empirically concrete through a back-of-envelope calibration under the discounted-Cobb-Douglas maintained specification. Consider three stylized firm profiles, each with total annual investment I = 1 (normalized), evaluated at r = .15. Under the maintained specification V_LR(w; r) = A · I · Π_t [m_t · w_t / (δ_t + r)]^{α_t} with α_t calibrated as (α_6 = .12; α_4 = α_5 = .24; α_2 = α_3 = .20; Σα_t = 1), separability factors (m_6 = .25; m₄₋₅ = 1.0; m₂₋₃ = .6), and decay rates from Table 1:

**Profile A (Tier-6-heavy D2C, calibrated to sector-allocation patterns):** w₆ = .70, w₄₋₅ = .20 (split equally: w₄ = w₅ = .10), w₂₋₃ = .10 (split equally: w₂ = w₃ = .05). Profile A's high Tier-6 share is consistent with D2C-sector advertising-intensity patterns documented in Belo, Lin, and Vitorino (2014), who calibrate δ₆ = .50 from Compustat advertising expenditure (XAD) and show that high-XAD-intensity firms concentrate a large fraction of total investment in flow-dependent surface expenditure.

Effective per-tier factors at r = .15: m₆·w₆/(δ₆+r) = .25·.70/.65 = .269; m₄·w₄/(δ₄+r) = 1.0·.10/.30 = .333; m₅·w₅/(δ₅+r) = 1.0·.10/.325 = .308; m₂·w₂/(δ₂+r) = .6·.05/.225 = .133; m₃·w₃/(δ₃+r) = .133.

V_LR(A; .15) = .269^{.12} · .333^{.24} · .308^{.24} · .133^{.20} · .133^{.20} ≈ .221 (normalized)

**Profile B (Tier-4/Tier-5-heavy specialty B2B, calibrated to sector-allocation patterns):** w₆ = .15, w₄₋₅ = .65 (split: w₄ = w₅ = .325), w₂₋₃ = .20 (split: w₂ = w₃ = .10). Profile B's high Tier-4/5 share is consistent with the intangible-capital composition documented in Peters and Taylor (2017), who show that specialty-B2B and industrial sectors allocate the majority of intangible investment to organizational capital (SG&A-derived, corresponding to Tier 5) and R&D capital (corresponding to Tier 4), with advertising intensity (Tier 6) substantially below the median for high-XAD consumer sectors. Lev and Sougiannis (1996) independently report that R&D-intensive industries carry R&D capital-to-total-investment ratios in the .40–.70 range, corroborating the elevated Tier-4/5 allocation in Profile B.

Effective per-tier factors at r = .15: m₆·w₆/(δ₆+r) = .25·.15/.65 = .058; m₄·w₄/(δ₄+r) = 1.0·.325/.30 = 1.083; m₅·w₅/(δ₅+r) = 1.0·.325/.325 = 1.000; m₂·w₂/(δ₂+r) = .6·.10/.225 = .267; m₃·w₃/(δ₃+r) = .267.

V_LR(B; .15) = .058^{.12} · 1.083^{.24} · 1.000^{.24} · .267^{.20} · .267^{.20} ≈ .427 (normalized)

**Profile C (balanced mid-market, calibrated to sector-allocation patterns):** w₆ = .40, w₄₋₅ = .40 (split: w₄ = w₅ = .20), w₂₋₃ = .20 (split: w₂ = w₃ = .10). Profile C's balanced allocation is consistent with the mid-market sector patterns documented in Peters and Taylor (2017): firms in broadly diversified consumer-goods and retail sectors split intangible investment roughly equally between advertising (Tier 6) and organizational/R&D capital (Tiers 4–5), with neither category dominating total investment.

V_LR(C; .15) ≈ .380 (normalized; computed via companion script at r = .15)

The M&A multiple ratios are: V_LR(B)/V_LR(A) ≈ **1.93×** and V_LR(B)/V_LR(C) ≈ **1.12×** and V_LR(C)/V_LR(A) ≈ **1.72×**. The B/A ratio of 1.93 is r-invariant under constant returns to scale (Σα_t = 1): as r rises, all per-tier productivity factors fall proportionally in the B/A ratio, canceling out exactly. The V_LR *levels* do vary with r — V_LR(A) falls from .268 at r = .10 to .221 at r = .15 to .188 at r = .20 — reflecting that a higher discount rate compresses the present value of all perpetuity-form tier stocks. The ordinal structure B >> C >> A and the 1.93× ratio are robust across the full discount-rate range (Online Supplement S2).

These ratios reproduce the *ordinal* structure of observed M&A multiple gaps — Profile B dominates Profile C dominates Profile A — but do not close the full empirical gap (Tier-4/Tier-5-heavy specialty businesses trade at 6–12× revenue against 1–2× for Tier-6-heavy D2C exits, an empirical ratio closer to 4–6×). The 1.93× model ratio is a frictionless-planner benchmark; the 4–6× empirically observed gap reflects the agency-amplified equilibrium described in the Discussion (long-horizon principal vs. short-tenure agent), with full closure expected once α_t is estimated from panel data rather than calibrated from m_t separability priors (Online Supplement S3 and Appendix Priority 1). The planner's optimal Tier-6 dollar-share rises from 4.6% at r = .10 to 5.8% at r = .20 — a 1.2 percentage-point shift that is a feature of the frictionless benchmark; the agency-augmented model predicts larger observable shifts driven by reporting-horizon incentives and information asymmetry.

The back-of-envelope is explicitly stylized; it is not an econometric estimate. It demonstrates that the tier-allocation mechanism reproduces the qualitative multiple-gap pattern from first principles — the necessary condition for a falsifiable theoretical mechanism. Full sensitivity analysis across r ∈ {.10, .15, .20} and alternative α_t calibrations is in Online Supplement S2 and S3.

*CES Robustness.*

The 1.93× result is derived under the Cobb-Douglas maintained specification (σ = 1). Table 2 summarizes the B/A ratio and V_LR levels under CES aggregation at σ ∈ {.5, 1.0, 1.5}, computed from the companion script at r = .15. The qualitative ordering — Profile B strictly dominates Profile A — holds across all three elasticity values. Under gross substitutes (σ = 1.5) the B/A ratio rises to 2.17×, moving closer to the empirical 4–6× range. Under gross complements (σ = .5, strong co-specialization), the B/A ratio attenuates to 1.22× but does not reverse. The maintained Cobb-Douglas (σ = 1) is therefore a conservative middle-ground choice. Under σ < 1, the two-tier optimizer tilts toward more symmetric interior solutions and the comparative static ∂w_6*/∂r can reverse — an empirically interesting boundary case documented in full in Online Supplement S4.

**Table 2: CES Robustness Check — B/A Ratio at r = .15.**

| σ | V_LR(A) | V_LR(B) | Ratio B/A |
|---|---------|---------|---------|
| .5 (gross complements) | .202 | .247 | 1.22 |
| 1.0 (Cobb-Douglas, maintained) | .221 | .427 | 1.93 |
| 1.5 (gross substitutes) | .227 | .494 | 2.17 |

*Notes*: Profile A is Tier-6-heavy (w₆ = .70); Profile B is Tier-4/5-heavy (w₄₋₅ = .65). r = .15. The maintained CD specification at σ = 1 yields the 1.93× ratio reported above. The qualitative B > A ordering is robust across σ; the magnitude is sensitive to the elasticity assumption, motivating the full CES derivation in Online Supplement S4. All values reproducible from `back_of_envelope.py`, function `reproduce_appendix_a4_ces()`.

*Contour Structure Over the (w_4, w_6) Plane*

Figure 1 generalizes the three-profile comparison to the full two-dimensional allocation surface, plotting iso-V_LR contours over the (w_4, w_6) plane at r = .15, with the residual budget (1 − w_4 − w_6) held at the planner-optimal relative shares among tiers {2, 3, 5} (.353, .353, .294). The contour map makes three structural features visible that the discrete-profile comparison cannot. First, the high-V_LR ridge runs through the moderate-w_4 / low-w_6 region: allocations that concentrate Tier-4 investment while holding Tier-6 investment near zero receive the highest long-run value, consistent with Profile B's position near the ridge. Second, the iso-V_LR contours are steep in the high-w_6 / low-w_4 corner — the region where Profile A resides — indicating that additional allocation to Tier 6 imposes rapid welfare losses once the surface tier already absorbs a large budget share. The Cobb-Douglas log-concavity is pronounced in this corner because the Tier-6 factor (m_6 · w_6 / (δ_6 + r))^{α_6} is bounded by the low separability weight m_6 = .25 and the high rental rate (δ_6 + r) = .65, so V_LR is insensitive to w_6 increases in the high-w_6 region while remaining highly sensitive near the planner's interior optimum. Third, the interior optimum (w_4*, w_6*) ≈ (.23, .05) — derived from the FOC w_t*(r) = α_t / (δ_t + r) and renormalized — sits well inside the feasible region and is clearly distinct from both stylized profiles. The .228 Tier-4 share and .053 Tier-6 share of the planner's optimum are substantially different from Profile A (.10, .70) and modestly different from Profile B (.325, .15), confirming that the 1.93× valuation gap between the two profiles reflects welfare losses from sub-optimal allocation in opposite directions from the ridge. The contour is reproducible from the companion computation script (`back_of_envelope.py`, function `generate_contour_plot()`).

![Long-run value V_LR(w; r) over the (w_4, w_6) plane at r = .15, holding (w_2, w_3, w_5) at their planner-optimal relative shares (.353, .353, .294) of the residual budget. Iso-V_LR contours show the welfare-loss surface near the high-w_6 corner (Profile A) and the value ridge in the moderate-w_4 / low-w_6 region. The interior optimum at (w_4*, w_6*) ≈ (.23, .05) is marked.](figures/tier_allocation_contour.png){width=70%}

---

**Cross-Tier Portfolio: Comparative Statics and Propositions**

*General Results*

In the full five-tier model, optimizing V_LR(w; r) subject to the Jorgensonian budget constraint Σ_t (δ_t + r) · w_t = 1 yields the interior optimum w_t*(r) = α_t / (δ_t + r), with the observable dollar-weighted share dollar-share_t*(r) = [α_t / (δ_t + r)] / Σ_s [α_s / (δ_s + r)]. The formal derivation and the proof that ∂(dollar-share_6*)/∂r > 0 are in Online Supplement S1; the two-tier minimal illustration (preceding section) establishes the result numerically. Three general properties hold across all parameter combinations in the calibrated range:

(i) ∂(dollar-share_6*)/∂r > 0 — the comparative static derived in Online Supplement S1. The sign follows from δ₆ > δ_S, making it a direct function of the decay-rate differential. The optimal dollar-shares at r ∈ {.10, .15, .20} are tabulated in the companion computation script.

(ii) ∂²ln(V_LR)/∂w_t² = −α_t/w_t² < 0 for all t: V_LR is strictly log-concave, so interior optima exist by construction without adjustment-cost augmentation. High-r over-allocation to Tier 6 is a welfare loss relative to the long-run-value-maximizing portfolio.

(iii) The cross-sectional multiplier V_LR(w*_low_r) / V_LR(w*_high_r) increases in (δ₆ − δ_S): wider decay-rate gaps produce larger long-run value penalties from discount-rate-driven over-allocation to Tier 6.

***Proposition 1 — Goodwill Impairment Hazard.***

Pre-deal w₆ share predicts post-acquisition goodwill impairment hazard within 36 months of deal close, controlling for deal size, sector, acquirer characteristics, and pre-deal revenue growth.

*Derivation.* In the tier-allocation framework, goodwill represents the acquirer's payment for the present value of the target's long-run value function V_LR(w). Goodwill impairment occurs when realized long-run value falls below the premium paid. Targets with high pre-deal w₆ shares have low S₄* and S₅* stocks; they are over-valued when acquirers capitalize current EBITDA multiples without discounting for Tier-6 intensity, because the flow-dependent revenue requires continuous reinvestment to persist. Goodwill impairment is the accounting recognition of this mismatch — consistent with Glaum, Landsman, and Wyrwa (2018), who document that impairments concentrate in acquisitions where post-close monitoring of intangible asset quality is weakest, precisely the condition created by tier-independent deal pricing.

The deal formally involves two distinct discount rates: the target's r_T (at which the target's pre-deal w-vector was set) and the acquirer's r_A (at which post-close V_LR is realized). Impairment hazard is monotonically increasing in (r_T − r_A) interacted with pre-deal w_6 share — a sharpening of P1 that is tractable in the Compustat-PitchBook panel. The goodwill-impairment literature provides the empirical setting. Hayn and Hughes (2006) establish canonical leading indicators of goodwill impairment from deal characteristics; P1 adds tier-allocation composition as a structural predictor absent from their specification. Gu and Lev (2011) show that goodwill impairment also reflects acquirer overpayment from sentiment-inflated equity; the tier-allocation mechanism is complementary — structural mis-valuation operates even absent sentiment inflation. Ramanna and Watts (2012) document discretionary impairment timing; the cross-sectional direction of P1 is robust to this because the w₆-intensity predictor captures the magnitude of the V_LR gap, not its timing.

*Falsifiable prediction.* In a Cox proportional hazard model of post-close goodwill impairment events within 36 months, the pre-deal w₆ coefficient (operationalized as XAD/total investment in the three years preceding deal close) is predicted to be positive and statistically significant, controlling for industry fixed effects, deal size, leverage, and acquirer quality. P1 is the sharpest single-equation test of the tier-allocation mechanism: it requires only Compustat XAD data and PitchBook deal-level data with goodwill impairment identifiers (GDWLIP), and it generates a directional prediction that no existing capital-allocation model produces.

***Proposition 2 — Long-Horizon Principal w-Shift.***

Holding sector and rotation stage fixed, principals with lower effective discount rates — of which long-tenured founder-CEO control and active family-firm governance are observable proxies — exhibit lower equilibrium w₆ shares and higher equilibrium w₄ + w₅ shares than shorter-horizon peers in the same industry.

*Derivation.* By the comparative static ∂w₆*/∂r > 0 (Online Supplement S1), long-horizon principals with lower effective r face optimal w₄ and w₅ shares that are larger and optimal w₆ shares that are smaller than short-horizon peers. The theoretically load-bearing variable is the effective discount rate — long-horizon governance is the mechanism, family ownership is one observable proxy. Any governance structure that compresses the effective discount rate — founder-CEO tenure, long-lock-up institutional ownership — shifts the optimal w₆ downward regardless of ownership form. Family-controlled firms do exhibit systematically lower advertising-to-sales ratios and higher R&D-to-sales and capex ratios than matched non-family peers (Anderson and Reeb 2003; Villalonga and Amit 2006; Bertrand and Schoar 2006), consistent with the model.

P2 is a conditional prediction about the discount-rate mechanism, not an unconditional claim about family-firm advertising behavior. The contested empirical record on family-firm advertising intensity reflects that family ownership is an imperfect proxy for the long-horizon governance construct P2 formalizes; it is not a falsification of P2. The appropriate test is a within-industry matched-firm OLS regression in which the family-firm indicator (or CEO tenure, or ownership concentration) predicts w₆ share negatively, with the long-horizon effect attenuating in second-generation professionally-managed family firms (Bertrand and Schoar 2006). This prediction is not available from Stein (1997) or Maksimovic and Phillips (2002), which treat the discount rate as a fixed firm characteristic rather than endogenizing the allocation response to it.

***Proposition 3 — Discount-Rate Moderation of Tier-6 Share.***

The optimal w₆ share increases in the firm's cost of capital, with the sensitivity largest in firms operating in sectors with large (δ₆ − δ_S) decay-rate gaps.

*Derivation.* P3 is the cross-sectional and longitudinal generalization of P2. P2 uses governance as a proxy for the discount rate in a matched-firm cross-section; P3 uses the cost of capital directly, allowing for both cross-sectional variation in WACC and longitudinal variation induced by macroeconomic interest-rate shocks. The sensitivity term — the magnitude of ∂w₆*/∂r — increases in the decay-rate gap (δ₆ − δ_S) because wider gaps produce larger changes in the ρ_S(r)/ρ₆(r) ratio per unit change in r. This cross-sector prediction is testable: industries with large gaps between stock-tier and flow-tier decay rates (e.g., pharmaceutical companies with long-lived patent portfolios δ₄ ≈ .12 versus short-lived advertising δ₆ ≈ .50) should exhibit stronger w₆ sensitivity to cost-of-capital shocks than industries with narrow gaps (e.g., fast-fashion retailers where product-specification assets depreciate nearly as rapidly as advertising). The macroeconomic quasi-experiment that makes P3 tractable is the zero-lower-bound period (2009–2015) versus the post-2022 rate-normalization period: firms facing exogenously lower borrowing costs during 2009–2015 should exhibit lower optimal w₆ shares in a difference-in-differences design, with the magnitude of the shift predicted to be larger in high-gap sectors.

*Scope condition.* Proposition 3 holds under the maintained Cobb-Douglas (σ = 1) and gross-substitutes (σ > 1) regimes. Under sufficiently strong gross complementarity (σ ≪ 1; documented at σ = .5 in Table 2 and Online Supplement S4), the optimizer in the two-tier reduction tilts toward symmetric interior solutions and the comparative static can reverse — an empirically interesting boundary case but outside the regime relevant for the goodwill-impairment-hazard prediction in P1.

***Proposition 4 — Rotation-Stage Moderation of Marginal Return to Tier-4 Investment.***

The marginal return to Tier-4 investment relative to Tier-6 investment — measured by the exit-multiple premium on w₄ share — increases as the firm advances along the Tier-Rotation Curve (Zharnikov 2026ai), with the interaction between Tier-Rotation Stage and w₄ share positive and statistically significant in a deal-multiple regression. (Note: Zharnikov 2026ai supplies the empirical proxy — a trademark-composition ratio — used to operationalize Tier-Rotation Stage in the P4 test; the theoretical mechanism of rotation-stage moderation of returns to Tier-4 codification investment is derived locally from the per-tier accumulation model and does not depend on 2026ai for its derivation.)

*Derivation.* The Tier-Rotation Curve (Zharnikov 2026ai) characterizes the temporal trajectory by which founder-bound brand signal migrates into organizational Tier-4 substrate. At early rotation stages (Stage 1: minimal Tier-4 codification), Tier-4 investment compounds onto a small existing base; the return to additional Tier-4 investment is limited by the organizational capacity to hold and deploy it. At later rotation stages (Stages 3–4: substantial Tier-4 codification established), Tier-4 investment compounds onto a developed substrate with established delivery systems, skilled teams, and codified processes that amplify the return to each additional unit. The marginal return to w₄ investment is stage-dependent under the Cobb-Douglas maintained specification: ∂ln(V_LR)/∂ln(w₄) = α₄ scales as w₄ rises, and the multiplicative interaction with existing Tier-4 substrate (S₄*(τ) at rotation stage τ) generates super-additive returns by construction — the rotation-stage moderation is built into the Cobb-Douglas form rather than introduced as a separate extension. The empirical test is a deal-multiple regression with an interaction term: w₄ share × Rotation Stage indicator (Stage 1/2 versus Stage 3/4), where the interaction coefficient is predicted to be positive. The Rotation Stage can be proxied by the trademark-composition measure developed in Zharnikov (2026ai): the ratio of product-attribute marks to founder-name marks in the USPTO filing history of the target firm.

**Table 3: Comparative Statics Summary Across Propositions P1–P4.**

| Proposition | Predicted Direction | Key Variable | Comparison | Empirical Test |
|------------|-------------------|--------------|------------|----------------|
| P1 — Goodwill impairment hazard | Pre-deal w₆ ↑ → impairment hazard ↑ | Pre-deal w₆ share | High w₆ vs. low w₆ targets | Cox hazard model on GDWLIP within 36 months |
| P2 — Long-horizon principal w-shift | Lower discount rate → lower w₆*, higher w₄* + w₅* | Governance proxy (family-firm indicator, CEO tenure) | Family vs. non-family; high vs. low tenure | Within-industry matched-firm OLS |
| P3 — Discount-rate moderation | Higher WACC → higher w₆* (largest in high-gap sectors) | Cost of capital (WACC; ZLB quasi-experiment) | High-WACC vs. low-WACC; ZLB vs. post-ZLB | DiD with ZLB as exogenous shock |
| P4 — Rotation-stage interaction | w₄ × Stage-3/4 → exit-multiple premium | w₄ share × Tier-Rotation Stage | Stage-1/2 vs. Stage-3/4 targets at same w₄ | Deal-multiple regression with interaction term |

*Notes*: All propositions are derived from the comparative statics of V_LR(w; r) = A · I · Π_t [m_t · w_t / (δ_t + r)]^{α_t} (Equation 3) under the Jorgensonian user-cost-of-capital budget constraint Σ_t (δ_t + r) · w_t = 1. The w₆ share is operationalized as XAD / (XAD + R&D + CAPEX + org-capital SG&A component) in Compustat. Tier-Rotation Stage is proxied by the trademark-composition measure from Zharnikov (2026ai). DiD = difference-in-differences; ZLB = zero lower bound (2009–2015).

---

**Illustrative Cases**

Four cases span the tier-allocation portfolio space from extreme Tier-6 concentration to extreme Tier-4/Tier-5 concentration. These cases illustrate the theory's internal logic; they do not constitute statistical tests. Table 4 presents the four cases in summary form.

**Table 4: Illustrative Cases — Firm Profiles and Tier-Allocation Predictions.**

| Case | Tier Profile | Governance | Discount Rate | Predicted V_LR Multiple | P1 Risk | Key Illustrative Outcome |
|------|-------------|-----------|---------------|--------------------------|---------|--------------------------|
| Casper Sleep (stylized) | w₆ ≈ .70, w₄₋₅ ≈ .20, w₂₋₃ ≈ .10 | VC-backed; short horizon | High | Low (~Profile A: V_LR ≈ .22 at r = .15) | High | IPO multiple ~.5× revenues; subsequent acquisition at discount to IPO |
| Roper Technologies (stylized; parameters loosely match Profile B with w₂₋₃ heavier) | w₆ ≈ .05, w₄₋₅ ≈ .65, w₂₋₃ ≈ .30 | Public; long acquisition horizon | Low | High (broadly Profile-B-class; V_LR ≈ .43 at r = .15) | Low | EV/Revenue persistently 8–10×; clean post-acquisition integration |
| 3G-style PE portfolio (stylized) | Pre: w₆ ≈ .40, w₄₋₅ ≈ .40; Post-close: w₆ ↓ | PE; high hurdle rate, short hold | High (post-close) | Compresses during hold; impairment risk at exit | Elevated at secondary exit | Kraft Heinz $15.4B goodwill impairment 2019 consistent with P1 |
| Hermès International | w₆ ≈ .05–.07 of revenues; w₄₋₅ dominant | Family-controlled (~66%); generational horizon | Very low | Very high (EV/Revenue >15× sustained) | Low | Highest sustained luxury multiple; consistent with P2 and P4 |

*Notes*: V_LR Multiple is estimated from the back-of-envelope calibration in the "Two-Tier Minimal Illustration" section using r = .15 and stylized w profiles. Casper Sleep advertising-to-revenue ratios estimated from pre-IPO S-1 filings; Hermès advertising intensity from annual reports. The 3G Kraft Heinz goodwill impairment is illustrative of P1 operating post-acquisition (Tier-6 compression accelerating brand-capital decay); the P1 test is pre-deal, not post-acquisition. These cases illustrate the theory's internal logic; they do not constitute statistical tests.

---

*Casper Sleep (stylized).* Casper's pre-IPO advertising-to-revenue ratios consistently exceeded 30% — a w₆ share that dwarfed CPG sector medians. Tier-4 substrate was thin relative to advertising investment; Tier-5 logistics were largely outsourced. The February 2021 IPO priced at ~.5× revenues, consistent with Profile A in the back-of-envelope calibration. Subsequent acquisition at a discount to IPO price illustrates P1: the advertising-funded revenue could not sustain deal-price multiples once an acquirer discounted for the flow-dependent character of the revenue base.

*Roper Technologies (stylized).* Roper's model is characterized by high w₄/w₅ allocation — proprietary software specifications, calibration standards, and regulatory certifications that transfer cleanly across ownership changes — and negligible Tier-6 advertising. Enterprise-value-to-revenue multiples have consistently exceeded 8–10× from 2015–2025, consistent with Profile B. The case also illustrates P4: Roper selects acquisition targets at advanced rotation stages where the Tier-4 substrate is fully codified, maximizing the marginal return to further Tier-4 investment over the holding period.

*3G Capital-style PE portfolio (stylized).* 3G's zero-based-budgeting approach systematically compressed Tier-6 advertising post-acquisition (Burger King, Heinz, Kraft, AB InBev), generating short-run earnings improvement while degrading Tier-4 brand-capital stocks over 3–7 years. The model predicts that optimal post-acquisition Tier-6 compression is larger for short-hold, high-hurdle-rate principals under P2, and that the Tier-4 decay that follows creates impairment risk for the secondary buyer. The Kraft Heinz $15.4 billion goodwill impairment in 2019 is directionally consistent: the goodwill booked at deal close reflected the target's pre-deal operational profile, which diverged structurally from the post-deal model.

*Hermès International.* Hermès's advertising-to-revenue ratio (~5–7%) is among the lowest in luxury, while its Tier-4 investment — artisan training, production process codification, trademark portfolio, and brand specification documentation — is among the highest as a share of total investment. Family control (~66% equity) extends the effective discount rate across generations. Enterprise-value-to-revenue has persistently exceeded 15×, more than twice the multiple of sector peers with higher advertising intensity. The case illustrates P2: long-horizon-principal governance produces a low-w₆/high-w₄ portfolio and materially higher long-run value.

---

**Discussion**

*Theoretical Implications for Dynamic Capabilities*

The tier-allocation framework advances the dynamic-capabilities tradition in four ways. First, it converts the single-channel capability-intensity variable of Teece (2007) into a multi-tier portfolio variable, making the direction of investment — not merely its aggregate level — theoretically consequential. Second, the calibrated δ_t vector formalizes Dierickx and Cool's (1989) observation that accumulation properties differ across asset types: anchoring decay rates to an architectural ontology provides the organizational mechanism underlying empirical depreciation heterogeneity. Third, the V_LR(w) formulation supplies the quantitative mechanism that Schilke, Hu, and Helfat (2018) identify as the central gap in the dynamic-capabilities stream. Fourth, the allocation vector w operationalizes the resource-orchestration decisions that Sirmon, Hitt, Ireland, and Gilbert (2011) conceptualize, with architectural tier identity as the organizing principle. Bloom, Sadun, and Van Reenen (2012) document substantial cross-firm variation in managerial practices affecting intangible accumulation, providing empirical grounding for the cross-firm variation in w_t that the framework's propositions predict.

*Theoretical Implications for Internal Capital Markets*

The tier-allocation model introduces the architectural tier as the unit of analysis alongside the existing divisional unit. Stein (1997) establishes headquarters winner-picking across divisions; the tier-allocation framework establishes that within any division, capital is further allocated across tiers, and that this within-business allocation is as value-relevant as the cross-division allocation Stein models. The Berger and Ofek (1995) 13–15% diversification discount has an analog here: a within-business "tier-concentration discount" for firms that over-allocate to Tier 6, whose magnitude depends on the sector's decay-rate gap (δ₆ − δ_S) and the firm's discount rate. The two discounts are additive — a diversified, Tier-6-heavy firm faces both simultaneously.

The agency distortion is structurally complementary: Tier-6 managers can report advertising returns more immediately and legibly (awareness metrics, campaign-level ROI) than Tier-4 or Tier-5 managers, who face longer evaluation timelines and softer intermediate indicators. This information-asymmetry distortion is the cross-tier analog of the divisional influence costs documented by Glaser, Lopez-de-Silanes, and Sautner (2013). The frictionless benchmark here is the necessary first step; the agency extension (following section) derives the equilibrium over-allocation to Tier 6 relative to the planner's optimum.

*Agency Extension: Why Observed Tier-Allocation Diverges from the Planner's Optimum*

The frictionless planner's optimum w_t*(r) = α_t / (δ_t + r) provides the correct baseline for optimal allocation direction but understates the magnitude of the empirically observed 30–60% over-allocation to Tier 6 relative to durability-adjusted benchmarks. The gap requires a principal-agent structure.

Consider a long-horizon principal P — a founder, family firm, or patient-capital LP — who maximizes V_LR(w; r_P) at low effective discount rate r_P, and a short-tenure CEO/agent A who maximizes a horizon-truncated objective over the next T = 3–5 years. Stein (1997) formalizes how horizon mismatch and private information about project quality distort headquarters-level allocation; the same mechanics apply within a business at the tier level. The agent A cannot commit to a long investment horizon; compensation contracts tying agent reward to short-window EBITDA amplify the incentive to over-weight Tier-6 spend, whose returns manifest as measurable revenue within the contract period. Under the FOC, the agent effectively faces an inflated discount rate r_A > r_P — a truncation premium reflecting the opportunity cost of deferring payoffs beyond the agent's tenure horizon. By the comparative static ∂w_6*/∂r > 0, a higher effective r_A tilts optimal allocation toward the high-decay surface tier. The agent over-allocates not irrationally but because the agent's optimization problem has a different r than the principal's. Bertrand and Mullainathan (2003) document that managers insulated from takeover pressure systematically reduce plant creation and productivity, consistent with weaker principal control raising the agent's effective r. Aghion and Tirole (1997) formalize how formal authority and real authority diverge as information asymmetry grows, providing the general apparatus for the cross-tier distortion.

Three falsifiable predictions follow that the frictionless model cannot generate: (1) founder-CEO firms exhibit lower w_6 dollar-shares than comparable professional-CEO firms; (2) Tier-6 share rises following CEO-tenure-truncating events; (3) longer vesting horizons reduce equilibrium w_6 share, testable against Execucomp vesting-schedule data matched to XAD/sales. The full formal treatment — deriving the equilibrium (w_6^A, w_6^P) pair under adverse selection and moral hazard with tier-specific reporting legibility — is reserved for a planned companion paper.

*Theoretical Implications for Marketing Finance*

The Mizik and Jacobson (2003, 2009) empirical signature — brand-capital stock commands a valuation premium independent of current advertising spend — is a portfolio consequence of the δ₄ ≪ δ₆ differential derived in the Theoretical Foundations section. Firms accumulating Tier-4 stock while maintaining moderate Tier-6 flow achieve the valuation premium because S₄* is large and durable. Firms harvesting Tier-4 stock by diverting investment to Tier-6 flow achieve short-run earnings improvement at the cost of long-run stock depletion — exactly the trade-off Mizik and Jacobson document, now explained by the structural non-fungibility of the two investment categories. External capital-markets evidence is consistent with the model's predicted Tier-4 valuation premium. Brand Finance's *World's Most Valuable B2B Brands 2026* (Brand Finance 2026) finds that AAA-rated B2B brands trade at 20.9× EBIT, 19.7× forward P/E, and 3.4× revenue, versus 14.3×, 11.9×, and 1.0× respectively for B-rated peers (the 65% forward-P/E premium representing the headline gap). Aggregate B2B brand value reached $4 trillion in 2026, equal to approximately 11% of total enterprise value across the 300-firm sample.

*Managerial Implications*

Four practical implications follow directly. Firms approaching exit should audit tier-allocation ratios prospectively: high surface-tier intensity signals elevated goodwill-impairment risk and discounted acquisition multiples. PE-backed firms should calibrate optimal Tier-6 compression to hold-period discount rate; the residual sale creates impairment risk for the next buyer. Long-horizon investors should screen targets for w₄/w₅ share as a value indicator analogous to price-to-book. Governance structures should align the principal's effective discount rate with the tier-allocation portfolio: founder-controlled firms with Tier-6-heavy portfolios face a structural misalignment that the agency extension predicts produces equilibrium over-investment in marketing surface. Recent enterprise-survey data (Gartner 2026) corroborate this prediction: among 350 AI-deploying enterprises, 80% reported workforce reductions but the firms achieving higher ROI exhibited equivalent reduction rates to those with negative outcomes — workforce reduction at the operational tier does not, on its own, translate into the multi-tier value-creation the cascade predicts.

---

**Limitations and Scope Conditions**

Three assumptions bound the model's applicability.

*Assumption 1 — δ_t Exogeneity.* Decay rates are treated as exogenous, time-invariant constants common to all firms within a sector. This holds for mature firms in stable sectors (CPG, industrial manufacturing, financial services) where δ_t is a structural property of the tier rather than the firm. It is a boundary condition, not a failure mode: the empirical strategy targets the cross-section of S&P 1500 firms where the assumption is defensible. Endogenous δ_t — where firms invest in substrate durability — is a natural extension; relaxing this assumption is expected to strengthen the directional propositions.

*Assumption 2 — Cobb-Douglas Aggregation.* The long-run value function V_LR(w; r) = A · I · Π_t [m_t · w_t / (δ_t + r)]^{α_t} is adopted as the maintained specification throughout, following Belo, Lin, and Vitorino (2014) who employ a two-capital production function multiplicatively. The Cobb-Douglas is the tractable special case of the Milgrom-Roberts (1990, 1995) supermodularity framework: it captures cross-tier complementarities in reduced form while admitting the closed-form comparative statics that generate P1–P4. The constant-returns-to-scale constraint (Σ_t α_t = 1) ensures the B/A ratio is r-invariant while V_LR levels vary with r. The additive-separability of V_LR across tiers (Assumption 2 allows each tier's contribution to be computed independently before aggregation) is a maintained scope condition. It holds well within the firm's own architectural hierarchy; it is a boundary condition for firms embedded in tightly co-specialized partner ecosystems. Adner (2012) demonstrates that the value of any single component depends on the coordinated readiness of other ecosystem components rather than on the component's standalone substrate; Adner (2017) formalizes the ecosystem as a structure — a set of interdependent actors whose alignment determines the value of any single node — providing the theoretical architecture within which the additive-separability assumption breaks down most visibly. Firms operating at the center of dense co-specialization networks as Adner (2017) characterizes may face cross-tier interdependencies that violate additive separability; the ecosystem extension is identified as future work. A CES robustness check across σ ∈ {.5, 1.0, 1.5} is reported in Table 2 and Online Supplement S4; the B/A qualitative ordering is robust across all three elasticity values, while the sign of ∂w_6*/∂r under σ < 1 is ambiguous in the two-tier reduction (see Online Supplement S4). Increasing-returns relaxation is identified as a subsequent extension. The calibrated magnitude gap (model ~1.93× against empirical ~4–6×) closes as α_t is estimated from panel data rather than calibrated from separability priors (Appendix Priority 1).

*Assumption 3 — Allocation-vs-Financing Separability.* The cross-tier allocation problem is separable from the firm's financing decision — the cross-tier analog of Modigliani-Miller (1958). It holds when capital markets are frictionless; it fails when financial constraints bind (Stein 1997). The empirical strategy partitions by the Hadlock and Pierce (2010) SA index, conditioning the primary test on the unconstrained subsample (bottom-tercile SA) and treating the constrained subsample as a boundary-conditions robustness check. This converts a potential scope-condition violation into a testable cross-subsample prediction.

*Sector and time scope.* P1–P4 apply to firms with substantive operations across all six tiers — primarily CPG, industrial, retail, and consumer-services firms. Digital-native firms require sector-specific operationalization of the Tier-5/Tier-6 boundary but are not excluded. Single-product commodity producers face a trivial allocation problem and are excluded. The δ_t parameters are estimated from panels covering 1986–2020; post-2020 estimates require sector-specific re-estimation, particularly for δ₆ given post-2020 shifts in advertising attribution.

---

Empirical validation priorities — operationalizing the w vector from Compustat/USPTO data, testing P1–P4 with Cox hazard, matched-firm OLS, ZLB difference-in-differences, and deal-multiple regressions, and partitioning by the Hadlock and Pierce (2010) SA index — are detailed in the Appendix.

*Companion Computation Script*

Every computed numerical value reported in this paper — Profile A/B/C V_LR multipliers in the "Two-Tier Minimal Illustration" section including Table 2 (CES robustness), Figure 1 contour data, and the optimal dollar-weighted investment shares — is reproducible from a deterministic Python script published alongside the paper. Full sensitivity tables (r-sensitivity, alternative α_t calibrations, and CES derivation) are in the Online Supplement and equally reproducible. The script implements Equations 1–3 directly under the discounted-Cobb-Douglas maintained specification V_LR(w; r) = A · I · Π_t [m_t · w_t / (δ_t + r)]^{α_t} with Jorgensonian user-cost-of-capital budget constraint Σ_t (δ_t + r) · w_t = 1, hard-codes the calibrated parameters from Table 1 (decay rates δ_t, separability factors m_t, output elasticities α_t) and the Profile A/B/C w-vectors, and prints all reported values with no external data dependencies. The function `optimal_dollar_share(r)` computes the planner's optimal dollar-weighted investment shares from the FOC w_t*(r) = α_t/(δ_t + r), demonstrating the comparative static dollar-share_6*(r=.10) = .046 < dollar-share_6*(r=.15) = .053 < dollar-share_6*(r=.20) = .058. The function `reproduce_appendix_a4_ces()` implements the CES aggregator and confirms ∂w_6*/∂r > 0 under σ = 1.5 numerically via scipy.optimize. The function `generate_contour_plot()` generates Figure 1 (requires matplotlib and numpy). The script is published at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-allocation/code/back_of_envelope.py and runs as `uv run python back_of_envelope.py` (Python 3.10+; requires numpy, matplotlib, scipy for Figure 1 and Online Supplement S4). Figure 1 PNG and the contour-generation function `generate_contour_plot()` are published at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-allocation/figures/tier_allocation_contour.png and https://github.com/spectralbranding/orgschema-papers/blob/main/tier-allocation/code/back_of_envelope.py respectively.

---

**Conclusion**

By anchoring differential decay rates to tier position, the tier-allocation framework makes architectural investment direction — not merely intensity — the theoretically consequential variable. The closed-form optimum w_t*(r) = α_t / (δ_t + r) and the comparative static ∂w_6*/∂r > 0 emerge directly from the decay-rate differential and Jorgensonian user-cost structure; four propositions link this mechanism to M&A outcomes, governance, cost-of-capital shocks, and rotation-stage moderation.

Theoretical contributions proceed across three streams. For dynamic capabilities, the framework decomposes Teece's (2007) single-channel accumulation into a portfolio variable whose optimization depends on governance horizon, thereby linking managerial capabilities (Adner and Helfat 2003; Helfat and Martin 2015) to measurable investment-direction outcomes — supplying the mechanism specification that Schilke, Hu, and Helfat (2018) identify as the tradition's central gap. For resource orchestration (Sirmon et al. 2011), the allocation vector w operationalizes bundling and leveraging decisions across architectural durability layers, showing how orchestration effectiveness interacts with principal time horizons. For internal capital markets, the model demonstrates that within-business tier allocation is as value-consequential as across-division allocation (Stein 1997), generating a tier-concentration discount that compounds with the traditional diversification discount.

Future strategy research can treat organizational tier as a new unit of analysis alongside business unit, capability, and resource. The framework predicts which firms survive ownership transitions and why patient capital creates architectural advantage — questions the existing literature has answered descriptively but not yet resolved mechanistically.

---

**Online Supplement.** Mathematical derivations (Lagrangian setup, FOC, sign of ∂w₆*/∂r), sensitivity analysis to r, alternative α_t calibrations, and CES robustness check at σ ∈ {.5, 1.0, 1.5} are reported in the Online Supplement (file `Zharnikov_2026aj_Tier_Allocation_Supplement.pdf`) available as a separate file in the paper's Zenodo record at https://doi.org/10.5281/zenodo.20072288. The companion computation script (`back_of_envelope.py`) reproduces all values.

---

**Acknowledgments**

AI assistants (Claude Opus 4.7, Grok 4.1, Gemini 3.1) were used for initial literature search, editorial refinement, and implementation of the companion computation script (`back_of_envelope.py`, including the contour plot, CES robustness check, and optimal-share solver); all theoretical claims, propositions, interpretations, and numerical results are the author's sole responsibility, and all script outputs were independently verified against the closed-form derivations in Online Supplement S1.

## CRediT contributions

Zharnikov, Dmitry: Conceptualization; Methodology; Formal analysis; Writing -- original draft; Writing -- review and editing.

---

**References**

Adner, Ron. (2012). *The Wide Lens: A New Strategy for Innovation*. New York: Portfolio/Penguin. ISBN: 978-1591844600.

Adner, Ron. (2017). Ecosystem as structure: An actionable construct for strategy. *Journal of Management*, 43(1), 39–58.

Adner, Ron, and Constance E. Helfat. (2003). Corporate effects and dynamic managerial capabilities. *Strategic Management Journal*, 24(10), 1011–1025. DOI: 10.1002/smj.331.

Aghion, Philippe, and Jean Tirole. (1997). Formal and real authority in organizations. *Journal of Political Economy*, 105(1), 1–29. DOI: 10.1086/262063.

Anderson, Ronald C., and David M. Reeb. (2003). Founding-family ownership and firm performance: Evidence from the S&P 500. *Journal of Finance*, 58(3), 1301–1328. DOI: 10.1111/1540-6261.00567.

Barney, Jay. (1991). Firm resources and sustained competitive advantage. *Journal of Management*, 17(1), 99–120. DOI: 10.1177/014920639101700108.

Belo, Frederico, Xiaoji Lin, and Maria Ana Vitorino. (2014). Brand capital and firm value. *Review of Economic Dynamics*, 17(1), 150–169. DOI: 10.1016/j.red.2013.05.001.

Bennedsen, Morten, Kasper Meisner Nielsen, Francisco Pérez-González, and Daniel Wolfenzon. (2007). Inside the family firm: The role of families in succession decisions and performance. *Quarterly Journal of Economics*, 122(2), 647–691. DOI: 10.1162/qjec.122.2.647.

Berger, Philip G., and Eli Ofek. (1995). Diversification's effect on firm value. *Journal of Financial Economics*, 37(1), 39–65. DOI: 10.1016/0304-405X(94)00798-6.

Bertrand, Marianne, and Sendhil Mullainathan. (2003). Enjoying the quiet life? Corporate governance and managerial preferences. *Journal of Political Economy*, 111(5), 1043–1075. DOI: 10.1086/376950.

Bertrand, Marianne, and Antoinette Schoar. (2006). The role of family in family firms. *Journal of Economic Perspectives*, 20(2), 73–96. DOI: 10.1257/jep.20.2.73.

Bloom, Nicholas, Raffaella Sadun, and John Van Reenen. (2012). The organization of firms across countries. *Quarterly Journal of Economics*, 127(4), 1663–1705. DOI: 10.1093/qje/qje029.

Brand Finance. (2026). *World's Most Valuable B2B Brands 2026*. London: Brand Finance. https://brandirectory.com/reports/b2b

Corrado, Carol A., Charles R. Hulten, and Daniel E. Sichel. (2009). Intangible capital and U.S. economic growth. *Review of Income and Wealth*, 55(3), 661–685. DOI: 10.1111/j.1475-4991.2009.00343.x.

Dierickx, Ingemar, and Karel Cool. (1989). Asset stock accumulation and sustainability of competitive advantage. *Management Science*, 35(12), 1504–1511. DOI: 10.1287/mnsc.35.12.1504.

Doraszelski, Ulrich, and Sarit Markovich. (2007). Advertising dynamics and competitive advantage. *RAND Journal of Economics*, 38(3), 557–592. DOI: 10.1111/j.0741-6261.2007.00101.x.

Eisfeldt, Andrea L., and Dimitris Papanikolaou. (2013). Organization capital and the cross-section of expected returns. *Journal of Finance*, 68(4), 1365–1406. DOI: 10.1111/jofi.12059.

Eggers, J.P., and Sarah Kaplan. (2013). Cognition and capabilities: A multi-level perspective. *Academy of Management Annals*, 7(1), 295–340. DOI: 10.1080/19416520.2013.769318.

Erickson, Gary, and Robert Jacobson. (1992). Gaining comparative advantage through discretionary expenditures: The returns to R&D and advertising. *Management Science*, 38(9), 1264–1279. DOI: 10.1287/mnsc.38.9.1264.

Fainshmidt, Stav, Lucas Wenger, Amir Pezeshkan, and Mark R. Mallon. (2019). When do dynamic capabilities lead to competitive advantage? The importance of strategic fit. *Journal of Management Studies*, 56(4), 758–787. DOI: 10.1111/joms.12415.

Felin, Teppo, Nicolai J. Foss, and Robert E. Ployhart. (2015). The microfoundations movement in strategy and organization theory. *Academy of Management Annals*, 9(1), 575–632. DOI: 10.1080/19416520.2015.1007651.

Galbraith, Jay R. (1973). *Designing Complex Organizations*. Reading, MA: Addison-Wesley.

Galunic, D. Charles, and Kathleen M. Eisenhardt. (1996). The evolution of intracorporate domains: Divisional charter losses in high-technology, multidivisional corporations. *Organization Science*, 7(3), 255–282. DOI: 10.1287/orsc.7.3.255.

Ghemawat, Pankaj. (1991). *Commitment: The Dynamic of Strategy*. New York: Free Press. ISBN: 978-0029116715.

Ghemawat, Pankaj, and Daniel Levinthal. (2008). Choice interactions and business strategy. *Management Science*, 54(9), 1638–1651. DOI: 10.1287/mnsc.1080.0883.

Gartner. (2026, May 5). Gartner Says Autonomous Business and AI Layoffs May Create Budget Room, but Do Not Deliver Returns [press release]. Stamford, CT: Gartner. https://www.gartner.com/en/newsroom/press-releases/2026-05-05-gartner-says-autonomous-business-and-artificial-intelligence-layoffs-may-create-budget-room-but-do-not-deliver-returns

Glaser, Markus, Florencio Lopez-de-Silanes, and Zacharias Sautner. (2013). Opening the black box: Internal capital markets and managerial power. *Journal of Finance*, 68(4), 1577–1631. DOI: 10.1111/jofi.12046.

Glaum, Martin, Wayne R. Landsman, and Sven Wyrwa. (2018). Goodwill impairment: The effects of public enforcement and monitoring by institutional investors. *The Accounting Review*, 93(6), 149–180. DOI: 10.2308/accr-52006.

Gu, Feng, and Baruch Lev. (2011). Overpriced shares, ill-advised acquisitions, and goodwill impairment. *The Accounting Review*, 86(6), 1995–2022. DOI: 10.2308/accr-10131.

Hadlock, Charles J., and Joshua R. Pierce. (2010). New evidence on measuring financial constraints: Moving beyond the KZ index. *Review of Financial Studies*, 23(5), 1909–1940. DOI: 10.1093/rfs/hhq009.

Hall, Bronwyn H., Adam B. Jaffe, and Manuel Trajtenberg. (2005). Market value and patent citations. *RAND Journal of Economics*, 36(1), 16–38. DOI: 10.2307/1593752.

Hayn, Carla, and Patricia J. Hughes. (2006). Leading indicators of goodwill impairment. *Journal of Accounting, Auditing & Finance*, 21(3), 223–265. DOI: 10.1177/0148558X0602100303.

Helfat, Constance E., and Jeffrey A. Martin. (2015). Dynamic managerial capabilities: Review and assessment of managerial impact on strategic change. *Journal of Management*, 41(5), 1281–1312. DOI: 10.1177/0149206314561301.

Helfat, Constance E., and Margaret A. Peteraf. (2003). The dynamic resource-based view: Capability lifecycles. *Strategic Management Journal*, 24(10), 997–1010. DOI: 10.1002/smj.332.

Helfat, Constance E., and Margaret A. Peteraf. (2015). Managerial cognitive capabilities and the microfoundations of dynamic capabilities. *Strategic Management Journal*, 36(6), 831–850. DOI: 10.1002/smj.2247.

Jorgenson, Dale W. (1963). Capital theory and investment behavior. *American Economic Review*, 53(2), 247–259.

Lev, Baruch, and Theodore Sougiannis. (1996). The capitalization, amortization, and value-relevance of R&D. *Journal of Accounting and Economics*, 21(1), 107–138. DOI: 10.1016/0165-4101(95)00410-6.

Maksimovic, Vojislav, and Gordon Phillips. (2002). Do conglomerate firms allocate resources inefficiently across industries? Theory and evidence. *Journal of Finance*, 57(2), 721–767. DOI: 10.1111/1540-6261.00440.

Mintzberg, Henry. (1979). *The Structuring of Organizations*. Englewood Cliffs, NJ: Prentice-Hall.

Milgrom, Paul, and John Roberts. (1990). The economics of modern manufacturing: Technology, strategy, and organization. *American Economic Review*, 80(3), 511–528. DOI: 10.1257/aer.80.3.511.

Milgrom, Paul, and John Roberts. (1995). Complementarities and fit: Strategy, structure, and organizational change in manufacturing. *Journal of Accounting and Economics*, 19(2–3), 179–208. DOI: 10.1016/0165-4101(94)00382-F.

Mizik, Natalie, and Robert Jacobson. (2003). Trading off between value creation and value appropriation: The financial implications of shifts in strategic emphasis. *Journal of Marketing*, 67(1), 63–76. DOI: 10.1509/jmkg.67.1.63.18595.

Mizik, Natalie, and Robert Jacobson. (2009). Valuing branded businesses. *Journal of Marketing*, 73(6), 137–153. DOI: 10.1509/jmkg.73.6.137.

Modigliani, Franco, and Merton H. Miller. (1958). The cost of capital, corporation finance and the theory of investment. *American Economic Review*, 48(3), 261–297.

Nadiri, M. Ishaq, and Ingmar R. Prucha. (1996). Estimation of the depreciation rate of physical and R&D capital in the U.S. total manufacturing sector. *Economic Inquiry*, 34(1), 43–56. DOI: 10.1111/j.1465-7295.1996.tb01368.x.

Naik, Prasad A. (1999). Estimating the half-life of advertisements. *Marketing Letters*, 10(3), 351–362. DOI: 10.1023/A:1008158119567.

Penrose, Edith T. (1959). *The Theory of the Growth of the Firm*. Oxford: Basil Blackwell.

Peters, Ryan H., and Lucian A. Taylor. (2017). Intangible capital and the investment-q relation. *Journal of Financial Economics*, 123(2), 251–272. DOI: 10.1016/j.jfineco.2016.03.011.

Rajan, Raghuram, Henri Servaes, and Luigi Zingales. (2000). The cost of diversity: The diversification discount and inefficient investment. *Journal of Finance*, 55(1), 35–80. DOI: 10.1111/0022-1082.00200.

Ramanna, Karthik, and Richard L. Watts. (2012). Evidence on the use of unverifiable estimates in required goodwill impairment. *Review of Accounting Studies*, 17(4), 749–780. DOI: 10.1007/s11142-012-9188-5.

Scharfstein, David S., and Jeremy C. Stein. (2000). The dark side of internal capital markets: Divisional rent-seeking and inefficient investment. *Journal of Finance*, 55(6), 2537–2564. DOI: 10.1111/0022-1082.00299.

Schilke, Oliver, Songcui Hu, and Constance E. Helfat. (2018). Quo vadis, dynamic capabilities? A content-analytic review of the current state of knowledge and recommendations for future research. *Academy of Management Annals*, 12(1), 390–439. DOI: 10.5465/annals.2016.0014.

Sethi, Suresh P. (1977). Dynamic optimal control models in advertising: A survey. *SIAM Review*, 19(4), 685–725. DOI: 10.1137/1019104.

Sirmon, David G., Michael A. Hitt, R. Duane Ireland, and Brett A. Gilbert. (2011). Resource orchestration to create competitive advantage: Breadth, depth, and life cycle effects. *Journal of Management*, 37(5), 1390–1412. DOI: 10.1177/0149206310385695.

Stein, Jeremy C. (1997). Internal capital markets and the competition for corporate resources. *Journal of Finance*, 52(1), 111–133. DOI: 10.1111/j.1540-6261.1997.tb03810.x.

Teece, David J. (2007). Explicating dynamic capabilities: The nature and microfoundations of (sustainable) enterprise performance. *Strategic Management Journal*, 28(13), 1319–1350. DOI: 10.1002/smj.640.

Teece, David J. (2018). Business models and dynamic capabilities. *Long Range Planning*, 51(1), 40–49. DOI: 10.1016/j.lrp.2017.06.006.

Teece, David J., Gary Pisano, and Amy Shuen. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal*, 18(7), 509–533.

Villalonga, Belén, and Raphael Amit. (2006). How do family ownership, control, and management affect firm value? *Journal of Financial Economics*, 80(2), 385–417. DOI: 10.1016/j.jfineco.2004.12.005.

Wernerfelt, Birger. (1984). A resource-based view of the firm. *Strategic Management Journal*, 5(2), 171–180. DOI: 10.1002/smj.4250050207.

Wiggins, Robert R., and Timothy W. Ruefli. (2002). Sustained competitive advantage: Temporal dynamics and the incidence and persistence of superior economic performance. *Organization Science*, 13(1), 81–105. DOI: 10.1287/orsc.13.1.82.542.

Zharnikov, Dmitry. (2026ag). Dual hierarchies of organizational transferability: A six-tier ontology and theory of acquisition failure propagation. Working Paper. https://doi.org/10.5281/zenodo.19895813

Zharnikov, Dmitry. (2026ai). The Tier-Rotation Curve: A theory of brand-substrate decoupling and its M&A-value geometry. Working Paper. https://doi.org/10.5281/zenodo.20069605

---

## Appendix: Validation Roadmap

The present paper is a pure-deductive-theory contribution; no new data are analyzed in the main body. The following empirical priorities govern the companion validation paper.

*Priority 1 — Operationalizing the w Vector.* The tier-allocation vector w is operationalized as the firm's dollar-weighted investment share across tiers, computed from Compustat, USPTO, and SG&A decomposition data. The empirical w₆ measure is XAD / (XAD + XRD + CAPEX + org-capital SG&A component). Under Online Supplement S1 Step 5, the dollar-weighted share is dollar-share_t* = (α_t / (δ_t + r)) / Σ_s (α_s / (δ_s + r)); the empirical XAD/total-investment ratio is the observable counterpart of dollar-share_6. The w₄ share is R&D + USPTO trademark stock / total investment. The w₅ share follows the Eisfeldt and Papanikolaou (2013) perpetual-inventory method applied to organizational capital from the non-routine SG&A component. Constructing the full w vector for approximately 150 firms with at least one ownership transition event is the primary data task for the validation paper.

*Priority 2 — Testing P1 (Goodwill Impairment Hazard).* The primary empirical test is a Cox proportional hazard model of post-close goodwill impairment (Compustat GDWLIP > 0 within 36 months of deal close) on pre-deal w₆ share, with PitchBook deal-level data identifying ownership transitions. Controls include deal size (log enterprise value), deal structure (earnout indicator), sector (NAICS 3-digit), acquirer leverage, and the Hadlock and Pierce (2010) SA index of the acquirer. The instrument for w₆ endogeneity is regulatory shocks to trademark protection (Trademark Dilution Revision Act 2006; Trademark Modernization Act 2020), which shift the cost and value of Tier-4 investment and thereby instrument for cross-sectional variation in w₄ share (and, by the portfolio constraint, w₆ share).

*Priority 3 — Testing P2 (Long-Horizon Principal w-Shift).* A within-industry matched-firm OLS regression predicts w₆ share from a family-firm indicator (active family-CEO control, following Anderson and Reeb 2003 criteria) or CEO tenure (log years in post), matching on sector (NAICS 4-digit), firm size (log assets quintile), and decade. A robustness check replaces the family-firm indicator with insider ownership concentration (fraction of shares held by top-5 insiders).

*Priority 4 — Testing P4 (Rotation-Stage Interaction).* A deal-multiple regression includes an interaction term between pre-deal w₄ share and a Tier-Rotation Stage indicator (Stage 1/2 vs. Stage 3/4, proxied by the trademark-composition ratio from Zharnikov 2026ai: product-attribute marks to founder-name marks in the USPTO filing history). The interaction coefficient is predicted positive. The gender-of-first-born instrument (Bennedsen, Nielsen, Pérez-González, and Wolfenzon 2007) provides an IV for the family-firm governance indicator in P2.

*Financial Constraint Partitioning.* All four primary tests are partitioned by the Hadlock and Pierce (2010) SA index: primary tests use the unconstrained subsample (bottom-tercile SA); the constrained subsample serves as a boundary-conditions robustness check. Under Assumption 3 (financing separability), the tier-allocation comparative statics should hold in the unconstrained subsample but may be attenuated in the constrained subsample — a testable cross-subsample prediction.
