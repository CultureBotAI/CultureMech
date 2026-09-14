#!/usr/bin/env python3
"""Repair the score-35 Taiyang Medium No.9 public MediaDive placeholder."""

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

CURATOR = "repair_mediadive_p2_score35.py"
ACTION = "RESOLVED_MEDIADIVE_P2_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

P2_TAIYANG = "bacterial/taiyang_medium_no_9_prototype.yaml"
EXPECTED_ID = "CultureMech:010432"
EXPECTED_SOURCE_TERM = "mediadive.medium:P2"

P2_PUBLIC = "https://www.bacmedia.dsmz.de/medium/P2"
SRC_P2 = "MediaDive public Medium P2"

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
    "salinity",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
    "parent_media",
    "variant_relationship",
    "variant_modifications",
    "variant_children",
)


@dataclass(frozen=True)
class RecipeUpdate:
    path: str
    notes: str
    recipe: dict[str, Any]
    reference_urls: tuple[str, ...]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    identifier: str | None = None,
    label: str | None = None,
    notes: str | None = None,
) -> dict[str, Any]:
    component: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SRC_P2,
    }
    if notes:
        component["notes"] = notes
    if identifier and label:
        component["term"] = _term(identifier, label)
        if identifier.startswith("CHEBI:"):
            component["mediaingredientmech_chebi_term"] = _term(identifier, label)
    return component


def _g_per_l(
    preferred_term: str,
    value: str,
    term: tuple[str, str] | None = None,
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    identifier, label = term or (None, None)
    return _component(
        preferred_term,
        value,
        "G_PER_L",
        identifier=identifier,
        label=label,
        notes=notes,
    )


def _ml_per_l(
    preferred_term: str,
    value: str,
    term: tuple[str, str] | None = None,
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    identifier, label = term or (None, None)
    return _component(
        preferred_term,
        value,
        "ML_PER_L",
        identifier=identifier,
        label=label,
        notes=notes,
    )


ARTIFICAL_SEA_WATER = {
    "preferred_term": "Artifical Sea Water",
    "concentration": {"value": "50", "unit": "ML_PER_L"},
    "notes": "P2 adds 50 ml Artifical Sea Water to 1 L Taiyang Medium No.9.",
    "composition": [
        _g_per_l("NaCl", "23.47", ("CHEBI:26710", "sodium chloride")),
        _g_per_l("Na2SO4", "3.92", ("CHEBI:32149", "sodium sulfate")),
        _g_per_l(
            "MgCl2 x 6 H2O",
            "10.64",
            ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        ),
        _g_per_l("CaCl2", "1.10", ("CHEBI:3312", "calcium dichloride")),
        _g_per_l("NaHCO3", "0.192", ("CHEBI:32139", "sodium hydrogencarbonate")),
        _g_per_l("KCl", "0.664", ("CHEBI:32588", "potassium chloride")),
        _g_per_l("KBr", "0.096", ("CHEBI:32030", "potassium bromide")),
        _g_per_l("H3BO3", "0.026", ("CHEBI:33118", "boric acid")),
        _g_per_l("SrCl2", "0.024", ("CHEBI:36383", "strontium dichloride")),
        _g_per_l("NaF", "0.003", ("CHEBI:28741", "sodium fluoride")),
    ],
}

HAEMIN_SOLUTION = {
    "preferred_term": "Haemin solution",
    "concentration": {"value": "10", "unit": "ML_PER_L"},
    "notes": "P2 adds 10 ml Haemin solution to 1 L Taiyang Medium No.9.",
    "composition": [
        _g_per_l("Haemin", "0.5", ("CHEBI:50385", "hemin")),
        _ml_per_l(
            "NaOH (1 N)",
            "10",
            ("CHEBI:32145", "sodium hydroxide"),
            notes="P2 dissolves 50 mg Haemin in 1 ml 1 N NaOH and fills the stock to 100 ml.",
        ),
    ],
}

UPDATE = RecipeUpdate(
    path=P2_TAIYANG,
    notes=(
        "MediaDive public Medium P2 provides a user-provided Taiyang Medium "
        "No.9 prototype formulation with clarified rumen fluid, sheep blood, "
        "carbohydrate polymers, filtered pyruvate, trehalose, L-Cysteine HCl, "
        "Haemin solution, and Artifical Sea Water. MediaDive lists this public "
        "medium as not curated/tested and with no valid reference, so only "
        "formulation and preparation fields visible on the MediaDive page were "
        "curated."
    ),
    recipe={
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ml_per_l("Clarified rumen fluid", "25"),
            _ml_per_l("Sheep blood", "25"),
            _g_per_l("Peptone", "1"),
            _g_per_l("Yeast extract", "1", ("FOODON:03315426", "yeast extract")),
            _g_per_l("NaCl", "1", ("CHEBI:26710", "sodium chloride")),
            _g_per_l("Cellulose", "0.5", ("CHEBI:18246", "Cellulose")),
            _g_per_l("Pectin", "0.5", ("CHEBI:17309", "Pectin")),
            _g_per_l("Starch", "0.5", ("CHEBI:28017", "Starch")),
            _g_per_l("Inulin", "0.5", ("CHEBI:15443", "Inulin")),
            _g_per_l("Trehalose", "0.5", ("CHEBI:27082", "Trehalose")),
            _g_per_l("Sodium pyruvate", "1", ("CHEBI:50144", "sodium pyruvate")),
            _g_per_l("dextrin", "0.5", ("CHEBI:28675", "Dextrin")),
            _g_per_l("L-Cysteine HCl", "0.1", ("CHEBI:91247", "L-Cysteine HCl")),
            _g_per_l("Agar", "15", ("CHEBI:2509", "agar")),
        ],
        "solutions": [
            ARTIFICAL_SEA_WATER,
            HAEMIN_SOLUTION,
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Dissolve all Artifical Sea Water components in water.",
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": "Autoclave the Artifical Sea Water at 121 C for 20 min and store at room temperature.",
            },
            {
                "step_number": 3,
                "action": "FILTER_STERILIZE",
                "description": (
                    "Dissolve 50 mg Haemin in 1 ml 1 N NaOH, make up to 100 "
                    "ml with distilled water, filter sterilize, and store "
                    "refrigerated."
                ),
            },
            {
                "step_number": 4,
                "action": "MIX",
                "description": (
                    "Mix clarified rumen fluid, 50 ml Artifical Sea Water, "
                    "peptone, yeast extract, NaCl, cellulose, pectin, starch, "
                    "inulin, dextrin, agar, and water; leave out trehalose, "
                    "sodium pyruvate, L-Cysteine HCl, sheep blood, and Haemin "
                    "solution until after autoclaving."
                ),
            },
            {
                "step_number": 5,
                "action": "AUTOCLAVE",
                "description": "Autoclave the main medium at 121 C for 15 min.",
            },
            {
                "step_number": 6,
                "action": "MIX",
                "description": (
                    "Add filter-sterilized trehalose, sodium pyruvate, "
                    "L-Cysteine HCl, and Haemin solution, then add sheep "
                    "blood after autoclaving."
                ),
            },
            {
                "step_number": 7,
                "action": "STORE",
                "description": "Place the completed medium or agar in an anaerobic workstation before use.",
            },
        ],
        "sterilization": {
            "method": "AUTOCLAVE",
            "notes": (
                "The main medium is autoclaved; trehalose, sodium pyruvate, "
                "L-Cysteine HCl, sheep blood, and Haemin solution are added "
                "after autoclaving."
            ),
        },
    },
    reference_urls=(P2_PUBLIC,),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term") or {}
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _require_target(doc: dict[str, Any], relative_path: str) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{relative_path}: found id {doc.get('id')!r}, expected {EXPECTED_ID!r}")

    if _source_term_id(doc) != EXPECTED_SOURCE_TERM:
        raise ValueError(
            f"{relative_path}: found source term {_source_term_id(doc)!r}, "
            f"expected {EXPECTED_SOURCE_TERM!r}"
        )


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
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
        nested_components = (
            [i for i in nested if isinstance(i, dict)] if isinstance(nested, list) else []
        )
        components.extend(nested_components or [solution])
    return components


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
        if obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    components = _composition_components(doc)
    if any(_grounded(component) for component in components):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")

    has_unmapped = any(not _grounded(component) for component in components)
    if has_unmapped:
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    if flags:
        doc["data_quality_flags"] = flags
    else:
        doc.pop("data_quality_flags", None)


def _ensure_references(doc: dict[str, Any], update: RecipeUpdate) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{update.path}: references is not a list")

    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in update.reference_urls:
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _append_curation_event(doc: dict[str, Any], update: RecipeUpdate) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved score-35 MediaDive P2 placeholder graph",
        "source": "; ".join(update.reference_urls),
        "notes": update.notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{update.path}: curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def _repair_with_recipe(doc: dict[str, Any], update: RecipeUpdate) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        if field in update.recipe:
            repaired[field] = copy.deepcopy(update.recipe[field])
        else:
            repaired.pop(field, None)
    repaired["notes"] = update.notes
    _ensure_flags(repaired)
    _ensure_references(repaired, update)
    _append_curation_event(repaired, update)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / UPDATE.path
    doc = _load(path)
    _require_target(doc, UPDATE.path)
    return {path: _repair_with_recipe(doc, UPDATE)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
        if args.apply:
            changed = write_record(path, doc)
        else:
            changed = dump_record(doc) != path.read_text(encoding="utf-8")
        if changed:
            changed_count += 1
            print(path.relative_to(args.normalized_dir))

    action = "Updated" if args.apply else "Would update"
    print(f"{action} {changed_count} MediaDive P2 score-35 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
