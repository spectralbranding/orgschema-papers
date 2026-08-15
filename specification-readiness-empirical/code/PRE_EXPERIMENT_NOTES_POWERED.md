# Pre-experiment notes — the POWERED zero-activity placebo (2026an, run 2)

**Written 2026-08-15, BEFORE the run.** Anti-HARKing register, in the same pattern as
`PRE_EXPERIMENT_NOTES.md` (run 1, 2026-08-09). Everything below is fixed before any run-2 result is
seen. The post-experiment report records what actually happened, including every deviation.

This is **run 2 of the same placebo**, not a new study. Run 1 is not superseded and is not re-run:
its verdict stands as INDETERMINATE, and this run exists because that verdict was underpowered.

## Why run 2 exists

Run 1 returned n = 30 zero-activity against n = 20 operating pairs, primary $d = -.457$ with Welch
$p = .065$ — an effect of moderate size that the design could not resolve. The pre-registered rule
called that INDETERMINATE and said in terms that "an underpowered null is not evidence of absence
and will not be written as one." Two facts make the re-run worth the cost and nothing else does:

1. **The direction reversed the paper's premise.** Boundary condition C7 and the Table 1
   "Realized operating history" row asserted that a zero-activity filer scores *high*. The empty
   panel scored *below* the operating panel in every arm. That correction has since been applied to
   the published paper, so run 2 is not deciding whether to correct — it is deciding whether the
   reversal is real.
2. **The candidate mechanism is measurable and is already visible.** Run 1's zero panel averaged
   4,447 MD&A words against 12,500 for the operating panel, and its length-stratified arm returned
   the largest effect in the study ($d = -.866$, $p = .036$) on 18 pairs. Document length and the
   share of the document that is boilerplate are therefore **the candidate mechanism, not nuisance
   controls**, and run 2 enters both explicitly rather than stratifying after the fact.

## What is unchanged from run 1, and may not be changed

The **measure**, exactly as published and exactly as run 1 computed it. Item 7 (MD&A) from the 10-K
primary document, non-narrative content stripped; **BERT-base-uncased**, pinned literally, never
resolved through the shared model registry; non-overlapping 512-token windows, document embedding =
mean of mean-pooled chunk embeddings; cosine rescaled from $[-1, 1]$ to $[0, 1]$. Secondary
bag-of-words cosine over the same two texts. Item 1 (Business) as the alternative-section arm.

Run 2 imports these functions from `zero_activity_placebo.py` rather than restating them, so that
"the measure is unchanged" is enforced by the code and not by a promise. **No threshold, no
preprocessing choice and no model substitution may change after a result is seen.**

## Power, and the target n

Run 1's primary effect was $d = -.457$. Two-sided $\alpha = .05$, equal groups:

| Target | n per panel |
|---|---|
| 80% power at $d = .457$ (run 1's estimate) | 76 |
| 80% power at $d = .40$ | 100 |
| 90% power at $d = .457$ | 101 |

**Target n = 100 usable firm-year pairs per panel**, which resolves run 1's own point estimate with
about 93% power and still has 80% power against an effect a fifth smaller. Run 1's binding
constraint was the *operating* panel (n = 20), not the zero panel, so run 2 targets the two panels
independently rather than letting one starve the other.

**If the population cannot supply 100.** The screens are not loosened to reach the number. The run
reports the achieved n, the power that n actually attains against $d = .457$, and — if n falls below
76 per panel — reports the result as **still underpowered**, in those words. Reaching a smaller n is
a fact about the population of structurally zero-activity filers; it is not a licence to redefine
the population.

## Panels — three pre-registered deviations from run 1, each with its reason

The screens are otherwise run 1's: SIC **6770 (Blank Checks)** plus **no revenue tag reporting a
nonzero value in either fiscal year** for the zero panel; a seeded random draw of 10-K filers with
**revenue above $50 million in both fiscal years** for the operating panel; a pair is usable only
when Item 7 is extractable from both filings at **200+ words** each; failures are counted and
reported, never silently dropped.

**Deviation 1 — both panels are restricted to fiscal years ending 2011 or later.** This corrects a
defect in run 1 rather than tuning it. The zero screen reads "no revenue tag reports a nonzero
value," and XBRL company-facts coverage only becomes universal with the 2009-2011 phase-in. For a
fiscal year before that, "no revenue reported" and "no data exists" are indistinguishable, so run 1's
2006 and 2010 pairs entered the zero panel on absent data rather than on reported zero revenue.
Three of run 1's thirty zero pairs are affected. The restriction also removes the reason the
operating panel could not be filled: it could never match a year in which no operating firm can pass
a revenue floor that requires XBRL to evaluate.

**Deviation 1 carries an integrity check that run 1 had no way to perform.** A firm enters the zero
panel only if it reports a `us-gaap:Assets` fact, in a 10-K, at **both** fiscal-year ends. A
post-2011 10-K filer reports Assets in XBRL; so if Assets is present and no revenue tag reports a
nonzero value, the zero is **reported** rather than **missing**. Firms failing this check are
counted under their own rejection reason and reported, not folded into the others.

**Deviation 2 — the operating panel selects the consecutive 10-K pair that matches a needed fiscal
year, instead of always taking the firm's most recent pair.** Run 1 drew a candidate, took its most
recent pair, and discarded the candidate when that year was already filled. Since most current
filers' most recent pair sits in 2024-2025 and the zero panel's years are spread across the decade,
that rule discarded almost everything and is why the operating panel stopped at 20. Selecting the
pair by the year that is needed is a *closer* reading of the paper's own words — "matched operating
firms in the same filing years" — not a looser one. The zero panel keeps most-recent-pair selection,
because the zero panel is what defines the target year distribution.

**Deviation 3 — the operating candidate pool is drawn from all four quarters of the EDGAR full
index, for each needed fiscal year and the year after it.** A 10-K for a fiscal year ending in
December is filed in the following calendar year, so run 1's year-`t` QTR1-3 draw systematically
missed the filings it was looking for. Mechanical fix to the draw; the screens on the drawn firms
are unchanged.

**Not a deviation, and checked rather than asserted: the screening transport.** Run 1 evaluated the
revenue screen with five `companyconcept` requests per fiscal year. Run 2 evaluates the identical
rule — same tag list, same 10-K / 10-K-A form filter, same 300-day duration filter, same
max-across-tags selection — against a single `companyfacts` payload, because eleven requests per
candidate does not scale to the number of candidates a powered panel needs. This changes the
transport and nothing else, and **`--build` proves it before it screens anything new**: it re-runs
run 1's own function against run 2's on all fifty of run 1's firm-years, every fetch a cache hit,
and **aborts** on a single disagreement. A transport change that cannot be shown to be one is a
measurement change.

Matching remains **on fiscal-year pair only**. Length is not matched, for run 1's stated reason —
length is plausibly part of the phenomenon — and run 2 goes further by entering it as a variable.

## The two mechanism variables, defined before they are computed

Both are computed identically for both panels, from the same two texts the outcome is computed
from, and both are reported as objects of interest rather than as controls to be partialled out and
forgotten.

**Document length.** $\text{length}_{i}$ = mean of the two MD&A word counts for the pair. Entered as
$\log$ length. Reported per panel as mean, median and range before any model is fitted.

**Boilerplate share.** Computed over the **union corpus**: every MD&A document from both panels and
both fiscal years, so neither panel sets its own threshold. Documents are lowercased and tokenized
to runs of two or more ASCII letters. Every 4-word sequence (tetragram) is enumerated per document.
A tetragram is **boilerplate** if it occurs in **at least 5% of the documents in the union corpus**.
A document's boilerplate share is the fraction of its tetragram positions occupied by boilerplate
tetragrams; the pair's boilerplate share is the mean of its two documents'. This is the standard
repeated-language construction used in the disclosure-text literature, stated here in full so that
it is reproducible from this file alone; no external implementation is called and no threshold is
chosen after seeing a result.

**Why both, and why not one composite.** The two are correlated but they are different claims. Length
says the operating MD&A is bigger; boilerplate share says a larger fraction of it is language that
recurs everywhere and therefore cannot move year to year. If the reversal survives length but not
boilerplate share, the mechanism has a name that length alone does not give it.

## Analysis, fixed in advance

1. **Primary.** Welch's $t$ on the BERT Item 7 index, zero panel against operating panel, with
   Cohen's d, Mann-Whitney $U$, both panel means, SDs, medians and the distribution overlap. Exact
   three-digit $p$; no significance stars.
2. **The mechanism model.** OLS of the BERT Item 7 index on `zero_panel` (indicator) +
   `log_length` + `boilerplate_share`. Reported with each coefficient's standard error, $t$, exact
   $p$, and the model $R^2$. The quantity of interest is what happens to the `zero_panel`
   coefficient between the unadjusted comparison and this model.
3. **Pre-registered robustness**, each reported as prominently as the primary if it reverses it:
   (a) bag-of-words secondary measure, (b) Item 1 in place of Item 7, (c) the length-stratified
   comparison run 1 pre-registered, on the middle tercile of the pooled length distribution.
4. **Ceiling reporting.** Run 1 established that both panels sit in the top 2% of the index's scale
   (cross-firm baseline: BERT .979, bag-of-words .925 over 200 unrelated-firm pairs). Run 2 reports
   every panel mean against that baseline as well as on the raw scale, because a difference of .002
   on a scale whose realized range is .021 is not the same object as a difference of .002 on
   $[0, 1]$. This is a reporting rule, not a new measure: no statistic is computed on a rescaled
   index.

## Decision rule — all four outcomes, committed now

The interesting outcome is the **inversion**, because it is the one the existing literature does not
already assume. The two kill conditions are stated first so they cannot be reinterpreted later.

- **KILL — powered null.** $|d| < .2$ with $n \geq 76$ per panel and $p > .05$. The measure neither
  separates the panels nor inverts. The question closes: the surviving claim from the whole line of
  work is the one run 1 already licenses — **no instrument abstains** — and nothing further is
  claimed. Note that a powered null is *still* a finding about abstention; it is a kill for the
  *inversion*, not for the placebo.
- **KILL — the by-construction direction.** The zero panel scores **at or above** the operating
  panel, $p < .05$. This is the direction the paper originally asserted and the direction that
  follows trivially from the construction of a similarity measure: nothing happened, so the text
  repeats. Confirming it restores C7 as first written and produces nothing the literature does not
  already believe. The question closes; the correction applied on 2026-08-15 is reverted with the
  same visibility it was applied with.
- **PROCEED — the inversion, mechanism named.** The zero panel scores **below** the operating panel
  at $p < .05$, **and** entering $\log$ length (with or without boilerplate share) drives the
  `zero_panel` coefficient to non-significance. This is the only outcome that raises the line to
  HIGH. It names the confound precisely: what the index reads as specification readiness is
  substantially a document-length artifact, and that is a correction the existing measurement
  literature can adopt without adopting anything else of ours.
- **PROCEED WITH CAUTION — the inversion, mechanism not named.** The inversion holds at $p < .05$
  and survives both covariates. Real, powered, and unexplained. Reported as such; it does **not**
  license a mechanism claim, and the next step would be a design question rather than a write-up.

**The container decision stays deferred** regardless of outcome, per the 2026-08-15 decision: run
the experiment, do not choose a venue for it, do not draft a paper. The output of this run is
`POST_EXPERIMENT_REPORT_POWERED.md` and the paper's `PENDING_UPDATES.md`, nothing else.

## What this still cannot establish

Unchanged from run 1, and worth restating because power tempts overreach. It bounds the **extreme**
case only. It says nothing about the middle of the distribution, where Brown and Tucker's
large-sample estimate — economic change explaining under 6% of the variation in year-over-year
MD&A modification — is the relevant evidence. It is not a validation of the SCI as a construct:
nothing here tests whether the measure captures specification readiness where readiness exists. A
powered inversion licenses exactly one new claim, that the index's apparent discrimination at the
zero-activity extreme runs the wrong way and tracks document length.

## Reproducibility

Fixed seed **20260815** for the operating draw (run 1's seed 20260809 is retained inside the
imported measure code, where it seeds the embedder). Python 3.12 + uv. Data: SEC EDGAR only —
public, no licence, no authentication, declared User-Agent, fair-access rate limit respected. All
fetches share run 1's on-disk cache keyed by `sha256(url)`, so a re-run pays only for filings not
already fetched, and the analysis phase re-runs with no network at all.

Run commands, in order:

```
uv run python code/powered_placebo.py --build
uv run --with torch --with transformers python code/powered_placebo.py --score
```
