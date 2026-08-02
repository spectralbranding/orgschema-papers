#!/usr/bin/env python3
"""Triple-coding harness for the Tier-Bundle Algebra n=30 empirical pass.

Implements the coding phase locked in CASE_CODING_PROTOCOL.md sec.3 and
PREREGISTRATION_V1.md sec.3 (with Amendments 3-4). For EACH evidence dossier in
`dossiers/` it runs THREE independent AI coders -- Claude (Anthropic), Gemini
(google-genai), Grok (xAI, openai-compatible) -- each of which sees ONLY the
dossier text, never the paper, the pre-registration, the hypotheses, the
predicted direction, or the anchor-vs-extension status of the case. This
dossier-driven (not algebra-driven) framing is the anti-confirmation-bias design
(CASE_CODING_PROTOCOL.md sec.5, "Coding-bias risk").

Per cell the three coders are combined by MAJORITY-VOTE-OR-FLAG: >=2 agree ->
majority value; otherwise FLAG for author adjudication. A coder that cannot
determine a cell from the dossier must return "uncertain" (anti-fabrication HARD
rule) -- it is never guessed.

Every model call is logged as JSONL via the corpus llm_call_logger
(feedback_llm_call_professional_logging: this coding is an EXPERIMENT whose codes
land in the paper's Results, so the calls are public-logged). Logs ->
`research/empirical_cases_v1/logs/`.

Outputs:
  - coding_raw/<case_id>_codes.json  (per-model codes + majority + per-cell flags)
  - coding_raw/fleiss_kappa.json     (inter-rater reliability, all binary cells)
  - coding_raw/fleiss_kappa.png      (inter-rater figure)

BLINDING / registered-before-data discipline: this harness (and the empty
coded-dataset schema) is committed BEFORE any coded datum exists. The coder prompt
below withholds all hypothesis content; it operationalizes the structural
constructs (bundle signature, tier-transfer gaps, failure-pathway incidence) in
neutral factual language grounded in the dossier's own section structure.

Run (all three coders; injects BWS keys ANTHROPIC_API_KEY / GOOGLE_API_KEY_FreeTier
/ GROK_API_KEY into the subprocess only, never the ambient shell):

    bws run -- uv run --with anthropic --with google-genai --with openai \\
        --with matplotlib python research/empirical_cases_v1/triple_code_dossiers.py

Flags:
    --limit N        code only the first N dossiers (smoke test)
    --only ID[,ID]   code only the named case_ids (e.g. A01,E03)
    --coders LIST    subset of {claude,gemini,grok} (default all three)
    --dry-run        print what would be coded; make no API calls
    --overwrite      re-code cases that already have a coding_raw/*.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
DOSSIER_DIR = HERE / "dossiers"
OUT_DIR = HERE / "coding_raw"
LOGS_DIR = HERE / "logs"

# Corpus LLM-call logger (llm_call_logger.py).
sys.path.insert(0, str(REPO / "research" / "code"))
from llm_call_logger import log_call  # noqa: E402

# ---------------------------------------------------------------------------
# Model pins (recorded so each coded datum's provenance is exact).
# ---------------------------------------------------------------------------
CLAUDE_MODEL = "claude-opus-4-8"
GEMINI_MODEL = "gemini-3.1-pro-preview"  # NOT gemini-3.1-pro (404s)
GROK_MODEL = "grok-4.3"

# ---------------------------------------------------------------------------
# Coding schema. One structured record per case. The cell keys the analysis
# pipeline consumes are gap_45, p4_pathway, gap_56, p5_pathway (+ gap_mitigated);
# the remaining fields carry the full class A-E record for the descriptive layer.
# ---------------------------------------------------------------------------
SIGMA_ALPHABET = [
    "1-1",
    "N-1",
    "1-N",
    "subset",
    "partial",
    "read-only",
    "swap",
    "terminate",
    "null",
]
T1_ALPHABET = [
    "replace",
    "imprint-share",
    "continue",
    "terminate",
    "reconstruct",
    "replicate",
    "mutual-replace",
]
COLLAPSE_STATES = ["none", "T1=T4", "T1=T3", "T1=T3=T4", "T1=T2", "T1=T6"]
TRISTATE = ["0", "1", "uncertain"]
MITIGATED = ["yes", "no", "NA"]

# Binary cells over which inter-rater reliability (Fleiss kappa) is computed.
BINARY_CELLS = [
    "gap_45",
    "gap_56",
    "p4_pathway",
    "p5_pathway",
    "t1_archetype",
    "t2_model",
]

CODING_TOOL_SCHEMA: dict = {
    "type": "object",
    "required": [
        "sigma_T1",
        "sigma_T2",
        "sigma_T3",
        "sigma_T4",
        "sigma_T5",
        "sigma_T6",
        "collapse_state",
        "gap_45",
        "gap_56",
        "p4_pathway",
        "p5_pathway",
        "t1_archetype",
        "t2_model",
        "gap_mitigated",
        "performance_metric",
        "rationale",
    ],
    "properties": {
        "sigma_T1": {"type": "string", "enum": T1_ALPHABET + ["uncertain"]},
        "sigma_T2": {"type": "string", "enum": SIGMA_ALPHABET + ["uncertain"]},
        "sigma_T3": {"type": "string", "enum": SIGMA_ALPHABET + ["uncertain"]},
        "sigma_T4": {"type": "string", "enum": SIGMA_ALPHABET + ["uncertain"]},
        "sigma_T5": {"type": "string", "enum": SIGMA_ALPHABET + ["uncertain"]},
        "sigma_T6": {"type": "string", "enum": SIGMA_ALPHABET + ["uncertain"]},
        "collapse_state": {"type": "string", "enum": COLLAPSE_STATES + ["uncertain"]},
        "gap_45": {"type": "string", "enum": TRISTATE},
        "gap_56": {"type": "string", "enum": TRISTATE},
        "p4_pathway": {"type": "string", "enum": TRISTATE},
        "p5_pathway": {"type": "string", "enum": TRISTATE},
        "t1_archetype": {"type": "string", "enum": TRISTATE},
        "t2_model": {"type": "string", "enum": TRISTATE},
        "gap_mitigated": {"type": "string", "enum": MITIGATED},
        "performance_metric": {"type": "string"},
        "rationale": {"type": "string"},
    },
}

CODEBOOK = f"""\
You are a careful, neutral coder of a corporate-transaction case. You are given ONE
evidence dossier assembled from public primary sources (SEC filings, company
releases, reputable press). Read ONLY that dossier. Do not use outside knowledge of
the case; code strictly what the dossier documents. If the dossier does not let you
determine a field, you MUST say so with the "uncertain" value -- never guess, never
infer from what you personally recall about the companies.

You will emit a single structured record with these fields.

A. BUNDLE SIGNATURE -- for each of six organizational tiers, classify what happened
to that tier when the transaction crossed the ownership boundary. Use exactly one
label per tier from the controlled vocabulary.
  Tiers (dossier section 2 has one line each):
    T1 Owner Intent  -- the controlling principal / imprint.
       Labels: {", ".join(T1_ALPHABET)}, uncertain.
         replace = old controlling intent exited, a new one installed;
         imprint-share = both principals' intent co-present;
         continue = same controlling intent persists;
         terminate = the controlling intent ended with no successor;
         reconstruct = intent re-formed into a new (often non-commercial) purpose;
         replicate = intent copied into a standardized template (e.g. franchising);
         mutual-replace = two intents fused into a jointly-new one (merger of equals).
    T2 Business Model, T3 Business Entity (legal vehicle), T4 Product
       (customer-acceptance layer), T5 Process (operations), T6 Organization
       (people/culture).
       Labels for T2-T6: {", ".join(SIGMA_ALPHABET)}, uncertain.
         1-1 = transferred whole, one-to-one; N-1 = many collapsed into one;
         1-N = one split into many; subset = only part transferred;
         partial = transferred but incompletely / with friction;
         read-only = licensed / accessed without ownership transfer;
         swap = exchanged for a different one (e.g. new legal domicile);
         terminate = ended; null = not applicable / nothing at this tier.

B. TIER-TRANSFER GAPS -- code strictly from the STRUCTURE OF THE DEAL AT CLOSING
(dossier section 2), independent of any later outcome:
  gap_45: Did the customer-facing product/asset (T4, what customers buy) cross the
    ownership boundary WITHOUT the operational processes that produce or deliver it
    (T5) transferring or being aligned coherently alongside it? A documented
    product-vs-process structural mismatch at closing. 1 = yes such a gap; 0 = no
    (product and its processes moved together, or neither moved); uncertain.
  gap_56: Did the operational processes (T5) transfer or get re-engineered WITHOUT
    the organization / people / management / culture that run them (T6) transferring
    or aligning coherently alongside? A documented process-vs-organization structural
    mismatch at closing. 1 = yes; 0 = no; uncertain.

C. FAILURE-PATHWAY INCIDENCE -- code strictly from the DOCUMENTED OUTCOME at the
3-5 year horizon (dossier sections 3-4), independent of the deal structure:
  p4_pathway: Is there documented disruption specifically at the product/process
    interface (the acquired product could not be aligned with the operating
    processes; product-line/operations incoherence)? 1 = yes; 0 = no / none
    documented; uncertain.
  p5_pathway: Is there documented fracture specifically at the process/organization
    interface (operations vs people/management/culture; integration of operations
    broke against the organization)? 1 = yes; 0 = no / none documented; uncertain.
  t1_archetype: Is there documented incoherence in the controlling-intent archetype
    itself (e.g. an announced "merger of equals" executed as one-sided dominance)?
    This is a channel SEPARATE from B/C above. 1 = yes; 0 = no; uncertain.
  t2_model: Is there documented incompatibility of the two business models
    (value-capture logics that could not be reconciled)? A channel SEPARATE from B/C.
    1 = yes; 0 = no; uncertain.

  gap_mitigated: If (and only if) you coded a structural gap in B, was that gap
    documented as contractually absorbed at closing via a transitional-services or
    operating agreement allocating the shared substrate? yes / no / NA (NA if you
    coded no gap in B).

D. performance_metric: the single best-documented post-deal outcome scalar in the
   dossier (e.g. "divested 80.1% after ~108 months", "~$99bn goodwill write-down",
   "no divestiture; assets retained"). One short phrase. If none, "not documented".

E. collapse_state: Any Tier-1 fusion documented? none / T1=T4 (founder identity IS
   the product) / T1=T3 (the legal subject IS a specific natural person) / T1=T3=T4 /
   T1=T2 / T1=T6 / uncertain.

rationale: 2-4 sentences citing the dossier lines that drove your gap_45, gap_56,
p4_pathway, and p5_pathway codes specifically.

Emit ONLY the structured record. Code conservatively: absence of evidence for a
pathway is coded 0 (not-documented), and inability to determine a structural field
is coded "uncertain".
"""


# ---------------------------------------------------------------------------
# Dossier discovery
# ---------------------------------------------------------------------------
def discover_dossiers() -> list[tuple[str, str, Path]]:
    """Return sorted [(case_id, case_name, path)] for A*/E* dossiers."""
    out = []
    for p in sorted(DOSSIER_DIR.glob("*.md")):
        if p.name == "DOSSIER_TEMPLATE.md":
            continue
        m = re.match(r"^([AE]\d{2})_", p.name)
        if not m:
            continue
        case_id = m.group(1)
        text = p.read_text(encoding="utf-8")
        name_m = re.search(
            r"^#\s*Evidence dossier\s*[—-]\s*(.+?)\s*$", text, re.MULTILINE
        )
        case_name = name_m.group(1) if name_m else p.stem
        out.append((case_id, case_name, p))
    return out


# ---------------------------------------------------------------------------
# Validation of a returned coder record
# ---------------------------------------------------------------------------
def validate_record(rec: dict) -> dict:
    """Coerce/validate a coder record to the schema; unknown -> uncertain."""
    props = CODING_TOOL_SCHEMA["properties"]
    clean: dict = {}
    for key, spec in props.items():
        val = rec.get(key)
        if key in ("performance_metric", "rationale"):
            clean[key] = str(val) if val is not None else ""
            continue
        allowed = spec["enum"]
        sval = str(val).strip() if val is not None else ""
        # Normalize common variants.
        sval = sval.replace("≡", "=")  # unicode identity sign
        if key.startswith("gap_") and key != "gap_mitigated":
            sval = {"true": "1", "false": "0", "yes": "1", "no": "0"}.get(
                sval.lower(), sval
            )
        if key in ("p4_pathway", "p5_pathway", "t1_archetype", "t2_model"):
            sval = {"true": "1", "false": "0", "yes": "1", "no": "0"}.get(
                sval.lower(), sval
            )
        if sval in allowed:
            clean[key] = sval
        elif "uncertain" in allowed:
            clean[key] = "uncertain"
        elif key == "gap_mitigated":
            clean[key] = "NA"
        else:
            clean[key] = allowed[0]
    return clean


def build_user_prompt(dossier_text: str) -> str:
    return (
        "Here is the evidence dossier. Read it and emit the structured coding "
        "record.\n\n[DOSSIER BEGIN]\n" + dossier_text + "\n[DOSSIER END]\n"
    )


# ---------------------------------------------------------------------------
# Coder backends. Each returns (validated_record | None, raw_text).
# ---------------------------------------------------------------------------
def code_with_claude(case_id: str, dossier_text: str) -> tuple[dict | None, str]:
    import anthropic

    client = anthropic.Anthropic()
    tool = {
        "name": "emit_case_coding",
        "description": "Emit the structured coding record for one transaction case.",
        "input_schema": CODING_TOOL_SCHEMA,
    }
    # Opus 4.x adaptive-thinking models take no sampling params (no temperature/
    # top_p/prefill); determinism comes from the forced tool_choice + the fixed
    # dossier input, not a temperature setting.
    params = {"max_tokens": 2000}
    with log_call(
        phase="n30-coding",
        operation=f"code_{case_id}",
        operator="claude",
        operator_role="extractor",
        endpoint="https://api.anthropic.com/v1/messages",
        sdk_version=f"anthropic=={getattr(anthropic, '__version__', '?')}",
        logs_dir=LOGS_DIR,
    ) as logger:
        logger.set_model_version(CLAUDE_MODEL)
        logger.set_system_prompt(CODEBOOK)
        logger.set_user_prompt(build_user_prompt(dossier_text))
        logger.set_parameters(params)
        resp = client.messages.create(
            model=CLAUDE_MODEL,
            system=CODEBOOK,
            messages=[{"role": "user", "content": build_user_prompt(dossier_text)}],
            tools=[tool],
            tool_choice={"type": "tool", "name": "emit_case_coding"},
            **params,
        )
        logger.capture_response(resp)
    for block in resp.content:
        if getattr(block, "type", None) == "tool_use":
            return validate_record(block.input), json.dumps(block.input)
    return None, str(resp.content)


def code_with_grok(case_id: str, dossier_text: str) -> tuple[dict | None, str]:
    from openai import OpenAI

    api_key = os.environ.get("GROK_API_KEY")
    if not api_key:
        raise RuntimeError("GROK_API_KEY not set")
    client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
    schema_hint = json.dumps(CODING_TOOL_SCHEMA["properties"], indent=0)
    sys_prompt = (
        CODEBOOK
        + "\n\nReturn a single JSON object with exactly these keys (values must "
        "satisfy the stated enums):\n" + schema_hint
    )
    params = {"temperature": 0.0, "max_tokens": 2000}
    with log_call(
        phase="n30-coding",
        operation=f"code_{case_id}",
        operator="grok",
        operator_role="extractor",
        endpoint="https://api.x.ai/v1/chat/completions",
        sdk_version="openai(xai)",
        logs_dir=LOGS_DIR,
    ) as logger:
        logger.set_model_version(GROK_MODEL)
        logger.set_system_prompt(sys_prompt)
        logger.set_user_prompt(build_user_prompt(dossier_text))
        logger.set_parameters(params)
        resp = client.chat.completions.create(
            model=GROK_MODEL,
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": build_user_prompt(dossier_text)},
            ],
            response_format={"type": "json_object"},
            **params,
        )
        logger.capture_response(resp)
    raw = resp.choices[0].message.content or ""
    parsed = _extract_json(raw)
    return (validate_record(parsed) if parsed is not None else None), raw


def code_with_gemini(case_id: str, dossier_text: str) -> tuple[dict | None, str]:
    from google import genai
    from google.genai import types

    sys.path.insert(0, str(REPO / "audit" / "scripts"))
    from _gemini_throttle import throttled  # noqa: E402

    api_key = os.environ.get("GOOGLE_API_KEY_FreeTier") or os.environ.get(
        "GOOGLE_API_KEY"
    )
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY_FreeTier / GOOGLE_API_KEY not set")
    client = genai.Client(api_key=api_key)
    schema_hint = json.dumps(CODING_TOOL_SCHEMA["properties"], indent=0)
    prompt = (
        CODEBOOK
        + "\n\nReturn a single JSON object with exactly these keys (values must "
        "satisfy the stated enums):\n"
        + schema_hint
        + "\n\n"
        + build_user_prompt(dossier_text)
    )
    # gemini-3.1-pro is a thinking model; the default output budget is shared with
    # thinking tokens and can truncate the JSON mid-string. Raise max_output_tokens
    # and cap the thinking budget so the structured record always completes.
    cfg_kwargs = dict(
        temperature=0.0,
        response_mime_type="application/json",
        max_output_tokens=4096,
    )
    try:
        cfg_kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=512)
    except Exception:  # noqa: BLE001 - older SDKs lack ThinkingConfig
        pass
    params = {
        "temperature": 0.0,
        "response_mime_type": "application/json",
        "max_output_tokens": 4096,
        "thinking_budget": 512,
    }
    with log_call(
        phase="n30-coding",
        operation=f"code_{case_id}",
        operator="gemini",
        operator_role="extractor",
        endpoint="https://generativelanguage.googleapis.com",
        sdk_version="google-genai",
        logs_dir=LOGS_DIR,
    ) as logger:
        logger.set_model_version(GEMINI_MODEL)
        logger.set_system_prompt(CODEBOOK)
        logger.set_user_prompt(build_user_prompt(dossier_text))
        logger.set_parameters(params)
        resp = throttled(
            lambda: client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(**cfg_kwargs),
            ),
            label=case_id,
        )
        raw = resp.text or ""
        logger.capture_response(raw)
    parsed = _extract_json(raw)
    return (validate_record(parsed) if parsed is not None else None), raw


def _first_balanced_object(text: str) -> str | None:
    """Return the first brace-balanced {...} substring (string-aware).

    Handles a trailing extra brace or trailing prose after a valid object (the
    greedy '{.*}' regex mis-grabs those), by scanning from the first '{' to its
    matching close, respecting string literals and escapes.
    """
    start = text.find("{")
    if start < 0:
        return None
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    return None


def _extract_json(text: str) -> dict | None:
    """Parse the first JSON object out of a model response."""
    if not text:
        return None
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Brace-matched first object (robust to a trailing extra '}' or trailing text).
    obj = _first_balanced_object(text)
    if obj:
        try:
            return json.loads(obj)
        except json.JSONDecodeError:
            pass
    # Last resort: greedy match (handles some minor cases the scanner misses).
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            return None
    return None


CODERS = {
    "claude": code_with_claude,
    "gemini": code_with_gemini,
    "grok": code_with_grok,
}


# ---------------------------------------------------------------------------
# Majority-vote-or-flag
# ---------------------------------------------------------------------------
def majority_vote(values: list[str]) -> tuple[str, bool]:
    """Return (majority_value, flagged). Flagged when no value has >=2 support."""
    present = [v for v in values if v is not None]
    if not present:
        return "uncertain", True
    counts: dict[str, int] = {}
    for v in present:
        counts[v] = counts.get(v, 0) + 1
    best = max(counts.items(), key=lambda kv: kv[1])
    if best[1] >= 2:
        return best[0], False
    return best[0], True  # 3-way split (or 2 present & disagree): flag


ALL_CELLS = [
    "sigma_T1",
    "sigma_T2",
    "sigma_T3",
    "sigma_T4",
    "sigma_T5",
    "sigma_T6",
    "collapse_state",
    "gap_45",
    "gap_56",
    "p4_pathway",
    "p5_pathway",
    "t1_archetype",
    "t2_model",
    "gap_mitigated",
]


def combine(per_model: dict[str, dict | None]) -> dict:
    majority: dict[str, str] = {}
    flags: dict[str, bool] = {}
    for cell in ALL_CELLS:
        vals = [
            (per_model[m].get(cell) if per_model.get(m) else None)
            for m in CODERS
            if m in per_model
        ]
        maj, flagged = majority_vote(vals)
        majority[cell] = maj
        flags[cell] = flagged
    return {"majority": majority, "flags": flags}


# ---------------------------------------------------------------------------
# Fleiss' kappa over the binary cells
# ---------------------------------------------------------------------------
def fleiss_kappa(records: list[dict], coders: list[str]) -> dict:
    """Fleiss' kappa over BINARY_CELLS; categories {0,1,uncertain}; n raters."""
    categories = ["0", "1", "uncertain"]
    items: list[list[int]] = []  # per item: counts over categories
    for rec in records:
        per_model = rec["per_model"]
        for cell in BINARY_CELLS:
            row = [0, 0, 0]
            n_rated = 0
            for m in coders:
                pm = per_model.get(m)
                if not pm:
                    continue
                v = pm.get(cell)
                if v in categories:
                    row[categories.index(v)] += 1
                    n_rated += 1
            if n_rated == len(coders):  # only fully-rated items
                items.append(row)
    n_items = len(items)
    n_raters = len(coders)
    if n_items == 0 or n_raters < 2:
        return {"kappa": None, "n_items": n_items, "n_raters": n_raters}
    # Proportion of ratings in each category.
    totals = [sum(items[i][c] for i in range(n_items)) for c in range(3)]
    grand = sum(totals)
    p_j = [t / grand for t in totals]
    # Per-item agreement.
    P_i = []
    for row in items:
        s = sum(n * (n - 1) for n in row)
        P_i.append(s / (n_raters * (n_raters - 1)))
    P_bar = sum(P_i) / n_items
    P_e = sum(p * p for p in p_j)
    kappa = (P_bar - P_e) / (1 - P_e) if (1 - P_e) != 0 else None
    return {
        "kappa": kappa,
        "n_items": n_items,
        "n_raters": n_raters,
        "P_bar": P_bar,
        "P_e": P_e,
        "category_proportions": dict(zip(categories, p_j)),
        "cells": BINARY_CELLS,
    }


def write_kappa_figure(kappa_info: dict, per_cell_agreement: dict, path: Path) -> None:
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:  # noqa: BLE001
        print(f"[warn] matplotlib unavailable, skipping figure: {exc}")
        return
    cells = list(per_cell_agreement.keys())
    agrees = [per_cell_agreement[c] for c in cells]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(cells, agrees, color="#3b6ea5")
    ax.set_ylim(0, 1.0)
    ax.set_ylabel("Unanimous-agreement rate (3/3 coders)")
    k = kappa_info.get("kappa")
    ktxt = f"{k:.3f}" if isinstance(k, float) else "n/a"
    ax.set_title(
        f"Triple-coder inter-rater agreement by cell\n"
        f"Fleiss' kappa (all binary cells) = {ktxt}  "
        f"(n_items={kappa_info.get('n_items')}, raters={kappa_info.get('n_raters')})"
    )
    ax.axhline(0.7, color="#a5493b", linestyle="--", linewidth=1, label="0.70 target")
    ax.legend()
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--only", type=str, default=None, help="comma-separated case_ids")
    ap.add_argument("--coders", type=str, default="claude,gemini,grok")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument(
        "--fill-missing",
        action="store_true",
        help=(
            "For cases already coded, re-run ONLY the coders whose per_model "
            "entry is missing/null (e.g. a rate-limited Gemini call), merge them "
            "into the existing record, and recompute majority/flags. Preserves "
            "the coders that already succeeded."
        ),
    )
    args = ap.parse_args()

    coders = [c.strip() for c in args.coders.split(",") if c.strip()]
    for c in coders:
        if c not in CODERS:
            print(f"unknown coder: {c}", file=sys.stderr)
            return 2

    dossiers = discover_dossiers()
    if args.only:
        want = {x.strip() for x in args.only.split(",")}
        dossiers = [d for d in dossiers if d[0] in want]
    if args.limit:
        dossiers = dossiers[: args.limit]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Triple-coding {len(dossiers)} dossiers with coders={coders}")
    print(f"Models: claude={CLAUDE_MODEL} gemini={GEMINI_MODEL} grok={GROK_MODEL}")
    print("=" * 70)

    records = []
    for case_id, case_name, path in dossiers:
        out_file = OUT_DIR / f"{case_id}_codes.json"
        if out_file.exists() and not args.overwrite:
            existing = json.loads(out_file.read_text())
            missing = [c for c in coders if not existing.get("per_model", {}).get(c)]
            if args.fill_missing and missing:
                print(f"[fill] {case_id}: re-running missing coder(s) {missing}")
                dossier_text = path.read_text(encoding="utf-8")
                for coder in missing:
                    t0 = time.time()
                    try:
                        rec, raw = CODERS[coder](case_id, dossier_text)
                    except Exception as exc:  # noqa: BLE001
                        print(f"  [{coder}] ERROR {type(exc).__name__}: {exc}")
                        rec, raw = None, f"[ERROR] {type(exc).__name__}: {exc}"
                    existing["per_model"][coder] = rec
                    existing.setdefault("per_model_raw", {})[coder] = raw
                    print(
                        f"  [{coder}] {'ok' if rec else 'FAILED'} ({time.time() - t0:.1f}s)"
                    )
                combined = combine(existing["per_model"])
                existing["majority"] = combined["majority"]
                existing["flags"] = combined["flags"]
                existing["n_flags"] = sum(combined["flags"].values())
                out_file.write_text(json.dumps(existing, indent=2, ensure_ascii=False))
                print(f"  -> {out_file.name}  ({existing['n_flags']} flagged cell(s))")
            else:
                print(f"[skip] {case_id} already coded ({out_file.name})")
            records.append(existing)
            continue
        if args.dry_run:
            print(f"[dry-run] would code {case_id} {case_name}")
            continue
        dossier_text = path.read_text(encoding="utf-8")
        per_model: dict[str, dict | None] = {}
        per_model_raw: dict[str, str] = {}
        for coder in coders:
            t0 = time.time()
            try:
                rec, raw = CODERS[coder](case_id, dossier_text)
            except Exception as exc:  # noqa: BLE001
                print(f"  [{coder}] ERROR {type(exc).__name__}: {exc}")
                rec, raw = None, f"[ERROR] {type(exc).__name__}: {exc}"
            per_model[coder] = rec
            per_model_raw[coder] = raw
            status = "ok" if rec else "FAILED"
            print(f"  [{coder}] {status} ({time.time() - t0:.1f}s)")
        combined = combine(per_model)
        n_flags = sum(combined["flags"].values())
        record = {
            "case_id": case_id,
            "case": case_name,
            "coders": coders,
            "models": {
                "claude": CLAUDE_MODEL,
                "gemini": GEMINI_MODEL,
                "grok": GROK_MODEL,
            },
            "per_model": per_model,
            "per_model_raw": per_model_raw,
            "majority": combined["majority"],
            "flags": combined["flags"],
            "n_flags": n_flags,
        }
        out_file.write_text(json.dumps(record, indent=2, ensure_ascii=False))
        records.append(record)
        print(f"  -> {out_file.name}  ({n_flags} flagged cell(s))")

    if args.dry_run or not records:
        return 0

    # Inter-rater reliability across the binary cells.
    kinfo = fleiss_kappa(records, coders)
    # Per-cell unanimous-agreement rate for the figure.
    per_cell_agree: dict[str, float] = {}
    for cell in BINARY_CELLS:
        n_unan = 0
        n_tot = 0
        for rec in records:
            vals = [
                (
                    rec["per_model"].get(m, {}).get(cell)
                    if rec["per_model"].get(m)
                    else None
                )
                for m in coders
            ]
            if all(v is not None for v in vals):
                n_tot += 1
                if len(set(vals)) == 1:
                    n_unan += 1
        per_cell_agree[cell] = (n_unan / n_tot) if n_tot else 0.0
    (OUT_DIR / "fleiss_kappa.json").write_text(
        json.dumps({"fleiss": kinfo, "per_cell_unanimous": per_cell_agree}, indent=2)
    )
    write_kappa_figure(kinfo, per_cell_agree, OUT_DIR / "fleiss_kappa.png")
    k = kinfo.get("kappa")
    ktxt = f"{k:.3f}" if isinstance(k, float) else "n/a"
    total_flags = sum(r["n_flags"] for r in records)
    total_cells = len(records) * len(ALL_CELLS)
    print("=" * 70)
    print(f"Fleiss' kappa (binary cells) = {ktxt}  over {kinfo.get('n_items')} items")
    print(
        f"Flagged cells: {total_flags}/{total_cells} "
        f"({100 * total_flags / total_cells:.1f}%) across {len(records)} cases"
    )
    print(f"Outputs in {OUT_DIR}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
