# Case-coding protocol for the Tier-Bundle Algebra v1.0 empirical pass

**Status**: partner-approved 2026-05-19; protocol locked at the
options below; execution awaits v0.2 paper merge.
**Partner decisions applied 2026-05-19**:
- Most academically robust path at each design dimension chosen.
- Triple-coding via three models (Claude + Gemini + Grok) with
  majority-vote-or-flag at each cell, replacing the original
  single-AI-coder recommendation.
- Pre-registration on GitHub (public SSOT path) before analysis.
  direction has higher acceptance probability than empirical given
  the n=30 corpus size;[venue omitted]accepts pure-theory + framework-level
  papers with falsifying-direction propositions; the v1.0 empirical
  pass becomes supporting rather than critical.
**Companion**: `V1_EMPIRICAL_CASES_CANDIDATES.md` (the case selection
that this protocol will be applied to).
**Anchors**: TIER_BUNDLE_ALGEBRA_PAPER.md v0.1.2 §3 (cascade-rule κ +
conformance-predicate π), §6.5 (P1–P6 in canonical form), §8 (v1.0
roadmap); parent paper Zharnikov (2026ag) §6 (P1–P7 failure pathways).

## 1. What "case-coding" means in this context

The v1.0 empirical pass tests Proposition 6 of the paper — cascade-
conformance failure predicts a defined subset of integration-failure
pathways — against documented public M&A cases. "Case-coding" is the
operational step of converting each documented case (Daimler-Chrysler
1998, eBay-PayPal 2015, etc.) into a structured row in a coded
dataset, against which statistical tests can be run.

Per case, the coder assigns three classes of variables:

| Class | What is coded | Cardinality |
|---|---|---|
| **A. Bundle signature σ** | Per-tier direction-and-cardinality token for T1–T6 | 6 tokens drawn from the §6 alphabet |
| **B. Cascade-conformance π(B)** | Per-tier flag: was κ(B) ⊆ Image(B) at each tier? | 6 binary flags (conformant / cascade-gap) |
| **C. Failure-pathway incidence** | Per case, which of parent paper's P1–P7 failure pathways manifested at the post-deal 3-5 year horizon? | 7 binary flags |
| **D. Performance metric** | Documented post-deal outcome | 1–3 quantitative scalars |
| **E. Collapse state** | Seller's collapse-state S ∈ {none, T1≡T4, T1≡T3, T1≡T3≡T4, T1≡T2, T1≡T6} | 1 categorical |

The coded dataset is therefore a (per-case row) × (per-variable column)
matrix with `n_cases × ~20 columns`. The statistical test on P6 is
typically a 2×2 contingency between {cascade-gap at φ_4→φ_5: yes/no}
and {P4-pathway disruption observed: yes/no} (and analogously the
φ_5→φ_6 vs P5 cell).

## 2. The five design dimensions of the protocol

Each design dimension has options; the protocol is the set of choices
across them.

### Dimension 1 — Coding granularity

**Option 1a: Binary coding** (recommended for v1.0 first pass).
- Cascade-conformance per tier: {0, 1} — gap-present vs gap-absent.
- Failure-pathway per Pn: {0, 1} — manifested vs not-manifested at the 3-5yr horizon.
- Test: chi-square or Fisher's exact on the contingency table.
- Statistical power: with n = 30 and a true effect size of moderate
  strength, binary 2×2 chi-square achieves ~80% power at α = 0.05.

**Option 1b: Ordinal coding** (richer, more partner-time-consuming).
- Cascade-conformance per tier: {0 (no fork), 1 (clean fork), 2 (partial fork), 3 (cascade-gap with documented friction)}.
- Failure-pathway intensity: {0 (none), 1 (minor), 2 (material), 3 (deal-defining)}.
- Test: ordinal regression (proportional odds model).
- Statistical power: lower for ordinal tests at n = 30; typically requires n ≥ 50.

**Option 1c: Continuous-where-possible coding** (most ambitious).
- Cascade-conformance: track ratio of κ-implied operations actually present in B.
- Failure-pathway intensity: documented financial impact (write-down magnitude, share-price reaction, divestiture timing).
- Test: linear regression / structural-equation modelling.
- Statistical power: highest per case BUT requires partner subject-matter judgment per case + per case 4-6 hours partner time.

**Recommended for v1.0**: Option 1a (binary) as the baseline pass.
If Option 1a yields a significant result on P6, partner may upgrade to
Option 1b for the publication version. Option 1c is reserved for v2.0
follow-up paper if v1.0 lands well.

### Dimension 2 — Coder structure

**Option 2a: Single-coder protocol.**
- One coder (Zharnikov OR a designated research assistant) codes all
  cases.
- Reliability: not assessable. Risk of systematic coder bias.
- Time-cost: lowest. ~30-60 min per case for binary coding (n = 30 → ~15-30 partner hours).

**Option 2b: Dual-coder with inter-rater reliability** (recommended for
publication-grade work).
- Two coders independently code all cases; disagreements adjudicated
  by a third (senior strategy faculty / partner).
- Reliability assessed via Cohen's κ (different κ from the algebra
  κ — context will disambiguate); target κ ≥ 0.70.
  adjudication time.

**Option 2c: AI-assisted coding with human verification.**
- LLM-based coder produces a first-pass coding from documented case
  studies; human coder verifies and corrects.
- Reliability: depends on how often the human corrects. Tracked.
- Time-cost: ~1.5× single-coder; mostly in verification rather than
  primary coding.
- Risk: LLM may anchor on training-data narratives that the algebra
  is designed to challenge — the case may have been previously coded
  by reviewers without the algebra's tier framework, so the LLM's
  prior is structurally biased.

**Recommended for v1.0**: Option 2c (AI-assisted with human
verification) for the first pass; Option 2b (dual-coder) for the
publication-version reviewer-response if reviewers push back on
reliability.

### Dimension 3 — Corpus size + composition

**Option 3a: One case per Table 1 row (n = 14).**
- Pros: tightly mapped to the paper; each row anchored.
- Cons: statistical power too low for chi-square on the P6 contingency
  (n = 14 gives ~30% power at moderate effect size).
- Verdict: insufficient for the empirical claim P6 makes.

**Option 3b: 30-50 documented Western public M&A cases** (recommended).
- Sourced from HBR case-collection (the M&A subset is ~200 cases) +
  documented public deals from FT / WSJ / Bloomberg archives.
- Composition: oversample the empirically-canonical cases (Daimler-
  Chrysler, AOL-Time Warner, eBay-PayPal, Microsoft-LinkedIn, NUMMI,
  Novartis-GSK three-way) + supplement with documented deals where
  cascade-gaps are explicitly described in the case narrative.
- Power: ~80% on 2×2 chi-square at moderate effect size.

**Option 3c: 100+ cases via Compustat M&A database join** (most
ambitious).
- Compustat + SDC Platinum M&A databases provide structured deal data
  for ~10,000+ US public deals 1980-present.
- Coding requires inferring tier-level transfer content from the
  deal-document and post-deal performance — much heavier per-case work
  AND many deals don't have rich enough public coverage to support
  cascade-conformance coding.
- Verdict: out of scope for v1.0; reserved for a follow-up empirical
  paper.

**Recommended for v1.0**: Option 3b (30-50 cases), starting from the
14 Table 1a+1b anchored cases in V1_EMPIRICAL_CASES_CANDIDATES.md and
extending by 16-36 more from HBR + FT archives along the same
selection criteria.

### Dimension 4 — Statistical test design

The critical test on P6 is **2×2 contingency** between cascade-
gap-at-φ_n→φ_{n+1} (yes/no) and Pn-pathway-disruption (yes/no), for
each n where the cascade rule has structural implications. The
paper's P6 statement specifies two such cells:

**Cell 1 (P6/φ_4→φ_5)**: cascade gap at the φ_4→φ_5 step predicts
P4-pathway disruption (Product–Process incoherence at the parent
paper's Tier-4 to Tier-5 service link).
**Cell 2 (P6/φ_5→φ_6)**: cascade gap at the φ_5→φ_6 step predicts
P5-pathway fracture (Process–Organization detachment at the parent
paper's Tier-5 to Tier-6 service link).

Plus a global test:

**Cell 3 (P6/aggregate)**: any cascade-gap predicts any P4-or-P5-
pathway incidence.

**Statistical test**: Fisher's exact test (preferred for n < 50 where
chi-square approximations break down). Reported with effect size
(Cramér's V) + 95% CI.

**Falsifying-criterion threshold** (per v0.1.2 §6.5 P6 falsifying
direction): the test fails to reject the null of independence at
α = 0.05 (i.e., p ≥ 0.05) on the aggregate-P6 cell (Cell 3).
This is the operational definition of "indistinguishable" in the
paper's P6 falsifying-direction language.

**Confirmation threshold**: p < 0.05 on either Cell 1 or Cell 2 (or
both) under a Bonferroni-corrected α of 0.025 for the two-cell
family — sufficient to claim P6 has empirical support at the
sub-cell level.

### Dimension 5 — Case-data sourcing

For each case in the v1.0 corpus, the coder needs:

1. **Deal document** (SPA / merger agreement) OR documented case study
   with tier-level transfer content extractable. HBR cases typically
   suffice; SEC filings (8-K, S-4, proxy statements) for US public
   deals supply legal substrate.
2. **Post-deal performance documentation** at the 3-5yr horizon:
   - Financial: share-price reaction (CAR study) OR documented
     write-down magnitude OR divestiture timing.
   - Strategic: documented integration outcome from press archives.
3. **Failure-pathway documentation** for any P1–P7 manifestation: HBR
   case narratives, post-mortem journalism, academic case studies.

**Recommended workflow**:
- Per case, assemble a 3-5 page evidence dossier with verbatim
  excerpts from the deal-doc + 5-yr-horizon outcome doc + failure-
  pathway documentation.
- Coder reads the dossier (not the full underlying documents) and
  applies the codebook.
- Dossier preserved as supplementary online material at v1.0
  publication; reviewers can audit each coding decision against the
  dossier.

## 3. Locked v1.0 protocol (partner-approved 2026-05-19; most academically robust path at each dimension)

### Instrument pins — the exact model identifiers as called

A family name is not an instrument. These are the identifiers the coding harness
actually sent, recovered from the `model_version` field of every call record in
the published call logs rather than from any human-written note:

| Coder role | Identifier as called | Logged calls |
|---|---|---|
| Extractor / rater A | `claude-opus-4-8` | 84 |
| Extractor / rater B | `gemini-3.1-pro-preview` | 104 |
| Extractor / rater C | `grok-4.3` | 82 |

**The `-preview` suffix is part of the served identifier, not a placeholder.** The
bare `gemini-3.1-pro` is not served on this endpoint and returns 404, so a
reproducer who types the short human-readable form the Acknowledgments use will
get no response at all. Recorded here in 2026-08-09 because the run predates the
convention of pinning literally in the protocol; the run itself is unaffected and
no coded value changes. Being a pre-registered instrument, these pins are frozen:
a newer model is a reason to keep them, never to change them.

| Dimension | Locked choice | Rationale |
|---|---|---|
| Coding granularity | **Binary (1a) as baseline + ordinal (1b) on a 10-case sub-sample** | Binary 2×2 chi-square/Fisher's exact is the conventional analytic default; ordinal sub-sample acts as robustness check against reviewer pushback. |
| Coder structure | **Triple-AI coding (Claude + Gemini + Grok)** with **majority-vote-or-flag** per cell + **partner verification of all disagreements** | Mirrors the deep-research three-engine pattern that surfaced the `klepper2001` hallucination. Single-AI coding inherits one model's systematic bias; triple-coding with disagreement flagging acts as a per-cell anti-hallucination filter. Partner verifies any cell where the three engines disagree (typically 10-20% of cells). |
| Corpus size | **n = 30 cases (3b) as baseline; pre-registered extension to n = 50 if Fisher's exact at n = 30 returns 0.05 ≤ p < 0.20** | n = 30 + ordinal-sub-sample robustness gives ~80% power at moderate effect size; n = 50 extension is the pre-registered fallback. |
| Statistical test | **Fisher's exact on 3 cells (P6/φ_4→φ_5; P6/φ_5→φ_6; P6/aggregate)** with **Bonferroni α = 0.025** for the two-cell family + **Cramér's V + 95% CI** for effect size. Additional ordinal regression (proportional odds) on the 10-case sub-sample. | Fisher's exact is the reviewer-default at small n; Bonferroni handles multiple testing; effect size + CI satisfy the reviewer expectation that "statistically significant" be paired with "practically meaningful." |
| Sourcing | **3-5 page evidence dossier per case** drawn from public-record sources only (HBR cases, FT/WSJ/Bloomberg archives, SEC filings); **dossier preserved as supplementary online material** at v1.0 publication. | Allows reviewers to audit each coding decision against the verbatim source data;[venue omitted]reviewers explicitly request this kind of transparency for theoretical-empirical-hybrid papers. |
| **Pre-registration** | **GitHub-stored pre-registration** at `orgschema-papers/tier-bundle-algebra/PREREGISTRATION_V1.md` (mirror) + `spectral-branding/[internal path omitted]PREREGISTRATION_V1.md` (SSOT). Pre-registered BEFORE any case-coding begins; cited from the v1.0 paper. | GitHub is the same public-SSOT mechanism the corpus already uses (zenodo-deposited papers cite GitHub for code + data). Adopts the pre-registration discipline without requiring an OSF or AsPredicted account. The PREREGISTRATION_V1.md document is git-stamped at the pre-analysis commit; that commit's SHA + timestamp is the verifiable "registered-before-data" anchor. |

Partner time estimate at the locked protocol: **60-80 partner hours
total** (30 cases × 1-2 hr verification on majority-vote AI coding +
~5-10 hr per-case disagreement adjudication + ~10 hr statistical
analysis + ~15 hr write-up + ~10 hr pre-registration discipline).
The extra ~20 hr over the prior single-AI-coder estimate reflects
the triple-coding + disagreement-adjudication discipline.

## 4. Sequencing within v1.0 development

1. **Lock case-set** (n = 30; build on the 14 anchors in
   V1_EMPIRICAL_CASES_CANDIDATES.md). Partner action.
2. **Build evidence dossiers** for all 30 cases. Claude-assisted
   from HBR + FT / WSJ / Bloomberg archives via web-search; partner
   verifies each dossier before coding.
3. **AI-first-pass coding** by Claude using the dossier. Output: 30
   coded rows per the 5-variable schema above.
4. **Partner verification** of the AI coding. Disagreements logged
   per case; if disagreement rate > 20%, escalate to dual-coder mode
   for the publication version.
5. **Statistical pass** in R or Python (Fisher's exact + Cramér's V
   + 95% CI). 30 minutes of analyst time.
6. **v1.0 §7 rewrite**: replace illustrative §7 examples with the
   full empirical cases (~1.5-2 pages each; the most empirically
   anchored 10-12 cases get full prose treatment; the remaining
   18-20 cases are summarised in a results table + supplementary
   material).
7. **v1.0 §8 results paragraph**: state the test outcome on Cells 1,
   2, 3; report effect size + 95% CI; discuss falsifying-criterion
   pass-or-fail.

## 5. Risks + mitigations

- **Coding-bias risk**: any tier-level coding requires interpretive
  judgment; LLM coders may anchor on the algebra's predictions and
  produce confirming coding bias. *Mitigation*: dossier-driven coding
  (coder sees evidence not the predicted answer); inter-coder
  reliability check on a 20% subset.

- **Cherry-picking risk**: starting from the V1_EMPIRICAL_CASES_CANDIDATES
  list anchors the corpus on cases the algebra was developed against.
  *Mitigation*: extend the n = 14 anchor set to n = 30 by adding 16
  cases drawn from a *pre-registered random sample* of HBR M&A cases
  with the algebra's coders blinded to which cases are anchors vs
  random-extension.

- **Selection bias for failure cases**: M&A literature over-reports
  failures and under-reports successes; this biases the failure-
  pathway incidence rate upward. *Mitigation*: stratify the
  random-extension sample by post-deal performance (50% successes
  by share-price reaction at 3-yr / 50% failures).

- **Tier-level inference risk**: documented cases describe deals in
  practitioner vocabulary (asset deal, share sale, merger), not in
  the algebra's tier-level transfer content. *Mitigation*: the
  v0.1.2 §6 per-row narrative supplies the mapping; the per-case
  evidence dossier explicitly applies this mapping with verbatim
  excerpts.

- **Statistical power risk**: if true effect size is small, n = 30
  may fail to detect. *Mitigation*: pre-specify the corpus extension
  to n = 50 as the trigger if Fisher's exact at n = 30 returns
  0.05 ≤ p < 0.20.

## 6. Companion artefacts

- `V1_EMPIRICAL_CASES_CANDIDATES.md` — the case-set list this protocol
  applies to.
- `raw/DR_EMPIRICAL_Q*_*.md` — supporting deep-research data per case.
- `VERIFICATION_REPORT_2026-05-19.md` — Perplexity verification of
  the 37 cross-engine VERIFIED-X lit-review candidates plus row-1b/10
  craftsman-case candidates.
- (FUTURE) `EVIDENCE_DOSSIERS/<case>.md` — one file per case in the
  locked v1.0 corpus.
- (FUTURE) `CODING_RESULTS.csv` + `STATISTICAL_ANALYSIS.md` — the
  output of the coded pass.

## 7. Partner decisions LOCKED 2026-05-19

All five open questions answered. Locked decisions:

1. ✓ **Protocol choices in §3** — accepted; most academically robust
   path at each dimension.
2. ✓ **n = 30 → 50 escalation rule** — accepted; pre-registered as
   the conditional fallback.
3. ✓ **AI coder identity + triple-coding** — Claude + Gemini + Grok
   majority-vote-or-flag; partner adjudicates disagreements.
4. ✓ **Pre-registration on GitHub** — `spectral-branding/[internal path omitted]
   empirical_cases_v1/PREREGISTRATION_V1.md` as SSOT (drafted this
   session); mirrored at `orgschema-papers/tier-bundle-algebra/
   PREREGISTRATION_V1.md` when the public scaffold lands. The
   pre-analysis commit's SHA + timestamp is the verifiable
   registered-before-data anchor.
   theoretical direction; backup [venue omitted] if[venue omitted]rejects.

The protocol is no longer at design-draft status; it is locked and
ready to execute against the 14 anchor + 13 comparator cases in
V1_EMPIRICAL_CASES_CANDIDATES.md. Next steps in execution order:

1. Land v0.2 paper (lit-review integration) and merge to main.
2. Land PREREGISTRATION_V1.md to GitHub with the pre-analysis commit.
3. Build the 30 case evidence dossiers (extend the 14 anchors by 16
   from HBR + FT archives + pre-registered random sample).
4. Triple-code the 30 cases via Claude + Gemini + Grok (Claude this
   session would NOT have access to the dossiers at runtime, so this
   is a future-session task; partner runs each model with the dossier
   in prompt; tracks per-case agreements + disagreements).
5. Adjudicate disagreements; finalise coded dataset.
6. Run Fisher's exact on Cells 1, 2, 3 + Cramér's V + 95% CI.
7. Write up v1.0 §7 + §8 results section.

## 8. Pilot-informed amendment (2026-07-29)

**Transparency note.** This section amends the locked protocol *after* a small,
explicitly-labeled pilot (`pilot/PILOT_CASE_CODING_2026-07-29.md`, coded dataset +
deterministic analysis script in `pilot/`). The pilot is a single-coder, n = 8,
knowledge-based exercise — NOT the pre-registered analysis, and NOT an inference
test. It was run to confirm the coding scheme is operable and to surface coding
refinements. The two refinements below were derived from the pilot and are folded
in *before* the pre-registered n = 30 analysis is run, so they precede rather than
follow the confirmatory data. Recording them here, dated, preserves the
registered-before-data discipline: the pilot informs the design; the n = 30
program remains the confirmatory test. The pilot did NOT alter the P6 hypotheses,
the falsifying criterion, or the statistical test — those stay exactly as locked
in §3–§4.

**Amendment A — cascade-gap-mitigation moderator.** Add, per case, a binary code
`gap_mitigated ∈ {yes, no, NA}`: was a documented cascade gap contractually
absorbed at closing (a transitional-services or operating agreement allocating the
shared substrate)? The pilot's eBay–PayPal case had a real Tier-5 gap that produced
no failure because an operating agreement absorbed it — a managed gap and an
unmanaged gap are not the same risk, and pooling them biases the P6 test toward the
null. The confirmatory P6 test is run on the full sample as locked; the moderator is
reported as a pre-specified secondary stratification (unmanaged-gap subset vs. full
sample), NOT as a new primary hypothesis.

**Amendment B — explicit non-cascade failure channels.** Code Tier-1-archetype
incoherence (e.g. an announced merger-of-equals executed as one-sided dominance) and
Tier-2-business-model incompatibility as failure channels **distinct** from the
φ4→φ6 cascade the P6 predictions target. The pilot's two largest failures
(Daimler–Chrysler, T1/T6; AOL–Time Warner, T2) sit outside the cascade P6 addresses;
without separating these channels a coder could mis-attribute a non-cascade failure
to a cascade gap (or, conversely, read cascade-conformance as predicting success).
This refines coding class C (failure-pathway incidence) in §1; it does not change the
P6 cells, which remain defined on the φ4→φ5 and φ5→φ6 boundaries only.

Both amendments are additive coding columns; neither relaxes the falsifying criterion
or the confirmation threshold in §4.
