"""Multi-Brand Capacity Diagnostic (MBCD) scoring tool.

Companion script for:
    Zharnikov, D. (2026). Brand as a Modular Layer: Tiered Organizational
    Architecture, Separability, and Firm Performance in Multi-Brand Strategies.
    Working Paper. https://doi.org/10.5281/zenodo.19930157

The MBCD predicts, from per-tier separability scores plus the V parameter,
how many additional Tier-4 brand instances a firm can host on its current
substrate without performance degradation.

Each tier is scored on a 1-5 scale of separability under multi-brand
operation:
    1 = fully bound (single-brand only)
    2 = mostly bound (separation requires substantial new investment)
    3 = mixed (some brand-agnostic, some brand-bound)
    4 = mostly separable (modest adaptation enables additional brands)
    5 = fully separable (substrate routinely hosts many brands)

Tier 4 is omitted (it IS the brand instance; capacity is measured in
Tier-4 units). Tier 1 (Owner Intent) is admissibility-only: an Owner
Intent that is brand-bound (s1 = 1) blocks portfolio expansion regardless
of downstream separability.

The composite capacity prediction is:
    K_hat = round(  base * f(s2, s3, s5, s6) * g(V)  )

where
    base   = current Tier-4 instance count operated by the firm
    f(.)   = geometric mean of (s2, s3, s5, s6) rescaled to [0.2, 2.0]
    g(V)   = 1 + (1 - V) * lambda_V       # low V amplifies capacity
    lambda_V default = 0.5

The geometric mean is used because tier separability is a Liebig-style
binding constraint: the worst tier limits the rest. The g(V) term reflects
that low V (house-of-brands) confers additional capacity headroom over
high V (branded-house) at equal separability scores, because Tier-1
propagation does not contaminate new Tier-4 instances at low V.

Calibration is illustrative; weights and the lambda_V parameter should be
re-fit on the empirical capacity panel described in P1's confirming
criteria once available.

Usage:
    uv run python mbcd_scorer.py
"""

from dataclasses import dataclass


@dataclass
class FirmAudit:
    name: str
    base_brand_count: int
    s1: int  # Tier 1 Owner Intent separability (1-5)
    s2: int  # Tier 2 Business Model separability
    s3: int  # Tier 3 Business Entity separability
    s5: int  # Tier 5 Process separability
    s6: int  # Tier 6 Organization separability
    v: float  # Tier-3-visibility-in-Tier-4 parameter


def _geo_mean(values: list[int]) -> float:
    product = 1.0
    for v in values:
        product *= max(v, 1)
    return product ** (1 / len(values))


def predict_capacity(audit: FirmAudit, lambda_v: float = 0.5) -> dict:
    """Return predicted multi-brand capacity and component diagnostic."""
    if audit.s1 == 1:
        return {
            "blocked": True,
            "reason": "Tier-1 Owner Intent fully brand-bound; no headroom.",
            "K_hat": audit.base_brand_count,
            "f_separability": float("nan"),
            "g_V": float("nan"),
        }
    g_v = 1 + (1 - audit.v) * lambda_v
    geo = _geo_mean([audit.s2, audit.s3, audit.s5, audit.s6])
    # Map geometric mean from [1, 5] to [0.2, 2.0]
    f_sep = 0.2 + (geo - 1) / 4 * (2.0 - 0.2)
    k_hat = round(audit.base_brand_count * f_sep * g_v)
    return {
        "blocked": False,
        "geo_mean_s2_s3_s5_s6": round(geo, 3),
        "f_separability": round(f_sep, 3),
        "g_V": round(g_v, 3),
        "K_hat": k_hat,
        "headroom": k_hat - audit.base_brand_count,
    }


# -----------------------------------------------------------------------------
# Worked examples
# -----------------------------------------------------------------------------

EXAMPLES = [
    FirmAudit(
        name="P&G (house of brands; high separability)",
        base_brand_count=200,
        s1=4, s2=3, s3=5, s5=5, s6=5, v=0.05,
    ),
    FirmAudit(
        name="Inditex (Zara/MD/Pull&Bear; high Tier-5 sharing)",
        base_brand_count=8,
        s1=3, s2=3, s3=4, s5=5, s6=4, v=0.15,
    ),
    FirmAudit(
        name="Marriott (endorsed; portfolio mid-V)",
        base_brand_count=30,
        s1=3, s2=3, s3=4, s5=4, s6=3, v=0.4,
    ),
    FirmAudit(
        name="Toyota (sub-brand; mid-high V)",
        base_brand_count=3,
        s1=3, s2=3, s3=3, s5=3, s6=3, v=0.7,
    ),
    FirmAudit(
        name="Virgin Group (branded house; high V on broad separability)",
        base_brand_count=12,
        s1=4, s2=4, s3=4, s5=3, s6=2, v=0.95,
    ),
    FirmAudit(
        name="Founder-led single brand (Tier-1 bound)",
        base_brand_count=1,
        s1=1, s2=2, s3=2, s5=2, s6=2, v=1.0,
    ),
]


def main() -> None:
    print("MBCD worked examples")
    print("=" * 78)
    for audit in EXAMPLES:
        result = predict_capacity(audit)
        print(f"\n{audit.name}")
        print(
            f"  scores: s1={audit.s1} s2={audit.s2} s3={audit.s3} "
            f"s5={audit.s5} s6={audit.s6}; V={audit.v:.2f}; "
            f"base K={audit.base_brand_count}"
        )
        if result["blocked"]:
            print(f"  BLOCKED: {result['reason']}")
            continue
        print(
            f"  geo-mean(s2,s3,s5,s6) = {result['geo_mean_s2_s3_s5_s6']}; "
            f"f_sep = {result['f_separability']}; g(V) = {result['g_V']}"
        )
        print(
            f"  predicted capacity K_hat = {result['K_hat']}  "
            f"(headroom = {result['headroom']:+d})"
        )


if __name__ == "__main__":
    main()
