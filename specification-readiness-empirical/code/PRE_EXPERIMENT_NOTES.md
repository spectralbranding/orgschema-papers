# Pre-experiment notes — the zero-activity-filer placebo (2026an)

**Written 2026-08-09, BEFORE the run.** Anti-HARKing register, in the pattern of the pre-experiment
notes for the companion theoretical paper (2026am). Everything below is fixed before any result
is seen; the post-experiment report records what actually happened, including any deviation.

## Why this runs now

2026an's robustness battery specifies a placebo it has never run. Its own `PENDING_UPDATES.md`
gates it behind "the archival pass," which needs licensed panel data and has not happened. But the
placebo does **not** need that pass — it needs public filings and the published index, nothing else.
The Sep 16 article states in its body that the control is specified and not run. Running it converts
the paper's weakest sentence into its strongest, or deletes the item. Either outcome is worth the
afternoon.

## The claim under test

The paper's continuous measure is year-over-year narrative similarity. Similarity has two sources: a
firm whose commitments are codified restates them consistently, and **a firm to which nothing
happened also restates them consistently, because there is nothing new to state.** Reading the whole
of the similarity as codification attributes the second source to the first, and the error is
one-signed — firms with low event density score as highly ready.

A structurally zero-activity filer is the extreme of the second source: economic change is not low
but pinned at zero. If the measure cannot tell that firm from a codified one, the confound is
demonstrated on the measure rather than argued about in a limitations paragraph.

## The measure — published spec, unchanged. No tuning is permitted.

From the paper's Data and Measurement section, taken verbatim as the specification:

- Section: **Item 7 (MD&A)**, parsed from the 10-K primary document, non-narrative content stripped.
- Embedding: **BERT-base-uncased**, the paper's stated primary. Documents exceed the 512-token
  limit, so each MD&A is chunked into non-overlapping 512-token windows and the document embedding
  is the mean of mean-pooled chunk embeddings. **The paper does not specify a chunking rule** — this
  is the one construction choice it leaves open, it is declared here in advance, and it is applied
  identically to both panels so it cannot favour either.
- $\text{SCI\_continuous}_{i,t} = \cos(\text{emb}(\text{Item7}_{i,t}), \text{emb}(\text{Item7}_{i,t-1}))$,
  rescaled from $[-1, 1]$ to $[0, 1]$.
- Secondary measure: **bag-of-words cosine** over the same two texts. The paper's framework section
  names "bag-of-words or contextual-embedding representations," so this is inside the published spec
  rather than a substitute for it. Reported alongside, never instead.

No threshold, no preprocessing choice, and no model substitution may be changed after seeing a
result. If BERT cannot be installed, the run is reported as not done — not silently downgraded.

## Panels

**Zero-activity panel.** Filers with SEC SIC code **6770 (Blank Checks)** holding two consecutive
10-Ks, screened further on XBRL company facts: **no revenue tag reporting a nonzero value in either
fiscal year**. SIC alone is not trusted — a blank-cheque vehicle that has completed a combination
keeps the code for a while, and the revenue screen is what makes the population *structurally*
zero-activity rather than merely categorised as such.

**Operating panel.** A random sample (fixed seed) of 10-K filers drawn from the same filing years,
screened to **revenue above $50 million in both fiscal years**. Random rather than hand-picked: a
curated comparison group would let case selection produce the result.

**Matching.** On fiscal-year pair only, which is what the paper's own wording specifies ("matched
operating firms in the same filing years"). Document length is *not* matched, because length is
plausibly part of the phenomenon; instead it is measured on both panels and a length-stratified
comparison is pre-registered as robustness below.

**Target n**: 30 or more usable firm-year pairs per panel. A pair is usable only when Item 7 is
extractable from both filings and yields at least 200 words in each. Firms failing extraction are
counted and reported, never silently dropped.

## Decision rule — stated now, in the paper's own words

> "If the zero-activity panel scores at or above the operating panel, the confound is demonstrated
> on the paper's own measure; if it does not, this whole item is void and should be deleted."

Operationalized:

- **CONFIRMED** — mean SCI of the zero-activity panel exceeds the operating panel, Welch's t-test
  $p < .05$. The confound is demonstrated; the covariate control becomes a necessary rather than a
  precautionary part of the specification, and the boundary exclusion is justified on evidence.
- **VOID** — mean SCI of the zero-activity panel is *below* the operating panel, $p < .05$. The
  concern is retired. The pending item is deleted, the article's claim is corrected before Sep 16,
  and the correction is published rather than quietly dropped.
- **INDETERMINATE** — neither. Reported as such. An underpowered null is not evidence of absence and
  will not be written as one.

Reported regardless of direction: both panel means and SDs, medians, Welch $t$ with exact
three-digit $p$, **Cohen's d**, Mann-Whitney $U$, and the full distribution overlap. Effect size is
mandatory alongside every test (PAQS).

**Pre-registered robustness**: (a) the bag-of-words secondary measure, (b) a length-stratified
comparison restricted to pairs whose MD&A word counts fall in the same tercile, (c) Item 1
(Business) in place of Item 7 as an alternative section. Any of these that reverses the primary
result is reported as prominently as the primary.

## What this can and cannot establish

It bounds the **extreme** case only. It says nothing about the middle of the distribution, where
Brown and Tucker's large-sample estimate — economic change explaining under 6% of the variation in
year-over-year narrative modification — is the relevant evidence and where the confound remains
bounded rather than eliminated. A CONFIRMED verdict does **not** license the claim that the SCI
measures inactivity in general. It licenses exactly one claim: that at zero activity the measure
does not abstain.

It is also not a validation of the SCI as a construct. Nothing here tests whether the measure
captures specification readiness where readiness exists.

## Reproducibility

Fixed seed **20260809**. Python 3.12 + uv. Data source: SEC EDGAR, public, no licence, no
authentication. All fetched filings and extracted sections are cached to `output/` so the analysis
re-runs without re-fetching, and the SEC fair-access rate limit is respected with a declared
User-Agent.

Run command:

```
uv run python code/zero_activity_placebo.py
```
