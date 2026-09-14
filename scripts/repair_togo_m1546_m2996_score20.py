#!/usr/bin/env python3
"""Repair score-20 TOGO Marine Broth and PPLO sparse imports."""

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

CURATOR = "repair_togo_m1546_m2996_score20.py"
ACTION = "RESOLVED_TOGO_M1546_M2996_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

TOGO_M1546 = "https://togomedium.org/medium/M1546"
TOGO_M2996 = "https://togomedium.org/medium/M2996"
NBRC_339 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=339"

MARINE_BROTH = "bacterial/marine_broth_2216.yaml"
PPLO = "bacterial/pplo_pleuropneumonia_like_organism_medium.yaml"

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
)


@dataclass(frozen=True)
class RecipeUpdate:
    path: str
    expected_id: str
    expected_source_term: str
    expected_ingredients: frozenset[str]
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


UPDATES: tuple[RecipeUpdate, ...] = (
    RecipeUpdate(
        path=MARINE_BROTH,
        expected_id="CultureMech:008094",
        expected_source_term="TOGO:M1546",
        expected_ingredients=frozenset(
            {
                "Distilled water",
                "Bacto Marine Broth 2216 (Difco)",
            }
        ),
        notes=(
            "TOGO M1546/NBRC Medium 339 record 37.4 g/L Bacto Marine "
            "Broth 2216 from Difco in 1.0 L distilled water with pH unadjusted."
        ),
        reference_urls=(TOGO_M1546, NBRC_339),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _water("TOGO M1546/NBRC Medium 339"),
                _ingredient(
                    "Bacto Marine Broth 2216 (Difco)",
                    "37.4",
                    "G_PER_L",
                    source="TOGO M1546/NBRC Medium 339",
                    notes=(
                        "TOGO M1546 and NBRC Medium 339 list 37.4 g/L "
                        "Bacto Marine Broth 2216 from Difco."
                    ),
                ),
            ],
        },
    ),
    RecipeUpdate(
        path=PPLO,
        expected_id="CultureMech:009512",
        expected_source_term="TOGO:M2996",
        expected_ingredients=frozenset(
            {
                "PPLO (pleuropneumonia-like organism) medium",
                "CO2",
            }
        ),
        notes=(
            "TOGO M2996 records one liter of PPLO medium with 10 mg/L NAD "
            "and growth at 37 C in a 5% CO2 atmosphere."
        ),
        reference_urls=(TOGO_M2996,),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "temperature_value": 37.0,
            "ingredients": [
                _ingredient(
                    "PPLO (pleuropneumonia-like organism) medium",
                    "1000",
                    "ML_PER_L",
                    source="TOGO M2996",
                    notes="TOGO M2996 lists 1.0 L PPLO medium from Difco.",
                ),
                _ingredient(
                    "NAD",
                    "10",
                    "MG_PER_L",
                    source="TOGO M2996",
                    notes=(
                        "TOGO M2996 states PPLO medium was supplemented " "with NAD at 10 ug/mL."
                    ),
                    term=("CHEBI:15846", "NAD(+)"),
                ),
                _ingredient(
                    "CO2",
                    "5",
                    "PERCENT_V_V",
                    source="TOGO M2996",
                    notes="TOGO M2996 records growth in a 5% CO2 atmosphere.",
                    term=("CHEBI:16526", "carbon dioxide"),
                ),
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


def _require_target(doc: dict[str, Any], update: RecipeUpdate) -> None:
    if doc.get("id") != update.expected_id:
        raise ValueError(
            f"{update.path}: expected id {update.expected_id}, found {doc.get('id')!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != update.expected_source_term:
        raise ValueError(
            f"{update.path}: expected source term {update.expected_source_term}, "
            f"found {source_term!r}"
        )

    ingredient_names = {
        str(row.get("preferred_term") or "")
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    }
    repaired_ingredients = {
        str(row.get("preferred_term") or "")
        for row in update.recipe.get("ingredients") or []
        if isinstance(row, dict)
    }
    if ingredient_names not in (update.expected_ingredients, repaired_ingredients):
        raise ValueError(f"{update.path}: ingredient list drifted")


def _ensure_references(doc: dict[str, Any], urls: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in urls:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], update: RecipeUpdate) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(update.reference_urls),
        "notes": update.notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
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
    existing_references = repaired.pop("references", [])
    repaired.pop("data_quality_flags", None)
    for field in RECIPE_FIELDS:
        repaired.pop(field, None)
    _put_after(repaired, "notes", update.notes, "media_term")
    for key, value in update.recipe.items():
        repaired[key] = copy.deepcopy(value)
    repaired["data_quality_flags"] = [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    repaired["references"] = existing_references
    _ensure_references(repaired, update.reference_urls)
    _append_curation_event(repaired, update)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans = {}
    for update in UPDATES:
        path = normalized / update.path
        plans[path] = repair_record(_load(path), update)
    return plans


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in plans.items():
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
