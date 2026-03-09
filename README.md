# Organizational Schema Theory -- Research Papers

Research publications on Organizational Schema Theory (orgschema), a reverse-design TDD methodology for business operations. Businesses are designed backward from desired customer experience through testable, version-controlled specifications where each operational layer validates the layer above it.

## Papers

| Paper | Words | Refs | Status |
|-------|-------|------|--------|
| [The Organizational Schema Theory: Test-Driven Business Design](organizational-schema-theory/paper.md) | ~8,300 | 25 | Working paper, Mar 2026 |

### The Organizational Schema Theory (Zharnikov 2026c)

Introduces the orgschema methodology: a six-level TDD cascade (customer experience contracts, signal requirements, process contracts, procedures, input specifications, sourcing requirements) where each level functions as the acceptance test for the level below it. Demonstrated through a complete specialty coffee operation (Spectra Coffee) specified across all six levels. Evaluated by five independent expert reviewers. Discusses implications for franchise models, organizational openness, and cross-industry perception transplant.

**Keywords**: test-driven development, business design, configuration management, design science research, declarative process management, organizational specification

- [Read on GitHub](organizational-schema-theory/paper.md)
- SSRN (forthcoming)

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

## Author

**Dmitry Zharnikov** -- dmitry@spectralbranding.com

Creator of Organizational Schema Theory and Spectral Brand Theory. Background in financial systems engineering and applied epistemology.

## License

All papers are released under [MIT License](LICENSE). Use, cite, and build upon this work freely with attribution.

## Trademarks

"Organizational Schema Theory" and "orgschema" are trademarks of Dmitry Zharnikov. The MIT license applies to the source code and text only and does not grant permission to use the project trademarks.
