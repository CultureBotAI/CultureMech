#!/usr/bin/env python3
"""Repair KOMODO Medium 131_6216 with its exact KOMODO metabolite table."""

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
TARGET = Path("bacterial/medium_131_modified_for_dsm_6216.yaml")
EXPECTED_ID = "CultureMech:004066"
EXPECTED_MEDIA_TERM = "komodo.medium:131_6216"
PARENT_PATH = "data/normalized_yaml/archaea/KOMODO_131_METHANOBACTERIUM_THERMOAUTOTROPHICUM_MEDIUM.yaml"
PARENT_ID = "CultureMech:004074"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_131_6216_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=131_6216"
)
KOMODO_131_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=131"
)
DSMZ_131_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium131.pdf"
)

SOURCE_131_6216 = "KOMODO Medium 131_6216"
SOURCE_131 = "Archived DSMZ Medium 131"
CURATOR = "repair_komodo_131_6216_score35.py"
ACTION = "RESOLVED_KOMODO_131_6216_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "KOMODO Medium 131_6216 records MEDIUM 131 MODIFIED FOR DSM 6216 as "
    "an anaerobic, defined derivative of DSMZ Medium 131 with an exact "
    "KOMODO metabolite table, including 3.00 g/L Na-acetate; archived "
    "DSMZ Medium 131 provides the pH 7.2 parent instructions and H2/CO2 "
    "and N2 gas context."
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
    return f"{SOURCE_131_6216} lists {amount} {name} per liter."


def _dsmz_note(name: str) -> str:
    return f"{SOURCE_131} applies {name} to DSMZ Medium 131 and its KOMODO 131_6216 derivative."


COMPONENTS: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.29",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_131_6216,
        _komodo_note("KH2PO4", "0.29 g"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.00167",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_131_6216,
        _komodo_note("CoCl2 x 6 H2O", "1.67E-3 g"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.08",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_131_6216,
        _komodo_note("CaCl2 x 2 H2O", "0.08 g"),
    ),
    Component(
        "Na2S x 9 H2O",
        "1.47",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_131_6216,
        _komodo_note("Na2S x 9 H2O", "1.47 g"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.0000980",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        SOURCE_131_6216,
        _komodo_note("Pyridoxine-HCl", "9.80E-5 g"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.0000490",
        "G_PER_L",
        ("CHEBI:132751", "thiamine hydrochloride dihydrate"),
        SOURCE_131_6216,
        _komodo_note("Thiamine-HCl x 2 H2O", "4.90E-5 g"),
    ),
    Component(
        "H3BO3",
        "0.0000980",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_131_6216,
        _komodo_note("H3BO3", "9.80E-5 g"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.000108",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_131_6216,
        _komodo_note("Na2MoO4 x 2 H2O", "1.08E-4 g"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.000245",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_131_6216,
        _komodo_note("NiCl2 x 6 H2O", "2.45E-4 g"),
    ),
    Component(
        "MgSO4 x 7 H2O",
        "0.18",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        SOURCE_131_6216,
        _komodo_note("MgSO4 x 7 H2O", "0.18 g"),
    ),
    Component(
        "Distilled water",
        "variable",
        "VARIABLE",
        ("CHEBI:15377", "water"),
        SOURCE_131_6216,
        "KOMODO Medium 131_6216 lists H2O with null gram and molar amounts.",
    ),
    Component(
        "Cysteine-HCl x H2O",
        "1.47",
        "G_PER_L",
        ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
        SOURCE_131_6216,
        _komodo_note("Cysteine-HCl x H2O", "1.47 g"),
    ),
    Component(
        "Resazurin",
        "0.000980",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_131_6216,
        _komodo_note("Resazurin", "9.80E-4 g"),
    ),
    Component(
        "Na2CO3",
        "3.92",
        "G_PER_L",
        ("CHEBI:29377", "sodium carbonate"),
        SOURCE_131_6216,
        _komodo_note("Na2CO3", "3.92 g"),
    ),
    Component(
        "Folic acid",
        "0.0000196",
        "G_PER_L",
        ("CHEBI:27470", "folic acid"),
        SOURCE_131_6216,
        _komodo_note("Folic acid", "1.96E-5 g"),
    ),
    Component(
        "Biotin",
        "0.0000196",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_131_6216,
        _komodo_note("Biotin", "1.96E-5 g"),
    ),
    Component(
        "CuSO4",
        "0.000490",
        "G_PER_L",
        ("CHEBI:23414", "copper(II) sulfate"),
        SOURCE_131_6216,
        _komodo_note("CuSO4", "4.90E-4 g"),
    ),
    Component(
        "K2HPO4",
        "0.15",
        "G_PER_L",
        ("CHEBI:131527", "dipotassium hydrogen phosphate"),
        SOURCE_131_6216,
        _komodo_note("K2HPO4", "0.15 g"),
    ),
    Component(
        "Na-acetate",
        "3.00",
        "G_PER_L",
        ("CHEBI:32954", "sodium acetate"),
        SOURCE_131_6216,
        _komodo_note("Na-acetate", "3.00 g"),
    ),
    Component(
        "FeSO4 x 7 H2O",
        "0.00490",
        "G_PER_L",
        ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        SOURCE_131_6216,
        _komodo_note("FeSO4 x 7 H2O", "4.90E-3 g"),
    ),
    Component(
        "Ca-pantothenate",
        "0.0000490",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_131_6216,
        _komodo_note("Ca-pantothenate", "4.90E-5 g"),
    ),
    Component(
        "Na2-EDTA",
        "0.00627",
        "G_PER_L",
        ("CHEBI:64734", "EDTA disodium salt (anhydrous)"),
        SOURCE_131_6216,
        _komodo_note("Na2-EDTA", "6.27E-3 g"),
    ),
    Component(
        "Nicotinic acid",
        "0.0000490",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        SOURCE_131_6216,
        _komodo_note("Nicotinic acid", "4.90E-5 g"),
    ),
    Component(
        "(NH4)2SO4",
        "1.47",
        "G_PER_L",
        ("CHEBI:62946", "ammonium sulfate"),
        SOURCE_131_6216,
        _komodo_note("(NH4)2SO4", "1.47 g"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.00000980",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_131_6216,
        _komodo_note("p-Aminobenzoic acid", "9.80E-6 g"),
    ),
    Component(
        "KAl(SO4)2 x 12 H2O",
        "0.000176",
        "G_PER_L",
        ("CHEBI:86465", "potassium aluminium sulfate dodecahydrate"),
        SOURCE_131_6216,
        _komodo_note("KAl(SO4)2 x 12 H2O", "1.76E-4 g"),
    ),
    Component(
        "MnSO4 x 4 H2O",
        "0.00539",
        "G_PER_L",
        ("CHEBI:86358", "manganese(II) sulfate tetrahydrate"),
        SOURCE_131_6216,
        _komodo_note("MnSO4 x 4 H2O", "5.39E-3 g"),
    ),
    Component(
        "Vitamin B12",
        "0.0000000980",
        "G_PER_L",
        ("CHEBI:176843", "vitamin B12"),
        SOURCE_131_6216,
        _komodo_note("Vitamin B12", "9.80E-8 g"),
    ),
    Component(
        "Riboflavin",
        "0.0000490",
        "G_PER_L",
        ("CHEBI:17015", "riboflavin"),
        SOURCE_131_6216,
        _komodo_note("Riboflavin", "4.90E-5 g"),
    ),
    Component(
        "ZnSO4 x 7 H2O",
        "0.00176",
        "G_PER_L",
        ("CHEBI:32312", "zinc sulfate heptahydrate"),
        SOURCE_131_6216,
        _komodo_note("ZnSO4 x 7 H2O", "1.76E-3 g"),
    ),
    Component(
        "NaCl",
        "0.60",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_131_6216,
        _komodo_note("NaCl", "0.60 g"),
    ),
    Component(
        "H2",
        "variable",
        "VARIABLE",
        ("CHEBI:18276", "dihydrogen"),
        SOURCE_131,
        _dsmz_note("an 80:20 H2/CO2 anaerobic atmosphere"),
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_131,
        _dsmz_note("an 80:20 H2/CO2 anaerobic atmosphere"),
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_131,
        _dsmz_note("N2-sterilized reducing solutions"),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


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
        {"reference": KOMODO_131_6216_URL},
        {"reference": KOMODO_131_URL},
        {"reference": DSMZ_131_URL},
    ]


def _ensure_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": KOMODO_131_6216_URL,
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


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(
            f"{TARGET}: expected immutable id {EXPECTED_ID}, found {doc.get('id')!r}"
        )
    source_term = _source_term_id(doc)
    if source_term != EXPECTED_MEDIA_TERM:
        raise ValueError(
            f"{TARGET}: expected source term {EXPECTED_MEDIA_TERM}, found {source_term!r}"
        )


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _require_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.2, "physical_state")
    repaired["ingredients"] = [_ingredient(component) for component in COMPONENTS]
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["parent_media"] = {
        "path": PARENT_PATH,
        "relationship": "STRAIN_SPECIFIC_VARIANT",
        "id": PARENT_ID,
        "name": "methanobacterium_thermoautotrophicum_medium",
    }
    repaired["variant_relationship"] = "STRAIN_SPECIFIC_VARIANT"
    repaired["variant_modifications"] = [
        (
            "KOMODO Medium 131_6216 provides DSM 6216-specific concentrations "
            "relative to DSMZ Medium 131 and adds 3.00 g/L Na-acetate."
        )
    ]
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_curation_event(repaired)
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
