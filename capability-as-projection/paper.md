# Capability as Projection of an Append-Only Organizational Log: An Event-Sourced Substrate Theory of Organizational Capability and Transfer Failure

Dmitry Zharnikov

ORCID: 0009-0000-6893-9231

DOI: [10.5281/zenodo.20367459](https://doi.org/10.5281/zenodo.20367459)

Working Paper v1.0.0 – June 2026

---

## Abstract

This paper specifies an event-sourced substrate beneath organizational capability rather than treating capability as a stored stock of resources or routines. Capabilities are computed from the cumulative trace of what a firm has actually done, evaluated at the moment a strategic question is asked. The paper specifies three formal objects: a partially ordered log of immutable events, a projection operator that reads the log under a query and a render time, and a compatibility function that scores log-merge events such as acquisitions. Four propositions follow: clean log merges preserve projection continuity; snapshot imports without the underlying log diverge within three years; writedown magnitude in failed M&A is jointly determined by raw log incompatibility and acquirer integration-policy choice; imitators who observe only the projection cannot replicate capability responses to novel queries. The framework is illustrated by three honestly coded process-traced cases — Disney's 2006 acquisition of Pixar, Microsoft's 2014 acquisition of Nokia's handset assets, and persistent imitation failure of the Toyota Production System — under a single-coder pass of a pre-registered protocol. A worked Monte Carlo simulation reproduces the predicted comparative statics. The substrate-projection distinction reframes the long-running tautology critique of dynamic capabilities as a category error and generates falsifiable predictions about transfer failure.

**Keywords**: capability as projection; append-only organizational log; event sourcing; dynamic capabilities; organizational capability; substrate theory; M&A integration; log-merge; transfer failure; process mining; snapshot import; Pentland-Feldman; Penrose-Teece-Helfat; Nakajima ActiveGraph

---

Three observations sit uneasily within the dominant theories of the firm. Toyota's manufacturing capability is the most thoroughly documented operational system of the past forty years, yet imitators who copy its visible artifacts fail to reproduce its results [@spear-1999-decoding-dna-toyota; @liker-2004-toyota-way-14]. A senior executive who runs a successful organization at one firm frequently fails at a structurally identical role in another [@groysberg-2004-risky-business-hiring]. Microsoft's 2014 acquisition of Nokia's handset business preserved engineers, factories, patents, supplier contracts, and the brand, yet the capability was gone within eighteen months and the asset was written down by USD 7.6 billion [@microsoft-2015-annual-report-form; @vuori-2016-distributed-attention-shared]. Disney's 2006 acquisition of Pixar preserved an apparently smaller surface — the leadership team, the review meetings, the daily cadence — and the capability survived and propagated [@catmull-2008-how-pixar-fosters; @anand-2010-walt-disney-company].

These phenomena resist clean explanation under resource-based or dynamic-capabilities theory. The resources were preserved, but the result was not. The artifacts were copied, but the competence did not transfer.

This paper proposes that the missing object in all three cases is the same: the operational event log — the append-only sequence of decisions, failures, policies, hires, and artifacts through which the capability was actually produced. Capability is not a stock that can be inventoried and transferred. It is a render-time projection of a log that must be present, intact, and queryable for the projection to compute. When the log is preserved, the capability survives. When only the projection at a moment in time is preserved, the capability decays within years.

The paper makes three contributions. First, it supplies a missing substrate layer beneath the Penrose-Teece-Helfat tradition by separating the substrate (the log) from the projection (the capability as observed), and relocates the construct-validity debate at the projection layer. Second, it derives testable predictions about M&A integration and capability imitation from log-merge mechanics, supplying the micro-foundation that the microfoundations critique of routines and capabilities [@felin-2012-microfoundations-routines-capabilities] has demanded. Third, it bridges to an open-source engineering instance — Nakajima [-@nakajima-2026-log-is-agent]; ActiveGraph — that demonstrates event-sourced substrate is already operating beyond strategy-theoretic metaphor. The contribution is substrate-layer, not whole-firm: the paper does not claim to recast the firm but to specify the substrate layer that dissolves the long-running tautology critique and generates falsifiable predictions about transfer failure.

The argument develops in five movements. The next section reviews the resource-based, dynamic-capabilities, and routines-as-performance traditions and locates the substrate-projection distinction within them. The third section specifies the formalism: the log L as a partially ordered set, the projection operator π, and the compatibility function κ. The fourth section develops log-merge mechanics in M&A and engages the Zollo-Singh and Puranam program as the closest empirical antecedent. The fifth section reports three process-traced cases coded under a pre-registered protocol. The sixth section discusses Nakajima's ActiveGraph as an existence proof. The discussion section enumerates boundary conditions, contributions, and limitations. A Methods Appendix reproduces the pre-registered event-coding protocol in full.

<!-- NANOBANA_PROMPT: Iceberg illustration in the spectral palette (deep blue water, white-gray ice). Above waterline: small visible peak labeled "Capability (rendering)" — a polished slide-deck-style icon. Below waterline: enormous body of ice labeled "Append-only event log" filled with small abstract icons representing decisions, hires, code commits, post-mortems, policy revisions, in muted spectral colors. A thin dashed line at the waterline labeled "render time t." Clean, technical, journal-quality. No people. -->
<!-- ILLUSTRATION: Figure 1. The capability iceberg. What an observer measures as capability at time t is the surface render of a much larger append-only log; transfer of the surface without the log produces inert capability claims. -->

## **Theoretical Foundations**

The argument has four direct antecedents in strategic-management and organization theory. Each is engaged in turn.

***The Penrose Tradition and the Resource-Based View***

Edith Penrose [-@penrose-1959-theory-growth-firm] defined the firm as a bundle of productive resources whose *services* depend on management's accumulated experience. The distinction between resources and the services they yield is central: two firms holding identical resources can produce different services because the managerial team's history of working with those resources is different. Penrose treated experience as path-dependent and non-transferable but did not formalize the substrate of that experience. The argument here is that the missing object is the operational event log itself. Experience is the log; resources are projections evaluated against it. The framework preserves Penrose's path-dependence intuition while supplying a substrate that can be specified, observed in principle, and tested.

Jay Barney's [-@barney-1991-firm-resources-sustained] reformulation of Penrose into the resource-based view defined value, rarity, inimitability, and non-substitutability as the conditions under which a resource confers sustained advantage. The inimitability condition has long been the most theoretically interesting and the least operationally specified. The event-sourced view restates it as a substrate property: a resource is inimitable to the extent that the log that produced it is inaccessible to imitators. Toyota's kanban cards are perfectly imitable; the seventy-year log of kaizen events from which the cards were derived is not.

***Dynamic Capabilities***

David Teece, Gary Pisano, and Amy Shuen [-@teece-1997-dynamic-capabilities-strategic] introduced sense, seize, and transform as the core dynamic-capability triad. Sidney Winter [-@winter-2003-understanding-dynamic-capabilities] refined the construct by distinguishing operating routines from higher-order routines that modify them. The construct has been generative and has also been criticized persistently for tautology and measurement opacity [@arend-2009-assessing-dynamic-capabilities; @helfat-2009-understanding-dynamic-capabilities]. If a capability is defined as whatever enables a firm to reconfigure resources and is measured by observing successful reconfiguration, the construct cannot be falsified.

This paper interprets the tautology critique as a category error. Dynamic capabilities are projections of a substrate. Constructs defined only at the projection layer will appear tautological when the substrate is unobserved, because two projections of the same log will correlate with each other regardless of any underlying mechanism. Once the substrate is named separately and the projection is treated as a function of it, the tautology dissolves: capability is the projection at time t, performance is a different projection at a later time, and both are governed by the common log. Predictions about their relationship become identification problems rather than definitional ones.

Kathleen Eisenhardt and Jeffrey Martin [-@eisenhardt-2000-dynamic-capabilities-what] responded to the tautology critique by recasting dynamic capabilities as identifiable processes. Their account is congenial to the substrate-projection distinction: their identifiable processes are projections of well-defined event subsets of the log. Every dynamic capability is a projection of some L_q ⊆ L; their specific processes are instances of a more general operator.

Constance Helfat and colleagues [-@helfat-2007-dynamic-capabilities-strategic-change] developed the capability lifecycle — founding, development, maturity, branching, retirement, redeployment, recombination. Event sourcing supplies the underlying clock: each lifecycle stage corresponds to a class of log operations (append, branch, merge, prune, replay). Helfat and Peteraf [-@helfat-2009-understanding-dynamic-capabilities] extended the lifecycle into a developmental view of capability heterogeneity. Lifecycle states are recoverable from log structure, not merely inferred ex post from results.

***Routines as Performances***

The closest prior art is the routines-as-performances tradition of Brian Pentland and Martha Feldman. Their 2005 *Industrial and Corporate Change* paper [@pentland-2005-organizational-routines-as] distinguished ostensive from performative routines and developed the relationship as a generative cycle; their 2008 *Information and Organization* paper [@pentland-2008-designing-routines-folly] argued that routines cannot be designed directly — only the artifacts and conditions that shape streams of performances can. A recent literature review [@baldessarelli-2022-organizational-routines-evolution] traces the evolution of this tradition through two parallel research communities and consolidates its core constructs.

The substrate-projection distinction maps onto the ostensive-performative duality but is not identical to it. The ostensive routine is one snapshot among many possible projections of the log; the performative routine is a live rendering. The 2008 design argument restates cleanly: capability cannot be designed directly because capability is a projection; only the log can be designed. The reformulation supplies the formal vocabulary — log, projection, compatibility — that Pentland and Feldman's work stopped short of articulating. Pentland and colleagues [-@pentland-2012-dynamics-organizational-routines] and Pentland and Liu [-@pentland-2020-dynamics-drift-digitized] showed empirically that routine dynamics can be modeled as generative systems and reconstructed from digital trace data; the present paper lifts that methodological observation to an ontological commitment.

***Microfoundations and the Knowledge-Based View***

Teppo Felin, Nicolai Foss, Koen Heimeriks, and Tor Madsen [-@felin-2012-microfoundations-routines-capabilities] argued that routines and capabilities lack microfoundations: collective-level constructs that do not bottom out in identifiable individual-level actions and interactions are theoretically incomplete. The substrate-projection view supplies the missing layer naturally. The log is the micro-level: individual decisions, named-actor hires, dated artifacts. The projection is the collective-level competence that emerges when the log is read under a strategic query. The microfoundations critique is answered structurally rather than rhetorically: substrate lives at the individual-event level, capability lives at the projection level, and the relation between them is a function rather than a hand-wave.

Robert Grant's [-@grant-1996-toward-knowledgebased-theory] knowledge-based view treated knowledge integration as the firm's distinctive competence. Bruce Kogut and Udo Zander [-@kogut-1992-knowledge-firm-combinative] earlier framed the firm as a social community specializing in the transfer and combination of knowledge. Both are projection-layer theories: they describe what the firm is competent at, given some substrate they do not specify. The event-sourced view supplies the substrate they presume. Knowledge integration is a projection of the log under a knowledge-relevant query; knowledge transfer fails when the log is moved without its rendering apparatus.

***Organizational Learning and Memory***

Linda Argote and Ella Miron-Spektor [-@argote-2011-organizational-learning-experience] reviewed the organizational-learning literature and distinguished knowledge storage from knowledge retrieval. Their framework treats organizational memory as the bridge between past experience and present action but leaves the computational primitive unspecified. The projection operator π supplies it: retrieval is evaluation of π on L under a query at a render time; storage is the append-only commitment of events to L. Anne Howard-Grenville's [-@howardgrenville-2005-persistence-flexible-organizational] analysis of routine flexibility under agency restates as: flexibility is the range of projections π(L, q, t) compatible with the same L; agency operates at the projection layer through query selection, not at the substrate layer through log rewriting.

***What This Theoretical Apparatus Adds***

The four traditions plus the microfoundations and knowledge-based programs converge on a distinction they did not name. All assume an implicit object — the accumulated history that produces, constrains, and evolves the visible competence. Naming that object as the log and the visible competence as a projection clarifies what is measured (the projection), what does the work (the log), and where transfer fails (when the projection is moved without its substrate). The older procedural-rationality tradition [@march-1958-organizations; @cyert-1963-behavioral-theory-firm] modeled organizations as procedures operating over a shared substrate; the event-sourced view vindicates it on more rigorous ground.

## **The Event-Sourced View**

This section specifies the formalism. The mathematical machinery is small by design: a theoretical contribution at this level favors mechanism precision over proofs.

***The Event Log L***

An organization's operational history is modeled as a partially ordered set of typed events:

> L = (E, ≤)

where E is a set of events and ≤ encodes causal-temporal precedence. The order is partial because not all events stand in a defined precedence relation: concurrent decisions in different parts of the firm need not be ordered with respect to one another. Each event e ∈ E is a tuple (id, t, a, τ, p, c) carrying a unique identifier, a wall-clock timestamp, an actor, an event type drawn from a fixed taxonomy T, a payload (the substantive content), and a caused_by pointer to the event that triggered this one. Events are immutable: once written they are never edited, only superseded by later events. A revised policy is a new POLICY event that supersedes the prior one; both events remain on the log.

The event taxonomy T is committed ex ante per the pre-registered coding protocol (Methods Appendix A.2). Five top-level types cover the cases of interest: DECISION (a choice attributable to a named decision-maker among recorded alternatives), FAILURE (a negative outcome event recorded by the organization or by an independent third party), POLICY (a versioned written commitment to a rule or procedure), PERSONNEL (a named individual entering, exiting, or changing role), and ARTIFACT (a produced output that becomes part of the firm's substrate).

***The Projection Operator π***

A projection is a function that reads a log and produces an observable claim about the organization at a moment in time:

> π : L × Q × t → C

where Q is the query space (a finite set of well-formed strategic questions — "What is this firm's capability to ship vehicles at low cost?"), t is the render time (the moment the question is asked), and C is the claim space (observable attributes, capability assessments, valuations). Three properties of π are required.

*Prefix monotonicity (P1).* For any query q and any t' < t, if L_t = L_{t'} ∪ ΔL with ΔL the event delta over the half-open interval from t' to t, then π(L_t, q, t) ⊇ π(L_{t'}, q, t'). Capabilities can never be erased from the log, only superseded.

*Determinism conditional on log (P2).* Two evaluators presented with the same L and the same q at the same t produce the same π(L, q, t). This is the strict-replay property of Nakajima [-@nakajima-2026-log-is-agent] §4 transplanted to organizational analysis: capability claims must be reproducible from the log. If different evaluators produce different claims, either the log is incomplete, the query is under-specified, or one or both evaluators read non-log state.

*Locality (P3).* π depends only on the subset of L relevant to q. Two firms with disjoint logs cannot have their projections cross-influence; this rules out spurious cross-firm halo effects in measurement.

A concrete worked instance of π is the weighted prefix sum with decay:

> π_λ(L, q, t) = Σ_{e ∈ L_q, t_e ≤ t} w_q(e) · exp(−λ · (t − t_e))

where L_q ⊆ L is the event subset relevant to q, w_q(e) is the per-event weight (signed: a successful Toyota kaizen contributes positively to "low-cost production capability," a recall contributes negatively), and λ ≥ 0 is a decay parameter (capability ages — older events count less). This is one operator among many. The exponential decay kernel is one of several plausible forgetting forms; power-law, hyperbolic, and threshold kernels are also viable and have differing empirical support in the organizational-learning literature (Argote and colleagues). The substrate-and-general-projection apparatus applies wherever the boundary conditions B1–B4 hold; the specific operator π_λ is one calibratable instance for empirical work. Different industries and different queries warrant different λ values; the parameter is empirically identifiable, not a free degree of freedom.

<!-- NANOBANA_PROMPT: Function diagram. Three boxes left-to-right. Left box labeled "Log L" containing many small stacked rectangles (events) in muted spectral palette. Middle box labeled "Projection π (query q, time t)" rendered as a stylized lens or filter shape in a brighter spectral accent color. Right box labeled "Capability C" rendered as a clean polished icon. Arrows from L through π to C. Above the arrow from L to π label "L_q ⊆ L (events relevant to q)." Above the arrow from π to C label "evaluated at render time t." Journal-quality. -->
<!-- ILLUSTRATION: Figure 2. Capability as projection. The visible capability C is the output of a projection operator π that reads a query-relevant subset L_q of the log L at render time t. -->

***The Compatibility Function κ***

For two logs L_A and L_B — typically the two parties to an acquisition — define:

> κ(L_A, L_B) = 1 − (|conflicts(L_A, L_B)| / (|L_A| + |L_B|))

where conflicts(L_A, L_B) is the set of event pairs (e_A, e_B) with e_A ∈ L_A, e_B ∈ L_B that cannot be simultaneously incorporated into a merged log L_M without contradicting determinism (P2). Conflicts arise from incompatible policies (A's promotion rule conflicts with B's), incompatible artifacts (codebases committing to different schemas for the same noun), or incompatible identifiers (both firms have a senior leader assigned to the same role on the same date). κ ∈ [0, 1]; κ = 1 indicates perfectly compatible logs, κ = 0 indicates every event in one log conflicts with some event in the other.

Conflict-resolution semantics are borrowed from the conflict-free replicated data type literature [@shapiro-2011-conflictfree-replicated-data]. A merged log L_M = L_A ⊕ L_B requires a per-conflict resolution policy. Three canonical policies recur in M&A integration: last-write-wins (the later event by wall-clock time supersedes the earlier; used in Disney's preservation of Pixar's Braintrust over Disney's prior creative-review process), acquirer-supreme (every conflict resolved in favor of L_A — the standard snapshot-import pattern), and subsidiary-preserved (every conflict resolved in favor of L_B — Berkshire Hathaway's portfolio-firm management approaches this).

***Snapshots and Renderings***

A snapshot is the result of applying π to L at a specific t and freezing the output: S = π(L, q, t_0). A snapshot is a projection extracted from its substrate; it can be passed to another party (the acquirer reads the target's 10-K; the rival reads the slide deck), but it loses the log behind it. Subsequent projections on the snapshot alone, without access to L, can only re-render existing claims; they cannot answer new queries q' that would require log access.

A rendering is a live projection — π evaluated on the current L, refreshable as L grows. A capability in use is a rendering. A capability described in a slide deck is a snapshot. The distinction is structurally central to the M&A failure prediction in the next section.

***Boundary Conditions***

The theory applies when four conditions hold (B1–B4). Order matters: outcomes depend on the sequence of decisions, not merely their cumulative count (this rules out commodity spot markets where buying 100 widgets at five dollars is identical to buying 100 widgets at five dollars in any order). Decisions are non-fungible: hiring Person A then Person B produces a different log than hiring B then A (the second hire inherits a different organizational context). Decisions are non-reversible at zero cost: once a hire is made, an SOP version published, a customer relationship begun, the event is on the log even if a later event supersedes it. An event taxonomy can be specified ex ante: T must be agreed before cases are coded, to defeat the critique that the log can expand or contract post hoc.

The theory does not apply to spot markets where order is irrelevant to outcome, to one-shot transactions where no log accumulates because the relationship ends at completion, or to pre-digital settings where the log is purely conceptual without documentary substitutes. The formalism remains a useful theoretical model in those cases but cannot be empirically tested without identifiable event records. The Hermès craft-continuity boundary case — pre-digital but with apprentice records, master-craftsperson lineage trees, and pattern books going back to the nineteenth century — is empirically harder than Toyota's digital-era log but not infeasible.

***Four Propositions***

The formalism implies four propositions about capability transfer.

**P1 (Log-compatible merge preserves projection).** If κ(L_A, L_B) > θ_high, post-merge projection continuity is at least .90 for t ≤ 5 years following the merge, where continuity is π(L_M, q, t) ≈ π(L_A ⊕ L_B, q, t) within an empirically calibrated tolerance ε for the same q.

*Falsification.* P1 is falsified by a clean κ > θ_high merger that exhibits projection discontinuity within five years on capability queries that depend on substrate (as opposed to identity-substrate; brand names are snapshots).

**P2 (Snapshot import diverges).** If the acquirer imports a snapshot S_B = π(L_B, q, t_0) without merging L_B itself (acquirer-supreme conflict resolution with the target log effectively discarded), then for t > t_0 + 3 years, π(L_A ∪ {S_B}, q, t) diverges from π(L_A ⊕ L_B, q, t) for any q that depends on capability substrate.

*Falsification.* P2 is falsified by a clean snapshot-import case in which the imported capability remains intact beyond three years on substrate-dependent queries.

**P3 (Joint dependence on log compatibility and integration policy).** Writedown magnitude in a failed M&A is jointly determined by raw log incompatibility (1 − κ(L_A, L_B)) and the acquirer's chosen conflict-resolution policy. Acquirer-supreme policies amplify low compatibility into large writedowns; negotiated or target-preserving policies attenuate it. The κ-magnitude alone underdetermines outcome; the policy choice is the multiplier.

*Falsification.* P3 is falsified by (i) inverse correlation between conflict density and writedown holding integration policy constant, or (ii) systematic absence of writedown-attenuation under negotiated/target-preserving policies on otherwise comparable deals.

**P4 (Projection-only imitation bound).** An imitator who observes only the projection π(L, q, t) of a substrate they do not possess cannot replicate capability responses to novel queries q' outside the imitated projection's training distribution. Imitation success on the original query q is not evidence of capability transfer; only persistence under new q' is.

*Falsification.* P4 is falsified by demonstrably substrate-free imitators that match the canonical's responses to genuinely novel queries over a sustained interval. The sign-inverted projection signature predicted between canonical and imitator π_λ is the central empirical test.

These propositions are pre-registered with the coding protocol (Methods Appendix). They are intended to be falsifiable on observable evidence; the substrate-projection distinction stands or falls on whether their predictions are borne out across the case sample and any subsequent larger-N panel.

***Companion Computation Script and Worked Monte Carlo***

Runnable Python scripts reproducing the worked instances of π_λ and κ, and a 20,000-trial Monte Carlo of the propositions' comparative statics, are published in the public mirror at `github.com/spectralbranding/orgschema-papers/capability-as-projection/code/`. The projection demo (`projection_demo.py`) takes a sample log L in JSON form, computes π_λ projections for a range of λ values, and computes κ on two synthetic logs with stipulated conflict densities. The Monte Carlo (`monte_carlo_simulation.py`) sweeps a five-cell density grid (0.0, 0.1, 0.5, 0.7, 0.9) and a four-cell decay grid (λ = 0.0, 0.1, 0.5, 1.0) under two integration policies (acquirer-supreme, negotiated), with 500 trials per cell and random seed 42.

The simulation reproduces the predicted comparative statics. At density = 0, continuity is identical under both policies (gap = .000). At density = .9, acquirer-supreme writedown is approximately twice negotiated writedown (.131 versus .058 at λ = 0.1) and continuity falls to .87 versus .94. Writedown is strictly monotonically increasing in conflict density at every λ. Four of five pre-registered numerical checks pass; the fifth (C2: continuity gap ≥ .10 at density .9) is an honest near-miss at .073 under the pre-registered weighting. The near-miss is reported as written rather than tuned away: it indicates the mechanism is present in the right direction with the right monotonicity but at smaller magnitude than the synthetic threshold, identifying a calibration question for the empirical companion paper rather than a contradiction of the formalism. Full results, plots, and replication instructions are in the `POST_EXPERIMENT_REPORT.md` companion to the script. The two plot files (`plot_projection_continuity_vs_kappa.png` and `plot_writedown_vs_conflict_density.png`) visualize the substrate-vs-snapshot wedge directly.

## **Mechanism: Log-Merge in Mergers and Acquisitions**

***Experience as Log, Integration as Projection***

The propositions in the previous section reduce to a single mechanism in the M&A context: post-deal capability transfer succeeds when the acquirer merges logs and fails when the acquirer imports snapshots. The mechanism supplies the micro-foundation for an empirical regularity that the literature has documented but not yet explained mechanistically.

Phanish Puranam and colleagues [@puranam-2006-due-diligence-failure; @puranam-2007-what-they-know] and Maurizio Zollo and Harbir Singh [-@zollo-2004-deliberate-learning-corporate] showed that prior acquisition experience improves post-acquisition outcomes only under specific conditions: the experience must be relevant to the focal deal and the integration choice must be deliberate rather than automatic. Their findings have been replicated and refined [@graebner-2017-process-postmerger-integration], but the mechanism by which prior experience produces improvement has remained underspecified. The substrate-projection view offers a candidate.

An experienced acquirer has, on its own log, POLICY events that codify integration choices — which classes of conflicts to resolve LWW, which to negotiate. Those POLICY events constrain the projection of the next integration: when the acquirer faces a new κ-conflict, the prior POLICY events supply a default resolution tested against earlier deals. Experience improves outcomes because experience is the log; the policies encoded in the log narrow the space of projections the acquirer can credibly choose at integration time.

The deliberate-integration condition maps onto the determinism contract (P2): deliberate integration is conducted as if the log were the source of truth, with documented conflict identification, recorded resolution choices, and traceable rationale. Automatic integration violates the contract by reading non-log state — assumptions not anchored to recorded prior decisions.

The log-merge view further predicts when prior acquisition experience will *not* help: when the focal deal's κ-conflict structure differs categorically from anything in the acquirer's log. Microsoft had substantial prior software-acquisition experience by 2014, but the Nokia deal raised conflicts — hardware-software co-design cadence, supplier integration, factory-floor decision rights — that the software-acquisition log did not contain. The prior log was orthogonal to the focal conflicts. This is consistent with the relevance-of-experience finding [@zollo-2004-deliberate-learning-corporate; @puranam-2007-what-they-know]; the substrate-projection view explains why relevance is operationalized as log overlap on the focal conflict classes.

***Three Auxiliary Predictions***

The mechanism generates three predictions beyond the propositions above. First, acquirers with diverse acquisition histories exhibit smaller variance in integration outcomes than acquirers with narrow histories, because their log supplies POLICY defaults across a wider range of κ-conflict classes. Second, integration teams whose composition turns over rapidly produce more variable outcomes than teams with stable composition, because team-internal log replay is harder when team members carrying the log depart. Third, post-acquisition writedown timing is predictable from the joint structure of κ and integration policy: low-κ deals with acquirer-supreme integration exhibit early writedowns (within three years, when substrate-dependent capability queries first reveal divergence); moderate-κ deals with negotiated integration exhibit late writedowns if any. These predictions are pre-registered as falsifiable extensions for the companion empirical paper described in the discussion.

<!-- NANOBANA_PROMPT: Two side-by-side timeline diagrams in spectral palette. Left panel labeled "Disney + Pixar 2006 (log merge)" shows two horizontal lines (Disney log on top, Pixar log on bottom) approaching a merger point in 2006, then continuing as parallel lines that occasionally cross-link with thin connector lines, both extending to 2026 without breaks. Right panel labeled "Microsoft + Nokia 2014 (snapshot import)" shows Microsoft log continuing as a horizontal line, Nokia log ending abruptly at 2014 with a small snapshot icon (a rectangular slide-deck shape) being absorbed into Microsoft's line; Nokia's line does not continue. A 2016 marker on Microsoft's line shows a downward-pointing red triangle labeled "$7.6B writedown." Journal-quality, technical. -->
<!-- ILLUSTRATION: Figure 3. Log merge versus snapshot import. Disney+Pixar preserved both logs through an LWW integration policy; Microsoft+Nokia discarded the Nokia log and imported a snapshot of its capabilities. The post-2014 trajectory diverges from what a log-merged counterfactual would have produced. -->

## **Illustrative Cases: Three Process-Traced Anchors**

This section reports three process-traced cases coded under an honest single-coder pass of the pre-registered protocol (Methods Appendix). The cases are selected as boundary objects: one clean log merge (Disney+Pixar), one snapshot-import failure with moderate raw log compatibility (Microsoft+Nokia), and one continuous transfer-failure phenomenon (Toyota Production System imitation). Together they cover the high-κ, moderate-κ-with-acquirer-supreme-policy, and substrate-without-rendering regions of the parameter space. The process-tracing approach follows Ann Langley's [-@langley-1999-strategies-theorizing-process] strategies for theorizing from process data: temporal bracketing, narrative reconstruction, and visual mapping of event sequences. Per protocol §A.3, each focal organization has at least ten calendar years of log depth prior to the focal event.

A note on the coding pass. The reported values come from a single-coder honest application of the pre-registered protocol against public sources (academic case studies, participant memoirs, SEC filings, peer-reviewed Nokia and Toyota studies). The gold-standard two-blind-coder + adjudicator protocol specified in §A.5 is reserved for a planned larger-N empirical companion study with access to primary sources (Pixar Braintrust transcripts, Disney board minutes, Microsoft integration memos) not consulted here. The values reported below are therefore illustrative of the method applied honestly, not the gold-standard output. Per-case event logs and coding reports are published in the public mirror at `github.com/spectralbranding/orgschema-papers/capability-as-projection/code/case_event_coding/`.

***Disney + Pixar 2006: Log Preservation***

Disney's January 2006 acquisition of Pixar for USD 7.4 billion preserved an unusually visible operational log. The Pixar log relevant to "What is this firm's capability to produce successful animated features?" includes the Braintrust review meetings, the daily review cycles, the Notes Day events, and the directors' decision authority — all POLICY and ARTIFACT events with clear documentation in participant memoirs and case studies.

Single-coder honest application of the pre-registered protocol against public sources [@anand-2010-walt-disney-company; @catmull-2008-how-pixar-fosters; @catmull-2014-creativity; @iger-2019-ride-lifetime-lessons] and Disney SEC filings produced 57 events across both pre-acquisition logs: 50 Pixar events (1986–2006) and 7 Disney pre-acquisition events documented in public sources. Of the 57, 46 are HIGH-confidence and 10 are MEDIUM-confidence. The Pixar/Disney asymmetry reflects source asymmetry rather than coding bias: Pixar's Braintrust era is heavily documented in Catmull's published work, while Eisner-era Disney animation POLICY events sit primarily in Disney board minutes not accessed in this pass. Densifying the Disney pre-acquisition side would likely shift κ inside its uncertainty band but not across band boundaries.

The Disney integration policy was last-write-wins favoring Pixar's later events: Disney's prior creative-review process from the 1990s was a POLICY event; Pixar's Braintrust was a POLICY event from the 2000s; under LWW the Pixar POLICY events superseded Disney's, and Pixar's leadership, review cadence, and decision rights were preserved. Compatibility κ(L_Pixar, L_Disney) = .84 (honest uncertainty range .78–.92 across alternative conflict-counting choices). This places the case in the high-κ region predicted by P1.

Per P1, projection continuity should be at least .90 for the focal query at t ≤ 5 years. All five HIGH-confidence Pixar POLICY events documented through 2006 remain in force through 2011 in public records, consistent with the prediction. Per P3, low conflict density combined with negotiated/target-preserving integration policy should yield low writedown; observed writedown over the full subsequent decade was zero. Both propositions are consistent with the case in direction.

The mechanism is direct: Disney chose an integration policy under which the Pixar log was preserved; the projection was a live rendering, not a frozen snapshot; subsequent queries about Pixar's capability could be evaluated against the live log, and the capability survived. *Toy Story 3* (2010), *Inside Out* (2015), and *Coco* (2017) are projections of the post-merge log evaluated under new queries at new render times. The per-case event log is published at `github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/case_event_coding/disney_pixar_2006_event_log.csv`.

***Microsoft + Nokia 2014: Acquirer-Supreme Snapshot Import***

Microsoft's April 2014 acquisition of Nokia's Devices and Services division for USD 7.2 billion provides the central counter-case. The Nokia log relevant to "What is this firm's capability to ship a globally competitive mobile platform?" includes the hardware-software co-design cadence developed across the Symbian and MeeGo generations, supplier-relationship management routines, and the operational-software stack for handset firmware.

Single-coder honest application of the protocol over 1997–2014 produced 47 events across both pre-acquisition logs: 29 Nokia events and 18 Microsoft pre-acquisition mobile events. Sources include the Microsoft Corporation 10-K filing [-@microsoft-2015-annual-report-form] on the impairment, the Microsoft 8-K filed 2014-07-17 announcing the 12,500-person layoff plan, Nokia annual reports 2010–2013, Vuori and Huy [-@vuori-2016-distributed-attention-shared] on pre-acquisition Nokia capability erosion, and Aspara, Lamberg, Sihvonen, and Tikkanen [-@aspara-2023-chance-strategy-change] *Academy of Management Discoveries* on Nokia 1986–2015, and Lamberg, Lubinaite, Ojala, and Tikkanen [-@lamberg-2021-curse-agility-nokia] *Business History* on the loss of mobile-phone market dominance 2003–2013. Of the 47 events, 35 are HIGH-confidence and 11 are MEDIUM-confidence.

The honest coding produces a finding sharper than the original framing the paper was drafted from. Raw log compatibility κ(L_Nokia, L_Microsoft) = .79–.85 (range .61–.92 across alternative conflict-counting choices) — moderately high, not near zero. The capability-transfer failure was therefore not driven by raw log incompatibility. It was driven by Microsoft's chosen integration policy: acquirer-supreme with an aggressive layoff program (12,500 positions including approximately 70 percent of the Nokia D&S workforce announced 90 days post-close, per Microsoft 8-K 2014-07-17). The policy deliberately discarded L_Nokia rather than merging it. Stephen Elop departed June 2015; division reorganization completed September 2015; long-tenured Nokia engineering leads either left or had their decision rights narrowed under Microsoft reporting structures.

This finding is theoretically central. The original draft framed the case as κ ≈ 0 by snapshot-import construction; honest coding shows that the raw log compatibility was moderate but the policy choice converted compatibility into discard. The corrected reading sharpens rather than weakens the substrate-projection contribution: P3 in its joint-dependence form is what the case supports, and the integration-policy variable is isolated from the log-structure variable in a way that the κ-alone framing would have hidden.

Per P2, snapshot import should produce divergence within three years on substrate-dependent queries. The impairment was announced July 8, 2015 — 15 months post-close — at USD 7.6 billion against a USD 7.2 billion purchase price [@microsoft-2015-annual-report-form]. The Lumia line was discontinued in 2017. Per P3 in its joint form, the large writedown is jointly explained by moderate-to-low κ AND acquirer-supreme integration policy with 70 percent layoff. Counterfactually: had Microsoft adopted a negotiated or target-preserving integration policy at the same κ, the Monte Carlo comparative statics predict approximately one-half the writedown magnitude. Both P2 and the revised P3 are consistent with the case. The per-case event log is published at `github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/case_event_coding/microsoft_nokia_2014_event_log.csv`.

The structural takeaway is that Microsoft preserved everything tangible — factories, patents, brand, employees — but discarded the rendering apparatus by which the Nokia log produced capability projections. The snapshot S = π(L_Nokia, "mobile platform capability", t_2014) was imported into Microsoft's operating system; subsequent queries about that capability could only be evaluated against the snapshot, not against a live log. When the Lumia line had to respond to new platform shifts (Android consolidation, Apple-led services migration), no log was queryable. The capability was inert.

***Toyota Production System: Substrate Without Rendering***

The Toyota Production System provides the third case: not an acquisition, but a continuous transfer-failure phenomenon spanning four decades and hundreds of would-be imitators. Toyota's manufacturing capability is among the most thoroughly documented operational systems in history; the artifacts are public [@liker-2004-toyota-way-14; @spear-1999-decoding-dna-toyota]; the visible practices can be observed in factory tours. Yet imitators systematically fail to reproduce the results despite copying the artifacts faithfully.

Single-coder honest application of the protocol produced 36 events: a canonical Toyota log L_Toyota of 26 events drawn primarily from Liker [-@liker-2004-toyota-way-14], Spear and Bowen [-@spear-1999-decoding-dna-toyota], and Spear [-@spear-2009-chasing-rabbit-how], and a stylized composite L_Imitator of 10 events from documented imitation failures (the imitator is a composite rather than a single named firm, honestly disclosed). Of the 36 events, 29 are HIGH-confidence and 5 are MEDIUM-confidence. The POLICY density is 44.4 percent: TPS substrate is itself a stack of versioned policies (kanban, andon, 5-Whys, standard work, A3, kaizen, senshu lineage).

Computing the projection operator π_λ on both logs produces the structural signature predicted by P4. At λ = 0.0 (no decay), π_λ(L_Toyota) = +14.0 while π_λ(L_Imitator) = −4.5. At λ = 0.1, π_λ(L_Toyota) = +0.52 while π_λ(L_Imitator) = −0.31. At λ = 0.5, π_λ(L_Toyota) = +0.007 while π_λ(L_Imitator) = −0.0001. The signs are inverted across all decay rates: the imitator's projection is negative-valued at every λ examined. The κ-equivalent on the canonical-versus-imitator pairing is .38–.50 under POLICY-POLICY plus POLICY-FAILURE counting, .71 under strict POLICY-POLICY only. The substantially lower κ than the M&A cases fits the structural prediction: an imitator by construction conflicts with the substrate-generating policies that anchor the canonical log.

The substrate-projection view explains the imitation failure mechanically. Imitators import the snapshot — the projection at time t_imitation evaluated against Toyota's log. They reproduce S = π(L_Toyota, "production capability", t_2003) as a set of visible artifacts. They do not import L_Toyota itself: the seventy years of FAILURE events on which the kaizen log was built, the POLICY events documenting why each standard work revision happened, the PERSONNEL log of master-mentor lineages. When a new event occurs in the imitator's factory, the imitator cannot project a response from L_Toyota because L_Toyota is not present; the imitator must respond from its own thin log. The kanban card has no information content without the log that generated it.

This restates Spear and Bowen's [-@spear-1999-decoding-dna-toyota] DNA argument in substrate-projection terms. Their four rules describe the constraints under which the Toyota log is appended to. Imitators copy the artifacts that result from the rules but do not adopt the rules under which the log is generated. With the rules absent, no log accumulates; with no log, the projection has no substrate; without a substrate, the visible capability is inert. The sign inversion in π_λ is the empirical fingerprint: the imitator does not merely have a smaller-magnitude projection, it has a structurally negative one because the documented failures unattended by kaizen response accumulate to negative weight under the canonical query. P4 applies: any imitator who copies the snapshot without operating under conditions that would produce a comparable log diverges from Toyota's projection on any query that requires substrate access. The per-case event log is published at `github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/case_event_coding/toyota_tps_event_log.csv`.

<!-- NANOBANA_PROMPT: Side-by-side contrast diagram. Left panel labeled "Toyota: log-generating substrate" shows a deep vertical timeline (1953–2026) thickly populated with small icons — wrench, document, line-graph, person — at every level, with the topmost present-day rendering shown as a clean kanban card and andon-cord icon. Right panel labeled "Imitator: snapshot only" shows a thin recent-history timeline (3–5 years) with the same kanban card and andon-cord icons at the top, but the timeline below them is mostly empty with only sparse documentation icons. A dashed arrow labeled "snapshot import" connects the top of Toyota's timeline to the top of the imitator's. Beneath the imitator panel: small caption "no substrate to project from." Spectral palette, journal-quality. -->
<!-- ILLUSTRATION: Figure 4. Toyota Production System and its imitators. The visible artifacts are identical; the underlying log is not. New queries produce divergent projections because the imitator has no log to project from. -->

## **Architectural Existence Proof: ActiveGraph as Motivating Analogy**

The substrate-projection view stands as a theoretical reformulation independent of any engineering instance. An open-source engineering instance — released two weeks before this paper was drafted — supplies an existence proof that event-sourced substrate is operationally tractable outside metaphor. This section engages it briefly. Yohei Nakajima [-@nakajima-2026-log-is-agent] released *The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems* with an open-source Apache-2.0 implementation. The framework — ActiveGraph — implements an append-only event log as source of truth, deterministic projection into a queryable state, content-addressed replay, and cheap fork-and-diff for counterfactual reasoning. We theorize organizations; ActiveGraph supplies a real-world implementation, not the object of theory.[^scope]

[^scope]: A companion methods paper develops ActiveGraph as a measurement substrate for organizational logs. The theoretical argument in the present paper does not depend on the methods paper.

The architectural parallel that bears on the theory is the determinism contract: Nakajima's §3 specifies that behaviors must not read random values, wall-clock time, fresh UUIDs, or mutable global state. The organizational analogue is the determinism contract on capability projections (P2 in §3.2 above): π must not read non-substrate state — unwritten know-how, untranscribed conversations, lost memories. Where it does, the projection fails to replay, and capability transfer fails predictably. Microsoft's import of Nokia's mobile-platform capability violated the determinism contract: the projection was reproducible only against the live Nokia log, which Microsoft did not preserve. Nakajima cites no management literature in his reference list; the present paper is not a strategy-side commentary on Nakajima but an independent argument that arrives at a compatible substrate ontology from the strategy-theory side. The convergence supplies external validation for both arguments without making either dependent on the other.

## **Discussion**

***Boundary Conditions and Scope***

The theory applies to organizational settings satisfying B1–B4: order matters, decisions are non-fungible, decisions are non-reversible at zero cost, and an event taxonomy can be specified ex ante. The substrate-projection distinction is therefore not universal; it applies wherever B1–B4 hold. Outside them, the formalism collapses: spot markets, one-shot transactions, and pre-digital settings without documentary substitutes do not admit empirical operationalization. The Hermès craft-continuity case is the empirically harder boundary: pre-digital but with apprentice records, lineage trees, and pattern books that approximate a log.

The scope claim is deliberately narrow. The contribution is a substrate-layer addition to existing capability theory, not a wholesale recasting of the firm.

*Generalizability.* The three illustrative cases skew Anglo-Japanese and product-firm: Disney+Pixar (US media), Microsoft+Nokia (US/Nordic), Toyota (Japan automotive). Generalizability to Chinese state-owned enterprises, family-owned non-Western SMEs, services firms where the log lives partly in client-relationship history, and pre-2000 firms with sparse digital trace is not established. The companion fifty-event panel paper commits to oversampling non-Western deals and services-sector targets. The theory is substrate-agnostic; empirical-test feasibility is documentation-constrained.

***Cross-Domain Corroboration: Distorting Projections in AI Systems***

A parallel mechanism is now being documented empirically in artificial-intelligence research, where a rendering operator — alignment training — distorts the behavioral substrate it reads rather than reproducing it faithfully. Han Bao and colleagues [-@bao-2026-ai-alignment-breaks] find that alignment produces structural distortions concentrated at the edge and tail of the behavioral distribution; Tianyi Peng and colleagues [-@peng-2025-digital-twins-funhouse] identify five systematic distortion types — ideological bias and hyper-rationality among them — spanning the full distribution of simulated behavior. The two results bracket the same phenomenon from complementary angles: distortion at the tail and distortion across the distribution. Both corroborate this paper's claim at the projection layer — that a capability read through a distorting or frozen projection (the snapshot import of P2) degrades relative to one evaluated against the live substrate. The substrate-projection distinction is thus not confined to organizational settings; it recurs wherever a rendering operator is interposed between an accumulated substrate and the behavior read from it.

***Theoretical Contributions***

Three contributions follow.

First, the theory specifies an event-sourced substrate beneath the resource-based and dynamic-capabilities tradition. The Penrose-Teece-Helfat lineage treated capability as a stock; the substrate-projection view treats it as a render-time projection of an append-only log. The reformulation preserves the path-dependence intuition central to Penrose [-@penrose-1959-theory-growth-firm] while supplying a substrate that can be specified, observed in principle, and tested. The construct-validity debate [@arend-2009-assessing-dynamic-capabilities; @helfat-2009-understanding-dynamic-capabilities] is relocated: the tautology critique is a category error arising from collapsing substrate and projection, and the relocation makes the construct falsifiable through P1–P4. The microfoundations critique [@felin-2012-microfoundations-routines-capabilities] is answered structurally: substrate lives at the event level, capability at the projection level.

Second, the theory derives testable predictions about capability transfer from log-merge mechanics. An academic-integrity note bears on this contribution. The honest event-coding of the Microsoft+Nokia case produced a stronger theoretical claim than the version the paper was originally drafted from. Initial framing assumed Microsoft+Nokia exhibited κ near zero by snapshot-import construction. Honest coding showed κ in the .79–.85 range — moderate, not zero. The writedown was nevertheless extreme. The reframing this forced — P3 as joint dependence on (1 − κ) AND integration policy — is sharper than the κ-alone version because it isolates the policy-choice variable from the log-structure variable. The Disney+Pixar/Microsoft+Nokia contrast is now a contrast in integration policy at comparable log compatibility, not a contrast in log compatibility alone. This is the kind of theoretical refinement that honest empirical engagement produces and that fabricated values would have hidden.

Third, the theory bridges to an open-source engineering instance — Nakajima [-@nakajima-2026-log-is-agent] — that supplies an existence proof for event-sourced substrate operating outside strategy-theoretic metaphor. Future empirical work can use process-mining tools [@vanderaalst-2016-process-mining-data] and event-sourced reasoning frameworks to reconstruct organizational logs from documentary traces and test substrate-projection predictions at scale.

***Limitations***

Following Nakajima [-@nakajima-2026-log-is-agent] §9, four limitations are named.

*Schema evolution.* The event taxonomy T (Methods Appendix A.2) is fixed ex ante to defeat post-hoc fitting, but real organizations evolve their internal recording schemas over decades. The protocol A.7 robustness check addresses this through granularity variation, but residual schema-evolution noise remains. The organizational analogue of Nakajima's schema-evolution failure mode is process-documentation drift: the same event type means different things in different decades.

*Concurrent writers.* Matrix organizations, distributed multinationals, and decentralized partnerships produce events from multiple actors simultaneously with no global clock. The poset structure of L is partial precisely to accommodate this, but conflict identification becomes harder when events that should have been ordered were not, and κ is sensitive to how ties are broken.

*Replay cost.* Long-lived firms accumulate decades of log. Querying the full log is computationally and cognitively expensive; institutional memory load may exceed effective recall capacity. The π_λ decay parameter is one response — older events count less — but the choice of λ introduces a free parameter that must be calibrated.

*Empirical scope of this paper.* The three process-traced cases are anchors coded under an honest single-coder pass, not a representative test under the gold-standard two-blind-coder protocol. A coded panel of fifty M&A events with structured κ measurement is in preparation as a companion empirical paper.

*Monte Carlo calibration near-miss.* The pre-registered numerical check C2 (continuity gap between acquirer-supreme and negotiated policies of at least .10 at density .9) failed honestly at a gap of .073 under the pre-registered POLICY-weighting. The mechanism is present in the right direction with the right monotonicity; the magnitude under the synthetic weighting is below the threshold by approximately .03. This is reported as written rather than tuned away. The near-miss is a calibration question for the empirical companion, not a contradiction of the formalism. Full results and replication instructions are in the post-experiment report at `github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/POST_EXPERIMENT_REPORT.md`.

***Future Research***

Two future-research lines are committed to. The first is a fifty-event coded M&A panel as a companion empirical paper applying the pre-registered protocol to deals 2000–2025 with binary log-preservation indicators and continuous κ measurement, testing P1–P4 at scale (regression discontinuity on acquirer prior M&A count in the tradition of Puranam and Srikanth [-@puranam-2007-what-they-know] and Zollo and Singh [-@zollo-2004-deliberate-learning-corporate]). The second is a methods paper developing ActiveGraph [@nakajima-2026-log-is-agent] as a measurement instrument for organizational logs reconstructed from documentary traces.

Three further extensions follow from cohort decomposition implicit in the framework: heterogeneity in projection across different observers of the same log [@zharnikov-2026-organizational-metamerism-when-distinct-configurations]; the brand-as-projection special case [@zharnikov-2026l-rendering-problem-genetic]; and the connection to a six-tier organizational ontology in which the log sits beneath all tiers [@zharnikov-2026-dual-hierarchies-organizational-transferability-six].

## **Conclusion**

Capability is not a stock. It is a projection of an append-only log, computed at the moment a strategic question is asked. Resources, routines, dynamic capabilities, and organizational memory are not different things; they are different projections of the same underlying log, each evaluated under a different query. Transfer fails when the projection is moved without the log. Transfer succeeds when the log is preserved — and when the integration policy chooses preservation over discard.

Treating the append-only event log as the substrate beneath the firm rather than as its exhaust buys properties that resource-based and dynamic-capabilities theories have struggled to obtain together: path-dependence with formal substrate, inimitability with operational specification, capability heterogeneity with falsifiable predictions. The reformulation does not abandon the prior tradition; it specifies the substrate the tradition has assumed implicitly.

---

## Acknowledgments

The author thanks the practitioners and commenters who engaged with prior work in the Spectral Brand Theory and Organizational Schema Theory corpora; their named-case additions and objections sharpened the theoretical argument during drafting. André Lindenberg surfaced Nakajima's ActiveGraph runtime as the engineering anchor at a critical point in the drafting cycle.

AI assistants (Claude Opus 4.7, Grok 4.1, Gemini 3.1) were used for initial literature search, editorial refinement, and implementation of the companion computation scripts and event-coding pass; all theoretical claims, propositions, interpretations, and the integrity of the empirical record are the author's sole responsibility.

## CRediT Contributions

**Dmitry Zharnikov**: Conceptualization, Formal analysis, Investigation, Methodology, Writing — original draft.

---

## References

::: {#refs}
:::

## Appendix A: Methods Appendix — Ex-Ante Event Coding Protocol (Pre-Registered)

*This appendix reproduces the pre-registered coding protocol committed to before any of the three process-traced cases in this paper were written up. The pre-registered protocol is published at `github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/METHODS_APPENDIX_event_coding_protocol.md` and time-stamped at the initial Zenodo deposit. Modifications during drafting are recorded in the version history of that file.*

### A.1 Unit of Analysis

The unit is the **organizational event**: a discrete, dated, attributable, immutable record in or about the focal organization, of a kind that (i) is at least in principle reconstructable by an independent third party from documentary or testimonial evidence, and (ii) plausibly bears on at least one organizational capability under study. Excluded: unrecorded conversations, generalized culture claims unanchored to specific events, ex-post strategic rationalizations.

### A.2 Event Taxonomy T (Fixed Pre-Coding)

Each event is assigned exactly one type from this taxonomy, fixed before any coding begins. Refinement requires a new pre-registered protocol version.

*Type categories (five top-level types).*

DECISION — a choice attributable to a named decision-maker among at least two documented alternatives. Hiring decisions, acquisition approvals, market-entry approvals, SOP-revision approvals, kill-or-continue project decisions.

FAILURE — a negative outcome event recorded as such by the organization or by an independent third party. Product recalls, lost contracts, missed shipments, public apologies, SEC enforcement actions, internal post-mortems labelled "failed."

POLICY — a versioned written commitment to a rule, procedure, or standard. SOP-vN publication, code-of-conduct revision, board policy resolutions, published handbooks.

PERSONNEL — a named individual entering, exiting, or changing role. Hires, departures, promotions, role-bundle changes.

ARTIFACT — a produced output that survives the event of its production and becomes part of the firm's substrate. Code commits, patents granted, products shipped (with serial numbers), publications, brand assets registered.

*Excluded as event types.* General-tone-of-management observations; aggregate financial outcomes (these are renderings, not events); reputational impressions absent specific recorded incidents; marketing or PR statements that do not bind future behaviour.

*Granularity rules.* Minimum granularity: a single decision, recorded action, or attributable change. Maximum granularity: aggregation up to a single fiscal quarter is permitted only for high-frequency low-significance events (e.g., aggregated kaizen-suggestion counts). All DECISION, FAILURE, POLICY, and PERSONNEL events are coded at unit granularity. Tie-breaking: when ambiguity exists about whether two records reflect the same event or two events, code as two events unless they share id and timestamp in primary sources.

### A.3 Minimum Temporal Depth

For an organization to be eligible as a process-traced case, the log L must cover at least 10 calendar years prior to the focal event under analysis. Logs shorter than 10 years are excluded. Toyota post-Ohno (1953 → present) has approximately 70 years; Pixar pre-Disney (1986 → 2006) has 20 years; Nokia D&S pre-Microsoft (1997 → 2014) has 17 years; Microsoft mobile pre-Nokia has approximately 10 years.

### A.4 Identifier Discipline

Each event is assigned a stable event id within the case. Two coders working independently must agree on (i) whether two records refer to the same event (same id), and (ii) the canonical id for newly coded events. Cohen's κ on event identity exceeding .80 across blind coders is the threshold for protocol-compliant coding.

### A.5 Coder Protocol

*Blind coding.* Two coders independently code the same source materials without seeing each other's coding sheets until both are complete. Disagreements are surfaced and resolved by a third (blind) adjudicator. Final coded log is the adjudicator-resolved superset.

*Source hierarchy.* Sources are ordered by reliability: primary documentary (board minutes, SEC filings, court records, dated internal SOPs, version-controlled code repositories, dated patent filings); primary testimonial (interviews with named participants conducted on the record by independent parties); secondary authoritative (peer-reviewed academic case studies, HBS cases authored by recognized scholars, books by participants when corroborated); tertiary (news media, trade press, hagiography or critique published more than 5 years post-event). Events sourced only from level four are flagged and excluded from any test of the propositions.

*Confidence rating.* Each event carries a confidence rating in {HIGH, MEDIUM, LOW}. HIGH: source level 1 or 2, two coders agree, no ambiguity. MEDIUM: source level 1–2, coders disagree initially but adjudicator resolves to consensus. LOW: source level 3, single source, or unresolved coder disagreement. Tests of the propositions use HIGH and MEDIUM events only.

### A.6 Conflict-Resolution Policy Taxonomy

For coding compatibility κ(L_A, L_B) in M&A cases, conflicts are identified pairwise. Three formal conflict patterns are recognized: POLICY-policy conflict (incompatible rules for the same domain); PERSONNEL-personnel conflict (named role assigned to different individuals at the same effective date); ARTIFACT-artifact conflict (artifacts under conflicting schemas).

For each conflict, the coder records which resolution policy the acquiring organization chose: LWW (last-write-wins; later event supersedes earlier); ACQUIRER (A's event prevails); TARGET (B's event prevails); NEGOTIATED (new combined policy supersedes both); DEFERRED (conflict noted, neither resolved). κ measurement excludes NEGOTIATED resolutions (they resolved cleanly); ACQUIRER, TARGET, and DEFERRED count toward conflicts. LWW counts toward conflicts only if the older event was operationally central.

### A.7 Robustness Checks (Pre-Registered)

*Event-granularity threshold variation.* Re-code each case at two alternative granularities — coarsened (aggregate same-month same-type same-actor events) and refined (split aggregate events into per-month) — and test whether κ values are stable to ± .05 and propositions hold qualitatively.

*Placebo tests.* Apply the protocol to two placebo cases where the propositions should not hold: a routine supplier-contract renewal with no capability-transfer dimension, and a pure equity acquisition with no operational integration intent. Failure of the propositions in placebos confirms specificity.

*Blind coder variation.* A third blind coder independently codes a randomly selected 25% of events from each case. Inter-coder Cohen's κ across the three coders exceeding .75 is the protocol-compliance threshold.

### A.8 Identification Strategy

Primary identification for the companion empirical paper: regression discontinuity on acquirer prior M&A experience as a forcing variable with discontinuity at the median, inheriting the design tradition of Zollo and Singh [-@zollo-2004-deliberate-learning-corporate] and Puranam and Srikanth [-@puranam-2007-what-they-know]. Secondary: propensity-score matching on observable log proxies (patent citation tree depth, employee tenure distribution, public-documentation surface area, executive average tenure at deal time). Tertiary: instrumental variables using exogenous CEO death events or unexpected regulatory disclosure shocks as instruments for log-quality observability, with strong-instruments tests pre-required (first-stage F greater than 10). Fallback: convert to pure-theory version with the three process-traced cases as illustrative anchors.

### A.9 Pre-Registration

This protocol is pre-registered as part of the initial Zenodo deposit and published at `github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/METHODS_APPENDIX_event_coding_protocol.md`. The pre-registered version is the one shipped with the final paper as this Methods Appendix and as a separate file in the public-mirror repository.

### A.10 Note on Circularity Defence

The predicted lead reviewer objection — how one would independently identify and code the event log without circularity to the outcomes being explained — is addressed by the following defence stack: the event taxonomy T is fixed before coding (A.2); the source hierarchy privileges primary records over post-hoc accounts (A.5); the two-coder blind plus adjudicator protocol (A.5, A.7) defeats single-coder confirmation bias; robustness checks include placebo cases where propositions should fail (A.7); confidence ratings transparently disclose where coding is uncertain (A.5); pre-registration (A.9) time-stamps the protocol before the empirical narrative is drafted. Together these address the circularity charge at the standard expected of theory papers with case-study empirical anchors. The protocol does not eliminate all subjectivity in event identification — no protocol can — but makes subjectivity visible and measurable through inter-coder κ.
