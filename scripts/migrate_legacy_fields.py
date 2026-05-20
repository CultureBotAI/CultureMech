#!/usr/bin/env python3
"""Bulk migrations for legacy field shapes in CultureMech YAMLs.

Applies five mechanical migrations idempotently:

  G02  curation_history[*].date           -> timestamp (ISO-8601 with timezone)
  G04  references[*].reference_id          -> reference
  G05  category UPPERCASE                  -> lowercase
  G17  concentration.unit aliases:
         UG_PER_L  -> MICROG_PER_L
         PERCENT   -> PERCENT_W_V (when no W_V/V_V context is available)
  G19  preparation_steps[*].instruction    -> description (+ infer `action`
       from text when missing; PreparationActionEnum)

Every file modified gets a CurationEvent appended documenting which
migrations fired. Re-runs are no-ops.

Usage:
    python scripts/migrate_legacy_fields.py [--dry-run] [--root DIR]
"""

from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path
from typing import Any

import yaml

from culturemech.preparation_actions import infer_prep_action
from culturemech.curate.curation_event import record_curation_event

CURATOR = "migrate_legacy_fields.py"
ACTION = "MIGRATED_LEGACY_FIELDS"
DEFAULT_ROOT = "data/normalized_yaml"

VALID_CATEGORIES = {"algae", "bacterial", "fungal", "archaea", "specialized", "imported"}

UNIT_ALIASES = {
    "UG_PER_L": "MICROG_PER_L",
    "PERCENT": "PERCENT_W_V",
}


def to_iso_timestamp(value: Any) -> str | None:
    """Coerce a date/datetime/string to ISO-8601 with timezone.

    Returns None if the value can't be parsed reasonably.
    """
    if value is None:
        return None
    if isinstance(value, datetime.datetime):
        if value.tzinfo is None:
            value = value.replace(tzinfo=datetime.timezone.utc)
        return value.isoformat()
    if isinstance(value, datetime.date):
        return datetime.datetime.combine(value, datetime.time(0, 0, 0),
                                          tzinfo=datetime.timezone.utc).isoformat()
    if isinstance(value, str):
        text = value.strip()
        # Already-ISO with timezone -> leave as-is.
        if text.endswith("Z") or "+" in text[10:] or "-" in text[10:]:
            return text
        # Try full ISO datetime *first* so time components aren't truncated
        # by the date-only fallback (e.g. "2026-03-14T21:07:04.735164").
        try:
            dt = datetime.datetime.fromisoformat(text)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=datetime.timezone.utc)
            return dt.isoformat()
        except ValueError:
            pass
        # date-only string YYYY-MM-DD -> midnight UTC
        try:
            d = datetime.date.fromisoformat(text[:10])
            return datetime.datetime.combine(d, datetime.time(0, 0, 0),
                                              tzinfo=datetime.timezone.utc).isoformat()
        except ValueError:
            pass
        return None
    return None


def migrate_curation_history_date(recipe: dict) -> int:
    history = recipe.get("curation_history") or []
    n = 0
    for entry in history:
        if not isinstance(entry, dict):
            continue
        if "date" in entry and "timestamp" not in entry:
            new_ts = to_iso_timestamp(entry["date"])
            if new_ts:
                entry["timestamp"] = new_ts
                del entry["date"]
                n += 1
    return n


def migrate_reference_id(recipe: dict) -> int:
    refs = recipe.get("references") or []
    n = 0
    for ref in refs:
        if isinstance(ref, dict) and "reference_id" in ref and "reference" not in ref:
            ref["reference"] = ref.pop("reference_id")
            n += 1
    return n


def migrate_category_case(recipe: dict) -> int:
    cat = recipe.get("category")
    if isinstance(cat, str):
        lower = cat.lower()
        if cat != lower and lower in VALID_CATEGORIES:
            recipe["category"] = lower
            return 1
    return 0


def _walk_concentrations(obj: Any) -> int:
    n = 0
    if isinstance(obj, dict):
        if "unit" in obj and isinstance(obj["unit"], str):
            new_unit = UNIT_ALIASES.get(obj["unit"])
            if new_unit:
                obj["unit"] = new_unit
                n += 1
        for v in obj.values():
            n += _walk_concentrations(v)
    elif isinstance(obj, list):
        for v in obj:
            n += _walk_concentrations(v)
    return n


def migrate_unit_aliases(recipe: dict) -> int:
    return _walk_concentrations(recipe)


def migrate_preparation_step_instruction(recipe: dict) -> int:
    """Drop legacy ``instruction`` keys from preparation steps.

    The schema's ``PreparationStep`` class declares ``additionalProperties:
    false`` and requires ``description`` + ``action``. The legacy importers
    (and an earlier pass of this script) wrote ``instruction`` instead of
    ``description``; some records have only ``instruction``, others have
    both ``instruction`` and ``description`` after a partial migration.

    For every step we now:

    - drop ``instruction`` unconditionally if it is present (it is never
      schema-valid);
    - promote its value to ``description`` only if ``description`` is
      absent (don't overwrite curator-set descriptions);
    - back-fill ``action`` from the text when missing, using the same
      heuristic as the importers (``infer_prep_action``).
    """
    steps = recipe.get("preparation_steps") or []
    n = 0
    for step in steps:
        if not isinstance(step, dict):
            continue
        changed = False
        if "instruction" in step:
            legacy = step.pop("instruction")
            if "description" not in step and isinstance(legacy, str):
                step["description"] = legacy
            changed = True
        if "action" not in step and isinstance(step.get("description"), str):
            step["action"] = infer_prep_action(step["description"])
            changed = True
        if changed:
            n += 1
    return n


MIGRATIONS = [
    ("curation_history.date->timestamp", migrate_curation_history_date),
    ("references.reference_id->reference", migrate_reference_id),
    ("category->lowercase", migrate_category_case),
    ("concentration.unit aliases", migrate_unit_aliases),
    ("preparation_steps.instruction->description+action", migrate_preparation_step_instruction),
]


def migrate_one(path: Path, dry_run: bool) -> dict[str, int] | None:
    """Returns per-migration counts if any migrations fired, else None."""
    try:
        with path.open() as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError:
        return None
    if not isinstance(data, dict):
        return None
    counts: dict[str, int] = {}
    for name, fn in MIGRATIONS:
        n = fn(data)
        if n:
            counts[name] = n
    if not counts:
        return None
    notes = "; ".join(f"{k}={v}" for k, v in counts.items())
    record_curation_event(data, curator=CURATOR, action=ACTION, notes=notes)
    if not dry_run:
        with path.open("w") as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=80)
    return counts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=DEFAULT_ROOT)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, help="Migrate at most N files")
    args = ap.parse_args()

    paths = sorted(Path(args.root).rglob("*.yaml"))
    totals: dict[str, int] = {name: 0 for name, _ in MIGRATIONS}
    files_changed = 0
    for p in paths:
        counts = migrate_one(p, args.dry_run)
        if counts:
            files_changed += 1
            for k, v in counts.items():
                totals[k] += v
            if args.limit and files_changed >= args.limit:
                break

    mode = "[DRY RUN] " if args.dry_run else ""
    print(f"{mode}scanned: {len(paths)}, files changed: {files_changed}", file=sys.stderr)
    for k, v in totals.items():
        print(f"  {k}: {v}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
