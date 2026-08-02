---
title: "Pre-registration — Tier-Bundle Algebra v1.0 empirical case-coding pass"
version: 1.0.0
status: pre-analysis registered (no case-coding yet executed)
registered_at: 2026-05-19
registered_by: Dmitry Zharnikov
registration_anchor: |
  This document's first-public-commit SHA + commit-timestamp in the
  spectral-branding repository serves as the verifiable
  "registered-before-data" anchor. Any modification to the protocol
  after the pre-analysis commit (i.e., after the first commit that
  lands case-coding results) must be recorded as a numbered
  amendment below and the rationale stated.
companion_to:
  - "[internal path omitted]CASE_CODING_PROTOCOL.md (v1.0; the operational protocol)"
  - "[internal path omitted]V1_EMPIRICAL_CASES_CANDIDATES.md (the 14-anchor + 13-comparator case selection)"
  - "[internal path omitted] (v0.2 — the paper whose P6 this study tests)"
public_mirror_planned: "orgschema-papers/tier-bundle-algebra/PREREGISTRATION_V1.md (when public scaffold is created at v1.0)"
target_venue: (working paper; venue omitted for the public release)

backup_venue: [venue omitted] ([venue omitted])
amendments:
  - id: 1
    date: 2026-07-29
    type: administrative
  - id: 2
    date: 2026-07-29
    type: design-informing-pilot
    summary: "A small single-coder pilot (n=8, pilot/PILOT_CASE_CODING_2026-07-29.md) was executed BEFORE the confirmatory program to confirm the coding scheme is operable and surface refinements. It is explicitly NOT the pre-registered analysis and reports no inference test. It informs Amendments 3-4 below; the confirmatory n=30 design (hypotheses, falsifier, Fisher's-exact plan) is unchanged."
  - id: 3
    date: 2026-07-29
    type: coding-class-addition
    summary: "Add binary moderator gap_mitigated in {yes,no,NA}: was a documented cascade gap contractually absorbed at closing (transitional-services / operating agreement)? Reported as a pre-specified SECONDARY stratification (unmanaged-gap subset vs full sample), NOT a new primary hypothesis. Rationale: pilot eBay-PayPal case had a real Tier-5 gap that produced no failure because an operating agreement absorbed it; pooling managed and unmanaged gaps biases the P6 test toward the null."
  - id: 4
    date: 2026-07-29
    type: coding-class-refinement
    summary: "Refine coding class C (failure-pathway incidence): code Tier-1-archetype incoherence and Tier-2-business-model incompatibility as failure channels DISTINCT from the phi4->phi6 cascade the P6 cells target. Does not change the H6a/H6b/H6c cell definitions (still on the phi4->phi5 and phi5->phi6 boundaries). Rationale: pilot's two largest failures (Daimler-Chrysler T1/T6; AOL-Time Warner T2) sit outside the cascade P6 addresses; separating these channels prevents mis-attribution."
  - id: 6
    date: 2026-07-29
    type: sampling-frame-finalization
    summary: "Finalize the extension frame after EDGAR reconnaissance (EXTENSION_FRAME_ENUMERATION_NOTES.md). EDGAR full-text search is 2001-present only, so the frame WINDOW is narrowed to DEFM14A filed 2001-01-01..2020-12-31 (O1; the anchor tier already covers pre-2001 deals: Daimler 1998, AT&T-Lucent 1996). Frame = the 85 deduplicated completed US-registrant public-company acquisitions with a retrieved DEFM14A accession enumerated in that file's sec.2b INCLUDED table; deduplicated to the deal (O4); filer-role = target (O5); S-4 excluded to avoid overlap (O6); foreign-domicile registrants excluded (O7). Because deal value is not a structured EDGAR field (O2) and 'completed' is not a filing flag (O3), the >= $1bn value and deal-completion are CONFIRMED per drawn case at dossier-build; any drawn case that fails (terminated, < $1bn, foreign registrant, or anchor-overlap) is replaced by the NEXT case in the seeded permutation. Draw mechanism: seed 20260520, Python random.Random(20260520) permutation of the frame sorted by its sec.2b index; first 16 = the extension sample, remainder = the ordered replacement queue. Draw executed by draw_extension_sample.py -> EXTENSION_SAMPLE_n16.md."
  - id: 5
    date: 2026-07-29
    type: sourcing-method
    summary: "Sourcing method SET (author decision 2026-07-29) to verified public-source dossiers. (1) EVIDENTIARY STANDARD: every coded field in a case dossier must be traceable to a cited public primary source (SEC EDGAR filing 8-K/S-4/DEFM14A/10-K; company release; or a reliable public press archive FT/WSJ/Reuters/Bloomberg/NYT); any fact not so verifiable is flagged UNVERIFIED and never guessed (corpus anti-fabrication HARD rule). (2) SAMPLING-FRAME SUBSTITUTION: the n=16 extension is drawn not from the inaccessible HBR case-collection catalogue but from the SEC-EDGAR-enumerable frame of completed US public-company acquisitions with an S-4 or DEFM14A filed 1995-2020 and disclosed deal value >= $1bn, enumerated via EDGAR full-text search (efts.sec.gov); seed unchanged (20260520), same Mersenne-Twister without-replacement procedure; sampled list committed to EXTENSION_SAMPLE_n16.md BEFORE any dossier is built. Non-US anchor cases (e.g. Daimler-Chrysler, elBulli) remain in the 14-anchor tier. (3) The performance-stratification and blinding provisions of CASE_CODING_PROTOCOL.md sec.5 are retained; blinding of the AI coders to anchor-vs-extension status is approximated by presenting each coder only the dossier, never this document. This is the path-(b) option named in the Coding-phase status section; it is a deviation from the sec.3 primary-source-dossier default recorded here transparently before coding begins."
---

# Pre-registration: Tier-Bundle Algebra v1.0 empirical pass

This pre-registration locks the design of the v1.0 empirical
case-coding pass that will test Proposition 6 of the Tier-Bundle
Algebra paper (Zharnikov 2026, working memo v0.2). It follows the
GitHub-stored-pre-registration discipline established for the
Zharnikov corpus — the file is committed to the SSOT
(`spectral-branding/[internal path omitted]PREREGISTRATION_V1.md`)
*before* any case-coding result is committed; the pre-analysis
commit's SHA + timestamp is the verifiable anchor.

## 1. Hypothesis under test

**P6 (per TIER_BUNDLE_ALGEBRA_PAPER.md v0.2 §6.5)**: Cascade-
conformance failure predicts a defined subset of integration-failure
pathways in the parent paper (Zharnikov 2026ag) typology:

- **H6a (φ_4→φ_5)**: Cascade gaps at the φ_4→φ_5 step predict elevated
  P4-pathway disruption (Product–Process incoherence at the parent
  paper's Tier-4 to Tier-5 service link).
- **H6b (φ_5→φ_6)**: Cascade gaps at the φ_5→φ_6 step predict elevated
  P5-pathway fracture (Process–Organization detachment at the parent
  paper's Tier-5 to Tier-6 service link).
- **H6c (aggregate)**: Any cascade gap predicts any P4-or-P5-pathway
  incidence (the aggregate test pooling H6a + H6b).

The null hypothesis for each Hn is that cascade-gap-status and
failure-pathway-incidence are statistically independent across the
case corpus.

## 2. Corpus

**Corpus size**: n = 30 documented public Western M&A cases.

**Selection criteria** (PRE-LOCKED at v0.1.2 in
V1_EMPIRICAL_CASES_CANDIDATES.md):
- Public Western M&A only (US, UK, EU, Canada, Australia).
- Rich academic + media coverage (HBR / [venue omitted] / [venue omitted] / FT / WSJ / etc.).
- Documented post-deal 3-5yr trajectory where applicable.
- NO Russian / Eastern-bloc cases (political sensitivity).
- NO mention of Maffin / MaffinLab / Petroff or any related person.
- Canonical recognition test: a strategy / M&A scholar would
  recognise the case from a one-line description.

**Composition**:
- 14 *anchor* cases = one PRIMARY case per Table 1 row (Table 1a + 1b),
  selected during the 2026-05-19 cross-engine deep-research pull and
  triaged in V1_EMPIRICAL_CASES_CANDIDATES.md. Listed in Appendix A
  of this document.
- 16 *extension* cases drawn from a **pre-registered random sample**
  of HBR M&A case-collection cases meeting the selection criteria
  above. Random sample to be drawn AFTER this pre-registration is
  committed; sampling seed: 20260520 (deterministic to allow
  replication).

**Extension fallback**: if Fisher's exact at n = 30 returns
0.05 ≤ p < 0.20 on the H6c aggregate cell, the corpus extends to
n = 50 (additional 20 cases via the same random-sample mechanism with
extension seed 20260603). This extension is pre-registered and
constitutes a single, not iterated, extension.

**Cases EXCLUDED from H6 testing** (still in corpus for descriptive
analysis but excluded from the chi-square cells):
- Row 1b/8 *intra-business pivot* — no ownership-boundary crossing,
  so the cascade rule is type-symmetric (forward and reverse) rather
  than asymmetric; P6 does not predict on this case-class.
- Row 1b/10 *sole-proprietor wind-down* — admissibility predicate α
  fires before cascade-rule κ; the case anchors P3 not P6.
- Row 1b/9 *redomiciliation* — pure Tier-3 swap with empty cascade
  in the modal case; P6 vacuous.

Expected H6-eligible corpus subset: ~24 of the 30 cases.

## 3. Coding protocol

Per `CASE_CODING_PROTOCOL.md` §3 (locked 2026-05-19):

**Variables coded per case** (5 classes):

- **A. Bundle signature σ**: per-tier direction-and-cardinality token
  for T1–T6, drawn from the v0.2 §6 alphabet {1→1, N→1, 1→N, subset,
  partial, read-only, swap, terminate, ∅; T1 composites: replace,
  imprint-share, continue, terminate, reconstruct, replicate,
  mutual-replace}.
- **B. Cascade-conformance π(B)**: per-tier binary flag — was
  κ(B) ⊆ Image(B) at this tier? Coded as 0 (gap) / 1 (conformant).
  The key cells are π_4→5 (cascade gap at the T4→T5 implication) and
  π_5→6.
- **C. Failure-pathway incidence**: per case, binary flag for each
  Pn ∈ {P1, …, P7} of the parent paper's typology. 0 (not manifested)
  / 1 (manifested at the 3-5yr horizon). Pn definitions from
  Zharnikov 2026ag §6.
- **D. Performance metric**: 3-5yr post-deal CAR (cumulative abnormal
  return) where measurable; OR documented write-down magnitude as a
  fraction of deal value; OR divestiture timing in months from
  closing. Whichever is documented for the case.
- **E. Collapse state S** ∈ {none, T1≡T4, T1≡T3, T1≡T3≡T4, T1≡T2,
  T1≡T6}. Where multiple collapse-state interpretations are tenable,
  the dominant collapse is coded with an alternative-collapse note.

**Coder structure**: triple-AI coding (Claude + Gemini + Grok) with
majority-vote-or-flag at each cell. Disagreements (≥1 model differs
from the other 2) flagged for partner adjudication.

**Evidence dossier**: 3-5 page dossier per case assembled BEFORE
coding, containing:
- Deal-document excerpts (SPA / merger agreement / SEC 8-K / S-4 /
  proxy statement) supplying tier-level transfer content.
- Post-deal performance documentation at 3-5yr horizon (press
  archive + financial filings).
- Failure-pathway documentation: HBR case narratives, post-mortem
  journalism, academic case studies.

Each coder (Claude, Gemini, Grok) sees the dossier ONLY, not the
predicted answers. Coding-bias is mitigated by the dossier-driven
rather than algebra-driven framing of the coder's prompt.

## 4. Statistical analysis

**Primary tests** (pre-registered):

- **H6a**: 2×2 Fisher's exact on cascade-gap-at-φ_4→φ_5 (yes/no) ×
  P4-pathway-disruption (yes/no), reported with Cramér's V + 95%
  Clopper-Pearson CI.
- **H6b**: 2×2 Fisher's exact on cascade-gap-at-φ_5→φ_6 (yes/no) ×
  P5-pathway-fracture (yes/no), reported with Cramér's V + 95% CI.
- **H6c**: 2×2 Fisher's exact on any-cascade-gap (yes/no) × any-
  P4-or-P5-incidence (yes/no), reported with Cramér's V + 95% CI.

**Multiple-testing correction**: Bonferroni α = 0.025 for the H6a +
H6b family. H6c is treated as the omnibus test at α = 0.05.

**Robustness sub-sample analysis** (pre-registered):

On a random 10-case sub-sample of the H6-eligible corpus, the same
variables are coded at ordinal granularity (4 levels per cascade-
conformance variable: 0=no fork, 1=clean fork, 2=partial fork,
3=cascade-gap-with-documented-friction; 4 levels per Pn: 0=none,
1=minor, 2=material, 3=deal-defining). Proportional-odds ordinal
regression of Pn on cascade-conformance, with α = 0.05 per test.
The sub-sample serves as a robustness check; the headline result
remains the binary Fisher's exact.

**Confirmation threshold for P6 (paper §6.5 falsifying-direction)**:
P6 is supported empirically if AT LEAST ONE of H6a, H6b at
Bonferroni-corrected α = 0.025 rejects independence with Cramér's
V ≥ 0.30 (moderate effect size). H6c at α = 0.05 with Cramér's V ≥
0.20 is reported regardless as the omnibus indicator.

**Falsifying threshold**: P6 is empirically falsified at v1.0 if NONE
of H6a, H6b, H6c rejects independence at p < 0.10 (i.e., even the
weakest non-corrected α threshold finds no signal). At p ≥ 0.10 on
all three cells, the v1.0 paper reports the null result and the
algebra's P6 is downgraded from "candidate predictor" to "not
empirically supported at n = 30/50" in the §8 discussion.

## 5. Variables NOT pre-registered (exploratory only)

The following analyses, if performed at v1.0, are EXPLORATORY rather
than confirmatory and will be reported separately:

- Tests on the other parent-paper propositions (P1, P2, P3, P4, P5,
  P7) using the same coded dataset.
- Industry-level sub-group analyses.
- Time-period sub-group analyses (pre-2008 vs post-2008 financial
  crisis; pre-2020 vs post-2020 COVID).
- Continuous performance-metric regression on cascade-conformance
  composite scores.
- Cross-tier composite signature analysis (multi-tier cascade gaps
  predicting multi-pathway failures).

Any finding from exploratory analysis at v1.0 is labelled as such
and not used to claim empirical support for the algebra's
propositions.

## 6. Deviations + amendments protocol

If a protocol deviation is required after this pre-registration is
committed:
- The deviation is recorded as a numbered amendment in the
  frontmatter `amendments:` block of this document.
- The amendment commit cites the rationale and the date.
- The original pre-registration text remains unmodified — amendments
  are additive.
- The v1.0 paper reports any amendments transparently in §7
  methodology.

## 7. Anticipated results and the falsifying-direction commitment

The author's prior is that H6a will reject the null (cascade-gaps at
φ_4→φ_5 correlate with P4-pathway disruption at moderate effect size)
based on the theoretical mechanism derived in v0.2 §4. The author's
prior on H6b is weaker but directionally similar. The author's prior
on H6c is moderate.

If results contradict these priors — i.e., if p ≥ 0.10 on all three
cells — the author commits to reporting the null result transparently
in v1.0 §8 and downgrading P6's empirical-support claim accordingly.
The v1.0 paper will not be revised to claim support that the data
does not provide; the algebra's other propositions (P1–P5) remain
defensible on theoretical grounds even if P6 fails.

## Appendix A — Pre-locked anchor cases (n = 14)

From V1_EMPIRICAL_CASES_CANDIDATES.md (locked at v0.1.2 commit):

| Table 1 row | PRIMARY case | Year |
|---|---|---|
| 1a/1 Share sale | Daimler-Chrysler | 1998 |
| 1a/2 Asset deal | Barclays-Lehman | 2008 |
| 1a/3 Carve-out | 3Com-Palm | 2000 |
| 1a/4 Acqui-hire | Facebook-FriendFeed | 2009 |
| 1a/5 Roll-up | SCI funeral-home roll-up | 1980s-1990s |
| 1a/6 Spin-out | AT&T-Lucent | 1996 |
| 1b/7 Franchise | McDonald's | 1955-present |
| 1b/8 Intra-business pivot | Netflix DVD→streaming | 2007-2011 |
| 1b/9 Redomiciliation | Medtronic-Covidien | 2015 |
| 1b/10 Sole-prop wind-down | elBulli (Ferran Adrià) | 2011 |
| 1b/11 Merger of equals | Daimler-Chrysler (re-used) | 1998 |
| 1b/12 Reverse merger | NYSE-Archipelago | 2005-2006 |
| 1b/13 Joint venture | GM-Toyota NUMMI | 1984-2010 |
| 1b/14 Asset swap | Novartis-GSK three-way | 2014-2015 |

Comparator cases (n = 13) per V1_EMPIRICAL_CASES_CANDIDATES.md
Section "Selection summary table".

## Appendix B — Extension random-sample seed + procedure

Seed: 20260520 (six-digit numeric; corresponds to 2026-05-20 as a
human-memorable date one day after this pre-registration commit).

Procedure: HBR M&A case-collection catalogue (filtered to the
v0.1.2 selection criteria) sorted alphabetically by case title;
Mersenne-Twister PRNG seeded with 20260520; 16 cases drawn without
replacement. Sampled case-list to be committed to
`[internal path omitted]EXTENSION_SAMPLE_n16.md` AFTER this
pre-registration is committed and BEFORE any case-coding begins.

If the extension to n = 50 is triggered: extension seed 20260603;
same procedure; 20 cases drawn from the catalogue WITH the 30
already-coded cases excluded.

## Appendix C — Files referenced

- `CASE_CODING_PROTOCOL.md` — operational protocol (locked 2026-05-19)
- `V1_EMPIRICAL_CASES_CANDIDATES.md` — anchor + comparator case list
- `VERIFICATION_REPORT_2026-05-19.md` — Perplexity verification of
  lit-review references underlying the algebra's positioning
- `analyze_study_n30.py` — pre-registered confirmatory analysis
  pipeline (Fisher's exact + Cramer's V + Clopper-Pearson + Bonferroni);
  committed BEFORE any coded datum, self-validated on a synthetic fixture
  (`--fixture`) with a known Fisher's-exact value
- `pilot/` — the design-informing n=8 pilot (Amendment 2)
- `EXTENSION_SAMPLE_n16.md` — NOT YET CREATED; will be committed
  after this pre-registration via the seeded sampling procedure
- `TIER_BUNDLE_ALGEBRA_PAPER.md v0.2` — the paper whose P6 this
  study tests

---

## Amendments log (additive; original text above is unmodified)

Per §6, amendments are additive and the locked body text above is left
unchanged. Full amendment records are in the frontmatter `amendments:`
block; summarized here for readability.

- **Amendment 1 (2026-07-29, administrative).** Paper supersession +
  venue retarget. P6 is now tested against `[internal path omitted]`
  Studies (primary) / [venue omitted] (alternate). Hypotheses,
  coding scheme, and statistical plan unchanged.
- **Amendment 2 (2026-07-29, design-informing pilot).** A single-coder
  n=8 pilot (`pilot/PILOT_CASE_CODING_2026-07-29.md`, deterministic
  analysis in `pilot/`) was run before the confirmatory program to
  confirm operability. Not the pre-registered analysis; no inference
  test. Informs Amendments 3-4.
- **Amendment 3 (2026-07-29, coding-class addition).** Add
  `gap_mitigated` moderator (secondary stratification only).
- **Amendment 4 (2026-07-29, coding-class refinement).** Separate
  Tier-1-archetype and Tier-2-model failure channels from the cascade
  cells (class C refinement; cell definitions unchanged).
- **Amendment 6 (2026-07-29, sampling-frame finalization).** After
  EDGAR reconnaissance (`EXTENSION_FRAME_ENUMERATION_NOTES.md`): window
  narrowed to DEFM14A 2001-2020 (EDGAR full-text search is 2001+ only;
  anchors cover pre-2001); frame = the 85 deduplicated target-registrant
  DEFM14A deals enumerated there; value >= $1bn and completion confirmed
  per drawn case at dossier-build, failures replaced by the next case in
  the seeded permutation. Draw: seed 20260520, run by
  `draw_extension_sample.py` -> `EXTENSION_SAMPLE_n16.md`.
- **Amendment 5 (2026-07-29, sourcing method).** Author set the
  sourcing method to **verified public-source dossiers**: every coded
  field traceable to a cited public primary source (EDGAR filings /
  company releases / reliable press), unverifiable facts flagged not
  guessed; the n=16 extension frame substituted from the inaccessible
  HBR catalogue to the SEC-EDGAR-enumerable frame (S-4/DEFM14A,
  1995-2020, >= $1bn), seed 20260520 unchanged. Resolves the
  Coding-phase status gate. Coding may begin once EXTENSION_SAMPLE_n16.md
  is drawn and dossiers are built to the evidentiary standard.

## Coding-phase status (2026-07-29) — document-access gate

The registered-before-data phase is complete and committed: this
pre-registration (with amendments), the reproducible statistical
analysis pipeline (`analyze_study_n30.py`, validated on a synthetic
fixture with a known Fisher's-exact value), and the coding schema are
all committed BEFORE any real coded datum exists, preserving the
registered-before-data anchor.

The **confirmatory coding itself is gated on primary-source document
access** that the drafting environment does not have:

1. **The n=16 random extension** (Appendix B) draws from the HBR M&A
   case-collection catalogue, which is not accessible here — the seeded
   draw (seed 20260520) cannot be executed without the catalogue frame.
2. **Dossier-driven coding** (§3) requires 3-5 page primary-source
   dossiers (SEC 8-K/S-4/proxy filings, HBR case narratives, deal
   documents) per case. These cannot be assembled to citation-grade in
   this environment. Coding 30 cases from an LLM's training-data priors
   instead would violate both this pre-registration's dossier-driven
   requirement and the corpus anti-fabrication standard, and is
   therefore NOT done.

Resolving the gate is an author decision on sourcing method, to be
recorded as a further amendment before coding begins:
- **(a) Primary-source dossiers** (author supplies HBR/document access;
  the locked gold-standard path).
- **(b) Verified public-source dossiers** (EDGAR SEC filings are public;
  major-deal outcomes are documented in reliable public press) — a
  multi-session build with a pre-registered sourcing amendment and a
  public-source-drawable sampling frame replacing the HBR catalogue.
- **(c) Explicitly-labeled triple-LLM elicitation from public-record
  knowledge (no dossiers)** — a stronger-than-pilot computational
  elicitation, honestly reported as NOT the primary-source confirmatory
  study; lowest evidentiary weight.
