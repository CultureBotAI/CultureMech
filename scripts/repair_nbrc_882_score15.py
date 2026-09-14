#!/usr/bin/env python3
"""Repair the recovered NBRC Medium 881 GYP medium record."""

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

CURATOR = "repair_nbrc_882_score15.py"
ACTION = "RESOLVED_NBRC_882_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TARGET_PATH = "bacterial/NBRC_882.yaml"
TARGET_ID = "CultureMech:007501"
REQUIRED_ACTION = "Recovered composition from source HTML"

SOURCE = "NBRC Medium 881"
NBRC_URL = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=881"
TITLE = "GYP medium (pH 6)"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Glucose", "10", "G_PER_L"),
    ("Bacto Yeast Extract (Difco)", "10", "G_PER_L"),
    ("Hipolypepton*", "5", "G_PER_L"),
    ("Sodium acetate", "2", "G_PER_L"),
    ("Tween 80 solution**", "10", "ML_PER_L"),
    ("Salts solution***", "5", "ML_PER_L"),
    ("Distilled water", "1", "L"),
)
FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    *IMPORTED_INGREDIENT_SIGNATURE,
    ("CaCO3", "5", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
)

TWEEN_80_SIGNATURE: tuple[Component, ...] = (
    ("Tween 80", "50", "G_PER_L"),
    ("Distilled water", "1", "L"),
)
SALTS_SIGNATURE: tuple[Component, ...] = (
    ("MgSO4·7H2O", "40", "G_PER_L"),
    ("MnSO4·4H2O", "2", "G_PER_L"),
    ("FeSO4·7H2O", "2", "G_PER_L"),
    ("NaCl", "2", "G_PER_L"),
    ("Distilled water", "1", "L"),
)
IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Tween 80 solution", TWEEN_80_SIGNATURE),
    ("Salts solution", SALTS_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "CaCO3": ("CHEBI:3311", "calcium carbonate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeSO4·7H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "MgSO4·7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnSO4·4H2O": ("CHEBI:86358", "manganese(II) sulfate tetrahydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Sodium acetate": ("CHEBI:32954", "sodium acetate"),
    "Tween 80": ("CHEBI:53426", "polysorbate 80"),
}

UNMAPPED_COMPONENTS = {
    "Bacto Yeast Extract (Difco)",
    "Hipolypepton*",
    "Tween 80 solution**",
    "Salts solution***",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": (
            "Prepare the basal GYP medium with Tween 80 solution and Salts "
            "solution, then adjust the medium to pH 6.0."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "For the solid medium, add 5 g/L CaCO3 and 15 g/L agar after " "the pH is adjusted."
        ),
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "Prepare the Salts solution with MgSO4·7H2O, MnSO4·4H2O, "
            "FeSO4·7H2O, NaCl, and distilled water, then add one drop of 12 "
            "N HCl to each 500 ml of the salts stock."
        ),
    },
)

NOTES = (
    "Source: NBRC Medium 881 | Link: "
    "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=881\n\n"
    "NBRC lists GYP medium (pH 6) with glucose, Bacto Yeast Extract "
    "(Difco), Hipolypepton, sodium acetate, Tween 80 solution, Salts "
    "solution, and distilled water at pH 6.0. The solid medium receives "
    "5 g/L CaCO3 and 15 g/L agar after pH adjustment."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str,
) -> dict[str, Any]:
    term = GROUNDINGS[preferred_term]
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
    }


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


def _solution_signature(solution: dict[str, Any]) -> SolutionSignature:
    return (
        str(solution.get("preferred_term") or ""),
        _signature(solution.get("composition"), "solution composition"),
    )


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")
    if any(not isinstance(solution, dict) for solution in solutions):
        raise ValueError("solutions contains a non-mapping row")
    return tuple(_solution_signature(solution) for solution in solutions)


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
    if doc.get("name") not in {"882", TITLE}:
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

    if _solution_signatures(doc) != IMPORTED_SOLUTION_SIGNATURES:
        raise ValueError(f"{TARGET_PATH}: nested solution signature drifted")


def _iter_components(doc: dict[str, Any]):
    yield from doc.get("ingredients") or []
    for solution in doc.get("solutions") or []:
        yield from solution.get("composition") or []


def _ground_components(doc: dict[str, Any]) -> None:
    for row in _iter_components(doc):
        name = str(row.get("preferred_term") or "")
        term = GROUNDINGS.get(name)
        if not term:
            continue
        row["term"] = _term(*term)
        row["mediaingredientmech_chebi_term"] = _term(*term)


def _ensure_solid_components(doc: dict[str, Any]) -> None:
    ingredients = doc.get("ingredients")
    if not isinstance(ingredients, list):
        raise ValueError(f"{TARGET_PATH}: ingredients is not a list")
    existing = {row.get("preferred_term") for row in ingredients if isinstance(row, dict)}

    if "CaCO3" not in existing:
        ingredients.append(
            _component(
                "CaCO3",
                "5",
                "G_PER_L",
                notes=(
                    "NBRC Medium 881 adds 5 g/L CaCO3 after pH adjustment " "for the solid medium."
                ),
            )
        )
    if "Agar" not in existing:
        ingredients.append(
            _component(
                "Agar",
                "15",
                "G_PER_L",
                notes=(
                    "NBRC Medium 881 adds 15 g/L agar after pH adjustment " "for the solid medium."
                ),
            )
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
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)

    chemical_rows = [
        row
        for row in _iter_components(doc)
        if (
            isinstance(row, dict)
            and str(row.get("preferred_term") or "") not in UNMAPPED_COMPONENTS
        )
    ]
    if any(not _grounded(row) for row in chemical_rows):
        raise ValueError(f"{TARGET_PATH}: not all source chemical rows were grounded")


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
        "changes": "Grounded recovered NBRC Medium 881 GYP solid-medium formula",
        "source": NBRC_URL,
        "notes": (
            "Added the NBRC Medium 881 source term and official title, "
            "structured the pH, added the missing source-listed CaCO3 and "
            "agar rows for the solid medium, grounded the recovered formula "
            "and nested stock solutions, converted preparation instructions "
            "into ordered steps, and added the official NBRC reference."
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
            "term": _term("nbrc.medium:881", SOURCE),
        },
        "physical_state",
    )
    _put_after(repaired, "ph_value", 6.0, "media_term")
    repaired.pop("ph_range", None)
    _put_after(repaired, "notes", NOTES, "description")

    _ground_components(repaired)
    _ensure_solid_components(repaired)
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))

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
    print(f"{action} {changed_count} NBRC 882 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
