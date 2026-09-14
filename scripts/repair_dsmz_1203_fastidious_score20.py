#!/usr/bin/env python3
"""Repair DSMZ 1203 Fastidious Anaerobe Agar and KOMODO source duplicates."""

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

CURATOR = "repair_dsmz_1203_fastidious_score20.py"
ACTION = "RESOLVED_DSMZ_1203_FASTIDIOUS_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

DSMZ = "bacterial/fastidious_anaerobe_agar.yaml"
KOMODO_1203 = "bacterial/KOMODO_1203_FASTIDIOUS_ANAEROBE_AGAR.yaml"
KOMODO_3136 = "bacterial/KOMODO_3136_Fastidious_Anaerobe_Agar.yaml"

DSMZ_URL = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1203.pdf"

FASTIDIOUS = "Fastidious Anaerobe Agar (Acumedia)"
IMPORTED_FASTIDIOUS = "Fastidious Anaerobe Agar"
WATER = "Deionized water"
HORSE_BLOOD = "Sterile defibrinated horse blood"
IMPORTED_HORSE_BLOOD = "Horse blood"

EXPECTED_IDS = {
    DSMZ: "CultureMech:000653",
    KOMODO_1203: "CultureMech:003951",
    KOMODO_3136: "CultureMech:004984",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ: "mediadive.medium:1203",
    KOMODO_1203: "komodo.medium:1203",
    KOMODO_3136: "komodo.medium:3136",
}


@dataclass(frozen=True)
class Target:
    path: str
    notes: str


TARGETS: tuple[Target, ...] = (
    Target(
        path=DSMZ,
        notes=(
            "DSMZ Medium 1203 lists 45.7 g Acumedia Fastidious Anaerobe Agar "
            "brought to one liter with deionized water, soaked, autoclaved at "
            "121 C, cooled to 47 C, and supplemented with 5-10% sterile "
            "defibrinated horse blood."
        ),
    ),
    Target(
        path=KOMODO_1203,
        notes=(
            "KOMODO Medium 1203 duplicates DSMZ Medium 1203: 45.7 g Acumedia "
            "Fastidious Anaerobe Agar per liter with 5-10% sterile defibrinated "
            "horse blood."
        ),
    ),
    Target(
        path=KOMODO_3136,
        notes=(
            "KOMODO Medium 3136 resolves to MediaDive/DSMZ Medium 1203: "
            "45.7 g Acumedia Fastidious Anaerobe Agar per liter with 5-10% "
            "sterile defibrinated horse blood."
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
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    if notes:
        row["notes"] = notes
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        FASTIDIOUS,
        "45.7",
        "G_PER_L",
        notes="DSMZ Medium 1203 lists this commercial Acumedia agar base as supplied.",
    ),
    _ingredient(
        WATER,
        "1000",
        "ML_PER_L",
        term=("CHEBI:15377", "water"),
        notes="DSMZ Medium 1203 brings the agar base to 1000 ml.",
    ),
    _ingredient(
        HORSE_BLOOD,
        "5-10",
        "PERCENT_V_V",
        term=("UBERON:0000178", "blood"),
        notes=(
            "DSMZ Medium 1203 instructs adding 5-10% sterile defibrinated horse "
            "blood after autoclaving and cooling to 47 C."
        ),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Allow the agar powder to soak for 10 min, then swirl to mix.",
        "duration": "10 minutes",
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the mixed medium at 121 C for 15 min.",
    },
    {
        "step_number": 3,
        "action": "COOL",
        "description": "Cool the sterilized medium to 47 C.",
        "temperature": {"value": 47.0, "unit": "CELSIUS"},
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Aseptically add 5-10% sterile defibrinated horse blood, mix well, "
            "and pour plates."
        ),
    },
)

STERILIZATION = {"method": "AUTOCLAVE"}
PH_RANGE = {"min": 7.0, "max": 7.4}

ACCEPTED_CONCENTRATIONS = {
    FASTIDIOUS: ({"value": "45.7", "unit": "G_PER_L"},),
    IMPORTED_FASTIDIOUS: ({"value": "45.7", "unit": "G_PER_L"},),
    WATER: (
        None,
        {"value": "1000", "unit": "ML_PER_L"},
        {"value": "1.0", "unit": "L"},
    ),
    HORSE_BLOOD: ({"value": "5-10", "unit": "PERCENT_V_V"},),
    IMPORTED_HORSE_BLOOD: (
        {"value": "100", "unit": "G_PER_L"},
        {"value": "5-10", "unit": "PERCENT_V_V"},
    ),
}

OFFICIAL_NAMES = frozenset(ACCEPTED_CONCENTRATIONS)
FASTIDIOUS_NAMES = frozenset((FASTIDIOUS, IMPORTED_FASTIDIOUS))
BLOOD_NAMES = frozenset((HORSE_BLOOD, IMPORTED_HORSE_BLOOD))

SOURCE_DUPLICATES = {
    KOMODO_1203: {
        "path": f"data/normalized_yaml/{KOMODO_1203}",
        "relationship": "SOURCE_DUPLICATE",
        "id": EXPECTED_IDS[KOMODO_1203],
        "name": "fastidious_anaerobe_agar",
        "notes": "KOMODO Medium 1203 is a duplicate of DSMZ Medium 1203.",
    },
    KOMODO_3136: {
        "path": f"data/normalized_yaml/{KOMODO_3136}",
        "relationship": "SOURCE_DUPLICATE",
        "id": EXPECTED_IDS[KOMODO_3136],
        "name": "fastidious_anaerobe_agar",
        "notes": "KOMODO Medium 3136 resolves to MediaDive/DSMZ Medium 1203.",
    },
}

DSMZ_PARENT = {
    "path": f"data/normalized_yaml/{DSMZ}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_IDS[DSMZ],
    "name": "fastidious_anaerobe_agar",
    "notes": "Parent DSMZ Medium 1203 formula for this KOMODO source duplicate.",
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
    if not FASTIDIOUS_NAMES.intersection(ingredients) or not BLOOD_NAMES.intersection(
        ingredients
    ):
        raise ValueError(f"{path}: missing Fastidious Anaerobe Agar core ingredient")
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


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    if DSMZ_URL not in {ref.get("reference") for ref in references if isinstance(ref, dict)}:
        references.append({"reference": DSMZ_URL})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved DSMZ Medium 1203 Fastidious Anaerobe Agar formula",
        "source": DSMZ_URL,
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


def _upsert_ref(refs: list[Any], new_ref: dict[str, Any]) -> None:
    for index, existing in enumerate(refs):
        if isinstance(existing, dict) and existing.get("path") == new_ref["path"]:
            refs[index] = new_ref
            return
    refs.append(new_ref)


def repair_document(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_target(doc, target.path)

    repaired = copy.deepcopy(doc)
    repaired["physical_state"] = "SOLID_AGAR"
    repaired["ph_range"] = copy.deepcopy(PH_RANGE)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "ingredients")
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    repaired["notes"] = target.notes

    if target.path == DSMZ:
        children = repaired.setdefault("variant_children", [])
        if not isinstance(children, list):
            raise ValueError(f"{target.path}: variant_children is not a list")
        for duplicate in SOURCE_DUPLICATES.values():
            _upsert_ref(children, copy.deepcopy(duplicate))
        children.sort(key=lambda row: row.get("path", "") if isinstance(row, dict) else "")
    else:
        _put_after(repaired, "parent_media", copy.deepcopy(DSMZ_PARENT), "sterilization")
        _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
        repaired["variant_modifications"] = [
            "Source duplicate of DSMZ Medium 1203 Fastidious Anaerobe Agar."
        ]

    _ensure_flags(repaired)
    _ensure_references(repaired)
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
