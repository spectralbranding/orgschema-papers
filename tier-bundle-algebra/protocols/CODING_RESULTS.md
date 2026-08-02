# Coding + analysis results — Tier-Bundle Algebra n=30 pre-registered pass

**Executed 2026-07-29** (triple-coding phase per `NEXT_SESSION_TRIPLE_CODING_PHASE.md`).
Pre-registration: `PREREGISTRATION_V1.md` (Amendments 1-6). Registered-before-data
chain intact: the harness (`triple_code_dossiers.py`) and the empty
`coded_dataset_n30.csv` schema were committed **before** any coded datum existed
(commit `4f845761`); the analysis pipeline (`analyze_study_n30.py`) was committed
earlier still, self-validated on a synthetic fixture with a known Fisher's-exact
value.

This document reports the outcome **honestly**, applying the pre-registered
thresholds and the §7 falsifying-direction commitment (`PREREGISTRATION_V1.md`).

## 1. Coding procedure as executed

- **Coders**: three independent AI coders — Claude (`claude-opus-4-8`), Gemini
  (`gemini-3.1-pro-preview`), Grok (`grok-4.3`) — each shown **only** the evidence
  dossier, never the paper, the pre-registration, the hypotheses, the predicted
  direction, or the anchor-vs-extension status of the case (blinding per
  `CASE_CODING_PROTOCOL.md` §5). Every call is logged as JSONL under `logs/`.
- **Cases coded**: 29 dossier files = the 30-case corpus (14 anchors, with
  Daimler-Chrysler serving both the share-sale and merger-of-equals rows, + 16
  extension). Per-case codes: `coding_raw/<case_id>_codes.json`.
- **Combination**: majority-vote-or-flag per cell (≥2 agree → majority; else FLAG).
- **Coverage**: 28 of 29 cases fully triple-coded. One case (A09
  Medtronic-Covidien, **H6-excluded** as a redomiciliation) has a truncated Gemini
  response and is coded by 2 of 3 coders; it never enters the confirmatory test.
  Gemini's free-tier rate-limiting and thinking-token truncation required a
  bounded-output retry; the JSONL logs record every attempt.

## 2. Inter-rater reliability

- **Fleiss' κ = .838** over the six binary cells (168 fully-rated coder-triples),
  "almost perfect" agreement — comfortably above the .70 target
  (`CASE_CODING_PROTOCOL.md` §3). Figure: `coding_raw/fleiss_kappa.png`; numbers:
  `coding_raw/fleiss_kappa.json`.
- **Flagged cells: 11 of 406 (2.7%)** — far below the 20% threshold that would
  escalate to dual-human coding for the publication version. **Every flagged cell
  is a descriptive class-A bundle-signature token** (`sigma_T2`, `sigma_T5`,
  `sigma_T3`, `sigma_T6`); **not one flag falls on an H6 confirmatory cell**
  (`gap_45`, `gap_56`, `p4_pathway`, `p5_pathway`). The three gap cases (A01, A03,
  A04) were coded **unanimously** by all three coders on every H6 cell.
- Per-cell unanimous-agreement rate: `p5_pathway` 1.00, `t2_model` 1.00,
  `t1_archetype` .96, `gap_56` .93, `p4_pathway` .93, `gap_45` .89.

## 3. Adjudication

All 11 flagged signature tokens plus one unanimous-uncertain H6 cell were
adjudicated by the author against the dossiers and logged in `ADJUDICATION.csv`
with a per-cell rationale:

- **E15 (Forest City / Brookfield) `gap_56`**: all three coders returned
  `uncertain` (the dossier marks T6 people-transfer detail `[UNVERIFIED]`).
  Adjudicated to **0 (no gap)** — the codebook's conservative rule codes
  absence-of-evidence-of-a-mismatch as 0 rather than guessing a gap into existence;
  the null-friendly direction. This was the only H6-relevant adjudication.
- The 11 signature-token adjudications affect the descriptive
  `coded_dataset_n30_full.csv` only, never the H6 test. Two JV-creation cases
  (A13 NUMMI, T2/T3) surfaced a genuine scheme boundary: the transfer-oriented
  signature alphabet has no clean token for "a new shared structure was created"
  rather than transferred — noted for the coding-scheme limitations.

Disagreement rate (2.7%) is well within tolerance; no escalation to dual-human
coding is triggered.

## 4. Confirmatory result (pre-registered primary tests)

H6-eligible corpus: **26 cases** (29 coded − A08 intra-business pivot, A09
redomiciliation, A10 founder wind-down; all excluded by case-class per §2).
Dataset: `coded_dataset_n30.csv`. Full run: `ANALYSIS_OUTPUT.txt`.

Descriptive base rates are low: `gap_45` present in 3/26, `gap_56` in 1/26,
`p4_pathway` in 2/26, `p5_pathway` in 1/26.

| Cell | 2×2 (gap×fail) | Fisher's exact *p* | Cramér's *V* | P(fail\|gap) [95% CI] | α | Reject |
|---|---|---|---|---|---|---|
| **H6a** φ₄→φ₅ | [[2,1],[0,23]] | **.009** | **.799** | .667 [.094, .992] | .025 | **yes** |
| **H6b** φ₅→φ₆ | [[1,0],[0,25]] | .039 | 1.000 | 1.000 [.025, 1.000] | .025 | no |
| **H6c** aggregate | [[2,1],[0,23]] | **.009** | **.799** | .667 [.094, .992] | .05 | **yes** |

**Pre-registered verdict: P6 is SUPPORTED, and NOT falsified.** H6a rejects
independence at the Bonferroni-corrected α = .025 with a large effect size
(V = .799 ≥ .30), meeting the pre-registered confirmation threshold
(`PREREGISTRATION_V1.md` §4); H6c rejects at α = .05. The falsifying criterion
(all three cells *p* ≥ .10) is not met.

### Honest reading of the strength of this result

The support is **real but fragile**, and must be reported as preliminary
confirmatory evidence rather than a settled finding:

1. **Very few gap cases.** The entire result rests on 3 cases with a φ₄→φ₅ gap
   (A01 Daimler-Chrysler, A03 3Com-Palm, A04 Facebook-FriendFeed), of which 2
   showed the P4 pathway. The 95% Clopper-Pearson interval on P(fail|gap) is
   enormous ([.094, .992]).
2. **What drives significance is specificity, not sensitivity.** 23 of 23 no-gap
   cases had no P4/P5 failure — perfect specificity in this sample — which is what
   makes Fisher's exact reject despite the tiny gap count. Sensitivity is only
   .667.
3. **H6b is a single data point.** Only one case (A01) carries a φ₅→φ₆ gap; it
   failed, giving V = 1.0 but *p* = .039, which does **not** clear the Bonferroni
   α = .025. H6b is not independently supported.
4. **The result is sensitive to gap operationalization.** The design-informing
   pilot (n = 8) had coded Daimler-Chrysler as cascade-*conformant* (a T1/T6
   failure outside the cascade) and found the association "weak and mixed." The
   blinded coders here, reading section-2 transfer content literally ("processes
   largely stayed separate" while product lines transferred whole), coded
   Daimler-Chrysler as a φ₄→φ₅ **and** φ₅→φ₆ gap. That single re-reading is much of
   the difference between the pilot's null-ish direction and this positive result —
   a genuine dependence on how "gap" is operationalized that the paper must state.

## 5. Secondary stratification (Amendment 3): unmanaged-gap subset

Recoding the one managed gap (A03 3Com-Palm, `gap_mitigated = yes`) as a non-gap
— the pre-registered unmanaged-gap view — **does not reject** independence:
H6a-unmanaged Fisher's *p* = .151, V = .458.

The reason is substantively informative and runs **against** the pilot's premise.
The pilot conjectured that a contractually mitigated gap should not produce a
failure, so pooling managed and unmanaged gaps biases the test toward the null.
But the single managed gap in the corpus (3Com-Palm's carve-out, where shared
services had to be stood up independently) **did** exhibit a P4 disruption
(`p4_pathway = 1`, unanimous). Recoding it as a non-gap therefore moves a
gap-*failure* into the no-gap-*failure* cell, breaking the perfect specificity and
weakening the association. The mitigation moderator did not behave as the pilot
predicted at n = 30; this is reported as a finding, not smoothed away.

## 6. What this means for the paper

- P6 is **supported by the pre-registered primary test** and this replaces the
  "designed but not executed / pilot only" language in Limitations and Future
  Research with the completed study's actual result.
- The result is **preliminary and fragile** (3 gap cases; wide CIs; H6b a single
  case; secondary stratification not rejecting; operationalization-sensitive). The
  paper reports it as confirmatory-but-preliminary evidence and retains every
  stated limitation, rather than over-claiming.
- No change to the paper's theoretical contribution, propositions, or falsifiers.
  The paper's publication status is unchanged (it remains held pending the
  unpublished-self-citation dependency; this empirical pass does not alter that).

## 7. Reproducibility

- `triple_code_dossiers.py` — coding harness (blinded triple-coder, majority vote,
  Fleiss κ, JSONL logging).
- `assemble_coded_dataset.py` — deterministic dataset assembly from `coding_raw/` +
  `ADJUDICATION.csv`.
- `analyze_study_n30.py` — pre-registered Fisher's-exact analysis + Amendment-3
  stratification (fixture self-check reproduces the textbook 3-1-1-3 value).
- Data: `coded_dataset_n30.csv` (H6-eligible), `coded_dataset_n30_full.csv` (all
  cases + per-coder codes + D/E), `coding_raw/` (per-case JSON + κ), `logs/`
  (per-call JSONL). Run command in each script's docstring.
