"""render_figure1.py — Render Figure 1 (Multi-Interface Specification Model)
for R-paper 2026am v1.1.0.

Companion figure-render script for:

    Zharnikov, D. (2026). Specification Readiness and Endogenous Friction:
    An Information-Theoretic Theory of Multi-Interface Organizational
    Architecture. Working paper key: 2026am.

Produces a clean academic hub-and-spoke diagram showing:
    - Specification vector S at the center (substrate)
    - Six perception-weight vectors w_1 ... w_6 as spokes with distinct
      dimension-weight patterns
    - Six rendering operators R_i(S, w_i) at the spoke ends
    - Six recipient-class interface labels at the periphery:
        Consumer / Investor / Employer-Brand / Regulatory /
        Supplier-Partner / Peer-and-Media

Output:
    code/plots/figure_1_multi_interface_specification_model.svg
    code/plots/figure_1_multi_interface_specification_model.png

Run command (from project root):
    uv run --with matplotlib --with numpy \\
        python research/multi_interface_paper/code/render_figure1.py

Style discipline:
    - Greyscale + minimal accent (academic print-safe)
    - Sans-serif typography
    - No leading zeros on numeric labels (.5 not 0.5)
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch
from matplotlib.lines import Line2D

CODE_DIR = Path(__file__).resolve().parent
PLOT_DIR = CODE_DIR / "plots"
PLOT_DIR.mkdir(parents=True, exist_ok=True)


INTERFACE_LABELS = [
    "Consumer",
    "Investor",
    "Employer-Brand",
    "Regulatory",
    "Supplier-Partner",
    "Peer-and-Media",
]


def render_figure() -> tuple[Path, Path]:
    fig, ax = plt.subplots(figsize=(10, 10), dpi=150)
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect("equal")
    ax.axis("off")

    # Hub: specification vector S
    hub = Circle(
        (0, 0), 0.18, facecolor="#222222", edgecolor="black", linewidth=1.6, zorder=5
    )
    ax.add_patch(hub)
    ax.text(
        0,
        0,
        r"$\mathbf{S}$",
        color="white",
        ha="center",
        va="center",
        fontsize=22,
        fontweight="bold",
        zorder=6,
    )
    ax.text(
        0,
        -0.30,
        "specification\nsubstrate",
        ha="center",
        va="top",
        fontsize=9.5,
        color="#333333",
        style="italic",
    )

    # Six spokes (w_i vectors) at 60-degree intervals
    n = 6
    angles = np.linspace(np.pi / 2, np.pi / 2 - 2 * np.pi, n, endpoint=False)
    spoke_inner = 0.20  # hub radius edge
    operator_node_radius = 0.99  # where the R_i rendering operator sits
    label_radius = 1.35  # where the interface class label sits

    # Distinct dash patterns per spoke to convey "distinct perception-weight vectors"
    dash_patterns = [
        (0, ()),  # solid
        (0, (5, 2)),  # dash
        (0, (1, 1.5)),  # dot
        (0, (4, 2, 1, 2)),  # dash-dot
        (0, (3, 1, 1, 1, 1, 1)),  # complex
        (0, (6, 2, 2, 2)),  # long-dash-dash
    ]

    for i, theta in enumerate(angles):
        x_in = spoke_inner * np.cos(theta)
        y_in = spoke_inner * np.sin(theta)
        x_out = operator_node_radius * np.cos(theta)
        y_out = operator_node_radius * np.sin(theta)

        # Spoke line: w_i with distinct pattern
        ax.add_line(
            Line2D(
                [x_in, x_out],
                [y_in, y_out],
                color="#555555",
                linewidth=1.6,
                linestyle=dash_patterns[i],
                zorder=2,
            )
        )

        # w_i label slightly offset from spoke midpoint, perpendicular outward
        mid_x = (x_in + x_out) * 0.45
        mid_y = (y_in + y_out) * 0.45
        # perpendicular unit vector (outward-rotated)
        perp_x = -np.sin(theta) * 0.10
        perp_y = np.cos(theta) * 0.10
        ax.text(
            mid_x + perp_x,
            mid_y + perp_y,
            f"$\\mathbf{{w}}_{i+1}$",
            ha="center",
            va="center",
            fontsize=12,
            color="#333333",
        )

        # Operator node: R_i(S, w_i)
        op_node = Circle(
            (x_out, y_out),
            0.14,
            facecolor="white",
            edgecolor="black",
            linewidth=1.3,
            zorder=4,
        )
        ax.add_patch(op_node)
        ax.text(
            x_out,
            y_out,
            f"$R_{i+1}$",
            ha="center",
            va="center",
            fontsize=11,
            color="#222222",
            zorder=5,
        )

        # Interface label at the periphery
        lab_x = label_radius * np.cos(theta)
        lab_y = label_radius * np.sin(theta)
        ax.text(
            lab_x,
            lab_y,
            INTERFACE_LABELS[i],
            ha="center",
            va="center",
            fontsize=10.5,
            color="#222222",
            fontweight="bold",
        )

        # Short arrow from operator node to interface label
        ax.add_patch(
            FancyArrowPatch(
                (x_out, y_out),
                (lab_x - 0.04 * np.cos(theta), lab_y - 0.04 * np.sin(theta)),
                arrowstyle="-|>",
                mutation_scale=12,
                color="#555555",
                linewidth=1.0,
                zorder=3,
            )
        )

    # Figure-internal text limited to in-figure labels (S hub label,
    # w_i spoke labels, R_i operator-node labels, interface-class periphery
    # labels). Figure title and full caption are supplied by the paper text
    # surrounding the embed, per AMA convention (caption above; notes below).

    plt.tight_layout()

    svg_path = PLOT_DIR / "figure_1_multi_interface_specification_model.svg"
    png_path = PLOT_DIR / "figure_1_multi_interface_specification_model.png"
    fig.savefig(svg_path, format="svg", bbox_inches="tight")
    fig.savefig(png_path, format="png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    return svg_path, png_path


if __name__ == "__main__":
    svg, png = render_figure()
    print(f"Wrote SVG: {svg}")
    print(f"Wrote PNG: {png}")
