#!/usr/bin/env python3
"""Repair KOMODO 2052 Trace element solution (medium 882)."""

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
TARGET = Path("bacterial/trace_element_solution_medium_882.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_2052_score15.py"
ACTION = "RESOLVED_KOMODO_2052_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:004325"
EXPECTED_MEDIA_TERM = "komodo.medium:2052"
KOMODO_2052 = (
    "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=2052"
)
SOURCE = "KOMODO Medium 2052"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (("H2SO4", "variable", "VARIABLE"),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("CoCl2 x 6 H2O", "0.06", "G_PER_L"),
    ("ZnCl2", "0.07", "G_PER_L"),
    ("MnCl2 x 2 H2O", "0.06", "G_PER_L"),
    ("H2O", "1.0", "L"),
    ("Na2MoO4", "0.01", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.07", "G_PER_L"),
    ("H2SO4", "variable", "VARIABLE"),
    ("H3BO3", "0.03", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2 H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "H2O": ("CHEBI:15377", "water"),
    "H2SO4": ("CHEBI:26836", "sulfuric acid"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "MnCl2 x 2 H2O": ("CHEBI:131395", "manganese(II) chloride dihydrate"),
    "Na2MoO4": ("CHEBI:75215", "sodium molybdate (anhydrous)"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "VARIABLE": "variable",
}

NOTES = (
    "KOMODO 2052 lists Trace element solution (medium 882) as a defined "
    "submedium at pH 1.8. Its metabolite table contains 0.07 g/L ZnCl2, "
    "0.07 g/L CuCl2 x 2 H2O, 0.06 g/L CoCl2 x 6 H2O, 0.06 g/L "
    "MnCl2 x 2 H2O, 0.03 g/L H3BO3, 0.01 g/L Na2MoO4, variable H2SO4, "
    "and H2O."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare the 1 L Trace element solution stock from H2O, H2SO4, "
            "and the cobalt, zinc, manganese, molybdate, copper, and borate "
            "salts listed by KOMODO 2052."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the Trace element solution stock to pH 1.8 with H2SO4 as needed.",
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if preferred_term == "H2O":
        row["notes"] = (
            f"{SOURCE} lists H2O without a gram amount; normalized here as "
            "the solvent for 1 L of Trace element solution (medium 882)."
        )
    elif preferred_term == "H2SO4":
        row["notes"] = (
            f"{SOURCE} lists H2SO4 without a gram amount and also identifies "
            "H2SO4 as the pH adjuster for pH 1.8."
        )

    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients() -> list[dict[str, Any]]:
    return [
        _component(preferred_term, value, unit)
        for preferred_term, value, unit in FINAL_INGREDIENT_SIGNATURE
    ]


def _signature(rows: Any) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("ingredients is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("ingredients contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"ingredient {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"))
    if ingredient_signature not in {
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    }:
        raise ValueError(f"{TARGET}: ingredient signature drifted to {ingredient_signature!r}")

    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")
    if solutions:
        raise ValueError(f"{TARGET}: unexpected solutions")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag not in {"extracted_from_notes", "incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(("has_ontology_mappings", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    if not any(row.get("reference") == KOMODO_2052 for row in references if isinstance(row, dict)):
        references.append({"reference": KOMODO_2052})


def _set_solution_record_kind(doc: dict[str, Any]) -> None:
    reordered: dict[str, Any] = {}
    inserted = False
    for key, value in doc.items():
        if key == "record_kind":
            continue
        reordered[key] = value
        if key == "category":
            reordered["record_kind"] = "SOLUTION"
            inserted = True
    if not inserted:
        reordered["record_kind"] = "SOLUTION"

    doc.clear()
    doc.update(reordered)


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": KOMODO_2052,
        "notes": (
            "Replaced the H2SO4-only pH-buffer import with the complete KOMODO "
            "2052 metabolite table; preserved H2SO4 as a variable listed "
            "component and pH adjuster; and grounded all disclosed components "
            "through MediaIngredientMech."
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


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    _set_solution_record_kind(repaired)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 1.8, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(PREPARATION_STEPS)),
        "notes",
    )
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_record(_load(path))}


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
