#!/usr/bin/env python3
"""Repair the score-15 NBRC Medium 274 TOGO import."""

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
TARGET = Path("bacterial/togo_medium_m1491.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:008036"
EXPECTED_MEDIA_TERM = "TOGO:M1491"

CURATOR = "repair_nbrc_274_score15.py"
ACTION = "RESOLVED_NBRC_274_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1491 = "https://togomedium.org/medium/M1491"
NBRC_274 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=274"
SOURCE = "NBRC Medium 274"

BACTO_TRYPTONE = "Bacto Tryptone (Difco)"
YEAST_EXTRACT = "Yeast extract"
BEEF_EXTRACT = "Beef extract"
SODIUM_ACETATE = "Sodium acetate"
DISTILLED_WATER = "Distilled water"
AGAR_IF_NEEDED = "Agar (if needed)"

Component = tuple[str, str, str]

LEGACY_INGREDIENTS: tuple[Component, ...] = (
    (DISTILLED_WATER, "1", "G_PER_L"),
    (YEAST_EXTRACT, "0.5", "G_PER_L"),
    (SODIUM_ACETATE, "0.2", "G_PER_L"),
    (AGAR_IF_NEEDED, "15", "G_PER_L"),
    (BACTO_TRYPTONE, "0.5", "G_PER_L"),
    (BEEF_EXTRACT, "0.2", "G_PER_L"),
)

FINAL_INGREDIENTS: tuple[Component, ...] = (
    (BACTO_TRYPTONE, "0.5", "G_PER_L"),
    (YEAST_EXTRACT, "0.5", "G_PER_L"),
    (BEEF_EXTRACT, "0.2", "G_PER_L"),
    (SODIUM_ACETATE, "0.2", "G_PER_L"),
    (DISTILLED_WATER, "1.0", "L"),
    (AGAR_IF_NEEDED, "15.0", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    AGAR_IF_NEEDED: ("CHEBI:2509", "agar"),
    DISTILLED_WATER: ("CHEBI:15377", "water"),
    SODIUM_ACETATE: ("CHEBI:32954", "sodium acetate"),
    YEAST_EXTRACT: ("FOODON:03315426", "yeast extract"),
}
PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    AGAR_IF_NEEDED: ("SOLIDIFYING_AGENT",),
}
UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
}
REFERENCES = (TOGO_M1491, NBRC_274)

RECIPE_NOTES = (
    "TOGO M1491 imports NBRC Medium 274, which lists 0.5 g/L Bacto "
    "Tryptone (Difco), 0.5 g/L Yeast extract, 0.2 g/L Beef extract, "
    "0.2 g/L Sodium acetate, 1 L Distilled water, and 15 g/L Agar if "
    "needed. The final pH is 7.2."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Combine 0.5 g/L Bacto Tryptone (Difco), 0.5 g/L Yeast "
            "extract, 0.2 g/L Beef extract, 0.2 g/L Sodium acetate, and "
            "1 L Distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": "Add 15 g/L agar when solid NBRC Medium 274 is needed.",
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.2.",
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
    if preferred_term == AGAR_IF_NEEDED:
        return f"{SOURCE} lists {value} {UNIT_LABELS[unit]} agar if needed."
    if preferred_term in {BACTO_TRYPTONE, BEEF_EXTRACT}:
        return (
            f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}; "
            "this source-disclosed complex component is retained without "
            "an ontology grounding."
        )
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
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles is not None:
        row["physicochemical_roles"] = list(physicochemical_roles)
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
            "Curated TOGO:M1491 from TOGO and NBRC Medium 274; corrected "
            "Distilled water from a mass-like 1 g/L import to 1 L, added "
            "pH 7.2, grounded yeast extract, sodium acetate, water, and "
            "agar, and retained Bacto Tryptone and Beef extract as sourced "
            "unmapped components."
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
    _put_after(repaired, "ph_value", 7.2, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "media_term")
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
