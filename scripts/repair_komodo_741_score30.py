#!/usr/bin/env python3
"""Repair empty KOMODO 741 CLOSTRIDIUM LONGISPORUM medium."""

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
TARGET = Path("bacterial/clostridium_longisporum_medium.yaml")
EXPECTED_ID = "CultureMech:006392"
EXPECTED_MEDIA_TERM = "komodo.medium:741"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_741_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=741"
)
DSMZ_741_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium741.pdf"
)

SOURCE_741 = "Archived DSMZ Medium 741"
SOURCE_KOMODO_741 = "KOMODO Medium 741"

CURATOR = "repair_komodo_741_score30.py"
ACTION = "RESOLVED_KOMODO_741_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 741 defines CLOSTRIDIUM LONGISPORUM MEDIUM as "
    "Reinforced Clostridial Medium (Oxoid CM 149) prepared under 100% CO2 "
    "with final pH 6.8; KOMODO Medium 741 expands the RCM base into final "
    "per-liter components."
)


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str]
    source: str
    notes: str


def _komodo_note(name: str, amount: str) -> str:
    return f"{SOURCE_KOMODO_741} expands the RCM base and lists {amount} g/L {name}."


COMPONENTS: tuple[Component, ...] = (
    Component(
        "Agar",
        "15.000000",
        "G_PER_L",
        ("CHEBI:2509", "agar"),
        SOURCE_KOMODO_741,
        _komodo_note("agar", "15.00"),
    ),
    Component(
        "Yeast extract",
        "3.000000",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        SOURCE_KOMODO_741,
        _komodo_note("yeast extract", "3.00"),
    ),
    Component(
        "Glucose",
        "5.000000",
        "G_PER_L",
        ("CHEBI:17634", "D-glucose"),
        SOURCE_KOMODO_741,
        _komodo_note("glucose", "5.00"),
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_741,
        f"{SOURCE_741} prepares the medium under 100% CO2.",
    ),
    Component(
        "Sodium acetate",
        "3.000000",
        "G_PER_L",
        ("CHEBI:32954", "sodium acetate"),
        SOURCE_KOMODO_741,
        _komodo_note("sodium acetate", "3.00"),
    ),
    Component(
        "Cysteine hydrochloride",
        "0.500000",
        "G_PER_L",
        ("CHEBI:91247", "L-cysteine hydrochloride"),
        SOURCE_KOMODO_741,
        _komodo_note("cysteine hydrochloride", "0.50"),
    ),
    Component(
        "Lab-Lemco powder",
        "10.000000",
        "G_PER_L",
        ("FOODON:03302088", "beef extract"),
        SOURCE_KOMODO_741,
        _komodo_note("Lab-Lemco powder", "10.00"),
    ),
    Component(
        "Sodium chloride",
        "5.000000",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_KOMODO_741,
        _komodo_note("sodium chloride", "5.00"),
    ),
    Component(
        "Soluble starch",
        "1.000000",
        "G_PER_L",
        ("CHEBI:28017", "starch"),
        SOURCE_KOMODO_741,
        _komodo_note("soluble starch", "1.00"),
    ),
    Component(
        "Peptone",
        "10.000000",
        "G_PER_L",
        ("FOODON:03302071", "peptone"),
        SOURCE_KOMODO_741,
        _komodo_note("peptone", "10.00"),
    ),
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
        {"reference": KOMODO_741_URL},
        {"reference": DSMZ_741_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_741_URL,
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
    row: dict[str, Any] = {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": component.unit},
        "term": term,
    }
    if component.term[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = term
    return row


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 6.8, "physical_state")
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
