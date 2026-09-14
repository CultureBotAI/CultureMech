#!/usr/bin/env python3
"""Repair KOMODO 1429 Sabouraud Glucose Medium."""

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
TARGET = Path("bacterial/sabouraud_glucose_medium.yaml")
EXPECTED_ID = "CultureMech:004154"
EXPECTED_MEDIA_TERM = "komodo.medium:1429"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_1429_sabouraud_score15.py"
ACTION = "RESOLVED_KOMODO_1429_SABOURAUD_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

DSMZ_1429 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1429.pdf"

SOURCE = "DSMZ Medium 1429"
TITLE = "SABOURAUD GLUCOSE MEDIUM"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("SABOURAUD- Glucose-Bouillon", "30", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("SABOURAUD-2% Glucose-Bouillon (Merck 108339)", "30.0", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

REFERENCES = (DSMZ_1429,)

NOTES = (
    "KOMODO Medium 1429 maps to DSMZ Medium 1429. DSMZ Medium 1429 "
    "contains 30.0 g SABOURAUD-2% Glucose-Bouillon (Merck 108339), "
    "15.0 g agar, and 1000.0 ml distilled water. The DSMZ pH 3-4 "
    "and pH 4-5 instructions describe acidified strain-specific variants "
    "prepared by adding filter-sterilized acetic acid after autoclaving, "
    "not the base three-component medium."
)

INGREDIENTS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "SABOURAUD-2% Glucose-Bouillon (Merck 108339)",
        "concentration": {"value": "30.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": (
            "DSMZ Medium 1429 lists 30.0 g SABOURAUD-2% "
            "Glucose-Bouillon (Merck 108339); this commercial product is "
            "retained as an opaque complex component."
        ),
    },
    {
        "preferred_term": "Agar",
        "concentration": {"value": "15.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": "DSMZ Medium 1429 lists 15.0 g agar.",
        "term": {"id": "CHEBI:2509", "label": "agar"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:2509", "label": "agar"},
    },
    {
        "preferred_term": "Distilled water",
        "concentration": {"value": "1000.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": "DSMZ Medium 1429 lists 1000.0 ml distilled water.",
        "term": {"id": "CHEBI:15377", "label": "water"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
    },
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Suspend 30.0 g SABOURAUD-2% Glucose-Bouillon "
            "(Merck 108339) and 15.0 g agar in 1000.0 ml "
            "distilled water."
        ),
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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
            f"{NOTES} Added the DSMZ distilled-water row, corrected the "
            "Sabouraud broth product name, grounded water and agar, retained "
            "the Sabouraud broth as an unmapped opaque ingredient, and removed "
            "the imported pH 3-4 range because DSMZ applies that pH to an "
            "acetic-acid variant rather than to the base medium."
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
    repaired.pop("ph_range", None)
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
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
