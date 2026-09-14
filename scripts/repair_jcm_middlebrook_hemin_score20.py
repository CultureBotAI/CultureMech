#!/usr/bin/env python3
"""Repair JCM 386 Middlebrook 7H10 agar and JCM 714 hemin variant."""

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

CURATOR = "repair_jcm_middlebrook_hemin_score20.py"
ACTION = "RESOLVED_JCM_MIDDLEBROOK_HEMIN_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

JCM386 = "bacterial/middlebrook_7h10_agar_with_oadc_enrichment.yaml"
JCM714 = "bacterial/JCM_J714_HEMIN_MEDIUM_FOR_MYCOBACTERIUM.yaml"

JCM386_URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=386"
JCM714_URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=714"

MIDDLEBROOK = "Middlebrook 7H10 agar (BD-Difco)"
IMPORTED_MIDDLEBROOK = "Middlebrook 7H10 agar"
GLYCEROL = "Glycerol"
WATER = "Distilled water"
OADC = "Middlebrook OADC Enrichment (BD-BBL)"
HEMIN = "Hemin"

EXPECTED_IDS = {
    JCM386: "CultureMech:002743",
    JCM714: "CultureMech:003061",
}

EXPECTED_SOURCE_TERMS = {
    JCM386: "mediadive.medium:J386",
    JCM714: "mediadive.medium:J714",
}


@dataclass(frozen=True)
class Target:
    path: str
    reference_urls: tuple[str, ...]
    notes: str


TARGETS: tuple[Target, ...] = (
    Target(
        path=JCM386,
        reference_urls=(JCM386_URL,),
        notes=(
            "Source: JCM Medium 386 | Link: "
            "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=386\n\n"
            "The JCM Middlebrook 7H10 Agar with OADC Enrichment table lists "
            "Middlebrook 7H10 agar, glycerol, distilled water, and a 100 ml/L "
            "aseptic addition of Middlebrook OADC Enrichment."
        ),
    ),
    Target(
        path=JCM714,
        reference_urls=(JCM714_URL, JCM386_URL),
        notes=(
            "Source: JCM Medium 714 | Link: "
            "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=714\n\n"
            "JCM Medium 714 supplements JCM Medium 386 with 60 micromol/L "
            "hemin solubilized in 1 N NaOH."
        ),
    ),
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    term: tuple[str, str] | None = None,
    notes: str | None = None,
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
    return row


BASE_INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        MIDDLEBROOK,
        "19",
        "G_PER_L",
        notes="JCM Medium 386 lists this commercial BD-Difco medium base as supplied.",
    ),
    _ingredient(
        GLYCEROL,
        "5",
        "ML_PER_L",
        term=("CHEBI:17754", "glycerol"),
        notes="JCM Medium 386 lists glycerol as 5 ml/L.",
    ),
    _ingredient(
        WATER,
        "895",
        "ML_PER_L",
        term=("CHEBI:15377", "water"),
        notes="JCM Medium 386 uses 895 ml/L distilled water before OADC addition.",
    ),
    _ingredient(
        OADC,
        "100",
        "ML_PER_L",
        notes="JCM Medium 386 aseptically adds this commercial BD-BBL enrichment.",
    ),
)

HEMIN_INGREDIENT = _ingredient(
    HEMIN,
    "60",
    "MICROMOLAR",
    term=("CHEBI:50385", "hemin"),
    notes="JCM Medium 714 adds 60 micromol/L hemin solubilized with 1 N NaOH.",
)

BASE_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Sterilize the Middlebrook 7H10 agar, glycerol, and distilled water "
            "at 121 C for 10 min."
        ),
    },
    {
        "step_number": 2,
        "action": "COOL",
        "description": "Cool to 50-55 C.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "Aseptically add 100 ml/L Middlebrook OADC Enrichment (BD-BBL) and " "mix thoroughly."
        ),
    },
)

HEMIN_PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    BASE_PREPARATION_STEPS[0],
    BASE_PREPARATION_STEPS[1],
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "Aseptically add 100 ml/L Middlebrook OADC Enrichment (BD-BBL), add "
            "hemin to 60 micromol/L after solubilizing it with 1 N NaOH, and mix "
            "thoroughly."
        ),
    },
)

ACCEPTED_CONCENTRATIONS = {
    MIDDLEBROOK: (
        {"value": "19", "unit": "G_PER_L"},
        {"value": "21.1111", "unit": "G_PER_L"},
    ),
    IMPORTED_MIDDLEBROOK: (
        {"value": "19", "unit": "G_PER_L"},
        {"value": "21.1111", "unit": "G_PER_L"},
    ),
    GLYCEROL: (
        {"value": "5", "unit": "ML_PER_L"},
        {"value": "5", "unit": "G_PER_L"},
    ),
    WATER: ({"value": "895", "unit": "ML_PER_L"},),
    OADC: ({"value": "100", "unit": "ML_PER_L"},),
    HEMIN: ({"value": "60", "unit": "MICROMOLAR"},),
}

OFFICIAL_NAMES = frozenset(ACCEPTED_CONCENTRATIONS)
MIDDLEBROOK_NAMES = frozenset((MIDDLEBROOK, IMPORTED_MIDDLEBROOK))

JCM714_CHILD = {
    "path": f"data/normalized_yaml/{JCM714}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_IDS[JCM714],
    "name": "hemin_medium_for_mycobacterium",
    "notes": "Adds 60 micromol/L hemin solubilized with 1 N NaOH.",
}

JCM386_PARENT = {
    "path": f"data/normalized_yaml/{JCM386}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_IDS[JCM386],
    "name": "middlebrook_7h10_agar_with_oadc_enrichment",
    "notes": "Parent JCM Medium 386 for the hemin-supplemented JCM Medium 714 recipe.",
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
        raise ValueError(f"{path}: found id {doc.get('id')!r}, expected {EXPECTED_IDS[path]!r}")

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[path]:
        raise ValueError(
            f"{path}: found source term {source_term!r}, "
            f"expected {EXPECTED_SOURCE_TERMS[path]!r}"
        )

    ingredients = _ingredients_by_name(doc)
    if not MIDDLEBROOK_NAMES.intersection(ingredients) or GLYCEROL not in ingredients:
        raise ValueError(f"{path}: missing Middlebrook 7H10 core ingredient")
    if set(ingredients) - OFFICIAL_NAMES:
        raise ValueError(f"{path}: ingredient list drifted")

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
        "changes": "Resolved JCM Medium 386/714 Middlebrook-hemin composition",
        "source": "; ".join(target.reference_urls),
        "notes": "Rebuilt the recipe from live JCM Medium 386 and 714 pages.",
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
    ingredients = list(BASE_INGREDIENTS)
    steps = list(BASE_PREPARATION_STEPS)

    if target.path == JCM714:
        ingredients.append(HEMIN_INGREDIENT)
        steps = list(HEMIN_PREPARATION_STEPS)
        repaired["physical_state"] = "SOLID_AGAR"
        _put_after(repaired, "parent_media", copy.deepcopy(JCM386_PARENT), "preparation_steps")
        _put_after(repaired, "variant_relationship", "SUPPLEMENTED_VARIANT", "parent_media")
    else:
        children = repaired.setdefault("variant_children", [])
        if not isinstance(children, list):
            raise ValueError(f"{target.path}: variant_children is not a list")
        _upsert_ref(children, copy.deepcopy(JCM714_CHILD))
        children.sort(key=lambda row: row.get("path", "") if isinstance(row, dict) else "")

    repaired["ingredients"] = copy.deepcopy(ingredients)
    _put_after(repaired, "preparation_steps", copy.deepcopy(steps), "ingredients")
    repaired["notes"] = target.notes

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
