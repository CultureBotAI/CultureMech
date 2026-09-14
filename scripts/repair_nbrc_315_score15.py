#!/usr/bin/env python3
"""Repair the score-15 NBRC Medium 315 TOGO import."""

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
TARGET = Path("bacterial/togo_medium_m1528.yaml")
PARENT = Path("bacterial/TOGO_M1524_Todd_Hewitt_Medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:008074"
EXPECTED_PARENT_ID = "CultureMech:008070"
EXPECTED_MEDIA_TERM = "TOGO:M1528"
EXPECTED_PARENT_MEDIA_TERM = "TOGO:M1524"

CURATOR = "repair_nbrc_315_score15.py"
ACTION = "RESOLVED_NBRC_315_SCORE15"
LINK_ACTION = "LINKED_NBRC_315_TODD_HEWITT_VARIANT"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1528 = "https://togomedium.org/medium/M1528"
NBRC_315 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=315"
SOURCE = "NBRC Medium 315"
PH_VALUE = 7.3

BACTO_TODD_HEWITT = "Bacto Todd Hewitt Broth (Difco)"
HORSE_SERUM = "Horse serum"
DISTILLED_WATER = "Distilled water"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

LEGACY_INGREDIENTS: tuple[Component, ...] = (
    (DISTILLED_WATER, "1", "G_PER_L"),
    (BACTO_TODD_HEWITT, "30", "G_PER_L"),
)

LEGACY_SOLUTIONS: tuple[SolutionSignature, ...] = (("Horse serum*", "5", "G_PER_L", ()),)

FINAL_INGREDIENTS: tuple[Component, ...] = (
    (BACTO_TODD_HEWITT, "30", "G_PER_L"),
    (HORSE_SERUM, "5", "ML_PER_L"),
    (DISTILLED_WATER, "1.0", "L"),
)
FINAL_SOLUTIONS: tuple[SolutionSignature, ...] = ()

GROUNDINGS: dict[str, tuple[str, str]] = {
    DISTILLED_WATER: ("CHEBI:15377", "water"),
    HORSE_SERUM: ("MICRO:0001235", "Horse serum"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "ML_PER_L": "ml/L",
}
REFERENCES = (TOGO_M1528, NBRC_315)

VARIANT_NOTES = "Adds 5 ml/L filter-sterilized Horse serum to NBRC Medium 311 Todd Hewitt Medium."
PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_PARENT_ID,
    "name": "todd_hewitt_medium",
    "notes": VARIANT_NOTES,
}
TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_ID,
    "name": "togo_medium_m1528",
    "notes": VARIANT_NOTES,
}

RECIPE_NOTES = (
    "TOGO M1528 imports NBRC Medium 315, which lists 30 g/L Bacto "
    "Todd Hewitt Broth (Difco), 5 ml/L Horse serum, and 1 L Distilled "
    "water at pH 7.3. The horse serum is sterilized separately by filtration."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Dissolve 30 g/L Bacto Todd Hewitt Broth (Difco) in 1 L distilled water.",
    },
    {
        "step_number": 2,
        "action": "FILTER_STERILIZE",
        "description": "Sterilize Horse serum separately by filtration.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": "Add 5 ml/L filter-sterilized Horse serum.",
    },
    {
        "step_number": 4,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.3.",
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
    if preferred_term == BACTO_TODD_HEWITT:
        return (
            f"{SOURCE} lists {value} {UNIT_LABELS[unit]} Bacto Todd Hewitt "
            "Broth from Difco; this commercial broth is retained as an "
            "opaque complex component."
        )
    if preferred_term == HORSE_SERUM:
        return (
            f"{SOURCE} lists {value} {UNIT_LABELS[unit]} Horse serum "
            "sterilized separately by filtration."
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

    solution_signatures = _solution_signatures(doc.get("solutions"), "solutions")
    if solution_signatures not in {LEGACY_SOLUTIONS, FINAL_SOLUTIONS}:
        raise ValueError(f"{TARGET}: solution signature drifted to {solution_signatures!r}")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"{PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")


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
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    repaired.pop("solutions", None)
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "media_term")
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(
        repaired,
        action=ACTION,
        notes=(
            "Curated TOGO:M1528 from TOGO and NBRC Medium 315; corrected "
            "Distilled water from a mass-like 1 g/L import to 1 L, moved "
            "Horse serum from a migrated G_PER_L solution to a 5 ml/L "
            "filter-sterilized ingredient, added pH 7.3, grounded Horse "
            "serum and water, and retained Bacto Todd Hewitt Broth as a "
            "sourced opaque component."
        ),
    )
    repaired["parent_media"] = copy.deepcopy(PARENT_MEDIA)
    repaired["variant_relationship"] = "SUPPLEMENTED_VARIANT"
    repaired["variant_modifications"] = [VARIANT_NOTES]
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    _ensure_variant_child(repaired)
    _append_curation_event(
        repaired,
        action=LINK_ACTION,
        notes="Linked NBRC Medium 315 as a 5 ml/L horse-serum Todd Hewitt variant.",
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
