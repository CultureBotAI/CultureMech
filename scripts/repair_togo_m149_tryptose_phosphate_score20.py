#!/usr/bin/env python3
"""Repair JCM Medium 158 Tryptose Phosphate Agar from the TOGO M149 mirror."""

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

PATH = Path("bacterial/tryptose_phosphate_agar.yaml")
EXPECTED_ID = "CultureMech:002516"
EXPECTED_SOURCE_TERM = "mediadive.medium:J158"

TOGO_M149 = "https://togomedium.org/medium/M149"
SOURCE = "TOGO M149/JCM Medium 158 snapshot"
CURATOR = "repair_togo_m149_tryptose_phosphate_score20.py"
ACTION = "RESOLVED_TOGO_M149_TRYPTOSE_PHOSPHATE_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "TOGO M149 records 15 g/L Bacto agar and 29.5 g/L Tryptose "
    "phosphate broth from BD-Difco in 1.0 L distilled water."
)

IMPORTED_INGREDIENTS = frozenset({"Tryptose-phosphate", "Agar"})


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


INGREDIENTS = [
    {
        "preferred_term": "Distilled water",
        "concentration": {"value": "1000", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": "TOGO M149 lists 1.0 L distilled water.",
        "term": _term("CHEBI:15377", "water"),
        "mediaingredientmech_chebi_term": _term("CHEBI:15377", "water"),
    },
    {
        "preferred_term": "Bacto agar (BD-Difco)",
        "concentration": {"value": "15", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": "TOGO M149 lists 15 g/L Bacto agar from BD-Difco.",
    },
    {
        "preferred_term": "Tryptose phosphate broth (BD-Difco)",
        "concentration": {"value": "29.5", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": "TOGO M149 lists 29.5 g/L Tryptose phosphate broth from BD-Difco.",
    },
]
REPAIRED_INGREDIENTS = frozenset(row["preferred_term"] for row in INGREDIENTS)


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
            f"{PATH}: expected source term {EXPECTED_SOURCE_TERM}, "
            f"found {source_term!r}"
        )

    ingredient_names = {
        str(row.get("preferred_term") or "")
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    }
    if ingredient_names not in (IMPORTED_INGREDIENTS, REPAIRED_INGREDIENTS):
        raise ValueError(f"{PATH}: ingredient list drifted")


def _ensure_reference(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    if not any(
        isinstance(row, dict) and row.get("reference") == TOGO_M149
        for row in references
    ):
        references.append({"reference": TOGO_M149})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": TOGO_M149,
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
