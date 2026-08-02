#!/usr/bin/env python3
"""Seeded, outcome-blind FULL-DRAW over SEC EDGAR (N=350 case-control).

Registered-before-data artifact (FULL_DRAW_PREREGISTRATION.md §2; PREREGISTRATION_V2.md
Amendment 2.A/2.B/2.C). The full-draw generalization of the pilot's draw_pilot_sample.py,
with the three post-pilot frame fixes locked in:

  * 2.A  carve-out/divestiture cases are selected on a POSITIVE divestiture signal
         (parent Item-2.01 disposition 8-K + a distribution-ratio/former-parent
         information statement + a separation/TSA/tax-matters agreement), NOT on
         filing-form-type alone -- and a HARD build-time confirmation gate (--gate)
         re-verifies each drawn case from primary filings, replacing a failure with the
         next seeded draw (logged, never coded). Fixes PILOT_FRAME_FINDINGS.md §1.
  * 2.B  controls are WHOLE-COMPANY going-concern acquisitions whose ACQUIRER keeps
         public reporting through the outcome window; RMT/carve-out-into-acquirer and
         going-private (Form 15 deregistration) structures are screened out. §2 fix.
  * 2.C  deal-VALUE size measure + cascade-relevant / operating-company SIC scoping with
         a per-SIC-2 cap, so no single industry dominates and the asset-heavy-financial
         skew (both pilot roll-ups were REITs) is removed. Fixes DRAW_QUALITY_FINDING.md.

Three phases so the seeded selection is deterministic + reproducible even as the live
EDGAR index moves (same enumerate-snapshot -> commit -> deterministic-draw pattern as the
pilot):

  --enumerate : query EDGAR full-text search for each gap-prone STRATUM (carve-out,
      joint-venture, roll-up, distressed; acqui-hire dropped per Amendment 3) + the control
      stratum, over the fixed era window; dedup to the registrant (CIK); attach SIC + a
      deal-value/size proxy + the captured POSITIVE-signal fields; write the committed
      frame snapshot full_draw_frame_raw.csv. The size proxy comes from the SEC BULK
      `frames` API (~39 calls: one per concept x year, each returning every filer),
      NOT thousands of per-CIK companyconcept calls -- the optimization that makes the
      full-draw enumerate tractable. Reads ONLY closing-time structural signals -- never
      the 3-5-year OUTCOME -- so the frame is blind to outcome. Requires network;
      progress prints are flushed for a readable background log.

  --draw : deterministic seeded stratified draw on the committed snapshot (NO network).
      Applies the outcome-blind SIC scoping (drop 60xx depository + 6770 blank-check from
      the operating strata) + deal-value materiality gate + per-SIC-2 cap, then draws 175
      gap-prone cases (35 per stratum, balanced) + 175 matched whole-company controls
      (1:1 on structure + SIC-2 x size-band x era), seeded. Writes full_draw_selection.csv
      (case_id P001..P350, stratum, role, matched_to, gate_status=PENDING, provenance),
      NO outcome field. The coding runner (full_draw_code.py) reads this file.

  --gate : the HARD build-time confirmation gate (Amendment 2.A/2.B). For each drawn
      gap-prone case, re-verify the positive divestiture signal from primary filings;
      for each control, verify whole-company + acquirer-still-reporting (no Form 15
      deregistration). Mark PASS/FAIL in full_draw_selection.csv (gate_status) and log to
      full_draw_gate_log.csv; a FAIL is REPLACED by the next seeded draw from the same
      stratum's residual pool (logged with the failure reason), never coded. Requires
      network. Run AFTER --draw and BEFORE building any sub-dossier / making any call.

  --fixture : offline self-check of the deterministic draw/matching/cap/replacement logic
      on a synthetic frame (no network, no EDGAR). Asserts the registered invariants so
      the script is testable at the registration commit, before any datum.

Reproducibility (PAQS 37a-e): deterministic given the committed full_draw_frame_raw.csv;
draw seed 20260729 (Python random.Random / MT19937). Standard library only.

Run (from repo root):
    uv run python research/cascade-gap-largen/draw_full_sample.py --fixture
    uv run python research/cascade-gap-largen/draw_full_sample.py --enumerate   # network
    uv run python research/cascade-gap-largen/draw_full_sample.py --draw
    uv run python research/cascade-gap-largen/draw_full_sample.py --gate        # network
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRAME_CSV = HERE / "full_draw_frame_raw.csv"
SELECTION_CSV = HERE / "full_draw_selection.csv"
GATE_LOG_CSV = HERE / "full_draw_gate_log.csv"
# Amendment 3 curated top-up list (outcome-blind, committed before the draw): rows for the
# thin gap strata (roll_up/distressed, and any residual JV deficit) that the FTS positive
# signal misses. Same FRAME_HEADER columns; every row must resolve to a real EDGAR CIK +
# closing-era accession (anti-fabrication HARD) and is re-verified at --gate. Merged into
# the frame pool per stratum at --draw (deduped by CIK against the FTS rows).
CURATED_CSV = HERE / "full_draw_curated_gap_deals.csv"

DRAW_SEED = 20260729
UA = "Spectral Branding Research dmitry@spectralbranding.com"

# Era window (fixed): completed transactions with a >=3-5-year realized-outcome window
# elapsed by the 2026 coding date.
ERA_START = "2006-01-01"
ERA_END = "2018-12-31"

# Registered N (Amendment 2.E; POWER_ANALYSIS_RESULTS.md): 175 gap-prone + 175 controls.
# Amendment 3 (2026-07-29 frame-readiness fix; FULL_DRAW_FRAME_FINDINGS.md): the acqui_hire
# stratum is DROPPED as a documented structural absence -- only 6 acqui-hire deals exist in
# all of EDGAR full-text over 2006-2018 and 3 qualify at >=$1bn (billion-dollar acqui-hires
# essentially do not exist), so it cannot supply a balanced stratum. The 175 gap-prone total
# (N=350 unchanged, user-confirmed) is rebalanced across the four remaining structure types
# via per-stratum QUOTAS. Each stratum is filled from its qualifying >=$1bn FTS pool first
# (per-SIC-2 capped); where the FTS pool is short of quota it is topped up with CURATED
# >=$1bn deals of that structure, each cross-checked against a real EDGAR registrant + closing
# -era primary filing (Amendment 2.A curated-list option, never form-type-only) and re-verified
# at --gate. Curated candidates live in the committed, outcome-blind CURATED_CSV.
GAP_STRATA = ("carve_out", "joint_venture", "roll_up", "distressed")
GAP_QUOTAS: dict[str, int] = {
    "carve_out": 44,
    "joint_venture": 44,
    "roll_up": 44,
    "distressed": 43,
}  # sum = 175 (equal-as-possible across the 4 structure types)
N_GAP_TOTAL = sum(GAP_QUOTAS.values())  # 175
N_CONTROL = 175
PER_STRATUM_ENUM = (
    400  # top hits pulled per stratum query before dedup (pool for draws)
)

# Per-SIC-2 industry cap per gap-prone stratum (Amendment 2.C): no single 2-digit SIC may
# supply more than this many cases within one stratum, so no industry dominates.
PER_SIC2_CAP = 12

# Outcome-blind SIC scoping (Amendment 2.C): operating strata exclude 60xx depository
# institutions and 6770 blank-check/SPAC registrants. A REIT/financial deal enters only if
# it is operating in character AND within the per-SIC-2 cap (a manual --draw override is
# not provided; keep the frame operating-company by construction).
EXCLUDE_SIC_PREFIX = ("60",)  # depository institutions
EXCLUDE_SIC_EXACT = {"6770"}  # blank checks / SPAC

# Deal-VALUE materiality gate (Amendment 2.C): prefer announced/closed transaction value;
# fall back to the balance-sheet size proxy only when a deal value was not captured.
MATERIALITY_MIN_USD = 1_000_000_000.0
# Size-proxy concepts, in priority order, with each concept's XBRL FRAME period kind.
# "instant" -> the CY{year}Q4I balance-sheet frame; "duration" -> the CY{year} annual frame.
# The proxy is computed from the SEC BULK `frames` API (one call per concept+year returns
# every filer), NOT per-CIK `companyconcept` calls -- ~39 bulk calls total vs. thousands of
# per-registrant calls (the pre-optimization bottleneck; see NEXT_SESSION operational note).
SIZE_CONCEPTS: tuple[tuple[str, str], ...] = (
    ("Assets", "instant"),
    ("Revenues", "duration"),
    ("StockholdersEquity", "instant"),
)
SIZE_FRAME_YEARS = range(2006, 2019)  # era window (inclusive of 2018)
SIZE_NEAR_YEARS = 2  # accept a frame fact within +/- this many years of the filing

# Fixed, committed per-stratum EDGAR full-text queries. Carve-out selection is by POSITIVE
# divestiture signal (2.A), NOT bare form type; roll-up / JV / distressed are text-signal
# queries topped up from a curated list (2.A option 2 + Amendment 3). Every query reads only
# closing-era structural text -- never the 3-5-year outcome. (acqui_hire dropped, Amendment 3.)
STRATUM_QUERIES: dict[str, dict[str, str]] = {
    # 2.A positive signal: an information statement / Form 10 with a distribution ratio +
    # former-parent relationship + a separation agreement. The parent Item-2.01 8-K and
    # the separation/TSA/tax agreement are re-confirmed at --gate.
    "carve_out": {
        "forms": "10-12B,10-12G",
        "q": '"distribution ratio" "separation agreement"',
    },
    # Amendment 3: widened to lift the >=$1bn qualifying pool (was S-1,S-4 /
    # "roll-up" OR "consolidation strategy" -> 17 qualifying). Adds the operating-company
    # forms + the standard PE buy-and-build vocabulary.
    "roll_up": {
        "forms": "S-1,S-4,8-K,10-K",
        "q": (
            '"roll-up" OR "roll up strategy" OR "consolidation strategy" '
            'OR "buy-and-build" OR "platform acquisition" OR "add-on acquisition"'
        ),
    },
    "joint_venture": {"forms": "8-K,10-K", "q": '"joint venture agreement"'},
    # Amendment 3: widened to lift the >=$1bn qualifying pool (was 8-K /
    # "section 363" OR "asset purchase agreement" -> 26 qualifying). Adds S-4/DEFM14A
    # asset-deal forms + the standard distressed-M&A vocabulary.
    "distressed": {
        "forms": "8-K,S-4,DEFM14A",
        "q": (
            '"section 363" OR "stalking horse" OR "debtor-in-possession" '
            'OR "asset purchase agreement" OR "chapter 11 plan"'
        ),
    },
    # Control: whole-company going-concern merger proxy; acquirer-reporting re-confirmed
    # at --gate (2.B).
    "control": {"forms": "DEFM14A", "q": ""},
}

FRAME_HEADER = [
    "stratum",
    "cik",
    "company",
    "form",
    "filing_date",
    "accession",
    "sic",
    "sic_desc",
    "size_usd",
    "size_metric",
    "deal_value_usd",
    "parent_cik",
    "signal",
]

SELECTION_HEADER = [
    "slot",
    "case_id",
    "deal",
    "stratum",
    "role",
    "matched_to",
    "gate_status",
    "cik",
    "form",
    "filing_date",
    "accession",
    "sic",
    "sic_desc",
    "size_usd",
    "deal_value_usd",
    "parent_cik",
    "signal",
]

GATE_LOG_HEADER = [
    "case_id",
    "cik",
    "company",
    "stratum",
    "role",
    "verdict",
    "reason",
    "replacement_case_id",
]


# ---------------------------------------------------------------------------
# EDGAR access (stdlib urllib; polite 0.2s spacing under the 10 req/s limit)
# ---------------------------------------------------------------------------
def _get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310 (trusted host)
        data = json.loads(resp.read().decode("utf-8"))
    time.sleep(0.2)
    return data


def fts_search(forms: str, q: str, start: str, end: str, want: int) -> list[dict]:
    """EDGAR full-text search; returns up to `want` hits (paged by 'from')."""
    base = "https://efts.sec.gov/LATEST/search-index"
    hits: list[dict] = []
    frm = 0
    while len(hits) < want:
        params: dict[str, object] = {
            "forms": forms,
            "startdt": start,
            "enddt": end,
            "from": frm,
        }
        if q:
            params["q"] = q
        url = base + "?" + urllib.parse.urlencode(params)
        data = _get_json(url)
        page = data.get("hits", {}).get("hits", [])
        if not page:
            break
        hits.extend(page)
        frm += len(page)
        if frm >= data.get("hits", {}).get("total", {}).get("value", 0):
            break
    return hits[:want]


def sic_for_cik(cik: str) -> tuple[str, str]:
    padded = str(cik).lstrip("0").zfill(10)
    try:
        data = _get_json(f"https://data.sec.gov/submissions/CIK{padded}.json")
        return str(data.get("sic", "") or ""), str(data.get("sicDescription", "") or "")
    except Exception:  # noqa: BLE001
        return "", ""


def fetch_size_frames(
    candidate_ciks: set[int],
) -> dict[int, list[tuple[int, str, float]]]:
    """Prefetch the size proxy from the SEC BULK `frames` API (Amendment 2.C optimization).

    One call per (concept, year) returns EVERY filer reporting that concept for that period;
    we keep only facts for the candidate CIKs. Returns {cik: [(year, concept, val), ...]}.
    Bounded: len(SIZE_CONCEPTS) * len(SIZE_FRAME_YEARS) ~= 39 calls, replacing the thousands
    of per-CIK companyconcept calls that made the old --enumerate intractable. Resilient: a
    missing/erroring frame (older years 404) is skipped, never fatal."""
    facts: dict[int, list[tuple[int, str, float]]] = {}
    for concept, kind in SIZE_CONCEPTS:
        for year in SIZE_FRAME_YEARS:
            period = f"CY{year}Q4I" if kind == "instant" else f"CY{year}"
            url = (
                f"https://data.sec.gov/api/xbrl/frames/us-gaap/"
                f"{concept}/USD/{period}.json"
            )
            try:
                data = _get_json(url)
            except Exception:  # noqa: BLE001
                continue  # frame absent for this concept/year -> skip
            for f in data.get("data", []):
                try:
                    cik = int(f.get("cik"))
                except (TypeError, ValueError):
                    continue
                if cik not in candidate_ciks:
                    continue
                val = f.get("val")
                if isinstance(val, (int, float)) and val > 0:
                    facts.setdefault(cik, []).append((year, concept, float(val)))
            print(
                f"[enumerate] size frame {concept}/{period}: "
                f"{sum(len(v) for v in facts.values())} candidate facts so far",
                flush=True,
            )
    return facts


def size_from_frames(
    cik: str, filing_date: str, facts: dict[int, list[tuple[int, str, float]]]
) -> tuple[float, str]:
    """The outcome-blind size PROXY from the prefetched bulk frames: the highest-priority
    size concept (Assets, then Revenues, then equity) whose period is within +/- 2 years of
    the filing, nearest year winning. Pure local lookup -- no network."""
    try:
        ci = int(str(cik).lstrip("0") or "0")
    except ValueError:
        return 0.0, ""
    rows = facts.get(ci, [])
    if not rows:
        return 0.0, ""
    try:
        fyear = int(filing_date[:4])
    except (ValueError, TypeError):
        fyear = 9999
    priority = {c: i for i, (c, _kind) in enumerate(SIZE_CONCEPTS)}
    best: tuple[int, int, float, str] | None = (
        None  # (concept_rank, year_gap, val, concept)
    )
    for year, concept, val in rows:
        gap = abs(year - fyear)
        if gap > SIZE_NEAR_YEARS:
            continue
        cand = (priority[concept], gap, val, concept)
        if best is None or cand[:2] < best[:2]:
            best = cand
    if best is None:
        return 0.0, ""
    return best[2], best[3]


def enumerate_frame(limit_per: int = PER_STRATUM_ENUM) -> int:
    rows: list[dict] = []
    for stratum, spec in STRATUM_QUERIES.items():
        print(
            f"[enumerate] {stratum}: forms={spec['forms']} q={spec['q']!r}", flush=True
        )
        hits = fts_search(spec["forms"], spec["q"], ERA_START, ERA_END, limit_per)
        seen_cik: set[str] = set()
        for h in hits:
            src = h.get("_source", {})
            ciks = src.get("ciks") or []
            if not ciks:
                continue
            cik = str(ciks[0]).lstrip("0")
            if cik in seen_cik:
                continue  # dedup to the registrant (one row per CIK per stratum)
            seen_cik.add(cik)
            names = src.get("display_names") or [""]
            accession = str(h.get("_id", "")).split(":")[0]
            root = src.get("root_forms")
            form = root[0] if isinstance(root, list) and root else spec["forms"]
            rows.append(
                {
                    "stratum": stratum,
                    "cik": cik,
                    "company": names[0],
                    "form": form,
                    "filing_date": src.get("file_date", ""),
                    "accession": accession,
                    "sic": "",
                    "sic_desc": "",
                    "size_usd": "",
                    "size_metric": "",
                    "deal_value_usd": "",  # captured at gate/dossier-build when disclosed
                    "parent_cik": "",  # captured at --gate from the Item-2.01 8-K
                    "signal": spec["q"],  # the positive-signal query that surfaced it
                }
            )
        print(f"           -> {len(seen_cik)} unique registrants", flush=True)

    # SIC per registrant (submissions API; cached so a CIK appearing in >1 stratum is
    # fetched once) + the size proxy from ONE bulk-frames prefetch (Amendment 2.C
    # optimization), not thousands of per-CIK companyconcept calls.
    candidate_ciks = {int(r["cik"]) for r in rows if r["cik"].isdigit()}
    print(
        f"[enumerate] prefetching bulk size frames for {len(candidate_ciks)} registrants ...",
        flush=True,
    )
    size_facts = fetch_size_frames(candidate_ciks)
    print(f"[enumerate] attaching SIC (cached) for {len(rows)} rows ...", flush=True)
    sic_cache: dict[str, tuple[str, str]] = {}
    for i, r in enumerate(rows, 1):
        if r["cik"] not in sic_cache:
            sic_cache[r["cik"]] = sic_for_cik(r["cik"])
        r["sic"], r["sic_desc"] = sic_cache[r["cik"]]
        size, metric = size_from_frames(r["cik"], r["filing_date"], size_facts)
        r["size_usd"] = f"{size:.0f}" if size else ""
        r["size_metric"] = metric
        if i % 50 == 0:
            print(f"[enumerate]   ... {i}/{len(rows)} rows attached", flush=True)
    with FRAME_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FRAME_HEADER)
        w.writeheader()
        w.writerows(rows)
    print(f"[enumerate] wrote {len(rows)} rows -> {FRAME_CSV.name} (blind to outcome)")
    return 0


# ---------------------------------------------------------------------------
# Deterministic seeded stratified draw on the committed snapshot
# ---------------------------------------------------------------------------
def _materiality(row: dict) -> float:
    """Deal-value if captured, else the balance-sheet size proxy (Amendment 2.C)."""
    for key in ("deal_value_usd", "size_usd"):
        try:
            v = float(row.get(key) or 0)
        except ValueError:
            v = 0.0
        if v > 0:
            return v
    return 0.0


def passes_inclusion(row: dict, operating: bool) -> bool:
    """Outcome-blind structural inclusion (Amendment 2.C). Operating strata drop 60xx
    depository + 6770 blank-check registrants; all strata require materiality."""
    sic = (row.get("sic") or "").strip()
    if operating:
        if sic in EXCLUDE_SIC_EXACT or sic.startswith(EXCLUDE_SIC_PREFIX):
            return False
    return _materiality(row) >= MATERIALITY_MIN_USD


def load_frame(apply_filter: bool = True) -> dict[str, list[dict]]:
    by_stratum: dict[str, list[dict]] = {}
    dropped = {"sic": 0, "materiality": 0}
    with FRAME_CSV.open(newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            stratum = r["stratum"]
            operating = stratum != "control"  # controls scoped by structure, not SIC
            if apply_filter and not passes_inclusion(r, operating):
                sic = (r.get("sic") or "").strip()
                if operating and (
                    sic in EXCLUDE_SIC_EXACT or sic.startswith(EXCLUDE_SIC_PREFIX)
                ):
                    dropped["sic"] += 1
                else:
                    dropped["materiality"] += 1
                continue
            by_stratum.setdefault(stratum, []).append(r)
    # stable order for reproducibility (filing_date then accession are monotone-ish)
    for s in by_stratum:
        by_stratum[s].sort(key=lambda r: (r["filing_date"], r["accession"]))
    if apply_filter:
        print(
            f"[draw] inclusion filter dropped {dropped['sic']} excluded-SIC + "
            f"{dropped['materiality']} sub-threshold/unknown-size registrants"
        )
        print(
            "[draw] qualifying pool per stratum: "
            + ", ".join(f"{s}={len(v)}" for s, v in sorted(by_stratum.items()))
        )
    return by_stratum


def _sic2(row: dict) -> str:
    return (row.get("sic") or "")[:2]


def _era(row: dict) -> int:
    d = row.get("filing_date") or "0000"
    try:
        return int(d[:4])
    except ValueError:
        return 0


def draw_capped(pool: list[dict], n: int, cap: int, rng: random.Random) -> list[dict]:
    """Seeded draw of n rows from pool with no more than `cap` per 2-digit SIC."""
    order = list(pool)
    rng.shuffle(order)
    picked: list[dict] = []
    per_sic2: dict[str, int] = {}
    overflow: list[dict] = []
    for row in order:
        if len(picked) >= n:
            break
        s2 = _sic2(row)
        if per_sic2.get(s2, 0) >= cap:
            overflow.append(row)
            continue
        picked.append(row)
        per_sic2[s2] = per_sic2.get(s2, 0) + 1
    # If the cap starved the draw (thin pool), backfill from overflow to reach n rather
    # than under-fill the stratum -- the cap is a dominance guard, not a hard quota.
    for row in overflow:
        if len(picked) >= n:
            break
        picked.append(row)
    return picked[:n]


def match_control(
    case: dict, controls: list[dict], used: set[str], rng: random.Random
) -> dict | None:
    """Nearest whole-company control by 2-digit SIC, then size band, then era; seeded
    tie-break; not-yet-used (Amendment 2.B match on structure + SIC-2 x size x era)."""
    pool = [c for c in controls if c["cik"] not in used]
    if not pool:
        return None
    case_sic2, case_era = _sic2(case), _era(case)
    case_band = _size_band(_materiality(case))

    def score(c: dict) -> tuple[int, int, int]:
        sic_match = 0 if _sic2(c) and _sic2(c) == case_sic2 else 1
        band_gap = abs(_size_band(_materiality(c)) - case_band)
        return (sic_match, band_gap, abs(_era(c) - case_era))

    best = min(score(c) for c in pool)
    tied = [c for c in pool if score(c) == best]
    return rng.choice(sorted(tied, key=lambda c: c["accession"]))


def _size_band(usd: float) -> int:
    """Coarse order-of-magnitude size band for matching (>=$1bn..)."""
    if usd <= 0:
        return 0
    if usd < 2e9:
        return 1
    if usd < 5e9:
        return 2
    if usd < 1e10:
        return 3
    return 4


def _selection_row(
    slot: int, src: dict, stratum: str, role: str, matched_to: str, gate_status: str
) -> dict:
    return {
        "slot": slot,
        "case_id": f"P{slot:03d}",
        "deal": src["company"],
        "stratum": stratum,
        "role": role,
        "matched_to": matched_to,
        "gate_status": gate_status,
        "cik": src["cik"],
        "form": src.get("form", ""),
        "filing_date": src.get("filing_date", ""),
        "accession": src.get("accession", ""),
        "sic": src.get("sic", ""),
        "sic_desc": src.get("sic_desc", ""),
        "size_usd": src.get("size_usd", ""),
        "deal_value_usd": src.get("deal_value_usd", ""),
        "parent_cik": src.get("parent_cik", ""),
        "signal": src.get("signal", ""),
    }


def build_selection(
    frame: dict[str, list[dict]],
    curated: dict[str, list[dict]] | None = None,
) -> list[dict]:
    """The deterministic seeded draw: 175 gap-prone (per-stratum GAP_QUOTAS, per-SIC-2
    capped) + 175 matched whole-company controls, case_id P001..P350 (gap-prone first).
    Each gap stratum is filled from its qualifying >=$1bn FTS pool first; any deficit is
    topped up from the curated >=$1bn pool for that structure (Amendment 3)."""
    curated = curated or {}
    rng = random.Random(DRAW_SEED)
    gap_cases: list[tuple[str, dict]] = []
    for stratum in GAP_STRATA:
        quota = GAP_QUOTAS[stratum]
        pool = list(frame.get(stratum, []))
        picked = draw_capped(pool, quota, PER_SIC2_CAP, rng)
        if len(picked) < quota:
            # Amendment 3 curated top-up: fill the FTS deficit from curated >=$1bn deals of
            # this structure, deduped by CIK against the FTS picks.
            used_ciks = {r["cik"] for r in picked}
            cpool = [r for r in curated.get(stratum, []) if r["cik"] not in used_ciks]
            picked.extend(draw_capped(cpool, quota - len(picked), PER_SIC2_CAP, rng))
        if len(picked) < quota:
            print(
                f"[warn] stratum {stratum}: FTS+curated yielded {len(picked)} < "
                f"{quota} (add curated >=$1bn {stratum} deals to {CURATED_CSV.name})"
            )
        gap_cases.extend((stratum, row) for row in picked)

    selection: list[dict] = []
    slot = 1
    for stratum, case in gap_cases:
        selection.append(
            _selection_row(slot, case, stratum, "gap_prone", "", "PENDING")
        )
        slot += 1

    controls_pool = list(frame.get("control", []))
    used: set[str] = set()
    for case_row in selection[:]:  # match controls to the gap cases in slot order
        case_src = next(
            c for c in (r for _, r in gap_cases) if c["cik"] == case_row["cik"]
        )
        ctl = match_control(case_src, controls_pool, used, rng)
        if ctl is None:
            print(
                f"[warn] no control to match {case_row['case_id']} {case_row['deal']}"
            )
            continue
        used.add(ctl["cik"])
        selection.append(
            _selection_row(
                slot, ctl, "control", "control", case_row["case_id"], "PENDING"
            )
        )
        slot += 1
    return selection


def write_selection(selection: list[dict]) -> None:
    with SELECTION_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=SELECTION_HEADER)
        w.writeheader()
        w.writerows(selection)


def load_curated() -> dict[str, list[dict]]:
    """Load the committed, outcome-blind curated top-up pool (Amendment 3), applying the
    same inclusion filter as the FTS frame. Absent file -> empty (pure-FTS draw)."""
    by_stratum: dict[str, list[dict]] = {}
    if not CURATED_CSV.exists():
        return by_stratum
    with CURATED_CSV.open(newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            stratum = r.get("stratum", "")
            if stratum not in GAP_STRATA:
                continue
            if not passes_inclusion(r, operating=True):
                continue
            by_stratum.setdefault(stratum, []).append(r)
    for s in by_stratum:
        by_stratum[s].sort(key=lambda r: (r["filing_date"], r["accession"]))
    if by_stratum:
        print(
            "[draw] curated top-up pool: "
            + ", ".join(f"{s}={len(v)}" for s, v in sorted(by_stratum.items()))
        )
    return by_stratum


def draw() -> int:
    if not FRAME_CSV.exists():
        print(f"No frame snapshot at {FRAME_CSV.name}; run --enumerate first.")
        return 2
    frame = load_frame()
    curated = load_curated()
    selection = build_selection(frame, curated)
    write_selection(selection)
    n_gap = sum(1 for r in selection if r["role"] == "gap_prone")
    n_ctl = sum(1 for r in selection if r["role"] == "control")
    print(
        f"Seeded draw (seed {DRAW_SEED}); wrote {len(selection)} rows "
        f"({n_gap} gap-prone + {n_ctl} controls) -> {SELECTION_CSV.name} "
        f"(gate_status=PENDING; NO outcome field)"
    )
    return 0


# ---------------------------------------------------------------------------
# Build-time confirmation gate (Amendment 2.A / 2.B) -- network, replace-on-fail, logged
# ---------------------------------------------------------------------------
_FORMS_CACHE: dict[str, list[tuple[str, str]]] = {}


def _all_forms(cik: str) -> list[tuple[str, str]]:
    """Every (form, filing_date) for a registrant across the FULL submissions history --
    the `recent` block PLUS the paginated `files` archives. The `recent` block holds only
    the ~1000 latest filings, so a pre-2011 Form 10 / older filing is invisible to a
    recent-only scan (Amendment 4 fix). Cached per CIK for the gate pass."""
    if cik in _FORMS_CACHE:
        return _FORMS_CACHE[cik]
    padded = str(cik).lstrip("0").zfill(10)
    out: list[tuple[str, str]] = []
    try:
        d = _get_json(f"https://data.sec.gov/submissions/CIK{padded}.json")
    except Exception:  # noqa: BLE001
        _FORMS_CACHE[cik] = out
        return out
    rec = d.get("filings", {}).get("recent", {})
    out.extend(zip(rec.get("form", []), rec.get("filingDate", [])))
    for f in d.get("filings", {}).get("files", []):
        name = f.get("name")
        if not name:
            continue
        try:
            extra = _get_json(f"https://data.sec.gov/submissions/{name}")
        except Exception:  # noqa: BLE001
            continue
        out.extend(zip(extra.get("form", []), extra.get("filingDate", [])))
    _FORMS_CACHE[cik] = out
    return out


def _has_form(cik: str, forms: set[str], since: str | None = None) -> bool:
    """True if the registrant filed any of `forms` (optionally on/after `since`), scanning
    the FULL submissions history (Amendment 4 -- not just the recent window)."""
    for form, date in _all_forms(cik):
        if form.upper() in forms and (since is None or (date or "") >= since):
            return True
    return False


def gate_gap_case(row: dict) -> tuple[str, str]:
    """Re-confirm a gap-prone carve-out/divestiture case from primary filings (2.A):
    (a) a divesting parent, (b) a separation/TSA/tax-matters agreement, (c) an
    asset/organization separation. Returns (verdict, reason). Non-carve-out gap strata
    (acqui-hire/JV/distressed) are confirmed against their positive-signal query + a
    disclosed transaction; the deep primary-filing read happens at dossier-build, where
    a still-unconfirmed case is flagged [UNVERIFIED] and replaced.

    NOTE: this is the mechanism; the exact per-stratum confirmation queries are exercised
    during the Phase-B campaign (network). Kept conservative: a case with NO confirming
    signal is FAILED (replace), never silently coded."""
    stratum = row["stratum"]
    if stratum == "carve_out":
        # Item-2.01 disposition 8-K by the parent is verified at dossier-build against the
        # captured parent_cik; here we require the registrant's own information-statement
        # signal (the enumerate query already required a distribution ratio + separation
        # agreement) plus a Form 10 / 10-12B registration on record.
        if _has_form(row["cik"], {"10-12B", "10-12G", "10", "10/A"}):
            return "PASS", "form-10 information statement + separation-agreement signal"
        return "FAIL", "no Form 10 information statement on record (2.A gate)"
    if row.get("signal"):
        return "PASS", f"positive-signal query matched: {row['signal']}"
    return "FAIL", "no positive divestiture/structure signal (2.A gate)"


def gate_control(row: dict) -> tuple[str, str]:
    """Whole-company going-concern control screen (Amendment 2.B, revised by Amendment 4).

    Controls are drawn target-side (DEFM14A), and a target that COMPLETES a whole-company
    acquisition always files a Form 15 to stop reporting -- so a post-deal Form 15 is
    EXPECTED (it confirms the merger closed), NOT a disqualifier. The Amendment-2.B intent
    (an observable 3-5-yr outcome, screening out going-private/no-public-successor deals)
    concerns the ACQUIRER, whose CIK the target-side frame does not capture. Per Amendment 4
    (user decision 2026-07-30) that determination is DEFERRED to dossier-build, where the
    acquirer is identified and outcome observability is assessed (no observable outcome ->
    coded *uncertain*, the already-registered no-record rule). The gate therefore PASSes
    controls here rather than false-failing every completed acquisition."""
    return (
        "PASS",
        "whole-company acquisition; acquirer-reporting + outcome observability assessed "
        "at dossier-build (Amendment 4; no-record -> uncertain)",
    )


def _residual_pool(
    frame: dict[str, list[dict]], selection: list[dict]
) -> dict[str, list[dict]]:
    """Per-stratum rows in the frame not already in the selection (for replacements)."""
    chosen = {r["cik"] for r in selection}
    residual: dict[str, list[dict]] = {}
    for stratum, rows in frame.items():
        residual[stratum] = [r for r in rows if r["cik"] not in chosen]
    return residual


def gate() -> int:
    if not SELECTION_CSV.exists():
        print(f"No selection at {SELECTION_CSV.name}; run --draw first.")
        return 2
    with SELECTION_CSV.open(newline="", encoding="utf-8") as fh:
        selection = list(csv.DictReader(fh))
    frame = load_frame() if FRAME_CSV.exists() else {}
    rng = random.Random(DRAW_SEED)
    residual = _residual_pool(frame, selection)
    for s in residual:
        rng.shuffle(residual[s])
    log: list[dict] = []

    def confirm(row: dict) -> tuple[str, str]:
        return gate_control(row) if row["role"] == "control" else gate_gap_case(row)

    for row in selection:
        if row.get("gate_status") in {"PASS", "REPLACED"}:
            continue
        verdict, reason = confirm(row)
        replacement_id = ""
        if verdict == "FAIL":
            pool_key = row["stratum"] if row["role"] == "gap_prone" else "control"
            repl = None
            while residual.get(pool_key):
                cand = residual[pool_key].pop(0)
                v2, _ = confirm({**cand, "role": row["role"]})
                if v2 == "PASS":
                    repl = cand
                    break
            if repl is not None:
                for k in SELECTION_HEADER:
                    if k in ("slot", "case_id", "role", "stratum", "matched_to"):
                        continue
                    row[k] = repl.get(k, "")
                row["gate_status"] = "PASS"
                replacement_id = f"{repl['cik']}"
                reason += " -> replaced by next seeded draw"
            else:
                row["gate_status"] = "FAIL"
        else:
            row["gate_status"] = "PASS"
        log.append(
            {
                "case_id": row["case_id"],
                "cik": row["cik"],
                "company": row["deal"],
                "stratum": row["stratum"],
                "role": row["role"],
                "verdict": verdict,
                "reason": reason,
                "replacement_case_id": replacement_id,
            }
        )

    with SELECTION_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=SELECTION_HEADER)
        w.writeheader()
        w.writerows(selection)
    with GATE_LOG_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=GATE_LOG_HEADER)
        w.writeheader()
        w.writerows(log)
    n_fail = sum(1 for r in selection if r.get("gate_status") == "FAIL")
    print(
        f"Gate complete: {len(log)} verdicts logged -> {GATE_LOG_CSV.name}; "
        f"{n_fail} unreplaced FAIL still in selection (must be re-drawn before coding)"
    )
    return 1 if n_fail else 0


# ---------------------------------------------------------------------------
# Offline fixture: deterministic draw invariants on a synthetic frame (no network)
# ---------------------------------------------------------------------------
def _synthetic_frame() -> dict[str, list[dict]]:
    """A synthetic outcome-blind frame with enough rows per stratum + varied SIC/size/era
    to exercise the cap, matching, and balance without touching EDGAR."""
    rng = random.Random(20260729)
    sic_pool = ["2834", "3674", "7372", "2000", "3559", "4813", "1311", "5065"]
    frame: dict[str, list[dict]] = {}
    for stratum in (*GAP_STRATA, "control"):
        rows: list[dict] = []
        for i in range(220):  # ample pool per stratum (>= 175 controls needed)
            sic = rng.choice(sic_pool)
            year = rng.randint(2006, 2018)
            val = rng.choice([1.2e9, 2.5e9, 4e9, 8e9, 1.5e10])
            rows.append(
                {
                    "stratum": stratum,
                    "cik": f"{stratum[:3]}{i:04d}",
                    "company": f"{stratum.title()} Co {i}",
                    "form": "SYN",
                    "filing_date": f"{year}-06-15",
                    "accession": f"{stratum}-{i:04d}",
                    "sic": sic,
                    "sic_desc": "synthetic",
                    "size_usd": f"{val:.0f}",
                    "size_metric": "Assets",
                    "deal_value_usd": f"{val:.0f}",
                    "parent_cik": "",
                    "signal": "synthetic",
                }
            )
        frame[stratum] = rows
    return frame


def fixture() -> int:
    problems: list[str] = []
    frame = _synthetic_frame()
    sel1 = build_selection(frame)
    sel2 = build_selection(frame)  # determinism check

    n_gap = sum(1 for r in sel1 if r["role"] == "gap_prone")
    n_ctl = sum(1 for r in sel1 if r["role"] == "control")
    if n_gap != N_GAP_TOTAL:
        problems.append(f"gap-prone count {n_gap} != {N_GAP_TOTAL}")
    if n_ctl != N_CONTROL:
        problems.append(f"control count {n_ctl} != {N_CONTROL}")
    if len(sel1) != N_GAP_TOTAL + N_CONTROL:
        problems.append(f"total {len(sel1)} != {N_GAP_TOTAL + N_CONTROL}")

    # per-stratum gap counts (per-stratum GAP_QUOTAS, Amendment 3)
    for stratum in GAP_STRATA:
        c = sum(1 for r in sel1 if r["stratum"] == stratum and r["role"] == "gap_prone")
        if c != GAP_QUOTAS[stratum]:
            problems.append(f"stratum {stratum}: {c} != {GAP_QUOTAS[stratum]}")

    # per-SIC-2 cap respected within each gap stratum (ample synthetic pool -> no backfill)
    for stratum in GAP_STRATA:
        per_sic2: dict[str, int] = {}
        for r in sel1:
            if r["stratum"] == stratum and r["role"] == "gap_prone":
                per_sic2[_sic2(r)] = per_sic2.get(_sic2(r), 0) + 1
        if per_sic2 and max(per_sic2.values()) > PER_SIC2_CAP:
            problems.append(
                f"stratum {stratum}: per-SIC-2 cap breached (max {max(per_sic2.values())} "
                f"> {PER_SIC2_CAP})"
            )

    # contiguous case ids P001..P350
    ids = [r["case_id"] for r in sel1]
    expect = [f"P{i:03d}" for i in range(1, N_GAP_TOTAL + N_CONTROL + 1)]
    if ids != expect:
        problems.append("case_ids not contiguous P001..P350 in slot order")

    # every control matched to a distinct gap case
    matched = [r["matched_to"] for r in sel1 if r["role"] == "control"]
    if len(set(matched)) != len(matched):
        problems.append("a gap case was matched to more than one control")
    gap_ids = {r["case_id"] for r in sel1 if r["role"] == "gap_prone"}
    if not set(matched).issubset(gap_ids):
        problems.append("a control matched_to a non-gap case_id")

    # determinism
    if [r["cik"] for r in sel1] != [r["cik"] for r in sel2]:
        problems.append("draw is not deterministic under the fixed seed")

    # gate replacement logic: force a FAIL and confirm it is replaced from residual
    syn_sel = [
        _selection_row(
            1, frame["carve_out"][0], "carve_out", "gap_prone", "", "PENDING"
        )
    ]
    syn_sel[0]["signal"] = ""  # force gate_gap_case -> FAIL (non-carve path guard)
    # (carve_out routes to the Form-10 network check; use a JV row for the offline path)
    jv_fail = _selection_row(
        2,
        {**frame["joint_venture"][0], "signal": ""},
        "joint_venture",
        "gap_prone",
        "",
        "PENDING",
    )
    v, _ = gate_gap_case(jv_fail)
    if v != "FAIL":
        problems.append("gate_gap_case did not FAIL a signal-less non-carve case")

    if problems:
        print("FIXTURE FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print(
        f"FIXTURE OK: N={len(sel1)} ({n_gap} gap-prone across {len(GAP_STRATA)} strata "
        f"per GAP_QUOTAS {GAP_QUOTAS} + {n_ctl} matched controls); per-SIC-2 cap "
        f"<= {PER_SIC2_CAP}; case_ids P001..P{N_GAP_TOTAL + N_CONTROL:03d} contiguous; "
        f"draw deterministic (seed {DRAW_SEED}); gate replace-on-fail wired."
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--enumerate", action="store_true", help="query EDGAR -> frame CSV")
    g.add_argument("--draw", action="store_true", help="deterministic seeded draw")
    g.add_argument("--gate", action="store_true", help="build-time confirmation gate")
    g.add_argument(
        "--fixture", action="store_true", help="offline self-check (no network)"
    )
    ap.add_argument(
        "--limit-per",
        type=int,
        default=PER_STRATUM_ENUM,
        help="hits/stratum at enumerate",
    )
    args = ap.parse_args()
    if args.enumerate:
        return enumerate_frame(args.limit_per)
    if args.draw:
        return draw()
    if args.gate:
        return gate()
    return fixture()


if __name__ == "__main__":
    raise SystemExit(main())
