#!/usr/bin/env python3
"""Restore MediaDB C00002/ATP and C00003/NAD+ in normalized records.

The archived MediaDB compound export has corrupt text in rows 1 through 4. The
row sequence and every subsequent row establish their KEGG identities:

    1 -> C00001 water
    2 -> C00002 ATP
    3 -> C00003 NAD+
    4 -> C00004 NADH

Rows 2 and 3 are used by 30 normalized media. Their corrupt source labels were
eventually reduced to an empty ``preferred_term``, creating 30 of the 32
``EMPTY_INGREDIENT_NAME`` findings in the 2026-08-24 media-content review.

This migration is intentionally narrow. It keys on the stable ``MEDIADB`` term,
requires the first ingredient name to be empty, and verifies the concentration
against the source formulation before changing anything. The raw snapshot stays
immutable; the importer contains the corresponding forward fix.

Usage::

    python scripts/fix_mediadb_leading_compounds.py          # dry run
    python scripts/fix_mediadb_leading_compounds.py --apply  # write 30 records
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
NORMALIZED = REPO / "data" / "normalized_yaml"


@dataclass(frozen=True)
class Correction:
    preferred_term: str
    term_id: str
    term_label: str
    expected_value: str
    source_row: str


CORRECTIONS: dict[str, Correction] = {
    "MEDIADB:33": Correction("ATP", "CHEBI:15422", "ATP", "0.00036", "C00002"),
    **{
        f"MEDIADB:{medium_id}": Correction(
            "ATP", "CHEBI:15422", "ATP", expected, "C00002"
        )
        for medium_id, expected in (
            *((str(i), "1.25") for i in range(46, 51)),
            *((str(i), "2.5") for i in range(51, 56)),
            *((str(i), "5.0") for i in range(56, 61)),
            *((str(i), "10.0") for i in range(61, 66)),
            *((str(i), "20.0") for i in range(66, 71)),
        )
    },
    **{
        f"MEDIADB:{medium_id}": Correction(
            "NAD+", "CHEBI:15846", "NAD(+)", "0.00603", "C00003"
        )
        for medium_id in range(279, 283)
    },
}


def media_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def apply_correction(doc: dict[str, Any]) -> tuple[bool, str]:
    """Apply one guarded correction and return ``(changed, explanation)``."""
    source_id = media_term_id(doc)
    correction = CORRECTIONS.get(source_id)
    if correction is None:
        return False, "not targeted"

    ingredients = doc.get("ingredients")
    if not isinstance(ingredients, list) or not ingredients:
        raise ValueError(f"{source_id}: expected a non-empty ingredients list")
    ingredient = ingredients[0]
    if not isinstance(ingredient, dict):
        raise ValueError(f"{source_id}: ingredients[0] is not a mapping")
    if str(ingredient.get("preferred_term") or "").strip():
        return False, "already named"

    concentration = ingredient.get("concentration")
    if not isinstance(concentration, dict):
        raise ValueError(f"{source_id}: ingredients[0] has no concentration")
    actual_value = str(concentration.get("value") or "")
    actual_unit = str(concentration.get("unit") or "")
    if actual_value != correction.expected_value or actual_unit != "MILLIMOLAR":
        raise ValueError(
            f"{source_id}: expected {correction.expected_value} MILLIMOLAR, "
            f"found {actual_value} {actual_unit}"
        )

    ingredient["preferred_term"] = correction.preferred_term
    ingredient["term"] = {
        "id": correction.term_id,
        "label": correction.term_label,
    }
    ingredient["notes"] = (
        f"Restored from MediaDB compound row {correction.source_row}; the archived "
        "leading compound labels are corrupt, while the row sequence preserves the "
        "KEGG identity."
    )
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{source_id}: curation_history is not a list")
    history.append(
        {
            "timestamp": "2026-08-25T00:00:00-07:00",
            "curator": "fix_mediadb_leading_compounds.py",
            "action": "RESTORED_CORRUPT_SOURCE_COMPOUND",
            "notes": (
                f"Restored {correction.source_row} as {correction.preferred_term} "
                f"({correction.term_id}) from the MediaDB row sequence; resolves the "
                "2026-08-24 EMPTY_INGREDIENT_NAME review finding."
            ),
        }
    )
    return True, f"{source_id} -> {correction.preferred_term}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    changed = 0
    seen: set[str] = set()
    for path in sorted(args.normalized_dir.rglob("*.yaml")):
        source_text = path.read_text(encoding="utf-8")
        if not any(source_id in source_text for source_id in CORRECTIONS):
            continue
        doc = yaml.safe_load(source_text)
        if not isinstance(doc, dict):
            continue
        source_id = media_term_id(doc)
        if source_id not in CORRECTIONS:
            continue
        seen.add(source_id)
        did_change, explanation = apply_correction(doc)
        if not did_change:
            print(f"skip  {path.relative_to(args.normalized_dir)}: {explanation}")
            continue
        changed += 1
        print(f"fix   {path.relative_to(args.normalized_dir)}: {explanation}")
        if args.apply:
            path.write_text(
                yaml.safe_dump(
                    doc,
                    default_flow_style=False,
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

    missing = set(CORRECTIONS) - seen
    if missing:
        raise SystemExit(f"Target MediaDB records not found: {sorted(missing)}")
    mode = "updated" if args.apply else "would update"
    print(f"\n{mode} {changed} records; expected {len(CORRECTIONS)}")
    if changed not in {0, len(CORRECTIONS)}:
        raise SystemExit("Partial correction set; inspect before proceeding")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
