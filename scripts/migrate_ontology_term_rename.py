#!/usr/bin/env python3
"""G13 follow-on: rename `ontology_term` -> `ontology_id` on
PerturbationContext and StrainModification entries.

Schema convention reconciled in the same PR: the `term` / `<provenance>_term`
suffix is reserved for typed `Term`-object slots; bare-string CURIE slots
use the `<provenance>_id` convention. These two slots were the only
outliers and only 2 records carry the legacy field.

Idempotent; appends a CurationEvent via the G10 helper.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from culturemech.curate import record_curation_event  # noqa: E402

CURATOR = "migrate_ontology_term_rename.py"
ACTION = "MIGRATED_ONTOLOGY_TERM_RENAME"
DEFAULT_ROOT = "data/normalized_yaml"


def _rename_in_perturbations(perts: list) -> int:
    n = 0
    for p in perts or []:
        if isinstance(p, dict) and "ontology_term" in p and "ontology_id" not in p:
            p["ontology_id"] = p.pop("ontology_term")
            n += 1
    return n


def _rename_in_strain_mods(mods: list) -> int:
    n = 0
    for m in mods or []:
        if isinstance(m, dict) and "ontology_term" in m and "ontology_id" not in m:
            m["ontology_id"] = m.pop("ontology_term")
            n += 1
    return n


def migrate_one(path: Path, dry_run: bool) -> int:
    try:
        with path.open() as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError:
        return 0
    if not isinstance(data, dict):
        return 0
    total = 0
    for org in data.get("target_organisms") or []:
        if not isinstance(org, dict):
            continue
        for gm in org.get("growth_metrics") or []:
            if isinstance(gm, dict):
                total += _rename_in_perturbations(gm.get("perturbations") or [])
        total += _rename_in_strain_mods(org.get("strain_modifications") or [])
    if total == 0:
        return 0
    record_curation_event(
        data, curator=CURATOR, action=ACTION,
        notes=f"ontology_term->ontology_id for {total} entry/entries",
    )
    if not dry_run:
        with path.open("w") as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=80)
    return total


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=DEFAULT_ROOT)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    paths = sorted(Path(args.root).rglob("*.yaml"))
    renames = 0
    files = 0
    for p in paths:
        n = migrate_one(p, args.dry_run)
        if n:
            renames += n
            files += 1
    mode = "[DRY RUN] " if args.dry_run else ""
    print(f"{mode}scanned: {len(paths)}, files changed: {files}, renames: {renames}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
