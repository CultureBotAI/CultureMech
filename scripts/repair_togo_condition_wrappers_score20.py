#!/usr/bin/env python3
"""Repair score-20 TOGO wrappers with simple product and condition evidence."""

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

CURATOR = "repair_togo_condition_wrappers_score20.py"
ACTION = "RESOLVED_TOGO_CONDITION_WRAPPERS_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

M2194_NUTRIENT_DIFCO = "bacterial/nutrient_broth_nb_difco.yaml"
M2225_MRS_BIOKAR = "bacterial/de_man_rogosa_sharpe_mrs_broth_biokar_diagnostic.yaml"
M2490_MRS_ERYTHROMYCIN = "bacterial/mrs_medium_containing_erythromycin.yaml"
M2795_MRS_CYSTEINE = "bacterial/mrs_supplemented_with_0_05_cysteine.yaml"
M2891_PPLO_CO2 = "bacterial/complete_pleuropneumonia_like_organism_pplo_medium.yaml"
M2896_THB_CO2 = "bacterial/todd_hewitt_broth.yaml"

TOGO_M2194 = "https://togomedium.org/medium/M2194"
TOGO_M2225 = "https://togomedium.org/medium/M2225"
TOGO_M2490 = "https://togomedium.org/medium/M2490"
TOGO_M2795 = "https://togomedium.org/medium/M2795"
TOGO_M2891 = "https://togomedium.org/medium/M2891"
TOGO_M2896 = "https://togomedium.org/medium/M2896"

EXPECTED_IDS = {
    M2194_NUTRIENT_DIFCO: "CultureMech:008787",
    M2225_MRS_BIOKAR: "CultureMech:008813",
    M2490_MRS_ERYTHROMYCIN: "CultureMech:009064",
    M2795_MRS_CYSTEINE: "CultureMech:009343",
    M2891_PPLO_CO2: "CultureMech:009427",
    M2896_THB_CO2: "CultureMech:009432",
}

EXPECTED_SOURCE_TERMS = {
    M2194_NUTRIENT_DIFCO: "TOGO:M2194",
    M2225_MRS_BIOKAR: "TOGO:M2225",
    M2490_MRS_ERYTHROMYCIN: "TOGO:M2490",
    M2795_MRS_CYSTEINE: "TOGO:M2795",
    M2891_PPLO_CO2: "TOGO:M2891",
    M2896_THB_CO2: "TOGO:M2896",
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
    "preparation_steps",
    "sterilization",
)


@dataclass(frozen=True)
class RecipeUpdate:
    path: str
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
    cellular_metabolic_roles: tuple[str, ...] = (),
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
    if cellular_metabolic_roles:
        row["cellular_metabolic_roles"] = list(cellular_metabolic_roles)
    return row


def _water(source: str) -> dict[str, Any]:
    return _ingredient(
        "Distilled water",
        "1000",
        "ML_PER_L",
        source=source,
        notes=f"{source} lists one liter of distilled water.",
        term=("CHEBI:15377", "water"),
    )


def _product(preferred_term: str, value: str, unit: str, source: str) -> dict[str, Any]:
    return _ingredient(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} lists {value} {unit} of {preferred_term}.",
    )


def _co2(source: str) -> dict[str, Any]:
    return _ingredient(
        "CO2",
        "5",
        "PERCENT_V_V",
        source=source,
        notes=f"{source} lists 5% CO2 as the incubation atmosphere.",
        term=("CHEBI:16526", "carbon dioxide"),
    )


def _mix_step(step_number: int, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": "MIX",
        "description": description,
    }


UPDATES: tuple[RecipeUpdate, ...] = (
    RecipeUpdate(
        path=M2194_NUTRIENT_DIFCO,
        notes=(
            "TOGO M2194 lists 8 g Nutrient broth (NB) from Difco in one "
            "liter of distilled water at pH 6.8 +/- 0.2."
        ),
        reference_url=TOGO_M2194,
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_range": {"min": 6.6, "max": 7.0},
            "temperature_value": 30.0,
            "ingredients": (
                _water("TOGO M2194"),
                _product("Nutrient broth (NB) (Difco)", "8", "G_PER_L", "TOGO M2194"),
            ),
            "preparation_steps": (
                "Dissolve 8 g Nutrient broth (NB) (Difco) in one liter of distilled water.",
                "Cultivate at 30 C.",
            ),
        },
    ),
    RecipeUpdate(
        path=M2225_MRS_BIOKAR,
        notes=(
            "TOGO M2225 lists 55.3 g De Man-Rogosa-Sharpe broth from Biokar "
            "Diagnostic in one liter of distilled water at pH 6.4 +/- 0.2."
        ),
        reference_url=TOGO_M2225,
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_range": {"min": 6.2, "max": 6.6},
            "temperature_value": 37.0,
            "ingredients": (
                _water("TOGO M2225"),
                _product(
                    "De Man-Rogosa-Sharpe (MRS) broth (Biokar Diagnostic)",
                    "55.3",
                    "G_PER_L",
                    "TOGO M2225",
                ),
            ),
            "preparation_steps": (
                "Dissolve 55.3 g De Man-Rogosa-Sharpe broth in one liter of distilled water.",
                "Cultivate anaerobically for 24 h at 37 C.",
            ),
        },
    ),
    RecipeUpdate(
        path=M2490_MRS_ERYTHROMYCIN,
        notes=(
            "TOGO M2490 lists MRS medium from Difco with erythromycin at "
            "5 ug/ml and 24 h incubation at 37 C."
        ),
        reference_url=TOGO_M2490,
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "temperature_value": 37.0,
            "ingredients": (
                _ingredient(
                    "erythromycin",
                    "5",
                    "MG_PER_L",
                    source="TOGO M2490",
                    notes=(
                        "TOGO M2490 lists erythromycin at 5 ug/ml; this is "
                        "stored as the equivalent 5 mg/L."
                    ),
                    term=("CHEBI:48923", "erythromycin"),
                    cellular_metabolic_roles=("INHIBITOR",),
                ),
                _product("MRS medium (Difco)", "1000", "ML_PER_L", "TOGO M2490"),
            ),
            "preparation_steps": (
                "Supplement one liter of MRS medium (Difco) with erythromycin to 5 ug/ml.",
                "Incubate for 24 h at 37 C.",
            ),
        },
    ),
    RecipeUpdate(
        path=M2795_MRS_CYSTEINE,
        notes=(
            "TOGO M2795 lists MRS broth supplemented with 0.05% cysteine and "
            "anaerobic propagation at 37 C."
        ),
        reference_url=TOGO_M2795,
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "temperature_value": 37.0,
            "ingredients": (
                _ingredient(
                    "Cysteine",
                    "0.05",
                    "PERCENT_W_V",
                    source="TOGO M2795",
                    notes="TOGO M2795 lists cysteine at 0.05%.",
                    term=("CHEBI:15356", "cysteine"),
                ),
                _product("MRS broth", "1000", "ML_PER_L", "TOGO M2795"),
            ),
            "preparation_steps": (
                "Supplement one liter of MRS broth with 0.05% cysteine.",
                "Cultivate anaerobically at 37 C.",
            ),
        },
    ),
    RecipeUpdate(
        path=M2891_PPLO_CO2,
        notes=(
            "TOGO M2891 lists one liter of PPLO medium and approximately "
            "48 h cultivation at 37 C in 5% CO2."
        ),
        reference_url=TOGO_M2891,
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "temperature_value": 37.0,
            "ingredients": (
                _product("PPLO medium", "1000", "ML_PER_L", "TOGO M2891"),
                _co2("TOGO M2891"),
            ),
            "preparation_steps": (
                "Use one liter of PPLO medium.",
                "Cultivate for approximately 48 h at 37 C in 5% CO2.",
            ),
        },
    ),
    RecipeUpdate(
        path=M2896_THB_CO2,
        notes=(
            "TOGO M2896 lists one liter of Todd-Hewitt broth from Oxoid and "
            "37 C cultivation with 5% CO2."
        ),
        reference_url=TOGO_M2896,
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "temperature_value": 37.0,
            "ingredients": (
                _product("Todd–Hewitt broth (Oxoid)", "1000", "ML_PER_L", "TOGO M2896"),
                _co2("TOGO M2896"),
            ),
            "preparation_steps": (
                "Use one liter of Todd-Hewitt broth (Oxoid).",
                "Cultivate at 37 C in 5% CO2.",
            ),
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


def _require_source_components(doc: dict[str, Any], update: RecipeUpdate) -> None:
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
        row["preferred_term"].lower() for row in update.recipe["ingredients"]
    }
    if _ingredient_terms(doc) != expected_terms:
        raise ValueError(
            f"{update.path}: found ingredient terms {sorted(_ingredient_terms(doc))!r}, "
            f"expected {sorted(expected_terms)!r}"
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

    rows = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    has_grounded = any(_grounded(row) for row in rows)
    has_unmapped = any(not _grounded(row) for row in rows)

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
    if update.reference_url not in {
        row.get("reference") for row in references if isinstance(row, dict)
    }:
        references.append({"reference": update.reference_url})


def _history(doc: dict[str, Any], path: str) -> list[Any]:
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{path}: curation_history is not a list")
    return history


def _append_curation_event(doc: dict[str, Any], update: RecipeUpdate) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved score-20 TOGO product and condition wrapper",
        "source": update.reference_url,
        "notes": update.notes,
    }
    history = _history(doc, update.path)
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_wrapper(doc: dict[str, Any], update: RecipeUpdate) -> dict[str, Any]:
    _require_source_components(doc, update)

    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        repaired.pop(field, None)

    for field, value in update.recipe.items():
        if field == "ingredients":
            repaired[field] = [copy.deepcopy(row) for row in value]
        elif field == "preparation_steps":
            repaired[field] = [
                _mix_step(index, description)
                for index, description in enumerate(value, start=1)
            ]
        else:
            repaired[field] = copy.deepcopy(value)
    _put_after(repaired, "notes", update.notes, "media_term")

    _ensure_flags(repaired)
    _ensure_references(repaired, update)
    _append_curation_event(repaired, update)
    if "data_quality_flags" in repaired:
        _put_after(
            repaired,
            "data_quality_flags",
            repaired["data_quality_flags"],
            "preparation_steps",
        )
    if "references" in repaired:
        _put_after(repaired, "references", repaired["references"], "data_quality_flags")
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for update in UPDATES:
        plans[normalized / update.path] = repair_wrapper(
            _load(normalized / update.path),
            update,
        )
    return plans


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
