#!/usr/bin/env python3
"""Repair JCM Medium 291 Modified MRS Medium."""

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
JCM_J291_PATH = Path("bacterial/modified_mrs_medium.yaml")
TOGO_M285_PATH = Path("bacterial/TOGO_M285_Modified_MRS_Medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_j291_modified_mrs_score15.py"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

JCM_291 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=291"
TOGO_M285 = "https://togomedium.org/medium/M285"
SOURCE = "JCM Medium 291"
TITLE = "MODIFIED MRS MEDIUM"

MRS_BROTH = "Lactobacilli MRS broth (BD-Difco)"
WATER = "Distilled water"
CYSTEINE = "L-Cysteine HCl x H2O"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term_id: str
    imported_signature: tuple[Component, ...]
    action: str
    event_notes: str
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()


JCM_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Lactobacilli MRS broth", "55", "G_PER_L"),
    (CYSTEINE, "0.5", "G_PER_L"),
)

TOGO_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "1", "G_PER_L"),
    ("L--Cysteine・HCl・H2O", "0.5", "G_PER_L"),
    (MRS_BROTH, "55", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (MRS_BROTH, "55.0", "G_PER_L"),
    (CYSTEINE, "0.5", "G_PER_L"),
    (WATER, "1.0", "L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    WATER: ("CHEBI:15377", "water"),
    CYSTEINE: ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
}

MEDIAINGREDIENT_CHEBI = frozenset({WATER, CYSTEINE})

SOURCE_DUPLICATE_NOTE = (
    "TOGO M285 imports the same JCM Medium 291 Modified MRS Medium formulation "
    "represented by MediaDive J291."
)

JCM_J291_CHILD = {
    "path": f"data/normalized_yaml/{JCM_J291_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:002649",
    "name": "modified_mrs_medium",
    "notes": SOURCE_DUPLICATE_NOTE,
}

TOGO_M285_PARENT = {
    "path": f"data/normalized_yaml/{TOGO_M285_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:009400",
    "name": "modified_mrs_medium",
    "notes": SOURCE_DUPLICATE_NOTE,
}

NOTES = (
    "JCM Medium 291 lists 55.0 g Lactobacilli MRS broth from BD-Difco, "
    "0.5 g L-Cysteine HCl x H2O, and 1.0 L Distilled water; the pH is "
    "adjusted to 6.5. Lactobacilli MRS broth is retained as a commercial "
    "medium product."
)

INGREDIENT_NOTES = {
    MRS_BROTH: (
        "JCM Medium 291 lists 55.0 g/L Lactobacilli MRS broth from BD-Difco; "
        "this commercial medium product is retained as an opaque component."
    ),
    CYSTEINE: "JCM Medium 291 lists 0.5 g/L L-Cysteine HCl x H2O.",
    WATER: "JCM Medium 291 lists 1.0 L Distilled water.",
}

PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Suspend 55.0 g Lactobacilli MRS broth and 0.5 g L-Cysteine "
            "HCl x H2O in 1.0 L distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 6.5.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "duration": "15 min",
        "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
    },
]

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
}

TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM_J291_PATH,
        record_id="CultureMech:002649",
        media_term_id="mediadive.medium:J291",
        imported_signature=JCM_IMPORTED_INGREDIENT_SIGNATURE,
        action="RESOLVED_JCM_J291_SCORE15",
        event_notes=(
            f"{NOTES} Restored the 1.0 L distilled-water row, preserved "
            "Lactobacilli MRS broth as a source-disclosed commercial input, "
            "added JCM autoclave evidence, and linked the TOGO M285 source "
            "duplicate."
        ),
        references=(JCM_291,),
        parent_media=TOGO_M285_PARENT,
    ),
    Target(
        path=TOGO_M285_PATH,
        record_id="CultureMech:009400",
        media_term_id="TOGO:M285",
        imported_signature=TOGO_IMPORTED_INGREDIENT_SIGNATURE,
        action="RESOLVED_TOGO_M285_SCORE15",
        event_notes=(
            f"{NOTES} Corrected the imported TOGO distilled-water unit to "
            "the 1.0 L JCM value, normalized L-Cysteine HCl x H2O, added "
            "JCM autoclave evidence, and linked the MediaDive J291 source "
            "duplicate."
        ),
        references=(TOGO_M285, JCM_291),
        variant_children=(JCM_J291_CHILD,),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": INGREDIENT_NOTES[preferred_term],
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if preferred_term in MEDIAINGREDIENT_CHEBI:
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS = tuple(
    _component(name, value, unit)
    for name, value, unit in FINAL_INGREDIENT_SIGNATURE
)


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
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
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
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.media_term_id:
        raise ValueError(f"{target.path}: expected media term {target.media_term_id}")

    if _signature(doc.get("ingredients"), "ingredients") not in (
        target.imported_signature,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")


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


def _ensure_references(doc: dict[str, Any], wanted: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in wanted:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ph_value"] = 6.5
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(PREPARATION_STEPS)
    repaired["sterilization"] = copy.deepcopy(STERILIZATION)

    if target.parent_media:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), "references")
        _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
        _put_after(
            repaired,
            "variant_modifications",
            [target.parent_media["notes"]],
            "variant_relationship",
        )
    else:
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
        repaired.pop("variant_modifications", None)

    if target.variant_children:
        repaired["variant_children"] = [
            copy.deepcopy(child) for child in target.variant_children
        ]
    else:
        repaired.pop("variant_children", None)

    _ensure_flags(repaired)
    _ensure_references(repaired, target.references)
    _append_curation_event(repaired, target)
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
