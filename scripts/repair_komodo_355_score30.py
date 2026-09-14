#!/usr/bin/env python3
"""Repair empty KOMODO 355 METHANOSARCINA FRISIA medium."""

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
from repair_komodo_324_score30 import COMPONENTS as KOMODO_324_COMPONENTS  # noqa: E402
from repair_komodo_324_score30 import (  # noqa: E402
    DSMZ_141_URL,
    Component,
    _term,
)

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = Path("archaea/methanosarcina_frisia_medium.yaml")
EXPECTED_ID = "CultureMech:005072"
EXPECTED_MEDIA_TERM = "komodo.medium:355"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_355_URL = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=355"
)
DSMZ_355_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium355.pdf"
)

SOURCE_355 = "Archived DSMZ Medium 355"

CURATOR = "repair_komodo_355_score30.py"
ACTION = "RESOLVED_KOMODO_355_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 355 defines METHANOSARCINA FRISIA MEDIUM as DSMZ "
    "Medium 141 prepared under 80:20 N2/CO2, with separately sterilized "
    "methanol added to 0.2% (v/v) and final pH 6.8-7.0; this record expands "
    "DSMZ Medium 141 trace and vitamin stocks into final per-liter components."
)

DSMZ_141_COMPONENTS = KOMODO_324_COMPONENTS[:-4]
DISTILLED_WATER = KOMODO_324_COMPONENTS[-1]

COMPONENTS: tuple[Component, ...] = (
    *DSMZ_141_COMPONENTS,
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_355,
        f"{SOURCE_355} prepares DSMZ Medium 141 under 80% N2 plus 20% CO2.",
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_355,
        f"{SOURCE_355} prepares DSMZ Medium 141 under 80% N2 plus 20% CO2.",
    ),
    Component(
        "Methanol",
        "0.200000",
        "PERCENT_V_V",
        ("CHEBI:17790", "methanol"),
        SOURCE_355,
        (
            f"{SOURCE_355} adds separately sterilized methanol to the medium "
            "to a final concentration of 0.2% v/v."
        ),
    ),
    DISTILLED_WATER,
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _check_source(doc: dict[str, Any]) -> None:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{TARGET}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: missing expected media term {EXPECTED_MEDIA_TERM}")


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

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "placeholder_composition",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)

    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    doc["references"] = [
        {"reference": KOMODO_355_URL},
        {"reference": DSMZ_355_URL},
        {"reference": DSMZ_141_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_355_URL,
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


def _ingredient(component: Component) -> dict[str, Any]:
    ingredient = {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": component.unit},
        "term": _term(*component.term),
    }
    if component.term[0].startswith("CHEBI:"):
        ingredient["mediaingredientmech_chebi_term"] = _term(*component.term)
    return ingredient


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(
            f"{TARGET}: expected immutable id {EXPECTED_ID}, " f"found {doc.get('id')!r}"
        )
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ph_range"] = {"min": 6.8, "max": 7.0}
    repaired["ingredients"] = [_ingredient(component) for component in COMPONENTS]
    _put_after(repaired, "notes", NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
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
