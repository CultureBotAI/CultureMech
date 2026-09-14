#!/usr/bin/env python3
"""Repair fungal JCM J293 MRS Maltose Medium score-15 import."""

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
TARGET = Path("fungal/mrs_maltose_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_j293_mrs_maltose_score15.py"
ACTION = "RESOLVED_JCM_J293_SCORE15"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

EXPECTED_ID = "CultureMech:010518"
EXPECTED_MEDIA_TERM = "mediadive.medium:J293"

JCM_J293 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=293"
MEDIADIVE_J293 = "https://mediadive.dsmz.de/medium/J293"
MEDIADIVE_J293_REST = "https://mediadive.dsmz.de/rest/medium/J293"
REFERENCES = (MEDIADIVE_J293, MEDIADIVE_J293_REST, JCM_J293)
SOURCE = "MediaDive JCM Medium J293"

Component = tuple[str, str, str]

MRS_BROTH = "Lactobacilli MRS broth (BD-Difco)"
IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Lactobacilli MRS broth", "55", "G_PER_L"),
    ("Maltose", "10", "G_PER_L"),
)
FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (MRS_BROTH, "55", "G_PER_L"),
    ("Maltose", "10", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Maltose": ("CHEBI:17306", "maltose"),
}

NOTES = (
    "MediaDive JCM Medium J293 lists 55 g/L Lactobacilli MRS broth (BD-Difco), "
    "10 g/L Maltose, 1000 mL/L Distilled water, and pH 6.5."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": f"{SOURCE} lists {value} g/L {preferred_term}.",
    }
    if preferred_term == "Distilled water":
        row["notes"] = f"{SOURCE} lists 1000 mL distilled water per 1 L medium."
    elif preferred_term == MRS_BROTH:
        row["notes"] = (
            f"{SOURCE} lists 55 g/L Lactobacilli MRS broth with the BD-Difco "
            "attribute; left ungrounded as an undefined commercial broth."
        )

    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients() -> list[dict[str, Any]]:
    return [
        _ingredient(MRS_BROTH, "55", "G_PER_L"),
        _ingredient("Maltose", "10", "G_PER_L"),
        _ingredient("Distilled water", "1000.0", "ML_PER_L"),
    ]


def _signature(rows: Any) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("ingredients is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("ingredients contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"ingredient {row.get('preferred_term')!r} lacks concentration")
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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"))
    if ingredient_signature not in {IMPORTED_INGREDIENT_SIGNATURE, FINAL_INGREDIENT_SIGNATURE}:
        raise ValueError(f"{TARGET}: ingredient signature drifted to {ingredient_signature!r}")

    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")
    if solutions:
        raise ValueError(f"{TARGET}: unexpected solutions")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag not in {"extracted_from_notes", "incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {
        row.get("reference")
        for row in references
        if isinstance(row, dict) and isinstance(row.get("reference"), str)
    }
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": MEDIADIVE_J293_REST,
        "notes": (
            "Added the missing 1000 mL/L distilled water row from MediaDive JCM "
            "Medium J293 and preserved Lactobacilli MRS broth as an intentionally "
            "ungrounded BD-Difco commercial broth."
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
    _put_after(repaired, "ph_value", 6.5, "physical_state")
    repaired["notes"] = NOTES
    repaired["ingredients"] = _ingredients()
    _put_after(
        repaired,
        "preparation_steps",
        [{"step_number": 1, "action": "ADJUST_PH", "description": "Adjust pH to 6.5."}],
        "ingredients",
    )
    repaired.pop("kg_microbe_match", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
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
