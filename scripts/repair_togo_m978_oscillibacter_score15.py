#!/usr/bin/env python3
"""Repair the TOGO M978 / JCM J932 Oscillibacter GH Medium duplicate cluster."""

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
MEDIADIVE_J932_PATH = Path("bacterial/oscillibacter_gh_medium.yaml")
TOGO_M978_PATH = Path("bacterial/TOGO_M978_Oscillibacter_GH_Medium.yaml")
SOLUTION_4943_PATH = Path("bacterial/mediadive_4943_Main_sol_J932.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m978_oscillibacter_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J932 = "https://mediadive.dsmz.de/medium/J932"
TOGO_M978 = "https://togomedium.org/medium/M978"
TOGO_M180 = "https://togomedium.org/medium/M180"
TOGO_M190 = "https://togomedium.org/medium/M190"
JCM_932 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=932"
JCM_187 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class MediaTarget:
    path: Path
    record_id: str
    source_term: str
    source_name: str
    imported_ingredients: tuple[Component, ...]
    imported_solutions: tuple[Component, ...]
    action: str
    references: tuple[str, ...]
    event_notes: str
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()


TOGO_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Tween 80", "0.03", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "5", "G_PER_L"),
    ("Polypeptone peptone (BD-BBL)", "5", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

TOGO_IMPORTED_SOLUTIONS: tuple[Component, ...] = (
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L"),
    ("FeCl2 solution (see Medium [M180])", "1", "G_PER_L"),
    ("Trace element solution (see Medium [M180])", "1", "G_PER_L"),
)

MEDIADIVE_J932_IMPORTED: tuple[Component, ...] = (
    ("Yeast extract", "4.94071", "G_PER_L"),
    ("Polypeptone", "4.94071", "G_PER_L"),
    ("Tween 80", "0.0296443", "G_PER_L"),
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

SOLUTION_4943_IMPORTED: tuple[Component, ...] = (
    ("Yeast extract", "4.94071", "G_PER_L"),
    ("Polypeptone", "4.94071", "G_PER_L"),
    ("Tween 80", "0.0296443", "G_PER_L"),
    ("Distilled water", "988.1422924901185", "PERCENT_V_V"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Yeast extract (BD-Difco)", "4.94071", "G_PER_L"),
    ("Polypeptone peptone (BD-BBL)", "4.94071", "G_PER_L"),
    ("Tween 80", "0.0296443", "G_PER_L"),
    ("Distilled water", "988.142", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Trace vitamins", "9.88142", "ML_PER_L"),
    ("FeCl2 solution", "0.988142", "ML_PER_L"),
    ("Trace element solution", "0.988142", "ML_PER_L"),
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

FECL2_COMPOSITION: tuple[Component, ...] = (
    ("HCl", "2.5", "G_PER_L"),
    ("FeCl2 x 4 H2O", "1.5", "G_PER_L"),
    ("Distilled water", "990.0", "ML_PER_L"),
)

TRACE_ELEMENT_COMPOSITION: tuple[Component, ...] = (
    ("ZnCl2", "70.0", "MG_PER_L"),
    ("MnCl2 x 4 H2O", "100.0", "MG_PER_L"),
    ("H3BO3", "6.0", "MG_PER_L"),
    ("CoCl2 x 6 H2O", "190.0", "MG_PER_L"),
    ("CuCl2 x 2 H2O", "2.0", "MG_PER_L"),
    ("NiCl2 x 6 H2O", "24.0", "MG_PER_L"),
    ("Na2MoO4 x 2 H2O", "36.0", "MG_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Biotin": ("CHEBI:15956", "biotin"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2 H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl2 x 4 H2O": ("CHEBI:86249", "iron dichloride tetrahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "HCl": ("CHEBI:17883", "hydrogen chloride"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "NiCl2 x 6 H2O": ("CHEBI:34887", "nickel dichloride"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Polypeptone peptone (BD-BBL)": ("FOODON:03315306", "Polypeptone"),
    "Pyridoxine hydrochloride": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Tween 80": ("CHEBI:53426", "polysorbate 80"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "yeast extract"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Biotin": ("VITAMIN_SOURCE",),
    "CoCl2 x 6 H2O": ("TRACE_ELEMENT",),
    "CuCl2 x 2 H2O": ("TRACE_ELEMENT",),
    "FeCl2 x 4 H2O": ("IRON_SOURCE", "TRACE_ELEMENT"),
    "Folic acid": ("VITAMIN_SOURCE",),
    "H3BO3": ("TRACE_ELEMENT",),
    "Lipoic acid": ("VITAMIN_SOURCE", "COFACTOR_PROVIDER"),
    "MnCl2 x 4 H2O": ("TRACE_ELEMENT",),
    "Na2MoO4 x 2 H2O": ("TRACE_ELEMENT",),
    "NiCl2 x 6 H2O": ("TRACE_ELEMENT",),
    "Nicotinic acid": ("VITAMIN_SOURCE",),
    "p-Aminobenzoic acid": ("VITAMIN_SOURCE",),
    "Pyridoxine hydrochloride": ("VITAMIN_SOURCE",),
    "Riboflavin": ("VITAMIN_SOURCE",),
    "Thiamine HCl": ("VITAMIN_SOURCE",),
    "Vitamin B12": ("VITAMIN_SOURCE", "COFACTOR_PROVIDER"),
    "Yeast extract (BD-Difco)": ("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
    "ZnCl2": ("TRACE_ELEMENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
}

SOURCE_NOTE = (
    "JCM Medium 932 lists 5.0 g yeast extract from BD-Difco, 5.0 g "
    "Polypeptone peptone from BD-BBL, 0.03 g Tween 80, 10.0 ml Trace "
    "vitamins from JCM Medium 197, 1.0 ml FeCl2 solution from JCM Medium "
    "187, 1.0 ml Trace element solution from JCM Medium 187, and 1.0 L "
    "distilled water; after mixing, adjust pH to 6.0, distribute under N2, "
    "seal with butyl rubber stoppers, and autoclave."
)

PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix yeast extract, Polypeptone peptone, Tween 80, distilled "
            "water, 9.88142 ml/L Trace vitamins, 0.988142 ml/L FeCl2 "
            "solution, and 0.988142 ml/L Trace element solution."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 6.0.",
    },
    {
        "step_number": 3,
        "action": "ALIQUOT",
        "description": (
            "Distribute the medium into culture vessels under a N2 gas "
            "stream and seal with butyl rubber stoppers."
        ),
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": "Autoclave the sealed medium.",
    },
]

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M978_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010404",
    "name": "oscillibacter_gh_medium",
    "notes": (
        "TOGO M978 imports the same JCM Medium 932 Oscillibacter GH Medium "
        "formulation represented by MediaDive J932."
    ),
}

J932_PARENT = {
    "path": f"data/normalized_yaml/{MEDIADIVE_J932_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003280",
    "name": "oscillibacter_gh_medium",
    "notes": TOGO_CHILD["notes"],
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
    identifier, label = GROUNDINGS[preferred_term]
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": _term(identifier, label),
    }
    if identifier.startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(identifier, label)
    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)
    return row


def _composition(source: str, rows: tuple[Component, ...]) -> list[dict[str, Any]]:
    return [
        _component(preferred_term, value, unit, source=source)
        for preferred_term, value, unit in rows
    ]


def _direct_ingredients(source: str) -> list[dict[str, Any]]:
    rows = _composition(source, FINAL_INGREDIENT_SIGNATURE)
    rows[-1]["notes"] = (
        f"{source} makes 1.012 L medium from 1.0 L distilled water plus 12.0 "
        "ml stock additions, equivalent to 988.142 ml/L distilled water."
    )
    return rows


def _stock_solution(
    preferred_term: str,
    volume: str,
    stock_source: str,
    rows: tuple[Component, ...],
    *,
    source: str,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    stock = {
        "preferred_term": preferred_term,
        "concentration": {"value": volume, "unit": "ML_PER_L"},
        "source": f"{source} / {stock_source}",
        "notes": f"{source} adds {volume} ml/L {preferred_term}.",
        "composition": _composition(stock_source, rows),
    }
    if preparation_notes:
        stock["preparation_notes"] = preparation_notes
    return stock


def _solutions(source: str) -> list[dict[str, Any]]:
    return [
        _stock_solution(
            "Trace vitamins",
            "9.88142",
            "JCM Medium 197",
            TRACE_VITAMIN_COMPOSITION,
            source=source,
            preparation_notes="JCM Medium 197 prints the Trace vitamins subrecipe per liter.",
        ),
        _stock_solution(
            "FeCl2 solution",
            "0.988142",
            "JCM Medium 187",
            FECL2_COMPOSITION,
            source=source,
            preparation_notes="First dissolve FeCl2 in the HCl, then dilute in water.",
        ),
        _stock_solution(
            "Trace element solution",
            "0.988142",
            "JCM Medium 187",
            TRACE_ELEMENT_COMPOSITION,
            source=source,
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


def _ensure_media(doc: dict[str, Any], target: MediaTarget) -> None:
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


def _ensure_solution_4943(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:013869":
        raise ValueError(f"expected CultureMech:013869, found {doc.get('id')}")
    term = doc.get("term")
    if not isinstance(term, dict) or term.get("id") != "mediadive.solution:4943":
        raise ValueError("expected mediadive.solution:4943")

    composition_signature = _signature(doc.get("composition"), "composition")
    if composition_signature not in (
        SOLUTION_4943_IMPORTED,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("solution 4943 composition signature drifted")

    solution_signature = _signature(doc.get("solutions"), "solutions")
    if solution_signature not in ((), FINAL_SOLUTION_SIGNATURE):
        raise ValueError("solution 4943 nested solution signature drifted")


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
        "has_unmapped_ingredients",
    ):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
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


def repair_media_record(doc: dict[str, Any], target: MediaTarget) -> dict[str, Any]:
    _ensure_media(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 6.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("kg_microbe_match", None)
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
            "sterilization",
        )
        _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
        _put_after(
            repaired,
            "variant_modifications",
            [J932_PARENT["notes"]],
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


def repair_solution_4943(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_solution_4943(doc)

    source = "MediaDive solution 4943 / JCM Medium 932"
    repaired = copy.deepcopy(doc)
    repaired["composition"] = _direct_ingredients(source)
    _put_after(repaired, "solutions", _solutions(source), "composition")
    repaired.pop("ingredients", None)
    repaired.pop("data_quality_flags", None)
    repaired["preparation_notes"] = (
        "Mix components thoroughly and adjust pH to 6.0. Distribute the "
        "medium into culture vessels under a N2 gas stream, seal with butyl "
        "rubber stoppers, and autoclave."
    )
    _put_after(
        repaired,
        "notes",
        (
            "MediaDive solution 4943 is the JCM Medium 932 main-solution "
            "import for Oscillibacter GH Medium."
        ),
        "preparation_notes",
    )
    _ensure_references(repaired, (MEDIADIVE_J932, JCM_932, JCM_187, JCM_197))
    _append_event(
        repaired,
        action="RESOLVED_MEDIADIVE_4943_OSCILLIBACTER_GH",
        references=(MEDIADIVE_J932, JCM_932, JCM_187, JCM_197),
        notes=(
            "Corrected the MediaDive J932 main solution's water from a false "
            "percent-volume value to ml/L, moved the JCM 187 and 197 stock "
            "components into nested solution additions, and removed the "
            "placeholder top-level ingredient."
        ),
    )
    return repaired


TARGETS: tuple[MediaTarget, ...] = (
    MediaTarget(
        path=MEDIADIVE_J932_PATH,
        record_id="CultureMech:003280",
        source_term="mediadive.medium:J932",
        source_name="MediaDive J932 / JCM Medium 932",
        imported_ingredients=MEDIADIVE_J932_IMPORTED,
        imported_solutions=(),
        action="RESOLVED_MEDIADIVE_J932_OSCILLIBACTER_GH",
        references=(MEDIADIVE_J932, JCM_932, JCM_187, JCM_197, TOGO_M978),
        event_notes=(
            "Restored the JCM Medium 932 source formula, added the missing "
            "water row, moved Trace vitamins, FeCl2 solution, and Trace "
            "element solution from flattened direct ingredients into nested "
            "ml/L solution additions, and linked the TOGO M978 source "
            "duplicate."
        ),
        variant_children=(TOGO_CHILD,),
    ),
    MediaTarget(
        path=TOGO_M978_PATH,
        record_id="CultureMech:010404",
        source_term="TOGO:M978",
        source_name="TOGO M978 / JCM Medium 932",
        imported_ingredients=TOGO_IMPORTED_INGREDIENTS,
        imported_solutions=TOGO_IMPORTED_SOLUTIONS,
        action="RESOLVED_TOGO_M978_OSCILLIBACTER_GH",
        references=(
            TOGO_M978,
            JCM_932,
            JCM_187,
            JCM_197,
            TOGO_M180,
            TOGO_M190,
            MEDIADIVE_J932,
        ),
        event_notes=(
            "Corrected distilled water from 1 g/L to 988.142 ml/L, removed "
            "the variable N2 ingredient in favor of N2 preparation steps, "
            "converted empty TOGO M190 and M180 cross-reference stubs to "
            "structured JCM 197 and JCM 187 stock solution additions, added "
            "pH 6.0, and linked the MediaDive J932 source duplicate."
        ),
        parent_media=J932_PARENT,
    ),
)


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_media_record(_load(path), target)

    solution_path = normalized / SOLUTION_4943_PATH
    plans[solution_path] = repair_solution_4943(_load(solution_path))
    return plans


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in plans.items():
        changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        if args.apply and changed:
            write_record(path, doc)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
