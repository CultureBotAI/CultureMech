#!/usr/bin/env python3
"""Repair sparse KOMODO 706 SYNTROPHOBACTER PFENNIGII MEDIUM."""

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
from repair_komodo_679_score35 import (  # noqa: E402
    BASE_1001_COMPONENTS,
    DSMZ_298_URL,
    DSMZ_320_URL,
    DSMZ_383_URL,
    DSMZ_503_URL,
    GASES_AND_WATER,
    SOURCE_383,
    SOURCE_503,
    Component,
)

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = Path("bacterial/syntrophobacter_pfennigii_medium.yaml")
EXPECTED_ID = "CultureMech:006338"
EXPECTED_MEDIA_TERM = "komodo.medium:706"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_706_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=706"
)
DSMZ_706_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium706.pdf"
)

SOURCE_706 = "Archived DSMZ Medium 706"

CURATOR = "repair_komodo_706_score35.py"
ACTION = "RESOLVED_KOMODO_706_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 706 defines SYNTROPHOBACTER PFENNIGII MEDIUM as "
    "DSMZ Medium 298 with only 0.7 g/L sodium sulfate, DSMZ Medium 503 "
    "vitamins, 1.5 g/L sodium propionate, 50 mg/L sulfide, 10-20 mg/L "
    "dithionite, and bicarbonate-adjusted pH 7.2-7.4; this record expands "
    "archived DSMZ Media 706, 298, 320, 503, and 383 into final per-liter "
    "components."
)


def _vitamin_note(name: str, value: str) -> str:
    return (
        f"{SOURCE_706} uses the {SOURCE_503}; KOMODO Medium 706 expands "
        f"that stock solution to {value} g/L {name} in the final medium."
    )


VITAMINS_503: tuple[Component, ...] = (
    Component(
        "Vitamin B12",
        "0.0000999",
        "G_PER_L",
        ("CHEBI:176843", "vitamin B12"),
        SOURCE_503,
        _vitamin_note("Vitamin B12", "0.0000999"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.0000799",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_503,
        _vitamin_note("p-Aminobenzoic acid", "0.0000799"),
    ),
    Component(
        "D(+)-Biotin",
        "0.0000200",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_503,
        _vitamin_note("D(+)-Biotin", "0.0000200"),
    ),
    Component(
        "Nicotinic acid",
        "0.000200",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        SOURCE_503,
        _vitamin_note("Nicotinic acid", "0.000200"),
    ),
    Component(
        "Calcium pantothenate",
        "0.0000999",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_503,
        _vitamin_note("Calcium pantothenate", "0.0000999"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.000300",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        SOURCE_503,
        _vitamin_note("Pyridoxine-HCl", "0.000300"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.000200",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_503,
        _vitamin_note("Thiamine-HCl x 2 H2O", "0.000200"),
    ),
)

KOMODO_706_ADDITIONS: tuple[Component, ...] = (
    Component(
        "Sodium propionate",
        "1.500000",
        "G_PER_L",
        ("CHEBI:132106", "sodium propionate"),
        SOURCE_706,
        f"{SOURCE_706} adds 1.5 g/L sodium propionate as the substrate.",
    ),
    Component(
        "Na2SO4",
        "0.700000",
        "G_PER_L",
        ("CHEBI:32149", "sodium sulfate"),
        SOURCE_706,
        f"{SOURCE_706} uses 0.7 g/L sodium sulfate.",
    ),
    Component(
        "sulfide",
        "0.050000",
        "G_PER_L",
        ("CHEBI:15138", "sulfide(2-)"),
        SOURCE_706,
        f"{SOURCE_706} adds 50.0 mg/L sulfide to reduce the medium.",
    ),
    Component(
        "Na2S2O4",
        "0.010-0.020",
        "G_PER_L",
        ("CHEBI:66870", "sodium dithionite"),
        SOURCE_383,
        (
            f"{SOURCE_706} adds 10-20 mg/L dithionite to reduce the medium; "
            f"{SOURCE_383} identifies the reductant as sodium dithionite."
        ),
    ),
)

COMPONENTS: tuple[Component, ...] = (
    *BASE_1001_COMPONENTS,
    *VITAMINS_503,
    *KOMODO_706_ADDITIONS,
    *GASES_AND_WATER,
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _check_source(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"expected immutable id {EXPECTED_ID}, found {doc.get('id')!r}")

    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{TARGET}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != EXPECTED_MEDIA_TERM:
        raise ValueError(
            f"{TARGET}: missing expected media term {EXPECTED_MEDIA_TERM}"
        )


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
        {"reference": KOMODO_706_URL},
        {"reference": DSMZ_706_URL},
        {"reference": DSMZ_298_URL},
        {"reference": DSMZ_320_URL},
        {"reference": DSMZ_503_URL},
        {"reference": DSMZ_383_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_706_URL,
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
    term = _term(*component.term)
    return {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": component.unit},
        "term": term,
        "mediaingredientmech_chebi_term": term,
    }


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_range", {"min": 7.2, "max": 7.4}, "physical_state")
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["ingredients"] = [_ingredient(component) for component in COMPONENTS]
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

    planned = plan_repairs(args.normalized_dir)
    changed = {
        path: doc
        for path, doc in planned.items()
        if path.read_text(encoding="utf-8") != dump_record(doc)
    }

    if args.apply:
        for path, doc in changed.items():
            write_record(path, doc)
            print(f"updated {path.relative_to(args.normalized_dir)}")
    else:
        for path in changed:
            print(f"would update {path.relative_to(args.normalized_dir)}")
        print(f"{len(changed)} file(s) would change")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
