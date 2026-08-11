"""Emit the paper's reported tables as machine-readable CSV.

WHY THIS EXISTS. The script is the ground truth for any value the paper calls computed:
if a script revision changes a number, the paper must change to match. That is only
enforceable if the numbers exist somewhere a diff can see them.
The other five scripts print human-readable tables and assert their own checks; this one
writes the same quantities to CSV so the paper's tables can be regenerated and compared
mechanically rather than by eye.

It computes NOTHING of its own. Every value is produced by calling the function in the
script that owns it, so this file cannot drift from the derivations -- if it disagrees
with them it is because it imported the wrong thing, not because it reimplemented it.

    Table 1  exact bracket width against the union bound        p2_exact
    Table 3  reported n_eff against the design-effect formula   reported_neff_check
    Table 4  bracket width surviving at a real panel's phi      p2_exact + phi_mapping
    Table 5  the dimensional ceiling, typical case              formal_model_checks
    Table 6  transferable share under a correlated panel        phi_mapping (kish)

Tables 2 and A1 and the worst-case block of Table 5 are Monte Carlo and are NOT emitted
here: they are produced, with their seeds and their own pass/fail checks, by
phi_mapping.py, threat1_kill_test.py and formal_model_checks.py respectively, whose
stdout `reproduce.sh` captures into ../output/logs/. Re-deriving them here would mean a
second implementation of a seeded simulation, which is the drift this file exists to
prevent.

RUN
    uv run --with numpy --with scipy python emit_paper_tables.py

Writes ../output/tables/table{1,3,4,5,6}.csv. Deterministic: no RNG is used.
"""

from __future__ import annotations

import csv
from pathlib import Path

from formal_model_checks import expected_abs_inner
from p2_exact import bracket_exact, marginal_flag_rate, phi_err_exact, union_bound
from phi_mapping import kish, rho_from_phi, t_of_q
from reported_neff_check import design_effect_neff

OUT = Path(__file__).resolve().parent.parent / "output" / "tables"

# The published nine-judge panel's reported figures. Quoted, not derived -- see
# reported_neff_check.py for the check that its n_eff IS this formula at this phi.
REPORTED = [
    ("MNLI", 9, 0.391, 2.18),
    ("SNLI", 9, 0.354, 2.35),
    ("AlphaNLI", 9, 0.328, 2.48),
    ("MNLI (chain-of-thought)", 9, 0.456, 1.94),
]


def write(name: str, header: list[str], rows: list[list]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)
    print(f"    wrote {path.relative_to(OUT.parent.parent)}  ({len(rows)} rows)")


def table1() -> None:
    """Exact bracket width against its union bound, k = 9, t = .30."""
    k, t = 9, 0.30
    p = marginal_flag_rate(t)
    rows = []
    for rho in (0.0, 0.5, 0.7, 0.9, 0.95, 0.99, 0.999):
        phi = phi_err_exact(rho, t)
        w = bracket_exact(rho, t, k)[2]
        ub = union_bound(k, p, phi)
        rows.append(
            [
                f"{rho:.3f}",
                f"{phi:.3f}",
                f"{w:.3f}",
                f"{ub:.3f}",
                f"{ub / w:.2f}",
                ub < 1.0,
            ]
        )
    write(
        "table1_bracket_width_vs_union_bound.csv",
        [
            "rho",
            "phi_err",
            "W_exact",
            "union_bound",
            "bound_over_exact",
            "bound_informative",
        ],
        rows,
    )


def table3() -> None:
    """Reported effective sample sizes against the design-effect formula."""
    rows = []
    for name, k, phi, reported in REPORTED:
        formula = design_effect_neff(k, phi)
        rows.append(
            [
                name,
                k,
                f"{phi:.3f}",
                f"{formula:.3f}",
                f"{reported:.2f}",
                f"{formula - reported:+.3f}",
            ]
        )
    write(
        "table3_reported_neff_vs_formula.csv",
        [
            "condition",
            "k",
            "reported_phi",
            "design_effect_formula",
            "reported_neff",
            "difference",
        ],
        rows,
    )


def table4() -> None:
    """Bracket width surviving at the published panel's error correlations."""
    k = 9
    rows = []
    for name, _k, phi, _n in REPORTED:
        cells = []
        for q in (0.10, 0.25, 0.50):
            t = t_of_q(q)
            rho = rho_from_phi(phi, t)
            w = bracket_exact(rho, t, k)[2]
            w0 = bracket_exact(0.0, t, k)[2]
            cells.append(f"{100 * w / w0:.1f}")
        rows.append([name, f"{phi:.3f}", *cells])
    write(
        "table4_bracket_surviving.csv",
        [
            "condition",
            "phi",
            "pct_surviving_q_.10",
            "pct_surviving_q_.25",
            "pct_surviving_q_.50",
        ],
        rows,
    )


def table5() -> None:
    """The dimensional ceiling, typical case: uniform inspection directions."""
    import math

    rows = []
    for n in (4, 10, 25, 48, 100):
        limit = 1.0 / expected_abs_inner(n)
        rows.append([n, f"{limit:.3f}", f"{math.sqrt(math.pi * n / 2):.3f}"])
    write(
        "table5_dimensional_ceiling_typical.csv",
        ["n", "exact_limit", "sqrt_pi_n_over_2"],
        rows,
    )


def table6() -> None:
    """Transferable share of a specification under a correlated receiving panel."""
    rows = []
    for r, k, phi in (
        (6, 3, 0.35),
        (6, 9, 0.39),
        (16, 9, 0.39),
        (16, 40, 0.39),
        (48, 200, 0.25),
    ):
        neff = kish(k, phi)
        sigma = min(neff, r) / r
        rows.append(
            [
                r,
                k,
                f"{phi:.2f}",
                f"{neff:.2f}",
                f"{100 * sigma:.1f}",
                f"{100 * (1 - sigma):.1f}",
            ]
        )
    write(
        "table6_transferable_share.csv",
        [
            "r_conditions",
            "k_evaluators",
            "phi_bar",
            "n_eff",
            "transferable_pct",
            "signatory_residual_pct",
        ],
        rows,
    )


def main() -> int:
    print("Emitting the paper's deterministic tables from their owning derivations.")
    table1()
    table3()
    table4()
    table5()
    table6()
    print(
        "\nTables 2 and A1, and the worst-case block of Table 5, are seeded Monte Carlo and\n"
        "are produced by phi_mapping.py, threat1_kill_test.py and formal_model_checks.py.\n"
        "Their stdout is captured by reproduce.sh into ../output/logs/."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
