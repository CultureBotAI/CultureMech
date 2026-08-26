#!/usr/bin/env python3
"""Restore JCM 996 as a Vero-cell-conditioned medium.

The JCM source defines the final medium as clarified Vero E6 culture
supernatant. The conditioning medium is IMDM with 10% heat-inactivated fetal
bovine serum. Vero cells are preparation agents removed by centrifugation, not
final-medium ingredients.

Apply mode requires the exact reviewed JCM HTML page and validates the one
available MIM identity against the MediaIngredientMech SSSOM. The MIM object is
NCIT-backed and cannot be encoded in the current ingredient-term CURIE pattern,
so it is retained in notes rather than forced into ``term``. Dry-run is the
default.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
MIM_SSSOM = REPO.parent / "MediaIngredientMech" / "mappings" / "ingredient_mappings.sssom.tsv"
TARGET_PATH = "bacterial/car_bacillus_medium.yaml"
TARGET_ID = "CultureMech:003345"
ACTION = "RESTORED_JCM_996_CONDITIONED_MEDIUM"
TIMESTAMP = "2026-08-25T00:00:00-07:00"
SOURCE_FILE = "JCM_996.html"
SOURCE_HASH = "f34523ccdcd09c53e60a2ebc7b2ab2bde7ded8af0626f0d2b052aaf654e233e2"
SOURCE_URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=996"
FBS_OBJECT = ("NCIT:C113696", "Fetal Bovine Serum")


def _component(
    preferred_term: str,
    value: str,
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "PERCENT_V_V"},
    }
    if notes:
        row["notes"] = notes
    return row


RECIPE: dict[str, Any] = {
    "medium_type": "COMPLEX",
    "composition_type": "UNDEFINED",
    "physical_state": "LIQUID",
    "ingredients": [],
    "solutions": [
        {
            "preferred_term": "Clarified Vero E6 cell culture supernatant fluid",
            "composition": [
                _component(
                    "Iscove's Modified Dulbecco's Medium (IMDM, GlutaMAX)",
                    "90",
                    notes=(
                        "Life Technologies Cat. No. 31980030. No defensible identity "
                        "object is present in the reviewed MIM SSSOM."
                    ),
                ),
                _component(
                    "Fetal bovine serum",
                    "10",
                    notes=(
                        "Heat-inactivate at 56 C for 30 minutes before use. MIM maps "
                        "this label to NCIT:C113696 (Fetal Bovine Serum), but the "
                        "current ingredient-term schema does not admit NCIT CURIEs."
                    ),
                ),
            ],
            "concentration": {"value": "100", "unit": "PERCENT_V_V"},
            "notes": (
                "The final CAR bacillus medium consists entirely of the clarified "
                "supernatant after Vero E6 conditioning."
            ),
        }
    ],
    "preparation_steps": [
        {
            "step_number": 1,
            "action": "HEAT",
            "description": "Heat-inactivate fetal bovine serum at 56 C for 30 minutes.",
        },
        {
            "step_number": 2,
            "action": "MIX",
            "description": "Supplement IMDM (GlutaMAX) with 10% heat-inactivated FBS.",
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": (
                "Incubate Vero E6 cells (ATCC CRL-1586) in the supplemented medium "
                "at 37 C under 5% CO2."
            ),
        },
        {
            "step_number": 4,
            "action": "MIX",
            "description": (
                "After cell cultivation, centrifuge the culture medium and retain "
                "the clarified supernatant fluid."
            ),
        },
        {
            "step_number": 5,
            "action": "MIX",
            "description": (
                "Cultivate the microorganism in the supernatant in the specified "
                "ultra-low-attachment 75 cm2 flask at 37 C under 5% CO2."
            ),
        },
    ],
}

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ingredients",
    "solutions",
    "preparation_steps",
)


def _projection(doc: dict[str, Any]) -> dict[str, Any]:
    return {field: copy.deepcopy(doc[field]) for field in RECIPE_FIELDS if field in doc}


def history_has_action(doc: dict[str, Any]) -> bool:
    return any(
        isinstance(row, dict) and row.get("action") == ACTION
        for row in doc.get("curation_history") or []
    )


def validate_source_file(source_dir: Path) -> None:
    path = source_dir / SOURCE_FILE
    if not path.is_file():
        raise ValueError(f"missing reviewed JCM source file: {path}")
    actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual_hash != SOURCE_HASH:
        raise ValueError(f"{path}: SHA-256 {actual_hash}, expected reviewed {SOURCE_HASH}")


def validate_mim_term(sssom_path: Path) -> None:
    if not sssom_path.is_file():
        raise ValueError(f"missing MediaIngredientMech SSSOM: {sssom_path}")
    with sssom_path.open(encoding="utf-8", newline="") as handle:
        rows = csv.DictReader((line for line in handle if not line.startswith("#")), delimiter="\t")
        objects = {
            (str(row.get("object_id") or ""), str(row.get("object_label") or "")) for row in rows
        }
    if FBS_OBJECT not in objects:
        raise ValueError(f"selected mapping is absent from the MIM SSSOM: {FBS_OBJECT}")


def _source_note() -> str:
    return (
        f"Composition verified against {SOURCE_URL} on 2026-08-25 "
        f"(SHA-256 {SOURCE_HASH})."
    )


def _validate_precondition(doc: dict[str, Any]) -> None:
    if str(doc.get("id") or "") != TARGET_ID:
        raise ValueError(f"{TARGET_PATH}: id {doc.get('id')!r}, expected {TARGET_ID}")
    if doc.get("ingredients") or doc.get("solutions"):
        raise ValueError(f"{TARGET_PATH}: record is no longer composition-empty")
    flags = doc.get("data_quality_flags") or []
    if "incomplete_composition" not in flags or "source_information_unavailable" not in flags:
        raise ValueError(f"{TARGET_PATH}: missing expected pre-repair quality flags")


def _assert_applied(doc: dict[str, Any]) -> None:
    if _projection(doc) != _projection(RECIPE):
        raise ValueError(f"{TARGET_PATH}: applied JCM 996 recipe drifted")
    flags = doc.get("data_quality_flags") or []
    if any(flag in flags for flag in ("incomplete_composition", "source_information_unavailable")):
        raise ValueError(f"{TARGET_PATH}: stale missing-source flag returned")
    if _source_note() not in str(doc.get("notes") or ""):
        raise ValueError(f"{TARGET_PATH}: source verification note is missing")


def repair_document(doc: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    if history_has_action(doc):
        _assert_applied(doc)
        return doc, False
    _validate_precondition(doc)

    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        repaired[field] = copy.deepcopy(RECIPE[field])

    flags = repaired.get("data_quality_flags") or []
    kept_flags = [
        flag
        for flag in flags
        if flag not in {"incomplete_composition", "source_information_unavailable"}
    ]
    if kept_flags:
        repaired["data_quality_flags"] = kept_flags
    else:
        repaired.pop("data_quality_flags", None)

    existing_notes = str(repaired.get("notes") or "").rstrip()
    note = _source_note()
    repaired["notes"] = f"{existing_notes}\n{note}" if existing_notes else note
    history = repaired.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET_PATH}: curation_history is not a list")
    history.append(
        {
            "timestamp": TIMESTAMP,
            "curator": "repair_jcm_car_bacillus.py",
            "action": ACTION,
            "changes": "ingredients 0 -> 0; solutions 0 -> 1",
            "notes": (
                "Represented the final medium as clarified Vero E6-conditioned "
                "IMDM plus 10% FBS. Vero cells remain preparation agents, not final "
                "ingredients; the NCIT-backed FBS identity was verified in the MIM "
                "SSSOM and retained in notes because the schema does not admit it."
            ),
        }
    )
    _assert_applied(repaired)
    return repaired, True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--sssom", type=Path, default=MIM_SSSOM)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    if args.source_dir is not None:
        validate_source_file(args.source_dir)
    elif args.apply:
        raise ValueError("--apply requires --source-dir with the reviewed JCM HTML page")
    validate_mim_term(args.sssom)

    path = args.normalized_dir / TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    repaired, changed = repair_document(doc)
    print(f"{'fix' if changed else 'skip':4s}  {TARGET_PATH}: JCM 996")
    if args.apply and changed:
        write_record(path, repaired)
    verb = "updated" if args.apply else "would update"
    print(f"\n{verb} {int(changed)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
