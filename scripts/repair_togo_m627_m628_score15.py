#!/usr/bin/env python3
"""Repair JCM/TOGO CYS Medium records with inline trace-stock additions."""

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
TOGO_M627_PATH = Path("bacterial/TOGO_M627_CYS_Medium.yaml")
TOGO_M628_PATH = Path("bacterial/TOGO_M628_CYS_Medium_For_YMO722.yaml")
JCM_J618_PATH = Path("bacterial/JCM_J618_CYS_MEDIUM.yaml")
JCM_J619_PATH = Path("bacterial/cys_medium_for_ymo722.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m627_m628_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M627 = "https://togomedium.org/medium/M627"
TOGO_M628 = "https://togomedium.org/medium/M628"
JCM_618 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=618"
JCM_619 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=619"
MEDIADIVE_J618 = "https://mediadive.dsmz.de/medium/J618"
MEDIADIVE_J619 = "https://mediadive.dsmz.de/medium/J619"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    source_term: str
    imported_signature: tuple[Component, ...]
    final_signature: tuple[Component, ...]
    nacl_value: str
    action: str
    source: str
    references: tuple[str, ...]
    notes: str
    event_notes: str
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()


TOGO_M627_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("NaCl", "20", "G_PER_L"),
    ("CaCl2\u30fb2H2O", "0.025", "G_PER_L"),
    ("MgCl2\u30fb6H2O", "0.125", "G_PER_L"),
    ("FeSO4\u30fb7H2O", "0.01", "G_PER_L"),
    ("Soluble starch (BD-Difco)", "1", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "2", "G_PER_L"),
    ("N-Z-Case (Wako)", "3", "G_PER_L"),
    ("MnCl2\u30fb4H2O (5.0 g/L in 0.01 N H2SO4)", "100", "G_PER_L"),
    ("ZnSO4\u30fb7H2O (0.6 g/L in 0.01 N H2SO4)", "100", "G_PER_L"),
    ("CuSO4\u30fb5H2O (0.15 g/L in 0.01 N H2SO4)", "100", "G_PER_L"),
    ("VOSO4\u30fbxH2O (1 g/L)", "100", "G_PER_L"),
    ("Na2MoO4\u30fb2H2O (12 g/L)", "100", "G_PER_L"),
    ("CoCl2\u30fb6H2O (8.0 g/L in 0.01 N H2SO4)", "100", "G_PER_L"),
    ("NiCl2\u30fb6H2O (0.2 g/L in 0.01 N H2SO4)", "100", "G_PER_L"),
)

TOGO_M628_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("NaCl", "16", "G_PER_L"),
    *TOGO_M627_IMPORTED[2:],
)

JCM_IMPORTED: tuple[Component, ...] = (
    ("N-Z-Case", "3.33333", "G_PER_L"),
    ("Yeast extract", "2.22222", "G_PER_L"),
    ("Starch", "1.11111", "G_PER_L"),
    ("NaCl", "22.2222", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.138889", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.0277778", "G_PER_L"),
    ("FeSO4 x 7 H2O", "0.0111111", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "100", "G_PER_L"),
    ("VOSO4 x n H2O", "100", "G_PER_L"),
    ("MnCl2 x 4 H2O", "100", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "100", "G_PER_L"),
    ("CuSO4 x 5 H2O", "100", "G_PER_L"),
    ("CoCl2 x 6 H2O", "100", "G_PER_L"),
    ("NiCl2 x 6 H2O", "100", "G_PER_L"),
)

BASE_FINAL: tuple[Component, ...] = (
    ("N-Z-Case (Wako)", "3.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "2.0", "G_PER_L"),
    ("Soluble starch (BD-Difco)", "1.0", "G_PER_L"),
    ("NaCl", "20.0", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.125", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.025", "G_PER_L"),
    ("FeSO4 x 7 H2O", "0.01", "G_PER_L"),
    ("Distilled water", "900.0", "ML_PER_L"),
)

SALINITY_FINAL: tuple[Component, ...] = (
    *BASE_FINAL[:3],
    ("NaCl", "16.0", "G_PER_L"),
    *BASE_FINAL[4:],
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "yeast extract"),
    "Soluble starch (BD-Difco)": ("CHEBI:28017", "starch"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "MgCl2 x 6 H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "VOSO4 x n H2O": ("CHEBI:87020", "vanadyl sulfate hydrate"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "NiCl2 x 6 H2O": ("CHEBI:53542", "nickel chloride hexahydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Add the base components to 900 ml distilled water and mix thoroughly.",
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": "Add each trace-metal stock solution at 0.1 ml/L in the listed order.",
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": (
            "Adjust pH to 7.5, bring the volume to 1.0 L with distilled " "water, and autoclave."
        ),
    },
    {
        "step_number": 4,
        "action": "HEAT",
        "description": "Inoculate into the medium prewarmed to the optimal growth temperature.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
}

JCM_J618_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J618_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:002965",
    "name": "cys_medium",
    "notes": "TOGO M627 imports the same JCM Medium 618 CYS Medium recipe.",
}

JCM_J619_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J618_PATH}",
    "relationship": "SALINITY_VARIANT",
    "id": "CultureMech:002965",
    "name": "cys_medium",
    "notes": "JCM Medium 619 uses JCM Medium 618 with 16.0 g/L final NaCl.",
}

TOGO_M628_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J619_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:002966",
    "name": "cys_medium_for_ymo722",
    "notes": "TOGO M628 imports the same JCM Medium 619 CYS Medium for YMO722 recipe.",
}

JCM_J619_CHILD = {
    "path": f"data/normalized_yaml/{JCM_J619_PATH}",
    "relationship": "SALINITY_VARIANT",
    "id": "CultureMech:002966",
    "name": "cys_medium_for_ymo722",
    "notes": "JCM Medium 619 uses JCM Medium 618 with 16.0 g/L final NaCl.",
}

TOGO_M627_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M627_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010027",
    "name": "cys_medium",
    "notes": "TOGO M627 imports the same JCM Medium 618 CYS Medium recipe.",
}

TOGO_M628_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M628_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010028",
    "name": "cys_medium_for_ymo722",
    "notes": "TOGO M628 imports the same JCM Medium 619 CYS Medium for YMO722 recipe.",
}

BASE_NOTES = (
    "JCM Medium 618 CYS Medium lists 3 g N-Z-Case, 2 g yeast extract, "
    "1 g soluble starch, 20 g NaCl, 0.125 g MgCl2 x 6 H2O, 0.025 g "
    "CaCl2 x 2 H2O, 0.01 g FeSO4 x 7 H2O, and seven trace-metal stocks "
    "added at 100 uL each before pH adjustment to 7.5 and final volume "
    "to 1 L."
)

SALINITY_NOTES = (
    "JCM Medium 619 CYS Medium for YMO722 uses JCM Medium 618 with 16.0 g/L " "final NaCl."
)

BASE_VARIANT_MODIFICATION = (
    "Same JCM Medium 618 CYS Medium formulation represented by MediaDive J618."
)

SALINITY_VARIANT_MODIFICATION = "NaCl decreased from 20.0 g/L to 16.0 g/L final concentration."


TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM_J618_PATH,
        record_id="CultureMech:002965",
        source_term="mediadive.medium:J618",
        imported_signature=JCM_IMPORTED,
        final_signature=BASE_FINAL,
        nacl_value="20.0",
        action="RESOLVED_JCM_618_CYS",
        source="MediaDive J618 / JCM Medium 618",
        references=(JCM_618, MEDIADIVE_J618),
        notes=BASE_NOTES,
        event_notes=(
            "Corrected the MediaDive import's 900 ml base scaling, represented "
            "the seven 100 uL trace-metal additions as stock solutions, added "
            "their CHEBI groundings, retained N-Z-Case as an intentionally "
            "unmapped Wako product, and linked JCM 619 and TOGO M627."
        ),
        variant_children=(JCM_J619_CHILD, TOGO_M627_CHILD),
    ),
    Target(
        path=JCM_J619_PATH,
        record_id="CultureMech:002966",
        source_term="mediadive.medium:J619",
        imported_signature=JCM_IMPORTED,
        final_signature=SALINITY_FINAL,
        nacl_value="16.0",
        action="RESOLVED_JCM_619_CYS_YMO722",
        source="MediaDive J619 / JCM Medium 619",
        references=(JCM_619, MEDIADIVE_J619, JCM_618),
        notes=SALINITY_NOTES,
        event_notes=(
            "Expanded the JCM Medium 619 wrapper into the corrected JCM 618 "
            "recipe with 16.0 g/L final NaCl, represented the seven 100 uL "
            "trace-metal additions as stock solutions, added CHEBI groundings, "
            "and linked JCM 618 and TOGO M628."
        ),
        parent_media=JCM_J619_PARENT,
        variant_children=(TOGO_M628_CHILD,),
        variant_relationship="SALINITY_VARIANT",
        variant_modifications=(SALINITY_VARIANT_MODIFICATION,),
    ),
    Target(
        path=TOGO_M627_PATH,
        record_id="CultureMech:010027",
        source_term="TOGO:M627",
        imported_signature=TOGO_M627_IMPORTED,
        final_signature=BASE_FINAL,
        nacl_value="20.0",
        action="RESOLVED_TOGO_M627_SCORE15",
        source="TOGO M627 / JCM Medium 618",
        references=(TOGO_M627, JCM_618, MEDIADIVE_J618),
        notes=BASE_NOTES,
        event_notes=(
            "Corrected the imported distilled-water and trace-stock units, added "
            "pH 7.5, represented the seven 100 uL trace-metal additions as stock "
            "solutions, grounded soluble starch, yeast extract, and the trace "
            "salts, retained N-Z-Case as intentionally unmapped, and linked "
            "MediaDive J618 as a source duplicate."
        ),
        parent_media=JCM_J618_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(BASE_VARIANT_MODIFICATION,),
    ),
    Target(
        path=TOGO_M628_PATH,
        record_id="CultureMech:010028",
        source_term="TOGO:M628",
        imported_signature=TOGO_M628_IMPORTED,
        final_signature=SALINITY_FINAL,
        nacl_value="16.0",
        action="RESOLVED_TOGO_M628_SCORE15",
        source="TOGO M628 / JCM Medium 619",
        references=(TOGO_M628, JCM_619, MEDIADIVE_J619, JCM_618),
        notes=SALINITY_NOTES,
        event_notes=(
            "Corrected the imported distilled-water and trace-stock units in "
            "the JCM Medium 619 16.0 g/L NaCl variant, represented the seven "
            "100 uL trace-metal additions as stock solutions, grounded soluble "
            "starch, yeast extract, and the trace salts, retained N-Z-Case as "
            "intentionally unmapped, and linked MediaDive J619 as a source "
            "duplicate."
        ),
        parent_media=TOGO_M628_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(BASE_VARIANT_MODIFICATION,),
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
    nutritional_roles: tuple[str, ...] = (),
    physicochemical_roles: tuple[str, ...] = (),
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
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


def _base_ingredients(source: str, nacl_value: str) -> list[dict[str, Any]]:
    return [
        _component(
            "N-Z-Case (Wako)",
            "3.0",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 3.0 g/L N-Z-Case (Wako).",
            nutritional_roles=("NITROGEN_SOURCE",),
        ),
        _component(
            "Yeast extract (BD-Difco)",
            "2.0",
            "G_PER_L",
            source=source,
            nutritional_roles=("NITROGEN_SOURCE",),
        ),
        _component(
            "Soluble starch (BD-Difco)",
            "1.0",
            "G_PER_L",
            source=source,
            nutritional_roles=("CARBON_SOURCE",),
        ),
        _component("NaCl", nacl_value, "G_PER_L", source=source),
        _component("MgCl2 x 6 H2O", "0.125", "G_PER_L", source=source),
        _component("CaCl2 x 2 H2O", "0.025", "G_PER_L", source=source),
        _component("FeSO4 x 7 H2O", "0.01", "G_PER_L", source=source),
        _component(
            "Distilled water",
            "900.0",
            "ML_PER_L",
            source=source,
            notes=f"{source} lists 900 ml distilled water before pH adjustment.",
        ),
    ]


def _stock(
    preferred_term: str,
    solute: str,
    stock_value: str,
    *,
    acidified: bool = False,
    source: str,
) -> dict[str, Any]:
    solvent = " in 0.01 N H2SO4" if acidified else ""
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": "0.1", "unit": "ML_PER_L"},
        "source": source,
        "notes": f"{source} adds 100 uL of {stock_value} g/L {solute}{solvent}.",
        "composition": [
            _component(
                solute,
                stock_value,
                "G_PER_L",
                source=source,
                notes=(
                    f"{preferred_term} is represented as a {stock_value} g/L "
                    f"{solute} stock{solvent}."
                ),
                nutritional_roles=("TRACE_ELEMENT",),
            )
        ],
    }


def _solutions(source: str) -> list[dict[str, Any]]:
    return [
        _stock("Na2MoO4 x 2 H2O stock", "Na2MoO4 x 2 H2O", "12.0", source=source),
        _stock("VOSO4 x n H2O stock", "VOSO4 x n H2O", "1.0", source=source),
        _stock(
            "MnCl2 x 4 H2O stock",
            "MnCl2 x 4 H2O",
            "5.0",
            acidified=True,
            source=source,
        ),
        _stock(
            "ZnSO4 x 7 H2O stock",
            "ZnSO4 x 7 H2O",
            "0.6",
            acidified=True,
            source=source,
        ),
        _stock(
            "CuSO4 x 5 H2O stock",
            "CuSO4 x 5 H2O",
            "0.15",
            acidified=True,
            source=source,
        ),
        _stock(
            "CoCl2 x 6 H2O stock",
            "CoCl2 x 6 H2O",
            "8.0",
            acidified=True,
            source=source,
        ),
        _stock(
            "NiCl2 x 6 H2O stock",
            "NiCl2 x 6 H2O",
            "0.2",
            acidified=True,
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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')}")
    if _source_term_id(doc) != target.source_term:
        raise ValueError(f"{target.path}: expected media term {target.source_term}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        target.imported_signature,
        target.final_signature,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")


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


def _append_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": target.action,
        "source": "; ".join(target.references),
        "notes": target.event_notes,
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == target.action
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
    _put_after(repaired, "ph_value", 7.5, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("high_metal", None)
    repaired["ingredients"] = _base_ingredients(target.source, target.nacl_value)
    _put_after(repaired, "notes", target.notes, "media_term")
    _put_after(repaired, "solutions", _solutions(target.source), "notes")
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
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
    _append_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_record(_load(path), target)
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
