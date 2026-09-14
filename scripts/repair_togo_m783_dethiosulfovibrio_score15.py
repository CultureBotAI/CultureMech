#!/usr/bin/env python3
"""Repair JCM/TOGO Dethiosulfovibrio II Medium stock solutions."""

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
JCM_J758_PATH = Path("bacterial/dethiosulfovibrio_ii_medium.yaml")
TOGO_M783_PATH = Path("bacterial/TOGO_M783_Dethiosulfovibrio_II_Medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m783_dethiosulfovibrio_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

JCM_758 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=758"
JCM_187 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187"
MEDIADIVE_J758 = "https://mediadive.dsmz.de/medium/J758"
TOGO_M783 = "https://togomedium.org/medium/M783"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    source_term: str
    source_name: str
    imported_ingredients: tuple[Component, ...]
    imported_solutions: tuple[Component, ...]
    action: str
    event_notes: str
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()


JCM_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("NaCl", "19.3424", "G_PER_L"),
    ("MgCl2 x 6 H2O", "2.90135", "G_PER_L"),
    ("KH2PO4", "0.967118", "G_PER_L"),
    ("Trisodium citrate x H2O", "2.90135", "G_PER_L"),
    ("Yeast extract", "4.83559", "G_PER_L"),
    ("Bacto peptone", "1.93424", "G_PER_L"),
    ("Resazurin", "0.000483559", "G_PER_L"),
    ("CaCl2 x 2 H2O", "2", "G_PER_L"),
    ("Na2S2O3 x 5 H2O", "20", "G_PER_L"),
    ("Na2S x 9 H2O", "10", "G_PER_L"),
    ("HCl", "2.5", "G_PER_L"),
    ("FeCl2 x 4 H2O", "1.5", "G_PER_L"),
    ("ZnCl2", "0.07", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.1", "G_PER_L"),
    ("H3BO3", "0.006", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.19", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.002", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.024", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.036", "G_PER_L"),
)

TOGO_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("NaCl", "20", "G_PER_L"),
    ("KH2PO4", "1", "G_PER_L"),
    ("Resazurin", "0.5", "G_PER_L"),
    ("MgCl2・6H2O", "3", "G_PER_L"),
    ("Trisodium citrate・H2O", "3", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "5", "G_PER_L"),
    ("Bacto peptone (BD-Difco)", "2", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

TOGO_IMPORTED_SOLUTIONS: tuple[Component, ...] = (
    ("FeCl2 solution (see Medium [M180])", "1", "G_PER_L"),
    ("Trace element solution (see Medium [M180])", "1", "G_PER_L"),
    ("10% CaCl2・2H2O solution", "2", "G_PER_L"),
    ("5% Na2S・9H2O solution", "10", "G_PER_L"),
    ("12.5% Na2S2O3・5H2O solution*", "20", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "19.3424", "G_PER_L"),
    ("MgCl2 x 6 H2O", "2.90135", "G_PER_L"),
    ("KH2PO4", "0.967118", "G_PER_L"),
    ("Trisodium citrate x H2O", "2.90135", "G_PER_L"),
    ("Yeast extract", "4.83559", "G_PER_L"),
    ("Bacto peptone", "1.93424", "G_PER_L"),
    ("Resazurin", "0.483559", "MG_PER_L"),
    ("Distilled water", "967.118", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("FeCl2 solution", "0.967118", "ML_PER_L"),
    ("Trace element solution", "0.967118", "ML_PER_L"),
    ("10% CaCl2 x 2 H2O solution", "1.93424", "ML_PER_L"),
    ("12.5% Na2S2O3 x 5 H2O solution", "19.3424", "ML_PER_L"),
    ("5% Na2S x 9 H2O solution", "9.67118", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "MgCl2 x 6 H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "Trisodium citrate x H2O": ("CHEBI:53258", "sodium citrate"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Na2S2O3 x 5 H2O": ("CHEBI:32150", "sodium thiosulfate pentahydrate"),
    "Na2S x 9 H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "HCl": ("CHEBI:17883", "hydrogen chloride"),
    "FeCl2 x 4 H2O": ("CHEBI:86249", "iron dichloride tetrahydrate"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2 H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "NiCl2 x 6 H2O": ("CHEBI:34887", "nickel dichloride"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Yeast extract": ("NITROGEN_SOURCE",),
    "Na2S2O3 x 5 H2O": ("SULFUR_SOURCE",),
    "Na2S x 9 H2O": ("SULFUR_SOURCE",),
    "FeCl2 x 4 H2O": ("IRON_SOURCE", "TRACE_ELEMENT"),
    "ZnCl2": ("TRACE_ELEMENT",),
    "MnCl2 x 4 H2O": ("TRACE_ELEMENT",),
    "H3BO3": ("TRACE_ELEMENT",),
    "CoCl2 x 6 H2O": ("TRACE_ELEMENT",),
    "CuCl2 x 2 H2O": ("TRACE_ELEMENT",),
    "NiCl2 x 6 H2O": ("TRACE_ELEMENT",),
    "Na2MoO4 x 2 H2O": ("TRACE_ELEMENT",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "KH2PO4": ("BUFFER",),
    "Trisodium citrate x H2O": ("BUFFER",),
    "Resazurin": ("REDOX_INDICATOR",),
    "Na2S x 9 H2O": ("REDUCING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
}

M783_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M783_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010192",
    "name": "dethiosulfovibrio_ii_medium",
    "notes": (
        "TOGO M783 imports the same JCM Medium 758 Dethiosulfovibrio II "
        "Medium formulation represented by MediaDive J758."
    ),
}

J758_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J758_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003101",
    "name": "dethiosulfovibrio_ii_medium",
    "notes": M783_CHILD["notes"],
}

SOURCE_NOTE = (
    "JCM Medium 758, MediaDive J758, and TOGO M783 describe Dethiosulfovibrio "
    "II Medium as a 1.034 L anoxic N2 medium containing 1.0 L distilled water, "
    "1.0 ml each of FeCl2 solution and Trace element solution from JCM Medium "
    "187, 0.5 mg resazurin, 2.0 ml 10% CaCl2 x 2 H2O, 20.0 ml 12.5% "
    "Na2S2O3 x 5 H2O, and 10.0 ml 5% Na2S x 9 H2O stocks."
)

PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix main-solution components including FeCl2 solution, Trace "
            "element solution, and 967.118 ml/L distilled water under a N2 "
            "atmosphere."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the main solution under a N2 atmosphere.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "After cooling, add 1.93424 ml/L 10% CaCl2 x 2 H2O solution, "
            "19.3424 ml/L 12.5% Na2S2O3 x 5 H2O solution, and 9.67118 ml/L "
            "5% Na2S x 9 H2O solution from sterile anaerobic stocks stored "
            "under N2; the thiosulfate stock is filter-sterilized."
        ),
    },
    {
        "step_number": 4,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 6.7-6.8 if necessary.",
    },
]

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
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


def _direct_ingredients(source: str) -> list[dict[str, Any]]:
    return [
        _component("NaCl", "19.3424", "G_PER_L", source=source),
        _component("MgCl2 x 6 H2O", "2.90135", "G_PER_L", source=source),
        _component("KH2PO4", "0.967118", "G_PER_L", source=source),
        _component("Trisodium citrate x H2O", "2.90135", "G_PER_L", source=source),
        _component("Yeast extract", "4.83559", "G_PER_L", source=source),
        _component("Bacto peptone", "1.93424", "G_PER_L", source=source),
        _component("Resazurin", "0.483559", "MG_PER_L", source=source),
        _component(
            "Distilled water",
            "967.118",
            "ML_PER_L",
            source=source,
            notes=f"{source} contributes 967.118 ml/L distilled water.",
        ),
    ]


def _percent_solution(
    preferred_term: str,
    volume: str,
    solute: str,
    percent: str,
    source: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": volume, "unit": "ML_PER_L"},
        "source": source,
        "notes": f"{source} adds {volume} ml/L {preferred_term}.",
        "composition": [
            _component(
                solute,
                percent,
                "PERCENT_W_V",
                source=source,
                notes=f"{source} specifies {preferred_term} as {percent}% w/v.",
            )
        ],
    }


def _solutions(source: str) -> list[dict[str, Any]]:
    return [
        {
            "preferred_term": "FeCl2 solution",
            "concentration": {"value": "0.967118", "unit": "ML_PER_L"},
            "source": f"{source} / JCM Medium 187",
            "notes": f"{source} adds 0.967118 ml/L FeCl2 solution.",
            "composition": [
                _component("HCl", "2.5", "G_PER_L", source="JCM Medium 187"),
                _component(
                    "FeCl2 x 4 H2O",
                    "1.5",
                    "G_PER_L",
                    source="JCM Medium 187",
                ),
                _component(
                    "Distilled water",
                    "990.0",
                    "ML_PER_L",
                    source="JCM Medium 187",
                    notes="JCM Medium 187 makes FeCl2 solution with 990.0 ml water.",
                ),
            ],
            "preparation_notes": ("First dissolve FeCl2 in the HCl, then dilute in water."),
        },
        {
            "preferred_term": "Trace element solution",
            "concentration": {"value": "0.967118", "unit": "ML_PER_L"},
            "source": f"{source} / JCM Medium 187",
            "notes": f"{source} adds 0.967118 ml/L Trace element solution.",
            "composition": [
                _component("ZnCl2", "70.0", "MG_PER_L", source="JCM Medium 187"),
                _component(
                    "MnCl2 x 4 H2O",
                    "100.0",
                    "MG_PER_L",
                    source="JCM Medium 187",
                ),
                _component("H3BO3", "6.0", "MG_PER_L", source="JCM Medium 187"),
                _component(
                    "CoCl2 x 6 H2O",
                    "190.0",
                    "MG_PER_L",
                    source="JCM Medium 187",
                ),
                _component("CuCl2 x 2 H2O", "2.0", "MG_PER_L", source="JCM Medium 187"),
                _component(
                    "NiCl2 x 6 H2O",
                    "24.0",
                    "MG_PER_L",
                    source="JCM Medium 187",
                ),
                _component(
                    "Na2MoO4 x 2 H2O",
                    "36.0",
                    "MG_PER_L",
                    source="JCM Medium 187",
                ),
                _component(
                    "Distilled water",
                    "1000.0",
                    "ML_PER_L",
                    source="JCM Medium 187",
                    notes="JCM Medium 187 makes Trace element solution up to 1.0 L.",
                ),
            ],
        },
        _percent_solution(
            "10% CaCl2 x 2 H2O solution",
            "1.93424",
            "CaCl2 x 2 H2O",
            "10.0",
            source,
        ),
        _percent_solution(
            "12.5% Na2S2O3 x 5 H2O solution",
            "19.3424",
            "Na2S2O3 x 5 H2O",
            "12.5",
            source,
        ),
        _percent_solution(
            "5% Na2S x 9 H2O solution",
            "9.67118",
            "Na2S x 9 H2O",
            "5.0",
            source,
        ),
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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
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


def _grounded(component: dict[str, Any]) -> bool:
    for key in ("term", "mediaingredientmech_term", "mediaingredientmech_chebi_term"):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _composition_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    components = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        nested = solution.get("composition") or []
        components.extend(i for i in nested if isinstance(i, dict))
    return components


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

    components = _composition_components(doc)
    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)
    if any(not _grounded(component) for component in components):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    else:
        while "has_unmapped_ingredients" in flags:
            flags.remove("has_unmapped_ingredients")


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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    _put_after(repaired, "ph_range", {"min": 6.7, "max": 6.8}, "physical_state")
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "notes", SOURCE_NOTE, "media_term")
    repaired["ingredients"] = _direct_ingredients(target.source_name)
    _put_after(repaired, "solutions", _solutions(target.source_name), "ingredients")
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

    if target.parent_media:
        _put_after(
            repaired,
            "parent_media",
            copy.deepcopy(target.parent_media),
            "references",
        )
        _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
        _put_after(
            repaired,
            "variant_modifications",
            [J758_PARENT["notes"]],
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
    _ensure_references(repaired, target.references)
    _append_event(
        repaired,
        action=target.action,
        references=target.references,
        notes=target.event_notes,
    )
    return repaired


TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM_J758_PATH,
        record_id="CultureMech:003101",
        source_term="mediadive.medium:J758",
        source_name="MediaDive J758 / JCM Medium 758",
        imported_ingredients=JCM_IMPORTED_INGREDIENTS,
        imported_solutions=(),
        action="RESOLVED_JCM_758_DETHIOSULFOVIBRIO_II_MEDIUM",
        event_notes=(
            "Moved FeCl2 solution, Trace element solution, 10% CaCl2 x 2 H2O, "
            "12.5% Na2S2O3 x 5 H2O, and 5% Na2S x 9 H2O into nested solution "
            "entries, restored main distilled water and anaerobic N2 handling, "
            "added the pH range, and linked the TOGO M783 source duplicate."
        ),
        references=(MEDIADIVE_J758, JCM_758, JCM_187),
        variant_children=(M783_CHILD,),
    ),
    Target(
        path=TOGO_M783_PATH,
        record_id="CultureMech:010192",
        source_term="TOGO:M783",
        source_name="TOGO M783 / JCM Medium 758",
        imported_ingredients=TOGO_IMPORTED_INGREDIENTS,
        imported_solutions=TOGO_IMPORTED_SOLUTIONS,
        action="RESOLVED_TOGO_M783_DETHIOSULFOVIBRIO_II_MEDIUM",
        event_notes=(
            "Moved FeCl2 solution, Trace element solution, 10% CaCl2 x 2 H2O, "
            "12.5% Na2S2O3 x 5 H2O, and 5% Na2S x 9 H2O from empty solution "
            "stubs into structured solution entries, removed the N2 placeholder "
            "in favor of anaerobic preparation steps, corrected resazurin and "
            "water units, and linked the MediaDive J758 source duplicate."
        ),
        references=(TOGO_M783, JCM_758, JCM_187, MEDIADIVE_J758),
        parent_media=J758_PARENT,
    ),
)


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_record(_load(path), target)
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
