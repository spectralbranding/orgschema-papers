# Capability as Projection of an Append-Only Organizational Log (2026al)

**Title**: Capability as Projection of an Append-Only Organizational Log: An Event-Sourced Substrate Theory of Organizational Capability and Transfer Failure

**Author**: Dmitry Zharnikov ([ORCID 0009-0000-6893-9231](https://orcid.org/0009-0000-6893-9231))

**Citation key**: 2026al

**Status**: Working paper v1.0.0. Phase-1.5 pre-draft critical review complete (verdict: GO). Phase-4 post-draft review cycle complete; companion code + Monte Carlo + honest event-coding pass complete and published in `code/`. Journal submission forthcoming after Zenodo upload.

**Concept DOI**: [10.5281/zenodo.20367459](https://doi.org/10.5281/zenodo.20367459)
**v1.0.0 DOI**: [10.5281/zenodo.20367460](https://doi.org/10.5281/zenodo.20367460)

## What this paper does

Organizational capability is commonly treated as a stock of resources or a bundle of routines. This paper argues that this conceptualization obscures a more fundamental object: an append-only, partially ordered organizational log that serves as the immutable substrate from which capabilities are computed. Capability itself is a render-time projection — π(L, q, t) — evaluated against a query-relevant subset of that log at the moment a strategic question is asked. The dominant resource- and dynamic-capabilities tradition treats capability as a noun. An event-sourced view treats capability as a verb. The paper formalizes the log as a poset of typed immutable events, defines a projection operator satisfying prefix monotonicity, conditional determinism, and locality, and introduces a compatibility function κ measuring conflict density between logs to be merged.

The framework is anchored in three process-traced cases — Disney's preservation of Pixar's creative log, Microsoft's snapshot import of Nokia's handset capability, and persistent imitation failure of the Toyota Production System — each coded under a pre-registered protocol. An open-source contemporaneous event-sourced runtime (Nakajima 2026 — ActiveGraph) supplies an existence proof that the proposed substrate is computationally tractable.

The substrate-projection distinction relocates the persistent tautology critique of dynamic capabilities from the projection (capability) layer to the unobserved substrate (log) layer, thereby converting a definitional problem into an identification problem.

## Three contributions

1. **Theoretical recasting** of organizational capability as a render-time property of an event-sourced operational log, sharpening the Penrose-Teece-Helfat tradition by separating substrate (log) from rendering (projection).
2. **Mechanism for transfer outcomes** derived from log-merge mechanics: clean merges preserve capability; snapshot imports without the underlying log produce visible but inert capability claims. The joint dependence of writedown magnitude on log incompatibility (1−κ) AND integration-policy choice is testable against M&A archival data.
3. **Empirical anchoring** through honest event-coding of three boundary cases + a 20,000-trial Monte Carlo simulation establishing numerical coherence of the propositions. Nakajima's ActiveGraph runtime (arXiv:2605.21997) supplies an in-the-wild engineering instance demonstrating that event-sourced organizational substrate is generative beyond analogy.

## Files

- `paper.md` — full paper (revised version incorporating Phase-4 fix pass and honest event-coding results forthcoming)
- `paper.yaml` — paper-spec schema (citation key, propositions, falsification criteria, dependencies, AI disclosure)
- `CITATION.cff` — citation file (CITATION File Format 1.2.0)
- `CONTRIBUTORS.yaml` — verified contributor attribution (CRediT taxonomy)
- `PROVENANCE.yaml` — version history and submission record
- `code/` — companion computation scripts + experiments + honest event-coding pass (see `code/README.md`)

## Companion articles (Substack)

This paper is preceded by a four-article public companion series:

- SBT *The Log Is the Brand: Why Marketing Is Runtime Exhaust* — [spectralbranding.substack.com](https://spectralbranding.substack.com/p/the-log-is-the-brand-why-marketing-is-runtime-exhaust) (Tue Aug 25)
- OST *The Business Is a Repository: Operations as Append-Only Log* — Thu Aug 27 (URL to follow)
- OST *Git Semantics for Companies* — Thu Sep 3 (URL to follow)
- OST *Capability Is Not What You Have. It's What Your History Renders.* — Sat Sep 12 (URL to follow)

## Related work

This paper extends and grounds in an event-sourced substrate the following prior contributions:

- The OST six-tier architecture: [Zharnikov (2026i) Organizational Schema Theory](https://doi.org/10.5281/zenodo.18946043). The log sits beneath all six tiers; each tier renders a projection of the same log.
- The six-tier M&A failure propagation model: [Zharnikov (2026ag) Dual Hierarchies of Organizational Transferability](https://doi.org/10.5281/zenodo.19895813)
- The brand-substrate decoupling model: [Zharnikov (2026ai) The Tier-Rotation Curve](https://doi.org/10.5281/zenodo.20069605)
- The projection cascade: [Zharnikov (2026m) The Projection Cascade](https://doi.org/10.5281/zenodo.19145205)

## Companion computation scripts

Reproducible scripts and experiment outputs are in `code/`. See `code/README.md` for full run instructions and the pre/post experiment reports.

- `projection_demo.py` — worked formalism example: [GitHub link](https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/projection_demo.py)
- `monte_carlo_simulation.py` — 20,000-trial Monte Carlo of π_λ comparative statics: [GitHub link](https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/monte_carlo_simulation.py)
- `case_event_coding/` — single-coder honest pass of the pre-registered METHODS_APPENDIX protocol on Disney+Pixar 2006, Microsoft+Nokia 2014, Toyota TPS: [GitHub link](https://github.com/spectralbranding/orgschema-papers/tree/main/capability-as-projection/code/case_event_coding/)
- `PRE_EXPERIMENT_REPORT.md` — pre-registered hypotheses, parameters, success criteria: [GitHub link](https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/PRE_EXPERIMENT_REPORT.md)
- `POST_EXPERIMENT_REPORT.md` — actual results, replication instructions, honest scope caveats: [GitHub link](https://github.com/spectralbranding/orgschema-papers/blob/main/capability-as-projection/code/POST_EXPERIMENT_REPORT.md)

## License

Creative Commons Attribution 4.0 International (CC BY 4.0).

## How to cite

```
Zharnikov, Dmitry (2026), "Capability as Projection of an Append-Only Organizational Log: An Event-Sourced Substrate Theory of Organizational Capability and Transfer Failure," Working Paper v1.0.0, Zenodo, doi:10.5281/zenodo.20367460. Concept DOI: 10.5281/zenodo.20367459.
```
