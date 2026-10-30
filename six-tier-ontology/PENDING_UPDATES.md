# Pending updates: Six-Tier Ontology (2026ag, Dual Hierarchies of Organizational Transferability)

Status: pending; raised 2026-10-30; source: decision log dz30#l=11 and #l=15 (ARCHIVE/SMD_raw/Решения_Дмитрия_2026-10-30.md); term spec smd-engine/work/ontology_terms_spec.md.

Owner instruction (Dmitry, 30.10): do not edit the paper files now; record the required updates here. Concept DOI 10.5281/zenodo.19895813; current version v1.3.0. Line numbers refer to paper.md at commit 4d514d3.

Term rule for every item: the owner is the tier-1 stakeholder, so the Owner Ontology is the stakeholder ontology of the owner. Write "stakeholder ontologies, the Owner Ontology among them", never "owner and stakeholder ontologies" as two kinds. Name the analyst's structure "six-tier ontology of a business" in full on first use and "six-tier ontology" after it; never bare "business ontology" (gate О4 В, term spec §10).

## 1. Tier 1 definition: Owner Intent is phrased in the Owner Ontology

- Location: "The Six-Tier Ontology" > "Tier 1 — Owner Intent", first paragraph, paper.md line 64.
- Change: after the second sentence, state that Owner Intent is phrased in the Owner Ontology and that the Owner Ontology is Tier 1 content, not a seventh tier.
- Proposed text: "Owner Intent is phrased in the Owner Ontology: the controlling principal's account of what exists in the business, what its basic terms mean, what is connected to what, and what is absent. The Owner Ontology is the stakeholder ontology of the tier-1 stakeholder. It is Tier 1 content carried by the same principal and not a seventh tier: the Owner Ontology fixes the terms in which questions about the business are worded, and Owner Intent fixes which questions are asked."
- Version: part of the minor release in item 7.

## 2. Table 1 notes: no new row

- Location: Table 1, row 1 (paper.md line 53) and its notes (line 60).
- Change: keep six rows. Add one sentence to the notes. Optional: extend the Tier 1 specification-surface cell.
- Proposed text (notes): "The Owner Ontology, in which Owner Intent is phrased, is Tier 1 content and has no row of its own. Every stakeholder of the business (owner, managers, employees, customers, lenders, regulators, a buyer or successor) has a stakeholder ontology of it, the Owner Ontology among them; the six-tier ontology of a business is the common language into which these stakeholder ontologies are translated."
- Optional cell text (Tier 1, Specification Surface): "Stated purpose + time horizon + exit criteria, phrased in the Owner Ontology".
- Version: part of item 7.

## 3. Attribution refinement and Figure 1: what exits with the principal

- Location: "Attribution refinement" paragraph, paper.md line 68 (after "it exits with the principal."); Figure 1 notes, line 92.
- Change: the Owner Ontology attaches to the principal and exits with the principal, as Owner Intent does; but Tiers 2-6 records were written in its terms. Name the split into a shareable part and a private part.
- Proposed text (line 68): "The same applies to the Owner Ontology in which that Intent is phrased, with one qualification. Records on Tiers 2 through 6 were written in its terms, and some of them, the ontology-dependent records, cannot be read correctly without it. The Owner Ontology therefore divides into a shareable part (the owner's terms as used in the records, verbatim, and the list of ontology-dependent records), which can pass to a buyer or successor as a document, and a private part (deliberate absences, causal beliefs, sources of the edge, values), which generates future records and stays with the principal unless the principal chooses to pass it on."
- Proposed text (line 92, append): "The Owner Ontology sits with Owner Intent on the principal substrate; only its shareable part can cross to the asset side, as a document."
- Version: part of item 7.

## 4. Separability diagnostic: a second readiness reading (author decision)

- Location: "The Six-Question Diagnostic", Table 4 row "1 Intent" (paper.md line 291) and the paragraph "How to read the profile" after the table notes.
- Change: keep the six questions. Add a note that the Fused / Partial / Independent states measure whether records exist outside the owner's head (fusion); they do not measure whether written records can be read without the Owner Ontology. The share of ontology-dependent records is a second readiness measure beside fusion.
- Proposed text (Table 4 notes, append): "A tier can be Independent in the sense of the diagnostic and still depend on the Owner Ontology: its records are written but use the owner's terms in senses a reader outside the firm does not share. The share of such ontology-dependent records is a second readiness measure beside fusion, and the shareable part of the Owner Ontology is the instrument that lowers it."
- Version: part of item 7.

## 5. Limitations: multi-principal configurations

- Location: "Limitations" > "Multi-principal Intent configurations", paper.md line 332.
- Change: one sentence that co-principals may have different stakeholder ontologies, not only different intents.
- Proposed text (append): "Dispersed ownership also multiplies ontologies: co-principals may word the same Intent in different stakeholder ontologies, and the framework as stated assumes a single Owner Ontology."
- Version: part of item 7.

## 6. ONTOLOGY.yaml, GLOSSARY.md, SPINE.yaml

- Location: six-tier-ontology/ONTOLOGY.yaml, `owns:` list (after `tier-1-owner-intent`); GLOSSARY.md (generated); SPINE.yaml (paper.yaml is generated from it).
- Change: add five owned terms, each with EN and RU canonical forms (RU and EN change together):
  - `stakeholder-ontology`: "stakeholder ontology" (RU: онтология стейкхолдера). A picture of what exists in an activity, what its basic terms mean, what is connected to what, and what is absent, as written from one named position (owner, manager, employee, customer, lender, regulator, buyer, successor), recorded in that position's own words.
  - `owner-ontology`: "Owner Ontology" (RU: онтология собственника). The stakeholder ontology of the controlling party (the tier-1 stakeholder); the terms in which Owner Intent is phrased and most of the firm's records are written. Tier 1 content, not a seventh tier. Relation: specializes `stakeholder-ontology`; part of `tier-1-owner-intent`.
  - `owner-ontology-shareable-part`: "shareable part" (RU: передаваемая часть онтологии собственника). The reading key to existing records: the owner's terms as used in records, verbatim, and the list of ontology-dependent records. Can pass to a buyer (data room) or successor.
  - `owner-ontology-private-part`: "private part" (RU: закрытая часть онтологии собственника). What generates future records: deliberate absences, causal beliefs, sources of the edge, values, judgement of people. Stays with the owner; passes to a successor only by the owner's choice.
  - `ontology-dependent-records`: "ontology-dependent records" (RU: записи, зависимые от онтологии собственника). Records whose meaning depends on the Owner Ontology; their share is a readiness measure beside fusion.
- Optional: extend the `tier-1-owner-intent` definition with "Phrased in the Owner Ontology." This changes its content hash and so touches every module that imports it (tier-bundle-algebra, succession-rotation, tier-rotation and others) at the next regeneration.
- Naming (gate О4 В, term spec §10): keep `term_key: six-tier-ontology` and `canonical_form: "six-tier ontology"` as the short form; add the full form "six-tier ontology of a business" (RU: шестиуровневая онтология бизнеса) to its definition, to set it apart from a stakeholder ontology, which is a business's own ontology as one position writes it. Bare "business ontology" is not used.
- Then: regenerate GLOSSARY.md (do not hand-edit); add the Tier 1 content claim of item 1 to SPINE.yaml and regenerate paper.yaml with code/generate_paper_yaml.py.
- Version: part of item 7.

## 7. Release

- Change: items 1-6 add a construct without changing any proposition: minor bump v1.3.0 to v1.4.0. Update paper.md line 9, CITATION.cff `version` and `date-released`, the README badge and the root README table; publish a new Zenodo version under concept DOI 10.5281/zenodo.19895813.
- Order: release this paper first; the other five PENDING_UPDATES.md files import the new terms from 2026ag.
