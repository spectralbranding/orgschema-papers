# The OrgSchema Audit: A Six-Level Diagnostic for Specification-Driven Organizations

Dmitry Zharnikov

**Abstract**

This paper introduces the OrgSchema Audit, a structured diagnostic protocol that evaluates organizational specification maturity across six cascading levels: experience contracts, signal requirements, process contracts, procedures, input specifications, and sourcing requirements. The protocol parallels the Spectral Audit developed for brand perception (Zharnikov, manuscript submitted for publication) but targets organizational operations rather than perceptual allocation. Each audit level defines what to examine, what a healthy specification looks like, what failure modes indicate, and what corrective actions restore specification integrity. A worked example using a specialty coffee operation demonstrates the full protocol. The paper argues that a significant share of organizational dysfunction originates not from poor execution but from absent or misaligned specifications, and that remediation should be prioritized by cascade position rather than symptom severity. The protocol is designed to be executable with or without AI assistance, though large language models substantially reduce the cost of initial specification extraction from existing documentation.

**Keywords**: organizational specification, test-driven business design, operational audit, specification maturity, six-level cascade, experience contracts, organizational schema theory, AI-assisted diagnostics

---

Every organization operates from a specification, whether or not that specification is written down. The barista who knows the espresso should extract in 26 to 30 seconds is executing a specification. The founder who insists on direct-trade sourcing has defined a constraint. The shift lead who trains new hires by showing rather than telling is transmitting a specification orally — and losing fidelity with every retelling.

The gap between what an organization intends and what it actually does is not always an execution problem. Often it is a specification problem. When the operations manual says "ensure quality" without defining measurable quality gates, when the brand guidelines specify colors but not the environmental signals that carry the majority of brand perception (Zharnikov 2026a), when the compliance documentation exists as a PDF that no one reads and no system validates — the organization is operating from an incomplete specification. Many downstream failures trace back to this incompleteness.

Existing diagnostic frameworks address parts of this problem but not its full architecture. The Balanced Scorecard (Kaplan and Norton 1996) cascades metrics from strategy to operations but does not verify that operational parameters satisfy customer experience goals. Quality Function Deployment (Akao 1990) cascades customer requirements through product design but is a design-time tool, not a continuous diagnostic. Service blueprinting (Bitner, Ostrom, and Morgan 2008) maps service encounters across visibility layers but produces descriptive maps, not testable specifications. The Process and Enterprise Maturity Model (Hammer 2007) audits process maturity across five enablers but does not require customer experience as the root specification — an organization can achieve full process maturity while those processes produce the wrong customer experience. Capability maturity models (CMMI Institute 2018) assess organizational capability without connecting it to experiential outcomes. Each framework audits *within* its level of analysis; none audits *across* levels to verify that every operational parameter traces to a customer-defined acceptance test.

Organizational Schema Theory (Zharnikov 2026i) formalizes this gap by modeling organizations as six-level specification cascades. The framework borrows the core insight of test-driven development from software engineering (Beck 2003): define the desired outcome first, then build the implementation that satisfies it. In software, this means writing tests before code. In organizations, this means specifying the customer experience before designing the processes that deliver it. This reverse-design logic has precedents in backward design for education (Wiggins and McTighe 1998), where curriculum design begins with desired understanding rather than content coverage, and in Service-Dominant Logic (Vargo and Lusch 2004), which argues that value is fundamentally defined by the beneficiary.

The Spectral Audit (Zharnikov, manuscript submitted for publication) applied this logic to brand perception, providing a six-step protocol for diagnosing misalignment between how a brand invests resources and what its target cohorts actually value across eight perceptual dimensions. The present paper extends the diagnostic logic to organizational operations. Where the Spectral Audit asks "Are you investing in the dimensions your customers care about?", the OrgSchema Audit asks "Does every operational parameter trace backward to a customer experience justification, and does every customer experience goal trace forward to a verifiable operational implementation?"

This paper makes three contributions. First, it translates the six-level specification cascade of Organizational Schema Theory into a practitioner-executable audit protocol, with explicit criteria for healthy and failing states at each level. Second, it demonstrates the protocol through a worked example that illustrates specification gaps not surfaced by conventional operational review. Third, it advances two propositions — cascade-position prioritization and bidirectional traceability completeness — that distinguish the OrgSchema Audit from existing diagnostic frameworks and are testable through field research.


**The Six-Level Specification Cascade**

The OrgSchema framework models every organization as a stack of six specification levels. Each level answers a distinct question, and each depends on the level above it for justification. The six levels are not arbitrary; they correspond to a natural decomposition along two axes: the abstraction gradient from customer perception (Level 0) to physical supply (Level 5), and the executor-invariance boundary between what must be achieved (Levels 0 through 2) and how to achieve it (Levels 3 through 5). This decomposition parallels the test-implementation separation in software (Beck 2003), the front-stage/back-stage distinction in service design (Bitner, Ostrom, and Morgan 2008), and the voice-of-customer cascade in quality function deployment (Akao 1990), while extending all three into a unified, continuously auditable specification architecture.

- **Level 0 — Experience Contracts**: What should customers perceive, feel, and experience? These are the acceptance tests for the entire organization. They include experiential qualities (taste, temperature, delivery time), environmental conditions (cleanliness, noise, lighting), interaction qualities (greeting, service pace, dietary accommodation), regulatory constraints (food safety, data protection), and voluntary commitments (ethical sourcing, sustainability pledges). Experience contracts are fully executor-invariant: "excellent espresso" means the same whether a human artisan or an automated machine produces it. This level embodies the central insight of Service-Dominant Logic (Vargo and Lusch 2004): value is defined by the beneficiary, not the provider.

- **Level 1 — Signal Requirements**: What signals must the organization emit to create the desired perception? Signals operate across eight dimensions identified by Spectral Brand Theory (Zharnikov 2026a): semiotic, narrative, ideological, experiential, social, economic, cultural, and temporal. Each signal requirement links upward to a specific experience contract. Approximately 70% of signal requirements are executor-invariant — the signal categories remain stable across executor types, though specific implementations vary.

- **Level 2 — Process Contracts**: What must each process achieve to emit the required signals? Process contracts define measurable outcomes, quality gates, tolerances, and failure actions — but not how to achieve them. An espresso process contract might specify "extraction time 25 to 30 seconds, yield 25 to 35 milliliters, temperature 92 to 94 degrees Celsius, crema present and golden-brown." These are the unit tests of the organization: pass/fail criteria that any executor type must satisfy. This is the level most closely aligned with Hammer's (2007) process enablers, but with a critical distinction: process contracts in the OrgSchema framework derive their existence from Level 1 signal requirements, which in turn derive from Level 0 experience contracts. A process that satisfies its own quality gates but serves no upward requirement is waste.

- **Level 3 — Procedures**: How does a specific executor type achieve the process contract? Procedures are the implementation layer — the only level that is fully executor-dependent. A human artisan follows manual dosing, tamping, and visual feedback. A hybrid setup uses machine dosing with human finishing. A fully automated system handles the complete cycle. Different procedures, same contract. This separation mirrors Conway's (1968) insight that organizational structure follows communication structure — in the OrgSchema framework, procedure structure follows contract structure, and can be reorganized without disrupting the contract layer above it (Skelton and Pais 2019).

- **Level 4 — Input Specifications**: What materials, equipment, and capabilities do the procedures require? This includes ingredient specifications (origin, freshness, roast date), equipment performance requirements (grinder type, temperature control precision), and human capability requirements (certifications, training). Input specifications create the bill of materials for each procedure.

- **Level 5 — Sourcing Requirements**: Where do inputs come from and what criteria must suppliers meet? Sourcing requirements define supplier certifications, delivery frequency, lead times, backup supplier policy, and contingency planning. Each sourcing requirement links upward to the Level 0 commitments it satisfies.

The cascade has a critical architectural property: design flows top-down (from desired perception to sourcing), while operation flows bottom-up (from sourcing to perceived experience). This bidirectional traceability means every operational parameter can answer two questions: "Why does this exist?" (trace upward to the experience contract it serves) and "What implements this?" (trace downward to the procedure, inputs, and suppliers that deliver it). Parameters that cannot answer the first question are waste. Experience goals that cannot answer the second question are aspirations without implementation.

Two propositions formalize the audit's theoretical claims:

**Proposition 1 (Cascade-Position Prioritization).** Specification failures at higher cascade levels (closer to Level 0) predict greater operational dysfunction than failures at lower levels, because higher-level failures invalidate the justification for all levels below them. Specifically, an absent or incoherent Level 0 experience contract renders all downstream specifications unjustified — they may be internally consistent but externally meaningless, because no customer-defined acceptance test exists to evaluate them against.

*Falsification*: P1 is falsified if field studies show that Level 4 or Level 5 failures predict operational outcomes more strongly than Level 0 or Level 1 failures after controlling for organization size and sector.

**Proposition 2 (Bidirectional Traceability Completeness).** Organizations in which every operational parameter traces upward to an experience contract AND every experience contract traces downward to an implementing procedure exhibit lower rates of operational failure, faster expansion, and more successful automation initiatives than organizations with partial or unidirectional traceability.

*Falsification*: P2 is falsified if organizations with complete bidirectional traceability show no difference in operational outcomes compared to organizations with partial traceability, measured over a 12-month period.


**Positioning Against Existing Frameworks**

The OrgSchema Audit occupies a distinct position in the landscape of organizational diagnostics. To clarify its contribution, this section engages with the five frameworks most likely to be seen as competitors.

*The Process and Enterprise Maturity Model.* Hammer's (2007) PEMM is the closest prior diagnostic in structure — a level-based audit of process maturity with traffic-light assessments. PEMM evaluates five process enablers (design, performers, owner, infrastructure, metrics) across four maturity levels and four enterprise capabilities. The critical structural difference is the absence of customer experience as a root specification. An organization can score green on every PEMM dimension — fully mature processes with skilled performers, clear ownership, adequate infrastructure, and comprehensive metrics — while those processes produce the wrong customer experience, because PEMM does not require processes to trace their existence to customer-defined acceptance tests. The OrgSchema Audit adds the vertical dimension that PEMM lacks: not "Is this process mature?" but "Does this process have a justified reason to exist, traceable to what the customer should experience?"

*Service blueprinting.* Bitner, Ostrom, and Morgan (2008) introduced service blueprinting as a layered visualization of service encounters, separating physical evidence, customer actions, on-stage contact, backstage processes, and support processes across lines of interaction and visibility. Published in this journal, service blueprinting established the principle that service operations should be analyzed across visibility layers — a principle the OrgSchema Audit inherits and extends. The extension is from descriptive mapping to executable specification: a service blueprint identifies fail points post hoc, while the OrgSchema Audit specifies acceptance criteria pre hoc. Blueprinting produces a diagram; the OrgSchema Audit produces a testable repository. Blueprinting is typically a one-time analysis; the OrgSchema Audit is designed for continuous validation.

*The Balanced Scorecard cascade.* Kaplan and Norton (1996) created the most widely adopted cascade framework in management, connecting corporate strategy through business units to operational metrics across four perspectives. The OrgSchema Audit inverts the cascade direction: where the BSC cascades metrics *downward* from strategy, the OrgSchema Audit cascades specifications *upward* from customer experience. This inversion reflects a different philosophical commitment — that customer experience is the root specification rather than an outcome of strategy. The BSC asks "Are we measuring the right things at each level?" The OrgSchema Audit asks "Does every operational parameter satisfy a customer-defined acceptance test?"

*Quality Function Deployment.* Akao's (1990) House of Quality is the original customer-requirement cascade, translating voice-of-customer through engineering characteristics, part characteristics, and process operations. QFD is the closest structural ancestor of the OrgSchema Audit's six-level cascade. The distinction is temporal: QFD is a design-time tool applied during product or service development, while the OrgSchema Audit is a continuous diagnostic applied to operating organizations. QFD cascades through design phases; the OrgSchema Audit cascades through operational levels. QFD does not include automated validation or waste detection through broken upward traces.

*Capability maturity models.* CMMI (CMMI Institute 2018) assesses organizational capability across five maturity levels (Initial through Optimizing). Like PEMM, CMMI evaluates how mature an organization's processes are without requiring those processes to trace to customer experience goals. An organization at CMMI Level 5 (Optimizing) can have perfectly optimized processes that produce the wrong output. The OrgSchema Audit's contribution relative to maturity models is the customer-experience root: maturity is necessary but not sufficient; specification traceability is the additional requirement.

| Framework | Root specification | Cascade direction | Validation | Continuity |
|:----------|:-------------------|:------------------|:-----------|:-----------|
| PEMM (Hammer 2007) | Process maturity | Within-level | Manual assessment | Periodic |
| Service Blueprint (Bitner et al. 2008) | Service encounter | Within-level | Visual inspection | One-time |
| Balanced Scorecard (Kaplan and Norton 1996) | Corporate strategy | Top-down metrics | Review meetings | Quarterly |
| QFD (Akao 1990) | Customer requirements | Design-time cascade | Matrix analysis | Design-time |
| CMMI (CMMI Institute 2018) | Process capability | Within-level | Appraisal | Periodic |
| **OrgSchema Audit** | **Customer experience** | **Bidirectional across levels** | **Automated + manual** | **Continuous** |

**Table 1.** Positioning of the OrgSchema Audit Against Existing Diagnostic Frameworks.


**The Audit Protocol**

The OrgSchema Audit proceeds through six steps, one per specification level, starting from the top. This ordering operationalizes Proposition 1: higher-level failures invalidate everything below them, so there is no value in auditing procedures (Level 3) if the experience contracts (Level 0) are absent or incoherent.

*Step 1: Experience Contract Audit (Level 0)*

**What to examine.** Does the organization have explicit, testable statements of what customers should perceive across the eight spectral dimensions? Are regulatory constraints and voluntary commitments documented as binding contracts with measurable criteria? Is the target cohort defined with sufficient precision to distinguish it from the general population?

**Healthy result.** Each experience goal is stated in terms that permit a pass/fail evaluation. "Espresso should taste balanced, sweet, and clean, with no bitterness" is testable through structured tasting protocols. "Customer should feel welcomed" is not testable unless operationalized as "greeting within 10 seconds of entry, warm tone, dietary needs asked proactively." Regulatory constraints cite specific standards (HACCP, EU Regulation 1169/2011, GDPR). Voluntary commitments specify measurable criteria ("all coffee direct-trade with 25% price premium above commodity, annual origin visit"). The target cohort is named and distinguished from anti-targets.

**Failing result.** Experience goals are absent, vague, or untestable. "We aim for quality" without dimensional decomposition. No distinction between regulatory constraints and voluntary commitments — everything blurred into "values." Target cohort undefined or defined so broadly as to be meaningless ("everyone who likes coffee"). No anti-target identified, so the organization tries to serve incompatible cohorts simultaneously.

**The fix.** Conduct a structured experience design session using the eight spectral dimensions as a framework. For each dimension, define the intended perception, a testable assertion, and proxy indicators. Separate experience contracts (what customers should perceive) from constraint contracts (what regulation requires) and commitment contracts (what the organization voluntarily promises). Name the target cohort and at least one anti-target. Duration: 4 to 8 hours for a single-location operation; 2 to 3 days for a multi-unit business.

*Step 2: Signal Requirements Audit (Level 1)*

**What to examine.** Has the organization mapped the signals it emits — both designed (intentional) and ambient (operational by-products) — to the eight spectral dimensions? Does each signal requirement trace upward to a specific Level 0 experience contract?

**Healthy result.** A signal map exists with 15 to 30 entries, each linking a specific configuration element (color palette, music schedule, pricing structure, staff communication norms) to the spectral dimension it addresses and the experience contract it serves. The designed-to-ambient ratio falls between 55% and 70% designed. Every experience contract has at least one signal requirement that serves it. No spectral dimension has zero signal coverage.

**Failing result.** No signal map exists. The organization has a brand guidelines document that covers semiotic signals (logo, colors, typography) but ignores the experiential, temporal, ideological, social, economic, and cultural dimensions that collectively carry the majority of perceived brand identity. Signal emissions are uncoordinated: the music contradicts the visual identity, the pricing structure contradicts the stated values, the staff communication norms contradict the customer-facing tone. Some experience contracts have no implementing signals at all.

**The fix.** Inventory all organizational configurations that are perceivable by any observer type (customer, employee, inspector, algorithm, delivery platform). For each, identify the spectral dimension it addresses, whether it is designed or ambient, and which experience contract it serves. Flag experience contracts with zero signal coverage (these are aspirations without operational implementation) and spectral dimensions with zero signals (these are blind spots). Duration: 1 to 2 days with cross-functional input.

*Step 3: Process Contract Audit (Level 2)*

**What to examine.** Does each operational process have a defined contract — measurable outcomes, quality gates, tolerances, and failure actions — separate from its implementation procedure? Do process contracts trace upward to signal requirements?

**Healthy result.** Every customer-facing and production process has a written contract specifying what the process must achieve, with numerical tolerances where applicable. "Espresso extraction: 25 to 30 seconds, 25 to 35 milliliters, 92 to 94 degrees Celsius. Failure action: discard shot, recalibrate grinder, re-extract." Contracts are executor-invariant — they do not reference who or what performs the process, only what the output must be. Each contract traces to at least one signal requirement.

**Failing result.** Process descriptions mix what and how — "the barista grinds 18 grams, tamps evenly, and extracts for 27 seconds" is a procedure, not a contract. No measurable tolerances: "make a good espresso" rather than specific parameters with ranges. No failure actions defined, so deviations go undetected until a customer complains. No traceability to signal requirements, so processes cannot justify their existence.

**The fix.** For each existing process, separate the contract (what must be achieved) from the procedure (how to achieve it). Define measurable quality gates with numerical tolerances. Specify failure actions for each quality gate violation. Link each contract to the signal requirement it implements. Flag processes with no upward trace — these are candidates for waste elimination. Duration: 2 to 4 days for a typical operation, depending on process count.

*Step 4: Procedure Specification Audit (Level 3)*

**What to examine.** Are procedures documented as executable playbooks rather than narrative descriptions? Are they tagged by executor type (human, hybrid, automated)? Does each procedure reference the process contract it implements?

**Healthy result.** Each procedure is a sequence of timestamped steps with responsible roles, preconditions, cross-references to relevant specifications, and anti-patterns (what not to do). Multiple executor profiles exist where applicable — for example, a human artisan procedure and a hybrid procedure for the same espresso process contract. Each procedure explicitly references its Level 2 contract, creating a test-implementation relationship: the contract is the test, the procedure is the code.

**Failing result.** Procedures exist only as oral tradition — senior staff train new hires by demonstration, and knowledge walks out when employees leave. This is not to deny the value of tacit knowledge (Polanyi 1966), which remains essential for craft judgment and interpersonal skill. The audit targets the *specifiable* components of procedures — those that can be documented without loss of fidelity — while acknowledging that the human premium above the specification floor (warmth, improvisation, aesthetic judgment) resists and should resist codification. Written procedures are narrative prose that requires interpretation ("ensure the grind is right") rather than executable steps with measurable checkpoints. No executor-type tagging, so the organization cannot evaluate the operational impact of introducing automation. No connection to process contracts, so there is no way to verify that a procedure actually satisfies its intended quality gates.

**The fix.** Convert narrative descriptions to step-by-step playbooks. Each step should specify: the action, the duration, the responsible role, the feedback mechanism (how the executor knows the step succeeded), and the cross-reference to relevant specifications. Document at least one anti-pattern per critical procedure ("do not skip grinder calibration, even when running late"). If the organization is considering automation, draft parallel procedures for human and hybrid executor types against the same Level 2 contract. Duration: 1 to 2 days per major process area (production, service, compliance, logistics).

*Step 5: Input Specification Audit (Level 4)*

**What to examine.** Are the materials, equipment, and human capabilities required by each procedure explicitly specified with measurable criteria? Do input specifications trace upward to the procedures that consume them?

**Healthy result.** Every ingredient has origin, quality grade, freshness window, and storage requirements. Equipment has performance specifications with tolerances (grinder: conical burr, stepless adjustment; espresso machine: PID temperature control, 9.0 bar plus or minus 0.5 bar). Human capability requirements are defined as certifications or demonstrated competencies, not as years of experience or subjective assessments. Cost structures are itemized at the input level, enabling margin computation per product.

**Failing result.** Ingredients specified by brand name rather than performance criteria, creating single-supplier dependency. Equipment specified by model number rather than capability, so replacement decisions require guesswork. Human capabilities defined as "experienced barista" rather than measurable competencies ("SCA Barista Skills Foundation certified, demonstrated grinder calibration proficiency"). No cost itemization, so the organization cannot compute true cost of goods or identify margin compression.

**The fix.** Replace brand-name specifications with performance criteria that any qualifying supplier or equipment vendor could satisfy. Define human capabilities as testable competencies with explicit assessment methods. Itemize costs per input, per product, so that COGS and margins are computed from specifications rather than estimated from accounting aggregates. Duration: 1 to 2 days, requiring procurement and finance input.

*Step 6: Sourcing Requirements Audit (Level 5)*

**What to examine.** Are supplier selection criteria linked to Level 0 commitments? Does the organization have backup suppliers for critical inputs? Are lead times, delivery frequencies, and contingency plans documented?

**Healthy result.** Each supplier has documented selection criteria that trace to specific Level 0 commitment contracts. "Coffee supplier must hold Fair Trade and Rainforest Alliance certifications" traces to "L0 commitment: ethical sourcing." Delivery frequency, lead times, and minimum order quantities are specified. At least one backup supplier is identified for every critical input. The organization knows how long it can operate if its primary supplier fails.

**Failing result.** Suppliers were chosen by relationship or price, with no documented criteria. No traceability between sourcing decisions and customer experience commitments — the organization claims "sustainable sourcing" but has no supplier certification requirements. Single-supplier dependency on critical inputs with no contingency plan. Lead times and delivery frequencies are known informally by the procurement person but not documented, creating a single point of failure if that person leaves.

**The fix.** Document supplier selection criteria and link each to the Level 0 commitment it satisfies. Identify backup suppliers for all critical inputs. Specify lead times, delivery frequencies, and contingency plans. Calculate the organization's operational resilience: how many days of operation are covered by current inventory if the primary supplier fails? Duration: 1 day with procurement involvement.


**Worked Example: Spectra Coffee**

To demonstrate the protocol in practice, consider Spectra Coffee, a specialty coffee operation in Berlin. The operation has a single location, six products, three staff roles (barista, shift lead, manager), and a stated mission of "excellent coffee with full transparency." The following summarizes the audit findings at each level. A caveat is warranted: Spectra Coffee was designed from its specifications (using the orgschema-demo reference implementation), so the audit is a formative demonstration of the protocol's mechanics rather than an independent validation. The more demanding test — applying the audit to a legacy organization that has never been specified — is discussed in Limitations.

*Level 0 Audit: Experience Contracts*

Spectra Coffee has an explicit customer experience contract spanning all eight spectral dimensions, with testable assertions for each. The target cohort is defined as "quality-conscious urban professional, specialty coffee enthusiast" with explicit anti-targets: "price-sensitive, speed-only, brand-indifferent." Regulatory constraints reference specific standards (HACCP, EU Regulation 1169/2011 for allergens). Voluntary commitments are measurable: "all coffee direct-trade with 25% price premium above commodity; packaging 100% compostable or reusable; zero food waste to landfill." Satisfaction targets are quantified: NPS greater than or equal to 50, 30-day repeat visit rate greater than or equal to 40%, complaint rate below 2 per 100 visits.

**Audit finding**: Healthy. Experience contracts are testable and dimensionally complete. Minor gap: the social dimension contract ("regulars recognized") lacks a measurable proxy — "recognized" should be operationalized as a specific behavior (greeting by name, remembering usual order).

*Level 1 Audit: Signal Requirements*

Spectra Coffee has a signal map with 19 entries across all eight dimensions. Designed-to-ambient ratio is 70% designed, 30% ambient — within the healthy range, though slightly above the 55% to 65% optimum. Every experience contract has at least one implementing signal. Notable signal design choices include:

- Oat milk priced as default, dairy as a minus-modifier at negative 0.46 euros — an economic signal that inverts industry convention and directly implements the ideological commitment to sustainability.
- Music schedule transitions through three phases (jazz, lo-fi, acoustic) with decreasing volume — a temporal signal that marks the passage of time and creates rhythm for regulars.
- Internal communication norms (direct, specific, blameless, kind, curious) treated as ambient ideological signals — staff behavior leaks internal culture to customer perception.

**Audit finding**: Healthy with one gap. The economic dimension has low signal strength (5 out of 10 in spectral profile analysis) despite the oat-milk pricing inversion, because COGS breakdown and margin transparency are not customer-facing. If transparency is a Level 0 commitment, the economic signals should be more visible to customers.

*Level 2 Audit: Process Contracts*

Every product has quantified extraction parameters with tolerances. The espresso contract specifies grind size (200 to 300 micrometers), dose (18.0 grams plus or minus 0.3 grams), extraction temperature (93 degrees Celsius plus or minus 1 degree), pressure (9.0 bar plus or minus 0.5 bar), yield (36 milliliters plus or minus 2 milliliters), and extraction time (26 to 30 seconds). Failure actions are defined: "discard shot if extraction time outside 22 to 35 seconds, or if crema is blonde, thin, very dark, or shows visible channeling." Quality control includes daily grinder calibration with recalibration triggers (new bag of beans, humidity change greater than 20%, extraction time drift greater than 3 seconds).

**Audit finding**: Healthy. Process contracts are executor-invariant and numerically specified. All contracts trace to signal requirements. One process — the daily taste calibration session — has a contract that could be strengthened by specifying the target flavor profile in structured terms rather than prose ("sweet, bright acidity, clean finish").

*Level 3 Audit: Procedure Specification*

Opening and closing procedures are documented as 12-step and 12-step playbooks respectively, with timestamps, responsible roles, and cross-references to relevant specifications. Anti-patterns are documented: "Do not skip grinder calibration. Do not open early before calibration. Do not power off espresso machine fully — standby maintains boiler temperature for faster morning startup."

**Audit finding**: Mostly healthy. Procedures are executable playbooks, not narrative prose. Gap: only one executor profile (human artisan) is documented. If the operation considers hybrid or automated execution in the future, parallel procedures should be drafted against the same Level 2 contracts to evaluate feasibility. This is not a current operational failure but a specification gap that would delay any automation initiative.

*Level 4 Audit: Input Specifications*

Ingredients specify origin, altitude, processing method, and freshness windows (coffee roasted within 21 days, opened within 7 days). Equipment specifies performance criteria (conical burr grinder with stepless adjustment; E61 group head or equivalent with PID temperature control). Staff competency requirements reference specific certifications (SCA Barista Skills Foundation; allergen awareness with 80% pass threshold; anaphylaxis emergency response).

**Audit finding**: Healthy. Input specifications use performance criteria rather than brand names, with one exception: oat milk specifies "Oatly Barista" by brand rather than by performance criteria (fat content, protein content, foaming behavior). This creates a single-product dependency that should be replaced with a performance specification any qualifying product could satisfy.

*Level 5 Audit: Sourcing Requirements*

Coffee supplier (Nordic Roasters GmbH) has documented certifications (direct trade), delivery frequency (weekly), and traceability to Level 0 ethical sourcing commitment. Allergen supplier documentation traces to EU Regulation 1169/2011 compliance.

**Audit finding**: Partial gap. Primary coffee supplier is documented with criteria, but no backup supplier is identified. Lead time and contingency planning are not specified. If the primary supplier experiences a disruption, the operation has no documented fallback. Additionally, supplier criteria for non-coffee inputs (milk, oat milk, croissants) lack the same specification depth as the coffee supply chain — a common pattern where the "hero product" receives specification attention while supporting inputs are under-specified.


**Audit Summary and Cascade Prioritization**

The Spectra Coffee audit reveals a high-maturity operation with five of six levels at healthy specification status. The findings, prioritized by cascade position:

**Table 2.** OrgSchema Audit Findings for Spectra Coffee, Prioritized by Cascade Position.

| Level | Finding | Severity | Impact if Unfixed |
|:------|:--------|:---------|:------------------|
| L0 | Social dimension under-operationalized | Low | Weak social signal measurement |
| L1 | Economic transparency gap | Medium | Declared value (transparency) under-signaled |
| L2 | Flavor profile in prose, not structured terms | Low | Calibration subjectivity |
| L3 | Single executor profile only | Low | Future automation friction |
| L4 | Oat milk specified by brand, not performance | Medium | Single-product dependency |
| L5 | No backup coffee supplier; supporting inputs under-specified | Medium | Supply chain fragility |

Cascade-position prioritization directs attention to the Level 1 economic transparency gap over the Level 5 sourcing gap, even though the sourcing gap poses a more immediate operational risk. The reasoning: the Level 1 gap represents a misalignment between stated values (transparency) and emitted signals (cost structure not customer-visible), which undermines the coherence of the entire specification cascade. The Level 5 gap is a resilience issue that, while important, does not propagate upward to distort the customer experience.

This prioritization logic operationalizes Proposition 1. Conventional operational reviews prioritize by symptom severity or financial exposure (Hammer 2007). The OrgSchema Audit prioritizes by specification position: we argue that a failure at Level 0 is more consequential than a failure at Level 5, because higher-level failures invalidate the justification for everything below them. Whether this prioritization produces better operational outcomes than severity-based prioritization is an empirical question that field studies should address.


**AI as Audit Operator**

The OrgSchema Audit is designed to be executable without AI assistance, but large language models substantially reduce the cost of two bottlenecks: initial specification extraction and cross-reference validation.

*Specification extraction.* Most organizations have partial specifications scattered across operations manuals, training documents, brand guidelines, compliance files, and the tacit knowledge of senior staff. An LLM can ingest these documents and generate a first-draft specification in the six-level structure, identifying gaps where documentation is silent. This characterization testing approach — borrowed from software engineering's practice of writing tests for legacy code before refactoring (Feathers 2004) — converts implicit specifications into explicit, auditable artifacts. The accuracy of LLM-extracted specifications remains an open question; human validation of the extracted specification is a necessary step, not an optional one.

*Cross-reference validation.* Once specifications exist in structured form, an LLM can traverse the cascade to verify that every operational parameter traces upward to an experience contract (justification) and every experience contract traces downward to an implementing procedure (realization). Parameters without upward trace are waste candidates. Experience contracts without downward trace are unimplemented aspirations. This traversal, which would take a human auditor days for a moderately complex operation, takes an LLM seconds.

*Waste detection.* An LLM can flag specifications that exist at lower levels but have no upward justification — processes that no one remembers why they exist, input requirements that serve no current purpose, supplier relationships that pre-date the current experience design. In software, these are dead code. In organizations, they are dead process — consuming resources without contributing to customer experience.

The cost of a full OrgSchema Audit with LLM assistance has not been formally measured across multiple organizations, but the Spectra Coffee demonstration suggests modest resource requirements. For a single-location operation, specification extraction from existing documentation requires an estimated 2 to 4 hours of LLM-assisted work plus 4 to 8 hours of human validation. The audit itself adds 1 to 2 days. These estimates should be treated as preliminary until validated through field studies.


**Managerial Implications**

The OrgSchema Audit reframes operational management from symptom response to specification repair. Three implications deserve emphasis.

*Specification maturity as competitive advantage.* Organizations at high specification maturity (all six levels documented, traced, and validated) can replicate operations at new locations by sharing the specification, train new employees from the specification rather than from oral tradition, evaluate the impact of introducing automation by drafting parallel procedures against the same contracts, and respond to regulatory changes by updating constraint contracts and tracing the impact downward. Organizations at low specification maturity do all of these through ad hoc effort, informal knowledge transfer, and expensive trial-and-error. This advantage parallels the operational excellence discipline identified by Treacy and Wiersema (1993), but with a specific mechanism: specification traceability, rather than process efficiency alone, is the source of replicability.

*The specification gap as root cause.* When espresso quality is inconsistent, the conventional response is to retrain the barista (Level 3 intervention). The OrgSchema Audit may reveal that the problem is not the barista's execution but the absence of a grinder recalibration trigger in the process contract (Level 2), or an under-specified freshness window in the input specification (Level 4), or a supplier deviation from the sourcing requirement (Level 5). Treating symptoms at the procedure level while the specification gap exists at the contract or input level guarantees recurrence. This diagnostic logic extends Deming's (1986) and Shewhart's (1931) emphasis on system-level causes over individual-level blame, adding the cascade-position dimension: not just "the system is at fault" but "which level of the specification system is at fault."

*Organization as configuration, not identity.* The OrgSchema framework treats organizational structure as metadata — the most volatile layer of a three-layer stack where value is the most stable layer and process sits in between (Zharnikov 2026i). This perspective liberates managers from defending organizational forms as identity and instead treats them as configurations that can be modified, forked, or replaced when they no longer serve the experience contract. Different organizational structures producing the same value output are organizational metamers — structurally distinct but functionally equivalent. This aligns with recent reviews of organizational design (Joseph and Sengul 2025) that emphasize the contingent, reconfigurable nature of organizational structure.


**Discussion**

*Theoretical implications.* The OrgSchema Audit operationalizes the contract-procedure separation that is central to Organizational Schema Theory. By making this separation auditable, the protocol creates a bridge between the theoretical claim that organizations are specification systems (Simon 1996) and the practical question of what to do about it. The cascade-position prioritization principle (Proposition 1) extends existing quality management theory (Deming 1986; Shewhart 1931) by adding a specification-architectural dimension to failure analysis: not just "how severe is the failure?" but "where in the specification cascade does the failure originate?"

The protocol also formalizes the distinction between executor-invariant and executor-dependent layers. This distinction has practical consequences for automation readiness assessment: an organization that has clean Level 2 contracts can evaluate any executor type (human, hybrid, automated) by drafting Level 3 procedures and checking whether they satisfy the same contracts. An organization that has blended its contracts and procedures into a single description must redesign both simultaneously — a far more expensive and risky undertaking.

*Practical implications.* The OrgSchema Audit is positioned as a diagnostic instrument, not a consulting engagement. Like the Spectral Audit for brand perception, it produces a structured assessment that any competent manager can act on. The deliverable is not a recommendation but a specification gap map: which levels are healthy, which are failing, and what specific remediation each failing level requires.

For consulting firms, the protocol offers a standardized diagnostic methodology that reduces the cost of initial assessment and produces a testable deliverable (the specification repository) rather than an untestable one (the slide deck). Consulting impact becomes measurable: "14 of 18 process contracts now passing" is a more useful progress metric than "transformation initiative on track."

For organizations considering automation or expansion, the audit provides a pre-requisite assessment. Automation without clean Level 2 contracts means automating unspecified processes — a guaranteed way to produce consistent but wrong outputs at scale. Expansion without clean Level 0 contracts means replicating an organization whose intended customer experience is undefined — a guaranteed way to produce inconsistent but similarly confused locations.

*Convergence with the Spectral Audit.* The OrgSchema Audit and the Spectral Audit share diagnostic logic but address different questions. The Spectral Audit diagnoses whether a brand's resource allocation matches its target cohorts' perceptual weights across eight dimensions. The OrgSchema Audit diagnoses whether an organization's operational specifications are complete, traced, and validated across six cascade levels. Organizations that run both audits close the loop between perception (what customers experience) and operations (what produces that experience). The Rendering Problem (Zharnikov 2026l) argues that this loop — from specification to rendering to perception — is the fundamental pattern underlying organizational effectiveness.

*Limitations.* The protocol has been developed and demonstrated at coffee-shop scale. Whether the six-level cascade and the audit protocol scale to large, multi-division enterprises without modification is an open question. Complex organizations may require additional specification layers (inter-divisional contracts, shared-service specifications, governance protocols) that the current six-level model does not address. The specification cascade is inherently composable — each business unit can maintain its own L0 through L5 specification — but this composability has not been tested in practice.

The cascade-position prioritization principle (Proposition 1), while theoretically grounded, has not been empirically validated. Field studies comparing cascade-position prioritization against conventional severity-based prioritization would strengthen or qualify this claim.

The protocol assumes that customer experience can be decomposed into testable assertions across eight spectral dimensions. This assumption inherits the limitations of Spectral Brand Theory's dimensional model (Zharnikov 2026r), particularly the question of whether eight dimensions are necessary and sufficient for all organizational contexts. Organizations with multiple stakeholder groups (hospitals, universities) may require distinct experience contracts per constituency, complicating the single-root-specification assumption.

The worked example uses an organization that was designed from its specifications. Applying the audit to a legacy organization that has never been specified — the characterization testing scenario — introduces additional challenges: extracting implicit specifications from organizational behavior is inherently interpretive (Polanyi 1966), and the extracted specification may not match the organization's self-understanding. This gap between revealed specification and stated intention is itself a diagnostic finding, but navigating it requires organizational sensitivity that the protocol alone does not provide.

Finally, the current demonstration is limited to a single domain (specialty coffee) in a single cultural context (Berlin, Western Europe). Whether the audit protocol's assumptions — measurable quality gates, testable experience contracts, structured specification documents — transfer to high-context cultures, relationship-based business models, or purely B2B operations requires investigation.

*Future research.* Three directions are immediate. First, field validation: applying the OrgSchema Audit to 10 to 20 organizations of varying size and sector, measuring both the time and cost of the audit and the operational outcomes of specification-driven remediation over 6 to 12 months. This would provide the first empirical test of Propositions 1 and 2. Second, scale testing: extending the six-level model to organizations with 50 or more employees to identify where additional specification layers or modified audit procedures are required. Third, integration testing: running the OrgSchema Audit and the Spectral Audit jointly on the same organization to evaluate whether the combined diagnostic produces insights that neither audit alone would reveal — specifically, whether operational specification gaps predict perceptual coherence gaps, and vice versa.


**Disclosure**

This paper was drafted with AI assistance (Claude, Anthropic). The author assumes full responsibility for the intellectual content, claims, and any errors.


**References**

Akao, Yoji (1990), *Quality Function Deployment: Integrating Customer Requirements into Product Design*, Productivity Press.

Beck, Kent (2003), *Test-Driven Development: By Example*, Addison-Wesley.

Bitner, Mary Jo, Amy L. Ostrom, and Felicia N. Morgan (2008), "Service Blueprinting: A Practical Technique for Service Innovation," *California Management Review*, 50 (3), 66-94.

CMMI Institute (2018), *CMMI Model V2.0*, ISACA.

Conway, Melvin E. (1968), "How Do Committees Invent?," *Datamation*, 14 (4), 28-31.

Deming, W. Edwards (1986), *Out of the Crisis*, MIT Press.

Feathers, Michael C. (2004), *Working Effectively with Legacy Code*, Prentice Hall.

Hammer, Michael (2007), "The Process Audit," *Harvard Business Review*, 85 (4), 111-123.

Joseph, John, and Metin Sengul (2025), "Organization Design: Current Insights and Future Research Directions," *Journal of Management*, 51 (1), 249-308.

Kaplan, Robert S., and David P. Norton (1996), *The Balanced Scorecard: Translating Strategy into Action*, Harvard Business School Press.

Polanyi, Michael (1966), *The Tacit Dimension*, Doubleday.

Shewhart, Walter A. (1931), *Economic Control of Quality of Manufactured Product*, Van Nostrand.

Simon, Herbert A. (1996), *The Sciences of the Artificial*, 3rd ed., MIT Press.

Skelton, Matthew, and Manuel Pais (2019), *Team Topologies: Organizing Business and Technology Teams for Fast Flow*, IT Revolution Press.

Treacy, Michael, and Fred Wiersema (1993), "Customer Intimacy and Other Value Disciplines," *Harvard Business Review*, 71 (1), 84-93.

Vargo, Stephen L., and Robert F. Lusch (2004), "Evolving to a New Dominant Logic for Marketing," *Journal of Marketing*, 68 (1), 1-17.

Wiggins, Grant, and Jay McTighe (1998), *Understanding by Design*, ASCD.

Zharnikov, Dmitry (2026a), "Spectral Brand Theory: A Multi-Dimensional Framework for Brand Perception Analysis," Working Paper, https://doi.org/10.5281/zenodo.18945912.

Zharnikov, Dmitry (2026i), "The Organizational Schema Theory: Test-Driven Business Design," Working Paper, https://doi.org/10.5281/zenodo.18946043.

Zharnikov, Dmitry (manuscript submitted for publication), "The Spectral Audit: An Eight-Dimensional Diagnostic for AI-Era Brand Management," Under review at Journal of Business Research.

Zharnikov, Dmitry (2026l), "The Rendering Problem: From Genetic Expression to Brand Perception," Working Paper, https://doi.org/10.5281/zenodo.19064426.

Zharnikov, Dmitry (2026r), "Why Eight? Completeness and Necessity of the SBT Dimensional Taxonomy," Working Paper, https://doi.org/10.5281/zenodo.19207599.
