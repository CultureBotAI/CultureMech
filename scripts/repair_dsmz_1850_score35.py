#!/usr/bin/env python3
"""Repair the empty DSMZ 1850 Sf1Ep cell-culture medium record."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_dsmz_1850_score35.py"
ACTION = "RESOLVED_DSMZ_1850_SCORE35_GRAPH"
TIMESTAMP = "2026-09-08T00:00:00-07:00"

TARGET = "bacterial/cultivation_medium_for_sf1ep_cells_for_treponema_pallidum.yaml"
TARGET_ID = "CultureMech:001271"
TARGET_SOURCE = "mediadive.medium:1850"
DSMZ_1850 = "https://mediadive.dsmz.de/medium/1850"

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "temperature_value",
    "ingredients",
    "preparation_steps",
    "sterilization",
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _supplier(supplier_name: str, catalog_number: str) -> dict[str, str]:
    return {"supplier_name": supplier_name, "catalog_number": catalog_number}


def _ingredient(
    preferred_term: str,
    value: str,
    *,
    notes: str,
    term: tuple[str, str] | None = None,
    supplier_catalog: dict[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": "DSMZ Medium 1850",
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        row["mediaingredientmech_chebi_term"] = _term(*term)
    if supplier_catalog is not None:
        row["supplier_catalog"] = supplier_catalog
    return row


DSMZ_RECIPE = {
    "medium_type": "COMPLEX",
    "composition_type": "UNDEFINED",
    "physical_state": "LIQUID",
    "temperature_value": 37.0,
    "ingredients": [
        _ingredient(
            "Eagle's MEM",
            "884.956",
            notes=(
                "DSMZ Medium 1850 lists 500 ml Eagle's MEM (Sigma M4655) in "
                "a 565 ml Sf1Ep medium batch."
            ),
            supplier_catalog=_supplier("Sigma", "M4655"),
        ),
        _ingredient(
            "MEM Non-Essential Amino Acids",
            "8.84956",
            notes=(
                "DSMZ Medium 1850 lists 5 ml MEM Non-Essential Amino Acids "
                "(Gibco 11140-050) in a 565 ml Sf1Ep medium batch."
            ),
            supplier_catalog=_supplier("Gibco", "11140-050"),
        ),
        _ingredient(
            "L-glutamine solution",
            "8.84956",
            notes=(
                "DSMZ Medium 1850 lists 5 ml L-glutamine (Sigma G7513) in a "
                "565 ml Sf1Ep medium batch; the stock concentration is not "
                "disclosed."
            ),
            term=("CHEBI:18050", "L-glutamine"),
            supplier_catalog=_supplier("Sigma", "G7513"),
        ),
        _ingredient(
            "Sodium pyruvate solution",
            "8.84956",
            notes=(
                "DSMZ Medium 1850 lists 5 ml sodium pyruvate (Sigma S8636) "
                "in a 565 ml Sf1Ep medium batch; the stock concentration is "
                "not disclosed."
            ),
            term=("CHEBI:50144", "sodium pyruvate"),
            supplier_catalog=_supplier("Sigma", "S8636"),
        ),
        _ingredient(
            "Fetal bovine serum, heat inactivated",
            "88.4956",
            notes=(
                "DSMZ Medium 1850 lists 50 ml heat-inactivated fetal bovine "
                "serum in a 565 ml Sf1Ep medium batch."
            ),
        ),
    ],
    "preparation_steps": [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Combine Eagle's MEM, MEM Non-Essential Amino Acids, "
                "L-glutamine, sodium pyruvate, and heat-inactivated fetal "
                "bovine serum at the DSMZ Medium 1850 Sf1Ep medium ratios."
            ),
        },
        {
            "step_number": 2,
            "action": "FILTER_STERILIZE",
            "description": "Filter sterilize the Sf1Ep medium.",
        },
        {
            "step_number": 3,
            "action": "STORE",
            "description": "Store the filter-sterilized Sf1Ep medium at 4 C.",
        },
    ],
    "sterilization": {"method": "FILTER"},
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str | None:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return None
    term = media_term.get("term")
    if not isinstance(term, dict):
        return None
    term_id = term.get("id")
    return str(term_id) if term_id else None


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != TARGET_ID:
        raise ValueError(f"{TARGET}: found id {doc.get('id')!r}, expected {TARGET_ID!r}")

    source_term = _source_term_id(doc)
    if source_term != TARGET_SOURCE:
        raise ValueError(
            f"{TARGET}: found source term {source_term!r}, expected {TARGET_SOURCE!r}"
        )


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
        raise ValueError(f"{TARGET}: data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    ingredients = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    has_unmapped = any(not _grounded(row) for row in ingredients)

    if any("mediaingredientmech_chebi_term" in row for row in ingredients):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")
    elif "has_ontology_mappings" in flags:
        flags.remove("has_ontology_mappings")

    if has_unmapped and "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")
    elif not has_unmapped and "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    if not any(_grounded(row) for row in ingredients):
        raise ValueError("repaired recipe has no grounded ingredients")


def _ensure_reference(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{TARGET}: references is not a list")

    if not any(
        isinstance(row, dict) and row.get("reference") == DSMZ_1850
        for row in references
    ):
        references.append({"reference": DSMZ_1850})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved empty DSMZ 1850 Sf1Ep medium recipe",
        "source": DSMZ_1850,
        "notes": (
            "MediaDive's structured DSMZ Medium 1850 main solution is empty, "
            "but its DSMZ description explicitly lists a 565 ml Sf1Ep medium "
            "batch: 500 ml Eagle's MEM, 5 ml MEM Non-Essential Amino Acids, "
            "5 ml L-glutamine, 5 ml sodium pyruvate, and 50 ml "
            "heat-inactivated fetal bovine serum."
        ),
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET}: curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _require_target(doc)

    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        if field in DSMZ_RECIPE:
            repaired[field] = copy.deepcopy(DSMZ_RECIPE[field])
        else:
            repaired.pop(field, None)

    _put_after(
        repaired,
        "notes",
        (
            "DSMZ Medium 1850 records a Sf1Ep cottontail rabbit epithelial "
            "cell medium prepared from Eagle's MEM, MEM Non-Essential Amino "
            "Acids, L-glutamine, sodium pyruvate, and heat-inactivated fetal "
            "bovine serum, then filter-sterilized and stored at 4 C."
        ),
        "media_term",
    )
    _ensure_flags(repaired)
    _ensure_reference(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    repaired = repair_record(_load(path))
    if path.read_bytes() == dump_record(repaired).encode("utf-8"):
        return {}
    return {path: repaired}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    plans = plan_repairs()
    if args.dry_run:
        for path in plans:
            print(f"would update {path.relative_to(REPO)}")
        print(f"would update {len(plans)} DSMZ 1850 records")
        return

    changed = 0
    for path, doc in plans.items():
        if write_record(path, doc):
            changed += 1
    print(f"updated {changed} DSMZ 1850 records")


if __name__ == "__main__":
    main()
