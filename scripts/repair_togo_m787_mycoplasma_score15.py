#!/usr/bin/env python3
"""Repair MediaDive/TOGO JCM 761 Mycoplasma Medium stock handling."""

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
JCM_J761_PATH = Path("bacterial/mycoplasma_medium.yaml")
TOGO_M787_PATH = Path("bacterial/TOGO_M787_Mycoplasma_Medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m787_mycoplasma_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J761 = "https://mediadive.dsmz.de/medium/J761"
TOGO_M787 = "https://togomedium.org/medium/M787"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    source_term: str
    source_name: str
    imported_ingredients: tuple[Component, ...]
    imported_solutions: tuple[Component, ...]
    action: str
    event_notes: str
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()


JCM_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Heart Infusion Broth", "17.5", "G_PER_L"),
    ("Agar", "10", "G_PER_L"),
    ("Horse serum", "200", "G_PER_L"),
    ("Yeast extract", "100", "G_PER_L"),
)

TOGO_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "700", "G_PER_L"),
    ("Bacto agar (BD-Difco)", "10", "G_PER_L"),
    ("Heart infusion broth (BD-Difco)", "17.5", "G_PER_L"),
    ("Horse serum (heat--inactivated)", "200", "G_PER_L"),
)

TOGO_IMPORTED_SOLUTIONS: tuple[Component, ...] = (
    ("25% Yeast Extract Solution", "100", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "700.0", "ML_PER_L"),
    ("Heart Infusion Broth", "17.5", "G_PER_L"),
    ("Agar", "10.0", "G_PER_L"),
    ("Horse serum", "200.0", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("25% Yeast Extract Solution", "100.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Agar": ("CHEBI:2509", "agar"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Yeast extract": ("NITROGEN_SOURCE", "PROTEIN_SOURCE", "VITAMIN_SOURCE"),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Agar": ("SOLIDIFYING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
}

M787_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M787_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010196",
    "name": "mycoplasma_medium",
    "notes": (
        "TOGO M787 imports the same JCM Medium 761 Mycoplasma Medium "
        "formulation represented by MediaDive J761."
    ),
}

J761_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J761_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003105",
    "name": "mycoplasma_medium",
    "notes": M787_CHILD["notes"],
}

SOURCE_NOTE = (
    "MediaDive J761 and TOGO M787 describe JCM Medium 761 Mycoplasma "
    "Medium as a 1.0 L solid agar medium containing 700.0 ml distilled "
    "water, 17.5 g Heart Infusion Broth, 10.0 g Bacto agar, 200.0 ml "
    "heat-inactivated horse serum, and 100.0 ml 25% Yeast Extract Solution."
)

PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Dissolve Heart Infusion Broth and Agar in 700.0 ml/L "
            "distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the basal agar at 121 C for 15 min.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "Cool to 55 C and aseptically add 200.0 ml/L heat-inactivated "
            "horse serum and 100.0 ml/L filter-sterilized 25% Yeast Extract "
            "Solution warmed to 55 C."
        ),
    },
    {
        "step_number": 4,
        "action": "ADJUST_PH",
        "description": "Adjust final pH to 7.2-7.6.",
    },
]

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "Autoclave the basal agar before adding filter-sterilized solution.",
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
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
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
        _component(
            "Distilled water",
            "700.0",
            "ML_PER_L",
            source=source,
            notes=f"{source} contributes 700.0 ml/L distilled water.",
        ),
        _component(
            "Heart Infusion Broth",
            "17.5",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 17.5 g/L Heart Infusion Broth from BD-Difco.",
        ),
        _component(
            "Agar",
            "10.0",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 10.0 g/L Bacto agar from BD-Difco.",
        ),
        _component(
            "Horse serum",
            "200.0",
            "ML_PER_L",
            source=source,
            notes=f"{source} adds 200.0 ml/L heat-inactivated horse serum.",
        ),
    ]


def _solutions(source: str) -> list[dict[str, Any]]:
    return [
        {
            "preferred_term": "25% Yeast Extract Solution",
            "concentration": {"value": "100.0", "unit": "ML_PER_L"},
            "source": source,
            "notes": f"{source} adds 100.0 ml/L 25% Yeast Extract Solution.",
            "composition": [
                _component(
                    "Yeast extract",
                    "25.0",
                    "PERCENT_W_V",
                    source=source,
                    notes=(
                        f"{source} specifies 25% Yeast Extract Solution as "
                        "25.0% w/v."
                    ),
                )
            ],
        }
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
            f"{target.path}: expected {target.record_id}, found {doc.get('id')}"
        )
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
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    _put_after(repaired, "ph_range", {"min": 7.2, "max": 7.6}, "physical_state")
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
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
            "references",
        )
        _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
        _put_after(
            repaired,
            "variant_modifications",
            [J761_PARENT["notes"]],
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
    _append_event(
        repaired,
        action=target.action,
        references=target.references,
        notes=target.event_notes,
    )
    return repaired


TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM_J761_PATH,
        record_id="CultureMech:003105",
        source_term="mediadive.medium:J761",
        source_name="MediaDive J761 / JCM Medium 761",
        imported_ingredients=JCM_IMPORTED_INGREDIENTS,
        imported_solutions=(),
        action="RESOLVED_JCM_761_MYCOPLASMA_MEDIUM",
        event_notes=(
            "Restored distilled water, corrected horse serum and the 25% "
            "Yeast Extract Solution from flattened mass concentrations to "
            "volume additions, nested the yeast-extract stock composition, "
            "added the final pH range, and linked the TOGO M787 source "
            "duplicate."
        ),
        references=(MEDIADIVE_J761,),
        variant_children=(M787_CHILD,),
    ),
    Target(
        path=TOGO_M787_PATH,
        record_id="CultureMech:010196",
        source_term="TOGO:M787",
        source_name="TOGO M787 / JCM Medium 761",
        imported_ingredients=TOGO_IMPORTED_INGREDIENTS,
        imported_solutions=TOGO_IMPORTED_SOLUTIONS,
        action="RESOLVED_TOGO_M787_MYCOPLASMA_MEDIUM",
        event_notes=(
            "Moved 25% Yeast Extract Solution from an empty solution stub "
            "into a structured stock solution, corrected water, horse serum, "
            "and yeast-extract stock units, added the final pH range, and "
            "linked the MediaDive J761 source duplicate."
        ),
        references=(TOGO_M787, MEDIADIVE_J761),
        parent_media=J761_PARENT,
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
