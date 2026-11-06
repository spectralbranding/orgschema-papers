---
title: "Formalism v0 — Capability as Projection of an Append-Only Organizational Log"
paper_slug: capability_as_projection_paper
version: v0.1.0
date: 2026-05-24
status: pre-paper formalism; implemented by the companion simulations in code/
---

# Formalism: Capability as Projection of an Append-Only Organizational Log

This document specifies the minimal mathematical machinery the paper commits to. It is deliberately small — propositions with simple functional forms and comparative statics, no full stochastic-process measure theory and no agent-based simulation. The aim is mechanism precision rather than proofs.

## 1. Primitives

### 1.1 The event log L

An organization's operational history is modeled as a partially ordered set (poset) of typed events:

> L = (E, ≤)

where E is a set of events and ≤ is a partial order encoding causal-temporal precedence. The order is partial because not all events stand in a defined precedence relation (concurrent decisions in different parts of the firm need not be ordered with respect to each other).

Each event e ∈ E is a tuple:

> e = (id, t, a, τ, p, c)

with:
- **id**: unique identifier (UUID or content hash)
- **t**: wall-clock timestamp (ISO 8601)
- **a**: actor (named individual, role, team, or system)
- **τ**: event type drawn from a fixed taxonomy T (see METHODS_APPENDIX_event_coding_protocol.md §3)
- **p**: payload (the substantive content of the event — a decision recorded, a code commit landed, a hire approved, an SOP version published)
- **c**: caused_by pointer to the event that triggered this one (analogous to ActiveGraph's `caused_by`; null for root events)

Events are **immutable**. Once written they are never edited, only superseded by later events (the analogue of a `policy.updated` event that subsumes a prior `policy.created` event but does not delete it).

### 1.2 The projection operator π

A **projection** is a function that reads a log and produces an observable claim about the organization at a moment in time:

> π : L × Q × t → C

where:
- **Q** is the query space (a finite set of well-formed strategic questions — "What is this firm's capability to ship cars at low cost?" "How fast can this firm respond to a CEO transition?")
- **t** is the render time (the moment the question is asked)
- **C** is the claim space (observable attributes, capability assessments, market valuations, M&A bid prices)

Three required properties of π:

**(P1) Prefix monotonicity.** For any query q and any t' < t, if L_t = L_{t'} ∪ ΔL where ΔL is the event delta over (t', t], then π(L_t, q, t) ⊇ π(L_{t'}, q, t') — the later projection is informed by a superset of the same events. Capabilities can never be erased from the log, only superseded.

**(P2) Determinism conditional on log.** Two evaluators presented with the same L and the same q at the same t produce the same π(L, q, t). This is the strict-replay property of Nakajima §4 transplanted to organizational analysis: capability claims must be reproducible from the log. If different evaluators produce different claims, either (i) the log is incomplete (some events were not recorded), (ii) the query is under-specified, or (iii) one or both evaluators read non-log state.

**(P3) Locality.** π depends only on the subset of L relevant to q (events bearing on the queried capability). Two firms with disjoint logs cannot have their projections cross-influence; this rules out spurious cross-firm "halo" effects in measurement.

A concrete worked instance of π suitable for empirical anchoring is the **weighted prefix sum with decay**:

> π_λ(L, q, t) = Σ_{e ∈ L_q, t_e ≤ t} w_q(e) · exp(−λ · (t − t_e))

where:
- L_q ⊆ L is the subset of events relevant to q
- w_q(e) ∈ ℝ is the per-event weight under query q (signed; e.g., a successful Toyota kaizen-event contributes positively to "low-cost production capability," a recall event contributes negatively)
- λ ≥ 0 is a decay parameter (capability ages — older events count less)

This is one concrete operator among many possible π. The paper claims the substrate (log + general projection) is universal; the specific operator (π_λ) is one calibratable instance for empirical work.

### 1.3 The compatibility function κ

For two logs L_A and L_B (typically the two parties to an acquisition), define:

> κ(L_A, L_B) = 1 − (|conflicts(L_A, L_B)| / (|L_A| + |L_B|))

where conflicts(L_A, L_B) is the set of event pairs (e_A, e_B) with e_A ∈ L_A, e_B ∈ L_B that cannot be simultaneously incorporated into a merged log L_M without contradicting the determinism property (P2). Conflicts arise from (i) incompatible policies (A's promotion rule conflicts with B's), (ii) incompatible artifacts (A's codebase and B's codebase commit to different schemas for the same noun), (iii) incompatible identifiers (A and B both have a senior leader assigned to the same role).

κ ∈ [0, 1]. κ = 1 means perfectly compatible logs; κ = 0 means every event in one log conflicts with some event in the other.

The conflict-resolution semantics are borrowed from the CRDT literature (Shapiro, Preguiça, Baquero, & Zawirski, 2011 — Conflict-Free Replicated Data Types, CACM Vol. 54 No. 5). A merged log L_M = L_A ⊕ L_B requires a per-conflict resolution policy. Three canonical policies:
- **Last-write-wins (LWW)**: the later event by wall-clock time supersedes the earlier (used in Disney's preservation of Pixar's Braintrust over Disney's prior creative-review process — Pixar's later events superseded Disney's older defaults).
- **Acquirer-supreme**: every conflict resolved in favor of L_A (the acquirer's log; the standard "snapshot import" pattern; Microsoft–Nokia is the canonical failure mode).
- **Subsidiary-preserved**: every conflict resolved in favor of L_B (the target's log preserved intact within the parent; Berkshire Hathaway's portfolio firm management is close to this).

### 1.4 Snapshots and renderings

A **snapshot** is the result of applying π to L at a specific t and freezing the output:

> S = π(L, q, t_0)

A snapshot is a projection extracted from its substrate. A snapshot can be passed to another party (the acquirer reads the target's 10-K — that is a snapshot). The snapshot loses the log behind it. Subsequent projections on the snapshot alone (without access to L) can only re-render existing claims; they cannot answer new queries q' that would require log access.

A **rendering** is a live projection — π evaluated on the current L, refreshable as L grows. A capability "in use" is a rendering. A capability "described in a slide deck" is a snapshot.

The snapshot/rendering distinction is critical for the M&A failure prediction (see §3 propositions below).

## 2. Boundary conditions

The theory applies when ALL of the following hold:

**(B1) Order matters.** Outcomes depend on the sequence of decisions, not merely their cumulative count. (Rules out commodity spot markets where buying 100 widgets at $5 is identical to buying 100 widgets at $5 in any order.)

**(B2) Decisions are non-fungible.** Hiring Person A then Person B produces a different log than hiring Person B then Person A (the second-hired person inherits a different organizational context). (Rules out perfectly substitutable transactions.)

**(B3) Decisions are non-reversible at zero cost.** Once a hire is made, an SOP version is published, a customer relationship is started — the event is on the log even if a later event supersedes it. (Rules out one-shot reversible transactions like a single insurance policy renewal.)

**(B4) An event taxonomy can be specified ex-ante.** The taxonomy T (see METHODS_APPENDIX §3) must be agreed before the cases are coded, to defeat the "log can expand or contract post hoc" critique.

The theory does NOT apply when:
- **Spot markets** where order is irrelevant to outcome.
- **One-shot transactions** where no log accumulates because the relationship ends at completion.
- **Pre-digital traceability settings** where the log is purely conceptual — the formalism still applies as a *theoretical* model, but empirical work requires identifiable event records (Pixar Braintrust transcripts, Toyota A3 archives, board minutes, SEC filings, code commits, internal SOP versioning) or robust documentary substitutes.

(The Hermès craft-continuity claim from the foundation article is the boundary case: pre-digital but with documented apprentice records, master-craftsperson lineage trees, and pattern books going back to the 19th century. This is empirically harder than Toyota's digital-era log but not infeasible.)

## 3. Propositions

Three formal propositions with comparative statics:

**P1 (Log-compatible merge preserves projection).** If κ(L_A, L_B) > θ_high (high compatibility), then post-merge projection continuity is at least 90% for t ≤ 5 years following the merge, where continuity is defined as `π(L_M, q, t) ≈ π(L_A ⊕ L_B, q, t)` within an empirically calibrated tolerance ε for the same q.

**P2 (Snapshot import diverges).** If the acquirer imports a snapshot S_B = π(L_B, q, t_0) without merging L_B itself (the acquirer-supreme conflict-resolution policy with κ → 0 by construction because L_B is discarded), then for t > t_0 + 3 years, π(L_A ∪ {S_B}, q, t) diverges from π(L_A ⊕ L_B, q, t) for any query q that depends on capability-substrate (as opposed to identity-substrate; brand names are snapshots that can be imported without the log).

**P3 (Conflict density predicts writedown).** Writedown magnitude in a failed M&A is monotonically increasing in 1 − κ(L_A, L_B), holding constant deal size and industry. Calibration anchor: Microsoft–Nokia ($7.6B writedown, κ ≈ 0 by snapshot-import construction); Disney–Pixar (zero writedown, κ ≈ 1 preserved by integration choice). Intermediate cases (Daimler–Chrysler, AOL–Time Warner) fall on the curve.

Comparative statics on the parameters:
- **λ in π_λ**: higher λ means capability decays faster; older log events lose weight. Empirical estimation of λ per industry is a calibration task; not a free parameter.
- **θ_high in P1**: chosen ex-ante per industry; calibrated against historical successful M&A samples.
- **ε in continuity**: query-dependent; small for narrow technical capabilities (production-process yield rates), large for diffuse cultural capabilities (employer brand strength).

These propositions are pre-registered for falsification: a clean κ = 1 merger that fails within 5 years, OR a clean κ = 0 snapshot import that succeeds beyond 3 years, falsifies P1 / P2 respectively. P3 falsifies on inverse correlations between conflict density and writedown magnitude.

## 4. Connection to existing theory

The formalism specifies the substrate that has been implicit in three prior literatures:

- **Penrose 1959 / Resource-based view**: resources are projections π over a firm-specific log L. Resources cannot be transferred independent of their log; this restates Barney's (1991) inimitability condition as a substrate property, not a resource property.
- **Teece-Pisano-Shuen 1997 / Dynamic capabilities**: dynamic capabilities are time-varying projections π(L, ·, t) — the capability to sense and seize new opportunities is the capability to query the log under new q at new t. Penrose's tautology critique (Arend & Bromiley, 2009) becomes a category error: critics were comparing capability (projection) to performance (also a projection on the same log) without recognizing that the substrate (L) is the common cause.
- **Pentland-Feldman 2003/2005/2008 / Routines as performances**: the ostensive/performative distinction maps onto snapshot (ostensive — the abstract pattern of the routine as recorded) versus rendering (performative — the routine as actually executed against the current state of the log). The performance is π evaluated at the moment of execution. Their argument that routines cannot be designed directly, only the conditions shaping streams of performances (2008), is restated here: capability cannot be designed directly, only L can be designed; π is constrained by what L contains.
- **Nakajima 2026 / Event-sourced agentic systems**: this paper supplies the strategy-side translation of his CS-side substrate. The four log properties Nakajima specifies — append-only, deterministic projection, content-addressed replay cache, fork-and-diff — all carry over. The determinism contract in Nakajima §3 (no random / wall-clock / fresh UUIDs / mutable global state) becomes our determinism contract for capability projections: no unwritten know-how, no untranscribed conversations, no lost memories.

The contribution is the explicit substrate layer that prior theories left implicit. The "thing that has been a stock" in Penrose-Teece-Helfat tradition is the **rendering**; the substrate is the **log**; the operator is the **projection π**. None of the three is reducible to the others.

## 5. What the formalism does NOT claim

- It does not claim that organizations are computers. The log is an analytical construct; firms do not literally execute behaviors over a content-addressed event store. The claim is that capability research is most usefully conducted *as if* an immutable log existed, because the empirical anchor (event records: minutes, SOPs, code commits, hires, public filings) maps cleanly onto the formal log.
- It does not claim full determinism in the limit. Real organizations have non-log inputs (intuitive judgment, undocumented relationships, market shocks). The claim is conditional: *given* the log, capability projections that depend on it should be reproducible. Where they are not, the determinism contract has been violated and we have a research target (find the missing log entries, or characterize the irreducibly non-log component).
- It does not claim a unique optimal projection π. Different queries q produce different projections of the same L; the operator is a function of the question, not a property of the firm. (This is why the same firm can have a "world-class engineering capability" and a "mediocre marketing capability" from the same log — different π over different L_q subsets.)
- It does not claim that all M&A failures are log-merge failures. Many M&A deals fail for non-log reasons (market timing, regulatory shocks, founder departure unrelated to capability transfer). The claim is that *holding those constant*, log-merge mechanics predict the residual variance in transfer success.

---

## Status

This is the v0 formalism (2026-05-24) that the companion simulations in `code/` implement. The paper restates it in prose in the section "The Event-Sourced View". There, P3 is stated as joint dependence of writedown magnitude on log compatibility and integration policy, which extends the v0 P3 above. The CRDT semantics (Shapiro et al. 2011) are explicitly cited; the CQRS projection idea (Kleppmann 2017) is implicit in the projection operator definition.
