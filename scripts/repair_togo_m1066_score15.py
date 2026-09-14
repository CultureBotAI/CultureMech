#!/usr/bin/env python3
"""Repair TOGO M1066 Clostridium Swellfunianum Medium."""

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

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = Path("bacterial/TOGO_M1066_Clostridium_Swellfunianum_Medium.yaml")
EXPECTED_ID = "CultureMech:007583"
EXPECTED_MEDIA_TERM = "TOGO:M1066"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1066_score15.py"
ACTION = "RESOLVED_TOGO_M1066_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1066 = "https://togomedium.org/medium/M1066"
TOGO_M433 = "https://togomedium.org/medium/M433"
TOGO_M190 = "https://togomedium.org/medium/M190"
JCM_1009 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1009"
JCM_433 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"

SOURCE = "TOGO M1066 / JCM Medium 1009"
TRACE_SOURCE = "TOGO M433 / JCM Medium 433"
VITAMIN_SOURCE = "TOGO M190 / JCM Medium 197"
TITLE = "Clostridium Swellfunianum Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Sol. 1", "5", "G_PER_L"),
    ("Sol. 2", "0.2", "G_PER_L"),
    ("Distilled water", "1", "G_PER_L"),
    ("KH2PO4", "0.33", "G_PER_L"),
    ("NH4Cl", "0.33", "G_PER_L"),
    ("KCl", "0.33", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.5", "G_PER_L"),
    ("Tryptone (BD-Difco)", "3", "G_PER_L"),
    ("L--Cysteine\u30fbHCl\u30fbH2O", "0.5", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

SOLUTION_1_SIGNATURE: tuple[Component, ...] = (
    ("NH4Cl", "0.33", "G_PER_L"),
    ("KCl", "0.33", "G_PER_L"),
    ("KH2PO4", "0.33", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.5", "G_PER_L"),
    ("Tryptone (BD-Difco)", "3.0", "G_PER_L"),
    ("Trace element solution SL-10", "1.0", "ML_PER_L"),
    ("Trace vitamins", "10.0", "ML_PER_L"),
    ("1% CaCl2 x 2H2O solution", "33.0", "ML_PER_L"),
    ("2% MgCl2 x 6H2O solution", "16.5", "ML_PER_L"),
    ("L-Cysteine HCl H2O", "0.5", "G_PER_L"),
    ("1% Resazurin solution", "1.0", "ML_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("N2", "variable", "VARIABLE"),
    ("CO2", "variable", "VARIABLE"),
)

SOLUTION_2_SIGNATURE: tuple[Component, ...] = (
    ("3% (w/v) Na2S x 9H2O solution", "variable", "VARIABLE"),
    ("10% (w/v) NaHCO3 solution", "variable", "VARIABLE"),
    ("20% (w/v) Glucose solution", "variable", "VARIABLE"),
)

CACL2_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("CaCl2 x 2H2O", "10.0", "G_PER_L"),
)
MGCL2_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("MgCl2 x 6H2O", "20.0", "G_PER_L"),
)
RESAZURIN_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Resazurin", "10.0", "G_PER_L"),
)
NAHCO3_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("NaHCO3", "100.0", "G_PER_L"),
)
GLUCOSE_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Glucose", "200.0", "G_PER_L"),
)
NA2S_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Na2S x 9H2O", "30.0", "G_PER_L"),
)

TRACE_ELEMENT_SIGNATURE: tuple[Component, ...] = (
    ("HCl (25%, 7.7 M)", "10.0", "ML_PER_L"),
    ("FeCl2 x 4H2O", "1.5", "G_PER_L"),
    ("ZnCl2", "70.0", "MG_PER_L"),
    ("MnCl2 x 4H2O", "100.0", "MG_PER_L"),
    ("H3BO3", "6.0", "MG_PER_L"),
    ("CoCl2 x 6H2O", "190.0", "MG_PER_L"),
    ("CuCl2 x 2H2O", "2.0", "MG_PER_L"),
    ("NiCl2 x 6H2O", "24.0", "MG_PER_L"),
    ("Na2MoO4 x 2H2O", "36.0", "MG_PER_L"),
    ("Distilled water", "990.0", "ML_PER_L"),
)

TRACE_VITAMINS_SIGNATURE: tuple[Component, ...] = (
    ("Biotin", "2.0", "MG_PER_L"),
    ("Folic acid", "2.0", "MG_PER_L"),
    ("Pyridoxine HCl", "10.0", "MG_PER_L"),
    ("Thiamine HCl", "5.0", "MG_PER_L"),
    ("Riboflavin", "5.0", "MG_PER_L"),
    ("Nicotinic acid", "5.0", "MG_PER_L"),
    ("Calcium pantothenate", "5.0", "MG_PER_L"),
    ("Vitamin B12", "0.1", "MG_PER_L"),
    ("p-Aminobenzoic acid", "5.0", "MG_PER_L"),
    ("Lipoic acid", "5.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("1% CaCl2\u30fb2H2O solution", "33", "G_PER_L", ()),
    ("2% MgCl2\u30fb6H2O solution", "16.5", "G_PER_L", ()),
    ("1% Resazurin solution", "1", "G_PER_L", ()),
    ("Trace element solution SL--10 (see Medium [M433])", "1", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
    ("10% (w/v) NaHCO3 solution*", "0.05", "G_PER_L", ()),
    ("20% (w/v) Glucose solution", "0.1", "G_PER_L", ()),
    ("3% (w/v) Na2S\u30fb9H2O solution", "0.05", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Sol. 1", "5.0", "ML_PER_L", SOLUTION_1_SIGNATURE),
    ("Sol. 2", "0.2", "ML_PER_L", SOLUTION_2_SIGNATURE),
    ("1% CaCl2 x 2H2O solution", "33.0", "ML_PER_L", CACL2_STOCK_SIGNATURE),
    ("2% MgCl2 x 6H2O solution", "16.5", "ML_PER_L", MGCL2_STOCK_SIGNATURE),
    ("1% Resazurin solution", "1.0", "ML_PER_L", RESAZURIN_STOCK_SIGNATURE),
    ("Trace element solution SL-10", "1.0", "ML_PER_L", TRACE_ELEMENT_SIGNATURE),
    ("Trace vitamins", "10.0", "ML_PER_L", TRACE_VITAMINS_SIGNATURE),
    ("10% (w/v) NaHCO3 solution", "variable", "VARIABLE", NAHCO3_STOCK_SIGNATURE),
    ("20% (w/v) Glucose solution", "variable", "VARIABLE", GLUCOSE_STOCK_SIGNATURE),
    ("3% (w/v) Na2S x 9H2O solution", "variable", "VARIABLE", NA2S_STOCK_SIGNATURE),
)

REFERENCES = (TOGO_M1066, JCM_1009, TOGO_M433, JCM_433, TOGO_M190, JCM_197)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "CO2": ("CHEBI:16526", "carbon dioxide"),
    "CoCl2 x 6H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl2 x 4H2O": ("CHEBI:86249", "iron dichloride tetrahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "HCl (25%, 7.7 M)": ("CHEBI:17883", "hydrogen chloride"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "L-Cysteine HCl H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "MgCl2 x 6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MnCl2 x 4H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "N2": ("CHEBI:17997", "dinitrogen"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "NiCl2 x 6H2O": ("CHEBI:53542", "nickel chloride hexahydrate"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    term: tuple[str, str] | None | bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }

    grounding: tuple[str, str] | None
    if term is True:
        grounding = GROUNDINGS.get(preferred_term)
    elif term is False:
        grounding = None
    else:
        grounding = term

    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)

    return row


def _listed_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    term: tuple[str, str] | None | bool = True,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        term=term,
    )


def _stock_reference(preferred_term: str, value: str, *, source: str) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        "ML_PER_L",
        source=source,
        notes=f"{source} adds {value} ml/L {preferred_term}.",
        term=False,
    )


def _post_autoclave_reference(
    preferred_term: str,
    amount: str,
    *,
    source: str,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        "variable",
        "VARIABLE",
        source=source,
        notes=(
            f"{source} adds {amount} {preferred_term} per 5.0 ml medium "
            "after autoclaving."
        ),
        term=False,
    )


def _percent_stock(
    preferred_term: str,
    *,
    solute: str,
    stock_value: str,
    concentration: dict[str, str],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": concentration,
        "source": SOURCE,
        "notes": (
            f"{SOURCE} references {preferred_term}; the listed percentage "
            f"stock is represented as {stock_value} g/L {solute}."
        ),
        "composition": [
            _component(
                solute,
                stock_value,
                "G_PER_L",
                source=SOURCE,
                notes=(
                    f"{SOURCE} lists {preferred_term}, equivalent to "
                    f"{stock_value} g/L {solute}."
                ),
            )
        ],
    }


def _trace_element_solution() -> dict[str, Any]:
    return {
        "preferred_term": "Trace element solution SL-10",
        "concentration": {"value": "1.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds 1.0 ml/L Trace element solution SL-10 from M433.",
        "composition": [
            _listed_component("HCl (25%, 7.7 M)", "10.0", "ML_PER_L", source=TRACE_SOURCE),
            _listed_component("FeCl2 x 4H2O", "1.5", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("ZnCl2", "70.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("MnCl2 x 4H2O", "100.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("H3BO3", "6.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("CoCl2 x 6H2O", "190.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("CuCl2 x 2H2O", "2.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("NiCl2 x 6H2O", "24.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("Na2MoO4 x 2H2O", "36.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("Distilled water", "990.0", "ML_PER_L", source=TRACE_SOURCE),
        ],
        "preparation_notes": (
            "Dissolve FeCl2 x 4H2O first in HCl, then dilute in distilled "
            "water and add the remaining salts."
        ),
    }


def _trace_vitamins() -> dict[str, Any]:
    return {
        "preferred_term": "Trace vitamins",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds 10.0 ml/L Trace vitamins from M190.",
        "composition": [
            _listed_component("Biotin", "2.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Folic acid", "2.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Pyridoxine HCl", "10.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Thiamine HCl", "5.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Riboflavin", "5.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component(
                "Nicotinic acid",
                "5.0",
                "MG_PER_L",
                source=VITAMIN_SOURCE,
            ),
            _listed_component(
                "Calcium pantothenate",
                "5.0",
                "MG_PER_L",
                source=VITAMIN_SOURCE,
            ),
            _listed_component("Vitamin B12", "0.1", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component(
                "p-Aminobenzoic acid",
                "5.0",
                "MG_PER_L",
                source=VITAMIN_SOURCE,
            ),
            _listed_component("Lipoic acid", "5.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Distilled water", "1.0", "L", source=VITAMIN_SOURCE),
        ],
    }


SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Sol. 1",
        "concentration": {"value": "5.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            f"{SOURCE} prepares the base anaerobic medium and dispenses "
            "5.0 ml portions before autoclaving."
        ),
        "composition": [
            _listed_component("NH4Cl", "0.33", "G_PER_L", source=SOURCE),
            _listed_component("KCl", "0.33", "G_PER_L", source=SOURCE),
            _listed_component("KH2PO4", "0.33", "G_PER_L", source=SOURCE),
            _listed_component(
                "Yeast extract (BD-Difco)",
                "0.5",
                "G_PER_L",
                source=SOURCE,
                term=False,
            ),
            _listed_component(
                "Tryptone (BD-Difco)",
                "3.0",
                "G_PER_L",
                source=SOURCE,
                term=False,
            ),
            _stock_reference("Trace element solution SL-10", "1.0", source=SOURCE),
            _stock_reference("Trace vitamins", "10.0", source=SOURCE),
            _stock_reference("1% CaCl2 x 2H2O solution", "33.0", source=SOURCE),
            _stock_reference("2% MgCl2 x 6H2O solution", "16.5", source=SOURCE),
            _listed_component("L-Cysteine HCl H2O", "0.5", "G_PER_L", source=SOURCE),
            _stock_reference("1% Resazurin solution", "1.0", source=SOURCE),
            _listed_component("Distilled water", "1.0", "L", source=SOURCE),
            _component(
                "N2",
                "variable",
                "VARIABLE",
                source=SOURCE,
                notes=f"{SOURCE} prepares the medium under an N2-CO2 gas mixture.",
            ),
            _component(
                "CO2",
                "variable",
                "VARIABLE",
                source=SOURCE,
                notes=(
                    f"{SOURCE} prepares the medium under an N2-CO2 (4:1, v/v) "
                    "gas mixture."
                ),
            ),
        ],
    },
    {
        "preferred_term": "Sol. 2",
        "concentration": {"value": "0.2", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            f"{SOURCE} adds 0.2 ml anaerobic stock solutions per 5.0 ml "
            "medium after autoclaving."
        ),
        "composition": [
            _post_autoclave_reference(
                "3% (w/v) Na2S x 9H2O solution",
                "0.05 ml",
                source=SOURCE,
            ),
            _post_autoclave_reference(
                "10% (w/v) NaHCO3 solution",
                "0.05 ml",
                source=SOURCE,
            ),
            _post_autoclave_reference(
                "20% (w/v) Glucose solution",
                "0.1 ml",
                source=SOURCE,
            ),
        ],
        "preparation_notes": (
            "Autoclave or filter-sterilize the anaerobic stocks under an N2 "
            "atmosphere, then add them after autoclaving the base medium."
        ),
    },
    _percent_stock(
        "1% CaCl2 x 2H2O solution",
        solute="CaCl2 x 2H2O",
        stock_value="10.0",
        concentration={"value": "33.0", "unit": "ML_PER_L"},
    ),
    _percent_stock(
        "2% MgCl2 x 6H2O solution",
        solute="MgCl2 x 6H2O",
        stock_value="20.0",
        concentration={"value": "16.5", "unit": "ML_PER_L"},
    ),
    _percent_stock(
        "1% Resazurin solution",
        solute="Resazurin",
        stock_value="10.0",
        concentration={"value": "1.0", "unit": "ML_PER_L"},
    ),
    _trace_element_solution(),
    _trace_vitamins(),
    _percent_stock(
        "10% (w/v) NaHCO3 solution",
        solute="NaHCO3",
        stock_value="100.0",
        concentration={"value": "variable", "unit": "VARIABLE"},
    ),
    _percent_stock(
        "20% (w/v) Glucose solution",
        solute="Glucose",
        stock_value="200.0",
        concentration={"value": "variable", "unit": "VARIABLE"},
    ),
    _percent_stock(
        "3% (w/v) Na2S x 9H2O solution",
        solute="Na2S x 9H2O",
        stock_value="30.0",
        concentration={"value": "variable", "unit": "VARIABLE"},
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare Sol. 1 with salts, yeast extract, tryptone, cysteine, "
            "Trace element solution SL-10, Trace vitamins, CaCl2, MgCl2, "
            "and Resazurin stocks, and distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the base medium to pH 7.3.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": (
            "Prepare the medium anaerobically under N2-CO2 (4:1, v/v), "
            "distribute 5.0 ml aliquots under the same gas mixture, seal, "
            "and autoclave."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "After autoclaving, add 0.05 ml 3% Na2S x 9H2O, 0.05 ml "
            "filter-sterilized 10% NaHCO3, and 0.1 ml 20% Glucose anaerobic "
            "stocks per 5.0 ml medium."
        ),
    },
)

NOTES = (
    "TOGO M1066 records JCM Medium 1009 with 5.0 ml Sol. 1 dispensed "
    "anaerobically under N2-CO2 (4:1, v/v), sealed and autoclaved, then "
    "supplemented after autoclaving with 0.2 ml Sol. 2 anaerobic stocks per "
    "5.0 ml medium. Sol. 1 contains CaCl2, MgCl2, Resazurin, Trace element "
    "solution SL-10 from M433/JCM 433, Trace vitamins from M190/JCM 197, "
    "NH4Cl, KCl, KH2PO4, yeast extract, Tryptone, L-Cysteine HCl H2O, "
    "distilled water, and N2/CO2 gas; Sol. 2 supplies NaHCO3, Glucose, and "
    "Na2S x 9H2O stocks."
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


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError("solution row lacks concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(solution.get("composition"), "solution composition"),
            )
        )
    return tuple(signatures)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (IMPORTED_INGREDIENT_SIGNATURE, ()):
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": NOTES,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
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
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.3, "physical_state")
    repaired.pop("ph_range", None)
    repaired["ingredients"] = []
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    _put_after(repaired, "sterilization", {"method": "AUTOCLAVE"}, "preparation_steps")
    _put_after(repaired, "notes", NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
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
    for path, doc in plans.items():
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
