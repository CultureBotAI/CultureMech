#!/usr/bin/env python3
"""Repair TOGO M2215 PPLO broth."""

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
TARGET = Path("bacterial/TOGO_M2215_PPLO_broth.yaml")
EXPECTED_ID = "CultureMech:008805"
EXPECTED_MEDIA_TERM = "TOGO:M2215"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2215_score15.py"
ACTION = "RESOLVED_TOGO_M2215_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M2215 = "https://togomedium.org/medium/M2215"

SOURCE = "TOGO M2215"
TITLE = "PPLO broth"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("1% (w/v) Phenol red", "4", "G_PER_L"),
    ("25% (w/v) Glucose", "10", "G_PER_L"),
    ("Distilled water", "1", "G_PER_L"),
    ("Horse serum", "200", "G_PER_L"),
    ("Ampicillin", "120", "G_PER_L"),
    ("Salmon sperm DNA (Sigma)", "0.2", "G_PER_L"),
    ("PPLO broth powder (Difco)", "22.5", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("Horse serum", "200.0", "ML_PER_L"),
    ("Ampicillin", "120.0", "MG_PER_L"),
    ("Salmon sperm DNA (Sigma)", "0.2", "G_PER_L"),
    ("PPLO broth powder (Difco)", "22.5", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("IsoVitaleX solution (Becton Dickinson)", "5", "G_PER_L", ()),
)

PHENOL_RED_SIGNATURE: tuple[Component, ...] = (
    ("Phenol red", "1.0", "PERCENT_W_V"),
)

GLUCOSE_SIGNATURE: tuple[Component, ...] = (
    ("Glucose", "25.0", "PERCENT_W_V"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("1% (w/v) Phenol red", "4.0", "ML_PER_L", PHENOL_RED_SIGNATURE),
    ("25% (w/v) Glucose", "10.0", "ML_PER_L", GLUCOSE_SIGNATURE),
    ("IsoVitaleX solution (Becton Dickinson)", "5.0", "ML_PER_L", ()),
)

REFERENCES = (TOGO_M2215,)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Ampicillin": ("CHEBI:28971", "ampicillin"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Phenol red": ("CHEBI:31991", "phenol red"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
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
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes or f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Distilled water",
        "1.0",
        "L",
        notes=f"{SOURCE} lists 1 L distilled water.",
    ),
    _component(
        "Horse serum",
        "200.0",
        "ML_PER_L",
        notes=(
            f"{SOURCE} lists 200 ml/L horse serum; this serum is retained as "
            "an opaque complex component."
        ),
    ),
    _component("Ampicillin", "120.0", "MG_PER_L"),
    _component(
        "Salmon sperm DNA (Sigma)",
        "0.2",
        "G_PER_L",
        notes=(
            f"{SOURCE} lists 0.2 g/L Salmon sperm DNA from Sigma; this "
            "commercial biological product is retained as an opaque complex "
            "component."
        ),
    ),
    _component(
        "PPLO broth powder (Difco)",
        "22.5",
        "G_PER_L",
        notes=(
            f"{SOURCE} lists 22.5 g/L PPLO broth powder from Difco; the "
            "catalog broth is not reducible to one ChEBI molecule."
        ),
    ),
)


def _stock_solution(
    preferred_term: str,
    value: str,
    signature: tuple[Component, ...],
    *,
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": notes,
        "composition": [
            _component(
                component,
                amount,
                unit,
                notes=f"{SOURCE} identifies the stock as {amount} {UNIT_LABELS[unit]} {component}.",
            )
            for component, amount, unit in signature
        ],
    }


SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock_solution(
        "1% (w/v) Phenol red",
        "4.0",
        PHENOL_RED_SIGNATURE,
        notes=f"{SOURCE} lists 4 ml/L 1% (w/v) Phenol red.",
    ),
    _stock_solution(
        "25% (w/v) Glucose",
        "10.0",
        GLUCOSE_SIGNATURE,
        notes=f"{SOURCE} lists 10 ml/L 25% (w/v) Glucose.",
    ),
    {
        "preferred_term": "IsoVitaleX solution (Becton Dickinson)",
        "concentration": {"value": "5.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            f"{SOURCE} lists 5 ml/L IsoVitaleX solution from Becton "
            "Dickinson; this commercial enrichment is retained as an opaque "
            "complex component."
        ),
        "composition": [],
    },
)

NOTES = (
    "TOGO M2215 lists PPLO broth as a growth medium containing, per liter, "
    "22.5 g PPLO broth powder from Difco, 0.2 g Salmon sperm DNA from Sigma, "
    "200 ml horse serum, 5 ml IsoVitaleX solution from Becton Dickinson, "
    "10 ml 25% (w/v) Glucose, 4 ml 1% (w/v) Phenol red, 120 mg Ampicillin, "
    "and 1 L distilled water. The TOGO record does not state pH, temperature, "
    "or sterilization conditions."
)


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
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(
            f"{TARGET}: solution signature drifted from "
            f"{IMPORTED_SOLUTION_SIGNATURES!r} to {solution_signatures!r}"
        )


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


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected ml/L and mg/L import artifacts, moved the "
            "disclosed glucose and phenol-red stocks into solutions, and "
            "kept commercial or biological complex inputs unmapped."
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
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired.pop("preparation_steps", None)
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
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
