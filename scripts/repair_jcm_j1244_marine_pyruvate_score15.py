#!/usr/bin/env python3
"""Repair specialized MediaDive/JCM J1244 marine broth with pyruvate."""

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
TARGET = Path("specialized/marine_broth_2216_with_pyruvate.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_j1244_marine_pyruvate_score15.py"
ACTION = "RESOLVED_JCM_J1244_MARINE_PYRUVATE_SCORE15"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

EXPECTED_ID = "CultureMech:015395"
EXPECTED_MEDIA_TERM = "mediadive.medium:J1244"
MEDIADIVE_PAGE = "https://mediadive.dsmz.de/medium/J1244"
MEDIADIVE_REST = "https://mediadive.dsmz.de/rest/medium/J1244"
SOURCE = "MediaDive JCM Medium J1244"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Marine broth 2216", "37.0297", "G_PER_L"),
    ("Sodium pyruvate", "10", "G_PER_L"),
)
FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Marine broth 2216 (BD-Difco)", "37.4", "G_PER_L"),
    ("Distilled water", "1000", "ML_PER_L"),
)
FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("1.0 M Sodium pyruvate solution", "10.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Sodium pyruvate": ("CHEBI:50144", "sodium pyruvate"),
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _grounded_component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    grounding = GROUNDINGS[preferred_term]
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "term": _term(*grounding),
        "mediaingredientmech_chebi_term": _term(*grounding),
    }


def _ingredient(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
    }
    if preferred_term == "Marine broth 2216 (BD-Difco)":
        row["notes"] = (
            f"{SOURCE} lists 37.4 g Marine broth 2216 with the BD-Difco attribute; "
            "left ungrounded as an undefined commercial broth."
        )
    else:
        row["notes"] = f"{SOURCE} lists 1000 mL distilled water."
        row.update(_grounded_component(preferred_term, value, unit))
    return row


def _solution() -> dict[str, Any]:
    return {
        "preferred_term": "1.0 M Sodium pyruvate solution",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "notes": (
            f"{SOURCE} adds 10 mL autoclaved 1.0 M Sodium pyruvate solution after "
            "cooling the autoclaved Marine broth 2216 base."
        ),
        "composition": [_grounded_component("Sodium pyruvate", "1.0", "MOLAR")],
    }


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
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
        raise ValueError(f"{TARGET}: expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")
    if _signature(doc.get("solutions"), "solutions") not in (
        (),
        FINAL_SOLUTION_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


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

    obsolete = {"incomplete_composition", "needs_manual_curation"}
    flags = [flag for flag in flags if flag not in obsolete]
    flags.extend(("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in (MEDIADIVE_PAGE, MEDIADIVE_REST):
        if reference not in existing:
            references.append({"reference": reference})


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": MEDIADIVE_REST,
        "notes": (
            "Rebuilt J1244 from MediaDive's JCM payload by restoring the 1000 mL "
            "distilled water row and modeling 10 mL of 1.0 M sodium pyruvate as an "
            "autoclaved stock solution added after cooling."
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
    repaired["notes"] = (
        "MediaDive JCM Medium J1244 lists 37.4 g Marine broth 2216 (BD-Difco), "
        "1000 mL distilled water, and pH 8.0, then adds 10 mL autoclaved 1.0 M "
        "sodium pyruvate solution after cooling."
    )
    repaired["ingredients"] = [
        _ingredient("Marine broth 2216 (BD-Difco)", "37.4", "G_PER_L"),
        _ingredient("Distilled water", "1000", "ML_PER_L"),
    ]
    _put_after(repaired, "solutions", [_solution()], "ingredients")
    repaired["preparation_steps"] = [
        {
            "step_number": 1,
            "action": "MIX",
            "description": "Suspend 37.4 g Marine broth 2216 (BD-Difco) in 1000 mL water.",
        },
        {"step_number": 2, "action": "ADJUST_PH", "description": "Adjust pH to 8.0."},
        {"step_number": 3, "action": "AUTOCLAVE", "description": "Autoclave the base."},
        {
            "step_number": 4,
            "action": "MIX",
            "description": (
                "After cooling, add 10 mL autoclaved 1.0 M sodium pyruvate solution."
            ),
        },
        {
            "step_number": 5,
            "action": "FILTER",
            "description": (
                "Remove any precipitate yielded after autoclaving by filtration, "
                "if necessary."
            ),
        },
    ]
    _put_after(repaired, "sterilization", {"method": "AUTOCLAVE"}, "preparation_steps")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
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
