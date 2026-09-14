#!/usr/bin/env python3
"""Repair JCM 1099 Heart Infusion Agar with horse blood and its TOGO duplicate."""

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
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_1099_heart_infusion_horse_score15.py"
ACTION = "RESOLVED_JCM_1099_HEART_INFUSION_HORSE_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

JCM_TARGET = Path("bacterial/heart_infusion_agar_with_5_horse_blood.yaml")
TOGO_TARGET = Path("bacterial/TOGO_M1172_Heart_Infusion_Agar_With_5_Horse_Blood.yaml")

JCM_1099 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1099"
TOGO_M1172 = "https://togomedium.org/medium/M1172"
TOGO_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1172"
SOURCE = "JCM Medium 1099"
TITLE = "HEART INFUSION AGAR WITH 5% HORSE BLOOD"

Component = tuple[str, str, str]

JCM_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Heart Infusion Broth", "25", "G_PER_L"),
    ("Horse blood", "50", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
)

TOGO_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "950", "G_PER_L"),
    ("Horse blood", "50", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Heart infusion broth (BD-Difco)", "25", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Heart infusion broth (BD-Difco)", "25.0", "G_PER_L"),
    ("Horse blood", "50.0", "ML_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Distilled water", "950.0", "ML_PER_L"),
)

JCM_NOTES = (
    "JCM Medium 1099 lists Heart Infusion Agar with 5% horse blood per liter "
    "as 25.0 g Heart infusion broth (BD-Difco), 50.0 ml Horse blood, "
    "15.0 g Agar, and 950.0 ml Distilled water. The source uses JCM's "
    "default autoclaving at 121 C for 15 min and aseptically adds sterile "
    "defibrinated horse blood after the base cools to about 50 C."
)

TOGO_NOTES = f"TOGO M1172 imports JCM_M1099. {JCM_NOTES}"

JCM_PARENT_REF = {
    "path": f"data/normalized_yaml/{JCM_TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:002278",
    "name": "heart_infusion_agar_with_5_horse_blood",
    "notes": "JCM Medium 1099 authoritative formulation.",
}

TOGO_CHILD_REF = {
    "path": f"data/normalized_yaml/{TOGO_TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:007697",
    "name": "heart_infusion_agar_with_5_horse_blood",
    "notes": (
        "TOGO M1172 imports JCM_M1099 and mirrors the same Heart Infusion "
        "Agar With 5% Horse Blood formulation."
    ),
}


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    expected_media_term: str
    imported_signature: tuple[Component, ...]
    notes: str
    references: tuple[str, ...]
    source_duplicate_parent: bool


TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM_TARGET,
        expected_id="CultureMech:002278",
        expected_media_term="mediadive.medium:J1099",
        imported_signature=JCM_IMPORTED_INGREDIENT_SIGNATURE,
        notes=JCM_NOTES,
        references=(JCM_1099,),
        source_duplicate_parent=True,
    ),
    Target(
        path=TOGO_TARGET,
        expected_id="CultureMech:007697",
        expected_media_term="TOGO:M1172",
        imported_signature=TOGO_IMPORTED_INGREDIENT_SIGNATURE,
        notes=TOGO_NOTES,
        references=(TOGO_M1172, TOGO_API, JCM_1099),
        source_duplicate_parent=False,
    ),
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


INGREDIENTS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Heart infusion broth (BD-Difco)",
        "concentration": {"value": "25.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": (
            "JCM Medium 1099 lists 25.0 g/L Heart infusion broth from "
            "BD-Difco; this commercial base is retained as an opaque "
            "component."
        ),
    },
    {
        "preferred_term": "Horse blood",
        "concentration": {"value": "50.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            "JCM Medium 1099 lists 50.0 ml/L Horse blood and instructs "
            "aseptic addition of sterile defibrinated horse blood as the "
            "final 5% supplement."
        ),
        "term": _term("UBERON:0000178", "blood"),
    },
    {
        "preferred_term": "Agar",
        "concentration": {"value": "15.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": "JCM Medium 1099 lists 15.0 g/L Agar.",
        "term": _term("CHEBI:2509", "agar"),
        "mediaingredientmech_chebi_term": _term("CHEBI:2509", "agar"),
    },
    {
        "preferred_term": "Distilled water",
        "concentration": {"value": "950.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": "JCM Medium 1099 lists 950.0 ml/L Distilled water.",
        "term": _term("CHEBI:15377", "water"),
        "mediaingredientmech_chebi_term": _term("CHEBI:15377", "water"),
    },
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix 25.0 g Heart infusion broth (BD-Difco) and 15.0 g Agar "
            "with 950.0 ml Distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": ("Autoclave the base at 121 C for 15 min and cool to about 50 C."),
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": "Aseptically add 50.0 ml sterile defibrinated horse blood.",
    },
    {
        "step_number": 4,
        "action": "POUR_PLATES",
        "description": "Mix and quickly dispense into sterile petri dishes.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": (
        "JCM states to sterilize media by autoclaving at 121 C for 15 min "
        "unless otherwise stated; in Medium 1099, the horse blood is added "
        "aseptically after the autoclaved base cools."
    ),
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.expected_media_term:
        raise ValueError(f"{target.path}: expected media term {target.expected_media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        target.imported_signature,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    if doc.get("solutions"):
        raise ValueError(f"{target.path}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.references:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.references),
        "notes": (
            f"{target.notes} Corrected the imported ml/L unit artifacts, "
            "grounded water, agar, and horse blood, and kept Heart infusion "
            "broth (BD-Difco) intentionally unmapped as a source-disclosed "
            "commercial base."
        ),
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


def _set_source_duplicate_links(doc: dict[str, Any], target: Target) -> None:
    if target.source_duplicate_parent:
        doc.pop("parent_media", None)
        doc.pop("variant_relationship", None)
        doc.pop("variant_modifications", None)
        _put_after(doc, "variant_children", [copy.deepcopy(TOGO_CHILD_REF)], "references")
        return

    _put_after(doc, "parent_media", copy.deepcopy(JCM_PARENT_REF), "references")
    _put_after(doc, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
    _put_after(
        doc,
        "variant_modifications",
        ["TOGO source-catalogue duplicate of JCM Medium 1099."],
        "variant_relationship",
    )
    doc.pop("variant_children", None)


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", target.notes, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["sterilization"] = copy.deepcopy(STERILIZATION)
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _set_source_duplicate_links(repaired, target)
    _append_curation_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path), target)
        for target in TARGETS
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
