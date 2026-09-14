#!/usr/bin/env python3
"""Repair JCM/TOGO MJY Medium for Pyrolinea marinus records."""

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
JCM_J700_PATH = Path("bacterial/mjy_medium_for_pyrolinea_marinus.yaml")
TOGO_M721_PATH = Path("bacterial/TOGO_M721_MJY_Medium_For_Pyrolinea_Marinus.yaml")
TOGO_M722_PATH = Path("bacterial/TOGO_M722_MJY_Medium_For_Pyrolinea_Marinus.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m721_m722_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J700 = "https://mediadive.dsmz.de/medium/J700"
MEDIADIVE_J266 = "https://mediadive.dsmz.de/medium/J266"
MEDIADIVE_J268 = "https://mediadive.dsmz.de/medium/J268"
TOGO_M258 = "https://togomedium.org/medium/M258"
TOGO_M260 = "https://togomedium.org/medium/M260"
TOGO_M721 = "https://togomedium.org/medium/M721"
TOGO_M722 = "https://togomedium.org/medium/M722"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    source_term: str
    source_name: str
    imported_ingredients: tuple[Component, ...]
    imported_solutions: tuple[Component, ...]
    final_solutions: tuple[Component, ...]
    action: str
    event_notes: str
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, Any], ...] = ()
    include_rumen: bool = False


JCM_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("NH4Cl", "0.246305", "G_PER_L"),
    ("NaNO3", "0.492611", "G_PER_L"),
    ("Yeast extract", "0.985222", "G_PER_L"),
    ("NaHCO3", "5", "G_PER_L"),
    ("Na2S x 9 H2O", "10", "G_PER_L"),
    ("NaCl", "29.703", "G_PER_L"),
    ("K2HPO4", "0.138614", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.138614", "G_PER_L"),
    ("MgSO4 x 7 H2O", "3.36634", "G_PER_L"),
    ("MgCl2 x 6 H2O", "4.13861", "G_PER_L"),
    ("KCl", "0.326733", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.00049505", "G_PER_L"),
    ("Na2SeO3 x 5 H2O", "0.00049505", "G_PER_L"),
    ("Fe(NH4)2(SO4)2 x 6 H2O", "0.00990099", "G_PER_L"),
)

TOGO_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Yeast extract", "1", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("NaNO3", "0.5", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

TOGO_M721_IMPORTED_SOLUTIONS: tuple[Component, ...] = (
    ("MJ(-N) synthetic seawater (see Medium [M260])", "1", "G_PER_L"),
    ("8.0% NaHCO3 solution*", "5", "G_PER_L"),
    ("5.0% Na2S\u30fb9H2O solution", "10", "G_PER_L"),
)

TOGO_M722_IMPORTED_SOLUTIONS: tuple[Component, ...] = (
    *TOGO_M721_IMPORTED_SOLUTIONS,
    ("Rumen fluid, clarified (see Medium [M258])", "20", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Yeast extract", "1.0", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("NaNO3", "0.5", "G_PER_L"),
)

FINAL_BASE_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("MJ(-N) synthetic seawater", "1000.0", "ML_PER_L"),
    ("8% NaHCO3 solution", "5.0", "ML_PER_L"),
    ("5% Na2S x 9 H2O solution", "10.0", "ML_PER_L"),
)

FINAL_RUMEN_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    *FINAL_BASE_SOLUTION_SIGNATURE,
    ("Rumen fluid, clarified", "20.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MgCl2 x 6 H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "NiCl2 x 6 H2O": ("CHEBI:34887", "nickel dichloride"),
    "Na2SeO3 x 5 H2O": ("CHEBI:131361", "disodium selenite pentahydrate"),
    "Fe(NH4)2(SO4)2 x 6 H2O": (
        "CHEBI:76181",
        "ferrous ammonium sulfate hexahydrate",
    ),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "Na2S x 9 H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "NaNO3": ("CHEBI:63005", "sodium nitrate"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "MgSO4 x 7 H2O": ("SULFUR_SOURCE", "TRACE_ELEMENT"),
    "NiCl2 x 6 H2O": ("TRACE_ELEMENT",),
    "Na2SeO3 x 5 H2O": ("TRACE_ELEMENT",),
    "Fe(NH4)2(SO4)2 x 6 H2O": (
        "IRON_SOURCE",
        "NITROGEN_SOURCE",
        "SULFUR_SOURCE",
        "TRACE_ELEMENT",
    ),
    "NH4Cl": ("NITROGEN_SOURCE",),
    "NaNO3": ("NITROGEN_SOURCE",),
    "Yeast extract": ("NITROGEN_SOURCE",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "K2HPO4": ("BUFFER",),
    "NaHCO3": ("BUFFER",),
    "Na2S x 9 H2O": ("REDUCING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
    "L": "L",
}

M721_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M721_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010129",
    "name": "mjy_medium_for_pyrolinea_marinus",
    "notes": (
        "TOGO M721 imports the same JCM Medium 700 MJY Medium for Pyrolinea "
        "marinus formulation represented by MediaDive J700."
    ),
}

M722_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M722_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:010130",
    "name": "mjy_medium_for_pyrolinea_marinus",
    "notes": "Adds 20.0 ml/L Rumen fluid, clarified to JCM Medium 700 MJY Medium.",
}

JCM_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J700_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003046",
    "name": "mjy_medium_for_pyrolinea_marinus",
    "notes": (
        "TOGO M721 imports the same JCM Medium 700 MJY Medium for Pyrolinea "
        "marinus formulation represented by MediaDive J700."
    ),
}

JCM_SUPPLEMENT_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J700_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:003046",
    "name": "mjy_medium_for_pyrolinea_marinus",
    "notes": "Adds 20.0 ml/L Rumen fluid, clarified to JCM Medium 700 MJY Medium.",
}

M721_VARIANT_MODIFICATION = (
    "Same JCM Medium 700 MJY Medium for Pyrolinea marinus formulation as the "
    "MediaDive J700 source record."
)

M722_VARIANT_MODIFICATION = (
    "Adds 20.0 ml/L Rumen fluid, clarified from TOGO M258/JCM Medium 266 to "
    "JCM Medium 700 MJY Medium."
)

SOURCE_NOTE = (
    "MediaDive J700 and TOGO M721 describe JCM Medium 700 MJY Medium for "
    "Pyrolinea marinus as 1.0 L MJ(-N) synthetic seawater supplemented with "
    "1.0 g/L Yeast extract, 0.25 g/L NH4Cl, and 0.5 g/L NaNO3; after "
    "anaerobic autoclaving, 5.0 ml/L 8% NaHCO3 and 10.0 ml/L 5% Na2S x 9 H2O "
    "solutions are added and the final pH is checked at 6.0-6.5."
)

RUMEN_SOURCE_NOTE = (
    f"{SOURCE_NOTE} TOGO M722 additionally adds 20.0 ml/L Rumen fluid, "
    "clarified from TOGO M258/JCM Medium 266."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Mix 1.0 L MJ(-N) synthetic seawater, NH4Cl, NaNO3, and Yeast "
            "extract thoroughly; distribute the medium into culture vessels "
            "under a N2-CO2 (4:1, v/v) gas mixture, seal with butyl rubber "
            "stoppers, and autoclave."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "After cooling, add 5.0 ml/L 8% NaHCO3 solution and 10.0 ml/L "
            "5% Na2S x 9 H2O solution that were filter-sterilized or "
            "autoclaved and stored anaerobically."
        ),
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": (
            "Pressurize the culture vessels to 200 kPa N2-CO2 (4:1, v/v) "
            "and check the final pH at 6.0-6.5."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "MJ(-N) synthetic seawater can be replaced with a commercial "
            "synthetic seawater such as Jamarin S. For strain JCM 15506, "
            "inoculate with a 5-10% inoculum."
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
        _component("Yeast extract", "1.0", "G_PER_L", source=source),
        _component("NH4Cl", "0.25", "G_PER_L", source=source),
        _component("NaNO3", "0.5", "G_PER_L", source=source),
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
            _component("NaCl", "30.0", "G_PER_L", source="TOGO M260 / JCM Medium 268"),
            _component(
                "K2HPO4",
                "0.14",
                "G_PER_L",
                source="TOGO M260 / JCM Medium 268",
            ),
            _component(
                "CaCl2 x 2 H2O",
                "0.14",
                "G_PER_L",
                source="TOGO M260 / JCM Medium 268",
            ),
            _component(
                "MgSO4 x 7 H2O",
                "3.4",
                "G_PER_L",
                source="TOGO M260 / JCM Medium 268",
            ),
            _component(
                "MgCl2 x 6 H2O",
                "4.18",
                "G_PER_L",
                source="TOGO M260 / JCM Medium 268",
            ),
            _component("KCl", "0.33", "G_PER_L", source="TOGO M260 / JCM Medium 268"),
            _component(
                "NiCl2 x 6 H2O",
                "0.5",
                "MG_PER_L",
                source="TOGO M260 / JCM Medium 268",
            ),
            _component(
                "Na2SeO3 x 5 H2O",
                "0.5",
                "MG_PER_L",
                source="TOGO M260 / JCM Medium 268",
            ),
            _component(
                "Fe(NH4)2(SO4)2 x 6 H2O",
                "0.01",
                "G_PER_L",
                source="TOGO M260 / JCM Medium 268",
            ),
            _component(
                "Trace minerals",
                "10.0",
                "ML_PER_L",
                source="TOGO M260 / JCM Medium 268",
                notes=("TOGO M260/JCM Medium 268 adds 10.0 ml/L Trace minerals " "from TOGO M142."),
            ),
            _component(
                "Distilled water",
                "1.0",
                "L",
                source="TOGO M260 / JCM Medium 268",
                notes="TOGO M260/JCM Medium 268 lists 1.0 L Distilled water.",
            ),
        ],
        "preparation_notes": "Adjust pH to 7.5.",
    }


def _base_solutions(source: str) -> list[dict[str, Any]]:
    return [
        _mj_n_synthetic_seawater(source),
        {
            "preferred_term": "8% NaHCO3 solution",
            "concentration": {"value": "5.0", "unit": "ML_PER_L"},
            "source": source,
            "notes": f"{source} adds 5.0 ml/L 8% NaHCO3 solution after cooling.",
            "composition": [
                _component(
                    "NaHCO3",
                    "8.0",
                    "PERCENT_W_V",
                    source=source,
                    notes=f"{source} specifies the added NaHCO3 solution as 8% w/v.",
                )
            ],
            "preparation_notes": "Filter-sterilize or autoclave and store anaerobically.",
        },
        {
            "preferred_term": "5% Na2S x 9 H2O solution",
            "concentration": {"value": "10.0", "unit": "ML_PER_L"},
            "source": source,
            "notes": f"{source} adds 10.0 ml/L 5% Na2S x 9 H2O solution after cooling.",
            "composition": [
                _component(
                    "Na2S x 9 H2O",
                    "5.0",
                    "PERCENT_W_V",
                    source=source,
                    notes=(f"{source} specifies the added Na2S x 9 H2O solution " "as 5% w/v."),
                )
            ],
            "preparation_notes": "Autoclave and store anaerobically.",
        },
    ]


def _solutions(source: str, *, include_rumen: bool) -> list[dict[str, Any]]:
    solutions = _base_solutions(source)
    if include_rumen:
        solutions.append(
            {
                "preferred_term": "Rumen fluid, clarified",
                "concentration": {"value": "20.0", "unit": "ML_PER_L"},
                "source": "TOGO M722 / TOGO M258 / JCM Medium 266",
                "notes": (
                    "TOGO M722 adds 20.0 ml/L Rumen fluid, clarified from "
                    "TOGO M258/JCM Medium 266 after cooling."
                ),
                "preparation_notes": (
                    "TOGO M258/JCM Medium 266 prepares clarified rumen fluid by "
                    "preheating rumen content at 120 C for 15 min and using the "
                    "supernatant after centrifuging at 25,000 x g for 15 min."
                ),
            }
        )
    return solutions


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
        target.final_solutions,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_range", None)
    _put_after(repaired, "ph_range", {"min": 6.0, "max": 6.5}, "physical_state")
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _direct_ingredients(target.source_name)
    _put_after(
        repaired,
        "notes",
        RUMEN_SOURCE_NOTE if target.include_rumen else SOURCE_NOTE,
        "media_term",
    )
    _put_after(
        repaired,
        "solutions",
        _solutions(target.source_name, include_rumen=target.include_rumen),
        "ingredients",
    )
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "solutions",
    )
    repaired.pop("sterilization", None)

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


TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM_J700_PATH,
        record_id="CultureMech:003046",
        source_term="mediadive.medium:J700",
        source_name="MediaDive J700 / JCM Medium 700",
        imported_ingredients=JCM_IMPORTED_INGREDIENTS,
        imported_solutions=(),
        final_solutions=FINAL_BASE_SOLUTION_SIGNATURE,
        action="RESOLVED_JCM_700_MJY_MEDIUM",
        event_notes=(
            "Restored JCM Medium 700 direct ingredients from flattened "
            "MediaDive concentrations, moved MJ(-N) synthetic seawater, "
            "8% NaHCO3, and 5% Na2S x 9 H2O into structured solution "
            "entries, added the final pH range and anaerobic gas handling "
            "steps, and linked the TOGO M721/M722 variants."
        ),
        references=(MEDIADIVE_J700, MEDIADIVE_J268, TOGO_M260),
        variant_children=(M721_CHILD, M722_CHILD),
    ),
    Target(
        path=TOGO_M721_PATH,
        record_id="CultureMech:010129",
        source_term="TOGO:M721",
        source_name="TOGO M721 / JCM Medium 700",
        imported_ingredients=TOGO_IMPORTED_INGREDIENTS,
        imported_solutions=TOGO_M721_IMPORTED_SOLUTIONS,
        final_solutions=FINAL_BASE_SOLUTION_SIGNATURE,
        action="RESOLVED_TOGO_M721_MJY_MEDIUM",
        event_notes=(
            "Moved MJ(-N) synthetic seawater, 8% NaHCO3, and 5% Na2S x 9 H2O "
            "from empty solution stubs into structured solution entries, "
            "removed gas placeholders in favor of anaerobic preparation steps, "
            "added the final pH range, and linked the MediaDive J700 source "
            "duplicate."
        ),
        references=(TOGO_M721, MEDIADIVE_J700, MEDIADIVE_J268, TOGO_M260),
        parent_media=JCM_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(M721_VARIANT_MODIFICATION,),
    ),
    Target(
        path=TOGO_M722_PATH,
        record_id="CultureMech:010130",
        source_term="TOGO:M722",
        source_name="TOGO M722 / JCM Medium 700-2",
        imported_ingredients=TOGO_IMPORTED_INGREDIENTS,
        imported_solutions=TOGO_M722_IMPORTED_SOLUTIONS,
        final_solutions=FINAL_RUMEN_SOLUTION_SIGNATURE,
        action="RESOLVED_TOGO_M722_MJY_RUMEN_MEDIUM",
        event_notes=(
            "Moved MJ(-N) synthetic seawater, 8% NaHCO3, 5% Na2S x 9 H2O, "
            "and Rumen fluid, clarified from empty solution stubs into "
            "structured solution entries, removed gas placeholders in favor "
            "of anaerobic preparation steps, added the final pH range, and "
            "linked the MediaDive J700 base recipe."
        ),
        references=(
            TOGO_M722,
            TOGO_M258,
            MEDIADIVE_J266,
            MEDIADIVE_J700,
            MEDIADIVE_J268,
            TOGO_M260,
        ),
        parent_media=JCM_SUPPLEMENT_PARENT,
        variant_relationship="SUPPLEMENTED_VARIANT",
        variant_modifications=(M722_VARIANT_MODIFICATION,),
        include_rumen=True,
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
