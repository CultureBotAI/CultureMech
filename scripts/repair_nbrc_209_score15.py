#!/usr/bin/env python3
"""Repair the score-15 NBRC Medium 209 TOGO import."""

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
TARGET = Path("bacterial/togo_medium_m1444.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:007984"
EXPECTED_MEDIA_TERM = "TOGO:M1444"

CURATOR = "repair_nbrc_209_score15.py"
ACTION = "RESOLVED_NBRC_209_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1444 = "https://togomedium.org/medium/M1444"
NBRC_209 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=209"
SOURCE = "NBRC Medium 209"
SI_MEDIUM_SUPPLIER = "Nippon Jozo Kyokai, Tokyo"

DISTILLED_WATER = "Distilled water"
ETHYL_ALCOHOL = "Ethyl alcohol"
SI_MEDIUM = "SI Medium Dehydrated"

Component = tuple[str, str, str]

LEGACY_INGREDIENTS: tuple[Component, ...] = ((DISTILLED_WATER, "900", "G_PER_L"),)
LEGACY_SOLUTIONS: tuple[Component, ...] = (
    ("Ethyl alcohol**", "100", "G_PER_L"),
    ("SI Medium Dehydrated*", "50", "G_PER_L"),
)
FINAL_INGREDIENTS: tuple[Component, ...] = (
    (SI_MEDIUM, "50", "G_PER_L"),
    (ETHYL_ALCOHOL, "100", "ML_PER_L"),
    (DISTILLED_WATER, "900", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    DISTILLED_WATER: ("CHEBI:15377", "water"),
    ETHYL_ALCOHOL: ("CHEBI:16236", "ethanol"),
}
UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}
REFERENCES = (TOGO_M1444, NBRC_209)

RECIPE_NOTES = (
    "TOGO M1444 imports NBRC Medium 209: SI Medium Dehydrated from Nippon "
    "Jozo Kyokai, ethyl alcohol, and 900 ml distilled water. NBRC footnotes "
    "the ethanol addition: sterilize it by filtration and add it to "
    "autoclaved SI medium."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": ("Autoclave 50 g/L SI Medium Dehydrated in 900 ml/L distilled water."),
    },
    {
        "step_number": 2,
        "action": "FILTER_STERILIZE",
        "description": "Sterilize 100 ml/L ethyl alcohol by filtration.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": ("Add the filter-sterilized ethyl alcohol to the autoclaved SI medium."),
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


def _notes(preferred_term: str, value: str, unit: str) -> str:
    if preferred_term == SI_MEDIUM:
        return (
            f"{SOURCE} lists {value} {UNIT_LABELS[unit]} SI Medium Dehydrated "
            f"from {SI_MEDIUM_SUPPLIER}; this dehydrated commercial medium is "
            "retained as an opaque complex component."
        )
    if preferred_term == ETHYL_ALCOHOL:
        return (
            f"{SOURCE} lists {value} {UNIT_LABELS[unit]} ethyl alcohol; the "
            "source footnote says to sterilize it by filtration and add it to "
            "SI medium sterilized by autoclaving."
        )
    if preferred_term == DISTILLED_WATER:
        return f"{SOURCE} lists {value} {UNIT_LABELS[unit]} distilled water."
    return f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}."


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": _notes(preferred_term, value, unit),
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients() -> list[dict[str, Any]]:
    return [_component(name, value, unit) for name, value, unit in FINAL_INGREDIENTS]


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in {LEGACY_INGREDIENTS, FINAL_INGREDIENTS}:
        raise ValueError(f"{TARGET}: ingredient signature drifted to {ingredient_signature!r}")

    solution_signature = _signature(doc.get("solutions"), "solutions")
    if solution_signature and solution_signature != LEGACY_SOLUTIONS:
        raise ValueError(f"{TARGET}: solution signature drifted to {solution_signature!r}")


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
            "Curated TOGO:M1444 from TOGO and NBRC Medium 209; moved the SI "
            "Medium Dehydrated and ethyl alcohol rows out of empty solution "
            "wrappers, corrected volume rows to ml/L, grounded ethanol and "
            "water, and added autoclave and filter-sterilization steps."
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
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
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
