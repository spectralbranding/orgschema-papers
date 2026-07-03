# AI Tier Penetration: A Theory of Substrate-Dependent Competitive Advantage

**Dmitry Zharnikov**

ORCID: 0009-0000-6893-9231

DOI: [10.5281/zenodo.20087036](https://doi.org/10.5281/zenodo.20087036)

Working Paper v1.0.0 – May 2026

---

## Abstract

Why do identical AI investments produce sharply divergent M&A multiples despite comparable short-run productivity gains? Strategy research has examined AI spend, task exposure, and decision augmentation but has left unspecified the architectural tier at which AI-generated output accumulates. We address this omission by extending a multi-tier Jorgensonian capital-allocation model with two AI-specific shocks per tier: a cost shock γ_t that reduces effective rental prices and a durability shock Δ_t that lowers decay rates for substrate-accumulating tiers. The resulting closed-form share rule decomposes AI's consequences into price and persistence channels. Three core propositions emerge. First, surface-tier (Tier 6) cost reductions raise short-run earnings yet lower long-run M&A multiples by reallocating investment away from durable substrate. Second, a discrete substrate-building threshold exists at Tier 4: only proprietary or strongly embedded deployments generate level shifts in valuation. Third, AI's net value effect flips sign with the principal's effective discount rate — deep-tier deployments that codify tacit knowledge extend founder horizon and reinforce substrate accumulation, while surface deployments compress horizon and erode it. The complementary AI Tier Penetration Curve traces deployment depth as a dynamic-stage trajectory, reframing competitive advantage in the AI era as architectural penetration rather than investment intensity.

**Keywords**: artificial intelligence; capital allocation; firm architecture; tier durability; M&A multiples; AI strategy; substrate accumulation

---

Two firms operating in the same sector announce equal-magnitude AI investments in the same fiscal year. Each commits an identical fraction of operating budget to large-language-model deployment. Each reports comparable contemporaneous productivity gains in the same earnings cycle. Three years later, one firm trades at a forward multiple roughly twice the other's, and acquirers in the sector treat the two firms as structurally non-comparable in due diligence. No standard AI-and-strategy framework predicts this divergence. Aggregate AI-spend specifications (Babina, Fedyk, He, and Hodson 2024) treat AI investment as homogeneous; capability- or task-displacement specifications (Acemoglu and Restrepo 2018; Felten, Raj, and Seamans 2021) measure occupational exposure rather than firm architecture; cognitive-process taxonomies of AI-augmented decision making (Doshi, Bell, Mirzayev, and Vanneste 2025) classify decision micro-foundations rather than the substrate in which AI-generated output accumulates. Each supplies a necessary but incomplete unit of analysis. None pinpoints the architectural location at which the AI-augmented output lands inside the firm.

We argue that this location is first-order. When AI is deployed, its output either accumulates as durable organizational substrate or is consumed as accelerated flow. The difference is governed by the tier of deployment within a six-tier architecture ordered by transferability under M&A separation. Surface-tier deployments (marketing, customer-service chatbots) primarily cheapen current-period costs but leave no residual asset. Deeper-tier deployments (product specification, business-model mechanisms, founder intent codification) can build persistent capital whose half-life materially exceeds accounting conventions. Because M&A markets price expected future cash flows net of decay, identical AI spend can produce opposite valuation consequences depending on tier penetration.

This paper formalizes that insight. We extend the tiered capital-allocation model of Zharnikov (2026aj) with per-tier cost (γ_t) and durability (Δ_t) shocks. The generalized share rule that emerges yields three propositions. Proposition 1 (Tier-6 Paradox): surface-only cost reductions increase optimal allocation to the lowest-persistence tier, raising short-run margins while lowering long-run multiples. Proposition 2 (Substrate Threshold): durable value creation requires crossing a discrete threshold at Tier 4 from rented API capacity to proprietary or embedded configurations. Proposition 3 (Horizon Flip): AI's net effect on firm value depends on whether it extends or compresses the principal's effective decision horizon, interacting with the inherited comparative static on discount rates.

The framework contributes to three literatures. First, it supplies the missing architectural dimension to the IT-complementarity tradition (Bresnahan, Brynjolfsson, and Hitt 2002; Brynjolfsson and Hitt 1996), showing that complementarities are tier-specific rather than smoothly continuous. Second, it advances AI-and-strategy research by engaging the automation-augmentation paradox (Raisch and Krakowski 2021) — the finding that AI's net effect on firm performance depends on whether deployment replaces or amplifies human judgment — and showing that tier of deployment is the structural mechanism behind that paradox. Third, it extends dynamic capabilities (Teece 2007; Teece 2018) by decomposing reconfiguring into tier-specific persistence shocks and linking them to founder-horizon governance.

The remainder develops the theory, derives the model, states three propositions with mechanisms, introduces the AI Tier Penetration Curve as the temporal counterpart to rotation dynamics, discusses boundary conditions, and outlines implications for empirical testing. We deliberately limit scope to mature multi-tier firms capable of proprietary deployment; pure-software platforms and SMEs face different architectural collapses and resource constraints.

---

**Theory Synthesis**

The framework draws on three research traditions. The first treats information-technology capital as productive only in the presence of complementary organizational intangibles. The second examines artificial intelligence as a strategic input. The third decomposes the firm into architecturally distinct tiers ordered by transferability. The contribution sits at the intersection of all three.

**The IT-capital and architectural-tier traditions.**

The starting point is the resolution of the productivity paradox proposed by Brynjolfsson and Hitt (1996) and Hitt and Brynjolfsson (1996): IT investment yields measurable returns only when paired with organizational redesign, decentralized decision rights, and worker-skill upgrading. Bresnahan, Brynjolfsson, and Hitt (2002) sharpen this into a three-way complementarity claim — IT, workplace organization, and skilled labor are mutually complementary inputs whose joint adoption is required to capture the IT productivity gain. Tambe, Hitt, and Brynjolfsson (2012) and Tambe (2014) extend the argument to the firm's stock of IT-specific human capital. The persistence parameters used here trace to this tradition: Belo, Lin, and Vitorino (2014) estimate brand-capital depreciation at .50 per year; Eisfeldt and Papanikolaou (2013) estimate organization-capital depreciation near .15; Corrado, Hulten, and Sichel (2009) frame intangibles accounting with depreciation in the .15-to-.20 range; Lev and Sougiannis (1996) estimate R&D amortization at .12-to-.20; Hall, Jaffe, and Trajtenberg (2005) develop patent-citation knowledge stocks of similar persistence.

What this tradition cannot generate is a discrete tier-deployment prediction. The complementary-intangibles literature treats intangibles as a continuous stock and predicts smoothly increasing returns to joint IT-and-organizational-change investment. An architectural-tier framework predicts discontinuous returns at specific tier-deployment thresholds — a structurally distinct claim the present paper formalizes.

The architectural-tier tradition is grounded in five strategy-theory anchors. Penrose (1959) supplies the constraint-hierarchy logic from which architectural decomposition flows. Williamson (1985) supplies the entity-tier framing in which the legal boundary is itself a strategic artifact. Teece (2007; 2018) supplies the dynamic-capabilities tradition: dynamic capabilities are decomposed into sensing, seizing, and reconfiguring micro-foundations, and the architectural-tier ontology supplies the missing decomposition of where in the firm those activities reside as accumulating substrate. Dierickx and Cool (1989) supply the asset-stock-accumulation logic operating at Tiers 2-5: strategic asset stocks accumulate through irreversible flow commitments under time-compression diseconomies and asset-erosion processes. Pentland and Feldman (2005) supply the operative friction at Tier 5: organizational routines decompose into ostensive (codifiable) and performative (enacted) aspects, with only the ostensive aspect surviving M&A separation. The tier ontology that Zharnikov (2026ag) develops is the partition that emerges when these five anchors are jointly imposed. Appendix A re-derives it in self-contained form; the body uses the partition without further re-derivation.

**The AI-and-strategy tradition.**

The contemporary AI-and-strategy literature supplies the constructs this paper extends. Brynjolfsson, Li, and Raymond (2025) document a 15% productivity gain from generative AI in customer-service work — by the authors' own framing, a Tier-6 finding concentrated at the surface tier of customer-facing communication. Babina, Fedyk, He, and Hodson (2024) measure firm-level AI investment using job-posting data and document positive returns to AI-skill hiring, treating AI deployment as a homogeneous firm-level shock without architectural decomposition. Felten, Raj, and Seamans (2021) construct the AI Occupational Exposure index — an occupation-level measure — and find measurable productivity and wage effects on exposed occupations. Acemoglu and Restrepo (2018; 2020) provide the task-based displacement framework in which AI substitutes for tasks within occupations.

Closer to the present paper, Krakowski, Luger, and Raisch (2023) develop a capability-complementarity argument; Raisch and Krakowski (2021) frame the automation-augmentation paradox — AI's net effect depends on whether deployment replaces or amplifies human judgment, and the two modes operate differently on firm-level performance; Doshi, Bell, Mirzayev, and Vanneste (2025) propose a cognitive-process taxonomy of generative-AI-augmented strategic decision-making; Choi, Kang, Kim, and Kim (2025) document that exposure to an AI-powered decision-support system improves human strategic decision-making in pattern-recognition tasks — empirical evidence for the substrate-augmentation channel Proposition 3 attributes to deep-tier deployment; Iansiti and Lakhani (2020) supply the operating-model-as-AI thesis under which data-flywheel network effects sustain competitive advantage. Teece (2018) argues that in the digital economy, profiting from innovation requires understanding platform architectures and the standards and licensing mechanisms through which AI-era intangibles are appropriated — a direct antecedent to the tier-persistence framing here. Foss and Klein (2014) argue that managerial authority remains essential when decisions are time-sensitive, key knowledge is concentrated in the management team, and internal coordination is required — precisely the conditions under which Tier-1 founder horizon interacts with the Horizon Flip mechanism of Proposition 3.

None of these treatments decomposes AI deployment by the architectural tier of landing. The Raisch and Krakowski (2021) automation-augmentation paradox identifies the right behavioral distinction — replace versus amplify — but does not supply the architectural mechanism that determines which mode operates at which deployment level. The present paper supplies that mechanism: the tier of landing determines whether AI replaces substrate or builds it.

---

**Per-Tier AI Deployment Phenomenology**

This section traces AI deployment across the six tiers, descending from Tier 6 (where deployment density is highest in the post-2023 frontier) to Tier 1 (where hard ceilings apply). For each tier the discussion identifies the concrete deployment forms observed in the 2023-2026 frontier window, the substrate-accumulation mechanism, the per-tier (γ_t, Δ_t) shock pattern the model assigns, and the strategic implication for long-run firm value. The treatment is illustrative rather than statistical: four boundary-object cases (Klarna's customer-service deployment; Spotify's recommendation system; Bloomberg's terminal-corpus large language model; Stripe's Radar fraud-decisioning system) anchor the discussion as theory-consistent illustrations, not empirical tests. Table 1 summarizes the four cases against the per-tier (γ_t, Δ_t) shock pattern and the M&A-multiple implication the framework assigns.

*Table 1: Boundary Objects × Tier of Landing × Shock Pattern × M&A-Multiple Implication.*

| Boundary object | Primary tier of landing | γ_t pattern | Δ_t pattern | M&A-multiple implication |
|---|---|---|---|---|
| Klarna AI customer-service chatbot | Tier 6 (Organizational Surface) | γ_6 < 1 (per-resolution cost reduction; 700 FTE-equivalent labor substitution) | Δ_6 ≈ 0 (no admissible substrate at the surface tier) | Negative long-run effect through compositional shift toward lowest-substrate tier (P1 paradox) |
| Spotify recommendation system | Tier 2 (Business Model) | γ_2 < 1 (cheaper recommendation generation per user-session) | Δ_2 → δ_2^0 (data-flywheel substrate accumulating without bound under continuing user-behavior data) | Largest cross-firm dispersion among Tier-2-feasible sectors |
| BloombergGPT proprietary fine-tune | Tier 5 (Process and Operations) with Tier 4 spillover | γ_5 < 1 (lower per-document financial-language processing cost) | Δ_5 > 0 (proprietary fine-tune on proprietary corpus; non-replicable by competitors) | Positive level shift via substrate-building threshold (P2 analog at Tier 5) |
| Stripe Radar fraud-decisioning | Tier 2 (Business Model) | γ_2 < 1 (lower per-transaction fraud-screening cost) | Δ_2 > 0 (proprietary transaction-level training data; data-flywheel substrate) | Positive long-run effect; same mechanism as Spotify |

*Notes*: Primary tier of landing is the architectural location at which the durable artifact resides. Secondary-tier spillovers (e.g., BloombergGPT's terminal-embedded outputs at Tier 4) are discussed in the per-tier text. M&A-multiple implications are derived in §5; the table forecasts propositions P1, P2 against the boundary objects without establishing them.

**Tier 6 (Organizational Surface).**

Concrete Tier-6 deployment forms are the most numerous and the easiest to observe: generative marketing copy, programmatic-bidding optimization, generative-display creative, customer-service chatbots, AI-narrated audio advertising, and AI-driven SEO content. The deployment is labor-substitutive and content-multiplicative. Klarna's 2024 disclosure that an OpenAI-powered chatbot performed work equivalent to 700 full-time agents, with comparable satisfaction levels and measurable cost-per-resolution reduction, anchors the case. The mechanism is pure throughput acceleration; the artifact remains a Tier-6 communication regardless of authorship.

The persistence rate δ_6 is unchanged or worsens under widespread AI mediation. Belo, Lin, and Vitorino (2014) calibrated δ_6 ≈ .50 per year on pre-LLM advertising data, and Mizik and Jacobson (2003) show that surface-tier marketing investment trades off against value-creation investment in a way that depresses long-run firm value when surface allocation rises. There is no mechanism by which AI-generated ads persist longer than human-generated ones. Value capture diffuses to the AI infrastructure stack — model providers, hyperscalers, platforms — leaving the deploying firm with cost reduction but no durable competitive advantage. The strategic implication is the Tier-6 over-allocation paradox: γ_6 < 1 with no Δ_t shock at deeper tiers shifts the optimal allocation toward the lowest-substrate tier, raising short-run earnings while mechanically lowering the long-run M&A multiple.

**Tier 5 (Process and Operations).**

Tier-5 AI deployments codify operational routines into algorithmic execution: workflow-automation agents, internal code-generation tooling (Peng, Kalliamvakou, Cihon, and Demirer 2023 document a ~55% completion-time gain for GitHub Copilot in a controlled developer-productivity RCT), AI supply-chain optimization, AI radiology and pathology, and AI-driven scheduling. The mechanism codifies Pentland and Feldman (2005) ostensive routines into agent prompts, fine-tunes, and orchestration graphs. Codified routines transfer with the firm under M&A separation in a way that tacit routines do not.

The persistence effect splits sharply by deployment configuration. BloombergGPT (Wu, Irsoy, Lu, Dabravolski, Dredze, Gehrmann, Kambadur, Rosenberg, and Mann 2023) is the proprietary-fine-tune exemplar: a 50-billion-parameter model trained on the terminal corpus produces domain-specific performance that materially exceeds general-purpose models, the fine-tune is non-replicable by competitors lacking corpus access, and the corpus continues to grow with the firm's operations — generating Δ_5 > 0. Klarna's chatbot, by contrast, is API-only on a third-party foundation model: the firm captures cost reduction but does not accumulate proprietary AI substrate (γ_5 < 1, Δ_5 ≈ 0). Two firms with identical Tier-5 AI spend can have radically different M&A consequences depending on whether their deployment built proprietary substrate or rented commodity capacity.

**Tier 4 (Product Specification and Brand Codification).**

The Tier-4 substrate-accumulation pattern predates AI. Hermès commits roughly five percent of revenue to marketing while LVMH peers commit thirteen to fourteen percent; the marketing-surface gap is invested instead in atelier capacity, leather-sourcing specifications, and saddle-stitch training, and the resulting EV/EBITDA premium has persisted at three to five turns above Kering and LVMH for over a decade. Apple under Steve Jobs (1997-2011) ran marketing at five to seven percent of revenue against Samsung Electronics' twelve to fifteen percent while reinvesting in industrial-design depth; the firm's cash position rose from $1.2 billion to $76 billion across the same window. Costco runs advertising at five basis points of revenue against Walmart's sixty and Target's two hundred while building Kirkland-Signature private-label specifications and supplier-audit infrastructure; EV/EBITDA has held above twenty for a decade. The pattern is the Tier-4 substrate-building threshold of Proposition 2 firing in the pre-AI regime: firms that allocate to product-specification depth rather than marketing-surface frequency compound a different asset on the balance sheet, with a longer half-life. AI deployment at Tier 4 is the latest instance of this enduring architectural pattern, not a new phenomenon — the new question is which AI configurations build substrate (γ_4 < 1 with Δ_4 > 0) versus rent it (γ_4 < 1, Δ_4 ≈ 0).

Tier-4 AI deployment itself splits into three sub-cases: AI-as-product (Anthropic's Claude, OpenAI's GPT, Cursor, Perplexity); AI-as-feature embedded in non-AI-native products (Apple Intelligence in iPhone, Notion AI, Klarna's AI shopping assistant); and AI-codified product specification, where AI output is the product specification of a software firm (Cursor and Claude Code generate code that is the substantive specification of a software product).

The substrate-building threshold Δ_4 > 0 applies under two conditions: owned model weights (hyperscalers and frontier-model firms), or strong embedding-context switching costs (the user invests in customizing the AI to their workflow, the AI accumulates user documents and behavioral patterns, and switching to a competitor erases the customization investment). Tier 4 is the first tier at which AI deployment can simultaneously cheapen factor cost and build durable substrate, and cross-sectional dispersion in firm-level AI returns is concentrated at Tier 4 — a claim §5 develops as Proposition 2.

**Tier 3 (Business Entity).**

Tier-3 AI deployments cover legal and regulatory work supporting the firm's entity layer: AI contract drafting (Harvey, Spellbook, Ironclad), AI compliance monitoring (Hummingbird AI, Behavox), AI tax structuring inside Big Four practices, AI-augmented audit (KPMG Clara, Deloitte's Omnia), AI-assisted regulatory filings, and AI-prepared due-diligence document review. The mechanism is labor substitution at the legal and compliance staff level. The artifact — the contract, the filing, the audit working paper — transfers with the entity in M&A regardless of authorship; legal enforceability is independent of authorship, contingent on a human-principal signature where required.

The persistence rate δ_3 is unchanged. The entity's persistence is a function of legal-system durability, not the means of drafting. AI is purely a γ_3 cost shock with no Δ_3 component. The hard ceiling is legal personhood: AI cannot sign as a legal person, enter contracts as principal, bear liability, or serve as registered agent or fiduciary. The exception case is the autonomous-agent legal-entity structure: Wyoming's DAO LLC statute (Wyo. Stat. Ann. §§ 17-31-101 to 17-31-115, 2021), Vermont's Blockchain-Based LLC statute (11 V.S.A. §§ 4172-4176, 2018), and the Republic of the Marshall Islands DAO Act of 2022 allow some decentralized-autonomous-organization structures to register as limited-liability entities. The doctrinal nuance, established in CFTC v. Ooki DAO, No. 3:22-cv-05416-WHO (N.D. Cal. June 8, 2023; Orrick, J.), is that the DAO itself is a legal person — an unincorporated association under California law — capable of being sued and bound by injunction. The framework treats the legal-personhood ceiling as constitutional rather than technological: capability improvement alone does not move it.

**Tier 2 (Business Model).**

Tier-2 AI deployment splits into two sub-forms. Sub-form 2a, AI as strategy advisor (founders use language models for pricing brainstorms; consultancies use them for draft work; CFOs use them for unit-economics modeling), is consultative not constitutive — δ_2 unchanged, Δ_2 ≈ 0. Sub-form 2b is AI as the business-model mechanism itself: Spotify's recommendation system, Stripe Radar's fraud-decisioning, Uber's surge pricing, TikTok's recommendation algorithm. The data-flywheel mechanism distinguishes sub-form 2b: user behavior generates training data, training data improves the AI capability, improved capability attracts more users. The same foundation model is available to competitors, but the data is not transferable. Strong increasing returns in the data flywheel drive Δ_2 → δ_2, so the effective decay rate collapses toward zero under continuing data accumulation. Cross-firm dispersion in long-run AI returns is largest at Tier 2; two firms in the same sector with identical aggregate AI spend but different Tier-2 deployment depth can exhibit M&A multiples differing by 2× to 5×.

**Tier 1 (Owner Intent).**

Tier-1 AI deployment is bounded by three layered ceilings: legal personhood, specification impossibility, and moral-political legitimacy. Currently feasible patterns are AI as decision-support extending the principal's effective horizon, AI as proxy under existing trust law for routine decisions specified in advance, and DAO governance with AI-agent participation under Wyoming/Vermont/Marshall Islands statutes. Specification impossibility (Zharnikov 2026h) imposes a residual specification gap at Tier 1: in high-dimensional preference spaces the set of contexts in which the principal might have to act is combinatorially larger than any finite specification, and preferences themselves are the substrate from which specifications are derived, so any AI implementing a specified-in-advance preference set under novel circumstances will produce decisions whose legitimacy is contestable.

The framework's Tier-1 prediction operates not through w_1 (which is not in the allocation vector) but through the principal's discount rate r. AI that extends the principal's horizon — surviving founder partial-incapacity, extending decision capacity over a larger surface — lowers effective r. AI that compresses the principal's horizon — algorithmic-feedback decision loops shortening time preference toward shareholder-quarterly logic — raises effective r. The sign of AI's effect on r determines the sign of AI's value effect through the framework's comparative statics, a claim §5 develops as Proposition 3.

---

**Formal Model Extension**

This section extends the Cobb-Douglas + Jorgensonian tier-allocation model recapped in Appendix A.3 by introducing two AI-specific shock parameters per tier: a cost shock γ_t ∈ (0, 1] that cheapens factor cost at tier t, and a durability shock Δ_t ∈ [0, δ_t^0) that raises substrate persistence at tier t by lowering the per-period decay rate. The closed-form share rule generalizes naturally; the comparative-statics structure that drives Propositions P1-P3 follows from the generalized first-order conditions stated below. Full algebraic derivation, log-concavity verification, and signs of ∂w_t*/∂γ_t and ∂w_t*/∂Δ_t are in Online Supplement S1.

*Recap of the inherited base model.*

The starting point is the multi-tier extension of the Belo, Lin, and Vitorino (2014) two-capital production function. Each tier t accumulates a stock S_t according to the linear differential equation dS_t/dτ = w_t · I − δ_t · S_t, where w_t ∈ [0, 1] is the tier-t allocation share, I is total annual investment, and δ_t > 0 is the tier-specific decay rate calibrated in Appendix A.2 below (δ_6 = .50; δ_5 ≈ .175; δ_4 ≈ .15; δ_3 ≈ δ_2 ≈ .075). Long-run value aggregates the tier stocks via a constant-returns-to-scale Cobb-Douglas production function:

V_LR(w; r) = A · I · ∏_t [m_t · w_t / (δ_t + r)]^{α_t}

where A > 0 is a productivity scalar, m_t ∈ [0, 1] is the tier-t M&A separability factor (m_6 = .25; m_4 = m_5 = 1.0; m_2 = m_3 = .6), α_t ∈ (0, 1) is the tier-t output elasticity satisfying Σ_t α_t = 1, and r is the principal's effective discount rate. The denominator term (δ_t + r) is the Jorgensonian (1963) per-period user cost of capital for tier t. Optimization of ln V_LR(w; r) subject to the rental-rate budget constraint Σ_t (δ_t + r) · w_t = 1 yields the closed-form interior optimum w_t*(r) = α_t / (δ_t + r), with the comparative static ∂w_6*/∂r > 0 following from sign(δ_6 − δ_S) > 0, where δ_S = .119. Appendix A.3 provides the self-contained re-derivation; the present section adds AI-specific shocks.

*The two AI-specific shocks.*

AI deployment at tier t enters the model through two channels. The first is a cost shock γ_t ∈ (0, 1] that scales the per-tier rental price downward: the firm faces effective rental price q_t(γ) = γ_t · (δ_t + r) per unit of tier-t allocation, with γ_t = 1 corresponding to no AI cost reduction at that tier and γ_t < 1 corresponding to AI-driven labor substitution, throughput multiplication, or input-cost compression. The Klarna chatbot deployment illustrates the canonical γ_6 < 1 case: AI substitutes for the customer-service workforce and the per-resolution cost falls without any change in the durability of the underlying surface artifact. The second channel is a durability shock Δ_t ∈ [0, δ_t^0) that raises substrate persistence at tier t by lowering the effective per-period decay rate. Define the effective decay rate as

δ_t^eff = δ_t^0 − Δ_t

where δ_t^0 is the inherited pre-AI persistence rate from Appendix A.2 and Δ_t is the AI-induced persistence improvement. The BloombergGPT case illustrates the Δ_5 > 0 case: a proprietary fine-tune trained on a proprietary corpus that continues to grow with the firm's operations generates a durable Tier-5 substrate whose effective decay rate is materially below the pre-AI baseline. The Spotify recommendation engine illustrates the Δ_2 → δ_2^0 limit case: a data-flywheel substrate whose persistence approaches infinite half-life under continuing data accumulation. The two shocks are conceptually distinct: γ_t operates on the price of tier-t allocation while Δ_t operates on the productivity of tier-t accumulation.

*The generalized long-run value function.*

Substituting the effective decay rate δ_t^eff = δ_t^0 − Δ_t into the inherited V_LR and adding the per-tier cost shock γ_t to the budget constraint produces the generalized long-run value function:

V_LR(w; r, γ, Δ) = A · I · ∏_t [m_t · w_t / (δ_t^eff + r)]^{α_t}

subject to the generalized Jorgensonian budget constraint:

Σ_t γ_t · (δ_t^eff + r) · w_t = 1

The generalized value function preserves the structural properties of the inherited base model. Cobb-Douglas log-concavity is unchanged: ∂² ln V_LR / ∂w_t² = − α_t / w_t² < 0 holds for any (γ, Δ) within the admissible parameter range, so the planner's optimum remains uniquely interior. Constant returns to scale is unchanged: V_LR scales linearly with total investment I because Σ_t α_t = 1, and the AI shocks do not enter through I but through the per-tier price-and-persistence vector.

*The Lagrangian and the generalized share rule.*

The interior optimum follows from Lagrangian maximization of ln V_LR(w; r, γ, Δ) subject to the generalized budget constraint. The Lagrangian is:

L = ln A + ln I + Σ_t α_t · [ln m_t + ln w_t − ln(δ_t^eff + r)] − λ · [Σ_t γ_t · (δ_t^eff + r) · w_t − 1]

The first-order condition with respect to w_t is:

α_t / w_t − λ · γ_t · (δ_t^eff + r) = 0

which implies w_t*(r; γ, Δ) = α_t / [λ · γ_t · (δ_t^eff + r)]. Substituting into the budget constraint and using Σ_t α_t = 1 under constant returns to scale, λ = 1 and the interior optimum simplifies to the **generalized closed-form share rule:**

**w_t*(r; γ, Δ) = α_t / [γ_t · (δ_t^eff + r)]**

The dollar-weighted (empirically observable) tier-t share is:

dollar-share_t*(r; γ, Δ) = w_t*(r; γ, Δ) / Σ_s w_s*(r; γ, Δ) = (α_t / [γ_t · (δ_t^eff + r)]) / Σ_s (α_s / [γ_s · (δ_s^eff + r)])

This is the central formal anchor of the paper. The three propositions P1-P3 of §5 follow from differentiating the generalized share rule with respect to γ_t and Δ_t under specific tier-deployment patterns. Online Supplement S1 carries the full derivation.

*Calibration.*

Table 2 summarizes the per-tier persistence δ_t, output elasticity α_t, and M&A separability m_t calibration. The persistence values are externally anchored to the IT-capital-and-intangibles tradition; the elasticity and separability values are calibrated from the architectural rationale of Appendix A.1.

*Table 2: Per-Tier Calibration Values for δ_t, α_t, m_t.*

| Tier | Tier name | δ_t (annual decay) | α_t (output elasticity) | m_t (M&A separability) | Persistence source |
|---|---|---|---|---|---|
| 6 | Organizational Surface | .50 | .12 | .25 | Belo, Lin, and Vitorino (2014); Naik (1999) |
| 5 | Process and Operations | .175 (range .15-.20) | .24 | 1.0 | Eisfeldt and Papanikolaou (2013); Corrado, Hulten, and Sichel (2009) |
| 4 | Product Specification | .15 (range .12-.20) | .24 | 1.0 | Lev and Sougiannis (1996); Hall, Jaffe, and Trajtenberg (2005) |
| 3 | Business Entity | .075 (range .05-.10) | .20 | .60 | Wiggins and Ruefli (2002); Williamson (1985) framing |
| 2 | Business Model | .075 (range .05-.10) | .20 | .60 | Wiggins and Ruefli (2002); Penrose (1959) framing |
| 1 | Owner Intent | n/a (not in allocation vector) | n/a | n/a | Operates through r, not w_t |

*Notes*: δ_t values are pre-AI persistence rates (δ_t^0 in §4). α_t values are calibrated proportional to m_t and normalized to sum to 1 across Tiers 2-6; constant returns to scale Σ_t α_t = 1. m_t values follow the architectural rationale of Appendix A.1. The aggregate substrate-tier persistence rate δ_S = .119/year is the investment-weighted aggregate of δ_2 through δ_5. Tier 1 enters the framework through the principal's effective discount rate r rather than through an allocation share.

The Cobb-Douglas (σ = 1) specification is maintained throughout. Online Supplement S2 reports a CES robustness check at σ ∈ {.5, 1.0, 1.5} for the AI-extended model and finds that the sign of ∂(dollar-share_6*)/∂γ_6 < 0 is preserved across the elasticity range, with the gross-substitutes case strengthening the prediction and the gross-complements case attenuating it without sign reversal.

---

**Three Core Propositions**

The three propositions P1 through P3 follow from differentiating the generalized share rule w_t*(r; γ, Δ) = α_t / [γ_t · (δ_t^eff + r)] under specific patterns of AI deployment. Each proposition is stated with its derivation, mechanism, and diagnostic indicators for empirical testing. The three remaining comparative statics — Tier-2 moat asymmetry, penetration-depth ordering, and rotation acceleration — follow as auxiliary implications developed in §8.2.

*Proposition 1 (Tier-6 Over-Allocation Paradox).*

When AI is concentrated at Tier 6 with γ_6 ∈ (0, 1) and γ_t = 1 for t ≤ 5 and all Δ_t = 0, the optimal Tier-6 share rises monotonically as γ_6 falls: ∂(dollar-share_6*)/∂γ_6 < 0. The mechanism is a relative-price substitution: γ_6 < 1 lowers the effective rental price at Tier 6 while substrate-tier prices stay fixed, so the optimizer reallocates toward the cheapened factor. Total V_LR rises because output per dollar increases, but the composition shifts toward the lowest-substrate tier — and at Tier 6 most of the AI-driven gain is consumed as flow rather than accumulated as substrate, because δ_6 = .50 is the largest decay rate in the calibrated vector.

The M&A-multiple consequence is predictable from the share rule. The long-run firm value is

V_LR(w*; r, γ, Δ) = A · I · ∏_t [m_t · α_t / (γ_t · (δ_t^eff + r)²)]^{α_t}

When γ_6 falls and deeper-tier shocks are unchanged, V_LR rises in the short run (higher throughput at the surface tier reduces current-period costs), but the M&A multiple — priced on expected long-run substrate — falls, because the optimal allocation shifts further toward the lowest-persistence tier, compounding the substrate erosion. The formal derivation is in Online Supplement S1 (Proposition S1.1).

The diagnostic indicator is the joint observation of two contemporaneous patterns in the same firm: positive EBIT shifts alongside negative 36-month forward M&A-multiple shifts, in firms deploying AI exclusively at Tier 6.

*Falsification*: P1 is falsified if firms with exclusively Tier-6 AI deployment show no negative 36-month forward M&A-multiple shift conditional on a positive contemporaneous EBIT shift, in samples matched on aggregate AI investment intensity.

*Proposition 2 (Substrate-Building Threshold at Tier 4).*

When γ_4 ∈ (0, 1) is paired with Δ_4 > 0, the long-run Tier-4 stock S_4* = w_4 · I / δ_4^eff exhibits a super-linear response to (γ_4^{-1} · Δ_4): both γ_4 and δ_4^eff = δ_4^0 − Δ_4 enter the share-rule denominator, and the stock denominator depends only on δ_4^eff. The first-positive-Δ_4 threshold — the point at which Tier-4 AI crosses from API-rented capacity to proprietary-fine-tune or owned-weights configuration — produces a level shift in M&A multiples rather than a continuous slope shift, because the substrate-building effect is conditional on owned-substrate or strong embedding-context switching costs.

The formal derivation is in Online Supplement S1 (Proposition S1.2): ∂S_4*/∂Δ_4 > 0, with the level-shift interpretation arising from the structural distinction between Δ_4 = 0 (API-only, γ-shock only, no substrate accumulation) and Δ_4 > 0 (proprietary, substrate-building component becomes admissible). The discrete-tier cleavage at Tier 4 is structurally distinct from a continuous "intangibles" measure; a continuous-intangibles specification cannot generate the threshold discontinuity this proposition predicts.

The diagnostic indicator is a discontinuity in M&A multiples at the disclosure-coded Δ_4 threshold within a sample matched on aggregate AI investment intensity. A continuous-slope finding without threshold discontinuity would be inconsistent with the proposition.

*Falsification*: P2 is falsified if firms crossing the disclosure-coded Δ_4 threshold show no level shift in M&A multiples relative to firms remaining at Δ_4 = 0, in samples matched on aggregate AI investment intensity.

*Proposition 3 (Horizon-Conditional Sign Flip).*

Proposition 3 is the deepest implication of the framework. AI deployment at deep tiers (Tier 4, Tier 2) extends the principal's effective decision horizon by codifying tacit knowledge into substrate surviving founder-incapacity events; AI deployment at shallow tiers (Tier 6) compressed by algorithmic-feedback loops and shareholder-quarterly logic raises the effective discount rate. When AI extends horizon (effective r falls), the inherited ∂w_6*/∂r > 0 comparative static shifts allocation away from Tier 6 toward substrate tiers, and AI's value effect is positive in both short and long run. When AI compresses horizon (effective r rises), allocation shifts toward Tier 6: AI's value effect is positive short-run (margin expansion at Tier 6) but negative long-run (substrate erosion at Tiers 4 and 2). Two firms with identical aggregate AI spend can have opposite long-run-value effects depending on whether deployment extends or compresses horizon.

This mechanism connects the framework to the automation-augmentation paradox of Raisch and Krakowski (2021): surface deployments that automate judgment-proxies compress horizon (higher r), while deep deployments that augment tacit founder knowledge extend it (lower r). The sign-flip is therefore the formal-model expression of the paradox at the firm-valuation level. Foss and Klein (2014) supply the governance micro-foundation: managerial authority persists precisely because decisions are time-sensitive and key knowledge is concentrated — the conditions under which the principal's effective horizon is the binding strategic constraint.

The positive sign of ∂w_6*/∂r holds under the maintained Cobb-Douglas (σ = 1) and CES with σ ≥ 1; under σ < 1 (gross complementarity) the sign may attenuate or reverse in highly co-specialized portfolios. Online Supplement S2 reports the CES robustness across σ ∈ {.5, 1, 1.5}, with the σ = .5 sign-attenuation case explicitly disclosed; the proposition's primary scope is therefore σ ≥ 1, the empirically modal regime in multi-tier capital structures.

The diagnostic indicator is a sign flip in the long-run-value effect of AI between long-horizon principals (founder-CEOs, family-firm controlled, low institutional concentration) and short-horizon principals (high institutional concentration, activist-pressured), at matched aggregate AI spend. Identification requires AI-deployment-depth measures paired with founder-horizon proxies (Bennedsen, Nielsen, Pérez-González, and Wolfenzon 2007 instrument; founder-CEO tenure; institutional-concentration measures).

*Falsification*: P3 is falsified if no sign flip in the long-run AI-value effect is observed between long-horizon and short-horizon principals at matched aggregate AI spend, conditional on σ ≥ 1 prevailing in the sample's tier-complementarity structure.

Aggregate enterprise-survey evidence is consistent with P3. Gartner (2026) surveyed 350 global enterprises with at least $1 billion in revenue, all of which were piloting or deploying autonomous AI capabilities. Eighty percent reported workforce reductions tied to AI initiatives. Critically, the workforce-reduction rate was nearly identical for firms reporting higher ROI versus those experiencing only modest gains or negative outcomes — i.e., the magnitude of workforce reduction had no measurable correlation with ROI realization. Some respondents had cut up to 20% of headcount. The Klarna and BloombergGPT cases are not isolated anomalies; they are predictable consequences of treating tier-6 cost reduction as a substitute for cascade-deeper substrate investment. As Gartner Distinguished VP Analyst Helen Poitevin stated: "Many CEOs turn to layoffs to demonstrate quick AI returns; however, this disposition is misplaced. Workforce reductions may create budget room, but they do not create return."

*Table 3: Three Core Propositions with Mechanisms and Diagnostic Indicators.*

| Proposition | Shock pattern | Sign condition | Diagnostic indicator | Illustrative anchor |
|---|---|---|---|---|
| P1 Tier-6 Over-Allocation Paradox | γ_6 < 1; γ_t = 1 for t ≤ 5; Δ_t = 0 | ∂(ds_6\*)/∂γ_6 < 0; long-run V_LR↓ while contemporaneous EBIT↑ | Positive contemporaneous EBIT shift jointly with negative 36-month forward M&A-multiple shift, in firms with surface-only AI deployment | Klarna chatbot (Tier 6) |
| P2 Substrate-Building Threshold at Tier 4 | γ_4 < 1 paired with Δ_4 > 0 | δ_4^eff = δ_4^0 − Δ_4; super-linear stock response in (γ_4^{−1}·Δ_4) above the Δ_4 = 0 threshold | Discontinuity in M&A multiples at the disclosure-coded Δ_4 threshold, in samples matched on aggregate AI investment intensity | BloombergGPT proprietary fine-tune |
| P3 Horizon-Conditional Sign Flip | AI shifts effective r per tier of deployment | sign(∂V_LR/∂AI) flips with sign(∂r/∂AI), via inherited ∂w_6\*/∂r > 0 | Sign flip in long-run-value effect of AI between long-horizon and short-horizon principals at matched aggregate AI spend | Founder-CEO panel + Bennedsen et al. (2007) instrument |

*Notes*: Mechanism for P1 is relative-price substitution toward the cheapened surface tier (δ_6 = .50 is the largest decay rate in the calibrated vector; the M&A multiple prices substrate not throughput). Mechanism for P2 is that proprietary fine-tunes or owned-weights configurations make substrate accumulation admissible at Tier 4, so the same aggregate spend produces different durability consequences. Mechanism for P3 is that surface deployment raises effective r by automating judgment-proxies while deep deployment lowers r by augmenting tacit founder knowledge — the formal-model expression of Raisch and Krakowski's (2021) automation-augmentation paradox. Diagnostic indicators are qualitative signatures for empirical testing, not preregistered effect-size floors. The framework's primary contribution is deductive derivation of the three mechanisms; the empirical follow-on is a validation roadmap.

---

**Implications for Empirical Testing**

The framework's propositions are testable conditional on operationalizing the per-tier deployment-depth vector (γ̂_t, Δ̂_t) at the firm-year level. This section sketches the testable implications and identification challenges qualitatively. Full instrument specifications, dictionary exemplars, and the threats-to-identification structure are in Online Supplement S4.

*Operationalizing tier deployment depth.*

The methodological precedent is Hassan, Hollander, van Lent, and Tahoun (2019), whose text-based political-risk method constructs firm-quarter scores from earnings-call transcripts using a dictionary plus context filter. The tier-depth measure applies that template to AI-related disclosure language: 10-K Item 1A, Item 7 MD&A, and earnings-call transcripts are coded for deployment artifacts per tier. Tier-6 exemplar phrases include "generative marketing copy," "AI customer-service chatbot"; Tier-5 exemplars include "proprietary fine-tune," "owned model weights"; Tier-4 exemplars include "AI-as-product," "embedding-context switching cost"; Tier-2 exemplars include "data flywheel," "recommendation engine constitutive of product." Loughran and McDonald (2011) supplies the finance-domain calibration discipline; Hoberg and Phillips (2016) supplies the text-based-classification validation precedent.

*Identification challenges.*

Three first-order challenges apply. First, selection on unobservables: firms ready for Tier-4 deployment in 2022 had superior pre-existing data infrastructure correlated with subsequent outcomes through non-AI channels. Diagnostic mitigations include pre-trends testing, firm fixed effects, and entropy-balancing on size, intangible intensity, and prior R&D spend. Second, parallel-trends: GPT-3 → GPT-4 → GPT-5 capability-frontier shocks correlate with broader tech-sector time trends. Mitigations include sector-by-time fixed effects, placebo DiD on capital-light service sectors (Callaway and Sant'Anna 2021; De Chaisemartin and D'Haultfœuille 2020), and Oster (2019) coefficient-stability bounds. Third, founder-horizon endogeneity: founder-CEO status is itself an outcome of past performance, so horizon proxies are endogenous to the firm-value outcomes P3 attempts to explain. The Bennedsen, Nielsen, Pérez-González, and Wolfenzon (2007) gender-of-first-born instrument provides partial relief, though its first-stage strength has weakened in the post-2010 governance environment.

A fourth concern is the separability of γ_t and Δ_t in disclosure data. A 10-K passage describing "a proprietary fine-tune that has reduced our customer-service operating cost while building a defensible asset" may reflect γ_5 reduction, Δ_5 increase, or both, and clean separate identification may be infeasible with public data. The framework explicitly acknowledges this constraint: empirical implementation may reduce to joint identification of (γ_t, Δ_t) at the tier level. Joint identification is sufficient for P1 and P2 but not for the Δ_t-specific channel of Proposition 3. Full identification threats and proposed mitigations are developed in Online Supplement S4.

---

**Boundary Conditions and Scope**

The framework's claims are conditional on four scope axes — sector, firm size, time, and capability frontier — and on the founder-horizon discount rate r as the operative conditioning variable.

*Sector scope.* The framework applies to mature firms with substantive operations across multiple architectural tiers. Three sector configurations fit less cleanly. Pure software and digital-native platforms collapse Tier-5 process and Tier-6 surface into a single platform-engineering function; for such firms, AI deployment is often inherently Tier 4 or Tier 2, and the surface-tier paradox does not arise in the predicted form. Pure financial-services firms face a regulatory architecture that tightly couples Tier 3 and Tier 4, so AI deployment must navigate a regulatory layer that constrains the tier-assignment protocol. Single-product, single-tier firms present trivial cross-tier decomposition; the framework's predictions reduce to the textbook IT-capital result.

*Firm-size scope.* Deep-tier AI deployment requires resource commitments small firms typically cannot afford. Proprietary fine-tunes on owned data, owned-weights deployment, data-flywheel architecture sufficient to drive Δ_2 toward δ_2, and the firm-internal infrastructure to operate these systems at scale all impose minimum-viable-asset thresholds. The framework's full prediction set applies primarily to S&P 1500-scale firms. For smaller firms, the framework's predictions concentrate on Stages 1 and 2 (Tier-6 surface adoption and shallow Tier-5 process deployment).

*Time and capability-frontier scope.* The persistence parameters δ_t are calibrated from 1986-2026 panel data. The AI shock parameters γ_t and Δ_t are calibrated for the 2023-2026 deployment window. The framework's directional predictions are robust to recalibration because they depend on sign conditions — sign(δ_6 − δ_S) and sign(Δ_t) — rather than on point estimates.

*The founder-horizon r as the conditioning variable.* Predictions are sharper for low-r principals (founder-CEO control, family-firm governance) because the substrate-accumulating tiers carry larger optimal allocation shares, so deviations produce larger M&A-multiple effects. Predictions for high-r principals are weaker because the planner's optimal Tier-6 share is already large and AI shocks produce smaller incremental compositional shifts.

---

**Discussion**

**Tier-Penetration vs. existing AI-and-strategy literature.**

The framework's contribution is not to displace the existing AI-and-strategy literature but to add a per-tier deployment-depth aggregation that the leading specifications operate orthogonally to. Aggregate-AI-spend specifications (Babina, Fedyk, He, and Hodson 2024) treat AI investment as a homogeneous firm-level shock. Task-displacement specifications (Acemoglu and Restrepo 2018; 2020) decompose AI's labor-market effect at the task level within occupations. Capability-complementarity specifications (Krakowski, Luger, and Raisch 2023) operate at the capability level — but capabilities live across architectural tiers, and the same capability deployed at different tiers has different durability consequences. Cognitive-process taxonomies (Doshi, Bell, Mirzayev, and Vanneste 2025) classify generative-AI-augmented strategic decisions into search, representation, and aggregation sub-processes; the taxonomy operates at the decision-evaluation micro-foundation level, while the tier framework operates at the architectural-substrate level. Table 4 makes the contrast explicit.

*Table 4: Tier-Penetration Framework vs. Existing AI-and-Strategy Literatures.*

| Prediction or property | Tier-Penetration | Complementary-intangibles | Aggregate-AI-spend | Cognitive-process | Task-displacement |
|---|---|---|---|---|---|
| Cross-sectional dispersion in AI returns | Predicted via tier-mix | Via continuous intangibles | Not predicted (homogeneous AI) | Via decision-evaluation type | Via task automatability |
| P1 Tier-6 over-allocation paradox | Sharp; closed-form via γ_6 < 1 | No discrete prediction | No prediction | No prediction | No prediction |
| P2 Tier-4 threshold (Δ_4 > 0 → multiple jump) | Sharp; level shift | No (continuous) | No prediction | No prediction | No prediction |
| P3 Horizon-conditional sign flip | Sharp; sign of long-run effect flips with sign(∂r/∂AI) | No prediction | No prediction | No prediction | No prediction |
| Short-run productivity | Real but composition-shifted to Tier 6 | Via intangibles | Via AI investment | Via decision type | Via task automatability |
| Unit of analysis | Firm-tier-deployment | Firm | Firm | Decision-task | Task |
| Functional form | Cobb-Douglas + tier-Jorgensonian + (γ_t, Δ_t) | Reduced-form with intangibles index | Reduced-form with AI exposure | Taxonomic | Task-displacement production |

*Notes*: Column labels for the four comparison frameworks abbreviate: Tambe-Hitt-Brynjolfsson complementary-intangibles tradition; Babina, Fedyk, He, and Hodson (2024) aggregate-AI-spend specifications; Doshi, Bell, Mirzayev, and Vanneste (2025) cognitive-process taxonomy; Acemoglu and Restrepo (2018; 2020) task-displacement framework. The framework's marginal contribution sits at the unit-of-analysis row (firm-tier-deployment): the existing literatures aggregate over architectural tiers and therefore cannot generate the cross-tier deployment-depth predictions P1-P3.

**The short-run-productivity vs. long-run-substrate cleavage.**

The framework explicitly reconciles P1 with Brynjolfsson, Li, and Raymond (2025). Brynjolfsson, Li, and Raymond document a 15% productivity gain from generative AI in customer-service work — entirely consistent with what P1 predicts at the surface tier: γ_6 < 1 lowers per-resolution cost at Tier 6 and the contemporaneous EBIT effect is positive. The framework's prediction is not that AI fails to raise productivity at Tier 6 — it does — but that the same cost reduction shifts the optimal allocation toward the lowest-substrate tier, depleting allocation to substrate-accumulating tiers, and lowering the long-run M&A multiple even as short-run earnings rise. Short-run productivity, the dependent variable in Brynjolfsson, Li, and Raymond (2025), and long-run M&A multiple, the dependent variable in the present paper, are measured on different margins.

**The AI Tier Penetration Curve as temporal companion to the Tier-Rotation Curve.**

The AI Tier Penetration Curve is the stage-model construct that translates the cross-sectional comparative statics of P1-P3 into a temporal trajectory of firm AI deployment depth. Stage 0 (pre-deployment) describes firms with no generative-AI deployment. Stage 1 (surface adoption) confines deployment to Tier 6. Stage 2 (process penetration) extends deployment to Tier 5, distinguishing Stage 2a (API-only, γ_5 < 1, Δ_5 ≈ 0) from Stage 2b (proprietary fine-tune, γ_5 < 1 paired with Δ_5 > 0). Stage 3 (product penetration) reaches Tier 4 and is the first stage at which M&A multiples meaningfully rise via the substrate-building threshold P2. Stage 4 (business-model penetration) reaches Tier 2, with the data-flywheel substrate driving Δ_2 toward δ_2 and cross-firm dispersion maximized. Stage 5 (asymptotic ceiling) describes the bounded approach to Tier-3 and Tier-1 deployment under the legal-personhood, specification-impossibility, and legitimacy ceilings.

The penetration curve runs surface-to-deep — opposite in direction to the Tier-Rotation Curve (Zharnikov 2026ai), which runs Tier-1-founder-resident to Tier-4-product-codified across multi-decade horizons. The two curves describe different objects and are coupled at Tier 4: Tier-4 AI deployment with Δ_4 > 0 acts as a SECI-externalization technology in the Nonaka and Takeuchi (1995) sense, codifying tacit founder-resident knowledge into product specifications faster than human documentation can.

**Auxiliary implications.**

Three additional comparative statics follow from the generalized share rule but are auxiliary to the three core propositions. First, the Tier-2 moat asymmetry: when γ_2 ∈ (0, 1) is paired with Δ_2 → δ_2^0 (the data-flywheel limit), δ_2^eff → 0 and the Tier-2 long-run stock expands without bound under continuing data accumulation. Cross-firm dispersion in long-run AI returns is largest at Tier 2 — two firms in the same sector with identical aggregate AI spend but different Tier-2 deployment depth can exhibit M&A multiples differing by 2× to 5×. Second, the penetration-depth ordering: the cross-sectional rank order of long-run firm-value gain from AI deployment is Tier 2 > Tier 4 > Tier 5-with-substrate > Tier 5-API-only ≈ Tier 6 ≈ Tier 3, following from joint movement of γ_t < 1 (cost cheapening, available everywhere) and Δ_t > 0 (durability gain, available only where substrate accumulation is feasible). Third, rotation acceleration: Tier-4 AI deployment with Δ_4 > 0 accelerates the rotation rate dα/dt because AI codifies tacit founder-resident knowledge into product specifications faster than human documentation — the SECI-externalization mechanism that connects the two curves at Tier 4.

**γ-vs-Δ separability fall-back inventory.**

The framework explicitly acknowledges that clean separate identification of γ_t and Δ_t with public data may be infeasible. The inventory of which propositions survive joint rather than separate identification: P1 SURVIVES — only γ_6 < 1 is needed. P2 SURVIVES with weakened sharpness — the discontinuity remains testable but is then a joint shift in the (γ_4, Δ_4) vector at the threshold. P3 PARTIAL — the sign of the long-run effect remains testable because the founder-horizon channel operates through r rather than through γ or Δ separately, but the magnitude attribution to γ versus Δ does not. P1 and P2 are joint-identification-robust; P3 survives in sign under joint identification.

---

**Conclusion**

This paper theorizes AI adoption not as a homogeneous productivity shock but as a tiered intervention into organizational architecture. By embedding per-tier cost and durability shocks within a Jorgensonian allocation framework, we derive why identical AI investments can produce opposite effects on long-run firm value. Surface deployments accelerate flow at the expense of substrate; only deeper deployments that cross the Tier-4 threshold build the persistent intangibles priced in M&A markets. The horizon-conditional sign flip further shows that governance — specifically the principal's effective discount rate — moderates these effects, linking AI strategy to fundamental questions of ownership and time preference.

Theoretically, the framework advances dynamic capabilities (Teece 2007; 2018) by specifying where and how reconfiguring activities accumulate (or dissipate) across discrete architectural layers. It reconciles the IT-complementarity literature's emphasis on organizational co-investment with a structural prediction that complementarities are neither continuous nor uniform. For AI-and-strategy research, it offers a parsimonious explanation for the emerging divergence between impressive short-run productivity numbers and ambiguous long-run shareholder returns — connecting formally to the automation-augmentation paradox (Raisch and Krakowski 2021) whose firm-level mechanism had not been derived.

Practically, the penetration-curve construct provides executives with a diagnostic: audit current AI initiatives by the tier at which durable artifacts reside. Firms over-allocated to Tier 6 may be harvesting near-term earnings at the expense of strategic option value. Boards should track tier-penetration depth alongside spend intensity when evaluating AI transformation budgets and founder-succession risks.

Several boundary conditions apply. The predictions are sharpest for large, multi-tier firms operating near the post-2023 capability frontier. Smaller firms or pure-platform businesses experience attenuated effects. Future capability improvements at Tier 3 (legal personhood) or Tier 1 (constitutive judgment) would require reformulation rather than recalibration — these are constitutional ceilings, not capability thresholds.

The central insight survives even if clean identification of cost versus durability shocks proves empirically challenging: deployment depth, not merely AI intensity, determines whether artificial intelligence augments or ultimately erodes the architectural foundations of competitive advantage. Strategy scholars and practitioners alike must therefore ask not how much AI a firm adopts, but where it lands.

---

**Appendix A. Self-Contained Re-Derivation: Six-Tier Ontology, Persistence Calibration, and Base Model**

This appendix re-derives, in self-contained form, the architectural primitives the body invokes from companion working papers. A reviewer who has not encountered Zharnikov (2026ag), (2026aj), (2026ah), (2026ai), (2026h), or (2026v) can read sections A.1 through A.5 below and then return to the body equipped with everything required to evaluate Propositions P1 through P3.

*A.1 Tier ontology recap.*

The six-tier ontology partitions the acquisition target into six architecturally distinct organizational tiers, each defined by three properties: a governor (the agent or force that determines the tier's configuration), a specification surface (the set of observable artifacts that describe the tier's state), and a transferability mode (the mechanism by which the tier does or does not cross an ownership boundary under merger-and-acquisition separation). The unifying axis on which the partition rests is *transferability mode of the artifact under M&A separation*. Tiers are ordered by position in a constraint hierarchy with Tier 1 most constraining and Tier 6 least constraining.

Tier 1, *Owner Intent*, is the controlling principal's psychic and strategic commitment to the firm's purpose. Tier 1's transferability mode is *fused*: the artifact does not transfer in M&A because it is constitutive of the controlling principal rather than separable from the principal (Selznick 1957). Tier 2, *Business Model*, is the intent-driven commercial logic by which value flows from the market into organizational resources. Tier 2's transferability mode is *independent-by-document*: a Business Model is conceptually replicable by a successor management team without acquiring the entity, but it is not legally owned and does not transfer in a share deal. Tier 3, *Business Entity*, is the legal and regulatory artifact that holds rights, obligations, and property — charter, cap table, debt structure, counterparty contracts, audited financials. Tier 3's transferability mode is *by document*: the Entity transfers as written instruments and is the only tier that transfers cleanly as a legal artifact. Tier 4, *Product Specification* (including brand codification), is the specific outcome a customer is paying for, governed by customer acceptance. Tier 4's transferability mode is *partial — independent if codified, fused if tacit*: a written product specification transfers; a tacit one remains with the principal who holds it (Penrose 1959; Dierickx and Cool 1989). Tier 5, *Process and Operations*, is the coordinated activity that produces the Tier 4 product. Tier 5's transferability mode is *partial — codified-routines transfer, tacit-routines do not* (Pentland and Feldman 2005). Tier 6, *Organizational Surface*, is the marketing, communications, and paid-media artifacts that carry the firm's signal to the customer environment. Tier 6's transferability mode is *partial — paid artifacts transfer, the human relationships and tacit cultural content do not*.

The architectural-transferability cut-point criterion produces exactly six discrete transferability modes: Fused (Tier 1), Independent-by-document (Tier 2), By-document (Tier 3), Partial-codified-or-fused (Tier 4), Partial-ostensive-or-performative (Tier 5), and Partial-paid-or-relational (Tier 6). The six modes are exhaustive and mutually exclusive within the architectural domain the ontology covers, and they are *discrete* rather than continuous because transferability under M&A separation is a structural property.

*Why six and not two or eight.* Collapsing the partition to two tiers loses the substrate-building threshold at Tier 4 (Proposition P2) and the data-flywheel asymmetry at Tier 2; the two-tier collapse cannot represent a paper whose central comparative-statics structure depends on the substrate-building tiers being architecturally distinct. Splitting the partition further to eight or more tiers generates non-orthogonal dimensions because tier identity is defined by transferability mode, and there are exactly six discrete modes available under M&A separation. The six-tier partition is the minimum sufficient partition for the framework's prediction structure and the maximum partition compatible with single-axis architectural-transferability orthogonality.

*A.2 Persistence calibration.*

The per-tier persistence parameters δ_t enter the formal model in §4 through the Jorgensonian user-cost-of-capital denominator (δ_t + r) and through the long-run stock S_t* = w_t · I / δ_t. Each calibration value is anchored to external published estimates.

*Tier 6 (Organizational Surface): δ_6 ≈ .50/year.* Belo, Lin, and Vitorino (2014) construct firm-level brand-capital stocks from Compustat selling-general-and-administrative-expense flows using the perpetual-inventory method and estimate the brand-capital depreciation rate at .50 per year. The estimate is consistent with Naik (1999) advertising half-life estimates, which find advertising-effect half-life on the order of months rather than years for most consumer-product categories. The .50/year decay rate is the largest in the calibrated vector and is the structural source of the Tier-6 over-allocation paradox of Proposition P1.

*Tier 5 (Process and Operations): δ_5 ≈ .15-.20/year.* Eisfeldt and Papanikolaou (2013) construct organization-capital stocks from SG&A flows under the perpetual-inventory method with a depreciation rate of .15 per year, validated against the cross-section of expected stock returns. Corrado, Hulten, and Sichel (2009) provide the broader intangibles-accounting framework with depreciation rates in the .15-to-.20 range for organization capital and economic competencies. The 2005 precursor is published as a chapter in *Measuring Capital in the New Economy* (NBER Chapters / University of Chicago Press, pp. 11-46). The body uses δ_5 = .175 as the midpoint.

*Tier 4 (Product Specification): δ_4 ≈ .12-.20/year.* Lev and Sougiannis (1996) estimate research-and-development capital amortization rates near .12 to .20 across two-digit SIC industries. Hall, Jaffe, and Trajtenberg (2005) construct patent-citation knowledge stocks from USPTO citation data and estimate similar persistence rates. The body uses δ_4 = .15 as the midpoint.

*Tiers 2-3 (Business Model and Business Entity): δ_2 ≈ δ_3 ≈ .05-.10/year.* Wiggins and Ruefli (2002) document, using hazard-model estimation on a panel of 6,772 firms across 40 industries from 1972 to 1997, that competitive-advantage half-lives remain in the multi-year range for sustained-superior-performer firms, with implied annual persistence rates in the .05-.10 range. The body uses δ_2 = δ_3 = .075 as the midpoint.

*The aggregate substrate-tier persistence rate δ_S.* The aggregate decay rate of the four substrate tiers is the investment-weighted average: δ_S = (1/4)(.075) + (1/4)(.075) + (1/4)(.15) + (1/4)(.175) = .119/year, computed under equal substrate-tier weights. The aggregate δ_S = .119 is the structural anchor for the comparative static ∂w_6*/∂r > 0: sign(δ_6 − δ_S) = sign(.50 − .119) > 0.

*A.3 Cobb-Douglas + Jorgensonian base model recap.*

This subsection re-derives the inherited base model so that a reviewer can evaluate the §4 generalization without consulting Zharnikov (2026aj). The derivation has three parts: the per-tier accumulation equation, the Cobb-Douglas long-run value function with Jorgensonian user-cost denominators, and the Lagrangian optimization that yields the closed-form share rule.

*Per-tier accumulation.* Each tier t ∈ {2, 3, 4, 5, 6} carries a stock S_t that evolves according to dS_t/dτ = w_t · I − δ_t · S_t. At long-run steady state, the equilibrium stock is S_t* = w_t · I / δ_t.

*Cobb-Douglas long-run value function with Jorgensonian denominators.* Long-run firm value aggregates the tier stocks via:

V_LR(w; r) = A · I · ∏_t [m_t · w_t / (δ_t + r)]^{α_t}

where A > 0 is a productivity scalar, m_t ∈ [0, 1] is the tier-t M&A separability factor, α_t ∈ (0, 1) is the tier-t output elasticity satisfying Σ_t α_t = 1, and r is the principal's effective discount rate. The denominator term (δ_t + r) is the per-period user cost of capital for tier t in the sense of Jorgenson (1963). The two-capital Cobb-Douglas production-function structure follows Belo, Lin, and Vitorino (2014); the multi-tier extension preserves the multiplicative structure across the substrate-tier vector.

*Output-elasticity calibration.* The α_t values are calibrated proportional to the M&A separability factors m_t and normalized to sum to 1: α_6 = .12; α_4 = α_5 = .24; α_2 = α_3 = .20 (sum = 1.00).

*Lagrangian optimization.* The interior optimum follows from Lagrangian maximization of ln V_LR(w; r) subject to Σ_t (δ_t + r) · w_t = 1. The Lagrangian is

L = ln A + ln I + Σ_t α_t · [ln m_t + ln w_t − ln(δ_t + r)] − λ · [Σ_t (δ_t + r) · w_t − 1]

and the first-order condition with respect to w_t is ∂L/∂w_t = α_t / w_t − λ · (δ_t + r) = 0, which implies w_t*(r) = α_t / [λ · (δ_t + r)]. Substituting into the budget constraint and using Σ_t α_t = 1 under constant returns to scale, λ = 1 and the interior optimum simplifies to the **closed-form share rule:**

**w_t*(r) = α_t / (δ_t + r)**

*Comparative static on the founder-horizon discount rate.* Differentiating the dollar-weighted share at Tier 6 with respect to r, the inherited base model establishes ∂(dollar-share_6*)/∂r > 0 from sign(δ_6 − δ_S) > 0, where δ_S = .119. When the principal's effective discount rate r rises, the relative user cost at the high-decay surface tier rises by a smaller proportional amount than at the low-decay substrate tiers, so the optimizer reallocates toward the surface tier even though that tier has the lowest persistence. Short-horizon principals over-allocate to the surface tier relative to long-horizon principals; the deviation is a welfare loss measured against the planner's optimum.

*CES robustness.* The Cobb-Douglas (σ = 1) specification is maintained throughout the body. Online Supplement S2 reports a constant-elasticity-of-substitution robustness check at σ ∈ {.5, 1.0, 1.5} for the AI-extended model and finds that the qualitative ordering of optimal allocations across the parameter range is robust. Cobb-Douglas is the tractable special case of the Milgrom and Roberts (1990; 1995) supermodularity framework: it captures cross-tier complementarities in reduced form while admitting the closed-form comparative statics that drive P1-P3.

*A.4 Separability axioms and M&A-multiple cleavage.*

The discrete-tier cleavage at Tier 4 is structurally distinct from a continuous "intangibles" measure; this distinction is the formal source of the framework's distinguishing proposition P2 (the substrate-building threshold). A continuous-intangibles specification treats firm intangibles as a continuous one-dimensional or low-dimensional stock and predicts a smooth slope in returns to additional investment in that stock. The slope-only prediction cannot generate a level shift at any specific intangible-intensity threshold.

The tier framework with positive Δ_4 produces a level shift rather than a slope shift. When Tier-4 AI deployment crosses from API-rented capacity (Δ_4 = 0) to proprietary-fine-tune or owned-weights configuration (Δ_4 > 0), the long-run stock S_4* = w_4 · I / δ_4^eff jumps discontinuously because δ_4^eff = δ_4^0 − Δ_4 jumps discontinuously at the substrate-building threshold. The discontinuity is structural: it reflects the architectural admissibility of substrate accumulation at Tier 4 only above the threshold, and below the threshold the AI deployment reduces to a γ-only cost shock with no substrate component.

*A.5 What is new in 2026ak versus inherited.*

*Inherited.* The six-tier ontology and architectural-transferability cut-point criterion are inherited from Zharnikov (2026ag) and recapped in A.1. The Cobb-Douglas long-run value function with Jorgensonian per-tier user-cost denominators, the closed-form share rule w_t*(r) = α_t / (δ_t + r), and the comparative static ∂w_6*/∂r > 0 are inherited from Zharnikov (2026aj) and recapped in A.3. The brand-as-Tier-4 projection is inherited from Zharnikov (2026ah). The Tier-Rotation Curve is inherited from Zharnikov (2026ai). The specification-impossibility bound on Tier-1 AI penetration is inherited from Zharnikov (2026h). The dimensional-collapse ceiling on Tier-4 brand codification is inherited from Zharnikov (2026v). The SECI-externalization mechanism is inherited from Nonaka and Takeuchi (1995). The persistence parameters δ_t are inherited from Belo, Lin, and Vitorino (2014), Eisfeldt and Papanikolaou (2013), Corrado, Hulten, and Sichel (2009), Lev and Sougiannis (1996), and Hall, Jaffe, and Trajtenberg (2005) as compiled in A.2.

*New in 2026ak.* The per-tier cost-shock parameter γ_t ∈ (0, 1] and the per-tier durability-shock parameter Δ_t ∈ [0, δ_t^0) are introduced for the first time in this paper. The generalized closed-form share rule w_t*(r; γ, Δ) = α_t / [γ_t · (δ_t^eff + r)] with δ_t^eff = δ_t^0 − Δ_t is derived in §4 and Online Supplement S1; it is new. The three propositions P1-P3 — the Tier-6 over-allocation paradox, the substrate-building threshold at Tier 4, and the horizon-conditional sign flip — are derived in §5 and are new to this paper. The AI Tier Penetration Curve as the stage-model construct, with Stage 0 (pre-deployment) through Stage 5 (asymptotic ceiling at Tiers 3 and 1), is introduced in §8.3 and is new. The four boundary-object case treatments (Klarna, Spotify, BloombergGPT, Stripe Radar) under the per-tier framework, the contrast Table 4 against the existing AI-and-strategy literature, and the three auxiliary comparative statics (Tier-2 moat asymmetry, penetration-depth ordering, rotation acceleration) are also new in the present paper.

---

**Online Supplement**

The Online Supplement is published as a separate file alongside this paper. It contains S1 Lagrangian setup, first-order conditions, and signs of comparative statics for the AI-extended share rule (formal proofs of the propositions stated in §4 and §5); S2 CES robustness for the AI-extended share rule at σ ∈ {.5, 1.0, 1.5}; S3 sensitivity to alternative α_t calibrations across three scenarios (m_t-proportional baseline, conservative-uniform, concentrated-stock); S4 the full threats-to-identification discussion with five threats (selection on unobservables; parallel-trends violation; founder-horizon endogeneity; measurement error in the tier-depth disclosure measure; attrition due to acquisition during the panel) including full instrument specifications and dictionary exemplars; and S5 the companion-script docstring, run command, function inventory, and parameter table for `tier_penetration_simulation.py`. Companion script is published at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-penetration/code/tier_penetration_simulation.py.

**Companion Computation Script.** Every numerical value in this paper that is not directly traceable to an external published source is reproducible from `tier_penetration_simulation.py` (run command: `uv run python tier_penetration_simulation.py`; fixed seed numpy.random.seed(42); no external data dependencies). The script is published at https://github.com/spectralbranding/orgschema-papers/blob/main/tier-penetration/code/tier_penetration_simulation.py. See Online Supplement S5 for full function inventory and parameter table.

---

## Acknowledgments

AI assistants (Claude Opus 4.7, Grok 4.1, Gemini 3.1) were used for initial literature search, editorial refinement, and implementation of the companion computation script (`tier_penetration_simulation.py`, including the AI-extended optimal-share solver, CES robustness check across σ ∈ {.5, 1.0, 1.5}, and comparative-statics verification for Propositions P1-P3); all theoretical claims, propositions, interpretations, and numerical results are the author's sole responsibility, and all script outputs were independently verified against the closed-form derivations in Online Supplement S1.

## CRediT contributions

Conceptualization, methodology, formal analysis, investigation, writing -- original draft, writing -- review and editing, visualization: Dmitry Zharnikov.

---

**References**

Acemoglu, Daron, and Pascual Restrepo. (2018). The race between man and machine: Implications of technology for growth, factor shares, and employment. *American Economic Review*, 108(6), 1488-1542. DOI: 10.1257/aer.20160696.

Acemoglu, Daron, and Pascual Restrepo. (2020). Robots and jobs: Evidence from US labor markets. *Journal of Political Economy*, 128(6), 2188-2244. DOI: 10.1086/705716.

Babina, Tania, Anastassia Fedyk, Alex Xi He, and James Hodson. (2024). Artificial intelligence, firm growth, and product innovation. *Journal of Financial Economics*, 151, 103745. DOI: 10.1016/j.jfineco.2023.103745.

Belo, Frederico, Xiaoji Lin, and Maria Ana Vitorino. (2014). Brand capital and firm value. *Review of Economic Dynamics*, 17(1), 150-169. DOI: 10.1016/j.red.2013.05.001.

Bennedsen, Morten, Kasper Meisner Nielsen, Francisco Pérez-González, and Daniel Wolfenzon. (2007). Inside the family firm: The role of families in succession decisions and performance. *Quarterly Journal of Economics*, 122(2), 647-691.

Bresnahan, Timothy F., Erik Brynjolfsson, and Lorin M. Hitt. (2002). Information technology, workplace organization, and the demand for skilled labor: Firm-level evidence. *Quarterly Journal of Economics*, 117(1), 339-376. DOI: 10.1162/003355302753399526.

Brynjolfsson, Erik, and Lorin M. Hitt. (1996). Paradox lost? Firm-level evidence on the returns to information systems spending. *Management Science*, 42(4), 541-558. DOI: 10.1287/mnsc.42.4.541.

Brynjolfsson, Erik, Danielle Li, and Lindsey R. Raymond. (2025). Generative AI at work. *Quarterly Journal of Economics*, 140(2), 889-942. DOI: 10.1093/qje/qjae044.

Callaway, Brantly, and Pedro H. C. Sant'Anna. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics*, 225(2), 200-230. DOI: 10.1016/j.jeconom.2020.12.001.

Coase, Ronald H. (1937). The nature of the firm. *Economica*, 4(16), 386-405. DOI: 10.1111/j.1468-0335.1937.tb00002.x.

Choi, Sukwoong, Hyo Kang, Namil Kim, and Junsik Kim. (2025). How does artificial intelligence improve human decision-making? Evidence from the AI-powered Go program. *Strategic Management Journal*, 46(6), 1523-1554. DOI: 10.1002/smj.3694.

Corrado, Carol, Charles Hulten, and Daniel Sichel. (2005). Measuring capital and technology: An expanded framework. In *Measuring Capital in the New Economy* (NBER Chapters), 11-46. Chicago: University of Chicago Press.

Corrado, Carol, Charles Hulten, and Daniel Sichel. (2009). Intangible capital and U.S. economic growth. *Review of Income and Wealth*, 55(3), 661-685. DOI: 10.1111/j.1475-4991.2009.00343.x.

De Chaisemartin, Clément, and Xavier D'Haultfœuille. (2020). Two-way fixed effects estimators with heterogeneous treatment effects. *American Economic Review*, 110(9), 2964-2996. DOI: 10.1257/aer.20181169.

Dierickx, Ingemar, and Karel Cool. (1989). Asset stock accumulation and sustainability of competitive advantage. *Management Science*, 35(12), 1504-1511. DOI: 10.1287/mnsc.35.12.1504.

Doshi, Anil R., J. Jason Bell, Emil Mirzayev, and Bart S. Vanneste. (2025). Generative artificial intelligence and evaluating strategic decisions. *Strategic Management Journal*, 46(3), 583-610. DOI: 10.1002/smj.3677.

Eisfeldt, Andrea L., and Dimitris Papanikolaou. (2013). Organization capital and the cross-section of expected returns. *Journal of Finance*, 68(4), 1365-1406. DOI: 10.1111/jofi.12034.

Felten, Edward W., Manav Raj, and Robert Seamans. (2021). Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses. *Strategic Management Journal*, 42(12), 2195-2217. DOI: 10.1002/smj.3286.

Foss, Nicolai J., and Peter G. Klein. (2014). Why managers still matter. *MIT Sloan Management Review*, 56(1), 73-80.

Gartner. (2026, May 5). Gartner Says Autonomous Business and AI Layoffs May Create Budget Room, but Do Not Deliver Returns [press release]. Stamford, CT: Gartner. https://www.gartner.com/en/newsroom/press-releases/2026-05-05-gartner-says-autonomous-business-and-artificial-intelligence-layoffs-may-create-budget-room-but-do-not-deliver-returns

Grant, Robert M. (1996). Toward a knowledge-based theory of the firm. *Strategic Management Journal*, 17(S2), 109-122. DOI: 10.1002/smj.4250171110.

Hall, Bronwyn H., Adam Jaffe, and Manuel Trajtenberg. (2005). Market value and patent citations. *RAND Journal of Economics*, 36(1), 16-38. JSTOR: 1593752.

Hassan, Tarek A., Stephan Hollander, Laurence van Lent, and Ahmed Tahoun. (2019). Firm-level political risk: Measurement and effects. *Quarterly Journal of Economics*, 134(4), 2135-2202. DOI: 10.1093/qje/qjz021.

Heckman, James J. (1979). Sample selection bias as a specification error. *Econometrica*, 47(1), 153-161. DOI: 10.2307/1912352.

Hitt, Lorin M., and Erik Brynjolfsson. (1996). Productivity, business profitability, and consumer surplus: Three different measures of information technology value. *MIS Quarterly*, 20(2), 121-142. JSTOR: 249475.

Hoberg, Gerard, and Gordon Phillips. (2016). Text-based network industries and endogenous product differentiation. *Journal of Political Economy*, 124(5), 1423-1465. DOI: 10.1086/688176.

Iansiti, Marco, and Karim R. Lakhani. (2020). *Competing in the Age of AI: Strategy and Leadership When Algorithms and Networks Run the World*. Boston: Harvard Business Review Press. ISBN: 978-1633697621.

Jorgenson, Dale W. (1963). Capital theory and investment behavior. *American Economic Review*, 53(2), 247-259.

Keller, Kevin Lane. (1993). Conceptualizing, measuring, and managing customer-based brand equity. *Journal of Marketing*, 57(1), 1-22. DOI: 10.1177/002224299305700101.

Krakowski, Sebastian, Johannes Luger, and Sebastian Raisch. (2023). Artificial intelligence and the changing sources of competitive advantage. *Strategic Management Journal*, 44(6), 1425-1452. DOI: 10.1002/smj.3387.

Krippendorff, Klaus. (2004). *Content Analysis: An Introduction to Its Methodology*. 2nd ed. Thousand Oaks: Sage Publications.

Lev, Baruch, and Theodore Sougiannis. (1996). The capitalization, amortization, and value-relevance of R&D. *Journal of Accounting and Economics*, 21(1), 107-138. DOI: 10.1016/0165-4101(95)00410-6.

Loughran, Tim, and Bill McDonald. (2011). When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. *Journal of Finance*, 66(1), 35-65. DOI: 10.1111/j.1540-6261.2010.01625.x.

Milgrom, Paul, and John Roberts. (1990). The economics of modern manufacturing: Technology, strategy, and organization. *American Economic Review*, 80(3), 511-528.

Milgrom, Paul, and John Roberts. (1995). Complementarities and fit: Strategy, structure, and organizational change in manufacturing. *Journal of Accounting and Economics*, 19(2-3), 179-208. DOI: 10.1016/0165-4101(94)00382-F.

Mizik, Natalie, and Robert Jacobson. (2003). Trading off between value creation and value appropriation: The financial implications of shifts in strategic emphasis. *Journal of Marketing*, 67(1), 63-76. DOI: 10.1509/jmkg.67.1.63.18595.

Naik, Prasad A. (1999). Estimating the half-life of advertisements. *Marketing Letters*, 10(3), 351-362. DOI: 10.1023/A:1008158119567.

Nonaka, Ikujiro, and Hirotaka Takeuchi. (1995). *The Knowledge-Creating Company: How Japanese Companies Create the Dynamics of Innovation*. New York: Oxford University Press.

Oster, Emily. (2019). Unobservable selection and coefficient stability: Theory and evidence. *Journal of Business and Economic Statistics*, 37(2), 187-204. DOI: 10.1080/07350015.2016.1227711.

Osterwalder, Alexander. (2004). *The Business Model Ontology: A Proposition in a Design Science Approach*. PhD dissertation, University of Lausanne.

Peng, Sida, Eirini Kalliamvakou, Peter Cihon, and Mert Demirer. (2023). The impact of AI on developer productivity: Evidence from GitHub Copilot. arXiv:2302.06590. DOI: 10.48550/arXiv.2302.06590.

Penrose, Edith T. (1959). *The Theory of the Growth of the Firm*. Oxford: Basil Blackwell.

Pentland, Brian T., and Martha S. Feldman. (2005). Organizational routines as a unit of analysis. *Industrial and Corporate Change*, 14(5), 793-815. DOI: 10.1093/icc/dth070.

Polanyi, Michael. (1966). *The Tacit Dimension*. Garden City, NY: Doubleday.

Raisch, Sebastian, and Sebastian Krakowski. (2021). Artificial intelligence and management: The automation-augmentation paradox. *Academy of Management Review*, 46(1), 192-210. DOI: 10.5465/amr.2018.0072.

Selznick, Philip. (1957). *Leadership in Administration: A Sociological Interpretation*. New York: Harper & Row.

Tambe, Prasanna. (2014). Big data investment, skills, and firm value. *Management Science*, 60(6), 1452-1469. DOI: 10.1287/mnsc.2014.1899.

Tambe, Prasanna, Lorin M. Hitt, and Erik Brynjolfsson. (2012). The extroverted firm: How external information practices affect innovation and productivity. *Management Science*, 58(5), 843-859. DOI: 10.1287/mnsc.1110.1446.

Teece, David J. (2007). Explicating dynamic capabilities: The nature and microfoundations of (sustainable) enterprise performance. *Strategic Management Journal*, 28(13), 1319-1350. DOI: 10.1002/smj.640.

Teece, David J. (2010). Business models, business strategy and innovation. *Long Range Planning*, 43(2-3), 172-194. DOI: 10.1016/j.lrp.2009.07.003.

Teece, David J. (2018). Profiting from innovation in the digital economy: Enabling technologies, standards, and licensing models in the wireless world. *Research Policy*, 47(8), 1367-1387. DOI: 10.1016/j.respol.2017.01.015.

Wiggins, Robert R., and Timothy W. Ruefli. (2002). Sustained competitive advantage: Temporal dynamics and the incidence and persistence of superior economic performance. *Organization Science*, 13(1), 81-105. DOI: 10.1287/orsc.13.1.81.542.

Williamson, Oliver E. (1985). *The Economic Institutions of Capitalism: Firms, Markets, Relational Contracting*. New York: Free Press.

Wu, Shijie, Ozan Irsoy, Steven Lu, Vadim Dabravolski, Mark Dredze, Sebastian Gehrmann, Prabhanjan Kambadur, David Rosenberg, and Gideon Mann. (2023). BloombergGPT: A large language model for finance. arXiv:2303.17564. DOI: 10.48550/arXiv.2303.17564.

Zharnikov, D. (2026h). Specification impossibility in organizational design: A high-dimensional geometric analysis. Working Paper. https://doi.org/10.5281/zenodo.18945591

Zharnikov, D. (2026v). Dimensional collapse in AI-mediated brand perception: Large language models as metameric observers. Working Paper. https://doi.org/10.5281/zenodo.19422427

Zharnikov, D. (2026ag). Dual hierarchies of organizational transferability: A six-tier ontology and theory of acquisition failure propagation. Working Paper. https://doi.org/10.5281/zenodo.19895813

Zharnikov, D. (2026ah). Brand as a modular layer: Tiered organizational architecture, separability, and firm performance in multi-brand strategies. Working Paper. https://doi.org/10.5281/zenodo.19930157

Zharnikov, D. (2026ai). The Tier-Rotation Curve: A theory of brand-substrate decoupling and its M&A-value geometry. Working Paper. https://doi.org/10.5281/zenodo.20069605

Zharnikov, D. (2026aj). Tier-allocation of capital: A theory of investment-tier choice and long-run firm value. Working Paper. https://doi.org/10.5281/zenodo.20072288

**Legal Authorities.**

*CFTC v. Ooki DAO, Inc.*, No. 3:22-cv-05416-WHO, 2023 WL 3911801 (N.D. Cal. June 8, 2023) (Orrick, J.).

Republic of the Marshall Islands Decentralized Autonomous Organizations Act of 2022 (as amended 2023; regulations 2024).

Vermont Blockchain-Based Limited Liability Company Act, 11 V.S.A. §§ 4172-4176 (2018).

Wyoming Decentralized Autonomous Organization Supplement, Wyo. Stat. Ann. §§ 17-31-101 to 17-31-115 (2021).
