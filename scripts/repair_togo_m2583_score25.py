#!/usr/bin/env python3
"""Add source evidence and unit corrections to TOGO M2583."""

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
TARGET = "bacterial/mueller_hinton_medium_with_10_rabbit_serum.yaml"
EXPECTED_ID = "CultureMech:009151"
EXPECTED_MEDIA_TERM = "TOGO:M2583"
SOURCE_URL = "https://togomedium.org/medium/M2583"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2583_score25.py"
ACTION = "RESOLVED_TOGO_M2583_SCORE25"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

NOTES = (
    "TOGO M2583 records 22 g BD 211443 Mueller Hinton Broth in 900 ml DI Water, "
    "autoclaved at 121 C, cooled, and aseptically supplemented with 100 ml sterile "
    "rabbit serum."
)

PREPARATION_STEPS: list[dict[str, Any]] = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Prepare 900 ml DI Water with 22 g Mueller Hinton Broth (BD 211443).",
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C and let cool.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": "Aseptically add 100 ml sterile rabbit serum.",
    },
    {
        "step_number": 4,
        "action": "ALIQUOT",
        "description": "Dispense into an appropriate vessel.",
    },
]


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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
        raise ValueError(f"{TARGET}: data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated", "has_unmapped_ingredients"):
        if flag not in flags:
            flags.append(flag)


def _ensure_reference(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{TARGET}: references is not a list")

    found = {row.get("reference") for row in references if isinstance(row, dict)}
    if SOURCE_URL not in found:
        references.append({"reference": SOURCE_URL})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Corrected units and added source metadata to TOGO M2583",
        "source": SOURCE_URL,
        "notes": NOTES,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET}: curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def _check_source(doc: dict[str, Any]) -> None:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{TARGET}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: missing expected media term {EXPECTED_MEDIA_TERM}")


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected immutable id {EXPECTED_ID}, found {doc.get('id')!r}")
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = [
        {
            "preferred_term": "DI Water",
            "concentration": {"value": "900", "unit": "ML_PER_L"},
            "source": "TOGO M2583",
            "term": _term("CHEBI:15377", "water"),
            "mediaingredientmech_chebi_term": _term("CHEBI:15377", "water"),
            "notes": "TOGO M2583 lists 900 ml DI Water.",
        },
        {
            "preferred_term": "Mueller Hinton Broth (BD 211443)",
            "concentration": {"value": "22", "unit": "G_PER_L"},
            "source": "TOGO M2583",
            "notes": (
                "TOGO M2583 lists 22 g Mueller Hinton Broth from BD catalog 211443 "
                "without disclosing the broth composition."
            ),
        },
        {
            "preferred_term": "Rabbit serum",
            "concentration": {"value": "100", "unit": "ML_PER_L"},
            "source": "TOGO M2583",
            "notes": "TOGO M2583 says to aseptically add 100 ml of sterile rabbit serum.",
        },
    ]
    _put_after(repaired, "preparation_steps", copy.deepcopy(PREPARATION_STEPS), "ingredients")
    _put_after(repaired, "sterilization", {"method": "AUTOCLAVE"}, "preparation_steps")
    _put_after(repaired, "notes", NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_reference(repaired)
    _ensure_event(repaired)
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
