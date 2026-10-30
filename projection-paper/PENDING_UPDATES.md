# Pending updates: The Projection Cascade (2026m)

Status: pending; raised 2026-10-30; source: decision log dz30#l=11 and #l=15 (ARCHIVE/SMD_raw/Решения_Дмитрия_2026-10-30.md); term spec smd-engine/work/ontology_terms_spec.md (§3 rule, §5).

Owner instruction (Dmitry, 30.10): do not edit the paper files now; record the required updates here. Concept DOI 10.5281/zenodo.19145205; current version v2.1.0. Line numbers refer to paper.md at commit 4d514d3. Depends on the six-tier-ontology release that owns the new terms (six-tier-ontology/PENDING_UPDATES.md item 6).

Term rule: the Owner Ontology is the stakeholder ontology of the owner (the tier-1 stakeholder), not a separate kind beside stakeholder ontologies.

## 1. A translation step before T_1

- Location: "The Projection Cascade" > "Six-Tier Vector-Space Construction", after the composite cascade Π, paper.md line 116-118.
- Change: name the step that precedes the cascade. A stakeholder ontology is recorded in the position's own words; its translation into the six-tier ontology is a separate rank-reducing map with its own kernel, of the same kind as each junction Π_{i→i+1}.
- Proposed text: "The cascade starts from T_1 as already written in the six-tier ontology. In practice T_1 content is first stated in a stakeholder ontology, for the controlling principal the Owner Ontology, in that position's own words. Let O_s be that content space and Θ_s: O_s → T_1 the translation into the six-tier ontology, with nullity r_0 = dim(O_s) − rank(Θ_s). Θ_s is a lossy step of the same kind as each junction: what lies in its kernel is absent from every tier below."
- Version: part of the minor release in item 4.

## 2. Corollary 1 extended by r_0

- Location: Corollary 1, paper.md line 227 and the paragraph after the proof, line 247.
- Change: state the bound for the extended cascade Π ∘ Θ_s. The kernel sub-additivity argument carries over unchanged, so this is a remark, not a new theorem.
- Proposed text: "For the extended cascade Π ∘ Θ_s, the same sub-additivity gives dim ker(Π ∘ Θ_s) ≤ r_0 + r_1 + ... + r_5. Content of the Owner Ontology that the six-tier ontology has no coordinate for is lost before the first junction, and no intervention at T_2 to T_6 recovers it."
- Version: part of item 4.

## 3. Boundary conditions and future research

- Location: "Boundary conditions and what the cascade does not explain", "Static-frame applicability", paper.md line 420; "Future research", line 438-450.
- Change: (a) ownership change replaces the Owner Ontology as well as Owner Intent, so Θ_s changes with the principal; (b) add a research direction on measuring r_0 and on translation into other stakeholder ontologies (customers, regulators, employees), without which a new ontology has no market.
- Proposed text (line 420, append): "Ownership change also replaces Θ_s: the incoming principal reads T_1 to T_6 through a different Owner Ontology, and records written in the prior one become ontology-dependent."
- Proposed text (new item in "Future research"): "*Translation between ontologies.* Stakeholder ontologies, the Owner Ontology among them, enter the cascade through a translation Θ_s whose nullity r_0 is not measured here. Eliciting a stakeholder ontology in the position's own words and comparing it with its six-tier rendering would measure r_0 directly, and the same comparison applies to the translations a new Owner Ontology needs into customers', regulators' and employees' ontologies."
- Version: part of item 4.

## 4. ONTOLOGY.yaml and release

- Location: projection-paper/ONTOLOGY.yaml `imports:`; GLOSSARY.md (generated); SPINE.yaml.
- Change: import `stakeholder-ontology`, `owner-ontology`, `ontology-dependent-records` from 2026ag; regenerate GLOSSARY.md; add the remark of item 2 to SPINE.yaml and regenerate paper.yaml.
- Version: propositions P1-P4 unchanged; minor bump v2.1.0 to v2.2.0 (paper.md line 9, CITATION.cff, README) and a new Zenodo version under concept DOI 10.5281/zenodo.19145205.
