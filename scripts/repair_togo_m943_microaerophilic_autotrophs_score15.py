#!/usr/bin/env python3
"""Repair MediaDive/TOGO JCM 902 MJ Medium for Microaerophilic Autotrophs."""

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
MEDIADIVE_J902_PATH = Path("bacterial/mj_medium_for_microaerophilic_autotrophs.yaml")
TOGO_M943_PATH = Path("bacterial/TOGO_M943_MJ_Medium_For_Microaerophilic_Autotrophs.yaml")
MAIN_HELPER_PATH = Path("bacterial/mediadive_4901_Main_sol_J902.yaml")
MJ_BASAL_PATH = Path("bacterial/mj_basal_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m943_microaerophilic_autotrophs_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J902 = "https://mediadive.dsmz.de/medium/J902"
JCM_902 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=902"
TOGO_M943 = "https://togomedium.org/medium/M943"
TOGO_M260 = "https://togomedium.org/medium/M260"
TOGO_M190 = "https://togomedium.org/medium/M190"

SOURCE_TOGO = "TOGO M943 / JCM Medium 902"
SOURCE_MEDIADIVE = "MediaDive J902 / JCM Medium 902"
SOURCE_MJ_N = "TOGO M260 / JCM Medium 268"
SOURCE_VITAMINS = "TOGO M190 / JCM Medium 197"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


MEDIADIVE_FLATTENED_INGREDIENTS: tuple[Component, ...] = (
    ("NH4Cl", "0.242718", "G_PER_L"),
    ("NaHCO3", "5", "G_PER_L"),
    ("Na2S2O3 x 5 H2O", "15", "G_PER_L"),
    ("NaCl", "29.703", "G_PER_L"),
    ("K2HPO4", "0.138614", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.138614", "G_PER_L"),
    ("MgSO4 x 7 H2O", "3.36634", "G_PER_L"),
    ("MgCl2 x 6 H2O", "4.13861", "G_PER_L"),
    ("KCl", "0.326733", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.00049505", "G_PER_L"),
    ("Na2SeO3 x 5 H2O", "0.00049505", "G_PER_L"),
    ("Fe(NH4)2(SO4)2 x 6 H2O", "0.00990099", "G_PER_L"),
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
)

TOGO_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("NH4Cl", "0.25", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Oxygen gas", "variable", "VARIABLE"),
)

FINAL_INGREDIENTS: tuple[Component, ...] = (
    ("NH4Cl", "0.25", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Oxygen gas", "variable", "VARIABLE"),
)

TOGO_IMPORTED_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("MJ(-N) synthetic seawater (see Medium [M260])", "1", "G_PER_L", ()),
    ("8% NaHCO3 solution", "5", "G_PER_L", ()),
    ("10% Na2S2O3・5H2O solution", "15", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
)

MEDIADIVE_HELPER_IMPORTED_COMPOSITION: tuple[Component, ...] = (
    ("NH4Cl", "0.242718", "G_PER_L"),
    ("NaHCO3", "4.854368932038835", "PERCENT_V_V"),
    ("Na2S2O3 x 5 H2O", "14.563106796116505", "PERCENT_V_V"),
)

MJ_N_COMPOSITION: tuple[Component, ...] = (
    ("NaCl", "30.0", "G_PER_L"),
    ("K2HPO4", "0.14", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.14", "G_PER_L"),
    ("MgSO4 x 7 H2O", "3.4", "G_PER_L"),
    ("MgCl2 x 6 H2O", "4.18", "G_PER_L"),
    ("KCl", "0.33", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.5", "MG_PER_L"),
    ("Na2SeO3 x 5 H2O", "0.5", "MG_PER_L"),
    ("Fe(NH4)2(SO4)2 x 6 H2O", "0.01", "G_PER_L"),
    ("Trace minerals", "10.0", "ML_PER_L"),
    ("Distilled water", "1.0", "L"),
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
    ("MJ(-N) synthetic seawater", "1000.0", "ML_PER_L", MJ_N_COMPOSITION),
    ("8% NaHCO3 solution", "5.0", "ML_PER_L", (("NaHCO3", "8.0", "PERCENT_W_V"),)),
    (
        "10% Na2S2O3 x 5 H2O solution",
        "15.0",
        "ML_PER_L",
        (("Na2S2O3 x 5 H2O", "10.0", "PERCENT_W_V"),),
    ),
    ("Trace vitamins", "10.0", "ML_PER_L", TRACE_VITAMIN_COMPOSITION),
)

PLACEHOLDER_INGREDIENTS: tuple[Component, ...] = (
    ("See source for composition", "variable", "VARIABLE"),
)

MJ_MEDIUM_CHILD = {
    "path": f"data/normalized_yaml/{MEDIADIVE_J902_PATH}",
    "relationship": "CONCENTRATION_VARIANT",
    "id": "CultureMech:003251",
    "name": "mj_medium_for_microaerophilic_autotrophs",
    "notes": (
        "Reviewed MJ basal/autotroph pair; child keeps the marine salt, trace "
        "metal, and vitamin base unchanged but raises NaHCO3 from 1.4985 to 5 "
        "g/L and Na2S2O3 x 5 H2O from 1.4985 to 15 g/L, with pH 5.5 recorded "
        "in the child."
    ),
}

M943_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M943_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010366",
    "name": "mj_medium_for_microaerophilic_autotrophs",
    "notes": (
        "TOGO M943 imports the same JCM Medium 902 MJ Medium for "
        "Microaerophilic Autotrophs formulation represented by MediaDive J902."
    ),
}

J902_PARENT = {
    "path": f"data/normalized_yaml/{MEDIADIVE_J902_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003251",
    "name": "mj_medium_for_microaerophilic_autotrophs",
    "notes": M943_CHILD["notes"],
}

SOURCE_NOTE = (
    "JCM Medium 902, MediaDive J902, and TOGO M943 describe MJ Medium for "
    "Microaerophilic Autotrophs as 0.25 g/L NH4Cl in 1.0 L MJ(-N) synthetic "
    "seawater from TOGO M260/JCM Medium 268; after pH 5.5 adjustment, "
    "autoclaving, and cooling, 5.0 ml/L 8% NaHCO3 solution, 15.0 ml/L 10% "
    "Na2S2O3 x 5 H2O solution, and 10.0 ml/L Trace vitamins from TOGO M190/JCM "
    "Medium 197 are added aseptically and the medium is sealed under an "
    "N2-CO2-O2 (76:19:5, v/v) gas mixture at 50 kPa."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Mix NH4Cl with 1.0 L MJ(-N) synthetic seawater.",
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust to pH 5.5 and autoclave.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "After cooling, aseptically add filter-sterilized 5.0 ml/L 8% "
            "NaHCO3 solution, 15.0 ml/L 10% Na2S2O3 x 5 H2O solution, and "
            "10.0 ml/L Trace vitamins."
        ),
    },
    {
        "step_number": 4,
        "action": "ALIQUOT",
        "description": (
            "Distribute under an N2-CO2-O2 (76:19:5, v/v) gas mixture, seal "
            "with butyl rubber stoppers, and pressurize to 50 kPa with the "
            "same gas mixture."
        ),
    },
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Fe(NH4)2(SO4)2 x 6 H2O": (
        "CHEBI:76181",
        "ferrous ammonium sulfate hexahydrate",
    ),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "MgCl2 x 6 H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Na2S2O3 x 5 H2O": ("CHEBI:32150", "sodium thiosulfate pentahydrate"),
    "Na2SeO3 x 5 H2O": ("CHEBI:131361", "disodium selenite pentahydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "NiCl2 x 6 H2O": ("CHEBI:34887", "nickel dichloride"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "Oxygen gas": ("CHEBI:15379", "dioxygen"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine hydrochloride": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Biotin": ("VITAMIN_SOURCE",),
    "Calcium pantothenate": ("VITAMIN_SOURCE",),
    "Folic acid": ("VITAMIN_SOURCE",),
    "Fe(NH4)2(SO4)2 x 6 H2O": (
        "IRON_SOURCE",
        "NITROGEN_SOURCE",
        "SULFUR_SOURCE",
        "TRACE_ELEMENT",
    ),
    "Lipoic acid": ("VITAMIN_SOURCE",),
    "NH4Cl": ("NITROGEN_SOURCE",),
    "Na2S2O3 x 5 H2O": ("SULFUR_SOURCE",),
    "NiCl2 x 6 H2O": ("TRACE_ELEMENT",),
    "Na2SeO3 x 5 H2O": ("TRACE_ELEMENT",),
    "Nicotinic acid": ("VITAMIN_SOURCE",),
    "p-Aminobenzoic acid": ("VITAMIN_SOURCE",),
    "Pyridoxine hydrochloride": ("VITAMIN_SOURCE",),
    "Riboflavin": ("VITAMIN_SOURCE",),
    "Thiamine HCl": ("VITAMIN_SOURCE",),
    "Vitamin B12": ("VITAMIN_SOURCE",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "K2HPO4": ("BUFFER",),
    "NaHCO3": ("BUFFER",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
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
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }

    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
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


def _ingredients(source: str) -> list[dict[str, Any]]:
    gas_note = f"{source} uses {{gas}} in an N2-CO2-O2 (76:19:5, v/v) gas mixture."
    return [
        _component("NH4Cl", "0.25", "G_PER_L", source=source),
        _component(
            "Carbon dioxide gas",
            "variable",
            "VARIABLE",
            source=source,
            notes=gas_note.format(gas="Carbon dioxide gas"),
        ),
        _component(
            "Nitrogen gas",
            "variable",
            "VARIABLE",
            source=source,
            notes=gas_note.format(gas="Nitrogen gas"),
        ),
        _component(
            "Oxygen gas",
            "variable",
            "VARIABLE",
            source=source,
            notes=gas_note.format(gas="Oxygen gas"),
        ),
    ]


def _mj_n_synthetic_seawater(source: str) -> dict[str, Any]:
    return {
        "preferred_term": "MJ(-N) synthetic seawater",
        "concentration": {"value": "1000.0", "unit": "ML_PER_L"},
        "source": source,
        "notes": (
            f"{source} adds 1.0 L MJ(-N) synthetic seawater from TOGO M260/" "JCM Medium 268."
        ),
        "composition": [
            _component("NaCl", "30.0", "G_PER_L", source=SOURCE_MJ_N),
            _component("K2HPO4", "0.14", "G_PER_L", source=SOURCE_MJ_N),
            _component("CaCl2 x 2 H2O", "0.14", "G_PER_L", source=SOURCE_MJ_N),
            _component("MgSO4 x 7 H2O", "3.4", "G_PER_L", source=SOURCE_MJ_N),
            _component("MgCl2 x 6 H2O", "4.18", "G_PER_L", source=SOURCE_MJ_N),
            _component("KCl", "0.33", "G_PER_L", source=SOURCE_MJ_N),
            _component("NiCl2 x 6 H2O", "0.5", "MG_PER_L", source=SOURCE_MJ_N),
            _component("Na2SeO3 x 5 H2O", "0.5", "MG_PER_L", source=SOURCE_MJ_N),
            _component(
                "Fe(NH4)2(SO4)2 x 6 H2O",
                "0.01",
                "G_PER_L",
                source=SOURCE_MJ_N,
            ),
            _component(
                "Trace minerals",
                "10.0",
                "ML_PER_L",
                source=SOURCE_MJ_N,
                notes=("TOGO M260/JCM Medium 268 adds 10.0 ml/L Trace minerals " "from TOGO M142."),
            ),
            _component(
                "Distilled water",
                "1.0",
                "L",
                source=SOURCE_MJ_N,
                notes="TOGO M260/JCM Medium 268 lists 1.0 L Distilled water.",
            ),
        ],
        "preparation_notes": "Adjust pH to 7.5.",
    }


def _trace_vitamins(source: str) -> dict[str, Any]:
    return {
        "preferred_term": "Trace vitamins",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": source,
        "notes": (
            f"{source} adds 10.0 ml/L Trace vitamins from TOGO M190/JCM "
            "Medium 197 after cooling."
        ),
        "composition": [
            _component(name, value, unit, source=SOURCE_VITAMINS)
            for name, value, unit in TRACE_VITAMIN_COMPOSITION
        ],
        "preparation_notes": "Filter-sterilize.",
    }


def _solutions(source: str) -> list[dict[str, Any]]:
    return [
        _mj_n_synthetic_seawater(source),
        {
            "preferred_term": "8% NaHCO3 solution",
            "concentration": {"value": "5.0", "unit": "ML_PER_L"},
            "source": source,
            "notes": f"{source} adds 5.0 ml/L 8% NaHCO3 solution after cooling.",
            "term": _term(*GROUNDINGS["NaHCO3"]),
            "mediaingredientmech_chebi_term": _term(*GROUNDINGS["NaHCO3"]),
            "composition": [
                _component(
                    "NaHCO3",
                    "8.0",
                    "PERCENT_W_V",
                    source=source,
                    notes=f"{source} specifies the added NaHCO3 solution as 8% w/v.",
                )
            ],
            "preparation_notes": "Filter-sterilize.",
        },
        {
            "preferred_term": "10% Na2S2O3 x 5 H2O solution",
            "concentration": {"value": "15.0", "unit": "ML_PER_L"},
            "source": source,
            "notes": (f"{source} adds 15.0 ml/L 10% Na2S2O3 x 5 H2O solution " "after cooling."),
            "term": _term(*GROUNDINGS["Na2S2O3 x 5 H2O"]),
            "mediaingredientmech_chebi_term": _term(*GROUNDINGS["Na2S2O3 x 5 H2O"]),
            "composition": [
                _component(
                    "Na2S2O3 x 5 H2O",
                    "10.0",
                    "PERCENT_W_V",
                    source=source,
                    notes=(f"{source} specifies the added Na2S2O3 x 5 H2O " "solution as 10% w/v."),
                )
            ],
            "preparation_notes": "Filter-sterilize.",
        },
        _trace_vitamins(source),
    ]


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
    solutions = doc.get("solutions")
    if solutions is None:
        solutions = []
    if not isinstance(solutions, (list, tuple)):
        raise ValueError("solutions is not a list")
    signatures: list[SolutionSignature] = []
    for solution in solutions:
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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation", "resolved_reference"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


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


def _ensure_mediadive_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:003251":
        raise ValueError(
            f"{MEDIADIVE_J902_PATH}: expected id CultureMech:003251, " f"found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != "mediadive.medium:J902":
        raise ValueError(f"{MEDIADIVE_J902_PATH}: expected media term J902")

    ingredient_signature = _signature(doc.get("ingredients"), "J902 ingredients")
    if ingredient_signature not in (MEDIADIVE_FLATTENED_INGREDIENTS, FINAL_INGREDIENTS):
        raise ValueError(f"{MEDIADIVE_J902_PATH}: ingredient signature drifted")

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in ((), FINAL_SOLUTIONS):
        raise ValueError(f"{MEDIADIVE_J902_PATH}: solution signature drifted")


def _ensure_togo_m943(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:010366":
        raise ValueError(
            f"{TOGO_M943_PATH}: expected id CultureMech:010366, " f"found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != "TOGO:M943":
        raise ValueError(f"{TOGO_M943_PATH}: expected media term TOGO:M943")

    ingredient_signature = _signature(doc.get("ingredients"), "M943 ingredients")
    if ingredient_signature not in (TOGO_IMPORTED_INGREDIENTS, FINAL_INGREDIENTS):
        raise ValueError(f"{TOGO_M943_PATH}: ingredient signature drifted")

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (TOGO_IMPORTED_SOLUTIONS, FINAL_SOLUTIONS):
        raise ValueError(f"{TOGO_M943_PATH}: solution signature drifted")


def _ensure_main_helper(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:013830":
        raise ValueError(
            f"{MAIN_HELPER_PATH}: expected id CultureMech:013830, " f"found {doc.get('id')!r}"
        )
    term = doc.get("term")
    if not isinstance(term, dict) or term.get("id") != "mediadive.solution:4901":
        raise ValueError(f"{MAIN_HELPER_PATH}: expected mediadive solution 4901")

    composition_signature = _signature(
        doc.get("composition"),
        "MediaDive 4901 composition",
    )
    if composition_signature not in (
        MEDIADIVE_HELPER_IMPORTED_COMPOSITION,
        (FINAL_INGREDIENTS[0],),
    ):
        raise ValueError(f"{MAIN_HELPER_PATH}: composition signature drifted")

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in ((), FINAL_SOLUTIONS):
        raise ValueError(f"{MAIN_HELPER_PATH}: solution signature drifted")

    ingredient_signature = _signature(doc.get("ingredients"), "MediaDive 4901 ingredients")
    if ingredient_signature not in (PLACEHOLDER_INGREDIENTS, ()):
        raise ValueError(f"{MAIN_HELPER_PATH}: placeholder signature drifted")


def _ensure_mj_basal(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:002716":
        raise ValueError(
            f"{MJ_BASAL_PATH}: expected id CultureMech:002716, " f"found {doc.get('id')!r}"
        )

    children = doc.get("variant_children")
    if children is None:
        return
    if not isinstance(children, list):
        raise ValueError(f"{MJ_BASAL_PATH}: variant_children is not a list")
    for child in children:
        if not isinstance(child, dict):
            raise ValueError(f"{MJ_BASAL_PATH}: variant_children contains non-mapping")


def _apply_common_medium_fields(
    repaired: dict[str, Any],
    *,
    source: str,
) -> None:
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 5.5, "physical_state")
    repaired["ingredients"] = _ingredients(source)
    _put_after(repaired, "solutions", _solutions(source), "ingredients")
    _put_after(repaired, "notes", SOURCE_NOTE, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "solutions",
    )
    repaired["incubation_atmosphere"] = "MICROAEROPHILIC"
    repaired["aeration"] = "N2-CO2-O2 (76:19:5, v/v) gas atmosphere, 50 kPa"
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)


def repair_mediadive_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_mediadive_parent(doc)

    references = (MEDIADIVE_J902, JCM_902, TOGO_M260, TOGO_M190)
    repaired = copy.deepcopy(doc)
    _apply_common_medium_fields(repaired, source=SOURCE_MEDIADIVE)
    repaired["variant_children"] = [copy.deepcopy(M943_CHILD)]
    repaired.pop("parent_media", None)
    repaired.pop("variant_relationship", None)
    repaired.pop("variant_modifications", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, references)
    _append_event(
        repaired,
        action="RESOLVED_MEDIADIVE_J902_MICROAEROPHILIC_AUTOTROPHS",
        references=references,
        notes=(
            "Replaced MediaDive final-volume flattening of MJ(-N) synthetic "
            "seawater, NaHCO3, Na2S2O3 x 5 H2O, and Trace vitamins with the "
            "nested JCM Medium 902 stock formulation and linked TOGO M943 as "
            "a source duplicate."
        ),
    )
    return repaired


def repair_togo_m943(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_togo_m943(doc)

    references = (TOGO_M943, JCM_902, TOGO_M260, TOGO_M190, MEDIADIVE_J902)
    repaired = copy.deepcopy(doc)
    _apply_common_medium_fields(repaired, source=SOURCE_TOGO)
    _put_after(repaired, "parent_media", copy.deepcopy(J902_PARENT), "references")
    _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        [M943_CHILD["notes"]],
        "variant_relationship",
    )
    repaired.pop("variant_children", None)
    repaired.pop("kg_microbe_match", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, references)
    _append_event(
        repaired,
        action="RESOLVED_TOGO_M943_MICROAEROPHILIC_AUTOTROPHS",
        references=references,
        notes=(
            "Moved MJ(-N) synthetic seawater, 8% NaHCO3, 10% Na2S2O3 x 5 H2O, "
            "and Trace vitamins from empty solution stubs into structured "
            "solution entries, corrected their ml/L addition volumes, added "
            "pH 5.5 and microaerophilic gas handling, grounded Oxygen gas, "
            "and removed the stale MediaDive J780 match."
        ),
    )
    return repaired


def repair_main_helper(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_main_helper(doc)

    references = (MEDIADIVE_J902, JCM_902, TOGO_M260, TOGO_M190)
    repaired = copy.deepcopy(doc)
    repaired["composition"] = [
        _component("NH4Cl", "0.25", "G_PER_L", source=SOURCE_MEDIADIVE),
    ]
    repaired["solutions"] = _solutions(SOURCE_MEDIADIVE)
    repaired.pop("ingredients", None)
    repaired["preparation_notes"] = " ".join(str(step["description"]) for step in PREPARATION_STEPS)
    repaired["category"] = "bacterial"
    repaired["notes"] = (
        "MediaDive solution 4901 is the JCM Medium 902 main-solution import "
        "for MJ Medium for Microaerophilic Autotrophs."
    )
    _ensure_flags(repaired)
    _ensure_references(repaired, references)
    _append_event(
        repaired,
        action="RESOLVED_MEDIADIVE_4901_MAIN_SOL_J902",
        references=references,
        notes=(
            "Replaced flattened final-volume composition rows and the "
            "placeholder top-level ingredient with the JCM Medium 902 "
            "main-solution recipe."
        ),
    )
    return repaired


def repair_mj_basal(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_mj_basal(doc)

    repaired = copy.deepcopy(doc)
    children = repaired.get("variant_children")
    if isinstance(children, list):
        repaired["variant_children"] = [child for child in children if child != MJ_MEDIUM_CHILD]
        if not repaired["variant_children"]:
            repaired.pop("variant_children", None)

    _append_event(
        repaired,
        action="REMOVED_STALE_J902_VARIANT_EDGE",
        references=(MEDIADIVE_J902, JCM_902),
        notes=(
            "Removed the MJ Medium for Microaerophilic Autotrophs child edge "
            "because it was based on MediaDive's flattened bicarbonate and "
            "thiosulfate stock volumes, not on the nested JCM Medium 902 "
            "source recipe."
        ),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized
        / MEDIADIVE_J902_PATH: repair_mediadive_parent(_load(normalized / MEDIADIVE_J902_PATH)),
        normalized / TOGO_M943_PATH: repair_togo_m943(_load(normalized / TOGO_M943_PATH)),
        normalized / MAIN_HELPER_PATH: repair_main_helper(_load(normalized / MAIN_HELPER_PATH)),
        normalized / MJ_BASAL_PATH: repair_mj_basal(_load(normalized / MJ_BASAL_PATH)),
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
    print(f"\n{verb} {changed_count} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
