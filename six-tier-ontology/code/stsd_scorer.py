"""STSD scorer — Six-Tier Separability Diagnostic companion script.

Implements the structured-judgment instrument from Zharnikov 2026ag, Table 4.
Given an ordinal response per tier (Fused / Partial / Independent), the scorer
returns:

    1. The six-cell separability profile (one state per tier)
    2. A Fused-tier count (the framework's primary risk index)
    3. A flip-case flag (Tier 1 = Fused signals identity-bound owner)
    4. A tier-level integration-priority ranking derived from the
       constraint hierarchy

The scorer encodes the ordinal mapping defined in Table 4 of the paper:
Fused = 0, Partial = 1, Independent = 2. It is a structured-judgment
calculator; it does not produce a continuous score because the underlying
construct is ordinal, not interval (per the paper's *Notes* on Table 4).

Usage:

    python stsd_scorer.py --example
    python stsd_scorer.py --input target_responses.json

Run:

    python stsd_scorer.py --example

prints the two illustrative profiles from the paper:

    - Independent / Independent / Independent / Independent / Partial / Partial
      (the SaaS company in the Tier 4 vignette)
    - Fused / Fused / Partial / Fused / Partial / Fused
      (the regional manufacturer in the Tier 1 vignette)

Reproducibility: deterministic. No random number generation. No external
dependencies beyond the Python standard library.

Citation:
    Zharnikov, D. (2026). Dual Hierarchies of Organizational Transferability:
    A Six-Tier Ontology and Theory of Acquisition Failure Propagation.
    Working paper, doi:10.5281/zenodo.19895813.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from typing import Literal

# --------------------------------------------------------------------------
# Constants — encode Table 4 (the paper's STSD)
# --------------------------------------------------------------------------

State = Literal["Fused", "Partial", "Independent"]

VALID_STATES: tuple[str, ...] = ("Fused", "Partial", "Independent")

ORDINAL_MAP: dict[str, int] = {
    "Fused": 0,
    "Partial": 1,
    "Independent": 2,
}

TIER_NAMES: tuple[str, ...] = (
    "Tier 1 Owner Intent",
    "Tier 2 Business Model",
    "Tier 3 Business Entity",
    "Tier 4 Product",
    "Tier 5 Process",
    "Tier 6 Organization",
)

DIAGNOSTIC_QUESTIONS: tuple[str, ...] = (
    "Can the owner state Intent in one sentence not naming the company?",
    "Is the Business Model articulated as a written canvas independent of habit?",
    "Are debts and obligations decoupled from the owner's balance sheet?",
    "Is there a written Product specification a third party could test against?",
    "Does the Process run a continuous month without the owner present?",
    "Does every owner role have a named, trained successor?",
)


# --------------------------------------------------------------------------
# Data classes
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class STSDProfile:
    """A six-cell STSD profile, one state per tier."""

    tier_1_intent: State
    tier_2_model: State
    tier_3_entity: State
    tier_4_product: State
    tier_5_process: State
    tier_6_organization: State

    def as_tuple(self) -> tuple[State, ...]:
        return (
            self.tier_1_intent,
            self.tier_2_model,
            self.tier_3_entity,
            self.tier_4_product,
            self.tier_5_process,
            self.tier_6_organization,
        )

    def fused_count(self) -> int:
        """Number of tiers in the Fused state.

        The paper's primary risk index. Higher Fused-tier count => lower
        transferability => higher predicted post-acquisition value
        degradation (the tested hypothesis in the validation agenda).
        """
        return sum(1 for s in self.as_tuple() if s == "Fused")

    def is_flip_case(self) -> bool:
        """True iff Tier 1 = Fused (identity-bound owner / flip case).

        Per the paper's "Flip Case" subsection, Tier 1 = Fused signals
        Intent ≡ Product, which is a structural feature of the target,
        not a remediable information asymmetry. The framework's
        prescription is price renegotiation or deal exit, not
        integration planning.
        """
        return self.tier_1_intent == "Fused"

    def integration_priority(self) -> list[tuple[str, str, int]]:
        """Tier-level integration priority derived from the constraint
        hierarchy.

        Returns a list of (tier_name, state, priority_rank) tuples in
        constraint-hierarchy order (Tier 1 first, Tier 6 last). The
        constraint hierarchy implies that upper-tier specification
        clarity is logically prior to lower-tier integration execution
        (see Table 3, "Integration Sequencing"). Tiers with state =
        Fused at constraint-hierarchy position N are flagged as
        higher-priority than equivalent Fused tiers at position N+1.
        """
        return [
            (name, state, rank)
            for rank, (name, state) in enumerate(zip(TIER_NAMES, self.as_tuple()), start=1)
        ]


# --------------------------------------------------------------------------
# Scorer
# --------------------------------------------------------------------------


def validate_response(state: str) -> State:
    if state not in VALID_STATES:
        raise ValueError(
            f"Invalid state '{state}'. Must be one of {VALID_STATES}."
        )
    return state  # type: ignore[return-value]


def score(responses: dict[str, str]) -> STSDProfile:
    """Build an STSDProfile from a dict of tier responses.

    Expected keys: 'tier_1_intent', 'tier_2_model', 'tier_3_entity',
    'tier_4_product', 'tier_5_process', 'tier_6_organization'.
    """
    required = {
        "tier_1_intent",
        "tier_2_model",
        "tier_3_entity",
        "tier_4_product",
        "tier_5_process",
        "tier_6_organization",
    }
    missing = required - set(responses)
    if missing:
        raise ValueError(f"Missing tier responses: {sorted(missing)}")
    return STSDProfile(
        tier_1_intent=validate_response(responses["tier_1_intent"]),
        tier_2_model=validate_response(responses["tier_2_model"]),
        tier_3_entity=validate_response(responses["tier_3_entity"]),
        tier_4_product=validate_response(responses["tier_4_product"]),
        tier_5_process=validate_response(responses["tier_5_process"]),
        tier_6_organization=validate_response(responses["tier_6_organization"]),
    )


def render_report(profile: STSDProfile) -> str:
    """Render a human-readable report of the profile."""
    lines: list[str] = []
    lines.append("STSD profile")
    lines.append("=" * 50)
    for name, state, rank in profile.integration_priority():
        lines.append(f"  [{rank}] {name:32s} {state}")
    lines.append("")
    lines.append(f"Fused-tier count : {profile.fused_count()} / 6")
    lines.append(f"Flip case        : {profile.is_flip_case()}")
    lines.append("")
    if profile.is_flip_case():
        lines.append(
            "FLIP CASE FLAG: Tier 1 = Fused. Per the framework, this is a "
            "structural feature of the target, not a remediable information "
            "asymmetry. Recommended action: price renegotiation or deal "
            "exit, not integration planning."
        )
    elif profile.fused_count() >= 3:
        lines.append(
            "HIGH RISK: Three or more Fused tiers. Per the integration "
            "sequencing principle, address upper-tier Fused states (Tier 1, "
            "Tier 2) before committing to lower-tier integration."
        )
    elif profile.fused_count() >= 1:
        lines.append(
            "MODERATE RISK: At least one Fused tier. Address per "
            "constraint-hierarchy priority (upper tiers first)."
        )
    else:
        lines.append("LOW PRE-CLOSE TRANSFERABILITY RISK based on STSD only.")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Examples — the two illustrative profiles from the paper
# --------------------------------------------------------------------------

EXAMPLE_SAAS = {
    "tier_1_intent": "Independent",
    "tier_2_model": "Independent",
    "tier_3_entity": "Independent",
    "tier_4_product": "Independent",
    "tier_5_process": "Partial",
    "tier_6_organization": "Partial",
}

EXAMPLE_REGIONAL_MANUFACTURER = {
    "tier_1_intent": "Fused",
    "tier_2_model": "Fused",
    "tier_3_entity": "Partial",
    "tier_4_product": "Fused",
    "tier_5_process": "Partial",
    "tier_6_organization": "Fused",
}


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Score the Six-Tier Separability Diagnostic (STSD)."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--example",
        action="store_true",
        help="Print the two illustrative profiles from the paper.",
    )
    group.add_argument(
        "--input",
        type=str,
        help="Path to a JSON file containing tier responses.",
    )
    args = parser.parse_args(argv)

    if args.example:
        print("Example 1: SaaS company (Tier 4 vignette)")
        print("-" * 50)
        print(render_report(score(EXAMPLE_SAAS)))
        print()
        print("Example 2: Regional manufacturer (Tier 1 vignette)")
        print("-" * 50)
        print(render_report(score(EXAMPLE_REGIONAL_MANUFACTURER)))
        return 0

    with open(args.input, encoding="utf-8") as f:
        responses = json.load(f)
    print(render_report(score(responses)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
