#!/usr/bin/env python3
"""Pre-registered confirmatory analysis for the Tier-Bundle Algebra n=30 study.

Implements the statistical plan locked in PREREGISTRATION_V1.md §4:
  - H6a: Fisher's exact 2x2 on cascade-gap-at-phi4->phi5 x P4-pathway-disruption
  - H6b: Fisher's exact 2x2 on cascade-gap-at-phi5->phi6 x P5-pathway-fracture
  - H6c: Fisher's exact 2x2 on any-cascade-gap x any-P4-or-P5-incidence (omnibus)
Each reported with Cramer's V and a 95% Clopper-Pearson CI on the gap-conditional
failure proportion. Multiple-testing: Bonferroni alpha = 0.025 for the H6a+H6b
family; H6c at alpha = 0.05 (per §4). Secondary stratification on the
`gap_mitigated` moderator (pre-registration Amendment 3).

THIS SCRIPT IS COMMITTED BEFORE ANY REAL CODED DATUM EXISTS (registered-before-
data). It has two runnable modes:
  * --fixture : run on a synthetic table with a known Fisher's-exact value and
                assert the implementation reproduces it (pipeline self-check). This
                is the only mode that runs until the coded dataset is built.
  * --data PATH : run the pre-registered analysis on a coded dataset CSV once the
                dossier-driven coding phase (see PREREGISTRATION_V1.md
                "Coding-phase status") has produced one.

Reproducibility (PAQS items 37a-37e):
  - Deterministic: Fisher's exact and Clopper-Pearson are exact (no RNG). No seed
    is required for the analysis; the only randomness in the whole program is the
    pre-registered case-sampling (seed 20260520), which lives in a separate step.
  - Run command (from repo root):
        uv run --with scipy python code/analyze_study_n30.py --fixture
    and, once coding is complete:
        uv run --with scipy python code/analyze_study_n30.py \\
            --data data/coded_dataset_n30.csv
  - Dependencies: Python 3.12 + scipy (fisher_exact, binomtest, chi2_contingency).
    scipy version is printed in the run header so the exact numeric provenance of
    any reported p-value is recorded.

Expected coded-dataset schema (one row per H6-eligible case):
    case_id, case, gap_45, p4_pathway, gap_56, p5_pathway, gap_any, p45_any,
    gap_mitigated
  where each of gap_45, p4_pathway, gap_56, p5_pathway, gap_any, p45_any is in
  {0, 1} and gap_mitigated is in {yes, no, NA}. Cases excluded from H6 per
  PREREGISTRATION_V1.md §2 (intra-business pivot, sole-proprietor wind-down,
  redomiciliation) must NOT appear in this file.
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path

from scipy import stats  # type: ignore
from scipy import __version__ as scipy_version  # type: ignore

# Fisher's exact two-sided p for the classic 3-1-1-3 tea-tasting table, used as the
# implementation self-check. This is a textbook-stable value (Fisher 1935).
FIXTURE_TABLE = [[3, 1], [1, 3]]
FIXTURE_FISHER_P = 0.4857142857142857


def cramers_v(table: list[list[int]]) -> float:
    """Cramer's V for a 2x2 table (equals phi = sqrt(chi2 / n) for 2x2)."""
    n = sum(sum(row) for row in table)
    if n == 0:
        return float("nan")
    chi2, _, _, _ = stats.chi2_contingency(table, correction=False)
    return math.sqrt(chi2 / n)


def clopper_pearson(successes: int, trials: int) -> tuple[float, float]:
    """Exact 95% Clopper-Pearson CI on a binomial proportion."""
    if trials == 0:
        return (float("nan"), float("nan"))
    ci = stats.binomtest(successes, trials).proportion_ci(
        confidence_level=0.95, method="exact"
    )
    return (ci.low, ci.high)


def analyze_cell(name: str, table: list[list[int]], alpha: float) -> dict:
    """One pre-registered 2x2 cell: Fisher's exact + Cramer's V + Clopper-Pearson."""
    _, p = stats.fisher_exact(table, alternative="two-sided")
    v = cramers_v(table)
    # gap-present row is table[0]; failure=yes column is col 0
    gap_present_fail = table[0][0]
    gap_present_total = table[0][0] + table[0][1]
    ci_low, ci_high = clopper_pearson(gap_present_fail, gap_present_total)
    return {
        "name": name,
        "table": table,
        "fisher_p": p,
        "cramers_v": v,
        "gap_fail_prop": (
            gap_present_fail / gap_present_total if gap_present_total else float("nan")
        ),
        "ci95": (ci_low, ci_high),
        "alpha": alpha,
        "reject": p < alpha,
    }


def print_cell(res: dict) -> None:
    t = res["table"]
    print(f"  {res['name']} (alpha = {res['alpha']}):")
    print(f"                 fail=YES  fail=NO")
    print(f"    gap=YES         {t[0][0]:>3}      {t[0][1]:>3}")
    print(f"    gap=NO          {t[1][0]:>3}      {t[1][1]:>3}")
    print(
        f"    Fisher's exact p = {res['fisher_p']:.4f}   Cramer's V = {res['cramers_v']:.3f}"
    )
    lo, hi = res["ci95"]
    print(
        f"    P(fail | gap) = {res['gap_fail_prop']:.3f}  "
        f"95% Clopper-Pearson CI [{lo:.3f}, {hi:.3f}]"
    )
    print(f"    reject independence at alpha: {res['reject']}")


def build_tables(rows: list[dict]) -> dict[str, list[list[int]]]:
    """Build the three pre-registered 2x2 tables from coded rows."""

    def two_by_two(gap_col: str, fail_col: str) -> list[list[int]]:
        cells = [[0, 0], [0, 0]]
        for r in rows:
            g = int(r[gap_col])
            f = int(r[fail_col])
            cells[0 if g == 1 else 1][0 if f == 1 else 1] += 1
        return cells

    return {
        "H6a phi4->phi5": two_by_two("gap_45", "p4_pathway"),
        "H6b phi5->phi6": two_by_two("gap_56", "p5_pathway"),
        "H6c aggregate": two_by_two("gap_any", "p45_any"),
    }


def run_fixture() -> int:
    print("Pipeline self-check (synthetic fixture; no study data)")
    print("=" * 70)
    print(f"scipy {scipy_version}")
    _, p = stats.fisher_exact(FIXTURE_TABLE, alternative="two-sided")
    v = cramers_v(FIXTURE_TABLE)
    lo, hi = clopper_pearson(3, 4)
    print(f"Fixture table {FIXTURE_TABLE}: Fisher's exact p = {p:.10f}")
    print(f"  expected {FIXTURE_FISHER_P:.10f}")
    print(f"Cramer's V = {v:.4f}; Clopper-Pearson CI on 3/4 = [{lo:.4f}, {hi:.4f}]")
    ok = abs(p - FIXTURE_FISHER_P) < 1e-9
    # Necessary-condition helper self-check on the study's own 2x2 shape
    # ([[gap&fail, gap&nofail],[nogap&fail, nogap&nofail]] = 2,1,0,23): the
    # empty no-gap/failure cell => P(fail|no gap)=0, necessity consistency=1.0,
    # sufficiency=2/3, dichotomous NCA ceiling d=.25.
    nc_rows = (
        [{"gap_any": "1", "p45_any": "1"}] * 2
        + [{"gap_any": "1", "p45_any": "0"}] * 1
        + [{"gap_any": "0", "p45_any": "0"}] * 23
    )
    nc = necessary_condition_stats(nc_rows, "gap_any", "p45_any")
    nc_ok = (
        nc["safe_harbor_fail_rate"] == 0.0
        and abs(nc["necessity_consistency"] - 1.0) < 1e-12
        and abs(nc["sufficiency"] - 2 / 3) < 1e-12
        and nc["nca_ceiling_d"] == 0.25
    )
    print(
        f"Necessary-condition helper on [2,1,0,23]: "
        f"P(fail|no gap)={nc['safe_harbor_fail_rate']:.3f}, "
        f"consistency={nc['necessity_consistency']:.3f}, "
        f"sufficiency={nc['sufficiency']:.3f}, d={nc['nca_ceiling_d']:.2f}"
    )
    print()
    if ok and nc_ok:
        print("SELF-CHECK OK: statistical implementation reproduces the known value.")
        return 0
    print("SELF-CHECK FAILED: Fisher's exact or necessary-condition helper drifted.")
    return 1


def run_data(path: Path) -> int:
    if not path.exists():
        print(f"No coded dataset at {path}.", file=sys.stderr)
        print(
            "The dossier-driven coding phase has not produced a dataset yet; "
            "see PREREGISTRATION_V1.md 'Coding-phase status'. Run --fixture to "
            "validate the pipeline.",
            file=sys.stderr,
        )
        return 2
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    print("Tier-Bundle Algebra n=30 confirmatory analysis (Proposition 6)")
    print("=" * 70)
    print(f"scipy {scipy_version}")
    print(f"H6-eligible cases coded: {len(rows)}")
    print()
    tables = build_tables(rows)
    results = {
        "H6a phi4->phi5": analyze_cell(
            "H6a phi4->phi5", tables["H6a phi4->phi5"], 0.025
        ),
        "H6b phi5->phi6": analyze_cell(
            "H6b phi5->phi6", tables["H6b phi5->phi6"], 0.025
        ),
        "H6c aggregate": analyze_cell("H6c aggregate", tables["H6c aggregate"], 0.05),
    }
    for res in results.values():
        print_cell(res)
        print()
    # Pre-registered confirmation threshold (PREREGISTRATION_V1.md §4).
    supported = any(
        results[h]["reject"] and results[h]["cramers_v"] >= 0.30
        for h in ("H6a phi4->phi5", "H6b phi5->phi6")
    )
    falsified = all(res["fisher_p"] >= 0.10 for res in results.values())
    print("Pre-registered verdict:")
    print(f"  P6 SUPPORTED (>=1 of H6a/H6b at alpha=.025 with V>=.30): {supported}")
    print(f"  P6 FALSIFIED at n=30 (all three p >= .10):              {falsified}")
    print()
    run_secondary_stratification(rows)
    print()
    run_necessary_condition_analysis(rows)
    return 0


def run_secondary_stratification(rows: list[dict]) -> None:
    """Amendment-3 secondary stratification (PREREGISTRATION_V1.md Amendment 3).

    A cascade gap that was contractually absorbed at closing (gap_mitigated == 'yes')
    is expected NOT to produce a failure; pooling managed and unmanaged gaps biases
    the P6 test toward the null. This SECONDARY, pre-specified stratification recodes
    a managed gap as non-gap (unmanaged-gap-only view) and re-runs H6a and H6c. It is
    a robustness lens on the primary result, NOT a new primary hypothesis; the
    headline result remains the full-sample binary Fisher's exact above.
    """
    print("Secondary stratification (Amendment 3): unmanaged-gap subset")
    print("-" * 70)
    n_managed = sum(1 for r in rows if r.get("gap_mitigated") == "yes")
    print(
        f"  Managed-gap cases recoded to non-gap for this view: {n_managed} "
        f"(gap_mitigated == 'yes')"
    )

    def two_by_two_unmanaged(gap_col: str, fail_col: str) -> list[list[int]]:
        cells = [[0, 0], [0, 0]]
        for r in rows:
            managed = r.get("gap_mitigated") == "yes"
            g = 1 if (int(r[gap_col]) == 1 and not managed) else 0
            f = int(r[fail_col])
            cells[0 if g == 1 else 1][0 if f == 1 else 1] += 1
        return cells

    for name, gap_col, fail_col, alpha in (
        ("H6a phi4->phi5 (unmanaged)", "gap_45", "p4_pathway", 0.025),
        ("H6c aggregate (unmanaged)", "gap_any", "p45_any", 0.05),
    ):
        res = analyze_cell(name, two_by_two_unmanaged(gap_col, fail_col), alpha)
        print_cell(res)
        print()


def necessary_condition_stats(rows: list[dict], gap_col: str, fail_col: str) -> dict:
    """Necessary-condition / safe-harbor statistics for one binary gap x fail pair.

    EXPLORATORY (see run_necessary_condition_analysis). Reports the statistics that
    describe an "X is necessary for Y" structure rather than "X is sufficient for Y":
      - the empty-cell safe-harbor test P(fail | no gap) with an exact binomial CI
        (the strength of conformance as a safe harbor);
      - necessity consistency P(gap | fail) (did every failure carry a gap?);
      - sufficiency P(fail | gap) (stated explicitly as the weak direction);
      - a dichotomous NCA-style ceiling effect size (Dul 2016): in the fully binary
        case the CE-FDH ceiling reduces to the empty-cell criterion, so the ceiling
        zone is the single low-condition/high-outcome quadrant (area .25 of the unit
        scope) when that cell is empty, giving d = .25 (Dul's "medium" band); d = 0
        when that cell is populated (the necessary condition is contradicted).
    """
    n = len(rows)
    n00 = n01 = n10 = n11 = 0  # [gap][fail]
    for r in rows:
        g = int(r[gap_col])
        f = int(r[fail_col])
        if g == 0 and f == 0:
            n00 += 1
        elif g == 0 and f == 1:
            n01 += 1  # no-gap-but-failure: the cell that must be empty for necessity
        elif g == 1 and f == 0:
            n10 += 1
        else:
            n11 += 1
    n_nogap = n00 + n01
    n_gap = n10 + n11
    n_fail = n01 + n11
    # Safe harbor: P(fail | no gap), exact 95% CI.
    sh_low, sh_high = clopper_pearson(n01, n_nogap)
    # NCA dichotomous ceiling effect size (see docstring).
    nca_d = 0.25 if n01 == 0 else 0.0
    return {
        "gap_col": gap_col,
        "fail_col": fail_col,
        "n": n,
        "counts": {"n00": n00, "n01": n01, "n10": n10, "n11": n11},
        "safe_harbor_fail_rate": (n01 / n_nogap if n_nogap else float("nan")),
        "safe_harbor_ci95": (sh_low, sh_high),
        "n_nogap": n_nogap,
        "necessity_consistency": (n11 / n_fail if n_fail else float("nan")),
        "n_fail": n_fail,
        "sufficiency": (n11 / n_gap if n_gap else float("nan")),
        "n_gap": n_gap,
        "nca_ceiling_d": nca_d,
    }


def print_necessary_condition(res: dict) -> None:
    c = res["counts"]
    print(f"  {res['gap_col']} necessary for {res['fail_col']} (n = {res['n']}):")
    print(f"                 fail=YES  fail=NO")
    print(f"    gap=YES         {c['n11']:>3}      {c['n10']:>3}")
    print(f"    gap=NO          {c['n01']:>3}      {c['n00']:>3}")
    lo, hi = res["safe_harbor_ci95"]
    print(
        f"    SAFE HARBOR   P(fail | no gap) = {res['safe_harbor_fail_rate']:.3f}  "
        f"({c['n01']}/{res['n_nogap']})  95% CI [{lo:.3f}, {hi:.3f}]"
    )
    print(
        f"    NECESSITY     P(gap | fail)   = {res['necessity_consistency']:.3f}  "
        f"({c['n11']}/{res['n_fail']})  [consistency of the necessary condition]"
    )
    print(
        f"    SUFFICIENCY   P(fail | gap)   = {res['sufficiency']:.3f}  "
        f"({c['n11']}/{res['n_gap']})  [the WEAK direction — stated explicitly]"
    )
    print(
        f"    NCA ceiling   d = {res['nca_ceiling_d']:.3f}  "
        f"[dichotomous CE-FDH; .25 = Dul's 'medium' band when the "
        f"no-gap/failure cell is empty]"
    )


def run_necessary_condition_analysis(rows: list[dict]) -> None:
    """EXPLORATORY necessary-condition + safe-harbor re-analysis (Stage S1 / Fork E).

    HARD HONESTY (PROGRAM_PLAN.md Locked Decision 3): this block is POST-HOC /
    EXPLORATORY on the n=26 corpus. The pre-registration tested SUFFICIENCY
    (H6a/b/c, run above and untouched). This re-scoping to a necessary-condition +
    safe-harbor reading is a data-motivated lens on the same data; it becomes the
    PRE-REGISTERED confirmatory hypothesis only for the large-N replication. Never
    label this result "pre-registered." The Fisher's-exact tests above remain the
    registered primary result and are not modified by anything here.

    Reports, for the aggregate cell and the phi4->phi5 cell:
      - the empty-cell safe-harbor test P(fail | no gap) with an exact binomial CI;
      - necessity consistency P(gap | fail) and the weak sufficiency P(fail | gap);
      - a dichotomous NCA-style ceiling effect size (Dul 2016).
    """
    print("Necessary-condition + safe-harbor re-analysis (EXPLORATORY; Fork E)")
    print("=" * 70)
    print(
        "  POST-HOC / EXPLORATORY on n=26 (NOT pre-registered; the registered test\n"
        "  above tested sufficiency). Method framing: Necessary Condition Analysis\n"
        "  (Dul 2016, Organizational Research Methods 19(1):10-52)."
    )
    print()
    for gap_col, fail_col in (("gap_any", "p45_any"), ("gap_45", "p4_pathway")):
        res = necessary_condition_stats(rows, gap_col, fail_col)
        print_necessary_condition(res)
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--fixture", action="store_true", help="Run the pipeline self-check only."
    )
    group.add_argument("--data", type=Path, help="Path to the coded n=30 dataset CSV.")
    args = parser.parse_args()
    if args.fixture:
        return run_fixture()
    return run_data(args.data)


if __name__ == "__main__":
    raise SystemExit(main())
