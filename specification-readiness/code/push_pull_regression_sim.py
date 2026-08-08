"""push_pull_regression_sim.py -- Regression identification simulation for
propositions P1-P5.

Companion computation script for:

    Zharnikov, D. (2026). Toward a Thermodynamic Theory of Organizational
    Coupling: Push, Pull, and the Multi-Interface Architecture of the Firm
    Under AI Mediation. Working paper key: 2026am.

Implements the regression simulation specified in METHODS_APPENDIX.md
Section B (pre-registered before execution). Anti-HARKing discipline:
hypotheses, effect sizes, DGP parameters, and decision rules are fixed in
METHODS_APPENDIX.md and in PRE_EXPERIMENT_NOTES.md.

For each proposition P1-P5 this script:
    1. Generates synthetic panel data under H0 (no effect) and H1 (pre-registered effect).
    2. Runs 1,000 simulated datasets per condition.
    3. Computes Type I error (false-positive rate under H0) and power (true-positive
       rate under H1) at alpha = .05 two-sided.
    4. Runs primary and alternative specifications (METHODS_APPENDIX B.6).
    5. Writes results to regression_simulation_summary.csv and plots.

Panel structure (METHODS_APPENDIX B.3):
    P1, P2, P4, P5: N_firms = 1,000 x T = 10 years = 10,000 firm-year obs.
    P3 (event study):  N_events = 200 x window = 5 years = 1,000 event-year obs.

Fixed seed: np.random.seed(20260525)

Outputs (under code/plots/ and code/):
    plots/power_curve_P1.png ... plots/power_curve_P5.png
    plots/null_distribution_qq.png
    plots/effect_size_sensitivity.png
    regression_simulation_summary.csv
    logs/regression_simulation_run_<YYYYMMDD>.log

Run command (from the paper directory):
    uv run --with numpy==2.2.2 --with scipy==1.14.0 --with statsmodels==0.14.4 \\
           --with matplotlib==3.10.0 --with pandas==2.2.3 \\
           python code/push_pull_regression_sim.py

Expected runtime: 15-20 minutes on a 2024 Apple Silicon Mac.

Pre-registered effect sizes (METHODS_APPENDIX B.4):
    P1: beta = -.08, Cohen's d = 0.5
    P2: beta = -.12, Cohen's d = 0.3
    P3: CAR = -.15 (high-push), Cohen's d = 0.7
    P4: beta = +.10, Cohen's d = 0.4
    P5: beta = +.15, Cohen's d = 0.5

Decision rules (METHODS_APPENDIX B.6):
    Power threshold: < .80 at assumed effect size -> declared underpowered.
    Type I error threshold: > .05 under H0 -> declared mis-specified.
    Effect-size plausibility: point estimate outside [.5x, 2.0x] expected -> flagged.

Scope note: synthetic-data simulation is a numerical-coherence check for
identification. It does not constitute empirical confirmation in real firms.
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

# statsmodels kept for optional use; core OLS uses numpy linalg for speed
try:
    import statsmodels.api as sm  # noqa: F401
except ImportError:
    sm = None  # type: ignore[assignment]

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
CSV_PATH = CODE_DIR / "regression_simulation_summary.csv"
LOG_PATH = LOG_DIR / f"regression_simulation_run_{datetime.date.today():%Y%m%d}.log"

PLOT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Logger
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
# Simulation parameters
# ---------------------------------------------------------------------------
N_SIM: int = 1_000  # simulated datasets per (proposition, condition, spec)
N_SIM_POWER: int = (
    500  # simulated datasets for power-curve sweep (fewer needed for curve shape)
)
N_FIRMS: int = 1_000
T_YEARS: int = 10
N_EVENTS: int = 200  # for P3 event study
EVENT_WINDOW: int = 5  # years per event
ALPHA_TEST: float = 0.05  # two-sided significance level (t-critical ~ 1.96)

# Pre-registered effect sizes (METHODS_APPENDIX B.4)
PRE_REG = {
    "P1": {"beta": -0.08, "cohens_d": 0.5, "r2": 0.15, "direction": -1},
    "P2": {"beta": -0.12, "cohens_d": 0.3, "r2": 0.10, "direction": -1},
    "P3": {"beta": -0.15, "cohens_d": 0.7, "r2": 0.20, "direction": -1},
    "P4": {"beta": +0.10, "cohens_d": 0.4, "r2": 0.12, "direction": +1},
    "P5": {"beta": +0.15, "cohens_d": 0.5, "r2": 0.18, "direction": +1},
}

# Effect-size sweep for power curves (from .25d to 2.0d in .25 increments)
D_MULTIPLES = np.arange(0.25, 2.01, 0.25)  # [.25, .50, .75, ..., 2.00]

# ---------------------------------------------------------------------------
# Data-generating processes (METHODS_APPENDIX B.3)
# ---------------------------------------------------------------------------


def dgp_panel(
    prop: str,
    beta_true: float,
    rng: np.random.Generator,
    n_firms: int = N_FIRMS,
    t_years: int = T_YEARS,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Generate synthetic panel data for P1, P2, P4, P5.

    Returns (X, Y, industry_fe, year_fe) as 1D arrays of length n_firms * t_years.
    X is the main independent variable; Y is the dependent variable.
    industry_fe and year_fe are integer indicators for fixed effects.
    """
    n_obs = n_firms * t_years
    config = PRE_REG[prop]
    r2 = config["r2"]

    # Firm and year indices
    firm_ids = np.repeat(np.arange(n_firms), t_years)
    year_ids = np.tile(np.arange(t_years), n_firms)

    # X calibrated to reasonable distributions per METHODS_APPENDIX B.3
    if prop in ("P1", "P5"):
        # SCI: uniform [0, 1]
        X = rng.uniform(0.0, 1.0, size=n_obs)
    elif prop == "P2":
        # Delta log functional headcount fraction: normal(0, .10)
        X = rng.normal(0.0, 0.10, size=n_obs)
    elif prop == "P4":
        # Contradiction index: beta(2, 5) mapped to [0, 1]
        X = rng.beta(2.0, 5.0, size=n_obs)
    else:
        X = rng.uniform(0.0, 1.0, size=n_obs)

    # Industry FE (20 industries, Fama-French style)
    n_industries = 20
    firm_industry = rng.integers(0, n_industries, size=n_firms)
    industry_ids = firm_industry[firm_ids]

    # Controls: 3 independent N(0,1) variables
    controls = rng.normal(0.0, 1.0, size=(n_obs, 3))
    gamma = rng.normal(0.0, 0.05, size=3)

    # Firm and year random effects (partial analog to FE in DGP)
    firm_re = rng.normal(0.0, 0.05, size=n_firms)
    year_re = rng.normal(0.0, 0.03, size=t_years)

    # Compute Y variance needed to achieve target R2
    # Y = beta*X + gamma*controls + firm_re + year_re + eps
    systematic = (
        beta_true * X + controls @ gamma + firm_re[firm_ids] + year_re[year_ids]
    )
    var_systematic = np.var(systematic)
    if r2 > 0 and var_systematic > 0:
        var_eps = var_systematic * (1.0 - r2) / r2
    else:
        var_eps = 1.0
    eps = rng.normal(0.0, np.sqrt(var_eps), size=n_obs)
    Y = systematic + eps

    return X, Y, industry_ids, year_ids


def dgp_event_study(
    beta_true: float,
    rng: np.random.Generator,
    n_events: int = N_EVENTS,
    window: int = EVENT_WINDOW,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Generate synthetic event-study data for P3.

    Returns (push_intensity, CAR, industry_ids).
    push_intensity is the pre-event XAD/SALE quintile rank (1-5).
    CAR is the cumulative abnormal return over the event window.
    """
    n_obs = n_events * window
    config = PRE_REG["P3"]
    r2 = config["r2"]

    # Event and year indices
    event_ids = np.repeat(np.arange(n_events), window)
    year_ids = np.tile(np.arange(window), n_events)

    # Push intensity: quintile rank 1-5 per Fama-French industry * year
    push_quintile = rng.integers(1, 6, size=n_events)  # 1=low push, 5=high push
    X = push_quintile[event_ids].astype(float) / 5.0  # normalize to [.2, 1.0]

    # Industry FE
    n_industries = 20
    event_industry = rng.integers(0, n_industries, size=n_events)
    industry_ids = event_industry[event_ids]

    # Controls
    controls = rng.normal(0.0, 1.0, size=(n_obs, 3))
    gamma = rng.normal(0.0, 0.05, size=3)

    # Event RE
    event_re = rng.normal(0.0, 0.05, size=n_events)

    systematic = beta_true * X + controls @ gamma + event_re[event_ids]
    var_systematic = np.var(systematic)
    if r2 > 0 and var_systematic > 0:
        var_eps = var_systematic * (1.0 - r2) / r2
    else:
        var_eps = 1.0
    eps = rng.normal(0.0, np.sqrt(var_eps), size=n_obs)
    Y = systematic + eps

    return X, Y, industry_ids


# ---------------------------------------------------------------------------
# OLS regression runner
# ---------------------------------------------------------------------------


def _fast_ols_tstat(
    X_matrix: np.ndarray,
    Y: np.ndarray,
) -> tuple[float, float, float]:
    """Fast OLS t-stat for the first regressor (index 1 after constant).

    Uses numpy linalg for speed. Returns (t_stat, p_value, beta_hat).
    Assumes X_matrix[:, 0] is the constant and X_matrix[:, 1] is the variable
    of interest.
    """
    n, k = X_matrix.shape
    try:
        # Normal equations via lstsq
        beta, _, rank, _ = np.linalg.lstsq(X_matrix, Y, rcond=None)
        residuals = Y - X_matrix @ beta
        sigma2 = float(np.dot(residuals, residuals) / (n - rank))
        XtX_inv = np.linalg.inv(X_matrix.T @ X_matrix)
        se = np.sqrt(sigma2 * np.diag(XtX_inv))
        beta_hat = float(beta[1])
        se_hat = float(se[1])
        if se_hat < 1e-15:
            return 0.0, 1.0, beta_hat
        t_stat = beta_hat / se_hat
        # Two-sided p-value from t(n - k)
        df = n - rank
        p_value = float(2.0 * stats.t.sf(abs(t_stat), df=df))
        return float(t_stat), p_value, beta_hat
    except Exception:
        return 0.0, 1.0, 0.0


def _build_fe_dummies(
    ids: np.ndarray,
) -> np.ndarray:
    """Build K-1 dummy columns for a categorical id array."""
    n_obs = len(ids)
    n_levels = int(ids.max()) + 1
    dummies = np.zeros((n_obs, n_levels - 1), dtype=np.float64)
    for k in range(1, n_levels):
        dummies[:, k - 1] = (ids == k).astype(float)
    return dummies


def run_ols_panel(
    X: np.ndarray,
    Y: np.ndarray,
    industry_ids: np.ndarray,
    year_ids: np.ndarray,
    include_fe: bool = True,
) -> tuple[float, float, float]:
    """Run OLS with optional industry and year fixed effects (dummy variables).

    Returns (t_stat, p_value, point_estimate) for the main X coefficient.
    Uses fast numpy linalg instead of statsmodels for speed.
    """
    if include_fe:
        year_dummies = _build_fe_dummies(year_ids)
        ind_dummies = _build_fe_dummies(industry_ids)
        X_matrix = np.column_stack(
            [
                np.ones(len(Y)),
                X.reshape(-1, 1),
                year_dummies,
                ind_dummies,
            ]
        )
    else:
        X_matrix = np.column_stack([np.ones(len(Y)), X.reshape(-1, 1)])

    return _fast_ols_tstat(X_matrix, Y)


def run_ols_event(
    X: np.ndarray,
    Y: np.ndarray,
    industry_ids: np.ndarray,
    include_fe: bool = True,
) -> tuple[float, float, float]:
    """Run OLS for event-study design (P3). Returns (t_stat, p_value, beta_hat)."""
    if include_fe:
        ind_dummies = _build_fe_dummies(industry_ids)
        X_matrix = np.column_stack(
            [
                np.ones(len(Y)),
                X.reshape(-1, 1),
                ind_dummies,
            ]
        )
    else:
        X_matrix = np.column_stack([np.ones(len(Y)), X.reshape(-1, 1)])

    return _fast_ols_tstat(X_matrix, Y)


# ---------------------------------------------------------------------------
# Single proposition simulation
# ---------------------------------------------------------------------------


def simulate_proposition(
    prop: str,
    beta_true: float,
    rng: np.random.Generator,
    spec_label: str = "primary",
    include_fe: bool = True,
) -> dict:
    """Run N_SIM datasets under H0 (beta=0) and H1 (beta=beta_true).

    Returns a dict with power, type1_error, mean/sd point estimates.
    """
    is_p3 = prop == "P3"
    expected_direction = PRE_REG[prop]["direction"]
    expected_beta = PRE_REG[prop]["beta"]

    # --- H0 simulation ---
    t_stats_h0 = np.empty(N_SIM)
    p_vals_h0 = np.empty(N_SIM)

    for i in range(N_SIM):
        if is_p3:
            X, Y, ind_ids = dgp_event_study(0.0, rng)
            t, p, _ = run_ols_event(X, Y, ind_ids, include_fe=include_fe)
        else:
            X, Y, ind_ids, yr_ids = dgp_panel(prop, 0.0, rng)
            t, p, _ = run_ols_panel(X, Y, ind_ids, yr_ids, include_fe=include_fe)
        t_stats_h0[i] = t
        p_vals_h0[i] = p

    type1_error = float((p_vals_h0 < ALPHA_TEST).mean())

    # --- H1 simulation ---
    t_stats_h1 = np.empty(N_SIM)
    p_vals_h1 = np.empty(N_SIM)
    betas_h1 = np.empty(N_SIM)

    for i in range(N_SIM):
        if is_p3:
            X, Y, ind_ids = dgp_event_study(beta_true, rng)
            t, p, b = run_ols_event(X, Y, ind_ids, include_fe=include_fe)
        else:
            X, Y, ind_ids, yr_ids = dgp_panel(prop, beta_true, rng)
            t, p, b = run_ols_panel(X, Y, ind_ids, yr_ids, include_fe=include_fe)
        t_stats_h1[i] = t
        p_vals_h1[i] = p
        betas_h1[i] = b

    power = float((p_vals_h1 < ALPHA_TEST).mean())

    # Plausibility check: is mean estimate in [.5, 2.0] * expected_beta?
    mean_beta = float(betas_h1.mean())
    sd_beta = float(betas_h1.std(ddof=1))
    lo = 0.5 * abs(expected_beta)
    hi = 2.0 * abs(expected_beta)
    pct_in_range = float(((np.abs(betas_h1) >= lo) & (np.abs(betas_h1) <= hi)).mean())

    # Direction check: fraction with correct sign under H1
    pct_correct_sign = float((np.sign(betas_h1) == expected_direction).mean())

    return {
        "proposition": prop,
        "beta_true": beta_true,
        "condition": "H0_and_H1",
        "specification": spec_label,
        "type1_error": type1_error,
        "power": power,
        "mean_point_estimate": mean_beta,
        "sd_point_estimate": sd_beta,
        "pct_in_plausible_range": pct_in_range,
        "pct_correct_sign_h1": pct_correct_sign,
        # Store t-stats for QQ plot (not in CSV)
        "_t_stats_h0": t_stats_h0,
        "_t_stats_h1": t_stats_h1,
        "_betas_h1": betas_h1,
    }


def simulate_power_curve(
    prop: str,
    rng: np.random.Generator,
    d_multiples: np.ndarray = D_MULTIPLES,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute power at each effect-size multiple of pre-registered Cohen's d.

    Returns (d_values, powers) arrays.
    """
    base_beta = PRE_REG[prop]["beta"]
    powers = np.empty(len(d_multiples))

    for j, mult in enumerate(d_multiples):
        beta_sweep = base_beta * mult
        is_p3 = prop == "P3"
        p_vals = np.empty(N_SIM_POWER)
        for i in range(N_SIM_POWER):
            if is_p3:
                X, Y, ind_ids = dgp_event_study(beta_sweep, rng)
                _, p, _ = run_ols_event(X, Y, ind_ids, include_fe=True)
            else:
                X, Y, ind_ids, yr_ids = dgp_panel(prop, beta_sweep, rng)
                _, p, _ = run_ols_panel(X, Y, ind_ids, yr_ids, include_fe=True)
            p_vals[i] = p
        powers[j] = float((p_vals < ALPHA_TEST).mean())

    return d_multiples * PRE_REG[prop]["cohens_d"], powers


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

PROP_COLORS = {
    "P1": "#1f77b4",
    "P2": "#ff7f0e",
    "P3": "#2ca02c",
    "P4": "#d62728",
    "P5": "#9467bd",
}


def plot_power_curve(
    prop: str,
    d_vals: np.ndarray,
    powers: np.ndarray,
    power_primary: float,
    out_path: Path,
) -> None:
    """Power curve for one proposition."""
    fig, ax = plt.subplots(figsize=(7.5, 5.0))
    ax.plot(
        d_vals,
        powers,
        color=PROP_COLORS[prop],
        linewidth=2.0,
        marker="o",
        markersize=5,
        label=f"{prop} power curve",
    )
    ax.axhline(
        0.80, color="gray", linewidth=1.0, linestyle="--", label="Power = .80 threshold"
    )
    pre_d = PRE_REG[prop]["cohens_d"]
    ax.axvline(
        pre_d,
        color="black",
        linewidth=1.0,
        linestyle=":",
        label=f"Pre-reg Cohen's d = {pre_d:.2f}",
    )
    ax.scatter(
        [pre_d],
        [power_primary],
        color="black",
        zorder=5,
        s=60,
        label=f"Power at pre-reg d = {power_primary:.2f}",
    )
    ax.set_xlabel("Effect size (Cohen's d)")
    ax.set_ylabel("Statistical power (two-sided alpha = .05)")
    ax.set_title(
        f"Power curve -- {prop}\n"
        f"N_sim = {N_SIM_POWER} (curve), {N_FIRMS} firms x {T_YEARS} years"
        if prop != "P3"
        else f"Power curve -- {prop}\n"
        f"N_sim = {N_SIM_POWER} (curve), {N_EVENTS} events x {EVENT_WINDOW} years"
    )
    ax.set_ylim(0.0, 1.05)
    ax.set_xlim(0.0, d_vals.max() * 1.05)
    ax.legend(loc="lower right")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_null_qq(
    prop_results: dict[str, dict],
    out_path: Path,
) -> None:
    """QQ plot of t-statistics under H0 vs N(0,1) for all propositions."""
    n_props = len(prop_results)
    ncols = 3
    nrows = (n_props + ncols - 1) // ncols
    fig, axes = plt.subplots(
        nrows, ncols, figsize=(5.0 * ncols, 4.5 * nrows), squeeze=False
    )

    for idx, (prop, res) in enumerate(prop_results.items()):
        row, col = divmod(idx, ncols)
        ax = axes[row][col]
        t_h0 = res["_t_stats_h0"]
        # QQ plot manually
        n = len(t_h0)
        quantiles_emp = np.sort(t_h0)
        quantiles_theo = stats.norm.ppf(np.linspace(0.001, 0.999, n))
        ax.scatter(
            quantiles_theo, quantiles_emp, s=2, alpha=0.4, color=PROP_COLORS[prop]
        )
        ax.plot(
            quantiles_theo,
            quantiles_theo,
            color="gray",
            linewidth=1.0,
            linestyle="--",
            label="y = x (ideal)",
        )
        ax.set_xlabel("Theoretical N(0,1) quantiles")
        ax.set_ylabel("Empirical t-stat quantiles")
        ax.set_title(f"{prop}: QQ under H0\nType I error = {res['type1_error']:.3f}")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    # Hide unused subplots
    for idx in range(n_props, nrows * ncols):
        row, col = divmod(idx, ncols)
        axes[row][col].set_visible(False)

    fig.suptitle(
        "QQ plots of t-statistics under H0 vs N(0,1)\n"
        "Correct Type I error calibration: points follow diagonal",
        fontsize=12,
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_effect_size_sensitivity(
    prop_results: dict[str, dict],
    out_path: Path,
) -> None:
    """Point estimates and 95% CIs under H1 for each proposition."""
    props = list(prop_results.keys())
    x = np.arange(len(props))
    fig, ax = plt.subplots(figsize=(9.0, 5.5))

    for i, prop in enumerate(props):
        res = prop_results[prop]
        betas = res["_betas_h1"]
        mean_b = float(betas.mean())
        se_b = float(betas.std(ddof=1))
        ci95 = 1.96 * se_b
        expected_b = PRE_REG[prop]["beta"]

        ax.errorbar(
            i,
            mean_b,
            yerr=ci95,
            fmt="o",
            color=PROP_COLORS[prop],
            markersize=8,
            capsize=6,
            linewidth=2.0,
            label=f"{prop} estimate (CI)",
        )
        ax.scatter(
            i,
            expected_b,
            marker="D",
            color=PROP_COLORS[prop],
            s=60,
            zorder=5,
            edgecolors="black",
            label=f"{prop} pre-reg" if i == 0 else None,
        )

    ax.axhline(0.0, color="gray", linewidth=0.8, linestyle=":")
    ax.set_xticks(x)
    ax.set_xticklabels(props)
    ax.set_ylabel("Point estimate (mean over N_sim = 1,000 datasets)")
    ax.set_title(
        "Effect-size sensitivity: estimated vs pre-registered beta\n"
        "Circles = mean +/- 1.96*SD; diamonds = pre-registered expectation"
    )
    ax.grid(True, alpha=0.3, axis="y")
    # Custom legend (avoid duplicates)
    handles, labels = ax.get_legend_handles_labels()
    # Keep distinct
    seen = set()
    filtered = [
        (h, l) for h, l in zip(handles, labels) if l not in seen and not seen.add(l)
    ]
    ax.legend(
        [h for h, l in filtered],
        [l for h, l in filtered],
        loc="lower right",
        fontsize=9,
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Decision rules evaluation
# ---------------------------------------------------------------------------


def evaluate_decision_rules(summary_rows: list[dict]) -> list[str]:
    """Apply pre-registered decision rules (METHODS_APPENDIX B.6).

    Returns list of verdict strings.
    """
    verdicts = []
    for r in summary_rows:
        prop = r["proposition"]
        spec = r["specification"]
        power = r["power"]
        t1e = r["type1_error"]
        pct_range = r["pct_in_plausible_range"]
        pct_sign = r["pct_correct_sign_h1"]

        power_status = "PASS" if power >= 0.80 else "FAIL (underpowered)"
        t1e_status = "PASS" if t1e <= 0.05 else "FAIL (inflated Type I)"
        range_status = "PASS" if pct_range >= 0.80 else "FLAG (effect-size mismatch)"

        verdicts.append(
            f"  {prop} [{spec}]: power={power:.2f} {power_status} | "
            f"Type_I={t1e:.3f} {t1e_status} | "
            f"pct_in_range={pct_range:.2f} {range_status} | "
            f"pct_correct_sign={pct_sign:.2f}"
        )
    return verdicts


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def run() -> None:
    t0 = time.time()
    log.info("push_pull_regression_sim.py -- Thermodynamic Coupling (Zharnikov 2026am)")
    log.info("=" * 72)
    log.info(f"RANDOM_SEED = {RANDOM_SEED}")
    log.info(f"N_SIM       = {N_SIM:,} simulated datasets per condition")
    log.info(f"N_FIRMS     = {N_FIRMS:,}  T = {T_YEARS} years (P1/P2/P4/P5)")
    log.info(f"N_EVENTS    = {N_EVENTS}  window = {EVENT_WINDOW} years (P3)")
    log.info(f"ALPHA_TEST  = {ALPHA_TEST}")
    log.info("")
    log.info("Pre-registered effect sizes:")
    for prop, cfg in PRE_REG.items():
        log.info(
            f"  {prop}: beta={cfg['beta']:+.2f}, d={cfg['cohens_d']}, "
            f"R2={cfg['r2']}"
        )
    log.info("")

    rng = np.random.default_rng(RANDOM_SEED)

    # ---------------------------------------------------------------------------
    # Primary specification: run each P with pre-registered beta
    # ---------------------------------------------------------------------------
    log.info("--- Primary specification ---")
    primary_results: dict[str, dict] = {}
    for prop in ["P1", "P2", "P3", "P4", "P5"]:
        log.info(f"  Running {prop} (primary) ...")
        beta = PRE_REG[prop]["beta"]
        res = simulate_proposition(
            prop, beta, rng, spec_label="primary", include_fe=True
        )
        primary_results[prop] = res
        log.info(
            f"    {prop}: power={res['power']:.2f}, Type_I={res['type1_error']:.3f}, "
            f"mean_beta={res['mean_point_estimate']:.4f}, "
            f"pct_correct_sign={res['pct_correct_sign_h1']:.2f}"
        )
        elapsed = time.time() - t0
        log.info(f"    elapsed: {elapsed:.1f}s")

    # ---------------------------------------------------------------------------
    # Alternative specification: no fixed effects (robustness check per B.6)
    # ---------------------------------------------------------------------------
    log.info("\n--- Alternative specification (no FE) ---")
    alt_results: dict[str, dict] = {}
    for prop in ["P1", "P2", "P3", "P4", "P5"]:
        log.info(f"  Running {prop} (no-FE alt) ...")
        beta = PRE_REG[prop]["beta"]
        res = simulate_proposition(
            prop, beta, rng, spec_label="no_FE", include_fe=False
        )
        alt_results[prop] = res
        log.info(
            f"    {prop}: power={res['power']:.2f}, Type_I={res['type1_error']:.3f}, "
            f"mean_beta={res['mean_point_estimate']:.4f}"
        )
        elapsed = time.time() - t0
        log.info(f"    elapsed: {elapsed:.1f}s")

    # ---------------------------------------------------------------------------
    # Power curves
    # ---------------------------------------------------------------------------
    log.info("\n--- Power curves ---")
    power_curve_data: dict[str, tuple[np.ndarray, np.ndarray]] = {}
    for prop in ["P1", "P2", "P3", "P4", "P5"]:
        log.info(f"  Power curve {prop} ...")
        d_vals, powers = simulate_power_curve(prop, rng)
        power_curve_data[prop] = (d_vals, powers)
        log.info(f"    {prop}: power at pre-reg d = {powers[3]:.2f} (index 3 = 1.0x d)")
        elapsed = time.time() - t0
        log.info(f"    elapsed: {elapsed:.1f}s")

    # ---------------------------------------------------------------------------
    # Write summary CSV
    # ---------------------------------------------------------------------------
    summary_rows = []
    for prop, res in primary_results.items():
        summary_rows.append(
            {
                "proposition": prop,
                "condition": "H0_and_H1",
                "specification": "primary",
                "power": res["power"],
                "type1_error": res["type1_error"],
                "mean_point_estimate": res["mean_point_estimate"],
                "sd_point_estimate": res["sd_point_estimate"],
                "pct_in_plausible_range": res["pct_in_plausible_range"],
                "pct_correct_sign_h1": res["pct_correct_sign_h1"],
                "pre_reg_beta": PRE_REG[prop]["beta"],
                "pre_reg_cohens_d": PRE_REG[prop]["cohens_d"],
            }
        )
    for prop, res in alt_results.items():
        summary_rows.append(
            {
                "proposition": prop,
                "condition": "H0_and_H1",
                "specification": "no_FE",
                "power": res["power"],
                "type1_error": res["type1_error"],
                "mean_point_estimate": res["mean_point_estimate"],
                "sd_point_estimate": res["sd_point_estimate"],
                "pct_in_plausible_range": res["pct_in_plausible_range"],
                "pct_correct_sign_h1": res["pct_correct_sign_h1"],
                "pre_reg_beta": PRE_REG[prop]["beta"],
                "pre_reg_cohens_d": PRE_REG[prop]["cohens_d"],
            }
        )

    fieldnames = [
        "proposition",
        "condition",
        "specification",
        "power",
        "type1_error",
        "mean_point_estimate",
        "sd_point_estimate",
        "pct_in_plausible_range",
        "pct_correct_sign_h1",
        "pre_reg_beta",
        "pre_reg_cohens_d",
    ]
    with CSV_PATH.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for r in summary_rows:
            writer.writerow({k: r[k] for k in fieldnames})
    log.info(f"\nWrote: {CSV_PATH}")

    # ---------------------------------------------------------------------------
    # Decision rules
    # ---------------------------------------------------------------------------
    log.info("\n--- Decision-rule verdicts (METHODS_APPENDIX B.6) ---")
    verdicts = evaluate_decision_rules(summary_rows)
    for v in verdicts:
        log.info(v)

    # ---------------------------------------------------------------------------
    # Plots
    # ---------------------------------------------------------------------------
    log.info("\n--- Generating plots ---")

    for prop in ["P1", "P2", "P3", "P4", "P5"]:
        d_vals, powers = power_curve_data[prop]
        # Power at pre-registered d (index 3 = 1.0 * d)
        power_at_prereg = float(powers[3])
        out_p = PLOT_DIR / f"power_curve_{prop}.png"
        plot_power_curve(prop, d_vals, powers, power_at_prereg, out_p)
        log.info(f"  Wrote: {out_p}")

    qq_path = PLOT_DIR / "null_distribution_qq.png"
    plot_null_qq(primary_results, qq_path)
    log.info(f"  Wrote: {qq_path}")

    eff_path = PLOT_DIR / "effect_size_sensitivity.png"
    plot_effect_size_sensitivity(primary_results, eff_path)
    log.info(f"  Wrote: {eff_path}")

    # ---------------------------------------------------------------------------
    # Final summary
    # ---------------------------------------------------------------------------
    elapsed = time.time() - t0
    log.info(f"\nTotal runtime: {elapsed:.1f}s ({elapsed/60:.1f} min)")
    log.info(f"Log written to: {LOG_PATH}")
    log.info("OK -- push_pull_regression_sim.py completed.")


if __name__ == "__main__":
    run()
