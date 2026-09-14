#!/usr/bin/env python3
"""Ground the DSMZ/KOMODO 459 SUCROSE-PEPTONE-MEDIUM duplicate pair."""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_dsmz_459_score20.py"
ACTION = "RESOLVED_DSMZ_459_SCORE20_GRAPH"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

SOURCE = "DSMZ Medium 459"
DSMZ_459_URL = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium459.pdf"

PEPTONE = {"id": "MICRO:0000178", "label": "Peptone"}
SUCROSE = {"id": "CHEBI:17992", "label": "sucrose"}


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    expected_media_term: str


TARGETS: tuple[Target, ...] = (
    Target(
        path=Path("bacterial/sucrose_peptone_medium.yaml"),
        expected_id="CultureMech:001573",
        expected_media_term="mediadive.medium:459",
    ),
    Target(
        path=Path("bacterial/KOMODO_459_SUCROSE-Peptone-MEDIUM.yaml"),
        expected_id="CultureMech:005464",
        expected_media_term="komodo.medium:459",
    ),
)

EXPECTED_INGREDIENTS = [
    {
        "preferred_term": "Peptone",
        "concentration": {"value": "20", "unit": "G_PER_L"},
    },
    {
        "preferred_term": "Sucrose",
        "concentration": {"value": "20", "unit": "G_PER_L"},
    },
]

NOTES = (
    "DSMZ Medium 459 defines SUCROSE-PEPTONE-MEDIUM as 20 g/L peptone "
    "and 20 g/L sucrose in 1000 mL distilled water; this repair grounds the "
    "peptone component and adds DSMZ source evidence to the DSMZ record and "
    "matching KOMODO source duplicate."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _check_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected immutable id {target.expected_id}, "
            f"found {doc.get('id')!r}"
        )

    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{target.path}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != target.expected_media_term:
        raise ValueError(f"{target.path}: missing expected media term {target.expected_media_term}")

    compact_ingredients = [
        {
            "preferred_term": row.get("preferred_term"),
            "concentration": row.get("concentration"),
        }
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    ]
    if compact_ingredients != EXPECTED_INGREDIENTS:
        raise ValueError(f"{target.path}: ingredient list drifted")


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

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "placeholder_composition",
        "source_information_unavailable",
        "has_unmapped_ingredients",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)

    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_459_URL,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _check_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ingredients"][0]["source"] = SOURCE
    repaired["ingredients"][0]["notes"] = "DSMZ Medium 459 lists 20.0 g/L peptone."
    repaired["ingredients"][0]["term"] = dict(PEPTONE)
    repaired["ingredients"][1]["source"] = SOURCE
    repaired["ingredients"][1]["notes"] = "DSMZ Medium 459 lists 20.0 g/L sucrose."
    repaired["ingredients"][1]["term"] = dict(SUCROSE)
    repaired["ingredients"][1]["mediaingredientmech_chebi_term"] = dict(SUCROSE)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["references"] = [{"reference": DSMZ_459_URL}]
    _ensure_flags(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path), target)
        for target in TARGETS
    }


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
