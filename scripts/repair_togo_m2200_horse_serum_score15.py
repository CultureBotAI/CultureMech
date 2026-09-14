#!/usr/bin/env python3
"""Repair TOGO M2200 DSMZ Medium 1 with 20% horse serum."""

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
TARGET = Path("bacterial/medium_1_liquid_with_20_horse_serum.yaml")
PARENT = Path("bacterial/nutrient_agar.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:008794"
EXPECTED_PARENT_ID = "CultureMech:001297"
EXPECTED_MEDIA_TERM = "TOGO:M2200"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:1"

CURATOR = "repair_togo_m2200_horse_serum_score15.py"
ACTION = "RESOLVED_TOGO_M2200_SCORE15"
LINK_ACTION = "LINKED_TOGO_M2200_HORSE_SERUM_VARIANT"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2200 = "https://togomedium.org/medium/M2200"
DSMZ_1 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1.pdf"
SOURCE = "TOGO M2200 / DSMZ Medium 1"
TITLE = "Medium 1 liquid, with 20 % horse serum"
PH_VALUE = 7.0

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1000", "G_PER_L"),
    ("Horse serum", "20", "PERCENT_W_V"),
    ("Agar", "15", "G_PER_L"),
    ("Meat extract", "3", "G_PER_L"),
    ("Peptone", "5", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "5.0", "G_PER_L"),
    ("Meat extract", "3.0", "G_PER_L"),
    ("Horse serum", "20.0", "PERCENT_V_V"),
    ("Agar", "15.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

REFERENCES = (TOGO_M2200, DSMZ_1)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0.",
    },
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Peptone": ("MICRO:0000178", "Peptone"),
}

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_PARENT_ID,
    "name": "nutrient_agar",
    "notes": "TOGO M2200 imports DSMZ Medium 1 with a 20% horse-serum supplement.",
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_ID,
    "name": "medium_1_liquid_with_20_horse_serum",
    "notes": "TOGO M2200 imports DSMZ Medium 1 with a 20% horse-serum supplement.",
}

VARIANT_MODIFICATIONS = "Adds 20% v/v horse serum to DSMZ Medium 1."

NOTES = (
    "TOGO M2200 imports DSMZ Medium 1 with a 20% horse-serum supplement. "
    "The TOGO M2200 component table lists 5 g Peptone, 3 g Meat extract, "
    "20% Horse serum, 15 g Agar, and 1000 ml Distilled water; the source "
    "pH is 7.0. TOGO M2200 retains the DSMZ Medium 1 agar row despite the "
    "medium name containing liquid."
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
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Peptone",
        "5.0",
        "G_PER_L",
        notes="DSMZ Medium 1 and TOGO M2200 list 5 g/L Peptone.",
    ),
    _component(
        "Meat extract",
        "3.0",
        "G_PER_L",
        notes=(
            "DSMZ Medium 1 and TOGO M2200 list 3 g/L Meat extract; this "
            "generic complex extract is retained without an ontology grounding."
        ),
    ),
    _component(
        "Horse serum",
        "20.0",
        "PERCENT_V_V",
        notes=(
            "TOGO M2200 lists the horse-serum supplement as 20%; this liquid "
            "serum addition is represented as % v/v and retained without an "
            "ontology grounding."
        ),
    ),
    _component(
        "Agar",
        "15.0",
        "G_PER_L",
        notes="TOGO M2200 carries the DSMZ Medium 1 15 g/L Agar row.",
    ),
    _component(
        "Distilled water",
        "1.0",
        "L",
        notes="DSMZ Medium 1 and TOGO M2200 list 1000 ml Distilled water.",
    ),
)


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
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
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
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    if doc.get("solutions"):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(
            f"{PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(
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


def _ensure_variant_child(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    for index, child in enumerate(children):
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID or child.get("path") == TOGO_CHILD["path"]:
            children[index] = copy.deepcopy(TOGO_CHILD)
            return
    children.append(copy.deepcopy(TOGO_CHILD))


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(
        repaired,
        action=ACTION,
        notes=(
            f"{NOTES} Corrected the imported water unit and horse-serum "
            "percent artifacts, grounded the disclosed simple and "
            "protein-hydrolysate components, kept Meat extract and Horse serum "
            "intentionally unmapped, and linked the record to DSMZ Medium 1."
        ),
    )
    repaired["parent_media"] = copy.deepcopy(PARENT_MEDIA)
    repaired["variant_relationship"] = "SUPPLEMENTED_VARIANT"
    repaired["variant_modifications"] = [VARIANT_MODIFICATIONS]
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    _ensure_variant_child(repaired)
    _append_curation_event(
        repaired,
        action=LINK_ACTION,
        notes="Linked TOGO M2200 as a 20% horse-serum variant of DSMZ Medium 1.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    parent_path = normalized / PARENT
    return {
        target_path: repair_target(_load(target_path)),
        parent_path: repair_parent(_load(parent_path)),
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
