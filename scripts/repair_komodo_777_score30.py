#!/usr/bin/env python3
"""Repair empty KOMODO 777 SPOROMUSA SILVACETICA medium."""

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
from repair_komodo_515_score35 import (  # noqa: E402
    DSMZ_141_URL,
    DSMZ_311_URL,
    DSMZ_320_URL,
    SOURCE_141,
    SOURCE_311,
    SOURCE_320,
    Component,
    _ingredient,
    _trace_note,
    _vitamin_note,
)

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = Path("bacterial/sporomusa_silvacetica_medium.yaml")
EXPECTED_ID = "CultureMech:006435"
EXPECTED_MEDIA_TERM = "komodo.medium:777"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_777_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=777"
)
DSMZ_777_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium777.pdf"
)

SOURCE_777 = "Archived DSMZ Medium 777"

CURATOR = "repair_komodo_777_score30.py"
ACTION = "RESOLVED_KOMODO_777_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 777 defines SPOROMUSA SILVACETICA MEDIUM as DSMZ "
    "Medium 311 with betaine omitted, yeast extract and Casitone limited to "
    "1 g/L each, NaHCO3 reduced to 1.5 g/L, and 0.5% fructose added; this "
    "record expands archived DSMZ Media 777, 311, 320, and 141 into final "
    "per-liter components."
)


def _base_note(name: str, source_amount: str, value: str) -> str:
    return (
        f"{SOURCE_311} contributes {source_amount} {name} to 1000 mL "
        "distilled water plus 10 mL vitamin stock and 1 mL SL-10 trace "
        f"stock, yielding {value} g/L in the 1011 mL final formulation."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "K2HPO4",
        "0.344214",
        "G_PER_L",
        ("CHEBI:131527", "dipotassium hydrogen phosphate"),
        SOURCE_311,
        _base_note("K2HPO4", "0.348 g", "0.344214"),
    ),
    Component(
        "KH2PO4",
        "0.224530",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_311,
        _base_note("KH2PO4", "0.227 g", "0.224530"),
    ),
    Component(
        "NH4Cl",
        "0.494560",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_311,
        _base_note("NH4Cl", "0.500 g", "0.494560"),
    ),
    Component(
        "MgSO4 x 7 H2O",
        "0.494560",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        SOURCE_311,
        _base_note("MgSO4 x 7 H2O", "0.500 g", "0.494560"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.247280",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_311,
        _base_note("CaCl2 x 2 H2O", "0.250 g", "0.247280"),
    ),
    Component(
        "NaCl",
        "2.225519",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_311,
        _base_note("NaCl", "2.250 g", "2.225519"),
    ),
    Component(
        "FeSO4 x 7 H2O",
        "0.001978",
        "G_PER_L",
        ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        SOURCE_311,
        _base_note("FeSO4 x 7 H2O", "0.002 g", "0.001978"),
    ),
    Component(
        "HCl",
        "0.002473",
        "G_PER_L",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_320,
        _trace_note("HCl", "2.50 g/L", "0.002473"),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001484",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_320,
        _trace_note("FeCl2 x 4 H2O", "1.50 g/L", "0.001484"),
    ),
    Component(
        "ZnCl2",
        "0.0000692",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_320,
        _trace_note("ZnCl2", "0.070 g/L", "0.0000692"),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000989",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_320,
        _trace_note("MnCl2 x 4 H2O", "0.100 g/L", "0.0000989"),
    ),
    Component(
        "H3BO3",
        "0.00000593",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_320,
        _trace_note("H3BO3", "0.006 g/L", "0.00000593"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000188",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_320,
        _trace_note("CoCl2 x 6 H2O", "0.190 g/L", "0.000188"),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.00000198",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_320,
        _trace_note("CuCl2 x 2 H2O", "0.002 g/L", "0.00000198"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.0000237",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_320,
        _trace_note("NiCl2 x 6 H2O", "0.024 g/L", "0.0000237"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000356",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_320,
        _trace_note("Na2MoO4 x 2 H2O", "0.036 g/L", "0.0000356"),
    ),
    Component(
        "NaHSeO3",
        "0.100",
        "MICROMOLAR",
        ("CHEBI:29924", "hydrogenselenite"),
        SOURCE_311,
        f"{SOURCE_311} specifies NaHSeO3 at a final 10^-7 M concentration.",
    ),
    Component(
        "Yeast extract",
        "1.000000",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        SOURCE_777,
        f"{SOURCE_777} limits the DSMZ Medium 311 yeast extract to 1 g/L.",
    ),
    Component(
        "Casitone",
        "1.000000",
        "G_PER_L",
        None,
        SOURCE_777,
        f"{SOURCE_777} limits the DSMZ Medium 311 Casitone to 1 g/L.",
    ),
    Component(
        "D-Fructose",
        "5.000000",
        "G_PER_L",
        ("CHEBI:28757", "D-fructose"),
        SOURCE_777,
        f"{SOURCE_777} adds fructose at 0.5% final concentration.",
    ),
    Component(
        "NaHCO3",
        "1.500000",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_777,
        f"{SOURCE_777} uses only 1.5 g/L NaHCO3 for pH 6.5-6.7.",
    ),
    Component(
        "Resazurin",
        "0.000989",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_311,
        _base_note("Resazurin", "1.000 mg", "0.000989"),
    ),
    Component(
        "Cysteine-HCl x H2O",
        "0.296736",
        "G_PER_L",
        ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
        SOURCE_311,
        _base_note("Cysteine-HCl x H2O", "0.300 g", "0.296736"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.296736",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_311,
        _base_note("Na2S x 9 H2O", "0.300 g", "0.296736"),
    ),
    Component(
        "Biotin",
        "0.0000198",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_141,
        _vitamin_note("Biotin", "0.002 g/L", "0.0000198"),
    ),
    Component(
        "Folic acid",
        "0.0000198",
        "G_PER_L",
        ("CHEBI:27470", "folic acid"),
        SOURCE_141,
        _vitamin_note("Folic acid", "0.002 g/L", "0.0000198"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.0000989",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        SOURCE_141,
        _vitamin_note("Pyridoxine-HCl", "0.010 g/L", "0.0000989"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.0000495",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_141,
        _vitamin_note("Thiamine-HCl x 2 H2O", "0.005 g/L", "0.0000495"),
    ),
    Component(
        "Riboflavin",
        "0.0000495",
        "G_PER_L",
        ("CHEBI:17015", "riboflavin"),
        SOURCE_141,
        _vitamin_note("Riboflavin", "0.005 g/L", "0.0000495"),
    ),
    Component(
        "Nicotinic acid",
        "0.0000495",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        SOURCE_141,
        _vitamin_note("Nicotinic acid", "0.005 g/L", "0.0000495"),
    ),
    Component(
        "D-Ca-pantothenate",
        "0.0000495",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_141,
        _vitamin_note("D-Ca-pantothenate", "0.005 g/L", "0.0000495"),
    ),
    Component(
        "Vitamin B12",
        "0.000000989",
        "G_PER_L",
        ("CHEBI:176843", "vitamin B12"),
        SOURCE_141,
        _vitamin_note("Vitamin B12", "0.0001 g/L", "0.000000989"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.0000495",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_141,
        _vitamin_note("p-Aminobenzoic acid", "0.005 g/L", "0.0000495"),
    ),
    Component(
        "Lipoic acid",
        "0.0000495",
        "G_PER_L",
        ("CHEBI:16494", "lipoic acid"),
        SOURCE_141,
        _vitamin_note("Lipoic acid", "0.005 g/L", "0.0000495"),
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_311,
        f"{SOURCE_311} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_311,
        f"{SOURCE_311} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_311,
        (
            f"{SOURCE_311} lists 1000 mL distilled water before addition of "
            f"10 mL vitamin stock and 1 mL SL-10 trace stock; {SOURCE_777} "
            "omits betaine."
        ),
    ),
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

    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)

    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    doc["references"] = [
        {"reference": KOMODO_777_URL},
        {"reference": DSMZ_777_URL},
        {"reference": DSMZ_311_URL},
        {"reference": DSMZ_320_URL},
        {"reference": DSMZ_141_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_777_URL,
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
    repaired["ph_range"] = {"min": 6.5, "max": 6.7}
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
