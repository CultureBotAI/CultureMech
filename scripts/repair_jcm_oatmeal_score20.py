#!/usr/bin/env python3
"""Repair JCM 148 Oatmeal Agar and its TOGO source duplicate."""

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

CURATOR = "repair_jcm_oatmeal_score20.py"
ACTION = "RESOLVED_JCM_J148_OATMEAL_AGAR"
TIMESTAMP = "2026-09-08T00:00:00-07:00"

JCM = "bacterial/JCM_J148_OATMEAL_AGAR.yaml"
TOGO = "bacterial/TOGO_M139_Oatmeal_Agar.yaml"

JCM_URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=148"
TOGO_URL = "https://togomedium.org/medium/M139"

OATMEAL = "Oatmeal (Quaker White Oats)"
IMPORTED_OATMEAL = "Oatmeal"
AGAR = "Agar"
WATER = "Distilled water"

EXPECTED_IDS = {
    JCM: "CultureMech:002506",
    TOGO: "CultureMech:007935",
}

EXPECTED_SOURCE_TERMS = {
    JCM: "mediadive.medium:J148",
    TOGO: "TOGO:M139",
}


@dataclass(frozen=True)
class Target:
    path: str
    reference_urls: tuple[str, ...]
    notes: str


TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM,
        reference_urls=(JCM_URL,),
        notes=(
            "Source: JCM Medium 148 | Link: "
            "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=148\n\n"
            "The JCM Oatmeal Agar table lists oatmeal, agar, and distilled water; "
            "the oatmeal is boiled in distilled water, filtered through cloth, "
            "restored to 1 L, and boiled again after agar addition."
        ),
    ),
    Target(
        path=TOGO,
        reference_urls=(TOGO_URL, JCM_URL),
        notes=(
            "Source: TOGO Medium M139 | Link: https://togomedium.org/medium/M139\n\n"
            "TOGO Medium M139 mirrors JCM Medium 148 Oatmeal Agar: oatmeal, "
            "agar, and distilled water."
        ),
    ),
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str = "G_PER_L",
    *,
    term: tuple[str, str] | None = None,
    notes: str | None = None,
    physicochemical_roles: tuple[str, ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
    }
    if term:
        row["term"] = _term(*term)
        row["mediaingredientmech_chebi_term"] = _term(*term)
    if notes:
        row["notes"] = notes
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        OATMEAL,
        "30",
        notes="JCM Medium 148 lists this brand-specific oatmeal as supplied.",
    ),
    _ingredient(
        AGAR,
        "20",
        term=("CHEBI:2509", "agar"),
        notes="JCM Medium 148 uses agar to solidify the oatmeal infusion.",
        physicochemical_roles=("SOLIDIFYING_AGENT",),
    ),
    _ingredient(
        WATER,
        "1000",
        "ML_PER_L",
        term=("CHEBI:15377", "water"),
        notes="JCM Medium 148 brings the oatmeal filtrate back to 1 L.",
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "HEAT",
        "description": (
            "Boil 30 g oatmeal with 1 L distilled water over a water bath for "
            "1 hr, stirring occasionally; filter through cloth, bring the "
            "filtrate back to 1 L, add agar, and boil until dissolved."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C for 15 min.",
    },
)

ACCEPTED_CONCENTRATIONS = {
    OATMEAL: ({"value": "30", "unit": "G_PER_L"},),
    IMPORTED_OATMEAL: ({"value": "30", "unit": "G_PER_L"},),
    AGAR: ({"value": "20", "unit": "G_PER_L"},),
    WATER: (
        {"value": "1", "unit": "G_PER_L"},
        {"value": "1000", "unit": "ML_PER_L"},
    ),
}

OFFICIAL_NAMES = frozenset(ACCEPTED_CONCENTRATIONS)
OATMEAL_NAMES = frozenset((OATMEAL, IMPORTED_OATMEAL))

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TOGO}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_IDS[TOGO],
    "name": "oatmeal_agar",
    "notes": "TOGO Medium M139 points to the same JCM Medium 148 recipe.",
}

JCM_PARENT = {
    "path": f"data/normalized_yaml/{JCM}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_IDS[JCM],
    "name": "oatmeal_agar",
    "notes": "MediaDive JCM import for the same JCM Medium 148 recipe.",
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ingredients_by_name(doc: dict[str, Any]) -> dict[str, dict[str, Any]]:
    ingredients = doc.get("ingredients") or []
    if not isinstance(ingredients, list):
        raise ValueError("ingredients is not a list")

    by_name: dict[str, dict[str, Any]] = {}
    for ingredient in ingredients:
        if not isinstance(ingredient, dict):
            raise ValueError("ingredients contains a non-mapping row")
        name = str(ingredient.get("preferred_term") or "")
        if name in by_name:
            raise ValueError(f"duplicate ingredient {name!r}")
        by_name[name] = ingredient
    return by_name


def _require_target(doc: dict[str, Any], path: str) -> None:
    if doc.get("id") != EXPECTED_IDS[path]:
        raise ValueError(
            f"{path}: found id {doc.get('id')!r}, expected {EXPECTED_IDS[path]!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[path]:
        raise ValueError(
            f"{path}: found source term {source_term!r}, "
            f"expected {EXPECTED_SOURCE_TERMS[path]!r}"
        )

    ingredients = _ingredients_by_name(doc)
    if AGAR not in ingredients or not OATMEAL_NAMES.intersection(ingredients):
        raise ValueError(f"{path}: missing Oatmeal Agar core ingredient")
    if set(ingredients) - OFFICIAL_NAMES:
        raise ValueError(f"{path}: ingredient list drifted")
    if path == TOGO and WATER not in ingredients:
        raise ValueError(f"{path}: missing imported distilled water")

    for name, ingredient in ingredients.items():
        if ingredient.get("concentration") not in ACCEPTED_CONCENTRATIONS[name]:
            raise ValueError(f"{path}: concentration drifted for {name}")


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

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)

    ingredients = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    if any(not _grounded(ingredient) for ingredient in ingredients):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in target.reference_urls:
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved JCM Medium 148 Oatmeal Agar composition",
        "source": "; ".join(target.reference_urls),
        "notes": "Rebuilt the Oatmeal Agar ingredients from the JCM Medium 148 table.",
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


def _upsert_ref(refs: list[Any], new_ref: dict[str, Any]) -> None:
    for index, existing in enumerate(refs):
        if isinstance(existing, dict) and existing.get("path") == new_ref["path"]:
            refs[index] = new_ref
            return
    refs.append(new_ref)


def repair_document(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_target(doc, target.path)

    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "ingredients")
    repaired["notes"] = target.notes

    if target.path == JCM:
        children = repaired.setdefault("variant_children", [])
        if not isinstance(children, list):
            raise ValueError(f"{target.path}: variant_children is not a list")
        _upsert_ref(children, copy.deepcopy(TOGO_CHILD))
        children.sort(key=lambda row: row.get("path", "") if isinstance(row, dict) else "")
    else:
        _put_after(repaired, "parent_media", copy.deepcopy(JCM_PARENT), "preparation_steps")
        _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")

    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_document(_load(normalized / target.path), target)
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
