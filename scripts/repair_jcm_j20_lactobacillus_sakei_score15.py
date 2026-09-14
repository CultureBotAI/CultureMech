#!/usr/bin/env python3
"""Repair MediaDive/JCM J20 Lactobacillus sakei medium."""

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
TARGET = Path("bacterial/lactobacillus_sakei_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_j20_lactobacillus_sakei_score15.py"
ACTION = "RESOLVED_JCM_J20_LACTOBACILLUS_SAKEI_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:002571"
EXPECTED_MEDIA_TERM = "mediadive.medium:J20"
JCM_20 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=20"
MEDIADIVE_J20 = "https://mediadive.dsmz.de/rest/medium/J20"
SOURCE = "MediaDive J20 / JCM Medium 20"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Sake", "700", "G_PER_L"),
    ("Yeast extract", "6.25", "G_PER_L"),
    ("Agar", "16.25", "G_PER_L"),
    ("Liver extract concentrate", "0.25", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Sake", "875.0", "ML_PER_L"),
    ("Yeast extract", "6.25", "G_PER_L"),
    ("Agar", "16.25", "G_PER_L"),
    ("Liver extract concentrate", "0.25", "G_PER_L"),
    ("Distilled water", "125.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

NOTES = (
    "MediaDive J20 imports JCM Medium 20. JCM 20 records Lactobacillus Sakei "
    "Medium as an 800 ml sake-water agar recipe with yeast extract and liver "
    "extract concentrate and does not state a pH."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix 700 ml sake, 100 ml distilled water, 5.0 g yeast extract, "
            "13.0 g agar, and 0.2 g Liver extract concentrate."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 degrees C for 15 min.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "Autoclave the complete agar medium at the JCM default settings.",
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
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": (notes or f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}."),
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Sake",
        "875.0",
        "ML_PER_L",
        notes=(
            "JCM Medium 20 lists 700 ml sake in an 800 ml recipe; MediaDive J20 "
            "records the same original 800 ml main-solution volume."
        ),
    ),
    _component("Yeast extract", "6.25", "G_PER_L"),
    _component("Agar", "16.25", "G_PER_L"),
    _component(
        "Liver extract concentrate",
        "0.25",
        "G_PER_L",
        notes=(
            "JCM Medium 20 lists 0.2 g Liver extract concentrate in an 800 ml "
            "recipe; the product is source-disclosed but not reducible to one "
            "ChEBI molecule."
        ),
    ),
    _component(
        "Distilled water",
        "125.0",
        "ML_PER_L",
        notes=(
            "JCM Medium 20 lists 100 ml distilled water in an 800 ml recipe; "
            "MediaDive J20 records this as the original 800 ml main-solution volume."
        ),
    ),
)


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
        raise ValueError(f"{TARGET}: expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")


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
    for reference in (MEDIADIVE_J20, JCM_20):
        if reference not in existing:
            references.append({"reference": reference})


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": f"{MEDIADIVE_J20}; {JCM_20}",
        "notes": (
            f"{NOTES} Corrected the imported sake row from a g/L artifact "
            "to an ml/L volume, restored the distilled-water row, and "
            "normalized the 800 ml recipe to per-liter concentrations."
        ),
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "notes")
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_record(_load(path))}


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
