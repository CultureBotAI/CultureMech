#!/usr/bin/env python3
"""Repair TOGO M2310 / DSMZ Medium 464a reactivation medium."""

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
TARGET = Path("bacterial/reactivation_with_liquid_medium_464_plate_count_agar.yaml")
PARENT = Path("bacterial/reactivation_with_liquid_medium_464.yaml")
EXPECTED_ID = "CultureMech:008897"
EXPECTED_PARENT_ID = "CultureMech:001584"
EXPECTED_MEDIA_TERM = "TOGO:M2310"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:464a"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2310_reactivation_464a_score15.py"
ACTION = "RESOLVED_TOGO_M2310_REACTIVATION_464A_SCORE15"
LINK_ACTION = "LINKED_TOGO_M2310_SOURCE_DUPLICATE"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2310 = "https://togomedium.org/medium/M2310"
DSMZ_464A = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium464a.pdf"
REFERENCES = (TOGO_M2310, DSMZ_464A)
SOURCE = "TOGO M2310 / DSMZ Medium 464a"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1000", "G_PER_L"),
    ("Yeast extract", "2.5", "G_PER_L"),
    ("Dextrose", "1", "G_PER_L"),
    ("Agar, if required", "15", "G_PER_L"),
    ("Tryptone", "5", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("Yeast extract", "2.5", "G_PER_L"),
    ("Dextrose", "1.0", "G_PER_L"),
    ("Agar, if required", "15.0", "G_PER_L"),
    ("Tryptone", "5.0", "G_PER_L"),
)

PARENT_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Tryptone", "5", "G_PER_L"),
    ("Yeast extract", "2.5", "G_PER_L"),
    ("Dextrose", "1", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Yeast extract": ("FOODON:03315426", "Yeast extract"),
    "Dextrose": ("CHEBI:17634", "D-glucose"),
    "Agar, if required": ("CHEBI:2509", "agar"),
    "Tryptone": ("MICRO:0000182", "tryptone"),
}

MEDIAINGREDIENT_CHEBI = frozenset(
    {
        "Distilled water",
        "Dextrose",
        "Agar, if required",
    }
)

NUTRITIONAL_ROLES = {
    "Yeast extract": ("NITROGEN_SOURCE",),
    "Dextrose": ("CARBON_SOURCE",),
    "Tryptone": ("NITROGEN_SOURCE", "AMINO_ACID_SOURCE"),
}

PHYSICOCHEMICAL_ROLES = {
    "Agar, if required": ("SOLIDIFYING_AGENT",),
}

INGREDIENT_NOTES = {
    "Distilled water": (
        "TOGO M2310 / DSMZ Medium 464a lists 1000 ml distilled water as the "
        "Plate Count Agar solvent; the TOGO import unit is corrected to 1 L."
    ),
    "Yeast extract": "TOGO M2310 / DSMZ Medium 464a lists 2.5 g/L Yeast extract.",
    "Dextrose": "TOGO M2310 / DSMZ Medium 464a lists 1 g/L Dextrose.",
    "Agar, if required": ("TOGO M2310 / DSMZ Medium 464a lists 15 g/L Agar, if required."),
    "Tryptone": "TOGO M2310 / DSMZ Medium 464a lists 5 g/L Tryptone.",
}

NOTES = (
    "TOGO M2310 imports DSMZ Medium 464a Reactivation With Liquid Medium 464, "
    "which uses DSMZ Medium 464 Plate Count Agar with 5 g tryptone, 2.5 g "
    "yeast extract, 1 g dextrose, 15 g agar if required, 1000 ml distilled "
    "water, pH 7.0, and rehydration of lyophilized cells from the ampoule in "
    "liquid medium 464 before subsequent subculture in liquid or agar medium."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Rehydrate and grow lyophilized cells from the ampoule in liquid "
            "medium 464; subsequent subculturing may be carried out in "
            "liquid medium or an agar medium."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0.",
    },
)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_PARENT_ID,
    "name": "reactivation_with_liquid_medium_464",
    "notes": (
        "TOGO M2310 imports the same DSMZ Medium 464a reactivation formula "
        "represented by the MediaDive parent record."
    ),
}

VARIANT_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_ID,
    "name": "reactivation_with_liquid_medium_464_plate_count_agar",
    "notes": (
        "TOGO M2310 imports the DSMZ Medium 464a reactivation formula from "
        "the same DSMZ PDF as the MediaDive parent record."
    ),
}

VARIANT_MODIFICATIONS = (
    "TOGO M2310 is the TOGO import of DSMZ Medium 464a and explicitly retains "
    "the distilled-water solvent listed in the source PDF."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": INGREDIENT_NOTES[preferred_term],
        "term": _term(*GROUNDINGS[preferred_term]),
    }
    if preferred_term in MEDIAINGREDIENT_CHEBI:
        row["mediaingredientmech_chebi_term"] = copy.deepcopy(row["term"])
    if nutritional_roles := NUTRITIONAL_ROLES.get(preferred_term):
        row["nutritional_roles"] = list(nutritional_roles)
    if physicochemical_roles := PHYSICOCHEMICAL_ROLES.get(preferred_term):
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(
    _component(*component) for component in FINAL_INGREDIENT_SIGNATURE
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
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

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solutions = doc.get("solutions") or []
    if solutions:
        raise ValueError(f"{TARGET}: unexpected solutions block")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"{PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")

    if _signature(doc.get("ingredients"), "ingredients") != PARENT_INGREDIENT_SIGNATURE:
        raise ValueError(f"{PARENT}: ingredient signature drifted")


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    if key in doc:
        doc[key] = value
        return

    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True
    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)
    while "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_event(doc: dict[str, Any], action: str, notes: str) -> None:
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


def _ensure_variant_child(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    for index, child in enumerate(children):
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID or child.get("path") == VARIANT_CHILD["path"]:
            children[index] = copy.deepcopy(VARIANT_CHILD)
            return
    children.append(copy.deepcopy(VARIANT_CHILD))


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "media_term")
    _put_after(repaired, "notes", NOTES, "preparation_steps")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(
        repaired,
        ACTION,
        (
            "Corrected the TOGO M2310 distilled-water unit to 1 L, added pH "
            "7.0, grounded every DSMZ Medium 464a component, and linked the "
            "record as a DSMZ Medium 464a source duplicate."
        ),
    )
    repaired["parent_media"] = copy.deepcopy(PARENT_MEDIA)
    repaired["variant_relationship"] = "SOURCE_DUPLICATE"
    repaired["variant_modifications"] = [VARIANT_MODIFICATIONS]
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    _ensure_variant_child(repaired)
    _append_event(
        repaired,
        LINK_ACTION,
        "Linked TOGO M2310 as a source duplicate of DSMZ Medium 464a.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    parent_path = normalized / PARENT
    return {
        parent_path: repair_parent(_load(parent_path)),
        target_path: repair_target(_load(target_path)),
    }


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
            changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
