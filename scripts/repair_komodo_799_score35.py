#!/usr/bin/env python3
"""Repair empty KOMODO 799 DESULFOVIBRIO INOPINATUS records."""

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

KOMODO_799_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=799"
)
KOMODO_799_REPLACE_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed"
    "?MediaInfo=799_replace_Na-pyruvate_with_1,2,4-trihydroxybenzene"
)
DSMZ_799_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium799.pdf"
)
DSMZ_193_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium193.pdf"
)
DSMZ_320_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf"
)
DSMZ_141_URL = (
    "https://web.archive.org/web/20121030075431id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf"
)
DSMZ_385_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf"
)
DSMZ_503_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf"
)

SOURCE_799 = "Archived DSMZ Medium 799"
SOURCE_193 = "Archived DSMZ Medium 193"
SOURCE_320 = "Archived DSMZ Medium 320 SL-10 trace element solution"
SOURCE_141 = "Archived DSMZ Medium 141 vitamin solution"
SOURCE_385 = "Archived DSMZ Medium 385 selenite/tungsten solution"
SOURCE_503 = "Archived DSMZ Medium 503 Seven Vitamins Solution"

CURATOR = "repair_komodo_799_score35.py"
ACTION = "RESOLVED_KOMODO_799_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES_799 = (
    "Archived DSMZ Medium 799 defines DESULFOVIBRIO INOPINATUS MEDIUM as "
    "DSMZ Medium 193 supplemented with 1 mL/L DSMZ Medium 503 Seven "
    "Vitamins Solution, 1 mL/L DSMZ Medium 385 selenite-tungstate "
    "solution, 5 mL/L of a 10% yeast extract stock, and 10 mL/L of 25% "
    "Na-pyruvate replacing acetate; this record expands archived DSMZ "
    "Media 193, 320, 141, 385, 503, and 799 into final per-liter "
    "components."
)
NOTES_799_REPLACE = (
    "Archived DSMZ Medium 799 defines DESULFOVIBRIO INOPINATUS MEDIUM as "
    "DSMZ Medium 193 supplemented with DSMZ Medium 503 Seven Vitamins "
    "Solution, DSMZ Medium 385 selenite-tungstate solution, 5 mL/L of a "
    "10% yeast extract stock, and 2 mM 1,2,4-trihydroxybenzene replacing "
    "acetate; the KOMODO replacement variant expands this trihydroxybenzene "
    "branch into final per-liter components."
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
    path: str
    expected_id: str
    expected_media_term: str
    notes: str
    components: tuple[Component, ...]
    references: tuple[str, ...]


def _base_note(final_ml: int, name: str, source_amount: str, value: str) -> str:
    return (
        f"{SOURCE_193} contributes {source_amount} {name} to a {final_ml} mL "
        f"final formulation, yielding {value} g/L."
    )


def _trace_note(final_ml: int, name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_193} adds 1 mL of the {SOURCE_320} to a {final_ml} mL "
        f"final formulation; the SL-10 stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


def _medium_141_note(final_ml: int, name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_193} adds 10 mL of the {SOURCE_141} to a {final_ml} mL "
        f"final formulation; the vitamin stock contains {stock_amount} {name}, "
        f"yielding {value} g/L."
    )


def _medium_503_note(final_ml: int, name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_799} uses 1 mL/L of the {SOURCE_503}; the Seven Vitamins "
        f"stock contains {stock_amount} {name}, yielding {value} g/L in the "
        f"{final_ml} mL final formulation."
    )


def _combined_vitamin_note(
    final_ml: int,
    name: str,
    value_141: str,
    value_503: str,
    total: str,
) -> str:
    return (
        f"{SOURCE_141} and {SOURCE_503} both contribute {name}; their scaled "
        f"contributions of {value_141} and {value_503} g/L yield {total} g/L "
        f"in the {final_ml} mL final formulation."
    )


def _selenite_tungstate_note(
    final_ml: int,
    name: str,
    stock_amount: str,
    value: str,
) -> str:
    return (
        f"{SOURCE_799} adds 1 mL/L of the {SOURCE_385}; the stock contains "
        f"{stock_amount} {name}, yielding {value} g/L in the {final_ml} mL "
        "final formulation."
    )


def _common_components(
    final_ml: int,
    values: dict[str, str],
    substrates: tuple[Component, ...],
) -> tuple[Component, ...]:
    return (
        Component(
            "Na2SO4",
            values["Na2SO4"],
            "G_PER_L",
            ("CHEBI:32149", "sodium sulfate"),
            SOURCE_193,
            _base_note(final_ml, "Na2SO4", "3.00 g", values["Na2SO4"]),
        ),
        Component(
            "KH2PO4",
            values["KH2PO4"],
            "G_PER_L",
            ("CHEBI:63036", "potassium dihydrogen phosphate"),
            SOURCE_193,
            _base_note(final_ml, "KH2PO4", "0.20 g", values["KH2PO4"]),
        ),
        Component(
            "NH4Cl",
            values["NH4Cl"],
            "G_PER_L",
            ("CHEBI:31206", "ammonium chloride"),
            SOURCE_193,
            _base_note(final_ml, "NH4Cl", "0.30 g", values["NH4Cl"]),
        ),
        Component(
            "NaCl",
            values["NaCl"],
            "G_PER_L",
            ("CHEBI:26710", "sodium chloride"),
            SOURCE_193,
            _base_note(final_ml, "NaCl", "7.00 g", values["NaCl"]),
        ),
        Component(
            "MgCl2 x 6 H2O",
            values["MgCl2"],
            "G_PER_L",
            ("CHEBI:86345", "magnesium dichloride hexahydrate"),
            SOURCE_193,
            _base_note(final_ml, "MgCl2 x 6 H2O", "1.30 g", values["MgCl2"]),
        ),
        Component(
            "KCl",
            values["KCl"],
            "G_PER_L",
            ("CHEBI:32588", "potassium chloride"),
            SOURCE_193,
            _base_note(final_ml, "KCl", "0.50 g", values["KCl"]),
        ),
        Component(
            "CaCl2 x 2 H2O",
            values["CaCl2"],
            "G_PER_L",
            ("CHEBI:86158", "calcium chloride dihydrate"),
            SOURCE_193,
            _base_note(final_ml, "CaCl2 x 2 H2O", "0.15 g", values["CaCl2"]),
        ),
        Component(
            "Resazurin",
            values["Resazurin"],
            "G_PER_L",
            ("CHEBI:8806", "Resazurin"),
            SOURCE_193,
            _base_note(final_ml, "Resazurin", "1.00 mg", values["Resazurin"]),
        ),
        Component(
            "HCl",
            values["HCl"],
            "G_PER_L",
            ("CHEBI:17883", "hydrogen chloride"),
            SOURCE_320,
            _trace_note(final_ml, "HCl", "2.50 g/L", values["HCl"]),
        ),
        Component(
            "FeCl2 x 4 H2O",
            values["FeCl2"],
            "G_PER_L",
            ("CHEBI:86249", "iron dichloride tetrahydrate"),
            SOURCE_320,
            _trace_note(final_ml, "FeCl2 x 4 H2O", "1.50 g/L", values["FeCl2"]),
        ),
        Component(
            "ZnCl2",
            values["ZnCl2"],
            "G_PER_L",
            ("CHEBI:49976", "zinc dichloride"),
            SOURCE_320,
            _trace_note(final_ml, "ZnCl2", "0.070 g/L", values["ZnCl2"]),
        ),
        Component(
            "MnCl2 x 4 H2O",
            values["MnCl2"],
            "G_PER_L",
            ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
            SOURCE_320,
            _trace_note(final_ml, "MnCl2 x 4 H2O", "0.100 g/L", values["MnCl2"]),
        ),
        Component(
            "H3BO3",
            values["H3BO3"],
            "G_PER_L",
            ("CHEBI:33118", "boric acid"),
            SOURCE_320,
            _trace_note(final_ml, "H3BO3", "0.006 g/L", values["H3BO3"]),
        ),
        Component(
            "CoCl2 x 6 H2O",
            values["CoCl2"],
            "G_PER_L",
            ("CHEBI:53503", "cobalt chloride hexahydrate"),
            SOURCE_320,
            _trace_note(final_ml, "CoCl2 x 6 H2O", "0.190 g/L", values["CoCl2"]),
        ),
        Component(
            "CuCl2 x 2 H2O",
            values["CuCl2"],
            "G_PER_L",
            ("CHEBI:86318", "copper(II) chloride dihydrate"),
            SOURCE_320,
            _trace_note(final_ml, "CuCl2 x 2 H2O", "0.002 g/L", values["CuCl2"]),
        ),
        Component(
            "NiCl2 x 6 H2O",
            values["NiCl2"],
            "G_PER_L",
            ("CHEBI:53542", "nickel chloride hexahydrate"),
            SOURCE_320,
            _trace_note(final_ml, "NiCl2 x 6 H2O", "0.024 g/L", values["NiCl2"]),
        ),
        Component(
            "Na2MoO4 x 2 H2O",
            values["Na2MoO4"],
            "G_PER_L",
            ("CHEBI:75213", "sodium molybdate dihydrate"),
            SOURCE_320,
            _trace_note(final_ml, "Na2MoO4 x 2 H2O", "0.036 g/L", values["Na2MoO4"]),
        ),
        Component(
            "NaHCO3",
            values["NaHCO3"],
            "G_PER_L",
            ("CHEBI:32139", "sodium hydrogencarbonate"),
            SOURCE_193,
            _base_note(final_ml, "NaHCO3", "5.00 g", values["NaHCO3"]),
        ),
        *substrates,
        Component(
            "Biotin",
            values["Biotin141"],
            "G_PER_L",
            ("CHEBI:15956", "biotin"),
            SOURCE_141,
            _medium_141_note(final_ml, "Biotin", "0.002 g/L", values["Biotin141"]),
        ),
        Component(
            "Folic acid",
            values["Folic"],
            "G_PER_L",
            ("CHEBI:27470", "folic acid"),
            SOURCE_141,
            _medium_141_note(final_ml, "Folic acid", "0.002 g/L", values["Folic"]),
        ),
        Component(
            "D(+)-Biotin",
            values["Biotin503"],
            "G_PER_L",
            ("CHEBI:15956", "biotin"),
            SOURCE_503,
            _medium_503_note(final_ml, "D(+)-Biotin", "0.020 g/L", values["Biotin503"]),
        ),
        Component(
            "Pyridoxine-HCl",
            values["Pyridoxine"],
            "G_PER_L",
            ("CHEBI:30961", "pyridoxine hydrochloride"),
            SOURCE_503,
            _combined_vitamin_note(
                final_ml,
                "Pyridoxine-HCl",
                values["Pyridoxine141"],
                values["Pyridoxine503"],
                values["Pyridoxine"],
            ),
        ),
        Component(
            "Thiamine-HCl x 2 H2O",
            values["Thiamine"],
            "G_PER_L",
            ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
            SOURCE_503,
            _combined_vitamin_note(
                final_ml,
                "Thiamine-HCl x 2 H2O",
                values["Thiamine141"],
                values["Thiamine503"],
                values["Thiamine"],
            ),
        ),
        Component(
            "Riboflavin",
            values["Riboflavin"],
            "G_PER_L",
            ("CHEBI:17015", "riboflavin"),
            SOURCE_141,
            _medium_141_note(final_ml, "Riboflavin", "0.005 g/L", values["Riboflavin"]),
        ),
        Component(
            "Nicotinic acid",
            values["Nicotinic"],
            "G_PER_L",
            ("CHEBI:15940", "nicotinic acid"),
            SOURCE_503,
            _combined_vitamin_note(
                final_ml,
                "Nicotinic acid",
                values["Nicotinic141"],
                values["Nicotinic503"],
                values["Nicotinic"],
            ),
        ),
        Component(
            "D-Ca-pantothenate",
            values["Pantothenate141"],
            "G_PER_L",
            ("CHEBI:31345", "Calcium pantothenate"),
            SOURCE_141,
            _medium_141_note(
                final_ml,
                "D-Ca-pantothenate",
                "0.005 g/L",
                values["Pantothenate141"],
            ),
        ),
        Component(
            "Calcium pantothenate",
            values["Pantothenate503"],
            "G_PER_L",
            ("CHEBI:31345", "Calcium pantothenate"),
            SOURCE_503,
            _medium_503_note(
                final_ml,
                "Calcium pantothenate",
                "0.100 g/L",
                values["Pantothenate503"],
            ),
        ),
        Component(
            "Vitamin B12",
            values["B12"],
            "G_PER_L",
            ("CHEBI:176843", "vitamin B12"),
            SOURCE_503,
            _combined_vitamin_note(
                final_ml,
                "Vitamin B12",
                values["B12141"],
                values["B12503"],
                values["B12"],
            ),
        ),
        Component(
            "p-Aminobenzoic acid",
            values["PABA"],
            "G_PER_L",
            ("CHEBI:30753", "4-aminobenzoic acid"),
            SOURCE_503,
            _combined_vitamin_note(
                final_ml,
                "p-Aminobenzoic acid",
                values["PABA141"],
                values["PABA503"],
                values["PABA"],
            ),
        ),
        Component(
            "Lipoic acid",
            values["Lipoic"],
            "G_PER_L",
            ("CHEBI:16494", "lipoic acid"),
            SOURCE_141,
            _medium_141_note(final_ml, "Lipoic acid", "0.005 g/L", values["Lipoic"]),
        ),
        Component(
            "Na2S x 9 H2O",
            values["Na2S"],
            "G_PER_L",
            ("CHEBI:76209", "sodium sulfide nonahydrate"),
            SOURCE_193,
            _base_note(final_ml, "Na2S x 9 H2O", "0.40 g", values["Na2S"]),
        ),
        Component(
            "NaOH",
            values["NaOH"],
            "G_PER_L",
            ("CHEBI:32145", "sodium hydroxide"),
            SOURCE_385,
            _selenite_tungstate_note(final_ml, "NaOH", "0.500 g/L", values["NaOH"]),
        ),
        Component(
            "Na2SeO3 x 5 H2O",
            values["Na2SeO3"],
            "G_PER_L",
            ("CHEBI:131361", "disodium selenite pentahydrate"),
            SOURCE_385,
            _selenite_tungstate_note(
                final_ml,
                "Na2SeO3 x 5 H2O",
                "0.003 g/L",
                values["Na2SeO3"],
            ),
        ),
        Component(
            "Na2WO4 x 2 H2O",
            values["Na2WO4"],
            "G_PER_L",
            ("CHEBI:63939", "sodium tungstate dihydrate"),
            SOURCE_385,
            _selenite_tungstate_note(
                final_ml,
                "Na2WO4 x 2 H2O",
                "0.004 g/L",
                values["Na2WO4"],
            ),
        ),
        Component(
            "CO2",
            "variable",
            "VARIABLE",
            ("CHEBI:16526", "carbon dioxide"),
            SOURCE_193,
            f"{SOURCE_193} prepares the medium under 80% N2 and 20% CO2.",
        ),
        Component(
            "N2",
            "variable",
            "VARIABLE",
            ("CHEBI:17997", "dinitrogen"),
            SOURCE_193,
            f"{SOURCE_193} prepares the medium under 80% N2 and 20% CO2.",
        ),
        Component(
            "Distilled water",
            "990.000",
            "ML_PER_L",
            ("CHEBI:15377", "water"),
            SOURCE_193,
            (
                f"{SOURCE_193} lists 990 mL direct distilled water across "
                f"solutions A, C, D, and F before {SOURCE_799} stock "
                "additions."
            ),
        ),
    )


V1008 = {
    "Na2SO4": "2.976190",
    "KH2PO4": "0.198413",
    "NH4Cl": "0.297619",
    "NaCl": "6.944444",
    "MgCl2": "1.289683",
    "KCl": "0.496032",
    "CaCl2": "0.148810",
    "Resazurin": "0.000992",
    "HCl": "0.002480",
    "FeCl2": "0.001488",
    "ZnCl2": "0.0000694",
    "MnCl2": "0.0000992",
    "H3BO3": "0.00000595",
    "CoCl2": "0.000188",
    "CuCl2": "0.00000198",
    "NiCl2": "0.0000238",
    "Na2MoO4": "0.0000357",
    "NaHCO3": "4.960317",
    "Biotin141": "0.0000198",
    "Folic": "0.0000198",
    "Biotin503": "0.0000198",
    "Pyridoxine141": "0.0000992",
    "Pyridoxine503": "0.000298",
    "Pyridoxine": "0.000397",
    "Thiamine141": "0.0000496",
    "Thiamine503": "0.000198",
    "Thiamine": "0.000248",
    "Riboflavin": "0.0000496",
    "Nicotinic141": "0.0000496",
    "Nicotinic503": "0.000198",
    "Nicotinic": "0.000248",
    "Pantothenate141": "0.0000496",
    "Pantothenate503": "0.0000992",
    "B12141": "0.000000992",
    "B12503": "0.0000992",
    "B12": "0.000100",
    "PABA141": "0.0000496",
    "PABA503": "0.0000794",
    "PABA": "0.000129",
    "Lipoic": "0.0000496",
    "Na2S": "0.396825",
    "NaOH": "0.000496",
    "Na2SeO3": "0.00000298",
    "Na2WO4": "0.00000397",
}

V1003 = {
    "Na2SO4": "2.991027",
    "KH2PO4": "0.199402",
    "NH4Cl": "0.299103",
    "NaCl": "6.979063",
    "MgCl2": "1.296112",
    "KCl": "0.498504",
    "CaCl2": "0.149551",
    "Resazurin": "0.000997",
    "HCl": "0.002493",
    "FeCl2": "0.001496",
    "ZnCl2": "0.0000698",
    "MnCl2": "0.0000997",
    "H3BO3": "0.00000598",
    "CoCl2": "0.000189",
    "CuCl2": "0.00000199",
    "NiCl2": "0.0000239",
    "Na2MoO4": "0.0000359",
    "NaHCO3": "4.985045",
    "Biotin141": "0.0000199",
    "Folic": "0.0000199",
    "Biotin503": "0.0000199",
    "Pyridoxine141": "0.0000997",
    "Pyridoxine503": "0.000299",
    "Pyridoxine": "0.000399",
    "Thiamine141": "0.0000499",
    "Thiamine503": "0.000199",
    "Thiamine": "0.000249",
    "Riboflavin": "0.0000499",
    "Nicotinic141": "0.0000499",
    "Nicotinic503": "0.000199",
    "Nicotinic": "0.000249",
    "Pantothenate141": "0.0000499",
    "Pantothenate503": "0.0000997",
    "B12141": "0.000000997",
    "B12503": "0.0000997",
    "B12": "0.000101",
    "PABA141": "0.0000499",
    "PABA503": "0.0000798",
    "PABA": "0.000130",
    "Lipoic": "0.0000499",
    "Na2S": "0.398804",
    "NaOH": "0.000499",
    "Na2SeO3": "0.00000299",
    "Na2WO4": "0.00000399",
}

MEDIUM_799_COMPONENTS: tuple[Component, ...] = _common_components(
    1008,
    V1008,
    (
        Component(
            "Na-pyruvate",
            "2.500000",
            "G_PER_L",
            ("CHEBI:50144", "sodium pyruvate"),
            SOURCE_799,
            f"{SOURCE_799} replaces acetate with 10 mL/L of 25% Na-pyruvate.",
        ),
        Component(
            "Yeast extract",
            "0.500000",
            "G_PER_L",
            ("FOODON:03315426", "yeast extract"),
            SOURCE_799,
            f"{SOURCE_799} adds 5 mL/L of a 10% yeast extract stock.",
        ),
    ),
)

MEDIUM_799_REPLACE_COMPONENTS: tuple[Component, ...] = _common_components(
    1003,
    V1003,
    (
        Component(
            "1,2,4-trihydroxybenzene",
            "2.000",
            "MILLIMOLAR",
            ("CHEBI:16971", "benzene-1,2,4-triol"),
            SOURCE_799,
            (
                f"{SOURCE_799} replaces acetate with 2 mM "
                "1,2,4-trihydroxybenzene."
            ),
        ),
        Component(
            "Yeast extract",
            "0.500000",
            "G_PER_L",
            ("FOODON:03315426", "yeast extract"),
            SOURCE_799,
            f"{SOURCE_799} adds 5 mL/L of a 10% yeast extract stock.",
        ),
    ),
)

TARGETS: tuple[Target, ...] = (
    Target(
        "bacterial/desulfovibrio_inopinatus_medium.yaml",
        "CultureMech:006511",
        "komodo.medium:799",
        NOTES_799,
        MEDIUM_799_COMPONENTS,
        (
            KOMODO_799_URL,
            DSMZ_799_URL,
            DSMZ_193_URL,
            DSMZ_320_URL,
            DSMZ_141_URL,
            DSMZ_385_URL,
            DSMZ_503_URL,
        ),
    ),
    Target(
        (
            "bacterial/desulfovibrio_inopinatus_medium_replace_na_pyruvate_"
            "with_1_2_4_trihydroxybenzene.yaml"
        ),
        "CultureMech:006510",
        "komodo.medium:799_replace_Na-pyruvate_with_1,2,4-trihydroxybenzene",
        NOTES_799_REPLACE,
        MEDIUM_799_REPLACE_COMPONENTS,
        (
            KOMODO_799_REPLACE_URL,
            DSMZ_799_URL,
            DSMZ_193_URL,
            DSMZ_320_URL,
            DSMZ_141_URL,
            DSMZ_385_URL,
            DSMZ_503_URL,
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


def _check_source(doc: dict[str, Any], target: Target) -> None:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{target.path}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != target.expected_media_term:
        raise ValueError(
            f"{target.path}: missing expected media term "
            f"{target.expected_media_term}"
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


def _ensure_flags(doc: dict[str, Any], target: Target) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError(f"{target.path}: data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    found = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.references:
        if url not in found:
            references.append({"reference": url})


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Replaced empty KOMODO 799 composition with archived DSMZ data",
        "source": DSMZ_799_URL,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected immutable id {target.expected_id}, "
            f"found {doc.get('id')!r}"
        )
    _check_source(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_range", {"min": 7.1, "max": 7.4}, "physical_state")
    repaired["ingredients"] = [_ingredient(component) for component in target.components]
    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired, target)
    _ensure_references(repaired, target)
    _ensure_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path), target)
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
