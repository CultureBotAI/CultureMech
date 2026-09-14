#!/usr/bin/env python3
"""Repair JCM/TOGO water and sparse product score-20 rows."""

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

CURATOR = "repair_jcm_togo_water_products_score20.py"
ACTION = "RESOLVED_JCM_TOGO_WATER_PRODUCTS_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

TOGO_M97 = "https://togomedium.org/medium/M97"
TOGO_M240 = "https://togomedium.org/medium/M240"
M97_SOURCE = "TOGO M97/JCM Medium 105 snapshot"
M240_SOURCE = "TOGO M240/JCM Medium 248 snapshot"

HIA_JCM = Path("bacterial/half_strength_heart_infusion_agar.yaml")
HIA_TOGO = Path("bacterial/TOGO_M97_Half_Strength_Heart_Infusion_Agar.yaml")
COW_MANURE_JCM = Path("bacterial/jcm_medium_no_248.yaml")
COW_MANURE_TOGO = Path("bacterial/togo_medium_m240.yaml")

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
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
class Target:
    path: Path
    expected_id: str
    expected_source_term: str
    accepted_ingredient_sets: frozenset[frozenset[str]]
    notes: str
    reference_url: str
    recipe: dict[str, Any]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _water(source: str) -> dict[str, Any]:
    return {
        "preferred_term": "Distilled water",
        "concentration": {"value": "1000", "unit": "ML_PER_L"},
        "source": source,
        "notes": f"{source} lists 1.0 L distilled water.",
        "term": _term("CHEBI:15377", "water"),
        "mediaingredientmech_chebi_term": _term("CHEBI:15377", "water"),
    }


def _agar(source: str) -> dict[str, Any]:
    return {
        "preferred_term": "Agar",
        "concentration": {"value": "15", "unit": "G_PER_L"},
        "source": source,
        "notes": f"{source} lists 15 g/L agar.",
        "term": _term("CHEBI:2509", "agar"),
        "mediaingredientmech_chebi_term": _term("CHEBI:2509", "agar"),
    }


HEART_INFUSION_AGAR_RECIPE = {
    "medium_type": "COMPLEX",
    "composition_type": "UNDEFINED",
    "physical_state": "SOLID_AGAR",
    "ingredients": [
        _water(M97_SOURCE),
        _agar(M97_SOURCE),
        {
            "preferred_term": "Heart infusion broth (BD-Difco)",
            "concentration": {"value": "12.5", "unit": "G_PER_L"},
            "source": M97_SOURCE,
            "notes": f"{M97_SOURCE} lists 12.5 g/L Heart infusion broth from BD-Difco.",
        },
    ],
}

COW_MANURE_RECIPE = {
    "medium_type": "COMPLEX",
    "composition_type": "UNDEFINED",
    "physical_state": "SOLID_AGAR",
    "ingredients": [
        _water(M240_SOURCE),
        {
            "preferred_term": "Cow manure",
            "concentration": {"value": "50", "unit": "G_PER_L"},
            "source": M240_SOURCE,
            "notes": f"{M240_SOURCE} lists 50 g/L dry cow manure.",
        },
        _agar(M240_SOURCE),
    ],
    "preparation_steps": [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Suspend 50.0 g of dry cow manure in 1.0 L distilled water, "
                "boil for 1 hr, filter first through cheesecloth and then "
                "paper, and make up the volume to 1.0 L."
            ),
        },
    ],
}

TARGETS = (
    Target(
        path=HIA_JCM,
        expected_id="CultureMech:002240",
        expected_source_term="mediadive.medium:J105",
        accepted_ingredient_sets=frozenset(
            {
                frozenset({"heart infusion broth", "agar"}),
                frozenset({"distilled water", "heart infusion broth (bd-difco)", "agar"}),
            }
        ),
        notes=(
            "TOGO M97 is a snapshot of JCM_M105 and records 1.0 L distilled "
            "water, 12.5 g/L Heart infusion broth from BD-Difco, and "
            "15 g/L agar."
        ),
        reference_url=TOGO_M97,
        recipe=HEART_INFUSION_AGAR_RECIPE,
    ),
    Target(
        path=HIA_TOGO,
        expected_id="CultureMech:010406",
        expected_source_term="TOGO:M97",
        accepted_ingredient_sets=frozenset(
            {
                frozenset({"distilled water", "heart infusion broth (bd-difco)", "agar"}),
            }
        ),
        notes=(
            "TOGO M97 records 1.0 L distilled water, 12.5 g/L Heart infusion "
            "broth from BD-Difco, and 15 g/L agar."
        ),
        reference_url=TOGO_M97,
        recipe=HEART_INFUSION_AGAR_RECIPE,
    ),
    Target(
        path=COW_MANURE_JCM,
        expected_id="CultureMech:002609",
        expected_source_term="mediadive.medium:J248",
        accepted_ingredient_sets=frozenset(
            {
                frozenset({"cow manure", "agar"}),
                frozenset({"distilled water", "cow manure", "agar"}),
            }
        ),
        notes=(
            "TOGO M240 is a snapshot of JCM_M248 and records 1.0 L distilled "
            "water, 50 g/L dry cow manure, and 15 g/L agar."
        ),
        reference_url=TOGO_M240,
        recipe=COW_MANURE_RECIPE,
    ),
    Target(
        path=COW_MANURE_TOGO,
        expected_id="CultureMech:008993",
        expected_source_term="TOGO:M240",
        accepted_ingredient_sets=frozenset(
            {
                frozenset({"distilled water", "cow manure", "agar"}),
            }
        ),
        notes=(
            "TOGO M240 records 1.0 L distilled water, 50 g/L dry cow manure, " "and 15 g/L agar."
        ),
        reference_url=TOGO_M240,
        recipe=COW_MANURE_RECIPE,
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True

    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ingredient_names(doc: dict[str, Any]) -> frozenset[str]:
    return frozenset(
        str(row.get("preferred_term") or "").lower()
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    )


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: found id {doc.get('id')!r}, " f"expected {target.expected_id!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != target.expected_source_term:
        raise ValueError(
            f"{target.path}: found source term {source_term!r}, "
            f"expected {target.expected_source_term!r}"
        )

    if _ingredient_names(doc) not in target.accepted_ingredient_sets:
        raise ValueError(f"{target.path}: ingredient list drifted")


def _grounded(row: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = row.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    ingredients = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    has_grounded = any(_grounded(row) for row in ingredients)
    has_unmapped = any(not _grounded(row) for row in ingredients)

    if has_grounded and "has_ontology_mappings" not in flags:
        flags.append("has_ontology_mappings")
    elif not has_grounded and "has_ontology_mappings" in flags:
        flags.remove("has_ontology_mappings")

    if has_unmapped and "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")
    elif not has_unmapped and "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    if flags:
        doc["data_quality_flags"] = flags
    else:
        doc.pop("data_quality_flags", None)


def _ensure_reference(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")
    found = {row.get("reference") for row in references if isinstance(row, dict)}
    if target.reference_url not in found:
        references.append({"reference": target.reference_url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": target.reference_url,
        "notes": target.notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.path}: curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_target(doc, target)

    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        if field in target.recipe:
            repaired[field] = copy.deepcopy(target.recipe[field])
        else:
            repaired.pop(field, None)

    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired)
    _ensure_reference(repaired, target)
    _append_curation_event(repaired, target)
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
    for path, doc in sorted(plans.items()):
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
