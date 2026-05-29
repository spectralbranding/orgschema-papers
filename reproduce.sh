#!/usr/bin/env bash
# reproduce.sh — Hub-level orchestrator
#
# Iterates paper-slug subdirectories (any subdir that contains paper.md or
# paper.yaml) and invokes each per-paper reproduce.sh if present.
# Conforms to PUBLIC_MIRROR_STANDARD.md v1.0.0.
#
# Usage:
#   ./reproduce.sh                  # Run every per-paper reproduce.sh
#   ./reproduce.sh --check-only     # Verify per-paper orchestrators exist; do not execute
#   ./reproduce.sh --fast           # Pass --fast through to each per-paper reproduce.sh
#
# Run log lands in output/logs/hub_run.log

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

mkdir -p output/figures output/tables output/logs
LOG_FILE="output/logs/hub_run.log"

echo "==================================================" | tee -a "$LOG_FILE"
echo "Hub pipeline run: $(date -u +%Y-%m-%dT%H:%M:%SZ)" | tee -a "$LOG_FILE"
echo "Repo: $REPO_ROOT" | tee -a "$LOG_FILE"
echo "Git SHA: $(git rev-parse HEAD 2>/dev/null || echo 'not-a-repo')" | tee -a "$LOG_FILE"
echo "==================================================" | tee -a "$LOG_FILE"

# Parse flags
CHECK_ONLY=0
FAST=0
for arg in "$@"; do
  case "$arg" in
    --check-only) CHECK_ONLY=1 ;;
    --fast) FAST=1 ;;
    *) echo "Unknown flag: $arg" | tee -a "$LOG_FILE"; exit 2 ;;
  esac
done

PAPER_COUNT=0
RUN_COUNT=0
SKIP_COUNT=0

# Discover paper-slug subdirectories. A subdir is a paper-slug iff it contains
# paper.md or paper.yaml at its root.
for child in "$REPO_ROOT"/*/; do
  child="${child%/}"
  slug="$(basename "$child")"
  case "$slug" in
    output|.*) continue ;;
  esac
  if [[ -f "$child/paper.md" || -f "$child/paper.yaml" ]]; then
    PAPER_COUNT=$((PAPER_COUNT + 1))
    if [[ -x "$child/reproduce.sh" ]]; then
      echo ">>> [$slug] invoking per-paper reproduce.sh" | tee -a "$LOG_FILE"
      if [[ "$CHECK_ONLY" == "1" ]]; then
        ( cd "$child" && ./reproduce.sh --check-only ) 2>&1 | tee -a "$LOG_FILE"
      elif [[ "$FAST" == "1" ]]; then
        ( cd "$child" && ./reproduce.sh --fast ) 2>&1 | tee -a "$LOG_FILE"
      else
        ( cd "$child" && ./reproduce.sh ) 2>&1 | tee -a "$LOG_FILE"
      fi
      RUN_COUNT=$((RUN_COUNT + 1))
    elif [[ -f "$child/reproduce.sh" ]]; then
      echo ">>> [$slug] reproduce.sh present but not executable — skipping" | tee -a "$LOG_FILE"
      SKIP_COUNT=$((SKIP_COUNT + 1))
    else
      echo ">>> [$slug] no reproduce.sh — skipping (paper-only mirror)" | tee -a "$LOG_FILE"
      SKIP_COUNT=$((SKIP_COUNT + 1))
    fi
  fi
done

echo "==================================================" | tee -a "$LOG_FILE"
echo "Hub pipeline complete: $(date -u +%Y-%m-%dT%H:%M:%SZ)" | tee -a "$LOG_FILE"
echo "Paper-slugs discovered: $PAPER_COUNT" | tee -a "$LOG_FILE"
echo "Per-paper reproduce.sh executed: $RUN_COUNT" | tee -a "$LOG_FILE"
echo "Per-paper skipped (no orchestrator): $SKIP_COUNT" | tee -a "$LOG_FILE"
echo "==================================================" | tee -a "$LOG_FILE"
