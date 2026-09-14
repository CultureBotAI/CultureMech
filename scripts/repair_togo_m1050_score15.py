#!/usr/bin/env python3
"""Repair TOGO M1050 M30."""

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
TARGET = Path("bacterial/TOGO_M1050_M30.yaml")
EXPECTED_ID = "CultureMech:007567"
EXPECTED_MEDIA_TERM = "TOGO:M1050"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1050_score15.py"
ACTION = "RESOLVED_TOGO_M1050_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1050 = "https://togomedium.org/medium/M1050"
TOGO_M1049 = "https://togomedium.org/medium/M1049"
TOGO_M941 = "https://togomedium.org/medium/M941"
TOGO_M140 = "https://togomedium.org/medium/M140"
JCM_995 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=995"
JCM_900 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=900"
JCM_149 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=149"

SOURCE = "TOGO M1050 / JCM Medium 995"
VITAMIN_SOURCE = "TOGO M1049 / JCM Medium 995"
HUTNER_SOURCE = "TOGO M941 / JCM Medium 900"
METALS_SOURCE = "TOGO M140 / JCM Medium 149"
TITLE = "M30"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("0.1 M Tris--HCl buffer (pH 7.5)", "50", "G_PER_L"),
    ("Distilled water", "300.0", "G_PER_L"),
    ("gelrite (Gellan Gum)", "5", "G_PER_L"),
    ("Aged seawater", "700", "G_PER_L"),
    ("Ampicillin (50 mg/ml)", "4", "G_PER_L"),
    ("Na2HPO4\u30fb2H2O", "0.01", "G_PER_L"),
    ("N--Acetyl--D--glucosamine (Sigma)", "2", "G_PER_L"),
)

SOLUTION_1_SIGNATURE: tuple[Component, ...] = (
    ("0.1 M Tris-HCl buffer (pH 7.5)", "50.0", "ML_PER_L"),
    ("Distilled water", "260.0", "ML_PER_L"),
    ("gelrite (Gellan Gum)", "5.0", "G_PER_L"),
    ("Aged seawater", "700.0", "ML_PER_L"),
    ("Modified Hutner's basal salts", "20.0", "ML_PER_L"),
)

SOLUTION_2_SIGNATURE: tuple[Component, ...] = (
    ("Ampicillin (50 mg/ml)", "variable", "VARIABLE"),
    ("Distilled water", "variable", "VARIABLE"),
    ("Na2HPO4 x 2H2O", "variable", "VARIABLE"),
    ("N-Acetyl-D-glucosamine (Sigma)", "variable", "VARIABLE"),
    ("Vitamin solution No. 6", "variable", "VARIABLE"),
)

MODIFIED_HUTNER_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "950.0", "ML_PER_L"),
    ("Nitrilotriacetic acid", "10.0", "G_PER_L"),
    ("MgSO4 x 7H2O", "29.7", "G_PER_L"),
    ("CaCl2 x 2H2O", "3.335", "G_PER_L"),
    ("(NH4)6Mo7O24 x 4H2O", "9.25", "MG_PER_L"),
    ("FeSO4 x 7H2O", "99.0", "MG_PER_L"),
    ('Metals "44"', "50.0", "ML_PER_L"),
    ("KOH", "variable", "VARIABLE"),
    ("NaOH", "variable", "VARIABLE"),
    ("H2SO4", "variable", "VARIABLE"),
)

METALS_44_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("EDTA x 2Na", "250.0", "MG_PER_L"),
    ("ZnSO4 x 7H2O", "1095.0", "MG_PER_L"),
    ("FeSO4 x 7H2O", "500.0", "MG_PER_L"),
    ("MnSO4 x H2O", "154.0", "MG_PER_L"),
    ("CuSO4 x 5H2O", "39.2", "MG_PER_L"),
    ("Co(NO3)2 x 6H2O", "24.8", "MG_PER_L"),
    ("Na2B4O7 x 10H2O", "17.7", "MG_PER_L"),
)

VITAMIN_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("Biotin", "4.0", "MG_PER_L"),
    ("Pyridoxine HCl", "20.0", "MG_PER_L"),
    ("Thiamine HCl 2H2O", "10.0", "MG_PER_L"),
    ("Calcium pantothenate", "10.0", "MG_PER_L"),
    ("p-Aminobenzoic acid", "10.0", "MG_PER_L"),
    ("Folic acid", "4.0", "MG_PER_L"),
    ("Riboflavin", "10.0", "MG_PER_L"),
    ("Nicotinamide", "10.0", "MG_PER_L"),
    ("Vitamin B12", "0.2", "MG_PER_L"),
)

SCHEMA_INVALID_NESTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Solution 1", "1030", "ML_PER_L", SOLUTION_1_SIGNATURE),
    ("Solution 2", "0.2", "ML_PER_L", SOLUTION_2_SIGNATURE),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Solution 1", "1030", "G_PER_L", ()),
    ("Solution 2", "0.2", "G_PER_L", ()),
    ("Modified Hutner's basal salts (see Medium [M941])", "20", "G_PER_L", ()),
    ("Vitamin solution No. 6 (see Medium [M1049])", "10", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Solution 1", "1030", "ML_PER_L", SOLUTION_1_SIGNATURE),
    ("Solution 2", "0.2", "ML_PER_L", SOLUTION_2_SIGNATURE),
    ("Modified Hutner's basal salts", "20.0", "ML_PER_L", MODIFIED_HUTNER_SIGNATURE),
    ('Metals "44"', "50.0", "ML_PER_L", METALS_44_SIGNATURE),
    ("Vitamin solution No. 6", "variable", "VARIABLE", VITAMIN_SOLUTION_SIGNATURE),
)

REFERENCES = (TOGO_M1050, JCM_995, TOGO_M1049, TOGO_M941, JCM_900, TOGO_M140, JCM_149)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)6Mo7O24 x 4H2O": (
        "CHEBI:86244",
        "hexaammonium heptamolybdate tetrahydrate",
    ),
    "Ampicillin (50 mg/ml)": ("CHEBI:28971", "ampicillin"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Co(NO3)2 x 6H2O": ("CHEBI:86214", "cobalt dinitrate hexahydrate"),
    "CuSO4 x 5H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "EDTA x 2Na": ("CHEBI:64734", "EDTA disodium salt (anhydrous)"),
    "FeSO4 x 7H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "H2SO4": ("CHEBI:26836", "sulfuric acid"),
    "KOH": ("CHEBI:32035", "potassium hydroxide"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "N-Acetyl-D-glucosamine (Sigma)": ("CHEBI:506227", "N-acetyl-D-glucosamine"),
    "Na2B4O7 x 10H2O": ("CHEBI:131366", "disodium tetraborate decahydrate"),
    "Na2HPO4 x 2H2O": ("CHEBI:91258", "disodium hydrogenphosphate dihydrate"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "Nicotinamide": ("CHEBI:17154", "nicotinamide"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Thiamine HCl 2H2O": ("CHEBI:132751", "thiamine hydrochloride dihydrate"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "ZnSO4 x 7H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
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


def _absolute_component(
    preferred_term: str,
    amount: str,
    *,
    source: str,
    term: tuple[str, str] | None | bool = True,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        "variable",
        "VARIABLE",
        source=source,
        notes=f"{source} lists {amount} {preferred_term} in Solution 2.",
        term=term,
    )


def _metals_44() -> dict[str, Any]:
    return {
        "preferred_term": 'Metals "44"',
        "concentration": {"value": "50.0", "unit": "ML_PER_L"},
        "source": HUTNER_SOURCE,
        "notes": f"{HUTNER_SOURCE} adds 50.0 ml/L Metals 44 from TOGO M140.",
        "composition": [
            _listed_component("Distilled water", "1.0", "L", source=METALS_SOURCE),
            _listed_component("EDTA x 2Na", "250.0", "MG_PER_L", source=METALS_SOURCE),
            _listed_component(
                "ZnSO4 x 7H2O",
                "1095.0",
                "MG_PER_L",
                source=METALS_SOURCE,
            ),
            _listed_component(
                "FeSO4 x 7H2O",
                "500.0",
                "MG_PER_L",
                source=METALS_SOURCE,
            ),
            _listed_component(
                "MnSO4 x H2O",
                "154.0",
                "MG_PER_L",
                source=METALS_SOURCE,
                term=False,
            ),
            _listed_component(
                "CuSO4 x 5H2O",
                "39.2",
                "MG_PER_L",
                source=METALS_SOURCE,
            ),
            _listed_component(
                "Co(NO3)2 x 6H2O",
                "24.8",
                "MG_PER_L",
                source=METALS_SOURCE,
            ),
            _listed_component(
                "Na2B4O7 x 10H2O",
                "17.7",
                "MG_PER_L",
                source=METALS_SOURCE,
            ),
        ],
    }


def _modified_hutner() -> dict[str, Any]:
    return {
        "preferred_term": "Modified Hutner's basal salts",
        "concentration": {"value": "20.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            f"{SOURCE} adds 20.0 ml/L Modified Hutner's basal salts from TOGO "
            "M941."
        ),
        "composition": [
            _listed_component("Distilled water", "950.0", "ML_PER_L", source=HUTNER_SOURCE),
            _listed_component("Nitrilotriacetic acid", "10.0", "G_PER_L", source=HUTNER_SOURCE),
            _listed_component("MgSO4 x 7H2O", "29.7", "G_PER_L", source=HUTNER_SOURCE),
            _listed_component("CaCl2 x 2H2O", "3.335", "G_PER_L", source=HUTNER_SOURCE),
            _listed_component(
                "(NH4)6Mo7O24 x 4H2O",
                "9.25",
                "MG_PER_L",
                source=HUTNER_SOURCE,
            ),
            _listed_component("FeSO4 x 7H2O", "99.0", "MG_PER_L", source=HUTNER_SOURCE),
            _listed_component(
                'Metals "44"',
                "50.0",
                "ML_PER_L",
                source=HUTNER_SOURCE,
                term=False,
            ),
            _component(
                "KOH",
                "variable",
                "VARIABLE",
                source=HUTNER_SOURCE,
                notes=(
                    "TOGO M941 / JCM Medium 900 dissolves nitrilotriacetic acid "
                    "and adjusts to pH 7.0 with about 7.3 g KOH before adding "
                    "the remaining salts."
                ),
            ),
            _component(
                "NaOH",
                "variable",
                "VARIABLE",
                source=HUTNER_SOURCE,
                notes=(
                    "TOGO M941 / JCM Medium 900 readjusts Modified Hutner's "
                    "basal salts to pH 6.8 with NaOH or H2SO4 as needed."
                ),
            ),
            _component(
                "H2SO4",
                "variable",
                "VARIABLE",
                source=HUTNER_SOURCE,
                notes=(
                    "TOGO M941 / JCM Medium 900 readjusts Modified Hutner's "
                    "basal salts to pH 6.8 with NaOH or H2SO4 as needed."
                ),
            ),
        ],
        "preparation_notes": (
            "Dissolve nitrilotriacetic acid, adjust to pH 7.0 with about "
            "7.3 g KOH, add the remaining salts, then readjust to pH 6.8 "
            "with NaOH or H2SO4."
        ),
    }


def _vitamin_solution() -> dict[str, Any]:
    return {
        "preferred_term": "Vitamin solution No. 6",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": SOURCE,
        "notes": f"{SOURCE} lists 10.0 ml Vitamin solution No. 6 in Solution 2.",
        "composition": [
            _listed_component("Distilled water", "1.0", "L", source=VITAMIN_SOURCE),
            _listed_component("Biotin", "4.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Pyridoxine HCl", "20.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component(
                "Thiamine HCl 2H2O",
                "10.0",
                "MG_PER_L",
                source=VITAMIN_SOURCE,
            ),
            _listed_component(
                "Calcium pantothenate",
                "10.0",
                "MG_PER_L",
                source=VITAMIN_SOURCE,
            ),
            _listed_component(
                "p-Aminobenzoic acid",
                "10.0",
                "MG_PER_L",
                source=VITAMIN_SOURCE,
            ),
            _listed_component("Folic acid", "4.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Riboflavin", "10.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Nicotinamide", "10.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Vitamin B12", "0.2", "MG_PER_L", source=VITAMIN_SOURCE),
        ],
        "preparation_notes": "Filter-sterilize.",
    }


SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Solution 1",
        "concentration": {"value": "1030", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            f"{SOURCE} combines 1030 ml Solution 1 with 0.2 ml "
            "filter-sterilized Solution 2."
        ),
        "composition": [
            _listed_component(
                "0.1 M Tris-HCl buffer (pH 7.5)",
                "50.0",
                "ML_PER_L",
                source=SOURCE,
                term=False,
            ),
            _listed_component("Distilled water", "260.0", "ML_PER_L", source=SOURCE),
            _listed_component(
                "gelrite (Gellan Gum)",
                "5.0",
                "G_PER_L",
                source=SOURCE,
                term=False,
            ),
            _listed_component(
                "Aged seawater",
                "700.0",
                "ML_PER_L",
                source=SOURCE,
                term=False,
            ),
            _component(
                "Modified Hutner's basal salts",
                "20.0",
                "ML_PER_L",
                source=SOURCE,
                notes=(
                    f"{SOURCE} adds 20.0 ml/L Modified Hutner's basal salts "
                    "from TOGO M941."
                ),
                term=False,
            ),
        ],
    },
    {
        "preferred_term": "Solution 2",
        "concentration": {"value": "0.2", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds 0.2 ml filter-sterilized Solution 2 to Solution 1.",
        "composition": [
            _absolute_component("Ampicillin (50 mg/ml)", "4.0 ml", source=SOURCE),
            _absolute_component("Distilled water", "40.0 ml", source=SOURCE),
            _absolute_component("Na2HPO4 x 2H2O", "0.01 g", source=SOURCE),
            _absolute_component(
                "N-Acetyl-D-glucosamine (Sigma)",
                "2.0 g",
                source=SOURCE,
            ),
            _absolute_component("Vitamin solution No. 6", "10.0 ml", source=SOURCE),
        ],
        "preparation_notes": "Filter-sterilize Solution 2 before adding it to Solution 1.",
    },
    _modified_hutner(),
    _metals_44(),
    _vitamin_solution(),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare Solution 1 from Tris-HCl buffer, distilled water, "
            "gelrite, aged seawater, and Modified Hutner's basal salts."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Prepare Solution 2 from 50 mg/ml Ampicillin, distilled water, "
            "Na2HPO4 x 2H2O, N-Acetyl-D-glucosamine, and Vitamin solution "
            "No. 6."
        ),
    },
    {
        "step_number": 3,
        "action": "FILTER_STERILIZE",
        "description": "Filter-sterilize Solution 2.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": "Add 0.2 ml filter-sterilized Solution 2 to Solution 1.",
    },
)

NOTES = (
    "TOGO M1050 records the solid JCM Medium 995 M30 variant: 1030 ml "
    "Solution 1 plus 0.2 ml filter-sterilized Solution 2. Solution 1 "
    "contains 5 g/L gelrite, aged seawater, Tris-HCl buffer, distilled "
    "water, and Modified Hutner's basal salts from M941/JCM 900; Solution 2 "
    "contains 50 mg/ml Ampicillin, Na2HPO4 x 2H2O, "
    "N-Acetyl-D-glucosamine, and Vitamin solution No. 6 from M1049/JCM 995."
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
        SCHEMA_INVALID_NESTED_SOLUTION_SIGNATURES,
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
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
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
