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

- **six-tier ontology**
  - The ontology that decomposes an organization into six nested specification tiers, always in the order Owner Intent -> Business Model -> Business Entity -> Product -> Process -> Organization. Each tier answers a distinct governing question and transfers differently on sale.
  - _defined by 2026ag_
