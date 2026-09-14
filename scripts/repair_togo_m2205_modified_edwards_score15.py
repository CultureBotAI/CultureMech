#!/usr/bin/env python3
"""Repair TOGO M2205 Modified Edward's medium."""

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
TARGET = Path("bacterial/modified_edwards_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:008797"
EXPECTED_MEDIA_TERM = "TOGO:M2205"

CURATOR = "repair_togo_m2205_modified_edwards_score15.py"
ACTION = "RESOLVED_TOGO_M2205_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2205 = "https://togomedium.org/medium/M2205"
SOURCE = "TOGO M2205"
TITLE = "Modified Edward's medium"
PH_VALUE = 7.6
TEMPERATURE_VALUE = 37.0

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "5", "G_PER_L"),
    ("KCl", "1.3", "G_PER_L"),
    ("NaOAc", "5", "G_PER_L"),
    ("Horse serum", "6", "PERCENT_W_V"),
    ("Glucose", "0.5", "PERCENT_W_V"),
    ("Tryptose", "20", "G_PER_L"),
    ("Yeast dialysate", "5", "PERCENT_W_V"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "5.0", "G_PER_L"),
    ("KCl", "1.3", "G_PER_L"),
    ("NaOAc", "5.0", "G_PER_L"),
    ("Horse serum", "6.0", "PERCENT_W_V"),
    ("Glucose", "0.5", "PERCENT_W_V"),
    ("Tryptose", "20.0", "G_PER_L"),
    ("Yeast dialysate", "5.0", "PERCENT_W_V"),
)

REFERENCES = (TOGO_M2205,)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "NaOAc": ("CHEBI:32954", "sodium acetate"),
    "Horse serum": ("MICRO:0001235", "Horse serum"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Tryptose": ("MICRO:0000183", "Tryptose"),
}

MEDIAINGREDIENT_CHEBI = frozenset({"NaCl", "KCl", "NaOAc", "Glucose"})

NOTES = (
    "TOGO M2205 records Modified Edward's medium with 5 g/L NaCl, "
    "1.3 g/L KCl, 5 g/L NaOAc, 6% horse serum, 0.5% glucose, "
    "20 g/L tryptose, 5% yeast dialysate, pH 7.6, and growth at 37 C."
)

INGREDIENT_NOTES = {
    "NaCl": "TOGO M2205 lists 5 g/L NaCl.",
    "KCl": "TOGO M2205 lists 1.3 g/L KCl.",
    "NaOAc": (
        "TOGO M2205 lists 5 g/L NaOAc and identifies the component as "
        "Sodium acetate."
    ),
    "Horse serum": "TOGO M2205 lists 6% Horse serum.",
    "Glucose": "TOGO M2205 lists 0.5% Glucose.",
    "Tryptose": (
        "TOGO M2205 lists 20 g/L Bacto Tryptose as an undefined component."
    ),
    "Yeast dialysate": (
        "TOGO M2205 lists 5% Yeast dialysate; this undefined yeast fraction "
        "remains intentionally unmapped."
    ),
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
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": INGREDIENT_NOTES[preferred_term],
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if preferred_term in MEDIAINGREDIENT_CHEBI:
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(
    _component(*component) for component in FINAL_INGREDIENT_SIGNATURE
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

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in (IMPORTED_INGREDIENT_SIGNATURE, FINAL_INGREDIENT_SIGNATURE):
        raise ValueError(f"{TARGET}: ingredient signature drifted")


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
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Added the source pH and temperature, grounded NaOAc, "
            "Horse serum, and Tryptose, and retained Yeast dialysate as an "
            "intentionally unmapped undefined component."
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
    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    _put_after(repaired, "temperature_value", TEMPERATURE_VALUE, "ph_value")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired.pop("preparation_steps", None)
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
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
