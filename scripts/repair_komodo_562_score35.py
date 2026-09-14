#!/usr/bin/env python3
"""Repair empty KOMODO 562 GLUTARATE medium."""

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
TARGET = Path("bacterial/glutarate_medium.yaml")
EXPECTED_ID = "CultureMech:006014"
EXPECTED_MEDIA_TERM = "komodo.medium:562"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_562_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=562"
)
DSMZ_562_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium562.pdf"
)
DSMZ_298_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium298.pdf"
)
DSMZ_320_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf"
)

SOURCE_562 = "Archived DSMZ Medium 562"
SOURCE_298 = "Archived DSMZ Medium 298"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"

CURATOR = "repair_komodo_562_score35.py"
ACTION = "RESOLVED_KOMODO_562_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 562 defines GLUTARATE MEDIUM as DSMZ Medium 298 "
    "with butanediol replaced by 2.6 g/L sodium glutarate and with 2% v/v "
    "rumen fluid; this record expands archived DSMZ Media 298, 320, and 562 "
    "into final per-liter components."
)


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    source: str
    notes: str
    term: tuple[str, str] | None = None


def _base_note(name: str, source_amount: str, value: str) -> str:
    return (
        f"{SOURCE_298} contributes {source_amount} {name} to a 1001 mL "
        f"DSMZ Medium 298 base formulation, yielding {value} g/L before "
        f"{SOURCE_562} replaces butanediol and adds rumen fluid."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_298} adds 1 mL of the {SOURCE_320} to a 1001 mL "
        f"DSMZ Medium 298 base formulation; the SL-10 stock contains "
        f"{stock_amount} {name}, yielding {value} g/L."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.199800",
        "G_PER_L",
        SOURCE_298,
        _base_note("KH2PO4", "0.20 g", "0.199800"),
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
    ),
    Component(
        "NH4Cl",
        "0.249750",
        "G_PER_L",
        SOURCE_298,
        _base_note("NH4Cl", "0.25 g", "0.249750"),
        ("CHEBI:31206", "ammonium chloride"),
    ),
    Component(
        "NaCl",
        "0.999001",
        "G_PER_L",
        SOURCE_298,
        _base_note("NaCl", "1.00 g", "0.999001"),
        ("CHEBI:26710", "sodium chloride"),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "0.399600",
        "G_PER_L",
        SOURCE_298,
        _base_note("MgCl2 x 6 H2O", "0.40 g", "0.399600"),
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    ),
    Component(
        "KCl",
        "0.499500",
        "G_PER_L",
        SOURCE_298,
        _base_note("KCl", "0.50 g", "0.499500"),
        ("CHEBI:32588", "potassium chloride"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.149850",
        "G_PER_L",
        SOURCE_298,
        _base_note("CaCl2 x 2 H2O", "0.15 g", "0.149850"),
        ("CHEBI:86158", "calcium chloride dihydrate"),
    ),
    Component(
        "Resazurin",
        "0.000999",
        "G_PER_L",
        SOURCE_298,
        _base_note("Resazurin", "1.00 mg", "0.000999"),
        ("CHEBI:8806", "Resazurin"),
    ),
    Component(
        "HCl",
        "0.002498",
        "G_PER_L",
        SOURCE_320,
        _trace_note("HCl", "2.50 g/L", "0.002498"),
        ("CHEBI:17883", "hydrogen chloride"),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001499",
        "G_PER_L",
        SOURCE_320,
        _trace_note("FeCl2 x 4 H2O", "1.50 g/L", "0.001499"),
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
    ),
    Component(
        "ZnCl2",
        "0.0000699",
        "G_PER_L",
        SOURCE_320,
        _trace_note("ZnCl2", "0.070 g/L", "0.0000699"),
        ("CHEBI:49976", "zinc dichloride"),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000999",
        "G_PER_L",
        SOURCE_320,
        _trace_note("MnCl2 x 4 H2O", "0.100 g/L", "0.0000999"),
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    ),
    Component(
        "H3BO3",
        "0.00000599",
        "G_PER_L",
        SOURCE_320,
        _trace_note("H3BO3", "0.006 g/L", "0.00000599"),
        ("CHEBI:33118", "boric acid"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000190",
        "G_PER_L",
        SOURCE_320,
        _trace_note("CoCl2 x 6 H2O", "0.190 g/L", "0.000190"),
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.00000200",
        "G_PER_L",
        SOURCE_320,
        _trace_note("CuCl2 x 2 H2O", "0.002 g/L", "0.00000200"),
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.0000240",
        "G_PER_L",
        SOURCE_320,
        _trace_note("NiCl2 x 6 H2O", "0.024 g/L", "0.0000240"),
        ("CHEBI:53542", "nickel chloride hexahydrate"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000360",
        "G_PER_L",
        SOURCE_320,
        _trace_note("Na2MoO4 x 2 H2O", "0.036 g/L", "0.0000360"),
        ("CHEBI:75213", "sodium molybdate dihydrate"),
    ),
    Component(
        "NaHCO3",
        "2.497502",
        "G_PER_L",
        SOURCE_298,
        _base_note("NaHCO3", "2.50 g", "2.497502"),
        ("CHEBI:32139", "sodium hydrogencarbonate"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.359640",
        "G_PER_L",
        SOURCE_298,
        _base_note("Na2S x 9 H2O", "0.36 g", "0.359640"),
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
    ),
    Component(
        "sodium glutarate",
        "2.600000",
        "G_PER_L",
        SOURCE_562,
        f"{SOURCE_562} replaces butanediol with 2.6 g/L sodium glutarate.",
        ("CHEBI:24329", "glutarate"),
    ),
    Component(
        "Rumen fluid",
        "20.000",
        "ML_PER_L",
        SOURCE_562,
        f"{SOURCE_562} adds 2% v/v rumen fluid to DSMZ Medium 298.",
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        SOURCE_298,
        f"{SOURCE_298} prepares the medium under 80% N2 and 20% CO2.",
        ("CHEBI:16526", "carbon dioxide"),
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        SOURCE_298,
        f"{SOURCE_298} prepares the medium under 80% N2 and 20% CO2.",
        ("CHEBI:17997", "dinitrogen"),
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        SOURCE_298,
        (
            f"{SOURCE_298} lists 1000 mL distilled water before adding the "
            "SL-10 trace solution and later anaerobic stock solutions."
        ),
        ("CHEBI:15377", "water"),
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
        {"reference": KOMODO_562_URL},
        {"reference": DSMZ_562_URL},
        {"reference": DSMZ_298_URL},
        {"reference": DSMZ_320_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": KOMODO_562_URL,
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
    ingredient: dict[str, Any] = {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": component.unit},
    }
    if component.term is not None:
        term = _term(*component.term)
        ingredient["term"] = term
        ingredient["mediaingredientmech_chebi_term"] = term
    return ingredient


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(
            f"{TARGET}: expected immutable id {EXPECTED_ID}, "
            f"found {doc.get('id')!r}"
        )
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.2, "physical_state")
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
