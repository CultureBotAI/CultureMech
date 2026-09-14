#!/usr/bin/env python3
"""Repair TOGO M2125 R2A Medium (DAIGO)."""

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
TARGET = Path("bacterial/r2a_medium_daigo.yaml")
PARENT = Path("bacterial/r2a_broth.yaml")
EXPECTED_ID = "CultureMech:008718"
EXPECTED_PARENT_ID = "CultureMech:003183"
EXPECTED_MEDIA_TERM = "TOGO:M2125"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2125_r2a_daigo_score15.py"
ACTION = "RESOLVED_TOGO_M2125_R2A_DAIGO_SCORE15"
LINK_ACTION = "LINKED_TOGO_M2125_R2A_DAIGO_SCORE15_CHILD"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2125 = "https://togomedium.org/medium/M2125"
NBRC_1455 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1455"
SOURCE = "TOGO M2125 / NBRC Medium 1455"
TITLE = "R2A Medium (DAIGO)"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ('R2A Broth "DAIGO"', "3.2", "G_PER_L"),
    ("Agar (if needed)", "15.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ('R2A Broth \\"DAIGO\\"*', "3.2", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = ()

REFERENCES = (TOGO_M2125, NBRC_1455)

R2A_BROTH = {"id": EXPECTED_PARENT_ID, "label": "R2A Broth"}
AGAR = ("CHEBI:2509", "agar")
WATER = ("CHEBI:15377", "water")

NOTES = (
    "TOGO M2125 imports NBRC Medium 1455 R2A Medium (DAIGO), which lists 3.2 g "
    'R2A Broth "DAIGO", 15 g agar if needed, and 1 L distilled water.'
)

PARENT_NOTES = (
    'Adds 15 g/L agar if needed to 3.2 g/L R2A Broth "DAIGO" premix.'
)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "PHYSICAL_STATE_VARIANT",
    "id": EXPECTED_PARENT_ID,
    "name": "r2a_broth",
    "notes": PARENT_NOTES,
}

CHILD_REFERENCE = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "PHYSICAL_STATE_VARIANT",
    "id": EXPECTED_ID,
    "name": "r2a_medium_daigo",
    "notes": PARENT_NOTES,
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    term: tuple[str, str] | None = None,
    culturemech_term: dict[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        row["mediaingredientmech_chebi_term"] = _term(*term)
    if culturemech_term is not None:
        row["culturemech_term"] = copy.deepcopy(culturemech_term)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        'R2A Broth "DAIGO"',
        "3.2",
        "G_PER_L",
        source=SOURCE,
        notes='TOGO M2125 / NBRC Medium 1455 lists 3.2 g/L R2A Broth "DAIGO".',
        culturemech_term=R2A_BROTH,
    ),
    _ingredient(
        "Agar (if needed)",
        "15.0",
        "G_PER_L",
        source=SOURCE,
        notes="TOGO M2125 / NBRC Medium 1455 lists 15.0 g/L Agar (if needed).",
        term=AGAR,
    ),
    _ingredient(
        "Distilled water",
        "1.0",
        "L",
        source=SOURCE,
        notes="TOGO M2125 / NBRC Medium 1455 lists 1.0 L Distilled water.",
        term=WATER,
    ),
)

PREPARATION_STEPS = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            'Dissolve 3.2 g R2A Broth "DAIGO", and 15 g agar if needed, '
            "in 1 L distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the medium.",
    },
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
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(
            f"{PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}"
        )


def _component_rows(doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        rows.append(solution)
        composition = solution.get("composition") or []
        if isinstance(composition, list):
            rows.extend(row for row in composition if isinstance(row, dict))
    return rows


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")
    if any(_grounded(component) for component in _component_rows(doc)):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")
    if any(not _grounded(component) for component in _component_rows(doc)):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], *, action: str, notes: str) -> None:
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


def _upsert_child(parent: dict[str, Any]) -> None:
    children = parent.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError(f"{PARENT}: variant_children is not a list")
    for index, child in enumerate(children):
        if isinstance(child, dict) and child.get("path") == CHILD_REFERENCE["path"]:
            children[index] = copy.deepcopy(CHILD_REFERENCE)
            break
    else:
        children.append(copy.deepcopy(CHILD_REFERENCE))


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "solutions")
    _put_after(
        repaired,
        "sterilization",
        {"method": "AUTOCLAVE"},
        "preparation_steps",
    )
    _put_after(repaired, "parent_media", copy.deepcopy(PARENT_MEDIA), "references")
    _put_after(repaired, "variant_relationship", "PHYSICAL_STATE_VARIANT", "parent_media")
    _put_after(repaired, "variant_modifications", [PARENT_NOTES], "variant_relationship")
    _put_after(repaired, "notes", NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired, action=ACTION, notes=NOTES)
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    _upsert_child(repaired)
    _append_curation_event(
        repaired,
        action=LINK_ACTION,
        notes=f"Added or refreshed {TARGET} as a physical-state child of {PARENT}.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / TARGET: repair_target(_load(normalized / TARGET)),
        normalized / PARENT: repair_parent(_load(normalized / PARENT)),
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
