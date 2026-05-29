"""V parameter computation for the Tier-3-visibility-in-Tier-4 measure (P7).

Companion script for:
    Zharnikov, D. (2026). Brand as a Modular Layer: Tiered Organizational
    Architecture, Separability, and Firm Performance in Multi-Brand Strategies.
    Working Paper. https://doi.org/10.5281/zenodo.19930157

The V parameter operationalizes the Aaker-Joachimsthaler (2000) Brand
Relationship Spectrum continuously rather than typologically.

V is defined on [0, 1] as a convex combination of three observable indicators:
    V = w1 * v_name + w2 * v_visual + w3 * v_endorse

where
    v_name    = corporate-name appearance ratio at Tier-4 surfaces
                (fraction of brand instances whose customer-facing name
                contains the corporate parent's name; e.g., "Virgin Atlantic"
                contributes 1, "Tide" contributes 0).
    v_visual  = corporate-visual-element ratio (fraction of Tier-4
                instances whose primary packaging, signage, or interface
                carries the corporate parent's logo, color system, or
                typographic mark).
    v_endorse = endorsement coverage ratio (fraction of Tier-4 instances
                accompanied by an explicit "by [Parent]" or "from [Parent]"
                endorsement in customer-facing communication).

Default weights w1 = w2 = w3 = 1/3 (equal). Empirical recalibration is
encouraged; see paper P7 confirming criteria for inter-rater agreement
benchmarks (>.80 Krippendorff alpha across raters using the SBT eight-
dimension coding scheme).

Usage:
    uv run python v_parameter.py            # runs default examples
    python v_parameter.py                   # plain CPython works too

Reproducibility: this script is deterministic. No RNG seeded.
"""

from dataclasses import dataclass


@dataclass
class BrandInstance:
    """A single Tier-4 brand instance.

    Each indicator is a 0/1 flag for that one instance.
    """

    name: str
    parent: str
    name_carries_parent: int  # 0 or 1
    visual_carries_parent: int  # 0 or 1
    endorsement_present: int  # 0 or 1


def compute_v(
    instances: list[BrandInstance],
    w_name: float = 1 / 3,
    w_visual: float = 1 / 3,
    w_endorse: float = 1 / 3,
) -> dict:
    """Compute V across a set of Tier-4 instances belonging to one firm.

    Returns a dict with the three component ratios and the composite V.
    """
    if not instances:
        raise ValueError("instances must be non-empty")
    if abs((w_name + w_visual + w_endorse) - 1.0) > 1e-9:
        raise ValueError("weights must sum to 1.0")
    n = len(instances)
    v_name = sum(b.name_carries_parent for b in instances) / n
    v_visual = sum(b.visual_carries_parent for b in instances) / n
    v_endorse = sum(b.endorsement_present for b in instances) / n
    v = w_name * v_name + w_visual * v_visual + w_endorse * v_endorse
    return {
        "v_name": v_name,
        "v_visual": v_visual,
        "v_endorse": v_endorse,
        "V": v,
        "n_instances": n,
    }


def architecture_class(v: float) -> str:
    """Map V to the Aaker-Joachimsthaler architecture class."""
    if v >= 0.85:
        return "Branded House"
    if v >= 0.55:
        return "Sub-brand"
    if v >= 0.20:
        return "Endorsed"
    return "House of Brands"


# -----------------------------------------------------------------------------
# Worked examples
# -----------------------------------------------------------------------------

def _virgin_example() -> list[BrandInstance]:
    """Virgin Group: classic branded-house anchor (V close to 1)."""
    return [
        BrandInstance("Virgin Atlantic", "Virgin", 1, 1, 1),
        BrandInstance("Virgin Money", "Virgin", 1, 1, 1),
        BrandInstance("Virgin Media", "Virgin", 1, 1, 1),
        BrandInstance("Virgin Galactic", "Virgin", 1, 1, 1),
    ]


def _toyota_example() -> list[BrandInstance]:
    """Toyota / Lexus: sub-brand mid-V anchor.

    Toyota-branded models dominate the portfolio (high name + visual
    visibility); Lexus carries Toyota endorsement only via corporate
    disclosures (counted at endorsement axis, not name or visual).
    """
    return [
        BrandInstance("Toyota Camry", "Toyota", 1, 1, 1),
        BrandInstance("Toyota Corolla", "Toyota", 1, 1, 1),
        BrandInstance("Toyota RAV4", "Toyota", 1, 1, 1),
        BrandInstance("Toyota Highlander", "Toyota", 1, 1, 1),
        BrandInstance("Lexus RX", "Toyota", 0, 0, 1),
        BrandInstance("Lexus ES", "Toyota", 0, 0, 1),
    ]


def _marriott_example() -> list[BrandInstance]:
    """Marriott portfolio: endorsed mid-low V anchor."""
    return [
        BrandInstance("Courtyard by Marriott", "Marriott", 1, 1, 1),
        BrandInstance("Residence Inn", "Marriott", 0, 0, 1),
        BrandInstance("Ritz-Carlton", "Marriott", 0, 0, 0),
        BrandInstance("W Hotels", "Marriott", 0, 0, 0),
        BrandInstance("Sheraton", "Marriott", 0, 0, 0),
    ]


def _pg_example() -> list[BrandInstance]:
    """P&G: house-of-brands V close to 0 anchor."""
    return [
        BrandInstance("Tide", "P&G", 0, 0, 0),
        BrandInstance("Pampers", "P&G", 0, 0, 0),
        BrandInstance("Gillette", "P&G", 0, 0, 0),
        BrandInstance("Pantene", "P&G", 0, 0, 0),
        BrandInstance("Crest", "P&G", 0, 0, 0),
    ]


def main() -> None:
    print("V parameter worked examples")
    print("=" * 70)
    for name, factory in [
        ("Virgin (Branded House anchor)", _virgin_example),
        ("Toyota / Lexus (Sub-brand anchor)", _toyota_example),
        ("Marriott (Endorsed anchor)", _marriott_example),
        ("P&G (House of Brands anchor)", _pg_example),
    ]:
        result = compute_v(factory())
        print(f"\n{name}")
        print(f"  v_name    = {result['v_name']:.3f}")
        print(f"  v_visual  = {result['v_visual']:.3f}")
        print(f"  v_endorse = {result['v_endorse']:.3f}")
        print(f"  V         = {result['V']:.3f}")
        print(f"  Class     = {architecture_class(result['V'])}")


if __name__ == "__main__":
    main()
