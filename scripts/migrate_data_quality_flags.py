#!/usr/bin/env python3
"""Migrate dict-shape `data_quality_flags` to the schema's list shape.

The schema declares `MediaRecipe.data_quality_flags` as `range: string,
multivalued: true` (a list of strings). 273 records carry a dict like:

    data_quality_flags:
      incomplete_composition: false
      has_ontology_mappings: true
      ingredients_curated: true
      curation_method: automated_expert_mapping

This script rewrites those to the conventional list shape:
  - boolean True keys become flag names (e.g. `has_ontology_mappings`)
  - boolean False keys are dropped (absence == false)
  - non-boolean fields become `key:value` strings (e.g.
    `curation_method:automated_expert_mapping`) — matches the in-corpus
    convention already used by 5,220 list-shape records.

Appends a CurationEvent on rewrite so the migration is auditable.

Usage:
    python scripts/migrate_data_quality_flags.py [--dry-run] [--limit N]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from culturemech.curate import record_curation_event  # noqa: E402

CURATOR = "migrate_data_quality_flags.py"
ACTION = "MIGRATED_DATA_QUALITY_FLAGS"
DEFAULT_ROOT = "data/normalized_yaml"


def dict_to_list(flags: dict) -> list[str]:
    out: list[str] = []
    for key, value in flags.items():
        if isinstance(value, bool):
            if value:
                out.append(key)
        else:
            out.append(f"{key}:{value}")
    return out


def append_curation_event(recipe: dict, before_count: int, after_count: int) -> None:
    record_curation_event(
        recipe,
        curator=CURATOR,
        action=ACTION,
        notes=f"dict({before_count} keys) -> list({after_count} entries)",
    )


def migrate_one(path: Path, dry_run: bool) -> bool:
    """Returns True if file was migrated."""
    try:
        with path.open() as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError:
        return False
    if not isinstance(data, dict):
        return False
    flags = data.get("data_quality_flags")
    if not isinstance(flags, dict):
        return False
    before = len(flags)
    new = dict_to_list(flags)
    data["data_quality_flags"] = new
    append_curation_event(data, before, len(new))
    if not dry_run:
        with path.open("w") as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=80)
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=DEFAULT_ROOT, help="Directory tree to walk")
    ap.add_argument("--dry-run", action="store_true", help="Don't write files")
    ap.add_argument("--limit", type=int, help="Process at most N migrations")
    args = ap.parse_args()

    paths = sorted(Path(args.root).rglob("*.yaml"))
    migrated = 0
    scanned = 0
    for p in paths:
        scanned += 1
        if migrate_one(p, args.dry_run):
            migrated += 1
            if args.limit and migrated >= args.limit:
                break

    mode = "[DRY RUN] " if args.dry_run else ""
    print(f"{mode}scanned: {scanned}, migrated: {migrated}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
