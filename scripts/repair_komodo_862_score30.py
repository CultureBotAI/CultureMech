#!/usr/bin/env python3
"""Repair empty KOMODO 862 XB45/XB90/PB90-2 MEDIUM."""

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
TARGET = Path("bacterial/xb45_xb90_pb90_2_medium.yaml")
EXPECTED_ID = "CultureMech:006693"
EXPECTED_MEDIA_TERM = "komodo.medium:862"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KOMODO_862_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=862"
)
DSMZ_862_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium862.pdf"
)
DSMZ_503_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf"
)
DSMZ_320_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf"
)
DSMZ_141_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf"
)

SOURCE_862 = "Archived DSMZ Medium 862"
SOURCE_503 = "Archived DSMZ Medium 503"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"
SOURCE_141 = "Archived DSMZ Medium 141 vitamin solution"

CURATOR = "repair_komodo_862_score30.py"
ACTION = "RESOLVED_KOMODO_862_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "Archived DSMZ Medium 862 defines XB45/XB90/PB90-2 MEDIUM as DSMZ "
    "Medium 503 with Solution D omitted, 100 mL/L bicarbonate solution, "
    "7.2 mL/L 10% glucose solution, and an additional 10 mL/L DSMZ Medium "
    "141 vitamin solution; this record expands archived DSMZ Media 862, "
    "503, 320, and 141 into final per-liter components."
)


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str]
    source: str
    notes: str


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _base_note(name: str, source_amount: str, value: str) -> str:
    return (
        f"{SOURCE_503} contributes {source_amount} {name} to a 1069.2 mL "
        f"final formulation, yielding {value} g/L."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_503} adds 1 mL of the {SOURCE_320}; the SL-10 stock "
        f"contains {stock_amount} {name}, yielding {value} g/L in the "
        "1069.2 mL final formulation."
    )


def _medium_503_vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_503} adds 1 mL of its Seven vitamins solution; the stock "
        f"contains {stock_amount} {name}, yielding {value} g/L in the "
        "1069.2 mL final formulation."
    )


def _medium_141_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_862} adds 10 mL/L of the {SOURCE_141}; the stock contains "
        f"{stock_amount} {name}, yielding {value} g/L in the 1069.2 mL "
        "final formulation."
    )


def _combined_vitamin_note(
    name: str,
    value_503: str,
    value_141: str,
    total: str,
) -> str:
    return (
        f"{SOURCE_503} and {SOURCE_141} both contribute {name}; their "
        f"scaled contributions of {value_503} and {value_141} g/L yield "
        f"{total} g/L in the 1069.2 mL final formulation."
    )


COMPONENTS: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.187056",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_503,
        _base_note("KH2PO4", "0.20 g", "0.187056"),
    ),
    Component(
        "NH4Cl",
        "0.233820",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_503,
        _base_note("NH4Cl", "0.25 g", "0.233820"),
    ),
    Component(
        "NaCl",
        "0.935279",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_503,
        _base_note("NaCl", "1.00 g", "0.935279"),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "0.374111",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_503,
        _base_note("MgCl2 x 6 H2O", "0.40 g", "0.374111"),
    ),
    Component(
        "KCl",
        "0.467639",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_503,
        _base_note("KCl", "0.50 g", "0.467639"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.140292",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_503,
        _base_note("CaCl2 x 2 H2O", "0.15 g", "0.140292"),
    ),
    Component(
        "Resazurin",
        "0.000468",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_503,
        _base_note("Resazurin", "0.50 mg", "0.000468"),
    ),
    Component(
        "HCl",
        "0.002338",
        "G_PER_L",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_320,
        _trace_note("HCl", "2.50 g/L", "0.002338"),
    ),
    Component(
        "FeCl2 x 4 H2O",
        "0.001403",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        SOURCE_320,
        _trace_note("FeCl2 x 4 H2O", "1.50 g/L", "0.001403"),
    ),
    Component(
        "ZnCl2",
        "0.0000655",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_320,
        _trace_note("ZnCl2", "0.070 g/L", "0.0000655"),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.0000935",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_320,
        _trace_note("MnCl2 x 4 H2O", "0.100 g/L", "0.0000935"),
    ),
    Component(
        "H3BO3",
        "0.00000561",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_320,
        _trace_note("H3BO3", "0.006 g/L", "0.00000561"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000178",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_320,
        _trace_note("CoCl2 x 6 H2O", "0.190 g/L", "0.000178"),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.00000187",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_320,
        _trace_note("CuCl2 x 2 H2O", "0.002 g/L", "0.00000187"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.0000224",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_320,
        _trace_note("NiCl2 x 6 H2O", "0.024 g/L", "0.0000224"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000337",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_320,
        _trace_note("Na2MoO4 x 2 H2O", "0.036 g/L", "0.0000337"),
    ),
    Component(
        "D(+)-Biotin",
        "0.0000187",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_503,
        _medium_503_vitamin_note("D(+)-Biotin", "0.020 g/L", "0.0000187"),
    ),
    Component(
        "Biotin",
        "0.0000187",
        "G_PER_L",
        ("CHEBI:15956", "biotin"),
        SOURCE_141,
        _medium_141_note("Biotin", "0.002 g/L", "0.0000187"),
    ),
    Component(
        "Folic acid",
        "0.0000187",
        "G_PER_L",
        ("CHEBI:27470", "folic acid"),
        SOURCE_141,
        _medium_141_note("Folic acid", "0.002 g/L", "0.0000187"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.000374",
        "G_PER_L",
        ("CHEBI:30961", "pyridoxine hydrochloride"),
        SOURCE_503,
        _combined_vitamin_note("Pyridoxine-HCl", "0.000281", "0.0000935", "0.000374"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.000234",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_503,
        _combined_vitamin_note(
            "Thiamine-HCl x 2 H2O",
            "0.000187",
            "0.0000468",
            "0.000234",
        ),
    ),
    Component(
        "Riboflavin",
        "0.0000468",
        "G_PER_L",
        ("CHEBI:17015", "riboflavin"),
        SOURCE_141,
        _medium_141_note("Riboflavin", "0.005 g/L", "0.0000468"),
    ),
    Component(
        "Nicotinic acid",
        "0.000234",
        "G_PER_L",
        ("CHEBI:15940", "nicotinic acid"),
        SOURCE_503,
        _combined_vitamin_note("Nicotinic acid", "0.000187", "0.0000468", "0.000234"),
    ),
    Component(
        "D-Ca-pantothenate",
        "0.0000468",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_141,
        _medium_141_note("D-Ca-pantothenate", "0.005 g/L", "0.0000468"),
    ),
    Component(
        "Calcium pantothenate",
        "0.0000935",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_503,
        _medium_503_vitamin_note("Calcium pantothenate", "0.100 g/L", "0.0000935"),
    ),
    Component(
        "Vitamin B12",
        "0.0000944",
        "G_PER_L",
        ("CHEBI:176843", "vitamin B12"),
        SOURCE_503,
        _combined_vitamin_note(
            "Vitamin B12",
            "0.0000935",
            "0.000000935",
            "0.0000944",
        ),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.000122",
        "G_PER_L",
        ("CHEBI:30753", "4-aminobenzoic acid"),
        SOURCE_503,
        _combined_vitamin_note(
            "p-Aminobenzoic acid",
            "0.0000748",
            "0.0000468",
            "0.000122",
        ),
    ),
    Component(
        "Lipoic acid",
        "0.0000468",
        "G_PER_L",
        ("CHEBI:16494", "lipoic acid"),
        SOURCE_141,
        _medium_141_note("Lipoic acid", "0.005 g/L", "0.0000468"),
    ),
    Component(
        "NaHCO3",
        "4.676394",
        "G_PER_L",
        ("CHEBI:32139", "sodium hydrogencarbonate"),
        SOURCE_862,
        (
            f"{SOURCE_862} increases DSMZ Medium 503 bicarbonate solution "
            "to 100 mL/L, yielding 4.676394 g/L NaHCO3."
        ),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.280584",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_503,
        _base_note("Na2S x 9 H2O, 3% w/v solution", "10.00 mL", "0.280584"),
    ),
    Component(
        "D-Glucose",
        "0.673401",
        "G_PER_L",
        ("CHEBI:17634", "D-glucose"),
        SOURCE_862,
        f"{SOURCE_862} adds 7.2 mL/L of a 10% w/v glucose solution.",
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
        (
            f"{SOURCE_503} lists 940 mL distilled water in Solution A; "
            f"{SOURCE_862} omits selenite-tungstate Solution D."
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

    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)

    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    doc["references"] = [
        {"reference": KOMODO_862_URL},
        {"reference": DSMZ_862_URL},
        {"reference": DSMZ_503_URL},
        {"reference": DSMZ_320_URL},
        {"reference": DSMZ_141_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_862_URL,
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
    return {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": component.unit},
        "term": _term(*component.term),
        "mediaingredientmech_chebi_term": _term(*component.term),
    }


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(
            f"{TARGET}: expected immutable id {EXPECTED_ID}, "
            f"found {doc.get('id')!r}"
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
