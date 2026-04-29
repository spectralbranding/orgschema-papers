# Organizational Schema Theory -- Research Papers

Research publications on Organizational Schema Theory (orgschema), a reverse-design TDD methodology for business operations. Businesses are designed backward from desired customer experience through testable, version-controlled specifications where each operational layer validates the layer above it.

## Papers

| Paper | Words | Refs | Status |
|-------|-------|------|--------|
| [The Organizational Schema Theory: Test-Driven Business Design](organizational-schema-theory/paper.md) | ~8,300 | 25 | Working paper, Mar 2026 |
| [The OrgSchema Audit: A Six-Level Diagnostic for Specification-Driven Organizations](orgschema-audit/paper.md) | ~9,200 | 24 | Working paper, Apr 2026 |
| [Verification as Operator: Why Acceptance Testing Succeeds Where Conventional Audit Fails](verification-as-operator/paper.md) | ~6,100 | 31 | Working paper v0.4, Apr 2026 — [DOI](https://doi.org/10.5281/zenodo.19778588) |
| [Organizational Metamerism: When Distinct Configurations Produce Equivalent Outputs](org-as-metadata/paper.md) | ~10,300 | 48 | Working paper v1.0.0, Apr 2026 — Zenodo upload pending |

### The Organizational Schema Theory (Zharnikov 2026c)

Introduces the orgschema methodology: a six-level TDD cascade (customer experience contracts, signal requirements, process contracts, procedures, input specifications, sourcing requirements) where each level functions as the acceptance test for the level below it. Demonstrated through a complete specialty coffee operation (Spectra Coffee) specified across all six levels. Evaluated by five independent expert reviewers. Discusses implications for franchise models, organizational openness, and cross-industry perception transplant.

**Keywords**: test-driven development, business design, configuration management, design science research, declarative process management, organizational specification

- [Read on GitHub](organizational-schema-theory/paper.md)
- [Preprint (DOI)](https://doi.org/10.5281/zenodo.18946043)

### Verification as Operator (Zharnikov 2026ae)

Provides the first explicit algebraic identification of organizational acceptance testing as a spectral projection operator. Conventional audit (per Power 1997) is shown to be a degenerate rank-1 projection that discards all dimensions of organizational performance orthogonal to the compliance axis; OST's six-level cascade is full-rank, preserving dimensional structure across the specification hierarchy. The paper synthesizes three convergent lineages — organizational cybernetics (Beer 1972; Beer 1984), behavioral organization theory (March and Simon 1958; Argyris and Schön 1978), and software engineering verification (Beck 2002) — and shows that all three implicitly rely on the projection identity without naming it. Three formal propositions establish the rank inequality, cascade-consistency condition, and bandwidth bound. A Python simulation in Appendix B confirms that rank-1 audit misses ~90% of total organizational deviation across all noise levels.

**Keywords**: organizational verification, spectral projection, acceptance testing, audit society, viable system model, test-driven development, organizational learning, information-processing design

- [Read on GitHub](verification-as-operator/paper.md)
- [Preprint (DOI)](https://doi.org/10.5281/zenodo.19778588)
- Target venue: Academy of Management Review

### The OrgSchema Audit (Zharnikov 2026)

Introduces a structured diagnostic protocol that evaluates organizational specification maturity across six cascading levels. Each audit level defines what to examine, what a healthy specification looks like, what failure modes indicate, and what corrective actions restore specification integrity. Demonstrates the full protocol through a worked example using a specialty coffee operation. Advances two propositions: cascade-position prioritization and bidirectional traceability completeness.

**Keywords**: organizational specification, test-driven business design, operational audit, specification maturity, six-level cascade, experience contracts, organizational schema theory, AI-assisted diagnostics

- [Read on GitHub](orgschema-audit/paper.md)
- [Preprint (DOI)](https://doi.org/10.5281/zenodo.19555201)

## How to Cite

```bibtex
@article{zharnikov2026ost,
  title={The Organizational Schema Theory: Test-Driven Business Design},
  author={Zharnikov, Dmitry},
  year={2026},
  url={https://github.com/spectralbranding/orgschema-papers}
}
```

Machine-readable citation: [CITATION.cff](organizational-schema-theory/CITATION.cff)

## Companion Repositories

| Repository | Description |
|-----------|-------------|
| [orgschema-framework](https://github.com/spectralbranding/orgschema-framework) | Python validator + JSON Schema for orgschema specifications |
| [orgschema-demo](https://github.com/spectralbranding/orgschema-demo) | Spectra Coffee reference implementation -- 25 YAML files, CI/CD pipeline |
| [sbt-framework](https://github.com/spectralbranding/sbt-framework) | Spectral Brand Theory -- the perception specification language used for L0-L1 |
| [sbt-papers](https://github.com/spectralbranding/sbt-papers) | SBT research papers (sibling framework) |

## Related Work

Orgschema is a sibling framework to Spectral Brand Theory (SBT). Both emerge from specification-first epistemology but target different domains:

- **SBT** models how brands are perceived (observer-dependent, 8 dimensions)
- **Orgschema** uses SBT as the test specification language for L0-L1 (desired perception determines required signals)

See [Zharnikov 2026a](https://github.com/spectralbranding/sbt-papers) for the SBT paper.

### Cross-Cutting Methodology Papers (in sbt-papers)

Several papers in the [sbt-papers](https://github.com/spectralbranding/sbt-papers) repo are cross-cutting methodology pieces that apply equally to SBT, Orgschema, and the broader specification-first research program. They live in sbt-papers for historical reasons (originated there before the orgschema-papers split) but are conceptually shared between the two frameworks:

| Key | Paper | DOI | Relevance to Orgschema |
|-----|-------|-----|------------------------|
| R13 | [Paper as Specification: A Machine-Readable Standard for Scientific Claims](https://github.com/spectralbranding/sbt-papers/tree/main/r13-paper-as-specification) | [10.5281/zenodo.19210037](https://doi.org/10.5281/zenodo.19210037) | Applies the orgschema test-driven cascade pattern to scientific publishing — papers as testable specifications. |
| R14 | [Research as Repository: A Git-Native Protocol for Scientific Knowledge Production](https://github.com/spectralbranding/sbt-papers/tree/main/r14-paper-as-repository) | [10.5281/zenodo.19294864](https://doi.org/10.5281/zenodo.19294864) | Extends orgschema's "git as system of record" architecture to scientific knowledge production. |
| 2026l | [The Rendering Problem: From Genetic Expression to Brand Perception](https://github.com/spectralbranding/sbt-papers/tree/main/rendering-problem) | [10.5281/zenodo.19064426](https://doi.org/10.5281/zenodo.19064426) | Cross-domain formalization of the specification-rendering gap that orgschema's L1-L5 cascade addresses operationally. |

These papers' Zenodo DOIs and GitHub paths remain in sbt-papers; this repo points to them rather than duplicating.

## Author

**Dmitry Zharnikov** -- dmitry@spectralbranding.com

Creator of Organizational Schema Theory and Spectral Brand Theory. Background in financial systems engineering and applied epistemology.

## License

All papers are released under [MIT License](LICENSE). Use, cite, and build upon this work freely with attribution.

## Trademarks

"Organizational Schema Theory" and "orgschema" are trademarks of Dmitry Zharnikov. The MIT license applies to the source code and text only and does not grant permission to use the project trademarks.
