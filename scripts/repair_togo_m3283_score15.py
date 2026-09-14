#!/usr/bin/env python3
"""Repair TOGO M3283 Pectin Medium."""

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
TARGET = Path("bacterial/TOGO_M3283_Pectin_Medium.yaml")
PARENT = Path("bacterial/pectin_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009697"
EXPECTED_PARENT_ID = "CultureMech:001273"
EXPECTED_MEDIA_TERM = "TOGO:M3283"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:1855"

CURATOR = "repair_togo_m3283_score15.py"
ACTION = "RESOLVED_TOGO_M3283_SCORE15"
LINK_ACTION = "LINKED_TOGO_M3283_DERIVED_FROM"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M3283 = "https://togomedium.org/medium/M3283"
JCM_1453 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1453"

SOURCE = "TOGO M3283 / JCM Medium 1453"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

MIDDLE_DOT = "\u00b7"

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "3", "G_PER_L"),
    ("NaCl", "5", "G_PER_L"),
    ("Pectin (from citrus)", "3", "G_PER_L"),
    (f"L-Cysteine{MIDDLE_DOT}HCl{MIDDLE_DOT}H2O", "0.5", "G_PER_L"),
    ("Hipolypepton", "3", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "5.0", "G_PER_L"),
    ("Yeast extract", "3.0", "G_PER_L"),
    ("Hipolypepton", "3.0", "G_PER_L"),
    ("Pectin (from citrus)", "3.0", "G_PER_L"),
    ("L-Cysteine HCl H2O", "0.5", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("0.1% Resazurin solution", "1", "G_PER_L", ()),
)

RESAZURIN_STOCK_SIGNATURE: tuple[Component, ...] = (("Resazurin", "1.0", "G_PER_L"),)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("0.1% Resazurin solution", "1.0", "ML_PER_L", RESAZURIN_STOCK_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "Distilled water": ("CHEBI:15377", "water"),
    "L-Cysteine HCl H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "Pectin (from citrus)": ("CHEBI:17309", "pectin"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "ML_PER_L": "ml/L",
    "VARIABLE": "variable",
}

REFERENCES = (TOGO_M3283, JCM_1453)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "DERIVED_FROM",
    "id": EXPECTED_PARENT_ID,
    "name": "pectin_medium",
    "notes": (
        "TOGO M3283 imports JCM Medium 1453, a recognizable Pectin medium "
        "formulation that uses lower Yeast extract, pH 7.5, and N2-CO2 "
        "autoclaving relative to DSMZ Medium 1855."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "DERIVED_FROM",
    "id": EXPECTED_ID,
    "name": "pectin_medium",
    "notes": (
        "TOGO M3283 imports JCM Medium 1453, a pectin medium formulation "
        "derived from the DSMZ Medium 1855 component set with different "
        "yeast-extract and pH conditions."
    ),
}

VARIANT_MODIFICATIONS = (
    "Uses the DSMZ Medium 1855 pectin base components with 3.0 g/L instead "
    "of 5.0 g/L Yeast extract, pH 7.5 instead of pH 6.5, and JCM Medium "
    "1453 autoclaving under N2-CO2 (1:1, v/v)."
)

NOTES = (
    "TOGO M3283 imports JCM Medium 1453 Pectin Medium. JCM Medium 1453 lists, "
    "per liter, 5.0 g NaCl, 3.0 g Yeast extract, 3.0 g Hipolypepton, "
    "3.0 g Pectin from citrus, 0.5 g L-Cysteine HCl H2O, 1.0 ml 0.1% "
    "Resazurin solution, and 1.0 L Distilled water. Thoroughly mix the "
    "components, adjust to pH 7.5, and autoclave under N2-CO2 (1:1, v/v)."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str | None = None,
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes or f"JCM Medium 1453 lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredient(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    if unit == "VARIABLE":
        return _component(
            preferred_term,
            value,
            unit,
            notes=(
                "JCM Medium 1453 autoclaves the medium under an N2-CO2 "
                "(1:1, v/v) gas atmosphere."
            ),
        )
    return _component(
        preferred_term,
        value,
        unit,
        term=preferred_term not in {"Yeast extract", "Hipolypepton"},
    )


def _ingredients() -> list[dict[str, Any]]:
    return [
        _ingredient(preferred_term, value, unit)
        for preferred_term, value, unit in FINAL_INGREDIENT_SIGNATURE
    ]


def _solutions() -> list[dict[str, Any]]:
    return [
        {
            "preferred_term": "0.1% Resazurin solution",
            "concentration": {"value": "1.0", "unit": "ML_PER_L"},
            "source": SOURCE,
            "notes": "JCM Medium 1453 adds 1.0 ml/L 0.1% Resazurin solution.",
            "composition": [
                _component(
                    "Resazurin",
                    "1.0",
                    "G_PER_L",
                    notes=("A 0.1% w/v Resazurin solution is represented as " "1.0 g/L Resazurin."),
                )
            ],
        }
    ]


PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Thoroughly mix NaCl, Yeast extract, Hipolypepton, Pectin from "
            "citrus, L-Cysteine HCl H2O, 0.1% Resazurin solution, and "
            "Distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.5.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave under an N2-CO2 (1:1, v/v) gas atmosphere.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": (
        "Autoclave the fully mixed medium under N2-CO2 (1:1, v/v); JCM "
        "defines autoclaving as 121 C for 15 min unless otherwise stated."
    ),
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
    if not isinstance(rows, (list, tuple)):
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


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError("solution row lacks concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(solution.get("composition"), "solution composition"),
            )
        )
    return tuple(signatures)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"{PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")


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


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(
    doc: dict[str, Any],
    *,
    action: str,
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(REFERENCES),
        "notes": notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
        ):
            history[index] = event
            return
    history.append(event)


def _ensure_variant_child(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    for index, child in enumerate(children):
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID or child.get("path") == TOGO_CHILD["path"]:
            children[index] = copy.deepcopy(TOGO_CHILD)
            return
    children.append(copy.deepcopy(TOGO_CHILD))


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.5, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    repaired["solutions"] = _solutions()
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(PREPARATION_STEPS)),
        "solutions",
    )
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _put_after(repaired, "notes", NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(
        repaired,
        action=ACTION,
        notes=(
            f"{NOTES} Corrected the imported water and Resazurin stock-addition "
            "unit artifacts, expanded the 0.1% Resazurin solution, added the "
            "JCM pH and N2-CO2 autoclaving conditions, left Yeast extract and "
            "Hipolypepton intentionally unmapped, and linked the record to "
            "DSMZ Medium 1855."
        ),
    )
    repaired["parent_media"] = copy.deepcopy(PARENT_MEDIA)
    repaired["variant_relationship"] = "DERIVED_FROM"
    repaired["variant_modifications"] = [VARIANT_MODIFICATIONS]
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    _ensure_variant_child(repaired)
    _append_curation_event(
        repaired,
        action=LINK_ACTION,
        notes="Linked TOGO M3283 as a derived variant of DSMZ Medium 1855.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    parent_path = normalized / PARENT
    return {
        target_path: repair_target(_load(target_path)),
        parent_path: repair_parent(_load(parent_path)),
    }


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
