#!/usr/bin/env python3
"""Repair MediaDive/TOGO JCM 15 Tomato Juice Agar records."""

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
MEDIADIVE_J15_PATH = Path("bacterial/tomato_juice_agar.yaml")
TOGO_M8_PATH = Path("bacterial/TOGO_M8_Tomato_Juice_Agar.yaml")
SOLUTION_3636_PATH = Path("bacterial/mediadive_3636_Main_sol_J15.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m8_tomato_juice_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J15 = "https://mediadive.dsmz.de/medium/J15"
JCM_15 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=15"
TOGO_M8 = "https://togomedium.org/medium/M8"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class MediumTarget:
    path: Path
    record_id: str
    source_term: str
    source_name: str
    imported_ingredients: tuple[Component, ...]
    action: str
    event_notes: str
    references: tuple[str, ...]
    parent_media: dict[str, Any] | None = None
    variant_children: tuple[dict[str, Any], ...] = ()


J15_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Tryptone", "10", "G_PER_L"),
    ("Yeast extract", "10", "G_PER_L"),
    ("Tomato juice", "200", "G_PER_L"),
    ("Agar", "11", "G_PER_L"),
)

M8_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "800", "G_PER_L"),
    ("Tomato juice, filtered, pH 7.0", "200", "G_PER_L"),
    ("Agar", "11", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "10", "G_PER_L"),
    ("Tryptone (BD-Difco)", "10", "G_PER_L"),
)

IMPORTED_SOLUTION_3636_COMPOSITION: tuple[Component, ...] = (
    ("Tryptone", "10", "G_PER_L"),
    ("Yeast extract", "10", "G_PER_L"),
    ("Tomato juice", "200", "PERCENT_V_V"),
    ("Agar", "11", "G_PER_L"),
    ("Distilled water", "800", "PERCENT_V_V"),
)

PLACEHOLDER_INGREDIENTS: tuple[Component, ...] = (
    ("See source for composition", "variable", "VARIABLE"),
)

DIRECT_COMPOSITION: tuple[Component, ...] = (
    ("Distilled water", "800.0", "ML_PER_L"),
    ("Tomato juice", "200.0", "ML_PER_L"),
    ("Agar", "11.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "10.0", "G_PER_L"),
    ("Tryptone (BD-Difco)", "10.0", "G_PER_L"),
)

SOLUTION_3636_COMPOSITION: tuple[Component, ...] = (
    ("Tryptone (BD-Difco)", "10.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "10.0", "G_PER_L"),
    ("Tomato juice", "200.0", "ML_PER_L"),
    ("Agar", "11.0", "G_PER_L"),
    ("Distilled water", "800.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Tomato juice": ("FOODON:03301454", "Tomato juice"),
    "Agar": ("CHEBI:2509", "agar"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "Yeast extract"),
    "Tryptone (BD-Difco)": ("MICRO:0000182", "Tryptone"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Yeast extract (BD-Difco)": ("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
    "Tryptone (BD-Difco)": ("PROTEIN_SOURCE",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Agar": ("SOLIDIFYING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

SOURCE_NOTE = (
    "JCM Medium 15 / Tomato Juice Agar lists 800.0 ml/L distilled water, "
    "200.0 ml/L filtered tomato juice at pH 7.0, 11.0 g/L agar, 10.0 g/L "
    "BD-Difco yeast extract, and 10.0 g/L BD-Difco tryptone, adjusted to "
    "final pH 7.2; TOGO M8 and MediaDive J15 report the same JCM recipe."
)

PREPARATION_STEPS = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix 800.0 ml/L distilled water, 200.0 ml/L filtered tomato "
            "juice at pH 7.0, 11.0 g/L agar, 10.0 g/L BD-Difco yeast "
            "extract, and 10.0 g/L BD-Difco tryptone."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.2.",
    },
)

M8_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M8_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010318",
    "name": "tomato_juice_agar",
    "notes": (
        "TOGO M8 imports the same JCM Medium 15 Tomato Juice Agar "
        "formulation represented by MediaDive J15."
    ),
}

J15_PARENT = {
    "path": f"data/normalized_yaml/{MEDIADIVE_J15_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:002518",
    "name": "tomato_juice_agar",
    "notes": M8_CHILD["notes"],
}


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.load(handle, Loader=YAML_LOADER)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return data


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
        "term": _term(*GROUNDINGS[preferred_term]),
    }
    if preferred_term == "Tomato juice":
        row["notes"] = (
            f"{source} lists {value} ml/L filtered tomato juice that was "
            "adjusted to pH 7.0 before addition."
        )

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


def _composition(
    source: str,
    components: tuple[Component, ...],
) -> list[dict[str, Any]]:
    return [_component(name, value, unit, source=source) for name, value, unit in components]


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

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in (target.imported_ingredients, DIRECT_COMPOSITION):
        raise ValueError(f"{target.path}: ingredient signature drifted")


def _ensure_solution_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:012716":
        raise ValueError(
            f"{SOLUTION_3636_PATH}: expected CultureMech:012716, " f"found {doc.get('id')}"
        )
    if _term_id(doc) != "mediadive.solution:3636":
        raise ValueError(f"{SOLUTION_3636_PATH}: expected MediaDive solution 3636")

    composition = _signature(doc.get("composition"), "composition")
    if composition not in (
        IMPORTED_SOLUTION_3636_COMPOSITION,
        SOLUTION_3636_COMPOSITION,
    ):
        raise ValueError(f"{SOLUTION_3636_PATH}: composition signature drifted")

    ingredients = _signature(doc.get("ingredients"), "ingredients")
    if ingredients not in (PLACEHOLDER_INGREDIENTS, ()):
        raise ValueError(f"{SOLUTION_3636_PATH}: ingredient signature drifted")


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
    for key in (
        "term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _composition_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    rows.extend(row for row in doc.get("composition") or [] if isinstance(row, dict))
    return rows


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

    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)

    components = _composition_components(doc)
    if any(not _grounded(component) for component in components):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    else:
        while "has_unmapped_ingredients" in flags:
            flags.remove("has_unmapped_ingredients")


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


def repair_medium_record(
    doc: dict[str, Any],
    target: MediumTarget,
) -> dict[str, Any]:
    _ensure_medium_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.2, "physical_state")
    repaired.pop("kg_microbe_match", None)
    _put_after(repaired, "notes", SOURCE_NOTE, "media_term")
    repaired["ingredients"] = _composition(target.source_name, DIRECT_COMPOSITION)
    repaired.pop("solutions", None)
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "ingredients",
    )

    _ensure_references(repaired, target.references)
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
            [M8_CHILD["notes"]],
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
    _append_event(
        repaired,
        action=target.action,
        references=target.references,
        notes=target.event_notes,
    )
    return repaired


def repair_solution_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_solution_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _composition(
        "MediaDive solution 3636 / JCM Medium 15",
        SOLUTION_3636_COMPOSITION,
    )
    repaired.pop("ingredients", None)
    repaired["preparation_notes"] = (
        "Mix BD-Difco tryptone, BD-Difco yeast extract, filtered tomato juice, "
        "agar, and distilled water, then adjust pH to 7.2."
    )
    _put_after(
        repaired,
        "notes",
        (
            "MediaDive solution 3636 is the complete main solution for JCM "
            "Medium J15 / Tomato Juice Agar."
        ),
        "preparation_notes",
    )

    _ensure_flags(repaired)
    _ensure_references(repaired, (MEDIADIVE_J15,))
    _append_event(
        repaired,
        action="RESOLVED_MEDIADIVE_3636_MAIN_SOL_J15",
        references=(MEDIADIVE_J15,),
        notes=(
            "Corrected the Tomato juice and Distilled water rows from false "
            "percent-volume values to source ml/L units, restored the "
            "BD-Difco attributes for tryptone and yeast extract, and removed "
            "the placeholder top-level ingredient."
        ),
    )
    return repaired


TARGETS: tuple[MediumTarget, ...] = (
    MediumTarget(
        path=MEDIADIVE_J15_PATH,
        record_id="CultureMech:002518",
        source_term="mediadive.medium:J15",
        source_name="MediaDive J15 / JCM Medium 15",
        imported_ingredients=J15_IMPORTED_INGREDIENTS,
        action="RESOLVED_MEDIADIVE_J15_TOMATO_JUICE_AGAR",
        event_notes=(
            "Corrected tomato juice from 200 g/L to 200.0 ml/L, added "
            "800.0 ml/L distilled water, restored BD-Difco tryptone and "
            "yeast extract names, and linked the TOGO M8 source duplicate."
        ),
        references=(MEDIADIVE_J15, JCM_15, TOGO_M8),
        variant_children=(M8_CHILD,),
    ),
    MediumTarget(
        path=TOGO_M8_PATH,
        record_id="CultureMech:010318",
        source_term="TOGO:M8",
        source_name="TOGO M8 / JCM Medium 15",
        imported_ingredients=M8_IMPORTED_INGREDIENTS,
        action="RESOLVED_TOGO_M8_TOMATO_JUICE_AGAR",
        event_notes=(
            "Corrected water from 800 g/L to 800.0 ml/L, corrected tomato "
            "juice from 200 g/L to 200.0 ml/L, added final pH 7.2 from TOGO "
            "M8 and MediaDive J15, and linked the MediaDive J15 source "
            "duplicate."
        ),
        references=(TOGO_M8, MEDIADIVE_J15, JCM_15),
        parent_media=J15_PARENT,
    ),
)


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_medium_record(_load(path), target)

    solution_path = normalized / SOLUTION_3636_PATH
    plans[solution_path] = repair_solution_record(_load(solution_path))
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
