#!/usr/bin/env python3
"""S5 FULL-DRAW separated coding runner — 3-of-4 per-construct rotation.

Registered-before-data harness (FULL_DRAW_PREREGISTRATION.md §4; PREREGISTRATION_V2.md
Amendment 2.D). Codes the N=350 deals' SEPARATED-FROM-THE-START sub-dossiers under the
pre-registered 3-of-4 rotation (full_draw_rotation.json): for each case-slot the STRUCTURAL
construct is coded by a 3-model triple and the OUTCOME construct by a DIFFERENT 3-model
triple (a different model omitted from each), so per-construct coding stays as separated as
a 4-model pool allows. The rotation is seed-fixed and committed before any coding call.

This runner REUSES the S4/pilot separated-pass harness
(research/empirical_cases_v1/recode_separated_passes.py): the pass codebooks/schemas, the
four coder backends (incl. `code_with_openai`), validation, and majority-vote-or-flag. It
differs from the pilot runner (pilot_code.py) only where the full-draw design requires:
  1. 3 rater-slots per construct (over the pilot's 2), driven by structural_triple /
     outcome_triple in full_draw_rotation.json;
  2. reliability is reported as Fleiss' kappa AND **Gwet's AC1** (prevalence-adjusted, the
     primary read for the rare outcome cell) via analyze_full_draw's kernels;
  3. the no-record outcome resolves to UNCERTAIN, not 0 (Amendment 2.D): a case whose
     outcome majority is uncertain on both pathways is marked outcome_uncertain=1 and set
     aside by analyze_full_draw, so absence-of-data never fills the no-failure cell;
  4. 3-digit case ids (P001..P350); sub-dossiers in full_draw_dossiers/.

Blinding (HARD): each coder sees only its evidence slice. Anti-fabrication (HARD): a cell a
coder cannot determine is "uncertain", never guessed. Every model call is JSONL-logged
(phase s5-fulldraw-recode).

Run (keys injected into the subprocess only via BWS):

    bws run -- uv run --with anthropic --with google-genai --with openai \\
        python research/cascade-gap-largen/full_draw_code.py

Flags:
    --only S[,S]     code only the named slots/case_ids (e.g. 1,3 or P001,P003)
    --dry-run        print the rotation wiring + slice sizes; make NO API calls
    --overwrite      re-code cases that already have output JSON
    --fill-missing   re-run only the coder(s) whose per_model entry is missing/null
    --assemble-only  skip coding; (re)assemble full_draw_dataset.csv from existing JSON
    --max-retries N  per-call attempts before a cell is recorded failed (default 3)
    --breaker N      consecutive failures on a coder -> trip it DOWN for the run (default 4)

Fault tolerance (HARD): if ANY model stops mid-run -- transient API error, timeout, or a
hard stop such as a ZERO DEPOSIT / disabled key -- the run does NOT break. A TRANSIENT
failure is retried (backoff), then recorded as a failed cell (the remaining raters still
form a majority); after --breaker consecutive failures the coder is tripped DOWN and
skipped for the rest of the run (a dead model is never hammered ~700x). A PERMANENT
zero-deposit / hard-billing stop is detected by its provider signature (HTTP 402, "credit
balance is too low", insufficient_quota, "no credits", billing-not-active, ...) and trips
the coder DOWN on the FIRST occurrence -- no wasted retries on a call that cannot succeed
until top-up. Per-case errors are isolated (one bad case is skipped, not fatal); if ALL
coders trip DOWN the loop stops and assembles partial results. Every case's output is
persisted immediately, so a stopped run is resumed with --fill-missing after the model is
topped up / re-enabled. Coder health is written to full_draw_code_out/run_state.json.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))

# Reuse the S4 separated-pass harness (codebooks, schemas, coder backends, helpers).
sys.path.insert(0, str(REPO / "research" / "empirical_cases_v1"))
import recode_separated_passes as rsp  # noqa: E402

# Pure helpers reused from the pilot runner + the full-draw analysis kernels.
from pilot_code import construct_items, pooled_fleiss  # noqa: E402
from analyze_full_draw import gwet_ac1  # noqa: E402

# Distinct provenance for the full-draw calls: own phase + own logs dir (set AFTER the
# pilot_code import, which sets the pilot phase — this overrides it for the full draw).
rsp.PHASE = "s5-fulldraw-recode"
rsp.LOGS_DIR = HERE / "logs_fulldraw"

ROTATION_FILE = HERE / "full_draw_rotation.json"
DOSSIER_DIR = HERE / "full_draw_dossiers"
OUT_DIR = HERE / "full_draw_code_out"
SELECTION_FILE = HERE / "full_draw_selection.csv"
DATASET_FILE = HERE / "full_draw_dataset.csv"

DATASET_HEADER = [
    "case_id",
    "deal",
    "stratum",
    "role",
    "matched_to",
    "gate_status",
    "gap_45",
    "gap_56",
    "gap_any",
    "gap_mitigated",
    "p4_pathway",
    "p5_pathway",
    "p45_any",
    "outcome_uncertain",
    "struct_coders",
    "outcome_coders",
    "struct_flags",
    "outcome_flags",
    "notes",
]


# --- resilience: per-coder circuit breaker ---------------------------------------------
# A 350-case run makes 2,100 calls across 4 models. If any ONE model stops (transient API
# error, timeout, or a hard stop like a zero deposit / disabled key), the run must NOT
# break: the call is retried a few times, then recorded as a failed cell (the other raters
# still produce a majority), and after a run of consecutive failures the coder is tripped
# DOWN and skipped for the rest of the run so a dead model is not hammered ~700 times.
# Recovery: top up / re-enable the model, then re-run with --fill-missing to fill its
# cells; already-coded cells are untouched (outputs are persisted per case).
DEFAULT_MAX_RETRIES = 3  # per-call attempts before recording a cell failure
DEFAULT_BREAKER = 4  # consecutive failures on a coder -> trip it DOWN for the run
RETRY_BACKOFF_S = (2.0, 8.0, 20.0)  # sleep between retries (last value repeats)

CODER_HEALTH: dict[str, dict] = {}
RUN_STATE_FILE_NAME = "run_state.json"

# A ZERO-DEPOSIT / disabled-key / hard-billing-cap condition is PERMANENT for the run:
# retrying it 3x with backoff and waiting for `breaker` consecutive failures just burns
# minutes on a call that can never succeed until the account is topped up. When we can
# positively identify such an error we trip the coder DOWN on the FIRST occurrence and
# skip its remaining ~700 calls immediately (the other raters still form a majority; the
# case outputs are persisted so `--fill-missing` fills its cells after top-up). Detection
# is by the providers' balance/billing signatures (Anthropic "credit balance is too low";
# OpenAI 402 / insufficient_quota / billing_hard_limit; xAI "no/insufficient credits";
# Gemini FAILED_PRECONDITION billing-disabled). We deliberately do NOT fail-fast on plain
# 429 rate-limit / RESOURCE_EXHAUSTED, which are transient and DO recover on retry.
_BILLING_SIGNATURES = (
    "credit balance is too low",  # Anthropic zero balance
    "insufficient_quota",  # OpenAI zero balance / exhausted paid quota
    "insufficient quota",
    "billing_hard_limit_reached",  # OpenAI hard cap
    "billing hard limit",
    "insufficient credits",  # xAI / generic
    "insufficient_credits",
    "no credits",
    "doesn't have any credits",
    "does not have any credits",
    "out of credits",
    "payment required",  # HTTP 402 text
    "billing_not_active",  # Gemini billing disabled
    "billing is not active",
    "billing account",
    "exceeded your current quota",  # OpenAI quota-exhausted phrasing
    "plan and billing",
)


def _is_permanent_billing_error(exc: Exception) -> bool:
    """True when `exc` is a hard billing / zero-deposit stop that cannot recover within
    this run (as opposed to a transient timeout / rate-limit worth retrying). Matches on
    HTTP status 402 and on the providers' balance-exhausted message signatures. Errs on
    the side of NOT fail-fast (returns False) for ambiguous 429/quota text so a transient
    rate spike never falsely kills a coder for the whole run."""
    status = getattr(exc, "status_code", None) or getattr(exc, "code", None)
    if status == 402:
        return True
    blob = f"{type(exc).__name__}: {exc}".lower()
    # A bare 429 is transient (rate limit); only treat it as permanent when the body also
    # carries an explicit quota/credit-exhaustion signature (handled by the substring scan).
    return any(sig in blob for sig in _BILLING_SIGNATURES)


def _init_health(coders) -> None:
    for c in coders:
        CODER_HEALTH.setdefault(
            c, {"ok": 0, "fail": 0, "consecutive": 0, "down": False}
        )


def all_down(coders) -> bool:
    return bool(coders) and all(CODER_HEALTH.get(c, {}).get("down") for c in coders)


def call_coder(coder, case_id, pass_name, slice_text, cfg, args) -> tuple:
    """Resilient single-coder call. Skips if the coder is already tripped DOWN; else retries
    transient failures up to args.max_retries with backoff; on exhaustion records a failure
    and, after args.breaker consecutive failures, trips the coder DOWN for the run (so a
    zero-balance / outage model is not hammered ~700x). Never raises. Returns (rec, raw).
    """
    h = CODER_HEALTH.setdefault(
        coder, {"ok": 0, "fail": 0, "consecutive": 0, "down": False}
    )
    if h["down"]:
        return None, f"[SKIPPED] {coder} tripped DOWN earlier this run"
    attempts = max(1, args.max_retries)
    last_exc = ""
    for attempt in range(1, attempts + 1):
        try:
            rec, raw = rsp.CODERS[coder](case_id, pass_name, slice_text, cfg)
            h["ok"] += 1
            h["consecutive"] = 0
            return rec, raw
        except Exception as exc:  # noqa: BLE001
            last_exc = f"{type(exc).__name__}: {exc}"
            print(
                f"    [{coder}] attempt {attempt}/{attempts} ERROR {last_exc}",
                flush=True,
            )
            # Zero-deposit / hard-billing stop is permanent for the run: stop retrying and
            # trip the coder DOWN immediately rather than burning the remaining attempts
            # (and every future call) on a request that can never succeed until top-up.
            if _is_permanent_billing_error(exc):
                h["fail"] += 1
                h["consecutive"] += 1
                if not h["down"]:
                    h["down"] = True
                    print(
                        f"    [{coder}] *** CIRCUIT BREAKER (billing): zero deposit / "
                        f"billing stop detected -> marking {coder} DOWN for the rest of "
                        f"the run immediately (no further retries). Top up + re-run with "
                        f"--fill-missing to fill its cells. ***",
                        flush=True,
                    )
                return None, f"[BILLING-STOP] {last_exc}"
            if attempt < attempts:
                time.sleep(RETRY_BACKOFF_S[min(attempt - 1, len(RETRY_BACKOFF_S) - 1)])
    h["fail"] += 1
    h["consecutive"] += 1
    if h["consecutive"] >= args.breaker and not h["down"]:
        h["down"] = True
        print(
            f"    [{coder}] *** CIRCUIT BREAKER: {h['consecutive']} consecutive failures "
            f"-> marking {coder} DOWN for the rest of the run (likely zero balance / API "
            f"outage). Top up + re-run with --fill-missing to fill its cells. ***",
            flush=True,
        )
    return None, f"[ERROR after {attempts} attempts] {last_exc}"


def write_run_state() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / RUN_STATE_FILE_NAME).write_text(
        json.dumps({"coder_health": CODER_HEALTH}, indent=2)
    )


def load_rotation() -> dict[int, dict]:
    payload = json.loads(ROTATION_FILE.read_text())
    return {r["slot"]: r for r in payload["rotation"]}


def slot_to_case(slot: int) -> str:
    return f"P{slot:03d}"


def case_to_slot(case_id: str) -> int:
    return int(case_id[1:])


def sub_dossier(case_id: str, pass_name: str) -> Path:
    return DOSSIER_DIR / f"{case_id}_{pass_name}.md"


def code_case_pass(case_id: str, pass_name: str, coders: list[str], args) -> dict:
    """One pass (struct or outcome) for one case, using the rotation's assigned triple."""
    cfg = rsp.PASS_CONFIG[pass_name]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUT_DIR / f"{case_id}_{pass_name}.json"
    dfile = sub_dossier(case_id, pass_name)

    if args.dry_run:
        chars = len(dfile.read_text(encoding="utf-8")) if dfile.exists() else "MISSING"
        print(
            f"  [{pass_name}] {case_id}: coders={coders}  file={dfile.name}  chars={chars}"
        )
        return {}

    if not dfile.exists():
        # Non-fatal: a missing sub-dossier skips this pass but never aborts the batch.
        print(
            f"  [warn] {pass_name} {case_id}: missing sub-dossier {dfile.name}; skipped"
        )
        return {}
    slice_text = dfile.read_text(encoding="utf-8")

    if out_file.exists() and not args.overwrite and not args.fill_missing:
        print(f"  [skip] {pass_name} {case_id} already coded")
        return json.loads(out_file.read_text())

    existing = {}
    if out_file.exists() and args.fill_missing:
        existing = json.loads(out_file.read_text())

    per_model = dict(existing.get("per_model", {}))
    per_model_raw = dict(existing.get("per_model_raw", {}))
    to_run = [c for c in coders if not (args.fill_missing and per_model.get(c))]
    print(f"  [{pass_name}] {case_id}: coders={coders} running={to_run}")
    for coder in to_run:
        t0 = time.time()
        rec, raw = call_coder(coder, case_id, pass_name, slice_text, cfg, args)
        per_model[coder] = rec
        per_model_raw[coder] = raw
        print(
            f"    [{coder}] {'ok' if rec else 'FAILED'} ({time.time() - t0:.1f}s)",
            flush=True,
        )

    combined = rsp.combine(per_model, cfg["cells"], coders)
    record = {
        "case_id": case_id,
        "pass": pass_name,
        "coders": coders,
        "models": {c: rsp.MODEL_IDS[c] for c in coders},
        "per_model": per_model,
        "per_model_raw": per_model_raw,
        "majority": combined["majority"],
        "flags": combined["flags"],
        "n_flags": sum(combined["flags"].values()),
    }
    out_file.write_text(json.dumps(record, indent=2, ensure_ascii=False))
    print(f"    -> {out_file.name}  ({record['n_flags']} flagged cell(s))")
    return record


def _binarize(val: str, notes: list[str], cell: str) -> int:
    if val == "1":
        return 1
    if val == "0":
        return 0
    notes.append(f"{cell}={val}->0")
    return 0


def load_selection() -> dict[str, dict]:
    if not SELECTION_FILE.exists():
        return {}
    with SELECTION_FILE.open(newline="", encoding="utf-8") as fh:
        return {r["case_id"]: r for r in csv.DictReader(fh)}


def assemble_dataset(slots: list[int]) -> int:
    sel = load_selection()
    rows = []
    for slot in slots:
        cid = slot_to_case(slot)
        sf = OUT_DIR / f"{cid}_struct.json"
        of = OUT_DIR / f"{cid}_outcome.json"
        if not sf.exists() or not of.exists():
            print(f"[warn] {cid}: missing coded output; skipped in assembly")
            continue
        s = json.loads(sf.read_text())
        o = json.loads(of.read_text())
        sm, om = s["majority"], o["majority"]
        notes: list[str] = []
        g45 = _binarize(sm.get("gap_45", "uncertain"), notes, "gap_45")
        g56 = _binarize(sm.get("gap_56", "uncertain"), notes, "gap_56")
        p4_raw = om.get("p4_pathway", "uncertain")
        p5_raw = om.get("p5_pathway", "uncertain")
        p4 = _binarize(p4_raw, notes, "p4_pathway")
        p5 = _binarize(p5_raw, notes, "p5_pathway")
        # Amendment 2.D: no-record outcome -> UNCERTAIN, not 0. If BOTH pathways are
        # uncertain (the outcome pass could not determine either from its slice), the
        # case is outcome-uncertain and set aside by analyze_full_draw.
        outcome_uncertain = (
            1 if (p4_raw == "uncertain" and p5_raw == "uncertain") else 0
        )
        meta = sel.get(cid, {})
        rows.append(
            {
                "case_id": cid,
                "deal": meta.get("deal", ""),
                "stratum": meta.get("stratum", ""),
                "role": meta.get("role", ""),
                "matched_to": meta.get("matched_to", ""),
                "gate_status": meta.get("gate_status", ""),
                "gap_45": g45,
                "gap_56": g56,
                "gap_any": 1 if (g45 == 1 or g56 == 1) else 0,
                "gap_mitigated": sm.get("gap_mitigated", "NA"),
                "p4_pathway": p4,
                "p5_pathway": p5,
                "p45_any": 1 if (p4 == 1 or p5 == 1) else 0,
                "outcome_uncertain": outcome_uncertain,
                "struct_coders": "|".join(s["coders"]),
                "outcome_coders": "|".join(o["coders"]),
                "struct_flags": "|".join(c for c, f in s.get("flags", {}).items() if f),
                "outcome_flags": "|".join(
                    c for c, f in o.get("flags", {}).items() if f
                ),
                "notes": ";".join(notes),
            }
        )
    with DATASET_FILE.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=DATASET_HEADER)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"Assembled {len(rows)} rows -> {DATASET_FILE}")
    return len(rows)


def report_reliability(struct_records: list[dict], outcome_records: list[dict]) -> None:
    """Per-construct Fleiss' kappa (3-rater) AND Gwet's AC1 (prevalence-adjusted)."""
    s_items = construct_items(struct_records, rsp.STRUCT_BINARY_CELLS)
    o_items = construct_items(outcome_records, rsp.OUTCOME_BINARY_CELLS)
    s_k, o_k = pooled_fleiss(s_items), pooled_fleiss(o_items)
    s_ac, o_ac = gwet_ac1(s_items), gwet_ac1(o_items)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "kappa_struct.json").write_text(
        json.dumps({"fleiss": s_k, "gwet_ac1": s_ac}, indent=2)
    )
    (OUT_DIR / "kappa_outcome.json").write_text(
        json.dumps({"fleiss": o_k, "gwet_ac1": o_ac}, indent=2)
    )

    def fmt(k, key):
        v = k.get(key)
        return f"{v:.3f}" if isinstance(v, float) else "n/a"

    s_flags = sum(r["n_flags"] for r in struct_records)
    o_flags = sum(r["n_flags"] for r in outcome_records)
    print("-" * 70)
    print(
        f"structural: Fleiss kappa={fmt(s_k, 'kappa')}  Gwet AC1={fmt(s_ac, 'ac1')}  "
        f"over {s_k['n_items']} rater-slot items; flagged {s_flags}"
    )
    print(
        f"outcome:    Fleiss kappa={fmt(o_k, 'kappa')}  Gwet AC1={fmt(o_ac, 'ac1')}  "
        f"over {o_k['n_items']} rater-slot items; flagged {o_flags}"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", type=str, default=None, help="slots or case_ids")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--fill-missing", action="store_true")
    ap.add_argument("--assemble-only", action="store_true")
    ap.add_argument(
        "--max-retries",
        type=int,
        default=DEFAULT_MAX_RETRIES,
        help="per-call attempts before a cell is recorded failed (resilience)",
    )
    ap.add_argument(
        "--breaker",
        type=int,
        default=DEFAULT_BREAKER,
        help="consecutive failures on a coder before it is tripped DOWN for the run",
    )
    args = ap.parse_args()

    rotation = load_rotation()
    slots = sorted(rotation)
    if args.only:
        want = set()
        for tok in args.only.split(","):
            tok = tok.strip()
            if not tok:
                continue
            want.add(case_to_slot(tok) if tok.upper().startswith("P") else int(tok))
        slots = [s for s in slots if s in want]

    if args.assemble_only:
        return 0 if assemble_dataset(slots) >= 0 else 1

    print(f"S5 full-draw rotated coding: {len(slots)} slots")
    print("Models: " + " ".join(f"{k}={v}" for k, v in rsp.MODEL_IDS.items()))
    print("=" * 70)

    _init_health(rsp.MODEL_IDS)
    struct_records, outcome_records = [], []
    for slot in slots:
        cid = slot_to_case(slot)
        rot = rotation[slot]
        # Per-case isolation: an unexpected error on one case is logged and skipped, never
        # aborts the batch (partial outputs are already persisted per case).
        try:
            s_rec = code_case_pass(
                cid, "struct", sorted(rot["structural_triple"]), args
            )
            o_rec = code_case_pass(cid, "outcome", sorted(rot["outcome_triple"]), args)
        except Exception as exc:  # noqa: BLE001
            print(
                f"[warn] {cid}: unexpected error {type(exc).__name__}: {exc}; skipped",
                flush=True,
            )
            continue
        if s_rec:
            struct_records.append(s_rec)
        if o_rec:
            outcome_records.append(o_rec)
        if not args.dry_run and all_down(list(rsp.MODEL_IDS)):
            print(
                "[abort] all coders tripped DOWN (all models unavailable / zero balance); "
                "stopping the loop and assembling partial results. Fix the models, then "
                "re-run with --fill-missing.",
                flush=True,
            )
            break

    if args.dry_run:
        print("\nDRY RUN: rotation wiring shown above; no API calls made.")
        return 0

    # Always run the reliability report + assembly, even after coder failures, so partial
    # results are usable; neither is allowed to abort the process.
    try:
        report_reliability(struct_records, outcome_records)
    except Exception as exc:  # noqa: BLE001
        print(
            f"[warn] reliability report failed: {type(exc).__name__}: {exc}", flush=True
        )
    try:
        assemble_dataset(slots)
    except Exception as exc:  # noqa: BLE001
        print(
            f"[warn] dataset assembly failed: {type(exc).__name__}: {exc}", flush=True
        )
    write_run_state()
    down = [c for c in rsp.MODEL_IDS if CODER_HEALTH.get(c, {}).get("down")]
    print("=" * 70)
    if down:
        print(
            f"NOTE: coders tripped DOWN this run: {down}. Their cells are unfilled; top up "
            f"/ re-enable and re-run with --fill-missing. Health -> {OUT_DIR / RUN_STATE_FILE_NAME}"
        )
    print(f"Outputs in {OUT_DIR}/ ; dataset {DATASET_FILE.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
