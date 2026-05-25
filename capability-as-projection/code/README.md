# Companion computation scripts — Zharnikov 2026al

Companion code for:

> Zharnikov, D. (2026). *Capability as Projection of an Append-Only Organizational Log: An Event-Sourced Substrate Theory of Organizational Capability and Transfer Failure*. Working paper. doi:10.5281/zenodo.20367460

Per the corpus computational-reproducibility standard, every computed numerical value cited in the paper must be reproducible from a script in this directory with a fixed seed and a documented run command.

## Files in this directory

| File | Purpose |
|---|---|
| `projection_demo.py` | Worked example of the formalism on a 20-event synthetic two-firm scenario |
| `monte_carlo_simulation.py` | Comparative-statics Monte Carlo (20,000 trials across density x lambda x policy) |
| `requirements.txt` | Pinned dependencies (numpy, matplotlib, pandas) |
| `PRE_EXPERIMENT_REPORT.md` | Pre-registered hypotheses, parameters, success criteria |
| `POST_EXPERIMENT_REPORT.md` | Actual outputs, comparison to predictions, replication instructions |
| `monte_carlo_results.csv` | Aggregated results (one row per density-lambda-policy cell) |
| `plots/plot_projection_continuity_vs_kappa.png` | P1 + P2 visualization |
| `plots/plot_writedown_vs_conflict_density.png` | P3 visualization |
| `logs/projection_demo_output.txt` | Captured stdout from `projection_demo.py` |
| `logs/monte_carlo_run_output.txt` | Captured stdout from `monte_carlo_simulation.py` |
| `case_event_coding/` | Event logs and coding reports for the three process-traced cases; committed alongside the Zenodo upload |

## Run order

1. Install dependencies (or use `uv run --with ...` per the commands below).
2. Run `projection_demo.py` first — fast (sub-second) sanity check on the formalism.
3. Run `monte_carlo_simulation.py` second — completes in under 30 seconds on a 2024 Apple Silicon Mac.

```
uv run --with numpy==2.2.2 --with matplotlib==3.10.0 --with pandas==2.2.3 python projection_demo.py
uv run --with numpy==2.2.2 --with matplotlib==3.10.0 --with pandas==2.2.3 python monte_carlo_simulation.py
```

Or with a venv:

```
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt
python projection_demo.py
python monte_carlo_simulation.py
```

## What the experiments show

The simulations are **numerical-coherence checks** for the propositions P1, P2, P3 stated in `FORMALISM_v0.md` Section 3. They demonstrate that:

- A clean (negotiated) log merge preserves projection continuity across the full range of synthetic conflict densities, with only a small negotiation cost (P1).
- The acquirer-supreme merge policy — the snapshot-import failure mode — produces a continuity gap that widens monotonically with conflict density (P2).
- Simulated writedown magnitude rises monotonically with conflict density `1 - kappa`, and the gap between the two policies is the substrate-vs-snapshot wedge the paper argues for (P3).

See `PRE_EXPERIMENT_REPORT.md` for the pre-registered hypotheses and success criteria, and `POST_EXPERIMENT_REPORT.md` for the per-check PASS/FAIL evaluation and the explicit scope limitation (synthetic data; not an empirical confirmation in real firms).

## Reproducibility

- All scripts use Python 3.12 with `RANDOM_SEED = 42`.
- Run commands are documented in each script's module docstring.
- Output is deterministic across platforms; minor differences (1e-9) may appear under different BLAS implementations but do not affect the aggregate statistics.
- No network calls; no external data; no API keys.

## `case_event_coding/`

Event-log CSVs and coding reports for the three process-traced cases will be committed here alongside the Zenodo upload:

- `disney_pixar_events.csv` — coded event log for the Disney+Pixar acquisition (2006-2012)
- `microsoft_nokia_events.csv` — coded event log for the Microsoft+Nokia acquisition (2013-2016)
- `toyota_tps_events.csv` — coded event log for the Toyota Production System (longitudinal sample)
- `coding_report.md` — inter-rater reliability report and coding protocol

These case event-coding outputs ship alongside the paper in the v1.0.0 Zenodo deposit.

## License

MIT (matching the paper's public mirror license).
