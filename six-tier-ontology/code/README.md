# STSD scorer — companion code for Zharnikov 2026ag

Reference implementation of the Six-Tier Separability Diagnostic (STSD) from Table 4 of:

> Zharnikov, D. (2026). *Dual Hierarchies of Organizational Transferability: A Six-Tier Ontology and Theory of Acquisition Failure Propagation*. Working paper. doi:10.5281/zenodo.19895813

## What this is

A structured-judgment calculator that takes a six-cell ordinal response (one state per tier from {Fused, Partial, Independent}) and returns:

1. The six-cell separability profile in tabular form
2. The Fused-tier count (the framework's primary risk index)
3. A flip-case flag (Tier 1 = Fused signals identity-bound owner)
4. A constraint-hierarchy-ordered integration priority ranking

The script encodes Table 4 of the paper exactly. It does not compute a continuous score because the underlying construct is ordinal, not interval (per *Notes* on Table 4).

## Run

```
python stsd_scorer.py --example
```

prints the two illustrative profiles from the paper (the SaaS company in the Tier 4 vignette; the regional manufacturer in the Tier 1 vignette). Output is captured at `sample_output.txt`.

To score a custom target, pass a JSON file:

```
python stsd_scorer.py --input target_responses.json
```

where `target_responses.json` contains:

```json
{
  "tier_1_intent": "Fused",
  "tier_2_model": "Partial",
  "tier_3_entity": "Independent",
  "tier_4_product": "Fused",
  "tier_5_process": "Partial",
  "tier_6_organization": "Partial"
}
```

Valid states for every tier are exactly `Fused`, `Partial`, `Independent`.

## Reproducibility

- Deterministic. No random number generation, no external dependencies beyond the Python standard library.
- Tested on Python 3.10+.
- The two example outputs match the two profiles described in the paper's "How to read the profile" paragraph.

## What this is *not*

- Not a validation of the STSD. The paper's "Validation and Future Research Agenda" lists the four-priority empirical validation roadmap (inter-rater reliability, predictive validity, cross-form invariance, platform extension); none of those validations is encoded here.
- Not a substitute for structured-interview administration. The paper specifies a semi-structured interview protocol with probes; this script computes the scoring step only.

## License

MIT (matching the paper's public mirror license).
