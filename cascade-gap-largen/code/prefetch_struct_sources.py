#!/usr/bin/env python3
"""Batch pre-fetch of the N=350 full-draw STRUCTURAL source filings (step 4).

For every case in ``full_draw_selection.csv`` this fetches the DRAWN accession's
primary document (the closing-era 10-12B / DEFM14A / S-4 / Form 10 / 8-K named in the
row) and writes the stripped plain text to ``full_draw_dossiers/_raw/struct/P###.txt``
(git-ignored). It records a manifest row per case with the char count + status.

Why this exists (anti-fabrication, HARD): the dossier-building subagents must extract
structural facts from the REAL filing text -- never from recall. Pre-staging the drawn
source centrally (a) guarantees the accession in the row actually resolves, (b) surfaces
any dead/moved accession BEFORE a subagent is dispatched, and (c) lets each subagent
work from a fetched file it cites, so no accession is ever invented.

The OUTCOME source (3-5-year 10-K/20-F) is NOT pre-fetched here -- it is not named in
the draw and the subagent selects + fetches it via ``fetch_filing.py`` at build time.

Usage (from repo root):
  uv run python research/cascade-gap-largen/prefetch_struct_sources.py            # fetch all
  uv run python research/cascade-gap-largen/prefetch_struct_sources.py P001 P044  # only these
  uv run python research/cascade-gap-largen/prefetch_struct_sources.py --report   # manifest only

Polite: 0.2s spacing (fetch_filing.get already sleeps), skips files already present.
"""

from __future__ import annotations

import csv
import json
import sys
import urllib.error
from pathlib import Path

import fetch_filing as ff

HERE = Path(__file__).resolve().parent
SELECTION = HERE / "full_draw_selection.csv"
STRUCT_RAW = HERE / "full_draw_dossiers" / "_raw" / "struct"
MANIFEST = HERE / "full_draw_dossiers" / "_prefetch_manifest.csv"
FIELDS = ["case_id", "stratum", "role", "cik", "form", "accession", "chars", "status"]


def load_selection() -> list[dict]:
    with open(SELECTION, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def fetch_one(cik: str, accession: str) -> tuple[str, int]:
    """Return (stripped_text, chars). Raises on network / structure error."""
    accn = accession.replace("-", "")
    base = f"https://www.sec.gov/Archives/edgar/data/{str(cik).lstrip('0')}/{accn}"
    idx = json.loads(ff.get(f"{base}/index.json"))
    items = idx["directory"]["item"]
    htms = sorted(
        (i for i in items if i["name"].lower().endswith((".htm", ".html"))),
        key=ff._size,
        reverse=True,
    )
    cands = htms or [i for i in items if i["name"].lower().endswith(".txt")]
    if not cands:
        raise RuntimeError("no primary document in index")
    text = ff.strip_html(ff.get(f"{base}/{cands[0]['name']}"))
    return text, len(text)


def read_manifest() -> dict[str, dict]:
    if not MANIFEST.exists():
        return {}
    with open(MANIFEST, newline="", encoding="utf-8") as fh:
        return {r["case_id"]: r for r in csv.DictReader(fh)}


def write_manifest(rows: dict[str, dict]) -> None:
    ordered = sorted(rows.values(), key=lambda r: r["case_id"])
    with open(MANIFEST, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(ordered)


def report(rows: dict[str, dict]) -> None:
    from collections import Counter

    by_status = Counter(r["status"] for r in rows.values())
    print(f"manifest rows: {len(rows)}")
    for k, v in sorted(by_status.items()):
        print(f"  {k}: {v}")
    fails = [r for r in rows.values() if not r["status"].startswith("ok")]
    for r in sorted(fails, key=lambda r: r["case_id"]):
        print(f"  FAIL {r['case_id']} {r['form']} {r['accession']}: {r['status']}")


def main(argv: list[str]) -> int:
    if "--report" in argv:
        report(read_manifest())
        return 0
    only = {a for a in argv if a.startswith("P")}
    STRUCT_RAW.mkdir(parents=True, exist_ok=True)
    sel = load_selection()
    manifest = read_manifest()
    for row in sel:
        cid = row["case_id"]
        if only and cid not in only:
            continue
        out = STRUCT_RAW / f"{cid}.txt"
        if out.exists() and manifest.get(cid, {}).get("status", "").startswith("ok"):
            continue
        base = {
            "case_id": cid,
            "stratum": row["stratum"],
            "role": row["role"],
            "cik": row["cik"],
            "form": row["form"],
            "accession": row["accession"],
        }
        try:
            text, chars = fetch_one(row["cik"], row["accession"])
            out.write_text(text, encoding="utf-8")
            manifest[cid] = {**base, "chars": str(chars), "status": "ok"}
            print(f"[ok]   {cid} {row['form']:8} {chars:>9} chars", flush=True)
        except (urllib.error.URLError, RuntimeError, KeyError, ValueError) as exc:
            manifest[cid] = {**base, "chars": "0", "status": f"error:{exc}"[:120]}
            print(f"[FAIL] {cid} {row['form']:8} {row['accession']}: {exc}", flush=True)
        write_manifest(manifest)
    report(manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
