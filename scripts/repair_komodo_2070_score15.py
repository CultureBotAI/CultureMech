#!/usr/bin/env python3
"""Repair KOMODO 2070 Trace metal solution (Kelly solution T) records."""

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
PRIMARY_TARGET = Path("bacterial/trace_metal_solution_kelly_solution_t.yaml")
REPLACEMENT_TARGET = Path(
    "bacterial/"
    "trace_metal_solution_kelly_solution_t_replace_cacl2_x_2_h2o_with_cacl2_x_2_h2o.yaml"
)
TARGETS: dict[Path, dict[str, str]] = {
    PRIMARY_TARGET: {
        "id": "CultureMech:004346",
        "media_term": "komodo.medium:2070",
    },
    REPLACEMENT_TARGET: {
        "id": "CultureMech:004345",
        "media_term": "komodo.medium:2070_replace_CaCl2 x 2 H2O_with_CaCl2 x 2 H2O",
    },
}
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_2070_score15.py"
ACTION = "RESOLVED_KOMODO_2070_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

KOMODO_2070 = (
    "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=2070"
)
SOURCE = "KOMODO Medium 2070"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (("NaOH", "variable", "VARIABLE"),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("CoCl2 x 6 H2O", "0.50", "G_PER_L"),
    ("Ammonium molybdate", "0.50", "G_PER_L"),
    ("CaCl2 x 2 H2O", "5.00", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "1.00", "G_PER_L"),
    ("H2O", "1.0", "L"),
    ("EDTA", "50.00", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.20", "G_PER_L"),
    ("MnCl2 x 4 H2O", "2.50", "G_PER_L"),
    ("FeSO4 x 7 H2O", "5.00", "G_PER_L"),
    ("NaOH", "9.00", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Ammonium molybdate": ("CHEBI:91249", "ammonium molybdate"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "EDTA": ("CHEBI:4735", "ethylenediaminetetraacetic acid"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "H2O": ("CHEBI:15377", "water"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
}

PH_VALUE = 6.0

NOTES = (
    "KOMODO 2070 lists Trace metal solution (Kelly solution T) as a defined "
    "submedium at pH 6.0. Its metabolite table contains 50.00 g/L EDTA, "
    "9.00 g/L NaOH, 5.00 g/L CaCl2 x 2 H2O, 5.00 g/L FeSO4 x 7 H2O, "
    "2.50 g/L MnCl2 x 4 H2O, 1.00 g/L ZnSO4 x 7 H2O, "
    "0.50 g/L CoCl2 x 6 H2O, 0.50 g/L Ammonium molybdate, "
    "0.20 g/L CuSO4 x 5 H2O, and H2O."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare the 1 L Kelly solution T stock from H2O, EDTA, NaOH, "
            "and the cobalt, molybdate, calcium, zinc, copper, manganese, "
            "and iron salts listed by KOMODO 2070."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the Kelly solution T stock to pH 6.0 with NaOH as needed.",
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
            "the solvent for 1 L of Kelly solution T."
        )
    elif preferred_term == "NaOH":
        row["notes"] = (
            f"{SOURCE} lists 9.00 g/L NaOH and also identifies NaOH as the "
            "pH adjuster for pH 6.0."
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


def _ensure_target(target: Path, doc: dict[str, Any]) -> None:
    expected = TARGETS[target]
    if doc.get("id") != expected["id"]:
        raise ValueError(f"{target}: expected id {expected['id']}, found {doc.get('id')!r}")
    if _source_term_id(doc) != expected["media_term"]:
        raise ValueError(f"{target}: expected media term {expected['media_term']}")

    ingredient_signature = _signature(doc.get("ingredients"))
    if ingredient_signature not in {
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    }:
        raise ValueError(f"{target}: ingredient signature drifted to {ingredient_signature!r}")

    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")
    if solutions:
        raise ValueError(f"{target}: unexpected solutions")


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

    if not any(row.get("reference") == KOMODO_2070 for row in references if isinstance(row, dict)):
        references.append({"reference": KOMODO_2070})


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
        "source": KOMODO_2070,
        "notes": (
            "Replaced the NaOH-only pH-buffer import with the complete KOMODO "
            "2070 metabolite table; preserved NaOH as a quantitative listed "
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


def repair_record(target: Path, doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(target, doc)

    repaired = copy.deepcopy(doc)
    _set_solution_record_kind(repaired)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ph_value"] = PH_VALUE
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
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target
        plans[path] = repair_record(target, _load(path))
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
