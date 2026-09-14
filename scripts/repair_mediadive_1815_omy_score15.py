#!/usr/bin/env python3
"""Repair DSMZ/MediaDive Medium 1815 OMY."""

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
TARGET = Path("bacterial/omy.yaml")
EXPECTED_ID = "CultureMech:001248"
EXPECTED_MEDIA_TERM = "mediadive.medium:1815"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_mediadive_1815_omy_score15.py"
ACTION = "RESOLVED_MEDIADIVE_1815_OMY_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

MEDIADIVE_1815 = "https://mediadive.dsmz.de/medium/1815"
SOURCE = "DSMZ/MediaDive Medium 1815"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Oat flakes", "15", "G_PER_L"),
    ("Malt extract broth", "5", "G_PER_L"),
    ("Yeast extract", "3", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Malt extract broth": ("FOODON:03301056", "malt extract"),
    "Yeast extract": ("FOODON:03315426", "Yeast extract"),
    "Agar": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
}

NOTES = (
    "MediaDive Medium 1815 lists OMY as a complex DSMZ solid medium made from "
    "oat flakes, malt extract broth, yeast extract, agar, and distilled water."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    notes: str,
    *,
    ground: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    if ground:
        term = _term(*GROUNDINGS[preferred_term])
        row["term"] = term
        if term["id"].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)
    return row


def _source_note(amount: str, preferred_term: str) -> str:
    return f"MediaDive Medium 1815 lists {amount} {preferred_term}."


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Oat flakes",
        "15.0",
        "G_PER_L",
        (
            "MediaDive Medium 1815 lists 15.0 g oat flakes. This ingredient is "
            "left ungrounded because the pinned MIM label index has no Oat "
            "flakes decision."
        ),
        ground=False,
    ),
    _component(
        "Malt extract broth",
        "5.0",
        "G_PER_L",
        _source_note("5.0 g", "Malt extract broth"),
    ),
    _component("Yeast extract", "3.0", "G_PER_L", _source_note("3.0 g", "Yeast extract")),
    _component("Agar", "15.0", "G_PER_L", _source_note("15.0 g", "Agar")),
    _component(
        "Distilled water",
        "1000.0",
        "ML_PER_L",
        _source_note("1000.0 ml", "Distilled water"),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "HEAT",
        "description": (
            "Briefly boil oat flakes with water, then add malt extract broth, "
            "yeast extract, and agar."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the completed medium.",
    },
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in INGREDIENTS
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ingredient_signature(rows: Any) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("ingredients is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("ingredients contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"ingredient {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _ingredient_signature(doc.get("ingredients"))
    solution_signature = _ingredient_signature(doc.get("solutions"))
    if (ingredient_signature, solution_signature) not in {
        (IMPORTED_INGREDIENT_SIGNATURE, ()),
        (FINAL_INGREDIENT_SIGNATURE, ()),
    }:
        raise ValueError(f"{TARGET}: ingredient/solution signature drifted")


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

    if not any(
        isinstance(row, dict) and row.get("reference") == MEDIADIVE_1815
        for row in references
    ):
        references.append({"reference": MEDIADIVE_1815})


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": MEDIADIVE_1815,
        "notes": (
            "Added the missing 1000 ml distilled water, grounded MediaDive "
            "components via the pinned MIM label index where possible, added "
            "preparation steps, and removed false kg_microbe_match "
            "mediadive.medium:12."
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
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "ingredients")
    repaired.pop("kg_microbe_match", None)
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
