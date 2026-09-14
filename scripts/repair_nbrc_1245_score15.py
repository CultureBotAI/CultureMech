#!/usr/bin/env python3
"""Repair the NBRC Medium 1243 Brain Heart Infusion + 2% NaCl record."""

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

CURATOR = "repair_nbrc_1245_score15.py"
ACTION = "RESOLVED_NBRC_1245_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TARGET_PATH = "bacterial/NBRC_1245.yaml"
TARGET_ID = "CultureMech:007466"
REQUIRED_ACTION = "Removed corrupt rows, kept curated composition"

SOURCE = "NBRC Medium 1243"
NBRC_URL = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1243"
TITLE = "Brain Heart Infusion + 2% NaCl"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Calf brains", "variable", "VARIABLE"),
    ("Beef heart", "variable", "VARIABLE"),
    ("Proteose peptone", "10.0", "G_PER_L"),
    ("Dextrose", "2.0", "G_PER_L"),
    ("Sodium chloride", "5.0", "G_PER_L"),
    ("Disodium phosphate", "2.5", "G_PER_L"),
)
NBRC_ADDITION_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "L"),
    ("NaCl", "20", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
)
FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    IMPORTED_INGREDIENT_SIGNATURE + NBRC_ADDITION_SIGNATURE
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "Dextrose": ("CHEBI:17634", "D-glucose"),
    "Disodium phosphate": ("CHEBI:34683", "disodium hydrogenphosphate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Sodium chloride": ("CHEBI:26710", "sodium chloride"),
}

ADDITIONAL_COMPONENTS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Distilled water",
        "concentration": {"value": "1", "unit": "L"},
        "source": SOURCE,
        "notes": "NBRC Medium 1243 lists 1 L distilled water.",
    },
    {
        "preferred_term": "NaCl",
        "concentration": {"value": "20", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": (
            "NBRC Medium 1243 supplements 37 g Bacto Brain Heart Infusion with "
            "20 g additional NaCl."
        ),
    },
    {
        "preferred_term": "Agar (if needed)",
        "concentration": {"value": "15", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": "NBRC Medium 1243 lists 15 g agar if needed.",
    },
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "DISSOLVE",
        "description": (
            "Dissolve 37 g Bacto Brain Heart Infusion and 20 g NaCl in 1 L "
            "distilled water; add 15 g agar if solid medium is needed."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Sterilize by autoclaving.",
    },
)

NOTES = (
    "Source: NBRC Medium 1243 | Link: "
    "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1243\n\n"
    "NBRC lists Brain Heart Infusion + 2% NaCl with 37 g Bacto Brain Heart "
    "Infusion, 20 g supplemental NaCl, 1 L distilled water, and 15 g agar if "
    "solid medium is needed. The BHI premix is preserved as a curated expanded "
    "constituent formula from the existing record."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(template: dict[str, Any]) -> dict[str, Any]:
    row = copy.deepcopy(template)
    term = GROUNDINGS[str(row["preferred_term"])]
    row["term"] = _term(*term)
    row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


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


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _has_history_action(doc: dict[str, Any], action: str) -> bool:
    return any(
        isinstance(event, dict) and event.get("action") == action
        for event in doc.get("curation_history") or []
    )


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != TARGET_ID:
        raise ValueError(
            f"{TARGET_PATH}: found id {doc.get('id')!r}, expected {TARGET_ID!r}"
        )
    if not _has_history_action(doc, REQUIRED_ACTION):
        raise ValueError(f"{TARGET_PATH}: missing recovery action {REQUIRED_ACTION!r}")
    if doc.get("name") not in {"1245", TITLE}:
        raise ValueError(f"{TARGET_PATH}: NBRC title/name drifted")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in {
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    }:
        raise ValueError(
            f"{TARGET_PATH}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )


def _ground_components(doc: dict[str, Any]) -> None:
    for row in doc.get("ingredients") or []:
        if not isinstance(row, dict):
            continue
        term = GROUNDINGS.get(str(row.get("preferred_term") or ""))
        if not term:
            continue
        row["term"] = _term(*term)
        row["mediaingredientmech_chebi_term"] = _term(*term)


def _ensure_nbrc_rows(doc: dict[str, Any]) -> None:
    ingredients = doc.get("ingredients")
    if not isinstance(ingredients, list):
        raise ValueError("ingredients is not a list")

    existing = {
        row.get("preferred_term") for row in ingredients if isinstance(row, dict)
    }
    for template in ADDITIONAL_COMPONENTS:
        if template["preferred_term"] not in existing:
            ingredients.append(_component(template))


def _grounded(component: dict[str, Any]) -> bool:
    term = component.get("term")
    return isinstance(term, dict) and bool(term.get("id"))


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)

    ingredients = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    if any(not _grounded(ingredient) for ingredient in ingredients):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


def _ensure_reference(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    found = {row.get("reference") for row in references if isinstance(row, dict)}
    if NBRC_URL not in found:
        references.append({"reference": NBRC_URL})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Curated NBRC Medium 1243 identity and composition",
        "source": NBRC_URL,
        "notes": (
            "Added the NBRC Medium 1243 source term and official title, kept "
            "the curated BHI premix expansion, and restored NBRC's 20 g NaCl, "
            "1 L distilled water, and 15 g agar if needed."
        ),
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


def repair_document(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "name", TITLE, "id")
    _put_after(repaired, "original_name", TITLE, "name")
    _put_after(
        repaired,
        "media_term",
        {
            "preferred_term": SOURCE,
            "term": _term("nbrc.medium:1243", SOURCE),
        },
        "physical_state",
    )
    _put_after(repaired, "notes", NOTES, "description")

    _ground_components(repaired)
    _ensure_nbrc_rows(repaired)
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["sterilization"] = {"method": "AUTOCLAVE"}

    _ensure_flags(repaired)
    _ensure_reference(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET_PATH
    return {path: repair_document(_load(path))}


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

    action = "Updated" if args.apply else "Would update"
    print(f"{action} {changed_count} NBRC 1245 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
