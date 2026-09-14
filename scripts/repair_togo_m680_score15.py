#!/usr/bin/env python3
"""Repair TOGO M680 MBG-20 and its JCM J662 duplicate."""

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
TARGET = Path("bacterial/TOGO_M680_MBG-20.yaml")
PARENT = Path("bacterial/mbg_20.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:010085"
EXPECTED_PARENT_ID = "CultureMech:003008"
EXPECTED_MEDIA_TERM = "TOGO:M680"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:J662"

CURATOR = "repair_togo_m680_score15.py"
ACTION = "RESOLVED_TOGO_M680_SCORE15"
PARENT_ACTION = "RESOLVED_JCM_662_MBG_20"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M680 = "https://togomedium.org/medium/M680"
JCM_662 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=662"
MEDIADIVE_J662 = "https://mediadive.dsmz.de/medium/J662"

TOGO_SOURCE = "TOGO M680 / JCM Medium 662"
PARENT_SOURCE = "MediaDive J662 / JCM Medium 662"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "4", "G_PER_L"),
    ("Sea salts (Sigma)", "40", "G_PER_L"),
    ("Glucose", "5", "G_PER_L"),
    ("Peptone", "16", "G_PER_L"),
)

IMPORTED_PARENT_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "16", "G_PER_L"),
    ("Yeast extract", "4", "G_PER_L"),
    ("Glucose", "5", "G_PER_L"),
    ("Sea Salt", "40", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "16.0", "G_PER_L"),
    ("Yeast extract", "4.0", "G_PER_L"),
    ("Glucose", "5.0", "G_PER_L"),
    ("Sea salts (Sigma)", "40.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Peptone": ("MICRO:0000178", "peptone"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Distilled water": ("CHEBI:15377", "water"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
}

REFERENCES = (TOGO_M680, JCM_662, MEDIADIVE_J662)
PARENT_REFERENCES = (JCM_662, MEDIADIVE_J662)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_PARENT_ID,
    "name": "mbg_20",
    "notes": (
        "TOGO M680 imports the same JCM Medium 662 MBG-20 formulation "
        "represented by MediaDive J662."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_ID,
    "name": "mbg_20",
    "notes": (
        "TOGO M680 imports the same JCM Medium 662 MBG-20 formulation "
        "represented by MediaDive J662."
    ),
}

VARIANT_MODIFICATION = "Same JCM Medium 662 MBG-20 formulation as the MediaDive J662 source record."

RECIPE_NOTES = (
    "JCM Medium 662 MBG-20 lists 16.0 g Peptone, 4.0 g Yeast extract, "
    "5.0 g Glucose, 40.0 g Sea salts (Sigma), and 1.0 L Distilled water, "
    "then adjusts pH to 7.0."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0.",
    },
    {
        "step_number": 2,
        "action": "DISSOLVE",
        "description": "Dissolve Sea salts (Sigma) in distilled water.",
    },
    {
        "step_number": 3,
        "action": "FILTER_STERILIZE",
        "description": "Sterilize the Sea salts solution by filtration.",
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": "Separately autoclave Peptone, Yeast extract, and Glucose solutions.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Add the sterile Peptone, Yeast extract, and Glucose solutions "
            "to the sterile Sea salts solution."
        ),
    },
    {
        "step_number": 6,
        "action": "MIX",
        "description": (
            "Make the liquid medium anaerobic by repeated cycles, three "
            "times, of degassing and charging with argon."
        ),
    },
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
    source: str,
    notes: str | None = None,
    nutritional_roles: tuple[str, ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)
    return row


def _ingredients(source: str) -> list[dict[str, Any]]:
    return [
        _component(
            "Peptone",
            "16.0",
            "G_PER_L",
            source=source,
            nutritional_roles=("NITROGEN_SOURCE",),
        ),
        _component(
            "Yeast extract",
            "4.0",
            "G_PER_L",
            source=source,
            nutritional_roles=("NITROGEN_SOURCE",),
        ),
        _component(
            "Glucose",
            "5.0",
            "G_PER_L",
            source=source,
            nutritional_roles=("CARBON_SOURCE",),
        ),
        _component(
            "Sea salts (Sigma)",
            "40.0",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists 40.0 g/L Sea salts (Sigma); this commercial "
                "sea-salt mixture is retained as an opaque complex component."
            ),
        ),
        _component(
            "Distilled water",
            "1.0",
            "L",
            source=source,
            notes=f"{source} lists 1.0 L Distilled water.",
        ),
    ]


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


def _ensure_target(
    doc: dict[str, Any],
    *,
    path: Path,
    record_id: str,
    source_term: str,
    imported_signature: tuple[Component, ...],
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{path}: expected {record_id}, found {doc.get('id')}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{path}: expected media term {source_term}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        imported_signature,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{path}: ingredient signature drifted")


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

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
    ):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], references: tuple[str, ...]) -> None:
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for reference in references:
        if reference not in existing:
            rows.append({"reference": reference})
            existing.add(reference)


def _append_event(
    doc: dict[str, Any],
    *,
    action: str,
    references: tuple[str, ...],
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(references),
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


def repair_togo(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(
        doc,
        path=TARGET,
        record_id=EXPECTED_ID,
        source_term=EXPECTED_MEDIA_TERM,
        imported_signature=IMPORTED_INGREDIENT_SIGNATURE,
    )

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(TOGO_SOURCE)
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "notes",
    )
    _put_after(repaired, "parent_media", copy.deepcopy(PARENT_MEDIA), "references")
    repaired["variant_relationship"] = "SOURCE_DUPLICATE"
    repaired["variant_modifications"] = [VARIANT_MODIFICATION]
    repaired.pop("variant_children", None)
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, REFERENCES)
    _append_event(
        repaired,
        action=ACTION,
        references=REFERENCES,
        notes=(
            "Corrected the imported distilled-water unit, added pH 7.0, "
            "grounded Peptone, Yeast extract, and Glucose, kept Sea salts "
            "(Sigma) intentionally ungrounded, added the split filtration, "
            "autoclaving, and argon preparation instructions, and linked the "
            "JCM 662 source duplicate."
        ),
    )
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(
        doc,
        path=PARENT,
        record_id=EXPECTED_PARENT_ID,
        source_term=EXPECTED_PARENT_MEDIA_TERM,
        imported_signature=IMPORTED_PARENT_INGREDIENT_SIGNATURE,
    )

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    repaired["ingredients"] = _ingredients(PARENT_SOURCE)
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "ingredients",
    )
    repaired.pop("sterilization", None)
    repaired.pop("parent_media", None)
    repaired["variant_children"] = [copy.deepcopy(TOGO_CHILD)]
    repaired.pop("variant_relationship", None)
    repaired.pop("variant_modifications", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, PARENT_REFERENCES)
    _append_event(
        repaired,
        action=PARENT_ACTION,
        references=PARENT_REFERENCES,
        notes=(
            "Restored the JCM Medium 662 recipe with 1.0 L Distilled water, "
            "normalized Sea salts (Sigma), grounded the disclosed reducible "
            "nutrients, retained the Sigma sea-salt mixture as an opaque "
            "commercial component, and linked TOGO M680."
        ),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    parent_path = normalized / PARENT
    return {
        target_path: repair_togo(_load(target_path)),
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
