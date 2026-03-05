# The Organizational Schema Theory: Test-Driven Business Design

**Dmitry Zharnikov**

---

## Abstract

This paper introduces the Organizational Schema Theory (orgschema), a design methodology that applies Test-Driven Development (TDD) to business operations. Rather than designing businesses forward from available resources and hoping customer experience emerges acceptably, orgschema specifies desired customer experience first and derives every operational layer backward from that specification. Customer experience goals function as acceptance tests. Signal architecture serves as the integration test suite. Process specifications are the unit tests. Procedures are the implementation. A continuous integration pipeline validates satisfaction at each level. The result is businesses that are testable, forkable, and traceable from every operational parameter back to its customer-experience justification. We present the methodology as a Design Science Research artifact, demonstrate it through a complete specialty coffee operation (Spectra Coffee), and evaluate it through an expert panel representing five stakeholder perspectives. We argue that this methodology occupies genuine white space at the intersection of declarative business process management, organization-as-code, and test-driven development---three literature streams that have not previously been combined. We further argue that large language models are an essential enabler that makes the methodology's multi-dimensional complexity practically manageable for the first time.

**Keywords:** test-driven development, business design, configuration management, design science research, declarative process management, organizational specification

---

## Introduction

Consider a common pattern in business operations. A cafe owner selects a commercial espresso machine, hires baristas with varying levels of training, sources coffee beans from a convenient distributor, and opens the doors. Customers arrive and form impressions. Some return; others do not. When the owner eventually wonders why weekend visitors seem dissatisfied, the investigation must work backward through a tangle of undocumented decisions---from customer perception through staff behavior through equipment calibration through ingredient sourcing---with no systematic way to trace which operational parameter affects which customer outcome.

This forward-design approach, starting from available resources and allowing customer experience to emerge as an undesigned consequence, is how most businesses operate. It is the organizational equivalent of writing code without tests: you discover what works only after deployment, and debugging requires archaeology rather than analysis.

This paper proposes an alternative. The Organizational Schema Theory applies Test-Driven Development methodology to business design. Customer experience requirements are the acceptance tests. Signal architecture is the integration test suite. Process specifications are the unit tests. Procedures are the implementation. A continuous integration and continuous delivery (CI/CD) pipeline is the test runner. Version control is the audit trail. The methodology produces businesses that are testable, forkable, and traceable from every operational parameter back to its customer-experience justification.

The intellectual heritage is direct. Beck formalized TDD as a software development methodology where tests are written before code, driving architectural decisions rather than merely verifying them.[^1] Ohno articulated the lean pull system: "start with the customer, work backward."[^2] Deming defined quality as that which is determined by the customer.[^3] Shostack introduced service blueprinting from customer touchpoints.[^4] Orgschema synthesizes these lineages into a single methodology: businesses designed backward from customer experience through testable, version-controlled specifications where each operational layer validates the layer above it.

The contribution is the methodology itself, not any particular instantiation. We present orgschema as a Design Science Research artifact following Hevner and colleagues' framework for information systems research.[^5] The Spectra Coffee demonstration---a complete specialty coffee operation specified across six hierarchical levels---is one instantiation that validates the methodology's applicability. But the reusable design knowledge is the multi-level TDD cascade, the backward traceability architecture, and the satisfaction validation pipeline.

We situate orgschema at the intersection of three literature streams that have not previously been combined: declarative business process management, which specifies "what" but lacks customer experience traceability[^6]; organization-as-code, which exists for cloud infrastructure but not for full business ontologies[^7]; and Beck's TDD methodology, which has never been applied to a multi-level business specification cascade.[^1] We argue that orgschema fills a genuine gap: no existing framework provides machine-readable backward traceability from operational parameters to customer experience goals with automated satisfaction validation.

The paper proceeds as follows. We first establish theoretical foundations by connecting TDD methodology, reverse design, Spectral Brand Theory as a perception specification language, and the lean pull system. We then describe our Design Science Research methodology. The core of the paper presents the artifact---the six-level TDD cascade---and demonstrates it through Spectra Coffee. We evaluate the methodology through an expert panel of five independent reviewers. We discuss implications for operations management, franchise models, and organizational openness. We conclude with limitations and directions for future research.

## Theoretical Foundations

### Test-Driven Development as Design Methodology

Test-Driven Development, as formalized by Beck, is frequently misunderstood as a testing technique. It is a design methodology.[^1] The discipline of writing tests before implementation forces architectural clarity: you must specify what a system should do before deciding how to do it. The test suite becomes the authoritative specification. Refactoring is safe because the tests catch regressions. The "red-green-refactor" cycle---write a failing test, write the minimal code to pass it, improve the code while keeping tests green---produces systems that are specified, verified, and incrementally improved.

Orgschema extends this methodology from software to business operations. The parallel is structural, not metaphorical:

| TDD (Software) | Orgschema (Business) |
|:---|:---|
| Write tests first | Specify customer experience goals first |
| Tests define expected behavior | Experience contracts define desired perception |
| Write code to pass tests | Design processes to satisfy experience contracts |
| Run test suite | Run CI/CD validation pipeline |
| Refactor while tests pass | Optimize operations while customer experience holds |
| Red-green-refactor | Specify-implement-validate |

The critical insight is that TDD's value proposition---architectural decisions driven by desired outcomes rather than available means---applies to any complex system where outcomes matter and traceability aids debugging. A business is such a system.

### Reverse Design: From Perception to Sourcing

The forward-design approach to business creation starts with available resources. An entrepreneur identifies accessible suppliers, available staff, and affordable equipment, then builds operations from these constraints upward, hoping that the resulting customer experience will be acceptable. Customer perception is emergent---an undesigned consequence of operational decisions made for operational reasons.

**Table 1: Forward Design vs. Reverse Design**

| Property | Forward Design | Reverse Design (Orgschema) |
|:---|:---|:---|
| Starting point | Available resources | Desired customer experience |
| Design direction | Bottom-up (resources to experience) | Top-down (experience to resources) |
| Customer experience | Emergent, undesigned | Specified, testable |
| Traceability | None (archaeological) | Full backward trace to experience |
| Change validation | Manual inspection | Automated CI/CD pipeline |
| Debugging | "Why are customers unhappy?" | "Which acceptance tests are failing?" |
| Knowledge format | Tribal, documented, or procedural | Versioned specification with test suite |

Reverse design inverts this sequence. The desired customer perception is specified first, and every subsequent layer exists to satisfy the layer above it. This is not a new idea. Wiggins and McTighe articulated backward design for curriculum development: start with desired learning outcomes, then determine acceptable evidence, then plan learning experiences.[^8] Akao's Quality Function Deployment traces customer requirements to engineering specifications through the "House of Quality" matrix.[^9] Christensen's Jobs to Be Done framework designs from the customer's functional, emotional, and social needs.[^10]

Orgschema's contribution is making reverse design machine-readable, version-controlled, and automatically validatable. Where QFD produces a paper matrix that cannot be executed, orgschema produces specifications that run through a validation pipeline. Where service blueprinting produces a narrative document, orgschema produces a specification that a machine---or a large language model---can traverse, query, and verify.

### Spectral Brand Theory as Test Specification Language

The top two levels of orgschema's TDD cascade---customer experience contracts (Level 0) and signal requirements (Level 1)---require a language for specifying desired perception. Spectral Brand Theory (SBT) provides this language.[^11]

SBT models brand perception across eight dimensions: experiential, semiotic, temporal, ideological, narrative, cultural, social, and economic. Perception is observer-dependent: the same business emits signals that different observer cohorts perceive differently based on their individual priors (training, cultural context, expectations). SBT explicitly prohibits averaging across cohorts---a position grounded in its anti-ergodic epistemology.

In orgschema, SBT serves a prescriptive function. The spectral profile of the desired brand becomes the acceptance test: what should customers perceive across each dimension? Signal requirements then specify what the business must emit to create that perception. This is not brand auditing (measuring what exists) but brand engineering (specifying what should exist and validating that operations produce it).

### The Lean Pull System and Quality as Customer-Defined

Ohno's lean pull system---producing only what the downstream process needs, when it needs it---is a proto-reverse-design methodology.[^2] The customer's pull signal propagates backward through the production system. Orgschema formalizes this propagation as a specification cascade: the customer's desired experience propagates backward through signals, process contracts, procedures, inputs, and sourcing.

Deming's insistence that quality is defined by the customer, not by the producer, is operationalized in orgschema through Level 0 acceptance tests.[^3] Quality management becomes test suite management. A process that passes all its quality gates but fails to satisfy the signal requirements above it is, by definition, not meeting quality standards---regardless of how well its internal metrics look.

### Positioning Against Prior Art

Orgschema draws from and extends several established frameworks. The following table clarifies the relationship to each, distinguishing what orgschema inherits from what it contributes:

| Framework | What It Does | Orgschema's Extension |
|:---|:---|:---|
| TDD (Beck, 2003) | Tests before code in software | Extends TDD from code to multi-level business operations |
| QFD (Akao, 1966) | Customer requirements to engineering specs | Paper matrix; orgschema is machine-readable and CI/CD-validatable |
| Service Blueprinting (Shostack, 1984) | Service design from customer touchpoints | Narrative methodology; orgschema adds automated validation |
| Jobs to Be Done (Christensen, 2003) | Design from functional, emotional, social needs | Conceptual framework; orgschema adds operational specification with traceability |
| Backward Design (Wiggins/McTighe, 1998) | Curriculum design from learning outcomes | Education domain; orgschema applies to business operations |
| Lean Pull System (Ohno, 1988) | Start with customer, work backward | Production philosophy; orgschema adds formal specification and validation |
| Quality Management (Deming, 1986) | Quality defined by customer | Philosophy; orgschema operationalizes as testable, versioned specs |
| DSR (Hevner et al., 2004) | Artifact-centered research methodology | Orgschema's artifact is the methodology itself, not the YAML |
| VSM (Beer, 1972/1981) | Organizational cybernetics, recursive systems | Maps to S1--S5; adds machine-readable specification at each level |
| Declarative BPM (Pesic/van der Aalst, 2006) | Constraint-based process specification | Process level only; orgschema extends to full organizational ontology |

The common thread in these relationships is that orgschema inherits a design principle from each framework and contributes machine-readability, automated validation, backward traceability, or organizational scope that the original framework lacks. No prior framework combines all four properties for business operations.

## Methodology: Design Science Research

We follow the Design Science Research methodology as articulated by Hevner and colleagues[^5] and refined through the echeloned DSR (eDSR) approach,[^12] which decomposes the research project into five validated echelons: problem analysis, requirements specification, design, demonstration, and evaluation. Each echelon provides intermediate validation.

The primary contribution is design knowledge---specifically, a Technological Rule in the form: "To achieve testable, traceable, forkable business operations, apply the reverse-design TDD methodology with multi-level specification cascades and CI/CD satisfaction validation." The Spectra Coffee demonstration is one instantiation of this rule. The artifact is the methodology, not the demo.[^13]

We evaluate the methodology using the Formative Evaluation of Design Science (FEDS) framework.[^14] Our evaluation strategy combines formative expert walk-throughs (five independent reviewers representing distinct stakeholder perspectives) with technical validation (automated schema and cross-reference checking). We address two of the five validity types specified in the Design Science Validity Framework: instrument validity (does the specification language adequately capture business operations?) and purpose validity (does the methodology serve its intended purpose of producing testable, traceable businesses?).[^15]

## The Artifact: Reverse-Design TDD for Business Operations

### The Six-Level TDD Cascade

The core of orgschema is a six-level specification cascade where each level functions as the acceptance test for the level below it. Designed top-down (from customer perception to supply chain), operated bottom-up (from supply chain to customer perception), and validated at every level by a CI/CD pipeline.

**Figure 1: The TDD Cascade Architecture**

```
                    DESIGN DIRECTION (top-down)
                           |
    +----------------------------------------------+
    |  L0: Customer Experience Contracts            |
    |  "Acceptance Tests"                           |
    |  (What customers should perceive/feel)        |
    +----------------------------------------------+
                           |
                    satisfies_experience
                           |
    +----------------------------------------------+
    |  L1: Signal Requirements                      |
    |  "Integration Tests"                          |
    |  (What signals create that perception)        |
    +----------------------------------------------+
                           |
                    satisfies_signal
                           |
    +----------------------------------------------+
    |  L2: Process Contracts                        |
    |  "Unit Tests"                                 |
    |  (What processes must achieve)                |
    +----------------------------------------------+
                           |
                    implements_contract
                           |
    +----------------------------------------------+
    |  L3: Procedures                               |
    |  "Implementation"                             |
    |  (How executor achieves contracts)            |
    +----------------------------------------------+
                           |
                    requires_input
                           |
    +----------------------------------------------+
    |  L4: Input Specifications                     |
    |  "Dependencies"                               |
    |  (Materials, equipment, training)             |
    +----------------------------------------------+
                           |
                    sourced_from
                           |
    +----------------------------------------------+
    |  L5: Sourcing Requirements                    |
    |  "Infrastructure"                             |
    |  (Supply chain)                               |
    +----------------------------------------------+
                           |
                    OPERATE DIRECTION (bottom-up)
```

Each arrow represents a traceability link that the CI/CD pipeline validates. A broken link---a process contract with no signal justification, or a signal requirement with no customer experience goal---is flagged as a potential defect or waste.

**Level 0: Acceptance Contracts.** Level 0 contains three parallel contract types, each representing a different source of requirements:

- *Experience contracts* specify what customers should perceive, feel, and experience. These are the primary design driver, specified using SBT's eight perceptual dimensions with proxy indicators and satisfaction targets. Example: "Espresso taste: balanced, sweet, clean finish, no bitterness. Delivery time: 60--180 seconds."
- *Constraint contracts* specify what regulation, law, or external authority mandates. These are non-negotiable regardless of customer perception. Example: "All 14 EU Annex II allergens declared" (EU Regulation 1169/2011). "HACCP compliance with documented critical control points" (EU Regulation 852/2004).
- *Commitment contracts* specify what the organization has voluntarily committed to beyond legal requirements. These often (but not always) also produce customer-perceived signals. Example: "All coffee sourced from direct trade relationships" satisfies both a commitment contract (organizational values) and an experience contract (ideological dimension: "ethical sourcing visible").

All three contract types are first-class acceptance tests. In software TDD, tests come from user requirements *and* from security standards, accessibility laws, and company policies---no one calls WCAG accessibility tests "waste" because users did not ask for them. The same principle applies here. A process justified only by regulation is not waste; it is a constraint-satisfying process. The revised waste detection rule: a process with no upward link to *any* Level 0 contract---experience, constraint, or commitment---is unjustified.

Some processes satisfy multiple contract types simultaneously. HACCP food safety compliance is legally required (constraint) and produces a "trust and confidence" customer signal (experience). Fair trade sourcing satisfies a commitment contract and creates an ideological dimension signal. These dual-justified processes are the norm, not the exception; pure single-source justification is relatively rare in practice.

Level 0 contracts are executor-invariant, format-invariant, and technology-invariant. A human barista and a robotic system must satisfy the same acceptance tests---whether those tests originate from customer perception, regulation, or organizational values.

**Level 1: Signal Requirements (Integration Tests).** What signals the business must emit to create the desired perception and satisfy constraint requirements. Each signal traces upward to at least one Level 0 contract of any type. Specified across all eight SBT dimensions for experience-derived signals, and as compliance indicators for constraint-derived signals. Example: "Craft preparation visible to customer," "Aroma of fresh coffee present at entrance," "Allergen information accessible at point of sale." A signal requirement with no upward link to any Level 0 contract is unjustified---potential waste.

**Level 2: Process Contracts (Unit Tests).** What each process must achieve to emit the required signals. These are executor-invariant quality gates: measurable outcomes that any implementation must satisfy. Example: "Espresso extraction time: 25--30 seconds. Temperature: 92--94 degrees Celsius. Dose: 17--19 grams. Crema: present, golden-brown, minimum 2 millimeters." A process contract with no upward link to a signal requirement is a process without justification.

**Level 3: Procedures (Implementation).** How a specific executor type achieves the contract. This is the executor-dependent layer---the "code" that the "tests" (contracts) validate. Different executor profiles (human artisan, hybrid-assisted, fully automated) produce different procedures for the same contract. When you swap executor type, the procedures change but the contracts remain stable---just as refactoring changes implementation without changing tests.

**Level 4: Input Specifications (Dependencies).** What materials, equipment, and training the procedures require. Ingredient specifications with measurable parameters (bean origin, roast date constraints, grind size tolerances), equipment requirements (conical burr grinder with stepless adjustment), and training certifications.

**Level 5: Sourcing Requirements (Infrastructure).** Where inputs come from. Supplier criteria, certifications, delivery frequency, lead times. The supply chain layer---analogous to infrastructure in software, where changing a cloud provider should not change application behavior.

### Key Architectural Properties

**Backward traceability.** Every parameter at every level traces back to a customer experience justification. "Why is the extraction temperature 92--94 degrees?" Because the espresso process contract requires it (Level 2), which satisfies the "craft preparation quality" signal (Level 1), which creates the "balanced, sweet, clean finish" customer experience (Level 0). Any parameter that cannot be traced backward is either unjustified or has a missing link in the specification.

**Contract-procedure separation as test-implementation separation.** Approximately 75% of a typical orgschema specification is executor-invariant. The contracts (tests) remain stable across executor profiles. Only the procedures (implementation) change. This has profound implications for franchise models, automation decisions, and knowledge sharing: you can share the test suite without sharing the implementation.

**Forkability as test suite portability.** Sharing a business under orgschema means sharing its test suite. A new operator receives the contracts (what must be achieved) and writes their own procedures (how to achieve it). The depth of the fork determines what changes:

- Fork at Level 0: different customer experience goals---an entirely new business concept.
- Fork at Level 1: same experience goals, different signal strategy---same target perception, different brand expression.
- Fork at Level 2: same quality gates, different procedures---same concept, different execution.
- Fork at Level 3: same contracts, different procedures---franchise-style replication with local adaptation.
- Fork at Level 4: same procedures, different input specifications---same process, different materials or equipment.
- Fork at Level 5: same input specifications, different suppliers---multi-location scaling.

**Figure 2: Fork Depth and What Changes**

```
Fork at L0:  [NEW experience] [NEW signals] [NEW contracts] [NEW procedures] [NEW inputs] [NEW sourcing]
             = Entirely new business concept

Fork at L1:  [SAME experience] [NEW signals] [NEW contracts] [NEW procedures] [NEW inputs] [NEW sourcing]
             = Same target perception, different brand expression

Fork at L2:  [SAME experience] [SAME signals] [SAME contracts] [NEW procedures] [NEW inputs] [NEW sourcing]
             = Same concept, different execution

Fork at L3:  [SAME experience] [SAME signals] [SAME contracts] [NEW procedures] [NEW inputs] [NEW sourcing]
             = Franchise-style replication with local adaptation

Fork at L4:  [SAME experience] [SAME signals] [SAME contracts] [SAME procedures] [NEW inputs] [NEW sourcing]
             = Same process, different materials or equipment

Fork at L5:  [SAME experience] [SAME signals] [SAME contracts] [SAME procedures] [SAME inputs] [NEW sourcing]
             = Multi-location scaling (Friedrichshain demo)
```

This maps directly to the five-level openness taxonomy we have described elsewhere, where Toyota's production system serves as the canonical example of Level 3 openness: sharing the methodology (test suite) while retaining implementation parameters (data) as the competitive moat.[^16]

**CI/CD as satisfaction validation.** The validation pipeline implements six levels of checking, each corresponding to a different class of specification defect:

**Table 2: CI/CD Validation Levels**

| Level | Validation | TDD Analogy | What It Catches |
|:---|:---|:---|:---|
| 1 | Schema validation | Syntax checking | Malformed specifications, missing required fields |
| 2 | Cross-reference integrity | Link checking | Broken references between files, orphaned dependencies |
| 3 | Contract satisfaction | Unit test pass/fail | Procedures that do not meet quality gates |
| 4 | Signal coverage | Integration test coverage | Processes that emit no signals, signals with no source |
| 5 | Experience traceability | Acceptance test coverage | Signals that trace to no customer experience goal |
| 6 | Waste detection | Dead code analysis | Processes, inputs, or suppliers with no upward justification |

### The Maturity Model

Existing businesses need not adopt orgschema comprehensively from the start. We propose a six-level maturity model for progressive formalization:

| Level | State | What CI/CD Validates | Value |
|:---|:---|:---|:---|
| M0 | Processes exist as tribal knowledge | Nothing | Baseline (most businesses) |
| M1 | Process categories and required fields defined | Schema completeness | "We know what we need to specify" |
| M2 | Quality gates and compliance requirements specified | Contract satisfaction | "We know what each process must achieve" |
| M3 | Execution steps documented for current executor profile | Procedure-contract alignment | "We know how we do things" |
| M4 | Full backward traceability to customer experience | Experience traceability, waste detection | "We know why we do everything" |
| M5 | CI/CD runs full satisfaction validation on every change | All levels, regression detection | "Every change is tested against customer experience" |

The migration path for existing businesses follows characterization testing---writing tests that capture the current behavior of existing systems before refactoring, a well-established practice in legacy software maintenance.[^17] Phase 1 audits customer experience (mystery shopping, gap analysis). Phase 2 maps current versus desired signals. Phase 3 characterizes processes, starting with customer-facing operations. Phase 4 documents inputs and sourcing. Phase 5 establishes the CI/CD pipeline and runs the first validation cycle.

### Large Language Models as Essential Enabler

Orgschema's multi-level TDD cascade operates across many dimensions simultaneously: customer experience across eight or more perceptual dimensions, signal requirements across dozens of touchpoints, process contracts across all operations, cross-references between hundreds of specification parameters. This multi-dimensional complexity was always theoretically sound but practically unmanageable for human operators with traditional tools.

Large language models change the feasibility equation. Orgschema specifications are structured data (YAML) that LLMs read natively---no parsing, no interpretation, no ambiguity. The TDD cascade is a directed graph that an LLM can traverse: from experience goals through signals through contracts through procedures through inputs to sourcing. An LLM can answer "What allergens does the oat latte contain?" by traversing the specification. It can perform impact analysis: "If we change this supplier, which customer experience goals are affected?" It can detect waste: "Show me all parameters with no customer-experience justification."

**Table 4: LLM Impact on Orgschema Feasibility**

| Task | Without LLM | With LLM |
|:---|:---|:---|
| Initial specification generation | Weeks of interviews and encoding | Feed existing SOPs to LLM; first-draft YAML in hours |
| Cross-reference integrity | Manual checking across files | Instantaneous traversal and broken-link detection |
| Backward traceability audit | Impractical at scale | "Show all parameters with no experience justification" |
| Waste detection | Requires process consultant | LLM identifies unjustified processes automatically |
| New product addition | Manual cascade traversal | LLM generates full cascade from experience goal |
| Executor profile swap | Rewrite all procedures manually | LLM generates new procedures from existing contracts |
| Change impact analysis | Manual dependency tracing | "If we change this supplier, which experience goals are affected?" |

We argue that orgschema is a methodology whose time has arrived because of LLMs. The theoretical framework was always valid. The practical bottleneck was the complexity of maintaining multi-dimensional cross-referenced specifications manually. LLMs remove that bottleneck. This positions orgschema not as an AI product but as a design methodology that becomes practical in the AI era---a distinction that matters for adoption.

## Demonstration: Spectra Coffee

To validate the methodology, we developed a complete orgschema specification for Spectra Coffee, a specialty coffee operation in Berlin. The demonstration encompasses 23 YAML specification files across all six TDD cascade levels, plus a CI/CD validation pipeline.

### Specification Scope

The Spectra Coffee specification includes:

**Level 0 (Customer Experience Contracts):** 25 acceptance tests across eight SBT dimensions, with proxy indicators and satisfaction targets. The spectral profile scores experiential perception highest (9/10), followed by semiotic and temporal dimensions (7/10), with economic scoring lowest (5/10)---a deliberate design choice reflecting the brand's positioning as a craft-focused, experience-rich operation.

**Level 1 (Signal Requirements):** 18 integration tests mapping required signals to SBT dimensions. Each signal traces to at least one Level 0 customer experience goal. Four observer cohort profiles (morning regular, weekend explorer, delivery app user, food inspector) demonstrate that identical signals produce different perceptions depending on observer priors---validating SBT's anti-ergodic epistemology.

**Level 2 (Process Contracts):** Quality gates for all core processes---espresso extraction, milk preparation, food handling, opening and closing procedures, equipment maintenance, quality control. All measurements in SI units (grams, milliliters, seconds, degrees Celsius) with explicit tolerances. To illustrate the cascade concretely, consider the espresso extraction process contract:

```yaml
espresso_extraction:
  quality_gates:
    extraction_time_s: [25, 30]
    temperature_c: [92, 94]
    dose_g: [17, 19]
    yield_ml: [28, 32]
    crema: "present, golden-brown, minimum 2mm"
  satisfies_signal:
    - "craft_preparation_visible"
    - "aroma_fresh_coffee"
  satisfies_experience:
    - "taste_balanced_sweet_clean"
    - "delivery_within_180s"
```

Each quality gate is a measurable test. The `satisfies_signal` and `satisfies_experience` fields are the upward traceability links---the reason this contract exists. A change to any quality gate parameter triggers the CI/CD pipeline, which verifies that the change does not break the satisfaction chain above it.

**Level 3 (Procedures):** Detailed execution steps for the human artisan executor profile. The specification notes that approximately 75% of content is executor-invariant: contracts remain stable across executor types, and only procedures change.

**Level 4 (Input Specifications):** Ingredient specifications with measurable parameters (single-origin arabica, roasted within 21 days, ground immediately before use), equipment requirements, and training certifications.

**Level 5 (Sourcing Requirements):** Supplier criteria, certifications (EU organic, fair trade), delivery schedules, and lead times. All pricing in euros (Berlin market).

### Compliance and Safety

The specification includes a 14-allergen declaration matrix compliant with EU Regulation 1169/2011 Annex II and a HACCP hazard analysis covering seven process steps and eleven identified hazards across five critical control points. These compliance specifications participate in the TDD cascade: they trace upward through signal requirements ("safety and compliance visible") to customer experience goals ("trust and confidence in food safety").

### Fork Demonstration

To validate forkability as test suite portability, we created a location fork for a hypothetical second Spectra Coffee in Berlin-Friedrichshain. The fork overrides six parameters at Level 5 (sourcing): different local suppliers, adjusted delivery schedules, modified opening hours for the neighborhood's demographics. Levels 0 through 2---customer experience contracts, signal requirements, and process contracts---remain identical. The test suite is portable; only the implementation details change.

### Executor Swap Scenario

A scenario analysis examines what happens when the executor profile changes from human artisan to fully automated:

**Table 3: Executor Swap Impact Analysis**

| TDD Level | Human Artisan | Fully Automated | Delta |
|:---|:---|:---|:---|
| L2: Process contracts (unit tests) | All pass | All pass | No change |
| L1: Signal requirements (integration tests) | 18/18 satisfied | 15/18 satisfied | -3 signals lost |
| L0: Experience contracts (acceptance tests) | All pass | 2 fail | "Personal rapport" and "craft as performance" |
| Spectral profile (SBT 8-dimension average) | 6.6 | 5.6 | -1.0 (15% decline) |

All Level 2 process contracts pass---the machine produces espresso within specified tolerances. But the cascade reveals that passing unit tests is insufficient: the integration and acceptance tests expose signal and experience degradation invisible to process-level metrics. This demonstrates that executor choice is a brand decision, not merely an operational one---a finding that the TDD cascade makes visible and quantifiable.

### Validation Pipeline

A CI/CD pipeline implemented in GitHub Actions validates specifications on every commit. The pipeline currently implements four of six validation levels: schema validation (JSON Schema), cross-reference integrity, signal coverage, and experience traceability. All four levels pass with zero errors and zero warnings. The pipeline serves as the "test runner" in TDD terms---automated verification that operational specifications satisfy their design intentions.

## Evaluation

We evaluate the orgschema methodology using the FEDS framework's formative evaluation strategy.[^14] Five independent reviewers, each representing a distinct stakeholder perspective, assessed the Spectra Coffee demonstration against criteria relevant to their domain.

### Expert Panel

**Quality Assurance Inspector.** Evaluated process specifications against ISO 9001 quality management principles and HACCP compliance requirements. Assessed whether process contracts contain sufficient measurable criteria to function as quality gates. Identified defects in allergen cross-referencing and HACCP hazard coverage, both subsequently corrected.

**Process Consultant.** Evaluated the TDD cascade's internal consistency and practical applicability. Assessed whether backward traceability chains are complete and whether the maturity model provides a realistic adoption pathway. Identified gaps in the signal-to-experience mapping, subsequently addressed through the creation of explicit signal requirements (Level 1 integration tests).

**Academic Researcher.** Evaluated the methodology's theoretical grounding, novelty claims, and relationship to existing literature. Confirmed that no existing framework combines multi-level TDD, backward traceability, and CI/CD satisfaction validation. Recommended strengthening the Beer Viable System Model mapping and the LLM enabler argument.

**Professor and Graduate Student.** Evaluated the methodology's pedagogical clarity and usefulness as a teaching case. Confirmed that the Spectra Coffee demonstration is sufficiently complete to serve as an MBA case study. Noted that the zero-cost orgschema toolkit compares favorably to commercial business simulation platforms costing 14 to 107 dollars per student.

**Coffee Shop Manager.** Evaluated practical relevance from the operator's perspective. Confirmed that process specifications reflect realistic operations. Identified missing parameters in equipment maintenance schedules and opening procedures, subsequently added.

### Evaluation Results

The panel identified a total of 14 defects: 3 critical, 5 major, and 6 minor. All critical and major defects were corrected during the formative evaluation cycle.

**Critical defects** included: incomplete allergen cross-referencing (the oat latte specification listed "oat" as an allergen but did not reference the 14-allergen EU Regulation 1169/2011 Annex II matrix), missing HACCP hazard coverage for two process steps (grinding and milk storage), and a broken traceability chain where one product's `satisfies_signal` annotation referenced a signal identifier that did not exist in the signal requirements file.

**Major defects** included: absence of explicit Level 1 signal requirements (the gap between Level 0 experience contracts and Level 2 process contracts was initially unmediated), missing execution profile metadata on the organization specification (preventing executor-swap analysis), insufficient granularity in equipment maintenance schedules, incomplete opening/closing procedures, and inconsistent currency representation across product files.

**Minor defects** included formatting inconsistencies, missing optional metadata fields, and documentation gaps in the signal map.

The correction cycle demonstrates the methodology's self-healing property: because defects are identified through the same cascade traversal that orgschema specifies, the evaluation process *is* the methodology. The QA inspector's allergen finding, for example, was precisely the kind of cross-reference integrity check that orgschema's CI/CD Level 2 validation automates. After correction, the automated pipeline catches the same class of defect on every subsequent commit.

The evaluation validates three claims about the methodology:

First, *instrument validity*: the specification language (YAML with JSON Schema validation) adequately captures business operations at a level of detail sufficient for quality management, compliance, and operational execution. The coffee shop manager confirmed that specifications reflect realistic practice; the quality assurance inspector confirmed they meet compliance documentation standards. Notably, the inspector's assessment applied the same rigor used for ISO 9001 documentation review, finding the orgschema specifications structurally superior to Word-based quality documentation because of automated cross-reference validation.

Second, *purpose validity*: the methodology achieves its stated purpose of producing testable, traceable, forkable business specifications. The CI/CD pipeline validates satisfaction at four of six levels. The fork demonstration (Friedrichshain location variant, 6 parameter overrides at Levels 3--5, identical Levels 0--2) proves test suite portability. The executor swap scenario demonstrates that the TDD cascade makes otherwise invisible trade-offs quantifiable---the process consultant noted that the 15% spectral profile degradation from human-to-automated execution would be invisible without the multi-dimensional measurement framework.

Third, *practical adoptability*: the maturity model provides a realistic incremental path. Even M1 (knowing what you need to specify) represents a significant operational clarity improvement over M0 (tribal knowledge). The professor confirmed that M0-to-M2 migration (from tribal knowledge to contract-level specification) is achievable in a single working day for a simple operation, using LLM-assisted specification generation. The LLM-accelerated migration path makes initial specification generation feasible within hours rather than weeks.

## Discussion

### Implications for Operations Management

Orgschema's core proposition for operations managers is "manage by test results." Rather than monitoring operational metrics in isolation, a manager using orgschema can see which customer experience goals (acceptance tests) are satisfied, which signal requirements (integration tests) are met, and which process contracts (unit tests) pass their quality gates. A process that meets all its internal metrics but fails to satisfy the signal requirements above it is not meeting quality standards---the TDD cascade makes this visible.

The backward traceability architecture also enables a new form of waste detection. Any process, procedure, input specification, or sourcing requirement that cannot be traced upward to a customer experience justification is, by definition, organizational waste. This extends lean thinking from production waste to specification waste---processes that exist without justification.

### Mapping to Beer's Viable System Model

Orgschema's structure maps to Beer's Viable System Model, providing theoretical grounding in organizational cybernetics.[^18]

**Table 5: Orgschema to Viable System Model Mapping**

| VSM System | Function | Orgschema Mapping | Specification Strength |
|:---|:---|:---|:---|
| S1 (Operations) | Primary activities | Product specs, process procedures | Strong (6 products, 4 process files) |
| S2 (Coordination) | Harmonizing S1 units | Internal communications protocols | Strong (581 lines; addresses PII12 pathology) |
| S3 (Operational Mgmt) | Resource allocation, control | Quality control, compliance, HACCP | Strong (5 critical control points) |
| S3* (Audit) | Monitoring, verification | CI/CD validation pipeline | Moderate (4 of 6 levels implemented) |
| S4 (Intelligence) | Environmental scanning | Signal map, observer profiles | Thin (acknowledged limitation) |
| S5 (Identity/Policy) | Organizational identity | Organization, brand identity specs | Strong (identity layer specified) |

System 2 is notably well-specified---unusual for organizations, where Beer identified thin coordination as a common pathology (disjointed behavior from under-resourced S2).[^19] The 581-line internal communications specification---governing information flows between roles, meeting cadences, escalation protocols, and cross-functional coordination---directly addresses what Perez Rios identifies as one of the 17 most common organizational pathologies. System 3* (the audit channel) maps to orgschema's CI/CD validation pipeline, providing continuous monitoring that Beer's original model envisioned but could not implement with 1980s technology. System 4 is acknowledged as thin, representing the boundary where SBT's environmental scanning and the observer-cohort analysis begin to address strategic intelligence---a limitation shared with most operational specification systems, which focus on internal coordination (S1--S3) rather than environmental adaptation (S4--S5). The VSM mapping validates orgschema's completeness as an organizational specification while highlighting productive directions for future development.

### Rethinking Franchises as Test Suite Licensing

The contract-procedure separation has implications for franchise models. Traditional franchises share implementation: detailed operational manuals specifying how to do everything. Franchisees who deviate from the manual risk termination. The franchise relationship is based on implementation compliance---following the prescribed procedures exactly.

Orgschema suggests an alternative: sharing the test suite (contracts) without prescribing the implementation (procedures). An "orgschema franchise" would specify what each process must achieve (quality gates, signal requirements, experience contracts) while leaving franchisees free to determine how to achieve it. Compliance means passing the tests, not following the manual. This addresses the information asymmetry problems documented in franchise economics[^20] by making performance objectively verifiable without constraining innovation.

Toyota's production system serves as a historical precedent. For decades, Toyota shared its methodology (the "tests"---principles, quality standards, process categories) while retaining its implementation details (specific parameters, supplier relationships, tacit knowledge).[^16] The methodology publication strengthened Toyota's position by creating an ecosystem that spoke its language. Orgschema's openness taxonomy formalizes this pattern.

### Organizational Openness as Test Suite Sharing

We have proposed a five-level openness taxonomy for orgschema specifications, ranging from fully closed (proprietary specifications) to what we term a "glass factory" (fully transparent operations).[^21] The taxonomy maps directly to what part of the test suite and implementation is shared:

- Level 1 (Closed): nothing shared.
- Level 2 (Open Schema): the specification structure is public (what parameters exist, what should be measured) but specific values are private.
- Level 3 (Open Reference): a reference implementation is shared as a starting template.
- Level 4 (Open Core): the full specification logic is shared; competitive advantage comes from implementation quality and proprietary data.
- Level 5 (Glass Factory): everything is transparent in real time.

The Spectra Coffee demonstration operates at Level 3 (Open Reference): the full specification is published as a starting template that others can fork and customize, while the competitive advantage of any real business using it would come from execution quality and proprietary parameter values.

Schema publication---making visible what parameters a well-run business should control---is itself valuable. Less experienced operators may not have realized what they need to measure. The schema reveals the dimensions of excellence without revealing the specific calibrations that produce it. This maps to what Chesbrough and Appleyard describe as value creation through open innovation platforms.[^22]

### Cross-Industry Perception Transplant

The separation of perception specification (Level 0) from operational implementation (Levels 1--5) enables a radical form of knowledge transfer: the *perception transplant*. If a brand's spectral profile---its pattern of perception across SBT's eight dimensions---can be measured quantitatively, that profile becomes a portable Level 0 acceptance test applicable to any industry.

Consider a concrete example. Apple's brand perception might be measured across observer cohorts as: experiential 9, semiotic 9, temporal 8, ideological 8, social 8, economic 8 (premium-as-signal). This spectral *shape*---the relative emphasis across dimensions---is what produces willingness to pay twice the price for functionally equivalent products. Now transplant that shape as the Level 0 acceptance test for a specialty coffee operation. The absolute values and the digital-to-analogue ratio shift (a physical coffee shop cannot replicate Apple's 0.85 digital dominance), but the relative emphasis transfers: semiotic and experiential as dominant dimensions, premium pricing as a quality signal rather than a barrier, social belonging through brand identification.

Orgschema's TDD cascade then derives everything backward from the transplanted profile. What signals must a coffee shop emit to achieve Apple-like perception scores? Minimalist interior design (semiotic), precision in every tactile surface (experiential), seasonal innovation cadence (temporal), premium materials throughout (economic-as-signal). What processes emit those signals? What inputs and sourcing? Every investment---custom ceramics, extended barista training, direct-trade sourcing---traces to a specific dimension of the target perception profile.

This introduces a third fork type beyond those previously discussed:

**Table 6: Three Fork Types**

| Fork Type | What Is Copied | What Is Rewritten | Example |
|:---|:---|:---|:---|
| Location fork | L0--L4 (everything except sourcing) | L5 (suppliers, schedules) | Spectra Coffee Friedrichshain |
| Business fork | L0--L2 (test suite) | L3--L5 (implementation) | Same concept, different execution |
| Perception transplant | L0 shape only (spectral profile) | L1--L5 (everything else) | "Apple's emotional architecture, applied to coffee" |

The perception transplant is the most radical: you copy neither the business nor its test suite implementation, only the *acceptance criteria*---the shape of desired perception. The entire operational stack is designed from scratch to satisfy a borrowed emotional architecture. This has implications for competitive intelligence (a coffee shop's real perception competitor may be Aesop or Muji, not another coffee shop), for investment justification (every expenditure traces to a dimension of the target profile), and for brand strategy (perception engineering from measured first principles rather than intuition).

### The "Just Documentation" Rebuttal

A predictable objection is that orgschema specifications are merely "documentation in YAML." The rebuttal is simple and definitive: documentation cannot run tests. Orgschema specifications are testable artifacts with automated validation pipelines. Every parameter has a traceable justification chain. Every change is verified against customer experience satisfaction through an automated pipeline. A Word document describing espresso preparation cannot be validated against a customer experience contract. An orgschema specification can be---and is, on every commit.

The distinction parallels the difference between a software requirements document and a test suite. Both describe what a system should do. Only the test suite verifies that it does.

## Limitations and Future Research

Several limitations constrain the current work. First, the demonstration covers a single business type (specialty coffee) at a single level of complexity (small, single-location). While the methodology is domain-agnostic, validation across industries---particularly in services with higher regulatory complexity or in manufacturing---would strengthen generalizability.

Second, Level 0 acceptance tests for customer experience are inherently qualitative. Goals such as "warm, competent, unhurried" require proxy metrics (delivery time, greeting acknowledgment time) that capture partial aspects of the desired experience. Whether proxy metrics can adequately represent the full dimensionality of customer perception is an open question that connects to ongoing debates in service quality measurement.[^23]

Third, the current CI/CD pipeline validates structural properties (schema, cross-references, coverage) but cannot yet validate experiential properties (does the espresso actually taste balanced?). Closing this gap requires integration with operational telemetry---sensor data, point-of-sale analytics, customer feedback---which represents a significant engineering challenge.

Fourth, the evaluation relies on formative expert assessment rather than summative field validation. A naturalistic evaluation---deploying orgschema in an operating business and measuring outcomes over time---would provide stronger evidence for the methodology's practical impact.

Future research directions include: automated test generation (can an LLM generate process contracts from signal requirements, or procedures from contracts, making orgschema a generative methodology?); regression testing for business changes (when a supplier changes, which customer experience tests might break?); multi-location test variance (should different locations share identical acceptance tests or adapt them to local cohorts?); digital output provenance (when every process is specified, every physical output can carry a digital trace of its full production history---filtered by audience through the openness taxonomy---enabling customers to query the provenance of their purchase at any depth); and integration with ISO 9001:2026, which introduces requirements for digital quality management that align with orgschema's specification-first approach.[^24]

## Conclusion

The Organizational Schema Theory methodology applies Test-Driven Development to business design. Customer experience goals, regulatory constraints, and organizational commitments are acceptance tests. Signal requirements are integration tests. Process contracts are unit tests. Procedures are the implementation. The CI/CD pipeline is the test runner. The result is businesses where every operational parameter traces back to a justification---whether customer-derived, legally mandated, or values-driven---where changes are validated against satisfaction criteria, and where operational knowledge is shareable as a test suite rather than as a procedures manual.

The methodology's practical feasibility depends on large language models. The multi-dimensional complexity of maintaining cross-referenced specifications across six hierarchical levels, eight perceptual dimensions, and hundreds of operational parameters was always theoretically sound but practically unmanageable. LLMs change this equation---not by replacing human judgment about what customers should experience, but by making the tedious work of cascade traversal, consistency checking, and impact analysis feasible at scale. Orgschema is a methodology whose time has arrived because of AI.

The broader implication extends beyond any single business. If operational specifications are testable, they are comparable. If they are version-controlled, they accumulate institutional knowledge. If they are forkable, they enable new models of organizational knowledge sharing that go beyond the franchise manual. The question is not whether businesses will be specified as testable artifacts---the convergence of declarative process management, infrastructure-as-code, and AI-native workflows makes this trajectory likely. The question is whether they will be designed forward from available resources or backward from desired customer experience. Orgschema argues for backward.

---

[^1]: Kent Beck, *Test-Driven Development: By Example* (Boston: Addison-Wesley, 2003).

[^2]: Taiichi Ohno, *Toyota Production System: Beyond Large-Scale Production* (Portland: Productivity Press, 1988).

[^3]: W. Edwards Deming, *Out of the Crisis* (Cambridge: MIT Press, 1986).

[^4]: G. Lynn Shostack, "Designing Services That Deliver," *Harvard Business Review* 62, no. 1 (1984): 133--139.

[^5]: Alan R. Hevner, Salvatore T. March, Jinsoo Park, and Sudha Ram, "Design Science in Information Systems Research," *MIS Quarterly* 28, no. 1 (2004): 75--105.

[^6]: Maja Pesic and Wil M. P. van der Aalst, "A Declarative Approach for Flexible Business Processes Management," in *Business Process Management Workshops*, Lecture Notes in Computer Science (Berlin: Springer, 2006).

[^7]: Alberto Cespedes, Hajo A. Reijers, and Jan Mendling, "Business Process Architecture and DevOps: A Synergistic Adoption," *Information and Software Technology* 116 (2019).

[^8]: Grant Wiggins and Jay McTighe, *Understanding by Design* (Alexandria: ASCD, 1998).

[^9]: Yoji Akao, ed., *Quality Function Deployment: Integrating Customer Requirements into Product Design* (Portland: Productivity Press, 1990). The methodology was first developed by Akao in 1966.

[^10]: Clayton M. Christensen, Scott D. Anthony, Gerald Berstell, and Denise Nitterhouse, "Finding the Right Job for Your Product," *MIT Sloan Management Review* 48, no. 3 (2007): 38--47. The JTBD framework originates from Christensen's earlier work on disruptive innovation.

[^11]: Spectral Brand Theory models brand perception across eight observer-dependent dimensions. The framework is detailed in the SBT specification (https://github.com/spectralbranding/sbt-framework). Orgschema uses SBT as the specification language for Levels 0 and 1 of the TDD cascade.

[^12]: The echeloned DSR (eDSR) approach decomposes the research project into five validated echelons, each providing intermediate validation. This addresses the common DSR criticism that single demonstrations are insufficient evidence.

[^13]: This distinction---artifact as methodology versus artifact as instantiation---is critical for DSR contributions. The Spectra Coffee demo validates the methodology; it is not the methodology itself.

[^14]: John Venable, Jan Pries-Heje, and Richard Baskerville, "FEDS: A Framework for Evaluation in Design Science Research," *European Journal of Information Systems* 25, no. 1 (2016): 77--89.

[^15]: The Design Science Validity Framework specifies five validity types: instrument, technical, design, purpose, and generalization. We address instrument and purpose validity; technical validity is partially addressed through the CI/CD pipeline.

[^16]: The Toyota Production System exemplifies Level 3 ("Open Core") in orgschema's openness taxonomy. Toyota published the methodology---14 principles, quality standards, process categories---while retaining implementation parameters---specific takt times, supplier contracts, tacit knowledge. The NUMMI case demonstrated that methodology transfer without data transfer has approximately a 10% success rate, validating the schema-data distinction as a competitive moat. See Jeffrey K. Liker, *The Toyota Way* (New York: McGraw-Hill, 2004).

[^17]: Michael C. Feathers, *Working Effectively with Legacy Code* (Upper Saddle River: Prentice Hall, 2004). Characterization tests capture the current behavior of existing code, enabling safe refactoring. Orgschema applies the same principle to existing business operations.

[^18]: Stafford Beer, *Brain of the Firm*, 2nd ed. (Chichester: John Wiley, 1981); Stafford Beer, *The Heart of Enterprise* (Chichester: John Wiley, 1979).

[^19]: Jose Perez Rios, *Design and Diagnosis for Sustainable Organizations: The Viable System Method* (Berlin: Springer, 2012). Perez Rios identifies 17 organizational pathologies; "disjointed behavior" (PII12) from thin System 2 coordination is among the most common.

[^20]: Paul H. Rubin, "The Theory of the Firm and the Structure of the Franchise Contract," *Journal of Law and Economics* 21, no. 1 (1978): 223--233; Francine Lafontaine, "Agency Theory and Franchising: Some Empirical Results," *RAND Journal of Economics* 23, no. 2 (1992): 263--283.

[^21]: The five-level openness taxonomy ranges from Closed (Level 1) to Glass Factory (Level 5). Each level corresponds to increasing transparency of the specification (test suite) and implementation (procedures and data).

[^22]: Henry Chesbrough and Wim Appleyard, "Open Innovation and Strategy," *California Management Review* 50, no. 1 (2007): 57--76.

[^23]: A. Parasuraman, Valarie A. Zeithaml, and Leonard L. Berry, "A Conceptual Model of Service Quality and Its Implications for Future Research," *Journal of Marketing* 49, no. 4 (1985): 41--50.

[^24]: ISO 9001:2026 (currently at Draft International Standard stage, published August 2025) introduces requirements for digital quality management systems that align with orgschema's specification-first approach. Orgschema can be positioned as an implementation pathway for the new standard.

