# A Blinded Multi-LLM Content-Coding Instrument: Protocol Specification and Inter-Coder Reliability Validation on an Organizational Corpus

Dmitry Zharnikov

ORCID: 0009-0000-6893-9231

Concept DOI: [10.5281/zenodo.21756063](https://doi.org/10.5281/zenodo.21756063)

Working Paper v1.0.0 – August 2026

## Abstract

Content coding is a reliability bottleneck of qualitative and mixed-methods organizational research: it is labor-intensive, difficult to reproduce, and vulnerable to a coder who can see the study's hypotheses. Large language models now annotate text at or above crowd-worker quality [@gilardi-2023-chatgpt-outperforms-crowd], but naive single-model use reintroduces the failure modes intercoder-reliability protocols were built to remove — unauditable calls, hypothesis leakage, fabricated codes, and single-rater dependence. This article specifies a blinded multi-LLM content-coding instrument that imports human intercoder-reliability discipline into machine-assisted coding. Three heterogeneous models code each case independently from a neutral, source-cited evidence dossier while blinded to the hypotheses and the case's study role; cells combine by majority-vote-or-flag with author adjudication; a model that cannot determine a cell returns *uncertain* rather than guess; every call is logged with an exact model pin; and the harness and the empty coding schema are committed before any datum exists. On a corpus of thirty documented organizational integration cases the instrument reached almost-perfect inter-coder agreement (Fleiss' $\kappa = .838$), with a 2.7% flag rate concentrated entirely on auxiliary tokens. Reliability is distinguished from downstream inferential validity, which is left to future contrast studies. The harness, logs, and datasets are released as an auditable artifact.

**Keywords**: content analysis; intercoder reliability; large language models; LLM-assisted coding; blinded coding; pre-registration; reproducibility; research methods

---

## The Coding-Reliability Problem

### *Why content coding is a reliability bottleneck*

Much of the evidence in organizational research begins as documents — filings, transcripts, case histories, patents — that a researcher must convert into structured variables before any analysis can run. That conversion, content coding, is where reproducibility is won or lost. Coding is labor-intensive, so studies economize on coders and cases; it is judgment-laden, so two readers of the same document can assign different values; and it is procedurally opaque, so a published coefficient rarely comes with a record of how each cell was decided. The field's answer has been an intercoder-reliability discipline: multiple independent coders, a fixed codebook, a reported agreement statistic, and adjudication of disagreements [@krippendorff-2004-content-analysis-introduction; @hayes-2007-answering-the-call]. This discipline is expensive enough that it is often applied to a subsample rather than the full corpus, and it does not by itself address a subtler threat — that a coder who knows the study's hypothesis may, without any intent, resolve ambiguous cells in the predicted direction.

### *Why naive LLM coding does not solve it*

Large language models can now annotate text at or above the quality of trained crowd workers [@gilardi-2023-chatgpt-outperforms-crowd], and are being adopted as coders across computational social science [@ziems-2024-can-large-language-models; @zhang-2024-sentiment-analysis-era-llms]. The temptation is to treat a single model with a task-describing prompt as a fast, cheap coder. Doing so, however, reintroduces every problem the reliability discipline was built to remove, and adds new ones. A single model is a single rater, so idiosyncratic errors carry straight into the data. A prompt written by the analyst who knows the hypothesis is a leakage channel as direct as an unblinded human coder. A model asked for a code it cannot support from the evidence will often produce a plausible one anyway — a fabrication with no analog in careful human coding. And an unlogged API call is unauditable: the coded value cannot be traced to the input and parameters that produced it, so the run is not reproducible. Whether a model's codes are even valid for a given latent construct is itself an open question that demands a reliability-first posture rather than uncritical adoption [@li-2024-frontiers-determining-validity].

### *What this paper contributes, and what it is not*

This article specifies and validates a coding instrument that imports the human reliability discipline into the multi-model LLM setting rather than discarding it. The contribution is threefold. First, the instrument itself: several heterogeneous models coding each case independently from a neutral evidence dossier, combined by an explicit per-cell rule. Second, a single discipline package — blinding, registered-before-data commitment, an anti-fabrication rule, and call-level provenance — that makes the procedure trustworthy and auditable. Third, a reliability validation on a real organizational corpus, reported as a worked example rather than a claim of universal performance. The instrument must be distinguished from a different use of language models it superficially resembles: simulating human respondents, or *silicon sampling*, in which a model stands in for survey or experimental subjects [@argyle-2023-out-one-many; @horton-2023-large-language-models]. This instrument does not simulate anyone. It codes documentary evidence that exists independently of the model, exactly as a human content coder would, and its output is a reproducible measurement of that evidence, not a synthetic datum.

## The Instrument

### *Architecture: three blinded coders over a neutral dossier*

The unit of work is the coding cell — one categorical or binary variable for one case. For each case, the analyst assembles an evidence dossier: a self-contained, source-cited compilation of the case's documentary record, organized by neutral factual sections and containing no statement of the study's hypotheses, predicted directions, or the case's role in the sample. Three heterogeneous large language models, each pinned to an exact version, then code the case independently. In the validation reported below the three were a Claude, a Gemini, and a Grok model; heterogeneity across model families is deliberate, so that a systematic quirk of one family cannot silently determine a cell. Each model receives only the dossier and a fixed coder prompt that operationalizes each target variable in neutral, factual language, and returns a structured record — one value per cell. No model sees the manuscript, the hypotheses, or any other case's codes.

### *Combination: majority-vote-or-flag and adjudication*

Per cell, the three independent codes combine by a rule stated before coding: majority-vote-or-flag. If at least two models agree, their shared value is the cell's value. If all three disagree, or the agreeing majority is composed of *uncertain* returns, the cell is flagged for author adjudication rather than resolved by fiat. Adjudication is performed by the author against the dossier, with a written per-cell rationale recorded in an adjudication ledger; a pre-stated conservative rule resolves genuinely indeterminate cells in the null-friendly direction rather than inventing a determination. The combination rule and the adjudication rule are fixed in the committed harness, so neither can be adjusted after the codes are seen. The flag rate is itself a reported diagnostic: a low rate indicates the coding scheme is legible to independent coders from the dossier alone, and a high rate (a pre-set threshold escalates to dual-human coding) signals a scheme or an evidence base too thin to code reliably.

## The Discipline Package

Four disciplines make the procedure trustworthy and auditable. They are presented as a single package because each is necessary and none is sufficient alone.

### *Blinding and registered-before-data*

Blinding removes the hypothesis-leakage channel: because the coder prompt and every dossier are free of hypothesis content and of the case's sample role, a model cannot shade an ambiguous cell toward a predicted result, for it has not been told what is predicted. Registered-before-data removes a second channel — tuning the coding rule to the outcome. The harness, the coder prompt, and the empty coding schema are committed to version control before any coded datum exists, and the analysis pipeline is committed earlier still, with a synthetic fixture that reproduces a textbook value of the reported statistic. The commit history is therefore an external witness that the measurement procedure preceded the measurements.

### *Anti-fabrication and provenance*

The anti-fabrication rule instructs each model to return *uncertain* when the dossier does not support a determination, rather than produce a plausible guess; uncertain-dominated cells then flow to adjudication under the conservative rule. This converts the model's most dangerous failure mode — confident fabrication — into an explicit, auditable flag. Provenance closes the loop: every model call is logged as a line of JSON with its exact model pin, timestamp, full prompt, and raw response, and the coded dataset is assembled from those logs by a deterministic script. Any value in the final dataset is thus traceable to the call that produced it, and the entire run can be regenerated from the committed inputs.

## Reliability Validation

### *The worked demonstration corpus*

The instrument was exercised on a corpus of thirty documented public merger-and-acquisition integration cases, each coded from a dossier built from primary and reputable public sources with in-line source citations. The coded variables comprised six binary structural-classification cells together with a set of descriptive category tokens; the six binary cells were the variables on which the demonstration study's own analysis depended, and the descriptive tokens were auxiliary. Twenty-eight of the twenty-nine coded case files were fully coded by all three models; one case drew a truncated response from one model under free-tier rate-limiting and was coded by two of three, and is excluded from the agreement denominator. This corpus is a single organizational-document domain and is presented as a worked example establishing feasibility and reliability, not as evidence of uniform performance across tasks.

### *Inter-coder agreement and the flag profile*

Agreement across the fully triple-coded binary cells, measured by Fleiss' multi-rater $\kappa$ [@fleiss-1971-measuring-nominal-scale], was $\kappa = .838$ — above the conventional $\kappa \geq .81$ threshold for "almost perfect" agreement [@landis-1977-measurement-observer-agreement]. Of 406 coded cells, 11 were flagged for adjudication, a flag rate of 2.7%, far below the 20% level pre-set to escalate to dual-human coding. The flag profile is as informative as the coefficient: every flagged cell fell on an auxiliary descriptive token, and not one fell on the six study-critical binary cells, which the three models coded unanimously. Per-cell unanimous-agreement rates ranged from .89 to 1.00. Table 1 summarizes the reliability outcome.

Table 1: Inter-Coder Reliability Outcome on the Demonstration Corpus.

| Reliability measure | Value |
|---|---|
| Fleiss' $\kappa$ (binary cells) | .838 |
| Agreement band [@landis-1977-measurement-observer-agreement] | almost perfect ($\kappa \geq .81$) |
| Flagged cells | 11 of 406 (2.7%) |
| Flags on study-critical cells | 0 |
| Per-cell unanimous-agreement range | .89 – 1.00 |
| Fully triple-coded cases | 28 of 29 |

*Notes*: Fleiss' $\kappa$ computed over the fully triple-coded binary cells. The single non-triple-coded case (a truncated response under hosted-model rate-limiting) is excluded from the denominator. All flagged cells fell on auxiliary descriptive tokens; the six study-critical binary cells were coded unanimously by the three models. Values are reproduced by the released analysis artifact from the committed per-coder codes.

## Scope and Applicability

### *Where the instrument applies*

The instrument is domain-general across organizational-research coding tasks that share two properties: the evidence is documentary, and the target variables are discretely codable. Beyond the integration-structure classification demonstrated here, candidate applications include coding escalation-of-commitment or managerial-attention signals from earnings-call transcripts and classifying technological relatedness or novelty from patent records — recurring coding problems where human coding is costly and single-model coding is tempting but undisciplined. In each, the same procedure applies unchanged: assemble a neutral dossier, code independently with heterogeneous pinned models, combine by majority-vote-or-flag, adjudicate flags against a written rationale, and release the logs.

### *The dossier evidentiary-richness precondition*

Trustworthiness carries an explicit precondition. The dossier must meet a minimum evidentiary-richness threshold for the target cell — enough documented fact for an independent reader to determine the value — below which the correct coder behavior is *uncertain* rather than a determination. The threshold is task-specific and stated in advance as part of the codebook. The anti-fabrication rule is what makes this precondition operational rather than aspirational: where a dossier is too thin, the instrument surfaces a flag instead of a fabricated code. In the demonstration, the one dossier cell whose person-transfer detail was marked unverified drew three *uncertain* returns and was adjudicated conservatively — the precondition and the anti-fabrication rule behaving exactly as designed.

## Boundary Conditions

The instrument is specified for discretely-codable variables over evidence that can be assembled into a self-contained, source-cited dossier. It is not specified for open-ended free-text extraction, for continuous ratings lacking a stated discretization rule, or for evidence that resists dossier assembly. Its coders are exact model versions, and its results are conditional on those versions; as models are retired and replaced, coded values are expected to drift. Pinned provenance and the multi-model majority mitigate that drift — a re-run records exactly which versions produced which codes, and a single model's change cannot silently move a majority cell — but they do not eliminate it, and periodic re-validation is part of responsible use.

## Discussion

### *Contribution*

The instrument's value is that it makes machine-assisted coding auditable and reproducible without surrendering the reliability discipline of careful human coding. Its almost-perfect agreement on the demonstration corpus, its low and diagnostically-placed flag rate, and its complete call-level provenance together show that a small ensemble of blinded, pinned models can code a real organizational corpus at reliability standards the field expects of human coders — while producing an artifact a reviewer can rerun. The discipline package is the durable part: blinding, registered-before-data commitment, the uncertain-over-guess rule, and JSONL provenance are transferable to any LLM-assisted coding task, independent of the particular models used.

### *Limitations*

Four limitations bound the claim. First, the validation is a single worked corpus in one organizational-document domain; broad generalizability requires replication on substantively different corpora, and that replication is future work rather than an established result. Second, and most important, high inter-coder reliability is not the same as downstream inferential validity. This article does not run a head-to-head contrast of blinded multi-LLM coding against single-LLM coding or against human double-coding on hypothesis-leakage or downstream-inference metrics, and so makes no claim of superiority on those axes; it establishes that the instrument codes reliably and reproducibly, not that it improves the inferences a study draws. Third, dependence on hosted models is a reproducibility hazard: one free-tier response truncated mid-run and required a bounded-output retry, and hosted models can change or disappear. Fourth, the multi-model design multiplies per-cell cost and latency, a practical constraint on corpus size.

## Future Research

The most direct extension is the contrast study this article deliberately does not attempt: coding one corpus under blinded multi-LLM, single-LLM, and human double-coding conditions, and comparing not only reliability but hypothesis-leakage and the downstream inferences each supports. That design would test whether blinding measurably reduces leakage and whether the multi-model majority improves on a single model, converting the present reliability result into an inferential-validity result. Pre-specified robustness checks for that study include leave-one-model-out reliability, sensitivity to coder-prompt wording, and comparison against two trained human coders on the identical dossiers, with a target coding-cell count large enough to narrow the agreement interval. A second thread is replication across domains — earnings-call and patent coding among them — to move from a worked example to a generalizability claim. A third is calibrating a quantitative minimum evidentiary-richness threshold per task against the observed rate of *uncertain* returns, so the dossier precondition can be stated numerically rather than qualitatively.

## Companion Computation Script

The reliability results in this article are reproducible from the released coding artifact. The coding harness runs the three blinded coders over the dossiers and computes Fleiss' $\kappa$; a deterministic assembler builds the coded dataset from the per-coder codes and the adjudication ledger; and an analysis script recomputes the reported reliability statistics and carries a fixture self-check that reproduces a known value. Each script names its run command in its docstring. The harness, the per-call JSON logs, the coded datasets, the adjudication ledger, and the analysis scripts are released together as the paper's computational artifact; the public archive location and the exact run command are recorded in the Data and Code Availability statement upon publication.

## Acknowledgments

Artificial-intelligence assistance is disclosed here at the level a paper reporting a companion computation requires. Three large language models served as the independent blinded coders in the validation reported above — Claude (Opus 4.8), Gemini (3.1 Pro), and Grok (4.3) — each shown only a per-case evidence dossier and returning a structured coding; every model call is logged with its full prompt, parameters, and response, and the coding harness, coded datasets, adjudication ledger, and analysis pipeline are released alongside the paper. The same assistants were also used for literature search and for editorial refinement of the manuscript. All methodological claims, the reliability interpretation, and every coding-adjudication decision are the author's sole responsibility.

## Author Contributions (CRediT)

Dmitry Zharnikov: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Software, Validation, Writing — original draft, Writing — review and editing.

## Data and Code Availability

The coding harness, the per-call JSON logs, the coded datasets, the adjudication ledger, and the analysis scripts that reproduce every reliability statistic reported here are released as the paper's computational artifact at https://github.com/spectralbranding/orgschema-papers/tree/main/multi-llm-coding-instrument under the MIT license for code and CC BY 4.0 for data and documentation. Because the coded corpus is small it is vendored with the code; `reproduce.sh` recomputes the reported reliability statistics from the released dataset. The paper's archival concept DOI is [10.5281/zenodo.21756063](https://doi.org/10.5281/zenodo.21756063) and the v1.0.0 version DOI is [10.5281/zenodo.21756064](https://doi.org/10.5281/zenodo.21756064).

## References

::: {#refs}
:::
