#!/usr/bin/env python3
"""Repair KOMODO 3133 VR salts B from Rogosa 1969."""

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
TARGET = Path("bacterial/vr_salts_b.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_3133_vr_salts_b_score15.py"
ACTION = "RESOLVED_KOMODO_3133_VR_SALTS_B_SCORE15"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

EXPECTED_ID = "CultureMech:004981"
EXPECTED_MEDIA_TERM = "komodo.medium:3133"

ROGOSA_1969 = "https://pmc.ncbi.nlm.nih.gov/articles/PMC284882/"
ROGOSA_1969_DOI = "https://doi.org/10.1128/jb.98.2.756-766.1969"
SOURCE = "Rogosa 1969 VR salts solution B"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (("NaOH", "variable", "VARIABLE"),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("MgSO4 x 7 H2O", "24.0", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.5", "G_PER_L"),
    ("FeSO4 x 7 H2O", "0.5", "G_PER_L"),
    ("ZnSO4", "0.25", "G_PER_L"),
    ("MnSO4 x H2O", "0.25", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.25", "G_PER_L"),
    ("VSO4 x 7 H2O", "0.25", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.25", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.125", "G_PER_L"),
    ("HCl", "2.0", "ML_PER_L"),
    ("Nitrilotriacetic acid", "5.0", "G_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "HCl": ("CHEBI:17883", "hydrogen chloride"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnSO4 x H2O": ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "ZnSO4": ("CHEBI:35176", "zinc sulfate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "mL/L",
    "VARIABLE": "variable",
}

NOTES = (
    "Rogosa 1969 defines VR salts solution B as a one-liter stock made from "
    "magnesium, calcium, iron, zinc, manganese, cobalt, vanadium, molybdate, "
    "and copper salts, HCl, nitrilotriacetic acid, distilled water, and 10 N "
    "NaOH to dissolve the NTA. KOMODO imported only the NaOH pH-buffer note "
    "for this submedium."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Dissolve the magnesium, calcium, iron, zinc, manganese, cobalt, "
            "vanadium, molybdate, and copper salts in about 700 ml water by "
            "applying heat and adding 2 ml HCl."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": (
            "Separately add nitrilotriacetic acid to 300 ml distilled water "
            "with stirring and add 10 N NaOH until the pH tends to stabilize "
            "at 7.0 to 7.4 and the NTA dissolves."
        ),
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "Slowly add the NTA solution to the stirred mixed-salts solution "
            "until the stock becomes fairly clear."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": "Adjust the volume of VR salts solution B to 1 liter.",
    },
    {
        "step_number": 5,
        "action": "FILTER",
        "description": "Filter VR salts solution B through paper.",
    },
    {
        "step_number": 6,
        "action": "STORE",
        "description": "Refrigerate the filtered VR salts solution B stock.",
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

    if preferred_term == "CoCl2 x 6 H2O":
        row["notes"] = (
            f"{SOURCE} lists 0.25 g/L CoCl2 x 6 H2O and allows "
            "Co(C2H3O2)2 x 4 H2O as an alternative cobalt source."
        )
    elif preferred_term == "Distilled water":
        row["notes"] = (
            f"{SOURCE} makes the stock up to one liter after dissolving salts "
            "in about 700 ml water and NTA in 300 ml distilled water."
        )
    elif preferred_term == "HCl":
        row["notes"] = (
            f"{SOURCE} adds 2 ml HCl while heating the salts; the HCl "
            "concentration is not stated."
        )
    elif preferred_term == "NaOH":
        row["notes"] = (
            f"{SOURCE} adds 10 N NaOH until the NTA solution tends to "
            "stabilize at pH 7.0 to 7.4."
        )
    elif preferred_term == "VSO4 x 7 H2O":
        row["notes"] = (
            f"{SOURCE} lists 0.25 g/L VSO4 x 7 H2O and allows NH4VO3 as an "
            "alternative vanadium source."
        )
    elif preferred_term == "ZnSO4":
        row["notes"] = f"{SOURCE} lists anhydrous ZnSO4 at 0.25 g/L."

    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
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
    flags.extend(("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in (ROGOSA_1969, ROGOSA_1969_DOI):
        if reference not in existing:
            references.append({"reference": reference})


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
        "source": ROGOSA_1969,
        "notes": (
            "Replaced the NaOH-only pH-buffer import with Rogosa's VR salts "
            "solution B stock recipe, choosing the first listed cobalt and "
            "vanadium source alternatives and leaving VSO4 x 7 H2O ungrounded."
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
    repaired.pop("ph_value", None)
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
