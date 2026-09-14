#!/usr/bin/env python3
"""Repair TOGO M358 PY4SR Agar and its JCM PY4S Agar parent."""

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
TARGET = Path("bacterial/TOGO_M358_PY4SR_Agar.yaml")
PARENT = Path("bacterial/py4s_agar.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009738"
EXPECTED_PARENT_ID = "CultureMech:002722"
EXPECTED_MEDIA_TERM = "TOGO:M358"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:J363"

CURATOR = "repair_togo_m358_score15.py"
ACTION = "RESOLVED_TOGO_M358_SCORE15"
PARENT_ACTION = "RESOLVED_JCM_363_FOR_TOGO_M358"
LINK_ACTION = "LINKED_TOGO_M358_SUPPLEMENTED_VARIANT"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M358 = "https://togomedium.org/medium/M358"
JCM_364 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=364"
JCM_363 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=363"
JCM_133 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=133"

SOURCE = "TOGO M358 / JCM Medium 364"
PARENT_SOURCE = "JCM Medium 363"
SALT_SOURCE = "JCM Medium 133"
TITLE = "PY4SR Agar"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("plant residue extract (see below)", "50", "G_PER_L"),
    ("water", "variable", "VARIABLE"),
    ("rice straw", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("PY4S AGAR (see Medium [M357])", "1", "G_PER_L", ()),
)

PLANT_RESIDUE_SIGNATURE: tuple[Component, ...] = (
    ("Rice straw", "variable", "VARIABLE"),
    ("Distilled water", "variable", "VARIABLE"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Plant residue extract", "50.0", "ML_PER_L", PLANT_RESIDUE_SIGNATURE),
)

IMPORTED_PARENT_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Trypticase peptone", "9.96016", "G_PER_L"),
    ("Yeast extract", "4.98008", "G_PER_L"),
    ("Glucose", "0.249004", "G_PER_L"),
    ("Cellobiose", "0.249004", "G_PER_L"),
    ("Maltose", "0.249004", "G_PER_L"),
    ("Starch", "0.249004", "G_PER_L"),
    ("Sodium resazurin", "1", "G_PER_L"),
    ("Na2CO3", "2.5", "G_PER_L"),
    ("L-Cysteine HCl x H2O", "0.298805", "G_PER_L"),
    ("Agar", "14.9402", "G_PER_L"),
)

FINAL_PARENT_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Trypticase peptone (BD-BBL)", "10.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "5.0", "G_PER_L"),
    ("Glucose", "0.25", "G_PER_L"),
    ("Cellobiose", "0.25", "G_PER_L"),
    ("Maltose", "0.25", "G_PER_L"),
    ("Soluble starch", "0.25", "G_PER_L"),
    ("L-Cysteine HCl H2O", "0.3", "G_PER_L"),
    ("Bacto agar (BD-Difco)", "15.0", "G_PER_L"),
    ("Distilled water", "850.0", "ML_PER_L"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
)

IMPORTED_PARENT_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Salt Solution I", "75", "G_PER_L", ()),
    ("Salt Solution II", "75", "G_PER_L", ()),
)

SALT_I_SIGNATURE: tuple[Component, ...] = (
    ("K2HPO4", "7.8", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

SALT_II_SIGNATURE: tuple[Component, ...] = (
    ("KH2PO4", "4.7", "G_PER_L"),
    ("NaCl", "11.8", "G_PER_L"),
    ("(NH4)2SO4", "12.0", "G_PER_L"),
    ("CaCl2", "1.2", "G_PER_L"),
    ("MgSO4 x H2O", "2.5", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

RESAZURIN_SIGNATURE: tuple[Component, ...] = (("Sodium resazurin", "1.0", "G_PER_L"),)

CARBONATE_SIGNATURE: tuple[Component, ...] = (("Na2CO3", "80.0", "G_PER_L"),)

FINAL_PARENT_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Salt Solution I", "75.0", "ML_PER_L", SALT_I_SIGNATURE),
    ("Salt Solution II", "75.0", "ML_PER_L", SALT_II_SIGNATURE),
    ("0.1% (w/v) resazurin-Na", "1.0", "ML_PER_L", RESAZURIN_SIGNATURE),
    ("8% (w/v) Na2CO3", "2.5", "ML_PER_L", CARBONATE_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)2SO4": ("CHEBI:62946", "ammonium sulfate"),
    "Bacto agar (BD-Difco)": ("CHEBI:2509", "agar"),
    "CaCl2": ("CHEBI:3312", "calcium dichloride"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "Cellobiose": ("CHEBI:17057", "cellobiose"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "L-Cysteine HCl H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    "Maltose": ("CHEBI:17306", "maltose"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "Sodium resazurin": ("CHEBI:8806", "Resazurin"),
    "Soluble starch": ("CHEBI:28017", "starch"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "ML_PER_L": "ml/L",
    "VARIABLE": "variable",
}

TARGET_REFERENCES = (TOGO_M358, JCM_364, JCM_363)
PARENT_REFERENCES = (JCM_363, JCM_133)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_PARENT_ID,
    "name": "py4s_agar",
    "notes": (
        "JCM Medium 364 PY4SR Agar uses JCM Medium 363 PY4S Agar "
        "supplemented with 50 ml/L plant residue extract."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_ID,
    "name": "py4sr_agar",
    "notes": (
        "TOGO M358 imports JCM Medium 364 PY4SR Agar, which supplements "
        "JCM Medium 363 PY4S Agar with 50 ml/L plant residue extract."
    ),
}

VARIANT_MODIFICATIONS = (
    "Adds 50 ml/L plant residue extract prepared by autoclaving rice straw "
    "in water at a 1:5 ratio and using the supernatant after centrifugation."
)

TARGET_NOTES = (
    "TOGO M358 imports JCM Medium 364 PY4SR Agar. JCM Medium 364 uses "
    "JCM Medium 363 PY4S Agar supplemented with 50 ml/L plant residue "
    "extract prepared by autoclaving rice straw in water at a 1:5 ratio "
    "for 20 min at 120 C and using the supernatant after centrifugation."
)

PARENT_NOTES = (
    "JCM Medium 363 PY4S Agar lists, per liter, 75 ml Salt solution I from "
    "JCM Medium 133, 75 ml Salt solution II from JCM Medium 133, 10.0 g "
    "Trypticase peptone (BD-BBL), 5.0 g Yeast extract (BD-Difco), 0.25 g "
    "each Glucose, Cellobiose, Maltose, and Soluble starch, 1.0 ml 0.1% "
    "resazurin-Na, 2.5 ml 8% Na2CO3, 0.3 g L-Cysteine HCl H2O, 15.0 g "
    "Bacto agar (BD-Difco), and 850 ml Distilled water. The final pH is "
    "6.7, and the medium is prepared anaerobically and poured into "
    "rubber-stopped tubes under oxygen-free N2-CO2 (95:5)."
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


def _target_solutions() -> list[dict[str, Any]]:
    return [
        _solution(
            "Plant residue extract",
            "50.0",
            [
                _component(
                    "Rice straw",
                    "variable",
                    "VARIABLE",
                    source=SOURCE,
                    notes=(
                        "JCM Medium 364 prepares Plant residue extract by "
                        "autoclaving rice straw in water at a 1:5 ratio; the "
                        "final soluble rice-straw concentration is not specified."
                    ),
                    term=False,
                ),
                _component(
                    "Distilled water",
                    "variable",
                    "VARIABLE",
                    source=SOURCE,
                    notes=(
                        "JCM Medium 364 prepares Plant residue extract by "
                        "autoclaving rice straw in water at a 1:5 ratio."
                    ),
                ),
            ],
            source=SOURCE,
            notes="JCM Medium 364 adds 50 ml/L Plant residue extract to PY4S Agar.",
            preparation_notes=(
                "Autoclave rice straw in water (1:5) at 120 C for 20 min "
                "and use the supernatant after centrifugation."
            ),
        )
    ]


def _parent_ingredient(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    if unit == "VARIABLE":
        return _component(
            preferred_term,
            value,
            unit,
            source=PARENT_SOURCE,
            notes=(
                "JCM Medium 363 prepares and dispenses the medium under "
                "oxygen-free N2-CO2 (95:5)."
            ),
        )

    return _component(
        preferred_term,
        value,
        unit,
        source=PARENT_SOURCE,
        term=preferred_term not in {"Trypticase peptone (BD-BBL)", "Yeast extract (BD-Difco)"},
    )


def _parent_ingredients() -> list[dict[str, Any]]:
    return [
        _parent_ingredient(preferred_term, value, unit)
        for preferred_term, value, unit in FINAL_PARENT_INGREDIENT_SIGNATURE
    ]


def _parent_solutions() -> list[dict[str, Any]]:
    salt_i = _solution(
        "Salt Solution I",
        "75.0",
        _components(SALT_I_SIGNATURE, source=SALT_SOURCE),
        source=PARENT_SOURCE,
        notes=(
            "JCM Medium 363 adds 75 ml/L Salt solution I from JCM Medium "
            "133; JCM Medium 133 defines this stock as 0.78 g K2HPO4 in "
            "100 ml Distilled water."
        ),
    )
    salt_ii = _solution(
        "Salt Solution II",
        "75.0",
        _components(
            SALT_II_SIGNATURE,
            source=SALT_SOURCE,
            ungrounded=frozenset({"MgSO4 x H2O"}),
        ),
        source=PARENT_SOURCE,
        notes=(
            "JCM Medium 363 adds 75 ml/L Salt solution II from JCM Medium "
            "133; JCM Medium 133 defines this stock as KH2PO4, NaCl, "
            "(NH4)2SO4, CaCl2, and MgSO4 x H2O in 100 ml Distilled water."
        ),
    )
    resazurin = _solution(
        "0.1% (w/v) resazurin-Na",
        "1.0",
        _components(RESAZURIN_SIGNATURE, source=PARENT_SOURCE),
        source=PARENT_SOURCE,
        notes="JCM Medium 363 adds 1.0 ml/L 0.1% (w/v) resazurin-Na.",
    )
    carbonate = _solution(
        "8% (w/v) Na2CO3",
        "2.5",
        _components(CARBONATE_SIGNATURE, source=PARENT_SOURCE),
        source=PARENT_SOURCE,
        notes="JCM Medium 363 adds 2.5 ml/L 8% (w/v) Na2CO3.",
    )
    return [salt_i, salt_ii, resazurin, carbonate]


PARENT_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare PY4S Agar with Salt solution I, Salt solution II, "
            "Trypticase peptone, Yeast extract, Glucose, Cellobiose, "
            "Maltose, Soluble starch, resazurin-Na, Na2CO3, "
            "L-Cysteine HCl H2O, Bacto agar, and distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 6.7.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
    },
    {
        "step_number": 4,
        "action": "ALIQUOT",
        "description": (
            "Prepare anaerobically and pour into rubber-stopped tubes under "
            "oxygen-free N2-CO2 (95:5)."
        ),
    },
)

TARGET_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Autoclave rice straw in water at a 1:5 ratio at 120 C for "
            "20 min to prepare Plant residue extract."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "After centrifugation, use the supernatant to supplement PY4S "
            "Agar with 50 ml/L Plant residue extract."
        ),
    },
)

PARENT_STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": (
        "JCM states to sterilize media by autoclaving at 121 C for 15 min "
        "unless otherwise stated."
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


def _solution_signatures(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signatures: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signatures.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), f"{label} composition"),
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
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signatures = _solution_signatures(doc.get("solutions"), "solutions")
    if solution_signatures not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"{PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_PARENT_INGREDIENT_SIGNATURE,
        FINAL_PARENT_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{PARENT}: ingredient signature drifted")

    solution_signatures = _solution_signatures(doc.get("solutions"), "solutions")
    if solution_signatures not in (
        IMPORTED_PARENT_SOLUTION_SIGNATURES,
        FINAL_PARENT_SOLUTION_SIGNATURES,
    ):
        raise ValueError(f"{PARENT}: solution signature drifted")


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


def _ensure_references(doc: dict[str, Any], references_to_add: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in references_to_add:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(
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
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 6.7, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "ingredients", [], "physical_state")
    repaired["solutions"] = _target_solutions()
    _put_after(repaired, "notes", TARGET_NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(TARGET_PREPARATION_STEPS))
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, TARGET_REFERENCES)
    _append_curation_event(
        repaired,
        action=ACTION,
        references=TARGET_REFERENCES,
        notes=(
            f"{TARGET_NOTES} Corrected the imported stock-reference unit "
            "artifact, represented the plant residue extract as a 50 ml/L "
            "supplement, and linked the record to JCM Medium 363 PY4S Agar."
        ),
    )
    repaired["parent_media"] = copy.deepcopy(PARENT_MEDIA)
    repaired["variant_relationship"] = "SUPPLEMENTED_VARIANT"
    repaired["variant_modifications"] = [VARIANT_MODIFICATIONS]
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 6.7, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "notes", PARENT_NOTES, "media_term")
    repaired["ingredients"] = _parent_ingredients()
    repaired["solutions"] = _parent_solutions()
    repaired["preparation_steps"] = copy.deepcopy(list(PARENT_PREPARATION_STEPS))
    _put_after(
        repaired,
        "sterilization",
        copy.deepcopy(PARENT_STERILIZATION),
        "preparation_steps",
    )
    _ensure_flags(repaired)
    _ensure_references(repaired, PARENT_REFERENCES)
    _append_curation_event(
        repaired,
        action=PARENT_ACTION,
        references=PARENT_REFERENCES,
        notes=(
            f"{PARENT_NOTES} Corrected MediaDive stock-volume artifacts, "
            "expanded Salt solution I and II from JCM Medium 133, moved "
            "the resazurin-Na and Na2CO3 stocks to solutions, and restored "
            "the source component amounts before linking TOGO M358."
        ),
    )
    _ensure_variant_child(repaired)
    _append_curation_event(
        repaired,
        action=LINK_ACTION,
        references=TARGET_REFERENCES,
        notes="Linked TOGO M358 as a plant-residue supplemented variant of PY4S Agar.",
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
