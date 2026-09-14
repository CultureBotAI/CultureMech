#!/usr/bin/env python3
"""Repair MediaDive/TOGO JCM 763 Alkaline Tryptone Soya Broth records."""

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
JCM_J763_PATH = Path("bacterial/alkaline_tryptone_soya_broth_medium.yaml")
TOGO_M789_PATH = Path("bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml")
TOGO_M790_PATH = Path("bacterial/TOGO_M790_Alkaline_Tryptone_Soya_Broth_Medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m789_alkaline_tsb_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J763 = "https://mediadive.dsmz.de/medium/J763"
TOGO_M789 = "https://togomedium.org/medium/M789"
TOGO_M790 = "https://togomedium.org/medium/M790"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    source_term: str
    source_name: str
    imported_ingredients: tuple[Component, ...]
    imported_solutions: tuple[Component, ...]
    final_ingredients: tuple[Component, ...]
    physical_state: str
    solid: bool
    action: str
    event_notes: str
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, Any], ...] = ()


JCM_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Pancreatic digest of casein", "17.0", "G_PER_L"),
    ("Peptic digest of soybean meal", "3.0", "G_PER_L"),
    ("Glucose", "2.5", "G_PER_L"),
    ("Sodium chloride", "5.0", "G_PER_L"),
    ("Dipotassium phosphate", "2.5", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
)

M789_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Tryptone soya broth (Oxoid)", "30", "G_PER_L"),
)

M790_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("agar", "20", "G_PER_L"),
    ("Tryptone soya broth (Oxoid)", "30", "G_PER_L"),
)

IMPORTED_SODIUM_CARBONATE: tuple[Component, ...] = (
    ("sodium carbonate solution", "variable", "VARIABLE"),
)

LIQUID_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Tryptone soya broth (Oxoid)", "30.0", "G_PER_L"),
)

SOLID_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("Tryptone soya broth (Oxoid)", "30.0", "G_PER_L"),
    ("Agar", "20.0", "G_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("20% sodium carbonate solution", "variable", "VARIABLE"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Agar": ("CHEBI:2509", "agar"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Agar": ("SOLIDIFYING_AGENT",),
    "Na2CO3": ("BUFFER",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
}

M789_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M789_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010198",
    "name": "alkaline_tryptone_soya_broth_medium",
    "notes": (
        "TOGO M789 imports the same liquid JCM Medium 763 Alkaline "
        "Tryptone Soya Broth formulation represented by MediaDive J763."
    ),
}

M790_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M790_PATH}",
    "relationship": "PHYSICAL_STATE_VARIANT",
    "id": "CultureMech:010200",
    "name": "alkaline_tryptone_soya_broth_medium",
    "notes": "TOGO M790 adds 20.0 g/L agar to solidify JCM Medium 763.",
}

J763_PARENT_SOURCE_DUPLICATE = {
    "path": f"data/normalized_yaml/{JCM_J763_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003106",
    "name": "alkaline_tryptone_soya_broth_medium",
    "notes": M789_CHILD["notes"],
}

J763_PARENT_SOLID_VARIANT = {
    "path": f"data/normalized_yaml/{JCM_J763_PATH}",
    "relationship": "PHYSICAL_STATE_VARIANT",
    "id": "CultureMech:003106",
    "name": "alkaline_tryptone_soya_broth_medium",
    "notes": M790_CHILD["notes"],
}

SOLID_VARIANT_NOTE = "Add 20.0 g/L agar to solidify JCM Medium 763."


def _source_note(solid: bool) -> str:
    base = (
        "MediaDive J763 and TOGO M789 describe JCM Medium 763 Alkaline "
        "Tryptone Soya Broth Medium as 30.0 g/L Oxoid Tryptone soya broth "
        "in 1000.0 ml/L distilled water, adjusted after autoclaving to pH "
        "8.5-9.0 with sterile autoclaved 20% sodium carbonate solution."
    )
    if not solid:
        return base
    return f"{base} TOGO M790 additionally applies the 20.0 g/L agar " "solidification step."


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

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _direct_ingredients(source: str, *, solid: bool) -> list[dict[str, Any]]:
    rows = [
        _component(
            "Distilled water",
            "1000.0",
            "ML_PER_L",
            source=source,
            notes=f"{source} contributes 1000.0 ml/L distilled water.",
        ),
        _component(
            "Tryptone soya broth (Oxoid)",
            "30.0",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 30.0 g/L Oxoid Tryptone soya broth.",
        ),
    ]
    if solid:
        rows.append(
            _component(
                "Agar",
                "20.0",
                "G_PER_L",
                source=source,
                notes=f"{source} adds 20.0 g/L agar for solid medium.",
            )
        )
    return rows


def _solutions(source: str) -> list[dict[str, Any]]:
    return [
        {
            "preferred_term": "20% sodium carbonate solution",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": source,
            "notes": f"{source} uses sterile 20% sodium carbonate to adjust pH.",
            "composition": [
                _component(
                    "Na2CO3",
                    "20.0",
                    "PERCENT_W_V",
                    source=source,
                    notes=(
                        f"{source} specifies the pH-adjusting sodium carbonate "
                        "solution as 20.0% w/v."
                    ),
                )
            ],
            "preparation_notes": "Autoclave before adjusting the medium pH.",
        }
    ]


def _preparation_steps(solid: bool) -> list[dict[str, Any]]:
    first = "Dissolve 30.0 g/L Oxoid Tryptone soya broth in 1000.0 ml/L water."
    if solid:
        first = (
            "Dissolve 30.0 g/L Oxoid Tryptone soya broth and 20.0 g/L " "agar in 1000.0 ml/L water."
        )
    return [
        {"step_number": 1, "action": "MIX", "description": first},
        {"step_number": 2, "action": "AUTOCLAVE", "description": "Autoclave."},
        {
            "step_number": 3,
            "action": "ADJUST_PH",
            "description": (
                "After cooling, adjust pH to 8.5-9.0 with sterile "
                "autoclaved 20% sodium carbonate solution."
            ),
        },
    ]


STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": (
        "Autoclave the basal medium and the 20% sodium carbonate solution "
        "before final pH adjustment."
    ),
}


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
        target.final_ingredients,
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
    repaired["physical_state"] = target.physical_state
    repaired.pop("ph_value", None)
    _put_after(repaired, "ph_range", {"min": 8.5, "max": 9.0}, "physical_state")
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "notes", _source_note(target.solid), "media_term")
    repaired["ingredients"] = _direct_ingredients(
        target.source_name,
        solid=target.solid,
    )
    _put_after(repaired, "solutions", _solutions(target.source_name), "ingredients")
    _put_after(
        repaired,
        "preparation_steps",
        _preparation_steps(target.solid),
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
        path=JCM_J763_PATH,
        record_id="CultureMech:003106",
        source_term="mediadive.medium:J763",
        source_name="MediaDive J763 / JCM Medium 763",
        imported_ingredients=JCM_IMPORTED_INGREDIENTS,
        imported_solutions=(),
        final_ingredients=LIQUID_INGREDIENT_SIGNATURE,
        physical_state="LIQUID",
        solid=False,
        action="RESOLVED_JCM_763_ALKALINE_TRYPTONE_SOYA_BROTH",
        event_notes=(
            "Restored source-level Oxoid Tryptone soya broth, removed the "
            "Wikipedia-derived constituent expansion and agar from the "
            "liquid parent, nested 20% sodium carbonate as the variable pH "
            "adjuster, added the final pH range, and linked the TOGO M789 "
            "and M790 child records."
        ),
        references=(MEDIADIVE_J763,),
        variant_children=(M789_CHILD, M790_CHILD),
    ),
    Target(
        path=TOGO_M789_PATH,
        record_id="CultureMech:010198",
        source_term="TOGO:M789",
        source_name="TOGO M789 / JCM Medium 763",
        imported_ingredients=M789_IMPORTED_INGREDIENTS,
        imported_solutions=IMPORTED_SODIUM_CARBONATE,
        final_ingredients=LIQUID_INGREDIENT_SIGNATURE,
        physical_state="LIQUID",
        solid=False,
        action="RESOLVED_TOGO_M789_ALKALINE_TRYPTONE_SOYA_BROTH",
        event_notes=(
            "Moved sodium carbonate solution from an empty solution stub "
            "into a structured 20% stock used as a variable pH adjuster, "
            "corrected water units, added the final pH range, and linked "
            "the MediaDive J763 source duplicate."
        ),
        references=(TOGO_M789, MEDIADIVE_J763),
        parent_media=J763_PARENT_SOURCE_DUPLICATE,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(M789_CHILD["notes"],),
    ),
    Target(
        path=TOGO_M790_PATH,
        record_id="CultureMech:010200",
        source_term="TOGO:M790",
        source_name="TOGO M790 / JCM Medium 763",
        imported_ingredients=M790_IMPORTED_INGREDIENTS,
        imported_solutions=IMPORTED_SODIUM_CARBONATE,
        final_ingredients=SOLID_INGREDIENT_SIGNATURE,
        physical_state="SOLID_AGAR",
        solid=True,
        action="RESOLVED_TOGO_M790_ALKALINE_TRYPTONE_SOYA_BROTH_SOLID",
        event_notes=(
            "Moved sodium carbonate solution from an empty solution stub "
            "into a structured 20% stock used as a variable pH adjuster, "
            "corrected water units and agar naming, added the final pH "
            "range, and linked the MediaDive J763 liquid parent."
        ),
        references=(TOGO_M790, MEDIADIVE_J763),
        parent_media=J763_PARENT_SOLID_VARIANT,
        variant_relationship="PHYSICAL_STATE_VARIANT",
        variant_modifications=(SOLID_VARIANT_NOTE,),
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
