#!/usr/bin/env python3
"""Repair the DSMZ Medium 77 Liver Broth score-35 product record."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

TARGET = "bacterial/liver_broth_oxoid_cm_77.yaml"
EXPECTED_ID = "CultureMech:001915"
EXPECTED_SOURCE_TERM = "mediadive.medium:77"

CURATOR = "repair_dsmz_77_score35.py"
ACTION = "RESOLVED_DSMZ_77_SCORE35_GRAPH"
TIMESTAMP = "2026-09-08T00:00:00-07:00"

DSMZ_77 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium77.pdf"

NOTES = (
    "DSMZ Medium 77 lists Liver Broth (Oxoid CM 77) and instructs curators to "
    "prepare the medium according to bottle directions under a 100% N2 gas "
    "atmosphere; the source does not disclose the Oxoid CM 77 amount or "
    "internal formulation."
)

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term") or {}
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: found id {doc.get('id')!r}, expected {EXPECTED_ID!r}")

    if _source_term_id(doc) != EXPECTED_SOURCE_TERM:
        raise ValueError(
            f"{TARGET}: found source term {_source_term_id(doc)!r}, "
            f"expected {EXPECTED_SOURCE_TERM!r}"
        )


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError(f"{TARGET}: data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    ingredients = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    if any(_grounded(ingredient) for ingredient in ingredients):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")

    has_unmapped = any(not _grounded(ingredient) for ingredient in ingredients)
    if has_unmapped:
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    if flags:
        doc["data_quality_flags"] = flags
    else:
        doc.pop("data_quality_flags", None)


def _ensure_reference(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{TARGET}: references is not a list")

    if not any(
        isinstance(reference, dict) and reference.get("reference") == DSMZ_77
        for reference in references
    ):
        references.append({"reference": DSMZ_77})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved DSMZ Medium 77 product graph",
        "source": DSMZ_77,
        "notes": NOTES,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET}: curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


RECIPE: dict[str, Any] = {
    "medium_type": "COMPLEX",
    "composition_type": "UNDEFINED",
    "physical_state": "LIQUID",
    "ingredients": [
        {
            "preferred_term": "Liver Broth (Oxoid CM 77)",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": "DSMZ Medium 77",
            "notes": (
                "DSMZ Medium 77 identifies Liver Broth (Oxoid CM 77) but "
                "directs users to prepare the medium from the bottle without "
                "stating an amount or the internal formulation."
            ),
        },
        {
            "preferred_term": "N2 gas",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": "DSMZ Medium 77",
            "notes": (
                "DSMZ Medium 77 instructs users to prepare the medium under "
                "a 100% N2 gas atmosphere."
            ),
            "term": _term("CHEBI:17997", "dinitrogen"),
            "mediaingredientmech_chebi_term": _term("CHEBI:17997", "dinitrogen"),
        },
    ],
    "preparation_steps": [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Prepare Liver Broth (Oxoid CM 77) according to the bottle "
                "directions under a 100% N2 gas atmosphere."
            ),
        },
    ],
}


def _repair(doc: dict[str, Any]) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        if field in RECIPE:
            repaired[field] = copy.deepcopy(RECIPE[field])
        else:
            repaired.pop(field, None)
    repaired["notes"] = NOTES
    _ensure_flags(repaired)
    _ensure_reference(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    doc = _load(path)
    _require_target(doc)
    return {path: _repair(doc)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
        if args.apply:
            changed = write_record(path, doc)
        else:
            changed = dump_record(doc) != path.read_text(encoding="utf-8")
        if changed:
            changed_count += 1
            print(path.relative_to(args.normalized_dir))

    action = "Updated" if args.apply else "Would update"
    print(f"{action} {changed_count} DSMZ Medium 77 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
