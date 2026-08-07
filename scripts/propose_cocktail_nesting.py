#!/usr/bin/env python3
"""Propose (never apply) how to nest each flattened stock cocktail (#150).

A "flattened cocktail" is a stock trace/vitamin solution whose components were
written straight into a medium's `ingredients:` at their stock-solution strength
(e.g. ZnSO4 22 G_PER_L), instead of nested under a `solutions:` object added at a
small volume. Read as final per-litre values those magnitudes are implausible;
the fix is structural — move the cocktail under a stock solution with an addition
volume, so `stock_conc x volume/1000` gives the real final concentration.

The audit (`audit_concentration_plausibility`) already finds the 579 records. The
missing, judgement-heavy piece is the **addition volume**, and a wrong volume
silently corrupts a real recipe. So this tool does NOT edit anything. It:

  1. Detects each flattened cocktail and its flagged component rows.
  2. Tries to recover the addition volume from the record's OWN preparation_steps /
     notes (e.g. "add 1 ml of trace element solution per litre") — recovered from
     tracked data, never invented (#166).
  3. Emits a per-record proposal: the components to nest, the recovered volume (with
     the sentence it came from) or `MANUAL` when none is confidently found, and the
     proposed nested-solution shape.

Apply nothing here. The output is a worklist for a curator to review and apply,
which is what a volume-sensitive structural repair needs.

Usage::

    just propose-cocktail-nesting               # summary + write the proposal TSV/JSON
    just propose-cocktail-nesting --top 20       # also print the first 20 proposals
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import audit_concentration_plausibility as acp  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
DEFAULT_OUT = REPO / "data" / "import_tracking" / "reports" / "cocktail_nesting_proposals.tsv"
# Authoritative addition volumes fetched from MediaDive (#150), when present. These
# beat anything scraped from the record's prose: MediaDive states the volume as a
# structured solution reference, so it is read rather than inferred.
MEDIADIVE_VOLUMES = REPO / "data" / "import_tracking" / "reports" / "mediadive_solution_volumes.json"

# A CANDIDATE addition volume: an amount in ml sitting next to a
# trace/vitamin/element solution word, AND in an addition context — an "add"-type
# verb or a per-litre phrase nearby. The context requirement cuts obvious false
# positives (a volume in "...except vitamins..." or in an unrelated comment). Even
# so these are candidates a curator must verify against `volume_evidence`, never
# auto-applied — which is the whole point of this being a proposal.
_SOLUTION_WORD = r"(?:trace|vitamin|element|mineral|selenite|tungstate|SL-?\d+|metal)s?[\w \-]*?(?:solution|elements?)?"
_VOL = r"(\d+(?:\.\d+)?)\s*(?:ml|millilit(?:er|re)s?)\b"
_NEAR_VOL = re.compile(rf"(?:{_SOLUTION_WORD}[^.]{{0,40}}?({_VOL}))|(?:({_VOL})[^.]{{0,40}}?{_SOLUTION_WORD})", re.I)
_ADD_CONTEXT = re.compile(r"\b(?:add|added|adding|supplement|per\s+lit(?:er|re)|/\s*l\b|per\s+l\b)", re.I)


def recover_volume(doc: dict[str, Any]) -> tuple[str, str]:
    """(candidate_volume_ml, evidence_sentence) recovered from the record itself, or
    ("", ""). Requires an addition context in the sentence to avoid grabbing a volume
    that is merely near a solution word."""
    sentences: list[str] = []
    for step in doc.get("preparation_steps") or []:
        if isinstance(step, dict) and step.get("description"):
            sentences.append(str(step["description"]))
    if doc.get("notes"):
        sentences.append(str(doc["notes"]))
    for s in sentences:
        if not _ADD_CONTEXT.search(s):
            continue
        m = _NEAR_VOL.search(s)
        if m:
            vol = next(g for g in m.groups() if g and re.fullmatch(r"\d+(?:\.\d+)?", g))
            return vol, s.strip()[:160]
    return "", ""


def cocktail_components(rows: list[dict[str, str]], file_path: str) -> list[dict[str, str]]:
    """The flagged trace/vitamin rows for one record — the components to nest."""
    return [{"ingredient": r["ingredient"], "value": r["value"], "unit": r["unit"],
             "finding": r["finding"]}
            for r in rows if r["file_path"] == file_path
            and r["finding"] in ("TRACE_SALT_AS_STOCK", "INDICATOR_UNIT_SLIP")]


def load_mediadive_volumes() -> dict[str, Any]:
    """Authoritative addition volumes, keyed by record path, if they were fetched."""
    if not MEDIADIVE_VOLUMES.is_file():
        return {}
    try:
        return json.loads(MEDIADIVE_VOLUMES.read_text())
    except (json.JSONDecodeError, OSError):
        return {}


def build_proposals() -> list[dict[str, Any]]:
    rows = acp.audit(NORMALIZED)
    summary = acp.summarize_records(rows, NORMALIZED)
    cocktail_paths = [s["file_path"] for s in summary if s["flattened_cocktail"] == "yes"]
    mediadive = load_mediadive_volumes()
    proposals = []
    for fp in sorted(cocktail_paths):
        try:
            doc = yaml.safe_load((NORMALIZED / fp).read_text(errors="replace")) or {}
        except (yaml.YAMLError, OSError):
            doc = {}
        comps = cocktail_components(rows, fp)
        vol, evidence = recover_volume(doc)
        # MediaDive states the volume structurally, so it supersedes a prose scrape.
        additions = (mediadive.get(fp) or {}).get("additions") or []
        if additions:
            a = additions[0]
            vol = str(a.get("addition_volume_ml") or vol)
            evidence = (f"MediaDive {(mediadive[fp]).get('mediadive_id')}: "
                        f"{a.get('solution_name')} added at {a.get('addition_volume_ml')} ml "
                        f"(stock prepared in {a.get('stock_prepared_in_ml')} ml)")
        proposals.append({
            "file_path": fp,
            "record_id": str(doc.get("id") or ""),
            "n_components": len(comps),
            "components": "; ".join(f"{c['ingredient']}={c['value']}{c['unit']}" for c in comps),
            "candidate_volume_ml": vol,
            # MEDIADIVE = read from a structured solution reference (authoritative,
            # applyable). preparation_steps/notes = scraped from prose (a candidate a
            # curator must verify). MANUAL = nothing found.
            "volume_source": ("MEDIADIVE" if additions
                              else "preparation_steps/notes" if vol else "MANUAL"),
            "volume_evidence": evidence,
            # The proposed nested shape (curator applies): the flagged components move
            # under one solution added at candidate_volume_ml per litre.
            "proposed_solution": json.dumps({
                "preferred_term": "Trace/vitamin stock (nested from flattened ingredients)",
                "addition_volume": {"value": vol or "TBD", "unit": "MILLILITERS_PER_LITER"},
                "composition": [{"preferred_term": c["ingredient"],
                                 "concentration": {"value": c["value"], "unit": c["unit"]}}
                                for c in comps],
            }),
        })
    return proposals


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--top", type=int, default=0, help="Also print the first N proposals.")
    args = ap.parse_args(argv)

    proposals = build_proposals()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    cols = ["file_path", "record_id", "n_components", "components",
            "candidate_volume_ml", "volume_source", "volume_evidence", "proposed_solution"]
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=cols)
        w.writeheader()
        w.writerows(proposals)
    args.out.with_suffix(".json").write_text(json.dumps(proposals, indent=2) + "\n")

    recoverable = [p for p in proposals if p["candidate_volume_ml"]]
    print(f"Flattened cocktails proposed: {len(proposals)}")
    print(f"  candidate addition volume found in the record (verify vs evidence): {len(recoverable)}")
    print(f"  volume MANUAL (needs a curator / an external source): {len(proposals) - len(recoverable)}")
    print(f"\nProposal only — NOTHING is applied. Review {args.out.relative_to(REPO)} and apply per record.")
    for p in proposals[:args.top]:
        print(f"\n  {p['file_path']}  ({p['n_components']} components, vol={p['candidate_volume_ml'] or 'MANUAL'})")
        if p["volume_evidence"]:
            print(f"    evidence: {p['volume_evidence']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
