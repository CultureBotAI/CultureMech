#!/usr/bin/env python3
"""Repair DSMZ/KOMODO Medium 672 score-40 source duplicates."""

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

CURATOR = "repair_dsmz_672_score40.py"
ACTION = "RESOLVED_DSMZ_672_SCORE40_GRAPH"
LINK_ACTION = "LINKED_DSMZ_672_SOURCE_DUPLICATE"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

DSMZ_PARENT = "bacterial/half_strength_nutrient_broth_or_agar.yaml"
KOMODO_CHILD = "bacterial/KOMODO_672_HALF_STRENGTH_NUTRIENT_BROTH_OR_AGAR.yaml"

DSMZ_672_URL = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium672.pdf"

EXPECTED_IDS = {
    DSMZ_PARENT: "CultureMech:001813",
    KOMODO_CHILD: "CultureMech:006268",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ_PARENT: "mediadive.medium:672",
    KOMODO_CHILD: "komodo.medium:672",
}

RECIPE_NAMES = {
    DSMZ_PARENT: "half_strength_nutrient_broth_or_agar",
    KOMODO_CHILD: "half_strength_nutrient_broth_or_agar",
}

NOTES = (
    "DSMZ Medium 672 specifies alternative commercial Difco products, Difco "
    "0003 or Difco 0001, without printing a dehydrated-medium mass or "
    "separate broth/agar formulation."
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
    "parent_media",
    "variant_relationship",
    "variant_modifications",
    "variant_children",
)


def _recipe() -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": "Difco 0003 or Difco 0001",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
                "source": "DSMZ Medium 672",
                "notes": NOTES,
            },
        ],
    }


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


def _require_target(doc: dict[str, Any], relative_path: str) -> None:
    if doc.get("id") != EXPECTED_IDS[relative_path]:
        raise ValueError(
            f"{relative_path}: found id {doc.get('id')!r}, "
            f"expected {EXPECTED_IDS[relative_path]!r}"
        )

    if _source_term_id(doc) != EXPECTED_SOURCE_TERMS[relative_path]:
        raise ValueError(
            f"{relative_path}: found source term {_source_term_id(doc)!r}, "
            f"expected {EXPECTED_SOURCE_TERMS[relative_path]!r}"
        )


def _ensure_flags(doc: dict[str, Any], relative_path: str) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError(f"{relative_path}: data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "has_ontology_mappings",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")
    if "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")


def _ensure_reference(doc: dict[str, Any], relative_path: str) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{relative_path}: references is not a list")

    if not any(
        isinstance(ref, dict) and ref.get("reference") == DSMZ_672_URL
        for ref in references
    ):
        references.append({"reference": DSMZ_672_URL})


def _history(doc: dict[str, Any], relative_path: str) -> list[Any]:
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{relative_path}: curation_history is not a list")
    return history


def _upsert_history(
    doc: dict[str, Any],
    relative_path: str,
    event: dict[str, Any],
) -> None:
    history = _history(doc, relative_path)
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == event["action"]
        ):
            history[index] = event
            return
    history.append(event)


def _append_curation_event(doc: dict[str, Any], relative_path: str) -> None:
    _upsert_history(
        doc,
        relative_path,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Resolved DSMZ Medium 672 opaque commercial product row",
            "source": DSMZ_672_URL,
            "notes": NOTES,
        },
    )


def _append_link_event(doc: dict[str, Any]) -> None:
    _upsert_history(
        doc,
        DSMZ_PARENT,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": LINK_ACTION,
            "changes": "Linked KOMODO Medium 672 to DSMZ Medium 672",
            "source": DSMZ_672_URL,
            "notes": f"Added or refreshed reciprocal SOURCE_DUPLICATE link for {KOMODO_CHILD}.",
        },
    )


def _recipe_ref(relative_path: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{relative_path}",
        "relationship": "SOURCE_DUPLICATE",
        "id": EXPECTED_IDS[relative_path],
        "name": RECIPE_NAMES[relative_path],
        "notes": notes,
    }


def _upsert_ref(refs: list[Any], new_ref: dict[str, str]) -> None:
    for index, existing in enumerate(refs):
        if isinstance(existing, dict) and existing.get("path") == new_ref["path"]:
            refs[index] = new_ref
            return
    refs.append(new_ref)


def repair_record(doc: dict[str, Any], relative_path: str) -> dict[str, Any]:
    _require_target(doc, relative_path)

    repaired = copy.deepcopy(doc)
    recipe = _recipe()
    for field in RECIPE_FIELDS:
        if field in recipe:
            repaired[field] = copy.deepcopy(recipe[field])
        else:
            repaired.pop(field, None)

    repaired["notes"] = NOTES
    _ensure_flags(repaired, relative_path)
    _ensure_reference(repaired, relative_path)
    _append_curation_event(repaired, relative_path)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans = {
        normalized / relative_path: repair_record(
            _load(normalized / relative_path),
            relative_path,
        )
        for relative_path in EXPECTED_IDS
    }

    parent = plans[normalized / DSMZ_PARENT]
    child = plans[normalized / KOMODO_CHILD]
    link_notes = "KOMODO Medium 672 is a source-catalogue duplicate of DSMZ Medium 672."

    child["parent_media"] = _recipe_ref(DSMZ_PARENT, link_notes)
    child["variant_relationship"] = "SOURCE_DUPLICATE"
    child["variant_modifications"] = [
        "KOMODO source-catalogue duplicate of DSMZ Medium 672."
    ]

    children = parent.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError(f"{DSMZ_PARENT}: variant_children is not a list")
    _upsert_ref(children, _recipe_ref(KOMODO_CHILD, link_notes))
    _append_link_event(parent)

    return {
        path: doc
        for path, doc in plans.items()
        if path.read_bytes() != dump_record(doc).encode("utf-8")
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    for path in sorted(plans):
        print(path)

    if args.apply:
        changed = sum(write_record(path, doc) for path, doc in plans.items())
        print(f"Wrote {changed} record(s).")
    else:
        print(f"Dry run planned {len(plans)} record write(s). Pass --apply to write.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
