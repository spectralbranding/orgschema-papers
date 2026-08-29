<!-- GENERATED FILE - do not hand-edit. This glossary is a rendered projection of the corpus ontology graph, regenerated on each release. -->

## Glossary

_Terms used by **tier-bundle-algebra** (Tier-Bundle Algebra in Inter-Organizational Resource Transfer: A Fork-Operation Formalism Over the Six-Tier Acquisition-Target Ontology). Defined terms this paper introduces, refines, or imports from the corpus ontology._

*Terms introduced by this paper*

- **Bundle admissibility predicate** (write: `admissibility predicate`)
  - A structural predicate that rejects a tier-bundle incompatible with the seller's tier-collapse state on structural rather than legal grounds.
  - first use: Section 5 — Admissibility predicate
- **Fork cascade rule** (write: `cascade rule`)
  - The rule that a tier fork propagates asymmetrically along the service hierarchy (upward-implying but not downward-implying), so a Tier-4 fork induces a Tier-6 fork along the same modular boundary but not conversely.
  - first use: Section 4 — Cascade rule
- **Tier-bundle** (write: `tier-bundle`)
  - An ordered set of tier-fork operations executed under one transaction envelope, whose signature individuates a named M&A deal type modulo cardinality.
  - first use: Section 3 — Fork Operations and Tier-Bundles (Definition 3)
- **Tier-bundle algebra** (write: `tier-bundle algebra`)
  - A typed-fork-operation formalism over the six-tier acquisition-target ontology in which each named M&A transaction type decomposes into a signature bundle of fork operations across the seller's tier graph.
  - first use: Abstract / Introduction
- **Tier-fork operation** (write: `tier-fork operation`)
  - A typed transfer of a single Tier-n record from a seller's tier graph to a buyer's tier graph under a direction tag, well-typed only when source and target share the tier index.
  - first use: Section 3 — Fork Operations and Tier-Bundles (Definition 2)

*Imported terms (defined elsewhere)*

- **six-tier ontology**
  - The ontology that decomposes an organization into six nested specification tiers, always in the order Owner Intent -> Business Model -> Business Entity -> Product -> Process -> Organization. Each tier answers a distinct governing question and transfers differently on sale.
  - _defined by 2026ag_
- **Tier 1 (Owner Intent)**
  - Why the organization exists. Governed by founder / board chair / dominant shareholder; implicit or off-table in most professional-CEO companies. Transfers nothing directly, only its imprint on lower tiers.
  - _defined by 2026ag_
- **Tier 2 (Business Model)**
  - How value flows into resources. Governed by the CEO (founder-CEOs collapse Tier 1 into Tier 2). Conceptually replicable; not legally owned.
  - _defined by 2026ag_
- **Tier 3 (Business Entity)**
  - What is legally registered and saleable (IP, trademarks, contracts, corporate-legal personality). Governed by General Counsel / corporate treasury. Transfers by document. Often absent from AI-strategy meetings.
  - _defined by 2026ag_
- **Tier 4 (Product)**
  - What is delivered to whom; includes the brand surface (per Brand-as-Tier-4). CMO governs the brand sub-spec; CTO the technical sub-spec (canonical collision at Tier 4). Transfers if specified; not if tacit.
  - _defined by 2026ag_
- **Tier 5 (Process)**
  - How the product is produced. CFO governs the financial sub-spec; COO the operational sub-spec (canonical collision at Tier 5). Transfers if codified.
  - _defined by 2026ag_
- **Tier 6 (Organization)**
  - Who does the producing. Governed by CHRO (sometimes COO). Transfers only partially (retention contracts at best).
  - _defined by 2026ag_
