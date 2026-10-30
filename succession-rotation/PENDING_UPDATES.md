# Pending updates: Preparing to Sell and Preparing to Hand Over Are Rival Investments (2026bm, succession-rotation)

Status: pending; raised 2026-10-30; source: decision log dz30#l=11 and #l=15 (ARCHIVE/SMD_raw/Решения_Дмитрия_2026-10-30.md); term spec smd-engine/work/ontology_terms_spec.md (§4).

Owner instruction (Dmitry, 30.10): do not edit the paper files now; record the required updates here. Concept DOI 10.5281/zenodo.21868658; current version v1.0.0 (version DOI 10.5281/zenodo.21868659). Line numbers refer to paper.md at commit 4d514d3. Depends on the six-tier-ontology release that owns the new terms (six-tier-ontology/PENDING_UPDATES.md item 6).

Term rule: the Owner Ontology is the stakeholder ontology of the owner (the tier-1 stakeholder), not a separate kind beside stakeholder ontologies.

## 1. Carriers: the Owner Ontology splits between A and P

- Location: "The Persistence Column" > "Three modes of persistence", Artifact continuity (A), paper.md line 55, and Person continuity (P), line 57.
- Change: the paper classifies components by carrier. The Owner Ontology is a Tier 1 component that splits: its shareable part is carried by an artifact, its private part by the person. Owner Intent stays under P.
- Proposed text (line 55, append): "The shareable part of the Owner Ontology, the owner's terms as used in the records, verbatim, and the list of ontology-dependent records, once written down."
- Proposed text (line 57, append): "The private part of the Owner Ontology: deliberate absences, causal beliefs, sources of the edge, values and judgement of people, which generate the firm's future records."
- Version: part of the minor release in item 4.

## 2. Successor versus buyer

- Location: "Which Tier Binds" > "What replacement leaves intact", P3 and the paragraph after it, paper.md lines 71-73; Table 1 discussion, line 81.
- Change: the two events need different parts. Under removal (buyer with its own operating principal), the buyer needs the shareable part only to read the records it buys and then works in its own ontology; the private part is written off with the other person-carried components. Under replacement (succession), the successor needs the shareable part to read the records and, to produce new records in the same way, as much of the private part as the owner chooses to pass on, which is acquired by exposure, not by documents.
- Proposed text (after line 73): "The Owner Ontology divides the same way. A buyer supplying its own principal needs its shareable part only to read the records it acquires; it then works in its own ontology, and the private part is written off with the rest of the person-carried column. A successor needs the shareable part for the same reason and, beyond it, the part of the private Owner Ontology the incumbent chooses to pass on, which only exposure transfers."
- Version: part of item 4.

## 3. Budget constraint (P6): writing the shareable part is codification

- Location: "The Budget Constraint", P6, paper.md line 142.
- Change: one sentence placing the two parts on the two sides of the trade-off. Writing the shareable part converts person-carried residual into artifact and serves both events; passing the private part to a successor is exposure and serves only succession.
- Proposed text (after P6): "Writing the shareable part of the Owner Ontology is the one codification that serves both arms, because both a buyer and a successor must read the existing records; passing on its private part is exposure and serves only the succession arm."
- Version: part of item 4.

## 4. ONTOLOGY.yaml and release

- Location: succession-rotation/ONTOLOGY.yaml (`persistence-mechanism`, `person-carried-residual`, `documentation-coverage` entries; `imports:` at line 142 area); GLOSSARY.md (generated); SPINE.yaml.
- Change: import `owner-ontology`, `owner-ontology-shareable-part`, `owner-ontology-private-part`, `ontology-dependent-records` from 2026ag; optionally add a note on `documentation-coverage` that it includes the shareable part; regenerate GLOSSARY.md; add the statement of item 3 to SPINE.yaml and regenerate paper.yaml.
- Version: P1-P10 unchanged; minor bump v1.0.0 to v1.1.0 (paper.md line 9, CITATION.cff, README, Data and Code Availability version DOI line 342) and a new Zenodo version under concept DOI 10.5281/zenodo.21868658.
