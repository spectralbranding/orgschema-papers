# output/

Hub-level output of `./reproduce.sh` at the repository root.

- `logs/hub_run.log` is the log of the last full hub run. Each run starts a new log.
- `figures/` and `tables/` are empty here by design. The hub only runs each paper's own
  `reproduce.sh`; figures, tables and per-script logs are written to that paper's folder:
  `cascade-gap-largen/output/`, `multi-llm-coding-instrument/output/`,
  `tier-bundle-algebra/output/`, `verification-bandwidth/output/`.

Papers without a `reproduce.sh` have no pipeline for the hub to run. Where such a paper has
companion scripts, they sit in its `code/` folder with the run command in each script header.
