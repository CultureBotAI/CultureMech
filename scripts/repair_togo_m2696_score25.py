#!/usr/bin/env python3
"""Add source evidence and groundings to TOGO M2696."""

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
TARGET = "bacterial/togo_medium_m2696.yaml"
EXPECTED_ID = "CultureMech:009248"
EXPECTED_MEDIA_TERM = "TOGO:M2696"
SOURCE_URL = "https://togomedium.org/medium/M2696"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2696_score25.py"
ACTION = "RESOLVED_TOGO_M2696_SCORE25"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

NOTES = (
    "TOGO M2696 records 0.2% Yeast extract from Difco, 1% Trypticase from BBL, "
    "and Union Carbide SAG-471 antifoam without disclosing a target antifoam amount."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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
        "changes": "Added source metadata and groundings to TOGO M2696",
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
    repaired["notes"] = NOTES
    repaired["ingredients"] = [
        {
            "preferred_term": "Yeast extract (Difco)",
            "concentration": {"value": "0.2", "unit": "PERCENT_W_V"},
            "source": "TOGO M2696",
            "term": _term("FOODON:03315426", "Yeast extract"),
            "notes": "TOGO M2696 lists 0.2% Yeast extract from Difco.",
        },
        {
            "preferred_term": "Trypticase (BBL)",
            "concentration": {"value": "1", "unit": "PERCENT_W_V"},
            "source": "TOGO M2696",
            "term": _term("MICRO:0000175", "Trypticase peptone"),
            "notes": "TOGO M2696 lists 1% Trypticase from BBL.",
        },
        {
            "preferred_term": "Antifoam (Union Carbide Corp., SAG-471)",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": "TOGO M2696",
            "notes": (
                "TOGO M2696 lists Union Carbide SAG-471 antifoam without stating "
                "an amount."
            ),
        },
    ]
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
