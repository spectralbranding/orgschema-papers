# Pending updates: The Tier-Rotation Curve (2026ai)

Status: pending; raised 2026-10-30; source: decision log dz30#l=11 and #l=15 (ARCHIVE/SMD_raw/Решения_Дмитрия_2026-10-30.md); term spec smd-engine/work/ontology_terms_spec.md (§4, map marking).

Owner instruction (Dmitry, 30.10): do not edit the paper files now; record the required updates here. Concept DOI 10.5281/zenodo.20069605; current version v2.0.0. Line numbers refer to paper.md at commit 4d514d3. Depends on the six-tier-ontology release that owns the new terms (six-tier-ontology/PENDING_UPDATES.md item 6).

Term rule: the Owner Ontology is the stakeholder ontology of the owner (the tier-1 stakeholder), not a separate kind beside stakeholder ontologies.

## 1. Setup: written is not the same as readable

- Location: "Formal Model" > "Setup and Definitions", definition of s, paper.md line 102.
- Change: s counts signal in a substrate the acquirer can own. A Tier-4 artifact written in the founder's Owner Ontology is owned by the acquirer but read correctly only with that ontology. Name ontology-dependence as a second readiness measure beside fusion (1 − s, signal not written at all), without changing the model.
- Proposed text (after the definition of 1 − s): "The complement measures fusion: signal that has not been written into any separable substrate. A second, distinct measure is ontology-dependence: the share d of Tier-4 records that are written but whose meaning depends on the founder's Owner Ontology, the stakeholder ontology of the controlling principal. Such records count in s, since the acquirer owns them, but an acquirer without the shareable part of the Owner Ontology reads them in its own terms. The model treats d as zero; a brand with high s and high d is further along the rotation path than it is separable in practice."
- Version: part of the minor release in item 4.

## 2. Symbolic rotation and founder-language salience

- Location: "Decoupling: Substantive Versus Symbolic", paper.md line 94; Table 1 notes, line 88.
- Change: one form of symbolic rotation is codification written in the founder's own terms: brand guidelines exist but use the founder's vocabulary in senses only the founder fixes. Founder-language salience (Table 1) is a partial proxy for d as well as for 1 − s.
- Proposed text (line 94, append): "A second signature of apparent rotation is codification in the founder's own terms: guidelines and specifications exist, but their key terms carry meanings fixed in the founder's Owner Ontology and not written down. Such records are ontology-dependent; they raise measured s without raising what a buyer can read."
- Proposed text (line 88, append): "Founder-language salience also bears on ontology-dependence: a high share of founder-attributed terms in written specifications indicates records that depend on the Owner Ontology even where they exist."
- Version: part of item 4.

## 3. Scope conditions, succession, validation

- Location: "Scope Conditions", substrate-fragility paragraph, paper.md line 328; Table 6 row "Succession", line 373; "Formal Validation Agenda", Priority 1, line 422.
- Change: (a) list ontology-dependence as a second axis beside fragility, not modelled; (b) in succession the successor needs the shareable part and, by the founder's choice, part of the private part, while the M&A buyer needs only the shareable part; (c) add a measurement note.
- Proposed text (line 328, new sentence at the end of the paragraph): "Ontology-dependence is a further axis not modelled: the share of written Tier-4 records readable only through the founder's Owner Ontology, which the shareable part of that ontology lowers and which s does not register."
- Proposed text (Table 6 notes, append): "At M&A exit the buyer needs only the shareable part of the founder's Owner Ontology to read the records it acquires; at succession the successor needs it as well, and also whatever part of the private Owner Ontology the founder chooses to pass on."
- Proposed text (Priority 1, append): "Where specification documents are available, code the share of their key terms that are defined only by the founder's usage, as a first proxy for d."
- Version: part of item 4.

## 4. ONTOLOGY.yaml and release

- Location: tier-rotation/ONTOLOGY.yaml (`tier-4-share` entry at line 24; `imports:` at line 41 area); GLOSSARY.md (generated); SPINE.yaml.
- Change: import `owner-ontology`, `owner-ontology-shareable-part`, `ontology-dependent-records` from 2026ag; optionally add a relation note on `tier-4-share` ("contrasts: ontology-dependent-records; written versus readable"); regenerate GLOSSARY.md; add the second readiness measure to SPINE.yaml and regenerate paper.yaml.
- Version: equation 1, V(s) and P1-P5 unchanged; minor bump v2.0.0 to v2.1.0 (paper.md line 9, CITATION.cff, README) and a new Zenodo version under concept DOI 10.5281/zenodo.20069605. If the author instead adds d to V(s), that changes the model and calls for a major bump (v3.0.0).
