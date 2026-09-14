#!/usr/bin/env python3
"""Repair empty KOMODO 515 ACETONEMA medium."""

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
TARGET = "bacterial/acetonema_medium.yaml"
EXPECTED_ID = "CultureMech:005871"
EXPECTED_MEDIA_TERM = "komodo.medium:515"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_515_URL = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=515"
)
DSMZ_515_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium515.pdf"
)
DSMZ_311_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium311.pdf"
)
DSMZ_320_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf"
)
DSMZ_141_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf"
)

SOURCE_515 = "Archived DSMZ Medium 515"
SOURCE_311 = "Archived DSMZ Medium 311"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"
SOURCE_141 = "Archived DSMZ Medium 141 vitamin solution"

CURATOR = "repair_komodo_515_score35.py"
ACTION = "RESOLVED_KOMODO_515_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 515 defines ACETONEMA MEDIUM as DSMZ Medium 311 "
    "with 0.2% separately sterilized glucose replacing betaine and 1 mM "
    "dithiothreitol replacing cysteine and sulfide; this record expands "
    "archived DSMZ Media 311, 320, and 141 into final per-liter components."
)


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str] | None
    source: str
    notes: str


def _base_note(name: str, source_amount: str, value: str) -> str:
    return (
        f"{SOURCE_311} contributes {source_amount} {name} to 1000 mL "
        "distilled water plus 10 mL vitamin stock and 1 mL SL-10 trace "
        f"stock, yielding {value} g/L in 1011 mL final formulation."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_311} adds 1 mL of the {SOURCE_320} per 1011 mL final "
        f"formulation; the SL-10 stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


def _vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_311} adds 10 mL of the {SOURCE_141} per 1011 mL final "
        f"formulation; the vitamin stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
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
        "1.978239",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        SOURCE_311,
        _base_note("Yeast extract", "2.000 g", "1.978239"),
    ),
    Component(
        "Casitone",
        "1.978239",
        "G_PER_L",
        None,
        SOURCE_311,
        _base_note("Casitone", "2.000 g", "1.978239"),
    ),
    Component(
        "D-Glucose",
        "2.000000",
        "G_PER_L",
        ("CHEBI:17634", "D-glucose"),
        SOURCE_515,
        (
            f"{SOURCE_515} replaces betaine with 0.2% separately sterilized "
            "glucose, equivalent to 2 g/L."
        ),
    ),
    Component(
        "NaHCO3",
        "3.956479",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_311,
        _base_note("NaHCO3", "4.000 g", "3.956479"),
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
        "Dithiothreitol",
        "1.000",
        "MILLIMOLAR",
        ("CHEBI:18320", "1,4-dithiothreitol"),
        SOURCE_515,
        (f"{SOURCE_515} replaces cysteine and sodium sulfide with " "1 mmol/L dithiothreitol."),
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
            "10 mL vitamin stock and 1 mL SL-10 trace stock."
        ),
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
    for flag in (
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{TARGET}: references is not a list")

    found = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in (
        KOMODO_515_URL,
        DSMZ_515_URL,
        DSMZ_311_URL,
        DSMZ_320_URL,
        DSMZ_141_URL,
    ):
        if url not in found:
            references.append({"reference": url})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Replaced empty KOMODO 515 composition with archived DSMZ data",
        "source": DSMZ_515_URL,
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
    row: dict[str, Any] = {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": component.unit},
    }
    if component.term is not None:
        row["term"] = _term(*component.term)
        if component.term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*component.term)
    return row


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected immutable id {EXPECTED_ID}, found {doc.get('id')!r}")
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
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
