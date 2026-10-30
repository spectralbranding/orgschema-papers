# Pending updates: Capability as Projection (2026al, Append-Only Organizational Log)

Status: pending; raised 2026-10-30; source: decision log dz30#l=11 and #l=15 (ARCHIVE/SMD_raw/Решения_Дмитрия_2026-10-30.md); term spec smd-engine/work/ontology_terms_spec.md (§2, §4, §6).

Owner instruction (Dmitry, 30.10): do not edit the paper files now; record the required updates here. Concept DOI 10.5281/zenodo.20367459; current version v1.1.0 (version DOI 10.5281/zenodo.20939874, checked on Zenodo 2026-10-30). Line numbers refer to paper.md at commit 4d514d3. Depends on the six-tier-ontology release that owns the new terms (six-tier-ontology/PENDING_UPDATES.md item 6).

Term rule: the Owner Ontology is the stakeholder ontology of the owner (the tier-1 stakeholder), not a separate kind beside stakeholder ontologies. Name the analyst's structure "six-tier ontology of a business" in full on first use and "six-tier ontology" after it; never bare "business ontology" (gate О4 В, term spec §10).

## 1. The event log L is written in the Owner Ontology

- Location: "The Event-Sourced View" > "The Event Log L", paper.md line 82 (after the description of the event tuple).
- Change: say in whose terms event payloads are written, and separate this from the taxonomy T.
- Proposed text: "Event payloads are written in the terms of the position that records them. In an owner-operated firm most of the log is written in the Owner Ontology, the stakeholder ontology of the controlling principal: what counts as an asset, a customer, a good deal, a risk. The taxonomy T classifies events from the analyst's position; it does not translate their payloads."
- Version: part of the minor release in item 6.

## 2. The query space Q is worded in an ontology

- Location: "The Projection Operator π", definition of Q, paper.md line 92.
- Change: add that each query is worded in some stakeholder ontology; the owner's queries are worded in the Owner Ontology and selected by Owner Intent. This places π in the chain Owner Ontology -> Owner Intent (Q) -> log L -> visible capability C.
- Proposed text: "Each query q is worded in some stakeholder ontology. The controlling principal's queries are worded in the Owner Ontology, and Owner Intent decides which of them are asked; the Owner Ontology decides how they are worded."
- Version: part of item 6.

## 3. Determinism (O2) and ontology-dependent records

- Location: "Determinism conditional on log (O2)", paper.md line 96, last sentence.
- Change: add a fourth source of evaluator disagreement and name ontology-dependent records.
- Proposed text (replace the last sentence): "If different evaluators produce different claims, either the log is incomplete, the query is under-specified, one or both evaluators read non-log state, or the evaluators read the payloads in different ontologies. Records whose meaning depends on the Owner Ontology (ontology-dependent records) satisfy O2 only for evaluators who have its shareable part: the owner's terms as used in the records, verbatim, and the list of such records."
- Version: part of item 6.

## 4. Compatibility κ and log transfer: conflicts of terms

- Location: "The Compatibility Function κ", conflict examples, paper.md line 115; "Snapshots and Renderings", paper.md line 121.
- Change: (a) add term conflicts to the conflict sources: the same term defined differently in the two parties' Owner Ontologies. (b) A log transferred without the shareable part of the Owner Ontology behaves in part like a snapshot: ontology-dependent records are present but cannot answer new queries correctly.
- Proposed text (line 115, append to the list of conflict sources): "or incompatible terms (the two Owner Ontologies define the same noun, such as 'customer' or 'quality', differently)."
- Proposed text (line 121, append): "A log handed over without the shareable part of the Owner Ontology is between the two: its records are present, but its ontology-dependent records can be re-rendered only in the buyer's own terms, which is a translation with loss."
- Version: part of item 6.

## 5. Imitation (P4), limitations and future research

- Location: P4 paragraph, paper.md line 147; "Limitations" > "Schema evolution", line 263; "Future Research", line 277.
- Change: (a) P4: with the same reader π, the edge moves to L, to Q and to the ontology in which L is written and Q is asked; the ontology can be imitated, the log cannot (term spec §6). (b) Schema evolution: a change of Owner Ontology over time is the owner-side form of schema drift. (c) Add a fourth extension.
- Proposed text (after P4 falsification): "An imitator who adopts the canonical firm's Owner Ontology without its log still fails on novel q': an ontology can be copied, since people move and terms spread, while a log cannot. Durability of the edge therefore orders log, then ontology, then reader."
- Proposed text (line 263, append): "The owner-side form of the same drift is a change of the Owner Ontology itself: the terms in which events are written change meaning."
- Proposed text (line 277, append): "and the stakeholder ontologies, the Owner Ontology among them, in which the log is written and the queries are asked."
- Version: part of item 6.

## 6. ONTOLOGY.yaml and release

- Location: capability-as-projection/ONTOLOGY.yaml `imports:` (line 41 area); GLOSSARY.md (generated); SPINE.yaml.
- Change: import `owner-ontology`, `stakeholder-ontology`, `owner-ontology-shareable-part`, `ontology-dependent-records` from 2026ag; regenerate GLOSSARY.md; add the claim of item 5(a) to SPINE.yaml and regenerate paper.yaml.
- Version: no proposition changes; minor bump v1.1.0 to v1.2.0 (paper.md line 9, CITATION.cff, README) and a new Zenodo version under concept DOI 10.5281/zenodo.20367459.
