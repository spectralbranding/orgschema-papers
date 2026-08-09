# Post-experiment report — the zero-activity-filer placebo (2026an)

**Run date**: 2026-08-09. Seed 20260809. Pre-registration: `PRE_EXPERIMENT_NOTES.md`, written
before the run and not amended after it.

## Verdict: INDETERMINATE by the pre-registered rule — and the prediction failed

The paper predicted that a structurally zero-activity filer would score **at or above** matched
operating firms on the published index. It does not. It scores slightly **below**, and every arm
that reaches significance runs in that same direction. Nothing in this run supports the confound as
the paper states it.

| Measure | Zero-activity | Operating | d | Welch p | Mann-Whitney p |
|---|---|---|---|---|---|
| **SCI (BERT, Item 7) — primary** | M = .997 (SD .005), n = 30 | M = .999 (SD .001), n = 20 | −.457 | .065 | **.014** |
| SCI (bag-of-words, Item 7) | M = .991 (SD .018) | M = .995 (SD .009) | −.248 | .335 | .476 |
| SCI (BERT, Item 1) | M = .998 (SD .005), n = 21 | M = .998 (SD .004), n = 18 | −.005 | .987 | **.043** |
| SCI (BERT, Item 7), middle length tercile | M = .998, n = 12 | M = .999, n = 6 | −.866 | **.036** | — |

The pre-registered decision rule keyed on the Welch test of the primary measure. At p = .065 it does
not clear the .05 threshold in either direction, so the verdict is **INDETERMINATE** and the rule is
honoured as written. But the rule was designed to catch a confound that would have shown up as a
*positive* difference, and the difference is negative in all four rows. Reporting this as a null is
too generous to the original claim.

## Why the prediction failed — a shell company's paperwork changes more, not less

The confound's premise is that a firm to which nothing happened restates itself identically. That is
not how these filings behave.

A blank-cheque vehicle's MD&A is **short**: median 2,032 words against 8,644 for the operating panel.
Almost all of it is composed of things that *do* move year to year — trust-account balances, deadline
extensions, redemptions, going-concern language, warrant accounting, and progress in the search for a
target. There is little else in the document to hold the cosine up.

A large operating firm's MD&A is **long** and dominated by stable boilerplate: accounting policies,
risk language, segment descriptions, critical-estimate discussion. Genuine operational news is a
small fraction of a large stable document, so the cosine stays high no matter how eventful the year.

The dispersion says the same thing from the other side. The zero-activity panel's scores range from
**.974 to .99994**; the operating panel's from **.9954 to .99993**. The supposedly featureless
population is the one with the wider spread. The widest mover in the whole study is 26 Capital
Acquisition Corp., whose MD&A went from 2,451 to 20,597 words in the year it pursued its
combination — a blank-cheque vehicle having, by a wide margin, the most eventful disclosure year of
any firm sampled.

**"Nothing happened operationally" is not the same as "nothing changed in the document."** The
paper's confound argument silently assumed it was.

## The finding that matters more than the placebo: the index has almost no range

Both panels sit against the ceiling — .997 and .999 on a [0, 1] rescaled cosine, with the operating
panel's standard deviation at **.001**. Before treating that as a fact about firms, the obvious
alternative had to be ruled out: that the measure cannot separate *any* two 10-K narratives.

`ceiling_diagnostic.py` (POST-HOC, and labelled as such) computed the same index across 200 pairs of
**unrelated** firms:

| | Within-firm, zero-activity | Within-firm, operating | Cross-firm, unrelated | Separation |
|---|---|---|---|---|
| BERT, Item 7 | .997 | .999 | **.979** (SD .013) | **.020** |
| Bag-of-words, Item 7 | .991 | .995 | **.925** (SD .034) | **.070** |

So the measure is **not degenerate** — two unrelated companies do score lower than a company against
itself, and the ordering is right. But the entire working range of the published index is the **top
two percent of its scale**. Two companies with nothing whatsoever in common score .979; a company
against its own prior year scores .999. Every distinction the paper's regressions need to make lives
inside that band, where a parsing artifact, a boilerplate change, or a different chunking rule moves
the number as much as a real change in the firm would.

The bag-of-words variant has three and a half times the range of the BERT variant. That is worth
knowing: the paper names BERT as primary and dictionary cosine as secondary, and on this evidence the
ordering deserves re-examination, because mean-pooling a long document into one vector compresses
exactly the variation the construct is supposed to carry.

## What is now established, and what is not

**Established.**

1. The instrument does **not abstain** on a company with no operations. It returns .997 out of 1.000
   for a blank-cheque vehicle that had no product, no customers and no revenue in either year. The
   article's central observation — that a text-derived measure returns a confident high reading where
   it should decline to read — survives, and it is now measured rather than argued.
2. The instrument also returns .999 for PetSmart, Barracuda Networks and Independence Contract
   Drilling. **It cannot meaningfully tell them apart.**
3. The one-signed-error story, *as a comparative claim*, is not supported. If anything the sign is
   reversed.

**Not established.**

- Nothing here tests whether the SCI captures specification readiness where readiness exists. This
  was never a construct validation and must not be cited as one.
- Nothing here speaks to the middle of the distribution. Brown and Tucker's estimate — economic
  change explaining under 6% of year-over-year narrative modification across roughly 28,000
  company-years — remains the relevant evidence there, and the confound remains bounded rather than
  eliminated.
- The panels are small (30 and 20) and the operating panel fell short of its 30 target because 457
  candidates failed the revenue floor and 115 fell in already-filled years. An underpowered null is
  not evidence of absence, and the INDETERMINATE verdict is reported as exactly that.

## Deviations from the pre-registration

**One, and it is disclosed rather than absorbed.** The operating panel reached n = 20 against a
target of 30. The shortfall is a consequence of two pre-registered screens interacting — the $50M
revenue floor and the year-matching quota — not of any choice made after seeing results. No screen
was relaxed to recover the target, because relaxing a screen after seeing a result is the failure
this register exists to prevent.

Everything else ran as pre-registered: the measure was not tuned, no threshold moved, all three
robustness arms were computed and are reported above whether or not they helped, and the verdict was
computed by the script from the rule rather than chosen.

`ceiling_diagnostic.py` is **post-hoc** and is marked so in its own docstring, in its output, and
here. It was written after seeing the ceiling and asks a question the pre-registration did not.

## What this changes

1. **The pending item in 2026an is not deleted, and it is not confirmed either.** It is rewritten:
   the placebo has been run, the confound was not demonstrated at the extreme, and the reason it was
   not is itself a correction to the confound's premise.
2. **A new and higher-priority item joins it**: the index's working range is the top two percent of
   its scale, and the BERT construction has less range than the bag-of-words alternative the paper
   demotes to secondary. This bears on every hypothesis in the paper, not on the robustness battery
   alone.
3. **The Sep 16 article must be revised before it publishes.** It currently states the prediction
   this run failed to support, and it states that the control has not been run. Both are now wrong.
   The revision is not a retreat — a measured .997 on a company that did nothing, beside .999 on a
   real one, is a stronger and stranger result than the prediction was.

## Reproduce

```
uv run --with torch --with transformers python research/papers/2026an/code/zero_activity_placebo.py
uv run --with torch --with transformers python research/papers/2026an/code/ceiling_diagnostic.py
```

Fixed seed 20260809; SEC EDGAR only, public and unauthenticated. The filing cache is git-ignored
(~1.6 GB) and rebuilds itself on a re-run. Outputs: `output/results.json`,
`output/ceiling_diagnostic.json`, `output/panel_zero.csv`, `output/panel_operating.csv`,
`output/run.log`.
