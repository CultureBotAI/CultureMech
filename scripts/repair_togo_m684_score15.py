#!/usr/bin/env python3
"""Repair JCM/TOGO/NBRC YM broth records around TOGO M684."""

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
JCM_J666_PATH = Path("bacterial/ym_broth.yaml")
TOGO_M684_PATH = Path("bacterial/TOGO_M684_YM_Broth.yaml")
TOGO_M1599_PATH = Path("bacterial/ym_liquid_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m684_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M684 = "https://togomedium.org/medium/M684"
TOGO_M1599 = "https://togomedium.org/medium/M1599"
JCM_666 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=666"
MEDIADIVE_J666 = "https://mediadive.dsmz.de/medium/J666"
NBRC_703 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=703"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    source_term: str
    imported_signature: tuple[Component, ...]
    action: str
    source: str
    notes: str
    event_notes: str
    references: tuple[str, ...]
    preparation_steps: tuple[dict[str, Any], ...]
    ph_value: float | None = None
    sterilization: dict[str, Any] | None = None
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()


JCM_IMPORTED: tuple[Component, ...] = (
    ("Glucose", "10", "G_PER_L"),
    ("Peptone", "5", "G_PER_L"),
    ("Yeast extract", "3", "G_PER_L"),
    ("Malt extract", "3", "G_PER_L"),
)

TOGO_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "3", "G_PER_L"),
    ("Glucose", "10", "G_PER_L"),
    ("Malt extract", "3", "G_PER_L"),
    ("Peptone", "5", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Glucose", "10.0", "G_PER_L"),
    ("Peptone", "5.0", "G_PER_L"),
    ("Yeast extract", "3.0", "G_PER_L"),
    ("Malt extract", "3.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Glucose": ("CHEBI:17234", "glucose"),
    "Peptone": ("MICRO:0000178", "peptone"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "Malt extract": ("FOODON:03301056", "malt extract"),
    "Distilled water": ("CHEBI:15377", "water"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Glucose": ("CARBON_SOURCE",),
    "Peptone": ("NITROGEN_SOURCE",),
    "Yeast extract": ("NITROGEN_SOURCE",),
    "Malt extract": ("CARBON_SOURCE", "NITROGEN_SOURCE"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
}

JCM_RECIPE_NOTES = (
    "JCM Medium 666 YM Broth lists 10.0 g Glucose, 5.0 g Peptone, "
    "3.0 g Yeast extract, 3.0 g Malt extract, and 1.0 L Distilled water, "
    "then adjusts pH to 6.2."
)

NBRC_RECIPE_NOTES = (
    "NBRC Medium 703 YM Liquid Medium lists 10.0 g Glucose, 5.0 g "
    "Peptone, 3.0 g Yeast extract, 3.0 g Malt extract, and 1.0 L "
    "Distilled water; the source does not report a final pH."
)

JCM_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Dissolve 10.0 g Glucose, 5.0 g Peptone, 3.0 g Yeast extract, "
            "and 3.0 g Malt extract in 1.0 L distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 6.2.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C for 15 min.",
    },
)

NBRC_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Combine 10.0 g Glucose, 5.0 g Peptone, 3.0 g Yeast extract, "
            "3.0 g Malt extract, and 1.0 L distilled water."
        ),
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
}

M684_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M684_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010089",
    "name": "ym_broth",
    "notes": "TOGO M684 imports the same JCM Medium 666 YM Broth formulation.",
}

JCM_J666_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J666_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003012",
    "name": "ym_broth",
    "notes": "TOGO M684 imports the same JCM Medium 666 YM Broth formulation.",
}

M684_VARIANT_MODIFICATION = (
    "Same JCM Medium 666 YM Broth formulation as the MediaDive J666 source record."
)

TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM_J666_PATH,
        record_id="CultureMech:003012",
        source_term="mediadive.medium:J666",
        imported_signature=JCM_IMPORTED,
        action="RESOLVED_JCM_666_YM_BROTH",
        source="MediaDive J666 / JCM Medium 666",
        notes=JCM_RECIPE_NOTES,
        event_notes=(
            "Restored the JCM Medium 666 recipe with 1.0 L Distilled water, "
            "grounded the disclosed ingredients, added JCM's default "
            "autoclaving instruction, and linked TOGO M684 as a JCM source "
            "duplicate."
        ),
        references=(JCM_666, MEDIADIVE_J666),
        ph_value=6.2,
        preparation_steps=JCM_PREPARATION_STEPS,
        sterilization=STERILIZATION,
        variant_children=(M684_CHILD,),
    ),
    Target(
        path=TOGO_M684_PATH,
        record_id="CultureMech:010089",
        source_term="TOGO:M684",
        imported_signature=TOGO_IMPORTED,
        action="RESOLVED_TOGO_M684_YM_BROTH",
        source="TOGO M684 / JCM Medium 666",
        notes=JCM_RECIPE_NOTES,
        event_notes=(
            "Corrected the imported distilled-water unit, added JCM pH 6.2, "
            "grounded Peptone, Yeast extract, Malt extract, and Glucose, "
            "added JCM's default autoclaving instruction, and linked the "
            "MediaDive J666 source duplicate."
        ),
        references=(TOGO_M684, JCM_666, MEDIADIVE_J666),
        ph_value=6.2,
        preparation_steps=JCM_PREPARATION_STEPS,
        sterilization=STERILIZATION,
        parent_media=JCM_J666_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(M684_VARIANT_MODIFICATION,),
    ),
    Target(
        path=TOGO_M1599_PATH,
        record_id="CultureMech:008150",
        source_term="TOGO:M1599",
        imported_signature=TOGO_IMPORTED,
        action="RESOLVED_NBRC_703_YM_LIQUID",
        source="TOGO M1599 / NBRC Medium 703",
        notes=NBRC_RECIPE_NOTES,
        event_notes=(
            "Corrected the imported distilled-water unit, grounded Peptone, "
            "Yeast extract, Malt extract, and Glucose, and removed the "
            "heuristic TOGO M684 source-duplicate link because NBRC Medium "
            "703 does not state JCM's pH 6.2 adjustment."
        ),
        references=(TOGO_M1599, NBRC_703),
        preparation_steps=NBRC_PREPARATION_STEPS,
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
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    if grounding[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    roles = NUTRITIONAL_ROLES.get(preferred_term)
    if roles:
        row["nutritional_roles"] = list(roles)
    return row


def _ingredients(source: str) -> list[dict[str, Any]]:
    return [
        _component("Glucose", "10.0", "G_PER_L", source=source),
        _component("Peptone", "5.0", "G_PER_L", source=source),
        _component("Yeast extract", "3.0", "G_PER_L", source=source),
        _component("Malt extract", "3.0", "G_PER_L", source=source),
        _component("Distilled water", "1.0", "L", source=source),
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
        FINAL_INGREDIENT_SIGNATURE,
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


def repair_target(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    if target.ph_value is None:
        repaired.pop("ph_value", None)
    else:
        _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "notes", target.notes, "media_term")
    repaired["ingredients"] = _ingredients(target.source)
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in target.preparation_steps],
        "notes",
    )
    if target.sterilization:
        _put_after(
            repaired,
            "sterilization",
            copy.deepcopy(target.sterilization),
            "preparation_steps",
        )
    else:
        repaired.pop("sterilization", None)

    if target.parent_media:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), "references")
        repaired["variant_relationship"] = target.variant_relationship
        repaired["variant_modifications"] = list(target.variant_modifications)
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
    _append_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_target(_load(normalized / target.path), target)
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
