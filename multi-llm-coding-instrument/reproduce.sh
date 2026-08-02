#!/usr/bin/env bash
# reproduce.sh — Multi-LLM Coding Instrument: recompute reliability from the vendored dataset.
# Conforms to PUBLIC_MIRROR_STANDARD.md.
#   ./reproduce.sh              # run
#   ./reproduce.sh --check-only # verify deps only
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; cd "$REPO_ROOT"
mkdir -p output/tables output/logs
LOG="output/logs/master_run.log"
{
echo "=== Instrument reproduction: $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
command -v uv >/dev/null 2>&1 || { echo "ERROR: uv not found"; exit 1; }
uv sync
[[ "${1:-}" == "--check-only" ]] && { echo "check-only; done."; exit 0; }
echo ">>> Fixture self-check..."
uv run --no-project --with scipy --with numpy python code/analyze_study_n30.py --fixture
echo ">>> Reliability on the coded dataset..."
uv run --no-project --with scipy --with numpy python code/analyze_study_n30.py --data data/coded_dataset_n30.csv | tee output/tables/reliability_stdout.txt
echo "=== complete: $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
} 2>&1 | tee -a "$LOG"
