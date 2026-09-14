#!/usr/bin/env python3
"""Repair MediaDive/TOGO JCM 825 KOKO Medium records."""

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
JCM_J825_PATH = Path("bacterial/koko_medium.yaml")
TOGO_M860_PATH = Path("bacterial/TOGO_M860_KOKO_Medium.yaml")
SOLUTION_4784_PATH = Path("bacterial/mediadive_4784_Main_sol_J825.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m860_koko_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J825 = "https://mediadive.dsmz.de/medium/J825"
JCM_J825 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=825"
TOGO_M860 = "https://togomedium.org/medium/M860"
TOGO_M335 = "https://togomedium.org/medium/M335"
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
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()


J825_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Tryptone", "0.979432", "G_PER_L"),
    ("Peptone", "0.979432", "G_PER_L"),
    ("Yeast extract", "0.979432", "G_PER_L"),
    ("K2HPO4", "1.56709", "G_PER_L"),
    ("NaH2PO4 x 2 H2O", "0.979432", "G_PER_L"),
    ("NH4Cl", "0.489716", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.156709", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.0587659", "G_PER_L"),
    ("Resazurin", "0.000489716", "G_PER_L"),
    ("Glucose", "50", "G_PER_L"),
    ("NaHCO3", "1.25", "G_PER_L"),
    ("L-Cysteine HCl x H2O", "10", "G_PER_L"),
    ("Na2S x 9 H2O", "10", "G_PER_L"),
    ("EDTA", "0.5", "G_PER_L"),
    ("FeSO4 x 7 H2O", "0.2", "G_PER_L"),
    ("Biotin", "0.002", "G_PER_L"),
    ("Folic acid", "0.002", "G_PER_L"),
    ("Pyridoxine hydrochloride", "0.01", "G_PER_L"),
    ("Thiamine HCl", "0.005", "G_PER_L"),
    ("Riboflavin", "0.005", "G_PER_L"),
    ("Nicotinic acid", "0.005", "G_PER_L"),
    ("Calcium pantothenate", "0.005", "G_PER_L"),
    ("Vitamin B12", "0.0001", "G_PER_L"),
    ("p-Aminobenzoic acid", "0.005", "G_PER_L"),
    ("Lipoic acid", "0.005", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.03", "G_PER_L"),
    ("H3BO3", "0.3", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.2", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.01", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.02", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.03", "G_PER_L"),
)

M860_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "930", "G_PER_L"),
    ("MgSO4\u30fb7H2O", "0.16", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("CaCl2\u30fb2H2O", "0.06", "G_PER_L"),
    ("NH4Cl", "0.5", "G_PER_L"),
    ("K2HPO4", "1.6", "G_PER_L"),
    ("Resazurin", "0.5", "G_PER_L"),
    ("NaH2PO4\u30fb2H2O", "1", "G_PER_L"),
    ("Tryptone (BD-Difco)", "1", "G_PER_L"),
    ("Peptone", "1", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

M860_IMPORTED_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("SL--4 trace element solution (see Medium [M335])", "10", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
    ("8% NaHCO3 solution*", "1.25", "G_PER_L", ()),
    ("10% Glucose solution", "50", "G_PER_L", ()),
    ("3% Na2S\u30fb9H2O solution", "10", "G_PER_L", ()),
    ("3% L--Cysteine\u30fbHCl\u30fbH2O solution", "10", "G_PER_L", ()),
)

IMPORTED_SOLUTION_4784_COMPOSITION: tuple[Component, ...] = (
    ("Tryptone", "0.979432", "G_PER_L"),
    ("Peptone", "0.979432", "G_PER_L"),
    ("Yeast extract", "0.979432", "G_PER_L"),
    ("K2HPO4", "1.56709", "G_PER_L"),
    ("NaH2PO4 x 2 H2O", "0.979432", "G_PER_L"),
    ("NH4Cl", "0.489716", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.156709", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.0587659", "G_PER_L"),
    ("Resazurin", "0.000489716", "G_PER_L"),
    ("Distilled water", "910.871694417238", "PERCENT_V_V"),
    ("Glucose", "48.97159647404506", "PERCENT_V_V"),
    ("NaHCO3", "1.2242899118511263", "PERCENT_V_V"),
    ("L-Cysteine HCl x H2O", "9.79431929480901", "PERCENT_V_V"),
    ("Na2S x 9 H2O", "9.79431929480901", "PERCENT_V_V"),
)

PLACEHOLDER_INGREDIENTS: tuple[Component, ...] = (
    ("See source for composition", "variable", "VARIABLE"),
)

DIRECT_COMPOSITION: tuple[Component, ...] = (
    ("Distilled water", "930.0", "ML_PER_L"),
    ("MgSO4 x 7 H2O", "0.16", "G_PER_L"),
    ("Yeast extract", "1.0", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.06", "G_PER_L"),
    ("NH4Cl", "0.5", "G_PER_L"),
    ("K2HPO4", "1.6", "G_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("NaH2PO4 x 2 H2O", "1.0", "G_PER_L"),
    ("Tryptone (BD-Difco)", "1.0", "G_PER_L"),
    ("Peptone", "1.0", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

TRACE_SL4_COMPOSITION: tuple[Component, ...] = (
    ("EDTA", "0.5", "G_PER_L"),
    ("FeSO4 x 7 H2O", "0.2", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.01", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.003", "G_PER_L"),
    ("H3BO3", "0.03", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.02", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.001", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.002", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.003", "G_PER_L"),
    ("Distilled water", "900.0", "ML_PER_L"),
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
    ("Trace element solution SL-4", "10.0", "ML_PER_L", TRACE_SL4_COMPOSITION),
    ("Trace vitamins", "10.0", "ML_PER_L", TRACE_VITAMIN_COMPOSITION),
    ("8% NaHCO3 solution", "1.25", "ML_PER_L", (("NaHCO3", "80.0", "G_PER_L"),)),
    (
        "10% Glucose solution",
        "50.0",
        "ML_PER_L",
        (("Glucose", "100.0", "G_PER_L"),),
    ),
    (
        "3% Na2S x 9 H2O solution",
        "10.0",
        "ML_PER_L",
        (("Na2S x 9 H2O", "30.0", "G_PER_L"),),
    ),
    (
        "3% L-Cysteine HCl x H2O solution",
        "10.0",
        "ML_PER_L",
        (("L-Cysteine HCl x H2O", "30.0", "G_PER_L"),),
    ),
)

SOLUTION_4784_COMPOSITION: tuple[Component, ...] = (
    ("Tryptone (BD-Difco)", "1.0", "G_PER_L"),
    ("Peptone", "1.0", "G_PER_L"),
    ("Yeast extract", "1.0", "G_PER_L"),
    ("K2HPO4", "1.6", "G_PER_L"),
    ("NaH2PO4 x 2 H2O", "1.0", "G_PER_L"),
    ("NH4Cl", "0.5", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.16", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.06", "G_PER_L"),
    ("Trace element solution SL-4", "10.0", "ML_PER_L"),
    ("Trace vitamins", "10.0", "ML_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("Distilled water", "930.0", "ML_PER_L"),
    ("10% Glucose solution", "50.0", "ML_PER_L"),
    ("8% NaHCO3 solution", "1.25", "ML_PER_L"),
    ("3% L-Cysteine HCl x H2O solution", "10.0", "ML_PER_L"),
    ("3% Na2S x 9 H2O solution", "10.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "Yeast extract": ("FOODON:03315426", "Yeast extract"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "NaH2PO4 x 2 H2O": ("CHEBI:37585", "sodium dihydrogenphosphate"),
    "Tryptone (BD-Difco)": ("MICRO:0000182", "Tryptone"),
    "Peptone": ("MICRO:0000178", "Peptone"),
    "N2": ("CHEBI:17997", "dinitrogen"),
    "EDTA": ("CHEBI:4735", "ethylenediaminetetraacetic acid"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2 H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "NiCl2 x 6 H2O": ("CHEBI:53542", "nickel chloride hexahydrate"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
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
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Na2S x 9 H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "L-Cysteine HCl x H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Yeast extract": ("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
    "Tryptone (BD-Difco)": ("PROTEIN_SOURCE",),
    "Peptone": ("PROTEIN_SOURCE",),
    "NH4Cl": ("NITROGEN_SOURCE",),
    "K2HPO4": ("PHOSPHATE_SOURCE",),
    "NaH2PO4 x 2 H2O": ("PHOSPHATE_SOURCE",),
    "FeSO4 x 7 H2O": ("IRON_SOURCE",),
    "ZnSO4 x 7 H2O": ("TRACE_ELEMENT",),
    "MnCl2 x 4 H2O": ("TRACE_ELEMENT",),
    "H3BO3": ("TRACE_ELEMENT",),
    "CoCl2 x 6 H2O": ("TRACE_ELEMENT",),
    "CuCl2 x 2 H2O": ("TRACE_ELEMENT",),
    "NiCl2 x 6 H2O": ("TRACE_ELEMENT",),
    "Na2MoO4 x 2 H2O": ("TRACE_ELEMENT",),
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
    "Glucose": ("CARBON_SOURCE", "ENERGY_SOURCE"),
    "Na2S x 9 H2O": ("SULFUR_SOURCE",),
    "L-Cysteine HCl x H2O": ("AMINO_ACID_SOURCE", "SULFUR_SOURCE"),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "K2HPO4": ("BUFFER",),
    "NaH2PO4 x 2 H2O": ("BUFFER",),
    "Resazurin": ("REDOX_INDICATOR",),
    "EDTA": ("CHELATOR",),
    "NaHCO3": ("BUFFER",),
    "Na2S x 9 H2O": ("REDUCING_AGENT",),
    "L-Cysteine HCl x H2O": ("REDUCING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "VARIABLE": "variable concentration",
}

SOURCE_NOTE = (
    "JCM Medium 825 / KOKO Medium lists 930.0 ml/L distilled water, 0.16 "
    "g/L MgSO4 x 7 H2O, 1.0 g/L yeast extract, 0.06 g/L CaCl2 x 2 H2O, "
    "0.5 g/L NH4Cl, 1.6 g/L K2HPO4, 0.5 mg/L resazurin, 1.0 g/L "
    "NaH2PO4 x 2 H2O, 1.0 g/L BD-Difco tryptone, 1.0 g/L peptone, "
    "10.0 ml/L SL-4 trace element solution, 10.0 ml/L Trace vitamins, "
    "N2 gas, and sterile anaerobic 8% NaHCO3, 10% glucose, 3% Na2S x "
    "9 H2O, and 3% L-cysteine HCl x H2O stocks; MediaDive J825 reports "
    "the same recipe at pH 7.0."
)

PREPARATION_STEPS = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix the basal salts, yeast extract, BD-Difco tryptone, peptone, "
            "resazurin, 10.0 ml/L Trace element solution SL-4, 10.0 ml/L "
            "Trace vitamins, and 930.0 ml/L distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the medium to pH 7.0.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the medium under an N2 atmosphere.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "After autoclaving, add 1.25 ml/L sterile anaerobic 8% NaHCO3 "
            "solution, 50.0 ml/L 10% glucose solution, 10.0 ml/L 3% "
            "Na2S x 9 H2O solution, and 10.0 ml/L 3% L-cysteine HCl x H2O "
            "solution."
        ),
    },
)

M860_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M860_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010277",
    "name": "koko_medium",
    "notes": (
        "TOGO M860 imports the same JCM Medium 825 KOKO Medium formulation "
        "represented by MediaDive J825."
    ),
}

J825_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J825_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003169",
    "name": "koko_medium",
    "notes": M860_CHILD["notes"],
}

CULTUREMECH_SOLUTIONS: dict[str, tuple[str, str]] = {
    "Trace element solution SL-4": (
        "CultureMech:013111",
        "Trace element solution SL-4",
    ),
    "Trace vitamins": ("CultureMech:012935", "Trace vitamins"),
}

MEDIADIVE_SOLUTION_TERMS: dict[str, tuple[str, str]] = {
    "Trace element solution SL-4": (
        "mediadive.solution:4059",
        "Trace element solution SL-4",
    ),
    "Trace vitamins": ("mediadive.solution:3861", "Trace vitamins"),
}

STOCK_SOLUTION_TERMS: dict[str, tuple[str, str]] = {
    "8% NaHCO3 solution": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "10% Glucose solution": ("CHEBI:17234", "glucose"),
    "3% Na2S x 9 H2O solution": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "3% L-Cysteine HCl x H2O solution": (
        "CHEBI:91248",
        "L-cysteine hydrochloride hydrate",
    ),
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
    notes: str | None = None,
) -> dict[str, Any]:
    if notes is None and unit == "VARIABLE":
        notes = (
            f"{source} lists {preferred_term} as an atmosphere component with no "
            "fixed liquid-phase concentration."
        )

    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": _term(*GROUNDINGS[preferred_term]),
    }

    term_id, term_label = GROUNDINGS[preferred_term]
    if term_id.startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(term_id, term_label)

    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _composition(
    source: str,
    components: tuple[Component, ...],
) -> list[dict[str, Any]]:
    return [_component(name, value, unit, source=source) for name, value, unit in components]


def _sl4_composition(source: str) -> list[dict[str, Any]]:
    rows = _composition(source, TRACE_SL4_COMPOSITION)
    sl6_notes = {
        "ZnSO4 x 7 H2O": "0.1",
        "MnCl2 x 4 H2O": "0.03",
        "H3BO3": "0.3",
        "CoCl2 x 6 H2O": "0.2",
        "CuCl2 x 2 H2O": "0.01",
        "NiCl2 x 6 H2O": "0.02",
        "Na2MoO4 x 2 H2O": "0.03",
    }
    for row in rows:
        stock_value = sl6_notes.get(row["preferred_term"])
        if stock_value is None:
            continue
        row["notes"] = (
            f"{source} expands 100.0 ml/L Trace element solution SL-6 into "
            f"Trace element solution SL-4; {stock_value} g/L "
            f"{row['preferred_term']} in SL-6 contributes "
            f"{row['concentration']['value']} g/L in SL-4."
        )
    rows[-1]["notes"] = (
        f"{source} lists 900.0 ml/L direct distilled water before adding "
        "100.0 ml/L Trace element solution SL-6."
    )
    return rows


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
            "Trace element solution SL-4",
            "10.0",
            _sl4_composition(source),
            source=source,
            notes=(
                f"{source} adds 10.0 ml/L Trace element solution SL-4. "
                "The inline stock composition expands the SL-6 trace-element "
                "stock that SL-4 contains."
            ),
        ),
        _stock_solution(
            "Trace vitamins",
            "10.0",
            _composition(source, TRACE_VITAMIN_COMPOSITION),
            source=source,
            notes=f"{source} adds 10.0 ml/L Trace vitamins from JCM Medium 197.",
        ),
        _stock_solution(
            "8% NaHCO3 solution",
            "1.25",
            _composition(source, (("NaHCO3", "80.0", "G_PER_L"),)),
            source=source,
            notes=f"{source} adds 1.25 ml/L sterile anaerobic 8% NaHCO3 stock.",
        ),
        _stock_solution(
            "10% Glucose solution",
            "50.0",
            _composition(source, (("Glucose", "100.0", "G_PER_L"),)),
            source=source,
            notes=f"{source} adds 50.0 ml/L sterile anaerobic 10% glucose stock.",
        ),
        _stock_solution(
            "3% Na2S x 9 H2O solution",
            "10.0",
            _composition(source, (("Na2S x 9 H2O", "30.0", "G_PER_L"),)),
            source=source,
            notes=(f"{source} adds 10.0 ml/L sterile anaerobic 3% " "Na2S x 9 H2O stock."),
        ),
        _stock_solution(
            "3% L-Cysteine HCl x H2O solution",
            "10.0",
            _composition(source, (("L-Cysteine HCl x H2O", "30.0", "G_PER_L"),)),
            source=source,
            notes=(f"{source} adds 10.0 ml/L sterile anaerobic 3% " "L-cysteine HCl x H2O stock."),
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

    term = MEDIADIVE_SOLUTION_TERMS.get(preferred_term)
    if term:
        row["culturemech_term"] = _term(*CULTUREMECH_SOLUTIONS[preferred_term])

    return row


def _solution_4784_composition(source: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for name, value, unit in SOLUTION_4784_COMPOSITION:
        if unit == "ML_PER_L" and name not in GROUNDINGS:
            rows.append(_flat_solution_component(name, value, source=source))
        else:
            rows.append(_component(name, value, unit, source=source))
    return rows


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
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _solution_signature(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), f"{label}.composition"),
            )
        )
    return tuple(signature)


def _media_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _term_id(doc: dict[str, Any]) -> str:
    term = doc.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_medium_target(doc: dict[str, Any], target: MediumTarget) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')}")
    if _media_term_id(doc) != target.source_term:
        raise ValueError(f"{target.path}: expected media term {target.source_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (target.imported_ingredients, DIRECT_COMPOSITION):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    solution_signature = _solution_signature(doc.get("solutions"), "solutions")
    if solution_signature not in (target.imported_solutions, FINAL_SOLUTIONS):
        raise ValueError(f"{target.path}: solution signature drifted")


def _ensure_solution_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:013726":
        raise ValueError(
            f"{SOLUTION_4784_PATH}: expected CultureMech:013726, " f"found {doc.get('id')}"
        )
    if _term_id(doc) != "mediadive.solution:4784":
        raise ValueError(f"{SOLUTION_4784_PATH}: expected MediaDive solution 4784")

    composition_signature = _signature(doc.get("composition"), "composition")
    if composition_signature not in (
        IMPORTED_SOLUTION_4784_COMPOSITION,
        SOLUTION_4784_COMPOSITION,
    ):
        raise ValueError(f"{SOLUTION_4784_PATH}: composition signature drifted")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (PLACEHOLDER_INGREDIENTS, ()):
        raise ValueError(f"{SOLUTION_4784_PATH}: ingredient signature drifted")


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


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "chebi_term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _composition_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    components = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    components.extend(i for i in doc.get("composition") or [] if isinstance(i, dict))
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        nested = solution.get("composition") or []
        components.extend(i for i in nested if isinstance(i, dict))
    return components


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    components = _composition_components(doc)
    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)
    if any(not _grounded(component) for component in components):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    else:
        while "has_unmapped_ingredients" in flags:
            flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any], references: tuple[str, ...]) -> None:
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for reference in references:
        if reference not in existing:
            rows.append({"reference": reference})
            existing.add(reference)


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
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
        ):
            history[index] = event
            return
    history.append(event)


def repair_medium_record(
    doc: dict[str, Any],
    target: MediumTarget,
) -> dict[str, Any]:
    _ensure_medium_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    _put_after(repaired, "ph_range", {"min": 7.0, "max": 7.0}, "physical_state")
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "notes", SOURCE_NOTE, "media_term")
    repaired["ingredients"] = _composition(target.source_name, DIRECT_COMPOSITION)
    _put_after(repaired, "solutions", _solutions(target.source_name), "ingredients")
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "solutions",
    )

    if target.parent_media:
        _put_after(
            repaired,
            "parent_media",
            copy.deepcopy(target.parent_media),
            "references",
        )
        _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
        _put_after(
            repaired,
            "variant_modifications",
            [M860_CHILD["notes"]],
            "variant_relationship",
        )
    else:
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
        repaired.pop("variant_modifications", None)

    if target.variant_children:
        repaired["variant_children"] = [copy.deepcopy(child) for child in target.variant_children]
    else:
        repaired.pop("variant_children", None)

    _ensure_flags(repaired)
    _ensure_references(repaired, target.references)
    _append_event(
        repaired,
        action=target.action,
        references=target.references,
        notes=target.event_notes,
    )
    return repaired


def repair_solution_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_solution_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _solution_4784_composition(
        "MediaDive solution 4784 / JCM Medium 825",
    )
    repaired.pop("ingredients", None)
    repaired["preparation_notes"] = (
        "Mix components thoroughly and adjust pH to 7.0. Autoclave the medium "
        "under an N2 atmosphere. Add the glucose, NaHCO3, Na2S x 9 H2O, and "
        "L-cysteine HCl x H2O solutions from sterile anaerobic stocks."
    )
    _put_after(
        repaired,
        "notes",
        (
            "MediaDive solution 4784 represents the main solution for JCM "
            "Medium 825. Stock-solution additions are kept as asserted ml/L "
            "solution rows because this SolutionRecipe record cannot nest the "
            "source stock compositions inline."
        ),
        "preparation_notes",
    )

    _ensure_flags(repaired)
    _ensure_references(repaired, (MEDIADIVE_J825,))
    _append_event(
        repaired,
        action="RESOLVED_MEDIADIVE_4784_MAIN_SOL_J825",
        references=(MEDIADIVE_J825,),
        notes=(
            "Restored the MediaDive J825 source-level direct component and "
            "stock-solution additions, corrected water and stock additions from "
            "false percent-volume values to ml/L, corrected resazurin to 0.5 "
            "mg/L, and removed the placeholder top-level ingredient."
        ),
    )
    return repaired


TARGETS: tuple[MediumTarget, ...] = (
    MediumTarget(
        path=JCM_J825_PATH,
        record_id="CultureMech:003169",
        source_term="mediadive.medium:J825",
        source_name="MediaDive J825 / JCM Medium 825",
        imported_ingredients=J825_IMPORTED_INGREDIENTS,
        imported_solutions=(),
        action="RESOLVED_JCM_825_KOKO_MEDIUM",
        event_notes=(
            "Replaced the previously flattened stock constituents with the "
            "source-level KOKO Medium recipe, corrected the water and resazurin "
            "units, restored the SL-4, Trace vitamins, glucose, NaHCO3, Na2S, "
            "and L-cysteine stock additions, and linked the TOGO M860 source "
            "duplicate."
        ),
        references=(MEDIADIVE_J825, JCM_J825),
        variant_children=(M860_CHILD,),
    ),
    MediumTarget(
        path=TOGO_M860_PATH,
        record_id="CultureMech:010277",
        source_term="TOGO:M860",
        source_name="TOGO M860 / JCM Medium 825",
        imported_ingredients=M860_IMPORTED_INGREDIENTS,
        imported_solutions=M860_IMPORTED_SOLUTIONS,
        action="RESOLVED_TOGO_M860_KOKO_MEDIUM",
        event_notes=(
            "Corrected water from 930 g/L to 930.0 ml/L, corrected resazurin "
            "from 0.5 g/L to 0.5 mg/L, converted the empty stock-solution "
            "placeholders to ml/L stock additions with inline compositions, "
            "added pH 7.0 from MediaDive J825, and linked the MediaDive J825 "
            "source duplicate."
        ),
        references=(TOGO_M860, MEDIADIVE_J825, JCM_J825, TOGO_M335, TOGO_M190),
        parent_media=J825_PARENT,
    ),
)


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_medium_record(_load(path), target)

    solution_path = normalized / SOLUTION_4784_PATH
    plans[solution_path] = repair_solution_record(_load(solution_path))
    return plans


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write repaired records; by default only report planned changes",
    )
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed: list[Path] = []
    for path, doc in plans.items():
        rendered = dump_record(doc)
        old = path.read_text(encoding="utf-8")
        if old != rendered:
            changed.append(path)
            if args.apply:
                write_record(path, doc)

    action = "wrote" if args.apply else "would write"
    for path in changed:
        print(f"{action} {path.relative_to(REPO)}")
    print(f"{action} {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
