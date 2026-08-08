#!/usr/bin/env python3
"""List the flattened cocktails that need literature research, and why (#150).

The cocktail repair nests a stock solution back under `solutions:` with the volume
it is added at. Both facts come from MediaDive for the records that resolve there.
This lists the ones that do NOT, so they can be sent to Edison
(`templates/media_stock_solution_research.md`) instead — and, just as usefully,
records the reason each is blocked so the population is not treated as homogeneous.

## Reasons

id resolves to a DIFFERENT medium
    The record's id translates to a MediaDive medium whose NAME disagrees. Almost
    always a KOMODO id: DSMZ medium numbers are MediaDive ids, but the KOMODO->DSMZ
    mapping is 43.5% bare identity and MediaDive has renumbered since (#244). The
    record's own id is fine; there is simply no trustworthy MediaDive counterpart.

no MediaDive-resolvable id
    A JCM/TOGO/CCAP-sourced record. MediaDive does not serve these.

resolved but no cocktail stock in MediaDive
    The medium was found and matched by name, but its recipe references no
    trace/vitamin stock — so the flattening came from somewhere else.

Read-only. Output feeds `research_media_edison.py --batch`.

Usage::

    just list-cocktail-research-targets
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
NORMALIZED = REPO / "data" / "normalized_yaml"
REPORTS = REPO / "data" / "import_tracking" / "reports"
PROPOSALS = REPORTS / "cocktail_nesting_proposals.tsv"
VOLUMES = REPORTS / "mediadive_solution_volumes.json"
DEFAULT_OUT = REPORTS / "cocktail_research_targets.json"


def build() -> list[dict[str, str]]:
    if not PROPOSALS.is_file():
        print(f"Run `just propose-cocktail-nesting` first — {PROPOSALS.name} missing.",
              file=sys.stderr)
        return []
    volumes = json.loads(VOLUMES.read_text()) if VOLUMES.is_file() else {}

    out = []
    with PROPOSALS.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            rel = row["file_path"]
            try:
                doc = yaml.safe_load((NORMALIZED / rel).read_text(errors="replace"))
            except (yaml.YAMLError, OSError):
                continue
            if not isinstance(doc, dict) or doc.get("solutions"):
                continue                      # already repaired
            info = volumes.get(rel)
            if info and info.get("name_mismatch"):
                reason = "id resolves to a DIFFERENT medium"
            elif info and info.get("additions"):
                continue                      # MediaDive has the data; not blocked
            elif info:
                reason = "resolved but no cocktail stock in MediaDive"
            else:
                reason = "no MediaDive-resolvable id"
            out.append({
                "file_path": rel,
                "record_id": row["record_id"],
                "name": str(doc.get("original_name") or doc.get("name") or ""),
                "n_components": row["n_components"],
                "reason": reason,
            })
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--reason", help="Only targets with this blocking reason.")
    args = ap.parse_args(argv)

    targets = build()
    if args.reason:
        targets = [t for t in targets if t["reason"] == args.reason]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(targets, indent=2) + "\n")

    print(f"Flattened cocktails still needing a stock + volume: {len(targets)}")
    for reason, n in Counter(t["reason"] for t in targets).most_common():
        print(f"  {n:5d}  {reason}")

    # Many are near-duplicate variants of one base medium ("MEDIUM 252 MODIFIED FOR
    # DSM ..."), so researching the base answers all of them. Worth knowing before
    # spending research time per record.
    import re

    def base(name: str) -> str:
        n = re.sub(r"\s*(modified\s+)?for dsm.*", "", name.lower())
        return re.sub(r"[^a-z0-9]+", " ", n).strip()

    clusters = Counter(base(t["name"]) for t in targets)
    multi = {k: v for k, v in clusters.items() if v > 1 and k}
    print(f"\n  distinct base media: {len(clusters)} "
          f"({sum(multi.values())} records fall into {len(multi)} multi-record clusters)")
    for k, v in Counter(multi).most_common(5):
        print(f"    {v:4d}x  {k[:56]}")
    print(f"\nWrote {args.out.relative_to(REPO)} — feed to "
          f"`research_media_edison.py --batch`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
