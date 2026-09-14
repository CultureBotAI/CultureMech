#!/usr/bin/env python3
"""Repair TOGO M1338 Marine Broth 2216 with pyruvate."""

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
TARGET = Path("bacterial/marine_broth_2216_with_pyruvate.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1338_marine_pyruvate_score15.py"
ACTION = "RESOLVED_TOGO_M1338_MARINE_PYRUVATE_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:007874"
EXPECTED_MEDIA_TERM = "TOGO:M1338"
TOGO_M1338 = "https://togomedium.org/medium/M1338"
SOURCE = "TOGO Medium M1338"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Marine Broth 2216 (BD-Difco)", "37.4", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("1.0 M Sodium pyruvate solution", "10", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Marine Broth 2216 (BD-Difco)", "37.4", "G_PER_L"),
    ("Distilled water", "1000", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("1.0 M Sodium pyruvate solution", "10.0", "ML_PER_L"),
)

REFERENCES = (TOGO_M1338,)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Sodium pyruvate": ("CHEBI:50144", "sodium pyruvate"),
}

COMPONENT_NOTES = {
    "Marine Broth 2216 (BD-Difco)": (
        "TOGO M1338 lists 37.4 g/L Marine Broth 2216 from BD-Difco "
        "without disclosing the product composition."
    ),
    "Distilled water": "TOGO M1338 lists 1 L distilled water.",
}

NOTES = (
    "TOGO Medium M1338 lists 37.4 g Marine Broth 2216 (BD-Difco) and "
    "1 L distilled water, adjusts pH to 8.0, autoclaves the base, then "
    "adds 10 ml/L autoclaved 1.0 M sodium pyruvate solution after cooling. "
    "TOGO preserves the original source as JCM_M1244 and notes that any "
    "precipitate yielded after autoclaving can be removed by filtration."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": ("Suspend 37.4 g Marine Broth 2216 (BD-Difco) in 1 L distilled " "water."),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 8.0.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the Marine Broth 2216 base.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "After cooling, add 10 ml autoclaved 1.0 M sodium pyruvate " "solution per liter."
        ),
    },
    {
        "step_number": 5,
        "action": "FILTER",
        "description": (
            "Remove any precipitate yielded after autoclaving by filtration, " "if necessary."
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


def _grounded_component(
    preferred_term: str,
    value: str,
    unit: str,
) -> dict[str, Any]:
    grounding = GROUNDINGS[preferred_term]
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "term": _term(*grounding),
        "mediaingredientmech_chebi_term": _term(*grounding),
    }


def _ingredient(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
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
    _ingredient(name, value, unit) for name, value, unit in FINAL_INGREDIENT_SIGNATURE
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "1.0 M Sodium pyruvate solution",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "notes": (
            "TOGO M1338 adds 10 ml/L autoclaved 1.0 M sodium pyruvate "
            "solution after cooling the autoclaved Marine Broth 2216 base."
        ),
        "composition": [_grounded_component("Sodium pyruvate", "1.0", "MOLAR")],
    },
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
    if _signature(doc.get("solutions"), "solutions") not in (
        IMPORTED_SOLUTION_SIGNATURE,
        FINAL_SOLUTION_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


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
        "source": TOGO_M1338,
        "notes": (
            f"{NOTES} Corrected distilled water from 1 g/L to 1 L, "
            "converted the pyruvate solution addition from an empty 10 g/L "
            "solution to a 10 ml/L 1.0 M stock solution, grounded water and "
            "sodium pyruvate, and restored TOGO's pH and preparation notes."
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
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ph_value"] = 8.0
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["notes"] = NOTES
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["sterilization"] = {"method": "AUTOCLAVE"}
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
