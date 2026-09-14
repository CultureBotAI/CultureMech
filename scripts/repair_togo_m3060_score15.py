#!/usr/bin/env python3
"""Repair TOGO M3060 OTTOW MEDIUM."""

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
TARGET = Path("bacterial/TOGO_M3060_OTTOW_MEDIUM.yaml")
DSMZ_PARENT = Path("bacterial/ottow_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009575"
EXPECTED_PARENT_ID = "CultureMech:001596"
EXPECTED_MEDIA_TERM = "TOGO:M3060"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:467"

CURATOR = "repair_togo_m3060_score15.py"
ACTION = "RESOLVED_TOGO_M3060_SCORE15"
LINK_ACTION = "LINKED_TOGO_M3060_SUPPLEMENTED_VARIANT"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M3060 = "https://togomedium.org/medium/M3060"
NBRC_1631 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1631"
SOURCE = "TOGO M3060 / NBRC Medium 1631"
TITLE = "OTTOW MEDIUM"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "2.5", "G_PER_L"),
    ("NaCl", "5", "G_PER_L"),
    ("Gellan Gum (if needed)", "7", "G_PER_L"),
    ("Glucose", "1", "G_PER_L"),
    ("Meat extract", "5", "G_PER_L"),
    ("Casamino acids", "2.5", "G_PER_L"),
    ("Peptone", "7.5", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Glucose", "1.0", "G_PER_L"),
    ("Peptone", "7.5", "G_PER_L"),
    ("Meat extract", "5.0", "G_PER_L"),
    ("Yeast extract", "2.5", "G_PER_L"),
    ("Casamino acids", "2.5", "G_PER_L"),
    ("NaCl", "5.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("Gellan Gum (if needed)", "7.0", "G_PER_L"),
)

REFERENCES = (TOGO_M3060, NBRC_1631)
PH_VALUE = 8.5

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Casamino acids": ("FOODON:03315719", "mammalian milk protein (hydrolyzed)"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Gellan Gum (if needed)": ("CHEBI:85248", "gellan gum"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Meat extract": ("FOODON:03315424", "Meat Extract"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Peptone": ("MICRO:0000178", "Peptone"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "DISSOLVE",
        "description": (
            "Dissolve glucose, peptone, meat extract, yeast extract, "
            "casamino acids, NaCl, and, if needed, 7.0 g/L gellan gum in "
            "1.0 L distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 8.5.",
    },
)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{DSMZ_PARENT}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_PARENT_ID,
    "name": "ottow_medium",
    "notes": (
        "NBRC Medium 1631 uses distilled water in place of DSMZ tap water "
        "and adds optional 7.0 g/L gellan gum."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_ID,
    "name": "ottow_medium",
    "notes": (
        "TOGO M3060 imports NBRC Medium 1631, which uses distilled water "
        "in place of DSMZ tap water and adds optional 7.0 g/L gellan gum."
    ),
}

VARIANT_MODIFICATIONS = (
    "NBRC Medium 1631 uses distilled water in place of DSMZ Medium 467 tap "
    "water and adds 7.0 g/L gellan gum if needed."
)

NOTES = (
    "TOGO M3060 imports NBRC Medium 1631, OTTOW MEDIUM. NBRC Medium 1631 "
    "lists, in 1 L Distilled water, 1.0 g Glucose, 7.5 g Peptone, "
    "5.0 g Meat extract, 2.5 g Yeast extract, 2.5 g Casamino acids, 5 g "
    "NaCl, and, if needed, 7 g Gellan Gum. pH 8.5."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    grounding = GROUNDINGS[preferred_term]
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": f"NBRC Medium 1631 lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": _term(*grounding),
    }
    if preferred_term == "Gellan Gum (if needed)":
        row["notes"] = "NBRC Medium 1631 lists 7.0 g/L Gellan Gum if needed."
    if grounding[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(
    _component(name, value, unit) for name, value, unit in FINAL_INGREDIENT_SIGNATURE
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
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    if doc.get("solutions"):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(
            f"{DSMZ_PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{DSMZ_PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
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
    repaired["physical_state"] = "LIQUID"
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
            f"{NOTES} Corrected the distilled-water unit, added pH and "
            "composition preparation steps, grounded all components, and "
            "linked the record as an NBRC supplemented variant of DSMZ "
            "Medium 467."
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
        notes="Linked TOGO M3060 as an NBRC supplemented variant of DSMZ Medium 467.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    parent_path = normalized / DSMZ_PARENT
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
