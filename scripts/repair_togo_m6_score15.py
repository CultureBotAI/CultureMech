#!/usr/bin/env python3
"""Repair JCM/TOGO BL Agar records around TOGO M6."""

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
JCM_J13_PATH = Path("bacterial/bl_agar_glucose_blood_liver_agar.yaml")
TOGO_M6_PATH = Path("bacterial/TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml")
BACTERIAL_MALTOSE_PATH = Path("bacterial/bl_with_0_5_maltose.yaml")
FUNGAL_MALTOSE_PATH = Path("fungal/bl_with_0_5_maltose.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m6_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M6 = "https://togomedium.org/medium/M6"
TOGO_M416 = "https://togomedium.org/medium/M416"
JCM_13 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=13"
JCM_418 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=418"
MEDIADIVE_J13 = "https://mediadive.dsmz.de/medium/J13"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class AgarTarget:
    path: Path
    record_id: str
    source_term: str
    imported_ingredients: tuple[Component, ...]
    imported_solutions: tuple[Component, ...]
    source: str
    action: str
    event_notes: str
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, Any], ...] = ()


@dataclass(frozen=True)
class MaltoseTarget:
    path: Path
    record_id: str
    source_term: str
    action: str
    references: tuple[str, ...]


JCM_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Lab-Lemco beef extract", "2.85714", "G_PER_L"),
    ("Proteose peptone no. 3", "9.52381", "G_PER_L"),
    ("Trypticase peptone", "4.7619", "G_PER_L"),
    ("Phytone peptone", "2.85714", "G_PER_L"),
    ("Yeast extract", "4.7619", "G_PER_L"),
    ("Liver extract", "150", "G_PER_L"),
    ("Glucose", "9.52381", "G_PER_L"),
    ("Starch", "0.47619", "G_PER_L"),
    ("Tween 80", "0.952381", "G_PER_L"),
    ("Agar", "14.2857", "G_PER_L"),
    ("L-Cysteine HCl x H2O", "10", "G_PER_L"),
    ("Horse blood", "50", "G_PER_L"),
    ("K2HPO4", "100", "G_PER_L"),
    ("KH2PO4", "100", "G_PER_L"),
    ("MgSO4 x 7 H2O", "40", "G_PER_L"),
    ("NaCl", "2", "G_PER_L"),
    ("FeSO4 x 7 H2O", "2", "G_PER_L"),
    ("MnSO4 x n H2O", "2", "G_PER_L"),
)

TOGO_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "1025.0", "G_PER_L"),
    ("Tween 80", "1", "G_PER_L"),
    ("Horse blood", "50", "G_PER_L"),
    ("Glucose", "10", "G_PER_L"),
    ("Soluble starch", "0.5", "G_PER_L"),
    ("Bacto agar (BD-Difco)", "15", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "5", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "5", "G_PER_L"),
    ("Proteose peptone No. 3 (BD-Difco)", "10", "G_PER_L"),
    ("Phytone peptone (BD-BBL)", "3", "G_PER_L"),
    ("Lab--Lemco powder (Oxoid)", "3", "G_PER_L"),
    ("Liver extract (see below)", "150", "G_PER_L"),
    ("water", "170", "G_PER_L"),
    ("liver powder", "10", "G_PER_L"),
    ("KH2PO4", "10", "G_PER_L"),
    ("K2HPO4", "10", "G_PER_L"),
    ("MgSO4\u30fb7H2O", "4", "G_PER_L"),
    ("NaCl", "0.2", "G_PER_L"),
    ("FeSO4\u30fb7H2O", "0.2", "G_PER_L"),
    ("MnSO4\u30fbxH2O", "0.2", "G_PER_L"),
)

TOGO_IMPORTED_SOLUTIONS: tuple[Component, ...] = (
    ("5% L--Cysteine\u30fbHCl\u30fbH2O solution", "10", "G_PER_L"),
    ("Solution A (see below)", "10", "G_PER_L"),
    ("Solution B (see below)", "5", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Lab-Lemco powder (Oxoid)", "3.0", "G_PER_L"),
    ("Proteose peptone No. 3 (BD-Difco)", "10.0", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "5.0", "G_PER_L"),
    ("Phytone peptone (BD-BBL)", "3.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "5.0", "G_PER_L"),
    ("Glucose", "10.0", "G_PER_L"),
    ("Soluble starch", "0.5", "G_PER_L"),
    ("Tween 80", "1.0", "G_PER_L"),
    ("Bacto agar (BD-Difco)", "15.0", "G_PER_L"),
    ("Horse blood", "50.0", "ML_PER_L"),
    ("Distilled water", "825.0", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Liver extract", "150.0", "ML_PER_L"),
    ("Solution A", "10.0", "ML_PER_L"),
    ("Solution B", "5.0", "ML_PER_L"),
    ("5% L-Cysteine HCl x H2O solution", "10.0", "ML_PER_L"),
)

MALTOSE_INGREDIENT_SIGNATURE: tuple[Component, ...] = (("Maltose", "5.0", "G_PER_L"),)
MALTOSE_SOLUTION_SIGNATURE: tuple[Component, ...] = (("BL Agar", "1000", "ML_PER_L"),)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Lab-Lemco powder (Oxoid)": ("FOODON:03302088", "beef extract"),
    "Proteose peptone No. 3 (BD-Difco)": ("MICRO:0000180", "proteose peptone"),
    "Trypticase peptone (BD-BBL)": ("MICRO:0000175", "Trypticase peptone"),
    "Phytone peptone (BD-BBL)": ("MICRO:0000178", "peptone"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "yeast extract"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Soluble starch": ("CHEBI:28017", "starch"),
    "Tween 80": ("CHEBI:53426", "polysorbate 80"),
    "Bacto agar (BD-Difco)": ("CHEBI:2509", "agar"),
    "Horse blood": ("UBERON:0000178", "blood"),
    "Distilled water": ("CHEBI:15377", "water"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "L-Cysteine HCl x H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Lab-Lemco powder (Oxoid)": ("NITROGEN_SOURCE",),
    "Proteose peptone No. 3 (BD-Difco)": ("NITROGEN_SOURCE",),
    "Trypticase peptone (BD-BBL)": ("NITROGEN_SOURCE",),
    "Phytone peptone (BD-BBL)": ("NITROGEN_SOURCE",),
    "Yeast extract (BD-Difco)": ("NITROGEN_SOURCE",),
    "Glucose": ("CARBON_SOURCE",),
    "Soluble starch": ("CARBON_SOURCE",),
    "K2HPO4": ("PHOSPHATE_SOURCE",),
    "KH2PO4": ("PHOSPHATE_SOURCE",),
    "MgSO4 x 7 H2O": ("SULFUR_SOURCE", "TRACE_ELEMENT"),
    "FeSO4 x 7 H2O": ("IRON_SOURCE", "SULFUR_SOURCE", "TRACE_ELEMENT"),
    "MnSO4 x n H2O": ("TRACE_ELEMENT",),
    "L-Cysteine HCl x H2O": ("AMINO_ACID_SOURCE", "SULFUR_SOURCE"),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Tween 80": ("SURFACTANT",),
    "K2HPO4": ("BUFFER",),
    "KH2PO4": ("BUFFER",),
    "L-Cysteine HCl x H2O": ("REDUCING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
    "L": "L",
}

M6_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M6_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010107",
    "name": "bl_agar_glucose_blood_liver_agar",
    "notes": "TOGO M6 imports the same JCM Medium 13 BL Agar formulation.",
}

BACTERIAL_MALTOSE_CHILD = {
    "path": f"data/normalized_yaml/{BACTERIAL_MALTOSE_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:009801",
    "name": "bl_with_0_5_maltose",
    "notes": "Supplements 1.0 L BL Agar with 5.0 g/L maltose.",
}

FUNGAL_MALTOSE_CHILD = {
    "path": f"data/normalized_yaml/{FUNGAL_MALTOSE_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:010526",
    "name": "bl_with_0_5_maltose",
    "notes": "Supplements 1.0 L BL Agar with 5.0 g/L maltose.",
}

JCM_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J13_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:002499",
    "name": "bl_agar_glucose_blood_liver_agar",
    "notes": "TOGO M6 imports the same JCM Medium 13 BL Agar formulation.",
}

JCM_SUPPLEMENT_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J13_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:002499",
    "name": "bl_agar_glucose_blood_liver_agar",
    "notes": "Supplements 1.0 L BL Agar with 5.0 g/L maltose.",
}

BL_AGAR_JCM_TERM = {
    "id": "CultureMech:002499",
    "label": "BL Agar (Glucose Blood Liver Agar)",
}

SOURCE_NOTE = (
    "JCM Medium 13 BL Agar lists Lab-Lemco powder, three peptone products, "
    "yeast extract, liver extract, glucose, soluble starch, Solution A, "
    "Solution B, Tween 80, agar, 5% L-Cysteine HCl x H2O solution, horse "
    "blood, and distilled water; the formula is adjusted to pH 7.2 and "
    "horse blood is added aseptically after autoclaving and cooling."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare Liver extract by putting 10.0 g liver powder in 170.0 ml "
            "water, holding at 50-60 C for 1 hr, boiling for 5 min, adjusting "
            "pH to 7.2, and filtering."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Combine the base ingredients, 150.0 ml/L Liver extract, "
            "10.0 ml/L Solution A, 5.0 ml/L Solution B, 10.0 ml/L 5% "
            "L-Cysteine HCl x H2O solution, and 825.0 ml/L distilled water; "
            "omit horse blood before autoclaving."
        ),
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.2 before autoclaving.",
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C for 15 min.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": "Cool to 50 C and aseptically add 50.0 ml/L horse blood.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
}

M6_VARIANT_MODIFICATION = (
    "Same JCM Medium 13 BL Agar formulation as the MediaDive J13 source record."
)

AGAR_TARGETS: tuple[AgarTarget, ...] = (
    AgarTarget(
        path=JCM_J13_PATH,
        record_id="CultureMech:002499",
        source_term="mediadive.medium:J13",
        imported_ingredients=JCM_IMPORTED_INGREDIENTS,
        imported_solutions=(),
        source="MediaDive J13 / JCM Medium 13",
        action="RESOLVED_JCM_13_BL_AGAR",
        event_notes=(
            "Restored JCM Medium 13 direct ingredients, moved Liver extract, "
            "Solution A, Solution B, and the 5% L-Cysteine HCl x H2O solution "
            "from flattened top-level rows into solution entries, grounded "
            "source-disclosed components, and linked TOGO M6 plus the two "
            "BL With 0.5% Maltose children."
        ),
        references=(JCM_13, MEDIADIVE_J13),
        variant_children=(M6_CHILD, BACTERIAL_MALTOSE_CHILD, FUNGAL_MALTOSE_CHILD),
    ),
    AgarTarget(
        path=TOGO_M6_PATH,
        record_id="CultureMech:010107",
        source_term="TOGO:M6",
        imported_ingredients=TOGO_IMPORTED_INGREDIENTS,
        imported_solutions=TOGO_IMPORTED_SOLUTIONS,
        source="TOGO M6 / JCM Medium 13",
        action="RESOLVED_TOGO_M6_BL_AGAR",
        event_notes=(
            "Restored JCM Medium 13 direct ingredients, split merged stock and "
            "subrecipe components into Liver extract, Solution A, Solution B, "
            "and 5% L-Cysteine HCl x H2O solution entries, corrected ml "
            "addition units, added pH 7.2 and JCM's default autoclaving "
            "condition, and linked the MediaDive J13 source duplicate."
        ),
        references=(TOGO_M6, JCM_13, MEDIADIVE_J13),
        parent_media=JCM_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(M6_VARIANT_MODIFICATION,),
    ),
)

MALTOSE_TARGETS: tuple[MaltoseTarget, ...] = (
    MaltoseTarget(
        path=BACTERIAL_MALTOSE_PATH,
        record_id="CultureMech:009801",
        source_term="TOGO:M416",
        action="RELINKED_TOGO_M416_TO_JCM_13",
        references=(TOGO_M416, JCM_418, TOGO_M6, JCM_13),
    ),
    MaltoseTarget(
        path=FUNGAL_MALTOSE_PATH,
        record_id="CultureMech:010526",
        source_term="mediadive.medium:J418",
        action="RELINKED_JCM_418_TO_JCM_13",
        references=(JCM_418, JCM_13),
    ),
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


def _direct_ingredients(source: str) -> list[dict[str, Any]]:
    return [
        _component(
            "Lab-Lemco powder (Oxoid)",
            "3.0",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists 3.0 g/L Lab-Lemco powder (Oxoid), a "
                "source-disclosed beef-extract product."
            ),
        ),
        _component("Proteose peptone No. 3 (BD-Difco)", "10.0", "G_PER_L", source=source),
        _component("Trypticase peptone (BD-BBL)", "5.0", "G_PER_L", source=source),
        _component("Phytone peptone (BD-BBL)", "3.0", "G_PER_L", source=source),
        _component("Yeast extract (BD-Difco)", "5.0", "G_PER_L", source=source),
        _component("Glucose", "10.0", "G_PER_L", source=source),
        _component("Soluble starch", "0.5", "G_PER_L", source=source),
        _component("Tween 80", "1.0", "G_PER_L", source=source),
        _component("Bacto agar (BD-Difco)", "15.0", "G_PER_L", source=source),
        _component("Horse blood", "50.0", "ML_PER_L", source=source),
        _component("Distilled water", "825.0", "ML_PER_L", source=source),
    ]


def _solutions(source: str) -> list[dict[str, Any]]:
    return [
        {
            "preferred_term": "Liver extract",
            "concentration": {"value": "150.0", "unit": "ML_PER_L"},
            "source": source,
            "notes": f"{source} adds 150.0 ml/L Liver extract prepared as below.",
            "composition": [
                _component(
                    "Liver powder",
                    "58.8235",
                    "G_PER_L",
                    source=source,
                    notes=(
                        "JCM Medium 13 prepares Liver extract from 10.0 g liver "
                        "powder in 170.0 ml water before heating, pH adjustment, "
                        "and filtration."
                    ),
                ),
                _component(
                    "Distilled water",
                    "1000.0",
                    "ML_PER_L",
                    source=source,
                    notes=(
                        "JCM Medium 13 prepares Liver extract by suspending "
                        "10.0 g liver powder in 170.0 ml water."
                    ),
                ),
            ],
        },
        {
            "preferred_term": "Solution A",
            "concentration": {"value": "10.0", "unit": "ML_PER_L"},
            "source": source,
            "notes": f"{source} adds 10.0 ml/L Solution A.",
            "composition": [
                _component("K2HPO4", "100.0", "G_PER_L", source=source),
                _component("KH2PO4", "100.0", "G_PER_L", source=source),
                _component("Distilled water", "1000.0", "ML_PER_L", source=source),
            ],
        },
        {
            "preferred_term": "Solution B",
            "concentration": {"value": "5.0", "unit": "ML_PER_L"},
            "source": source,
            "notes": f"{source} adds 5.0 ml/L Solution B.",
            "composition": [
                _component("MgSO4 x 7 H2O", "40.0", "G_PER_L", source=source),
                _component("NaCl", "2.0", "G_PER_L", source=source),
                _component("FeSO4 x 7 H2O", "2.0", "G_PER_L", source=source),
                _component(
                    "MnSO4 x n H2O",
                    "2.0",
                    "G_PER_L",
                    source=source,
                    notes=(
                        "JCM Medium 13 lists 0.2 g MnSO4 x H2O of unspecified "
                        "hydrate number per 100.0 ml Solution B."
                    ),
                ),
                _component("Distilled water", "1000.0", "ML_PER_L", source=source),
            ],
        },
        {
            "preferred_term": "5% L-Cysteine HCl x H2O solution",
            "concentration": {"value": "10.0", "unit": "ML_PER_L"},
            "source": source,
            "notes": f"{source} adds 10.0 ml/L 5% L-Cysteine HCl x H2O solution.",
            "composition": [
                _component(
                    "L-Cysteine HCl x H2O",
                    "5.0",
                    "PERCENT_W_V",
                    source=source,
                    notes=(
                        "JCM Medium 13 specifies the added L-Cysteine HCl x H2O "
                        "solution as 5% w/v."
                    ),
                )
            ],
        },
    ]


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_agar_target(doc: dict[str, Any], target: AgarTarget) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')}")
    if _source_term_id(doc) != target.source_term:
        raise ValueError(f"{target.path}: expected media term {target.source_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        target.imported_ingredients,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    solution_signature = _signature(doc.get("solutions"), "solutions")
    if solution_signature not in (
        target.imported_solutions,
        FINAL_SOLUTION_SIGNATURE,
    ):
        raise ValueError(f"{target.path}: solution signature drifted")


def _ensure_maltose_target(doc: dict[str, Any], target: MaltoseTarget) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')}")
    if _source_term_id(doc) != target.source_term:
        raise ValueError(f"{target.path}: expected media term {target.source_term}")
    if _signature(doc.get("ingredients"), "ingredients") != MALTOSE_INGREDIENT_SIGNATURE:
        raise ValueError(f"{target.path}: ingredient signature drifted")
    if _signature(doc.get("solutions"), "solutions") != MALTOSE_SOLUTION_SIGNATURE:
        raise ValueError(f"{target.path}: solution signature drifted")


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

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
    ):
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


def _set_variant_children(
    doc: dict[str, Any],
    children: tuple[dict[str, Any], ...],
) -> None:
    if children:
        doc["variant_children"] = [copy.deepcopy(child) for child in children]
    else:
        doc.pop("variant_children", None)


def repair_agar_record(doc: dict[str, Any], target: AgarTarget) -> dict[str, Any]:
    _ensure_agar_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.2, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("high_metal", None)
    repaired["ingredients"] = _direct_ingredients(target.source)
    _put_after(repaired, "notes", SOURCE_NOTE, "media_term")
    _put_after(repaired, "solutions", _solutions(target.source), "ingredients")
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "solutions",
    )
    _put_after(
        repaired,
        "sterilization",
        copy.deepcopy(STERILIZATION),
        "preparation_steps",
    )

    if target.parent_media is None:
        repaired.pop("parent_media", None)
    else:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), "references")

    _set_variant_children(repaired, target.variant_children)
    if target.variant_relationship:
        _put_after(
            repaired,
            "variant_relationship",
            target.variant_relationship,
            "parent_media",
        )
    else:
        repaired.pop("variant_relationship", None)

    if target.variant_modifications:
        _put_after(
            repaired,
            "variant_modifications",
            list(target.variant_modifications),
            "variant_relationship",
        )
    else:
        repaired.pop("variant_modifications", None)

    _ensure_flags(repaired)
    _ensure_references(repaired, target.references)
    _append_event(
        repaired,
        action=target.action,
        references=target.references,
        notes=target.event_notes,
    )
    return repaired


def repair_maltose_record(doc: dict[str, Any], target: MaltoseTarget) -> dict[str, Any]:
    _ensure_maltose_target(doc, target)

    repaired = copy.deepcopy(doc)
    solutions = repaired.get("solutions")
    if not isinstance(solutions, list):
        raise ValueError(f"{target.path}: solutions is not a list")

    for solution in solutions:
        if isinstance(solution, dict) and solution.get("preferred_term") == "BL Agar":
            solution["culturemech_term"] = copy.deepcopy(BL_AGAR_JCM_TERM)
            break
    else:
        raise ValueError(f"{target.path}: BL Agar solution is missing")

    _put_after(repaired, "parent_media", copy.deepcopy(JCM_SUPPLEMENT_PARENT), "preparation_steps")
    _put_after(repaired, "variant_relationship", "SUPPLEMENTED_VARIANT", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        ["Supplements 1.0 L BL Agar with 5.0 g/L maltose."],
        "variant_relationship",
    )
    _ensure_references(repaired, target.references)
    _append_event(
        repaired,
        action=target.action,
        references=target.references,
        notes="Relinked this BL With 0.5% Maltose wrapper to the canonical JCM J13 BL Agar parent.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in AGAR_TARGETS:
        path = normalized / target.path
        plans[path] = repair_agar_record(_load(path), target)
    for target in MALTOSE_TARGETS:
        path = normalized / target.path
        plans[path] = repair_maltose_record(_load(path), target)
    return plans


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
