#!/usr/bin/env python3
"""Repair placeholder KOMODO 131 METHANOBACTERIUM THERMOAUTOTROPHICUM MEDIUM."""

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
TARGET = Path("archaea/KOMODO_131_METHANOBACTERIUM_THERMOAUTOTROPHICUM_MEDIUM.yaml")
EXPECTED_ID = "CultureMech:004074"
EXPECTED_MEDIA_TERM = "komodo.medium:131"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_131_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=131"
)
DSMZ_131_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium131.pdf"
)

SOURCE_131 = "Archived DSMZ Medium 131"
CURATOR = "repair_komodo_131_score30.py"
ACTION = "RESOLVED_KOMODO_131_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 131 defines METHANOBACTERIUM THERMOAUTOTROPHICUM "
    "MEDIUM with base mineral salts, 10 mL/L vitamin solution, 10 mL/L trace "
    "element solution, resazurin, cysteine hydrochloride hydrate, sodium "
    "sulfide nonahydrate, pH 7.2, an 80:20 H2/CO2 anaerobic atmosphere, "
    "and N2-sterilized reducing solutions; this record expands those stock "
    "solutions into final per-liter components."
)


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str]
    source: str
    notes: str


def _base_note(name: str, amount: str) -> str:
    return f"{SOURCE_131} lists {amount} {name} per liter in the main recipe."


def _combined_note(name: str, base: str, stock: str, value: str) -> str:
    return (
        f"{SOURCE_131} lists {base} {name} per liter in the main recipe and adds "
        f"10 mL/L of a trace element solution containing {stock} {name}, "
        f"yielding {value} g/L total."
    )


def _vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_131} adds 10 mL/L of a vitamin solution containing "
        f"{stock_amount} {name}, yielding {value} g/L."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_131} adds 10 mL/L of a trace element solution containing "
        f"{stock_amount} {name}, yielding {value} g/L."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.300000",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_131,
        _base_note("KH2PO4", "0.300 g/L"),
    ),
    Component(
        "(NH4)2SO4",
        "1.500000",
        "G_PER_L",
        ("CHEBI:62946", "ammonium sulfate"),
        SOURCE_131,
        _base_note("(NH4)2SO4", "1.500 g/L"),
    ),
    Component(
        "NaCl",
        "0.610000",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_131,
        _combined_note("NaCl", "0.600 g/L", "1.000 g/L", "0.610000"),
    ),
    Component(
        "MgSO4 x 7 H2O",
        "0.182000",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        SOURCE_131,
        _combined_note("MgSO4 x 7 H2O", "0.120 g/L", "6.200 g/L", "0.182000"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.081300",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_131,
        _combined_note("CaCl2 x 2 H2O", "0.080 g/L", "0.130 g/L", "0.081300"),
    ),
    Component(
        "FeSO4 x 7 H2O",
        "0.005000",
        "G_PER_L",
        ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        SOURCE_131,
        _combined_note("FeSO4 x 7 H2O", "4.000 mg/L", "0.100 g/L", "0.005000"),
    ),
    Component(
        "K2HPO4",
        "0.150000",
        "G_PER_L",
        ("CHEBI:131527", "dipotassium hydrogen phosphate"),
        SOURCE_131,
        _base_note("K2HPO4", "0.150 g/L"),
    ),
    Component(
        "Na2CO3",
        "4.000000",
        "G_PER_L",
        ("CHEBI:29377", "sodium carbonate"),
        SOURCE_131,
        _base_note("Na2CO3", "4.000 g/L"),
    ),
    Component(
        "Na2-EDTA",
        "0.006400",
        "G_PER_L",
        ("CHEBI:64734", "EDTA disodium salt (anhydrous)"),
        SOURCE_131,
        _trace_note("Na2-EDTA", "0.640 g/L", "0.006400"),
    ),
    Component(
        "MnSO4 x 4 H2O",
        "0.005500",
        "G_PER_L",
        ("CHEBI:86358", "manganese(II) sulfate tetrahydrate"),
        SOURCE_131,
        _trace_note("MnSO4 x 4 H2O", "0.550 g/L", "0.005500"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.001700",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_131,
        _trace_note("CoCl2 x 6 H2O", "0.170 g/L", "0.001700"),
    ),
    Component(
        "ZnSO4 x 7 H2O",
        "0.001800",
        "G_PER_L",
        ("CHEBI:32312", "zinc sulfate heptahydrate"),
        SOURCE_131,
        _trace_note("ZnSO4 x 7 H2O", "0.180 g/L", "0.001800"),
    ),
    Component(
        "CuSO4",
        "0.000500",
        "G_PER_L",
        ("CHEBI:23414", "copper(II) sulfate"),
        SOURCE_131,
        _trace_note("CuSO4", "0.050 g/L", "0.000500"),
    ),
    Component(
        "KAl(SO4)2 x 12 H2O",
        "0.000180",
        "G_PER_L",
        ("CHEBI:86465", "potassium aluminium sulfate dodecahydrate"),
        SOURCE_131,
        _trace_note("KAl(SO4)2 x 12 H2O", "0.018 g/L", "0.000180"),
    ),
    Component(
        "H3BO3",
        "0.000100",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_131,
        _trace_note("H3BO3", "0.010 g/L", "0.000100"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.000110",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_131,
        _trace_note("Na2MoO4 x 2 H2O", "0.011 g/L", "0.000110"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.000250",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_131,
        _trace_note("NiCl2 x 6 H2O", "0.025 g/L", "0.000250"),
    ),
    Component(
        "Biotin",
        "0.000020",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_131,
        _vitamin_note("Biotin", "2.000 mg/L", "0.000020"),
    ),
    Component(
        "Folic acid",
        "0.000020",
        "G_PER_L",
        ("CHEBI:27470", "folic acid"),
        SOURCE_131,
        _vitamin_note("Folic acid", "2.000 mg/L", "0.000020"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.000100",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        SOURCE_131,
        _vitamin_note("Pyridoxine-HCl", "10.000 mg/L", "0.000100"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.000050",
        "G_PER_L",
        ("CHEBI:132751", "thiamine hydrochloride dihydrate"),
        SOURCE_131,
        _vitamin_note("Thiamine-HCl x 2 H2O", "5.000 mg/L", "0.000050"),
    ),
    Component(
        "Riboflavine",
        "0.000050",
        "G_PER_L",
        ("CHEBI:17015", "riboflavin"),
        SOURCE_131,
        _vitamin_note("Riboflavine", "5.000 mg/L", "0.000050"),
    ),
    Component(
        "Nicotinic acid",
        "0.000050",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        SOURCE_131,
        _vitamin_note("Nicotinic acid", "5.000 mg/L", "0.000050"),
    ),
    Component(
        "Ca-pantothenate",
        "0.000050",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_131,
        _vitamin_note("Ca-pantothenate", "5.000 mg/L", "0.000050"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.000010",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_131,
        _vitamin_note("p-Aminobenzoic acid", "1.000 mg/L", "0.000010"),
    ),
    Component(
        "Vitamin B12",
        "0.000000100",
        "G_PER_L",
        ("CHEBI:176843", "vitamin B12"),
        SOURCE_131,
        _vitamin_note("Vitamin B12", "0.010 mg/L", "0.000000100"),
    ),
    Component(
        "Resazurin",
        "0.001000",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_131,
        _base_note("Resazurin", "1.000 mg/L"),
    ),
    Component(
        "Cysteine-HCl x H2O",
        "1.500000",
        "G_PER_L",
        ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
        SOURCE_131,
        _base_note("Cysteine-HCl x H2O", "1.500 g/L"),
    ),
    Component(
        "Na2S x 9 H2O",
        "1.500000",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_131,
        _base_note("Na2S x 9 H2O", "1.500 g/L"),
    ),
    Component(
        "H2",
        "variable",
        "VARIABLE",
        ("CHEBI:18276", "dihydrogen"),
        SOURCE_131,
        f"{SOURCE_131} prepares and sterilizes the medium under 80% H2 and 20% CO2.",
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_131,
        f"{SOURCE_131} prepares and sterilizes the medium under 80% H2 and 20% CO2.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_131,
        f"{SOURCE_131} sterilizes the cysteine and sulfide solutions under N2.",
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_131,
        f"{SOURCE_131} lists 1000 mL distilled water in the main recipe.",
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
        {"reference": KOMODO_131_URL},
        {"reference": DSMZ_131_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_131_URL,
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
