#!/usr/bin/env python3
"""Repair MediaDive/TOGO JCM 802 Modified CSY-3 Agar records."""

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
JCM_J802_PATH = Path("bacterial/modified_csy_3_agar.yaml")
TOGO_M837_PATH = Path("bacterial/TOGO_M837_Modified_CSY-3_Agar.yaml")
SOLUTION_4751_PATH = Path("bacterial/mediadive_4751_Main_sol_J802.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m837_modified_csy3_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

MEDIADIVE_J802 = "https://mediadive.dsmz.de/medium/J802"
JCM_J802 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=802"
TOGO_M837 = "https://togomedium.org/medium/M837"

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


J802_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Casitone", "1", "G_PER_L"),
    ("Phytone peptone", "1", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("Ferric ammonium citrate", "0.4", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Sea water", "1000", "G_PER_L"),
)

M837_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Seawater", "1", "G_PER_L"),
    ("Ferric ammonium citrate", "0.4", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "1", "G_PER_L"),
    ("Casitone (BD-Difco)", "1", "G_PER_L"),
    ("Phytone peptone (BD-BBL)", "1", "G_PER_L"),
)

IMPORTED_SOLUTION_COMPOSITION: tuple[Component, ...] = (
    ("Casitone", "1", "G_PER_L"),
    ("Phytone peptone", "1", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("Ferric ammonium citrate", "0.4", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Sea water", "1000", "PERCENT_V_V"),
)

PLACEHOLDER_INGREDIENTS: tuple[Component, ...] = (
    ("See source for composition", "variable", "VARIABLE"),
)

FINAL_COMPOSITION: tuple[Component, ...] = (
    ("Casitone (BD-Difco)", "1.0", "G_PER_L"),
    ("Phytone peptone (BD-BBL)", "1.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "1.0", "G_PER_L"),
    ("Ferric ammonium citrate", "0.4", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Sea water", "1000.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Phytone peptone (BD-BBL)": ("FOODON:03315720", "Soy peptone"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "Yeast extract"),
    "Ferric ammonium citrate": ("CHEBI:31604", "ferric ammonium citrate"),
    "Agar": ("CHEBI:2509", "agar"),
    "Sea water": ("ENVO:00002149", "sea water"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Casitone (BD-Difco)": ("PROTEIN_SOURCE",),
    "Phytone peptone (BD-BBL)": ("PROTEIN_SOURCE",),
    "Yeast extract (BD-Difco)": ("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
    "Ferric ammonium citrate": ("IRON_SOURCE",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Agar": ("SOLIDIFYING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

SOURCE_NOTE = (
    "MediaDive J802 describes JCM Medium 802 Modified CSY-3 Agar as 1.0 g/L "
    "BD-Difco Casitone, 1.0 g/L BD-BBL Phytone peptone, 1.0 g/L BD-Difco "
    "yeast extract, 0.4 g/L ferric ammonium citrate, and 15.0 g/L agar in "
    "1000.0 ml/L sea water, adjusted to pH 7.5."
)

PREPARATION_STEPS = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Dissolve 1.0 g/L BD-Difco Casitone, 1.0 g/L BD-BBL Phytone "
            "peptone, 1.0 g/L BD-Difco yeast extract, 0.4 g/L ferric ammonium "
            "citrate, and 15.0 g/L agar in 1000.0 ml/L sea water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.5.",
    },
)

M837_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M837_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010251",
    "name": "modified_csy_3_agar",
    "notes": (
        "TOGO M837 imports the same JCM Medium 802 Modified CSY-3 Agar "
        "formulation represented by MediaDive J802."
    ),
}

J802_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J802_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:003147",
    "name": "modified_csy_3_agar",
    "notes": M837_CHILD["notes"],
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
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
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


def _composition(source: str) -> list[dict[str, Any]]:
    return [
        _component(name, value, unit, source=source)
        for name, value, unit in FINAL_COMPOSITION
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
        raise ValueError(
            f"{target.path}: expected {target.record_id}, found {doc.get('id')}"
        )
    if _media_term_id(doc) != target.source_term:
        raise ValueError(f"{target.path}: expected media term {target.source_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (target.imported_ingredients, FINAL_COMPOSITION):
        raise ValueError(f"{target.path}: ingredient signature drifted")


def _ensure_solution_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:013698":
        raise ValueError(
            f"{SOLUTION_4751_PATH}: expected CultureMech:013698, "
            f"found {doc.get('id')}"
        )
    if _term_id(doc) != "mediadive.solution:4751":
        raise ValueError(f"{SOLUTION_4751_PATH}: expected MediaDive solution 4751")

    composition_signature = _signature(doc.get("composition"), "composition")
    if composition_signature not in (IMPORTED_SOLUTION_COMPOSITION, FINAL_COMPOSITION):
        raise ValueError(f"{SOLUTION_4751_PATH}: composition signature drifted")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (PLACEHOLDER_INGREDIENTS, ()):
        raise ValueError(f"{SOLUTION_4751_PATH}: ingredient signature drifted")


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
    for key in (
        "term",
        "chebi_term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _composition_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    components = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    components.extend(i for i in doc.get("composition") or [] if isinstance(i, dict))
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


def repair_medium_record(
    doc: dict[str, Any],
    target: MediumTarget,
) -> dict[str, Any]:
    _ensure_medium_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    _put_after(repaired, "ph_range", {"min": 7.5, "max": 7.5}, "physical_state")
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "notes", SOURCE_NOTE, "media_term")
    repaired["ingredients"] = _composition(target.source_name)
    repaired.pop("solutions", None)
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "ingredients",
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
            [M837_CHILD["notes"]],
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


def repair_solution_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_solution_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _composition("MediaDive solution 4751 / JCM Medium 802")
    repaired.pop("ingredients", None)
    repaired["preparation_notes"] = "Adjust pH to 7.5."
    _put_after(
        repaired,
        "notes",
        (
            "MediaDive solution 4751 is the main solution for JCM Medium 802 "
            "Modified CSY-3 Agar."
        ),
        "preparation_notes",
    )

    _ensure_flags(repaired)
    _ensure_references(repaired, (MEDIADIVE_J802,))
    _append_event(
        repaired,
        action="RESOLVED_MEDIADIVE_4751_MAIN_SOL_J802",
        references=(MEDIADIVE_J802,),
        notes=(
            "Corrected the sea-water quantity from 1000% v/v to 1000.0 ml/L, "
            "restored the same source-level component names as JCM Medium 802, "
            "and removed the placeholder top-level ingredient."
        ),
    )
    return repaired


TARGETS: tuple[MediumTarget, ...] = (
    MediumTarget(
        path=JCM_J802_PATH,
        record_id="CultureMech:003147",
        source_term="mediadive.medium:J802",
        source_name="MediaDive J802 / JCM Medium 802",
        imported_ingredients=J802_IMPORTED_INGREDIENTS,
        action="RESOLVED_JCM_802_MODIFIED_CSY3_AGAR",
        event_notes=(
            "Restored the MediaDive J802 source-level BD-Difco Casitone, "
            "BD-BBL Phytone peptone, BD-Difco yeast extract, ferric ammonium "
            "citrate, agar, and sea-water formulation; corrected sea water "
            "from a mass concentration to 1000.0 ml/L; and linked the TOGO "
            "M837 source duplicate."
        ),
        references=(MEDIADIVE_J802, JCM_J802),
        variant_children=(M837_CHILD,),
    ),
    MediumTarget(
        path=TOGO_M837_PATH,
        record_id="CultureMech:010251",
        source_term="TOGO:M837",
        source_name="TOGO M837 / JCM Medium 802",
        imported_ingredients=M837_IMPORTED_INGREDIENTS,
        action="RESOLVED_TOGO_M837_MODIFIED_CSY3_AGAR",
        event_notes=(
            "Restored the source-level BD-Difco Casitone, BD-BBL Phytone "
            "peptone, BD-Difco yeast extract, ferric ammonium citrate, agar, "
            "and sea-water formulation from MediaDive J802; corrected "
            "sea water from 1 g/L to 1000.0 ml/L; added pH 7.5; and linked "
            "the MediaDive J802 source duplicate."
        ),
        references=(TOGO_M837, MEDIADIVE_J802, JCM_J802),
        parent_media=J802_PARENT,
    ),
)


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_medium_record(_load(path), target)

    solution_path = normalized / SOLUTION_4751_PATH
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
