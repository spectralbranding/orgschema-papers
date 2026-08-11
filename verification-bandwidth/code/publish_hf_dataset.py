#!/usr/bin/env python3
"""Create + populate the 2026bn derived-results dataset repo on Hugging Face.

Run (token injected by BWS, never printed):
    bws run -- uv run --with huggingface_hub --with numpy --with scipy python \
        code/publish_hf_dataset.py

Idempotent: create_repo(exist_ok=True); upload_folder overwrites by path.
The USER mints the dataset DOI on HF after the first drop (Settings -> DOI); the
DOI then goes into the paper's availability section and the Zenodo metadata.

WHAT IS UPLOADED, AND WHY IT NEEDS NO REDACTION. This paper collected no data.
Every figure it reports is either arithmetic on another study's published summary
statistics or a seeded simulation of a stated model, so there is no third-party
text to withhold, no participant record, and no provider credential anywhere in
the pipeline. That is the opposite of the predecessor drop's situation and it is
why there is no redactor here: the whole tree is publishable as it sits.

THE GATE THIS SCRIPT DOES ENFORCE is the one that matters for a derived-results
record: that the tables being published still match the derivations that own
them. It re-runs the emitter into a scratch directory and compares byte-for-byte
against the committed tables. A drop whose tables no longer reproduce is a drop
that would publish a number the paper cannot defend, so any mismatch ABORTS and
nothing is uploaded.
"""

from __future__ import annotations

import filecmp
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from huggingface_hub import HfApi

PAPER_DIR = Path(__file__).resolve().parents[1]
CODE_DIR = PAPER_DIR / "code"
SLUG = "verification-bandwidth-derived-results"


def verify_tables(scratch: Path) -> None:
    """Re-emit the deterministic tables and compare against what is committed.

    The emitter writes to ../output/tables relative to itself, so it is copied
    into a scratch tree to regenerate without touching the working copy.
    """
    sandbox = scratch / "sandbox"
    (sandbox / "output" / "tables").mkdir(parents=True)
    shutil.copytree(CODE_DIR, sandbox / "code", dirs_exist_ok=True)

    proc = subprocess.run(
        [sys.executable, "emit_paper_tables.py"],
        cwd=str(sandbox / "code"),
        capture_output=True,
        text=True,
    )
    sys.stdout.write(proc.stdout)
    sys.stderr.write(proc.stderr)
    if proc.returncode != 0:
        raise SystemExit("ABORTED: the table emitter failed. Nothing uploaded.")

    committed = PAPER_DIR / "output" / "tables"
    regenerated = sandbox / "output" / "tables"
    names = sorted(p.name for p in committed.glob("*.csv"))
    if not names:
        raise SystemExit("ABORTED: no committed tables to publish. Nothing uploaded.")

    mismatched = [
        n
        for n in names
        if not (regenerated / n).exists()
        or not filecmp.cmp(committed / n, regenerated / n, shallow=False)
    ]
    if mismatched:
        raise SystemExit(
            "ABORTED: these tables no longer reproduce from their derivations: "
            + ", ".join(mismatched)
            + ". Re-run reproduce.sh and reconcile the paper before publishing."
        )
    print(
        f"VERIFY OK: {len(names)} tables reproduce byte-for-byte from the derivations"
    )


def build_release(scratch: Path) -> Path:
    """Assemble the upload tree: the card as README, plus the generated output."""
    root = scratch / "release_hf"
    root.mkdir()
    (root / "README.md").write_bytes((PAPER_DIR / "HF_DATASET_CARD.md").read_bytes())
    for sub in ("tables", "logs", "figures"):
        src = PAPER_DIR / "output" / sub
        if not src.is_dir():
            continue
        dst = root / sub
        dst.mkdir()
        for f in sorted(src.iterdir()):
            if f.is_file() and f.name != ".gitkeep":
                shutil.copy2(f, dst / f.name)
    return root


def main() -> int:
    token = os.environ.get("HUGGINGFACE_API_KEY")
    if not token:
        print("ERROR: HUGGINGFACE_API_KEY not in environment (run via `bws run --`).")
        return 2

    api = HfApi(token=token)
    print(f"authenticated as: {api.whoami().get('name')!r}")
    repo_id = f"spectralbranding/{SLUG}"

    with tempfile.TemporaryDirectory() as td:
        scratch = Path(td)
        verify_tables(scratch)
        root = build_release(scratch)
        files = sorted(
            p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()
        )
        print(f"staged {len(files)} files:")
        for f in files:
            print(f"    {f}")

        url = api.create_repo(
            repo_id=repo_id, repo_type="dataset", private=False, exist_ok=True
        )
        print(f"repo ready: {url}")
        api.upload_folder(
            folder_path=str(root),
            repo_id=repo_id,
            repo_type="dataset",
            commit_message=(
                "2026bn derived results: emitted tables, run logs and figures "
                "from the seeded companion computation"
            ),
        )
        print(f"uploaded {len(files)} files -> {repo_id}")

    print(
        "\nDONE. The dataset DOI is 10.57967/hf/9953 and is already carried by the paper's\n"
        "availability section and by the card; re-minting is not needed on a re-drop."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
