#!/usr/bin/env python3
"""Repair TOGO M2785 Hayflick medium."""

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
TARGET = Path("bacterial/hayflick_medium.yaml")
EXPECTED_ID = "CultureMech:009333"
EXPECTED_MEDIA_TERM = "TOGO:M2785"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2785_hayflick_score15.py"
ACTION = "RESOLVED_TOGO_M2785_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2785 = "https://togomedium.org/medium/M2785"
TOGO_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2785"
SOURCE = "TOGO M2785"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Yeast Extract", "19.6", "G_PER_L"),
    ("Horse serum", "157", "G_PER_L"),
    ("Phenol Red", "24", "G_PER_L"),
    ("DI Water", "843", "G_PER_L"),
    ("DNA sodium salt (Sigma, D1501)", "0.24", "G_PER_L"),
    ("PPLO", "17.7", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Yeast Extract", "19.6", "G_PER_L"),
    ("Horse serum", "157.0", "ML_PER_L"),
    ("Phenol Red", "24.0", "MG_PER_L"),
    ("Deionized water", "843.0", "ML_PER_L"),
    ("DNA sodium salt (Sigma, D1501)", "0.24", "G_PER_L"),
    ("Difco PPLO Broth", "17.7", "G_PER_L"),
)

REFERENCES = (TOGO_M2785, TOGO_API)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Deionized water": ("CHEBI:15377", "water"),
    "Phenol Red": ("CHEBI:31991", "phenol red"),
    "Yeast Extract": ("FOODON:03315426", "yeast extract"),
}

COMPONENT_NOTES: dict[str, str] = {
    "Yeast Extract": "TOGO M2785 lists 19.6 g/L Yeast Extract.",
    "Horse serum": (
        "TOGO M2785 lists 157 ml/L Horse serum, added aseptically after the "
        "autoclaved base cools to 55 C; this complex serum is retained as an "
        "opaque component."
    ),
    "Phenol Red": "TOGO M2785 lists 24 mg/L Phenol Red.",
    "Deionized water": "TOGO M2785 lists 843 ml/L DI Water.",
    "DNA sodium salt (Sigma, D1501)": (
        "TOGO M2785 lists 0.24 g/L DNA sodium salt from Sigma catalog D1501; "
        "this calf-thymus DNA product is retained as an opaque component."
    ),
    "Difco PPLO Broth": (
        "TOGO M2785 lists 17.7 g/L PPLO, annotated by TOGO as Difco PPLO "
        "Broth; this catalog broth is retained as an opaque component."
    ),
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Combine all ingredients except horse serum.",
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust to pH 7.8 +/- 0.2.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the base at 121 C and let the medium cool to 55 C.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": "Aseptically add horse serum and dispense as required.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": "TOGO M2785 autoclaves the base at 121 C before aseptic horse-serum addition.",
}

NOTES = (
    "TOGO M2785 lists Hayflick medium as, per liter, 19.6 g Yeast Extract, "
    "17.7 g PPLO annotated as Difco PPLO Broth, 0.24 g DNA sodium salt "
    "from Sigma D1501, 24 mg Phenol Red, 843 ml DI Water, and 157 ml "
    "Horse serum. The source adjusts the base to pH 7.8 +/- 0.2, "
    "autoclaves it at 121 C, cools it to 55 C, and then adds Horse serum "
    "aseptically."
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
        "notes": COMPONENT_NOTES[preferred_term],
    }

    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(
    _component(name, value, unit)
    for name, value, unit in FINAL_INGREDIENT_SIGNATURE
)


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
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

    pair = (
        _signature(doc.get("ingredients"), "ingredients"),
        _signature(doc.get("solutions"), "solutions"),
    )
    allowed = (
        (IMPORTED_INGREDIENT_SIGNATURE, ()),
        (FINAL_INGREDIENT_SIGNATURE, ()),
    )
    if pair not in allowed:
        raise ValueError(f"{TARGET}: recipe signature drifted to {pair!r}")


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
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected the ml/L and mg/L import artifacts, added the "
            "source pH and temperature, grounded yeast extract, phenol red, and "
            "water, and kept Horse serum, DNA sodium salt, and Difco PPLO Broth "
            "unmapped as complex inputs."
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
    _put_after(repaired, "ph_range", {"min": 7.6, "max": 8.0}, "physical_state")
    _put_after(repaired, "temperature_value", 37.0, "ph_range")
    repaired.pop("ph_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["sterilization"] = copy.deepcopy(STERILIZATION)
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
