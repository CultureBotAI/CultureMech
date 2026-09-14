#!/usr/bin/env python3
"""Repair MediaDive/TOGO JCM 276/894 Castenholz Thermus records."""

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
J276_PATH = Path("bacterial/JCM_J276_CASTENHOLZ_MEDIUM.yaml")
J894_PATH = Path("bacterial/microaerophilic_thermus_medium.yaml")
M935_PATH = Path("bacterial/TOGO_M935_Microaerophilic_Thermus_Medium.yaml")
CASTENHOLZ_3963_PATH = Path("bacterial/mediadive_3963_Castenholz_basal_salt_solution.yaml")
NITSCH_3964_PATH = Path("bacterial/mediadive_3964_Nitsch_s_trace_elements.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m935_microaerophilic_thermus_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J276 = "https://mediadive.dsmz.de/medium/J276"
MEDIADIVE_J894 = "https://mediadive.dsmz.de/medium/J894"
JCM_276 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=276"
JCM_894 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=894"
JCM_273 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=273"
TOGO_M266 = "https://togomedium.org/medium/M266"
TOGO_M935 = "https://togomedium.org/medium/M935"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...], tuple[Any, ...]]


@dataclass(frozen=True)
class MediumTarget:
    path: Path
    record_id: str
    source_term: str
    source_name: str
    imported_ingredients: tuple[Component, ...]
    imported_solutions: tuple[SolutionSignature, ...]
    final_ingredients: tuple[Component, ...]
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
    microaerophilic: bool = False


@dataclass(frozen=True)
class SolutionTarget:
    path: Path
    record_id: str
    solution_term: str
    source_name: str
    imported_composition: tuple[Component, ...]
    final_composition: tuple[Component, ...]
    imported_solutions: tuple[SolutionSignature, ...]
    final_solutions: tuple[SolutionSignature, ...]
    preparation_notes: str
    notes: str
    action: str
    event_notes: str
    references: tuple[str, ...]


FLATTENED_J276_INGREDIENTS: tuple[Component, ...] = (
    ("Tryptone", "1", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("Nitrilotriacetic acid", "0.980392", "G_PER_L"),
    ("CaSO4 x 2 H2O", "0.588235", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.980392", "G_PER_L"),
    ("NaCl", "0.0784314", "G_PER_L"),
    ("KNO3", "1.0098", "G_PER_L"),
    ("NaNO3", "6.7549", "G_PER_L"),
    ("Na2HPO4", "1.08824", "G_PER_L"),
    ("FeCl3 x 6 H2O", "10", "G_PER_L"),
)

TOGO_M935_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "900", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "1", "G_PER_L"),
    ("Tryptone (BD-Difco)", "1", "G_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Oxygen gas", "variable", "VARIABLE"),
)

TOGO_M935_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("Castenholz basal salt solution (see Medium [M266])", "100", "G_PER_L", (), ()),
)

CASTENHOLZ_IMPORTED_COMPOSITION: tuple[Component, ...] = (
    ("Nitrilotriacetic acid", "0.980392", "G_PER_L"),
    ("CaSO4 x 2 H2O", "0.588235", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.980392", "G_PER_L"),
    ("NaCl", "0.0784314", "G_PER_L"),
    ("KNO3", "1.0098", "G_PER_L"),
    ("NaNO3", "6.7549", "G_PER_L"),
    ("Na2HPO4", "1.08824", "G_PER_L"),
    ("FeCl3 x 6 H2O", "9.80392156862745", "PERCENT_V_V"),
    ("Distilled water", "980.3921568627451", "PERCENT_V_V"),
)

NITSCH_IMPORTED_COMPOSITION: tuple[Component, ...] = (
    ("H2SO4", "0.5", "PERCENT_V_V"),
    ("MnSO4 x n H2O", "2.2", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.5", "G_PER_L"),
    ("H3BO3", "0.5", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.016", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.025", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.046", "G_PER_L"),
    ("Distilled water", "1000", "PERCENT_V_V"),
)

PLACEHOLDER_INGREDIENTS: tuple[Component, ...] = (
    ("See source for composition", "variable", "VARIABLE"),
)

CASTENHOLZ_MEDIUM_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "900.0", "ML_PER_L"),
    ("Yeast extract (BD-Difco)", "1.0", "G_PER_L"),
    ("Tryptone (BD-Difco)", "1.0", "G_PER_L"),
)

MICROAEROPHILIC_INGREDIENTS: tuple[Component, ...] = (
    *CASTENHOLZ_MEDIUM_INGREDIENTS,
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Oxygen gas", "variable", "VARIABLE"),
)

CASTENHOLZ_COMPOSITION: tuple[Component, ...] = (
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("MgSO4 x 7 H2O", "1.0", "G_PER_L"),
    ("NaCl", "0.08", "G_PER_L"),
    ("NaNO3", "6.89", "G_PER_L"),
    ("Nitrilotriacetic acid", "1.0", "G_PER_L"),
    ("KNO3", "1.03", "G_PER_L"),
    ("Na2HPO4", "1.11", "G_PER_L"),
    ("CaSO4 x 2 H2O", "0.6", "G_PER_L"),
)

FECL3_SOLUTION_COMPOSITION: tuple[Component, ...] = (("FeCl3 x 6 H2O", "0.03", "PERCENT_W_V"),)

NITSCH_COMPOSITION: tuple[Component, ...] = (
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.025", "G_PER_L"),
    ("H3BO3", "0.5", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.046", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.5", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.016", "G_PER_L"),
    ("MnSO4 x n H2O", "2.2", "G_PER_L"),
    ("H2SO4", "0.5", "ML_PER_L"),
)

CASTENHOLZ_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("FeCl3 x 6 H2O solution (0.03%)", "10.0", "ML_PER_L", FECL3_SOLUTION_COMPOSITION, ()),
    ("Nitsch's trace elements", "10.0", "ML_PER_L", NITSCH_COMPOSITION, ()),
)

FINAL_CASTENHOLZ_SOLUTION: tuple[SolutionSignature, ...] = (
    (
        "Castenholz basal salt solution",
        "100.0",
        "ML_PER_L",
        CASTENHOLZ_COMPOSITION,
        CASTENHOLZ_SOLUTIONS,
    ),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "yeast extract"),
    "Tryptone (BD-Difco)": ("MICRO:0000182", "tryptone"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "Oxygen gas": ("CHEBI:15379", "dioxygen"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaNO3": ("CHEBI:63005", "sodium nitrate"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "KNO3": ("CHEBI:63043", "potassium nitrate"),
    "Na2HPO4": ("CHEBI:34683", "disodium hydrogenphosphate"),
    "CaSO4 x 2 H2O": ("CHEBI:32583", "calcium sulfate dihydrate"),
    "FeCl3 x 6 H2O": ("CHEBI:86254", "iron trichloride hexahydrate"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "MnSO4 x n H2O": ("CHEBI:86360", "manganese(II) sulfate"),
    "H2SO4": ("CHEBI:26836", "sulfuric acid"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Yeast extract (BD-Difco)": ("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
    "Tryptone (BD-Difco)": ("PROTEIN_SOURCE",),
    "NaNO3": ("NITROGEN_SOURCE",),
    "FeCl3 x 6 H2O": ("IRON_SOURCE",),
    "Na2MoO4 x 2 H2O": ("TRACE_ELEMENT",),
    "H3BO3": ("TRACE_ELEMENT",),
    "CoCl2 x 6 H2O": ("TRACE_ELEMENT",),
    "ZnSO4 x 7 H2O": ("TRACE_ELEMENT",),
    "CuSO4 x 5 H2O": ("TRACE_ELEMENT",),
    "MnSO4 x n H2O": ("TRACE_ELEMENT",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Na2HPO4": ("BUFFER",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
    "VARIABLE": "variable concentration",
}

J894_CHILD = {
    "path": f"data/normalized_yaml/{J894_PATH}",
    "relationship": "PH_VARIANT",
    "id": "CultureMech:003243",
    "name": "microaerophilic_thermus_medium",
    "notes": (
        "JCM Medium 894 uses the JCM Medium 276 Castenholz formulation "
        "adjusted to pH 8.0 and cultivated under a 99:1 N2/O2 gas atmosphere."
    ),
}

M269_CHILD = {
    "path": "data/normalized_yaml/bacterial/TOGO_M269_Castenholz_Medium.yaml",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:009252",
    "name": "castenholz_medium",
    "notes": "TOGO M269 is a source duplicate of JCM Medium 276.",
}

M935_CHILD = {
    "path": f"data/normalized_yaml/{M935_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010357",
    "name": "microaerophilic_thermus_medium",
    "notes": (
        "TOGO M935 imports the same JCM Medium 894 Microaerophilic Thermus "
        "Medium formulation represented by MediaDive J894."
    ),
}

J276_PARENT = {
    "path": f"data/normalized_yaml/{J276_PATH}",
    "relationship": "PH_VARIANT",
    "id": "CultureMech:002633",
    "name": "castenholz_medium",
    "notes": J894_CHILD["notes"],
}

J894_PARENT = {
    "path": f"data/normalized_yaml/{J894_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003243",
    "name": "microaerophilic_thermus_medium",
    "notes": M935_CHILD["notes"],
}

J276_NOTE = (
    "JCM Medium 276 / Castenholz Medium lists 900.0 ml distilled water, "
    "1.0 g/L BD-Difco yeast extract, 1.0 g/L BD-Difco tryptone, and "
    "100.0 ml/L Castenholz basal salt solution from JCM Medium 273, then "
    "adjusts the final medium to pH 8.2 with NaOH."
)

J894_NOTE = (
    "JCM Medium 894 / Microaerophilic Thermus Medium uses JCM Medium 276, "
    "adjusts the final medium to pH 8.0, and cultivates under a 99:1 "
    "N2/O2 gas atmosphere. MediaDive J894 and TOGO M935 report the same "
    "JCM recipe."
)

J276_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix 900.0 ml/L distilled water, 1.0 g/L BD-Difco yeast "
            "extract, 1.0 g/L BD-Difco tryptone, and 100.0 ml/L "
            "Castenholz basal salt solution."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 8.2 with NaOH.",
    },
)

MICROAEROPHILIC_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Use the JCM Medium 276 Castenholz formulation with 900.0 ml/L "
            "distilled water, 1.0 g/L BD-Difco yeast extract, 1.0 g/L "
            "BD-Difco tryptone, and 100.0 ml/L Castenholz basal salt solution."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 8.0 with NaOH.",
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


def _composition(source: str, rows: tuple[Component, ...]) -> list[dict[str, Any]]:
    return [_component(name, value, unit, source=source) for name, value, unit in rows]


def _fecl3_solution(source: str) -> dict[str, Any]:
    term = _term(*GROUNDINGS["FeCl3 x 6 H2O"])
    return {
        "preferred_term": "FeCl3 x 6 H2O solution (0.03%)",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": source,
        "notes": f"{source} adds 10.0 ml/L FeCl3 x 6 H2O solution at 0.03% w/v.",
        "term": term,
        "mediaingredientmech_chebi_term": dict(term),
        "composition": _composition(source, FECL3_SOLUTION_COMPOSITION),
    }


def _nitsch_solution(source: str) -> dict[str, Any]:
    return {
        "preferred_term": "Nitsch's trace elements",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": source,
        "notes": f"{source} adds 10.0 ml/L Nitsch's trace elements.",
        "term": _term("mediadive.solution:3964", "Nitsch's trace elements"),
        "culturemech_term": _term("CultureMech:013023", "Nitsch's trace elements"),
        "composition": _composition(source, NITSCH_COMPOSITION),
        "preparation_notes": (
            "Prepare the Nitsch trace-elements stock with 1.0 L distilled "
            "water, mineral salts, and 0.5 ml/L H2SO4."
        ),
    }


def _castenholz_solution(source: str) -> dict[str, Any]:
    return {
        "preferred_term": "Castenholz basal salt solution",
        "concentration": {"value": "100.0", "unit": "ML_PER_L"},
        "source": source,
        "notes": (
            f"{source} adds 100.0 ml/L Castenholz basal salt solution " "defined by JCM Medium 273."
        ),
        "term": _term("mediadive.solution:3963", "Castenholz basal salt solution"),
        "culturemech_term": _term("CultureMech:013022", "Castenholz basal salt solution"),
        "composition": _composition("JCM Medium 273", CASTENHOLZ_COMPOSITION),
        "solutions": [
            _fecl3_solution("JCM Medium 273"),
            _nitsch_solution("JCM Medium 273"),
        ],
        "preparation_notes": "Adjust pH to 8.2.",
    }


def _ingredients(target: MediumTarget) -> list[dict[str, Any]]:
    rows = _composition(target.source_name, target.final_ingredients)
    if not target.microaerophilic:
        return rows

    for row in rows[-2:]:
        row["notes"] = (
            f"{target.source_name} uses {row['preferred_term']} in a 99:1 gas atmosphere."
        )
    return rows


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
                _solution_signature(row.get("solutions") or [], f"{label}.solutions"),
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

    if _signature(doc.get("ingredients"), "ingredients") not in (
        target.imported_ingredients,
        target.final_ingredients,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    final_solutions = FINAL_CASTENHOLZ_SOLUTION
    if _solution_signature(doc.get("solutions"), "solutions") not in (
        target.imported_solutions,
        final_solutions,
    ):
        raise ValueError(f"{target.path}: solution signature drifted")


def _ensure_solution_target(doc: dict[str, Any], target: SolutionTarget) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')}")
    if _term_id(doc) != target.solution_term:
        raise ValueError(f"{target.path}: expected solution {target.solution_term}")
    if _signature(doc.get("composition"), "composition") not in (
        target.imported_composition,
        target.final_composition,
    ):
        raise ValueError(f"{target.path}: composition signature drifted")
    if _solution_signature(doc.get("solutions"), "solutions") not in (
        target.imported_solutions,
        target.final_solutions,
    ):
        raise ValueError(f"{target.path}: solution signature drifted")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        PLACEHOLDER_INGREDIENTS,
        (),
    ):
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
    for key in ("term", "mediaingredientmech_chebi_term", "culturemech_term"):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _solution_components(solution: dict[str, Any]) -> list[dict[str, Any]]:
    components = [row for row in solution.get("composition") or [] if isinstance(row, dict)]
    for child in solution.get("solutions") or []:
        if not isinstance(child, dict):
            continue
        components.extend(_solution_components(child) or [child])
    return components


def _all_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    rows.extend(row for row in doc.get("composition") or [] if isinstance(row, dict))
    for solution in doc.get("solutions") or []:
        if isinstance(solution, dict):
            rows.extend(_solution_components(solution) or [solution])
    return rows


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation", "resolved_reference"):
        while obsolete in flags:
            flags.remove(obsolete)

    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)

    if all(_grounded(row) for row in _all_components(doc)):
        while "has_unmapped_ingredients" in flags:
            flags.remove("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")


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


def repair_medium_record(doc: dict[str, Any], target: MediumTarget) -> dict[str, Any]:
    _ensure_medium_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    repaired["ingredients"] = _ingredients(target)
    _put_after(repaired, "solutions", [_castenholz_solution(target.source_name)], "ingredients")
    _put_after(repaired, "notes", target.source_note, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in target.preparation_steps],
        "solutions",
    )
    repaired.pop("kg_microbe_match", None)

    if target.microaerophilic:
        repaired["incubation_atmosphere"] = "MICROAEROPHILIC"
        repaired["aeration"] = "N2-O2 (99:1, v/v) gas atmosphere"
    else:
        repaired.pop("incubation_atmosphere", None)
        repaired.pop("aeration", None)

    _ensure_references(repaired, target.references)
    if target.parent_media is None:
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
        repaired.pop("variant_modifications", None)
    else:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), "references")
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


def repair_solution_record(doc: dict[str, Any], target: SolutionTarget) -> dict[str, Any]:
    _ensure_solution_target(doc, target)

    repaired = copy.deepcopy(doc)
    source = target.source_name
    repaired["composition"] = _composition(source, target.final_composition)
    if target.final_solutions:
        _put_after(
            repaired,
            "solutions",
            [_fecl3_solution(source), _nitsch_solution(source)],
            "composition",
        )
    else:
        repaired.pop("solutions", None)
    repaired.pop("ingredients", None)
    repaired["preparation_notes"] = target.preparation_notes
    _put_after(repaired, "notes", target.notes, "preparation_notes")
    _ensure_references(repaired, target.references)
    _ensure_flags(repaired)
    _append_event(
        repaired,
        action=target.action,
        references=target.references,
        notes=target.event_notes,
    )
    return repaired


TARGETS: tuple[MediumTarget, ...] = (
    MediumTarget(
        path=J276_PATH,
        record_id="CultureMech:002633",
        source_term="mediadive.medium:J276",
        source_name="MediaDive J276 / JCM Medium 276",
        imported_ingredients=FLATTENED_J276_INGREDIENTS,
        imported_solutions=(),
        final_ingredients=CASTENHOLZ_MEDIUM_INGREDIENTS,
        ph_value=8.2,
        source_note=J276_NOTE,
        preparation_steps=J276_STEPS,
        action="RESOLVED_MEDIADIVE_J276_CASTENHOLZ_MEDIUM",
        event_notes=(
            "Restored the JCM Medium 276 direct composition with 900.0 "
            "ml/L water, moved the flattened Castenholz stock salts into "
            "a 100.0 ml/L nested solution, expanded the Castenholz and "
            "Nitsch stock definitions from JCM Medium 273, and linked the "
            "JCM Medium 894 pH/atmosphere variant."
        ),
        references=(MEDIADIVE_J276, JCM_276, TOGO_M266, JCM_273),
        variant_children=(J894_CHILD, M269_CHILD),
    ),
    MediumTarget(
        path=J894_PATH,
        record_id="CultureMech:003243",
        source_term="mediadive.medium:J894",
        source_name="MediaDive J894 / JCM Medium 894",
        imported_ingredients=FLATTENED_J276_INGREDIENTS,
        imported_solutions=(),
        final_ingredients=MICROAEROPHILIC_INGREDIENTS,
        ph_value=8.0,
        source_note=J894_NOTE,
        preparation_steps=MICROAEROPHILIC_STEPS,
        action="RESOLVED_MEDIADIVE_J894_MICROAEROPHILIC_THERMUS",
        event_notes=(
            "Replaced the flattened JCM Medium 276 stock salts with the "
            "source 100.0 ml/L Castenholz basal salt solution, corrected "
            "JCM Medium 894 to a pH 8.0 variant under 99:1 N2/O2, "
            "grounded the gases, and linked TOGO M935 as a source duplicate."
        ),
        references=(MEDIADIVE_J894, JCM_894, MEDIADIVE_J276, JCM_276, TOGO_M266, JCM_273),
        parent_media=J276_PARENT,
        variant_relationship="PH_VARIANT",
        variant_modifications=(J894_CHILD["notes"],),
        variant_children=(M935_CHILD,),
        microaerophilic=True,
    ),
    MediumTarget(
        path=M935_PATH,
        record_id="CultureMech:010357",
        source_term="TOGO:M935",
        source_name="TOGO M935 / JCM Medium 894",
        imported_ingredients=TOGO_M935_INGREDIENTS,
        imported_solutions=TOGO_M935_SOLUTIONS,
        final_ingredients=MICROAEROPHILIC_INGREDIENTS,
        ph_value=8.0,
        source_note=J894_NOTE,
        preparation_steps=MICROAEROPHILIC_STEPS,
        action="RESOLVED_TOGO_M935_MICROAEROPHILIC_THERMUS",
        event_notes=(
            "Corrected water from 900 g/L to 900.0 ml/L, removed NaOH "
            "from the ingredient list because it is only the pH titrant, "
            "grounded yeast extract, tryptone, and the 99:1 N2/O2 gases, "
            "expanded the Castenholz basal salt stock from JCM Medium 273, "
            "and linked the MediaDive J894 source duplicate."
        ),
        references=(
            TOGO_M935,
            MEDIADIVE_J894,
            JCM_894,
            MEDIADIVE_J276,
            JCM_276,
            TOGO_M266,
            JCM_273,
        ),
        parent_media=J894_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(M935_CHILD["notes"],),
        microaerophilic=True,
    ),
)

SOLUTION_TARGETS: tuple[SolutionTarget, ...] = (
    SolutionTarget(
        path=CASTENHOLZ_3963_PATH,
        record_id="CultureMech:013022",
        solution_term="mediadive.solution:3963",
        source_name="MediaDive solution 3963 / JCM Medium 273",
        imported_composition=CASTENHOLZ_IMPORTED_COMPOSITION,
        final_composition=CASTENHOLZ_COMPOSITION,
        imported_solutions=(),
        final_solutions=CASTENHOLZ_SOLUTIONS,
        preparation_notes=(
            "Mix 1.0 L distilled water, the Castenholz salts, 10.0 ml/L "
            "0.03% FeCl3 x 6 H2O solution, and 10.0 ml/L Nitsch's trace "
            "elements; adjust the stock to pH 8.2."
        ),
        notes=(
            "MediaDive solution 3963 is the Castenholz basal salt solution "
            "from JCM Medium 273 used by JCM Medium 276 at 100.0 ml/L."
        ),
        action="RESOLVED_MEDIADIVE_3963_CASTENHOLZ_BASAL_SALT",
        event_notes=(
            "Restored the JCM Medium 273 Castenholz stock concentrations, "
            "corrected false percent-volume FeCl3 and water rows to the "
            "source FeCl3 stock addition plus 1000.0 ml/L water, restored "
            "the missing Nitsch's trace-elements addition, and removed the "
            "placeholder top-level ingredient."
        ),
        references=(MEDIADIVE_J276, TOGO_M266, JCM_273),
    ),
    SolutionTarget(
        path=NITSCH_3964_PATH,
        record_id="CultureMech:013023",
        solution_term="mediadive.solution:3964",
        source_name="MediaDive solution 3964 / JCM Medium 273",
        imported_composition=NITSCH_IMPORTED_COMPOSITION,
        final_composition=NITSCH_COMPOSITION,
        imported_solutions=(),
        final_solutions=(),
        preparation_notes=(
            "Mix the Nitsch trace-elements salts and 0.5 ml/L H2SO4 in " "1.0 L distilled water."
        ),
        notes=(
            "MediaDive solution 3964 is the Nitsch's trace-elements stock "
            "used by Castenholz basal salt solution at 10.0 ml/L."
        ),
        action="RESOLVED_MEDIADIVE_3964_NITSCH_TRACE_ELEMENTS",
        event_notes=(
            "Corrected the Nitsch stock water and H2SO4 rows from false "
            "percent-volume units to the source 1000.0 ml/L and 0.5 ml/L "
            "amounts, replaced upstream mediadive.compound groundings with "
            "direct ontology mappings, and removed the placeholder "
            "top-level ingredient."
        ),
        references=(MEDIADIVE_J276, TOGO_M266, JCM_273),
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
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed: list[Path] = []
    for path, doc in plans.items():
        rendered = dump_record(doc)
        if path.read_text(encoding="utf-8") != rendered:
            changed.append(path)
            if args.apply:
                write_record(path, doc)

    action = "wrote" if args.apply else "would write"
    for path in changed:
        print(f"{action} {path.relative_to(REPO)}")
    print(f"{action} {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
