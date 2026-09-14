#!/usr/bin/env python3
"""Repair sparse TOGO score-20 product records."""

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

CURATOR = "repair_togo_sparse_score20.py"
ACTION = "RESOLVED_TOGO_SPARSE_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

M250_ME_AGAR = "bacterial/TOGO_M250_ME_Agar.yaml"
M530_THIOGLYCOLLATE = "bacterial/TOGO_M530_Thioglycollate_Medium.yaml"
M2510_SHEEP_BLOOD = "bacterial/sheep_blood_agar.yaml"
M2684_GAM_BROTH = "bacterial/gifu_anaerobic_medium_gam_broth.yaml"
M2858_CHOCOLATE = "bacterial/TOGO_M2858_chocolate_agar.yaml"
M2859_BCYE = "bacterial/TOGO_M2859_BCYE_agar.yaml"

TOGO_M250 = "https://togomedium.org/medium/M250"
TOGO_M530 = "https://togomedium.org/medium/M530"
TOGO_M2510 = "https://togomedium.org/medium/M2510"
TOGO_M2684 = "https://togomedium.org/medium/M2684"
TOGO_M2858 = "https://togomedium.org/medium/M2858"
TOGO_M2859 = "https://togomedium.org/medium/M2859"
JCM_258 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=258"
JCM_529 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=529"

EXPECTED_IDS = {
    M250_ME_AGAR: "CultureMech:009081",
    M530_THIOGLYCOLLATE: "CultureMech:009923",
    M2510_SHEEP_BLOOD: "CultureMech:009082",
    M2684_GAM_BROTH: "CultureMech:009239",
    M2858_CHOCOLATE: "CultureMech:009398",
    M2859_BCYE: "CultureMech:009399",
}

EXPECTED_SOURCE_TERMS = {
    M250_ME_AGAR: "TOGO:M250",
    M530_THIOGLYCOLLATE: "TOGO:M530",
    M2510_SHEEP_BLOOD: "TOGO:M2510",
    M2684_GAM_BROTH: "TOGO:M2684",
    M2858_CHOCOLATE: "TOGO:M2858",
    M2859_BCYE: "TOGO:M2859",
}

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
class RecipeUpdate:
    path: str
    notes: str
    reference_urls: tuple[str, ...]
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
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _water(source: str) -> dict[str, Any]:
    return _ingredient(
        "Distilled water",
        "1000",
        "ML_PER_L",
        source=source,
        notes=f"{source} lists 1.0 L distilled water.",
        term=("CHEBI:15377", "water"),
    )


def _commercial_product(
    preferred_term: str,
    value: str,
    unit: str,
    source: str,
    notes: str,
) -> dict[str, Any]:
    return _ingredient(
        preferred_term,
        value,
        unit,
        source=source,
        notes=notes,
    )


def _co2(source: str) -> dict[str, Any]:
    return _ingredient(
        "CO2",
        "5",
        "PERCENT_V_V",
        source=source,
        notes=f"{source} records propagation in 5% CO2.",
        term=("CHEBI:16526", "carbon dioxide"),
    )


UPDATES: tuple[RecipeUpdate, ...] = (
    RecipeUpdate(
        path=M250_ME_AGAR,
        notes=(
            "TOGO M250 records 50 g/L Malt extract agar from Oxoid in "
            "distilled water and autoclaving at 115 C for 10 min."
        ),
        reference_urls=(TOGO_M250, JCM_258),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _water("TOGO M250"),
                _commercial_product(
                    "Malt extract agar (Oxoid)",
                    "50",
                    "G_PER_L",
                    "TOGO M250",
                    "TOGO M250 lists 50 g/L Malt extract agar from Oxoid.",
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
    RecipeUpdate(
        path=M530_THIOGLYCOLLATE,
        notes=(
            "TOGO M530 records 29.8 g/L Thioglycollate medium from Sigma in "
            "distilled water and describes the medium as semisolid."
        ),
        reference_urls=(TOGO_M530, JCM_529),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SEMISOLID",
            "ingredients": [
                _water("TOGO M530"),
                _commercial_product(
                    "Thioglycollate medium (Sigma)",
                    "29.8",
                    "G_PER_L",
                    "TOGO M530",
                    "TOGO M530 lists 29.8 g/L Thioglycollate medium from Sigma.",
                ),
            ],
        },
    ),
    RecipeUpdate(
        path=M2858_CHOCOLATE,
        notes=(
            "TOGO M2858 records F. tularensis strain FTNF002-00 propagated "
            "on chocolate agar at 37 C in 5% CO2; the source does not "
            "disclose the chocolate agar amount or formulation."
        ),
        reference_urls=(TOGO_M2858,),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "temperature_value": 37.0,
            "ingredients": [
                _commercial_product(
                    "Chocolate agar",
                    "variable",
                    "VARIABLE",
                    "TOGO M2858",
                    (
                        "TOGO M2858 names chocolate agar but does not state "
                        "an amount."
                    ),
                ),
                _co2("TOGO M2858"),
            ],
        },
    ),
    RecipeUpdate(
        path=M2684_GAM_BROTH,
        notes=(
            "TOGO M2684 records 59 g/L GAM broth from Nissui in distilled "
            "water with anaerobic growth at 37 C."
        ),
        reference_urls=(TOGO_M2684,),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "temperature_value": 37.0,
            "ingredients": [
                _water("TOGO M2684"),
                _commercial_product(
                    "GAM broth (Nissui)",
                    "59",
                    "G_PER_L",
                    "TOGO M2684",
                    "TOGO M2684 lists 59 g/L GAM broth from Nissui.",
                ),
            ],
        },
    ),
    RecipeUpdate(
        path=M2859_BCYE,
        notes=(
            "TOGO M2859 records L. pneumophila strains Paris and Lens grown "
            "on one liter of BCYE agar at 37 C for 3 d; the source does not "
            "disclose the BCYE agar formulation."
        ),
        reference_urls=(TOGO_M2859,),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "temperature_value": 37.0,
            "ingredients": [
                _commercial_product(
                    "BCYE agar",
                    "1000",
                    "ML_PER_L",
                    "TOGO M2859",
                    (
                        "TOGO M2859 lists one liter of BCYE agar without "
                        "spelling out the commercial product or formulation."
                    ),
                ),
            ],
        },
    ),
    RecipeUpdate(
        path=M2510_SHEEP_BLOOD,
        notes=(
            "TOGO M2510 records overnight growth on sheep blood agar at 37 C "
            "in 5% CO2; the source does not disclose the sheep blood agar "
            "formulation."
        ),
        reference_urls=(TOGO_M2510,),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "temperature_value": 37.0,
            "ingredients": [
                _commercial_product(
                    "sheep blood agar",
                    "variable",
                    "VARIABLE",
                    "TOGO M2510",
                    (
                        "TOGO M2510 names sheep blood agar but does not state "
                        "an amount."
                    ),
                ),
                _co2("TOGO M2510"),
            ],
        },
    ),
)

UPDATE_BY_PATH = {update.path: update for update in UPDATES}


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


def _ingredient_terms(doc: dict[str, Any]) -> set[str]:
    return {
        str(row.get("preferred_term") or "").lower()
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    }


def _require_target(doc: dict[str, Any], update: RecipeUpdate) -> None:
    if doc.get("id") != EXPECTED_IDS[update.path]:
        raise ValueError(
            f"{update.path}: found id {doc.get('id')!r}, "
            f"expected {EXPECTED_IDS[update.path]!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[update.path]:
        raise ValueError(
            f"{update.path}: found source term {source_term!r}, "
            f"expected {EXPECTED_SOURCE_TERMS[update.path]!r}"
        )

    expected_terms = {
        str(row["preferred_term"]).lower()
        for row in update.recipe["ingredients"]
        if isinstance(row, dict)
    }
    if _ingredient_terms(doc) != expected_terms:
        raise ValueError(
            f"{update.path}: found ingredient terms "
            f"{sorted(_ingredient_terms(doc))!r}, expected "
            f"{sorted(expected_terms)!r}"
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


def _ensure_references(doc: dict[str, Any], update: RecipeUpdate) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{update.path}: references is not a list")
    found = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference_url in update.reference_urls:
        if reference_url not in found:
            references.append({"reference": reference_url})
            found.add(reference_url)


def _append_curation_event(doc: dict[str, Any], update: RecipeUpdate) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved sparse score-20 TOGO product record",
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


def repair_record(doc: dict[str, Any], update: RecipeUpdate) -> dict[str, Any]:
    _require_target(doc, update)

    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        if field in update.recipe:
            repaired[field] = copy.deepcopy(update.recipe[field])
        else:
            repaired.pop(field, None)

    _put_after(repaired, "notes", update.notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, update)
    _append_curation_event(repaired, update)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / update.path: repair_record(
            _load(normalized / update.path),
            update,
        )
        for update in UPDATES
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
