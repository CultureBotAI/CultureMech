#!/usr/bin/env python3
"""Remove the "See source for composition" placeholder ingredient (#175).

100 media carry a single fake ingredient whose `preferred_term` is literally
"See source for composition" (value `variable`), a uniform import artifact — one
import path, not scattered gaps. The placeholder is not a component: it is a note
that the composition was never imported, and it is already recorded as such by a
`data_quality_flags: incomplete_composition` entry on 99 of the 100.

The harm is that the fake term matches every ingredient/text scan, so these records
look composed when they are empty — which is exactly how #175 surfaced them. This
lifts the placeholder out of `ingredients` (leaving the record honestly empty) and
guarantees the `incomplete_composition` flag, so the "no usable composition" state
is carried by the flag, not by a component that pollutes searches. It does NOT
attempt to recover the real composition — a re-import from the source database is
separate, and this does not foreclose it.

Report-only by default; `--apply` writes via record_io with a curation event.

Usage::

    just curate-placeholder-composition
    just curate-placeholder-composition --apply
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import write_record  # noqa: E402
from record_kinds import is_solution_record  # noqa: E402

from culturemech.curate.curation_event import record_curation_event  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
PLACEHOLDER = "see source for composition"
INCOMPLETE = "incomplete_composition"


def is_placeholder(ingredient: Any) -> bool:
    return (isinstance(ingredient, dict)
            and PLACEHOLDER in str(ingredient.get("preferred_term") or "").strip().lower())


def scan_parsed(records) -> list[tuple[Path, dict[str, Any]]]:
    """MEDIA records carrying the placeholder ingredient, from parsed (path, doc)
    pairs. Stock-solution records are excluded — #175 is about media composition,
    and ~4,775 solutions carry the same placeholder as a separate population."""
    out = []
    for path, doc in records:
        if not isinstance(doc, dict) or is_solution_record(doc):
            continue
        if any(is_placeholder(i) for i in doc.get("ingredients") or []):
            out.append((path, doc))
    return out


def scan(normalized: Path) -> list[tuple[Path, dict[str, Any]]]:
    records = []
    for path in sorted(normalized.rglob("*.yaml")):
        try:
            records.append((path, yaml.safe_load(path.read_text(errors="replace"))))
        except (yaml.YAMLError, OSError):
            continue
    return scan_parsed(records)


def repair(doc: dict[str, Any]) -> bool:
    """Drop the placeholder ingredient and guarantee the incomplete flag. Returns
    True if anything changed."""
    kept = [i for i in doc.get("ingredients") or [] if not is_placeholder(i)]
    if len(kept) == len(doc.get("ingredients") or []):
        return False
    doc["ingredients"] = kept
    flags = doc.setdefault("data_quality_flags", [])
    added_flag = INCOMPLETE not in flags
    # Only claim the record is empty when removing the placeholder actually left it
    # so; a placeholder sitting among real ingredients just gets de-polluted.
    if not kept and added_flag:
        flags.append(INCOMPLETE)
    note = ("Removed the 'See source for composition' placeholder ingredient; the "
            "record carries no imported composition and is flagged incomplete (#175)."
            if not kept else
            "Removed the 'See source for composition' placeholder from among real "
            "ingredients (#175).")
    record_curation_event(doc, curator="curate_placeholder_composition.py",
                          action="REMOVED_PLACEHOLDER_INGREDIENT", notes=note,
                          changes="Dropped placeholder ingredient 'See source for composition'"
                          + ("; added incomplete_composition flag" if (not kept and added_flag) else ""))
    return True


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--apply", action="store_true",
                    help="Write the repair. Default is report-only.")
    args = ap.parse_args(argv)

    affected = scan(args.normalized_dir)
    print(f"{len(affected)} record(s) carry the 'See source for composition' placeholder:")
    for path, _doc in affected[:60]:
        print(f"  {path.relative_to(args.normalized_dir)}")
    if len(affected) > 60:
        print(f"  ... and {len(affected) - 60} more")

    if not args.apply:
        print("\nReport only. Re-run with --apply to remove the placeholder.")
        return 0

    written = 0
    for path, doc in affected:
        if repair(doc) and write_record(path, doc):
            written += 1
    print(f"\nRepaired {written} record(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
