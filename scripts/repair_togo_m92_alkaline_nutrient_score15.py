#!/usr/bin/env python3
"""Repair MediaDive/TOGO JCM 74/100 Nutrient Agar records."""

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
JCM_J74_PATH = Path("bacterial/JCM_J74_NUTRIENT_AGAR.yaml")
TOGO_M65_PATH = Path("bacterial/TOGO_M65_Nutrient_Agar.yaml")
JCM_J100_PATH = Path("bacterial/JCM_J100_ALKALINE_NUTRIENT_AGAR.yaml")
TOGO_M92_PATH = Path("bacterial/TOGO_M92_Alkaline_Nutrient_Agar.yaml")
SOLUTION_3700_PATH = Path("bacterial/mediadive_3700_Main_sol_J74.yaml")
SOLUTION_3730_PATH = Path("bacterial/mediadive_3730_Main_sol_J100.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m92_alkaline_nutrient_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J74 = "https://mediadive.dsmz.de/medium/J74"
MEDIADIVE_J100 = "https://mediadive.dsmz.de/medium/J100"
JCM_74 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=74"
JCM_100 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=100"
TOGO_M65 = "https://togomedium.org/medium/M65"
TOGO_M92 = "https://togomedium.org/medium/M92"

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
    final_ingredients: tuple[Component, ...]
    final_solutions: tuple[SolutionSignature, ...]
    ph_value: float
    source_note: str
    preparation_steps: tuple[dict[str, Any], ...]
    action: str
    event_notes: str
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, Any], ...] = ()


@dataclass(frozen=True)
class SolutionTarget:
    path: Path
    record_id: str
    solution_term: str
    source_name: str
    imported_composition: tuple[Component, ...]
    final_composition: tuple[Component, ...]
    preparation_notes: str
    notes: str
    action: str
    event_notes: str
    references: tuple[str, ...]


IMPORTED_JCM_INGREDIENTS: tuple[Component, ...] = (
    ("Peptone", "5", "G_PER_L"),
    ("Beef extract", "3", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
)

IMPORTED_TOGO_NUTRIENT_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Beef extract", "3", "G_PER_L"),
    ("Peptone", "5", "G_PER_L"),
)

IMPORTED_NA2CO3_SOLUTION: tuple[SolutionSignature, ...] = (
    ("Na2CO3 solution", "variable", "VARIABLE", ()),
)

IMPORTED_MEDIADIVE_SOLUTION_COMPOSITION: tuple[Component, ...] = (
    ("Peptone", "5", "G_PER_L"),
    ("Beef extract", "3", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Distilled water", "1000", "PERCENT_V_V"),
)

PLACEHOLDER_INGREDIENTS: tuple[Component, ...] = (
    ("See source for composition", "variable", "VARIABLE"),
)

NUTRIENT_AGAR_COMPOSITION: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("Peptone", "5.0", "G_PER_L"),
    ("Beef extract", "3.0", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
)

MEDIADIVE_MAIN_SOLUTION_COMPOSITION: tuple[Component, ...] = (
    ("Peptone", "5.0", "G_PER_L"),
    ("Beef extract", "3.0", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

NA2CO3_SOLUTION_COMPOSITION: tuple[Component, ...] = (("Na2CO3", "10.0", "PERCENT_W_V"),)

FINAL_NA2CO3_SOLUTION: tuple[SolutionSignature, ...] = (
    ("10% Na2CO3 solution", "variable", "VARIABLE", NA2CO3_SOLUTION_COMPOSITION),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Peptone": ("MICRO:0000178", "Peptone"),
    "Beef extract": ("FOODON:03302088", "Beef extract"),
    "Agar": ("CHEBI:2509", "agar"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Peptone": ("PROTEIN_SOURCE",),
    "Beef extract": ("PROTEIN_SOURCE",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Agar": ("SOLIDIFYING_AGENT",),
    "Na2CO3": ("BUFFER",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
}

M65_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M65_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010062",
    "name": "nutrient_agar",
    "notes": (
        "TOGO M65 imports the same JCM Medium 74 Nutrient Agar "
        "formulation represented by MediaDive J74."
    ),
}

J100_CHILD = {
    "path": f"data/normalized_yaml/{JCM_J100_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:002194",
    "name": "alkaline_nutrient_agar",
    "notes": (
        "JCM Medium 100 starts from the JCM Medium 74 Nutrient Agar basal "
        "formulation and adjusts the final medium to pH 10.0 with sterile "
        "10% Na2CO3 solution after autoclaving."
    ),
}

NBRC_CHILD = {
    "path": "data/normalized_yaml/bacterial/NBRC_NUTRIENT_AGAR.yaml",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:007511",
    "name": "nutrient_agar",
    "notes": (
        "Reviewed JCM/NBRC Nutrient Agar records; both parsed formulations "
        "contain beef extract 3 g/L, peptone 5 g/L, and agar 15 g/L, with "
        "the JCM parent carrying pH 7.0 and the NBRC record not specifying pH."
    ),
}

M92_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M92_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010351",
    "name": "alkaline_nutrient_agar",
    "notes": (
        "TOGO M92 imports the same JCM Medium 100 Alkaline Nutrient Agar "
        "formulation represented by MediaDive J100."
    ),
}

J74_PARENT_SOURCE_DUPLICATE = {
    "path": f"data/normalized_yaml/{JCM_J74_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003093",
    "name": "nutrient_agar",
    "notes": M65_CHILD["notes"],
}

J74_PARENT_SUPPLEMENTED = {
    "path": f"data/normalized_yaml/{JCM_J74_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:003093",
    "name": "nutrient_agar",
    "notes": J100_CHILD["notes"],
}

J100_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J100_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:002194",
    "name": "alkaline_nutrient_agar",
    "notes": M92_CHILD["notes"],
}

NUTRIENT_NOTE = (
    "JCM Medium 74 / Nutrient Agar lists 1.0 L distilled water, 5.0 g/L "
    "peptone, 3.0 g/L beef extract, and 15.0 g/L agar, adjusted to pH "
    "7.0; TOGO M65 and MediaDive J74 report the same JCM recipe."
)

ALKALINE_NOTE = (
    "JCM Medium 100 / Alkaline Nutrient Agar uses the same Nutrient Agar "
    "basal formulation as JCM Medium 74, then after autoclaving adjusts "
    "the final medium to pH 10.0 with sterile 10% Na2CO3 solution. TOGO "
    "M92 and MediaDive J100 report the same JCM recipe."
)

NUTRIENT_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Dissolve 5.0 g/L peptone, 3.0 g/L beef extract, and 15.0 g/L "
            "agar in 1.0 L distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0.",
    },
)

ALKALINE_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Dissolve 5.0 g/L peptone, 3.0 g/L beef extract, and 15.0 g/L "
            "agar in 1.0 L distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the basal nutrient agar.",
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": (
            "After autoclaving, adjust pH to 10.0 with sterile 10% Na2CO3 " "solution."
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


def _solutions(source: str) -> list[dict[str, Any]]:
    return [
        {
            "preferred_term": "10% Na2CO3 solution",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": source,
            "notes": (
                f"{source} uses sterile 10% Na2CO3 solution to adjust the "
                "final medium to pH 10.0; the source does not specify a "
                "fixed addition volume."
            ),
            "composition": [
                _component(
                    "Na2CO3",
                    "10.0",
                    "PERCENT_W_V",
                    source=source,
                    notes=(
                        f"{source} specifies the pH-adjusting sodium "
                        "carbonate solution as 10.0% w/v."
                    ),
                )
            ],
            "preparation_notes": ("Sterilize before adjusting the basal medium to pH 10.0."),
        }
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
                _signature(row.get("composition") or [], f"{label}.composition"),
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
    if ingredient_signature not in (
        target.imported_ingredients,
        target.final_ingredients,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    solution_signature = _solution_signature(doc.get("solutions"), "solutions")
    if solution_signature not in (
        target.imported_solutions,
        target.final_solutions,
    ):
        raise ValueError(f"{target.path}: solution signature drifted")


def _ensure_solution_target(doc: dict[str, Any], target: SolutionTarget) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')}")
    if _term_id(doc) != target.solution_term:
        raise ValueError(f"{target.path}: expected solution {target.solution_term}")

    composition = _signature(doc.get("composition"), "composition")
    if composition not in (target.imported_composition, target.final_composition):
        raise ValueError(f"{target.path}: composition signature drifted")

    ingredients = _signature(doc.get("ingredients"), "ingredients")
    if ingredients not in (PLACEHOLDER_INGREDIENTS, ()):
        raise ValueError(f"{target.path}: ingredient signature drifted")


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    doc[key] = value
    items = list(doc.items())
    without = [(item_key, item_value) for item_key, item_value in items if item_key != key]

    rebuilt: dict[str, Any] = {}
    inserted = False
    for item_key, item_value in without:
        rebuilt[item_key] = item_value
        if item_key == after:
            rebuilt[key] = value
            inserted = True
    if not inserted:
        rebuilt[key] = value

    doc.clear()
    doc.update(rebuilt)


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _composition_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    rows.extend(row for row in doc.get("composition") or [] if isinstance(row, dict))
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        rows.extend(row for row in solution.get("composition") or [] if isinstance(row, dict))
    return rows


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

    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)

    components = _composition_components(doc)
    if any(not _grounded(component) for component in components):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    else:
        while "has_unmapped_ingredients" in flags:
            flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any], references: tuple[str, ...]) -> None:
    doc["references"] = [{"reference": reference} for reference in references]


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
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    repaired.pop("kg_microbe_match", None)
    _put_after(repaired, "notes", target.source_note, "media_term")
    repaired["ingredients"] = _composition(
        target.source_name,
        target.final_ingredients,
    )
    if target.final_solutions:
        _put_after(repaired, "solutions", _solutions(target.source_name), "ingredients")
    else:
        repaired.pop("solutions", None)
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in target.preparation_steps],
        "solutions" if target.final_solutions else "ingredients",
    )

    _ensure_references(repaired, target.references)
    if target.parent_media:
        _put_after(
            repaired,
            "parent_media",
            copy.deepcopy(target.parent_media),
            "references",
        )
        _put_after(
            repaired,
            "variant_relationship",
            target.variant_relationship,
            "parent_media",
        )
        _put_after(
            repaired,
            "variant_modifications",
            list(target.variant_modifications),
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
    _append_event(
        repaired,
        action=target.action,
        references=target.references,
        notes=target.event_notes,
    )
    return repaired


def repair_solution_record(
    doc: dict[str, Any],
    target: SolutionTarget,
) -> dict[str, Any]:
    _ensure_solution_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _composition(
        target.source_name,
        target.final_composition,
    )
    repaired.pop("ingredients", None)
    repaired["preparation_notes"] = target.preparation_notes
    _put_after(repaired, "notes", target.notes, "preparation_notes")

    _ensure_flags(repaired)
    _ensure_references(repaired, target.references)
    _append_event(
        repaired,
        action=target.action,
        references=target.references,
        notes=target.event_notes,
    )
    return repaired


TARGETS: tuple[MediumTarget, ...] = (
    MediumTarget(
        path=JCM_J74_PATH,
        record_id="CultureMech:003093",
        source_term="mediadive.medium:J74",
        source_name="MediaDive J74 / JCM Medium 74",
        imported_ingredients=IMPORTED_JCM_INGREDIENTS,
        imported_solutions=(),
        final_ingredients=NUTRIENT_AGAR_COMPOSITION,
        final_solutions=(),
        ph_value=7.0,
        source_note=NUTRIENT_NOTE,
        preparation_steps=NUTRIENT_PREPARATION_STEPS,
        action="RESOLVED_MEDIADIVE_J74_NUTRIENT_AGAR",
        event_notes=(
            "Added source 1.0 L distilled water, grounded peptone and beef "
            "extract, retained the pH 7.0 adjustment, and linked the TOGO "
            "M65 source duplicate plus JCM Medium 100 alkaline variant."
        ),
        references=(MEDIADIVE_J74, JCM_74, TOGO_M65, MEDIADIVE_J100, JCM_100),
        variant_children=(M65_CHILD, J100_CHILD, NBRC_CHILD),
    ),
    MediumTarget(
        path=TOGO_M65_PATH,
        record_id="CultureMech:010062",
        source_term="TOGO:M65",
        source_name="TOGO M65 / JCM Medium 74",
        imported_ingredients=IMPORTED_TOGO_NUTRIENT_INGREDIENTS,
        imported_solutions=(),
        final_ingredients=NUTRIENT_AGAR_COMPOSITION,
        final_solutions=(),
        ph_value=7.0,
        source_note=NUTRIENT_NOTE,
        preparation_steps=NUTRIENT_PREPARATION_STEPS,
        action="RESOLVED_TOGO_M65_NUTRIENT_AGAR",
        event_notes=(
            "Corrected water from 1 g/L to 1.0 L, grounded peptone and beef "
            "extract, added the pH 7.0 adjustment from TOGO M65 and "
            "MediaDive J74, and linked the MediaDive J74 source duplicate."
        ),
        references=(TOGO_M65, MEDIADIVE_J74, JCM_74),
        parent_media=J74_PARENT_SOURCE_DUPLICATE,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(M65_CHILD["notes"],),
    ),
    MediumTarget(
        path=JCM_J100_PATH,
        record_id="CultureMech:002194",
        source_term="mediadive.medium:J100",
        source_name="MediaDive J100 / JCM Medium 100",
        imported_ingredients=IMPORTED_JCM_INGREDIENTS,
        imported_solutions=(),
        final_ingredients=NUTRIENT_AGAR_COMPOSITION,
        final_solutions=FINAL_NA2CO3_SOLUTION,
        ph_value=10.0,
        source_note=ALKALINE_NOTE,
        preparation_steps=ALKALINE_PREPARATION_STEPS,
        action="RESOLVED_MEDIADIVE_J100_ALKALINE_NUTRIENT_AGAR",
        event_notes=(
            "Added source 1.0 L distilled water, grounded peptone and beef "
            "extract, structured sterile 10% Na2CO3 as the variable pH "
            "adjuster, and linked the JCM Medium 74 parent plus TOGO M92 "
            "source duplicate."
        ),
        references=(MEDIADIVE_J100, JCM_100, TOGO_M92, MEDIADIVE_J74, JCM_74),
        parent_media=J74_PARENT_SUPPLEMENTED,
        variant_relationship="SUPPLEMENTED_VARIANT",
        variant_modifications=(J100_CHILD["notes"],),
        variant_children=(M92_CHILD,),
    ),
    MediumTarget(
        path=TOGO_M92_PATH,
        record_id="CultureMech:010351",
        source_term="TOGO:M92",
        source_name="TOGO M92 / JCM Medium 100",
        imported_ingredients=IMPORTED_TOGO_NUTRIENT_INGREDIENTS,
        imported_solutions=IMPORTED_NA2CO3_SOLUTION,
        final_ingredients=NUTRIENT_AGAR_COMPOSITION,
        final_solutions=FINAL_NA2CO3_SOLUTION,
        ph_value=10.0,
        source_note=ALKALINE_NOTE,
        preparation_steps=ALKALINE_PREPARATION_STEPS,
        action="RESOLVED_TOGO_M92_ALKALINE_NUTRIENT_AGAR",
        event_notes=(
            "Corrected water from 1 g/L to 1.0 L, grounded peptone and beef "
            "extract, replaced the empty Na2CO3 solution stub with a "
            "sterile 10% variable pH-adjuster stock, and linked the "
            "MediaDive J100 source duplicate."
        ),
        references=(TOGO_M92, MEDIADIVE_J100, JCM_100),
        parent_media=J100_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(M92_CHILD["notes"],),
    ),
)

SOLUTION_TARGETS: tuple[SolutionTarget, ...] = (
    SolutionTarget(
        path=SOLUTION_3700_PATH,
        record_id="CultureMech:012782",
        solution_term="mediadive.solution:3700",
        source_name="MediaDive solution 3700 / JCM Medium 74",
        imported_composition=IMPORTED_MEDIADIVE_SOLUTION_COMPOSITION,
        final_composition=MEDIADIVE_MAIN_SOLUTION_COMPOSITION,
        preparation_notes="Mix peptone, beef extract, agar, and water; adjust pH to 7.0.",
        notes=(
            "MediaDive solution 3700 is the complete main solution for JCM "
            "Medium 74 / Nutrient Agar."
        ),
        action="RESOLVED_MEDIADIVE_3700_MAIN_SOL_J74",
        event_notes=(
            "Corrected the Distilled water row from a false percent-volume "
            "value to source ml/L units, grounded peptone and beef extract, "
            "and removed the placeholder top-level ingredient."
        ),
        references=(MEDIADIVE_J74,),
    ),
    SolutionTarget(
        path=SOLUTION_3730_PATH,
        record_id="CultureMech:012811",
        solution_term="mediadive.solution:3730",
        source_name="MediaDive solution 3730 / JCM Medium 100",
        imported_composition=IMPORTED_MEDIADIVE_SOLUTION_COMPOSITION,
        final_composition=MEDIADIVE_MAIN_SOLUTION_COMPOSITION,
        preparation_notes=(
            "Mix peptone, beef extract, agar, and water, autoclave, then "
            "adjust pH to 10.0 with sterile 10% Na2CO3 solution."
        ),
        notes=(
            "MediaDive solution 3730 is the complete basal main solution for "
            "JCM Medium 100 / Alkaline Nutrient Agar; its MediaDive step "
            "describes the final sterile Na2CO3 pH adjustment."
        ),
        action="RESOLVED_MEDIADIVE_3730_MAIN_SOL_J100",
        event_notes=(
            "Corrected the Distilled water row from a false percent-volume "
            "value to source ml/L units, grounded peptone and beef extract, "
            "and removed the placeholder top-level ingredient."
        ),
        references=(MEDIADIVE_J100,),
    ),
)


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_medium_record(_load(path), target)

    for target in SOLUTION_TARGETS:
        path = normalized / target.path
        plans[path] = repair_solution_record(_load(path), target)
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
