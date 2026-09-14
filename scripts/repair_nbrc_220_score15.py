#!/usr/bin/env python3
"""Repair the score-15 NBRC Medium 220 TOGO import."""

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
TARGET = Path("bacterial/togo_medium_m1448.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:007988"
EXPECTED_MEDIA_TERM = "TOGO:M1448"

CURATOR = "repair_nbrc_220_score15.py"
ACTION = "RESOLVED_NBRC_220_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1448 = "https://togomedium.org/medium/M1448"
NBRC_220 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=220"
SOURCE = "NBRC Medium 220"

YEAST_EXTRACT = "Yeast extract"
BACTO_TRYPTONE = "Bacto Tryptone (Difco)"
SODIUM_ACETATE = "Sodium acetate"
DISTILLED_WATER = "Distilled water"
AGAR_IF_NEEDED = "Agar (if needed)"
FARM_SOIL = "Farm soil"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

LEGACY_INGREDIENTS: tuple[Component, ...] = (
    (DISTILLED_WATER, "951.0", "G_PER_L"),
    (YEAST_EXTRACT, "2", "G_PER_L"),
    (SODIUM_ACETATE, "1", "G_PER_L"),
    (AGAR_IF_NEEDED, "15", "G_PER_L"),
    (BACTO_TRYPTONE, "1", "G_PER_L"),
    ("farm soil", "400", "G_PER_L"),
)

FINAL_INGREDIENTS: tuple[Component, ...] = (
    (YEAST_EXTRACT, "2", "G_PER_L"),
    (BACTO_TRYPTONE, "1", "G_PER_L"),
    (SODIUM_ACETATE, "1", "G_PER_L"),
    (DISTILLED_WATER, "950", "ML_PER_L"),
    (AGAR_IF_NEEDED, "15", "G_PER_L"),
)

SOIL_EXTRACT_COMPOSITION: tuple[Component, ...] = (
    (FARM_SOIL, "400", "G_PER_L"),
    (DISTILLED_WATER, "1000", "ML_PER_L"),
)

LEGACY_SOLUTIONS: tuple[SolutionSignature, ...] = (("Soil extract*", "50", "G_PER_L", ()),)
FINAL_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("Soil extract", "50", "ML_PER_L", SOIL_EXTRACT_COMPOSITION),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    AGAR_IF_NEEDED: ("CHEBI:2509", "agar"),
    DISTILLED_WATER: ("CHEBI:15377", "water"),
    SODIUM_ACETATE: ("CHEBI:32954", "sodium acetate"),
}
PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    AGAR_IF_NEEDED: ("SOLIDIFYING_AGENT",),
}
UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}
REFERENCES = (TOGO_M1448, NBRC_220)

RECIPE_NOTES = (
    "TOGO M1448 imports NBRC Medium 220, which lists 2 g/L Yeast extract, "
    "1 g/L Bacto Tryptone (Difco), 1 g/L Sodium acetate, 50 ml/L Soil "
    "extract, 950 ml/L Distilled water, and 15 g/L Agar if needed. The "
    "final pH is 7.4. Soil extract is prepared by autoclaving 400 g farm "
    "soil suspended in 1 L distilled water for 30 min, then removing solids "
    "by filtration."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Suspend 400 g farm soil in 1 L distilled water and autoclave "
            "for 30 min to prepare Soil extract."
        ),
    },
    {
        "step_number": 2,
        "action": "FILTER",
        "description": "Remove solids by filtration to prepare Soil extract.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "Combine 2 g/L Yeast extract, 1 g/L Bacto Tryptone (Difco), "
            "1 g/L Sodium acetate, 50 ml/L Soil extract, and 950 ml/L "
            "Distilled water."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": "Add 15 g/L agar when solid NBRC Medium 220 is needed.",
    },
    {
        "step_number": 5,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.4.",
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _put_after(doc: dict[str, Any], key: str, value: Any, after_key: str) -> None:
    if key in doc:
        doc[key] = value
        return

    rebuilt: dict[str, Any] = {}
    placed = False
    for existing_key, existing_value in doc.items():
        rebuilt[existing_key] = existing_value
        if existing_key == after_key:
            rebuilt[key] = value
            placed = True
    if not placed:
        rebuilt[key] = value

    doc.clear()
    doc.update(rebuilt)


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
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signatures.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), f"{label} composition"),
            )
        )
    return tuple(signatures)


def _notes(preferred_term: str, value: str, unit: str) -> str:
    if preferred_term == BACTO_TRYPTONE:
        return (
            f"{SOURCE} lists {value} {UNIT_LABELS[unit]} Bacto Tryptone "
            "from Difco; this commercial digest is retained as an opaque "
            "complex component."
        )
    if preferred_term == AGAR_IF_NEEDED:
        return f"{SOURCE} lists {value} {UNIT_LABELS[unit]} agar if needed."
    return f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}."


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes or _notes(preferred_term, value, unit),
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles is not None:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


def _ingredients() -> list[dict[str, Any]]:
    return [_component(name, value, unit) for name, value, unit in FINAL_INGREDIENTS]


def _soil_extract() -> dict[str, Any]:
    return {
        "preferred_term": "Soil extract",
        "concentration": {"value": "50", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds 50 ml/L Soil extract to the main liter.",
        "preparation_notes": (
            "Suspend 400 g farm soil in 1 L distilled water, autoclave for "
            "30 min, and remove solids by filtration."
        ),
        "composition": [
            _component(
                FARM_SOIL,
                "400",
                "G_PER_L",
                notes=(
                    f"{SOURCE} prepares Soil extract from 400 g farm soil "
                    "suspended in 1 L Distilled water."
                ),
            ),
            _component(
                DISTILLED_WATER,
                "1000",
                "ML_PER_L",
                notes=f"{SOURCE} prepares Soil extract with 1 L Distilled water.",
            ),
        ],
    }


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in {LEGACY_INGREDIENTS, FINAL_INGREDIENTS}:
        raise ValueError(f"{TARGET}: ingredient signature drifted to {ingredient_signature!r}")

    solution_signatures = _solution_signatures(doc.get("solutions"), "solutions")
    if solution_signatures not in {LEGACY_SOLUTIONS, FINAL_SOLUTIONS}:
        raise ValueError(f"{TARGET}: solution signature drifted to {solution_signatures!r}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag for flag in flags if flag not in {"incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Curated TOGO:M1448 from TOGO and NBRC Medium 220; corrected "
            "the Distilled water and Soil extract volume units, moved farm "
            "soil to the source-specific nested Soil extract, added pH 7.4, "
            "grounded Sodium acetate, Distilled water, and agar, and "
            "removed the false mediadive.solution:5555 Soil extract link."
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
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.4, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    _put_after(repaired, "solutions", [_soil_extract()], "ingredients")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "solutions")
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
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
    for path, doc in sorted(plans.items()):
        changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        if args.apply and changed:
            write_record(path, doc)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
