#!/usr/bin/env python3
"""Repair sparse MediaDive/JCM score-20 product siblings."""

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

CURATOR = "repair_jcm_sparse_siblings_score20.py"
ACTION = "RESOLVED_JCM_SPARSE_SIBLINGS_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

ME_AGAR = Path("bacterial/me_agar.yaml")
THIOGLYCOLLATE = Path("bacterial/thioglycollate_medium.yaml")

TOGO_M250 = "https://togomedium.org/medium/M250"
TOGO_M530 = "https://togomedium.org/medium/M530"
M250_SOURCE = "TOGO M250/JCM Medium 258 snapshot"
M530_SOURCE = "TOGO M530/JCM Medium 529 snapshot"

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
    expected_media_term: str
    accepted_ingredient_sets: frozenset[frozenset[str]]
    notes: str
    reference_url: str
    recipe: dict[str, Any]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    ingredient: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term is not None:
        ingredient["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            ingredient["mediaingredientmech_chebi_term"] = _term(*term)
    return ingredient


TARGETS: tuple[Target, ...] = (
    Target(
        path=ME_AGAR,
        expected_id="CultureMech:002616",
        expected_media_term="mediadive.medium:J258",
        accepted_ingredient_sets=frozenset(
            {
                frozenset({"malt extract agar"}),
                frozenset({"distilled water", "malt extract agar (oxoid)"}),
            }
        ),
        notes=(
            "TOGO M250 is a snapshot of JCM_M258 and records 50 g/L Malt "
            "extract agar from Oxoid in distilled water with autoclaving at "
            "115 C for 10 min."
        ),
        reference_url=TOGO_M250,
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Distilled water",
                    "1000",
                    "ML_PER_L",
                    source=M250_SOURCE,
                    notes=(
                        "TOGO M250 snapshots JCM_M258 and lists 1.0 L "
                        "distilled water."
                    ),
                    term=("CHEBI:15377", "water"),
                ),
                _ingredient(
                    "Malt extract agar (Oxoid)",
                    "50",
                    "G_PER_L",
                    source=M250_SOURCE,
                    notes=(
                        "TOGO M250 snapshots JCM_M258 and lists 50 g/L Malt "
                        "extract agar from Oxoid."
                    ),
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 115 C for 10 min.",
                },
            ],
        },
    ),
    Target(
        path=THIOGLYCOLLATE,
        expected_id="CultureMech:002878",
        expected_media_term="mediadive.medium:J529",
        accepted_ingredient_sets=frozenset(
            {
                frozenset({"thioglycolate"}),
                frozenset({"distilled water", "thioglycollate medium (sigma)"}),
            }
        ),
        notes=(
            "TOGO M530 is a snapshot of JCM_M529 and records 29.8 g/L "
            "Thioglycollate medium from Sigma in distilled water; the TOGO "
            "snapshot describes the medium as semisolid."
        ),
        reference_url=TOGO_M530,
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SEMISOLID",
            "ingredients": [
                _ingredient(
                    "Distilled water",
                    "1000",
                    "ML_PER_L",
                    source=M530_SOURCE,
                    notes=(
                        "TOGO M530 snapshots JCM_M529 and lists 1.0 L "
                        "distilled water."
                    ),
                    term=("CHEBI:15377", "water"),
                ),
                _ingredient(
                    "Thioglycollate medium (Sigma)",
                    "29.8",
                    "G_PER_L",
                    source=M530_SOURCE,
                    notes=(
                        "TOGO M530 snapshots JCM_M529 and lists 29.8 g/L "
                        "Thioglycollate medium from Sigma."
                    ),
                ),
            ],
        },
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


def _media_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ingredient_terms(doc: dict[str, Any]) -> frozenset[str]:
    return frozenset(
        str(row.get("preferred_term") or "").lower()
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    )


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected immutable id {target.expected_id}, "
            f"found {doc.get('id')!r}"
        )

    media_term_id = _media_term_id(doc)
    if media_term_id != target.expected_media_term:
        raise ValueError(
            f"{target.path}: expected media term {target.expected_media_term}, "
            f"found {media_term_id!r}"
        )

    ingredient_terms = _ingredient_terms(doc)
    if ingredient_terms not in target.accepted_ingredient_sets:
        raise ValueError(
            f"{target.path}: found ingredient terms "
            f"{sorted(ingredient_terms)!r}, expected one of "
            f"{[sorted(term_set) for term_set in target.accepted_ingredient_sets]!r}"
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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "needs_manual_curation",
        "placeholder_composition",
        "source_information_unavailable",
    ):
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

    if not any(
        isinstance(row, dict) and row.get("reference") == target.reference_url
        for row in references
    ):
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
        normalized / target.path: repair_record(
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
