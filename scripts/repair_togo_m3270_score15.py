#!/usr/bin/env python3
"""Repair TOGO M3270 TMBS4 Medium."""

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
TARGET = Path("bacterial/TOGO_M3270_Tmbs4_Medium.yaml")
PARENT = Path("bacterial/tmbs4_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009690"
EXPECTED_PARENT_ID = "CultureMech:001694"
EXPECTED_MEDIA_TERM = "TOGO:M3270"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:559"

CURATOR = "repair_togo_m3270_score15.py"
ACTION = "RESOLVED_TOGO_M3270_SCORE15"
LINK_ACTION = "LINKED_TOGO_M3270_SOURCE_DUPLICATE"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M3270 = "https://togomedium.org/medium/M3270"
TOGO_M180 = "https://togomedium.org/medium/M180"
TOGO_M190 = "https://togomedium.org/medium/M190"
TOGO_M401 = "https://togomedium.org/medium/M401"
TOGO_M431 = "https://togomedium.org/medium/M431"
JCM_1408 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1408"
JCM_187 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"
JCM_403 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403"
JCM_431 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431"

SOURCE = "TOGO M3270 / JCM Medium 1408"
JCM_187_SOURCE = "JCM Medium 187"
JCM_197_SOURCE = "JCM Medium 197"
JCM_403_SOURCE = "JCM Medium 403"
JCM_431_SOURCE = "JCM Medium 431"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

MIDDLE_DOT = "\u00b7"

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1030.0", "G_PER_L"),
    ("NaCl", "1", "G_PER_L"),
    (f"CaCl2{MIDDLE_DOT}2H2O", "0.15", "G_PER_L"),
    ("KH2PO4", "0.2", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("Resazurin", "0.5", "G_PER_L"),
    (f"MgCl2{MIDDLE_DOT}6H2O", "0.4", "G_PER_L"),
    ("KCl", "0.5", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Syringic acid", "6", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "1.0", "G_PER_L"),
    ("MgCl2 x 6H2O", "0.4", "G_PER_L"),
    ("CaCl2 x 2H2O", "0.15", "G_PER_L"),
    ("KCl", "0.5", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("KH2PO4", "0.2", "G_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("Distilled water", "930.0", "ML_PER_L"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("FeCl2 solution (see Medium [M180])", "1", "G_PER_L", ()),
    ("Trace element solution (see Medium [M180])", "1", "G_PER_L", ()),
    ("Selenite--tungstate solution (see Medium [M431])", "1", "G_PER_L", ()),
    ("5% NaHCO3 solution*", "30", "G_PER_L", ()),
    ("10% Yeast extract solution", "10", "G_PER_L", ()),
    ("5% Sodium thiosulfate solution", "2", "G_PER_L", ()),
    ("0.1 M Dithiothreitol solutuion*", "10", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
    ("Vitamin B12 solution (see Medium [M401])", "1", "G_PER_L", ()),
    ("Syringate solution (see below)", "10", "G_PER_L", ()),
    ("2.5% Sodium dithionite solution", "10", "G_PER_L", ()),
    ("2N NaOH solution", "variable", "VARIABLE", ()),
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

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "CoCl2 x 6H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2H2O": ("CHEBI:86318", "copper dichloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Dithiothreitol": ("CHEBI:18320", "1,4-dithiothreitol"),
    "FeCl2 x 4H2O": ("CHEBI:86249", "iron dichloride tetrahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "HCl": ("CHEBI:17883", "hydrogen chloride"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "MgCl2 x 6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MnCl2 x 4H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2SeO3 x 5H2O": ("CHEBI:131361", "disodium selenite pentahydrate"),
    "Na2WO4 x 2H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Sodium dithionite": ("CHEBI:66870", "sodium dithionite"),
    "Sodium thiosulfate": ("CHEBI:132112", "sodium thiosulfate"),
    "Syringic acid": ("CHEBI:68329", "syringic acid"),
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

REFERENCES = (
    TOGO_M3270,
    JCM_1408,
    TOGO_M180,
    JCM_187,
    TOGO_M190,
    JCM_197,
    TOGO_M401,
    JCM_403,
    TOGO_M431,
    JCM_431,
)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_PARENT_ID,
    "name": "tmbs4_medium",
    "notes": (
        "TOGO M3270 imports JCM Medium 1408, which records the same TMBS4 "
        "formulation as DSMZ Medium 559."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_ID,
    "name": "tmbs4_medium",
    "notes": (
        "TOGO M3270 imports JCM Medium 1408, a source duplicate of DSMZ " "Medium 559 TMBS4."
    ),
}

VARIANT_MODIFICATIONS = (
    "Same TMBS4 base formulation as DSMZ Medium 559; TOGO M3270 retains JCM "
    "Medium 1408 stock additions as structured solution entries."
)

NOTES = (
    "TOGO M3270 imports JCM Medium 1408 TMBS4 Medium. JCM Medium 1408 "
    "lists the 930 ml base, 1 ml/L FeCl2 stock from JCM Medium 187, 1 ml/L "
    "Trace element stock from JCM Medium 187, 1 ml/L Selenite-tungstate "
    "stock from JCM Medium 431, 30 ml/L 5% NaHCO3, 10 ml/L Trace vitamins "
    "from JCM Medium 197, 1 ml/L Vitamin B12 stock from JCM Medium 403, "
    "2 ml/L 5% Sodium thiosulfate, 10 ml/L 10% Yeast extract, 10 ml/L "
    "Syringate, 10 ml/L 0.1 M Dithiothreitol, and 10 ml/L freshly prepared "
    "2.5% Sodium dithionite after inoculation. The final pH is 7.2-7.4."
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
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
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
    source: str = SOURCE,
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


def _percent_solution(
    preferred_term: str,
    value: str,
    component: str,
    grams_per_l: str,
    *,
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
                source=SOURCE,
                notes=(
                    f"JCM Medium 1408 lists {preferred_term}; this records "
                    f"the stock as {grams_per_l} g/L {component}."
                ),
                term=term,
            )
        ],
        notes=f"JCM Medium 1408 adds {value} ml/L {preferred_term}.",
    )


def _ingredient(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    notes = None
    if unit == "VARIABLE":
        notes = (
            "JCM Medium 1408 uses an N2-CO2 (4:1, v/v) gas atmosphere "
            "during autoclaving and anaerobic dispensing."
        )
    return _component(preferred_term, value, unit, source=SOURCE, notes=notes)


def _ingredients() -> list[dict[str, Any]]:
    return [
        _ingredient(preferred_term, value, unit)
        for preferred_term, value, unit in FINAL_INGREDIENT_SIGNATURE
    ]


def _fecl2_solution() -> dict[str, Any]:
    return _solution(
        "FeCl2 solution",
        "1.0",
        _components(FECL2_SIGNATURE, source=JCM_187_SOURCE),
        notes="JCM Medium 1408 adds 1.0 ml/L FeCl2 solution from JCM Medium 187.",
        preparation_notes="JCM Medium 187 prepares the stock with 25% HCl (7.7 M).",
    )


def _trace_element_solution() -> dict[str, Any]:
    return _solution(
        "Trace element solution",
        "1.0",
        _components(
            TRACE_ELEMENT_SIGNATURE,
            source=JCM_187_SOURCE,
            ungrounded=frozenset({"NiCl2 x 6H2O"}),
        ),
        notes=("JCM Medium 1408 adds 1.0 ml/L Trace element solution from " "JCM Medium 187."),
    )


def _selenite_tungstate_solution() -> dict[str, Any]:
    return _solution(
        "Selenite-tungstate solution",
        "1.0",
        _components(SELENITE_TUNGSTATE_SIGNATURE, source=JCM_431_SOURCE),
        notes=("JCM Medium 1408 adds 1.0 ml/L Selenite-tungstate solution from " "JCM Medium 431."),
    )


def _trace_vitamins() -> dict[str, Any]:
    return _solution(
        "Trace vitamins",
        "10.0",
        _components(TRACE_VITAMINS_SIGNATURE, source=JCM_197_SOURCE),
        notes=(
            "JCM Medium 1408 adds 10.0 ml/L filter-sterilized Trace vitamins "
            "from JCM Medium 197."
        ),
        preparation_notes="Filter-sterilize while gassing with N2.",
    )


def _vitamin_b12_solution() -> dict[str, Any]:
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
        notes=(
            "JCM Medium 1408 adds 1.0 ml/L filter-sterilized Vitamin B12 "
            "solution from JCM Medium 403."
        ),
    )


def _syringate_solution() -> dict[str, Any]:
    return _solution(
        "Syringate solution",
        "10.0",
        [
            _component(
                "Syringic acid",
                "60.0",
                "G_PER_L",
                source=SOURCE,
                notes=(
                    "JCM Medium 1408 dissolves 6 g Syringic acid and fills "
                    "the Syringate solution to 100 ml."
                ),
            ),
            _component(
                "Distilled water",
                "1000.0",
                "ML_PER_L",
                source=SOURCE,
                notes=(
                    "JCM Medium 1408 fills the Syringate solution to 100 ml "
                    "with Distilled water."
                ),
            ),
            _component(
                "NaOH",
                "variable",
                "VARIABLE",
                source=SOURCE,
                notes=(
                    "JCM Medium 1408 adjusts the Syringate solution to pH 7.5 "
                    "with 2 N NaOH solution."
                ),
            ),
        ],
        notes="JCM Medium 1408 adds 10.0 ml/L Syringate solution.",
        preparation_notes=(
            "Dissolve 6 g syringic acid in 70 ml distilled water, adjust "
            "to pH 7.5 with 2 N NaOH, and fill to 100 ml."
        ),
    )


def _solutions() -> list[dict[str, Any]]:
    return [
        _fecl2_solution(),
        _trace_element_solution(),
        _selenite_tungstate_solution(),
        _percent_solution("5% NaHCO3 solution", "30.0", "NaHCO3", "50.0"),
        _trace_vitamins(),
        _vitamin_b12_solution(),
        _percent_solution(
            "5% Sodium thiosulfate solution",
            "2.0",
            "Sodium thiosulfate",
            "50.0",
        ),
        _percent_solution(
            "10% Yeast extract solution",
            "10.0",
            "Yeast extract",
            "100.0",
            term=False,
        ),
        _syringate_solution(),
        _solution(
            "0.1 M Dithiothreitol solution",
            "10.0",
            [
                _component(
                    "Dithiothreitol",
                    "0.1",
                    "MOLAR",
                    source=SOURCE,
                    notes="JCM Medium 1408 lists 0.1 M Dithiothreitol solution.",
                )
            ],
            notes=(
                "JCM Medium 1408 adds 10.0 ml/L filter-sterilized " "0.1 M Dithiothreitol solution."
            ),
        ),
        _percent_solution(
            "2.5% Sodium dithionite solution",
            "10.0",
            "Sodium dithionite",
            "25.0",
        ),
    ]


PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix the base salts, FeCl2 solution, Trace element solution, "
            "Selenite-tungstate solution, resazurin, and 930.0 ml distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave under an N2-CO2 (4:1, v/v) gas atmosphere.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "After cooling, add the 5% NaHCO3, Trace vitamins, Vitamin B12, "
            "5% Sodium thiosulfate, 10% Yeast extract, Syringate, and "
            "0.1 M Dithiothreitol stocks from anaerobic stocks in sequence."
        ),
    },
    {
        "step_number": 4,
        "action": "ALIQUOT",
        "description": (
            "Aseptically and anaerobically distribute the medium under the "
            "same gas mixture and seal culture vessels with butyl rubber stoppers."
        ),
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "After inoculation, add 10.0 ml/L freshly prepared and "
            "filter-sterilized 2.5% Sodium dithionite solution."
        ),
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": (
        "Autoclave the base under N2-CO2 (4:1, v/v); JCM Medium 1408 "
        "adds sterile anaerobic stocks after cooling and freshly prepared "
        "filter-sterilized Sodium dithionite solution after inoculation."
    ),
}


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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        IMPORTED_SOLUTION_SIGNATURES,
        _solution_signatures({"solutions": _solutions()}),
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"{PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")


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


def _append_curation_event(
    doc: dict[str, Any],
    *,
    action: str,
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(REFERENCES),
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


def _ensure_variant_child(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    for index, child in enumerate(children):
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID or child.get("path") == TOGO_CHILD["path"]:
            children[index] = copy.deepcopy(TOGO_CHILD)
            return
    children.append(copy.deepcopy(TOGO_CHILD))


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_range", {"min": 7.2, "max": 7.4}, "physical_state")
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    repaired["solutions"] = _solutions()
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "solutions")
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["high_metal"] = True
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(
        repaired,
        action=ACTION,
        notes=(
            f"{NOTES} Corrected the imported water and stock-addition unit "
            "artifacts, expanded the JCM Medium 187, 197, 403, and 431 stock "
            "recipes, corrected Resazurin to mg/L, fixed the Dithiothreitol "
            "solution spelling, and linked the record to DSMZ Medium 559."
        ),
    )
    repaired["parent_media"] = copy.deepcopy(PARENT_MEDIA)
    repaired["variant_relationship"] = "SOURCE_DUPLICATE"
    repaired["variant_modifications"] = [VARIANT_MODIFICATIONS]
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    _ensure_variant_child(repaired)
    _append_curation_event(
        repaired,
        action=LINK_ACTION,
        notes="Linked TOGO M3270 as a source duplicate of DSMZ Medium 559.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    parent_path = normalized / PARENT
    return {
        target_path: repair_target(_load(target_path)),
        parent_path: repair_parent(_load(parent_path)),
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
