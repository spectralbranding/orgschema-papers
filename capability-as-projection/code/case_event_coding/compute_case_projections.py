"""compute_case_projections.py — Compute pi_lambda projections and kappa
compatibility on the three coded case event logs.

This script reads the three CSV event logs in the same directory and
computes:

    1. pi_lambda(L, q, t) at lambda in {0.0, 0.1, 0.5} for each case's
       focal capability query, with render time t = the focal event date
       (acquisition close for Disney+Pixar and Microsoft+Nokia;
       2020-01-01 for Toyota TPS as a stable post-recall reference).

    2. kappa(L_A, L_B) compatibility between the two log halves of each
       case, using the FORMALISM v0 Section 1.3 definition:

           kappa(L_A, L_B) = 1 - |conflicts_implicated_events| /
                                  (|L_A| + |L_B|)

       Conflicts are POLICY-POLICY and PERSONNEL-PERSONNEL pairs on the
       same relevant_query domain (per METHODS_APPENDIX Section 6.1).

Reproducibility:

    Fixed RNG seed = 42 (not used — script is deterministic).
    Run command (from this directory):

        uv run python compute_case_projections.py

    No network calls, no external data. CSVs are the only inputs.

This script implements honest single-coder protocol-applied numbers, not
the gold-standard two-blind-coder-plus-adjudicator output. See the
per-case CODING_REPORT.md files for full scope caveats.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

RANDOM_SEED: int = 42

WEIGHT_BY_TYPE: dict[str, float] = {
    "DECISION": 1.0,
    "POLICY": 1.0,
    "ARTIFACT": 0.5,
    "FAILURE": -1.0,
    "PERSONNEL": 0.0,
}


@dataclass(frozen=True)
class CodedEvent:
    """A coded event row from a per-case event_log CSV."""

    event_id: str
    timestamp: datetime
    actor: str
    event_type: str
    payload: str
    caused_by: str | None
    source_level: int
    source_citation: str
    confidence: str
    relevant_query: str
    weight_sign: str


def _parse_timestamp(raw: str) -> datetime:
    """Parse a CSV timestamp, tolerating partial dates and circa ranges.

    Strategy: take the first 4-10 chars that look like ISO 8601 and
    parse with progressively coarser format strings. For ambiguous
    "1990s-2020s" style ranges, anchor at the midpoint of the first
    range component (e.g., "1990s-2020s" -> 1995-01-01).
    """
    raw = raw.strip()
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(raw[: len(fmt.replace("%Y", "0000").replace("%m", "00").replace("%d", "00"))], fmt)
        except ValueError:
            continue
    # Range like "1990s-2020s" or "1985-1995"
    if "s-" in raw or "-" in raw:
        first = raw.split("-")[0].strip().rstrip("s")
        try:
            year = int(first[:4])
            return datetime(year + 5, 1, 1)  # midpoint of the decade
        except ValueError:
            pass
    if raw.endswith("s") and raw[:-1].isdigit():
        return datetime(int(raw[:-1]) + 5, 1, 1)
    raise ValueError(f"unparseable timestamp: {raw!r}")


def load_events(csv_path: Path) -> list[CodedEvent]:
    events: list[CodedEvent] = []
    with csv_path.open("r", newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            ts = _parse_timestamp(row["timestamp"])
            events.append(
                CodedEvent(
                    event_id=row["event_id"],
                    timestamp=ts,
                    actor=row["actor"],
                    event_type=row["event_type"],
                    payload=row["payload"],
                    caused_by=row["caused_by"] or None,
                    source_level=int(row["source_level"]),
                    source_citation=row["source_citation"],
                    confidence=row["confidence"],
                    relevant_query=row["relevant_query"],
                    weight_sign=row["weight_sign"],
                )
            )
    return events


def projection_pi_lambda(
    events: list[CodedEvent],
    query_prefix: str,
    render_time: datetime,
    lam: float,
    confidence_filter: set[str] | None = None,
) -> float:
    """Compute pi_lambda over events whose relevant_query starts with
    query_prefix and confidence is in confidence_filter (default
    HIGH+MEDIUM). Time deltas are measured in years.
    """
    if confidence_filter is None:
        confidence_filter = {"HIGH", "MEDIUM"}
    total = 0.0
    seconds_per_year = 365.25 * 24 * 3600
    for e in events:
        if e.timestamp > render_time:
            continue
        if not e.relevant_query.startswith(query_prefix):
            continue
        if e.confidence not in confidence_filter:
            continue
        weight = WEIGHT_BY_TYPE.get(e.event_type, 0.0)
        dt_years = (render_time - e.timestamp).total_seconds() / seconds_per_year
        total += weight * math.exp(-lam * dt_years)
    return total


def kappa_compatibility(
    log_a: list[CodedEvent],
    log_b: list[CodedEvent],
    confidence_filter: set[str] | None = None,
) -> tuple[float, int, int, int]:
    """Compute kappa(L_A, L_B) on POLICY-POLICY and PERSONNEL-PERSONNEL
    same-domain conflicts. Returns (kappa, implicated_events,
    |L_A|, |L_B|).
    """
    if confidence_filter is None:
        confidence_filter = {"HIGH", "MEDIUM"}
    la = [e for e in log_a if e.confidence in confidence_filter]
    lb = [e for e in log_b if e.confidence in confidence_filter]
    implicated: set[str] = set()
    for ea in la:
        for eb in lb:
            if ea.relevant_query != eb.relevant_query:
                continue
            if ea.event_type == "POLICY" and eb.event_type == "POLICY":
                implicated.add(ea.event_id)
                implicated.add(eb.event_id)
            elif ea.event_type == "PERSONNEL" and eb.event_type == "PERSONNEL":
                # PERSONNEL conflicts: same role-domain at same effective date.
                # Operationalize as: same relevant_query AND timestamp within
                # 365 days (proxy for "same effective date").
                if abs((ea.timestamp - eb.timestamp).days) <= 365:
                    implicated.add(ea.event_id)
                    implicated.add(eb.event_id)
    denom = len(la) + len(lb)
    if denom == 0:
        return 1.0, 0, 0, 0
    return 1.0 - len(implicated) / denom, len(implicated), len(la), len(lb)


def confidence_distribution(events: list[CodedEvent]) -> dict[str, int]:
    out = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for e in events:
        out[e.confidence] = out.get(e.confidence, 0) + 1
    return out


def type_distribution(events: list[CodedEvent]) -> dict[str, int]:
    out: dict[str, int] = {}
    for e in events:
        out[e.event_type] = out.get(e.event_type, 0) + 1
    return out


def source_level_distribution(events: list[CodedEvent]) -> dict[int, int]:
    out: dict[int, int] = {}
    for e in events:
        out[e.source_level] = out.get(e.source_level, 0) + 1
    return out


def partition_by_prefix(events: list[CodedEvent], prefixes: tuple[str, ...]) -> dict[str, list[CodedEvent]]:
    """Partition events by event_id prefix. Useful for splitting a
    combined case CSV into L_A and L_B halves.
    """
    out: dict[str, list[CodedEvent]] = {p: [] for p in prefixes}
    for e in events:
        for p in prefixes:
            if e.event_id.startswith(p):
                out[p].append(e)
                break
    return out


def main() -> None:
    here = Path(__file__).parent

    # ---- Case 1: Disney + Pixar 2006 ----
    print("=" * 72)
    print("CASE 1: Disney + Pixar 2006")
    print("=" * 72)
    events_dp = load_events(here / "disney_pixar_2006_event_log.csv")
    parts_dp = partition_by_prefix(events_dp, ("PX", "DSN"))
    l_pixar, l_disney = parts_dp["PX"], parts_dp["DSN"]
    print(f"Total events: {len(events_dp)}")
    print(f"  L_Pixar:  {len(l_pixar)} events")
    print(f"  L_Disney: {len(l_disney)} events")
    print(f"Confidence distribution (full): {confidence_distribution(events_dp)}")
    print(f"Type distribution (full):       {type_distribution(events_dp)}")
    print(f"Source level distribution:      {source_level_distribution(events_dp)}")
    render_t_dp = datetime(2006, 5, 5)  # acquisition close
    for lam in (0.0, 0.1, 0.5):
        pi_p = projection_pi_lambda(l_pixar, "capability:creative", render_t_dp, lam)
        print(f"  pi_lambda(L_Pixar, 'creative-development', 2006-05-05, lam={lam}) = {pi_p:.3f}")
    # Restrict Pixar to pre-acquisition (PX001-PX025) for clean kappa
    l_pixar_pre = [e for e in l_pixar if e.timestamp <= datetime(2006, 1, 24)]
    l_disney_pre = [e for e in l_disney if e.timestamp <= datetime(2006, 1, 24)]
    print(f"  L_Pixar pre-acq:  {len(l_pixar_pre)} events")
    print(f"  L_Disney pre-acq: {len(l_disney_pre)} events")
    k, impl, na, nb = kappa_compatibility(l_pixar_pre, l_disney_pre)
    print(f"  kappa(L_Pixar_pre, L_Disney_pre) = {k:.3f}  ({impl} implicated events out of {na}+{nb})")

    # ---- Case 2: Microsoft + Nokia 2014 ----
    print()
    print("=" * 72)
    print("CASE 2: Microsoft + Nokia 2014")
    print("=" * 72)
    events_mn = load_events(here / "microsoft_nokia_2014_event_log.csv")
    parts_mn = partition_by_prefix(events_mn, ("NOK", "MSF"))
    l_nokia, l_ms = parts_mn["NOK"], parts_mn["MSF"]
    print(f"Total events: {len(events_mn)}")
    print(f"  L_Nokia:     {len(l_nokia)} events")
    print(f"  L_Microsoft: {len(l_ms)} events")
    print(f"Confidence distribution (full): {confidence_distribution(events_mn)}")
    print(f"Type distribution (full):       {type_distribution(events_mn)}")
    print(f"Source level distribution:      {source_level_distribution(events_mn)}")
    render_t_mn = datetime(2014, 4, 25)  # acquisition close
    for lam in (0.0, 0.1, 0.5):
        pi_n = projection_pi_lambda(l_nokia, "capability:mobile-platform", render_t_mn, lam)
        print(f"  pi_lambda(L_Nokia, 'mobile-platform-development', 2014-04-25, lam={lam}) = {pi_n:.3f}")
    # Pre-acquisition kappa
    l_nokia_pre = [e for e in l_nokia if e.timestamp <= datetime(2013, 9, 3)]
    l_ms_pre = [e for e in l_ms if e.timestamp <= datetime(2013, 9, 3)]
    print(f"  L_Nokia pre-acq:     {len(l_nokia_pre)} events")
    print(f"  L_Microsoft pre-acq: {len(l_ms_pre)} events")
    k, impl, na, nb = kappa_compatibility(l_nokia_pre, l_ms_pre)
    print(f"  kappa(L_Nokia_pre, L_MS_pre) = {k:.3f}  ({impl} implicated events out of {na}+{nb})")

    # ---- Case 3: Toyota TPS ----
    print()
    print("=" * 72)
    print("CASE 3: Toyota TPS vs Stylized Imitator")
    print("=" * 72)
    events_tt = load_events(here / "toyota_tps_event_log.csv")
    parts_tt = partition_by_prefix(events_tt, ("TOY", "IMI"))
    l_toyota, l_imi = parts_tt["TOY"], parts_tt["IMI"]
    print(f"Total events: {len(events_tt)}")
    print(f"  L_Toyota:   {len(l_toyota)} events")
    print(f"  L_Imitator: {len(l_imi)} events")
    print(f"Confidence distribution (full): {confidence_distribution(events_tt)}")
    print(f"Type distribution (full):       {type_distribution(events_tt)}")
    print(f"Source level distribution:      {source_level_distribution(events_tt)}")
    render_t_tt = datetime(2020, 1, 1)
    for lam in (0.0, 0.1, 0.5):
        pi_t = projection_pi_lambda(l_toyota, "capability:production-system", render_t_tt, lam)
        pi_i = projection_pi_lambda(l_imi, "capability:production-system", render_t_tt, lam)
        print(f"  pi_lambda(L_Toyota,   'production-system', 2020-01-01, lam={lam}) = {pi_t:.3f}")
        print(f"  pi_lambda(L_Imitator, 'production-system', 2020-01-01, lam={lam}) = {pi_i:.3f}")
    # kappa-equivalent (cross-domain, treated as POLICY/POLICY conflict on
    # production-system domain even though imitator events live under
    # capability:production-system-imitation -- override by query family).
    # Use loose query match for this case:
    impl: set[str] = set()
    for ea in l_toyota:
        if ea.confidence not in {"HIGH", "MEDIUM"}:
            continue
        for eb in l_imi:
            if eb.confidence not in {"HIGH", "MEDIUM"}:
                continue
            ea_family = ea.relevant_query.split("-imitation")[0]
            eb_family = eb.relevant_query.split("-imitation")[0]
            if ea_family != eb_family:
                continue
            if ea.event_type == "POLICY" and eb.event_type in {"POLICY", "FAILURE"}:
                impl.add(ea.event_id)
                impl.add(eb.event_id)
    la_hm = [e for e in l_toyota if e.confidence in {"HIGH", "MEDIUM"}]
    lb_hm = [e for e in l_imi if e.confidence in {"HIGH", "MEDIUM"}]
    denom = len(la_hm) + len(lb_hm)
    k_tt = 1.0 - len(impl) / denom if denom else 1.0
    print(f"  kappa-equivalent(L_Toyota, L_Imitator) = {k_tt:.3f}  ({len(impl)} implicated events out of {len(la_hm)}+{len(lb_hm)})")


if __name__ == "__main__":
    main()
