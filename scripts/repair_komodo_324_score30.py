#!/usr/bin/env python3
"""Repair empty KOMODO 324 METHANOLOBUS II medium."""

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
TARGET = Path("archaea/methanolobus_ii_medium.yaml")
EXPECTED_ID = "CultureMech:005015"
EXPECTED_MEDIA_TERM = "komodo.medium:324"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_324_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=324"
)
DSMZ_324_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium324.pdf"
)
DSMZ_141_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf"
)

SOURCE_324 = "Archived DSMZ Medium 324"
SOURCE_141 = "Archived DSMZ Medium 141"

CURATOR = "repair_komodo_324_score30.py"
ACTION = "RESOLVED_KOMODO_324_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 324 defines METHANOLOBUS II MEDIUM as DSMZ "
    "Medium 141 prepared under 80:20 N2/CO2, with methanol added to 0.5% "
    "(v/v) after anaerobic sterilization under N2 and final pH 6.8-7.0; "
    "this record expands DSMZ Medium 141 trace and vitamin stocks into final "
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


def _main_note(name: str, amount: str, value: str) -> str:
    return (
        f"{SOURCE_141} lists {amount} {name} and adds 10 mL trace solution "
        f"and 10 mL vitamin solution to 1000 mL water, yielding {value} g/L "
        "in the 1020 mL aqueous formulation."
    )


def _combined_note(name: str, base: str, stock: str, value: str) -> str:
    return (
        f"{SOURCE_141} lists {base} {name} in the main recipe and adds 10 "
        f"mL of a trace solution containing {stock} {name} to 1000 mL water "
        f"plus 10 mL vitamin solution, yielding {value} g/L in the 1020 mL "
        "aqueous formulation."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_141} adds 10 mL of a trace solution containing "
        f"{stock_amount} {name} to 1000 mL water plus 10 mL vitamin "
        f"solution, yielding {value} g/L in the 1020 mL aqueous formulation."
    )


def _vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_141} adds 10 mL of a vitamin solution containing "
        f"{stock_amount} {name} to 1000 mL water plus 10 mL trace solution, "
        f"yielding {value} g/L in the 1020 mL aqueous formulation."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "KCl",
        "0.333333",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_141,
        _main_note("KCl", "0.34 g", "0.333333"),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "3.921569",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_141,
        _main_note("MgCl2 x 6 H2O", "4.00 g", "3.921569"),
    ),
    Component(
        "MgSO4 x 7 H2O",
        "3.411765",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        SOURCE_141,
        _combined_note("MgSO4 x 7 H2O", "3.45 g", "3.00 g/L", "3.411765"),
    ),
    Component(
        "NH4Cl",
        "0.245098",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_141,
        _main_note("NH4Cl", "0.25 g", "0.245098"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.138235",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_141,
        _combined_note("CaCl2 x 2 H2O", "0.14 g", "0.10 g/L", "0.138235"),
    ),
    Component(
        "K2HPO4",
        "0.137255",
        "G_PER_L",
        ("CHEBI:131527", "dipotassium hydrogen phosphate"),
        SOURCE_141,
        _main_note("K2HPO4", "0.14 g", "0.137255"),
    ),
    Component(
        "NaCl",
        "17.656863",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_141,
        _combined_note("NaCl", "18.00 g", "1.00 g/L", "17.656863"),
    ),
    Component(
        "Fe(NH4)2(SO4)2 x 7 H2O",
        "0.001961",
        "G_PER_L",
        ("CHEBI:131378", "Fe(NH4)2(SO4)2 x 7 H2O"),
        SOURCE_141,
        _main_note("Fe(NH4)2(SO4)2 x 7 H2O", "2.00 mg", "0.001961"),
    ),
    Component(
        "NaHCO3",
        "4.901961",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_141,
        _main_note("NaHCO3", "5.00 g", "4.901961"),
    ),
    Component(
        "Na-acetate",
        "0.980392",
        "G_PER_L",
        ("CHEBI:32954", "Na-acetate"),
        SOURCE_141,
        _main_note("Na-acetate", "1.00 g", "0.980392"),
    ),
    Component(
        "Yeast extract",
        "1.960784",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        SOURCE_141,
        _main_note("Yeast extract", "2.00 g", "1.960784"),
    ),
    Component(
        "Trypticase",
        "1.960784",
        "G_PER_L",
        ("MICRO:0000175", "Trypticase"),
        SOURCE_141,
        _main_note("Trypticase", "2.00 g", "1.960784"),
    ),
    Component(
        "Resazurin",
        "0.000980",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_141,
        _main_note("Resazurin", "1.00 mg", "0.000980"),
    ),
    Component(
        "Cysteine-HCl x H2O",
        "0.490196",
        "G_PER_L",
        ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
        SOURCE_141,
        _main_note("Cysteine-HCl x H2O", "0.50 g", "0.490196"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.490196",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_141,
        _main_note("Na2S x 9 H2O", "0.50 g", "0.490196"),
    ),
    Component(
        "Nitrilotriacetic acid",
        "0.014706",
        "G_PER_L",
        ("CHEBI:44557", "nitrilotriacetic acid"),
        SOURCE_141,
        _trace_note("Nitrilotriacetic acid", "1.50 g/L", "0.014706"),
    ),
    Component(
        "MnSO4 x H2O",
        "0.004902",
        "G_PER_L",
        ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
        SOURCE_141,
        _trace_note("MnSO4 x H2O", "0.50 g/L", "0.004902"),
    ),
    Component(
        "FeSO4 x 7 H2O",
        "0.000980",
        "G_PER_L",
        ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("FeSO4 x 7 H2O", "0.10 g/L", "0.000980"),
    ),
    Component(
        "CoSO4 x 7 H2O",
        "0.001765",
        "G_PER_L",
        ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("CoSO4 x 7 H2O", "0.18 g/L", "0.001765"),
    ),
    Component(
        "ZnSO4 x 7 H2O",
        "0.001765",
        "G_PER_L",
        ("CHEBI:32312", "zinc sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("ZnSO4 x 7 H2O", "0.18 g/L", "0.001765"),
    ),
    Component(
        "CuSO4 x 5 H2O",
        "0.000098",
        "G_PER_L",
        ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
        SOURCE_141,
        _trace_note("CuSO4 x 5 H2O", "0.01 g/L", "0.000098"),
    ),
    Component(
        "KAl(SO4)2 x 12 H2O",
        "0.000196",
        "G_PER_L",
        ("CHEBI:86465", "potassium aluminium sulfate dodecahydrate"),
        SOURCE_141,
        _trace_note("KAl(SO4)2 x 12 H2O", "0.02 g/L", "0.000196"),
    ),
    Component(
        "H3BO3",
        "0.000098",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_141,
        _trace_note("H3BO3", "0.01 g/L", "0.000098"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.000098",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_141,
        _trace_note("Na2MoO4 x 2 H2O", "0.01 g/L", "0.000098"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.000294",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_141,
        _trace_note("NiCl2 x 6 H2O", "0.03 g/L", "0.000294"),
    ),
    Component(
        "Na2SeO3 x 5 H2O",
        "0.000002941",
        "G_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        SOURCE_141,
        _trace_note("Na2SeO3 x 5 H2O", "0.30 mg/L", "0.000002941"),
    ),
    Component(
        "Biotin",
        "0.000019608",
        "G_PER_L",
        ("CHEBI:15956", "Biotin"),
        SOURCE_141,
        _vitamin_note("Biotin", "2.00 mg/L", "0.000019608"),
    ),
    Component(
        "Folic acid",
        "0.000019608",
        "G_PER_L",
        ("CHEBI:27470", "Folic acid"),
        SOURCE_141,
        _vitamin_note("Folic acid", "2.00 mg/L", "0.000019608"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.000098",
        "G_PER_L",
        ("CHEBI:30961", "Pyridoxine hydrochloride"),
        SOURCE_141,
        _vitamin_note("Pyridoxine-HCl", "10.00 mg/L", "0.000098"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.000049",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_141,
        _vitamin_note("Thiamine-HCl x 2 H2O", "5.00 mg/L", "0.000049"),
    ),
    Component(
        "Riboflavin",
        "0.000049",
        "G_PER_L",
        ("CHEBI:17015", "Riboflavin"),
        SOURCE_141,
        _vitamin_note("Riboflavin", "5.00 mg/L", "0.000049"),
    ),
    Component(
        "Nicotinic acid",
        "0.000049",
        "G_PER_L",
        ("CHEBI:15940", "Nicotinic acid"),
        SOURCE_141,
        _vitamin_note("Nicotinic acid", "5.00 mg/L", "0.000049"),
    ),
    Component(
        "Calcium pantothenate",
        "0.000049",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_141,
        _vitamin_note("D-Ca-pantothenate", "5.00 mg/L", "0.000049"),
    ),
    Component(
        "Vitamin B12",
        "0.000000980",
        "G_PER_L",
        ("CHEBI:176843", "Vitamin B12"),
        SOURCE_141,
        _vitamin_note("Vitamin B12", "0.10 mg/L", "0.000000980"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.000049",
        "G_PER_L",
        ("CHEBI:30753", "p-Aminobenzoic acid"),
        SOURCE_141,
        _vitamin_note("p-Aminobenzoic acid", "5.00 mg/L", "0.000049"),
    ),
    Component(
        "(DL)-alpha-Lipoic acid",
        "0.000049",
        "G_PER_L",
        ("CHEBI:16494", "(DL)-alpha-Lipoic acid"),
        SOURCE_141,
        _vitamin_note("Lipoic acid", "5.00 mg/L", "0.000049"),
    ),
    Component(
        "KOH",
        "variable",
        "VARIABLE",
        ("CHEBI:32035", "potassium hydroxide"),
        SOURCE_141,
        f"{SOURCE_141} adjusts the trace element solution with KOH.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_324,
        (
            f"{SOURCE_324} prepares DSMZ Medium 141 under 80% N2 plus 20% "
            "CO2 and sterilizes methanol anaerobically under 100% N2."
        ),
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_324,
        f"{SOURCE_324} prepares DSMZ Medium 141 under 80% N2 plus 20% CO2.",
    ),
    Component(
        "Methanol",
        "0.500000",
        "PERCENT_V_V",
        ("CHEBI:17790", "methanol"),
        SOURCE_324,
        (
            f"{SOURCE_324} adds anaerobically sterilized methanol to the "
            "medium to a final concentration of 0.5% v/v."
        ),
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_141,
        f"{SOURCE_141} lists 1000 mL distilled water before stock additions.",
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
        {"reference": KOMODO_324_URL},
        {"reference": DSMZ_324_URL},
        {"reference": DSMZ_141_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_324_URL,
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
    ingredient = {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": component.unit},
        "term": _term(*component.term),
    }
    if component.term[0].startswith("CHEBI:"):
        ingredient["mediaingredientmech_chebi_term"] = _term(*component.term)
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
    repaired["ph_range"] = {"min": 6.8, "max": 7.0}
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
