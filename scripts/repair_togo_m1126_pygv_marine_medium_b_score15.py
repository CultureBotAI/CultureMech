#!/usr/bin/env python3
"""Repair TOGO M1126 liquid PYGV Marine Medium B."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import repair_togo_m1127_score15 as m1127  # noqa: E402
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = Path("bacterial/pygv_marine_medium_b.yaml")
EXPECTED_ID = "CultureMech:007647"
EXPECTED_MEDIA_TERM = "TOGO:M1126"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1126_pygv_marine_medium_b_score15.py"
ACTION = "RESOLVED_TOGO_M1126_PYGV_MARINE_B_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1126 = "https://togomedium.org/medium/M1126"
JCM_1059 = m1127.JCM_1059
TOGO_M299 = m1127.TOGO_M299
JCM_304 = m1127.JCM_304
JCM_149 = m1127.JCM_149

SOURCE = "TOGO M1126 / JCM Medium 1059"
STOCK_SOURCE = m1127.STOCK_SOURCE
METALS_44_SOURCE = m1127.METALS_44_SOURCE
TITLE = "PYGV Marine Medium (B)"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "710", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.25", "G_PER_L"),
    ("Bacto peptone (BD-Difco)", "0.25", "G_PER_L"),
    ("KOH", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Bacto peptone (BD-Difco)", "0.25", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.25", "G_PER_L"),
    ("Distilled water", "710.0", "ML_PER_L"),
    ("KOH", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURES = m1127.IMPORTED_SOLUTION_SIGNATURES
FINAL_SOLUTION_SIGNATURES = m1127.FINAL_SOLUTION_SIGNATURES
REFERENCES = (TOGO_M1126, JCM_1059, TOGO_M299, JCM_304, JCM_149)
GROUNDINGS = m1127.GROUNDINGS


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
    notes: str,
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _listed_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    term: bool = True,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} lists {value} {m1127.UNIT_LABELS[unit]} {preferred_term}.",
        term=term,
    )


def _stock_reference(
    preferred_term: str,
    value: str,
    source: str,
    notes: str,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        "ML_PER_L",
        source=source,
        notes=notes,
        term=False,
    )


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _listed_component("Bacto peptone (BD-Difco)", "0.25", "G_PER_L", source=SOURCE, term=False),
    _listed_component("Yeast extract (BD-Difco)", "0.25", "G_PER_L", source=SOURCE, term=False),
    _listed_component("Distilled water", "710.0", "ML_PER_L", source=SOURCE),
    _component(
        "KOH",
        "variable",
        "VARIABLE",
        source=SOURCE,
        notes=(
            "JCM Medium 1059 adjusts the medium to pH 7.2-7.4 with sterile KOH, "
            "if necessary."
        ),
    ),
)


def _solution(
    preferred_term: str,
    dose: str,
    composition: tuple[Component, ...],
    source: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": dose, "unit": "ML_PER_L"},
        "source": SOURCE if source == STOCK_SOURCE else source,
        "notes": f"JCM Medium 1059 adds {dose} ml/L {preferred_term}.",
        "composition": [
            _listed_component(name, value, unit, source=source, term=name in GROUNDINGS)
            for name, value, unit in composition
        ],
    }


SOLUTIONS: tuple[dict[str, Any], ...] = (
    _solution("Mineral salt solution", "20.0", m1127.MINERAL_SALT_SIGNATURE, STOCK_SOURCE),
    _solution("2.5% Glucose solution", "10.0", m1127.GLUCOSE_SIGNATURE, SOURCE),
    _solution("Vitamin solution", "10.0", m1127.VITAMIN_SIGNATURE, STOCK_SOURCE),
    _solution("Artificial seawater", "250.0", m1127.SEAWATER_SIGNATURE, STOCK_SOURCE),
)
SOLUTIONS[0]["composition"][5] = _stock_reference(
    "Metals 44",
    "50.0",
    METALS_44_SOURCE,
    "JCM Medium 304 adds 50.0 ml/L Metals 44 from JCM Medium 149.",
)
SOLUTIONS[1]["preparation_notes"] = "Filter-sterilize before aseptic addition."
SOLUTIONS[2]["preparation_notes"] = "Filter-sterilize before aseptic addition."

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix peptone, yeast extract, mineral salt solution, artificial seawater, "
            "and distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "HEAT",
        "description": "Gently heat and bring to a boil.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 degrees C for 15 min.",
    },
    {
        "step_number": 4,
        "action": "COOL",
        "description": "Cool to 45-50 degrees C.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Aseptically add the filter-sterilized glucose solution and vitamin "
            "solution."
        ),
    },
    {
        "step_number": 6,
        "action": "ADJUST_PH",
        "description": "Adjust to pH 7.2-7.4 with sterile KOH, if necessary.",
    },
)

NOTES = (
    "TOGO M1126 records the liquid JCM Medium 1059 PYGV Marine Medium (B) "
    "formulation with Bacto peptone, yeast extract, mineral salt solution from "
    "JCM Medium 304, 2.5% glucose solution, vitamin solution from JCM Medium 304, "
    "artificial seawater from JCM Medium 304, distilled water, and KOH for optional "
    "pH adjustment. JCM 1059 gently heats the base, autoclaves it, cools it to "
    "45-50 degrees C, adds filter-sterilized glucose and vitamin solutions "
    "aseptically, and adjusts pH to 7.2-7.4 with sterile KOH if necessary."
)


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    return m1127._signature(rows, label)


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    return m1127._solution_signatures(doc)


def _source_term_id(doc: dict[str, Any]) -> str:
    return m1127._source_term_id(doc)


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
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": NOTES,
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
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    m1127._put_after(repaired, "ph_range", {"min": 7.2, "max": 7.4}, "physical_state")
    repaired.pop("ph_value", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    m1127._put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    m1127._put_after(
        repaired,
        "sterilization",
        {
            "method": "AUTOCLAVE",
            "temperature": {"value": 121.0, "unit": "CELSIUS"},
            "duration": "15 min",
            "notes": "Filter-sterilize glucose and vitamin solutions separately.",
        },
        "preparation_steps",
    )
    m1127._put_after(repaired, "notes", NOTES, "media_term")
    m1127._ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
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
