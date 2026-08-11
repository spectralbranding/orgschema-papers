#!/usr/bin/env bash
#
# Reproduce every computed number in "Verification Bandwidth Under Correlated Evaluators".
#
# Concept DOI 10.5281/zenodo.21891435
#
# No network access, no provider key, and no data download are required: this paper
# collected no dataset. Every figure it reports is either arithmetic on another study's
# published summary statistics or a seeded simulation, and both are regenerated here from
# source. The whole pipeline runs in well under a minute on a laptop -- the Monte Carlo
# cells are large (200,000 to 2,000,000 draws) but vectorized.
#
#   ./reproduce.sh              run everything, write output/ and logs
#   ./reproduce.sh --quick      skip the two Monte Carlo scripts (Table 2, Table A1,
#                               and the figures are then not regenerated)
#
# Every script fixes seed 20260811 at file top and exits nonzero if any of its internal
# checks fails, so a silent numerical regression cannot pass this orchestrator.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODE="$HERE/code"
LOGS="$HERE/output/logs"
QUICK=0
[[ "${1:-}" == "--quick" ]] && QUICK=1

mkdir -p "$LOGS" "$HERE/output/tables" "$HERE/output/figures"
MASTER="$LOGS/master_run.log"

log() { printf '%s  %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$MASTER"; }

# ---- dependency check -------------------------------------------------------
# uv resolves per-script dependencies inline, so nothing is installed globally.
if ! command -v uv >/dev/null 2>&1; then
    echo "uv is required: https://docs.astral.sh/uv/  (or run each script under any" >&2
    echo "Python 3.12 environment with numpy, scipy and matplotlib available)" >&2
    exit 1
fi

: > "$MASTER"
log "reproduce.sh starting"
log "python: $(uv run python -c 'import sys; print(sys.version.split()[0])')"
log "seed: 20260811 (fixed in every script)"
log "quick mode: $QUICK"

run() {
    local name="$1"; shift
    log "--- running $name"
    if ( cd "$CODE" && "$@" ) > "$LOGS/${name%.py}.log" 2>&1; then
        log "    $name OK -> output/logs/${name%.py}.log"
        cat "$LOGS/${name%.py}.log" >> "$MASTER"
    else
        log "    $name FAILED -- see output/logs/${name%.py}.log"
        cat "$LOGS/${name%.py}.log" >> "$MASTER"
        exit 1
    fi
}

# ---- pipeline, in dependency order ------------------------------------------
# 1. The identification. Pure arithmetic on published summary statistics, no RNG.
#    This is the standing guard: it fails if the paper ever claims the estimator
#    it cites rather than citing it.
run reported_neff_check.py uv run --with numpy --with scipy python reported_neff_check.py

# 2. The map from inspection geometry to error correlation, its properties, the
#    panel-recovery check behind Table 2, and both figures.
if [[ $QUICK -eq 0 ]]; then
    run phi_mapping.py uv run --with numpy --with scipy --with matplotlib python phi_mapping.py
else
    log "--- skipping phi_mapping.py (quick mode; Table 2 and the figures are not regenerated)"
fi

# 3. The exact single-factor bracket width behind Tables 1 and 4.
run p2_exact.py uv run --with numpy --with scipy python p2_exact.py

# 4. Checks on the propositions, and the worst-case block of Table 5.
run formal_model_checks.py uv run --with numpy --with scipy python formal_model_checks.py

# 5. The bracket simulation behind Table A1.
if [[ $QUICK -eq 0 ]]; then
    run threat1_kill_test.py uv run --with numpy python threat1_kill_test.py
else
    log "--- skipping threat1_kill_test.py (quick mode; Table A1 is not regenerated)"
fi

# 6. Machine-readable projection of the deterministic tables, for diffing the paper
#    against its own derivations.
run emit_paper_tables.py uv run --with numpy --with scipy python emit_paper_tables.py

log "all steps completed"
log "tables:  output/tables/*.csv"
log "figures: output/figures/*.png"
log "logs:    output/logs/*.log"
