#!/usr/bin/env python3
"""S5 pilot separated coding runner — 4-coder disjoint-pair rotation.

Registered-before-data harness (PILOT_PREREGISTRATION.md §4, v1.2.0). Codes the 10
pilot deals' SEPARATED-FROM-THE-START sub-dossiers under the pre-registered disjoint-
pair rotation (pilot_rotation.json): for each case-slot the STRUCTURAL construct (the
gap) is coded by one disjoint pair of models and the OUTCOME construct (the pathway)
by the other pair, so no model codes both constructs for the same case. Which pair
does which is fixed by the seed in pilot_rotation.json (committed before any coding
call); across the 10 slots every model codes each construct 5x (balanced).

This runner REUSES the S4 separated-pass harness
(research/empirical_cases_v1/recode_separated_passes.py): the pass codebooks/schemas
(STRUCT_*, OUTCOME_*), the four coder backends (incl. the new `code_with_openai`),
validation, and majority-vote-or-flag. It differs from the S4 harness in two ways
required by the pilot design:
  1. dossiers are two SEPARATE files per case (built separated-from-the-start from
     primary filings), not slices of one pooled dossier -- so the structural pass
     reads P<nn>_struct.md and the outcome pass reads P<nn>_outcome.md directly;
  2. the coders for each pass come from the per-slot rotation, not a fixed triple, so
     each construct is coded by exactly 2 rater-slots (agree-or-flag) and per-construct
     Fleiss' kappa is pooled over 2 rater-slots (PILOT_PREREGISTRATION.md §4/§6).

Case-slot <-> file convention: slot i (1..10) is case_id P0i; its sub-dossiers are
pilot_dossiers/P0i_struct.md and pilot_dossiers/P0i_outcome.md. The rotation is keyed
by slot, so slot i's pairs code case P0i.

Blinding (HARD): each coder sees only its evidence slice -- never the hypotheses, the
predicted direction, or the case-vs-control status. Anti-fabrication (HARD): a cell a
coder cannot determine from its slice is "uncertain", never guessed. Every model call
is JSONL-logged (phase s5-pilot-recode) via the corpus llm_call_logger.

Run (keys injected into the subprocess only via BWS):

    bws run -- uv run --with anthropic --with google-genai --with openai \\
        python research/cascade-gap-largen/pilot_code.py

Flags:
    --only S[,S]     code only the named slots/case_ids (e.g. 1,3 or P01,P03)
    --dry-run        print the rotation wiring + slice sizes; make NO API calls
    --overwrite      re-code cases that already have output JSON
    --fill-missing   re-run only the coder(s) whose per_model entry is missing/null
    --assemble-only  skip coding; (re)assemble pilot_dataset.csv from existing JSON
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

# Reuse the S4 separated-pass harness (codebooks, schemas, coder backends, helpers).
sys.path.insert(0, str(REPO / "research" / "empirical_cases_v1"))
import recode_separated_passes as rsp  # noqa: E402

# Distinct provenance for the pilot calls: own phase + own logs dir.
rsp.PHASE = "s5-pilot-recode"
rsp.LOGS_DIR = HERE / "logs"

ROTATION_FILE = HERE / "pilot_rotation.json"
DOSSIER_DIR = HERE / "pilot_dossiers"
OUT_DIR = HERE / "pilot_code_out"
SELECTION_FILE = HERE / "pilot_selection.csv"
DATASET_FILE = HERE / "pilot_dataset.csv"

DATASET_HEADER = [
    "case_id",
    "deal",
    "stratum",
    "role",
    "matched_to",
    "gap_45",
    "p4_pathway",
    "gap_56",
    "p5_pathway",
    "gap_any",
    "p45_any",
    "gap_mitigated",
    "struct_coder",
    "outcome_coder",
    "struct_flags",
    "outcome_flags",
    "notes",
]


def load_rotation() -> dict[int, dict]:
    payload = json.loads(ROTATION_FILE.read_text())
    return {r["slot"]: r for r in payload["rotation"]}


def slot_to_case(slot: int) -> str:
    return f"P{slot:02d}"


def case_to_slot(case_id: str) -> int:
    return int(case_id[1:])


def sub_dossier(case_id: str, pass_name: str) -> Path:
    return DOSSIER_DIR / f"{case_id}_{pass_name}.md"


# ---------------------------------------------------------------------------
# Pooled 2-rater Fleiss' kappa (raters differ per item under rotation; only the
# NUMBER of raters per item is fixed at 2, which is all Fleiss' kappa requires).
# ---------------------------------------------------------------------------
def pooled_fleiss(items: list[list[int]]) -> dict:
    """items: per (case, cell) category-count rows [n0, n1, n_uncertain], each row
    summing to the fixed number of raters (2). Pools all rows for one construct."""
    n_items = len(items)
    if n_items == 0:
        return {"kappa": None, "n_items": 0, "n_raters": 0}
    n_raters = sum(items[0])
    if n_raters < 2 or any(sum(row) != n_raters for row in items):
        return {"kappa": None, "n_items": n_items, "n_raters": n_raters}
    totals = [sum(row[c] for row in items) for c in range(3)]
    grand = sum(totals)
    p_j = [t / grand for t in totals]
    P_i = [sum(n * (n - 1) for n in row) / (n_raters * (n_raters - 1)) for row in items]
    P_bar = sum(P_i) / n_items
    P_e = sum(p * p for p in p_j)
    kappa = (P_bar - P_e) / (1 - P_e) if (1 - P_e) != 0 else None
    return {
        "kappa": kappa,
        "n_items": n_items,
        "n_raters": n_raters,
        "P_bar": P_bar,
        "P_e": P_e,
        "category_proportions": dict(zip(["0", "1", "uncertain"], p_j)),
    }


def construct_items(records: list[dict], binary_cells: list[str]) -> list[list[int]]:
    cats = ["0", "1", "uncertain"]
    items: list[list[int]] = []
    for rec in records:
        pm = rec["per_model"]
        coders = rec["coders"]
        for cell in binary_cells:
            row = [0, 0, 0]
            n_rated = 0
            for m in coders:
                val = (pm.get(m) or {}).get(cell)
                if val in cats:
                    row[cats.index(val)] += 1
                    n_rated += 1
            if n_rated == len(coders):
                items.append(row)
    return items


# ---------------------------------------------------------------------------
# One pass (struct or outcome) for one case, using the rotation's assigned pair.
# ---------------------------------------------------------------------------
def code_case_pass(case_id: str, pass_name: str, coders: list[str], args) -> dict:
    cfg = rsp.PASS_CONFIG[pass_name]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUT_DIR / f"{case_id}_{pass_name}.json"
    dfile = sub_dossier(case_id, pass_name)

    if args.dry_run:
        chars = len(dfile.read_text(encoding="utf-8")) if dfile.exists() else "MISSING"
        print(
            f"  [{pass_name}] {case_id}: coders={coders}  "
            f"file={dfile.name}  chars={chars}"
        )
        return {}

    if not dfile.exists():
        raise FileNotFoundError(f"missing sub-dossier {dfile}")
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
        try:
            rec, raw = rsp.CODERS[coder](case_id, pass_name, slice_text, cfg)
        except Exception as exc:  # noqa: BLE001
            print(f"    [{coder}] ERROR {type(exc).__name__}: {exc}")
            rec, raw = None, f"[ERROR] {type(exc).__name__}: {exc}"
        per_model[coder] = rec
        per_model_raw[coder] = raw
        print(f"    [{coder}] {'ok' if rec else 'FAILED'} ({time.time()-t0:.1f}s)")

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


# ---------------------------------------------------------------------------
# Assembly: per-case struct+outcome JSON -> pilot_dataset.csv (+ selection meta).
# ---------------------------------------------------------------------------
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
        p4 = _binarize(om.get("p4_pathway", "uncertain"), notes, "p4_pathway")
        p5 = _binarize(om.get("p5_pathway", "uncertain"), notes, "p5_pathway")
        meta = sel.get(cid, {})
        rows.append(
            {
                "case_id": cid,
                "deal": meta.get("deal", ""),
                "stratum": meta.get("stratum", ""),
                "role": meta.get("role", ""),
                "matched_to": meta.get("matched_to", ""),
                "gap_45": g45,
                "p4_pathway": p4,
                "gap_56": g56,
                "p5_pathway": p5,
                "gap_any": 1 if (g45 == 1 or g56 == 1) else 0,
                "p45_any": 1 if (p4 == 1 or p5 == 1) else 0,
                "gap_mitigated": sm.get("gap_mitigated", "NA"),
                "struct_coder": "|".join(s["coders"]),
                "outcome_coder": "|".join(o["coders"]),
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


# ---------------------------------------------------------------------------
def report_kappa(struct_records: list[dict], outcome_records: list[dict]) -> None:
    s_items = construct_items(struct_records, rsp.STRUCT_BINARY_CELLS)
    o_items = construct_items(outcome_records, rsp.OUTCOME_BINARY_CELLS)
    s_k = pooled_fleiss(s_items)
    o_k = pooled_fleiss(o_items)
    (OUT_DIR / "kappa_struct.json").write_text(json.dumps({"fleiss": s_k}, indent=2))
    (OUT_DIR / "kappa_outcome.json").write_text(json.dumps({"fleiss": o_k}, indent=2))

    def fmt(k):
        return f"{k['kappa']:.3f}" if isinstance(k.get("kappa"), float) else "n/a"

    s_flags = sum(r["n_flags"] for r in struct_records)
    o_flags = sum(r["n_flags"] for r in outcome_records)
    print("-" * 70)
    print(
        f"structural pooled 2-rater Fleiss' kappa ({'/'.join(rsp.STRUCT_BINARY_CELLS)})"
        f" = {fmt(s_k)} over {s_k['n_items']} rater-slot items; flagged cells {s_flags}"
    )
    print(
        f"outcome pooled 2-rater Fleiss' kappa ({'/'.join(rsp.OUTCOME_BINARY_CELLS)})"
        f" = {fmt(o_k)} over {o_k['n_items']} rater-slot items; flagged cells {o_flags}"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", type=str, default=None, help="slots or case_ids")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--fill-missing", action="store_true")
    ap.add_argument("--assemble-only", action="store_true")
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

    print(f"S5 pilot rotated coding: slots={slots}")
    print("Models: " + " ".join(f"{k}={v}" for k, v in rsp.MODEL_IDS.items()))
    print("=" * 70)

    struct_records, outcome_records = [], []
    for slot in slots:
        cid = slot_to_case(slot)
        rot = rotation[slot]
        s_rec = code_case_pass(cid, "struct", sorted(rot["structural_pair"]), args)
        o_rec = code_case_pass(cid, "outcome", sorted(rot["outcome_pair"]), args)
        if s_rec:
            struct_records.append(s_rec)
        if o_rec:
            outcome_records.append(o_rec)

    if args.dry_run:
        print("\nDRY RUN: rotation wiring shown above; no API calls made.")
        return 0

    report_kappa(struct_records, outcome_records)
    assemble_dataset(slots)
    print("=" * 70)
    print(f"Outputs in {OUT_DIR}/ ; dataset {DATASET_FILE.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
