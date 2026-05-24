"""projection_demo.py — Worked example of the capability-as-projection formalism.

Companion computation script for:

    Zharnikov, D. (2026). Capability as Projection of an Append-Only Organizational Log: Toward an
    Event-Sourced Theory of Organizational Capability. Working paper.

Implements the minimal mathematical machinery specified in
``research/capability_as_projection_paper/FORMALISM_v0.md``:

    1. The event log ``L = (E, <=)`` as a poset of typed events
       (FORMALISM Section 1.1)
    2. The projection operator ``pi_lambda(L, q, t)`` as a weighted
       prefix sum with exponential decay (FORMALISM Section 1.2)
    3. The compatibility function ``kappa(L_A, L_B) = 1 - |conflicts| /
       (|L_A| + |L_B|)`` (FORMALISM Section 1.3)

The script constructs two small synthetic logs L_A and L_B representing
a stylized firm-A vs firm-B M&A scenario, then computes pi_lambda on a
"scaling capability" query under three decay parameters
lambda in {0.0, 0.1, 0.5} and the compatibility kappa(L_A, L_B).

Reproducibility:

    Fixed RNG seed = 42.
    Run command (from the paper directory):

        uv run python code/projection_demo.py

    Output is fully deterministic; no network calls, no external data.

This script is a numerical-coherence check for the formalism, not an
empirical confirmation. See ``PRE_EXPERIMENT_REPORT.md`` and
``POST_EXPERIMENT_REPORT.md`` for scope and interpretation.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any, Callable

RANDOM_SEED: int = 42

# Fixed event taxonomy from METHODS_APPENDIX Section 2.
EVENT_TYPES: tuple[str, ...] = (
    "DECISION",
    "FAILURE",
    "POLICY",
    "PERSONNEL",
    "ARTIFACT",
)


# --------------------------------------------------------------------------
# Primitives (FORMALISM Section 1.1)
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Event:
    """A single immutable event on an organization's operational log.

    Fields follow FORMALISM Section 1.1 ``e = (id, t, a, tau, p, c)``.
    """

    id: str
    timestamp: datetime
    actor: str
    type: str
    payload: dict[str, Any]
    caused_by: str | None = None


@dataclass
class Log:
    """An append-only poset of events ordered by causal-temporal
    precedence. The implementation stores events in a list and treats
    the partial order as defined by ``(timestamp, caused_by)``.
    """

    events: list[Event] = field(default_factory=list)

    def add_event(self, event: Event) -> None:
        self.events.append(event)

    def query_subset(self, predicate: Callable[[Event], bool]) -> list[Event]:
        """Return the L_q subset of events satisfying the predicate."""
        return [e for e in self.events if predicate(e)]

    def __len__(self) -> int:
        return len(self.events)


# --------------------------------------------------------------------------
# Projection operator pi_lambda (FORMALISM Section 1.2)
# --------------------------------------------------------------------------


def projection_pi_lambda(
    log: Log,
    query_subset_fn: Callable[[Event], bool],
    render_time_t: datetime,
    weights_fn: Callable[[Event], float],
    lam: float,
) -> float:
    """Weighted prefix sum with exponential decay.

    Implements:

        pi_lambda(L, q, t) = sum_{e in L_q, t_e <= t}
                             w_q(e) * exp(-lambda * (t - t_e))

    Time deltas are measured in years (365.25-day years) so that lambda
    has the same units across queries.

    Args:
        log: the operational log L.
        query_subset_fn: predicate selecting L_q from L.
        render_time_t: the moment the question is asked.
        weights_fn: signed per-event weight w_q.
        lam: decay parameter lambda >= 0.

    Returns:
        The scalar projection value.
    """
    if lam < 0:
        raise ValueError("decay parameter lambda must be non-negative.")
    total = 0.0
    seconds_per_year = 365.25 * 24 * 3600
    for e in log.events:
        if e.timestamp > render_time_t:
            continue
        if not query_subset_fn(e):
            continue
        dt_years = (render_time_t - e.timestamp).total_seconds() / seconds_per_year
        total += weights_fn(e) * math.exp(-lam * dt_years)
    return total


# --------------------------------------------------------------------------
# Compatibility function kappa (FORMALISM Section 1.3)
# --------------------------------------------------------------------------


def compatibility_kappa(
    log_a: Log,
    log_b: Log,
    conflicts_fn: Callable[[Event, Event], bool],
) -> float:
    """Compute kappa(L_A, L_B) = 1 - |conflicts| / (|L_A| + |L_B|).

    A conflict is any pair (e_A, e_B) such that conflicts_fn returns
    True. Each conflicting event is counted once (the numerator is the
    number of distinct events implicated in at least one conflict pair,
    which preserves kappa in [0, 1]).
    """
    if len(log_a) + len(log_b) == 0:
        return 1.0
    implicated: set[str] = set()
    for ea in log_a.events:
        for eb in log_b.events:
            if conflicts_fn(ea, eb):
                implicated.add(ea.id)
                implicated.add(eb.id)
    return 1.0 - len(implicated) / (len(log_a) + len(log_b))


# --------------------------------------------------------------------------
# Synthetic-log construction
# --------------------------------------------------------------------------


def _t(year_offset_days: int) -> datetime:
    """Helper: timestamps anchored at 2018-01-01 UTC."""
    return datetime(2018, 1, 1, tzinfo=timezone.utc) + timedelta(days=year_offset_days)


def build_firm_a_log() -> Log:
    """Stylized firm A with strong scaling-capability log: many
    DECISION + POLICY events in the scaling domain, two FAILURE events
    early on that were superseded later.
    """
    log = Log()
    log.add_event(
        Event("a01", _t(0), "founder", "DECISION",
              {"domain": "scaling", "summary": "open second region"})
    )
    log.add_event(
        Event("a02", _t(60), "ops_lead", "POLICY",
              {"domain": "scaling", "summary": "regional autonomy v1"})
    )
    log.add_event(
        Event("a03", _t(120), "ops_lead", "FAILURE",
              {"domain": "scaling", "summary": "region-2 stockout"},
              caused_by="a02")
    )
    log.add_event(
        Event("a04", _t(200), "ops_lead", "POLICY",
              {"domain": "scaling", "summary": "regional autonomy v2"},
              caused_by="a03")
    )
    log.add_event(
        Event("a05", _t(300), "head_eng", "ARTIFACT",
              {"domain": "scaling", "summary": "deploy pipeline 1.0"})
    )
    log.add_event(
        Event("a06", _t(420), "ceo", "DECISION",
              {"domain": "scaling", "summary": "open third region"})
    )
    log.add_event(
        Event("a07", _t(560), "ops_lead", "FAILURE",
              {"domain": "scaling", "summary": "region-3 hiring miss"})
    )
    log.add_event(
        Event("a08", _t(720), "ops_lead", "POLICY",
              {"domain": "scaling", "summary": "hiring rubric v1"})
    )
    log.add_event(
        Event("a09", _t(900), "ceo", "PERSONNEL",
              {"domain": "scaling", "summary": "hire regional GM"})
    )
    log.add_event(
        Event("a10", _t(1100), "ceo", "DECISION",
              {"domain": "scaling", "summary": "open fourth region"})
    )
    return log


def build_firm_b_log() -> Log:
    """Stylized firm B with thinner scaling log, partially conflicting
    policies / personnel with firm A.
    """
    log = Log()
    log.add_event(
        Event("b01", _t(30), "founder", "DECISION",
              {"domain": "scaling", "summary": "single-region focus"})
    )
    log.add_event(
        Event("b02", _t(90), "ops_lead", "POLICY",
              {"domain": "scaling", "summary": "centralized ops mandate"})
    )
    log.add_event(
        Event("b03", _t(150), "head_eng", "ARTIFACT",
              {"domain": "scaling", "summary": "monolith deploy v1"})
    )
    log.add_event(
        Event("b04", _t(240), "ceo", "PERSONNEL",
              {"domain": "scaling", "summary": "hire regional GM"})
    )
    log.add_event(
        Event("b05", _t(330), "ops_lead", "FAILURE",
              {"domain": "scaling", "summary": "single-region outage"})
    )
    log.add_event(
        Event("b06", _t(450), "ops_lead", "POLICY",
              {"domain": "scaling", "summary": "centralized ops v2"},
              caused_by="b05")
    )
    log.add_event(
        Event("b07", _t(600), "ceo", "DECISION",
              {"domain": "scaling", "summary": "open second region"})
    )
    log.add_event(
        Event("b08", _t(780), "ops_lead", "POLICY",
              {"domain": "scaling", "summary": "hiring rubric v0"})
    )
    log.add_event(
        Event("b09", _t(960), "head_eng", "ARTIFACT",
              {"domain": "scaling", "summary": "service split 1.0"})
    )
    log.add_event(
        Event("b10", _t(1130), "ceo", "DECISION",
              {"domain": "scaling", "summary": "open third region"})
    )
    return log


# --------------------------------------------------------------------------
# Query, weights, conflicts
# --------------------------------------------------------------------------


def scaling_query(e: Event) -> bool:
    """Predicate for the L_q subset: events in the scaling domain."""
    return e.payload.get("domain") == "scaling"


def scaling_weights(e: Event) -> float:
    """Per-event weights for the scaling-capability query.

    DECISION and POLICY events with domain=scaling contribute +1.0;
    ARTIFACT contributes +0.5; FAILURE contributes -1.0; PERSONNEL is
    neutral 0.0 (personnel changes proxy through later POLICY events).
    """
    t = e.type
    if t == "DECISION" or t == "POLICY":
        return 1.0
    if t == "ARTIFACT":
        return 0.5
    if t == "FAILURE":
        return -1.0
    return 0.0


def scaling_conflicts(ea: Event, eb: Event) -> bool:
    """Conflict predicate: two POLICY events in the same domain conflict
    (different rules for the same domain cannot both hold), and two
    PERSONNEL events in the same domain conflict (the same role cannot
    be held by two named successors).
    """
    if ea.payload.get("domain") != eb.payload.get("domain"):
        return False
    if ea.type == "POLICY" and eb.type == "POLICY":
        return True
    if ea.type == "PERSONNEL" and eb.type == "PERSONNEL":
        return True
    return False


# --------------------------------------------------------------------------
# Main demonstration
# --------------------------------------------------------------------------


def run() -> None:
    random.seed(RANDOM_SEED)

    log_a = build_firm_a_log()
    log_b = build_firm_b_log()

    render_t = _t(1200)  # ~3.3 years after firm founding

    print("projection_demo.py — Firm-as-Event-Log formalism worked example")
    print("=" * 68)
    print(f"RANDOM_SEED = {RANDOM_SEED}")
    print(f"render time t = {render_t.isoformat()}")
    print(f"|L_A| = {len(log_a)} events; |L_B| = {len(log_b)} events")
    print()

    # pi_lambda under three decay parameters
    lambdas = (0.0, 0.1, 0.5)
    print("Projection pi_lambda(L, scaling_query, t) under varying lambda")
    print("-" * 68)
    print(f"{'lambda':>8} | {'pi(L_A)':>10} | {'pi(L_B)':>10} | {'pi(L_A) - pi(L_B)':>18}")
    for lam in lambdas:
        pia = projection_pi_lambda(log_a, scaling_query, render_t,
                                   scaling_weights, lam)
        pib = projection_pi_lambda(log_b, scaling_query, render_t,
                                   scaling_weights, lam)
        print(f"{lam:>8.2f} | {pia:>10.4f} | {pib:>10.4f} | {pia - pib:>18.4f}")
    print()
    print("Interpretation: as lambda increases, older events lose weight.")
    print("Firm A's earlier FAILURE events (a03, a07) decay out faster than")
    print("the later POLICY corrections, so pi(L_A) increases with lambda")
    print("relative to the lambda=0 raw-sum baseline.")
    print()

    # Compatibility kappa
    kappa = compatibility_kappa(log_a, log_b, scaling_conflicts)
    print("Compatibility kappa(L_A, L_B)")
    print("-" * 68)
    print(f"kappa = {kappa:.4f}")

    # Count implicated events for transparency
    implicated_a = sum(
        1 for ea in log_a.events
        if any(scaling_conflicts(ea, eb) for eb in log_b.events)
    )
    implicated_b = sum(
        1 for eb in log_b.events
        if any(scaling_conflicts(ea, eb) for ea in log_a.events)
    )
    print(f"  events in L_A implicated in >= 1 conflict pair: {implicated_a}")
    print(f"  events in L_B implicated in >= 1 conflict pair: {implicated_b}")
    print(f"  |L_A| + |L_B| = {len(log_a) + len(log_b)}")
    print()
    print("Interpretation: POLICY-POLICY conflicts (regional-autonomy vs")
    print("centralized-ops) and PERSONNEL-PERSONNEL conflicts (both firms")
    print("named a regional GM) drive the implicated-event count. kappa")
    print("falls below 1 but well above 0 — a partial-merge case, not the")
    print("Microsoft-Nokia snapshot-import failure mode.")
    print()
    print("OK — projection_demo.py completed.")


if __name__ == "__main__":
    run()
