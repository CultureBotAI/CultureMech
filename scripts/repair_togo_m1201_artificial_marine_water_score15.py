#!/usr/bin/env python3
"""Repair TOGO M1201 Artficial Marine Water Medium."""

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
TARGET = Path("bacterial/artficial_marine_water_medium.yaml")
EXPECTED_ID = "CultureMech:007728"
EXPECTED_MEDIA_TERM = "TOGO:M1201"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1201_artificial_marine_water_score15.py"
ACTION = "RESOLVED_TOGO_M1201_ARTIFICIAL_MARINE_WATER_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

SOURCE = "JCM Medium 1123"
JCM_187_SOURCE = "JCM Medium 187"
JCM_403_SOURCE = "JCM Medium 403"
JCM_431_SOURCE = "JCM Medium 431"

TOGO_M1201 = "https://togomedium.org/medium/M1201"
JCM_1123 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1123"
JCM_187 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187"
JCM_403 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403"
JCM_431 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

MIDDLE_DOT = "\u30fb"

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "960", "G_PER_L"),
    ("NaCl", "26", "G_PER_L"),
    ("KH2PO4", "0.2", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("Resazurin", "1", "G_PER_L"),
    ("KCl", "0.72", "G_PER_L"),
    ("Na2SO4", "4", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("N2", "variable", "VARIABLE"),
)
IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("FeCl2 solution (see Medium [M180])", "1", "G_PER_L", ()),
    ("Trace element solution (see Medium [M180])", "1", "G_PER_L", ()),
    ("Selenite--tungstate solution (see Medium [M431])", "1", "G_PER_L", ()),
    ("8% NaHCO3 solution*", "30", "G_PER_L", ()),
    (f"1 M CaCl2{MIDDLE_DOT}2H2O solution", "10", "G_PER_L", ()),
    (f"1 M MgCl2{MIDDLE_DOT}6H2O solution", "40", "G_PER_L", ()),
    ("1 M Glucose solution*", "10", "G_PER_L", ()),
    ("Vitamin solution (see Medium [M401])", "1", "G_PER_L", ()),
    ("Thiamine solution (see Medium [M401])", "1", "G_PER_L", ()),
    ("Vitamin B12 solution (see Medium [M401])", "1", "G_PER_L", ()),
    (f"5% Na2S{MIDDLE_DOT}9H2O solution", "5", "G_PER_L", ()),
)

BASE_SIGNATURE: tuple[Component, ...] = (
    ("KH2PO4", "0.188501", "G_PER_L"),
    ("NH4Cl", "0.235627", "G_PER_L"),
    ("KCl", "0.678605", "G_PER_L"),
    ("NaCl", "24.5052", "G_PER_L"),
    ("Na2SO4", "3.77003", "G_PER_L"),
    ("Resazurin", "0.942507", "MG_PER_L"),
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
    "Glucose": ("CHEBI:17234", "glucose"),
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


def _base_component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    if preferred_term == "Distilled water":
        notes = f"{SOURCE} lists 960.0 ml distilled water before stock additions."
    elif unit == "MG_PER_L":
        notes = (
            f"{SOURCE} lists 1.0 mg {preferred_term} in a final 1.061 L "
            f"formulation; this records {value} mg/L."
        )
    elif unit == "VARIABLE":
        notes = f"{SOURCE} uses an N2-CO2 (4:1, v/v) gas atmosphere."
    else:
        notes = (
            f"{SOURCE} lists {preferred_term} in a final 1.061 L formulation; "
            f"this records {value} g/L."
        )

    return _component(preferred_term, value, unit, source=SOURCE, notes=notes)


def _stock_solution(
    preferred_term: str,
    value: str,
    component: str,
    *,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    return _solution(
        preferred_term,
        value,
        [_component(component, "1.0", "MOLAR", source=SOURCE)],
        notes=f"{SOURCE} adds {value} ml/L {preferred_term}.",
        preparation_notes=preparation_notes,
    )


def _percent_solution(
    preferred_term: str,
    value: str,
    component: str,
    grams_per_l: str,
    preparation_notes: str,
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
                    f"{SOURCE} lists {preferred_term}; this records the stock as "
                    f"{grams_per_l} g/L {component}."
                ),
            )
        ],
        notes=f"{SOURCE} adds {value} ml/L {preferred_term}.",
        preparation_notes=preparation_notes,
    )


def _fecl2_solution() -> dict[str, Any]:
    return _solution(
        "FeCl2 solution",
        "1.0",
        _components(FECL2_SIGNATURE, source=JCM_187_SOURCE),
        notes=f"{SOURCE} adds 1.0 ml/L FeCl2 solution from JCM Medium 187.",
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
        notes=f"{SOURCE} adds 1.0 ml/L Trace element solution from JCM Medium 187.",
    )


def _selenite_tungstate_solution() -> dict[str, Any]:
    return _solution(
        "Selenite-tungstate solution",
        "1.0",
        _components(SELENITE_TUNGSTATE_SIGNATURE, source=JCM_431_SOURCE),
        notes=f"{SOURCE} adds 1.0 ml/L Selenite-tungstate solution from JCM Medium 431.",
    )


def _vitamin_solution() -> dict[str, Any]:
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
        notes=f"{SOURCE} adds 1.0 ml/L filter-sterilized Vitamin solution.",
        preparation_notes=(
            "JCM Medium 403 prints the Vitamin solution subrecipe in 100.0 ml "
            "sodium phosphate buffer at 10 mM, pH 7.1."
        ),
    )


def _thiamine_solution() -> dict[str, Any]:
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
        notes=f"{SOURCE} adds 1.0 ml/L filter-sterilized Thiamine solution.",
        preparation_notes=(
            "JCM Medium 403 prints the Thiamine solution subrecipe in 100.0 ml "
            "sodium phosphate buffer at 25 mM, pH 3.4."
        ),
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
        notes=f"{SOURCE} adds 1.0 ml/L filter-sterilized Vitamin B12 solution.",
    )


def _ingredients() -> list[dict[str, Any]]:
    return [
        _base_component(preferred_term, value, unit)
        for preferred_term, value, unit in BASE_SIGNATURE
    ]


def _solutions() -> list[dict[str, Any]]:
    return [
        _fecl2_solution(),
        _trace_element_solution(),
        _selenite_tungstate_solution(),
        _percent_solution(
            "8% NaHCO3 solution",
            "30.0",
            "NaHCO3",
            "80.0",
            "Filter-sterilize separately.",
        ),
        _stock_solution("1 M MgCl2 x 6H2O solution", "40.0", "MgCl2 x 6H2O"),
        _stock_solution("1 M CaCl2 x 2H2O solution", "10.0", "CaCl2 x 2H2O"),
        _vitamin_solution(),
        _thiamine_solution(),
        _vitamin_b12_solution(),
        _stock_solution(
            "1 M Glucose solution",
            "10.0",
            "Glucose",
            preparation_notes="Filter-sterilize separately.",
        ),
        _percent_solution(
            "5% Na2S x 9H2O solution",
            "5.0",
            "Na2S x 9H2O",
            "50.0",
            "Autoclave and store under N2.",
        ),
    ]


def _preparation_steps() -> list[dict[str, Any]]:
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
                "thiamine, vitamin B12, and glucose stock solutions."
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


def _notes() -> str:
    return (
        "TOGO M1201 records JCM Medium 1123 as Artficial Marine Water Medium. "
        "JCM Medium 1123 supplies the complete base solution and post-autoclave "
        "stock volumes; JCM Media 187, 403, and 431 supply the FeCl2, Trace "
        "element, Selenite-tungstate, Vitamin, Thiamine, and Vitamin B12 stock "
        "compositions."
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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        _signature(_ingredients(), "final ingredients"),
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        IMPORTED_SOLUTION_SIGNATURES,
        _solution_signatures({"solutions": _solutions()}),
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


def _references() -> tuple[str, ...]:
    return (TOGO_M1201, JCM_1123, JCM_187, JCM_403, JCM_431)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in _references():
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], notes: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(_references()),
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


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    notes = _notes()
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    repaired["solutions"] = _solutions()
    _put_after(repaired, "preparation_steps", _preparation_steps(), "solutions")
    _put_after(repaired, "notes", notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired, notes)
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
