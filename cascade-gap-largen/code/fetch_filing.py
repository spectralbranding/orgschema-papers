#!/usr/bin/env python3
"""EDGAR filing fetch + HTML-strip helper for building the pilot's separated
sub-dossiers (PILOT_PREREGISTRATION.md §3). Keeps large primary filings OUT of the
session context: it strips a filing's primary document to plain text under
`pilot_dossiers/_raw/` (git-ignored), which the dossier author then greps for the
specific structural / outcome facts to cite. Anti-fabrication: every fact written into
a sub-dossier must trace to a filing retrieved this way and cite its accession.

WebFetch/defuddle get 403 from EDGAR; this uses stdlib urllib with the required
User-Agent, at a polite 0.2s spacing under the 10 req/s limit.

Usage (from repo root):
  # list a registrant's filings of a form type (optionally a year) to find sources:
  uv run python research/cascade-gap-largen/fetch_filing.py list <cik> <form[,form]> [year]
  # fetch + strip a filing's primary document to pilot_dossiers/_raw/:
  uv run python research/cascade-gap-largen/fetch_filing.py doc <cik> <accession> [out.txt]
  # target a specific exhibit by filename substring (e.g. the EX-99.1 information
  # statement of a Form 10-12B carve-out, which is NOT the primaryDocument cover):
  uv run python research/cascade-gap-largen/fetch_filing.py doc <cik> <accession> [out.txt] --name ex99

Structural sources = closing-time filings (10-12B info statement / S-4 / DEFM14A /
Form 10 / 8-K); outcome sources = the 3-5-year-later 10-K / 20-F + press. Fix which
transaction's window is the outcome at construction (the E06 lesson).
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW_DIR = HERE / "pilot_dossiers" / "_raw"
UA = "Spectral Branding Research dmitry@spectralbranding.com"


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:  # noqa: S310 (trusted host)
        data = r.read()
    time.sleep(0.2)
    return data.decode("utf-8", "replace")


def pad(cik: str) -> str:
    return str(cik).lstrip("0").zfill(10)


def list_filings(cik: str, forms: str, year: str | None = None) -> None:
    want = {f.strip().upper() for f in forms.split(",")}
    d = json.loads(get(f"https://data.sec.gov/submissions/CIK{pad(cik)}.json"))
    rec = d["filings"]["recent"]
    for form, date, acc, doc, desc in zip(
        rec["form"],
        rec["filingDate"],
        rec["accessionNumber"],
        rec["primaryDocument"],
        rec["primaryDocDescription"],
    ):
        if form.upper() in want and (year is None or date.startswith(str(year))):
            print(f"{form:10} {date} {acc} {doc}  {desc}")


def strip_html(html: str) -> str:
    html = re.sub(r"(?is)<script.*?</script>", " ", html)
    html = re.sub(r"(?is)<style.*?</style>", " ", html)
    html = re.sub(r"(?s)<[^>]+>", " ", html)
    html = re.sub(r"&#160;|&nbsp;", " ", html)
    html = re.sub(r"&amp;", "&", html)
    html = re.sub(r"&#821[67]|&[lr]squo;", "'", html)
    html = re.sub(r"&#822[01]|&[lr]dquo;", '"', html)
    html = re.sub(r"&#8212;|&mdash;", "--", html)
    html = re.sub(r"&[a-z]+;", " ", html)
    html = re.sub(r"[ \t]+", " ", html)
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", html)


def _size(item: dict) -> int:
    try:
        return int(item.get("size", 0) or 0)
    except (ValueError, TypeError):
        return 0


def primary_doc_name(cik: str, accession: str) -> str | None:
    """The submissions API's primaryDocument for this accession, if resolvable.

    Preferred over the largest-.htm heuristic: for modern iXBRL 10-K/10-Q the largest
    .htm is the XBRL data exhibit, not the narrative the coder needs. Best-effort: the
    submissions API only carries recent filings, so this returns None for older ones and
    the caller falls back to the largest-.htm heuristic.
    """
    try:
        d = json.loads(get(f"https://data.sec.gov/submissions/CIK{pad(cik)}.json"))
        rec = d["filings"]["recent"]
        for acc, doc in zip(rec["accessionNumber"], rec["primaryDocument"]):
            if acc == accession and doc:
                return doc
    except (urllib.error.URLError, KeyError, ValueError):
        return None
    return None


def fetch_doc(
    cik: str, accession: str, out: str | None = None, name_filter: str | None = None
) -> None:
    accn = accession.replace("-", "")
    base = f"https://www.sec.gov/Archives/edgar/data/{str(cik).lstrip('0')}/{accn}"
    idx = json.loads(get(f"{base}/index.json"))
    items = idx["directory"]["item"]
    names = {i["name"] for i in items}
    htms = sorted(
        (i for i in items if i["name"].lower().endswith((".htm", ".html"))),
        key=_size,
        reverse=True,
    )
    cands = htms or [i for i in items if i["name"].lower().endswith(".txt")]
    if not cands:
        print("no document found")
        return
    if name_filter:
        # Explicit selector: the LARGEST .htm/.txt whose filename contains this
        # substring (case-insensitive). Needed for Form 10-12B carve-outs where the
        # substantive EX-99.1 information statement is NOT the primaryDocument cover.
        matches = [i for i in cands if name_filter.lower() in i["name"].lower()]
        if not matches:
            print(f"no document matching --name {name_filter!r}; available:")
            for i in cands:
                print(f"  {i['name']:44} {i.get('size', '')}")
            return
        name = matches[0]["name"]
    else:
        # Prefer the submissions-API primaryDocument (the narrative) when present in
        # the accession; else fall back to the largest-.htm heuristic.
        primary = primary_doc_name(cik, accession)
        name = primary if (primary and primary in names) else cands[0]["name"]
    text = strip_html(get(f"{base}/{name}"))
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = Path(out) if out else RAW_DIR / f"{cik}_{accn}.txt"
    out_path.write_text(text)
    print(f"wrote {len(text)} chars from {name} -> {out_path}")
    for i in items:
        if i["name"].lower().endswith((".htm", ".html", ".txt")):
            print(f"  {i['name']:44} {i.get('size', '')}")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    # Pull the optional --name SUBSTR selector out of argv (doc command only).
    name_filter: str | None = None
    args = sys.argv[1:]
    if "--name" in args:
        i = args.index("--name")
        name_filter = args[i + 1] if i + 1 < len(args) else None
        del args[i : i + 2]
    cmd = args[0]
    if cmd == "list":
        list_filings(args[1], args[2], args[3] if len(args) > 3 else None)
    elif cmd == "doc":
        fetch_doc(
            args[1],
            args[2],
            args[3] if len(args) > 3 else None,
            name_filter=name_filter,
        )
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
