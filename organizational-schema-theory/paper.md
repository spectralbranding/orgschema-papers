# Machine-Checkable Acceptance Contracts for Organizational Design: A Design-Science Theory of Specification Cascades

Dmitry Zharnikov

ORCID: 0009-0000-6893-9231

DOI: [10.5281/zenodo.18946043](https://doi.org/10.5281/zenodo.18946043)

Working Paper v2.1.0 – March 2026 (revised July 2026)

## Abstract

Organizations possess many mechanisms that touch on quality and control: quality-management systems, enterprise-architecture frameworks, balanced scorecards, business-process conformance checking, requirements engineering, and cybernetic control. Each verifies process conformance or lagging outcomes. None makes a machine-checkable, ex-ante acceptance contract at the experience layer with backward traceability a structural invariant of the specification. This paper develops Organizational Schema Theory (OST), a design-science artifact that supplies this property through a six-level specification cascade in which stakeholder-experience contracts function as acceptance tests, signal requirements as integration tests, and process contracts as unit tests, with executor-invariance and continuous validation. The artifact is stated as six design principles, four mechanisms, and six boundary conditions, and formalized as a typed directed acyclic justification graph on which traceability, waste, cascade-compression, and reference-class relativity are decidable or falsifiable properties; a smallest-sufficient model gives a compression-impossibility sketch. Following the design-science evaluation taxonomy, the artifact is evaluated analytically, through independent industry convergence, and through a public demonstration corpus, with no controlled-outcome claim. The contribution is nascent design theory: acceptance testing operationalized as a tool-checkable invariant of organizational specification.

**Keywords:** design science research, organizational design, acceptance testing, specification cascade, backward traceability, executor-invariance

---

Consider a common pattern in business operations. A cafe owner selects a commercial espresso machine, hires baristas with varying levels of training, sources coffee beans from a convenient distributor, and opens for business. Customers arrive and form impressions. Some return; others do not. When the owner eventually wonders why weekend visitors seem dissatisfied, the investigation must work backward through a tangle of undocumented decisions—from customer perception through staff behavior through equipment calibration through ingredient sourcing—with no systematic way to trace which operational parameter affects which outcome.

This forward-design pattern—starting from available resources and allowing stakeholder experience to emerge as an undesigned consequence—is how most organizations operate. From a design perspective it is a system whose most consequential outputs are never specified: there is no mechanism to verify, before an operational decision is implemented, that it satisfies a stakeholder-defined quality criterion. Quality documentation records what should happen; whether operations actually deliver stakeholder value is checked only through periodic audits that sample a fraction of non-conformances [@vanderaalst-2016-process-mining-data].

It is tempting to state the gap in absolute terms—that organizational design, alone among design disciplines, lacks acceptance testing. That framing does not survive contact with the literature. Organizational control, quality management, enterprise architecture, process governance, requirements engineering, and performance measurement all provide mechanisms that verify some relationship between an organization and a standard. The defensible claim is narrower and more precise. Each of these mechanisms verifies either *process conformance*—does execution match the model?—or *lagging outcomes*—did the measured indicator move? None of them makes the following property a structural invariant of the specification itself: every operational parameter carries a tool-verifiable trace to a stakeholder-experience criterion that is expressed as a runnable acceptance test, and that trace is re-validated automatically on every change. This is a *machine-checkable, ex-ante acceptance contract at the experience layer with backward traceability*. It is the property this paper contributes, and Section 2 establishes systematically that no adjacent tradition supplies it jointly.

We treat acceptance testing—"specify the desired outcome, then verify the artifact against that specification before and during deployment"—not as a software practice imported into management but as a generic design principle of which software test-driven development is one rigorous instance. Test-Driven Development [@beck-2002-testdriven-development-by] is cited because it is the most rigorous formalization of the construct available, not because organizations are software systems.

This paper makes three contributions. First, it develops a design-science artifact—the six-level specification cascade with executor-invariant contract layers and continuous validation—that makes experience-layer acceptance testing a tool-checkable invariant, stated as explicit design principles, mechanisms, and boundary conditions. Second, it isolates what is genuinely new from what is adaptation and synthesis, and formalizes the new element: a typed directed acyclic justification graph on which completeness, acyclicity, specification waste, and executor-invariance are decidable properties, together with a cascade-compression impossibility sketch that no adjacent tradition possesses. Third, it frames the artifact as nascent design theory [@gregor-hevner-2013-positioning] and evaluates it honestly within the design-science evaluation taxonomy [@venable-2016-feds] as analytical, naturalistic-observational, and demonstration evidence—explicitly not as controlled outcome evidence.

The paper proceeds as follows. Section 2 positions the artifact against six adjacent literatures and delineates adaptation from innovation. Section 3 presents the design-science method and the artifact's design-theory components. Section 4 develops the artifact: design principles, mechanisms, and the six-level cascade. Section 5 gives the formal model. Section 6 states the empirical hypotheses as a forward research agenda. Section 7 provides an illustrative walkthrough. Section 8 evaluates the artifact. Section 9 discusses implications, boundary conditions, and limitations.

## 2. Related Work and Positioning

### 2.1 The property and the comparison axis

The contribution is best stated as a conjunction of four properties. An acceptance contract is *ex-ante* if it is verified before and during deployment rather than after; it is at the *experience layer* if the criterion it encodes is a stakeholder-defined outcome rather than an internal process metric; it is *machine-checkable* if satisfaction is decided automatically rather than by human inspection at an audit; and it is *backward-traceable* if every operational parameter is formally linked to at least one such criterion. Table 1 compares six established traditions against these four properties. The claim is not that any tradition is deficient in isolation—each is mature and effective at what it does—but that none supplies the four jointly, and that the reason in each case is structural rather than an oversight.

**Table 1: Six Adjacent Traditions Against the Four-Property Axis.**

| Tradition | Ex-ante | Experience-layer | Machine-checkable | Backward-traceable |
|:---|:---:|:---:|:---:|:---:|
| BPM conformance checking (van der Aalst [-@vanderaalst-2016-process-mining-data]; Dumas et al. [-@dumas-2018-fundamentals-bpm]) | ~ | — | ✓ | — |
| Enterprise architecture (Zachman [-@zachman-1987-framework-information-systems]; The Open Group [-@opengroup-2018-togaf-standard]) | ✓ | — | — | ~ |
| Balanced scorecard / performance measurement [@kaplan-1996-balanced-scorecard-translating] | — | ✓ | — | ~ |
| Requirements engineering / declarative process spec (van der Aa et al. [-@vanderaa-2019-extracting-declarative]) | ✓ | — | ✓ | ~ |
| ISO 9001 quality management systems | ~ | ~ | — | ~ |
| Cybernetic control [@beer-1979-the-heart-of] | ✓ | ✓ | — | — |
| **Organizational Schema Theory** | **✓** | **✓** | **✓** | **✓** |

*Notes*: ✓ = provided by design; ~ = partial or domain-limited; — = absent. Ratings are structural judgments about each tradition's design intent, not measurements of any deployment; they are argued individually in the text below.

### 2.2 Conformance checking operates below the experience layer

Conformance checking has become a mature subfield of business process management. Van der Aalst [-@vanderaalst-2016-process-mining-data] established process mining as a systematic approach to discovering, monitoring, and improving processes from event logs; Dumas et al. [-@dumas-2018-fundamentals-bpm] codify the BPM lifecycle and conformance techniques. These methods verify whether process execution matches a process model at the process level. They do not ask whether the process model itself satisfies a stakeholder-experience criterion. An organization can achieve perfect conformance while systematically failing to deliver stakeholder value, if its process models were never derived from experience-level acceptance criteria. Recent work extends declarative process specification toward machine-readable constraints, including extraction of declarative models from natural language (van der Aa et al. [-@vanderaa-2019-extracting-declarative]); this moves the process layer closer to specification but does not install an experience-layer acceptance contract with backward traceability above it. Backward traceability itself has a long lineage in requirements engineering, where the traceability problem—maintaining links between requirements and their downstream realizations—was named by Gotel and Finkelstein [-@gotel-1994-requirements-traceability-problem]; OST's departure from that tradition is to make the trace a continuously re-checked structural invariant rather than a hand-maintained artifact that degrades between reviews. Conformance checking supplies horizontal verification (does execution match the model?); OST supplies the missing vertical verification (does the model satisfy an experience-level acceptance test?).

### 2.3 Enterprise architecture classifies but does not validate against outcomes

TOGAF [@opengroup-2018-togaf-standard] and Zachman [-@zachman-1987-framework-information-systems] provide structured approaches to enterprise architecture. Both are classification systems, not validation systems: they prescribe what to document and how to organize it, but they do not specify what the documentation should achieve or provide a mechanism to verify it automatically against stakeholder-defined outcomes. IS reviewers will reasonably ask how OST differs from Zachman; the difference is that OST's cells are runnable predicates linked by machine-checked traces, whereas the Zachman framework is a taxonomy of representations.

### 2.4 Balanced scorecards track lagging outcomes, not ex-ante contracts

Kaplan and Norton's [-@kaplan-1996-balanced-scorecard-translating] Balanced Scorecard is the closest existing approach to vertical linkage: strategy maps connect financial objectives to customer propositions, internal processes, and learning. But the scorecard is a measurement system, not a specification system. It tracks whether strategic objectives are being achieved—lagging indicators—without specifying the operational parameters that should produce them or validating the causal chain continuously. Where the scorecard asks "are we achieving our objectives?", OST asks "does every operational parameter trace to a stakeholder-defined outcome, and does changing any parameter break that trace?".

### 2.5 Quality management verifies conformance at planned intervals

ISO 9001 quality management systems reference customer focus (clause 5.1.2) and require internal audits at planned intervals (clause 9.2). The customer criterion is referenced, not encoded as a runnable acceptance test, and verification is periodic rather than continuous. We return to a direct, explicitly illustrative comparison with ISO 9001 documentation in Section 7; we do not present that comparison as establishing superiority.

### 2.6 Cybernetic control theorizes the audit channel but does not make it structural

Beer's [-@beer-1979-the-heart-of] Viable System Model describes an audit channel (S3\*) as sporadic, direct, unannounced monitoring—a safeguard against reporting distortion—and provides no mechanism demonstrating that operational activity is justified by identity-level commitments. OST realizes what Beer theorized as a sporadic channel as a continuous structural invariant, and adds the upward traceability from operations to identity that the VSM leaves implicit. We develop this mapping in Section 9.

### 2.7 Adaptation, synthesis, and innovation

Reverse design—specifying desired outcomes first and deriving operations backward—is not novel to OST. Backward design in curriculum [@wiggins-1998-understanding-by-design], Quality Function Deployment [@akao-1990-quality-function-deployment, developed 1966], the lean pull system [@ohno-1988-toyota-production-system], and quality-as-customer-defined [@deming-1986-out-of-the] all instantiate it. OST *adapts* this design direction. It *synthesizes* several structural ideas that already exist individually: machine-readable process specification (from declarative BPM), version-controlled configuration (from infrastructure-as-code), and hierarchical goal decomposition (from goal-modeling and the scorecard tradition). The *innovation*—the element none of the named traditions possesses—is the operationalization of the experience-layer acceptance contract as a machine-verifiable invariant of the whole specification: a typed justification graph on which completeness, acyclicity, waste, and executor-invariance are decidable and continuously re-checked, carrying a compression bound (Section 5). We state this delineation openly because the contribution is defensible as a graded advance—raising machine-checkable experience-linkage from a small fraction of parameters to near-complete coverage, and validation latency from periodic to continuous—not as a claim of unprecedented novelty.

### 2.8 The DO/WHAT structure and its kernel theories

The cascade encodes a distinction that predates its formalization: a separation between *what* a system is obligated to deliver and *how* internal coordination produces it. Levels 0 and 1—experience acceptance contracts and signal requirements—constitute the WHAT specification; Levels 3 through 5—procedures, inputs, and sourcing—constitute the DO specification; Level 2 (process contracts) is the interface. Mintzberg [-@mintzberg-1979-structuring-organizations-synthesis] distinguishes standardization of outputs from standardization of work processes as distinct coordination mechanisms, corresponding to the WHAT and DO layers. Iyer, Schwarz, and Zenios [-@iyer-2001-screening-contracts-product] show that product (WHAT) and process (HOW) specifications carry asymmetric verifiability in screening contracts: outcomes can be contracted on because they are observable; procedures often cannot, because the principal lacks inspection rights. Adler and Borys [-@adler-1996-two-types-bureaucracy] identify enabling bureaucracy—which formalizes best practices for achieving outcomes—as categorically different from coercive bureaucracy, which enforces procedural compliance irrespective of outcomes; OST's acceptance-test layer is structurally enabling, and its procedure layer becomes coercive only when severed from the WHAT layer above it. Simon's [-@simon-1962-architecture-complexity-proceedings] near-decomposability grounds the level decomposition itself: the cascade is a nearly-decomposable hierarchy in which within-level coupling is dense and between-level coupling passes only through typed traces.

A perception-measurement instrument can serve as the L0 language where stakeholder experience is the object of specification. Established, public multidimensional instruments already supply this form: SERVQUAL scores perceived service quality across five dimensions—tangibles, reliability, responsiveness, assurance, and empathy—each of which is expressible as a predicate over a stakeholder-experience score [@parasuraman-1985-parasuraman-valarie]. Spectral Brand Theory [@zharnikov-2026-spectral-brand-theory-computational-framework] is a second candidate, scoring delivered perception across eight dimensions; we use it illustratively in Section 7 and do not make the artifact depend on it. Any instrument that yields machine-checkable predicates over stakeholder experience—SERVQUAL, a scorecard customer measure, or a domain-specific scale—can occupy the same slot, so the L0 language is not tied to any single instrument.

## 3. Design-Science Method and Design-Theory Components

We follow the Design Science Research methodology of Hevner et al. [-@hevner-2004-design-science-information], situate the contribution within Gregor and Hevner's [-@gregor-hevner-2013-positioning] knowledge-contribution framework as an *exaptation*—extending an established solution (acceptance testing) to a new problem domain (organizational specification)—and structure the research through the elaborated DSR process model of Mullarkey and Hevner [-@mullarkey-2019-elaborated-adr]. We evaluate using the Framework for Evaluation in Design Science [FEDS; @venable-2016-feds].

Because a recurring critique of nascent-design-theory papers is that the design-theory components are left implicit, we state them explicitly, following the eight-component anatomy of a design theory [@gregor-2007-anatomy-design-theory] and stating each design principle in the aim-mechanism-rationale form of Gregor, Chandra Kruse, and Seidel [-@gregor-2020-anatomy-design-principle] rather than as an ad hoc list.

*Artifact.* The six-level specification cascade with executor-invariant contract layers and a continuous-validation pipeline.

*Design principles (DP1–DP6).* Prescriptive design knowledge, stated in Section 4.1.

*Mechanisms.* Four graph operations (Section 4.3) that make the principles machine-checkable.

*Kernel theories.* Mintzberg [-@mintzberg-1979-structuring-organizations-synthesis], Beer [-@beer-1979-the-heart-of], Beck [-@beck-2002-testdriven-development-by], Iyer, Schwarz, and Zenios [-@iyer-2001-screening-contracts-product], Adler and Borys [-@adler-1996-two-types-bureaucracy], Simon [-@simon-1962-architecture-complexity-proceedings], Kano, Seraku, Takahashi, and Tsuji [-@kano-1984-attractive-quality-must], and Kahneman and Tversky [-@kahneman-1979-prospect-theory-analysis], each with a stated role.

*Boundary conditions (C1–C6).* Scope conditions under which the artifact holds and fails, stated in Section 9.5.

*Knowledge contribution.* A technological rule—"to achieve testable, traceable, continuously validated organizational operations, specify experience-layer acceptance contracts and derive operations backward under machine-checked traceability"—advanced from concept to formalized artifact and mapped, per Gregor and Hevner [-@gregor-hevner-2013-positioning], to a nascent design theory.

## 4. The Artifact: A Specification Cascade

### 4.1 Design principles

- **DP1 (experience-first specification).** Specify stakeholder-experience outcomes as runnable acceptance tests (L0) before any process, resource, or executor is chosen. This operationalizes the service-dominant position that value is co-created in use and defined by the beneficiary [@vargo-2004-evolving-new-dominant]: the acceptance criterion is the stakeholder's experience, not a producer metric.
- **DP2 (traceability-as-invariant).** Require every operational parameter to carry a tool-verifiable directed trace to at least one L0 acceptance contract; a parameter with no such trace is flagged, by construction, as specification waste.
- **DP3 (executor-invariance).** Separate executor-invariant contract layers (L0–L2) from executor-dependent procedures (L3–L5). The contract layer carries executor-type metadata—human, automated, or AI agent—and remains stable across changes of who or what executes, so an executor swap changes procedures without changing acceptance criteria.
- **DP4 (continuous machine-checkable validation).** Re-validate the full justification graph automatically on every change, replacing periodic audit with a per-change structural invariant.
- **DP5 (forkability).** Represent a bounded responsibility center as a shareable L0–L2 test suite plus local L3–L5 procedures, so a unit can be transferred or replicated by sharing contracts without prescribing implementation. The contract/procedure boundary is a module interface in the sense of Baldwin and Clark [-@baldwin-2000-design-rules-power]: the L0–L2 test suite is the modular specification, the L3–L5 procedures the hidden implementation.
- **DP6 (reference-class-relative specification).** Set L0 scope—which stakeholder-experience dimensions carry an acceptance contract at all—and L0 threshold values relative to a reference class: the set of specifiers a stakeholder currently checks across competing options. Within an already-checked dimension, differentiation is value-relative—set the threshold against the reference class's observed distribution, echoing the reference-dependence Kahneman and Tversky [-@kahneman-1979-prospect-theory-analysis] document for judgment generally, not an independently-derived optimum. Outside it, differentiation is scope-relative—introduce a new L0 vertex the reference class does not yet carry, in the spirit of the attractive-quality category Kano and colleagues [-@kano-1984-attractive-quality-must] isolate. A scope-expansion vertex answers to DP2 like any other: an unverifiable new dimension is a claim, not a specification.

### 4.2 The six-level cascade

The artifact is a six-level specification cascade in which each level functions as the acceptance test for the level below it: designed top-down (from stakeholder experience to supply chain), operated bottom-up, and validated at every level by a continuous pipeline.

**Figure 1: The Six-Level Specification Cascade.**

```
        DESIGN DIRECTION (top-down)
                 |
  L0  Experience Contracts   ->  "Acceptance Tests"
                 |  satisfies_experience
  L1  Signal Requirements    ->  "Integration Tests"
                 |  satisfies_signal
  L2  Process Contracts      ->  "Unit Tests"
                 |  implements_contract
  L3  Procedures             ->  "Implementation"
                 |  requires_input
  L4  Input Specifications   ->  "Dependencies"
                 |  sourced_from
  L5  Sourcing Requirements  ->  "Infrastructure"
                 |
        OPERATE DIRECTION (bottom-up)
```

*Notes*: Each vertical bar is a typed traceability link (labelled with its edge type) validated on every change. The levels specify, top to bottom: L0 what stakeholders should perceive; L1 the signals that create that perception; L2 what processes must achieve; L3 how an executor achieves the contracts; L4 the materials, equipment, and training required; L5 the supply chain. Level 0 contains three contract types—experience contracts (perception), constraint contracts (what regulation mandates), and commitment contracts (what the organization has voluntarily committed to). A parameter with no upward path to any Level 0 contract is unjustified.

Levels 0–2 are executor-invariant specifications; Levels 3–5 contain executor-dependent implementation. This separation is architecturally significant: when an executor type changes, the contracts (tests) remain stable while only the procedures (implementation) change, exactly as refactoring changes software implementation without changing its tests.

### 4.3 Mechanisms

Four mechanisms make the design principles machine-checkable; Section 5 gives their formal basis.

- **M1 (trace traversal).** A directed traversal that decides, for each parameter, whether an upward path to an L0 contract exists (DP2).
- **M2 (schema and cross-reference integrity).** Structural checks that every referenced identifier resolves and every file conforms to its schema.
- **M3 (contract satisfaction).** Evaluation of each L2 quality gate as a predicate over measured or specified values (DP1, DP4).
- **M4 (waste detection).** A reverse-reachability pass from the L0 sinks that returns every unjustified parameter (DP2).

## 5. Formal Model

The design principles are made precise by treating an OST specification as a typed directed graph and stating the invariants as decidable graph properties. The model is deliberately minimal: it is the smallest structure sufficient to state completeness, waste, and cascade-compression. Full proofs of the compression bound live in companion formal papers (Zharnikov [-@zharnikov-2026-specification-impossibility-organizational-design-high; -@zharnikov-2026m-projection-cascade-why]); the operator-theoretic counterpart of the model appears in Zharnikov [-@zharnikov-2026-verification-as-operator-why-acceptance].

### 5.1 Intuition

Before the formal statements, the intuition. Picture the specification as a diagram of arrows in which every operational decision points upward to the stakeholder outcome it exists to serve. *Completeness* is the requirement that no chain of arrows dead-ends before it reaches an experience outcome—every parameter can answer the question "which stakeholder promise am I here for?". *Acyclicity* is the requirement that the chain never loops—nothing is justified by ultimately appealing to itself. A parameter from which no chain of arrows reaches any outcome is, by definition, unjustified: it is doing work no stakeholder asked for.

A four-vertex example makes this concrete. Let the graph contain one experience contract $e$ at L0 ("coffee served within three minutes"), one process contract $p$ at L2 ("extraction completes in 25–30 s") with an edge $p \to e$, one procedure $d$ at L3 ("tamp with 15 kg force") with an edge $d \to p$, and one further procedure $w$ at L3 ("engrave the barista's initials on the portafilter") with no outgoing edge. Reverse reachability from the L0 sink $e$ marks $\{e, p, d\}$ as justified: each reaches $e$ by following arrows. The remaining set $V \setminus R = \{w\}$ is the specification waste—engraving initials traces to no stakeholder outcome, so the pipeline flags it, not because it is forbidden but because nothing in the specification explains why it is there. Adding an edge from $w$ to some genuine outcome removes it from the waste set; that reversibility is the falsifiable content of the identification. The statements below generalize exactly this picture.

### 5.2 The justification graph

Let an OST specification be a directed graph $G = (V, E)$. Each vertex $v \in V$ is a contract carrying a level type $\ell(v) \in \{L0, L1, L2, L3, L4, L5\}$ and, for non-implementation vertices, a machine-checkable predicate $\pi(v)$; contract vertices additionally carry executor-type metadata. Each directed edge $(u, v) \in E$ is a *justifies* edge asserting that lower-level vertex $u$ exists to serve higher-level contract $v$; edges carry verifiability metadata. The graph satisfies two invariants:

- **Completeness.** Every non-L0 vertex has a directed path terminating at an L0 vertex. Equivalently, every vertex is *justified*: its existence is warranted by some experience-, constraint-, or commitment-level acceptance contract.
- **Acyclicity.** $G$ is a directed acyclic graph; no vertex justifies itself transitively.

Both invariants are decidable in time linear in $|V| + |E|$: completeness by a reverse reachability pass from the L0 vertices (the sinks of the justification relation), and acyclicity by topological sort. This is the formal content of DP2 and DP4: the pipeline of Section 4.3 recomputes both on every change.

### 5.3 Waste as unreachability

Let $R \subseteq V$ be the set of vertices from which a directed path reaches some L0 vertex. **Specification waste** is exactly $V \setminus R$. This gives Ohno's [-@ohno-1988-toyota-production-system] waste an ex-ante, structural definition at the specification layer—a parameter is wasteful if and only if it is unjustified—distinct from lagging-outcome waste measured after production. Mechanism M4 computes $V \setminus R$ by a single reverse-reachability pass, the organizational analog of dead-code elimination. The identification is falsifiable: a parameter with no upward trace that is nonetheless demonstrably required for an L0 outcome would refute it, indicating a missing edge rather than genuine waste.

### 5.4 Reference-class relativity

Waste as unreachability answers a question internal to one organization's graph: given a fixed vertex set, which vertices are unjustified? A second, external question is prior to it: which candidate L0 vertices are worth having in the graph at all, and at what threshold? DP6 answers it by making L0 scope and threshold selection relative to a reference class rather than an absolute optimum.

For a candidate L0 vertex $v$ at time $t$, define its reference class $\mathcal{R}(v, t)$ as the set of specifiers other than the focal organization who carry a vertex equivalent to $v$ in their own justification graph, intersected with the stakeholders who condition acceptance on $v$. Every candidate vertex falls into exactly one of three regimes with respect to $\mathcal{R}(v, t)$:

- **FLOOR.** $v$ is carried by approximately all of $\mathcal{R}(v, t)$ at a converged threshold. No differentiation is available; specifying $v$ is entry cost, not competitive advantage.
- **CONTESTED.** $v$ is carried by some of $\mathcal{R}(v, t)$ at varying thresholds. Differentiation is value-relative: the winning threshold is set against the reference class's observed distribution, not derived independently of it—the specification-layer analog of the reference-dependence Kahneman and Tversky [-@kahneman-1979-prospect-theory-analysis] document for judgment under risk.
- **UNCLAIMED.** $v$ is carried by none of $\mathcal{R}(v, t)$. Differentiation is scope-relative: specifying $v$ at all, provided $v$ meets DP2's machine-checkability requirement, is itself the competitive move.

This three-regime partition restates, in the justification graph's own vocabulary, the must-be/one-dimensional/attractive typology Kano and colleagues [-@kano-1984-attractive-quality-must] established empirically for quality attributes. It is the external-facing dual of waste as unreachability: that section asks whether a vertex reaches an L0 sink from below; this one asks whether an L0 vertex itself is already claimed by a reference class from outside. A vertex migrates UNCLAIMED → CONTESTED → FLOOR as members of $\mathcal{R}(v, t)$ imitate a successful scope-expansion; absent a change in what stakeholders condition acceptance on, migration runs one way. The partition presupposes an identifiable reference class (C6): in a genuinely first-of-kind category with no comparable specifier and no formed stakeholder query set, it is undefined until one forms.

A concrete case makes the UNCLAIMED regime legible. Consider a poultry producer whose reference class specifies no L0 vertex for feed composition or daily movement—chicken is bought and sold on price and appearance alone. A producer who begins publishing feed records and per-bird movement data, verifiable by a third party, adds a new L0 vertex outside every competitor's current scope: not a claim about taste or ethics, but a machine-checkable predicate a buyer can audit. Because it satisfies DP2, it is a specification, not marketing copy—the distinction Section 8.4 draws for the artifact generally applies here to a single vertex. As competitors adopt equivalent disclosure, the vertex migrates toward CONTESTED (whose feed formulation, whose movement threshold, is better) and eventually toward FLOOR (basic disclosure becomes assumed, as organic and free-range labeling did in adjacent categories). The differentiation available to the first mover is exactly the UNCLAIMED-regime advantage H4 predicts should decay with adoption—the elimination-by-aspects literature explains why the vertex was available to claim in the first place: buyers gate purchase decisions on a small active set of attributes [@tversky-1972-elimination-by-aspects], so a dimension outside that set is neither checked nor contested until someone puts it there.

### 5.5 Executor-invariance

Partition $V$ into the contract set $V_C = \{v : \ell(v) \in \{L0, L1, L2\}\}$ and the implementation set $V_I = \{v : \ell(v) \in \{L3, L4, L5\}\}$. An *executor swap* replaces the implementation subgraph induced by $V_I$ while leaving $V_C$ and the predicates $\pi$ on $V_C$ unchanged. DP3 is the requirement that acceptance is a function of $V_C$ alone: a swap changes how contracts are met, never which contracts must be met.

### 5.6 Cascade-compression is lossy under asymmetric verifiability

A natural efficiency question is whether adjacent levels can be collapsed—compressing the six-level cascade into fewer levels—without loss. The smallest sufficient model to answer it uses three levels ($L0$, $L2$, $L4$), two negotiating modules, a binary executor type $x \in \{\text{human}, \text{AI}\}$, and a single information-asymmetry parameter $\alpha \in [0, 1]$ measuring how much of a lower level is inspectable from the level above (following the asymmetric-verifiability setup of Iyer, Schwarz, and Zenios [-@iyer-2001-screening-contracts-product], where $\alpha = 1$ is full inspectability and $\alpha < 1$ is the generic case).

*Claim (compression sketch).* For $\alpha < 1$, no many-to-one mapping that collapses adjacent levels preserves both completeness (the justification invariant) and executor-invariance (DP3). *Sketch.* Collapsing $L2$ into $L0$ merges each process contract with the experience contract it justifies. The merged predicate must decide acceptance, so it must reference the executor-dependent content that distinguishes one procedure's satisfaction of the contract from another's; but under $\alpha < 1$ that content is not fully inspectable from the experience layer, so the merged predicate is either incomplete (it cannot decide acceptance for some executor) or it imports executor-dependent state into $V_C$, violating DP3. Either way an invariant is lost. The full result—that the effective specifiable dimensionality strictly decreases under compression, with a geometric bound on the loss—is proved for the high-dimensional case in Zharnikov [-@zharnikov-2026-specification-impossibility-organizational-design-high]; the projection apparatus that governs level-to-level compression is developed in Zharnikov [-@zharnikov-2026m-projection-cascade-why]. The operator-theoretic reading, in which a rank-1 audit projection discards all performance dimensions orthogonal to a single compliance axis while a full-rank cascade preserves the dimensional structure, is developed in Zharnikov [-@zharnikov-2026-verification-as-operator-why-acceptance].

The compression result is the formal core of the novelty claim: a checklist can be collapsed and re-expanded at will, but a cascade that maintains completeness and executor-invariance under $\alpha < 1$ cannot be, and that irreducibility is what distinguishes the artifact from documentation (a rival we address in Section 8.4).

### 5.7 Validation pipeline

Mechanisms M1–M4 compose into a per-change pipeline:

```
on every change to G:
  1. schema check      : every v conforms to its level schema           (M2)
  2. reference check   : every edge (u,v) resolves to existing vertices  (M2)
  3. contract check    : for every L2 vertex v, evaluate predicate pi(v) (M3)
  4. coverage check    : every L1/L2 vertex lies on a path to some L0    (M1)
  5. waste check       : report V \ R  (unjustified vertices)            (M4)
  fail the change if any of 1-4 reports an error; surface 5 as a warning
```

Steps 1–2 are structural, 3 is semantic, and 4–5 are the traceability invariants; all run in time linear in the specification size, so the pipeline is practical to run on every commit.

## 6. Propositions as a Forward Research Agenda

The design-science contribution is the artifact and its analytical evaluation. The following propositions are stated as *testable hypotheses for future research*, not as validated outcomes; the paper reports no data bearing on them, and none should be read as a causal or performance claim. Stating them separates the conceptual and formal register of Sections 4–5 from the empirical register here.

**H1 (traceability and diagnostic latency).** Operations specified with backward traceability will identify the operational parameter responsible for an experience failure faster than operations without it, because the justification graph makes the causal chain traversable. *Lead falsification test*: across at least three independent deployments below the minimum-specifiability threshold (C1), if more than a quarter of parameters cannot maintain machine-verifiable upward traces without manual override on more than a tenth of changes, then DP2 and DP4 jointly fail.

**H2 (continuous validation and drift).** Organizations using per-change validation will exhibit less accumulated structural non-conformance between periodic audits than organizations relying on periodic manual validation. This is testable by longitudinal comparison of non-conformances discovered at audit.

**H3 (test-suite transfer and information asymmetry).** Sharing a bounded responsibility center as a test suite (DP5) will transfer operational capability with lower information asymmetry than prescriptive procedure manuals in multi-site and franchise settings, where principal-agent asymmetry is well documented [@rubin-1978-theory-firm-franchise; @lafontaine-1992-agency-theory-franchising]. This requires controlled comparison.

**H4 (scope-differentiation decay).** The differentiation utility an organization captures from an UNCLAIMED L0 vertex (Section 5.4) will decay as reference-class adoption moves the vertex toward CONTESTED and then FLOOR. *Lead falsification test*: track the stakeholder-preference share attributable to vertex $v$ before and after at least two reference-class members adopt an equivalent vertex; share attributable to $v$ should fall as adoption count rises, holding $v$'s own threshold constant.

## 7. Illustrative Walkthrough

To make the cascade concrete we walk through a purpose-built specification for a fictional specialty-coffee operation. This is an *illustration of the artifact's structure*, not evaluation evidence; no claim about outcomes rests on it, and the fictional status is stated so the walkthrough is not mistaken for a case study.

A Level 2 process contract is a set of measurable quality gates with upward traces:

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

Each quality gate is a predicate $\pi(v)$; the `satisfies_signal` and `satisfies_experience` fields are the outgoing justifies-edges. A change to any gate triggers the pipeline, which verifies that the change does not break the satisfaction chain above it. Compliance content participates in the same cascade: an allergen matrix and a hazard analysis trace upward through constraint contracts at L0, so regulatory requirements are justified parameters rather than parallel documentation.

### 7.1 Executor swap (illustrative)

To show the cascade's diagnostic character, consider an executor swap from human artisan to fully automated preparation, with *illustrative* values that are not measurements.

**Table 2: Executor-Swap Impact (Illustrative).**

| Cascade level | Human artisan | Fully automated | Delta |
|:---|:---|:---|:---|
| L2 process contracts (unit tests) | all pass | all pass | no change |
| L1 signal requirements (integration tests) | 18/18 satisfied | 15/18 satisfied | −3 signals |
| L0 experience contracts (acceptance tests) | all pass | 2 fail | "personal rapport", "craft as performance" |

*Notes*: Values are illustrative, not empirical measurements; they demonstrate the diagnostic structure, not a magnitude. All L2 contracts pass—the machine meets tolerances—yet the cascade exposes signal and experience degradation invisible to process-level metrics. Executor choice is thereby shown to be a design decision with experience consequences, made visible by the cascade rather than asserted.

### 7.2 ISO 9001 comparison (illustrative and asymmetric)

We translate one espresso-preparation process from ISO 9001 clause-compliant documentation into the cascade and note what each format captures. This comparison is *illustrative and deliberately asymmetric*: it contrasts a fully-specified cascade with a conventional documentation format, and it establishes what the cascade makes explicit, not that the cascade is superior on any outcome. ISO 9001 does not prohibit automated traceability or continuous validation; it does not require them. The structural point is only that OST mandates these as invariants: in the cascade, the `extraction_time_s` gate traces through `craft_preparation_visible` to `taste_balanced_sweet_clean`, so changing the tolerance is visibly an experience change; cross-references are machine-readable identifiers checked on every commit rather than text references checked at the next audit; and the reverse-reachability pass reports unjustified parameters that conventional documentation provides no mechanism to distinguish from justified maintenance.

## 8. Evaluation

Following the FEDS framework [@venable-2016-feds], we evaluate the artifact through three strands: an analytical argument (primary), independent naturalistic corroboration, and a public demonstration. We make no causal or KPI-superiority claim: we do not claim that OST deployments outperform ISO 9001, TOGAF, or any other practice on any measured outcome. The evaluation establishes that the artifact has the properties it is designed to have and that an independent organization converged on the same design logic—not that it improves performance.

### 8.1 Analytical evaluation (primary)

The systematic comparison of Section 2 (Table 1) is the primary evaluation. Against the four-property axis, OST is the only artifact for which ex-ante, experience-layer, machine-checkable, and backward-traceable hold jointly, and Section 5 shows why the joint property is irreducible under asymmetric verifiability. Restated as a graded claim: the artifact raises machine-checkable experience-linkage from the small fraction of parameters that adjacent traditions link to an experience criterion toward near-complete coverage, and reduces validation latency from the periodic cadence of audit to continuous per-change checking. Both are analytical consequences of the design principles and the formal model, independent of any deployment.

### 8.2 Naturalistic corroboration: two independent industry cases

Two independent, publicly-documented firms exhibit structures that instantiate the artifact's design principles, each arrived at from operating practice rather than from this theory. We frame both as ex-post naturalistic corroboration of the design logic—evidence that the logic is not idiosyncratic to this paper—carrying no causal or performance claim.

The first corroborates continuous validation and the WHAT/DO separation. Block, Inc. [-@dorsey-botha-2026-hierarchy-intelligence] articulated a "world model" architecture that replaces hierarchical coordination with an AI-maintained organizational specification—a customer-facing specification, a machine-maintained company context, and time-bounded ownership rotations in place of permanent middle management. The architecture is structurally equivalent to the cascade's WHAT/DO separation (DP3) and continuous validation (DP4).

The second corroborates experience-first specification (DP1) through a firm at a different scale and era, which matters because it shows the design logic is not an artifact of the recent AI moment. Amazon's "working backwards" process requires a team to write an internal press release and a frequently-asked-questions document—describing the customer experience of a product as it would be announced—and to review and approve that artifact before any implementation begins [@bryar-carr-2021-working-backwards]. The press-release-and-FAQ is, structurally, an L0 experience acceptance contract authored before the operational stack: the desired stakeholder experience is specified and gated first, and the build is derived to satisfy it. That an independent firm institutionalized experience-first acceptance as a mandatory gate, decades before the cascade was formalized, is naturalistic evidence for DP1 specifically. The two cases corroborate different design principles from different firms, which is stronger than a single instance.

The wider industry signal is consistent with both: organizations reporting significant enterprise-wide AI impact are 2.8 times as likely to have fundamentally redesigned their workflows rather than layering AI tools on existing processes [@singla-2025-state-of-ai].

### 8.3 Demonstration: a public specification corpus (proof-of-concept)

The third strand is the weakest of the three and is offered only as proof-of-concept that the validation pipeline is implementable on real artifacts; it is subordinate to the two independent naturalistic cases above and carries no corroborative weight beyond feasibility. It requires no private data: the author's multi-month research corpus is itself an auditable instance of OST. Its specifications are maintained as dependency graphs; acceptance-test-style bundle gates check, on every change, that each artifact's claims trace to its specification and that cross-references resolve; tooling is executor-invariant in the sense of DP3 (the checks run identically regardless of who edits); and backward traceability is version-controlled. This shows that the per-change pipeline of Section 5 runs on a live specification—not that it improves any outcome. Because the corpus is authored by the same hand that states the theory, its self-referentiality (stated plainly as a limitation in Section 9.6) bars it from bearing evidential weight; the naturalistic cases, not this demonstration, carry the corroborative load.

### 8.4 Boundary objects

A design theory earns its keep by explaining phenomena that rival accounts leave anomalous. The artifact explains four. First, persistent strategy-execution gaps in digital transformations despite mature enterprise-architecture and BPM tooling: OST attributes them to missing experience-layer acceptance contracts and the absence of continuous trace validation—precisely the two properties Table 1 shows those tools lack. Second, the differential coordination success of "working-backwards" cultures relative to traditional matrix organizations: OST predicts it from executor-invariance and forkability (DP3, DP5), which let a specification survive reorganization. Third, the outcome-coherent forking of certain open-source organizational forms, which reproduce without a prescriptive manual: OST reads them as sharing a test suite rather than an implementation. Fourth, why a publicly auditable process disclosure shifts stakeholder preference where an unverifiable claim of identical content does not: OST reads the difference as whether the disclosed content is a genuine, DP2-compliant L0 vertex or an assertion outside the graph (DP6, Section 5.4). Conformance checking, balanced scorecards, and cybernetic control leave all four under-explained.

## 9. Discussion

### 9.1 The DO/WHAT bridge and measurement

The cascade's WHAT layer (L0–L1) specifies delivered experience; a measurement instrument scores it. Where Spectral Brand Theory [@zharnikov-2026-spectral-brand-theory-computational-framework] or an equivalent instrument is used, an L0 acceptance contract specifying, say, "warm, competent, unhurried" is satisfied or failed according to the dimensional profile that observer cohorts actually form, closing a specify-forward / measure-against-ground-truth loop without human inspection of individual results. The empirical anchoring is stronger in AI-mediated channels, where evidence suggests such channels are not neutral conduits but selectively compress some experience dimensions while preserving others [@zharnikov-2026-dimensional-collapse-ai-mediated-search], reinforcing the priority of specifying the WHAT layer explicitly for any organization operating in AI-augmented markets.

### 9.2 Nesting within a coarser transferability ontology

The cascade specifies an organization's internal layers at high resolution. A coarser six-tier ontology of the firm—owner intent, business model, business entity, product, process, organization—has been developed to address transferability in mergers and acquisitions [@zharnikov-2026-dual-hierarchies-organizational-transferability-six]. The OST cascade nests inside the lower tiers of that ontology: product corresponds to L0–L1, process to L2 and upper L3, and organization to lower L3 and L4–L5. The two hierarchies are not isomorphic: OST's L0 is the customer-facing apex (read top-down from experience to sourcing), whereas the six-tier ontology's deepest stratum is owner intent (read from the inside out). They share a count, not a reading direction or rung semantics; a formal mapping between the two, via the projection apparatus of Zharnikov [-@zharnikov-2026m-projection-cascade-why], is left to future work. The empirical case for specifying the WHAT layer is strengthened outside the OST literature: intangible assets now constitute roughly nine-tenths of large-firm market value, most of it internally generated and absent from the balance sheet [@peters-2017-intangible-capital-investmentq], so most operating value sits in dimensions financial reporting cannot extract; and across a case survey of acquisitions, organizational integration—not strategic fit—was the dominant factor in synergy realization [@larsson-1999-integrating-strategic-organizational], which OST reframes as cascade compatibility: when the L0–L1 specifications of acquirer and target are commensurable, integration is mechanical.

### 9.3 Cybernetic grounding

The cascade maps onto Beer's [-@beer-1979-the-heart-of] Viable System Model: operations (S1) to Levels 3–5, coordination (S2) to the cross-reference structure, operational management (S3) to Level 2 contracts, intelligence (S4) to Level 1 signals, and identity (S5) to Level 0 contracts. The theoretically significant mapping is the audit channel S3\*, which Beer described as sporadic and direct; OST realizes it as a continuous, automated, comprehensive check on every change, and adds the upward traceability from S1 to S5 that the VSM leaves implicit. We recast this in the language of continuous validation rather than cybernetic pathology, because the operational content—per-change checking of the justification graph—is what the artifact contributes.

### 9.4 Practical implications

For information-systems practitioners, the artifact suggests treating organizational specification as version-controlled, machine-checkable code: schema-first specifications, a CI/CD-style validation pipeline, and traceability that AI agents can consume directly. For operations managers, the cascade is a diagnostic instrument—traverse downward from a failing acceptance test to localize the responsible parameter. For multi-site and franchise operations, DP5 suggests sharing a test suite and verifying compliance through automated results rather than prescribing a manual. DP6 gives a decision rule for what to specify at all: classify a candidate L0 vertex as FLOOR, CONTESTED, or UNCLAIMED in the organization's reference class before allocating specification effort to it, rather than specifying every dimension an absolute standard could in principle support. The industry-convergence evidence indicates that the redesign this implies is where enterprise-wide AI impact concentrates [@singla-2025-state-of-ai].

### 9.5 Boundary conditions

- **C1 (minimum-specifiability threshold).** The artifact yields positive returns only where enough operational knowledge is articulable; below the threshold, trace-maintenance cost dominates. An observable signature is trace-maintenance effort exceeding a material fraction of operating effort.
- **C2 (high-tacit domains).** In fine dining, therapy, or coaching, where how something is done is inseparable from what is achieved, the executor-invariant boundary (DP3) weakens.
- **C3 (bootstrap).** Specifying L0 before an organization operates requires hypothesizing and refining acceptance tests, analogous to characterization testing of legacy systems [@feathers-2004-working-effectively-with].
- **C4 (preference drift).** The cascade rests on L0 tests remaining valid as preferences evolve; a renewal protocol governing L0 revision frequency and triggers is required and not yet formalized.
- **C5 (political economy).** Making constraints explicit reduces the ambiguity actors exploit as a discretionary resource [@crozier-1977-lacteur-et-le]; the artifact transforms rather than removes political dynamics, and can be resisted as any formalization is.
- **C6 (reference-class identifiability).** DP6 and the three-regime partition of Section 5.4 presuppose an identifiable reference class—a set of comparable specifiers and a stakeholder population that conditions acceptance on some dimension set. In a genuinely first-of-kind category with no comparable specifier and no formed stakeholder query set, FLOOR/CONTESTED/UNCLAIMED is undefined until a reference class forms; the artifact supplies no rule for when that formation happens.

These conditions also dissolve an apparent counterexample—that the most effective teams often operate with little documentation. Below C1's threshold, low-specification operation is rational; the artifact targets settings above it.

### 9.6 Limitations

First, no controlled outcome evidence: the evaluation is analytical, naturalistic-observational, and demonstration, and no causal claim is made. Second, two of the three evaluation strands—the demonstration corpus and the analytically-argued primary evaluation—are authored by the same hand; the independent naturalistic strand partly offsets this, but the evaluation is formative, not summative. Third, the embedded formal model is the smallest sufficient model, and the compression result is a proof sketch whose full proof is deferred to companion papers. Fourth, the empirical hypotheses (H1–H4) are a forward agenda and are not tested here.

## 10. Conclusion

Organizational design does not lack quality mechanisms; it lacks one specific property—a machine-checkable, ex-ante acceptance contract at the experience layer with backward traceability, maintained as a structural invariant of the specification. Organizational Schema Theory supplies that property through a six-level specification cascade, stated as six design principles and formalized as a typed justification graph on which completeness, waste, executor-invariance, cascade-compression, and reference-class relativity are decidable or falsifiable. The artifact is evaluated honestly—analytically, through independent industry convergence, and through a public demonstration corpus—with no outcome claim, and what is new in it is separated from what it adapts and synthesizes. The contribution is nascent design theory: acceptance testing operationalized as a tool-checkable invariant of organizational specification, with a research agenda that invites the controlled evaluation this paper deliberately does not claim.

## Acknowledgments

Generative AI tools (Claude Opus 4.8, Anthropic; Grok 4.20 and Grok 4.3, xAI; Gemini 2.5 Pro, Google) were used as research instruments for literature search, citation verification, and editorial refinement, and a large language model provided pre-draft and post-draft critical reviews of the paper's concept and manuscript. All theoretical framework construction, the formal model, analytical conclusions, and manuscript text are the author's own work. No generative tool authored the design theory or its evaluation.

## Author Contributions (CRediT)

Dmitry Zharnikov: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Project administration, Software, Validation, Writing — original draft, Writing — review and editing.

## Disclosure of Interest

The author declares no competing interests with respect to the research, authorship, and publication of this article.

## Funding

No funding was received for this research.

## Data and Code Availability

The demonstration specification corpus and the validation tooling referenced in Section 8.3 are publicly inspectable. The concept DOI for this work is [10.5281/zenodo.18946043](https://doi.org/10.5281/zenodo.18946043); this version (v2.1.0) is archived at [10.5281/zenodo.21623169](https://doi.org/10.5281/zenodo.21623169).

## References

::: {#refs}
:::
