#!/usr/bin/env python3
"""Repair the legacy NBRC YPG Medium record."""

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
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_nbrc_ypg_score15.py"
ACTION = "RESOLVED_NBRC_YPG_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TARGET_PATH = "bacterial/NBRC_YPG_MEDIUM.yaml"
TARGET_ID = "CultureMech:007512"
TITLE = "YPG Medium"
LEGACY_NBRC_URL = "https://www.nite.go.jp/en/nbrc/cultures/media/802.html"
CURRENT_MEDIUM_802_URL = (
    "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=802"
)

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Yeast extract", "5.0", "G_PER_L"),
    ("Peptone", "5.0", "G_PER_L"),
    ("Glucose", "20.0", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Peptone": ("MICRO:0000178", "peptone"),
    "Yeast extract": ("FOODON:03315426", "Yeast extract"),
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "DISSOLVE",
        "description": (
            "Dissolve yeast extract, peptone, glucose, and agar in "
            "1000 ml distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the medium to pH 7.0.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C for 15 minutes.",
    },
)

NOTES = (
    "Source: NBRC legacy English Medium 802 page | Link: "
    "https://www.nite.go.jp/en/nbrc/cultures/media/802.html\n\n"
    "The original NBRC import captured YPG Medium with 5.0 g/L yeast "
    "extract, 5.0 g/L peptone, 20.0 g/L glucose, and 15.0 g/L agar; "
    "preparation dissolved the ingredients in 1000 ml distilled water, "
    "adjusted the medium to pH 7.0, and autoclaved it at 121 C for 15 "
    "minutes. The legacy NBRC URL now returns NITE's 404 page, and the "
    "current NBRC Medium 802 catalogue page resolves to a different "
    "Hipolypepton/MgSO4 formula, so no live NBRC media CURIE is asserted."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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
    if not isinstance(rows, list):
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


def _has_nbrc_import(doc: dict[str, Any]) -> bool:
    return any(
        isinstance(event, dict)
        and event.get("curator") == "nbrc-import"
        and "802.html" in str(event.get("notes") or "")
        for event in doc.get("curation_history") or []
    )


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != TARGET_ID:
        raise ValueError(
            f"{TARGET_PATH}: found id {doc.get('id')!r}, expected {TARGET_ID!r}"
        )
    if not _has_nbrc_import(doc):
        raise ValueError(f"{TARGET_PATH}: missing legacy NBRC 802 import event")
    if doc.get("original_name") != TITLE:
        raise ValueError(f"{TARGET_PATH}: NBRC YPG title drifted")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature != IMPORTED_INGREDIENT_SIGNATURE:
        raise ValueError(
            f"{TARGET_PATH}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )


def _ground_components(doc: dict[str, Any]) -> None:
    for row in doc.get("ingredients") or []:
        name = str(row.get("preferred_term") or "")
        term = GROUNDINGS.get(name)
        if not term:
            continue

        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
            row.pop("mediaingredientmech_term", None)
        else:
            row.pop("mediaingredientmech_chebi_term", None)
            row.pop("mediaingredientmech_term", None)


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "has_unmapped_ingredients",
        "incomplete_composition",
        "needs_manual_curation",
    ):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "ingredients_curated",
        "legacy_source_url_unavailable",
    ):
        if flag not in flags:
            flags.append(flag)

    for row in doc.get("ingredients") or []:
        if not isinstance(row, dict):
            raise ValueError(f"{TARGET_PATH}: ingredient is not a mapping")
        term = row.get("term")
        if not isinstance(term, dict) or not term.get("id"):
            raise ValueError(f"{TARGET_PATH}: not all source rows were grounded")


def _ensure_reference(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    found = {row.get("reference") for row in references if isinstance(row, dict)}
    if LEGACY_NBRC_URL not in found:
        references.append({"reference": LEGACY_NBRC_URL})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Grounded legacy NBRC YPG Medium formula",
        "source": LEGACY_NBRC_URL,
        "notes": (
            "Structured pH 7.0, grounded yeast extract, peptone, glucose, "
            "and agar, added the legacy NBRC reference, and marked the old "
            "NBRC source URL unavailable because current NBRC Medium 802 "
            "contains a different Hipolypepton/MgSO4 formula."
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


def repair_document(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "name", TITLE, "id")
    _put_after(repaired, "original_name", TITLE, "name")
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("media_term", None)
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["notes"] = NOTES

    _ground_components(repaired)
    _ensure_flags(repaired)
    _ensure_reference(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET_PATH
    return {path: repair_document(_load(path))}


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

    action = "Updated" if args.apply else "Would update"
    print(f"{action} {changed_count} NBRC YPG records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
