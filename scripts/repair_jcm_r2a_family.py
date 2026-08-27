#!/usr/bin/env python3
"""Restore and source-correct the three-record JCM R2A family.

JCM 346 and 1091 were imported without their printed distilled water or default
autoclaving instruction. JCM 1311 retained its delegation to 346 but no usable
composition. This migration restores the pH variant, includes its separately
sterilized 10% sodium carbonate solution without inventing an addition volume,
and keeps all three variant links reciprocal.

Apply mode requires exact local copies of all three reviewed JCM HTML pages and
validates selected identity objects against the MediaIngredientMech SSSOM before
writing. Dry-run is the default.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
MIM_SSSOM = REPO.parent / "MediaIngredientMech" / "mappings" / "ingredient_mappings.sssom.tsv"
ACTION = "RESTORED_JCM_R2A_FAMILY"
TIMESTAMP = "2026-08-25T00:00:00-07:00"

SOURCE_FILES = {
    "JCM_346.html": "63dfbe90d38e903a76836e23c42651ec98b3fe778c285ca0274ccd4f816ea8bb",
    "JCM_1091.html": "3335c9e28273375ce3f454927ff1ed7d233af7b50869fb9f758d0e5451a944f5",
    "JCM_1311.html": "49ad5e1fc84575d78e62312592f5be1ec7e08b30e79f9ad89f534e73dcfc6577",
}


def _url(number: str) -> str:
    return f"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD={number}"


@dataclass(frozen=True)
class Target:
    relative_path: str
    record_id: str
    source_number: str
    recipe_key: str
    precondition: str


BASE_PATH = "bacterial/r2a_agar.yaml"
FIVE_X_PATH = "bacterial/5_x_r2a_agar.yaml"
PH9_PATH = "bacterial/r2a_agar_ph_9_0.yaml"

TARGETS = (
    Target(BASE_PATH, "CultureMech:002706", "346", "base", "parsed"),
    Target(FIVE_X_PATH, "CultureMech:002271", "1091", "five_x", "parsed"),
    Target(PH9_PATH, "CultureMech:002475", "1311", "ph9", "empty"),
)

MIM_TERMS: dict[str, tuple[str, str]] = {
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "Proteose peptone No. 3": ("MICRO:0000180", "proteose peptone"),
    "Casamino acids": ("FOODON:03315719", "mammalian milk protein (hydrolyzed)"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Soluble starch": ("CHEBI:28017", "starch"),
    "Sodium pyruvate": ("CHEBI:50144", "sodium pyruvate"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "Agar": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
}


def ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
    }
    identifier, label = MIM_TERMS[preferred_term]
    row["term"] = {"id": identifier, "label": label}
    if identifier.startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = {
            "id": identifier,
            "label": label,
        }
    if notes:
        row["notes"] = notes
    return row


def _r2a_ingredients(multiplier: int) -> list[dict[str, Any]]:
    if multiplier == 1:
        values = ("0.5", "0.5", "0.5", "0.5", "0.5", "0.3", "0.3", "0.05")
    elif multiplier == 5:
        values = ("2.5", "2.5", "2.5", "2.5", "2.5", "1.5", "1.5", "0.25")
    else:
        raise ValueError(f"unsupported R2A multiplier: {multiplier}")
    names = (
        "Yeast extract",
        "Proteose peptone No. 3",
        "Casamino acids",
        "Glucose",
        "Soluble starch",
        "Sodium pyruvate",
        "K2HPO4",
        "MgSO4 x 7 H2O",
    )
    return [
        *(ingredient(name, value, "G_PER_L") for name, value in zip(names, values, strict=True)),
        ingredient("Agar", "15.0", "G_PER_L"),
        ingredient("Distilled water", "1.0", "L"),
    ]


def _reference(
    relative_path: str,
    record_id: str,
    name: str,
    relationship: str,
    notes: str,
) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{relative_path}",
        "relationship": relationship,
        "id": record_id,
        "name": name,
        "notes": notes,
    }


def _base_steps(ph9: bool = False) -> list[dict[str, Any]]:
    steps = [
        {
            "step_number": 1,
            "action": "MIX",
            "description": "Combine the printed components with 1.0 L distilled water.",
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust the R2A base to pH 7.2.",
        },
        {
            "step_number": 3,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 C for 15 minutes.",
        },
    ]
    if ph9:
        steps.append(
            {
                "step_number": 4,
                "action": "ADJUST_PH",
                "description": (
                    "After autoclaving, adjust to pH 9.0 with separately sterilized "
                    "10% Na2CO3 solution. JCM does not specify the volume added."
                ),
            }
        )
    return steps


def recipe_for(target: Target) -> dict[str, Any]:
    recipe: dict[str, Any] = {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 9.0 if target.recipe_key == "ph9" else 7.2,
        "ingredients": _r2a_ingredients(5 if target.recipe_key == "five_x" else 1),
        "preparation_steps": _base_steps(target.recipe_key == "ph9"),
        "sterilization": {"method": "AUTOCLAVE"},
    }
    if target.recipe_key == "base":
        recipe["preparation_steps"].append(
            {
                "step_number": 4,
                "action": "MIX",
                "description": (
                    "The premixed powder is available from Becton Dickinson & Co. "
                    "as Difco R2A Agar."
                ),
            }
        )
        recipe["variant_children"] = [
            _reference(
                FIVE_X_PATH,
                "CultureMech:002271",
                "5_x_r2a_agar",
                "CONCENTRATION_VARIANT",
                "JCM 1091 increases the eight non-agar solids five-fold and retains 15 g/L agar.",
            ),
            _reference(
                PH9_PATH,
                "CultureMech:002475",
                "r2a_agar_ph_9_0",
                "PH_VARIANT",
                "JCM 1311 delegates to JCM 346 and adjusts the sterilized medium to pH 9.0.",
            ),
        ]
    else:
        relationship = "CONCENTRATION_VARIANT" if target.recipe_key == "five_x" else "PH_VARIANT"
        recipe["parent_media"] = _reference(
            BASE_PATH,
            "CultureMech:002706",
            "r2a_agar",
            relationship,
            "JCM 346 is the canonical R2A Agar formulation for this family.",
        )
        recipe["variant_relationship"] = relationship
        if target.recipe_key == "five_x":
            recipe["variant_modifications"] = [
                "Increase the eight non-agar solids five-fold; retain agar at 15 g/L."
            ]
        else:
            recipe["solutions"] = [
                {
                    "preferred_term": "10% Na2CO3 solution",
                    "composition": [
                        ingredient("Na2CO3", "100", "G_PER_L"),
                        ingredient("Distilled water", "1.0", "L"),
                    ],
                    "concentration": {"value": "variable", "unit": "VARIABLE"},
                    "notes": (
                        "Sterilize separately and add after autoclaving only as needed "
                        "to reach pH 9.0; JCM 1311 gives no addition volume."
                    ),
                }
            ]
            recipe["variant_modifications"] = [
                "After autoclaving, adjust to pH 9.0 with sterilized 10% Na2CO3 solution."
            ]
    return recipe


RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
    "parent_media",
    "variant_relationship",
    "variant_modifications",
    "variant_children",
)

PARSED_SIGNATURES = {
    "base": (
        ("Yeast extract", "0.5"),
        ("Proteose peptone no. 3", "0.5"),
        ("Casamino acids", "0.5"),
        ("Glucose", "0.5"),
        ("Starch", "0.5"),
        ("Sodium pyruvate", "0.3"),
        ("K2HPO4", "0.3"),
        ("MgSO4 x 7 H2O", "0.05"),
        ("Agar", "15"),
    ),
    "five_x": (
        ("Yeast extract", "2.5"),
        ("Proteose peptone no. 3", "2.5"),
        ("Casamino acids", "2.5"),
        ("Glucose", "2.5"),
        ("Starch", "2.5"),
        ("Sodium pyruvate", "1.5"),
        ("K2HPO4", "1.5"),
        ("MgSO4 x 7 H2O", "0.25"),
        ("Agar", "15"),
    ),
}


def _short_signature(doc: dict[str, Any]) -> tuple[tuple[str, str], ...]:
    return tuple(
        (
            str(row.get("preferred_term") or ""),
            str((row.get("concentration") or {}).get("value") or ""),
        )
        for row in doc.get("ingredients") or []
    )


def _projection(doc: dict[str, Any]) -> dict[str, Any]:
    return {field: copy.deepcopy(doc[field]) for field in RECIPE_FIELDS if field in doc}


def history_has_action(doc: dict[str, Any]) -> bool:
    return any(
        isinstance(row, dict) and row.get("action") == ACTION
        for row in doc.get("curation_history") or []
    )


def validate_source_files(source_dir: Path) -> None:
    for file_name, expected_hash in SOURCE_FILES.items():
        path = source_dir / file_name
        if not path.is_file():
            raise ValueError(f"missing reviewed JCM source file: {path}")
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            raise ValueError(f"{path}: SHA-256 {actual_hash}, expected reviewed {expected_hash}")


def validate_mim_terms(sssom_path: Path) -> None:
    if not sssom_path.is_file():
        raise ValueError(f"missing MediaIngredientMech SSSOM: {sssom_path}")
    with sssom_path.open(encoding="utf-8", newline="") as handle:
        rows = csv.DictReader((line for line in handle if not line.startswith("#")), delimiter="\t")
        objects = {
            (str(row.get("object_id") or ""), str(row.get("object_label") or "")) for row in rows
        }
    missing = sorted(set(MIM_TERMS.values()) - objects)
    if missing:
        rendered = ", ".join(f"{curie} ({label})" for curie, label in missing)
        raise ValueError(f"selected mappings are absent from the MIM SSSOM: {rendered}")


def _source_note(target: Target) -> str:
    own_name = f"JCM_{target.source_number}.html"
    own = (
        f"Composition verified against {_url(target.source_number)} on 2026-08-25 "
        f"(SHA-256 {SOURCE_FILES[own_name]})."
    )
    if target.recipe_key == "ph9":
        own += (
            f" The delegated JCM 346 base was verified at {_url('346')} "
            f"(SHA-256 {SOURCE_FILES['JCM_346.html']})."
        )
    return own


def _validate_precondition(doc: dict[str, Any], target: Target) -> None:
    if str(doc.get("id") or "") != target.record_id:
        raise ValueError(
            f"{target.relative_path}: id {doc.get('id')!r}, expected {target.record_id}"
        )
    if target.precondition == "parsed":
        if _short_signature(doc) != PARSED_SIGNATURES[target.recipe_key]:
            raise ValueError(f"{target.relative_path}: parsed R2A pre-state drifted")
        if doc.get("solutions"):
            raise ValueError(f"{target.relative_path}: unexpectedly already has solutions")
    elif target.precondition == "empty":
        if doc.get("ingredients") or doc.get("solutions"):
            raise ValueError(f"{target.relative_path}: record is no longer composition-empty")
        if "incomplete_composition" not in (doc.get("data_quality_flags") or []):
            raise ValueError(f"{target.relative_path}: missing incomplete_composition flag")
    else:
        raise ValueError(f"unknown precondition: {target.precondition}")


def _assert_applied(doc: dict[str, Any], target: Target) -> None:
    if _projection(doc) != _projection(recipe_for(target)):
        raise ValueError(f"{target.relative_path}: applied R2A recipe drifted")
    flags = doc.get("data_quality_flags") or []
    if any(flag in flags for flag in ("incomplete_composition", "source_information_unavailable")):
        raise ValueError(f"{target.relative_path}: stale missing-source flag returned")
    if _source_note(target) not in str(doc.get("notes") or ""):
        raise ValueError(f"{target.relative_path}: source verification note is missing")


def repair_document(doc: dict[str, Any], target: Target) -> tuple[dict[str, Any], bool]:
    if history_has_action(doc):
        _assert_applied(doc, target)
        return doc, False
    _validate_precondition(doc, target)

    repaired = copy.deepcopy(doc)
    recipe = recipe_for(target)
    for field in RECIPE_FIELDS:
        if field in recipe:
            repaired[field] = copy.deepcopy(recipe[field])
        else:
            repaired.pop(field, None)

    flags = repaired.get("data_quality_flags") or []
    if not isinstance(flags, list):
        raise ValueError(f"{target.relative_path}: data_quality_flags is not a list")
    kept_flags = [
        flag
        for flag in flags
        if flag not in {"incomplete_composition", "source_information_unavailable"}
    ]
    if kept_flags:
        repaired["data_quality_flags"] = kept_flags
    else:
        repaired.pop("data_quality_flags", None)

    note = _source_note(target)
    existing_notes = str(repaired.get("notes") or "").rstrip()
    repaired["notes"] = f"{existing_notes}\n{note}" if existing_notes else note

    history = repaired.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.relative_path}: curation_history is not a list")
    history.append(
        {
            "timestamp": TIMESTAMP,
            "curator": "repair_jcm_r2a_family.py",
            "action": ACTION,
            "changes": (
                f"ingredients {len(doc.get('ingredients') or [])} -> "
                f"{len(recipe['ingredients'])}; solutions "
                f"{len(doc.get('solutions') or [])} -> {len(recipe.get('solutions') or [])}"
            ),
            "notes": (
                "Restored the reviewed JCM R2A formulation, printed water, default "
                "sterilization, and reciprocal variant semantics. Identity objects "
                "were verified against the MIM SSSOM; unspecified carbonate volume "
                "remains explicitly variable."
            ),
        }
    )
    _assert_applied(repaired, target)
    return repaired, True


def _validate_inventory() -> None:
    if len(TARGETS) != 3 or len({target.relative_path for target in TARGETS}) != 3:
        raise ValueError("JCM R2A inventory must contain three unique records")
    if len({target.record_id for target in TARGETS}) != 3:
        raise ValueError("JCM R2A target ids must be unique")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--sssom", type=Path, default=MIM_SSSOM)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    _validate_inventory()
    if args.source_dir is not None:
        validate_source_files(args.source_dir)
    elif args.apply:
        raise ValueError("--apply requires --source-dir with the reviewed JCM HTML pages")
    validate_mim_terms(args.sssom)

    pending = []
    for target in TARGETS:
        path = args.normalized_dir / target.relative_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            raise ValueError(f"{path}: expected a YAML mapping")
        repaired, changed = repair_document(doc, target)
        pending.append((path, repaired, changed, target))
        print(
            f"{'fix' if changed else 'skip':4s}  {target.relative_path}: JCM {target.source_number}"
        )

    changed_count = sum(changed for _, _, changed, _ in pending)
    if args.apply:
        for path, repaired, changed, _ in pending:
            if changed:
                write_record(path, repaired)
    verb = "updated" if args.apply else "would update"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
