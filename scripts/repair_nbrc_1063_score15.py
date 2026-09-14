#!/usr/bin/env python3
"""Repair the recovered NBRC Medium 1062 Pae I urea record."""

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

CURATOR = "repair_nbrc_1063_score15.py"
ACTION = "RESOLVED_NBRC_1063_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TARGET_PATH = "bacterial/NBRC_1063.yaml"
TARGET_ID = "CultureMech:007453"
REQUIRED_ACTION = "Recovered composition from source HTML"

SOURCE = "NBRC Medium 1062"
NBRC_URL = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1062"
TITLE = "Pae I Medium + 0.1% (w/v) Urea"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Tryptone", "5", "G_PER_L"),
    ("Yeast extract", "3", "G_PER_L"),
    ("NaCl", "10", "G_PER_L"),
    ("Urea", "1", "G_PER_L"),
    ("Distilled water", "1", "L"),
    ("Agar (if needed)", "15", "G_PER_L"),
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str,
    term: tuple[str, str],
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
        "term": _term(*term),
    }
    if term[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _step(step_number: int, action: str, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": action,
        "description": description,
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Tryptone",
        "5",
        "G_PER_L",
        notes="NBRC Medium 1062 lists 5 g tryptone.",
        term=("MICRO:0000182", "tryptone"),
    ),
    _component(
        "Yeast extract",
        "3",
        "G_PER_L",
        notes="NBRC Medium 1062 lists 3 g yeast extract.",
        term=("FOODON:03315426", "yeast extract"),
    ),
    _component(
        "NaCl",
        "10",
        "G_PER_L",
        notes="NBRC Medium 1062 lists 10 g NaCl.",
        term=("CHEBI:26710", "sodium chloride"),
    ),
    _component(
        "Urea",
        "1",
        "G_PER_L",
        notes="NBRC Medium 1062 lists 1 g urea.",
        term=("CHEBI:16199", "urea"),
    ),
    _component(
        "Distilled water",
        "1",
        "L",
        notes="NBRC Medium 1062 lists 1 L distilled water.",
        term=("CHEBI:15377", "water"),
    ),
    _component(
        "Agar (if needed)",
        "15",
        "G_PER_L",
        notes="NBRC Medium 1062 lists 15 g agar if needed.",
        term=("CHEBI:2509", "agar"),
    ),
    _component(
        "Tris-HCl buffer",
        "variable",
        "VARIABLE",
        notes=("NBRC Medium 1062 adjusts the medium to pH 8.5 with 50 mM " "Tris-HCl buffer."),
        term=("CHEBI:9754", "tris"),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    _step(
        1,
        "DISSOLVE",
        (
            "Dissolve tryptone, yeast extract, NaCl, urea, and agar if needed "
            "in 1 L distilled water."
        ),
    ),
    _step(2, "ADJUST_PH", "Adjust pH to 8.5 with 50 mM Tris-HCl buffer."),
    _step(3, "AUTOCLAVE", "Sterilize by autoclaving."),
)

NOTES = (
    "Source: NBRC Medium 1062 | Link: "
    "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1062\n\n"
    "NBRC lists Pae I Medium with 0.1% (w/v) urea, tryptone, yeast extract, "
    "NaCl, optional agar, and adjustment to pH 8.5 with 50 mM Tris-HCl buffer."
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in INGREDIENTS
)


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
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
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
        raise ValueError(f"{TARGET_PATH}: found id {doc.get('id')!r}, expected {TARGET_ID!r}")
    if not _has_history_action(doc, REQUIRED_ACTION):
        raise ValueError(f"{TARGET_PATH}: missing recovery action {REQUIRED_ACTION!r}")
    if doc.get("name") not in {"1063", TITLE}:
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
        "changes": "Curated NBRC Medium 1062 identity, pH, buffer, and reference",
        "source": NBRC_URL,
        "notes": (
            "Added the NBRC Medium 1062 source term and official title, grounded "
            "tryptone, yeast extract, agar, and Tris-HCl buffer, and recorded "
            "pH 8.5."
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
            "term": _term("nbrc.medium:1062", SOURCE),
        },
        "physical_state",
    )
    _put_after(repaired, "ph_value", 8.5, "media_term")
    _put_after(repaired, "notes", NOTES, "description")

    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
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
    print(f"{action} {changed_count} NBRC 1063 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
