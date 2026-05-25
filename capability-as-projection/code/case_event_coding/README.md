# Case Event Coding — Firm as Append-Only Event Log

Honest single-coder application of the pre-registered event-coding protocol (v0.1.0, reproduced in full in `METHODS_APPENDIX_event_coding_protocol.md`) to the three process-traced cases anchoring Zharnikov (2026) *Capability as Projection of an Append-Only Organizational Log*.

## Status

**Single-coder pass by Claude Opus 4.7 on 2026-05-24.** This is NOT the gold-standard two-blind-coder + adjudicator protocol the METHODS_APPENDIX §5.1 specifies. It is honest application of the protocol's structural rules (taxonomy, source hierarchy, confidence ratings, conflict detection) by a single coder, intended to (i) supply honestly-computed values for the case-level propositions, and (ii) seed a future inter-coder pass.

## File index

| File | Purpose |
|---|---|
| `disney_pixar_2006_event_log.csv` | 57-event coded log: 50 Pixar (1986-2019) + 7 Disney (1985-2006) |
| `disney_pixar_2006_CODING_REPORT.md` | Sources, confidence distribution, projection π_λ, κ = 0.84 ± uncertainty |
| `microsoft_nokia_2014_event_log.csv` | 47-event coded log: 29 Nokia (1992-2013) + 18 Microsoft (2000-2017) |
| `microsoft_nokia_2014_CODING_REPORT.md` | Sources, confidence, π_λ, κ = 0.79-0.85 ± uncertainty + corrected P3 framing |
| `toyota_tps_event_log.csv` | 36-event coded log: 26 Toyota canonical + 10 stylized imitator composite |
| `toyota_tps_CODING_REPORT.md` | Sources, π_λ sign inversion, κ-equivalent = 0.38-0.50 |
| `compute_case_projections.py` | Reproducible script: parses CSVs, computes π_λ at λ ∈ {0.0, 0.1, 0.5}, computes κ |
| `CONSOLIDATED_RESULTS.md` | Cross-case table + honest scope discussion + paper.md replacement-text suggestions |

## Reproducibility

```
cd code/case_event_coding/
python3 compute_case_projections.py
```

The script is deterministic. It loads the three CSVs, applies the formalism from `FORMALISM_v0.md` (π_λ weighted prefix sum with exponential decay; κ = 1 − |implicated events| / (|L_A| + |L_B|)), and prints per-case event counts, confidence/source-level/type distributions, π_λ values at three decay rates, and κ values restricted to HIGH+MEDIUM events.

Anyone with access to the same public sources (Catmull 2014, Iger 2019, Anand-Collis 2010, Dyer-Kale-Singh 2015, Disney/Microsoft/Nokia SEC filings, Vuori-Huy 2016 ASQ, Lamberg et al 2021 *Business History Review*, Liker 2004, Spear-Bowen 1999 HBR, Spear 2009) should be able to **roughly reproduce the event counts** within ±5-15% per case (typical organizational-event-coding inter-coder variability). Exact event-by-event matching requires the published per-event source citations in the CSV `source_citation` column plus an adjudicator-resolved coding session.

## Honest limits

1. **Single coder, not two-blind + adjudicator.** Inter-coder Cohen's κ on event identity is not measured.
2. **Public sources only.** Internal records (Pixar Braintrust transcripts, Toyota A3 archives, Microsoft integration playbooks) are not consulted.
3. **The Toyota L_Imitator is a stylized composite**, not a single named firm.
4. **No placebo cases** (METHODS_APPENDIX §7.2 robustness check not performed).
5. **No granularity-variation robustness check** (§7.1 not performed).
6. **No third-coder 25% blind subset** (§7.3 not performed).

These limits are explicit in each per-case CODING_REPORT.md "Scope caveats" section and consolidated in `CONSOLIDATED_RESULTS.md`. The companion fifty-event SMJ panel paper (described in paper.md "Future Research" discussion) is the planned venue for the gold-standard protocol application.

## Headline numbers

| Case | κ central estimate | Honest range | Direction of propositions |
|---|---|---|---|
| Disney + Pixar 2006 | 0.84 | 0.78-0.92 | P1, P3 consistent |
| Microsoft + Nokia 2014 | 0.82 (script 0.85; +ARTIFACT 0.79) | 0.70-0.92 | P2 consistent; P3 needs revision (joint dependency on integration-policy) |
| Toyota TPS | 0.40 (κ-equivalent) | 0.38-0.71 | P2 strongly consistent (sign-inverted π_λ at all λ) |

The current paper.md (lines 196-232) contains placeholder values that this coding pass updates with honest single-coder estimates. See `CONSOLIDATED_RESULTS.md` "Recommended paper.md revisions" for replacement text.
