# Post-experiment report — the POWERED zero-activity placebo, run 2 (2026an)

**Run 2026-08-15**, against `PRE_EXPERIMENT_NOTES_POWERED.md`, written and committed before any run-2
result existed. Run 1's report (`POST_EXPERIMENT_REPORT.md`) stands unamended as the record of what
run 1 found; this file records what happens to it at power.

## Verdict: KILL — POWERED NULL, by the pre-registered rule

$n = 100$ per panel, exactly year-matched. The primary measure returned $M = .998$ ($SD = .003$) for
the zero-activity panel against $M = .998$ ($SD = .005$) for the operating panel — Cohen's
$d = .166$, Welch $t(174.41) = 1.17$, $p = .243$, Mann-Whitney $p = .660$.

The pre-registered kill condition was $\lvert d \rvert < .2$ with $n \geq 76$ per panel and
$p > .05$. All three hold. **The inversion is dead and the question closes.**

## Run 1 did not replicate, and the way it failed is the point

| arm | run 1 ($n = 30/20$) | run 2 ($n = 100/100$) |
|---|---|---|
| BERT Item 7 (primary) | $d = -.457$, $p = .065$ | $d = .166$, $p = .243$ |
| Bag-of-words Item 7 | $d = -.248$, $p = .335$ | $d = .023$, $p = .874$ |
| BERT Item 1 | $d = -.005$, $p = .987$ | $d = -.102$, $p = .511$ |
| Middle length tercile | $d = -.866$, $p = .036$ | $d = -.194$, $p = .438$ |

**The sign flipped and the magnitude collapsed** on 3.3 times the sample. Run 1's largest effect —
the length-stratified arm at $d = -.866$, the only arm that reached significance — was computed on 18
pairs and does not survive. This is the textbook shape of effect-size inflation at low power, and it
is the reason the 2026-08-15 decision ordered the experiment before the write-up.

**Consequence for the published paper, and it is not small.** 2026an currently carries a correction,
applied 2026-08-15 on run 1, stating that the predicted direction "was not observed in any arm" with
"the zero-activity panel below rather than above." The first clause survives. **The second does
not** — at power the panels are indistinguishable, and two of three arms now point weakly the other
way. The honest position is **non-separation, not inversion**: neither the paper's original premise
(empty filers score high) nor run 1's reversal (empty filers score low) is supported. See
`PENDING_UPDATES.md`.

## What run 2 establishes positively: the instrument does not abstain, and now that is powered

One hundred structurally zero-activity filers — SIC 6770, no revenue tag reporting a nonzero value in
either fiscal year, and a `us-gaap:Assets` fact present at both year ends so the zero is *reported*
rather than *missing* — were each handed to the published index, and the index returned a confident
number in its normal working range for every one of them. Against 100 operating firms matched
fiscal-year for fiscal-year, the readings are indistinguishable.

That is the claim the whole line of work licenses, and run 2 makes it much stronger than run 1 could:
**no instrument abstains.** A measure with no way to say *I cannot read this* does not fall silent on
a company with no operations behind its documents. It answers, and it answers in range.

## The finding that outranks the placebo: a trivial statistic separates what the index cannot

Document length and boilerplate share were entered as the candidate mechanism, not as nuisance
controls. Boilerplate share — the fraction of a document's tetragram positions occupied by tetragrams
recurring in at least 5% of the union corpus — behaves as follows:

| | zero-activity | operating |
|---|---|---|
| Boilerplate share | $M = .411$ ($SD = .195$) | $M = .104$ ($SD = .033$) |
| MD&A length, median | 3,223 words | 9,396 words |

**Separation, post-hoc and labelled as such** (boilerplate share was pre-registered as a covariate,
not as a classifier, so treating it as one is exploratory): boilerplate share orders a random
zero/operating pair correctly **94.9%** of the time (Cohen's $d = 2.203$). **The paper's own index
orders the same pairs correctly 51.8% of the time** — chance.

So a text statistic computable in a dozen lines, with no model, tells these two populations apart
almost perfectly, while a BERT-based index cannot tell them apart at all. That is a measurement fact
about the index, not about shells, and it belongs in the limitations.

## The mechanism model, and the reading it does NOT support

Pre-registered: OLS of the primary index on `zero_panel` + `log_length` + `boilerplate_share`.

| model | $R^2$ | `zero_panel` coefficient |
|---|---|---|
| unadjusted | .007 | $b = +.00067$, $p = .243$ |
| + log length | .082 | $b = +.00138$, $p = .018$ |
| + log length + boilerplate share | .146 | $b = +.00444$, $p < .001$ |

`log_length` enters at $b = +.00159$ ($p < .001$) and `boilerplate_share` at $b = -.00860$
($p < .001$). This is a **suppression pattern**: the zero panel's four-times-higher boilerplate share
pushes its score down, masking a positive panel effect, so conditioning on the two mechanism
variables uncovers one.

**This is not a back door to the by-construction direction, and must not be read as one.** The
pre-registered decision rule reads the *unadjusted* primary comparison, which is null. Three further
reasons to hold the line: the adjusted coefficient is a different estimand from the one the rule
governs; boilerplate share is derived from the same two texts as the outcome, so conditioning on it
is a decomposition rather than a clean control; and $b = +.0044$ sits on a measure whose entire
realized range is about .021, so even taken at face value it is a fifth of the range on a scale that
is 98% ceiling. Reported because it was pre-registered and because it names where the variance lives.
Not promoted.

## Secondary observations, reported because the pre-registration required them

- **Rank tests disagree with mean tests in the two secondary arms.** Bag-of-words: Welch $p = .874$
  but Mann-Whitney $p = .024$. Item 1: Welch $p = .511$ but Mann-Whitney $p = .038$. The primary arm
  shows nothing on either ($p = .243$ / $p = .660$). Means match while distribution *shapes* differ —
  consistent with the zero panel's much wider spread. It changes no verdict and is not a finding
  about level.
- **Ceiling reporting, per the pre-registration.** Against run 1's cross-firm baseline of .979, the
  zero panel sits at 92.3% of the realized range and the operating panel at 89.1%; the difference
  between them is 3.2% of that range. Run 1's ceiling finding replicates and remains the dominant
  fact about this index.
- **Item 1 attrition**: 83 of 100 zero and 92 of 100 operating pairs yielded an extractable Item 1
  in both years. Reported rather than silently dropped.

## Deviations from the pre-registration

**None.** The three declared panel deviations (fiscal years 2011+ with an `Assets`-presence integrity
check; year-matched pair selection for the operating panel; a four-quarter Y/Y+1 index draw) were
applied as written, and they worked: the two panels' fiscal-year distributions came out **identical,
year for year**, where run 1's operating panel had stalled at 20 and could not match.

The screening transport change was proven rather than assumed, as required: run 1's
`revenue_for_fy` was re-run against run 2's `companyfacts` evaluation on all fifty of run 1's
firm-years before any new screening, and agreed **50/50**. `--build` aborts on a single disagreement.

## What this changes, and what it does not

- **Closes**: the inversion, and with it the "zero-activity filers as an adversarial negative control"
  seed in its original *and* its reversed form. Neither direction is real at power.
- **Strengthens**: the abstention claim, and the C7 boundary exclusion — which was already retained
  on the ground that the measure is *uninformative* there rather than inflated. Non-separation is
  precisely what "uninformative" means, so run 2 supports the boundary condition as written better
  than run 1 did.
- **Adds a limitation**: the index is at chance on a distinction a tetragram counter makes at 94.9%.
- **Does not license**: any claim about the middle of the distribution. Brown and Tucker's
  large-sample estimate remains the relevant evidence there. Nor is this a construct validation:
  nothing here tests whether the index measures specification readiness where readiness exists.
- **Container decision stays deferred**, per the 2026-08-15 decision — run the experiment, do not
  choose a venue, do not draft a paper. A powered null does not change that, and arguably settles it.

## Reproduce

```
uv run python code/powered_placebo.py --build
uv run --with torch --with transformers python code/powered_placebo.py --score
```

Seed 20260815 for the operating draw; run 1's seed 20260809 seeds the embedder. `bert-base-uncased`
pinned literally. All statistics in `output/powered/results_powered.json`; panels in
`output/powered/panel_{zero,operating}_powered.csv`. The build phase needs network and no torch; the
score phase needs torch and no network.
