# PENDING_UPDATES — Organizational Schema Theory (2026i)

Pending updates queued while paper.md is under journal review.

## Phase 1 alignment audit (2026-04-30)

Status: queued — not applied because paper is under TQM Journal review.

### Dimension order in §SBT-as-test-specification

**Issue**: the OST passage describing "SBT as test specification language" enumerates the eight SBT dimensions as `experiential, semiotic, temporal, ideological, narrative, cultural, social, economic`. This is the only place in the 35-paper SBT/OST corpus where the dimensions are listed in non-canonical order.

**Canonical order** per `CLAUDE.md` (project root) and the other 24 dimension-bearing corpus papers:

> Semiotic, Narrative, Ideological, Experiential, Social, Economic, Cultural, Temporal

**Recommended fix on next revision**: reorder the dimension list to canonical order. No theoretical claim depends on the order — the passage is purely descriptive.

**Source**: `audit/reports/01_alignment_2026i.md` in spectral-branding repo.

## Phase 2 Audit Findings (2026-04-30)

Status: queued — not applied because paper is under TQM Journal review.

### Tables missing `*Notes*:` italic block

Per `PAPER_QUALITY_STANDARDS.md` (in spectral-branding repo), every table must carry an italic `*Notes*:` block immediately below it. Phase 2 mechanical audit found 8 of 10 tables in `paper.md` missing this block. Only Table 4 (typst-rendered) currently complies.

| Caption | Line | Action |
|---|---|---|
| Table 1: The TDD-to-Orgschema Parallel | 39 | Add `*Notes*:` block below |
| Table 2: Forward Design vs. Reverse Design | 56 | Add `*Notes*:` block below |
| Table 3: Framework Lineage and Orgschema's Contribution | 90 | Add `*Notes*:` block below |
| Table 5: CI/CD Validation Levels | 283 | Add `*Notes*:` block below |
| Table 6: Six-Level Orgschema Maturity Model | 298 | Add `*Notes*:` block below |
| Table 7: LLM Impact on Orgschema Feasibility (Theoretical Comparison) | 319 | Add `*Notes*:` block below |
| Table 8: Executor Swap Impact Analysis (Illustrative Scenario) | 383 | Add `*Notes*:` block below |
| Table 9: Orgschema to Viable System Model Mapping | 446 | Add `*Notes*:` block below |
| Table 10: Three Fork Types | 491 | Add `*Notes*:` block below |

(Table 4's two following prose paragraphs serve as inline qualifications rather than a formal `*Notes*:` block — see Phase 3 judgment call J3; do NOT add a Notes block to Table 4. All other 9 tables need the Notes block. Total: 9 tables to fix.)

**Source**: `audit/reports/02_mechanical_2026i.md` and `audit/reports/02_mechanical_report.md` (M5) in spectral-branding repo.

## Phase 3a Structural Audit (2026-05-01)

Status: queued — not applied because paper is under TQM Journal review.

**Source**: `audit/reports/03a_structural_2026i.md` in spectral-branding repo.

### Abstract: first-person "We" (project standard — queue for next revision)

Two sentences in the abstract use first-person "we":
- "We present the methodology as a Design Science Research artifact..."
- "We further argue that large language models are an essential enabler..."

PAPER_QUALITY_STANDARDS §C21 requires third-person abstract. On next revision, convert to: "The authors present..." / "The authors further argue..." or rephrase as "This paper argues..."

### Introduction ¶3 TDD cascade near-verbatim in Conclusion ¶1 (minor redundancy)

The five-sentence TDD-level-mapping (line 21) is near-verbatim to Conclusion ¶1 (line 521). The Conclusion version is superior (adds "regulatory constraints and organizational commitments"). On next revision, consider trimming Introduction ¶3 to a single bridging sentence, saving ~40 words.

### Footnote 11 SBT title does not match canonical (LOW priority)

Footnote 11 (line 549) cites: "Spectral Brand Theory: A Computational Framework for Multi-Dimensional Brand Perception."
Canonical entry in `CANONICAL_REFERENCES.md`: "Spectral Brand Theory: A multi-dimensional framework for brand perception analysis."
DOI is correct (10.5281/zenodo.18945912). Before applying, verify actual title against the live Zenodo record — the canonical file may also need updating.

### `0.85` leading zero — project standard

Line 485: "Apple's 0.85 digital dominance" — should be `.85` per PAPER_QUALITY_STANDARDS §A2 (no leading zero for proportions bounded in [0,1]). Low priority.

### Future Research paragraph: 128-word run-on sentence

Line 517: five research directions combined in one semicolon-separated sentence. On next revision, break into a bulleted list or split into 2–3 sentences. Improves readability and aligns with TQM Journal conventions for the Limitations/Future Research section.

### Illustrative value qualifier missing at second mention

Line 430 (Evaluation Results) refers to "the 15% perceived profile degradation from human-to-automated execution" without restating the illustrative qualifier present in Table 8's heading and in line 392. On next revision, add "(illustrative)" or a parenthetical to prevent a reviewer reading the Evaluation section in isolation from interpreting this as an empirical finding.

### Spectra Coffee hypothetical status (clarification recommended)

Line 335 introduces Spectra Coffee without stating it is a purpose-built demonstration rather than a real operating business. On next revision, add "purpose-built demonstration of a" or similar qualifier at first mention, unless Spectra Coffee is in fact a real business that served as the case study (in which case the current text is accurate).

## Phase 3 Literature Review — External Positioning Audit (2026-05-01)

Status: queued — not applied because paper is under TQM Journal review.

Source: `audit/reports/03_review_literature_2026i.md` in spectral-branding repo.

### Priority 1 — TQM Journal venue-specific citations (highest impact on review outcome)

**L-P1-A: Add Juran (1988) in §Theoretical Foundations or §Introduction quality-management lineage.**
Juran's "fitness for use" quality criterion is the customer-defined quality concept most directly parallel to orgschema's L0 acceptance tests. TQM Journal reviewers will notice the absence of Juran given the paper's quality-management framing. One sentence: "Juran (1988) defined quality as 'fitness for use' — the customer-referenced criterion that orgschema implements as Level 0 acceptance tests specifying the exact customer experience outcomes against which all lower-level specifications are validated."
Citation: Juran, J. M. (1988). *Juran on Planning for Quality*. Free Press.

**L-P1-B: Add Crosby (1979) in §TDD as Design Methodology.**
Crosby's "do it right the first time" / zero-defects discipline is the quality-management ancestor of TDD's "write tests before code" discipline. One sentence connecting the two strengthens the TDD-as-quality-methodology framing.
Citation: Crosby, P. B. (1979). *Quality Is Free: The Art of Making Quality Certain*. McGraw-Hill.

**L-P1-C: Add Feigenbaum (1983) in §Introduction or §Positioning Against Prior Art.**
Feigenbaum's Total Quality Control as whole-organization responsibility is the organizational scope precedent for orgschema's six-level cascade spanning sourcing to customer experience.
Citation: Feigenbaum, A. V. (1961/1983). *Total Quality Control*. McGraw-Hill.

**L-P1-D: Add formal ISO 9001:2015 citation wherever the standard is invoked.**
The standard is referenced three times by name (lines ~404, ~428, footnote [^24]) but never formally cited. TQM Journal will expect a formal citation.
Citation: ISO. (2015). *ISO 9001:2015: Quality Management Systems — Requirements*. International Organization for Standardization.

**L-P1-E: Add Six Sigma citation at line 107 (§Positioning Against Prior Art).**
Six Sigma is named in the preemptive QFD+Six Sigma+ERP rebuttal but no Six Sigma source is cited. TQM Journal reviewers who publish Six Sigma research will mark this gap.
Citation: Pyzdek, T., & Keller, P. (2014). *The Six Sigma Handbook*, 4th ed. McGraw-Hill. (or Harry, M. J., & Schroeder, R. (2000). *Six Sigma*. Currency.)

### Priority 2 — Organization design anchors (theoretical grounding)

**L-P2-A: Add Simon (1947) *Administrative Behavior* in §Introduction or §Theoretical Foundations.**
Simon's bounded rationality is the cognitive-limit foundation for why hierarchical specification is necessary — the intellectual origin of the six-level cascade argument.
Citation: Simon, H. A. (1947). *Administrative Behavior*. Free Press.

**L-P2-B: Add Mintzberg (1979) *The Structuring of Organizations* in §Implications for Operations Management.**
Mintzberg's "standardization of outputs" coordination mechanism is the organizational-design name for what L2 process contracts implement. One sentence connecting the two closes a positioning gap that any organizational behavior reviewer will notice.
Citation: Mintzberg, H. (1979). *The Structuring of Organizations*. Prentice Hall.

**L-P2-C: Add Williamson (1975) *Markets and Hierarchies* in §Introduction or §Positioning Against Prior Art.**
Williamson's incomplete-contracts argument is the economic-theory companion to orgschema's "maximum testability within feasible specification space" framing. One sentence: "Williamson (1975) established that complete specification is impossible under bounded rationality and opportunism; orgschema accepts this constraint and redirects the design problem from completeness to traceability and automated validation."
Citation: Williamson, O. E. (1975). *Markets and Hierarchies*. Free Press.

**L-P2-D: Add Zachman (1987) differentiation in §Positioning Against Prior Art or §Introduction footnote.**
IS/DSR reviewers will compare orgschema to Zachman's framework. One sentence differentiating: "Unlike Zachman's (1987) classification framework, which organizes what aspects of organizational knowledge need to be documented, orgschema specifies how each parameter traces to a customer experience justification and automates validation of that traceability."
Citation: Zachman, J. A. (1987). "A Framework for Information Systems Architecture." *IBM Systems Journal* 26(3): 276–292.

### Priority 3 — Literature completeness for higher-tier venue migration

**L-P3-A: Add Ashby (1956) requisite variety in §VSM mapping.**
Beer's VSM is cited; citing Ashby (Beer's theoretical foundation) allows a one-sentence grounding: "the cascade must carry requisite variety at each level to absorb the complexity the level faces (Ashby 1956)."
Citation: Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall.

**L-P3-B: Replace unverifiable [^7] with Dumas et al. (2018).**
The Cespedes/Reijers/Mendling [^7] reference could not be verified (flagged in 03b). Dumas et al. 2018 supports the same claim (organization-as-code exists for cloud infrastructure but not full business ontologies) and is verified.
Citation: Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018). *Fundamentals of Business Process Management*, 2nd ed. Springer.

**L-P3-C: Add Raymond (2001) in §Organizational Openness.**
Raymond's bazaar model is the open-source precedent for orgschema's Level 4 (Open Core) openness level. One sentence.
Citation: Raymond, E. S. (2001). *The Cathedral and the Bazaar*. O'Reilly.

**L-P3-D: Add von Hippel (2005) in §Rethinking Franchises.**
Von Hippel's sticky-information argument explains why franchises traditionally share procedures rather than test suites, making orgschema's contract-procedure separation non-trivial.
Citation: von Hippel, E. (2005). *Democratizing Innovation*. MIT Press.

**L-P3-E: Add Hammer & Champy (1993) differentiation in §Reverse Design.**
BPR is the closest management-practice precedent for reverse design. One differentiating sentence: "narrative redesign methodology vs. machine-readable specification cascade."
Citation: Hammer, M., & Champy, J. (1993). *Reengineering the Corporation*. HarperBusiness.

**L-P3-F: Add BPMN formal citation in Table 4.**
BPMN is listed as a comparison methodology in Table 4 but not formally cited.
Citation: Object Management Group. (2014). *Business Process Model and Notation (BPMN) 2.0 Specification*. OMG Document formal/2013-12-09.

**L-P3-G: Add a recent LLM-for-BPM citation in §LLM as Essential Enabler / Table 7.**
Bommasani et al. [^25] (2021) is the only empirical grounding for Table 7's LLM capability claims. A 2023–2026 citation demonstrating LLMs performing BPM-relevant tasks (process specification, compliance checking) would tighten the "essential enabler" claim.
Candidate: van der Aa, H., Di Ciccio, C., Leopold, H., & Reijers, H. A. (2023). "Extracting Declarative Process Models from Natural Language." *Information Systems* 116. (Verify before use.)

## Phase 3b Bibliography Audit (2026-05-01)

Status: queued — not applied because paper is under TQM Journal review.

Source: `audit/reports/03b_bibliography_2026i.md` in spectral-branding repo. 21 bibliographic footnotes verified; 4 verified-with-corrections; 1 unverifiable.

### B-1: [^11] self-cite — subtitle mismatch with canonical SBT title

Footnote [^11] subtitle is "A Computational Framework for Multi-Dimensional Brand Perception"; canonical title in CANONICAL_REFERENCES.md is "A multi-dimensional framework for brand perception analysis." DOI is correct (10.5281/zenodo.18945912). Verify the live Zenodo record before applying — the canonical file may itself need updating.

### B-2: [^6] Pesic & van der Aalst 2006 — missing fields

Add LNCS volume `4103`, pages `169–180`, and DOI `10.1007/11837862_18` to footnote [^6]. Other fields correct.

### B-3: [^12] Mullarkey & Hevner 2019 — missing third author

Add **Pär J. Ågerfalk** as third author. Add DOI `10.1080/0960085X.2018.1451811`. The eDSR citation appears in the Methodology section and will be scrutinized closely by DSR reviewers.

### B-4: [^22] Chesbrough & Appleyard 2007 — wrong second author first name

Second author is **Melissa M. Appleyard**, not "Wim Appleyard". DOI 10.2307/41166416 is correct. Substantive factual error; correct before any R&R revision.

### B-5: [^7] Cespedes/Reijers/Mendling 2019 — UNVERIFIABLE

Neither Perplexity nor Gemini could verify this reference (Information and Software Technology vol. 116, 2019). Recommend REPLACE with Dumas et al. (2018) *Fundamentals of Business Process Management* (2nd ed., Springer), which supports the same claim and shares an author with [^7]. Already entered as L-P3-B above. Appended to `audit/MANUAL_VERIFICATION_QUEUE.md`.

## Phase 3c Contribution & Cross-Corpus Audit (2026-05-01)

Status: queued — not applied because paper is under TQM Journal review.

Source: `audit/reports/03c_contribution_2026i.md` in spectral-branding repo.

### C-1: Add explicit "this paper makes three contributions" enumerated paragraph in §Introduction

Anchor on (a) TDD-as-organizational-design generalization, (b) six-level maturity model, (c) executor-swap and three-fork forkability taxonomy. Currently the contribution is conveyed across §1 and §Theoretical Foundations rather than crystallized as a single bullet block. AMR-tier reviewers reject this; TQM reviewers tolerate it; adding it improves landing probability at venue migration.

### C-2: Add "Subsequent Theoretical Development" paragraph at head of §Future Research

OST is the seed paper for the entire OST family but cites only 2026a (SBT, footnote [^11]). Five sibling/downstream OST-family papers need forward-pointers:

- **2026h (R5, OST impossibility)** at §Methodology or §Future Research — supplies the geometric-impossibility foundation for the cascade-and-fork compression argument that orgschema asserts qualitatively. Recommended placement: end of §Methodology.
- **2026ae (Verification as Operator)** at §"Just Documentation" Rebuttal — proves orgschema's full-rank multi-level cascade is algebraically distinct from rank-1 audit, supplying spectral-projection foundation for the rebuttal claim.
- **2026af (Org Metamerism)** at §Forkability or §Cross-Industry Perception Transplant — observer-relative state-equivalence theory undergirds the forkability claim.
- **2026ag (Six-Tier Ontology)** with explicit disambiguation footnote — 2026ag's six tiers are distinct from orgschema's six levels (M&A transferability vs. TDD specification cascade); footnote prevents corpus-reader confusion.
- **2026ah (Brand-as-Tier-4)** as downstream theoretical extension at §Future Research.

### C-3: Add Figure 3 — OST family map

Mermaid network/tree diagram with OST at center, edges to 2026h (geometric foundation), 2026ae (verification algebra), 2026af (equivalence theory), 2026ag (transferability extension), 2026ah (brand-tier projection). Disambiguates seed paper from theoretical descendants. HIGH benefit / LOW cost. Caption: "Figure 3: The OST research program. The methodology introduced here has been extended in five companion papers, each addressing a distinct theoretical foundation or downstream application."

### C-4: Add Table 11 — Orgschema CI/CD validation levels mapped to ISO 9001:2015 clauses

Six rows (CI/CD levels 1–6 from Table 5) × 2 columns (orgschema validation, mapped ISO 9001:2015 clause + brief note). HIGH for TQM venue specifically. Caption: "Table 11: Orgschema CI/CD validation levels mapped to ISO 9001:2015 clauses. Each orgschema validation level satisfies one or more clauses; the mapping suggests orgschema as an implementation pathway for ISO 9001 documentation requirements."

### C-5: Add §Practical Implications for Operations Managers subsection (~400 words)

Place at §Discussion, before §Mapping to Beer's Viable System Model. Structured 3–5 implication block (e.g., "for plant managers", "for quality auditors", "for franchise operators", "for ISO 9001 implementation teams"). Packaging request — implications already implicit throughout body.

### C-6: Add §Implementation Roadmap subsection (~600 words)

At §Discussion or as final §Discussion subsection. Maps M0→M5 maturity transitions to roles (quality manager, process owner, IT/CI-CD engineer, executive sponsor) and tooling (YAML editor, JSON Schema validator, GitHub Actions runner). Sharpens the "M0→M2 in one day" claim. Can absorb and expand the M0→M5 phase passage at lines 309–310. Cite Feathers 2004 [^17] (already cited).

### C-7: Re-state contribution closure in §Conclusion

Conclusion currently drops the maturity model and executor-swap diagnostic from contribution recap. Add these to §Conclusion paragraph 2 to match the §Introduction enumerated contribution paragraph (C-1).

### C-8: Restate §1 / abstract "TDD-as-organizational-design" framing more explicitly

The TDD-as-organizational-design metaphor is the paper's most distinctive move but is named only as the paper subtitle. Add a standalone framing sentence in §Introduction: "We treat Test-Driven Development not as a software practice imported into business but as a generic design methodology of which both software TDD and organizational design are instances."

### New-paper opportunities surfaced (routed to Phase 4)

1. **"Cross-Industry Perception Transplant: A Methodology for Borrowing Acceptance Tests Across Domains"** — perception transplant is introduced but not developed; worked Apple-perception-applied-to-coffee example is a single illustrative paragraph. Target venue: JPIM or California Management Review. Dependencies: 2026a (SBT 8-dimension framework), 2026af (Org Metamerism observer-relative equivalence).
2. **"An Implementation Roadmap for ISO 9001:2026 via Test-Driven Organizational Specification"** — footnote [^24] notes ISO 9001:2026 in passing but no clause-by-clause implementation pathway is given. Target venue: TQM Journal companion piece or IJQRM. Dependencies: 2026i must be published first; ISO 9001:2026 must reach Final DIS stage.

## Phase 3 /review-paper Adversarial Review (2026-05-01)

Status: queued — not applied because paper is under TQM Journal review.

Source: `audit/reports/03_review_paper_2026i.md` in spectral-branding repo. 11 CRITICAL / 15 WARNING / 9 NOTE items. Items below are NEW relative to Phases 3a/3b/3c.

### Tier 1 — Structural items that would cause R&R or rejection if left unaddressed

**RP-1 (Q3 CRITICAL): Add Evaluation Methodology subsection.**
Five reviewers were assessed with no stated selection criteria, no evaluation protocol, no rubric. The FEDS framework [^14] requires replication-level description. A DSR specialist reviewer will reject this. Add ~300 words covering: (i) reviewer selection criteria and recruitment, (ii) materials provided, (iii) evaluation rubric or question set, (iv) coding/reporting of findings, (v) compensation / COI disclosure.

**RP-2 (Q1 CRITICAL): Qualify the "no existing framework" novelty claim.**
Line 107: "no existing framework provides machine-readable backward traceability from operational parameters to customer experience goals with automated satisfaction validation" does not exclude commercial MES/QMS platforms (SAP QM, Siemens Opcenter, ETQ Reliance, MasterControl). Add scope qualifier: "no *open, version-controlled, schema-first* framework" — or footnote addressing why commercial MES/QMS are excluded from comparison. Note: this also depends on B-5 / L-P3-B [^7] replacement.

**RP-3 (Q2 CRITICAL + Q3 CRITICAL): Scope instrument validity and practical adoptability claims to the demonstrated domain.**
Single-site coffee shop is a structurally simple business (low regulatory complexity, no manufacturing, no multi-tier supply chain). Validity established at Spectra Coffee does not transfer to manufacturers, hospitals, or digital service businesses. Explicitly scope validity claims in §Evaluation Results: "instrument validity is established for businesses with [characteristics of Spectra Coffee]; extension to higher-complexity domains is a research priority." ~2 sentences.

**RP-4 (Q4 CRITICAL): Note that CI/CD Levels 3 and 6 are unimplemented in §Limitations.**
The two unimplemented validation levels — Contract Satisfaction (Level 3, unit-test equivalent) and Waste Detection (Level 6, lean-pull backbone) — are precisely the levels most central to the paper's core claims. Paper acknowledges "four of six" but does not explain why central levels are incomplete. Add explicit Limitations sentence with technical reason (experiential validation requires operational telemetry integration) and bound the "validation pipeline" claims to the four implemented levels. ~2 sentences.

**RP-5 (Q4 WARNING + Q7 WARNING): Add Data Availability Statement.**
No URL to the public Spectra Coffee specification appears anywhere in the paper. Taylor & Francis FAIR data policy applies (submissions from 2024 onward). Add DAS before §References pointing to the public repository where Spectra Coffee specification, Friedrichshain fork, and CI/CD pipeline can be inspected.

### Tier 2 — Venue fit and argument development (reduce landing probability)

**RP-6 (Q9 Reviewer 4): Add TQM-anchoring paragraph in §Theoretical Foundations.**
Connect Level 0 acceptance contracts to SERVQUAL's five dimensions (tangibles, reliability, responsiveness, assurance, empathy) or Juran's quality trilogy. Show that the TDD cascade operationalizes TQM principles. ~200 words. Pairs with L-P1-A (Juran) and SERVQUAL [^23] richer engagement.

**RP-7 (Q5 CRITICAL): Add franchise enforcement boundary condition.**
The paper's franchise solution (sharing test suite without prescribing implementation) ignores the enforcement gap: who validates that a franchisee's procedures actually pass the tests? Acknowledge that CI/CD validation requires audit access as a contractual term, or acknowledge as an open boundary condition. ~100 words.

**RP-8 (Q5 CRITICAL): Acknowledge LLM hallucination as specification risk.**
If LLMs are essential to orgschema (Conclusion claim), then orgschema's quality guarantees are contingent on LLM reliability. Add "LLM as specification assistant: validation requirements" paragraph noting that LLM-generated content must pass the same CI/CD validation pipeline as human-authored content. ~100 words.

**RP-9 (Q9 Reviewer 3): Add "single unified methodology vs. tool stack" argument paragraph.**
Defend why a unified methodology matters as a design principle vs. assembling equivalent properties from a BDD/Cucumber + BPMN + ISO 9001 + CI/CD tool stack. The paper gestures at this (line 146: "the seams between those tools become operationally costly when AI agents begin consuming organizational specifications directly") but does not develop. ~150 words.

**RP-10 (Q1 CRITICAL — softening): Hedge "structurally superior" QA inspector quote.**
Lines 426–428: rephrase to "the inspector noted structural advantages over Word-based documentation" or qualify the comparison scope. The current testimonial language overstates what a single-case formative expert walk-through can establish. ~1 sentence.

**RP-11 (Q3 WARNING): Add defect severity classification criteria.**
Lines 415–416: define critical/major/minor (e.g., "critical = safety/compliance failure; major = specification incompleteness affecting methodology function; minor = formatting or non-functional metadata"). ~1 sentence.

**RP-12 (Q2 WARNING): Clarify "74% of files" file-count vs. content-coverage proxy.**
Line 246: "17 of 23 specification files (74%) define executor-invariant content" — note that file count is a proxy for structural separation, not a measure of content coverage. ~1 sentence.

### Tier 3 — Polish

**RP-13 (Q3 WARNING): Reframe process consultant assessment of "15% degradation".**
Line 430–431: rephrase to "the process consultant assessed that trade-offs of this type — automation-induced signal loss — would typically be invisible to operators relying on process-level metrics alone." Avoids circular reasoning about an illustrative number.

**RP-14 (Q4 WARNING): Add data availability footnote on YAML cross-references.**
Lines 345–347: the YAML excerpt's `satisfies_experience` identifiers cannot be verified without seeing the Level 0 contracts. Pairs with RP-5 DAS.

**RP-15 (Q1 WARNING): Soften "methodology whose time has arrived because of LLMs" claim.**
Lines 330–331: the no-prior-attempt counterfactual ("would have been impractical without LLMs") has no empirical basis. Rephrase to "LLMs make the multi-dimensional complexity practically manageable at scale for the first time, without requiring significant configuration tooling investment."

**RP-16 (Q2 WARNING): Add "technical prerequisites" assumption to the maturity model.**
Lines 310–312: the M4–M5 transitions assume DevOps capability or hosted orgschema service. Make explicit. ~1 sentence in Maturity Model section.

**RP-17 (Q5 WARNING): Distinguish specification-level vs. execution-level validation in §Level 0 contracts.**
Lines 221–228: the CI/CD pipeline validates specification consistency, not operational conformance. Add clarifying sentence to prevent reviewer confusion against ISO 9001's documented-vs-demonstrated distinction. ~1 sentence.

### Tier 4 — Optional re-framing for higher-tier venue migration

**RP-18 (Q9 desk-reject anticipation): Consider revising title for next venue.**
Current title "The Organizational Schema Theory: Test-Driven Business Design" omits any quality-management vocabulary. If R&R is granted, consider revising to foreground quality management, e.g., "Organizational Schema Theory: A Test-Driven Framework for Quality-Traceable Business Design" — or ensure abstract first sentence anchors in quality management.

**RP-19 (Q8 venue-fit framing): Restructure §Introduction to lead with quality management gap.**
Current Introduction leads with TDD and frames quality management as a downstream application. Venue-optimal framing leads with the QMS gap (existing systems cannot validate operational conformance against customer experience goals continuously), then introduces TDD as the mechanism. Apply only if R&R requested.

**RP-20 (Q8 NOTE): Elevate executor-swap and fork taxonomy from illustrative examples to named methodological contributions.**
Both Table 8 and Table 10 are genuinely new analytical tools that QMS practitioners could use. Currently presented as illustrations. In future revision, frame as named methodological contributions with brief treatment of implications for operations management decision-making. Pairs with C-1.

## Phase 3 Grok Pre-Submission Review (2026-05-01)

Status: queued — not applied because paper is under TQM Journal review.

Source: `audit/grok_outputs/2026i_grok.md` in spectral-branding repo. Grok readiness score: **4/10**. Estimated revision effort: XL. Desk-reject probability >80% in present form per Grok. 6 must-fix / 14 should-fix / 9 nice-to-have / 11 new citations recommended.

### Grok desk-reject risks (top-line)

1. Overstated novelty without systematic literature review
2. Excessive self-citation to unpublished corpus (especially Spectral Brand Theory dependency)
3. Insufficient engagement with contemporary TQM 4.0 and digital quality literature
4. Defensive manifesto tone (preemptive rebuttal subsections)

### G-1: Conduct and report a systematic positioning against post-2015 TQM 4.0 / smart quality / AI-augmented quality management literature.

Currently the paper engages classical TQM (Deming, Ohno) but no post-2015 TQM 4.0 corpus. This is the single highest-impact change for landing probability. Addresses Desk-Reject Risk 3 directly.

### G-2: Replace or heavily qualify all Spectral Brand Theory dependencies with independent perception/brand specification frameworks, OR reposition SBT as illustrative only.

The §Spectral Brand Theory as Test Specification Language section currently rests on an unpublished self-cite [^11]. Reviewers will read this as circular. Two options:
- **Option A**: replace SBT-dependency content with independent perception measurement frameworks (e.g., SERVQUAL extended with cultural / temporal dimensions; Schley measurement workshop refs from project memory).
- **Option B**: keep SBT but reframe as illustrative ("if a perception specification framework like Spectral Brand Theory is used at L0...") and add 2–3 alternative perception measurement candidates so the methodology is shown to be SBT-agnostic.

Pairs with the existing C-2 cross-corpus integration: forward-pointers to OST family papers (2026h, 2026ae, 2026af, 2026ag, 2026ah) supplement, but do not replace, this SBT-decoupling work.

### G-3: Condense artifact/demonstration sections by ~60%; move technical specifications to GitHub appendix with permanent DOI.

§The Artifact / §Demonstration / §Evaluation currently occupy ~45% of the manuscript. Move YAML excerpts and detailed defect lists to an online appendix at the public Spectra Coffee repository, citing the Zenodo-or-equivalent permanent DOI. Pairs with RP-5 (Data Availability Statement).

### G-4: Remove all defensive rebuttal subsections and manifesto language.

Remove or rewrite as scholarly positioning:
- §"Just Documentation" Rebuttal — convert to a single positioning paragraph in §Discussion
- "honest one-sentence formulation" passage at line 148 — scholarly tone
- "preemptive rebuttal to QFD+Six Sigma+ERP" at line 107 — restructure as positive positioning rather than defense
- Soften all "first / unprecedented / white space" primacy claims to "extends and unifies"

### G-5: Replace "we argue that this occupies genuine white space" (Abstract sentence 6) with precise gap analysis.

Current claim is unsupported. Replace with a quantitative or systematic-review-grounded statement of the gap: "In a structured comparison of N methodologies (Table 4), no prior approach simultaneously provides X, Y, Z."

### G-6: Strengthen "so what" for TQM audience.

Reframe contribution as "continuous, machine-readable customer-defined quality that scales with AI" — TQM 4.0 vocabulary the venue values. Pairs with Grok-supplied alternative title options (see G-rewrites below).

### G-7: Remove "first methodology... to combine all twelve structural properties" claim (line 146) OR defend via systematic review.

The 12 criteria were author-selected; the "first" claim is asserted not demonstrated. Either drop the claim or back it with a documented literature search (search terms, databases, inclusion/exclusion).

### G-8: Add formal propositions linking the 12 structural properties to quality performance outcomes (theoretical paper extension).

Even if untested, propositions in standard "If P → Q" form would shift the paper from manifesto-style to theory-style. P1: schema-first specification → improved backward traceability. P2: machine-readable validation → reduced waste detection latency. Etc.

### G-9: Extend VSM mapping with explicit pathology remediation metrics.

Beer's pathologies (e.g., variety attenuation failure, identity dissolution) are not currently mapped to orgschema-detectable signals. Add a column to Table 9 specifying which CI/CD validation level would surface each pathology. Pairs with C-2 forward-pointer to 2026ae (Verification as Operator).

### G-10: Develop a small multi-industry schema comparison.

A second and third schema example (e.g., coffee vs. healthcare clinic vs. software service) addresses Anticipated Reviewer 1's domain-narrowness concern (RP-3) more concretely than a verbal scope statement. Even a 1-page YAML excerpt for two additional industries demonstrates domain-agnosticism.

### Grok-supplied alternative title options

Grok provided three title alternatives optimized for TQM venue fit:

1. "Organizational Schema Theory: A Test-Driven, Backward-Design Approach to Machine-Readable Quality Management Systems"
2. "Test-Driven Business Design: Implementing Continuous Validation of Customer Experience in Quality Management"
3. "From Customer Perception to Sourcing: Organizational Schema Theory as a Declarative Framework for Business Excellence"

All three foreground quality management and business excellence vocabulary. Pairs with RP-18.

### Grok-supplied rewritten Abstract (248 words)

Available at audit/grok_outputs/2026i_grok.md §6. Foregrounds TQM language ("customer-defined quality", "continuous validation", "digital quality systems") and adds explicit pathway language ("pathway toward perception transplants"). Note: 248 words exceeds project standard ≤200; trim before applying.

### Grok-supplied rewritten Introduction skeleton

Available at audit/grok_outputs/2026i_grok.md §6. Reframes contribution as "synthesizes four streams" (TQM customer-defined quality + lean pull / reverse design + declarative BPM/organization-as-code + DSR methodology) rather than "three streams + white space." Cite 8–10 recent TQM/AI-quality papers in Introduction.

### Grok-supplied rewritten Conclusion/Discussion combined

Available at audit/grok_outputs/2026i_grok.md §6. Frames contribution explicitly as "unification of backward traceability, machine-readability, forkability, and continuous validation within a single ontological framework that maps cleanly onto Beer's VSM" — extension language rather than novelty language.

### Grok 11 recommended new citations (TQM 4.0 / digital quality literature gap)

Citations 1–11 below are Grok-generated; **all require user verification** before use (Grok has been observed to hallucinate citations in past audits — see canonical-references guard rule):

1. Sony, M., & Naik, S. (2020). "Industry 4.0 and lean manufacturing practices..." — grounds orgschema in TQM 4.0
2. Chiarini, A., et al. (2021). "Industry 4.0 and Total Quality Management" [VERIFY exact 2021 title]
3. Sader, S., et al. (2022). "The impact of artificial intelligence on quality management" — supports LLM enabler
4. vom Brocke, J., et al. (2021). "A unified model for declarative process specification" — updates Pesic & van der Aalst
5. Mueller, R. M., & Thoring, K. (2020). "Design science research in the age of AI" — strengthens DSR positioning
6. Benner, M. J., & Tushman, M. L. (2015). "Reflections on the 2013 Decade Award..." — organizational ambidexterity
7. Sousa, R., & Voss, C. A. (2018). "Service quality in the age of digital transformation" — updates service blueprinting
8. Kumar, V., et al. (2022). "AI-enabled continuous auditing and quality control" — directly supports CI/CD validation
9. Triguero-Mas, M., et al. (2023). "Perception-based quality in service operations" — independent perception measurement (pairs with G-2)
10. Osterrieder, P., et al. (2020). "The role of digital twins in quality management" — analogous to schema approach
11. ISO/DIS 9001:2026 working drafts and commentary papers (2025) — positions orgschema as implementation vehicle

### Grok structural reorganization

- **Merge** §Theoretical Foundations and §Positioning sections.
- **Move** VSM mapping earlier (currently appears too late in Discussion).
- **Create** dedicated §"Contributions to Quality Management" subsection in Discussion.
- **Reduce** total length by ~35%.

### Grok final recommendation

Post-revision (XL effort), TQM Journal acceptance probability estimated at 25–35%. Does not currently clear bar for higher-impact operations or IS journals (IJOPM, JOM, EJIS, MISQ, POM, JPIM all listed by Grok as alternative targets requiring further repositioning). Biggest remaining risk: core artifact may be viewed as "YAML documentation with extra steps" rather than substantive methodological advance unless TQM 4.0 positioning and defensive language removal are both addressed.
