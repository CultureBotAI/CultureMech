#!/usr/bin/env python3
"""Repair empty KOMODO 679 SB/SW MEDIUM records."""

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

KOMODO_679_URL = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=679"
)
KOMODO_679_1_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=679.1"
)
KOMODO_679_2_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=679.2"
)
DSMZ_679_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium679.pdf"
)
DSMZ_298_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium298.pdf"
)
DSMZ_320_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf"
)
DSMZ_383_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium383.pdf"
)
DSMZ_503_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf"
)

SOURCE_679 = "Archived DSMZ Medium 679"
SOURCE_298 = "Archived DSMZ Medium 298"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"
SOURCE_383 = "Archived DSMZ Medium 383 sodium dithionite instruction"
SOURCE_503 = "Archived DSMZ Medium 503 Seven Vitamins Solution"

CURATOR = "repair_komodo_679_score35.py"
ACTION = "RESOLVED_KOMODO_679_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
BASE_NOTES = (
    "Archived DSMZ Medium 679 defines SB/SW MEDIUM as DSMZ Medium 298 "
    "with butanediol omitted; this record expands archived DSMZ Media 298, "
    "320, and 679 into final per-liter components."
)
BUSWELLII_NOTES = (
    "Archived DSMZ Medium 679 defines the S. buswellii DSM 2612M variant "
    "as DSMZ Medium 298 with butanediol omitted, 10 mL/L DSMZ Medium 503 "
    "Seven Vitamins Solution, 10 mM sodium crotonate, and sodium dithionite "
    "after inoculation; this record expands archived DSMZ Media 298, 320, "
    "383, 503, and 679 into final per-liter components."
)
WOLINII_NOTES = (
    "Archived DSMZ Medium 679 defines the S. wolinii DSM 2805M variant as "
    "DSMZ Medium 298 with butanediol omitted, 10 mL/L DSMZ Medium 503 "
    "Seven Vitamins Solution, 1.25 g/L sodium pyruvate, and sodium "
    "dithionite after inoculation; this record expands archived DSMZ "
    "Media 298, 320, 383, 503, and 679 into final per-liter components."
)


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str]
    source: str
    notes: str


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    media_term: str
    komodo_url: str
    notes: str
    substrate: Component | None = None
    uses_seven_vitamins: bool = False
    uses_dithionite: bool = False


def _base_note(name: str, source_amount: str, value: str, total_ml: int) -> str:
    return (
        f"{SOURCE_298} contributes {source_amount} {name} to a {total_ml} mL "
        f"final formulation, yielding {value} g/L."
    )


def _trace_note(name: str, stock_amount: str, value: str, total_ml: int) -> str:
    return (
        f"{SOURCE_298} adds 1 mL of the {SOURCE_320} to a {total_ml} mL "
        f"final formulation; the SL-10 stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


def _vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_679} uses 10 mL/L of the {SOURCE_503}; the Seven Vitamins "
        f"stock contains {stock_amount} {name}, yielding {value} g/L in the "
        "1011 mL final formulation."
    )


BASE_1001_COMPONENTS: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.199800",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_298,
        _base_note("KH2PO4", "0.20 g", "0.199800", 1001),
    ),
    Component(
        "NH4Cl",
        "0.249750",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_298,
        _base_note("NH4Cl", "0.25 g", "0.249750", 1001),
    ),
    Component(
        "NaCl",
        "0.999001",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_298,
        _base_note("NaCl", "1.00 g", "0.999001", 1001),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "0.399600",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_298,
        _base_note("MgCl2 x 6 H2O", "0.40 g", "0.399600", 1001),
    ),
    Component(
        "KCl",
        "0.499500",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_298,
        _base_note("KCl", "0.50 g", "0.499500", 1001),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.149850",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_298,
        _base_note("CaCl2 x 2 H2O", "0.15 g", "0.149850", 1001),
    ),
    Component(
        "Resazurin",
        "0.000999",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_298,
        _base_note("Resazurin", "1.00 mg", "0.000999", 1001),
    ),
    Component(
        "HCl",
        "0.002498",
        "G_PER_L",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_320,
        _trace_note("HCl", "2.50 g/L", "0.002498", 1001),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001499",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_320,
        _trace_note("FeCl2 x 4 H2O", "1.50 g/L", "0.001499", 1001),
    ),
    Component(
        "ZnCl2",
        "0.0000699",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_320,
        _trace_note("ZnCl2", "0.070 g/L", "0.0000699", 1001),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000999",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_320,
        _trace_note("MnCl2 x 4 H2O", "0.100 g/L", "0.0000999", 1001),
    ),
    Component(
        "H3BO3",
        "0.00000599",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_320,
        _trace_note("H3BO3", "0.006 g/L", "0.00000599", 1001),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000190",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_320,
        _trace_note("CoCl2 x 6 H2O", "0.190 g/L", "0.000190", 1001),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.00000200",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_320,
        _trace_note("CuCl2 x 2 H2O", "0.002 g/L", "0.00000200", 1001),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.0000240",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_320,
        _trace_note("NiCl2 x 6 H2O", "0.024 g/L", "0.0000240", 1001),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000360",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_320,
        _trace_note("Na2MoO4 x 2 H2O", "0.036 g/L", "0.0000360", 1001),
    ),
    Component(
        "NaHCO3",
        "2.497502",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_298,
        _base_note("NaHCO3", "2.50 g", "2.497502", 1001),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.359640",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_298,
        _base_note("Na2S x 9 H2O", "0.36 g", "0.359640", 1001),
    ),
)

BASE_1011_COMPONENTS: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.197824",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_298,
        _base_note("KH2PO4", "0.20 g", "0.197824", 1011),
    ),
    Component(
        "NH4Cl",
        "0.247280",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_298,
        _base_note("NH4Cl", "0.25 g", "0.247280", 1011),
    ),
    Component(
        "NaCl",
        "0.989120",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_298,
        _base_note("NaCl", "1.00 g", "0.989120", 1011),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "0.395648",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_298,
        _base_note("MgCl2 x 6 H2O", "0.40 g", "0.395648", 1011),
    ),
    Component(
        "KCl",
        "0.494560",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_298,
        _base_note("KCl", "0.50 g", "0.494560", 1011),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.148368",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_298,
        _base_note("CaCl2 x 2 H2O", "0.15 g", "0.148368", 1011),
    ),
    Component(
        "Resazurin",
        "0.000989",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_298,
        _base_note("Resazurin", "1.00 mg", "0.000989", 1011),
    ),
    Component(
        "HCl",
        "0.002473",
        "G_PER_L",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_320,
        _trace_note("HCl", "2.50 g/L", "0.002473", 1011),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001484",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_320,
        _trace_note("FeCl2 x 4 H2O", "1.50 g/L", "0.001484", 1011),
    ),
    Component(
        "ZnCl2",
        "0.0000692",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_320,
        _trace_note("ZnCl2", "0.070 g/L", "0.0000692", 1011),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000989",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_320,
        _trace_note("MnCl2 x 4 H2O", "0.100 g/L", "0.0000989", 1011),
    ),
    Component(
        "H3BO3",
        "0.00000593",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_320,
        _trace_note("H3BO3", "0.006 g/L", "0.00000593", 1011),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000188",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_320,
        _trace_note("CoCl2 x 6 H2O", "0.190 g/L", "0.000188", 1011),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.00000198",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_320,
        _trace_note("CuCl2 x 2 H2O", "0.002 g/L", "0.00000198", 1011),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.0000237",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_320,
        _trace_note("NiCl2 x 6 H2O", "0.024 g/L", "0.0000237", 1011),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000356",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_320,
        _trace_note("Na2MoO4 x 2 H2O", "0.036 g/L", "0.0000356", 1011),
    ),
    Component(
        "NaHCO3",
        "2.472799",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_298,
        _base_note("NaHCO3", "2.50 g", "2.472799", 1011),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.356083",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_298,
        _base_note("Na2S x 9 H2O", "0.36 g", "0.356083", 1011),
    ),
)

CROTONATE = Component(
    "sodium crotonate",
    "10.000000",
    "MILLIMOLAR",
    ("CHEBI:35899", "crotonate"),
    SOURCE_679,
    f"{SOURCE_679} adds 10 mM sodium crotonate for S. buswellii DSM 2612M.",
)

PYRUVATE = Component(
    "Sodium pyruvate",
    "1.250000",
    "G_PER_L",
    ("CHEBI:50144", "sodium pyruvate"),
    SOURCE_679,
    f"{SOURCE_679} adds 1.25 g/L sodium pyruvate for S. wolinii DSM 2805M.",
)

SEVEN_VITAMINS: tuple[Component, ...] = (
    Component(
        "Vitamin B12",
        "0.000989",
        "G_PER_L",
        ("CHEBI:176843", "vitamin B12"),
        SOURCE_503,
        _vitamin_note("Vitamin B12", "0.100 g/L", "0.000989"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.000791",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_503,
        _vitamin_note("p-Aminobenzoic acid", "0.080 g/L", "0.000791"),
    ),
    Component(
        "D(+)-Biotin",
        "0.000198",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_503,
        _vitamin_note("D(+)-Biotin", "0.020 g/L", "0.000198"),
    ),
    Component(
        "Nicotinic acid",
        "0.001978",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        SOURCE_503,
        _vitamin_note("Nicotinic acid", "0.200 g/L", "0.001978"),
    ),
    Component(
        "Calcium pantothenate",
        "0.000989",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_503,
        _vitamin_note("Calcium pantothenate", "0.100 g/L", "0.000989"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.002967",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        SOURCE_503,
        _vitamin_note("Pyridoxine hydrochloride", "0.300 g/L", "0.002967"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.001978",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_503,
        _vitamin_note("Thiamine-HCl x 2 H2O", "0.200 g/L", "0.001978"),
    ),
)

DITHIONITE = Component(
    "Na2S2O4",
    "0.010-0.020",
    "G_PER_L",
    ("CHEBI:66870", "sodium dithionite"),
    SOURCE_383,
    (
        f"{SOURCE_679} adds sodium dithionite as reductant after inoculation; "
        f"{SOURCE_383} states that adding 10-20 mg/L sodium dithionite can "
        "stimulate growth."
    ),
)

GASES_AND_WATER: tuple[Component, ...] = (
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_298,
        f"{SOURCE_298} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_298,
        f"{SOURCE_298} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_298,
        (
            f"{SOURCE_298} lists 1000 mL distilled water before adding the "
            "SL-10 trace solution and later anaerobic stock solutions."
        ),
    ),
)

TARGETS: tuple[Target, ...] = (
    Target(
        Path("bacterial/sb_sw_medium.yaml"),
        "CultureMech:006278",
        "komodo.medium:679",
        KOMODO_679_URL,
        BASE_NOTES,
    ),
    Target(
        Path("bacterial/for_s_buswellii_dsm_2612m.yaml"),
        "CultureMech:006276",
        "komodo.medium:679.1",
        KOMODO_679_1_URL,
        BUSWELLII_NOTES,
        CROTONATE,
        uses_seven_vitamins=True,
        uses_dithionite=True,
    ),
    Target(
        Path("bacterial/for_s_wolinii_dsm_2805m.yaml"),
        "CultureMech:006277",
        "komodo.medium:679.2",
        KOMODO_679_2_URL,
        WOLINII_NOTES,
        PYRUVATE,
        uses_seven_vitamins=True,
        uses_dithionite=True,
    ),
)
TARGETS_BY_ID = {target.expected_id: target for target in TARGETS}


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


def _target_for(doc: dict[str, Any]) -> Target:
    target = TARGETS_BY_ID.get(doc.get("id"))
    if target is None:
        expected = ", ".join(sorted(TARGETS_BY_ID))
        raise ValueError(f"expected immutable id in {{{expected}}}, found {doc.get('id')!r}")

    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{target.path}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != target.media_term:
        raise ValueError(f"{target.path}: missing expected media term {target.media_term}")
    return target


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

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


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = [
        {"reference": target.komodo_url},
        {"reference": DSMZ_679_URL},
        {"reference": DSMZ_298_URL},
        {"reference": DSMZ_320_URL},
    ]
    if target.uses_seven_vitamins:
        references.append({"reference": DSMZ_503_URL})
    if target.uses_dithionite:
        references.append({"reference": DSMZ_383_URL})
    doc["references"] = references


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": target.komodo_url,
        "notes": target.notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.path}: curation_history is not a list")
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


def _components(target: Target) -> list[Component]:
    components = (
        list(BASE_1011_COMPONENTS) if target.uses_seven_vitamins else list(BASE_1001_COMPONENTS)
    )
    if target.substrate is not None:
        components.append(target.substrate)
    if target.uses_seven_vitamins:
        components.extend(SEVEN_VITAMINS)
    if target.uses_dithionite:
        components.append(DITHIONITE)
    components.extend(GASES_AND_WATER)
    return components


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    target = _target_for(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.2, "physical_state")
    repaired["ingredients"] = [_ingredient(component) for component in _components(target)]
    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _ensure_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path))
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
