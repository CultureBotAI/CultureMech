#!/usr/bin/env python3
"""Repair TOGO M1200/M1202/M1203/M1204 artificial freshwater medium records."""

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

CURATOR = "repair_togo_m1200_m1204_score15.py"
ACTION = "RESOLVED_TOGO_M1200_M1204_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M180 = "https://togomedium.org/medium/M180"
TOGO_M401 = "https://togomedium.org/medium/M401"
TOGO_M431 = "https://togomedium.org/medium/M431"
JCM_187 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187"
JCM_403 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403"
JCM_431 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431"
JCM_1122 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1122"
JCM_1124 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124"
JCM_1125 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1125"
MEDIADIVE_J1122 = "https://mediadive.dsmz.de/rest/medium/J1122"
MEDIADIVE_J1124 = "https://mediadive.dsmz.de/rest/medium/J1124"
MEDIADIVE_J1125 = "https://mediadive.dsmz.de/rest/medium/J1125"

JCM_187_SOURCE = "JCM Medium 187"
JCM_403_SOURCE = "JCM Medium 403"
JCM_431_SOURCE = "JCM Medium 431"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term: str
    togo_url: str
    jcm_url: str
    mediadive_url: str
    jcm_label: str
    title: str
    media_dive_id: str

    @property
    def source(self) -> str:
        return f"{self.jcm_label} / MediaDive {self.media_dive_id}"


M1200 = Target(
    Path("bacterial/TOGO_M1200_Artficial_Brackish_Water_Medium.yaml"),
    "CultureMech:007727",
    "TOGO:M1200",
    "https://togomedium.org/medium/M1200",
    JCM_1122,
    MEDIADIVE_J1122,
    "JCM Medium 1122",
    "Artficial Brackish Water Medium",
    "J1122",
)
M1202 = Target(
    Path("bacterial/TOGO_M1202_Artficial_Freshwater_Medium_I.yaml"),
    "CultureMech:007729",
    "TOGO:M1202",
    "https://togomedium.org/medium/M1202",
    JCM_1124,
    MEDIADIVE_J1124,
    "JCM Medium 1124",
    "Artficial Freshwater Medium I",
    "J1124",
)
M1203 = Target(
    Path("bacterial/TOGO_M1203_Artficial_Freshwater_Medium_II.yaml"),
    "CultureMech:007730",
    "TOGO:M1203",
    "https://togomedium.org/medium/M1203",
    JCM_1125,
    MEDIADIVE_J1125,
    "JCM Medium 1125",
    "Artficial Freshwater Medium II",
    "J1125",
)
M1204 = Target(
    Path("bacterial/TOGO_M1204_Artficial_Freshwater_Medium_II.yaml"),
    "CultureMech:007731",
    "TOGO:M1204",
    "https://togomedium.org/medium/M1204",
    JCM_1125,
    MEDIADIVE_J1125,
    "JCM Medium 1125",
    "Artficial Freshwater Medium II",
    "J1125",
)
TARGETS = (M1200, M1202, M1203, M1204)

MIDDLE_DOT = "\u30fb"

IMPORTED_COMMON_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("FeCl2 solution (see Medium [M180])", "1", "G_PER_L", ()),
    ("Trace element solution (see Medium [M180])", "1", "G_PER_L", ()),
    ("Selenite--tungstate solution (see Medium [M431])", "1", "G_PER_L", ()),
)
IMPORTED_VITAMIN_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("Vitamin solution (see Medium [M401])", "1", "G_PER_L", ()),
    ("Thiamine solution (see Medium [M401])", "1", "G_PER_L", ()),
    ("Vitamin B12 solution (see Medium [M401])", "1", "G_PER_L", ()),
    (f"5% Na2S{MIDDLE_DOT}9H2O solution", "5", "G_PER_L", ()),
)
M1200_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "940", "G_PER_L"),
    ("NaCl", "13", "G_PER_L"),
    ("KH2PO4", "0.2", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("Resazurin", "1", "G_PER_L"),
    ("KCl", "0.36", "G_PER_L"),
    ("Na2SO4", "1.42", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("N2", "variable", "VARIABLE"),
)
M1202_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "960", "G_PER_L"),
    ("NaCl", "5", "G_PER_L"),
    ("KH2PO4", "0.2", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("Resazurin", "1", "G_PER_L"),
    ("KCl", "0.3", "G_PER_L"),
    ("Na2SO4", "1.4", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("N2", "variable", "VARIABLE"),
)
M1203_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "960", "G_PER_L"),
    ("KH2PO4", "0.2", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("Resazurin", "1", "G_PER_L"),
    ("KCl", "0.3", "G_PER_L"),
    ("Na2SO4", "1.4", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("N2", "variable", "VARIABLE"),
)
M1200_IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    *IMPORTED_COMMON_SOLUTIONS,
    ("8% NaHCO3 solution*", "30", "G_PER_L", ()),
    (f"1 M CaCl2{MIDDLE_DOT}2H2O solution", "5", "G_PER_L", ()),
    (f"1 M MgCl2{MIDDLE_DOT}6H2O solution", "15", "G_PER_L", ()),
    ("1 M Glucose solution", "10", "G_PER_L", ()),
    *IMPORTED_VITAMIN_SOLUTIONS,
)
M1202_IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    *IMPORTED_COMMON_SOLUTIONS,
    ("8% NaHCO3 solution*", "30", "G_PER_L", ()),
    (f"1 M CaCl2{MIDDLE_DOT}2H2O solution", "1", "G_PER_L", ()),
    (f"1 M MgCl2{MIDDLE_DOT}6H2O solution", "2.5", "G_PER_L", ()),
    ("1 M Fructose solution*", "10", "G_PER_L", ()),
    *IMPORTED_VITAMIN_SOLUTIONS,
)
M1203_IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    *IMPORTED_COMMON_SOLUTIONS,
    ("8% NaHCO3 solution*", "30", "G_PER_L", ()),
    (f"1 M CaCl2{MIDDLE_DOT}2H2O solution", "1", "G_PER_L", ()),
    (f"1 M MgCl2{MIDDLE_DOT}6H2O solution", "2.5", "G_PER_L", ()),
    ("10% Yeast extract solution", "1", "G_PER_L", ()),
    ("1 M Glycerin solution*", "10", "G_PER_L", ()),
    *IMPORTED_VITAMIN_SOLUTIONS,
)
M1204_IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    *IMPORTED_COMMON_SOLUTIONS,
    ("8% NaHCO3 solution*", "30", "G_PER_L", ()),
    (f"1 M CaCl2{MIDDLE_DOT}2H2O solution", "1", "G_PER_L", ()),
    (f"1 M MgCl2{MIDDLE_DOT}6H2O solution", "2.5", "G_PER_L", ()),
    ("10% Yeast extract solution", "1", "G_PER_L", ()),
    ("sodium lactate solution", "10", "G_PER_L", ()),
    *IMPORTED_VITAMIN_SOLUTIONS,
)

M1200_BASE_SIGNATURE: tuple[Component, ...] = (
    ("KH2PO4", "0.197824", "G_PER_L"),
    ("NH4Cl", "0.24728", "G_PER_L"),
    ("KCl", "0.356083", "G_PER_L"),
    ("NaCl", "12.8586", "G_PER_L"),
    ("Na2SO4", "1.40455", "G_PER_L"),
    ("Resazurin", "0.98912", "MG_PER_L"),
    ("Distilled water", "940.0", "ML_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("N2", "variable", "VARIABLE"),
)
M1202_BASE_SIGNATURE: tuple[Component, ...] = (
    ("KH2PO4", "0.197239", "G_PER_L"),
    ("NH4Cl", "0.246548", "G_PER_L"),
    ("KCl", "0.295858", "G_PER_L"),
    ("NaCl", "4.93097", "G_PER_L"),
    ("Na2SO4", "1.38067", "G_PER_L"),
    ("Resazurin", "0.986193", "MG_PER_L"),
    ("Distilled water", "960.0", "ML_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("N2", "variable", "VARIABLE"),
)
M1203_BASE_SIGNATURE: tuple[Component, ...] = (
    ("KH2PO4", "0.19685", "G_PER_L"),
    ("NH4Cl", "0.246063", "G_PER_L"),
    ("KCl", "0.295276", "G_PER_L"),
    ("Na2SO4", "1.37795", "G_PER_L"),
    ("Resazurin", "0.984252", "MG_PER_L"),
    ("Distilled water", "960.0", "ML_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("N2", "variable", "VARIABLE"),
)

FECL2_SIGNATURE: tuple[Component, ...] = (
    ("HCl", "10.0", "ML_PER_L"),
    ("FeCl2 x 4H2O", "1.5", "G_PER_L"),
    ("Distilled water", "990.0", "ML_PER_L"),
)
TRACE_ELEMENT_SIGNATURE: tuple[Component, ...] = (
    ("ZnCl2", "70.0", "MG_PER_L"),
    ("MnCl2 x 4H2O", "100.0", "MG_PER_L"),
    ("H3BO3", "6.0", "MG_PER_L"),
    ("CoCl2 x 6H2O", "190.0", "MG_PER_L"),
    ("CuCl2 x 2H2O", "2.0", "MG_PER_L"),
    ("NiCl2 x 6H2O", "24.0", "MG_PER_L"),
    ("Na2MoO4 x 2H2O", "36.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)
SELENITE_TUNGSTATE_SIGNATURE: tuple[Component, ...] = (
    ("NaOH", "0.4", "G_PER_L"),
    ("Na2SeO3 x 5H2O", "6.0", "MG_PER_L"),
    ("Na2WO4 x 2H2O", "8.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)
GROUNDINGS: dict[str, tuple[str, str]] = {
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "CoCl2 x 6H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2H2O": ("CHEBI:86318", "copper dichloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl2 x 4H2O": ("CHEBI:86249", "iron dichloride tetrahydrate"),
    "Fructose": ("CHEBI:28757", "fructose"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Glycerol": ("CHEBI:17754", "glycerol"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "HCl": ("CHEBI:17883", "hydrogen chloride"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "MgCl2 x 6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MnCl2 x 4H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "N2": ("CHEBI:17997", "dinitrogen"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Na2SeO3 x 5H2O": ("CHEBI:131361", "disodium selenite pentahydrate"),
    "Na2SO4": ("CHEBI:32149", "sodium sulfate"),
    "Na2WO4 x 2H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Sodium lactate": ("CHEBI:75228", "sodium lactate"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "ZnCl2": ("CHEBI:49976", "zinc chloride"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
    "VARIABLE": "variable",
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
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _components(
    signature: tuple[Component, ...],
    *,
    source: str,
    ungrounded: frozenset[str] = frozenset(),
) -> list[dict[str, Any]]:
    return [
        _component(
            preferred_term,
            value,
            unit,
            source=source,
            term=preferred_term not in ungrounded,
        )
        for preferred_term, value, unit in signature
    ]


def _solution(
    preferred_term: str,
    value: str,
    composition: list[dict[str, Any]],
    *,
    source: str,
    notes: str,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": composition,
    }
    if preparation_notes:
        row["preparation_notes"] = preparation_notes
    return row


def _base_component(preferred_term: str, value: str, unit: str, target: Target) -> dict[str, Any]:
    source = target.source
    if preferred_term == "Distilled water":
        notes = f"{target.jcm_label} lists {value} ml distilled water before stock additions."
    elif unit == "MG_PER_L":
        notes = (
            f"{target.jcm_label} lists 1.0 mg {preferred_term}; MediaDive "
            f"{target.media_dive_id} normalizes this to {value} mg/L."
        )
    elif unit == "VARIABLE":
        notes = f"{target.jcm_label} uses an N2-CO2 (4:1, v/v) gas atmosphere."
    else:
        notes = (
            f"{target.jcm_label} lists {preferred_term} in the main solution; "
            f"MediaDive {target.media_dive_id} normalizes this to {value} g/L."
        )

    return _component(preferred_term, value, unit, source=source, notes=notes)


def _stock_solution(
    preferred_term: str,
    value: str,
    component: str,
    *,
    source: str,
) -> dict[str, Any]:
    return _solution(
        preferred_term,
        value,
        [_component(component, "1.0", "MOLAR", source=source)],
        source=source,
        notes=f"{source} adds {value} ml/L {preferred_term}.",
    )


def _percent_solution(
    preferred_term: str,
    value: str,
    component: str,
    grams_per_l: str,
    *,
    source: str,
    term: bool = True,
) -> dict[str, Any]:
    return _solution(
        preferred_term,
        value,
        [
            _component(
                component,
                grams_per_l,
                "G_PER_L",
                source=source,
                notes=(
                    f"{source} lists {preferred_term}; this records the stock "
                    f"as {grams_per_l} g/L {component}."
                ),
                term=term,
            )
        ],
        source=source,
        notes=f"{source} adds {value} ml/L {preferred_term}.",
    )


def _fecl2_solution(source: str) -> dict[str, Any]:
    return _solution(
        "FeCl2 solution",
        "1.0",
        _components(FECL2_SIGNATURE, source=JCM_187_SOURCE),
        source=source,
        notes=f"{source} adds 1.0 ml/L FeCl2 solution from JCM Medium 187.",
        preparation_notes="JCM Medium 187 prepares the stock with 25% HCl (7.7 M).",
    )


def _trace_element_solution(source: str) -> dict[str, Any]:
    return _solution(
        "Trace element solution",
        "1.0",
        _components(
            TRACE_ELEMENT_SIGNATURE,
            source=JCM_187_SOURCE,
            ungrounded=frozenset({"NiCl2 x 6H2O"}),
        ),
        source=source,
        notes=f"{source} adds 1.0 ml/L Trace element solution from JCM Medium 187.",
    )


def _selenite_tungstate_solution(source: str) -> dict[str, Any]:
    return _solution(
        "Selenite-tungstate solution",
        "1.0",
        _components(SELENITE_TUNGSTATE_SIGNATURE, source=JCM_431_SOURCE),
        source=source,
        notes=f"{source} adds 1.0 ml/L Selenite-tungstate solution from JCM Medium 431.",
    )


def _vitamin_solution(source: str) -> dict[str, Any]:
    return _solution(
        "Vitamin solution",
        "1.0",
        [
            _component(
                "p-Aminobenzoic acid",
                "40.0",
                "MG_PER_L",
                source=JCM_403_SOURCE,
                notes=(
                    "JCM Medium 403 lists 4.0 mg p-Aminobenzoic acid in "
                    "100.0 ml Vitamin solution; this records the stock as "
                    "40.0 mg/L."
                ),
            ),
            _component(
                "Biotin",
                "10.0",
                "MG_PER_L",
                source=JCM_403_SOURCE,
                notes=(
                    "JCM Medium 403 lists 1.0 mg Biotin in 100.0 ml "
                    "Vitamin solution; this records the stock as 10.0 mg/L."
                ),
            ),
            _component(
                "Nicotinic acid",
                "100.0",
                "MG_PER_L",
                source=JCM_403_SOURCE,
                notes=(
                    "JCM Medium 403 lists 10.0 mg Nicotinic acid in 100.0 ml "
                    "Vitamin solution; this records the stock as 100.0 mg/L."
                ),
            ),
            _component(
                "Calcium pantothenate",
                "50.0",
                "MG_PER_L",
                source=JCM_403_SOURCE,
                notes=(
                    "JCM Medium 403 lists 5.0 mg DL-Calcium pantothenate in "
                    "100.0 ml Vitamin solution; this records the stock as "
                    "50.0 mg/L."
                ),
            ),
            _component(
                "Pyridoxine HCl",
                "100.0",
                "MG_PER_L",
                source=JCM_403_SOURCE,
                notes=(
                    "JCM Medium 403 lists 10.0 mg Pyridoxine HCl in "
                    "100.0 ml Vitamin solution; this records the stock as "
                    "100.0 mg/L."
                ),
            ),
            _component(
                "Sodium phosphate buffer (10 mM, pH 7.1)",
                "1000.0",
                "ML_PER_L",
                source=JCM_403_SOURCE,
                notes=(
                    "JCM Medium 403 lists 100.0 ml Sodium phosphate buffer "
                    "(10 mM, pH 7.1) as the 100.0 ml Vitamin solution base."
                ),
                term=False,
            ),
        ],
        source=source,
        notes=f"{source} adds 1.0 ml/L filter-sterilized Vitamin solution.",
        preparation_notes=(
            "JCM Medium 403 prints the Vitamin solution subrecipe in "
            "100.0 ml sodium phosphate buffer at 10 mM, pH 7.1."
        ),
    )


def _thiamine_solution(source: str) -> dict[str, Any]:
    return _solution(
        "Thiamine solution",
        "1.0",
        [
            _component(
                "Thiamine HCl",
                "100.0",
                "MG_PER_L",
                source=JCM_403_SOURCE,
                notes=(
                    "JCM Medium 403 lists 10.0 mg Thiamine HCl in 100.0 ml "
                    "Thiamine solution; this records the stock as 100.0 mg/L."
                ),
            ),
            _component(
                "Sodium phosphate buffer (25 mM, pH 3.4)",
                "1000.0",
                "ML_PER_L",
                source=JCM_403_SOURCE,
                notes=(
                    "JCM Medium 403 lists 100.0 ml Sodium phosphate buffer "
                    "(25 mM, pH 3.4) as the 100.0 ml Thiamine solution base."
                ),
                term=False,
            ),
        ],
        source=source,
        notes=f"{source} adds 1.0 ml/L filter-sterilized Thiamine solution.",
        preparation_notes=(
            "JCM Medium 403 prints the Thiamine solution subrecipe in "
            "100.0 ml sodium phosphate buffer at 25 mM, pH 3.4."
        ),
    )


def _vitamin_b12_solution(source: str) -> dict[str, Any]:
    return _solution(
        "Vitamin B12 solution",
        "1.0",
        [
            _component(
                "Vitamin B12",
                "50.0",
                "MG_PER_L",
                source=JCM_403_SOURCE,
                notes=(
                    "JCM Medium 403 lists 5.0 mg Vitamin B12 in 100.0 ml "
                    "Vitamin B12 solution; this records the stock as 50.0 mg/L."
                ),
            ),
            _component(
                "Distilled water",
                "1000.0",
                "ML_PER_L",
                source=JCM_403_SOURCE,
                notes=(
                    "JCM Medium 403 lists 100.0 ml Distilled water as the "
                    "100.0 ml Vitamin B12 solution base."
                ),
            ),
        ],
        source=source,
        notes=f"{source} adds 1.0 ml/L filter-sterilized Vitamin B12 solution.",
    )


def _base_signature(target: Target) -> tuple[Component, ...]:
    if target == M1200:
        return M1200_BASE_SIGNATURE
    if target == M1202:
        return M1202_BASE_SIGNATURE
    if target in (M1203, M1204):
        return M1203_BASE_SIGNATURE
    raise ValueError(f"{target.path}: no base signature configured")


def _ingredients(target: Target) -> list[dict[str, Any]]:
    return [
        _base_component(preferred_term, value, unit, target)
        for preferred_term, value, unit in _base_signature(target)
    ]


def _carbon_solutions(target: Target) -> list[dict[str, Any]]:
    source = target.jcm_label
    if target == M1200:
        return [_stock_solution("1 M Glucose solution", "10.0", "Glucose", source=source)]
    if target == M1202:
        return [_stock_solution("1 M Fructose solution", "10.0", "Fructose", source=source)]
    if target == M1203:
        return [
            _percent_solution(
                "10% Yeast extract solution",
                "1.0",
                "Yeast extract",
                "100.0",
                source=source,
                term=False,
            ),
            _stock_solution("1 M Glycerin solution", "10.0", "Glycerol", source=source),
        ]
    if target == M1204:
        return [
            _percent_solution(
                "10% Yeast extract solution",
                "1.0",
                "Yeast extract",
                "100.0",
                source=source,
                term=False,
            ),
            _stock_solution(
                "1 M sodium lactate solution",
                "10.0",
                "Sodium lactate",
                source=source,
            ),
        ]
    raise ValueError(f"{target.path}: no carbon stock repair configured")


def _solutions(target: Target) -> list[dict[str, Any]]:
    source = target.jcm_label
    magnesium_value = "15.0" if target == M1200 else "2.5"
    calcium_value = "5.0" if target == M1200 else "1.0"

    return [
        _fecl2_solution(source),
        _trace_element_solution(source),
        _selenite_tungstate_solution(source),
        _percent_solution(
            "8% NaHCO3 solution",
            "30.0",
            "NaHCO3",
            "80.0",
            source=source,
        ),
        _stock_solution(
            "1 M MgCl2 x 6H2O solution",
            magnesium_value,
            "MgCl2 x 6H2O",
            source=source,
        ),
        _stock_solution(
            "1 M CaCl2 x 2H2O solution",
            calcium_value,
            "CaCl2 x 2H2O",
            source=source,
        ),
        _vitamin_solution(source),
        _thiamine_solution(source),
        _vitamin_b12_solution(source),
        *_carbon_solutions(target),
        _percent_solution(
            "5% Na2S x 9H2O solution",
            "5.0",
            "Na2S x 9H2O",
            "50.0",
            source=source,
        ),
    ]


def _preparation_steps(target: Target) -> list[dict[str, Any]]:
    carbon_solution = (
        "glucose"
        if target == M1200
        else "fructose"
        if target == M1202
        else "yeast extract and glycerin"
        if target == M1203
        else "yeast extract and sodium lactate"
    )
    return [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Mix the base salts, FeCl2 solution, Trace element solution, "
                "Selenite-tungstate solution, resazurin, and distilled water."
            ),
        },
        {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave the base medium under an N2-CO2 (4:1, v/v) gas atmosphere.",
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": (
                "After cooling, add the listed NaHCO3, MgCl2, CaCl2, vitamin, "
                f"thiamine, vitamin B12, and {carbon_solution} stock solutions."
            ),
        },
        {
            "step_number": 4,
            "action": "ALIQUOT",
            "description": (
                "Aseptically and anaerobically distribute under the same gas "
                "mixture and seal with butyl rubber stoppers."
            ),
        },
        {
            "step_number": 5,
            "action": "MIX",
            "description": "Prior to use, add 5.0 ml/L 5% Na2S x 9H2O solution.",
        },
    ]


def _notes(target: Target) -> str:
    if target == M1204:
        return (
            "TOGO M1204 records a JCM_M1125-2 variant of Artficial Freshwater "
            "Medium II. JCM Medium 1125 / MediaDive J1125 supplies the complete "
            "base solution, FeCl2, Trace element, Selenite-tungstate, and "
            "vitamin stock compositions and directs using 1 M sodium lactate "
            "solution instead of the 1 M glycerin solution for JCM 31104."
        )

    return (
        f"TOGO {target.media_term.removeprefix('TOGO:')} records {target.jcm_label} "
        f"as {target.title}. {target.jcm_label} / MediaDive {target.media_dive_id} "
        "supplies the complete base solution; JCM Media 187, 403, and 431 supply "
        "the FeCl2, Trace element, Selenite-tungstate, Vitamin, Thiamine, and "
        "Vitamin B12 stock compositions."
    )


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


def _imported_ingredient_signature(target: Target) -> tuple[Component, ...]:
    if target == M1200:
        return M1200_IMPORTED_INGREDIENT_SIGNATURE
    if target == M1202:
        return M1202_IMPORTED_INGREDIENT_SIGNATURE
    if target in (M1203, M1204):
        return M1203_IMPORTED_INGREDIENT_SIGNATURE
    raise ValueError(f"{target.path}: no imported ingredient signature configured")


def _imported_solution_signatures(target: Target) -> tuple[SolutionSignature, ...]:
    if target == M1200:
        return M1200_IMPORTED_SOLUTION_SIGNATURES
    if target == M1202:
        return M1202_IMPORTED_SOLUTION_SIGNATURES
    if target == M1203:
        return M1203_IMPORTED_SOLUTION_SIGNATURES
    if target == M1204:
        return M1204_IMPORTED_SOLUTION_SIGNATURES
    raise ValueError(f"{target.path}: no imported solution signature configured")


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != target.media_term:
        raise ValueError(f"{target.path}: expected media term {target.media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        _imported_ingredient_signature(target),
        _signature(_ingredients(target), "final ingredients"),
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        _imported_solution_signatures(target),
        _solution_signatures({"solutions": _solutions(target)}),
    ):
        raise ValueError(f"{target.path}: solution signature drifted")


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


def _references(target: Target) -> tuple[str, ...]:
    return (
        target.togo_url,
        target.jcm_url,
        target.mediadive_url,
        TOGO_M180,
        JCM_187,
        TOGO_M401,
        JCM_403,
        TOGO_M431,
        JCM_431,
    )


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in _references(target):
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target, notes: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(_references(target)),
        "notes": notes,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    notes = _notes(target)
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED" if target in (M1200, M1202) else "COMPLEX"
    repaired["composition_type"] = "DEFINED" if target in (M1200, M1202) else "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(target)
    repaired["solutions"] = _solutions(target)
    _put_after(repaired, "preparation_steps", _preparation_steps(target), "solutions")
    _put_after(repaired, "notes", notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target, notes)
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
