<!-- GENERATED FILE - do not hand-edit. This glossary is a rendered projection of the corpus ontology graph, regenerated on each release. -->

## Glossary

_Terms used by **2026al** (Capability as Projection of an Append-Only Organizational Log: An Event-Sourced Substrate Theory of Organizational Capability and Transfer Failure). Defined terms this paper introduces, refines, or imports from the corpus ontology._

*Terms introduced by this paper*

- **Append-only organizational log** (write: `append-only organizational log`)
  - A partially ordered set of immutable, typed events (decisions, failures, policies, personnel, artifacts) recording everything a firm has actually done, serving as the substrate beneath capability.
  - first use: The Event-Sourced View — The Event Log
- **Capability as projection** (write: `capability as projection`)
  - The claim that organizational capability is not a stored stock but a render-time projection computed from a query over the firm's cumulative event log.
  - first use: Abstract / Introduction
- **Log-compatibility function** (write: `compatibility function`)
  - A function scoring how compatible two organizational logs are by counting event pairs that cannot be merged without violating determinism, predicting M&A transfer success.
  - first use: The Event-Sourced View — The Compatibility Function
- **Projection operator** (write: `projection operator`)
  - A function that reads a query-relevant subset of the log at a render time and produces an observable capability claim.
  - first use: The Event-Sourced View — The Projection Operator
- **Snapshot versus rendering** (write: `snapshot versus rendering`)
  - The distinction between a snapshot (a frozen projection extracted from its substrate that can only re-render existing claims) and a rendering (a live, refreshable projection over the current log that can answer new queries).
  - first use: The Event-Sourced View — Snapshots and Renderings

*Imported terms (defined elsewhere)*

- **ontology-dependent records**
  - Records whose meaning depends on the Owner Ontology, so that a reader outside the firm cannot read them correctly without it. Their share is a readiness measure beside fusion.
  - _defined by 2026ag_
- **Owner Ontology**
  - The stakeholder ontology of the controlling party (the Tier 1 stakeholder): the terms in which Owner Intent is phrased and most of the firm's records are written. Tier 1 content carried by the same principal as Owner Intent, not a seventh tier: the Owner Ontology fixes the terms in which questions about the business are worded, and Owner Intent fixes which questions are asked.
  - _defined by 2026ag_
- **shareable part**
  - The part of the Owner Ontology that is the reading key to existing records: the owner's terms as used in the records, verbatim, and the list of ontology-dependent records. It can pass to a buyer or successor as a document.
  - _defined by 2026ag_
- **six-tier ontology**
  - The ontology that decomposes an organization into six nested specification tiers, always in the order Owner Intent -> Business Model -> Business Entity -> Product -> Process -> Organization. Each tier answers a distinct governing question and transfers differently on sale. Full form: "six-tier ontology of a business". It is the analyst's common language for a business, set apart from a stakeholder ontology, which is the business's own ontology as one named position writes it.
  - _defined by 2026ag_
- **stakeholder ontology**
  - A picture of what exists in an activity, what its basic terms mean, what is connected to what, and what is absent, as written from one named position (owner, manager, employee, customer, lender, regulator, buyer, successor), recorded in that position's own words.
  - _defined by 2026ag_
- **Tier 1 (Owner Intent)**
  - Why the organization exists. Governed by founder / board chair / dominant shareholder; implicit or off-table in most professional-CEO companies. Transfers nothing directly, only its imprint on lower tiers.
  - _defined by 2026ag_
