#!/usr/bin/env python3
"""Repair TOGO M971 MRS Medium With Soybean Peptone."""

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
JCM_J925_PATH = Path("bacterial/mrs_medium_with_soybean_peptone.yaml")
TOGO_M971_PATH = Path("bacterial/TOGO_M971_MRS_Medium_With_Soybean_Peptone.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m971_mrs_soybean_score15.py"
ACTION = "RESOLVED_TOGO_M971_MRS_SOYBEAN"
TIMESTAMP = "2026-09-11T00:00:00-07:00"
FALSE_KG_MATCH = "mediadive.medium:12"

TOGO_M971 = "https://togomedium.org/medium/M971"
JCM_925 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=925"
SOURCE = "TOGO M971 / JCM Medium 925"

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


JCM_IMPORTED_SIGNATURE: tuple[Component, ...] = (
    ("Lactobacilli MRS broth", "55", "G_PER_L"),
    ("Phytone peptone", "5", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
)

TOGO_IMPORTED_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Bacto agar (BD-Difco)", "15", "G_PER_L"),
    ("Lactobacilli MRS broth (BD-Difco)", "55", "G_PER_L"),
    ("Phytone peptone (BD-BBL)", "5", "G_PER_L"),
)

FINAL_SIGNATURE: tuple[Component, ...] = (
    ("Lactobacilli MRS broth (BD-Difco)", "55.0", "G_PER_L"),
    ("Phytone peptone (BD-BBL)", "5.0", "G_PER_L"),
    ("Bacto agar (BD-Difco)", "15.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Bacto agar (BD-Difco)": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Phytone peptone (BD-BBL)": ("FOODON:03315720", "Soy peptone"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Phytone peptone (BD-BBL)": ("PROTEIN_SOURCE",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Bacto agar (BD-Difco)": ("SOLIDIFYING_AGENT",),
}

SOURCE_DUPLICATE_NOTE = (
    "TOGO M971 imports the same JCM Medium 925 MRS Medium With Soybean "
    "Peptone formulation represented by MediaDive J925."
)

JCM_J925_CHILD = {
    "path": f"data/normalized_yaml/{JCM_J925_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003272",
    "name": "mrs_medium_with_soybean_peptone",
    "notes": SOURCE_DUPLICATE_NOTE,
}

TOGO_M971_PARENT = {
    "path": f"data/normalized_yaml/{TOGO_M971_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010397",
    "name": "mrs_medium_with_soybean_peptone",
    "notes": SOURCE_DUPLICATE_NOTE,
}

PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Combine the MRS Medium With Soybean Peptone components listed by "
            "JCM Medium 925."
        ),
    },
    {
        "step_number": 2,
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

NOTES = (
    "JCM Medium 925 MRS Medium With Soybean Peptone lists 55.0 g/L "
    "Lactobacilli MRS broth, 5.0 g/L Phytone peptone, 15.0 g/L "
    "Bacto agar, and 1.0 L Distilled water; the JCM page applies "
    "default autoclaving at 121 C for 15 min."
)

TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM_J925_PATH,
        record_id="CultureMech:003272",
        media_term_id="mediadive.medium:J925",
        imported_signature=JCM_IMPORTED_SIGNATURE,
        action="RESOLVED_JCM_J925_MRS_SOYBEAN",
        event_notes=(
            "Restored the 1.0 L distilled-water row, normalized the JCM "
            "Medium 925 ingredient names to their source-listed commercial "
            "BD product names, added JCM autoclave evidence, removed the "
            "stale MediaDive 12 match, and linked the TOGO M971 source "
            "duplicate."
        ),
        references=(JCM_925,),
        parent_media=TOGO_M971_PARENT,
    ),
    Target(
        path=TOGO_M971_PATH,
        record_id="CultureMech:010397",
        media_term_id="TOGO:M971",
        imported_signature=TOGO_IMPORTED_SIGNATURE,
        action=ACTION,
        event_notes=(
            "Corrected the JCM Medium 925 water unit, grounded Bacto agar "
            "and Phytone peptone, retained Lactobacilli MRS broth as a "
            "source-listed unmapped commercial product, added the JCM "
            "default autoclaving condition, and linked the MediaDive J925 "
            "source duplicate."
        ),
        references=(TOGO_M971, JCM_925),
        variant_children=(JCM_J925_CHILD,),
    ),
)

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
}


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
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


def _composition() -> list[dict[str, Any]]:
    return [_component(*row) for row in FINAL_SIGNATURE]


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.media_term_id:
        raise ValueError(f"{target.path}: expected media term {target.media_term_id}")

    if _signature(doc.get("ingredients"), "ingredients") not in (
        target.imported_signature,
        FINAL_SIGNATURE,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    kg_match = doc.get("kg_microbe_match")
    if kg_match is not None and kg_match != FALSE_KG_MATCH:
        raise ValueError(f"{target.path}: unexpected kg_microbe_match {kg_match!r}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
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
    for reference in references_to_add:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
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


def repair_document(doc: dict[str, Any]) -> dict[str, Any]:
    return repair_record(doc, TARGETS[1])


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired["ingredients"] = _composition()
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(PREPARATION_STEPS),
        "ingredients",
    )
    _put_after(
        repaired,
        "sterilization",
        copy.deepcopy(STERILIZATION),
        "preparation_steps",
    )
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired.pop("kg_microbe_match", None)

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
    _ensure_event(repaired, target)
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
    print(f"\n{verb} {changed_count} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
