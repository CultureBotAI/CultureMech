#!/usr/bin/env python3
"""Repair TOGO M74 GAM Agar imported water units."""

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

PATH = Path("bacterial/gam_agar.yaml")
EXPECTED_ID = "CultureMech:010155"
EXPECTED_SOURCE_TERM = "TOGO:M74"

TOGO_M74 = "https://togomedium.org/medium/M74"
SOURCE = "TOGO M74/JCM Medium 83 snapshot"
CURATOR = "repair_togo_m74_gam_agar_score20.py"
ACTION = "RESOLVED_TOGO_M74_GAM_AGAR_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "TOGO M74 records 74 g/L GAM agar from Nissui in 1.0 L distilled "
    "water; this repair normalizes the imported water amount."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


INGREDIENTS = [
    {
        "preferred_term": "Distilled water",
        "concentration": {"value": "1000", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": "TOGO M74 lists 1.0 L distilled water.",
        "term": _term("CHEBI:15377", "water"),
        "mediaingredientmech_chebi_term": _term("CHEBI:15377", "water"),
    },
    {
        "preferred_term": "GAM agar (Nissui)",
        "concentration": {"value": "74", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": "TOGO M74 lists 74 g/L GAM agar from Nissui.",
    },
]


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True

    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{PATH}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERM:
        raise ValueError(
            f"{PATH}: expected source term {EXPECTED_SOURCE_TERM}, " f"found {source_term!r}"
        )

    ingredient_names = {
        str(row.get("preferred_term") or "").lower()
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    }
    if ingredient_names != {"distilled water", "gam agar (nissui)"}:
        raise ValueError(f"{PATH}: ingredient list drifted")


def _ensure_reference(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    if not any(isinstance(row, dict) and row.get("reference") == TOGO_M74 for row in references):
        references.append({"reference": TOGO_M74})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": TOGO_M74,
        "notes": NOTES,
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
    _require_target(doc)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["ingredients"] = copy.deepcopy(INGREDIENTS)
    repaired["data_quality_flags"] = [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    _ensure_reference(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / PATH
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
