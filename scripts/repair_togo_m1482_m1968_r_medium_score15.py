#!/usr/bin/env python3
"""Repair TOGO M1482/M1968 NBRC R medium records."""

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
PARENT = Path("bacterial/r_medium.yaml")
CHILD = Path("bacterial/r_medium_5_nacl.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1482_m1968_r_medium_score15.py"
ACTION_M1482 = "RESOLVED_TOGO_M1482_R_MEDIUM_SCORE15"
ACTION_M1968 = "RESOLVED_TOGO_M1968_R_MEDIUM_5_NACL_SCORE15"
LINK_ACTION = "LINKED_TOGO_M1968_R_MEDIUM_5_NACL_CHILD"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1482 = "https://togomedium.org/medium/M1482"
NBRC_264 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=264"
TOGO_M1968 = "https://togomedium.org/medium/M1968"
NBRC_1246 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1246"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term: str
    imported_signature: tuple[Component, ...]
    final_signature: tuple[Component, ...]
    ingredients: tuple[dict[str, Any], ...]
    source: str
    source_name: str
    references: tuple[str, ...]
    notes: str
    action: str
    event_notes: str


GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "Bacto Casamino Acids (Difco)": (
        "FOODON:03315719",
        "mammalian milk protein (hydrolyzed)",
    ),
    "Beef extract": ("FOODON:03302088", "beef extract"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Glycerol": ("CHEBI:17754", "glycerol"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "Malt extract": ("FOODON:03301056", "malt extract"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Peptone": ("MICRO:0000178", "Peptone"),
    "Tween 80": ("CHEBI:53426", "polysorbate 80"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Bacto Casamino Acids (Difco)": ("NITROGEN_SOURCE",),
    "Beef extract": ("NITROGEN_SOURCE",),
    "Glycerol": ("CARBON_SOURCE",),
    "MgSO4 x 7 H2O": ("TRACE_ELEMENT", "SULFUR_SOURCE"),
    "Malt extract": ("CARBON_SOURCE", "NITROGEN_SOURCE"),
    "Peptone": ("NITROGEN_SOURCE",),
    "Yeast extract": ("NITROGEN_SOURCE",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Agar (if needed)": ("SOLIDIFYING_AGENT",),
    "NaCl": ("OSMOTIC_AGENT",),
    "Tween 80": ("SURFACTANT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
}

BASE_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("MgSO4\u00b77H2O", "1", "G_PER_L"),
    ("Yeast extract", "5", "G_PER_L"),
    ("Tween 80", "0.05", "G_PER_L"),
    ("Glycerol", "2", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
    ("Malt extract", "5", "G_PER_L"),
    ("Beef extract", "2", "G_PER_L"),
    ("Bacto Casamino Acids (Difco)", "5", "G_PER_L"),
    ("Peptone", "10", "G_PER_L"),
)

CHILD_IMPORTED: tuple[Component, ...] = (
    BASE_IMPORTED[0],
    BASE_IMPORTED[1],
    BASE_IMPORTED[2],
    ("NaCl", "50", "G_PER_L"),
    *BASE_IMPORTED[3:],
)

BASE_FINAL: tuple[Component, ...] = (
    ("Peptone", "10.0", "G_PER_L"),
    ("Yeast extract", "5.0", "G_PER_L"),
    ("Malt extract", "5.0", "G_PER_L"),
    ("Bacto Casamino Acids (Difco)", "5.0", "G_PER_L"),
    ("Beef extract", "2.0", "G_PER_L"),
    ("Glycerol", "2.0", "G_PER_L"),
    ("Tween 80", "0.05", "G_PER_L"),
    ("MgSO4 x 7 H2O", "1.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("Agar (if needed)", "15.0", "G_PER_L"),
)

CHILD_FINAL: tuple[Component, ...] = (
    *BASE_FINAL[:8],
    ("NaCl", "50.0", "G_PER_L"),
    *BASE_FINAL[8:],
)

BASE_NOTES = (
    "TOGO M1482 imports NBRC Medium 264 R medium, which lists, per liter, "
    "10 g Peptone, 5 g Yeast extract, 5 g Malt extract, 5 g Bacto Casamino "
    "Acids (Difco), 2 g Beef extract, 2 g Glycerol, 0.05 g Tween 80, 1 g "
    "magnesium sulfate heptahydrate, 15 g Agar if needed, and final pH 7.0."
)

CHILD_NOTES = (
    "TOGO M1968 imports NBRC Medium 1246 R medium + 5% NaCl, which uses "
    "the NBRC R medium formula with 50 g/L NaCl and final pH 7.0."
)

CHILD_VARIANT_NOTES = "Adds 50 g/L NaCl to NBRC Medium 264 R medium."

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SALINITY_VARIANT",
    "id": "CultureMech:008026",
    "name": "r_medium",
    "notes": CHILD_VARIANT_NOTES,
}

CHILD_REFERENCE = {
    "path": f"data/normalized_yaml/{CHILD}",
    "relationship": "SALINITY_VARIANT",
    "id": "CultureMech:008549",
    "name": "r_medium_5_nacl",
    "notes": CHILD_VARIANT_NOTES,
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
    source_name: str,
) -> dict[str, Any]:
    grounding = GROUNDINGS[preferred_term]
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source_name} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": _term(*grounding),
    }
    if preferred_term == "Agar (if needed)":
        row["notes"] = f"{source_name} lists 15.0 g/L Agar if needed."
    if nutritional_roles := NUTRITIONAL_ROLES.get(preferred_term):
        row["nutritional_roles"] = list(nutritional_roles)
    if physicochemical_roles := PHYSICOCHEMICAL_ROLES.get(preferred_term):
        row["physicochemical_roles"] = list(physicochemical_roles)
    if grounding[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(
    signature: tuple[Component, ...],
    *,
    source: str,
    source_name: str,
) -> tuple[dict[str, Any], ...]:
    return tuple(
        _component(name, value, unit, source=source, source_name=source_name)
        for name, value, unit in signature
    )


PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "DISSOLVE",
        "description": (
            "Dissolve peptone, yeast extract, malt extract, Bacto Casamino "
            "Acids, beef extract, glycerol, Tween 80, magnesium sulfate "
            "heptahydrate, and agar if needed in 1.0 L distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0.",
    },
)

CHILD_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "DISSOLVE",
        "description": (
            "Dissolve peptone, yeast extract, malt extract, Bacto Casamino "
            "Acids, beef extract, glycerol, Tween 80, magnesium sulfate "
            "heptahydrate, NaCl, and agar if needed in 1.0 L distilled water."
        ),
    },
    PREPARATION_STEPS[1],
)

BASE_TARGET = Target(
    path=PARENT,
    record_id="CultureMech:008026",
    media_term="TOGO:M1482",
    imported_signature=BASE_IMPORTED,
    final_signature=BASE_FINAL,
    ingredients=_ingredients(
        BASE_FINAL,
        source="TOGO M1482 / NBRC Medium 264",
        source_name="NBRC Medium 264",
    ),
    source="TOGO M1482 / NBRC Medium 264",
    source_name="NBRC Medium 264",
    references=(TOGO_M1482, NBRC_264),
    notes=BASE_NOTES,
    action=ACTION_M1482,
    event_notes=(
        "Corrected the imported distilled-water unit from g/L to L, added pH "
        "7.0, grounded all ten disclosed components, and linked the NBRC "
        "Medium 1246 5% NaCl formulation as a salinity variant."
    ),
)

CHILD_TARGET = Target(
    path=CHILD,
    record_id="CultureMech:008549",
    media_term="TOGO:M1968",
    imported_signature=CHILD_IMPORTED,
    final_signature=CHILD_FINAL,
    ingredients=_ingredients(
        CHILD_FINAL,
        source="TOGO M1968 / NBRC Medium 1246",
        source_name="NBRC Medium 1246",
    ),
    source="TOGO M1968 / NBRC Medium 1246",
    source_name="NBRC Medium 1246",
    references=(TOGO_M1968, NBRC_1246),
    notes=CHILD_NOTES,
    action=ACTION_M1968,
    event_notes=(
        "Corrected the imported distilled-water unit from g/L to L, added pH "
        "7.0, grounded all eleven disclosed components, and linked this "
        "record to NBRC Medium 264 R medium as a salinity variant."
    ),
)

TARGETS = (BASE_TARGET, CHILD_TARGET)


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
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found " f"{doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.media_term:
        raise ValueError(f"{target.path}: expected media term {target.media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        target.imported_signature,
        target.final_signature,
    ):
        raise ValueError(
            f"{target.path}: ingredient signature drifted from "
            f"{target.imported_signature!r} to {ingredient_signature!r}"
        )

    if doc.get("solutions"):
        raise ValueError(f"{target.path}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "has_unmapped_ingredients",
        "incomplete_composition",
        "needs_manual_curation",
    ):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in target.references:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_event(
    doc: dict[str, Any],
    *,
    target: Target,
    action: str | None = None,
    notes: str | None = None,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action or target.action,
        "source": "; ".join(target.references),
        "notes": notes or target.event_notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == event["action"]
        ):
            history[index] = event
            return
    history.append(event)


def _upsert_child(parent: dict[str, Any]) -> None:
    children = parent.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")
    for index, child in enumerate(children):
        if isinstance(child, dict) and child.get("path") == CHILD_REFERENCE["path"]:
            children[index] = copy.deepcopy(CHILD_REFERENCE)
            break
    else:
        children.append(copy.deepcopy(CHILD_REFERENCE))


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired["ingredients"] = copy.deepcopy(list(target.ingredients))
    repaired.pop("solutions", None)
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(CHILD_PREPARATION_STEPS if target.path == CHILD else PREPARATION_STEPS)),
        "ingredients",
    )
    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_event(repaired, target=target)

    if target.path == PARENT:
        _upsert_child(repaired)
        _append_event(
            repaired,
            target=target,
            action=LINK_ACTION,
            notes=f"Added or refreshed {CHILD} as a salinity child of {PARENT}.",
        )
    else:
        _put_after(repaired, "parent_media", copy.deepcopy(PARENT_MEDIA), "references")
        _put_after(repaired, "variant_relationship", "SALINITY_VARIANT", "parent_media")
        _put_after(
            repaired,
            "variant_modifications",
            [CHILD_VARIANT_NOTES],
            "variant_relationship",
        )

    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized
        / target.path: repair_record(
            _load(normalized / target.path),
            target,
        )
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
