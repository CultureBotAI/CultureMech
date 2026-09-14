#!/usr/bin/env python3
"""Repair MediaDive/TOGO JCM 837 SYFAC Medium records."""

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
MEDIADIVE_J837_PATH = Path("bacterial/syfac_medium.yaml")
TOGO_M873_PATH = Path("bacterial/TOGO_M873_Syfac_Medium.yaml")
SOLUTION_4221_PATH = Path("bacterial/mediadive_4221_Wolfe_s_mineral_elixir.yaml")
SOLUTION_4801_PATH = Path("bacterial/mediadive_4801_Main_sol_J837.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m873_syfac_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J837 = "https://mediadive.dsmz.de/medium/J837"
JCM_J837 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=837"
TOGO_M873 = "https://togomedium.org/medium/M873"
TOGO_M471 = "https://togomedium.org/medium/M471"
TOGO_M190 = "https://togomedium.org/medium/M190"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class MediumTarget:
    path: Path
    record_id: str
    source_term: str
    source_name: str
    imported_ingredients: tuple[Component, ...]
    imported_solutions: tuple[SolutionSignature, ...]
    action: str
    event_notes: str
    source_label: str
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()


M873_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "925", "G_PER_L"),
    ("Resazurin", "0.5", "G_PER_L"),
    ("Sea salts (Sigma)", "35", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "1", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

M873_IMPORTED_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("Wolfe's mineral elixir (see Medium [M471])", "1", "G_PER_L", ()),
    ("8% NaHCO3 solution*", "25", "G_PER_L", ()),
    ("1 M Sodium acetate solution", "20", "G_PER_L", ()),
    ("1 M Sodium fumarate solution", "20", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
    ("5% Na2S\u30fb9H2O solution", "6", "G_PER_L", ()),
)

J837_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Sea Salt", "34.7567", "G_PER_L"),
    ("Yeast extract", "0.993049", "G_PER_L"),
    ("Resazurin", "0.000496524", "G_PER_L"),
    ("Sodium acetate", "20", "G_PER_L"),
    ("Sodium fumarate", "20", "G_PER_L"),
    ("Trace vitamins (see Medium No. 197)", "10", "G_PER_L"),
    ("NaHCO3", "25", "G_PER_L"),
    ("Na2S x 9 H2O", "6", "G_PER_L"),
    ("MgSO4 x 7 H2O", "30", "G_PER_L"),
    ("NaCl", "10", "G_PER_L"),
    ("CaCl2 x 2 H2O", "1", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.1", "G_PER_L"),
    ("AlK(SO4)2 x 12 H2O", "0.18", "G_PER_L"),
    ("H3BO3", "0.1", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.1", "G_PER_L"),
    ("(NH4)2Ni(SO4)2 x 6 H2O", "2.8", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.1", "G_PER_L"),
    ("Na2SeO4", "0.1", "G_PER_L"),
)

J837_IMPORTED_SOLUTIONS: tuple[SolutionSignature, ...] = (
    (
        "Wolfe's mineral elixir",
        "1",
        "ML_PER_L",
        (
            ("MnSO4 x n H2O", "5", "G_PER_L"),
            ("FeSO4 x 7 H2O", "1", "G_PER_L"),
            ("CoCl2 x 6 H2O", "1.8", "G_PER_L"),
            ("ZnSO4 x 7 H2O", "1.8", "G_PER_L"),
        ),
    ),
)

IMPORTED_SOLUTION_4801_COMPOSITION: tuple[Component, ...] = (
    ("Sea Salt", "34.7567", "G_PER_L"),
    ("Yeast extract", "0.993049", "G_PER_L"),
    ("Resazurin", "0.000496524", "G_PER_L"),
    ("Distilled water", "918.5700099304867", "PERCENT_V_V"),
    ("Sodium acetate", "19.8609731876862", "PERCENT_V_V"),
    ("Sodium fumarate", "19.8609731876862", "PERCENT_V_V"),
    ("Trace vitamins (see Medium No. 197)", "9.9304865938431", "PERCENT_V_V"),
    ("NaHCO3", "24.826216484607748", "PERCENT_V_V"),
    ("Na2S x 9 H2O", "5.958291956305859", "PERCENT_V_V"),
)

IMPORTED_SOLUTION_4221_COMPOSITION: tuple[Component, ...] = (
    ("MgSO4 x 7 H2O", "30", "G_PER_L"),
    ("MnSO4 x n H2O", "5", "G_PER_L"),
    ("NaCl", "10", "G_PER_L"),
    ("FeSO4 x 7 H2O", "1", "G_PER_L"),
    ("CoCl2 x 6 H2O", "1.8", "G_PER_L"),
    ("CaCl2 x 2 H2O", "1", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "1.8", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.1", "G_PER_L"),
    ("AlK(SO4)2 x 12 H2O", "0.18", "G_PER_L"),
    ("H3BO3", "0.1", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.1", "G_PER_L"),
    ("(NH4)2Ni(SO4)2 x 6 H2O", "2.8", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.1", "G_PER_L"),
    ("Na2SeO4", "0.1", "G_PER_L"),
    ("Distilled water", "1000", "PERCENT_V_V"),
)

PLACEHOLDER_INGREDIENTS: tuple[Component, ...] = (
    ("See source for composition", "variable", "VARIABLE"),
)

DIRECT_COMPOSITION: tuple[Component, ...] = (
    ("Distilled water", "925.0", "ML_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("Sea salts (Sigma)", "35.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "1.0", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

WOLFE_COMPOSITION: tuple[Component, ...] = (
    ("MgSO4 x 7 H2O", "30.0", "G_PER_L"),
    ("MnSO4 x n H2O", "5.0", "G_PER_L"),
    ("NaCl", "10.0", "G_PER_L"),
    ("FeSO4 x 7 H2O", "1.0", "G_PER_L"),
    ("CoCl2 x 6 H2O", "1.8", "G_PER_L"),
    ("CaCl2 x 2 H2O", "1.0", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "1.8", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.1", "G_PER_L"),
    ("AlK(SO4)2 x 12 H2O", "0.18", "G_PER_L"),
    ("H3BO3", "0.1", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.1", "G_PER_L"),
    ("(NH4)2Ni(SO4)2 x 6 H2O", "2.8", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.1", "G_PER_L"),
    ("Na2SeO4", "0.1", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

TRACE_VITAMIN_COMPOSITION: tuple[Component, ...] = (
    ("Biotin", "2.0", "MG_PER_L"),
    ("Folic acid", "2.0", "MG_PER_L"),
    ("Pyridoxine hydrochloride", "10.0", "MG_PER_L"),
    ("Thiamine HCl", "5.0", "MG_PER_L"),
    ("Riboflavin", "5.0", "MG_PER_L"),
    ("Nicotinic acid", "5.0", "MG_PER_L"),
    ("Calcium pantothenate", "5.0", "MG_PER_L"),
    ("Vitamin B12", "0.1", "MG_PER_L"),
    ("p-Aminobenzoic acid", "5.0", "MG_PER_L"),
    ("Lipoic acid", "5.0", "MG_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

FINAL_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("Wolfe's mineral elixir", "1.0", "ML_PER_L", WOLFE_COMPOSITION),
    ("8% NaHCO3 solution", "25.0", "ML_PER_L", (("NaHCO3", "80.0", "G_PER_L"),)),
    (
        "1 M Sodium acetate solution",
        "20.0",
        "ML_PER_L",
        (("Sodium acetate", "1.0", "MOLAR"),),
    ),
    (
        "1 M Sodium fumarate solution",
        "20.0",
        "ML_PER_L",
        (("Sodium fumarate", "1.0", "MOLAR"),),
    ),
    ("Trace vitamins", "10.0", "ML_PER_L", TRACE_VITAMIN_COMPOSITION),
    (
        "5% Na2S x 9 H2O solution",
        "6.0",
        "ML_PER_L",
        (("Na2S x 9 H2O", "50.0", "G_PER_L"),),
    ),
)

SOLUTION_4801_COMPOSITION: tuple[Component, ...] = (
    ("Sea salts (Sigma)", "35.0", "G_PER_L"),
    ("Wolfe's mineral elixir", "1.0", "ML_PER_L"),
    ("Yeast extract (BD-Difco)", "1.0", "G_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("Distilled water", "925.0", "ML_PER_L"),
    ("1 M Sodium acetate solution", "20.0", "ML_PER_L"),
    ("1 M Sodium fumarate solution", "20.0", "ML_PER_L"),
    ("Trace vitamins", "10.0", "ML_PER_L"),
    ("8% NaHCO3 solution", "25.0", "ML_PER_L"),
    ("5% Na2S x 9 H2O solution", "6.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "Yeast extract"),
    "N2": ("CHEBI:17997", "dinitrogen"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnSO4 x n H2O": ("CHEBI:86360", "manganese(II) sulfate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "AlK(SO4)2 x 12 H2O": (
        "CHEBI:86465",
        "potassium aluminium sulfate dodecahydrate",
    ),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "(NH4)2Ni(SO4)2 x 6 H2O": (
        "CHEBI:86149",
        "ammonium nickel sulfate hexahydrate",
    ),
    "Na2WO4 x 2 H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "Na2SeO4": ("CHEBI:77775", "sodium selenate"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "Sodium acetate": ("CHEBI:32954", "sodium acetate"),
    "Sodium fumarate": ("CHEBI:115156", "disodium fumarate"),
    "Na2S x 9 H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "Pyridoxine hydrochloride": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Yeast extract (BD-Difco)": ("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
    "FeSO4 x 7 H2O": ("IRON_SOURCE",),
    "MnSO4 x n H2O": ("TRACE_ELEMENT",),
    "CoCl2 x 6 H2O": ("TRACE_ELEMENT",),
    "ZnSO4 x 7 H2O": ("TRACE_ELEMENT",),
    "CuSO4 x 5 H2O": ("TRACE_ELEMENT",),
    "AlK(SO4)2 x 12 H2O": ("TRACE_ELEMENT",),
    "H3BO3": ("TRACE_ELEMENT",),
    "Na2MoO4 x 2 H2O": ("TRACE_ELEMENT",),
    "(NH4)2Ni(SO4)2 x 6 H2O": ("TRACE_ELEMENT",),
    "Na2WO4 x 2 H2O": ("TRACE_ELEMENT",),
    "Na2SeO4": ("TRACE_ELEMENT",),
    "Na2S x 9 H2O": ("SULFUR_SOURCE",),
    "Biotin": ("VITAMIN_SOURCE",),
    "Folic acid": ("VITAMIN_SOURCE",),
    "Pyridoxine hydrochloride": ("VITAMIN_SOURCE",),
    "Thiamine HCl": ("VITAMIN_SOURCE",),
    "Riboflavin": ("VITAMIN_SOURCE",),
    "Nicotinic acid": ("VITAMIN_SOURCE",),
    "Calcium pantothenate": ("VITAMIN_SOURCE",),
    "Vitamin B12": ("VITAMIN_SOURCE", "COFACTOR_PROVIDER"),
    "p-Aminobenzoic acid": ("VITAMIN_SOURCE",),
    "Lipoic acid": ("VITAMIN_SOURCE", "COFACTOR_PROVIDER"),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Resazurin": ("REDOX_INDICATOR",),
    "NaHCO3": ("BUFFER",),
    "Sodium acetate": ("BUFFER",),
    "Na2S x 9 H2O": ("REDUCING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
    "VARIABLE": "variable concentration",
}

STOCK_SOLUTION_TERMS: dict[str, tuple[str, str]] = {
    "8% NaHCO3 solution": GROUNDINGS["NaHCO3"],
    "1 M Sodium acetate solution": GROUNDINGS["Sodium acetate"],
    "1 M Sodium fumarate solution": GROUNDINGS["Sodium fumarate"],
    "5% Na2S x 9 H2O solution": GROUNDINGS["Na2S x 9 H2O"],
}

MEDIADIVE_SOLUTION_TERMS: dict[str, tuple[str, str]] = {
    "Wolfe's mineral elixir": (
        "mediadive.solution:4221",
        "Wolfe's mineral elixir",
    ),
}

CULTUREMECH_SOLUTIONS: dict[str, tuple[str, str]] = {
    "Wolfe's mineral elixir": (
        "CultureMech:013242",
        "Wolfe's mineral elixir",
    ),
    "Trace vitamins": ("CultureMech:012935", "Trace vitamins"),
}

SOURCE_NOTE = (
    "JCM Medium 837 / SYFAC Medium lists 925.0 ml/L distilled water, 0.5 "
    "mg/L resazurin, 35.0 g/L Sigma sea salts, 1.0 g/L BD-Difco yeast "
    "extract, 1.0 ml/L Wolfe's mineral elixir, N2 gas, and sterile "
    "anaerobic 8% NaHCO3, 1 M sodium acetate, 1 M sodium fumarate, Trace "
    "vitamins, and 5% Na2S x 9 H2O stock additions; MediaDive J837 reports "
    "the same JCM recipe."
)

PREPARATION_STEPS = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix distilled water, resazurin, Sigma sea salts, BD-Difco yeast "
            "extract, and 1.0 ml/L Wolfe's mineral elixir."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the medium under an N2 atmosphere.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "Aseptically and anaerobically add 25.0 ml/L sterile anaerobic "
            "8% NaHCO3 solution, 20.0 ml/L 1 M sodium acetate solution, "
            "20.0 ml/L 1 M sodium fumarate solution, and 10.0 ml/L Trace "
            "vitamins."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Distribute the medium under an N2-CO2 (4:1, v/v) gas stream, "
            "seal culture vessels with butyl rubber stoppers, then add 6.0 "
            "ml/L 5% Na2S x 9 H2O solution autoclaved and stored under N2."
        ),
    },
)

M873_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M873_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010291",
    "name": "syfac_medium",
    "notes": (
        "TOGO M873 imports the same JCM Medium 837 SYFAC Medium formulation "
        "represented by MediaDive J837."
    ),
}

J837_PARENT = {
    "path": f"data/normalized_yaml/{MEDIADIVE_J837_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003181",
    "name": "syfac_medium",
    "notes": M873_CHILD["notes"],
}


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.load(handle, Loader=YAML_LOADER)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not parse to a mapping")
    return data


def _term(curie: str, label: str) -> dict[str, str]:
    return {"id": curie, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
) -> dict[str, Any]:
    unit_label = UNIT_LABELS[unit]
    if unit == "VARIABLE":
        notes = f"{source} lists {preferred_term} as a gas with no fixed concentration."
    else:
        notes = f"{source} lists {value} {unit_label} {preferred_term}."
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }

    if preferred_term in GROUNDINGS:
        term = _term(*GROUNDINGS[preferred_term])
        row["term"] = term
        if term["id"].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = dict(term)

    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _composition(source: str, rows: tuple[Component, ...]) -> list[dict[str, Any]]:
    return [
        _component(name, value, unit, source=source)
        for name, value, unit in rows
    ]


def _stock_solution(
    preferred_term: str,
    value: str,
    composition: list[dict[str, Any]],
    *,
    source: str,
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": composition,
    }

    term = MEDIADIVE_SOLUTION_TERMS.get(preferred_term)
    if term:
        row["term"] = _term(*term)

    stock_term = STOCK_SOLUTION_TERMS.get(preferred_term)
    if stock_term:
        row["term"] = _term(*stock_term)

    culturemech_term = CULTUREMECH_SOLUTIONS.get(preferred_term)
    if culturemech_term:
        row["culturemech_term"] = _term(*culturemech_term)

    return row


def _solutions(source: str) -> list[dict[str, Any]]:
    return [
        _stock_solution(
            "Wolfe's mineral elixir",
            "1.0",
            _composition(source, WOLFE_COMPOSITION),
            source=source,
            notes=(
                f"{source} adds 1.0 ml/L Wolfe's mineral elixir from JCM "
                "Medium 470 / TOGO M471."
            ),
        ),
        _stock_solution(
            "8% NaHCO3 solution",
            "25.0",
            _composition(source, (("NaHCO3", "80.0", "G_PER_L"),)),
            source=source,
            notes=f"{source} adds 25.0 ml/L sterile anaerobic 8% NaHCO3 stock.",
        ),
        _stock_solution(
            "1 M Sodium acetate solution",
            "20.0",
            _composition(source, (("Sodium acetate", "1.0", "MOLAR"),)),
            source=source,
            notes=f"{source} adds 20.0 ml/L 1 M sodium acetate solution.",
        ),
        _stock_solution(
            "1 M Sodium fumarate solution",
            "20.0",
            _composition(source, (("Sodium fumarate", "1.0", "MOLAR"),)),
            source=source,
            notes=f"{source} adds 20.0 ml/L 1 M sodium fumarate solution.",
        ),
        _stock_solution(
            "Trace vitamins",
            "10.0",
            _composition(source, TRACE_VITAMIN_COMPOSITION),
            source=source,
            notes=f"{source} adds 10.0 ml/L Trace vitamins from JCM Medium 197.",
        ),
        _stock_solution(
            "5% Na2S x 9 H2O solution",
            "6.0",
            _composition(source, (("Na2S x 9 H2O", "50.0", "G_PER_L"),)),
            source=source,
            notes=f"{source} adds 6.0 ml/L 5% Na2S x 9 H2O solution.",
        ),
    ]


def _flat_solution_component(
    preferred_term: str,
    value: str,
    *,
    source: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": f"{source} lists {value} ml/L {preferred_term}.",
    }

    stock_term = STOCK_SOLUTION_TERMS.get(preferred_term)
    if stock_term:
        row["term"] = _term(*stock_term)

    culturemech_term = CULTUREMECH_SOLUTIONS.get(preferred_term)
    if culturemech_term:
        row["culturemech_term"] = _term(*culturemech_term)

    return row


def _solution_4801_composition(source: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for name, value, unit in SOLUTION_4801_COMPOSITION:
        if unit == "ML_PER_L" and (
            name in CULTUREMECH_SOLUTIONS or name in STOCK_SOLUTION_TERMS
        ):
            rows.append(_flat_solution_component(name, value, source=source))
        else:
            rows.append(_component(name, value, unit, source=source))
    return rows


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration") or {}
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _solution_signature(
    rows: Any,
    label: str,
) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError(f"{label} is not a list")

    signature: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration") or {}
        composition = row.get("composition") or row.get("ingredients") or []
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(composition, "solution composition"),
            )
        )
    return tuple(signature)


def _ensure_medium_target(doc: dict[str, Any], target: MediumTarget) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"expected {target.record_id}, found {doc.get('id')}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        target.imported_ingredients,
        DIRECT_COMPOSITION,
    ):
        raise ValueError(f"{target.path} ingredient signature drifted")
    if _solution_signature(doc.get("solutions"), "solutions") not in (
        target.imported_solutions,
        FINAL_SOLUTIONS,
    ):
        raise ValueError(f"{target.path} solution signature drifted")


def _ensure_solution_target(
    doc: dict[str, Any],
    *,
    record_id: str,
    expected: tuple[Component, ...],
    final: tuple[Component, ...],
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"expected {record_id}, found {doc.get('id')}")
    if _signature(doc.get("composition"), "composition") not in (expected, final):
        raise ValueError(f"{doc.get('id')} composition signature drifted")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        PLACEHOLDER_INGREDIENTS,
        (),
    ):
        raise ValueError(f"{doc.get('id')} placeholder ingredients drifted")


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    doc[key] = value
    items = list(doc.items())
    without = [(k, v) for k, v in items if k != key]

    rebuilt: dict[str, Any] = {}
    inserted = False
    for item_key, item_value in without:
        rebuilt[item_key] = item_value
        if item_key == after:
            rebuilt[key] = value
            inserted = True
    if not inserted:
        rebuilt[key] = value

    doc.clear()
    doc.update(rebuilt)


def _ensure_flags(doc: dict[str, Any], *, has_unmapped: bool) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for flag in (
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
    ):
        while flag in flags:
            flags.remove(flag)

    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)

    if has_unmapped and "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")
    if not has_unmapped:
        while "has_unmapped_ingredients" in flags:
            flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any], references: tuple[str, ...]) -> None:
    doc["references"] = [{"reference": reference} for reference in references]


def _append_event(
    doc: dict[str, Any],
    *,
    action: str,
    references: tuple[str, ...],
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(references),
        "notes": notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")

    for existing in history:
        if not isinstance(existing, dict):
            continue
        if existing.get("curator") == CURATOR and existing.get("action") == action:
            existing.update(event)
            return
    history.append(event)


def repair_medium_record(doc: dict[str, Any], target: MediumTarget) -> dict[str, Any]:
    _ensure_medium_target(doc, target)

    repaired = copy.deepcopy(doc)
    source = target.source_label
    repaired["ingredients"] = _composition(source, DIRECT_COMPOSITION)
    repaired["solutions"] = _solutions(source)
    repaired["notes"] = SOURCE_NOTE
    repaired["preparation_steps"] = list(copy.deepcopy(PREPARATION_STEPS))
    repaired.pop("ph_value", None)

    if target.parent_media is None:
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
        repaired.pop("variant_modifications", None)
    else:
        repaired["parent_media"] = copy.deepcopy(target.parent_media)
        repaired["variant_relationship"] = target.parent_media["relationship"]
        repaired["variant_modifications"] = [target.parent_media["notes"]]

    if target.variant_children:
        repaired["variant_children"] = list(copy.deepcopy(target.variant_children))
    else:
        repaired.pop("variant_children", None)

    _ensure_flags(repaired, has_unmapped=True)
    _ensure_references(repaired, target.references)
    _append_event(
        repaired,
        action=target.action,
        references=target.references,
        notes=target.event_notes,
    )
    return repaired


def repair_solution_4801_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_solution_target(
        doc,
        record_id="CultureMech:013742",
        expected=IMPORTED_SOLUTION_4801_COMPOSITION,
        final=SOLUTION_4801_COMPOSITION,
    )

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _solution_4801_composition(
        "MediaDive solution 4801 / JCM Medium 837",
    )
    repaired.pop("ingredients", None)
    repaired["preparation_notes"] = (
        "Mix components thoroughly and autoclave under an N2 atmosphere. Add "
        "the sodium acetate, sodium fumarate, Trace vitamins, NaHCO3, and "
        "Na2S x 9 H2O solutions from sterile anaerobic stocks."
    )
    _put_after(
        repaired,
        "notes",
        (
            "MediaDive solution 4801 represents the main solution for JCM "
            "Medium 837. Stock-solution additions are kept as asserted ml/L "
            "solution rows because this SolutionRecipe record cannot nest the "
            "source stock compositions inline."
        ),
        "preparation_notes",
    )

    _ensure_flags(repaired, has_unmapped=True)
    _ensure_references(repaired, (MEDIADIVE_J837,))
    _append_event(
        repaired,
        action="RESOLVED_MEDIADIVE_4801_MAIN_SOL_J837",
        references=(MEDIADIVE_J837,),
        notes=(
            "Restored the MediaDive J837 source-level direct component and "
            "stock-solution additions, corrected water and stock additions "
            "from false percent-volume values to ml/L, corrected resazurin "
            "to 0.5 mg/L, and removed the placeholder top-level ingredient."
        ),
    )
    return repaired


def repair_solution_4221_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_solution_target(
        doc,
        record_id="CultureMech:013242",
        expected=IMPORTED_SOLUTION_4221_COMPOSITION,
        final=WOLFE_COMPOSITION,
    )

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _composition(
        "MediaDive solution 4221 / JCM Medium 470",
        WOLFE_COMPOSITION,
    )
    repaired.pop("ingredients", None)
    repaired["preparation_notes"] = (
        "Adjust the Wolfe's mineral elixir stock to pH 1.0 with diluted "
        "H2SO4, then dissolve the salts."
    )
    _put_after(
        repaired,
        "notes",
        (
            "MediaDive solution 4221 is the Wolfe's mineral elixir stock used "
            "by JCM Medium 837 / SYFAC Medium at 1.0 ml/L."
        ),
        "preparation_notes",
    )

    _ensure_flags(repaired, has_unmapped=False)
    _ensure_references(repaired, (MEDIADIVE_J837, TOGO_M471))
    _append_event(
        repaired,
        action="RESOLVED_MEDIADIVE_4221_WOLFES_MINERAL_ELIXIR",
        references=(MEDIADIVE_J837, TOGO_M471),
        notes=(
            "Corrected the Wolfe's mineral elixir water row from a false "
            "percent-volume value to 1000.0 ml/L and replaced upstream "
            "mediadive.compound groundings with direct ontology mappings."
        ),
    )
    return repaired


TARGETS: tuple[MediumTarget, ...] = (
    MediumTarget(
        path=MEDIADIVE_J837_PATH,
        record_id="CultureMech:003181",
        source_term="mediadive.medium:J837",
        source_name="JCM Medium J837",
        imported_ingredients=J837_IMPORTED_INGREDIENTS,
        imported_solutions=J837_IMPORTED_SOLUTIONS,
        action="RESOLVED_MEDIADIVE_J837_SYFAC_MEDIUM",
        event_notes=(
            "Restored the JCM Medium 837 source-level composition, moved "
            "stock additions from false g/L direct ingredient rows to ml/L "
            "solutions, added inline Wolfe's mineral elixir and Trace "
            "vitamin compositions, and linked the TOGO M873 source duplicate."
        ),
        source_label="MediaDive J837 / JCM Medium 837",
        references=(MEDIADIVE_J837, JCM_J837, TOGO_M873, TOGO_M471, TOGO_M190),
        variant_children=(M873_CHILD,),
    ),
    MediumTarget(
        path=TOGO_M873_PATH,
        record_id="CultureMech:010291",
        source_term="TOGO:M873",
        source_name="TOGO Medium M873",
        imported_ingredients=M873_IMPORTED_INGREDIENTS,
        imported_solutions=M873_IMPORTED_SOLUTIONS,
        action="RESOLVED_TOGO_M873_SYFAC_MEDIUM",
        event_notes=(
            "Corrected water from 925 g/L to 925.0 ml/L, corrected "
            "resazurin from 0.5 g/L to 0.5 mg/L, converted the empty "
            "stock-solution placeholders to ml/L stock additions with "
            "inline compositions, and linked the MediaDive J837 source "
            "duplicate."
        ),
        source_label="TOGO M873 / JCM Medium 837",
        references=(TOGO_M873, MEDIADIVE_J837, JCM_J837, TOGO_M471, TOGO_M190),
        parent_media=J837_PARENT,
    ),
)

SOLUTION_TARGETS = {
    SOLUTION_4221_PATH: repair_solution_4221_record,
    SOLUTION_4801_PATH: repair_solution_4801_record,
}


def build_repairs() -> dict[Path, dict[str, Any]]:
    repairs: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = NORMALIZED / target.path
        repairs[path] = repair_medium_record(_load(path), target)

    for rel_path, repair in SOLUTION_TARGETS.items():
        path = NORMALIZED / rel_path
        repairs[path] = repair(_load(path))

    return repairs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write repairs. Without this flag, only report changed files.",
    )
    args = parser.parse_args(argv)

    changed = 0
    for path, doc in build_repairs().items():
        before = path.read_text(encoding="utf-8")
        after = dump_record(doc)
        if before == after:
            continue
        changed += 1
        if args.apply:
            write_record(path, doc)
            print(f"wrote {path.relative_to(REPO)}")
        else:
            print(f"would write {path.relative_to(REPO)}")

    print(f"{'wrote' if args.apply else 'would write'} {changed} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
