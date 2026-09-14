#!/usr/bin/env python3
"""Ground DSMZ Medium 1279 Helicobacter components from its MediaDive solution."""

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

TARGET = Path("bacterial/helicobacter_medium.yaml")
TARGET_ID = "CultureMech:000742"
SOURCE_TERM_ID = "mediadive.medium:1279"
SIGNATURE = (
    "Brucella Broth",
    "Demineralized water",
    "Fetal bovine serum",
    "Vitox",
    "Skirrow supplement",
    "Amphotericin",
)

TERMS = {
    "Brucella Broth": {"id": "mediadive.compound:1136", "label": "Brucella Broth"},
    "Fetal bovine serum": {
        "id": "mediadive.compound:954",
        "label": "Fetal bovine serum",
    },
    "Vitox": {"id": "mediadive.compound:1138", "label": "Vitox"},
    "Skirrow supplement": {
        "id": "mediadive.compound:1139",
        "label": "Skirrow supplement",
    },
    "Amphotericin": {"id": "mediadive.compound:1140", "label": "Amphotericin"},
}

NOTES = {
    "Brucella Broth": "MediaDive solution 2559 lists Brucella Broth for DSMZ Medium 1279.",
    "Fetal bovine serum": (
        "MediaDive solution 2559 lists Fetal bovine serum as an aseptic "
        "addition for DSMZ Medium 1279."
    ),
    "Vitox": (
        "MediaDive solution 2559 lists Vitox as an aseptic addition for " "DSMZ Medium 1279."
    ),
    "Skirrow supplement": (
        "MediaDive solution 2559 lists Skirrow supplement as an aseptic "
        "addition for DSMZ Medium 1279."
    ),
    "Amphotericin": (
        "MediaDive solution 2559 lists Amphotericin as an aseptic addition " "for DSMZ Medium 1279."
    ),
}

CURATOR = "repair_helicobacter_medium_1279_score10.py"
ACTION = "GROUNDED_HELICOBACTER_1279_COMPONENTS"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _ingredient_signature(doc: dict[str, Any]) -> tuple[str, ...]:
    ingredients = doc.get("ingredients") or []
    if not isinstance(ingredients, list):
        raise ValueError("ingredients is not a list")
    return tuple(
        str(row.get("preferred_term") or "") for row in ingredients if isinstance(row, dict)
    )


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    term = media_term.get("term") if isinstance(media_term, dict) else {}
    return str(term.get("id") or "") if isinstance(term, dict) else ""


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)


def _ensure_event(doc: dict[str, Any]) -> None:
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")

    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Grounded Helicobacter Medium 1279 commercial additions",
        "source": "MediaDive solution 2559 for DSMZ Medium 1279",
        "notes": (
            "Copied exact MediaDive compound identifiers for Brucella Broth, "
            "Fetal bovine serum, Vitox, Skirrow supplement, and Amphotericin."
        ),
    }

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
    if doc.get("id") != TARGET_ID:
        raise ValueError(f"{TARGET}: expected {TARGET_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != SOURCE_TERM_ID:
        raise ValueError(f"{TARGET}: expected {SOURCE_TERM_ID}")
    if _ingredient_signature(doc) != SIGNATURE:
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    repaired = copy.deepcopy(doc)
    for ingredient in repaired["ingredients"]:
        preferred_term = ingredient["preferred_term"]
        if preferred_term not in TERMS:
            continue
        ingredient["term"] = copy.deepcopy(TERMS[preferred_term])
        ingredient["source"] = "MediaDive solution 2559"
        ingredient["notes"] = NOTES[preferred_term]

    _ensure_flags(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {normalized / TARGET: repair_record(_load(normalized / TARGET))}


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
