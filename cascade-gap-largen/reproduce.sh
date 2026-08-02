#!/usr/bin/env bash
# reproduce.sh — Cascade-Gap Large-N Study, single-command reproduction.
# Conforms to PUBLIC_MIRROR_STANDARD.md.
#
# Usage:
#   ./reproduce.sh                # download HF evidence + run the full pipeline
#   ./reproduce.sh --check-only   # verify dependencies; do not run
#   ./reproduce.sh --fast         # analysis-only from the vendored dataset (skip HF download)
#
# Outputs land in output/{tables,logs}/. Run log: output/logs/master_run.log
#
# What it reproduces from the released 350-case dataset:
#   - the confirmatory 2x2 and exact Clopper-Pearson upper bound
#   - necessity consistency, sufficiency, the AC1/kappa reliability read
#   - the registered sample-size derivation (seed 20260729)
# Re-running the CODING from scratch (LLM calls) is optional and needs API keys;
# it is NOT required to reproduce the reported statistics.

set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

LOG_FILE="output/logs/master_run.log"
mkdir -p output/tables output/logs

CHECK_ONLY=0; FAST=0
for arg in "${@:-}"; do
  case "$arg" in
    --check-only) CHECK_ONLY=1 ;;
    --fast) FAST=1 ;;
    "") ;;
    *) echo "Unknown flag: $arg"; exit 2 ;;
  esac
done

{
echo "=================================================="
echo "Cascade-gap reproduction: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "Repo: $REPO_ROOT"
echo "=================================================="

echo ">>> Checking dependencies..."
command -v uv >/dev/null 2>&1 || { echo "ERROR: uv not found (https://astral.sh/uv)"; exit 1; }
uv sync

if [[ "$CHECK_ONLY" == "1" ]]; then
  echo ">>> Check-only mode; exiting before pipeline."
  exit 0
fi

# 1. Fetch the evidence corpus from Hugging Face (dossiers + coded records + logs).
if [[ "$FAST" == "0" ]]; then
  echo ">>> Downloading evidence dataset from Hugging Face..."
  uv run --with huggingface_hub python - <<'PY'
from huggingface_hub import snapshot_download
p = snapshot_download(repo_id="spectralbranding/tba-cascade-gap-largen",
                      repo_type="dataset", local_dir="hf_evidence")
print("downloaded to", p)
PY
else
  echo ">>> --fast: skipping HF download; using vendored data/ only."
fi

# 2. Stage the analysis input where the (verbatim) scripts expect it.
cp data/full_draw_dataset.csv code/full_draw_dataset.csv

# 3. Confirmatory analysis: 2x2, exact CI, necessity, reliability.
echo ">>> Confirmatory necessary-condition analysis..."
( cd code && uv run --with scipy python analyze_full_draw.py ) | tee output/tables/analysis_stdout.txt

# 4. Registered sample-size derivation (self-checking kernels, seed 20260729).
echo ">>> Power analysis / registered N..."
( cd code && uv run --with scipy python power_analysis_s5.py --fixture ) | tee output/tables/power_stdout.txt

echo "=================================================="
echo "Reproduction complete: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "=================================================="
} 2>&1 | tee -a "$LOG_FILE"
