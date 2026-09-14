#!/usr/bin/env python3
"""Repair the empty KOMODO 485 Metallosphaera medium record."""

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
TARGET = "archaea/metallosphaera_medium.yaml"
EXPECTED_ID = "CultureMech:005608"
EXPECTED_MEDIA_TERM = "komodo.medium:485"
SOURCE_URL = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=485"
)
SOURCE_NAME = "KOMODO MediaInfo 485"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_485_score35.py"
ACTION = "RESOLVED_KOMODO_485_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

NOTES = (
    "KOMODO MediaInfo 485 lists 14 quantified g/L components for "
    "METALLOSPHAERA medium and also lists H2O and H2SO4 without gram or mol "
    "amounts."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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
        "needs_manual_curation",
        "source_information_unavailable",
    ):
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
        "changes": "Replaced empty KOMODO 485 composition with live KOMODO MediaInfo data",
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


def _ingredient(
    preferred_term: str,
    value: str | None,
    term: tuple[str, str] | None,
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "source": SOURCE_NAME,
        "notes": notes,
    }
    if value is not None:
        row["concentration"] = {"value": value, "unit": "G_PER_L"}
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected immutable id {EXPECTED_ID}, found {doc.get('id')!r}")
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ingredients"] = [
        _ingredient(
            "KH2PO4",
            "0.28",
            ("CHEBI:63036", "potassium dihydrogen phosphate"),
            "KOMODO MediaInfo 485 lists 0.28 g/L KH2PO4.",
        ),
        _ingredient(
            "VOSO4 x 2 H2O",
            "3.00E-5",
            ("CHEBI:87009", "vanadyl sulfate dihydrate"),
            "KOMODO MediaInfo 485 lists 3.00E-5 g/L VOSO4 x 2 H2O.",
        ),
        _ingredient(
            "sulfitic ore (e.g. pyrite)",
            "20.00",
            None,
            "KOMODO MediaInfo 485 lists 20.00 g/L sulfitic ore, e.g. pyrite.",
        ),
        _ingredient(
            "CaCl2 x 2 H2O",
            "0.07",
            ("CHEBI:86158", "calcium chloride dihydrate"),
            "KOMODO MediaInfo 485 lists 0.07 g/L CaCl2 x 2 H2O.",
        ),
        _ingredient(
            "Yeast extract",
            "1.00",
            ("FOODON:03315426", "yeast extract"),
            "KOMODO MediaInfo 485 lists 1.00 g/L yeast extract.",
        ),
        _ingredient(
            "MnCl2 x 4 H2O",
            "1.80E-3",
            ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
            "KOMODO MediaInfo 485 lists 1.80E-3 g/L MnCl2 x 4 H2O.",
        ),
        _ingredient(
            "CuCl2 x 2 H2O",
            "5.00E-5",
            ("CHEBI:86318", "copper(II) chloride dihydrate"),
            "KOMODO MediaInfo 485 lists 5.00E-5 g/L CuCl2 x 2 H2O.",
        ),
        _ingredient(
            "(NH4)2SO4",
            "1.30",
            ("CHEBI:62946", "ammonium sulfate"),
            "KOMODO MediaInfo 485 lists 1.30 g/L (NH4)2SO4.",
        ),
        _ingredient(
            "Na2MoO4 x 2 H2O",
            "3.00E-5",
            ("CHEBI:75213", "sodium molybdate dihydrate"),
            "KOMODO MediaInfo 485 lists 3.00E-5 g/L Na2MoO4 x 2 H2O.",
        ),
        _ingredient(
            "FeCl3 x 6 H2O",
            "0.02",
            ("CHEBI:86254", "iron trichloride hexahydrate"),
            "KOMODO MediaInfo 485 lists 0.02 g/L FeCl3 x 6 H2O.",
        ),
        _ingredient(
            "MgSO4 x 7 H2O",
            "0.25",
            ("CHEBI:31795", "magnesium sulfate heptahydrate"),
            "KOMODO MediaInfo 485 lists 0.25 g/L MgSO4 x 7 H2O.",
        ),
        _ingredient(
            "H2O",
            None,
            ("CHEBI:15377", "water"),
            "KOMODO MediaInfo 485 lists H2O without a gram or mol amount.",
        ),
        _ingredient(
            "ZnSO4 x 7 H2O",
            "2.20E-4",
            ("CHEBI:32312", "zinc sulfate heptahydrate"),
            "KOMODO MediaInfo 485 lists 2.20E-4 g/L ZnSO4 x 7 H2O.",
        ),
        _ingredient(
            "Na2B4O7 x 10 H2O",
            "4.50E-3",
            ("CHEBI:131366", "disodium tetraborate decahydrate"),
            "KOMODO MediaInfo 485 lists 4.50E-3 g/L Na2B4O7 x 10 H2O.",
        ),
        _ingredient(
            "CoSO4",
            "1.00E-5",
            ("CHEBI:53470", "cobalt(2+) sulfate"),
            "KOMODO MediaInfo 485 lists 1.00E-5 g/L CoSO4.",
        ),
        _ingredient(
            "H2SO4",
            None,
            ("CHEBI:26836", "sulfuric acid"),
            "KOMODO MediaInfo 485 lists H2SO4 without a gram or mol amount.",
        ),
    ]
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
