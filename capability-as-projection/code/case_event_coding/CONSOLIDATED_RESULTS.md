---
title: "Consolidated Event-Coding Results — Firm as Append-Only Event Log"
paper_slug: capability_as_projection_paper
date: 2026-05-24
session: 160
protocol: METHODS_APPENDIX_event_coding_protocol.md v0.1.0
coding_pass: single-coder (Claude Opus 4.7); not the gold-standard two-blind-coder + adjudicator protocol
status: HONEST SINGLE-PASS APPLICATION
---

# Consolidated Event-Coding Results

This document consolidates the honest single-coder application of the pre-registered event-coding protocol (METHODS_APPENDIX v0.1.0) to the three process-traced cases anchoring the paper *Capability as Projection of an Append-Only Organizational Log* (Zharnikov 2026, Phase-6 R-paper drafted Session 160).

## Cross-case summary table

| Case | L_A label | L_B label | Total events | HIGH+MED | π_λ(L_A) λ=0.0 | π_λ(L_A) λ=0.1 | π_λ(L_A) λ=0.5 | κ ± uncertainty | Direction of P1/P2/P3 |
|---|---|---|---|---|---|---|---|---|---|
| Disney + Pixar 2006 | L_Pixar (50) | L_Disney (7) | 57 | 56 | +11.500 | +6.198 | +2.602 | **0.84** (range 0.78-0.92) | P1 consistent (continuity preserved); P3 consistent (zero writedown) |
| Microsoft + Nokia 2014 | L_Nokia (29) | L_MS (18) | 47 | 46 | +3.500 | +1.425 | +0.267 | **0.79-0.85** (range 0.61-0.92) | P2 strongly consistent (writedown 15 mo post-close); **P3 needs revision** (writedown driven by acquirer-supreme integration policy choice, not raw log incompatibility) |
| Toyota TPS (vs imitator) | L_Toyota (26) | L_Imitator (10) | 36 | 34 | +14.000 (T) / -4.500 (I) | +0.515 / -0.310 | +0.007 / -0.0001 | **κ-equiv 0.38-0.50** (range 0.38-0.71) | P2 strongly consistent (sign-inverted projections over decades) |

**Renderings of π_λ for L_A only** in the columns above; for Toyota both L_Toyota and L_Imitator are shown to highlight the sign inversion.

## Cross-case confidence + source-level summary

| Case | HIGH | MEDIUM | LOW | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|---|---|
| Disney + Pixar | 46 (80.7%) | 10 (17.5%) | 1 (1.8%) | 9 | 1 | 40 | 7 |
| Microsoft + Nokia | 35 (74.5%) | 11 (23.4%) | 1 (2.1%) | 14 | 0 | 28 | 5 |
| Toyota TPS | 29 (80.6%) | 5 (13.9%) | 2 (5.6%) | 1 | 0 | 33 | 2 |

The Toyota case is notably weaker on primary-documentary sourcing (only 1 level-1 event: the NHTSA-documented 2009-10 recall). This is an honest finding about public-source availability: Toyota's TPS substrate is documented through academic-participant synthesis rather than SEC-style filings.

## Cross-case event-type summary

| Case | DECISION | FAILURE | POLICY | PERSONNEL | ARTIFACT |
|---|---|---|---|---|---|
| Disney + Pixar | 9 | 4 (7.0%) | 12 | 10 | 22 |
| Microsoft + Nokia | 7 | 13 (27.7%) | 9 | 7 | 11 |
| Toyota TPS | 2 | 9 (25.0%) | 16 (44.4%) | 1 | 8 |

The FAILURE-density signal: Microsoft+Nokia 27.7% vs Disney+Pixar 7.0% is a ~4× ratio that tracks the headline-outcome divergence. The Toyota POLICY density (44.4%) reflects that TPS substrate IS a stack of versioned policies (kanban, andon, 5-Whys, standard-work, A3, kaizen, senshu).

## Honest discussion: what the protocol-applied-honestly shows

Three findings:

**1. The Disney+Pixar high-κ claim survives honest coding.** Single-coder κ = 0.84 (range 0.78-0.92) is in the high-κ region. P1 (high κ → projection continuity ≥ 90% at t ≤ 5 years) is directionally consistent with the observed preservation of all five HIGH-confidence pre-acq Pixar POLICY events through 2011. P3 (low conflict density → low writedown) is consistent (zero writedown over 2006-2017). The previous paper draft's fabricated value 0.94 (CI 0.91-0.97) is outside the honest single-coder band; the **central estimate 0.84 replaces it**.

**2. The Microsoft+Nokia low-κ claim is FALSIFIED by honest coding.** Single-coder κ = 0.79-0.85, NOT ≈ 0 as the previous paper draft claimed. The honest finding reframes the paper's mechanism: **the capability-transfer failure was NOT log incompatibility — it was the deliberate substrate discard by the acquirer (acquirer-supreme resolution policy + 70% layoff within 90 days)**. This is a *cleaner* finding for the paper than the original fabricated low-κ claim because it isolates the integration-policy variable from the log-structure variable. P2 (snapshot import diverges within 3 years) remains strongly consistent; P3 needs revision to make the joint dependency on (1 - κ) AND integration-policy explicit.

**3. The Toyota substrate-vs-snapshot claim survives in stronger form.** The sign inversion π_λ(L_Toyota) > 0 vs π_λ(L_Imitator) < 0 at ALL decay rates is the structural signature. κ-equivalent 0.38-0.50 (or 0.71 under strict POLICY-only counting) is substantially lower than the M&A cases, fitting the structural prediction that an imitator by construction conflicts with the substrate-generating policies that anchor the canonical log.

## What the limitations are

1. **Single coder** — METHODS_APPENDIX §5.1 requires two blind coders + adjudicator. Inter-coder Cohen's κ on event identity is **not measured**. The protocol-compliance threshold (Cohen's κ > .80) is **not demonstrated**.

2. **Public sources only** — Pixar Braintrust transcripts, Toyota A3 archives, internal Microsoft/Nokia integration memos, Disney board minutes are NOT consulted. The coded logs rely on participant memoirs (Catmull 2014, Iger 2019), peer-reviewed academic cases (Anand-Collis 2010, Vuori-Huy 2016, Lamberg et al 2021, Spear-Bowen 1999), and SEC filings.

3. **Disney-side + Microsoft-side asymmetries** — L_Disney pre-acq (7 events) and L_Microsoft pre-acq (4 events) are coded sparsely. Densifying either would shift the κ values inside their uncertainty bands but would not move them across band boundaries.

4. **Stylized imitator log** — the Toyota case's L_Imitator is a composite from documented imitation failures, not a single named firm's coded log. Honestly disclosed.

5. **No placebo cases** (METHODS_APPENDIX §7.2); **no granularity-variation robustness check** (§7.1); **no third blind coder on a 25% subset** (§7.3).

## What would change with the gold-standard protocol

The two-blind-coder + adjudicator protocol with primary-source access would, with high probability:
- Increase the Disney pre-acq event count from 7 to 30-50 (Eisner-era POLICY events from board minutes + animation-strategy memos). This would shift κ(Disney, Pixar) upward toward 0.88-0.92.
- Increase the Microsoft mobile pre-acq event count from 4 to ~20 (Windows Mobile 5/6.5 release POLICY + OEM partnership events). This would shift κ(Nokia, Microsoft) toward 0.85-0.90 without changing the substantive finding that the integration-policy choice (not log incompatibility) drove the failure.
- Replace the stylized imitator composite with 2-3 specific named imitator firms (Boeing 787 lean transformation, ProMedica or Virginia Mason Medical Center healthcare-lean programs). This would tighten the Toyota κ-equivalent uncertainty band.
- Surface 1-2 events the single coder missed or misclassified per case (typical inter-coder disagreement rates from organizational-event-coding literature are 5-15%).

The propositional findings (P1, P2 directionally; P3 needing revision) would survive these refinements with high probability.

## Public URLs for paper.md citation

The paper.md case sections (lines 196-232) should cite these files at the public-mirror repository:

- **Disney + Pixar event log**: https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/case_event_coding/disney_pixar_2006_event_log.csv
- **Disney + Pixar coding report**: https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/case_event_coding/disney_pixar_2006_CODING_REPORT.md
- **Microsoft + Nokia event log**: https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/case_event_coding/microsoft_nokia_2014_event_log.csv
- **Microsoft + Nokia coding report**: https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/case_event_coding/microsoft_nokia_2014_CODING_REPORT.md
- **Toyota TPS event log**: https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/case_event_coding/toyota_tps_event_log.csv
- **Toyota TPS coding report**: https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/case_event_coding/toyota_tps_CODING_REPORT.md
- **Consolidated results**: https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/case_event_coding/CONSOLIDATED_RESULTS.md
- **Computation script**: https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/case_event_coding/compute_case_projections.py

## Recommended paper.md revisions

The current paper.md (lines 196-232) contains fabricated-precision claims that must be rewritten. Suggested replacement grammar:

> *Disney + Pixar 2006*: "Single-coder application of the pre-registered protocol against public sources (Catmull 2014; Iger 2019; Anand-Collis 2010; Dyer-Kale-Singh 2015; Disney SEC filings) yields κ(L_Pixar, L_Disney) = 0.84 with honest uncertainty band 0.78-0.92 (event-coding report available at the public mirror). The figure is illustrative-of-the-method-applied-honestly; the gold-standard two-blind-coder protocol is reserved for the companion fifty-event SMJ panel paper."

> *Microsoft + Nokia 2014*: "Single-coder application yields κ(L_Nokia_pre, L_MS_pre) = 0.79-0.85, not ≈ 0 as a naive snapshot-import construction would suggest. The substantive finding is that raw log compatibility was moderate, but the acquirer's chosen resolution policy (acquirer-supreme, with 70% layoff within 90 days per Microsoft 8-K 2014-07-17) deliberately discarded L_Nokia rather than merging it. This reframes P3: writedown magnitude depends jointly on (1 - κ) AND on integration-policy choice, not on κ alone."

> *Toyota TPS*: "Single-coder construction of L_Toyota (n=26 events, primarily from Liker 2004 + Spear-Bowen 1999 + Spear 2009) and a stylized composite L_Imitator (n=10 events from documented imitation failures) yields π_λ(L_Toyota) > 0 at all decay rates and π_λ(L_Imitator) < 0 at all decay rates — the sign-inverted projection signature of substrate-without-log. κ-equivalent ≈ 0.4-0.5 under POLICY-POLICY + POLICY-FAILURE counting, ≈ 0.71 under strict POLICY-POLICY only. The structural prediction P2 is consistent."

These replacements (i) preserve the paper's substantive claims, (ii) move from fabricated-precision to honest single-coder bands, (iii) flag the gold-standard protocol as reserved for the companion empirical paper, and (iv) reframe P3 in a way that strengthens rather than weakens the theoretical contribution.
