# Specification Readiness and Endogenous Friction: An Information-Theoretic Theory of Multi-Interface Organizational Architecture

Dmitry Zharnikov

ORCID: 0009-0000-6893-9231

Working Paper v1.0.0 – May 2026

---

## Abstract

Organizations incur substantial friction when they must guess recipients' need profiles and push outputs toward those guesses. This paper develops an information-theoretic theory that treats alignment friction as endogenous to specification codification. Organizational architecture is decomposed into three layers: a codified specification substrate encoding commitments across six ontological tiers, an interface layer defined by recipient-class perception-weight vectors, and a function layer whose headcount and spend constitute a measurable tax on specification gaps. In push regimes, energy loss scales with cross-entropy between guessed and actual need profiles. In pull regimes, enabled by consumption-layer AI, recipients query the specification directly, collapsing misalignment toward zero as codification completeness rises. Recipient classes are architectural primitives whose distinct perception geometries impose coherence conditions across interfaces. The theory yields four contributions. First, it formalizes push-pull cost asymmetry as a structural analog to Shannon's cross-entropy. Second, it supplies geometric machinery linking specification to interface rendering. Third, it derives that functional friction is a consequence of specification investment rather than governance choice. Fourth, it establishes specification readiness as the critical moderator of AI returns, distinguishing Substrate-AI (query-constrained) from Surface-AI (locally fluent but globally inconsistent). By positioning specification codification as sequentially prior to governance, salience ranking, and capability deployment, the theory generates predictions distinct from transaction-cost economics, stakeholder theory, and existing AI-augmentation scholarship.

**Keywords**: organizational coupling; multi-interface architecture; specification readiness; recipient-class perception geometry; endogenous friction; push-pull asymmetry; AI-mediated pull

---

Every organization must solve a structural coupling problem: how to align what it actually is with what multiple, heterogeneous audiences perceive it to be. Traditional solutions have relied on push — pre-rendered outputs sent toward guessed recipient needs. The resulting misalignment generates measurable friction: marketing spend that fails to convert, investor relations efforts that do not shift valuations, recruiting costs that do not improve retention. This friction is not an exogenous feature of the environment but an endogenous consequence of incomplete specification investment.

Consumption-layer AI fundamentally alters the feasible solution space. When recipients — or their AI agents — can query a codified organizational substrate directly, the mechanical necessity of push disappears. Yet most firms continue to invest in ever-larger interface-maintaining functions rather than upstream specification codification. This observation reveals a theoretical puzzle that existing frameworks cannot resolve. Transaction-cost economics (Coase 1937; Williamson 1975, 1985) optimizes governance structures given a level of friction; it does not theorize the organizational investment that sets the friction level itself. Stakeholder theory (Freeman 1984; Mitchell, Agle, and Wood 1997) correctly identifies multiplicity of audiences but supplies salience-ranking mechanisms rather than architectural principles for rendering a common specification across non-commensurable perception geometries. Dynamic-capabilities scholarship (Teece, Pisano, and Shuen 1997; Raisch and Krakowski 2021; Schilke, Hu, and Helfat 2023) recognizes complementary investments yet stops short of specifying what those investments must be when AI operates at the consumption layer. Puranam's (2018) microstructure framework develops epistemic interdependence as a design principle but does not trace cost consequences when interdependence is unresolved across multiple recipient classes simultaneously.

The gap is both structural and consequential. Each tradition treats friction as an input. None asks how that friction level is set by prior specification choices. The present theory proposes that specification codification is the sequentially prior variable — the organizational choice that endogenizes the friction which downstream governance structures, salience allocations, and capability deployments then manage. Recognizing this priority reorients standard capital-allocation logic: the theory predicts that returns to specification codification dominate returns to functional capacity when AI penetrates to the consumption layer.

This paper develops an information-theoretic model of multi-audience organizational coupling. The model's central claim is that alignment friction is endogenous to specification codification. When specifications are incomplete or contradictory, functions must apply force (push) to compensate. When specifications are coherent and queryable, recipients — or their AI agents — pull directly, converting functions from force-appliers to monitors. The strategic variable is therefore not governance form but the firm's choice of how completely to codify commitments across six ontological tiers and how to design rendering policies for six canonical recipient classes, each characterized by a distinct perception-weight vector **w**_i.

This claim extends beyond brand or marketing scholarship. The manufacturing evidence establishes the point at scale: Ohno's (1988) Toyota Production System showed that push-based material requirements planning forces production against forecast, generating inventory buffers, waste, and rework; kanban-based pull systems let downstream demand signal upstream production directly, eliminating the buffer. Womack, Jones, and Roos (1990) generalized the demonstration; four decades of operations research confirm the structural logic. The present paper applies the same criterion to demand-specification coupling across all organizational output systems. The information-theoretic framing — following a structural analog to Shannon (1948), explicitly licensed in the tradition of Puranam, Raveendran, and Knudsen (2012) and Csaszar and Eggers (2013) — supplies the formal machinery to make this cross-domain claim tractable.

Four contributions follow. First, this paper formalizes push-pull asymmetry as a structural analog to Shannon's (1948) cross-entropy: push-regime energy loss is H(p, q) between actual and guessed recipient need profiles; pull-regime energy collapses toward zero as specification codification increases. Second, it introduces the multi-interface specification model, which decomposes organizational output architecture into specification, interface, and function layers and defines N recipient classes as the strategic variable organizing the interface layer. Third, it derives the function-as-friction-tax proposition with lineage in Radner (1993), providing the first architectural account of why functional headcount in interface-maintaining roles is a structural consequence of specification gaps rather than a governance choice. Fourth, it distinguishes Substrate-AI from Surface-AI and establishes that AI-ROI realization tracks specification readiness, not AI spend — directly engaging the theory-deficit Felin, Zenger, and Tomsik (2023) identify in AI research.

The paper proceeds as follows. The next section synthesizes structural deficiencies in prior literature and presents a comparative assumptions table. The Multi-Interface Specification Model section introduces the three-layer decomposition, formalizes the rendering operator and coherence condition, and states five formal propositions with comparative statics. The Formalization of Push-Pull Asymmetry section derives the information-theoretic asymmetry and the friction-tax proposition. The Discussion section develops theoretical contributions to the theory of the firm, stakeholder theory, and capability scholarship, enumerates five scope conditions, and addresses falsifiability. The paper concludes with the four interlocking contributions.

---

## **Theoretical Lacunae**

***Prior Traditions and Their Structural Gaps***

Three traditions form the direct intellectual antecedents of this paper. Each has developed substantial apparatus for the problems it addresses, and each leaves a structural gap that the present theory fills. Table 2 compares the core assumptions across these traditions and the proposed framework.

*Transaction-cost economics.* Coase (1937) asked where the boundary of the firm should be drawn: at the point where market transaction costs exceed internal coordination costs. Williamson (1975, 1985) developed TCE into a mature framework in which governance structures — markets, hierarchies, hybrids — are chosen to minimize transaction costs given existing frictions generated by asset specificity, uncertainty, and opportunism. The gap is equally precise: TCE treats friction as exogenous to governance choice. The sequentially prior question — what organizational investment sets the friction level itself — falls outside TCE's optimization problem. Massa, Tucci, and Afuah (2024) extend the Coase-Williamson framework for the digitization era; the present paper extends further by identifying specification readiness as the architectural determinant of pull feasibility in AI-mediated markets. Foss and Klein (2020) address post-digitization capabilities and boundaries but do not theorize the specification-readiness bottleneck. TCE generates no prediction about the sign of the relationship between specification investment and functional headcount; the present theory predicts a negative relationship.

*Stakeholder theory.* Freeman (1984) established that firms transact with multiple stakeholder classes whose interests and time horizons differ. Mitchell, Agle, and Wood (1997) formalized stakeholder salience as a function of power, legitimacy, and urgency, developing the ranking from latent to definitive salience. Donaldson and Preston (1995) established the normative-instrumental-descriptive structure of stakeholder theory. Harrison, Bosse, and Phillips (2010) formalized stakeholder utility-function heterogeneity as a determinant of competitive advantage. Bridoux and Stoelhorst (2014) supplied microfoundations for stakeholder heterogeneity in motivational architectures.

The structural gap is geometric. The most developed stakeholder-theory treatments operate on attributes of stakeholders as seen by managers (Mitchell, Agle, and Wood 1997) or on motivational heterogeneity (Bridoux and Stoelhorst 2014). Neither supplies the machinery to specify how the firm designs architecturally distinct interfaces for multiple recipient classes, or what it means for those interfaces to be coherent or contradictory. The question "how much attention should managers allocate to which stakeholders?" is different from the question "how should the firm design its interface architecture to minimize aggregate friction across all recipient classes simultaneously?" The six canonical interfaces in the present model correspond to the six structurally distinct evaluation traditions that Mitchell, Agle, and Wood's (1997) typology implies: consumer (Keller 1993), investor (Healy and Palepu 2001), employee (Edmondson 2003; Detert and Burris 2007), regulator (Bitektine 2011), supplier-partner (Dyer and Singh 1998), and peer-and-media (Rindova, Williamson, Petkova, and Sever 2005). These are not arbitrary — they correspond to six structurally distinct evaluation traditions in management scholarship.

*Dynamic capabilities.* Teece, Pisano, and Shuen (1997) introduced the sense-seize-reconfigure triad as the mechanism through which firms maintain advantage under technological change. Raisch and Krakowski (2021) established that AI automation and AI augmentation generate divergent returns depending on organizational substrates. Schilke, Hu, and Helfat (2023) provide a recent synthesis of the dynamic-capabilities construct. Teece (2023) updates the framework for AI-era competition. This literature correctly identifies that complementary investments moderate AI returns yet does not specify what those investments must be when AI operates at the consumption layer. The present paper closes that gap by identifying specification codification as the precise form of complementary investment that moderates AI-ROI.

***Information-Theoretic Lineage***

The information-theoretic framing draws on two lineages developed in organizational theory. The Radner (1993) lineage treats organizational layers as information-processing costs: Arrow (1974) established authority and communication channels as organizational costs; Milgrom and Roberts (1992) established complementarities in organizational design; Csaszar and Eggers (2013) model organizational decision-making using Shannon-adjacent language; Csaszar (2022) develops organizational structure as an information filter. Anderson, Banker, and Janakiraman (2003) provide the empirical anchor: SG&A costs are quasi-fixed overhead with asymmetric adjustment, consistent with function-layer spending as a structural consequence of specification gaps.

The modularity lineage supplies formal language for interface coherence. Baldwin and Clark (2000) establish that layered modular architectures reduce design costs through interface standardization. Ethiraj and Levinthal (2004) formalize the conditions under which module boundaries stabilize or fragment under search. Galbraith (2014) establishes interface design as the central problem of organizational architecture. Puranam and Raveendran (2022) develop architectural leverage as the mechanism through which modular design choices propagate performance implications across organizational layers — the cross-layer logic the present paper formalizes. Adner, Puranam, and Zhu (2023) establish that digital strategy's distinctiveness lies precisely in the feasibility of specification-constrained rendering that analog architectures could not achieve.

**Table 2: Comparison of Assumptions Across Four Theoretical Frameworks.**

| Theoretical assumption | TCE (Coase, Williamson) | Stakeholder Theory (Freeman, Mitchell et al.) | Dynamic Capabilities (Teece, Helfat) | Multi-Interface Specification Model |
|---|---|---|---|---|
| Friction status | Exogenous input to governance choice | Implicit / unmodeled | Bundled into "capabilities" | Endogenous to specification investment |
| Recipient treatment | Generic counterparty | Salience-ranked stakeholder | Capability beneficiary | Distinct perception geometry |
| Coupling object | Transaction | Stakeholder claim | Capability deployment | Specification rendering |
| Optimization variable | Governance form | Stakeholder attention | Capability development | Specification codification |
| AI role | Unspecified | Unspecified | Generic complement | Substrate vs surface penetration |

*Notes*: Each row identifies a structural assumption made by each tradition. The proposed framework's column shows the move adopted in this paper.

---

## **The Multi-Interface Specification Model**

The central architectural contribution is a three-layer decomposition of organizational output architecture: a specification layer that constitutes what the firm actually is; an interface layer through which that specification is rendered to distinct recipient classes; and a function layer comprising the operational capabilities that maintain alignment between specification and interface.

***The Specification Layer***

The specification layer is the substrate. It encodes what the firm actually is, what it commits to producing, how it operates, and under what conditions its commitments persist. The specification is not any single document. It is the full stack of commitments across all six tiers of the organizational ontology (Zharnikov 2026ag): the owner-intent commitment at Tier 1, the business-model logic at Tier 2, the legal-entity structure at Tier 3, the product and brand definition at Tier 4, the operational process codification at Tier 5, and the organizational capability and cultural commitment at Tier 6.

The specification has the properties Penrose (1959) identified as characteristic of inimitable organizational resources: its value derives from the organizational history that produced it, which competitors observing only surface renderings cannot access. Dierickx and Cool (1989) establish that asset stocks accumulate through sustained investment flows and cannot be acquired in factor markets; the specification substrate exhibits precisely this property. Barney's (1991) VRIN conditions apply directly: a coherent, versioned, machine-readable specification generated through organizational history is both inimitable and non-substitutable. Peteraf's (1993) four cornerstones map onto the specification substrate's competitive properties. Critically, a specification that claims one thing and does another is a contradictory specification, not a pull-capable substrate.

***The Interface Layer***

The interface layer comprises the distinct renderings of the specification that the firm produces for different recipient classes. Six canonical interfaces correspond to the primary recipient classes that strategic management theory and organizational economics have identified as consequential counterparties: the consumer interface, maintained toward purchasing and repeat-purchasing agents; the investor interface, maintained toward capital-allocating agents; the employer-brand interface, maintained toward current and prospective employees; the regulatory-positioning interface, maintained toward state and supra-state authority; the supplier-partner interface, maintained toward supply-chain and distribution counterparties; and the peer-and-media interface, maintained toward competitors, partners, analysts, and journalists.

Each interface has three defining attributes: the recipient class (the set of agents characterized by a common perception geometry, a common access pattern, and a common decision context); the emission policy (the firm's choice of whether to push this interface at this recipient class or to codify the specification so that the recipient class can pull it); and the interface-specific perception geometry (a weighting vector over the specification's dimensions that determines which elements of the specification are visible to this recipient class).

Interface coherence obtains when two conditions hold simultaneously: the specification is internally consistent across tiers, and each interface rendering accurately reflects the specification rather than papering over its gaps. Zavyalova, Pfarrer, Reger, and Hubbard's (2016) empirical finding — that the same firm signal generates structurally distinct reputation outcomes across audiences — is precisely the inter-interface divergence the present model identifies as a specification-level property rather than a communication artifact. Hannah and colleagues (2023) extend the organizational identity argument: digital disruption does not merely complicate communication but exposes specification-level inconsistencies that push-based interface management had previously suppressed.

***The Function Layer***

The function layer comprises the organizational capabilities that maintain spec-to-interface alignment. Marketing maintains the consumer interface. Investor relations maintains the investor interface. Human resources and recruiting maintain the employer-brand interface. Legal and compliance maintain the regulatory-positioning interface. Procurement and supply-chain management maintain the supplier-partner interface. Communications and public affairs maintain the peer-and-media interface.

Burton and colleagues (2023) establish organizational design in the AI age as the structural question of how information-processing capacity is distributed across layers — precisely the question the function-layer analysis addresses. When the specification is strong and coherent, the function's role is monitoring and calibration. When the specification is weak or contradictory, the function applies force — marketing spend, roadshow presentations, recruiter outreach, regulatory filings — to compensate.

***The Rendering Operator and Coherence Condition***

To operationalize perception geometry formally, let the specification be a vector **S** ∈ ℝ^d where d is the dimensionality of the firm's identity-relevant attributes across all six tiers. Recipient class r_i has a perception-weight vector **w**_i ∈ ℝ^d where **w**_{i,k} indicates how heavily attribute k weighs in r_i's evaluation. The rendering operator produces the scalar evaluation r_i applies to the firm:

> R_i(**S**, **w**_i) = ⟨**S**, **w**_i⟩ + ε_i

where ε_i is the rendering-process noise specific to the interface's emission policy: lower under pull, where the recipient queries the specification directly; higher under push, where the sender must guess the recipient's need profile and absorb alignment friction. Interface coherence between two recipient classes i and j holds when their normalized renderings are within a threshold κ:

> ‖⟨**S**, **w**_i⟩/‖**w**_i‖ − ⟨**S**, **w**_j⟩/‖**w**_j‖‖ ≤ κ

Interface incoherence is a specification-level contradiction — a property of **S** — not a communication failure. This coherence condition has no counterpart in TCE or stakeholder-salience theory, both of which treat coupling as bilateral and static rather than as a one-to-many architecture problem with cross-class coherence constraints. Ethiraj and Levinthal's (2004) formalization of module boundary stability supplies the closest prior-art machinery; the coherence condition generalizes their analysis from production modules to interface renderings.

Figure 1 illustrates the model architecture: a single specification vector **S** ∈ ℝ^d at the center; six perception-weight vectors **w**_1 through **w**_6 emanating outward, each with a distinct pattern of dimension weights; six rendering operators R_1 through R_6 mapping **S** × **w**_i to interface-specific scalar evaluations; and six interface labels (Consumer, Investor, Employer-Brand, Regulatory, Supplier-Partner, Peer-and-Media) at the periphery. The key architectural insight is that a single substrate supports six structurally distinct renderings — coherence is a property of **S**, not of any individual rendering.

*[Figure 1: The Multi-Interface Specification Model — One Substrate, Six Rendering Operators. A hub-and-spoke diagram: S vector at hub; six w_i vectors as spokes with distinct dimension-weight profiles; R_i(S, w_i) rendering operators at the spoke ends; interface class labels at periphery. Coherence is measured by the maximum pairwise difference between normalized renderings — a property of S's consistency across tiers, not of any individual w_i.]*

The Brand-as-Modular-Layer framework (Zharnikov 2026ah) establishes that brand surface is the Tier-4 product specification's consumer-facing interface. The present model extends laterally: rather than one interface at Tier 4, there are N structurally distinct interfaces each rendered to a different recipient class from the same specification substrate.

***Scope Conditions***

Five scope conditions define the theory's domain and appear here, immediately after the model, to sharpen interpretation of the propositions that follow.

*No-specification firms.* The pull regime requires a queryable substrate. Firms operating without a codified specification — early-stage startups before product-market fit stabilizes, firms in active restructuring — have no pull-capable substrate. The theory predicts that such firms will have high function-layer intensity as a structural consequence of specification absence.

*Monolithic recipient class.* The multi-interface architecture requires at least two structurally distinct recipient classes. Firms whose entire strategic dependency derives from a single recipient class operate with a degenerate architecture in which recipient-class differentiation collapses.

*No AI-mediation regime.* The phase-shift argument depends on AI operating at the consumption layer. In markets where AI-mediated consumption has not diffused — highly regulated information environments, air-gapped institutional settings — recipients default to push-dependent reception regardless of the firm's specification quality.

*Non-codifiable specifications.* Pull infrastructure requires a codifiable substrate. Domains in which the firm's core specification is genuinely tacit and resists codification — artisan craft, relational-service delivery, bespoke legal or surgical judgment — cannot build pull infrastructure regardless of AI capability at the consumption layer (Nonaka 1994). For these firms, push remains the only viable interface architecture because there is no substrate to query.

*Adversarial recipient classes.* A recipient class whose interests directly oppose the firm's reverses the pull efficiency claim: a fully machine-queryable specification that lowers alignment friction for cooperative recipients also lowers extraction friction for adversarial ones. The theory's pull-efficiency claim is scoped to non-adversarial recipient classes.

***Formal Propositions***

Five formal propositions with comparative statics follow from the three-layer architecture and the rendering operator. These are theoretical predictions derived from the model's structure — not empirical propositions with identification strategies, which are developed in companion empirical work.

**Proposition 1 (Interface Coherence).** Interface coherence — measured as the minimum cosine similarity between normalized renderings across pairs of recipient classes — is non-decreasing in specification consistency across tiers. Formally, if specification **S** is consistent across tiers t_1, t_2 (i.e., the value assigned to each attribute is identical across tier renderings), then min_{i,j} cos(R_i(**S**, **w**_i), R_j(**S**, **w**_j)) ≥ θ for some threshold θ > 0; if specification is inconsistent, coherence is unbounded below. *Comparative static*: ∂(min_{i,j} cos(·))/∂c ≥ 0, where c is specification codification completeness. Higher codification produces weakly greater inter-interface coherence.

**Proposition 2 (Friction-Tax Scaling).** The functional friction tax T scales positively with specification gap g and inversely with codification investment c. Formally, T(g, c) = α · g(c)/c + β, where g(c) is non-increasing in c (more codification reduces the gap). This derivation follows from Radner's (1993) information-processing-cost framework extended to multi-audience interface rendering. *Comparative static*: ∂T/∂c < 0 for all interior points of the codification domain. Increasing specification investment reduces the aggregate friction tax across all N interfaces.

**Proposition 3 (Push-Pull Cost Asymmetry).** Under the cross-entropy structural analog, push-regime alignment cost C_push = H(p, q), where p is the recipient's actual need profile and q is the firm's guessed need profile. Pull-regime alignment cost C_pull = H(p, **S**|p), which approaches 0 as specification codification completeness → 1 and recipient query capability → 1. *Comparative static*: ∂(C_push − C_pull)/∂c > 0. The cost asymmetry between push and pull grows strictly with codification investment. At full codification, pull dominates push at every interior point of the parameter space.

**Proposition 4 (AI Phase-Shift Boundary).** The fraction of firms operating in a viable pull regime is monotonically increasing in α, the consumption-layer AI penetration parameter. For α = 0, only domains with pre-AI codified substrates (financial accounting, manufacturing parts catalogs) operate in pull. For α ≥ α* ≈ .6 − .9 (domain-dependent), nearly all coupling domains become pull-viable. *Comparative static*: ∂(pull-viable fraction)/∂α > 0. Substrate-AI — specification-query-constrained generation — realizes the pull regime; Surface-AI — locally fluent but globally inconsistent generation — does not.

**Proposition 5 (Specification Readiness Moderates AI ROI).** AI return on investment, holding AI spend constant, is monotonically increasing in pre-AI specification codification c. Formally, ∂(ROI_AI)/∂c|_{spend} > 0. *Comparative static*: ∂(ROI_AI)/∂(spend)|_{c} is bounded above by a function of c — high AI spend without codification produces bounded marginal returns. This proposition operationalizes Brynjolfsson, Rock, and Syverson's (2017) complementarity finding by specifying what the complementary investment must be: not generic organizational capability but codification of the specification substrate that AI queries rather than substitutes.

---

## **Formalization of Push-Pull Asymmetry**

***Information-Theoretic License***

The energy-and-friction vocabulary used throughout this paper functions as a structural analog licensed by Shannon's (1948) information-entropy formalism, not a literal physical claim about organizations. The structural-analog license is the same Shannon invoked when he demonstrated that the mathematics of entropy, originally developed in statistical mechanics, applies with equal rigor to information uncertainty without requiring that messages and heat be commensurable. Energy in the present theory denotes measurable resource expenditure — budget, headcount, management attention — consumed to close the gap between what the firm produces and what the recipient class needs. Friction denotes the measurable waste generated by misalignment between a pushed output and the recipient's actual need profile. Entropy denotes the degree of misalignment between the firm's specification vector **S** and the recipient class's perception-weight vector **w**_i.

This is a structural analog in the tradition of Puranam, Raveendran, and Knudsen (2012) and Csaszar and Eggers (2013), who apply information-theoretic concepts as formal organizational analogs rather than literal physical claims. Empirical measurement requires resource-expenditure accounting, not calorimetry.

***Derivation of Push-Pull Cost Asymmetry***

The push-pull cost asymmetry follows from the structural-information-entropy analog as follows. Let p ∈ Δ^d be the recipient's true need profile over d specification attributes, and let q ∈ Δ^d be the firm's guessed need profile (where Δ^d is the d-simplex). Under push, the firm renders output against q; the alignment cost is the cross-entropy:

> H(p, q) = −Σᵢ pᵢ log qᵢ

By Gibbs' inequality, H(p, q) ≥ H(p) with equality if and only if p = q; misalignment cost is therefore bounded below by entropy of p and unbounded above. Kronrod and Huber (2019) document one mechanism through which push energy is systematically lost: high-frequency push generates annoyance that decays faster than memory, producing reversal effects in which the residual of a push campaign becomes positive only after the friction has dissipated. The push-energy-loss mechanism is empirically documented in the direction the theory predicts.

Under pull, recipient queries the firm's codified specification **S**. The cost is H(p, **S**|p) — the conditional cross-entropy between p and **S** given query knowledge of p. As codification completeness c → 1 and recipient AI query capability → 1, the conditional information about p contained in **S** approaches the recipient's own information; H(p, **S**|p) → 0 by the chain rule for conditional entropy. The asymmetry:

> C_push − C_pull = H(p, q) − H(p, **S**|p)

is strictly positive at all interior points of (c, AI penetration) parameter space, and approaches H(p, q) as c → 1. This establishes Proposition 3's comparative static analytically: the push-pull cost difference grows with codification investment and collapses push costs toward zero in the limit. Cao and Li (2022) document that machine-readable disclosures are increasingly consumed by AI systems that mine the underlying structured data rather than receiving pushed narrative summaries — precisely the investor-interface pull mechanism this derivation describes.

***Push-Regime Energy Loss***

Integrated over the population of recipients within a class and over the duration of the push campaign, total push energy is proportional to ∫∫ H(p_i, q_i) dt di. This is minimized when q = p across all recipients — a condition the function layer can approach only by investing in ever-finer-grained guessing of recipient need profiles. The function layer is therefore a structural embodiment of the firm's inability to observe p directly.

Hermès illustrates the consumer-interface pull state. The firm maintains relatively few retail locations globally, does not advertise at scale relative to category peers, and routinely generates waiting lists for its central products. The advertising-to-revenue ratio is structurally low; demand persistence following cessation of any given spend is structurally high. Patagonia approaches the same configuration from the ideological dimension: its specification's Tier-1 environmental commitment is sufficiently strong and verified over time that a large consumer cohort pulls the product without requiring constant push. Both cases exemplify the pull-capable state the theory describes.

***Pull-Regime Energy Collapse***

In pull regimes, H(p, **S**|p) → 0 in the limit of a perfectly codified specification coupled with a capable AI consumption layer that can render the specification into whatever format the recipient requires. Cao and Li (2022) show that machine-readable disclosures are increasingly consumed by AI systems — precisely the investor-interface pull mechanism the theory claims as timely. Li, Mayew, and Venkatachalam (2024) provide empirical evidence that AI-mediated consumption of corporate disclosures is reshaping the investor interface: AI systems increasingly process financial disclosures directly, reducing the exclusive role of sell-side analysts as human pull-interfaces.

***Proposition on the Friction Tax***

*Informally stated*: Every functional layer that exists to maintain interface coherence under push conditions absorbs a fraction of firm energy that a pure pull system would not require. The aggregate friction tax across all N interfaces is a monotonically increasing function of the specification gap — the distance between the firm's actual specification and its pull-capable codification ceiling. Firms minimize their aggregate friction tax by codifying and strengthening the specification, reducing the force required to close it, and in the limit converting each function from a force-applier to a monitor-and-calibrator.

*Formal derivation.* Let G_i denote the specification gap at interface i, defined as the Euclidean distance between the fully codified specification **S*** and the firm's actual specification **S**: G_i = ‖**S*** − **S**‖ projected onto recipient class i's perception geometry. The force F_i required to maintain interface coherence at class i under push is increasing in G_i: F_i(G_i) > 0 for G_i > 0, and F_i(0) = F_min_i > 0, where F_min_i is the irreducible monitoring cost under full codification. The aggregate friction tax across N interfaces is T = Σ_i F_i(G_i). Specification investment that reduces G_i toward zero reduces T toward Σ_i F_min_i — the monitoring floor that pull systems cannot eliminate but also need not exceed. This establishes Proposition 2: ∂T/∂c < 0 for all interior points.

Jensen and Meckling (1976) provide the economic framing in which monitoring and governance functions are defined as costs incurred because of principal-agent misalignment — the alignment-friction reading. Anderson, Banker, and Janakiraman (2003) establish empirically that SG&A costs are quasi-fixed and asymmetrically sticky — a structural consequence, on the present theory, of function layers existing to compensate for specification gaps rather than as flexibly efficient production inputs. This prediction — that specification codification reduces functional headcount and spend — is not derivable from TCE, which optimizes governance given G_i rather than predicting the functional-headcount consequences of G_i reduction.

***Surface-AI Versus Substrate-AI***

Prior to the deployment of AI at the consumption layer, most domains defaulted to push not from strategic preference but from mechanical necessity: recipients could not formulate a pull query against a raw substrate even when the substrate was technically available. With AI assistants operating at the consumption layer, recipients can now query substrates they could not previously interrogate. Raisch and Krakowski's (2021) automation-augmentation distinction directly grounds this dichotomy: AI augmentation requires investment in the organizational substrates that AI can augment.

Surface-AI denotes any AI content-generation workflow that does not access the firm's specification substrate at generation time. Each generation run is locally competent — the model produces fluent, well-formed output consistent with its training distribution — but globally inconsistent, because there is no mechanism ensuring consistency with the firm's Tier-1-through-Tier-4 commitments. Over time, surface-AI output accumulates inconsistencies across interfaces.

Substrate-AI denotes AI content-generation workflows that query the firm's specification substrate before generating output. The generation is constrained by the specification query at generation time, producing output that is locally competent and globally aligned across all functions and interfaces. Bloom, Garicano, Sadun, and Van Reenen (2014) document empirically that better information and communication technology flattens hierarchical function layers — the pre-AI analog of what Substrate-AI adoption delivers. Girotra, Meincke, and Terwiesch (2023) show that AI produces divergent quality outcomes depending on whether the underlying problem structure is coherent — a finding that maps directly onto the specification-readiness mechanism. Raisch and Fomina (2024) establish that combining human and artificial intelligence requires organizational preconditions that existing AI-strategy literature has not systematically enumerated; specification readiness is the central such precondition identified in this theory. Brynjolfsson, Rock, and Syverson (2017) established that AI delivers returns only after complementary organizational investments are in place; the present theory specifies what those investments must be: specification codification that makes Substrate-AI possible. Lindebaum and Ashraf (2024) document conditions under which AI augmentation produces negative organizational consequences — conditions that, on the present theory, correspond precisely to Surface-AI deployment against an incoherent specification.

The symmetry between Surface-AI and a specification-unaligned human operator is structural. A human employee who has not received specification cascade from Tier 1 through Tier 6 operates as a surface operator: locally competent within their domain and globally inconsistent. With specification cascade — a versioned brand-spec, a governance charter, a function-specific SOP library — the same employee becomes a substrate operator. AI generates the same structural dichotomy.

A companion computation repository establishing numerical coherence of the rendering operator and friction-tax derivations is available online.[^code]

[^code]: A companion computation repository is available at https://github.com/spectralbranding/orgschema-papers/tree/main/thermodynamic-coupling/code/. The primary experiment, `friction_tax_montecarlo.py`, implements a numerical exploration of friction-tax dynamics across push and pull regimes. Fixed seed: `np.random.seed(20260525)`. The repository does not constitute empirical confirmation; real-firm confirmation requires the archival panel study developed in companion empirical work.

---

## **Discussion**

***Theoretical Contributions***

The information-theoretic theory of multi-interface organizational architecture makes four interlocking contributions to strategic organization theory.

First, it establishes specification codification as the sequentially prior variable that endogenizes friction levels taken as given by transaction-cost economics, stakeholder theory, and dynamic-capabilities scholarship. By treating friction as an output of upstream architectural choices rather than an input to downstream optimization, the theory generates predictions — most notably a negative relationship between specification investment and interface-maintaining functional headcount — that cannot be derived from existing frameworks even in reframed form. TCE and stakeholder theory are not displaced by this move; they are extended by identifying the prior optimization problem that sets the friction levels and salience structures they then manage.

Second, the theory supplies geometric machinery — recipient-class perception-weight vectors and associated coherence conditions — that translates stakeholder multiplicity into architectural design choices rather than attentional ranking. Interface incoherence is revealed as a specification-level contradiction propagated across structurally distinct projections, not a communication failure amenable to functional effort. This shifts stakeholder theory from "how much attention?" to "how should the firm design its interface portfolio to satisfy cross-class coherence constraints while minimizing aggregate friction?"

Third, the function-as-friction-tax mechanism, with clear lineage in Radner (1993) and empirical grounding in SG&A stickiness (Anderson, Banker, and Janakiraman 2003), provides the first architectural account of why interface-maintaining functions expand with specification gaps. Codification reduces those gaps, converting force-application into monitoring and producing observable declines in functional intensity.

Fourth, the framework identifies specification readiness as the critical moderator of AI augmentation returns. The Substrate-AI versus Surface-AI distinction operationalizes the complementarity Brynjolfsson, Rock, and Syverson (2017) and Raisch and Krakowski (2021) identify but do not specify. AI does not render functional layers obsolete; coherent specification does.

***Implications for the Theory of the Firm***

The core implication for the theory of the firm is that firm boundaries should be evaluated not only where market transaction costs exceed internal coordination costs (Coase 1937; Williamson 1975) but where specification codification makes pull architecturally feasible — where a codified substrate can replace functional force-application as the mechanism of recipient-class alignment. Massa, Tucci, and Afuah (2024) extend the Coase-Williamson framework for the digitization era; the present theory extends to AI-mediated markets by identifying specification readiness as the architectural determinant of pull feasibility. Foss and Klein (2020) address post-digitization firm theory; the specification-readiness construct extends their analysis to multi-interface architecture. Adner, Puranam, and Zhu (2023) establish that digital strategy's distinctiveness lies in specification-constrained rendering; the present theory provides the organizational architecture through which that rendering is managed across multiple recipient classes simultaneously.

***Implications for Stakeholder Theory***

For stakeholder theory, the implication is that stakeholder multiplicity is architectural, not merely attentional. The present theory adds the geometric machinery: each stakeholder class occupies a distinct position in the firm's interface architecture, characterized by a perception-weight vector **w**_i that determines which specification dimensions are visible and at what rendering cost. This moves stakeholder theory from the question of "how much attention should managers allocate to which stakeholders?" to the question of "how should the firm design its interface architecture to minimize aggregate friction across all recipient classes simultaneously?" Harrison, Bosse, and Phillips (2010) and Bridoux and Stoelhorst (2014) provide the microfoundational grounding for this move.

The theory also generates a new diagnosis of stakeholder-relation failure. When inter-interface contradictions arise — when the consumer interface claims one thing and the investor interface implies another — stakeholder theory diagnoses a communication or attention failure. The present theory diagnoses a specification-level contradiction propagated to two structurally distinct projections. These are different diagnoses with different remedies: communication interventions cannot resolve specification-level contradictions.

***Implications for Capability and AI Scholarship***

For capability theory, the implication is that the AI phase shift is a dynamic-capability event (Teece, Pisano, and Shuen 1997) with a specific mechanism: specification readiness as the bottleneck. Firms that built pull-capable specification substrates before the shift realize the augmentation returns Raisch and Krakowski (2021) identify; firms invested in push infrastructure face a structural disadvantage that increased push expenditure cannot resolve. The specification substrate, as Penrose (1959) would recognize, derives its inimitability from the organizational history it records.

Schilke, Hu, and Helfat (2023) identify microfoundational specificity as the central challenge for dynamic-capabilities research. The present theory supplies a specific microfoundation for one class of dynamic-capability outcomes: specification codification is the observable organizational investment that determines whether AI augmentation generates returns or merely automates surface inconsistency. Felin, Zenger, and Tomsik (2023) argue that AI research lacks theoretical grounding in organizational mechanisms; the specification-codification construct is a direct response. Von Krogh, Seidel, Whittington, and Zenger (2023) identify knowledge-base architecture as central to AI organizational implications; the specification substrate is precisely this architecture at the interface-design level. Raisch and Fomina (2024) and Lindebaum and Ashraf (2024) establish performance and pathology conditions for human-AI combination; specification readiness is the architectural determinant of which condition obtains. Burton and colleagues (2023) establish organizational design in the AI age as the central structural question; the three-layer decomposition provides the framework through which that design problem is operationalized across multiple recipient classes.

***Boundary Conditions***

Five scope conditions bound the theory's domain, each generating a falsifiable restriction. The theory applies to non-adversarial recipient classes (adversarial classes reverse the pull-efficiency claim), multi-audience organizational contexts (monolithic recipient-class firms have degenerate architectures), AI-mediated consumption environments (pre-AI contexts default to push regardless of specification quality), codifiable specification domains (tacit-specification domains cannot build pull infrastructure regardless of AI capability), and stable ontological tiers (firms in active restructuring lack the specification coherence required for pull architecture). Deviation from any condition changes the prediction.

***Falsifiability and Future Research***

The theory generates several falsifiable predictions. First, a negative relationship between specification codification investment and functional headcount in interface-maintaining roles: as specification codification increases, functional headcount decreases — not merely becomes more efficient. This is observationally distinct from TCE predictions. Second, a positive interaction between specification readiness and AI adoption in predicting performance outcomes: firms with higher pre-AI specification codification should realize greater returns from subsequent AI investment, holding AI spend constant. Third, inter-interface coherence should covary positively with specification consistency across tiers, and negatively with push-proxy magnitudes from Table 1.

Operational empirical hypotheses derived from this theory are developed in companion empirical work. Future theoretical work should model mixed-adversarial portfolios, in which some recipient classes are cooperative and others adversarial, to specify the tradeoff between pull efficiency and extraction vulnerability. Future research should also formalize the optimal specification investment path under stochastic recipient perception vectors, building on Levinthal and Wu's (2023) capability redeployment framework for the dynamic version.

---

## **Conclusion**

These contributions redraw several theoretical boundaries. For the theory of the firm, boundaries should be evaluated not only where market transaction costs exceed internal coordination costs but where specification codification makes pull architecturally feasible. For stakeholder theory, the move from salience to perception geometry shifts the question from "how much attention?" to "how should the firm design its interface portfolio to satisfy cross-class coherence constraints while minimizing aggregate friction?" For capability and AI scholarship, the phase shift is not generic complementarity but a specific requirement that AI penetrate to the specification substrate rather than automate surface rendering.

The theory is bounded by the five scope conditions enumerated above. The ultimate prediction is architectural rather than technological: AI does not render functional layers obsolete, but coherent specification does. Under AI-mediated consumption, the theory predicts that returns to specification codification dominate returns to functional capacity — not as a prescriptive claim but as an observable structural consequence of the push-pull cost asymmetry derived in Proposition 3.

---

## Acknowledgments

AI assistants (Claude Opus 4.7, Grok 4.20 reasoning, Perplexity sonar-pro) were used for initial literature search and editorial refinement; all theoretical claims, propositions, and interpretations are the author's sole responsibility.

**CRediT Statement**: Dmitry Zharnikov: Conceptualization, Formal Analysis, Writing — Original Draft, Writing — Review and Editing.

---

## References

Adner, Ron, Phanish Puranam, and Feng Zhu (2023), "What Is Different About Digital Strategy? From Quantitative to Qualitative Change," *Strategic Management Journal*, 44 (6), 1412–1424. [DOI unverified — verify at upload]

Adner, Ron, and Rahul Kapoor (2010), "Value Creation in Innovation Ecosystems: How the Structure of Technological Interdependence Affects Firm Performance in New Technology Generations," *Strategic Management Journal*, 31 (3), 306–333. https://doi.org/10.1002/smj.821

Anderson, Mark C., Rajiv D. Banker, and Surya N. Janakiraman (2003), "Are Selling, General, and Administrative Costs 'Sticky'?" *Journal of Accounting Research*, 41 (1), 47–63. https://doi.org/10.1111/1475-679X.00095

Arrow, Kenneth J. (1974), *The Limits of Organization*, New York: Norton.

Baldwin, Carliss Y., and Kim B. Clark (2000), *Design Rules: The Power of Modularity*, Cambridge, MA: MIT Press.

Barney, Jay (1991), "Firm Resources and Sustained Competitive Advantage," *Journal of Management*, 17 (1), 99–120.

Bitektine, Alex (2011), "Toward a Theory of Social Judgments of Organizations: The Case of Legitimacy, Reputation, and Status," *Academy of Management Review*, 36 (1), 151–179. https://doi.org/10.5465/amr.2010.53502993

Bloom, Nicholas, Luis Garicano, Raffaella Sadun, and John Van Reenen (2014), "The Distinct Effects of Information Technology and Communication Technology on Firm Organization," *Management Science*, 60 (12), 2859–2885. https://doi.org/10.1287/mnsc.2014.2013

Boisot, Max H. (1998), *Knowledge Assets: Securing Competitive Advantage in the Information Economy*, Oxford: Oxford University Press.

Bridoux, Flore, and J. W. Stoelhorst (2014), "Microfoundations for Stakeholder Theory: Managing Stakeholders with Heterogeneous Motives," *Strategic Management Journal*, 35 (1), 107–125. https://doi.org/10.1002/smj.2089

Brown, John Seely, and Paul Duguid (2000), *The Social Life of Information*, Boston: Harvard Business School Press.

Brynjolfsson, Erik, Daniel Rock, and Chad Syverson (2017), "Artificial Intelligence and the Modern Productivity Paradox: A Clash of Expectations and Statistics," *NBER Macroeconomics Annual*, 32, 1–48. https://doi.org/10.1086/696117

Burton, Richard M., Dorthe Døjbak Håkonsson, Morten Henriksen, and Charles C. Snow (2023), "Organizational Design in the Age of Artificial Intelligence," *Organization Science*, 34 (3), 1201–1218. [DOI unverified — verify at upload]

Cao, Shuo, and Xuelin Li (2022), "Artificial Intelligence and the Future of Corporate Disclosure," *Journal of Accounting Research*, 60 (5), 1431–1475. https://doi.org/10.1111/1475-679X.12465

Christopher, Martin (2016), *Logistics and Supply Chain Management*, 5th ed., Harlow, UK: Pearson Education.

Coase, Ronald H. (1937), "The Nature of the Firm," *Economica*, 4 (16), 386–405.

Csaszar, Felipe A. (2022), "What Makes a Decision Strategic? Cognitive and Organizational Mechanisms," *Strategy Science*, 7 (2), 89–113. [DOI unverified — verify at upload]

Csaszar, Felipe A., and J. P. Eggers (2013), "Organizational Decision Making: An Information Aggregation View," *Academy of Management Review*, 38 (3), 435–455. https://doi.org/10.5465/amr.2011.0149

Davenport, Thomas H., and Laurence Prusak (1998), *Working Knowledge: How Organizations Manage What They Know*, Boston: Harvard Business School Press.

Detert, James R., and Ethan R. Burris (2007), "Leadership Behavior and Employee Voice: Is the Door Really Open?" *Academy of Management Journal*, 50 (4), 869–884. https://doi.org/10.5465/amj.2007.26279183

Dierickx, Ingemar, and Karel Cool (1989), "Asset Stock Accumulation and Sustainability of Competitive Advantage," *Management Science*, 35 (12), 1504–1511.

Donaldson, Thomas, and Lee E. Preston (1995), "The Stakeholder Theory of the Corporation: Concepts, Evidence, and Implications," *Academy of Management Review*, 20 (1), 65–91. https://doi.org/10.5465/amr.1995.9503271992

Dyer, Jeffrey H., and Harbir Singh (1998), "The Relational View: Cooperative Strategy and Sources of Interorganizational Competitive Advantage," *Academy of Management Review*, 23 (4), 660–679. https://doi.org/10.5465/amr.1998.1255632

Edmondson, Amy C. (2003), "Speaking Up in the Operating Room: How Team Leaders Promote Learning in Interdisciplinary Action Teams," *Journal of Management Studies*, 40 (6), 1419–1452. https://doi.org/10.1111/1467-6486.00386

Ethiraj, Sendil K., and Daniel Levinthal (2004), "Modularity and Innovation in Complex Systems," *Management Science*, 50 (2), 159–173. https://doi.org/10.1287/mnsc.1030.0145

Felin, Teppo, Todd R. Zenger, and Jordan Tomsik (2023), "The Need for Theory in AI Research," *Strategic Management Journal*, 44 (6), 1478–1490. https://doi.org/10.1002/smj.3490

Foss, Nicolai J., and Peter G. Klein (2020), "The Theory of the Firm and Its Critics: A Stocktaking and Assessment," in *The New Institutional Economics*, C. Ménard and M. M. Shirley, eds., Cambridge: Cambridge University Press, 89–114. [DOI unverified — verify at upload]

Freeman, R. Edward (1984), *Strategic Management: A Stakeholder Approach*, Boston: Pitman.

Galbraith, Jay R. (2014), *Designing Organizations: Strategy, Structure, and Process at the Business Unit and Enterprise Levels*, 3rd ed., San Francisco: Jossey-Bass.

Girotra, Karan, Lennart Meincke, and Christian Terwiesch (2023), "Ideas Are Dimes a Dozen: Large Language Models for Idea Generation in Innovation," *Management Science*, early online. [DOI unverified — verify at upload]

Hannah, David P., Blake E. Ashforth, Roderick E. Kramer, and Naomi B. Rothman (2023), "Reconceptualizing Organizational Identity Under Digital Disruption," *Academy of Management Review*, 48 (2), 291–314. [DOI unverified — verify at upload]

Harrison, Jason S., Douglas A. Bosse, and Robert A. Phillips (2010), "Managing for Stakeholders, Stakeholder Utility Functions, and Competitive Advantage," *Strategic Management Journal*, 31 (1), 58–74. https://doi.org/10.1002/smj.801

Healy, Paul M., and Krishna G. Palepu (2001), "Information Asymmetry, Corporate Disclosure, and the Capital Markets: A Review of the Empirical Disclosure Literature," *Journal of Accounting and Economics*, 31 (1–3), 405–440. https://doi.org/10.1016/S0165-4101(01)00018-0

Jacobides, Michael G., Carmelo Cennamo, and Annabelle Gawer (2018), "Towards a Theory of Ecosystems," *Strategic Management Journal*, 39 (8), 2255–2276. https://doi.org/10.1002/smj.2904

Jensen, Michael C., and William H. Meckling (1976), "Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure," *Journal of Financial Economics*, 3 (4), 305–360. https://doi.org/10.1016/0304-405X(76)90026-X

Kaul, Aseem, Ji-Yub Jay Kim, and Joseph T. Mahoney (2023), "The Future of Stakeholder Theory," *Academy of Management Review*, early online. [DOI unverified — verify at upload]

Keller, Kevin Lane (1993), "Conceptualizing, Measuring, and Managing Customer-Based Brand Equity," *Journal of Marketing*, 57 (1), 1–22.

Kronrod, Ann, and Joel Huber (2019), "Ad Wearout Wearout: How Time Can Reverse the Negative Effect of Frequent Advertising Repetition on Brand Preference," *International Journal of Research in Marketing*, 36 (2), 306–324. https://doi.org/10.1016/j.ijresmar.2018.11.008

Lee, Hau L. (2002), "Aligning Supply Chain Strategies with Product Uncertainties," *California Management Review*, 44 (3), 105–119.

Levinthal, Daniel A., and Brian Wu (2023), "Capability Redeployment and Technological Change: Organizational Adaptation Under Modular Disruption," *Strategic Management Journal*, early online. [DOI unverified — verify at upload]

Li, Feng, William J. Mayew, and Mohan Venkatachalam (2024), "Do Investors Use AI Tools to Process Financial Disclosures? Evidence from Earnings Calls," *The Accounting Review*, 99 (2), 101–132. https://doi.org/10.2308/TAR-2023-0312

Lindebaum, Dirk, and Muhammad Ashraf (2024), "The Dark Side of AI Augmentation: How AI Undermines Employee Voice and Inhibits Organizational Learning," *Academy of Management Review*, early online. [DOI unverified — verify at upload]

Massa, Lorenzo, Christopher L. Tucci, and Allan Afuah (2024), "A Theory of the Firm After Digitization," *Academy of Management Review*, 49 (1), 16–39. https://doi.org/10.5465/amr.2021.0002

Milgrom, Paul, and John Roberts (1992), *Economics, Organization and Management*, Englewood Cliffs, NJ: Prentice-Hall.

Mitchell, Ronald K., Bradley R. Agle, and Donna J. Wood (1997), "Toward a Theory of Stakeholder Identification and Salience: Defining the Principle of Who and What Really Counts," *Academy of Management Review*, 22 (4), 853–886. https://doi.org/10.5465/amr.1997.9711022105

Nonaka, Ikujiro (1994), "A Dynamic Theory of Organizational Knowledge Creation," *Organization Science*, 5 (1), 14–37. https://doi.org/10.1287/orsc.5.1.14

Ohno, Taiichi (1988), *Toyota Production System: Beyond Large-Scale Production*, Portland, OR: Productivity Press.

Olins, Wally (1989), *Corporate Identity: Making Business Strategy Visible Through Design*, London: Thames and Hudson.

Penrose, Edith T. (1959), *The Theory of the Growth of the Firm*, Oxford: Basil Blackwell.

Peteraf, Margaret A. (1993), "The Cornerstones of Competitive Advantage: A Resource-Based View," *Strategic Management Journal*, 14 (3), 179–191. https://doi.org/10.1002/smj.4250140303

Pillai, Rajiv, and colleagues (2024), "Artificial Intelligence and Organizational Cognition," *Organization Science*, early online. [DOI unverified — verify at upload]

Puranam, Phanish (2018), *The Microstructure of Organizations*, Oxford: Oxford University Press.

Puranam, Phanish, and Marlo Raveendran (2022), "Architectural Leverage: How Firms Use Modularity to Manage Complexity," *Strategic Management Journal*, 43 (9), 1810–1836. [DOI unverified — verify at upload]

Puranam, Phanish, Marlo Raveendran, and Thorbjørn Knudsen (2012), "Organization Design: The Epistemic Interdependence Perspective," *Academy of Management Review*, 37 (3), 419–440. https://doi.org/10.5465/amr.2010.0535

Radner, Roy (1993), "The Organization of Decentralized Information Processing," *Econometrica*, 61 (5), 1109–1146. https://doi.org/10.2307/2951766

Raisch, Sebastian, and Katharina Fomina (2024), "Combining Human and Artificial Intelligence: A Review and Agenda for Future Research," *Journal of Management*, 50 (3), 857–887. [DOI unverified — verify at upload]

Raisch, Sebastian, and Sebastian Krakowski (2021), "Artificial Intelligence and Management: The Automation-Augmentation Paradox," *Academy of Management Review*, 46 (1), 192–210. https://doi.org/10.5465/amr.2018.0072

Rindova, Violina P., Ian O. Williamson, Antoaneta P. Petkova, and Joy Marie Sever (2005), "Being Good or Being Known: An Empirical Examination of the Dimensions, Antecedents, and Consequences of Organizational Reputation," *Academy of Management Journal*, 48 (6), 1033–1049. https://doi.org/10.5465/amj.2005.19573108

Schilke, Oliver, Songcui Hu, and Constance E. Helfat (2023), "Dynamic Capabilities: A Review and Agenda for Future Research," *Academy of Management Review*, 48 (2), 390–420. [DOI unverified — verify at upload]

Shannon, Claude E. (1948), "A Mathematical Theory of Communication," *Bell System Technical Journal*, 27 (3), 379–423.

Teece, David J. (2023), "Dynamic Capabilities in the Age of Artificial Intelligence," *Strategic Management Journal*, 44 (6), 1403–1411. [DOI unverified — verify at upload]

Teece, David J., Gary Pisano, and Amy Shuen (1997), "Dynamic Capabilities and Strategic Management," *Strategic Management Journal*, 18 (7), 509–533. https://doi.org/10.1002/(SICI)1097-0266(199708)18:7<509::AID-SMJ882>3.0.CO;2-Z

von Krogh, Georg, Thomas Seidel, Richard Whittington, and Todd Zenger (2023), "Artificial Intelligence in Organization Studies," *Organization Science*, 34 (5), 1729–1751. [DOI unverified — verify at upload]

Williamson, Oliver E. (1975), *Markets and Hierarchies: Analysis and Antitrust Implications*, New York: Free Press.

Williamson, Oliver E. (1985), *The Economic Institutions of Capitalism*, New York: Free Press.

Womack, James P., Daniel T. Jones, and Daniel Roos (1990), *The Machine That Changed the World*, New York: Rawson Associates / Macmillan.

Zavyalova, Anastasiya, Michael D. Pfarrer, Rhonda K. Reger, and Timothy D. Hubbard (2016), "Reputation as a Multi-Audience Construct: Why Reputation Fails to Insulate a Firm Against Increases in Negative Media Coverage," *Academy of Management Journal*, 59 (1), 113–132. https://doi.org/10.5465/amj.2014.0596

Zharnikov, Dmitry (2026ag), "Dual Hierarchies of Organizational Transferability: A Six-Tier Ontology and Theory of Acquisition Failure Propagation," Working Paper. https://doi.org/10.5281/zenodo.19895813

Zharnikov, Dmitry (2026ah), "Brand as a Modular Layer: Tiered Organizational Architecture, Separability, and Firm Performance in Multi-Brand Strategies," Working Paper. https://doi.org/10.5281/zenodo.19930157

---

**Table 1: The Six Canonical Interfaces of the Multi-Interface Specification Model.**

| Interface | Recipient Class | Primary Decision Context | Push Proxy | Pull Proxy | Maintaining Function |
|-----------|----------------|--------------------------|-----------|-----------|---------------------|
| Consumer | Purchasing agents | Product acquisition / repeat purchase | XAD / SALE ratio | Brand equity without advertising spend; demand persistence under cessation | Marketing |
| Investor | Capital-allocating agents | Capital allocation / valuation | Roadshow frequency × IR headcount / market cap | XBRL-structured disclosure; AI-queryable financial substrate | Investor Relations |
| Employer-Brand | Prospective and current employees | Employment decisions; retention | Recruiter headcount / employer NPS | Employer-brand NPS without recruiter intensity | Human Resources |
| Regulatory-Positioning | State and supra-state authority | Compliance decisions; enforcement posture | Regulatory-counsel hours / regulatory mentions in 10-K | ISO certification; structured regulatory disclosure | Legal and Compliance |
| Supplier-Partner | Supply-chain and distribution counterparties | Procurement decisions; partnership terms | Supplier-outreach headcount / supplier NPS | Structured supplier specification; API-accessible procurement requirements | Procurement |
| Peer-and-Media | Competitors, analysts, journalists | Competitive positioning; narrative framing | PR and comms headcount / media mentions | Machine-queryable specification; structured research access | Communications |

*Notes*: Push proxies are the primary archival operationalizations for empirical work developed in companion papers. Pull proxies identify the pull-capable state in each interface dimension. The theory predicts that specification codification reduces push-proxy magnitudes toward the monitoring floor across all six interfaces simultaneously.
