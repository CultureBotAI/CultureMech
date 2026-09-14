#!/usr/bin/env python3
"""Repair TOGO M618 Sphaerotilus Medium and its JCM J610 duplicate."""

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
TARGET = Path("bacterial/TOGO_M618_Sphaerotilus_Medium.yaml")
PARENT = Path("bacterial/JCM_J610_SPHAEROTILUS_MEDIUM.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:010017"
EXPECTED_PARENT_ID = "CultureMech:002958"
EXPECTED_MEDIA_TERM = "TOGO:M618"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:J610"

CURATOR = "repair_togo_m618_score15.py"
ACTION = "RESOLVED_TOGO_M618_SCORE15"
PARENT_ACTION = "RESOLVED_JCM_610_SPHAEROTILUS"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M618 = "https://togomedium.org/medium/M618"
JCM_610 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=610"
MEDIADIVE_J610 = "https://mediadive.dsmz.de/medium/J610"

TOGO_SOURCE = "TOGO M618 / JCM Medium 610"
PARENT_SOURCE = "MediaDive J610 / JCM Medium 610"
TITLE = "Sphaerotilus Medium"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Glycerol", "1", "G_PER_L"),
    ("Agar (if needed)", "10", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.1", "G_PER_L"),
    ("Tryptone (BD-Difco)", "0.5", "G_PER_L"),
)

IMPORTED_PARENT_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Tryptone", "0.5", "G_PER_L"),
    ("Glycerol", "1", "G_PER_L"),
    ("Yeast extract", "0.1", "G_PER_L"),
    ("Agar", "10", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Tryptone (BD-Difco)", "0.5", "G_PER_L"),
    ("Glycerol", "1.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.1", "G_PER_L"),
    ("Agar (if needed)", "10.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Tryptone (BD-Difco)": ("MICRO:0000182", "Tryptone"),
    "Glycerol": ("CHEBI:17754", "glycerol"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "yeast extract"),
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
}

REFERENCES = (TOGO_M618, JCM_610, MEDIADIVE_J610)
PARENT_REFERENCES = (JCM_610, MEDIADIVE_J610)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_PARENT_ID,
    "name": "sphaerotilus_medium",
    "notes": (
        "TOGO M618 imports the same JCM Medium 610 Sphaerotilus Medium "
        "formulation represented by MediaDive J610."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_ID,
    "name": "sphaerotilus_medium",
    "notes": (
        "TOGO M618 imports the same JCM Medium 610 Sphaerotilus Medium "
        "formulation represented by MediaDive J610."
    ),
}

VARIANT_MODIFICATION = (
    "Same JCM Medium 610 Sphaerotilus Medium formulation as the MediaDive " "J610 source record."
)

RECIPE_NOTES = (
    "JCM Medium 610 Sphaerotilus Medium lists 0.5 g Tryptone (BD-Difco), "
    "1.0 g Glycerol, 0.1 g Yeast extract (BD-Difco), 10.0 g Agar if "
    "needed, and 1.0 L Distilled water, adjusted to pH 7.0."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
}


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
    physicochemical_roles: tuple[str, ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    if grounding[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


def _ingredients(source: str) -> list[dict[str, Any]]:
    return [
        _component(
            "Tryptone (BD-Difco)",
            "0.5",
            "G_PER_L",
            source=source,
            nutritional_roles=("NITROGEN_SOURCE",),
        ),
        _component(
            "Glycerol",
            "1.0",
            "G_PER_L",
            source=source,
            nutritional_roles=("CARBON_SOURCE",),
        ),
        _component(
            "Yeast extract (BD-Difco)",
            "0.1",
            "G_PER_L",
            source=source,
            nutritional_roles=("NITROGEN_SOURCE",),
        ),
        _component(
            "Agar (if needed)",
            "10.0",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 10 g/L Agar if needed.",
            physicochemical_roles=("SOLIDIFYING_AGENT",),
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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"expected media term {EXPECTED_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("target ingredient signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"expected {EXPECTED_PARENT_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"expected media term {EXPECTED_PARENT_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_PARENT_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("parent ingredient signature drifted")


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
        "has_unmapped_ingredients",
        "incomplete_composition",
        "needs_manual_curation",
    ):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
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


def _ensure_child_link(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    filtered: list[Any] = []
    inserted = False
    for child in children:
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID or child.get("path") == TOGO_CHILD["path"]:
            if not inserted:
                filtered.append(copy.deepcopy(TOGO_CHILD))
                inserted = True
            continue
        filtered.append(child)

    if not inserted:
        filtered.append(copy.deepcopy(TOGO_CHILD))
    doc["variant_children"] = filtered


def _repair_common(
    doc: dict[str, Any],
    *,
    source: str,
    action: str,
    references: tuple[str, ...],
    event_notes: str,
) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("solutions", None)
    repaired["ingredients"] = _ingredients(source)
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "notes")
    _put_after(
        repaired,
        "sterilization",
        copy.deepcopy(STERILIZATION),
        "preparation_steps",
    )
    _ensure_flags(repaired)
    _ensure_references(repaired, references)
    _append_event(
        repaired,
        action=action,
        references=references,
        notes=event_notes,
    )
    return repaired


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = _repair_common(
        doc,
        source=TOGO_SOURCE,
        action=ACTION,
        references=REFERENCES,
        event_notes=(
            "Corrected the imported distilled-water volume, added pH 7.0 from "
            "JCM Medium 610, grounded tryptone, yeast extract, glycerol, agar, "
            "and water, added JCM autoclave metadata, and linked MediaDive "
            "J610 as a source duplicate."
        ),
    )
    _put_after(repaired, "parent_media", copy.deepcopy(PARENT_MEDIA), "references")
    _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        [VARIANT_MODIFICATION],
        "variant_relationship",
    )
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = _repair_common(
        doc,
        source=PARENT_SOURCE,
        action=PARENT_ACTION,
        references=PARENT_REFERENCES,
        event_notes=(
            "Restored the JCM Medium 610 distilled-water component omitted by "
            "the MediaDive import, grounded tryptone and yeast extract, added "
            "JCM autoclave metadata, and linked the TOGO M618 source duplicate."
        ),
    )
    _ensure_child_link(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target = normalized / TARGET
    parent = normalized / PARENT
    return {
        target: repair_target(_load(target)),
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
