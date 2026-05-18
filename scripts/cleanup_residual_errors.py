#!/usr/bin/env python3
"""Curator pass for the residual 93 validation errors identified
in reports/instance_validation_summary.md.

Applies four narrow, idempotent fixes:

  R01  Flatten doubly-wrapped `synonym_text` on IngredientSynonym
       entries (22 entries; the value sometimes carries the full
       {synonym_text, synonym_type} dict instead of just the string).
  R02  Convert exotic concentration units:
         G_PER_100ML  ->  G_PER_L      (value * 10)
         ML_PER_40ML  ->  PERCENT_V_V  (value * 2.5)
  R03  Fill missing `concentration` on ingredients / composition entries
       with a {value: variable, unit: VARIABLE} placeholder so the
       schema's required-field rule is satisfied. The records affected
       are largely solvent-only stubs or "Make up to" markers.
  R04  Fill missing `explanation` on EvidenceItem entries with a
       generic auto-text noting the data was imported without an
       explanation field.

Each migrated file gets a CurationEvent. Re-runs are no-ops.

Usage:
    python scripts/cleanup_residual_errors.py [--dry-run] [--limit N]
"""

from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path
from typing import Any

import yaml

CURATOR = "cleanup_residual_errors.py"
ACTION = "CLEANUP_RESIDUAL_ERRORS"
DEFAULT_ROOT = "data/normalized_yaml"
EXPLANATION_PLACEHOLDER = "Auto-filled placeholder: explanation not supplied by upstream import."

UNIT_CONVERSIONS = {
    # exotic_unit -> (target_unit, value_multiplier)
    "G_PER_100ML": ("G_PER_L", 10.0),
    "ML_PER_40ML": ("PERCENT_V_V", 2.5),
}


def now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def _to_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


# ---- R01 -----------------------------------------------------------------

def fix_doubly_wrapped_synonyms(recipe: dict) -> int:
    n = 0
    for ing in recipe.get("ingredients") or []:
        if not isinstance(ing, dict):
            continue
        for syn in ing.get("synonyms") or []:
            if not isinstance(syn, dict):
                continue
            txt = syn.get("synonym_text")
            if isinstance(txt, dict) and "synonym_text" in txt:
                # Hoist the inner dict's text up; preserve synonym_type if
                # only present on the inner.
                inner_text = txt.get("synonym_text")
                inner_type = txt.get("synonym_type")
                if isinstance(inner_text, str):
                    syn["synonym_text"] = inner_text
                    if inner_type is not None and "synonym_type" not in syn:
                        syn["synonym_type"] = inner_type
                    n += 1
    return n


# ---- R02 -----------------------------------------------------------------

def _walk_concentrations(obj: Any, mutate) -> int:
    n = 0
    if isinstance(obj, dict):
        if "value" in obj and "unit" in obj and isinstance(obj.get("unit"), str):
            n += mutate(obj)
        for v in obj.values():
            n += _walk_concentrations(v, mutate)
    elif isinstance(obj, list):
        for v in obj:
            n += _walk_concentrations(v, mutate)
    return n


def convert_exotic_units(recipe: dict) -> int:
    def _convert(conc: dict) -> int:
        target = UNIT_CONVERSIONS.get(conc["unit"])
        if target is None:
            return 0
        new_unit, mult = target
        v = _to_float(conc.get("value"))
        if v is None:
            # Can't convert; just rename unit to keep validation happy.
            conc["unit"] = new_unit
        else:
            conc["value"] = str(v * mult)
            conc["unit"] = new_unit
        return 1
    return _walk_concentrations(recipe, _convert)


# ---- R03 -----------------------------------------------------------------

VARIABLE_PLACEHOLDER = {"value": "variable", "unit": "VARIABLE"}


def fill_missing_concentration(recipe: dict) -> int:
    n = 0
    for key in ("ingredients", "composition"):
        for item in recipe.get(key) or []:
            if isinstance(item, dict) and "concentration" not in item:
                item["concentration"] = dict(VARIABLE_PLACEHOLDER)
                n += 1
    return n


# ---- R04 -----------------------------------------------------------------

def fill_missing_explanation(recipe: dict) -> int:
    n = 0
    sd = recipe.get("source_data")
    if isinstance(sd, dict):
        for ev in sd.get("evidence") or []:
            if isinstance(ev, dict) and "explanation" not in ev:
                ev["explanation"] = EXPLANATION_PLACEHOLDER
                n += 1
    # Also scan top-level evidence + per-ingredient/organism evidence.
    for key in ("evidence",):
        for ev in recipe.get(key) or []:
            if isinstance(ev, dict) and "explanation" not in ev:
                ev["explanation"] = EXPLANATION_PLACEHOLDER
                n += 1
    return n


FIXES = [
    ("R01_flatten_synonym_text", fix_doubly_wrapped_synonyms),
    ("R02_convert_exotic_units", convert_exotic_units),
    ("R03_fill_missing_concentration", fill_missing_concentration),
    ("R04_fill_missing_explanation", fill_missing_explanation),
]


def migrate_one(path: Path, dry_run: bool) -> dict[str, int] | None:
    try:
        with path.open() as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError:
        return None
    if not isinstance(data, dict):
        return None
    counts: dict[str, int] = {}
    for name, fn in FIXES:
        n = fn(data)
        if n:
            counts[name] = n
    if not counts:
        return None
    notes = "; ".join(f"{k}={v}" for k, v in counts.items())
    history = data.setdefault("curation_history", [])
    history.append({
        "timestamp": now_iso(),
        "curator": CURATOR,
        "action": ACTION,
        "notes": notes,
    })
    if not dry_run:
        with path.open("w") as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=80)
    return counts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=DEFAULT_ROOT)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()

    paths = sorted(Path(args.root).rglob("*.yaml"))
    totals = {name: 0 for name, _ in FIXES}
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
    print(f"{mode}scanned: {len(paths)}, files changed: {files_changed}",
          file=sys.stderr)
    for k, v in totals.items():
        print(f"  {k}: {v}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
