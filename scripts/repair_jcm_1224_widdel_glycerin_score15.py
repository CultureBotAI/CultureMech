#!/usr/bin/env python3
"""Repair JCM 1224 Widdel Freshwater Medium With Glycerin."""

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
TARGET = Path("bacterial/widdel_freshwater_medium_with_glycerin.yaml")
PARENT = Path("bacterial/widdel_freshwater_medium_with_lactate.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_1224_widdel_glycerin_score15.py"
ACTION = "RESOLVED_JCM_1224_WIDDEL_GLYCERIN_SCORE15"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

EXPECTED_ID = "CultureMech:002391"
EXPECTED_MEDIA_TERM = "mediadive.medium:J1224"
PARENT_ID = "CultureMech:002390"
PARENT_MEDIA_TERM = "mediadive.medium:J1223"

JCM_1224 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1224"
JCM_1223 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1223"
JCM_301 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=301"
JCM_403 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403"
JCM_431 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431"
TOGO_M1316 = "https://togomedium.org/medium/M1316"
TOGO_M296 = "https://togomedium.org/medium/M296"
TOGO_M401 = "https://togomedium.org/medium/M401"
TOGO_M431 = "https://togomedium.org/medium/M431"

SOURCE = "JCM Medium 1224"
PARENT_SOURCE = "JCM Medium 1223"
SOURCE_M296 = "JCM Medium 301 / TOGO M296"
SOURCE_M401 = "JCM Medium 403 / TOGO M401"
SOURCE_M431 = "JCM Medium 431 / TOGO M431"

MIDDLE_DOT = "\u30fb"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "988", "ML_PER_L"),
    ("NaCl", "1", "G_PER_L"),
    (f"CaCl2{MIDDLE_DOT}2H2O", "0.1", "G_PER_L"),
    ("KH2PO4", "0.2", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("Resazurin", "1", "MG_PER_L"),
    (f"MgCl2{MIDDLE_DOT}6H2O", "0.4", "G_PER_L"),
    ("KCl", "0.5", "G_PER_L"),
    ("Na2SO4", "4", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("glycerin solution", "11", "ML_PER_L", ()),
    ("Trace element solution (see Medium [M296])", "1", "ML_PER_L", ()),
    ("Vitamin solution (see Medium [M401])", "1", "ML_PER_L", ()),
    ("Thiamine solution (see Medium [M401])", "1", "ML_PER_L", ()),
    ("Vitamin B12 solution (see Medium [M401])", "1", "ML_PER_L", ()),
    ("Selenite--tungstate solution (see Medium [M431])", "1", "ML_PER_L", ()),
    (f"5% Na2S{MIDDLE_DOT}9H2O solution", "2", "ML_PER_L", ()),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "1.0", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.4", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.1", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("KH2PO4", "0.2", "G_PER_L"),
    ("KCl", "0.5", "G_PER_L"),
    ("Na2SO4", "4.0", "G_PER_L"),
    ("Resazurin", "1.0", "MG_PER_L"),
    ("Distilled water", "988.0", "ML_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

TRACE_ELEMENT_M296: tuple[Component, ...] = (
    ("Nitrilotriacetic acid", "12.8", "G_PER_L"),
    ("FeSO4 x 7 H2O", "0.42", "G_PER_L"),
    ("H3BO3", "0.01", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.1", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.17", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.02", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.21", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.01", "G_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

VITAMIN_M401: tuple[Component, ...] = (
    ("p-Aminobenzoic acid", "40.0", "MG_PER_L"),
    ("Biotin", "10.0", "MG_PER_L"),
    ("Nicotinic acid", "100.0", "MG_PER_L"),
    ("Calcium pantothenate", "50.0", "MG_PER_L"),
    ("Pyridoxine HCl", "100.0", "MG_PER_L"),
    ("Sodium phosphate buffer (10 mM, pH 7.1)", "1000.0", "ML_PER_L"),
)

THIAMINE_M401: tuple[Component, ...] = (
    ("Thiamine HCl", "100.0", "MG_PER_L"),
    ("Sodium phosphate buffer (25 mM, pH 3.4)", "1000.0", "ML_PER_L"),
)

VITAMIN_B12_M401: tuple[Component, ...] = (
    ("Vitamin B12", "50.0", "MG_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

SELENITE_TUNGSTATE_M431: tuple[Component, ...] = (
    ("NaOH", "0.4", "G_PER_L"),
    ("Na2SeO3 x 5 H2O", "6.0", "MG_PER_L"),
    ("Na2WO4 x 2 H2O", "8.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Trace element solution", "1.0", "ML_PER_L", TRACE_ELEMENT_M296),
    ("Vitamin solution", "1.0", "ML_PER_L", VITAMIN_M401),
    ("Thiamine solution", "1.0", "ML_PER_L", THIAMINE_M401),
    ("Vitamin B12 solution", "1.0", "ML_PER_L", VITAMIN_B12_M401),
    ("Selenite-tungstate solution", "1.0", "ML_PER_L", SELENITE_TUNGSTATE_M431),
    ("1 M glycerin solution", "11.0", "ML_PER_L", (("Glycerol", "1.0", "MOLAR"),)),
    ("5% Na2S x 9H2O solution", "2.0", "ML_PER_L", (("Na2S x 9H2O", "50.0", "G_PER_L"),)),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2 H2O": ("CHEBI:86318", "copper dichloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Glycerol": ("CHEBI:17754", "glycerol"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "MgCl2 x 6 H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "N2": ("CHEBI:17997", "dinitrogen"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Na2SeO3 x 5 H2O": ("CHEBI:131361", "disodium selenite pentahydrate"),
    "Na2SO4": ("CHEBI:32149", "sodium sulfate"),
    "Na2WO4 x 2 H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "L": "L",
    "MOLAR": "M",
    "VARIABLE": "variable",
}

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SUBSTITUTED_COMPONENT_VARIANT",
    "id": PARENT_ID,
    "name": "widdel_freshwater_medium_with_lactate",
    "notes": (
        "JCM Medium 1224 uses JCM Medium 1223 and replaces the 1.0 M "
        "L-sodium lactate solution with 11.0 ml/L 1.0 M glycerin solution."
    ),
}

CHILD_REFERENCE = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SUBSTITUTED_COMPONENT_VARIANT",
    "id": EXPECTED_ID,
    "name": "widdel_freshwater_medium_with_glycerin",
    "notes": PARENT_MEDIA["notes"],
}

VARIANT_MODIFICATIONS = [
    (
        "11.0 ml/L separately autoclaved 1.0 M glycerin solution replaces "
        "JCM Medium 1223's 7.3 ml/L 1.0 M L-sodium lactate solution."
    )
]


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


def _trace_component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    notes = None
    if preferred_term == "NaOH":
        notes = (
            f"{SOURCE_M296} uses NaOH to adjust the trace element solution "
            "to pH 6.5."
        )
    elif preferred_term == "Distilled water":
        notes = (
            f"{SOURCE_M296} dissolves nitrilotriacetic acid in 800 ml "
            "distilled water and brings the stock to 1.0 L."
        )
    return _component(preferred_term, value, unit, source=SOURCE_M296, notes=notes)


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


def _base_component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    if preferred_term == "Distilled water":
        notes = f"{PARENT_SOURCE} lists 988.0 ml distilled water before stock additions."
    elif preferred_term == "N2":
        notes = f"{PARENT_SOURCE} autoclaves and distributes the medium under N2 gas."
    else:
        notes = f"{PARENT_SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}."
    return _component(preferred_term, value, unit, source=PARENT_SOURCE, notes=notes)


def _trace_element_solution() -> dict[str, Any]:
    return _solution(
        "Trace element solution",
        "1.0",
        [
            _trace_component(preferred_term, value, unit)
            for preferred_term, value, unit in TRACE_ELEMENT_M296
        ],
        source=PARENT_SOURCE,
        notes=f"{PARENT_SOURCE} adds 1.0 ml/L Trace element solution from JCM Medium 301.",
        preparation_notes=(
            "JCM Medium 301 dissolves nitrilotriacetic acid in 800 ml "
            "distilled water, adjusts to pH 6.5 with NaOH, then adds the "
            "minerals and brings the stock to 1.0 L."
        ),
    )


def _vitamin_solution() -> dict[str, Any]:
    return _solution(
        "Vitamin solution",
        "1.0",
        _components(
            VITAMIN_M401,
            source=SOURCE_M401,
            ungrounded=frozenset({"Sodium phosphate buffer (10 mM, pH 7.1)"}),
        ),
        source=PARENT_SOURCE,
        notes=f"{PARENT_SOURCE} adds 1.0 ml/L filter-sterilized Vitamin solution.",
        preparation_notes=(
            "JCM Medium 403 prints the Vitamin solution subrecipe in "
            "100.0 ml sodium phosphate buffer at 10 mM, pH 7.1."
        ),
    )


def _thiamine_solution() -> dict[str, Any]:
    return _solution(
        "Thiamine solution",
        "1.0",
        _components(
            THIAMINE_M401,
            source=SOURCE_M401,
            ungrounded=frozenset({"Sodium phosphate buffer (25 mM, pH 3.4)"}),
        ),
        source=PARENT_SOURCE,
        notes=f"{PARENT_SOURCE} adds 1.0 ml/L filter-sterilized Thiamine solution.",
        preparation_notes=(
            "JCM Medium 403 prints the Thiamine solution subrecipe in "
            "100.0 ml sodium phosphate buffer at 25 mM, pH 3.4."
        ),
    )


def _vitamin_b12_solution() -> dict[str, Any]:
    return _solution(
        "Vitamin B12 solution",
        "1.0",
        _components(VITAMIN_B12_M401, source=SOURCE_M401),
        source=PARENT_SOURCE,
        notes=f"{PARENT_SOURCE} adds 1.0 ml/L filter-sterilized Vitamin B12 solution.",
    )


def _selenite_tungstate_solution() -> dict[str, Any]:
    return _solution(
        "Selenite-tungstate solution",
        "1.0",
        _components(SELENITE_TUNGSTATE_M431, source=SOURCE_M431),
        source=PARENT_SOURCE,
        notes=f"{PARENT_SOURCE} adds 1.0 ml/L Selenite-tungstate solution from JCM Medium 431.",
    )


def _glycerin_solution() -> dict[str, Any]:
    return _solution(
        "1 M glycerin solution",
        "11.0",
        [
            _component(
                "Glycerol",
                "1.0",
                "MOLAR",
                source=SOURCE,
                notes=f"{SOURCE} adds a separately autoclaved 1.0 M glycerin solution.",
            )
        ],
        source=SOURCE,
        notes=(
            f"{SOURCE} adds 11.0 ml/L separately autoclaved 1.0 M glycerin "
            "solution instead of JCM Medium 1223's 1.0 M sodium lactate "
            "solution."
        ),
        preparation_notes="Autoclave separately.",
    )


def _na2s_solution() -> dict[str, Any]:
    return _solution(
        "5% Na2S x 9H2O solution",
        "2.0",
        [
            _component(
                "Na2S x 9H2O",
                "50.0",
                "G_PER_L",
                source=PARENT_SOURCE,
                notes=(
                    f"{PARENT_SOURCE} adds 2.0 ml/L 5% Na2S x 9H2O solution "
                    "immediately prior to use; this records the stock as "
                    "50.0 g/L Na2S x 9H2O."
                ),
            )
        ],
        source=PARENT_SOURCE,
        notes=f"{PARENT_SOURCE} adds 2.0 ml/L 5% Na2S x 9H2O solution prior to use.",
        preparation_notes="Autoclave under an N2 atmosphere.",
    )


def _ingredients() -> list[dict[str, Any]]:
    return [
        _base_component(preferred_term, value, unit)
        for preferred_term, value, unit in FINAL_INGREDIENT_SIGNATURE
    ]


def _solutions() -> list[dict[str, Any]]:
    return [
        _trace_element_solution(),
        _vitamin_solution(),
        _thiamine_solution(),
        _vitamin_b12_solution(),
        _selenite_tungstate_solution(),
        _glycerin_solution(),
        _na2s_solution(),
    ]


def _preparation_steps() -> list[dict[str, Any]]:
    return [
        {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": (
                "Mix the base components, adjust pH to 7.5, and autoclave "
                "under an N2 gas atmosphere."
            ),
        },
        {
            "step_number": 2,
            "action": "MIX",
            "description": (
                "After cooling, add sterile anaerobic stocks of Trace element "
                "solution, filter-sterilized Vitamin solution, "
                "filter-sterilized Thiamine solution, filter-sterilized "
                "Vitamin B12 solution, Selenite-tungstate solution, and 1.0 M "
                "glycerin solution."
            ),
        },
        {
            "step_number": 3,
            "action": "ALIQUOT",
            "description": (
                "Readjust pH to 7.5 if necessary; separately autoclave and "
                "dry iron metal grains; aseptically distribute the medium and "
                "iron metal into culture vessels under an N2 gas stream and "
                "seal with butyl rubber stoppers."
            ),
        },
        {
            "step_number": 4,
            "action": "MIX",
            "description": "Prior to use, add 2.0 ml/L 5% Na2S x 9H2O solution.",
        },
    ]


def _notes() -> str:
    return (
        "JCM Medium 1224 defines Widdel Freshwater Medium With Glycerin as "
        "JCM Medium 1223 with 11.0 ml/L separately autoclaved 1.0 M glycerin "
        "solution instead of 1.0 M sodium lactate solution. JCM Medium 1223 "
        "supplies the freshwater base and stock-addition schedule; JCM Media "
        "301, 403, and 431 supply the Trace element, Vitamin, Thiamine, "
        "Vitamin B12, and Selenite-tungstate stock compositions."
    )


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
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
    if ingredient_signature not in {
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    }:
        raise ValueError(f"{TARGET}: ingredient signature drifted to {ingredient_signature!r}")

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in {
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    }:
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != PARENT_ID:
        raise ValueError(f"{PARENT}: expected id {PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {PARENT_MEDIA_TERM}")


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
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag
        not in {
            "incomplete_composition",
            "needs_manual_curation",
            "source_information_unavailable",
        }
    ]
    flags.extend(("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _references() -> tuple[str, ...]:
    return (
        JCM_1224,
        JCM_1223,
        JCM_301,
        JCM_403,
        JCM_431,
        TOGO_M1316,
        TOGO_M296,
        TOGO_M401,
        TOGO_M431,
    )


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in _references():
        if url not in existing:
            references.append({"reference": url})


def _append_event(doc: dict[str, Any], notes: str) -> None:
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


def _ensure_child_reference(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")
    for row in children:
        if not isinstance(row, dict):
            raise ValueError("variant_children contains a non-mapping row")

    children[:] = [row for row in children if row.get("id") != EXPECTED_ID]
    children.append(copy.deepcopy(CHILD_REFERENCE))


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    notes = _notes()
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    _put_after(repaired, "ph_value", 7.5, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    _put_after(repaired, "solutions", _solutions(), "ingredients")
    _put_after(repaired, "preparation_steps", _preparation_steps(), "solutions")
    _put_after(repaired, "notes", notes, "media_term")
    _put_after(repaired, "parent_media", copy.deepcopy(PARENT_MEDIA), "notes")
    _put_after(repaired, "variant_relationship", "SUBSTITUTED_COMPONENT_VARIANT", "parent_media")
    _put_after(repaired, "variant_modifications", list(VARIANT_MODIFICATIONS), "variant_relationship")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired, notes)
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)
    repaired = copy.deepcopy(doc)
    _ensure_child_reference(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / TARGET: repair_record(_load(normalized / TARGET)),
        normalized / PARENT: repair_parent(_load(normalized / PARENT)),
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
