# Pending updates: Tier-Bundle Algebra (2026bj)

Status: pending; raised 2026-10-30; source: decision log dz30#l=11 and #l=15 (ARCHIVE/SMD_raw/Решения_Дмитрия_2026-10-30.md); term spec smd-engine/work/ontology_terms_spec.md (§4).

Owner instruction (Dmitry, 30.10): do not edit the paper files now; record the required updates here. Concept DOI 10.5281/zenodo.21756077; current version v1.1.0 (version DOI 10.5281/zenodo.21859802). Line numbers refer to paper.md at commit 4d514d3. Depends on the six-tier-ontology release that owns the new terms (six-tier-ontology/PENDING_UPDATES.md item 6).

Term rule: the Owner Ontology is the stakeholder ontology of the owner (the tier-1 stakeholder), not a separate kind beside stakeholder ontologies. Name the analyst's structure "six-tier ontology of a business" in full on first use and "six-tier ontology" after it; never bare "business ontology" (gate О4 В, term spec §10).

## 1. Assumption A: the Owner Ontology is replaced with Owner Intent

- Location: "Preliminaries", Assumption A, paper.md line 59, after "exits with the seller-principal."
- Change: state that the Owner Ontology, in which Owner Intent is phrased, is Tier 1 content and is replaced with it; only its shareable part crosses the boundary.
- Proposed text: "The Owner Ontology in which that Intent is phrased is Tier 1 content and is replaced with it: the buyer reads the asset in the buyer's own ontology. Only the shareable part of the seller's Owner Ontology (the seller's terms as used in the records, verbatim, and the list of ontology-dependent records) can cross the boundary, as a document; the private part exits with the seller-principal."
- Version: part of the minor release in item 4.

## 2. Tier record and the replace token

- Location: definition of the tier record, paper.md line 102 ("stated purpose, horizon, and exit criteria at Tier 1"); Tier-1 tokens, line 106.
- Change: (a) add the Owner Ontology to the Tier 1 record content; (b) under *replace*, attach the shareable part as a read-only fork of a document, not a fork of Tier 1. No new token.
- Proposed text (line 102): "stated purpose, horizon, and exit criteria at Tier 1, phrased in the Owner Ontology;"
- Proposed text (line 106, append): "The *replace* token may carry one attachment: a read-only fork of the shareable part of the seller's Owner Ontology, which lets the buyer read the Tier 2 to Tier 6 records that depend on it. The attachment does not transfer the Owner Ontology itself, and its absence leaves those ontology-dependent records forked but unreadable in the seller's sense."
- Version: part of item 4.

## 3. Table 3 notes and boundary conditions

- Location: Table 3 notes, paper.md line 243 ("All six rows share the replace operator at Tier 1"); "Boundary Conditions", second paragraph, line 358.
- Change: (a) in the notes, say what replace leaves behind; (b) in the boundary conditions, separate a record that exists but depends on the Owner Ontology from a record that does not exist (the existing unevaluated case).
- Proposed text (line 243, append): "Replace also leaves the seller's Owner Ontology with the seller; where Tier 2 to Tier 6 records are ontology-dependent, the 1-1 forks carry records the buyer reads only through the shareable part, or translates into its own ontology with loss."
- Proposed text (line 358, append): "A record that exists but whose meaning depends on the seller's Owner Ontology is a third case beside an existing record and an intended one: the predicate has its input, but the buyer's reading of that input depends on whether the shareable part was transferred."
- Version: part of item 4.

## 4. ONTOLOGY.yaml and release

- Location: tier-bundle-algebra/ONTOLOGY.yaml `imports:` (line 41 area); GLOSSARY.md (generated); SPINE.yaml.
- Change: import `owner-ontology`, `owner-ontology-shareable-part`, `owner-ontology-private-part`, `ontology-dependent-records` from 2026ag; regenerate GLOSSARY.md; add the replace-attachment statement of item 2 to SPINE.yaml and regenerate paper.yaml.
- Version: no change to the operators, the cascade rule or the admissibility rules; minor bump v1.1.0 to v1.2.0 (paper.md line 9, CITATION.cff, README, Data and Code Availability version DOI line 384) and a new Zenodo version under concept DOI 10.5281/zenodo.21756077.
