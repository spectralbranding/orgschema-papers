"""friction_tax_montecarlo.py -- Monte Carlo simulation of friction-tax dynamics
under push and pull regimes.

Companion computation script for:

    Zharnikov, D. (2026). Toward a Thermodynamic Theory of Organizational
    Coupling: Push, Pull, and the Multi-Interface Architecture of the Firm
    Under AI Mediation. Working paper key: 2026am.

Implements the Monte Carlo simulation specified in METHODS_APPENDIX.md
Section A (pre-registered before execution). Anti-HARKing discipline:
the hypotheses, effect sizes, parameter grid, and falsification conditions
are fixed in METHODS_APPENDIX.md and in PRE_EXPERIMENT_NOTES.md. No
post-hoc parameter changes are permitted without a dated changelog entry.

Formal model (METHODS_APPENDIX Section A.2):
    - Specification vector s in R^d, d = 8 (SBT eight dimensions).
    - Recipient need vector n_i = s + epsilon_i, epsilon_i ~ N(0, sigma^2 I).
    - Guessed need vector g_i = s + eta_i, eta_i ~ N(0, sigma^2 I), indep. of epsilon_i.
    - Push friction: f_push(i) = ||n_i - g_i||^2 = ||epsilon_i - eta_i||^2.
    - Pull friction: f_pull(i) = ||epsilon_query_i||^2, epsilon_query_i ~ N(0, (0.01*sigma)^2 I).
    - Alpha interpolation: f(i, alpha) = (1 - alpha) * f_push(i) + alpha * f_pull(i).
    - Aggregate: F(alpha) = mean over N recipients of f(i, alpha).

Parameter grid (full factorial):
    sigma in {.1, .2, .3, .5, .7, 1.0}
    N in {100, 500, 1000, 5000}
    alpha in {0, .2, .4, .6, .8, 1.0}
    d = 8 (fixed)
    functional form: quadratic (primary), L1, log-quadratic (robustness)
    Total cells: 6 x 4 x 6 x 3 = 432; each x 10,000 trials = 4,320,000 measurements.

Implementation note: all trials for a given (sigma, N, form, sigma_query_mult)
cell are computed simultaneously using vectorized numpy operations. The full trial
batch for a cell with N=5000 is shape (N_TRIALS, N, D) which may consume ~3 GB RAM
for the largest cells. To manage memory, N=5000 cells use chunked batching
(CHUNK_SIZE = 1000 trials per chunk).

Fixed seed: np.random.seed(20260525)

Outputs (under code/plots/ and code/):
    plots/friction_distribution_push_vs_pull.png
    plots/phase_shift_alpha.png
    plots/sensitivity_misalignment.png
    plots/functional_form_comparison.png
    monte_carlo_summary.csv
    logs/monte_carlo_run_<YYYYMMDD>.log

Run command (from the paper directory):
    uv run --with numpy==2.2.2 --with scipy==1.14.0 --with statsmodels==0.14.4 \\
           --with matplotlib==3.10.0 --with pandas==2.2.3 \\
           python code/friction_tax_montecarlo.py

Expected runtime: 5-15 minutes on a 2024 Apple Silicon Mac.

Falsification condition (METHODS_APPENDIX A.4):
    H_A is falsified if mu_push / mu_pull < 2.0 at any tested sigma value
    under baseline parameters (N=1000, alpha=0, quadratic norm).

Scope note: This is a numerical-coherence check for the formalism. It
demonstrates internal consistency across the specified parameter space.
It does not constitute empirical confirmation in real firms.
"""

from __future__ import annotations

import csv
import datetime
import logging
import sys
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy import stats  # noqa: E402

# ---------------------------------------------------------------------------
# Fixed seed -- must not be changed post-execution
# ---------------------------------------------------------------------------
RANDOM_SEED: int = 20260525
np.random.seed(RANDOM_SEED)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
CODE_DIR = Path(__file__).resolve().parent
PLOT_DIR = CODE_DIR / "plots"
LOG_DIR = CODE_DIR / "logs"
CSV_PATH = CODE_DIR / "monte_carlo_summary.csv"
LOG_PATH = LOG_DIR / f"monte_carlo_run_{datetime.date.today():%Y%m%d}.log"

PLOT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Logger: write to both stdout and file
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_PATH, mode="w", encoding="utf-8"),
    ],
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Parameter grid (pre-registered; METHODS_APPENDIX A.3)
# ---------------------------------------------------------------------------
SIGMAS: tuple[float, ...] = (0.1, 0.2, 0.3, 0.5, 0.7, 1.0)
N_RECIPIENTS: tuple[int, ...] = (100, 500, 1_000, 5_000)
ALPHAS: tuple[float, ...] = (0.0, 0.2, 0.4, 0.6, 0.8, 1.0)
D: int = 8  # specification dimensionality (SBT 8 dimensions)
N_TRIALS: int = 10_000
FUNCTIONAL_FORMS: tuple[str, ...] = ("quadratic", "l1", "log_quadratic")

# Pre-registered sigma_query multipliers for pull-friction robustness check
SIGMA_QUERY_MULTIPLIERS: tuple[float, ...] = (0.01, 0.10, 0.30)


# Chunking for memory management: target ~32 MB per array (T, N, D) float64.
# 32 MB = 32e6 bytes / 8 bytes_per_float64 / (N * D) = 4_000_000 / (N * 8).
# For N=100: chunk~5000; N=500: chunk~1000; N=1000: chunk~500; N=5000: chunk~100.
def _chunk_size(n: int) -> int:
    target_elements = 4_000_000  # 32 MB / 8 bytes
    return max(200, target_elements // (n * D))


# ---------------------------------------------------------------------------
# Vectorized friction computation -- operates on batch shape (T, N, D)
# where T = number of trials in the chunk, N = number of recipients
# ---------------------------------------------------------------------------


def batch_push_quadratic(epsilon: np.ndarray, eta: np.ndarray) -> np.ndarray:
    """Squared Euclidean distance. epsilon, eta shape (T, N, D) -> (T, N)."""
    return np.sum((epsilon - eta) ** 2, axis=-1)


def batch_push_l1(epsilon: np.ndarray, eta: np.ndarray) -> np.ndarray:
    """L1 distance. epsilon, eta shape (T, N, D) -> (T, N)."""
    return np.sum(np.abs(epsilon - eta), axis=-1)


def batch_push_log_quadratic(epsilon: np.ndarray, eta: np.ndarray) -> np.ndarray:
    """Log-quadratic penalty. shape (T, N, D) -> (T, N)."""
    sq = np.sum((epsilon - eta) ** 2, axis=-1)
    return np.log1p(sq)


def batch_pull_quadratic(delta: np.ndarray) -> np.ndarray:
    return np.sum(delta**2, axis=-1)


def batch_pull_l1(delta: np.ndarray) -> np.ndarray:
    return np.sum(np.abs(delta), axis=-1)


def batch_pull_log_quadratic(delta: np.ndarray) -> np.ndarray:
    sq = np.sum(delta**2, axis=-1)
    return np.log1p(sq)


PUSH_FN = {
    "quadratic": batch_push_quadratic,
    "l1": batch_push_l1,
    "log_quadratic": batch_push_log_quadratic,
}
PULL_FN = {
    "quadratic": batch_pull_quadratic,
    "l1": batch_pull_l1,
    "log_quadratic": batch_pull_log_quadratic,
}

# ---------------------------------------------------------------------------
# Single-cell simulation -- fully vectorized
# ---------------------------------------------------------------------------


def simulate_cell(
    sigma: float,
    n: int,
    alpha: float,
    form: str,
    sigma_query_mult: float = 0.01,
    rng: np.random.Generator | None = None,
) -> dict:
    """Run N_TRIALS for a single (sigma, N, alpha, form) cell.

    Uses chunked vectorized computation: all trials in a chunk are computed
    simultaneously. For large N cells (N=5000) this keeps RAM manageable.

    Returns summary statistics dict. Arrays for plotting are NOT returned
    here (they are recomputed on demand for the baseline cell).
    """
    if rng is None:
        rng = np.random.default_rng()

    sigma_query = sigma_query_mult * sigma
    push_fn = PUSH_FN[form]
    pull_fn = PULL_FN[form]

    chunk = _chunk_size(n)
    n_chunks = (N_TRIALS + chunk - 1) // chunk

    F_push_all = np.empty(N_TRIALS)
    F_pull_all = np.empty(N_TRIALS)

    idx = 0
    for c in range(n_chunks):
        t_start = idx
        t_end = min(idx + chunk, N_TRIALS)
        t_size = t_end - t_start

        # shape (t_size, n, D)
        epsilon = rng.normal(0.0, sigma, size=(t_size, n, D))
        eta = rng.normal(0.0, sigma, size=(t_size, n, D))
        delta = rng.normal(0.0, sigma_query, size=(t_size, n, D))

        # shape (t_size, n) -> (t_size,) after mean over recipients
        f_push = push_fn(epsilon, eta).mean(axis=1)
        f_pull = pull_fn(delta).mean(axis=1)

        F_push_all[t_start:t_end] = f_push
        F_pull_all[t_start:t_end] = f_pull
        idx = t_end

    # Interpolated aggregate
    F_alpha = (1.0 - alpha) * F_push_all + alpha * F_pull_all

    mu_push = float(F_push_all.mean())
    sd_push = float(F_push_all.std(ddof=1))
    mu_pull = float(F_pull_all.mean())
    sd_pull = float(F_pull_all.std(ddof=1))
    mu_alpha = float(F_alpha.mean())

    pooled_sd = float(np.sqrt((sd_push**2 + sd_pull**2) / 2.0))
    cohens_d = float((mu_push - mu_pull) / pooled_sd) if pooled_sd > 0 else np.nan
    ratio = float(mu_push / mu_pull) if mu_pull > 0 else np.inf

    p25_push = float(np.percentile(F_push_all, 2.5))
    p975_push = float(np.percentile(F_push_all, 97.5))
    p25_pull = float(np.percentile(F_pull_all, 2.5))
    p975_pull = float(np.percentile(F_pull_all, 97.5))

    return {
        "sigma": sigma,
        "N": n,
        "alpha": alpha,
        "functional_form": form,
        "sigma_query_mult": sigma_query_mult,
        "mu_push_mean": mu_push,
        "mu_push_sd": sd_push,
        "mu_push_p25": p25_push,
        "mu_push_p975": p975_push,
        "mu_pull_mean": mu_pull,
        "mu_pull_sd": sd_pull,
        "mu_pull_p25": p25_pull,
        "mu_pull_p975": p975_pull,
        "mu_alpha_mean": mu_alpha,
        "cohens_d": cohens_d,
        "ratio_push_pull": ratio,
        "n_trials": N_TRIALS,
    }


def simulate_cell_with_arrays(
    sigma: float,
    n: int,
    form: str,
    sigma_query_mult: float = 0.01,
    rng: np.random.Generator | None = None,
) -> tuple[np.ndarray, np.ndarray, dict]:
    """Like simulate_cell at alpha=0 but also returns F_push / F_pull arrays.

    Used for the baseline density plot only.
    """
    if rng is None:
        rng = np.random.default_rng()
    sigma_query = sigma_query_mult * sigma
    push_fn = PUSH_FN[form]
    pull_fn = PULL_FN[form]
    chunk = _chunk_size(n)
    n_chunks = (N_TRIALS + chunk - 1) // chunk
    F_push = np.empty(N_TRIALS)
    F_pull = np.empty(N_TRIALS)
    idx = 0
    for _ in range(n_chunks):
        t_start = idx
        t_end = min(idx + chunk, N_TRIALS)
        t_size = t_end - t_start
        epsilon = rng.normal(0.0, sigma, size=(t_size, n, D))
        eta = rng.normal(0.0, sigma, size=(t_size, n, D))
        delta = rng.normal(0.0, sigma_query, size=(t_size, n, D))
        F_push[t_start:t_end] = push_fn(epsilon, eta).mean(axis=1)
        F_pull[t_start:t_end] = pull_fn(delta).mean(axis=1)
        idx = t_end

    mu_push = float(F_push.mean())
    sd_push = float(F_push.std(ddof=1))
    mu_pull = float(F_pull.mean())
    sd_pull = float(F_pull.std(ddof=1))
    pooled_sd = float(np.sqrt((sd_push**2 + sd_pull**2) / 2.0))
    cohens_d = float((mu_push - mu_pull) / pooled_sd) if pooled_sd > 0 else np.nan
    ratio = float(mu_push / mu_pull) if mu_pull > 0 else np.inf

    info = {
        "sigma": sigma,
        "N": n,
        "alpha": 0.0,
        "functional_form": form,
        "sigma_query_mult": sigma_query_mult,
        "mu_push_mean": mu_push,
        "mu_push_sd": sd_push,
        "mu_pull_mean": mu_pull,
        "mu_pull_sd": sd_pull,
        "cohens_d": cohens_d,
        "ratio_push_pull": ratio,
    }
    return F_push, F_pull, info


# ---------------------------------------------------------------------------
# Phase-shift alpha* computation
# ---------------------------------------------------------------------------


def compute_phase_shift_curve(
    sigma: float,
    n: int = 1_000,
    form: str = "quadratic",
    rng: np.random.Generator | None = None,
) -> tuple[np.ndarray, np.ndarray, float]:
    """Compute F(alpha) / F(0) across alpha in [0, 1] for a given sigma.

    Returns (alpha_grid, normalized_F, alpha_star).
    alpha_star is the smallest alpha where F(alpha) / F(0) < .10.
    """
    if rng is None:
        rng = np.random.default_rng()

    F_push, F_pull, _ = simulate_cell_with_arrays(
        sigma=sigma,
        n=n,
        form=form,
        sigma_query_mult=0.01,
        rng=rng,
    )
    mu_push = F_push.mean()
    mu_pull = F_pull.mean()

    alpha_grid = np.linspace(0.0, 1.0, 101)
    F_alpha = (1.0 - alpha_grid) * mu_push + alpha_grid * mu_pull
    F_normalized = F_alpha / mu_push if mu_push > 0 else F_alpha

    threshold = 0.10
    below = np.where(F_normalized < threshold)[0]
    alpha_star = float(alpha_grid[below[0]]) if len(below) > 0 else 1.0

    return alpha_grid, F_normalized, alpha_star


# ---------------------------------------------------------------------------
# Dimensionality robustness check (Alternative 1)
# ---------------------------------------------------------------------------


def simulate_dimensionality_check(
    sigma: float = 0.3,
    n: int = 1_000,
    d_values: tuple[int, ...] = (2, 4, 8, 16),
    rng: np.random.Generator | None = None,
) -> dict[int, float]:
    """Push/pull ratio across dimensionalities. Returns {d: ratio}."""
    if rng is None:
        rng = np.random.default_rng()

    results = {}
    sigma_query = 0.01 * sigma

    for d in d_values:
        # Use d (not D) for dimensionality check cells
        chunk_d = max(200, 4_000_000 // (n * d))
        n_chunks = (N_TRIALS + chunk_d - 1) // chunk_d
        F_push = np.empty(N_TRIALS)
        F_pull = np.empty(N_TRIALS)
        idx = 0
        for _ in range(n_chunks):
            t_start = idx
            t_end = min(idx + chunk_d, N_TRIALS)
            t_size = t_end - t_start
            epsilon = rng.normal(0.0, sigma, size=(t_size, n, d))
            eta = rng.normal(0.0, sigma, size=(t_size, n, d))
            delta = rng.normal(0.0, sigma_query, size=(t_size, n, d))
            F_push[t_start:t_end] = batch_push_quadratic(epsilon, eta).mean(axis=1)
            F_pull[t_start:t_end] = batch_pull_quadratic(delta).mean(axis=1)
            idx = t_end
        ratio = float(F_push.mean() / F_pull.mean()) if F_pull.mean() > 0 else np.inf
        results[d] = ratio

    return results


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------


def plot_friction_distribution(
    F_push: np.ndarray,
    F_pull: np.ndarray,
    info: dict,
    out_path: Path,
) -> None:
    """Overlapping density plots of push vs pull at baseline parameters."""
    mu_push = info["mu_push_mean"]
    mu_pull = info["mu_pull_mean"]
    cohens_d = info["cohens_d"]
    sigma = info["sigma"]
    n = info["N"]
    ratio = info["ratio_push_pull"]

    fig, ax = plt.subplots(figsize=(8.0, 5.5))

    kde_push = stats.gaussian_kde(F_push)
    x_push = np.linspace(F_push.min(), F_push.max(), 600)
    ax.fill_between(
        x_push,
        kde_push(x_push),
        alpha=0.4,
        color="#2166ac",
        label=f"Push regime (mu = {mu_push:.4f})",
    )
    ax.plot(x_push, kde_push(x_push), color="#2166ac", linewidth=1.5)

    if F_pull.std() > 1e-12:
        kde_pull = stats.gaussian_kde(F_pull)
        x_pull = np.linspace(F_pull.min(), F_pull.max(), 600)
        ax.fill_between(
            x_pull,
            kde_pull(x_pull),
            alpha=0.4,
            color="#d73027",
            label=f"Pull regime (mu = {mu_pull:.8f})",
        )
        ax.plot(x_pull, kde_pull(x_pull), color="#d73027", linewidth=1.5)
    else:
        ax.axvline(
            mu_pull,
            color="#d73027",
            linewidth=2.0,
            linestyle="--",
            label=f"Pull regime (mu = {mu_pull:.8f}, near-zero)",
        )

    ax.set_xlabel(
        "Aggregate friction-tax cost F (squared specification-distance units)"
    )
    ax.set_ylabel("Density")
    ax.set_title(
        f"Push vs pull friction-tax distribution\n"
        f"sigma = {sigma}, N = {n}, alpha = 0, quadratic norm\n"
        f"Cohen's d = {cohens_d:.2f}, ratio mu_push/mu_pull = {ratio:.0f}"
    )
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_phase_shift(
    phase_data: dict[float, tuple[np.ndarray, np.ndarray, float]],
    out_path: Path,
) -> None:
    """F(alpha) / F(0) vs alpha for multiple sigma values."""
    fig, ax = plt.subplots(figsize=(8.0, 5.5))
    colors = {0.1: "#1b7837", 0.3: "#762a83", 0.7: "#e08214", 1.0: "#d6604d"}

    for sigma, (alpha_grid, F_norm, alpha_star) in phase_data.items():
        color = colors.get(sigma, "#333333")
        ax.plot(
            alpha_grid,
            F_norm,
            color=color,
            linewidth=2.0,
            label=f"sigma = {sigma} (alpha* = {alpha_star:.2f})",
        )
        ax.axvline(alpha_star, color=color, linewidth=0.8, linestyle=":")

    ax.axhline(
        0.10, color="gray", linewidth=1.0, linestyle="--", label="10% of F(0) threshold"
    )
    ax.set_xlabel("AI-mediation factor alpha")
    ax.set_ylabel("F(alpha) / F(0)  [normalized friction cost]")
    ax.set_title(
        "Phase-shift curve: normalized friction vs AI-mediation factor\n"
        "N = 1000, quadratic norm. Vertical dots mark alpha* threshold."
    )
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.05)
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_sensitivity_misalignment(
    rows: list[dict],
    out_path: Path,
) -> None:
    """mu_push / mu_pull ratio vs sigma for N in {100, 1000, 5000}."""
    fig, ax = plt.subplots(figsize=(8.0, 5.5))
    colors = {100: "#1f77b4", 1_000: "#ff7f0e", 5_000: "#2ca02c"}

    for n_val in (100, 1_000, 5_000):
        subset = [
            r
            for r in rows
            if r["N"] == n_val
            and r["alpha"] == 0.0
            and r["functional_form"] == "quadratic"
            and r["sigma_query_mult"] == 0.01
        ]
        if not subset:
            continue
        subset_sorted = sorted(subset, key=lambda r: r["sigma"])
        sigmas = [r["sigma"] for r in subset_sorted]
        ratios = [r["ratio_push_pull"] for r in subset_sorted]
        ax.plot(
            sigmas,
            ratios,
            marker="o",
            linewidth=2.0,
            markersize=6,
            color=colors.get(n_val, "#333333"),
            label=f"N = {n_val:,}",
        )

    ax.set_xlabel("Misalignment variance sigma")
    ax.set_ylabel("mu_push / mu_pull ratio  (log scale)")
    ax.set_yscale("log")
    ax.set_title(
        "Push/pull friction ratio vs misalignment variance\n"
        "alpha = 0, quadratic norm, sigma_query = .01 * sigma"
    )
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_functional_form_comparison(
    rows: list[dict],
    out_path: Path,
) -> None:
    """Cohen's d vs sigma for three functional forms at N=1000, alpha=0."""
    fig, ax = plt.subplots(figsize=(8.0, 5.5))
    colors = {"quadratic": "#1f77b4", "l1": "#ff7f0e", "log_quadratic": "#2ca02c"}
    labels = {
        "quadratic": "Quadratic (primary)",
        "l1": "L1 norm",
        "log_quadratic": "Log-quadratic",
    }

    for form in FUNCTIONAL_FORMS:
        subset = [
            r
            for r in rows
            if r["N"] == 1_000
            and r["alpha"] == 0.0
            and r["functional_form"] == form
            and r["sigma_query_mult"] == 0.01
        ]
        if not subset:
            continue
        subset_sorted = sorted(subset, key=lambda r: r["sigma"])
        sigmas = [r["sigma"] for r in subset_sorted]
        cohens_ds = [r["cohens_d"] for r in subset_sorted]
        ax.plot(
            sigmas,
            cohens_ds,
            marker="s",
            linewidth=2.0,
            markersize=7,
            color=colors[form],
            label=labels[form],
        )

    ax.axhline(
        1.0,
        color="gray",
        linewidth=1.0,
        linestyle="--",
        label="d = 1.0 (pre-registered minimum at sigma=.3)",
    )
    ax.set_xlabel("Misalignment variance sigma")
    ax.set_ylabel("Cohen's d  (push vs pull distribution distance)")
    ax.set_title(
        "Robustness: Cohen's d vs sigma across functional forms\n"
        "N = 1000, alpha = 0, sigma_query = .01 * sigma"
    )
    ax.legend(loc="lower right")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Falsification evaluation
# ---------------------------------------------------------------------------


def evaluate_falsification(rows: list[dict]) -> list[str]:
    """H_A falsification: ratio >= 2.0 required at every sigma."""
    findings = []
    primary = [
        r
        for r in rows
        if r["N"] == 1_000
        and r["alpha"] == 0.0
        and r["functional_form"] == "quadratic"
        and r["sigma_query_mult"] == 0.01
    ]
    primary_sorted = sorted(primary, key=lambda r: r["sigma"])
    for r in primary_sorted:
        ratio = r["ratio_push_pull"]
        status = "PASS" if ratio >= 2.0 else "FAIL"
        findings.append(f"  sigma={r['sigma']:.1f}: ratio={ratio:.1f} --> {status}")
    return findings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def run() -> None:
    t0 = time.time()
    log.info("friction_tax_montecarlo.py -- Thermodynamic Coupling (Zharnikov 2026am)")
    log.info("=" * 72)
    log.info(f"RANDOM_SEED     = {RANDOM_SEED}")
    log.info(f"N_TRIALS        = {N_TRIALS:,}")
    log.info(f"D               = {D} (SBT specification dimensions)")
    log.info(f"SIGMAS          = {SIGMAS}")
    log.info(f"N_RECIPIENTS    = {N_RECIPIENTS}")
    log.info(f"ALPHAS          = {ALPHAS}")
    log.info(f"FUNCTIONAL_FORMS= {FUNCTIONAL_FORMS}")
    log.info(f"SIGMA_Q_MULTS   = {SIGMA_QUERY_MULTIPLIERS}")
    log.info(
        f"CHUNK_SIZE      = dynamic (see _chunk_size; e.g., {_chunk_size(1000)} for N=1000)"
    )
    n_cells_primary = (
        len(SIGMAS) * len(N_RECIPIENTS) * len(ALPHAS) * len(FUNCTIONAL_FORMS)
    )
    n_cells_total = n_cells_primary * len(SIGMA_QUERY_MULTIPLIERS)
    log.info(f"Primary cells   = {n_cells_primary}")
    log.info(f"Total cells     = {n_cells_total}")
    log.info(f"Total trials    = {n_cells_total * N_TRIALS:,}")
    log.info("")

    rng = np.random.default_rng(RANDOM_SEED)

    all_rows: list[dict] = []
    cell_count = 0

    for sigma in SIGMAS:
        for n in N_RECIPIENTS:
            for alpha in ALPHAS:
                for form in FUNCTIONAL_FORMS:
                    for sq_mult in SIGMA_QUERY_MULTIPLIERS:
                        cell_count += 1
                        result = simulate_cell(
                            sigma=sigma,
                            n=n,
                            alpha=alpha,
                            form=form,
                            sigma_query_mult=sq_mult,
                            rng=rng,
                        )
                        all_rows.append(result)

                        if cell_count % 100 == 0:
                            elapsed = time.time() - t0
                            log.info(
                                f"  Completed {cell_count}/{n_cells_total} cells "
                                f"({elapsed:.1f}s elapsed)"
                            )
        elapsed = time.time() - t0
        log.info(f"Finished sigma={sigma:.1f}  ({elapsed:.1f}s)")

    log.info(f"\nAll {len(all_rows)} cells completed.")

    # ---------------------------------------------------------------------------
    # Write summary CSV
    # ---------------------------------------------------------------------------
    fieldnames = [
        "sigma",
        "N",
        "alpha",
        "functional_form",
        "sigma_query_mult",
        "mu_push_mean",
        "mu_push_sd",
        "mu_push_p25",
        "mu_push_p975",
        "mu_pull_mean",
        "mu_pull_sd",
        "mu_pull_p25",
        "mu_pull_p975",
        "mu_alpha_mean",
        "cohens_d",
        "ratio_push_pull",
        "n_trials",
    ]
    with CSV_PATH.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for r in all_rows:
            writer.writerow({k: r[k] for k in fieldnames})
    log.info(f"Wrote: {CSV_PATH}")

    # ---------------------------------------------------------------------------
    # Baseline result summary
    # ---------------------------------------------------------------------------
    log.info(
        "\n--- Pre-registered baseline check (sigma=.3, N=1000, alpha=0, quadratic) ---"
    )
    baseline_candidates = [
        r
        for r in all_rows
        if r["sigma"] == 0.3
        and r["N"] == 1_000
        and r["alpha"] == 0.0
        and r["functional_form"] == "quadratic"
        and r["sigma_query_mult"] == 0.01
    ]
    if baseline_candidates:
        b = baseline_candidates[0]
        log.info(f"  mu_push          = {b['mu_push_mean']:.6f}")
        log.info(f"  mu_pull          = {b['mu_pull_mean']:.10f}")
        log.info(f"  Cohen's d        = {b['cohens_d']:.2f}  (pre-reg >= 1.0)")
        log.info(f"  ratio push/pull  = {b['ratio_push_pull']:.1f}  (pre-reg >= 200)")
        log.info(f"  analytic mu_push = {2 * .3**2 * 8:.4f}  (= 2*sigma^2*d)")

    # ---------------------------------------------------------------------------
    # Falsification
    # ---------------------------------------------------------------------------
    log.info("\n--- H_A Falsification check (ratio >= 2.0 required at every sigma) ---")
    findings = evaluate_falsification(all_rows)
    for f in findings:
        log.info(f)

    # ---------------------------------------------------------------------------
    # Phase-shift curves (recompute on fresh rng state)
    # ---------------------------------------------------------------------------
    log.info("\n--- Phase-shift curves ---")
    phase_sigmas = (0.1, 0.3, 0.7, 1.0)
    phase_data: dict[float, tuple[np.ndarray, np.ndarray, float]] = {}
    for sigma in phase_sigmas:
        alpha_grid, F_norm, alpha_star = compute_phase_shift_curve(
            sigma=sigma,
            n=1_000,
            form="quadratic",
            rng=rng,
        )
        phase_data[sigma] = (alpha_grid, F_norm, alpha_star)
        log.info(
            f"  sigma={sigma:.1f}: alpha* = {alpha_star:.2f}  "
            f"(pre-reg range [.85, .95])"
        )

    # ---------------------------------------------------------------------------
    # Dimensionality robustness
    # ---------------------------------------------------------------------------
    log.info("\n--- Dimensionality robustness check ---")
    dim_ratios = simulate_dimensionality_check(
        sigma=0.3,
        n=1_000,
        d_values=(2, 4, 8, 16),
        rng=rng,
    )
    for d_val, ratio_val in dim_ratios.items():
        log.info(f"  d={d_val:2d}: push/pull ratio = {ratio_val:.1f}")

    # ---------------------------------------------------------------------------
    # Baseline density plot (recompute to get arrays)
    # ---------------------------------------------------------------------------
    log.info("\n--- Generating plots ---")
    F_push_base, F_pull_base, base_info = simulate_cell_with_arrays(
        sigma=0.3,
        n=1_000,
        form="quadratic",
        sigma_query_mult=0.01,
        rng=rng,
    )
    p1_path = PLOT_DIR / "friction_distribution_push_vs_pull.png"
    plot_friction_distribution(F_push_base, F_pull_base, base_info, p1_path)
    log.info(f"  Wrote: {p1_path}")

    p2_path = PLOT_DIR / "phase_shift_alpha.png"
    plot_phase_shift(phase_data, p2_path)
    log.info(f"  Wrote: {p2_path}")

    p3_path = PLOT_DIR / "sensitivity_misalignment.png"
    plot_sensitivity_misalignment(all_rows, p3_path)
    log.info(f"  Wrote: {p3_path}")

    p4_path = PLOT_DIR / "functional_form_comparison.png"
    plot_functional_form_comparison(all_rows, p4_path)
    log.info(f"  Wrote: {p4_path}")

    # ---------------------------------------------------------------------------
    # Final summary
    # ---------------------------------------------------------------------------
    elapsed = time.time() - t0
    log.info(f"\nTotal runtime: {elapsed:.1f}s ({elapsed/60:.1f} min)")
    log.info(f"Log written to: {LOG_PATH}")
    log.info("OK -- friction_tax_montecarlo.py completed.")


if __name__ == "__main__":
    run()
