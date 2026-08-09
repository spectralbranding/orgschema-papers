"""POST-HOC diagnostic: does the index have any dynamic range at all?

NOT pre-registered. This was written AFTER seeing the placebo result and is labelled
post-hoc for exactly that reason -- `PRE_EXPERIMENT_NOTES.md` fixed the placebo, and this
question was not in it.

Why it exists. The placebo returned both panels at the ceiling: zero-activity M = .997
(SD .005), operating M = .999 (SD .001), on a [0, 1] rescaled cosine. Before any of that is
interpreted as a fact about firms, one alternative has to be ruled out: that the measure as
constructed cannot discriminate ANY two 10-K narratives, in which case the ceiling is a
property of the construction and says nothing about zero-activity filers.

The test is simple and decisive. Compute the same index between narratives of DIFFERENT,
unrelated firms in different years. Those pairs share nothing but the genre.

    If cross-firm cosine is far below within-firm cosine, the measure discriminates and the
    ceiling is a real finding about how little 10-K narrative changes year over year.

    If cross-firm cosine is close to within-firm cosine, the measure is degenerate under this
    construction, the placebo comparison is uninformative, and nothing about the panels can
    be concluded from it.

Reuses the placebo's cached filings, so it re-runs offline in about a minute.

Run:
    uv run --with torch --with transformers python code/ceiling_diagnostic.py
"""

from __future__ import annotations

import csv
import json
import random
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from zero_activity_placebo import (  # noqa: E402
    ITEM7_END,
    ITEM7_START,
    OUT,
    SEED,
    Embedder,
    bow_cosine,
    extract_section,
    fetch,
    fmt,
    rescale,
    to_text,
)


def load_panel(name: str) -> list[dict]:
    p = OUT / name
    with p.open() as f:
        return list(csv.DictReader(f, delimiter=";"))


def main() -> int:
    rng = random.Random(SEED)
    rows = load_panel("panel_zero.csv") + load_panel("panel_operating.csv")
    print(f"loaded {len(rows)} firm-pairs from the placebo panels")

    # Rebuild each firm's year-t MD&A from the cache. One document per firm is enough --
    # the question is whether two DIFFERENT firms look different.
    docs: list[tuple[str, str]] = []
    for r in rows:
        raw = fetch(r["url_t"])
        if not raw:
            continue
        sec = extract_section(to_text(raw), ITEM7_START, ITEM7_END)
        if sec and len(sec.split()) >= 200:
            docs.append((r["name"], sec))
    print(f"rebuilt {len(docs)} year-t MD&A sections")
    if len(docs) < 10:
        print("ABORT: too few sections to say anything.")
        return 2

    emb = Embedder()
    vecs = {}
    for i, (name, text) in enumerate(docs, 1):
        v = emb.embed(text)
        if v is not None:
            vecs[name] = (v, text)
        if i % 10 == 0:
            print(f"  embedded {i}/{len(docs)}")

    names = list(vecs)
    pairs = set()
    while len(pairs) < min(200, len(names) * (len(names) - 1) // 2):
        a, b = rng.sample(names, 2)
        pairs.add(tuple(sorted((a, b))))

    cross_bert = [rescale(emb.cosine(vecs[a][0], vecs[b][0])) for a, b in pairs]
    cross_bow = [rescale(bow_cosine(vecs[a][1], vecs[b][1])) for a, b in pairs]

    within = json.loads((OUT / "results.json").read_text())
    w_bert_zero = within["primary"]["mean_zero"]
    w_bert_op = within["primary"]["mean_operating"]
    w_bow_zero = within["bow"]["mean_zero"]
    w_bow_op = within["bow"]["mean_operating"]

    cb_m, cb_sd = statistics.fmean(cross_bert), statistics.stdev(cross_bert)
    cw_m, cw_sd = statistics.fmean(cross_bow), statistics.stdev(cross_bow)

    print("\n=== dynamic range ===")
    print(f"  BERT  within-firm (zero-activity) M = {fmt(w_bert_zero)}")
    print(f"  BERT  within-firm (operating)     M = {fmt(w_bert_op)}")
    print(
        f"  BERT  CROSS-firm, unrelated pairs M = {fmt(cb_m)} (SD {fmt(cb_sd)}, n={len(cross_bert)})"
    )
    print(f"  -> BERT separation, within minus cross: {fmt(w_bert_op - cb_m)}")
    print()
    print(f"  BOW   within-firm (zero-activity) M = {fmt(w_bow_zero)}")
    print(f"  BOW   within-firm (operating)     M = {fmt(w_bow_op)}")
    print(
        f"  BOW   CROSS-firm, unrelated pairs M = {fmt(cw_m)} (SD {fmt(cw_sd)}, n={len(cross_bow)})"
    )
    print(f"  -> BOW separation, within minus cross: {fmt(w_bow_op - cw_m)}")

    # The verdict rule for THIS diagnostic, stated in the module docstring before the run:
    # a measure that cannot separate unrelated firms by more than it separates a firm from
    # itself has no dynamic range to carry a construct.
    bert_sep = w_bert_op - cb_m
    bow_sep = w_bow_op - cw_m
    if bert_sep < 0.01:
        verdict = "DEGENERATE (BERT construction)"
        why = (
            "cross-firm narratives score essentially as similar as a firm to itself, so the "
            "ceiling is a property of the embedding construction and the placebo comparison "
            "cannot be interpreted as a fact about zero-activity filers"
        )
    elif bert_sep < 0.05:
        verdict = "NARROW"
        why = "the measure separates unrelated firms only marginally; treat any small difference with suspicion"
    else:
        verdict = "DISCRIMINATES"
        why = "the measure clearly separates unrelated firms, so the high within-firm scores are a real finding"
    print(f"\nDIAGNOSTIC VERDICT: {verdict} — {why}")

    (OUT / "ceiling_diagnostic.json").write_text(
        json.dumps(
            {
                "n_docs": len(vecs),
                "n_cross_pairs": len(cross_bert),
                "bert_within_zero": w_bert_zero,
                "bert_within_operating": w_bert_op,
                "bert_cross_mean": cb_m,
                "bert_cross_sd": cb_sd,
                "bert_separation": bert_sep,
                "bow_within_zero": w_bow_zero,
                "bow_within_operating": w_bow_op,
                "bow_cross_mean": cw_m,
                "bow_cross_sd": cw_sd,
                "bow_separation": bow_sep,
                "verdict": verdict,
                "reason": why,
                "post_hoc": True,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"wrote {OUT}/ceiling_diagnostic.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
