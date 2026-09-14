#!/usr/bin/env python3
"""Repair TOGO M2255 / ATCC Medium 2515 half-strength Marine Medium."""

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
TARGET = Path("bacterial/strength_marine_medium.yaml")
PARENT = Path("bacterial/TOGO_M33_Marine_Broth_2216.yaml")
EXPECTED_ID = "CultureMech:008842"
EXPECTED_MEDIA_TERM = "TOGO:M2255"
EXPECTED_PARENT_ID = "CultureMech:009718"
EXPECTED_PARENT_MEDIA_TERM = "TOGO:M33"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2255_half_marine_score15.py"
ACTION = "RESOLVED_TOGO_M2255_HALF_MARINE_SCORE15"
PARENT_ACTION = "LINKED_TOGO_M2255_HALF_MARINE_VARIANT"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2255 = "https://togomedium.org/medium/M2255"
ATCC_2515 = "https://www.atcc.org/~/media/C64DF5CA9E954F51A0B94D9B6BABAB21.ashx"
REFERENCES = (TOGO_M2255, ATCC_2515)
SOURCE = "TOGO M2255 / ATCC Medium 2515"

WATER = "DI Water"
AGAR = "Agar"
MARINE_BROTH = "Marine Broth 2216 (BD 279110)"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "1000", "G_PER_L"),
    (AGAR, "15", "G_PER_L"),
    (MARINE_BROTH, "18.7", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (MARINE_BROTH, "18.7", "G_PER_L"),
    (AGAR, "15.0", "G_PER_L"),
    (WATER, "1000.0", "ML_PER_L"),
)

PARENT_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "CONCENTRATION_VARIANT",
    "id": EXPECTED_ID,
    "name": "strength_marine_medium",
    "notes": (
        "Uses one-half-strength Marine Broth 2216 at 18.7 g/L instead of "
        "the full 37.4 g/L and adds 15.0 g/L agar if needed."
    ),
}

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "CONCENTRATION_VARIANT",
    "id": EXPECTED_PARENT_ID,
    "name": "marine_broth_2216",
    "notes": ("Uses one-half-strength Marine Broth 2216 at 18.7 g/L instead of the full 37.4 g/L."),
}

GROUNDINGS: dict[str, tuple[str, str]] = {
    WATER: ("CHEBI:15377", "water"),
    AGAR: ("CHEBI:2509", "agar"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

NOTES = (
    "TOGO M2255 cites ATCC Medium 2515 1/2 Strength Marine Medium, which "
    "lists 18.7 g Marine Broth 2216 from BD 279110, optional 15.0 g Agar, "
    "and 1000.0 ml DI Water. The source autoclaves the medium at 121 C and "
    "keeps it spinning while dispensing so that precipitate is evenly "
    "distributed."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes or f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }

    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        term = _term(*grounding)
        row["term"] = term
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        MARINE_BROTH,
        "18.7",
        "G_PER_L",
        notes=(
            f"{SOURCE} lists 18.7 g/L Marine Broth 2216 from BD 279110; "
            "this commercial marine broth is retained as an opaque complex component."
        ),
    ),
    _component(
        AGAR,
        "15.0",
        "G_PER_L",
        notes=f"{SOURCE} lists 15.0 g/L Agar if solid medium is needed.",
    ),
    _component(WATER, "1000.0", "ML_PER_L"),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": ("Suspend Marine Broth 2216 and Agar, if needed, in 1000 ml DI Water."),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": (
            "Autoclave at 121 C and keep the medium spinning while dispensing "
            "so precipitate is evenly distributed."
        ),
    },
)

STERILIZATION = {"method": "AUTOCLAVE"}


def _put_after(doc: dict[str, Any], key: str, value: Any, after_key: str) -> None:
    if key in doc:
        doc[key] = value
        return

    rebuilt: dict[str, Any] = {}
    placed = False
    for existing_key, existing_value in doc.items():
        rebuilt[existing_key] = existing_value
        if existing_key == after_key:
            rebuilt[key] = value
            placed = True
    if not placed:
        rebuilt[key] = value

    doc.clear()
    doc.update(rebuilt)


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in (IMPORTED_INGREDIENT_SIGNATURE, FINAL_INGREDIENT_SIGNATURE):
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {signature!r}"
        )

    kg_match = doc.get("kg_microbe_match")
    if kg_match not in (None, "mediadive.medium:12"):
        raise ValueError(f"{TARGET}: unexpected kg_microbe_match {kg_match!r}")


def _ensure_parent(parent: dict[str, Any]) -> None:
    if parent.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(
            f"{PARENT}: expected parent id {EXPECTED_PARENT_ID}, found {parent.get('id')!r}"
        )
    if _source_term_id(parent) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")

    children = parent.get("variant_children") or []
    if not isinstance(children, list):
        raise ValueError(f"{PARENT}: variant_children is not a list")
    for child in children:
        if not isinstance(child, dict):
            raise ValueError(f"{PARENT}: variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID and child != PARENT_CHILD:
            raise ValueError(f"{PARENT}: existing {EXPECTED_ID} child pointer drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag for flag in flags if flag not in {"incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(
        (
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        )
    )
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_event(
    doc: dict[str, Any],
    *,
    action: str,
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(REFERENCES),
        "notes": notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(PREPARATION_STEPS)),
        "ingredients",
    )
    repaired["sterilization"] = copy.deepcopy(STERILIZATION)
    _put_after(repaired, "parent_media", copy.deepcopy(PARENT_MEDIA), "curation_history")
    _put_after(repaired, "variant_relationship", "CONCENTRATION_VARIANT", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        [
            "Uses 18.7 g/L Marine Broth 2216 (BD 279110).",
            "Adds 15.0 g/L Agar if solid medium is needed.",
        ],
        "variant_relationship",
    )
    repaired.pop("kg_microbe_match", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(
        repaired,
        action=ACTION,
        notes=(
            f"{NOTES} Corrected the DI Water unit to ml/L, removed the false "
            "kg_microbe_match to DSMZ Soil Extract Medium, and linked this "
            "recipe to Marine Broth 2216 as a half-strength concentration variant."
        ),
    )
    return repaired


def repair_parent(parent: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(parent)

    repaired = copy.deepcopy(parent)
    children = repaired.setdefault("variant_children", [])
    children[:] = [
        child
        for child in children
        if not (isinstance(child, dict) and child.get("id") == EXPECTED_ID)
    ]
    children.append(copy.deepcopy(PARENT_CHILD))
    _ensure_event(
        repaired,
        action=PARENT_ACTION,
        notes=(
            "Linked TOGO M2255 / ATCC Medium 2515 as a half-strength Marine "
            "Broth 2216 concentration variant with optional agar."
        ),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target = normalized / TARGET
    parent = normalized / PARENT
    return {
        target: repair_record(_load(target)),
        parent: repair_parent(_load(parent)),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in plans.items():
        if args.apply:
            changed = write_record(path, doc)
        else:
            changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
