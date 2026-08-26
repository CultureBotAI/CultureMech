#!/usr/bin/env python3
"""Restore four CCAP records from three reviewed source documents.

The source review found three empty MediaDive records and one malformed CCAP
record. NSS Low had stock formulations flattened into final-medium ingredients
(``NaNO`` was also truncated and mapped to the wrong concept). The source instead
adds three stocks to Tricine and makes the final medium up with seawater. wMY and
2SNA were absent altogether from their MediaDive records.

Apply mode requires local copies of the source documents and verifies their exact
SHA-256 hashes before validating every target and writing any record. The source
files reviewed on 2026-08-25 are:

* ``MR_NSS_low.pdf`` from CCAP (revision 002, approved 29 May 2026)
* ``atcc-medium-2432.pdf`` from ATCC
* ``SNA.html`` from Cyanosite

The command is dry-run by default. Use ``--source-dir /path --apply`` to write.
"""

from __future__ import annotations

import argparse
import copy
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
ACTION = "RESTORED_CCAP_SOURCE_COMPOSITION"
TIMESTAMP = "2026-08-25T00:00:00-07:00"

SOURCE_FILES = {
    "MR_NSS_low.pdf": "abb9004013ee9a0b370fc29a84608f7c965d19b1165a6ffc87d84ced88be1763",
    "atcc-medium-2432.pdf": "a639c2f74936c2ebf7e029b3d8357d29c85ed50b2b9c628afb5e3791b7e6298c",
    "SNA.html": "b7acf78efabf7db72befc85d9b82218c099655136e8263275e7c5c12656f8b49",
}

SOURCE_URLS = {
    "nss": "https://www.ccap.ac.uk/wp-content/uploads/MR_NSS_low.pdf",
    "wmy": (
        "https://www.atcc.org/-/media/product-assets/documents/"
        "microbial-media-formulations/2/4/3/2/atcc-medium-2432.pdf"
    ),
    "2sna": "https://www-cyanosite.bio.purdue.edu/media/table/SNA.html",
}


@dataclass(frozen=True)
class Target:
    relative_path: str
    record_id: str
    recipe_key: str
    precondition: str


TARGETS = (
    Target("algae/nss_low.yaml", "CultureMech:000107", "nss", "flattened_nss"),
    Target("bacterial/nss_low.yaml", "CultureMech:000383", "nss", "empty"),
    Target(
        "fungal/wmalt_yeast_extract_medium_wmy.yaml",
        "CultureMech:010440",
        "wmy",
        "empty",
    ),
    Target("bacterial/2sna.yaml", "CultureMech:000411", "2sna", "empty"),
)

FLATTENED_NSS_SIGNATURE = (
    ("NaNO", "15.00", "G_PER_L"),
    ("Na2HPO4", "0.60", "G_PER_L"),
    ("K2HPO4", "0.50", "G_PER_L"),
    ("Biotin", "0.0002", "G_PER_L"),
    ("Calcium pantothenate", "0.02", "G_PER_L"),
    ("Cyanocobalamin", "0.004", "G_PER_L"),
    ("Folic acid", "0.0004", "G_PER_L"),
    ("Inositol", "1.0", "G_PER_L"),
    ("Nicotinic acid", "0.02", "G_PER_L"),
    ("Thiamine HCl", "0.1", "G_PER_L"),
    ("Thymine", "0.6", "G_PER_L"),
    ("Tricine", "0.50", "G_PER_L"),
)


def mapped_ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    identifier: str | None = None,
    label: str | None = None,
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
    }
    if identifier and label:
        row["term"] = {"id": identifier, "label": label}
        if identifier.startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = {
                "id": identifier,
                "label": label,
            }
    if notes:
        row["notes"] = notes
    return row


def step(number: int, action: str, description: str) -> dict[str, Any]:
    return {"step_number": number, "action": action, "description": description}


def nss_recipe() -> dict[str, Any]:
    salts = [
        mapped_ingredient("NaNO3", "15.00", "G_PER_L", "CHEBI:63005", "sodium nitrate"),
        mapped_ingredient(
            "Na2HPO4",
            "0.60",
            "G_PER_L",
            "CHEBI:34683",
            "disodium hydrogenphosphate",
        ),
        mapped_ingredient(
            "K2HPO4",
            "0.50",
            "G_PER_L",
            "CHEBI:131527",
            "dipotassium hydrogen phosphate",
        ),
    ]
    vitamins = [
        mapped_ingredient("Biotin", "0.0002", "G_PER_L", "CHEBI:15956", "biotin"),
        mapped_ingredient(
            "Calcium pantothenate",
            "0.02",
            "G_PER_L",
            "CHEBI:31345",
            "Calcium pantothenate",
        ),
        mapped_ingredient(
            "Cyanocobalamin",
            "0.004",
            "G_PER_L",
            "CHEBI:17439",
            "cyanocob(III)alamin",
        ),
        mapped_ingredient("Folic acid", "0.0004", "G_PER_L", "CHEBI:27470", "folic acid"),
        mapped_ingredient("Inositol", "1.0", "G_PER_L", "CHEBI:24848", "inositol"),
        mapped_ingredient("Nicotinic acid", "0.02", "G_PER_L", "CHEBI:15940", "nicotinic acid"),
        mapped_ingredient(
            "Thiamine HCl",
            "0.1",
            "G_PER_L",
            "CHEBI:49105",
            "thiamine hydrochloride",
        ),
        mapped_ingredient("Thymine", "0.6", "G_PER_L", "CHEBI:17821", "thymine"),
    ]
    return {
        "ingredients": [
            mapped_ingredient("Tricine", "0.50", "G_PER_L", "CHEBI:46760", "tricine"),
            mapped_ingredient(
                "Filtered natural seawater",
                "1",
                "L",
                notes="Make the medium up to 1 L after adding Tricine and stocks.",
            ),
        ],
        "solutions": [
            {
                "preferred_term": "Extra salts (ASW stock 1)",
                "composition": salts,
                "concentration": {"value": "7.50", "unit": "ML_PER_L"},
                "notes": "CCAP NSS Low stock solution 1; stock composition is per litre.",
            },
            {
                "preferred_term": "Vitamin solution",
                "composition": vitamins,
                "concentration": {"value": "5.00", "unit": "ML_PER_L"},
                "notes": "CCAP NSS Low stock solution 2; stock composition is per litre.",
            },
            {
                "preferred_term": "Soil Extract 1 (SE1)",
                "composition": [],
                "concentration": {"value": "12.50", "unit": "ML_PER_L"},
                "notes": "Use the separately defined CCAP SE1 recipe.",
            },
        ],
        "preparation_steps": [
            step(1, "MIX", "Add Tricine and the three stock solutions at the stated amounts."),
            step(2, "MIX", "Make up to 1 L with filtered natural seawater."),
            step(3, "ADJUST_PH", "Adjust to pH 7.6-7.8 with 1 M NaOH or 1 M HCl."),
            step(4, "AUTOCLAVE", "Autoclave at 15 psi for 15 minutes."),
            step(
                5,
                "MIX",
                "Alternative seawater basis: make up to 1 L with deionized water and "
                "33.6 g Instant Ocean sea salts.",
            ),
        ],
        "ph_range": {"min": 7.6, "max": 7.8},
        "physical_state": "LIQUID",
        "sterilization": {"method": "AUTOCLAVE"},
    }


def wmy_recipe() -> dict[str, Any]:
    return {
        "ingredients": [
            mapped_ingredient(
                "K2HPO4",
                "0.75",
                "G_PER_L",
                "CHEBI:131527",
                "dipotassium hydrogen phosphate",
            ),
            mapped_ingredient(
                "Yeast extract",
                "0.002",
                "G_PER_L",
                "FOODON:03315426",
                "yeast extract",
            ),
            mapped_ingredient(
                "Malt extract",
                "0.002",
                "G_PER_L",
                "FOODON:03301056",
                "malt extract",
            ),
            mapped_ingredient("Distilled water", "1", "L", "CHEBI:15377", "water"),
        ],
        "solutions": [],
        "preparation_steps": [
            step(1, "MIX", "Add the constituents and make up to 1 L with distilled water."),
            step(2, "ADJUST_PH", "Adjust the final pH to 6.0-7.0."),
            step(3, "ADD_AGAR", "For an agar formulation, add 15 g/L agar."),
            step(4, "AUTOCLAVE", "Autoclave at 121 C."),
        ],
        "ph_range": {"min": 6.0, "max": 7.0},
        "physical_state": "LIQUID",
        "sterilization": {"method": "AUTOCLAVE"},
    }


def sna_recipe() -> dict[str, Any]:
    return {
        "ingredients": [
            mapped_ingredient("Nutrient agar (Oxoid CM3)", "28.0", "G_PER_L"),
            mapped_ingredient("NaCl", "35.0", "G_PER_L", "CHEBI:26710", "sodium chloride"),
            mapped_ingredient(
                "Filtered natural seawater",
                "1",
                "L",
                notes=(
                    "Natural-seawater formulation. The source also permits 35 g/L "
                    "synthetic sea salts in distilled water."
                ),
            ),
        ],
        "solutions": [],
        "preparation_steps": [
            step(1, "MIX", "Mix the constituents and ensure homogeneity."),
            step(2, "HEAT", "Steam for 30 minutes."),
            step(3, "ALIQUOT", "Dispense as required."),
            step(4, "AUTOCLAVE", "Autoclave at 15 psi."),
            step(5, "COOL", "For tubes, slope before the medium cools and solidifies."),
        ],
        "physical_state": "SOLID_AGAR",
        "sterilization": {"method": "AUTOCLAVE"},
    }


RECIPES = {"nss": nss_recipe(), "wmy": wmy_recipe(), "2sna": sna_recipe()}


def ingredient_signature(rows: list[dict[str, Any]]) -> tuple[tuple[str, str, str], ...]:
    return tuple(
        (
            str(row.get("preferred_term") or ""),
            str((row.get("concentration") or {}).get("value") or ""),
            str((row.get("concentration") or {}).get("unit") or ""),
        )
        for row in rows
    )


def descriptor_projection(row: dict[str, Any]) -> dict[str, Any]:
    projected = {
        key: copy.deepcopy(row[key])
        for key in ("preferred_term", "concentration", "notes", "preparation_notes")
        if key in row
    }
    if "composition" in row:
        projected["composition"] = [
            descriptor_projection(component) for component in row.get("composition") or []
        ]
    return projected


def recipe_projection(doc: dict[str, Any]) -> dict[str, Any]:
    return {
        "ingredients": [descriptor_projection(row) for row in doc.get("ingredients") or []],
        "solutions": [descriptor_projection(row) for row in doc.get("solutions") or []],
        "preparation_steps": copy.deepcopy(doc.get("preparation_steps") or []),
        "ph_range": copy.deepcopy(doc.get("ph_range")),
        "physical_state": doc.get("physical_state"),
        "sterilization": copy.deepcopy(doc.get("sterilization")),
    }


def source_note(target: Target) -> str:
    return f"Composition verified against {SOURCE_URLS[target.recipe_key]} on 2026-08-25."


def history_has_action(doc: dict[str, Any]) -> bool:
    return any(
        isinstance(row, dict) and row.get("action") == ACTION
        for row in doc.get("curation_history") or []
    )


def validate_source_files(source_dir: Path) -> None:
    for name, expected_hash in SOURCE_FILES.items():
        path = source_dir / name
        if not path.is_file():
            raise ValueError(f"missing reviewed source file: {path}")
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            raise ValueError(f"{path}: SHA-256 {actual_hash}, expected reviewed {expected_hash}")


def _validate_precondition(doc: dict[str, Any], target: Target) -> None:
    if str(doc.get("id") or "") != target.record_id:
        raise ValueError(
            f"{target.relative_path}: id {doc.get('id')!r}, expected {target.record_id}"
        )
    if target.precondition == "empty":
        if doc.get("ingredients") or doc.get("solutions"):
            raise ValueError(f"{target.relative_path}: record is no longer empty")
        if "incomplete_composition" not in (doc.get("data_quality_flags") or []):
            raise ValueError(f"{target.relative_path}: missing incomplete flag")
    elif target.precondition == "flattened_nss":
        actual = ingredient_signature(doc.get("ingredients") or [])
        if actual != FLATTENED_NSS_SIGNATURE or doc.get("solutions"):
            raise ValueError(f"{target.relative_path}: flattened NSS signature drifted")
    else:
        raise ValueError(f"unknown precondition {target.precondition}")


def _assert_applied(doc: dict[str, Any], target: Target) -> None:
    expected = recipe_projection(RECIPES[target.recipe_key])
    if recipe_projection(doc) != expected:
        raise ValueError(f"{target.relative_path}: applied source recipe drifted")
    if "incomplete_composition" in (doc.get("data_quality_flags") or []):
        raise ValueError(f"{target.relative_path}: incomplete flag returned")
    if source_note(target) not in str(doc.get("notes") or ""):
        raise ValueError(f"{target.relative_path}: source verification note is missing")


def repair_document(doc: dict[str, Any], target: Target) -> tuple[dict[str, Any], bool]:
    if history_has_action(doc):
        _assert_applied(doc, target)
        return doc, False
    _validate_precondition(doc, target)

    recipe = RECIPES[target.recipe_key]
    repaired = copy.deepcopy(doc)
    for field in (
        "ingredients",
        "solutions",
        "preparation_steps",
        "ph_range",
        "physical_state",
        "sterilization",
    ):
        value = recipe.get(field)
        if value in (None, []):
            repaired.pop(field, None)
        else:
            repaired[field] = copy.deepcopy(value)

    flags = repaired.get("data_quality_flags") or []
    if not isinstance(flags, list):
        raise ValueError(f"{target.relative_path}: data_quality_flags is not a list")
    kept_flags = [flag for flag in flags if flag != "incomplete_composition"]
    if kept_flags:
        repaired["data_quality_flags"] = kept_flags
    else:
        repaired.pop("data_quality_flags", None)

    note = source_note(target)
    existing_notes = str(repaired.get("notes") or "").rstrip()
    repaired["notes"] = f"{existing_notes}\n{note}" if existing_notes else note

    history = repaired.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.relative_path}: curation_history is not a list")
    old_ingredients = len(doc.get("ingredients") or [])
    old_solutions = len(doc.get("solutions") or [])
    history.append(
        {
            "timestamp": TIMESTAMP,
            "curator": "repair_ccap_missing_compositions.py",
            "action": ACTION,
            "changes": (
                f"ingredients {old_ingredients} -> {len(recipe['ingredients'])}; "
                f"solutions {old_solutions} -> {len(recipe['solutions'])}"
            ),
            "notes": (
                f"Restored {target.recipe_key} from the reviewed authoritative source. "
                "Preserved stock boundaries and source alternatives; removed the "
                "incomplete flag where present. Ingredient identities follow the "
                "MediaIngredientMech SSSOM."
            ),
        }
    )
    _assert_applied(repaired, target)
    return repaired, True


def _validate_inventory() -> None:
    paths = [target.relative_path for target in TARGETS]
    ids = [target.record_id for target in TARGETS]
    if len(TARGETS) != 4 or len(paths) != len(set(paths)) or len(ids) != len(set(ids)):
        raise ValueError("CCAP target inventory is not four unique paths and ids")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    _validate_inventory()
    if args.apply:
        if args.source_dir is None:
            raise ValueError("--apply requires --source-dir with reviewed source files")
        validate_source_files(args.source_dir)

    pending = []
    for target in TARGETS:
        path = args.normalized_dir / target.relative_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            raise ValueError(f"{path}: expected a YAML mapping")
        repaired, changed = repair_document(doc, target)
        pending.append((path, repaired, changed, target))
        print(f"{'fix' if changed else 'skip':4s}  {target.relative_path}: {target.recipe_key}")

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
