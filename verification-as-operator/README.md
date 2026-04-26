# Verification as Operator

**Verification as Operator: Why Acceptance Testing Succeeds Where Conventional Audit Fails**

Citation key: `2026ae` | Zenodo DOI: [10.5281/zenodo.19778588](https://doi.org/10.5281/zenodo.19778588) | Working Paper v1.0.0 (Apr 26, 2026) | Target venue: Academy of Management Review

## Summary

Organizational verification confronts a persistent paradox: firms invest heavily in audit and compliance yet sociological evidence shows these rituals often substitute procedural legibility for substantive performance alignment. This paper offers an operator-theoretic diagnosis. Verification is formalized as a spectral projection operator P that maps noisy organizational states onto invariant eigenspaces defined by acceptance criteria.

Conventional audit (per Power 1997) is a degenerate rank-1 projection onto a single compliance axis, discarding all information orthogonal to that axis -- an algebraic explanation for the information loss documented by audit-society research. Organizational Schema Theory's multi-level acceptance-testing cascade is full-rank, preserving dimensional structure across the specification hierarchy.

Three convergent lineages -- organizational cybernetics (Beer 1972; Beer 1984), behavioral organization theory (March and Simon 1958; Argyris and Schon 1978), and software engineering verification (Beck 2002) -- independently rely on the projection identity without naming it.

## Key Results

Python simulation (Appendix B): rank-1 audit misses approximately 90% of total organizational deviation across all noise levels. Three formal propositions establish:

- P1: rank inequality (rank-1 audit < full-rank cascade)
- P2: cascade-consistency condition for OST's six-level hierarchy
- P3: bandwidth bound on sustainable projection rank

## Files

| File | Description |
|------|-------------|
| `paper.md` | Full manuscript (markdown, v1.0.0) |
| `paper.yaml` | Machine-readable paper specification |
| `projection_simulation.py` | Python simulation (Appendix B) |
| `simulation_results.json` | Simulation outputs |
| `CITATION.cff` | Citation metadata |
| `CONTRIBUTORS.yaml` | Contributor attribution |
| `DATA_MANIFEST.yaml` | Data sources and method anchors |
| `PROVENANCE.yaml` | Drafting history and submission records |

## Status

**Working Paper v1.0.0.** 35 references, 2.9% self-cite. Target: Academy of Management Review. Fallback: Organization Science, Administrative Science Quarterly, Management Science (IS track).

## Relationship to Other Papers

- **OST (2026i)** -- L1 acceptance-testing cascade as primary instantiation of full-rank projection
- **R5 (2026h)** -- Verification rate bound; impossibility result grounded in cascade rank
- **R16 (2026x)** -- Brand Function as the invariant eigenspace the cascade must preserve
- **R19 (2026aa)** -- Rate-distortion / bandwidth framing; verification bandwidth bounds cascade rank
- **R22 (2026ad)** -- μ > λ stability condition for cascade under realistic organizational dynamics
