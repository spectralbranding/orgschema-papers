---
title: "Methods Appendix — Ex-Ante Event Coding Protocol"
version: v0.1.0
date: 2026-05-24
status: Pre-registered protocol for the empirical case-coding pass; published as part of the v1.0.0 Zenodo deposit.
---

# Methods Appendix: Ex-Ante Event Coding Protocol

This protocol is pre-committed BEFORE the empirical cases are written up, to address the post-hoc-coding circularity concern at the standard expected of theory papers with case-study empirical anchors. Coders must register adherence to this protocol; deviations must be flagged in the methods section of the final paper, not retrospectively justified.

## 1. Unit of analysis

The unit is the **organizational event**, defined as: a discrete, dated, attributable, immutable record in or about the focal organization, of a kind that (i) is at least in principle reconstructable by an independent third party from documentary or testimonial evidence, and (ii) plausibly bears on at least one organizational capability under study.

Excluded: unrecorded conversations, generalized "culture" claims unanchored to specific events, ex-post strategic rationalizations.

## 2. Event taxonomy T (fixed pre-coding)

Each event is assigned exactly one type from this taxonomy. The taxonomy is fixed before any coding begins. Refinement requires a new pre-registered protocol version.

### 2.1 Type categories (5 top-level types)

| Type τ | Definition | Examples |
|---|---|---|
| **DECISION** | A choice attributable to a named decision-maker among ≥ 2 documented alternatives. | Hiring decisions, acquisition approvals, market-entry approvals, SOP-revision approvals, kill-or-continue project decisions. |
| **FAILURE** | A negative outcome event recorded as such by the organization or by an independent third party. | Product recalls, lost contracts, missed shipments, public apologies, SEC enforcement actions, internal post-mortems labelled "failed." |
| **POLICY** | A versioned written commitment to a rule, procedure, or standard. | SOP-vN publication, code-of-conduct revision, board policy resolutions, published handbooks (GitLab is the modern reference case for fully visible POLICY events). |
| **PERSONNEL** | A named individual entering, exiting, or changing role. | Hires, departures, promotions, role-bundle changes (the "CEO assumes Chairman role" event). |
| **ARTIFACT** | A produced output that survives the event of its production and becomes part of the firm's substrate. | Code commits, patents granted, products shipped (with serial numbers), publications, brand assets registered. |

### 2.2 Excluded as event types

- General-tone-of-management observations
- Aggregate financial outcomes (these are renderings, not events; the events are the underlying decisions/failures/policies that produce the renderings)
- Reputational impressions absent specific recorded incidents
- Marketing or PR statements that do not bind future behaviour (announcements without follow-through; a public commitment that is later kept becomes a POLICY event)

### 2.3 Granularity rules

- **Minimum granularity**: a single decision, recorded action, or attributable change.
- **Maximum granularity**: aggregation up to a single fiscal quarter is permitted only for high-frequency low-significance events (e.g., "Toyota Q3 2018: 2,847 kaizen suggestions logged"). All DECISION, FAILURE, POLICY, and PERSONNEL events are coded at unit granularity.
- **Tie-breaking**: when ambiguity exists about whether two records reflect the same event or two events, code as **two events** unless they share id and timestamp in primary sources.

## 3. Minimum temporal depth

For an organization to be eligible as a process-traced case in this study, the log L must cover at least **10 calendar years** prior to the focal event under analysis (e.g., the M&A announcement date). Logs shorter than 10 years are excluded.

Rationale: capability transfer dynamics unfold over 3–5 years; the substrate that supports them must have at least double that window of accumulated events to be a meaningful object of study. Toyota TPS post-Ohno (1953 → present) has ~70 years; Pixar pre-Disney (1986 → 2006) has 20 years; Nokia D&S pre-Microsoft (1997 mobile-pivot → 2014 close) has 17 years; Microsoft mobile pre-Nokia has ~10 years. All four cases qualify.

## 4. Identifier discipline

Each event is assigned a stable **event id** within the case. Two coders working independently must agree on (i) whether two records refer to the same event (same id), and (ii) the canonical id for newly-coded events. Cohen's κ on event identity > .80 across blind coders is the threshold for protocol-compliant coding.

## 5. Coder protocol

### 5.1 Blind coding

Two coders independently code the same source materials without seeing each other's coding sheets until both are complete. Disagreements are surfaced and resolved by a third (blind) adjudicator. Final coded log is the adjudicator-resolved superset.

### 5.2 Source hierarchy

For each event, the coder records the source from which it was extracted. Sources are ordered by reliability:

1. **Primary documentary**: board minutes, SEC filings, court records, dated internal SOPs, version-controlled code repositories with commit timestamps, dated patent filings.
2. **Primary testimonial**: interviews with named participants conducted on the record by independent parties (HBS case authors, journalists with confirmed access).
3. **Secondary authoritative**: peer-reviewed academic case studies, HBS cases authored by recognized scholars, books by participants when corroborated by independent sources.
4. **Tertiary**: news media accounts, trade press, hagiography or critique published >5 years post-event.

Events sourced only from level 4 are flagged and excluded from any test of the propositions; they appear in narrative only.

### 5.3 Confidence rating

Each event carries a confidence rating ∈ {HIGH, MEDIUM, LOW}:
- **HIGH**: source level 1 or 2, two coders agree, no ambiguity in attribution.
- **MEDIUM**: source level 1–2, coders disagree initially but adjudicator-resolves to consensus.
- **LOW**: source level 3, single source, or unresolved coder disagreement (in which case the event is recorded but flagged).

Tests of the propositions use HIGH and MEDIUM events only. LOW events appear in narrative only.

## 6. Conflict-resolution policy taxonomy (κ measurement protocol)

For coding compatibility κ(L_A, L_B) in M&A cases, conflicts are identified pairwise:

### 6.1 Conflict definition

A conflict is a pair of events (e_A ∈ L_A, e_B ∈ L_B) such that merging both into a single log L_M produces an inconsistency that requires a resolution choice. Three formal conflict patterns:

- **POLICY-policy conflict**: e_A and e_B are both POLICY events specifying incompatible rules for the same domain (A: "merit-only promotion," B: "20% target diversity quota").
- **PERSONNEL-personnel conflict**: e_A and e_B both assign a named role to different individuals at the same effective date (A: "Jane = VP Sales effective 2014-Q1," B: "Bob = VP Sales effective 2014-Q1").
- **ARTIFACT-artifact conflict**: e_A and e_B produce artifacts under conflicting schemas (A: codebase commits to schema X; B: codebase commits to schema Y; merge requires migration).

### 6.2 Resolution policies (for κ-measurement reporting)

For each conflict, the coder records which resolution policy the acquiring organization chose:

- **LWW** (last-write-wins): later event wins; both logs continue to grow.
- **ACQUIRER**: A's event prevails.
- **TARGET**: B's event prevails.
- **NEGOTIATED**: new combined policy supersedes both; merged log accepts a new POLICY event with `caused_by` pointing to both originals.
- **DEFERRED**: conflict noted, neither resolved; both events sit in the merged log creating ongoing operational friction.

κ measurement excludes NEGOTIATED resolutions from the conflict count (they resolved cleanly); ACQUIRER, TARGET, and DEFERRED count toward conflicts. LWW depends on timestamp ordering; counted as conflict only if older event was operationally load-bearing.

## 7. Robustness checks (pre-registered)

The paper reports three robustness checks:

### 7.1 Event-granularity threshold variation

Re-code each case at two alternative granularities:
- **Coarsened**: aggregate same-month same-type same-actor events into single events. Test whether κ values are stable to ± 0.05.
- **Refined**: split aggregate events (e.g., quarterly kaizen counts) into per-month events. Test whether propositions P1–P3 hold qualitatively under refinement.

### 7.2 Placebo tests

Apply the coding protocol to two placebo cases where the propositions should NOT hold:
- A **routine supplier-contract renewal** with no capability-transfer dimension. The κ-writedown relationship should be absent or noisy.
- A **pure equity acquisition** (financial buyer, no operational integration intent). P1 and P2 should be silent because no projection-continuity claim is made.

Failure of the propositions in these placebos confirms specificity. Spurious confirmation in placebos suggests the operationalization is over-broad.

### 7.3 Blind coder variation

In addition to the primary two-coder + adjudicator protocol, a third blind coder independently codes a randomly-selected 25% of events from each case. Inter-coder Cohen's κ across the three coders > .75 is the protocol-compliance threshold. Lower values are reported transparently with a sensitivity analysis.

## 8. Identification strategy (for SMJ inferential claims)

Identification ranking:

### 8.1 Primary identification — regression discontinuity on acquirer prior M&A experience

For the 50-event coded panel (companion empirical paper if SMJ requests larger N), use prior M&A count as a forcing variable with a discontinuity at the median to identify a "learned log-preservation discipline" effect. Inheritance: Puranam, Powell & Singh (2006), SMJ 27(12), 1175-1197.

### 8.2 Secondary — propensity-score matching on observable log proxies

Observable proxies for log-quality at the time of deal announcement:
- Patent citation tree depth and density for both A and B
- Employee tenure distribution (deeper = older log, more durable substrate)
- Public-documentation surface area (handbook size, API doc surface, published SOP count where available)
- Executive average tenure at time of deal

Match acquirer-target pairs on these proxies; compare outcomes within matched pairs.

### 8.3 Tertiary — instrumental variables

Exogenous CEO death events or unexpected regulatory disclosure shocks that force log surfacing as candidate instruments for log-quality observability. Strong-instruments tests pre-required (first-stage F > 10).

### 8.4 Fallback

If the empirical strategy collapses under reviewer scrutiny, the paper converts to the AMR pure-theory version with the 3 process-traced cases as illustrative anchors only. The formalism alone is sufficiently novel for AMR.

## 9. Pre-registration

This protocol is pre-registered at `github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/METHODS_APPENDIX_event_coding_protocol.md` and time-stamped 2026-05-24. Modifications require an explicit changelog entry in this document with date and reason. The pre-registered version of this protocol is the one that ships with the final paper as Methods Appendix and as a separate file in the public-mirror `orgschema-papers/capability-as-projection/` repository.

## 10. Note on circularity defence

An anticipated reviewer objection: *"how would one independently identify and code the 'event log' without circularity to the outcomes being explained?"*

Defence stack:

1. **Event taxonomy T is fixed before coding** (§2). Cannot expand to fit cases.
2. **Source hierarchy** privileges primary records over post-hoc accounts (§5.2). Primary records pre-date outcomes by definition.
3. **Two-coder blind + adjudicator** protocol (§5.1, §7.3) defeats single-coder confirmation bias.
4. **Robustness checks** include placebo cases where propositions should fail (§7.2). Specificity is testable.
5. **Confidence ratings** transparently disclose where the coding is uncertain (§5.3). Tests use only HIGH/MEDIUM events.
6. **Pre-registration** (§9). The protocol is time-stamped before the empirical narrative is drafted.

Together these address the circularity concern at the standard expected of theory papers with case-study empirical anchors. The protocol does NOT eliminate all subjectivity in event identification (no protocol can); it makes subjectivity visible and measurable, which is what blind-coder κ > .80 operationalizes.

---

## Version

v0.1.0 (2026-05-24): Initial pre-registered version. Updates require an explicit changelog entry in this document.
