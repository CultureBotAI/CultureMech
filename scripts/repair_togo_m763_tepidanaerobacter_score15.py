#!/usr/bin/env python3
"""Repair the JCM 738 / TOGO M763 BM for Tepidanaerobacter acetoxydans records."""

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

CURATOR = "repair_togo_m763_tepidanaerobacter_score15.py"
ACTION = "RESOLVED_JCM_738_TOGO_M763_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J738 = "https://mediadive.dsmz.de/medium/J738"
JCM_738 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=738"
JCM_737 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=737"
JCM_294 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=294"
JCM_431 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"
TOGO_M763 = "https://togomedium.org/medium/M763"
TOGO_M762 = "https://togomedium.org/medium/M762"
TOGO_M288 = "https://togomedium.org/medium/M288"
TOGO_M431 = "https://togomedium.org/medium/M431"
TOGO_M190 = "https://togomedium.org/medium/M190"

SOURCE = "JCM Medium 738 / TOGO M763"
SOURCE_M762 = "JCM Medium 737 / TOGO M762"
SOURCE_M288 = "JCM Medium 294 / TOGO M288"
SOURCE_M431 = "JCM Medium 431 / TOGO M431"
SOURCE_M190 = "JCM Medium 197 / TOGO M190"

MIDDLE_DOT = "\u30fb"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term: str
    imported_ingredients: tuple[Component, ...]
    imported_solutions: tuple[SolutionSignature, ...]
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, Any], ...] = ()


JCM_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "830", "ML_PER_L"),
    ("Yeast extract", "0.2", "G_PER_L"),
    ("NaCl", "0.85", "G_PER_L"),
    (f"CaCl2{MIDDLE_DOT}2H2O", "0.1", "G_PER_L"),
    ("NH4Cl", "0.85", "G_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    (f"MgCl2{MIDDLE_DOT}6H2O", "0.28", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

TOGO_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "830", "G_PER_L"),
    ("Yeast extract", "0.2", "G_PER_L"),
    ("NaCl", "0.85", "G_PER_L"),
    (f"CaCl2{MIDDLE_DOT}2H2O", "0.1", "G_PER_L"),
    ("NH4Cl", "0.85", "G_PER_L"),
    ("Resazurin", "0.5", "G_PER_L"),
    (f"MgCl2{MIDDLE_DOT}6H2O", "0.28", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

JCM_IMPORTED_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("Trace metal solution (see Medium [M288])", "1", "ML_PER_L", ()),
    ("Selenite--tungstate solution (see Medium [M431])", "1", "ML_PER_L", ()),
    ("8% NaHCO3 solution*", "40", "ML_PER_L", ()),
    ("glucose solution", "100", "ML_PER_L", ()),
    (f"5% Na2S{MIDDLE_DOT}9H2O solution", "5", "ML_PER_L", ()),
    ("Phosphate solution (see Medium [M762])", "25", "ML_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "1", "ML_PER_L", ()),
)

TOGO_IMPORTED_SOLUTIONS: tuple[SolutionSignature, ...] = tuple(
    (name, value, "G_PER_L", composition)
    for name, value, _unit, composition in JCM_IMPORTED_SOLUTIONS
)

FINAL_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "830.0", "ML_PER_L"),
    ("Yeast extract", "0.2", "G_PER_L"),
    ("NaCl", "0.85", "G_PER_L"),
    ("CaCl2 x 2H2O", "0.1", "G_PER_L"),
    ("NH4Cl", "0.85", "G_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("MgCl2 x 6H2O", "0.28", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

TRACE_METAL_M288: tuple[Component, ...] = (
    ("HCl (32%)", "10.0", "ML_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("Na2MoO4 x 2H2O", "0.04", "G_PER_L"),
    ("H3BO3", "0.006", "G_PER_L"),
    ("MnCl2 x 4H2O", "0.1", "G_PER_L"),
    ("CoCl2 x 6H2O", "0.25", "G_PER_L"),
    ("NiCl2 x 6H2O", "0.07", "G_PER_L"),
    ("CuCl2 x 2H2O", "0.002", "G_PER_L"),
    ("ZnCl2", "0.07", "G_PER_L"),
    ("Na2WO4 x 2H2O", "0.006", "G_PER_L"),
    ("AlCl3", "0.025", "G_PER_L"),
    ("FeCl2 x 4H2O", "2.0", "G_PER_L"),
)

SELENITE_TUNGSTATE_M431: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("Na2SeO3 x 5H2O", "6.0", "MG_PER_L"),
    ("Na2WO4 x 2H2O", "8.0", "MG_PER_L"),
    ("NaOH", "0.4", "G_PER_L"),
)

NAHCO3_STOCK: tuple[Component, ...] = (("NaHCO3", "8.0", "PERCENT_W_V"),)
GLUCOSE_STOCK: tuple[Component, ...] = (("Glucose", "0.1", "MOLAR"),)
NA2S_STOCK: tuple[Component, ...] = (("Na2S x 9H2O", "5.0", "PERCENT_W_V"),)

PHOSPHATE_M762: tuple[Component, ...] = (
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("KH2PO4", "4.1", "G_PER_L"),
    ("Na2HPO4", "4.3", "G_PER_L"),
)

TRACE_VITAMINS_M190: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("Biotin", "2.0", "MG_PER_L"),
    ("p-Aminobenzoic acid", "5.0", "MG_PER_L"),
    ("Thiamine HCl", "5.0", "MG_PER_L"),
    ("Calcium pantothenate", "5.0", "MG_PER_L"),
    ("Pyridoxine HCl", "10.0", "MG_PER_L"),
    ("Folic acid", "2.0", "MG_PER_L"),
    ("Vitamin B12", "0.1", "MG_PER_L"),
    ("Riboflavin", "5.0", "MG_PER_L"),
    ("Nicotinic acid", "5.0", "MG_PER_L"),
    ("Lipoic acid", "5.0", "MG_PER_L"),
)

FINAL_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("Trace metal solution (TOGO Medium M288)", "1.0", "ML_PER_L", TRACE_METAL_M288),
    (
        "Selenite-tungstate solution (TOGO Medium M431)",
        "1.0",
        "ML_PER_L",
        SELENITE_TUNGSTATE_M431,
    ),
    ("8% NaHCO3 solution", "40.0", "ML_PER_L", NAHCO3_STOCK),
    ("0.1 M glucose solution", "100.0", "ML_PER_L", GLUCOSE_STOCK),
    ("5% Na2S x 9H2O solution", "5.0", "ML_PER_L", NA2S_STOCK),
    ("Phosphate solution (TOGO Medium M762)", "25.0", "ML_PER_L", PHOSPHATE_M762),
    ("Trace vitamins (TOGO Medium M190)", "1.0", "ML_PER_L", TRACE_VITAMINS_M190),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "AlCl3": ("CHEBI:30114", "aluminium trichloride"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "CoCl2 x 6H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2H2O": ("CHEBI:86318", "copper dichloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl2 x 4H2O": ("CHEBI:86249", "iron dichloride tetrahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "HCl (32%)": ("CHEBI:17883", "hydrogen chloride"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "MgCl2 x 6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MnCl2 x 4H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "Na2HPO4": ("CHEBI:34683", "disodium hydrogenphosphate"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Na2SeO3 x 5H2O": ("CHEBI:131361", "disodium selenite pentahydrate"),
    "Na2WO4 x 2H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "NiCl2 x 6H2O": ("CHEBI:53542", "nickel chloride hexahydrate"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "ZnCl2": ("CHEBI:49976", "zinc chloride"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "AlCl3": ("TRACE_ELEMENT",),
    "CoCl2 x 6H2O": ("TRACE_ELEMENT",),
    "CuCl2 x 2H2O": ("TRACE_ELEMENT",),
    "FeCl2 x 4H2O": ("IRON_SOURCE", "TRACE_ELEMENT"),
    "Glucose": ("CARBON_SOURCE",),
    "H3BO3": ("TRACE_ELEMENT",),
    "KH2PO4": ("PHOSPHATE_SOURCE",),
    "MnCl2 x 4H2O": ("TRACE_ELEMENT",),
    "Na2HPO4": ("PHOSPHATE_SOURCE",),
    "Na2MoO4 x 2H2O": ("TRACE_ELEMENT",),
    "Na2SeO3 x 5H2O": ("TRACE_ELEMENT",),
    "Na2WO4 x 2H2O": ("TRACE_ELEMENT",),
    "NaOH": ("TRACE_ELEMENT",),
    "NH4Cl": ("NITROGEN_SOURCE",),
    "NiCl2 x 6H2O": ("TRACE_ELEMENT",),
    "Yeast extract": ("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
    "ZnCl2": ("TRACE_ELEMENT",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "KH2PO4": ("BUFFER",),
    "Na2HPO4": ("BUFFER",),
    "Na2S x 9H2O": ("REDUCING_AGENT",),
    "NaHCO3": ("BUFFER",),
    "Resazurin": ("REDOX_INDICATOR",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
    "PERCENT_W_V": "% w/v",
    "VARIABLE": "variable",
}

JCM_PATH = Path("bacterial/bm_for_tepidanaerobacter_acetoxydans.yaml")
TOGO_PATH = Path("bacterial/TOGO_M763_BM_For_Tepidanaerobacter_Acetoxydans.yaml")

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010170",
    "name": "bm_for_tepidanaerobacter_acetoxydans",
    "notes": "TOGO M763 is a transcription of JCM Medium 738.",
}

JCM_PARENT = {
    "path": f"data/normalized_yaml/{JCM_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003081",
    "name": "bm_for_tepidanaerobacter_acetoxydans",
    "notes": "TOGO M763 is a transcription of JCM Medium 738.",
}

JCM_TARGET = Target(
    path=JCM_PATH,
    record_id="CultureMech:003081",
    media_term="mediadive.medium:J738",
    imported_ingredients=JCM_IMPORTED_INGREDIENTS,
    imported_solutions=JCM_IMPORTED_SOLUTIONS,
    references=(
        JCM_738,
        MEDIADIVE_J738,
        TOGO_M763,
        JCM_737,
        TOGO_M762,
        JCM_294,
        TOGO_M288,
        JCM_431,
        TOGO_M431,
        JCM_197,
        TOGO_M190,
    ),
    variant_children=(TOGO_CHILD,),
)

TOGO_TARGET = Target(
    path=TOGO_PATH,
    record_id="CultureMech:010170",
    media_term="TOGO:M763",
    imported_ingredients=TOGO_IMPORTED_INGREDIENTS,
    imported_solutions=TOGO_IMPORTED_SOLUTIONS,
    references=(
        TOGO_M763,
        JCM_738,
        JCM_737,
        TOGO_M762,
        JCM_294,
        TOGO_M288,
        JCM_431,
        TOGO_M431,
        JCM_197,
        TOGO_M190,
    ),
    parent_media=JCM_PARENT,
    variant_relationship="SOURCE_DUPLICATE",
    variant_modifications=("Same JCM Medium 738 formulation as the MediaDive J738 source record.",),
)

TARGETS = (JCM_TARGET, TOGO_TARGET)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix the base ingredients, Trace metal solution, and "
            "Selenite-tungstate solution under an N2-CO2 (80:20, v/v) gas mixture."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": (
            "Autoclave the base medium under the same gas mixture in bottles "
            "sealed with butyl rubber stoppers."
        ),
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "After cooling, aseptically and anaerobically add the NaHCO3, "
            "glucose, Na2S x 9H2O, Phosphate, and Trace vitamins stocks."
        ),
    },
)


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
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    if grounding[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*grounding)

    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _components(signature: tuple[Component, ...], source: str) -> list[dict[str, Any]]:
    rows = []
    for preferred_term, value, unit in signature:
        notes = None
        if preferred_term in {"KH2PO4", "Na2HPO4"} and source == SOURCE_M762:
            listed = "0.41" if preferred_term == "KH2PO4" else "0.43"
            notes = (
                f"{SOURCE_M762} lists {listed} g {preferred_term} in a 100 ml "
                "Phosphate solution; this records the stock as a per-liter "
                "concentration."
            )
        rows.append(_component(preferred_term, value, unit, source=source, notes=notes))
    return rows


def _solution(
    preferred_term: str,
    value: str,
    composition: tuple[Component, ...],
    *,
    source: str,
    component_source: str,
    notes: str,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": _components(composition, component_source),
    }
    if preparation_notes:
        row["preparation_notes"] = preparation_notes
    return row


def _ingredients() -> list[dict[str, Any]]:
    rows = []
    for preferred_term, value, unit in FINAL_INGREDIENTS:
        notes = None
        if preferred_term == "Distilled water":
            notes = f"{SOURCE} lists 830 ml distilled water before stock additions."
        elif preferred_term in {"Carbon dioxide gas", "Nitrogen gas"}:
            notes = f"{SOURCE} uses an N2-CO2 (80:20, v/v) gas atmosphere."
        rows.append(_component(preferred_term, value, unit, source=SOURCE, notes=notes))
    return rows


def _solutions() -> list[dict[str, Any]]:
    return [
        _solution(
            "Trace metal solution (TOGO Medium M288)",
            "1.0",
            TRACE_METAL_M288,
            source=SOURCE,
            component_source=SOURCE_M288,
            notes="JCM Medium 738 adds 1.0 ml/L Trace metal solution from TOGO M288.",
        ),
        _solution(
            "Selenite-tungstate solution (TOGO Medium M431)",
            "1.0",
            SELENITE_TUNGSTATE_M431,
            source=SOURCE,
            component_source=SOURCE_M431,
            notes=("JCM Medium 738 adds 1.0 ml/L Selenite-tungstate solution " "from TOGO M431."),
        ),
        _solution(
            "8% NaHCO3 solution",
            "40.0",
            NAHCO3_STOCK,
            source=SOURCE,
            component_source=SOURCE,
            notes="JCM Medium 738 adds 40.0 ml/L filter-sterilized 8% NaHCO3 solution.",
            preparation_notes="Filter-sterilize this anaerobic stock.",
        ),
        _solution(
            "0.1 M glucose solution",
            "100.0",
            GLUCOSE_STOCK,
            source=SOURCE,
            component_source=SOURCE,
            notes=(
                "JCM Medium 738 adds 100.0 ml/L 0.1 M glucose solution in "
                "place of JCM Medium 737's 0.1 M L-sodium lactate solution."
            ),
            preparation_notes="Filter-sterilize this anaerobic stock.",
        ),
        _solution(
            "5% Na2S x 9H2O solution",
            "5.0",
            NA2S_STOCK,
            source=SOURCE,
            component_source=SOURCE,
            notes="JCM Medium 738 adds 5.0 ml/L 5% Na2S x 9H2O solution.",
            preparation_notes="Autoclave this anaerobic stock under an N2 atmosphere.",
        ),
        _solution(
            "Phosphate solution (TOGO Medium M762)",
            "25.0",
            PHOSPHATE_M762,
            source=SOURCE,
            component_source=SOURCE_M762,
            notes="JCM Medium 738 adds 25.0 ml/L Phosphate solution from TOGO M762.",
        ),
        _solution(
            "Trace vitamins (TOGO Medium M190)",
            "1.0",
            TRACE_VITAMINS_M190,
            source=SOURCE,
            component_source=SOURCE_M190,
            notes="JCM Medium 738 adds 1.0 ml/L Trace vitamins from TOGO M190.",
            preparation_notes="JCM Medium 197 prints the Trace vitamins subrecipe per liter.",
        ),
    ]


def _notes() -> str:
    return (
        "JCM Medium 738 / TOGO M763 lists a defined anaerobic base with yeast "
        "extract, Trace metal solution from TOGO M288, Selenite-tungstate "
        "solution from TOGO M431, 8% NaHCO3, 0.1 M glucose, 5% Na2S x 9H2O, "
        "Phosphate solution from JCM Medium 737 / TOGO M762, Trace vitamins "
        "from TOGO M190, and an N2-CO2 (80:20, v/v) gas phase. The glucose "
        "stock replaces the 0.1 M L-sodium lactate stock in JCM Medium 737."
    )


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature = []
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
    signatures = []
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"solution {solution.get('preferred_term')!r} lacks concentration")
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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != target.media_term:
        raise ValueError(f"{target.path}: expected media term {target.media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    solution_signature = _solution_signatures(doc)
    if (ingredient_signature, solution_signature) not in (
        (target.imported_ingredients, target.imported_solutions),
        (FINAL_INGREDIENTS, FINAL_SOLUTIONS),
    ):
        raise ValueError(
            f"{target.path}: composition signature drifted from importer or " "repaired forms"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "has_unmapped_ingredients",
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
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.references:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.references),
        "notes": (
            "Expanded M763 stock-solution wrappers with TOGO M288, M431, "
            "M762, and M190 compositions; corrected liquid additions and "
            "resazurin units; grounded source-disclosed components; and linked "
            "JCM J738 to the TOGO M763 source duplicate."
        ),
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
        del doc[key]

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

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    for stale_key in ("ph_value", "ph_range", "temperature_value", "temperature_range"):
        repaired.pop(stale_key, None)
    repaired["ingredients"] = _ingredients()
    _put_after(repaired, "solutions", _solutions(), "ingredients")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "solutions")
    _put_after(repaired, "notes", _notes(), "media_term")
    if target.parent_media is not None:
        repaired["parent_media"] = copy.deepcopy(target.parent_media)
        repaired["variant_relationship"] = target.variant_relationship
        repaired["variant_modifications"] = list(target.variant_modifications)
    elif target.variant_children:
        repaired["variant_children"] = copy.deepcopy(list(target.variant_children))

    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
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
