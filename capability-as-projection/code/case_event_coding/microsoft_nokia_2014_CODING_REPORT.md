---
title: "Microsoft + Nokia 2014 — Event Coding Report"
case: Microsoft + Nokia Devices & Services 2014 acquisition
focal_event: 2014-04-25 (acquisition close)
focal_query: "capability:mobile-platform-development"
log_window_nokia: 1992-06 to 2014-04 (~22 years; pre-acq slice ends 2013-09-03)
log_window_microsoft: 2000 to 2017 (mobile-only sub-log; pre-acq slice ends 2013-09-03 with 4 events)
protocol_version: METHODS_APPENDIX_event_coding_protocol.md v0.1.0
coding_pass: single-coder (Claude Opus 4.7), 2026-05-24
status: HONEST SINGLE-PASS — not the gold-standard two-blind-coder + adjudicator protocol
---

# Microsoft + Nokia 2014 — Event Coding Report

## Sources consulted

1. Vuori, Timo O., and Quy N. Huy (2016), "Distributed Attention and Shared Emotions in the Innovation Process: How Nokia Lost the Smartphone Battle," *Administrative Science Quarterly* 61(1), 9-51. **Source level 2** (peer-reviewed academic study based on 76 interviews with named Nokia executives + middle managers; primary testimonial through ASQ research protocol).
2. Lamberg, Juha-Antti, Sandra Lubinaite, Jukka Ojala, and Henrikki Tikkanen (2021), "The Curse of Agility: The Nokia Corporation and the Loss of Market Dominance in Mobile Phones, 2003-2013," *Business History Review* (verified venue per Phase-4 fix plan; not *Industrial and Corporate Change* as originally cited). **Source level 3** (peer-reviewed historiographic case).
3. Microsoft Corporation 8-K filings: 2013-09-03 (Nokia D&S acquisition announcement), 2014-02-04 (Nadella appointment), 2014-04-25 (acquisition close), 2014-07-17 (18,000-person layoff), 2015-06-17 (Elop departure), 2015-07-08 ($7.6B writedown), 2016-05-25 (feature-phone divestment). **Source level 1** (primary documentary SEC filings).
4. Microsoft Corporation 10-K filings FY2011-FY2017. **Source level 1** (primary documentary SEC filings).
5. Nokia Corporation 20-F SEC filings FY2010-FY2013 + 6-K filings 2011-02-11 and 2013-09-03. **Source level 1** (primary documentary; Nokia was SEC-registered through ADR program).
6. Engadget + Wall Street Journal coverage of leaked Elop "Burning Platform" memo (2011-02-09). **Source level 4** (trade media; flagged in CSV).
7. Industry-tracker data (IDC + Gartner) for Windows Phone share. **Source level 4** (flagged).

## Coding pass description

Single-coder pass by Claude Opus 4.7 against METHODS_APPENDIX v0.1.0. The two-blind-coder + adjudicator gold standard (§5.1) was **not achieved** here; this is honest single-pass coding intended to seed future inter-coder work.

Prefix discipline: Nokia events use `NOK`, Microsoft events use `MSF`. The Nokia log is densely populated through the Vuori-Huy 2016 ASQ case study + Lamberg et al 2021 historiographic case; the Microsoft mobile pre-acquisition log is sparse because Microsoft's documented mobile-substrate pre-2014 is genuinely thin (Pocket PC 2000, Windows Mobile 2003, Windows Phone 7 launch 2010-2011) and the deeper substrate question is hardware-software co-design at scale, which Microsoft's pre-acquisition log does not contain. This sparseness is not coder underinvestment — it is the empirical finding the case is built around.

Per METHODS_APPENDIX §3 (minimum temporal depth ≥10 years): Nokia D&S has 22 years of mobile-substrate log; Microsoft mobile has ~14 years of (thinner) mobile-substrate log. Both qualify.

## Confidence-distribution summary

| Confidence | Count | Percentage |
|---|---|---|
| HIGH | 35 | 74.5% |
| MEDIUM | 11 | 23.4% |
| LOW | 1 | 2.1% |
| **Total** | **47** | 100% |

Tests of propositions use HIGH + MEDIUM events (46 events; 97.9% of coded log).

## Source-level distribution

| Level | Count | Notes |
|---|---|---|
| 1 (primary documentary) | 14 | Microsoft 8-K filings (×7), 10-K filings (×3), Nokia 20-F filings (×3), Nokia 6-K filings (×1) |
| 2 (primary testimonial) | 0 | Vuori-Huy 2016 ASQ is treated as level 3 here (peer-reviewed academic case using interview data; the interviews are level 2 inputs but the published case is the level-3 derived product) |
| 3 (secondary authoritative) | 28 | Vuori-Huy 2016, Lamberg et al 2021, peer-reviewed academic cases |
| 4 (tertiary: press, trade media) | 5 | Engadget/WSJ leak; press coverage of Symbian^3 reception; press coverage of Elop role narrowing; press coverage 2011 N9; trade-press characterizations |

Level-4 events are flagged in the CSV; per protocol §5.2 they appear in narrative but are excluded from κ tests.

## Event-type distribution

| Type | Count | Percentage |
|---|---|---|
| FAILURE | 13 | 27.7% |
| ARTIFACT | 11 | 23.4% |
| POLICY | 9 | 19.1% |
| DECISION | 7 | 14.9% |
| PERSONNEL | 7 | 14.9% |

The FAILURE-heavy distribution (27.7%) is the structural signal of the case: Nokia's substrate erosion (NOK09, NOK11, NOK12, NOK13, NOK20, NOK23, NOK24, NOK25) and Microsoft's integration failures (MSF08, MSF10, MSF13, MSF16, MSF17, MSF18) dominate the event landscape. By contrast, the Pixar coding (Disney+Pixar report) shows only 4 FAILURE events out of 57 (7.0%). The asymmetry is informative: ~4× higher FAILURE-event density in the Microsoft+Nokia substrate.

## Projection π_λ computation

Render time t = 2014-04-25 (acquisition close). Query q = `capability:mobile-platform-development`. Restricted to L_Nokia (29 events).

| λ (decay yr⁻¹) | π_λ(L_Nokia, q, 2014-04-25) | Interpretation |
|---|---|---|
| 0.0 | 3.500 | Net positive but barely; positive POLICY/DECISION events offset by FAILURE events from 2007 onward |
| 0.1 | 1.425 | Recent FAILURE events (NOK20-NOK25, 2011-2013) dominate; near-zero net signal |
| 0.5 | 0.267 | Effectively flat capability projection at acquisition close |

The decay-dependent collapse from 3.500 → 0.267 between λ=0.0 and λ=0.5 is the substrate-projection signature of substrate erosion: a Toyota-style stable substrate would show the projection roughly *stable* across λ values (deep cumulative weight at all decay rates), while Nokia's projection collapses at higher λ because the most-recent substrate events are net-negative.

## Compatibility κ(L_Nokia, L_Microsoft)

Pre-acquisition slice: L_Nokia (29 events with timestamp ≤ 2013-09-03, HIGH/MEDIUM only) and L_Microsoft (4 events, HIGH/MEDIUM only).

**Conflict identification** (METHODS_APPENDIX §6.1):

POLICY-POLICY conflicts on `capability:mobile-platform-development`:
1. (NOK04 Symbian consortium open-OS model, MSF03 Windows Phone 7 closed-platform model): direct incompatibility on OS-platform governance.
2. (NOK14 Symbian Foundation open-source model, MSF03 WP7 closed-platform model): direct incompatibility.
3. (NOK16 MeeGo open-source partnership model, MSF03 WP7 closed-platform model): direct incompatibility.
4. (NOK27 Symbian-era HW-SW co-design cadence, MSF03 WP7 closed-platform model): incompatibility on hardware-software integration locus.

Implicated POLICY events: NOK04, NOK14, NOK16, NOK27 (Nokia side) + MSF03 (Microsoft side) = 5 events.

PERSONNEL-PERSONNEL conflicts: NONE in the pre-acq slice (Elop appointment NOK17 in 2010 is unilateral on Nokia side; no Microsoft personnel events in same window with conflicting role).

ARTIFACT-ARTIFACT conflicts: Symbian codebase (NOK15) and Windows Phone 7 codebase (MSF04) are mobile OS artifacts under conflicting schemas. This would be a 6th + 7th implicated event under a strict reading of §6.1 ARTIFACT-ARTIFACT, but the script's current operationalization counts only POLICY-POLICY + PERSONNEL-PERSONNEL conflicts. Manual narrative count: +2 events implicated; revised κ = 1 - 7/33 = 0.788.

**Computed κ** (HIGH+MEDIUM, POLICY+PERSONNEL conflicts only via script): κ(L_Nokia_pre, L_MS_pre) = 1 - 5/(29+4) = **0.848**

**Including ARTIFACT-ARTIFACT conflicts** (narrative extension): κ = **0.788**

**Honest uncertainty band**:

- **Central estimate**: **κ = 0.79-0.85** (script-only vs script+narrative ARTIFACT conflicts)
- **Lower bound** (~0.70): if every Symbian-era hardware-software POLICY event (NOK06, NOK07, NOK08, NOK09 alongside NOK04/14/16/27) is counted as conflicting with MSF03 (since the entire pre-2010 Nokia substrate is structurally incompatible with the WP7 model), implicated count rises to ~13 events, denominator ~33, κ ≈ 0.61. Most coders would not be this aggressive.
- **Upper bound** (~0.92): if a denser Microsoft mobile pre-acquisition log is coded (Windows Mobile 5/6.5 era POLICY events, Pocket PC OEM relationships, Zune team transitions), the Microsoft denominator could grow to ~15-20 events without adding many same-query conflicts, raising κ to ~0.90.

**The headline finding**: κ(Nokia, Microsoft) on raw log compatibility is in the **0.70-0.90** band — **NOT** near zero as the original fabricated paper draft claimed. The original fabricated κ ≈ 0.08 (95% CI .05-.12) is **falsified by honest single-coder protocol application**.

## The corrected substantive finding

The honest computation reveals that the paper's argument needs **structural reframing**:

The previous paper draft claimed "κ ≈ 0 by snapshot-import construction." That conflated two different κ values:
1. **Raw log-compatibility κ(L_Nokia, L_Microsoft)** = 0.79-0.85. The two logs are NOT mutually contradictory at the structural level; many Nokia substrate events do NOT conflict with anything in Microsoft's pre-acq log because Microsoft's pre-acq log is sparse.
2. **Post-merge effective κ_eff** = κ(L_Microsoft, L_M_post) where L_M_post is the actually-realized merged log. By choosing acquirer-supreme resolution (MSF08: 70% layoff of Nokia D&S employees within 90 days of close; MSF09: hardware-software co-design POLICY not preserved; MSF18: Espoo R&D curtailed), Microsoft *discarded* most of L_Nokia rather than merging it. The effective post-merge log L_M ≈ L_Microsoft + a thin Lumia-product snapshot, with raw κ between L_Microsoft and this stripped-down merged log near 1.0 (no conflicts because L_Nokia substrate is no longer present).

**The capability-transfer failure mechanism is NOT log incompatibility — it is the deliberate substrate discard by the acquirer.** This is a *cleaner* finding for the paper than the original fabricated low-κ claim, because it isolates the integration-policy variable from the log-structure variable. The two logs *could* have been merged with moderate substrate preservation (κ in the 0.79-0.85 range supports this); the choice to discard L_Nokia was an integration-policy decision, not a log-mechanical inevitability.

This corrected framing maps cleanly onto FORMALISM §1.3 acquirer-supreme resolution policy: the integration produced a snapshot import, but the snapshot was a *choice* not a forced outcome.

## Per-proposition check (revised)

**P2 (snapshot import diverges within 3 years)**: writedown announced 2015-07-08 (15 months post-close); Lumia discontinued 2017 (3 years post-close); Windows Phone share collapse from 3% to <0.5% over 2014-2017. P2 is **strongly consistent with the case**. The mechanism is the acquirer-supreme resolution policy + 70% layoff (MSF08) discarding L_Nokia substrate rather than raw log incompatibility.

**P3 (writedown magnitude monotonic in 1 - κ)**: with corrected κ = 0.79-0.85, 1 - κ ≈ 0.15-0.21. Observed writedown / purchase price = $7.6B / $7.2B = 1.06. This is a much **steeper** writedown than the corrected (1 - κ) would predict on a linear log-mechanical relationship. **P3 as stated needs revision**: writedown magnitude is driven jointly by (1 - κ) AND by integration-policy choice (acquirer-supreme vs negotiated). The paper's proposition P3 should be rewritten to make this two-factor dependency explicit.

## Scope caveats

1. **Single coder** — gold-standard two-blind-coder + adjudicator protocol not executed.
2. **Public sources only** — Microsoft internal integration playbooks, Nokia internal Symbian-vs-MeeGo decision memos, Espoo-Redmond engineering coordination minutes are NOT consulted.
3. **Microsoft mobile log is genuinely sparse** — this is an empirical finding, not coder underinvestment. A coder commissioned to densify the Microsoft side would have ~10-15 additional ARTIFACT events (Windows Mobile 5/6.5/6.5.3 releases, HTC HD2 etc. OEM partnerships, Zune Phone cancellation) but few additional POLICY events that would conflict with NOK04/14/16/27.
4. **No placebo coding**; **no granularity-variation robustness check** per METHODS_APPENDIX §7.

## Files

- Event log: `microsoft_nokia_2014_event_log.csv` (this directory)
- Computation script: `compute_case_projections.py` (this directory)
