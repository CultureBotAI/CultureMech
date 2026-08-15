#!/usr/bin/env python3
"""Remove ingredient rows that are exact duplicates of another row (#263).

33 records list the same ingredient twice at the same concentration. Anything that sums
or iterates `ingredients:` reads those recipes as double-strength in the repeated
components -- `for_dsm_14290.yaml` carries Tryptone 10 g/l, Yeast extract 5 g/l and
Sodium chloride 10 g/l twice each.

This was found via YAML anchors (`&id001` / `*id001`), which is how `yaml.dump` renders
a repeated row when it happens to be the same Python object. That framing was misleading
and #263 was filed with the wrong cause: the anchors are a symptom, the duplication is
the defect, and **16 of the affected records have no anchors at all**.

The dedup is deliberately narrow. Two rows are collapsed only when they are identical in
EVERY field -- name, concentration, term, notes, supplier_catalog, all of it. Removing an
exact copy cannot lose information.

Rows that share a name and concentration but differ anywhere else are LEFT ALONE and
reported. 21 such rows exist, differing in `notes`, `supplier_catalog` or `term`; they
look like the same ingredient recorded from two sources, but choosing which provenance
survives is a curation decision, not a mechanical one. A blind dedup would silently pick
whichever came first.

Read-only by default; `--apply` writes via record_io with a curation event.

Usage::

    just dedupe-identical-ingredients                    # report
    just dedupe-identical-ingredients --limit 1 --apply  # canary
    just dedupe-identical-ingredients --apply
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from record_io import write_record  # noqa: E402

from culturemech.curate.curation_event import record_curation_event  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"


def _blob(ing: dict[str, Any]) -> str:
    return json.dumps(ing, sort_keys=True, default=str)


def _key(ing: dict[str, Any]) -> tuple[str, str, str]:
    conc = ing.get("concentration") or {}
    return (str(ing.get("preferred_term")), str(conc.get("value")), str(conc.get("unit")))


def dedupe(doc: dict[str, Any]) -> tuple[list[str], list[str]]:
    """Drop exact-duplicate ingredient rows in place.

    Returns (removed_names, kept_but_differing_names). The second list is the reason
    this is not a one-liner: a same-name/same-value pair that differs in `notes` or
    `supplier_catalog` is not safe to collapse.
    """
    ingredients = doc.get("ingredients")
    if not isinstance(ingredients, list):
        return [], []

    seen: set[str] = set()
    by_key: dict[tuple[str, str, str], list[str]] = defaultdict(list)
    kept: list[Any] = []
    removed: list[str] = []
    for ing in ingredients:
        if not isinstance(ing, dict):
            kept.append(ing)
            continue
        blob = _blob(ing)
        by_key[_key(ing)].append(blob)
        if blob in seen:
            removed.append(str(ing.get("preferred_term")))
            continue
        seen.add(blob)
        kept.append(ing)

    differing = sorted({k[0] for k, blobs in by_key.items()
                        if len(blobs) > 1 and len(set(blobs)) > 1})
    if removed:
        doc["ingredients"] = kept
    return removed, differing


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="Write. Default is report-only.")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED)
    args = ap.parse_args(argv)

    total_removed = 0
    changed = 0
    differing_records: list[tuple[str, list[str]]] = []
    for path in sorted(args.yaml_dir.resolve().rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        if not isinstance(doc, dict):
            continue
        removed, differing = dedupe(doc)
        if differing:
            differing_records.append((path.name, differing))
        if not removed:
            continue
        changed += 1
        total_removed += len(removed)
        print(f"  {path.name[:52]:54s} -{len(removed)}: {', '.join(sorted(set(removed)))[:60]}")
        if args.apply:
            record_curation_event(
                doc, curator="dedupe_identical_ingredients.py",
                action="REMOVED_DUPLICATE_INGREDIENT_ROWS",
                notes=(f"Removed {len(removed)} ingredient row(s) that were identical in "
                       f"every field to another row in this record, which made the recipe "
                       f"read as double-strength in those components (#263): "
                       f"{', '.join(sorted(set(removed)))}."),
                changes=f"ingredients {len(doc['ingredients']) + len(removed)} -> "
                        f"{len(doc['ingredients'])}")
            write_record(path, doc)
        if args.limit and changed >= args.limit:
            break

    print(f"\n{'Removed' if args.apply else 'Would remove'} {total_removed} exact-duplicate "
          f"row(s) from {changed} record(s).")
    if differing_records:
        n = sum(len(d) for _, d in differing_records)
        print(f"\nLEFT ALONE — {n} ingredient(s) in {len(differing_records)} record(s) "
              f"repeat a name+concentration but differ in another field "
              f"(notes / supplier_catalog / term). Collapsing them means choosing which "
              f"provenance survives, which is a curation call:")
        for name, names in differing_records[:12]:
            print(f"  {name[:52]:54s} {', '.join(names)[:50]}")
    if not args.apply:
        print("\nReport only. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
