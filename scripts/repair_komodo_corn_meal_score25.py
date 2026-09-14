#!/usr/bin/env python3
"""Repair sparse KOMODO Corn Meal Agar records left in the score-25 band."""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_corn_meal_score25.py"
ACTION = "RESOLVED_KOMODO_CORN_MEAL_SCORE25_GRAPH"
LINK_ACTION = "LINKED_KOMODO_CORN_MEAL_SCORE25_CHILDREN"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

DSMZ_PARENT = "bacterial/corn_meal_agar.yaml"
KOMODO_PARENT = "bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml"
KOMODO_DSM_25939 = "bacterial/for_dsm_25939.yaml"
KOMODO_DSM_25945 = "bacterial/for_dsm_25945.yaml"
KOMODO_DSM_25720 = "bacterial/for_dsm_25720.yaml"

DSMZ_191_URL = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium191.pdf"

EXPECTED_IDS = {
    DSMZ_PARENT: "CultureMech:001283",
    KOMODO_PARENT: "CultureMech:004218",
    KOMODO_DSM_25939: "CultureMech:004217",
    KOMODO_DSM_25945: "CultureMech:004216",
    KOMODO_DSM_25720: "CultureMech:004215",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ_PARENT: "mediadive.medium:191",
    KOMODO_PARENT: "komodo.medium:191",
    KOMODO_DSM_25939: "komodo.medium:191.4",
    KOMODO_DSM_25945: "komodo.medium:191.3",
    KOMODO_DSM_25720: "komodo.medium:191.2",
}

RECIPE_NAMES = {
    DSMZ_PARENT: "corn_meal_agar",
    KOMODO_PARENT: "corn_meal_agar",
    KOMODO_DSM_25939: "for_dsm_25939",
    KOMODO_DSM_25945: "for_dsm_25945",
    KOMODO_DSM_25720: "for_dsm_25720",
}

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
    "parent_media",
    "variant_relationship",
    "variant_modifications",
    "variant_children",
)


@dataclass(frozen=True)
class Target:
    path: str
    notes: str
    ph_value: float
    source_label: str


@dataclass(frozen=True)
class ChildLink:
    child_path: str
    relationship: str
    notes: str
    variant_modification: str


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _corn_meal_recipe(ph_value: float) -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": ph_value,
        "ingredients": [
            {
                "preferred_term": "Corn meal",
                "concentration": {"value": "50.0", "unit": "G_PER_L"},
                "source": "DSMZ Medium 191",
                "notes": (
                    "DSMZ Medium 191 blends 50.0 g corn meal in 800 ml "
                    "distilled water, leaves it overnight in the refrigerator, "
                    "heats it at 60 C for one hour, filters it, and brings the "
                    "filtrate to 1 L."
                ),
                "term": _term("mediadive.compound:2087", "Corn meal"),
            },
            {
                "preferred_term": "Agar",
                "term": _term("CHEBI:2509", "agar"),
                "concentration": {"value": "10.0", "unit": "G_PER_L"},
                "source": "DSMZ Medium 191",
                "notes": (
                    "DSMZ Medium 191 adds 10.0 g agar after bringing the "
                    "corn-meal filtrate to 1 L and heats to dissolve it before "
                    "autoclaving."
                ),
                "mediaingredientmech_chebi_term": _term("CHEBI:2509", "agar"),
            },
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Blend 50.0 g corn meal in 800 ml distilled water and "
                    "leave overnight in the refrigerator."
                ),
            },
            {
                "step_number": 2,
                "action": "HEAT",
                "description": "Heat at 60 C for one hour.",
            },
            {
                "step_number": 3,
                "action": "FILTER",
                "description": "Filter and bring the volume to 1 L.",
            },
            {
                "step_number": 4,
                "action": "HEAT",
                "description": "Add 10.0 g agar and heat to dissolve.",
            },
            {
                "step_number": 5,
                "action": "AUTOCLAVE",
                "description": "Autoclave the completed corn meal agar.",
            },
        ],
        "sterilization": {"method": "AUTOCLAVE"},
    }


TARGETS = (
    Target(
        DSMZ_PARENT,
        (
            "DSMZ Medium 191 prepares Corn Meal Agar from 50.0 g/L corn meal "
            "and 10.0 g/L agar after extracting the corn meal in distilled "
            "water overnight and at 60 C."
        ),
        6.0,
        "DSMZ Medium 191",
    ),
    Target(
        KOMODO_PARENT,
        (
            "KOMODO Medium 191 states DSMZ Medium 191 provenance; DSMZ Medium "
            "191 prepares Corn Meal Agar from 50.0 g/L corn meal and 10.0 g/L "
            "agar after extracting the corn meal in distilled water."
        ),
        6.0,
        "KOMODO Medium 191",
    ),
    Target(
        KOMODO_DSM_25939,
        (
            "KOMODO Medium 191.4 states DSMZ Medium 191 provenance and records "
            "pH 7.2 for DSM 25939; DSMZ Medium 191 provides the 50.0 g/L corn "
            "meal plus 10.0 g/L agar formulation."
        ),
        7.2,
        "KOMODO Medium 191.4",
    ),
    Target(
        KOMODO_DSM_25945,
        (
            "KOMODO Medium 191.3 states DSMZ Medium 191 provenance and records "
            "pH 7.4 for DSM 25945; DSMZ Medium 191 provides the 50.0 g/L corn "
            "meal plus 10.0 g/L agar formulation."
        ),
        7.4,
        "KOMODO Medium 191.3",
    ),
    Target(
        KOMODO_DSM_25720,
        (
            "KOMODO Medium 191.2 states DSMZ Medium 191 provenance and records "
            "pH 7.5 for DSM 25720; DSMZ Medium 191 provides the 50.0 g/L corn "
            "meal plus 10.0 g/L agar formulation."
        ),
        7.5,
        "KOMODO Medium 191.2",
    ),
)

CHILD_LINKS = (
    ChildLink(
        KOMODO_PARENT,
        "SOURCE_DUPLICATE",
        "KOMODO Medium 191 is a source-catalogue duplicate of DSMZ Medium 191.",
        "KOMODO source-catalogue duplicate of DSMZ Medium 191.",
    ),
    ChildLink(
        KOMODO_DSM_25939,
        "PH_VARIANT",
        (
            "KOMODO Medium 191.4 preserves DSMZ Medium 191 components and "
            "concentrations but records pH 7.2 for DSM 25939."
        ),
        (
            "KOMODO Medium 191.4 preserves DSMZ Medium 191 components and "
            "concentrations but records pH 7.2 for DSM 25939."
        ),
    ),
    ChildLink(
        KOMODO_DSM_25945,
        "PH_VARIANT",
        (
            "KOMODO Medium 191.3 preserves DSMZ Medium 191 components and "
            "concentrations but records pH 7.4 for DSM 25945."
        ),
        (
            "KOMODO Medium 191.3 preserves DSMZ Medium 191 components and "
            "concentrations but records pH 7.4 for DSM 25945."
        ),
    ),
    ChildLink(
        KOMODO_DSM_25720,
        "PH_VARIANT",
        (
            "KOMODO Medium 191.2 preserves DSMZ Medium 191 components and "
            "concentrations but records pH 7.5 for DSM 25720."
        ),
        (
            "KOMODO Medium 191.2 preserves DSMZ Medium 191 components and "
            "concentrations but records pH 7.5 for DSM 25720."
        ),
    ),
)


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


def _grounded(row: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = row.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _ensure_flags(doc: dict[str, Any], target: Target) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError(f"{target.path}: data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "has_unmapped_ingredients",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    ingredients = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    if any(_grounded(row) for row in ingredients):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")
    else:
        raise ValueError(f"{target.path}: repaired recipe has no grounded ingredients")


def _ensure_reference(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    if not any(
        isinstance(row, dict) and row.get("reference") == DSMZ_191_URL for row in references
    ):
        references.append({"reference": DSMZ_191_URL})


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
            and (event["action"] != LINK_ACTION or existing.get("notes") == event["notes"])
        ):
            history[index] = event
            return
    history.append(event)


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    _upsert_history(
        doc,
        target.path,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": f"Resolved {target.source_label} Corn Meal Agar recipe",
            "source": DSMZ_191_URL,
            "notes": target.notes,
        },
    )


def _append_link_event(doc: dict[str, Any], link: ChildLink) -> None:
    _upsert_history(
        doc,
        DSMZ_PARENT,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": LINK_ACTION,
            "changes": "Linked KOMODO Medium 191 children to DSMZ Medium 191",
            "source": DSMZ_191_URL,
            "notes": f"Added or refreshed reciprocal {link.relationship} link for {link.child_path}.",
        },
    )


def _recipe_ref(relative_path: str, relationship: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{relative_path}",
        "relationship": relationship,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_target(doc, target.path)

    repaired = copy.deepcopy(doc)
    recipe = _corn_meal_recipe(target.ph_value)
    for field in RECIPE_FIELDS:
        if field in recipe:
            repaired[field] = copy.deepcopy(recipe[field])
        else:
            repaired.pop(field, None)

    repaired["notes"] = target.notes
    _ensure_flags(repaired, target)
    _ensure_reference(repaired, target)
    _append_curation_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    targets = {target.path: target for target in TARGETS}
    docs = {path: _load(normalized / path) for path in EXPECTED_IDS}

    plans = {normalized / path: repair_record(doc, targets[path]) for path, doc in docs.items()}

    parent = plans[normalized / DSMZ_PARENT]
    children = parent.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError(f"{DSMZ_PARENT}: variant_children is not a list")

    for link in CHILD_LINKS:
        child = plans[normalized / link.child_path]
        child["parent_media"] = _recipe_ref(DSMZ_PARENT, link.relationship, link.notes)
        child["variant_relationship"] = link.relationship
        child["variant_modifications"] = [link.variant_modification]
        _upsert_ref(children, _recipe_ref(link.child_path, link.relationship, link.notes))
        _append_link_event(parent, link)

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
