# The Projection Cascade

**Title**: The Projection Cascade: Why Reorganizations Fail When the Specification Cascade Doesn't

**Author**: Dmitry Zharnikov ([ORCID 0009-0000-6893-9231](https://orcid.org/0009-0000-6893-9231))

**Citation key**: 2026m

**Status**: Working paper v2.1 (pre-Zenodo). v1 preserved at Zenodo concept DOI [10.5281/zenodo.19145205](https://doi.org/10.5281/zenodo.19145205). v2.1 concept DOI to be minted at release.

**Target venue**: Strategic Management Journal (primary); Academy of Management Review, Organization Science (alternates).

## What this paper does

Most major reorganizations fail to deliver expected performance gains — roughly 60 percent by meta-analytic estimate. This paper supplies a formal explanation: interventions at the org-chart surface (T_6) achieve effect-sizes geometrically smaller than interventions at deeper tiers, because each tier carries content already compressed in transit to the surface. The apparatus formalizes this as a six-tier *projection cascade* linking owner intent (T_1), business model (T_2), governance (T_3), product architecture (T_4), process routines (T_5), and positions (T_6). Each junction is a linear operator with rank deficiency that bounds information loss. Theorem 1 proves a unique cascade equilibrium under tier-by-tier Banach contractions. Corollary 1 shows that total information loss is junction-localizable: reorganizations fail specifically because the upstream rank deficiencies are not addressed.

## Three contributions

1. **Unification of design theories.** Galbraith's star, Williamson's governance choice, Mintzberg's configurations, Puranam's microstructure, and Burton-Obel-Hakonsson's computational design are recovered as nested cascade restrictions. The field's apparent fragmentation is a partial-view artifact, not ontological disagreement.

2. **Position formalization.** A *position triple* p = (P_p, A_p, R_p) decomposes any T_6 position into perceptual content from T_5, authority inherited from T_3, and role expectation from T_1 — the first formal multi-channel decomposition of "position" in the design literature.

3. **Four falsifiable propositions.** P1 cascade-distance scaling of reorganization-failure rate; P2 strict downward propagation of basis rotation under AI deployment; P3 variance amplification with cumulative rank deficiency; P4 algebraic decoupling at layer junctions. Each is derived from the apparatus, not stipulated separately.

## Companion computation script

All numerical values in §3.5 (Table 3, Corollary 1 sub-additivity verification, cascade Lipschitz bound) are reproducible from `code/cascade_numerical_example.py`:

```
uv run --with numpy python code/cascade_numerical_example.py
```

For the comparative-statics experiment (§4.6 cascade vs. design-theory restrictions):

```
uv run --with numpy python code/cascade_numerical_example.py --compare
```

Requires: Python 3.12+, numpy. No proprietary data. Fixed seed `SEED = 2026`.

## Files

- **paper.md** — full manuscript (~466 lines; Theorem 1; Corollary 1; 4 propositions; 4 tables; 1 Mermaid figure; Appendix A proof)
- **paper.yaml** — Paper Spec metadata (citation key, propositions, dependencies, AI disclosure)
- **CITATION.cff** — Citation File Format 1.2.0
- **CONTRIBUTORS.yaml** — contributor attribution
- **PROVENANCE.yaml** — version history and review pipeline summary
- **code/cascade_numerical_example.py** — companion computation script (735 lines; seed 2026)
- **code/README.md** — script documentation and run instructions
- **figures/cascade_schematic_mermaid.md** — Mermaid source for Figure 1 (Six-Tier Projection Cascade)

## Related work

This paper extends:
- [Zharnikov (2026ag) A Six-Tier Ontology](https://doi.org/10.5281/zenodo.19895813) — foundational six-tier architecture
- [Zharnikov (2026l) v1 Projection Paper](https://doi.org/10.5281/zenodo.19145205) — v1 single-step apparatus (preserved)
- [Zharnikov (2026ak) AI Tier Penetration](https://doi.org/10.5281/zenodo.20087036) — companion AI-deployment paper

## How to cite

Zharnikov, Dmitry. (2026). *The Projection Cascade: Why Reorganizations Fail When the Specification Cascade Doesn't*. Working paper v2.1. [DOI to be minted at v2.1 release]. https://github.com/spectralbranding/orgschema-papers/tree/main/projection-paper-v2

For v1 (preserved): Zharnikov, Dmitry. (2026). Working paper v1. Zenodo. https://doi.org/10.5281/zenodo.19145205

## License

CC-BY-4.0. Reuse permitted with attribution.
