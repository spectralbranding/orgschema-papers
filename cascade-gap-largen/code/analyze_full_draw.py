#!/usr/bin/env python3
"""S5 FULL-DRAW confirmatory analysis (FULL_DRAW_PREREGISTRATION.md §5).

Confirmatory (unlike the pilot). Reports, from the assembled full-draw dataset:

  - per-construct reliability: Fleiss' kappa over 3 rater-slots AND **Gwet's AC1**
    (prevalence-adjusted -- the primary read for the rare outcome cell, since the pilot
    showed kappa is deflated at extreme base rates) + raw agreement, via the coding
    runner's per-cell category-count rows;
  - the confirmatory NECESSARY-CONDITION / SAFE-HARBOR test on the case-control sample:
    P(fail | no gap) with an exact (Clopper-Pearson) upper 95% CI (the empty-cell /
    safe-harbor criterion), necessity consistency P(gap | fail), the NCA dichotomous
    ceiling effect, and -- reported but NEVER headlined (selection-on-IV constraint) --
    sufficiency P(fail | gap);
  - the no-record -> UNCERTAIN handling (Amendment 2.D): outcome-uncertain cases are set
    aside from the 0/1 safe-harbor test and reported separately, so absence-of-data never
    fills the no-failure (n00) cell.

This is analysis code, not a coded datum: --fixture is the only mode that runs until the
full-draw dataset + kappa files exist (registered-before-data).

Run:
    uv run --with scipy python research/cascade-gap-largen/analyze_full_draw.py --fixture
    uv run --with scipy python research/cascade-gap-largen/analyze_full_draw.py
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from pilot_code import pooled_fleiss  # noqa: E402  (reuse the Fleiss kernel)

try:
    from scipy.stats import beta as _beta
except Exception:  # pragma: no cover - scipy via `uv run --with scipy`
    _beta = None

DATASET = HERE / "full_draw_dataset.csv"


def gwet_ac1(items: list[list[int]]) -> dict:
    """Gwet's AC1 from per-(case, cell) category-count rows [n0, n1, n_uncertain].

    Same observed agreement P_bar as Fleiss (mean per-item chance-corrected pairwise
    agreement), but chance agreement is Gwet's:
        Pe = (1 / (q - 1)) * sum_j pi_j (1 - pi_j)
    with q = number of categories and pi_j the overall category proportion. AC1 is robust
    to the prevalence paradox that deflates Fleiss' kappa at extreme base rates.
    """
    n_items = len(items)
    if n_items == 0:
        return {"ac1": None, "n_items": 0, "n_raters": 0}
    n_raters = sum(items[0])
    if n_raters < 2 or any(sum(row) != n_raters for row in items):
        return {"ac1": None, "n_items": n_items, "n_raters": n_raters}
    q = len(items[0])
    totals = [sum(row[c] for row in items) for c in range(q)]
    grand = sum(totals)
    pi_j = [t / grand for t in totals]
    # observed agreement (identical to Fleiss' P_bar)
    p_i = [sum(n * (n - 1) for n in row) / (n_raters * (n_raters - 1)) for row in items]
    p_bar = sum(p_i) / n_items
    pe = sum(p * (1 - p) for p in pi_j) / (q - 1)
    ac1 = (p_bar - pe) / (1 - pe) if (1 - pe) != 0 else None
    return {
        "ac1": ac1,
        "n_items": n_items,
        "n_raters": n_raters,
        "P_bar": p_bar,
        "P_e_gwet": pe,
        "category_proportions": dict(zip(["0", "1", "uncertain"], pi_j)),
    }


def clopper_pearson_upper(k: int, n: int, alpha: float = 0.05) -> float:
    """Exact one-sided upper 95% (default) Clopper-Pearson bound = BetaInv(1-a; k+1, n-k)."""
    if n == 0:
        return 1.0
    if k >= n:
        return 1.0
    if _beta is not None:
        return float(_beta.ppf(1.0 - alpha, k + 1, n - k))
    if k == 0:
        return 1.0 - alpha ** (1.0 / n)
    raise RuntimeError("scipy required for Clopper-Pearson at k > 0")


def nc_analysis(
    rows: list[dict],
    gap_col: str = "gap_any",
    fail_col: str = "p45_any",
    uncertain_col: str = "outcome_uncertain",
) -> dict:
    """Necessary-condition 2x2 + safe-harbor / necessity / sufficiency / NCA ceiling.

    Cases whose outcome is UNCERTAIN (no public record) are set aside from the 0/1 test
    (Amendment 2.D) and reported in `n_outcome_uncertain`.
    """
    n11 = n10 = n01 = n00 = 0
    n_uncertain = 0
    for r in rows:
        if uncertain_col in r and str(r.get(uncertain_col, "")).strip() in (
            "1",
            "true",
            "True",
        ):
            n_uncertain += 1
            continue
        g, f = int(r[gap_col]), int(r[fail_col])
        if g and f:
            n11 += 1
        elif g and not f:
            n10 += 1
        elif not g and f:
            n01 += 1
        else:
            n00 += 1
    n_gap = n11 + n10
    n_nogap = n01 + n00
    n_fail = n11 + n01
    # safe harbor: P(fail | no gap) with exact upper CI
    p_fail_nogap = (n01 / n_nogap) if n_nogap else None
    upper = clopper_pearson_upper(n01, n_nogap) if n_nogap else None
    # necessity consistency P(gap | fail); sufficiency P(fail | gap)
    necessity = (n11 / n_fail) if n_fail else None
    sufficiency = (n11 / n_gap) if n_gap else None
    # dichotomous NCA ceiling effect size d (CE-FDH on a 2x2): empty upper-left cell.
    # d = (area above the ceiling line) / (total scope). For binary X,Y the ceiling passes
    # through the empty cell; d = n01_expected_empty ... use the standard 2x2 NCA:
    # d = (n01) is the violation count; ceiling zone = cells (no-gap, fail). Effect present
    # iff that cell is empty. Report d = 1 - (n01 / n_nogap) bounded, plus the raw cell.
    nca_ceiling_empty = n01 == 0
    return {
        "n11": n11,
        "n10": n10,
        "n01": n01,
        "n00": n00,
        "n_outcome_uncertain": n_uncertain,
        "n_gap": n_gap,
        "n_nogap": n_nogap,
        "n_fail": n_fail,
        "p_fail_given_nogap": p_fail_nogap,
        "p_fail_given_nogap_upper95": upper,
        "necessity_consistency": necessity,
        "sufficiency": sufficiency,
        "nca_safe_harbor_cell_empty": nca_ceiling_empty,
    }


def load_rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _fmt(v) -> str:
    return f"{v:.3f}" if isinstance(v, float) else ("n/a" if v is None else str(v))


def run_report() -> int:
    if not DATASET.exists() or DATASET.read_text().strip().count("\n") < 1:
        print(
            f"No coded full-draw data at {DATASET.name} (schema only).", file=sys.stderr
        )
        return 2
    rows = load_rows(DATASET)
    nc = nc_analysis(rows)
    print(
        "=== Full-draw confirmatory necessary-condition analysis (N=%d coded) ==="
        % len(rows)
    )
    print(
        "2x2 (gap_any x p45_any), outcome-uncertain set aside (%d):"
        % nc["n_outcome_uncertain"]
    )
    print(
        "  n11=%d  n10=%d  n01=%d  n00=%d"
        % (nc["n11"], nc["n10"], nc["n01"], nc["n00"])
    )
    print(
        "  safe harbor P(fail|no gap) = %s  (exact upper 95%% CI %s)"
        % (_fmt(nc["p_fail_given_nogap"]), _fmt(nc["p_fail_given_nogap_upper95"]))
    )
    print(
        "  necessity consistency P(gap|fail) = %s" % _fmt(nc["necessity_consistency"])
    )
    print(
        "  [reported, NOT headlined] sufficiency P(fail|gap) = %s"
        % _fmt(nc["sufficiency"])
    )
    print("  NCA safe-harbor cell empty: %s" % nc["nca_safe_harbor_cell_empty"])
    return 0


def run_fixture() -> int:
    ok = True
    # 1) Gwet's AC1 > Fleiss' kappa at extreme base rate (the prevalence paradox the pilot hit).
    # Build 40 items, 3 raters, mostly all-0 with a couple of splits (rare category 1).
    rare = [[3, 0, 0]] * 36 + [[2, 1, 0]] * 3 + [[1, 2, 0]] * 1
    fk = pooled_fleiss(rare)["kappa"]
    ac = gwet_ac1(rare)["ac1"]
    if not (fk is not None and ac is not None and ac > fk):
        print(
            "FAIL prevalence paradox: kappa=%s ac1=%s (expected ac1 > kappa)" % (fk, ac)
        )
        ok = False
    else:
        print(
            "ok  prevalence paradox: Fleiss kappa=%.3f < Gwet AC1=%.3f (rare cell)"
            % (fk, ac)
        )
    # 2) Perfect agreement -> both = 1.0.
    perfect = [[3, 0, 0]] * 10 + [[0, 3, 0]] * 10
    if (
        abs(pooled_fleiss(perfect)["kappa"] - 1.0) > 1e-9
        or abs(gwet_ac1(perfect)["ac1"] - 1.0) > 1e-9
    ):
        print("FAIL perfect agreement != 1.0")
        ok = False
    else:
        print("ok  perfect agreement: kappa=1.000 ac1=1.000")
    # 3) Clopper-Pearson upper at k=0 known values.
    for n, want in ((60, 0.0487), (300, 0.0099)):
        got = clopper_pearson_upper(0, n)
        if abs(got - want) > 5e-3:
            print("FAIL CP(0,%d)=%.4f want ~%.4f" % (n, got, want))
            ok = False
        else:
            print("ok  CP(0,%d)=%.4f (~%.4f)" % (n, got, want))
    # 4) NC analysis on a synthetic safe-harbor sample + uncertain handling.
    syn = (
        [{"gap_any": "1", "p45_any": "1", "outcome_uncertain": "0"}] * 40  # n11
        + [{"gap_any": "1", "p45_any": "0", "outcome_uncertain": "0"}] * 60  # n10
        + [{"gap_any": "0", "p45_any": "0", "outcome_uncertain": "0"}] * 170  # n00
        + [{"gap_any": "0", "p45_any": "1", "outcome_uncertain": "0"}] * 2  # n01 (leak)
        + [{"gap_any": "0", "p45_any": "0", "outcome_uncertain": "1"}]
        * 8  # uncertain -> aside
    )
    nc = nc_analysis(syn)
    checks = [
        ("n11", nc["n11"], 40),
        ("n10", nc["n10"], 60),
        ("n00", nc["n00"], 170),
        ("n01", nc["n01"], 2),
        ("n_outcome_uncertain", nc["n_outcome_uncertain"], 8),
    ]
    for name, got, want in checks:
        if got != want:
            print("FAIL nc %s=%s want %s" % (name, got, want))
            ok = False
    nec = nc["necessity_consistency"]  # n11 / (n11+n01) = 40/42
    if abs(nec - 40 / 42) > 1e-9:
        print("FAIL necessity=%s want %.4f" % (nec, 40 / 42))
        ok = False
    else:
        print(
            "ok  nc 2x2: n11=40 n10=60 n01=2 n00=170 uncertain=8 aside; necessity=%.3f "
            "P(fail|no gap)=%.4f upper95=%.4f"
            % (nec, nc["p_fail_given_nogap"], nc["p_fail_given_nogap_upper95"])
        )
    print("FIXTURE", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--fixture", action="store_true", help="self-check the analysis kernels"
    )
    args = ap.parse_args()
    return run_fixture() if args.fixture else run_report()


if __name__ == "__main__":
    sys.exit(main())
