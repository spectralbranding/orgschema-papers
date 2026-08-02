#!/usr/bin/env python3
"""Separated-pass re-coding harness (Stage S4 construct-validity separation).

Fixes the primary threat the v1 n=26 pass exposed (PREREGISTRATION_V2.md §1): the
structural gap (IV) and the outcome pathway (DV) were partly read from overlapping
evidence by a single coder that saw the whole dossier (the Daimler-Chrysler flip).
This harness codes the two constructs from DISJOINT evidence in SEPARATE passes, so
no single coding call ever sees both the closing-time deal structure and the
realized 3-5-year outcome. The porosity vector is closed by construction.

For each dossier it builds two slices, keyed on the dossier's own section headers
(consistent `## 1.` .. `## 7.` across every case):

  STRUCTURAL slice  = header/preamble + section 1 (deal identification)
                      + section 2 (tier-level transfer content, the closing structure)
                      + section 5 (cascade-gap-mitigation, closing-time)
                      + section 6 (collapse-state)
     -> codes gap_45, gap_56, gap_mitigated, collapse_state, sigma_T1..T6
     -> NEVER sees the post-deal outcome (sections 3, 4, 7 withheld)

  OUTCOME slice     = header/preamble + section 1 (deal identification)
                      + section 3 (post-deal performance, 3-5yr)
                      + section 4 (failure-pathway evidence)
     -> codes p4_pathway, p5_pathway, t1_archetype, t2_model
     -> NEVER sees the deal's structural transfer content (sections 2, 5, 6, 7 withheld)

Each slice is independently triple-coded (Claude / Gemini / Grok), blind to the
paper, the pre-registration, the hypotheses, the predicted direction, and the
anchor-vs-extension status (CASE_CODING_PROTOCOL.md sec.5). Per cell the three
coders are combined MAJORITY-VOTE-OR-FLAG (>=2 agree -> majority; else FLAG). A
coder that cannot determine a cell from its slice must return "uncertain"
(anti-fabrication HARD rule) -- never guessed. Per-construct Fleiss' kappa is
reported separately for the structural and the outcome cells. Every model call is
JSONL-logged via the corpus llm_call_logger.

REGISTERED-BEFORE-DATA: this harness + the empty recoded_dataset_separated.csv
schema are committed BEFORE any separated coded datum exists. `--dry-run` prints
the two slices for each case and makes NO API call, so the slicing is auditable
before spending a token.

Outputs:
  - recode_separated/<case_id>_struct.json    (structural-pass per-model + majority)
  - recode_separated/<case_id>_outcome.json   (outcome-pass per-model + majority)
  - recode_separated/kappa_struct.json         (structural-construct Fleiss' kappa)
  - recode_separated/kappa_outcome.json        (outcome-construct Fleiss' kappa)
  - recoded_dataset_separated.csv (via assemble_recoded_separated.py)

Run (all three coders; injects BWS keys into the subprocess only):

    bws run -- uv run --with anthropic --with google-genai --with openai \\
        python research/empirical_cases_v1/recode_separated_passes.py \\
        --only A01,A02,A03,A04,A05,A06,A07,A12,A13,A14,E01,E02,E03,E04,E05,E06,\\
E07,E08,E09,E10,E11,E12,E13,E14,E15,E16

Flags:
    --only ID[,ID]   code only the named case_ids (default: all A*/E* dossiers)
    --limit N        code only the first N dossiers (smoke test)
    --pass P         run only {struct,outcome} (default both)
    --coders LIST    subset of {claude,gemini,grok} (default all three)
    --dry-run        print the two slices; make no API calls
    --overwrite      re-code cases that already have output JSON
    --fill-missing   re-run only the coders whose per_model entry is missing/null
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
OUT_DIR = HERE / "recode_separated"
LOGS_DIR = HERE / "logs"

# Provenance phase for the JSONL call log. Overridable by importers (the S5 pilot
# runner sets PHASE = "s5-pilot-recode" + its own LOGS_DIR so pilot calls are
# distinct from the S4 deconfounding re-code).
PHASE = "s4-separated-recode"

# Corpus LLM-call logger (llm_call_logger.py).
sys.path.insert(0, str(REPO / "research" / "code"))
from llm_call_logger import log_call  # noqa: E402

# Reuse the robust JSON extractor from the v1 harness (pure function).
from triple_code_dossiers import _extract_json  # noqa: E402

# ---------------------------------------------------------------------------
# Model pins (identical to the v1 harness so provenance is comparable).
# ---------------------------------------------------------------------------
CLAUDE_MODEL = "claude-opus-4-8"  # Anthropic frontier reasoning (Opus tier)
GEMINI_MODEL = "gemini-3.1-pro-preview"  # Google flagship Pro (3.5 Pro not shipped)
GROK_MODEL = "grok-4.5"  # xAI frontier (2026-07; reasoning-only, configurable effort)
OPENAI_MODEL = "gpt-5.6-sol"  # OpenAI frontier reasoning (GPT-5.6 family flagship)

# ---------------------------------------------------------------------------
# Controlled vocabularies (shared with v1 where the field is shared).
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

# ---------------------------------------------------------------------------
# STRUCTURAL pass: schema, binary cells, codebook. Gap constructs ONLY.
# ---------------------------------------------------------------------------
STRUCT_BINARY_CELLS = ["gap_45", "gap_56"]
STRUCT_CELLS = [
    "sigma_T1",
    "sigma_T2",
    "sigma_T3",
    "sigma_T4",
    "sigma_T5",
    "sigma_T6",
    "collapse_state",
    "gap_45",
    "gap_56",
    "gap_mitigated",
]
STRUCT_SCHEMA: dict = {
    "type": "object",
    "required": STRUCT_CELLS + ["rationale"],
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
        "gap_mitigated": {"type": "string", "enum": MITIGATED},
        "rationale": {"type": "string"},
    },
}
STRUCT_CODEBOOK = f"""\
You are a careful, neutral coder of the STRUCTURE OF A CORPORATE TRANSACTION AT
CLOSING. You are given ONE evidence slice assembled from public primary sources
(SEC filings, company releases, reputable press). This slice describes ONLY how the
deal was structured -- what crossed the ownership boundary and what did not -- at
the moment of closing. You are DELIBERATELY NOT shown what happened to the combined
company afterward, and you must NOT speculate about later outcomes, success, or
failure. Code STRICTLY the deal as structured. If the slice does not let you
determine a field, you MUST return "uncertain" -- never guess, never infer from
outside knowledge of the companies.

Emit a single structured record with these fields.

A. BUNDLE SIGNATURE -- for each of six organizational tiers, classify what happened
to that tier when the transaction crossed the ownership boundary. Exactly one label
per tier.
  T1 Owner Intent (controlling principal / imprint).
     Labels: {", ".join(T1_ALPHABET)}, uncertain.
       replace = old controlling intent exited, a new one installed;
       imprint-share = both principals' intent co-present;
       continue = same controlling intent persists;
       terminate = the controlling intent ended with no successor;
       reconstruct = intent re-formed into a new (often non-commercial) purpose;
       replicate = intent copied into a standardized template (e.g. franchising);
       mutual-replace = two intents fused into a jointly-new one (merger of equals).
  T2 Business Model, T3 Business Entity (legal vehicle), T4 Product (customer-
  acceptance layer), T5 Process (operations), T6 Organization (people/culture).
     Labels for T2-T6: {", ".join(SIGMA_ALPHABET)}, uncertain.
       1-1 = transferred whole, one-to-one; N-1 = many collapsed into one;
       1-N = one split into many; subset = only part transferred;
       partial = transferred but incompletely / with friction;
       read-only = licensed / accessed without ownership transfer;
       swap = exchanged for a different one (e.g. new legal domicile);
       terminate = ended; null = not applicable / nothing at this tier.

B. TIER-TRANSFER GAPS -- code strictly from the STRUCTURE OF THE DEAL AT CLOSING.
A gap is a STRUCTURAL MISMATCH IN WHAT THE DEAL TRANSFERRED, not a later failure.
  gap_45: Did the customer-facing product/asset (T4, what customers buy) cross the
    ownership boundary WITHOUT the operational processes that produce or deliver it
    (T5) transferring or being aligned coherently alongside it? A documented
    product-vs-process structural mismatch AT CLOSING. 1 = yes such a gap; 0 = no
    (product and its processes moved together, or neither moved); uncertain.
  gap_56: Did the operational processes (T5) transfer or get re-engineered WITHOUT
    the organization / people / management / culture that run them (T6) transferring
    or aligning coherently alongside, AT CLOSING? 1 = yes; 0 = no; uncertain.
  gap_mitigated: If (and only if) you coded a structural gap above, was that gap
    documented as contractually absorbed at closing via a transitional-services or
    operating agreement allocating the shared substrate? yes / no / NA (NA if no gap).

E. collapse_state: Any Tier-1 fusion documented in the deal structure? none /
   T1=T4 (founder identity IS the product) / T1=T3 (the legal subject IS a specific
   natural person) / T1=T3=T4 / T1=T2 / T1=T6 / uncertain.

rationale: 2-4 sentences citing the slice lines that drove your gap_45 and gap_56
codes specifically. Cite ONLY closing-structure evidence; do NOT reason about later
outcomes.

Emit ONLY the structured record. Code conservatively: inability to determine a
structural field is "uncertain"; a gap you cannot document at closing is 0.
"""

# ---------------------------------------------------------------------------
# OUTCOME pass: schema, binary cells, codebook. Pathway constructs ONLY.
# ---------------------------------------------------------------------------
OUTCOME_BINARY_CELLS = ["p4_pathway", "p5_pathway", "t1_archetype", "t2_model"]
OUTCOME_CELLS = ["p4_pathway", "p5_pathway", "t1_archetype", "t2_model"]
OUTCOME_SCHEMA: dict = {
    "type": "object",
    "required": OUTCOME_CELLS + ["performance_metric", "rationale"],
    "properties": {
        "p4_pathway": {"type": "string", "enum": TRISTATE},
        "p5_pathway": {"type": "string", "enum": TRISTATE},
        "t1_archetype": {"type": "string", "enum": TRISTATE},
        "t2_model": {"type": "string", "enum": TRISTATE},
        "performance_metric": {"type": "string"},
        "rationale": {"type": "string"},
    },
}
OUTCOME_CODEBOOK = """\
You are a careful, neutral coder of the REALIZED OUTCOME of a corporate transaction
over the 3-5 years AFTER it closed. You are given ONE evidence slice assembled from
public primary sources (financial filings, reputable press) that describes ONLY the
post-deal trajectory -- how the combined company actually fared. You are
DELIBERATELY NOT shown how the deal was structured at closing (what transferred and
what did not), and you must NOT speculate about the deal's structure. Code STRICTLY
the documented realized outcome. If the slice does not let you determine a field,
you MUST return "uncertain" -- never guess, never infer from outside knowledge.

Emit a single structured record with these fields.

C. FAILURE-PATHWAY INCIDENCE -- code strictly from the DOCUMENTED OUTCOME at the
3-5 year horizon. A pathway is a REALIZED DISRUPTION OVER TIME, not a structural
property of the deal.
  p4_pathway: Is there documented disruption specifically at the product/process
    interface (the acquired product could not be aligned with the operating
    processes over time; product-line/operations incoherence realized after the
    deal)? 1 = yes; 0 = no / none documented; uncertain.
  p5_pathway: Is there documented fracture specifically at the process/organization
    interface (operations vs people/management/culture; integration of operations
    broke against the organization over time)? 1 = yes; 0 = no / none documented;
    uncertain.
  t1_archetype: Is there documented incoherence in the controlling-intent archetype
    itself as it played out (e.g. an announced "merger of equals" that operated as
    one-sided dominance)? A channel SEPARATE from the product/process and
    process/organization pathways. 1 = yes; 0 = no; uncertain.
  t2_model: Is there documented incompatibility of the two business models
    (value-capture logics that could not be reconciled over time)? A channel
    SEPARATE from the pathways above. 1 = yes; 0 = no; uncertain.

D. performance_metric: the single best-documented post-deal outcome scalar in the
   slice (e.g. "divested 80.1% after ~108 months", "~$99bn goodwill write-down",
   "no divestiture; assets retained"). One short phrase. If none, "not documented".

rationale: 2-4 sentences citing the slice lines that drove your p4_pathway and
p5_pathway codes specifically. Cite ONLY realized-outcome evidence; do NOT reason
about how the deal was structured at closing.

Emit ONLY the structured record. Code conservatively: absence of documented
evidence for a pathway is 0 (not-documented); inability to determine is "uncertain".
"""

PASS_CONFIG = {
    "struct": {
        "codebook": STRUCT_CODEBOOK,
        "schema": STRUCT_SCHEMA,
        "cells": STRUCT_CELLS,
        "binary_cells": STRUCT_BINARY_CELLS,
        "tool_name": "emit_structural_coding",
        "sections": (1, 2, 5, 6),
        "text_fields": ("rationale",),
    },
    "outcome": {
        "codebook": OUTCOME_CODEBOOK,
        "schema": OUTCOME_SCHEMA,
        "cells": OUTCOME_CELLS,
        "binary_cells": OUTCOME_BINARY_CELLS,
        "tool_name": "emit_outcome_coding",
        "sections": (1, 3, 4),
        "text_fields": ("performance_metric", "rationale"),
    },
}


# ---------------------------------------------------------------------------
# Dossier discovery + section slicing
# ---------------------------------------------------------------------------
def discover_dossiers() -> list[tuple[str, str, Path]]:
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


SECTION_RE = re.compile(r"^##\s+(\d+)\.\s", re.MULTILINE)


def split_sections(text: str) -> tuple[str, dict[int, str]]:
    """Return (preamble_before_section_1, {section_number: section_text})."""
    matches = list(SECTION_RE.finditer(text))
    if not matches:
        return text, {}
    preamble = text[: matches[0].start()]
    sections: dict[int, str] = {}
    for i, m in enumerate(matches):
        num = int(m.group(1))
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[num] = text[start:end].rstrip()
    return preamble, sections


def build_slice(text: str, keep_sections: tuple[int, ...]) -> str:
    """Assemble an evidence slice = preamble + only the kept sections, in order."""
    preamble, sections = split_sections(text)
    parts = [preamble.rstrip()]
    for num in sorted(keep_sections):
        if num in sections:
            parts.append(sections[num])
    return "\n\n".join(p for p in parts if p.strip()) + "\n"


# ---------------------------------------------------------------------------
# Record validation against a given pass schema
# ---------------------------------------------------------------------------
def validate_record(rec, schema: dict, text_fields: tuple[str, ...]):
    # A model occasionally emits the structured record wrapped in a one-element JSON
    # array ([ {...} ]) instead of a bare object; the extractor then hands `validate_record`
    # a list, which previously crashed with "'list' object has no attribute 'get'" and
    # (because the shape is deterministic for a given slice) could not be recovered even by
    # a retry. Coerce a list-wrapped object to its first dict element; if the payload is not
    # an object at all, return None so the caller records a clean failed cell (not a crash).
    if isinstance(rec, list):
        rec = next((x for x in rec if isinstance(x, dict)), None)
    if not isinstance(rec, dict):
        return None
    props = schema["properties"]
    clean: dict = {}
    for key, spec in props.items():
        val = rec.get(key)
        if key in text_fields:
            clean[key] = str(val) if val is not None else ""
            continue
        allowed = spec["enum"]
        sval = str(val).strip() if val is not None else ""
        sval = sval.replace("≡", "=")
        if key in (
            "gap_45",
            "gap_56",
            "p4_pathway",
            "p5_pathway",
            "t1_archetype",
            "t2_model",
        ):
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


def build_user_prompt(slice_text: str) -> str:
    return (
        "Here is the evidence slice. Read it and emit the structured coding "
        "record.\n\n[SLICE BEGIN]\n" + slice_text + "\n[SLICE END]\n"
    )


# ---------------------------------------------------------------------------
# Coder backends (one per model), parameterized by pass config.
# ---------------------------------------------------------------------------
def code_with_claude(case_id: str, pass_name: str, slice_text: str, cfg: dict):
    import anthropic

    client = anthropic.Anthropic()
    tool = {
        "name": cfg["tool_name"],
        "description": f"Emit the {pass_name} coding record for one transaction case.",
        "input_schema": cfg["schema"],
    }
    params = {"max_tokens": 2000}
    with log_call(
        phase=PHASE,
        operation=f"{pass_name}_{case_id}",
        operator="claude",
        operator_role="extractor",
        endpoint="https://api.anthropic.com/v1/messages",
        sdk_version=f"anthropic=={getattr(anthropic, '__version__', '?')}",
        logs_dir=LOGS_DIR,
    ) as logger:
        logger.set_model_version(CLAUDE_MODEL)
        logger.set_system_prompt(cfg["codebook"])
        logger.set_user_prompt(build_user_prompt(slice_text))
        logger.set_parameters(params)
        resp = client.messages.create(
            model=CLAUDE_MODEL,
            system=cfg["codebook"],
            messages=[{"role": "user", "content": build_user_prompt(slice_text)}],
            tools=[tool],
            tool_choice={"type": "tool", "name": cfg["tool_name"]},
            **params,
        )
        logger.capture_response(resp)
    for block in resp.content:
        if getattr(block, "type", None) == "tool_use":
            return (
                validate_record(block.input, cfg["schema"], cfg["text_fields"]),
                json.dumps(block.input),
            )
    return None, str(resp.content)


def code_with_grok(case_id: str, pass_name: str, slice_text: str, cfg: dict):
    from openai import OpenAI

    api_key = os.environ.get("GROK_API_KEY")
    if not api_key:
        raise RuntimeError("GROK_API_KEY not set")
    client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
    schema_hint = json.dumps(cfg["schema"]["properties"], indent=0)
    sys_prompt = (
        cfg["codebook"]
        + "\n\nReturn a single JSON object with exactly these keys (values must "
        "satisfy the stated enums):\n" + schema_hint
    )
    # grok-4.5 is a reasoning-only model: sampling params (temperature) are default-only
    # (do NOT pass temperature; reasoning_effort defaults to high). The server-side
    # reasoning trace counts toward the completion budget, so give the JSON verdict
    # headroom (mirrors the gemini thinking-trace allowance).
    params = {"max_tokens": 8000}
    with log_call(
        phase=PHASE,
        operation=f"{pass_name}_{case_id}",
        operator="grok",
        operator_role="extractor",
        endpoint="https://api.x.ai/v1/chat/completions",
        sdk_version="openai(xai)",
        logs_dir=LOGS_DIR,
    ) as logger:
        logger.set_model_version(GROK_MODEL)
        logger.set_system_prompt(sys_prompt)
        logger.set_user_prompt(build_user_prompt(slice_text))
        logger.set_parameters(params)
        resp = client.chat.completions.create(
            model=GROK_MODEL,
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": build_user_prompt(slice_text)},
            ],
            response_format={"type": "json_object"},
            **params,
        )
        logger.capture_response(resp)
    raw = resp.choices[0].message.content or ""
    parsed = _extract_json(raw)
    return (
        validate_record(parsed, cfg["schema"], cfg["text_fields"])
        if parsed is not None
        else None
    ), raw


def _lenient_json(raw: str) -> dict | None:
    """Recover a structured object from a gemini response.

    This model requires thinking mode, and its mandatory thinking trace can consume the
    output allowance so the response deterministically drops the trailing "}" (content
    otherwise complete) or, on the free tier, appends a stray tail before it. The shared
    `_extract_json` handles trailing extra "}"/text but not a MISSING closing brace, so
    fall back to (a) appending closing brace(s) for the truncated case and (b) a
    raw_decode of the object prefix for the trailing-garbage case.
    """
    obj = _extract_json(raw)
    if obj is not None:
        return obj
    if not raw:
        return None
    text = raw.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text)
    for suffix in ("}", '"}', '"}}'):
        try:
            return json.loads(text + suffix)
        except json.JSONDecodeError:
            pass
    i = text.find("{")
    if i >= 0:
        try:
            decoded, _ = json.JSONDecoder().raw_decode(text[i:])
            return decoded if isinstance(decoded, dict) else None
        except json.JSONDecodeError:
            pass
    # Last resort for the malformed-tail form (e.g. `...0)."\n)."\n}`): the last schema
    # field ("rationale") is always a string, so truncate after the final closing quote
    # of that value and re-close the object. This only runs after every strict parse has
    # failed, so it strictly recovers otherwise-lost data; the coded binary cells precede
    # rationale and are intact -- only trailing garbage in the non-scored text is dropped.
    t = text.rstrip()
    if t.endswith("}"):
        t = t[:-1].rstrip()
    for m in reversed([mo.start() for mo in re.finditer('"', t)]):
        try:
            recovered = json.loads(t[: m + 1] + "}")
        except json.JSONDecodeError:
            continue
        if isinstance(recovered, dict):
            return recovered
    return None


def code_with_gemini(case_id: str, pass_name: str, slice_text: str, cfg: dict):
    from google import genai
    from google.genai import types

    sys.path.insert(0, str(REPO / "audit" / "scripts"))
    from _gemini_throttle import throttled  # noqa: E402

    # Prefer the paid GOOGLE_API_KEY over the free tier: the free-tier serving of this
    # model emitted malformed structured JSON (a stray ")." before the closing brace) on
    # the larger struct dossiers, failing the extractor; the paid tier is more reliable.
    api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get(
        "GOOGLE_API_KEY_FreeTier"
    )
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY / GOOGLE_API_KEY_FreeTier not set")
    client = genai.Client(api_key=api_key)
    schema_hint = json.dumps(cfg["schema"]["properties"], indent=0)
    prompt = cfg[
        "codebook"
    ] + "\n\nReturn a single JSON object with exactly these keys (values must " "satisfy the stated enums):\n" + schema_hint + "\n\n" + build_user_prompt(
        slice_text
    )
    # This model requires thinking mode (budget 0 -> 400 INVALID_ARGUMENT), and its
    # mandatory thinking trace counts against max_output_tokens; at 4096 the trace left
    # no room for the trailing "}" of the structured JSON, truncating it (observed
    # deterministically on 2/40 S5-pilot calls). Cap the thinking and give the visible
    # output a large headroom so the full JSON always completes.
    cfg_kwargs = dict(
        temperature=0.0, response_mime_type="application/json", max_output_tokens=16384
    )
    try:
        cfg_kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=512)
    except Exception:  # noqa: BLE001
        pass
    params = {
        "temperature": 0.0,
        "response_mime_type": "application/json",
        "max_output_tokens": 16384,
        "thinking_budget": 512,
    }
    with log_call(
        phase=PHASE,
        operation=f"{pass_name}_{case_id}",
        operator="gemini",
        operator_role="extractor",
        endpoint="https://generativelanguage.googleapis.com",
        sdk_version="google-genai",
        logs_dir=LOGS_DIR,
    ) as logger:
        logger.set_model_version(GEMINI_MODEL)
        logger.set_system_prompt(cfg["codebook"])
        logger.set_user_prompt(build_user_prompt(slice_text))
        logger.set_parameters(params)
        resp = throttled(
            lambda: client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(**cfg_kwargs),
            ),
            label=f"{pass_name}_{case_id}",
        )
        raw = resp.text or ""
        logger.capture_response(raw)
    parsed = _lenient_json(raw)
    return (
        validate_record(parsed, cfg["schema"], cfg["text_fields"])
        if parsed is not None
        else None
    ), raw


def code_with_openai(case_id: str, pass_name: str, slice_text: str, cfg: dict):
    """OpenAI gpt-5.x coder (4th coder). Pinned to gpt-5.6-sol (GPT-5.6 frontier).

    gpt-5.x quirks (research/prism_core/provider.py): use max_completion_tokens (not
    max_tokens); temperature is default-only (do NOT pass it). gpt-5.6-sol is a
    reasoning model whose reasoning tokens count toward max_completion_tokens, so give
    the JSON verdict headroom. Same structured-JSON contract + JSONL logging as the
    other three backends.
    """
    from openai import OpenAI

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    client = OpenAI(api_key=api_key)
    schema_hint = json.dumps(cfg["schema"]["properties"], indent=0)
    sys_prompt = (
        cfg["codebook"]
        + "\n\nReturn a single JSON object with exactly these keys (values must "
        "satisfy the stated enums):\n" + schema_hint
    )
    params = {"max_completion_tokens": 8000}
    with log_call(
        phase=PHASE,
        operation=f"{pass_name}_{case_id}",
        operator="openai",
        operator_role="extractor",
        endpoint="https://api.openai.com/v1/chat/completions",
        sdk_version="openai",
        logs_dir=LOGS_DIR,
    ) as logger:
        logger.set_model_version(OPENAI_MODEL)
        logger.set_system_prompt(sys_prompt)
        logger.set_user_prompt(build_user_prompt(slice_text))
        logger.set_parameters(params)
        resp = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": build_user_prompt(slice_text)},
            ],
            response_format={"type": "json_object"},
            **params,
        )
        logger.capture_response(resp)
    raw = resp.choices[0].message.content or ""
    parsed = _extract_json(raw)
    return (
        validate_record(parsed, cfg["schema"], cfg["text_fields"])
        if parsed is not None
        else None
    ), raw


CODERS = {
    "claude": code_with_claude,
    "gemini": code_with_gemini,
    "grok": code_with_grok,
    "openai": code_with_openai,
}
MODEL_IDS = {
    "claude": CLAUDE_MODEL,
    "gemini": GEMINI_MODEL,
    "grok": GROK_MODEL,
    "openai": OPENAI_MODEL,
}


# ---------------------------------------------------------------------------
# Majority-vote-or-flag + Fleiss' kappa
# ---------------------------------------------------------------------------
def majority_vote(values: list[str | None]) -> tuple[str, bool]:
    present = [v for v in values if v is not None]
    if not present:
        return "uncertain", True
    counts: dict[str, int] = {}
    for v in present:
        counts[v] = counts.get(v, 0) + 1
    best = max(counts.items(), key=lambda kv: kv[1])
    if best[1] >= 2:
        return best[0], False
    return best[0], True


def combine(per_model: dict, cells: list[str], coders: list[str]) -> dict:
    majority: dict[str, str] = {}
    flags: dict[str, bool] = {}
    for cell in cells:
        vals = [
            (per_model[m].get(cell) if per_model.get(m) else None)
            for m in coders
            if m in per_model
        ]
        maj, flagged = majority_vote(vals)
        majority[cell] = maj
        flags[cell] = flagged
    return {"majority": majority, "flags": flags}


def fleiss_kappa(records: list[dict], binary_cells: list[str], coders: list[str]):
    categories = ["0", "1", "uncertain"]
    items: list[list[int]] = []
    for rec in records:
        per_model = rec["per_model"]
        for cell in binary_cells:
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
            if n_rated == len(coders):
                items.append(row)
    n_items = len(items)
    n_raters = len(coders)
    if n_items == 0 or n_raters < 2:
        return {"kappa": None, "n_items": n_items, "n_raters": n_raters}
    totals = [sum(items[i][c] for i in range(n_items)) for c in range(3)]
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
        "category_proportions": dict(zip(categories, p_j)),
        "cells": binary_cells,
    }


# ---------------------------------------------------------------------------
# Per-pass runner
# ---------------------------------------------------------------------------
def run_pass(pass_name, dossiers, coders, args) -> list[dict]:
    cfg = PASS_CONFIG[pass_name]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    records: list[dict] = []
    for case_id, case_name, path in dossiers:
        out_file = OUT_DIR / f"{case_id}_{pass_name}.json"
        text = path.read_text(encoding="utf-8")
        slice_text = build_slice(text, cfg["sections"])
        if args.dry_run:
            print(f"\n===== [{pass_name}] {case_id} {case_name} =====")
            print(f"  sections kept: {cfg['sections']}  slice chars: {len(slice_text)}")
            print("  --- slice preview (first 600 chars) ---")
            print("  " + slice_text[:600].replace("\n", "\n  "))
            continue
        if out_file.exists() and not args.overwrite:
            existing = json.loads(out_file.read_text())
            missing = [c for c in coders if not existing.get("per_model", {}).get(c)]
            if args.fill_missing and missing:
                print(f"[fill] {pass_name} {case_id}: re-running {missing}")
                for coder in missing:
                    t0 = time.time()
                    try:
                        rec, raw = CODERS[coder](case_id, pass_name, slice_text, cfg)
                    except Exception as exc:  # noqa: BLE001
                        print(f"  [{coder}] ERROR {type(exc).__name__}: {exc}")
                        rec, raw = None, f"[ERROR] {type(exc).__name__}: {exc}"
                    existing["per_model"][coder] = rec
                    existing.setdefault("per_model_raw", {})[coder] = raw
                    print(
                        f"  [{coder}] {'ok' if rec else 'FAILED'} ({time.time()-t0:.1f}s)"
                    )
                combined = combine(existing["per_model"], cfg["cells"], coders)
                existing["majority"] = combined["majority"]
                existing["flags"] = combined["flags"]
                existing["n_flags"] = sum(combined["flags"].values())
                out_file.write_text(json.dumps(existing, indent=2, ensure_ascii=False))
            else:
                print(f"[skip] {pass_name} {case_id} already coded")
            records.append(existing)
            continue
        per_model: dict = {}
        per_model_raw: dict = {}
        print(f"[{pass_name}] {case_id} {case_name}")
        for coder in coders:
            t0 = time.time()
            try:
                rec, raw = CODERS[coder](case_id, pass_name, slice_text, cfg)
            except Exception as exc:  # noqa: BLE001
                print(f"  [{coder}] ERROR {type(exc).__name__}: {exc}")
                rec, raw = None, f"[ERROR] {type(exc).__name__}: {exc}"
            per_model[coder] = rec
            per_model_raw[coder] = raw
            print(f"  [{coder}] {'ok' if rec else 'FAILED'} ({time.time()-t0:.1f}s)")
        combined = combine(per_model, cfg["cells"], coders)
        record = {
            "case_id": case_id,
            "case": case_name,
            "pass": pass_name,
            "coders": coders,
            "models": {c: MODEL_IDS[c] for c in coders},
            "sections_shown": list(cfg["sections"]),
            "per_model": per_model,
            "per_model_raw": per_model_raw,
            "majority": combined["majority"],
            "flags": combined["flags"],
            "n_flags": sum(combined["flags"].values()),
        }
        out_file.write_text(json.dumps(record, indent=2, ensure_ascii=False))
        records.append(record)
        print(f"  -> {out_file.name}  ({record['n_flags']} flagged cell(s))")
    return records


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", type=str, default=None, help="comma-separated case_ids")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--pass", dest="pass_", type=str, default="struct,outcome")
    ap.add_argument("--coders", type=str, default="claude,gemini,grok")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--fill-missing", action="store_true")
    args = ap.parse_args()

    coders = [c.strip() for c in args.coders.split(",") if c.strip()]
    for c in coders:
        if c not in CODERS:
            print(f"unknown coder: {c}", file=sys.stderr)
            return 2
    passes = [p.strip() for p in args.pass_.split(",") if p.strip()]
    for p in passes:
        if p not in PASS_CONFIG:
            print(f"unknown pass: {p}", file=sys.stderr)
            return 2

    dossiers = discover_dossiers()
    if args.only:
        want = {x.strip() for x in args.only.split(",")}
        dossiers = [d for d in dossiers if d[0] in want]
    if args.limit:
        dossiers = dossiers[: args.limit]

    print(
        f"Separated-pass re-coding: {len(dossiers)} dossiers, passes={passes}, "
        f"coders={coders}"
    )
    print(f"Models: claude={CLAUDE_MODEL} gemini={GEMINI_MODEL} grok={GROK_MODEL}")
    print("=" * 70)

    for pass_name in passes:
        records = run_pass(pass_name, dossiers, coders, args)
        if args.dry_run or not records:
            continue
        cfg = PASS_CONFIG[pass_name]
        kinfo = fleiss_kappa(records, cfg["binary_cells"], coders)
        (OUT_DIR / f"kappa_{pass_name}.json").write_text(
            json.dumps({"fleiss": kinfo}, indent=2)
        )
        k = kinfo.get("kappa")
        ktxt = f"{k:.3f}" if isinstance(k, float) else "n/a"
        total_flags = sum(r["n_flags"] for r in records)
        total_cells = len(records) * len(cfg["cells"])
        print("-" * 70)
        print(
            f"[{pass_name}] Fleiss' kappa ({'/'.join(cfg['binary_cells'])}) = {ktxt} "
            f"over {kinfo.get('n_items')} items; flags {total_flags}/{total_cells}"
        )
    print("=" * 70)
    print(f"Outputs in {OUT_DIR}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
