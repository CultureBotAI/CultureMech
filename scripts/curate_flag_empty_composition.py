#!/usr/bin/env python3
"""Flag media that carry no composition at all (#175).

A media record with no `ingredients` AND no `solutions` has no usable composition —
there is nothing to grow the organism in. `validate-strict` does not catch it
(`ingredients` is not required), so these sit in the corpus reading as complete.
226 media are in this state; 100 were just de-placeholdered (and already flagged),
but 126 carry no `data_quality_flags` at all — silently empty.

This stamps `incomplete_composition` on the unflagged ones so the gap is honest and
visible (the review-need ranking and any downstream reader can see it). It is
deliberately conservative: flagging records a value they lack, not deciding their
fate. Whether a given record is recoverable (re-import from its source), acceptably
empty, or spurious (a test fixture like test_medium_123 that should be retired) is a
per-record curation decision this does not make.

Report-only by default; `--apply` writes via record_io with a curation event.

Usage::

    just curate-flag-empty-composition
    just curate-flag-empty-composition --apply
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
INCOMPLETE = "incomplete_composition"


def has_no_composition(doc: dict[str, Any]) -> bool:
    ings = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    return not ings and not doc.get("solutions")


def needs_flag(doc: dict[str, Any]) -> bool:
    """A media record with no composition and no incomplete_composition flag."""
    return (not is_solution_record(doc)
            and has_no_composition(doc)
            and INCOMPLETE not in (doc.get("data_quality_flags") or []))


def scan_parsed(records) -> list[tuple[Path, dict[str, Any]]]:
    return [(p, d) for p, d in records if isinstance(d, dict) and needs_flag(d)]


def scan(normalized: Path) -> list[tuple[Path, dict[str, Any]]]:
    records = []
    for path in sorted(normalized.rglob("*.yaml")):
        try:
            records.append((path, yaml.safe_load(path.read_text(errors="replace"))))
        except (yaml.YAMLError, OSError):
            continue
    return scan_parsed(records)


def flag(doc: dict[str, Any]) -> bool:
    if not needs_flag(doc):
        return False
    doc.setdefault("data_quality_flags", []).append(INCOMPLETE)
    record_curation_event(
        doc, curator="curate_flag_empty_composition.py",
        action="FLAGGED_INCOMPLETE_COMPOSITION",
        notes="Media record has no ingredients and no solutions — no usable "
              "composition; flagged so the gap is not silent (#175).",
        changes=f"Added data_quality_flags: {INCOMPLETE}")
    return True


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--apply", action="store_true",
                    help="Write the flag. Default is report-only.")
    args = ap.parse_args(argv)

    affected = scan(args.normalized_dir)
    print(f"{len(affected)} media with no composition and no incomplete_composition flag:")
    for path, _doc in affected[:60]:
        print(f"  {path.relative_to(args.normalized_dir)}")
    if len(affected) > 60:
        print(f"  ... and {len(affected) - 60} more")

    if not args.apply:
        print("\nReport only. Re-run with --apply to flag them.")
        return 0

    written = sum(1 for path, doc in affected if flag(doc) and write_record(path, doc))
    print(f"\nFlagged {written} record(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
