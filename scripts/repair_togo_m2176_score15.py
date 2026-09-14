#!/usr/bin/env python3
"""Repair TOGO M2176 Renibacterium KDM-2 medium."""

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
TARGET = Path("bacterial/TOGO_M2176_Renibacterium_KDM-2_medium.yaml")
EXPECTED_ID = "CultureMech:008770"
EXPECTED_MEDIA_TERM = "TOGO:M2176"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2176_score15.py"
ACTION = "RESOLVED_TOGO_M2176_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M2176 = "https://togomedium.org/medium/M2176"
ATCC_1108 = "https://www.atcc.org/~/media/C5DA8BD389F44EC19C8D094B271B63B2.ashx"
SOURCE = "ATCC Medium 1108 via TOGO M2176"
TITLE = "Renibacterium KDM-2 medium"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "80", "G_PER_L"),
    ("Yeast extract", "0.05", "G_PER_L"),
    ("Fetal bovine serum", "20", "G_PER_L"),
    ("Agar", "1.5", "G_PER_L"),
    ("L-Cysteine . HCl", "0.1", "G_PER_L"),
    ("Peptone", "1", "G_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "10.0", "G_PER_L"),
    ("Yeast extract", "0.5", "G_PER_L"),
    ("L-Cysteine . HCl", "1.0", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Fetal bovine serum", "200.0", "ML_PER_L"),
    ("Distilled water", "800.0", "ML_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
)

REFERENCES = (TOGO_M2176, ATCC_1108)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "L-Cysteine . HCl": ("CHEBI:91247", "L-cysteine hydrochloride"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "Peptone": ("MICRO:0000178", "peptone"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
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


def _step(step_number: int, action: str, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": action,
        "description": description,
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Peptone",
        "10.0",
        "G_PER_L",
        notes="ATCC Medium 1108 lists 1.0% w/v peptone, normalized to 10 g/L.",
    ),
    _component(
        "Yeast extract",
        "0.5",
        "G_PER_L",
        notes=("ATCC Medium 1108 lists 0.05% w/v yeast extract, normalized to " "0.5 g/L."),
    ),
    _component(
        "L-Cysteine . HCl",
        "1.0",
        "G_PER_L",
        notes=("ATCC Medium 1108 lists 0.1% w/v L-Cysteine . HCl, normalized " "to 1 g/L."),
    ),
    _component(
        "Agar",
        "15.0",
        "G_PER_L",
        notes="ATCC Medium 1108 lists 1.5% w/v agar, normalized to 15 g/L.",
    ),
    _component(
        "Fetal bovine serum",
        "200.0",
        "ML_PER_L",
        notes=(
            "ATCC Medium 1108 lists 20.0% fetal bovine serum added at "
            "45 C, normalized to 200 ml/L; this serum is retained as an "
            "opaque complex component."
        ),
    ),
    _component(
        "Distilled water",
        "800.0",
        "ML_PER_L",
        notes=(
            "ATCC Medium 1108 dissolves peptone, yeast extract, and "
            "L-Cysteine . HCl in 80% final-volume distilled water, "
            "normalized to 800 ml/L."
        ),
    ),
    _component(
        "NaOH",
        "variable",
        "VARIABLE",
        notes=(
            "ATCC Medium 1108 adjusts to pH 6.5 with NaOH but does not "
            "state a final NaOH amount."
        ),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    _step(
        1,
        "DISSOLVE",
        "Dissolve peptone, yeast extract, and L-Cysteine . HCl in distilled water.",
    ),
    _step(2, "ADJUST_PH", "Adjust to pH 6.5 with NaOH."),
    _step(3, "HEAT", "Add agar and dissolve by heating."),
    _step(4, "AUTOCLAVE", "Autoclave at 121 C for 15 minutes."),
    _step(5, "COOL", "Cool to 45 C."),
    _step(6, "MIX", "Add fetal bovine serum at 45 C."),
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 minutes",
}

NOTES = (
    "TOGO M2176 imports ATCC Medium 1108 as Renibacterium KDM-2 medium. "
    "ATCC 1108 lists 1.0% w/v peptone, 0.05% w/v yeast extract, 0.1% "
    "w/v L-Cysteine . HCl, 1.5% w/v agar, and 20.0% fetal bovine serum. "
    "The ATCC preparation dissolves peptone, yeast extract, and cysteine "
    "in 80% final-volume distilled water, adjusts to pH 6.5 with NaOH, "
    "adds agar with heat, autoclaves for 15 minutes at 121 C, cools to "
    "45 C, and adds serum at 45 C."
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


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected the imported percent/water units, added the ATCC "
            "pH and autoclave steps, and marked the ATCC formula as curated."
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
    repaired["physical_state"] = "SOLID_AGAR"
    repaired["ph_value"] = 6.5
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["sterilization"] = copy.deepcopy(STERILIZATION)
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
