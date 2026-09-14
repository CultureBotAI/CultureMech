#!/usr/bin/env python3
"""Repair empty KOMODO 686 PROPIONIGENIUM MARIS medium."""

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
TARGET = Path("bacterial/propionigenium_maris_medium.yaml")
EXPECTED_ID = "CultureMech:006291"
EXPECTED_MEDIA_TERM = "komodo.medium:686"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_686_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=686"
)
DSMZ_686_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium686.pdf"
)
DSMZ_504_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium504.pdf"
)
DSMZ_503_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf"
)
DSMZ_320_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf"
)
DSMZ_385_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf"
)

SOURCE_686 = "Archived DSMZ Medium 686"
SOURCE_504 = "Archived DSMZ Medium 504"
SOURCE_503 = "Archived DSMZ Medium 503"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"
SOURCE_385 = "Archived DSMZ Medium 385 selenite/tungsten solution"

CURATOR = "repair_komodo_686_score35.py"
ACTION = "RESOLVED_KOMODO_686_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 686 defines PROPIONIGENIUM MARIS MEDIUM as DSMZ "
    "Medium 504 supplemented with 0.05% yeast extract and 2.5 g/L "
    "disodium succinate; Medium 504 is DSMZ Medium 503 with 20 g/L NaCl "
    "and 3.0 g/L MgCl2 x 6 H2O. This record expands archived DSMZ Media "
    "503, 504, 686, 320, and 385 into final per-liter components."
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
        f"{SOURCE_503} contributes {source_amount} {name} to a 1013 mL "
        f"final formulation, yielding {value} g/L."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_503} adds 1 mL of the {SOURCE_320} to a 1013 mL final "
        f"formulation; the SL-10 stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


def _vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_503} adds 1 mL of its Seven vitamins solution to a "
        f"1013 mL final formulation; the stock contains {stock_amount} "
        f"{name}, yielding {value} g/L."
    )


def _selenite_tungstate_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_503} adds 1 mL of the {SOURCE_385} to a 1013 mL final "
        f"formulation; the stock contains {stock_amount} {name}, yielding "
        f"{value} g/L."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.197433",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_503,
        _base_note("KH2PO4", "0.20 g", "0.197433"),
    ),
    Component(
        "NH4Cl",
        "0.246792",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_503,
        _base_note("NH4Cl", "0.25 g", "0.246792"),
    ),
    Component(
        "NaCl",
        "20.000000",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_504,
        f"{SOURCE_504} increases the DSMZ Medium 503 NaCl amount to 20 g/L.",
    ),
    Component(
        "MgCl2 x 6 H2O",
        "3.000000",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_504,
        f"{SOURCE_504} increases the DSMZ Medium 503 MgCl2 x 6 H2O amount to 3.0 g/L.",
    ),
    Component(
        "KCl",
        "0.493583",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_503,
        _base_note("KCl", "0.50 g", "0.493583"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.148075",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_503,
        _base_note("CaCl2 x 2 H2O", "0.15 g", "0.148075"),
    ),
    Component(
        "Resazurin",
        "0.000494",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_503,
        _base_note("Resazurin", "0.50 mg", "0.000494"),
    ),
    Component(
        "HCl",
        "0.002468",
        "G_PER_L",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_320,
        _trace_note("HCl", "2.50 g/L", "0.002468"),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001481",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_320,
        _trace_note("FeCl2 x 4 H2O", "1.50 g/L", "0.001481"),
    ),
    Component(
        "ZnCl2",
        "0.0000691",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_320,
        _trace_note("ZnCl2", "0.070 g/L", "0.0000691"),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000987",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_320,
        _trace_note("MnCl2 x 4 H2O", "0.100 g/L", "0.0000987"),
    ),
    Component(
        "H3BO3",
        "0.00000592",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_320,
        _trace_note("H3BO3", "0.006 g/L", "0.00000592"),
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
        "0.00000197",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_320,
        _trace_note("CuCl2 x 2 H2O", "0.002 g/L", "0.00000197"),
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
        "0.0000355",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_320,
        _trace_note("Na2MoO4 x 2 H2O", "0.036 g/L", "0.0000355"),
    ),
    Component(
        "Vitamin B12",
        "0.0000987",
        "G_PER_L",
        ("CHEBI:176843", "vitamin B12"),
        SOURCE_503,
        _vitamin_note("Vitamin B12", "0.100 g/L", "0.0000987"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.0000790",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_503,
        _vitamin_note("p-Aminobenzoic acid", "0.080 g/L", "0.0000790"),
    ),
    Component(
        "D(+)-Biotin",
        "0.0000197",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_503,
        _vitamin_note("D(+)-Biotin", "0.020 g/L", "0.0000197"),
    ),
    Component(
        "Nicotinic acid",
        "0.000197",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        SOURCE_503,
        _vitamin_note("Nicotinic acid", "0.200 g/L", "0.000197"),
    ),
    Component(
        "Calcium pantothenate",
        "0.0000987",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_503,
        _vitamin_note("Calcium pantothenate", "0.100 g/L", "0.0000987"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.000296",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        SOURCE_503,
        _vitamin_note("Pyridoxine hydrochloride", "0.300 g/L", "0.000296"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.000197",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_503,
        _vitamin_note("Thiamine-HCl x 2 H2O", "0.200 g/L", "0.000197"),
    ),
    Component(
        "NaOH",
        "0.000395",
        "G_PER_L",
        ("CHEBI:32145", "sodium hydroxide"),
        SOURCE_385,
        _selenite_tungstate_note("NaOH", "0.500 g/L", "0.000395"),
    ),
    Component(
        "Na2SeO3 x 5 H2O",
        "0.00000592",
        "G_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        SOURCE_385,
        _selenite_tungstate_note("Na2SeO3 x 5 H2O", "0.003 g/L", "0.00000592"),
    ),
    Component(
        "Na2WO4 x 2 H2O",
        "0.00000790",
        "G_PER_L",
        ("CHEBI:63939", "sodium tungstate dihydrate"),
        SOURCE_385,
        _selenite_tungstate_note("Na2WO4 x 2 H2O", "0.004 g/L", "0.00000790"),
    ),
    Component(
        "NaHCO3",
        "2.467917",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_503,
        _base_note("NaHCO3, 5% w/v solution", "50.00 mL", "2.467917"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.296150",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_503,
        _base_note("Na2S x 9 H2O, 3% w/v solution", "10.00 mL", "0.296150"),
    ),
    Component(
        "Disodium succinate",
        "2.500000",
        "G_PER_L",
        ("CHEBI:63675", "sodium succinate (anhydrous)"),
        SOURCE_686,
        f"{SOURCE_686} adds 2.5 g/L disodium succinate as the substrate.",
    ),
    Component(
        "Yeast extract",
        "0.500000",
        "G_PER_L",
        None,
        SOURCE_686,
        f"{SOURCE_686} supplements DSMZ Medium 504 with 0.05% yeast extract.",
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_503,
        f"{SOURCE_503} prepares medium part A under 80% N2 and 20% CO2.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_503,
        f"{SOURCE_503} prepares anaerobic stock solutions under N2.",
    ),
    Component(
        "Distilled water",
        "940.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_503,
        f"{SOURCE_503} lists 940 mL distilled water in Solution A.",
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
        {"reference": KOMODO_686_URL},
        {"reference": DSMZ_686_URL},
        {"reference": DSMZ_504_URL},
        {"reference": DSMZ_503_URL},
        {"reference": DSMZ_320_URL},
        {"reference": DSMZ_385_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_686_URL,
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
        term = _term(*component.term)
        row["term"] = term
        row["mediaingredientmech_chebi_term"] = term
    return row


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(
            f"{TARGET}: expected immutable id {EXPECTED_ID}, found {doc.get('id')!r}"
        )
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_range", {"min": 7.2, "max": 7.4}, "physical_state")
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
