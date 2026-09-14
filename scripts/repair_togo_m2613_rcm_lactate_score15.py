#!/usr/bin/env python3
"""Repair TOGO M2613 / ATCC 1252 RCM with sodium lactate."""

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
TARGET = Path(
    "bacterial/"
    "reinforced_clostridial_medium_oxoid_cm149_with_sodium_lactate_60_solution_at_a_concentration_of_1_5.yaml"
)
EXPECTED_ID = "CultureMech:009180"
EXPECTED_MEDIA_TERM = "TOGO:M2613"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2613_rcm_lactate_score15.py"
ACTION = "RESOLVED_TOGO_M2613_RCM_LACTATE_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2613 = "https://togomedium.org/medium/M2613"
ATCC_1252 = "https://www.atcc.org/~/media/CCB197296D624B1DA0BBFA3C2EB8632B.ashx"
REFERENCES = (TOGO_M2613, ATCC_1252)
SOURCE = "TOGO M2613 / ATCC Medium 1252"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1000", "G_PER_L"),
    ("Reinforced Clostridial medium (Oxoid CM149)", "38", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Sodium lactate (60% solution)", "1.5", "PERCENT_W_V"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("Sodium lactate (60% solution)", "1.5", "PERCENT_W_V"),
    ("Reinforced Clostridial medium (Oxoid CM149)", "38.0", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Sodium lactate (60% solution)": ("CHEBI:75228", "sodium lactate"),
}

NOTES = (
    "TOGO M2613 imports ATCC Medium 1252 Reinforced Clostridial medium "
    "(Oxoid CM149) with sodium lactate. ATCC 1252 discloses 1.5% sodium "
    "lactate 60% solution and a final pH of 7.0; TOGO additionally lists "
    "1000 ml distilled water and 38 g/L Reinforced Clostridial medium "
    "(Oxoid CM149). The commercial Oxoid base is retained as an opaque "
    "unmapped component because the source does not expand its composition."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust final pH to 7.0.",
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


INGREDIENTS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Distilled water",
        "concentration": {"value": "1.0", "unit": "L"},
        "source": SOURCE,
        "notes": (
            "TOGO M2613 lists 1000 ml distilled water; the import unit is " "corrected to 1 L."
        ),
        "term": _term(*GROUNDINGS["Distilled water"]),
        "mediaingredientmech_chebi_term": _term(*GROUNDINGS["Distilled water"]),
    },
    {
        "preferred_term": "Sodium lactate (60% solution)",
        "concentration": {"value": "1.5", "unit": "PERCENT_W_V"},
        "source": SOURCE,
        "notes": "ATCC Medium 1252 lists sodium lactate 60% solution at 1.5%.",
        "term": _term(*GROUNDINGS["Sodium lactate (60% solution)"]),
        "mediaingredientmech_chebi_term": _term(*GROUNDINGS["Sodium lactate (60% solution)"]),
        "nutritional_roles": ["CARBON_SOURCE"],
    },
    {
        "preferred_term": "Reinforced Clostridial medium (Oxoid CM149)",
        "concentration": {"value": "38.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": (
            "TOGO M2613 lists 38 g/L commercial Oxoid CM149 Reinforced "
            "Clostridial Medium; ATCC 1252 names the same commercial base but "
            "does not disclose its component recipe."
        ),
    },
)


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
    solution_signature = _signature(doc.get("solutions"), "solutions")
    if (
        ingredient_signature,
        solution_signature,
    ) not in (
        (IMPORTED_INGREDIENT_SIGNATURE, IMPORTED_SOLUTION_SIGNATURE),
        (FINAL_INGREDIENT_SIGNATURE, ()),
    ):
        raise ValueError(
            f"{TARGET}: signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} / {IMPORTED_SOLUTION_SIGNATURE!r}"
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
            existing.add(reference)


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Corrected the TOGO M2613 water unit, flattened the sodium "
            "lactate solution into a grounded ingredient, added pH 7.0, and "
            "marked the commercial Oxoid CM149 base as an opaque unmapped "
            "component."
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
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
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
