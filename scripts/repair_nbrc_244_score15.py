#!/usr/bin/env python3
"""Repair the score-15 TOGO import of NBRC Medium 244."""

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
TARGET = Path("bacterial/togo_medium_m1466.yaml")
PARENT = Path("bacterial/NBRC_245.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:008008"
EXPECTED_PARENT_ID = "CultureMech:007480"
EXPECTED_MEDIA_TERM = "TOGO:M1466"
EXPECTED_PARENT_MEDIA_TERM = "nbrc.medium:244"

CURATOR = "repair_nbrc_244_score15.py"
ACTION = "RESOLVED_TOGO_M1466_NBRC_244_SCORE15"
LINK_ACTION = "LINKED_TOGO_M1466_SOURCE_DUPLICATE"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1466 = "https://togomedium.org/medium/M1466"
NBRC_244 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=244"
SOURCE = "NBRC Medium 244"

YEAST_EXTRACT = "Yeast extract"
MALT_EXTRACT = "Malt extract"
GLUCOSE = "Glucose"
SEAWATER = "Seawater"
DISTILLED_WATER = "Distilled water"
AGAR_IF_NEEDED = "Agar (if needed)"

Component = tuple[str, str, str]

LEGACY_INGREDIENTS: tuple[Component, ...] = (
    (DISTILLED_WATER, "250", "G_PER_L"),
    (YEAST_EXTRACT, "4", "G_PER_L"),
    (SEAWATER, "750", "G_PER_L"),
    (GLUCOSE, "4", "G_PER_L"),
    (AGAR_IF_NEEDED, "20", "G_PER_L"),
    (MALT_EXTRACT, "10", "G_PER_L"),
)

FINAL_INGREDIENTS: tuple[Component, ...] = (
    (YEAST_EXTRACT, "4", "G_PER_L"),
    (MALT_EXTRACT, "10", "G_PER_L"),
    (GLUCOSE, "4", "G_PER_L"),
    (SEAWATER, "750", "ML_PER_L"),
    (DISTILLED_WATER, "250", "ML_PER_L"),
    (AGAR_IF_NEEDED, "20", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    AGAR_IF_NEEDED: ("CHEBI:2509", "agar"),
    DISTILLED_WATER: ("CHEBI:15377", "water"),
    GLUCOSE: ("CHEBI:17234", "glucose"),
    MALT_EXTRACT: ("FOODON:03301056", "Malt extract"),
    SEAWATER: ("ENVO:00002149", "Seawater"),
    YEAST_EXTRACT: ("FOODON:03315426", "Yeast extract"),
}
PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    AGAR_IF_NEEDED: ("SOLIDIFYING_AGENT",),
}
UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}
TARGET_REFERENCES = (TOGO_M1466, NBRC_244)
PARENT_REFERENCES = (NBRC_244,)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_PARENT_ID,
    "name": "245",
    "notes": (
        "TOGO M1466 imports the same NBRC Medium 244 formulation represented "
        "by the recovered NBRC Medium 244 source record."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_ID,
    "name": "togo_medium_m1466",
    "notes": (
        "TOGO M1466 imports the same NBRC Medium 244 formulation represented "
        "by the recovered NBRC Medium 244 source record."
    ),
}

VARIANT_MODIFICATIONS = (
    "Same NBRC Medium 244 formulation as the recovered NBRC Medium 244 source record."
)

RECIPE_NOTES = (
    "TOGO M1466 imports NBRC Medium 244, which lists 4 g/L Yeast extract, "
    "10 g/L Malt extract, 4 g/L Glucose, 750 ml/L Seawater, 250 ml/L "
    "Distilled water, and 20 g/L Agar if needed. The final pH is 7.6."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Combine 4 g/L Yeast extract, 10 g/L Malt extract, 4 g/L "
            "Glucose, 750 ml/L Seawater, and 250 ml/L Distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": "Add 20 g/L agar when solid NBRC Medium 244 is needed.",
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.6.",
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


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


def _notes(preferred_term: str, value: str, unit: str) -> str:
    if preferred_term == AGAR_IF_NEEDED:
        return f"{SOURCE} lists {value} {UNIT_LABELS[unit]} agar if needed."
    return f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}."


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    grounding = GROUNDINGS[preferred_term]
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": _notes(preferred_term, value, unit),
        "term": _term(*grounding),
    }
    if grounding[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles is not None:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


def _ingredients() -> list[dict[str, Any]]:
    return [_component(name, value, unit) for name, value, unit in FINAL_INGREDIENTS]


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in {LEGACY_INGREDIENTS, FINAL_INGREDIENTS}:
        raise ValueError(f"{TARGET}: ingredient signature drifted to {ingredient_signature!r}")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"{PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature != FINAL_INGREDIENTS:
        raise ValueError(f"{PARENT}: ingredient signature drifted to {ingredient_signature!r}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag
        not in {"has_unmapped_ingredients", "incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(("has_ontology_mappings", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], references_to_add: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in references_to_add:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_event(
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
    _put_after(repaired, "ph_value", 7.6, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    repaired.pop("solutions", None)
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "media_term")
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, TARGET_REFERENCES)
    _ensure_event(
        repaired,
        action=ACTION,
        references=TARGET_REFERENCES,
        notes=(
            "Curated TOGO:M1466 from TOGO and NBRC Medium 244; corrected "
            "Seawater and Distilled water from mass-like imports to 750 ml/L "
            "and 250 ml/L volume additions, added pH 7.6, grounded all "
            "formula components, and linked the existing recovered NBRC "
            "Medium 244 record as the source duplicate parent."
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
    _ensure_references(repaired, PARENT_REFERENCES)
    _ensure_event(
        repaired,
        action=LINK_ACTION,
        references=TARGET_REFERENCES,
        notes="Linked TOGO M1466 as a source duplicate of NBRC Medium 244.",
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
    for path, doc in sorted(plans.items()):
        changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        if args.apply and changed:
            write_record(path, doc)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
