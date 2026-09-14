#!/usr/bin/env python3
"""Repair placeholder KOMODO 707 THERMODESULFORHABDUS MEDIUM."""

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
TARGET = Path("bacterial/thermodesulforhabdus_medium.yaml")
EXPECTED_ID = "CultureMech:006339"
EXPECTED_MEDIA_TERM = "komodo.medium:707"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_707_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=707"
)
DSMZ_707_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium707.pdf"
)
DSMZ_320_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf"
)

SOURCE_707 = "Archived DSMZ Medium 707"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"

CURATOR = "repair_komodo_707_score35.py"
ACTION = "RESOLVED_KOMODO_707_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 707 defines THERMODESULFORHABDUS MEDIUM with "
    "acetate, sulfate, mineral salts, 1 mL/L DSMZ Medium 320 SL-10 trace "
    "element solution, sodium bicarbonate for pH 6.8 adjustment, 0.15 g/L "
    "sodium sulfide, and 50 mg/L sodium dithionite; this record expands "
    "archived DSMZ Media 707 and 320 into final per-liter components."
)


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str]
    source: str
    notes: str


def _base_note(name: str, source_amount: str) -> str:
    return f"{SOURCE_707} lists {source_amount} {name} per liter."


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_707} adds 1 mL of the {SOURCE_320}; the SL-10 stock "
        f"contains {stock_amount} {name}, yielding {value} g/L."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "Na-acetate x 3 H2O",
        "6.200000",
        "G_PER_L",
        ("CHEBI:32138", "sodium acetate trihydrate"),
        SOURCE_707,
        _base_note("Na-acetate x 3 H2O", "6.20 g/L"),
    ),
    Component(
        "Na2SO4",
        "7.000000",
        "G_PER_L",
        ("CHEBI:32149", "sodium sulfate"),
        SOURCE_707,
        _base_note("Na2SO4", "7.00 g/L"),
    ),
    Component(
        "NH4Cl",
        "0.250000",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_707,
        _base_note("NH4Cl", "0.25 g/L"),
    ),
    Component(
        "KH2PO4",
        "1.000000",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_707,
        _base_note("KH2PO4", "1.00 g/L"),
    ),
    Component(
        "NaCl",
        "10.000000",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_707,
        _base_note("NaCl", "10.00 g/L"),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "3.000000",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_707,
        _base_note("MgCl2 x 6 H2O", "3.00 g/L"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.150000",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_707,
        _base_note("CaCl2 x 2 H2O", "0.15 g/L"),
    ),
    Component(
        "HCl",
        "0.002498",
        "G_PER_L",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_320,
        _trace_note("HCl", "2.50 g/L", "0.002498"),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001499",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_320,
        _trace_note("FeCl2 x 4 H2O", "1.50 g/L", "0.001499"),
    ),
    Component(
        "ZnCl2",
        "0.0000699",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_320,
        _trace_note("ZnCl2", "0.070 g/L", "0.0000699"),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000999",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_320,
        _trace_note("MnCl2 x 4 H2O", "0.100 g/L", "0.0000999"),
    ),
    Component(
        "H3BO3",
        "0.00000599",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_320,
        _trace_note("H3BO3", "0.006 g/L", "0.00000599"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000190",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_320,
        _trace_note("CoCl2 x 6 H2O", "0.190 g/L", "0.000190"),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.00000200",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_320,
        _trace_note("CuCl2 x 2 H2O", "0.002 g/L", "0.00000200"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.0000240",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_320,
        _trace_note("NiCl2 x 6 H2O", "0.024 g/L", "0.0000240"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000360",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_320,
        _trace_note("Na2MoO4 x 2 H2O", "0.036 g/L", "0.0000360"),
    ),
    Component(
        "Resazurin",
        "0.000500",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_707,
        _base_note("Resazurin", "0.50 mg/L"),
    ),
    Component(
        "NaHCO3",
        "variable",
        "VARIABLE",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_707,
        f"{SOURCE_707} adjusts medium pH to 6.8 with sterile 5% sodium bicarbonate.",
    ),
    Component(
        "sodium sulfide",
        "0.150000",
        "G_PER_L",
        ("CHEBI:76208", "sodium sulfide (anhydrous)"),
        SOURCE_707,
        f"{SOURCE_707} reduces the medium with 0.15 g/L sodium sulfide.",
    ),
    Component(
        "Na2S2O4",
        "0.050000",
        "G_PER_L",
        ("CHEBI:66870", "sodium dithionite"),
        SOURCE_707,
        f"{SOURCE_707} reduces the medium with 50 mg/L sodium dithionite.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_707,
        f"{SOURCE_707} prepares the medium anaerobically under 100% N2.",
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_707,
        f"{SOURCE_707} prepares the sodium bicarbonate stock under 80% N2 and 20% CO2.",
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_707,
        f"{SOURCE_707} lists 1000 mL distilled water.",
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
        {"reference": KOMODO_707_URL},
        {"reference": DSMZ_707_URL},
        {"reference": DSMZ_320_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_707_URL,
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
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(
            f"{TARGET}: expected immutable id {EXPECTED_ID}, found {doc.get('id')!r}"
        )
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 6.8, "physical_state")
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
