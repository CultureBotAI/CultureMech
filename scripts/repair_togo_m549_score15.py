#!/usr/bin/env python3
"""Repair TOGO M549 Desulfotomaculum PBE Medium and its JCM J547 duplicate."""

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
TARGET = Path("bacterial/TOGO_M549_Desulfotomaculum_PBE_Medium.yaml")
PARENT = Path("bacterial/desulfotomaculum_pbe_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009942"
EXPECTED_PARENT_ID = "CultureMech:002894"
EXPECTED_MEDIA_TERM = "TOGO:M549"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:J547"

CURATOR = "repair_togo_m549_score15.py"
ACTION = "RESOLVED_TOGO_M549_SCORE15"
PARENT_ACTION = "RESOLVED_JCM_547_DESULFOTOMACULUM_PBE"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M549 = "https://togomedium.org/medium/M549"
JCM_547 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=547"
MEDIADIVE_J547 = "https://mediadive.dsmz.de/medium/J547"

TOGO_SOURCE = "TOGO M549 / JCM Medium 547"
PARENT_SOURCE = "MediaDive J547 / JCM Medium 547"
TITLE = "Desulfotomaculum PBE Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "900", "G_PER_L"),
    ("MgSO4\u30fb7H2O", "2", "G_PER_L"),
    ("Na2SO4", "1.5", "G_PER_L"),
    ("CaCl2", "0.1", "G_PER_L"),
    ("Beef extract", "1", "G_PER_L"),
    ("Peptone", "2", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
    ("5% Sodium lactate (autoclaved)", "70", "G_PER_L"),
)

IMPORTED_PARENT_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "2.0202", "G_PER_L"),
    ("Beef extract", "1.0101", "G_PER_L"),
    ("MgSO4 x 7 H2O", "2.0202", "G_PER_L"),
    ("Na2SO4", "1.51515", "G_PER_L"),
    ("CaCl2", "0.10101", "G_PER_L"),
    ("K2HPO4", "10", "G_PER_L"),
    ("Sodium lactate", "70", "G_PER_L"),
    ("Fe(NH4)2(SO4)2 x 6 H2O", "10", "G_PER_L"),
    ("Sodium ascorbate", "10", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "2.0", "G_PER_L"),
    ("Beef extract", "1.0", "G_PER_L"),
    ("MgSO4 x 7H2O", "2.0", "G_PER_L"),
    ("Na2SO4", "1.5", "G_PER_L"),
    ("CaCl2", "0.1", "G_PER_L"),
    ("Distilled water", "900.0", "ML_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("4% Fe(NH4)2(SO4)2\u30fb6H2O solution (filter--sterilized)", "10", "G_PER_L", ()),
    ("5% K2HPO4 solution (autoclaved)", "10", "G_PER_L", ()),
    ("1% Sodium ascorbate solution (filter--sterilized)", "10", "G_PER_L", ()),
)

K2HPO4_SIGNATURE: tuple[Component, ...] = (("K2HPO4", "5.0", "PERCENT_W_V"),)
SODIUM_LACTATE_SIGNATURE: tuple[Component, ...] = (
    ("Sodium lactate", "5.0", "PERCENT_W_V"),
)
FERROUS_AMMONIUM_SULFATE_SIGNATURE: tuple[Component, ...] = (
    ("Fe(NH4)2(SO4)2 x 6H2O", "4.0", "PERCENT_W_V"),
)
SODIUM_ASCORBATE_SIGNATURE: tuple[Component, ...] = (
    ("Sodium ascorbate", "1.0", "PERCENT_W_V"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("5% K2HPO4 solution", "10.0", "ML_PER_L", K2HPO4_SIGNATURE),
    ("5% Sodium lactate solution", "70.0", "ML_PER_L", SODIUM_LACTATE_SIGNATURE),
    (
        "4% Fe(NH4)2(SO4)2 x 6H2O solution",
        "10.0",
        "ML_PER_L",
        FERROUS_AMMONIUM_SULFATE_SIGNATURE,
    ),
    (
        "1% Sodium ascorbate solution",
        "10.0",
        "ML_PER_L",
        SODIUM_ASCORBATE_SIGNATURE,
    ),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Peptone": ("MICRO:0000178", "Peptone"),
    "Beef extract": ("FOODON:03302088", "Beef extract"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "Na2SO4": ("CHEBI:32149", "sodium sulfate"),
    "CaCl2": ("CHEBI:3312", "calcium dichloride"),
    "Distilled water": ("CHEBI:15377", "water"),
    "N2": ("CHEBI:17997", "dinitrogen"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "Sodium lactate": ("CHEBI:75228", "sodium lactate"),
    "Fe(NH4)2(SO4)2 x 6H2O": (
        "CHEBI:76181",
        "ferrous ammonium sulfate hexahydrate",
    ),
    "Sodium ascorbate": ("CHEBI:113451", "sodium ascorbate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
    "VARIABLE": "variable",
}

REFERENCES = (TOGO_M549, JCM_547, MEDIADIVE_J547)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_PARENT_ID,
    "name": "desulfotomaculum_pbe_medium",
    "notes": (
        "TOGO M549 imports the same JCM Medium 547 Desulfotomaculum PBE "
        "Medium formulation represented by MediaDive J547."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_ID,
    "name": "desulfotomaculum_pbe_medium",
    "notes": (
        "TOGO M549 imports the same JCM Medium 547 Desulfotomaculum PBE "
        "Medium formulation represented by MediaDive J547."
    ),
}

VARIANT_MODIFICATIONS = (
    "Same JCM Medium 547 Desulfotomaculum PBE Medium formulation as the "
    "MediaDive J547 source record."
)

RECIPE_NOTES = (
    "JCM Medium 547 Desulfotomaculum PBE Medium prepares Solution A from 2 g "
    "peptone, 1 g beef extract, 2 g MgSO4 x 7H2O, 1.5 g Na2SO4, 0.1 g CaCl2, "
    "and 900 ml distilled water, then autoclaves it under an N2 gas "
    "atmosphere. To complete the medium, 10 ml of autoclaved 5% K2HPO4, "
    "70 ml of autoclaved 5% sodium lactate, 10 ml of filter-sterilized 4% "
    "Fe(NH4)2(SO4)2 x 6H2O, and 10 ml of filter-sterilized 1% sodium "
    "ascorbate are added aseptically and anaerobically per liter. JCM, TOGO, "
    "and MediaDive do not report a final pH."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Mix Solution A components and autoclave under an N2 gas atmosphere."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Aseptically and anaerobically add 10 ml/L autoclaved 5% K2HPO4 "
            "solution, 70 ml/L autoclaved 5% sodium lactate solution, 10 ml/L "
            "filter-sterilized 4% Fe(NH4)2(SO4)2 x 6H2O solution, and "
            "10 ml/L filter-sterilized 1% sodium ascorbate solution."
        ),
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": (
        "Autoclave the Solution A base under N2. Separately autoclave the "
        "5% K2HPO4 and 5% sodium lactate stocks, and filter-sterilize the "
        "4% Fe(NH4)2(SO4)2 x 6H2O and 1% sodium ascorbate stocks."
    ),
}


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
    source: str,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    if grounding[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(source: str) -> list[dict[str, Any]]:
    return [
        _component(
            "Peptone",
            "2.0",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 2.0 g/L peptone.",
        ),
        _component(
            "Beef extract",
            "1.0",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 1.0 g/L beef extract.",
        ),
        _component("MgSO4 x 7H2O", "2.0", "G_PER_L", source=source),
        _component("Na2SO4", "1.5", "G_PER_L", source=source),
        _component("CaCl2", "0.1", "G_PER_L", source=source),
        _component("Distilled water", "900.0", "ML_PER_L", source=source),
        _component(
            "N2",
            "variable",
            "VARIABLE",
            source=source,
            notes=f"{source} uses N2 as the gas atmosphere for autoclaving.",
        ),
    ]


def _stock_solution(
    preferred_term: str,
    volume: str,
    compound: str,
    percent: str,
    source: str,
    *,
    preparation_notes: str,
) -> dict[str, Any]:
    notes = f"{source} adds {volume} ml/L {preferred_term}."
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": volume, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": [
            _component(
                compound,
                percent,
                "PERCENT_W_V",
                source=source,
                notes=f"{source} specifies {preferred_term} as {percent}% w/v.",
            )
        ],
        "preparation_notes": preparation_notes,
    }


def _solutions(source: str) -> list[dict[str, Any]]:
    return [
        _stock_solution(
            "5% K2HPO4 solution",
            "10.0",
            "K2HPO4",
            "5.0",
            source,
            preparation_notes="Autoclave before anaerobic addition.",
        ),
        _stock_solution(
            "5% Sodium lactate solution",
            "70.0",
            "Sodium lactate",
            "5.0",
            source,
            preparation_notes="Autoclave before anaerobic addition.",
        ),
        _stock_solution(
            "4% Fe(NH4)2(SO4)2 x 6H2O solution",
            "10.0",
            "Fe(NH4)2(SO4)2 x 6H2O",
            "4.0",
            source,
            preparation_notes="Filter-sterilize before anaerobic addition.",
        ),
        _stock_solution(
            "1% Sodium ascorbate solution",
            "10.0",
            "Sodium ascorbate",
            "1.0",
            source,
            preparation_notes="Filter-sterilize before anaerobic addition.",
        ),
    ]


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


def _solution_signatures(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signatures: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
        signatures.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), f"{label} composition"),
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
        raise ValueError(f"expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"expected media term {EXPECTED_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("target ingredient signature drifted")
    if _solution_signatures(doc.get("solutions"), "solutions") not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError("target solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"expected {EXPECTED_PARENT_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"expected media term {EXPECTED_PARENT_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_PARENT_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("parent ingredient signature drifted")
    if _solution_signatures(doc.get("solutions"), "solutions") not in (
        (),
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError("parent solution signature drifted")


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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "has_unmapped_ingredients",
        "incomplete_composition",
        "needs_manual_curation",
    ):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
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


def _append_curation_event(doc: dict[str, Any], *, action: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(REFERENCES),
        "notes": RECIPE_NOTES,
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


def _ensure_child_link(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    filtered: list[Any] = []
    inserted = False
    for child in children:
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID or child.get("path") == TOGO_CHILD["path"]:
            if not inserted:
                filtered.append(copy.deepcopy(TOGO_CHILD))
                inserted = True
            continue
        filtered.append(child)

    if not inserted:
        filtered.append(copy.deepcopy(TOGO_CHILD))
    doc["variant_children"] = filtered


def _repair_common(
    doc: dict[str, Any],
    *,
    source: str,
    action: str,
) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired["ingredients"] = _ingredients(source)
    _put_after(repaired, "solutions", _solutions(source), "ingredients")
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired, action=action)
    return repaired


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = _repair_common(doc, source=TOGO_SOURCE, action=ACTION)
    _put_after(repaired, "parent_media", copy.deepcopy(PARENT_MEDIA), "references")
    _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        [VARIANT_MODIFICATIONS],
        "variant_relationship",
    )
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = _repair_common(doc, source=PARENT_SOURCE, action=PARENT_ACTION)
    _ensure_child_link(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target = normalized / TARGET
    parent = normalized / PARENT
    return {
        target: repair_target(_load(target)),
        parent: repair_parent(_load(parent)),
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
