# Companion computation — 2026bm

One script, one computation. It reproduces **Table 1** of the paper and the three figures quoted in
the paragraph beneath it.

## What is here

| File | What it is |
|---|---|
| `power_divergence_signature.py` | Monte Carlo power simulation for the crossover contrast |
| `output/power_divergence_signature.txt` | A recorded run, committed so a reader can compare without executing anything |

## Run it

```
uv run python code/power_divergence_signature.py
```

Run from the paper directory. The only dependency is NumPy. There is no configuration, no input file,
no network call and no environment variable — the script's parameter grid is written into the script
itself, so a clean checkout reproduces the published numbers exactly.

## What it reproduces

**Table 1** — the smallest per-arm sample size reaching power of .80 for the crossover contrast, over
three values of the correlation between the two investments and three per-arm standardised effects.

It also produces the three figures the paper quotes when reading that table: the equality of crossover
power and single-slope power at zero correlation (.352 against .349 at n = 40; .719 against .720 at
n = 100), which is why the paper states that the factor of two falls on the total sample rather than
on the contrast.

The seed is fixed at `20260810` and the output is deterministic, so the recorded run in `output/`
should match a fresh run byte for byte. Each cell is 20,000 replications at a two-sided alpha of .05.
If a future revision changes any number, the paper's Table 1 must be updated in the same commit — the
script is the ground truth for every value the paper calls simulated.

## Provenance

This code accompanies *Preparing to Sell and Preparing to Hand Over Are Rival Investments: A
Persistence Column for the Six-Tier Ontology*, concept DOI
[10.5281/zenodo.21868658](https://doi.org/10.5281/zenodo.21868658). The simulation supports the
paper's pre-registered design: it establishes what sample size the proposed study would need, and it
is the reason the paper states its target as a per-arm figure rather than a total. The design itself
has not been executed — no dataset accompanies this paper, and the reason is argued in the paper's
own text.

Licensed as the repository's code is licensed (MIT); the paper text is under CC-BY-4.0.
