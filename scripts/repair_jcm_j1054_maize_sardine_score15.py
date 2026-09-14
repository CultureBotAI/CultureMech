#!/usr/bin/env python3
"""Repair JCM J1054 Maize Meal-Sardine Agar."""

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
TARGET = Path("bacterial/maize_meal_sardine_agar.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_j1054_maize_sardine_score15.py"
ACTION = "RESOLVED_JCM_J1054_MAIZE_SARDINE_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:002237"
EXPECTED_MEDIA_TERM = "mediadive.medium:J1054"
JCM_1054 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1054"
SOURCE = "JCM Medium J1054"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Maize meal", "20", "G_PER_L"),
    ("Small dried sardine", "20", "G_PER_L"),
    ("Agar", "20", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Maize meal", "20", "G_PER_L"),
    ("Small dried sardine", "20", "G_PER_L"),
    ("Agar", "20", "G_PER_L"),
    ("Distilled water", "1000", "ML_PER_L"),
)

REFERENCES = (JCM_1054,)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
}

COMPONENT_NOTES = {
    "Maize meal": (
        "JCM Medium 1054 lists 20 g/L maize meal, extracted by boiling with "
        "small dried sardine in 500 ml of the final distilled-water volume."
    ),
    "Small dried sardine": (
        "JCM Medium 1054 lists 20 g/L small dried sardine, extracted by "
        "boiling with maize meal in 500 ml of the final distilled-water volume."
    ),
    "Agar": "JCM Medium 1054 lists 20 g/L agar.",
    "Distilled water": "JCM Medium 1054 lists 1 L distilled water.",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "HEAT",
        "description": (
            "Boil 20 g maize meal and 20 g small dried sardine with 500 ml "
            "distilled water for 20 min."
        ),
        "duration": "20 min",
    },
    {
        "step_number": 2,
        "action": "FILTER",
        "description": "Filter the maize-sardine extract through cloth.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": "Bring the filtrate to 1 L with distilled water.",
    },
    {
        "step_number": 4,
        "action": "HEAT",
        "description": "Add 20 g agar and boil until dissolved.",
    },
    {
        "step_number": 5,
        "action": "AUTOCLAVE",
        "description": "Autoclave the completed medium at 121 C for 15 min.",
        "temperature": {"value": 121.0, "unit": "CELSIUS"},
        "duration": "15 min",
    },
)

NOTES = (
    "JCM Medium J1054 Maize Meal-Sardine Agar lists 20 g maize meal, 20 g "
    "small dried sardine, 20 g agar, and 1 L distilled water. JCM instructs "
    "boiling the maize meal and sardine with 500 ml distilled water for 20 min, "
    "filtering through cloth, bringing the filtrate to 1 L, adding agar, and "
    "boiling until dissolved; JCM's standing instruction is to autoclave media "
    "at 121 C for 15 min unless otherwise stated."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": COMPONENT_NOTES[preferred_term],
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(
    _component(name, value, unit) for name, value, unit in FINAL_INGREDIENT_SIGNATURE
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
        raise ValueError(f"{TARGET}: expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")
    if doc.get("solutions"):
        raise ValueError(f"{TARGET}: unexpected solutions")


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
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": JCM_1054,
        "notes": (
            f"{NOTES} Restored the 1 L distilled-water row from the source, "
            "grounded water and agar, and split the importer's single "
            "misclassified preparation note into explicit heat, filter, mix, "
            "heat, and autoclave steps."
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


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("solutions", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["notes"] = NOTES
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["sterilization"] = {
        "method": "AUTOCLAVE",
        "temperature": {"value": 121.0, "unit": "CELSIUS"},
        "duration": "15 min",
    }
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    return {target_path: repair_target(_load(target_path))}


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
