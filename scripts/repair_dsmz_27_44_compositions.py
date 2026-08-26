#!/usr/bin/env python3
"""Correct DSMZ 27 stock structure and restore its explicit duplicates.

MediaDive flattened the four stock solutions in DSMZ Medium 27 into direct
final-medium ingredients. That made vitamin B12 10,000-fold too concentrated,
the SL-6 trace salts 1,000-fold too concentrated, and resazurin 10-fold too
concentrated. DSMZ Medium 44, whose source says only "Same as modified medium
27", was imported without a composition. The KOMODO record explicitly cites
DSMZ 27 and copied the same flattened formulation.

Apply mode requires exact local copies of the two reviewed DSMZ PDFs and checks
every selected ontology object against the MediaIngredientMech SSSOM before any
record is written. Dry-run is the default.
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
ACTION = "CORRECTED_DSMZ_27_44_STOCK_STRUCTURE"
TIMESTAMP = "2026-08-25T00:00:00-07:00"

SOURCE_FILES = {
    "DSMZ_Medium27.pdf": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
    "DSMZ_Medium44.pdf": "5481d1ffe5c2d81a54a8ad650e4829f44b3de8863b267adf91f4c92a2430b16b",
}
SOURCE_URLS = {
    "27": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium27.pdf",
    "44": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium44.pdf",
}


@dataclass(frozen=True)
class Target:
    relative_path: str
    record_id: str
    source_key: str
    precondition: str


TARGETS = (
    Target(
        "bacterial/rhodospirillaceae_medium_modified.yaml",
        "CultureMech:001375",
        "27",
        "flattened",
    ),
    Target(
        "bacterial/KOMODO_27_RHODOSPIRILLACEAE_medium_modified.yaml",
        "CultureMech:004707",
        "27",
        "flattened",
    ),
    Target(
        "bacterial/rhodocyclus_purpureus_medium.yaml",
        "CultureMech:001559",
        "44",
        "empty",
    ),
)

# These are object id/label pairs present in the sibling MIM SSSOM. Source
# labels without a more specific MIM object retain the defensible broader object
# selected by MIM (notably cobalt and nickel chlorides).
MIM_TERMS: dict[str, tuple[str, str]] = {
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "Disodium succinate": ("CHEBI:63675", "sodium succinate (anhydrous)"),
    "Ammonium acetate": ("CHEBI:62947", "ammonium acetate"),
    "Fe(III) citrate": ("CHEBI:144421", "iron(III) citrate"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "L-Cysteine HCl": ("CHEBI:91247", "L-cysteine hydrochloride"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2 H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "NiCl2 x 6 H2O": ("CHEBI:34887", "nickel dichloride"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
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


def stock(
    preferred_term: str,
    use_value: str,
    composition: list[dict[str, Any]],
    *,
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "composition": composition,
        "concentration": {"value": use_value, "unit": "ML_PER_L"},
        "notes": notes,
    }


def _base_recipe() -> dict[str, Any]:
    direct = [
        ingredient("Yeast extract", "0.30", "G_PER_L"),
        ingredient("Disodium succinate", "1.00", "G_PER_L"),
        ingredient("Ammonium acetate", "0.50", "G_PER_L"),
        ingredient("KH2PO4", "0.50", "G_PER_L"),
        ingredient("MgSO4 x 7 H2O", "0.40", "G_PER_L"),
        ingredient("NaCl", "0.40", "G_PER_L"),
        ingredient("NH4Cl", "0.40", "G_PER_L"),
        ingredient("CaCl2 x 2 H2O", "0.05", "G_PER_L"),
        ingredient("L-Cysteine HCl", "0.30", "G_PER_L"),
        ingredient(
            "Distilled water",
            "1000.00",
            "ML_PER_L",
            notes="Amount printed for the final-medium batch in DSMZ Medium 27.",
        ),
    ]
    water = ingredient("Distilled water", "1000.00", "ML_PER_L")
    solutions = [
        stock(
            "Fe(III) citrate solution (0.1% in water)",
            "5.00",
            [ingredient("Fe(III) citrate", "1.00", "G_PER_L"), copy.deepcopy(water)],
            notes="0.1% (w/v) stock; add 5.00 ml per printed final-medium batch.",
        ),
        stock(
            "Vitamin B12 solution (10 mg in 100 ml water)",
            "0.40",
            [ingredient("Vitamin B12", "0.10", "G_PER_L"), copy.deepcopy(water)],
            notes=(
                "10 mg per 100 ml stock; add 0.40 ml per printed final-medium batch. "
                "This is 0.04 mg vitamin B12 per litre before any volume correction."
            ),
        ),
        stock(
            "Trace element solution SL-6",
            "1.00",
            [
                ingredient("ZnSO4 x 7 H2O", "0.10", "G_PER_L"),
                ingredient("MnCl2 x 4 H2O", "0.03", "G_PER_L"),
                ingredient("H3BO3", "0.30", "G_PER_L"),
                ingredient(
                    "CoCl2 x 6 H2O",
                    "0.20",
                    "G_PER_L",
                    notes="MIM SSSOM maps this hydrated source label to cobalt dichloride.",
                ),
                ingredient("CuCl2 x 2 H2O", "0.01", "G_PER_L"),
                ingredient(
                    "NiCl2 x 6 H2O",
                    "0.02",
                    "G_PER_L",
                    notes="MIM SSSOM maps this hydrated source label to nickel dichloride.",
                ),
                ingredient("Na2MoO4 x 2 H2O", "0.03", "G_PER_L"),
                copy.deepcopy(water),
            ],
            notes="DSMZ SL-6 stock composition is printed per litre; add 1.00 ml.",
        ),
        stock(
            "Resazurin solution (0.1%)",
            "0.50",
            [ingredient("Resazurin", "1.00", "G_PER_L"), copy.deepcopy(water)],
            notes="0.1% (w/v) stock; add 0.50 ml per printed final-medium batch.",
        ),
    ]
    return {
        "medium_type": "COMPLEX",
        "composition_type": "SEMI_DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.8,
        "ingredients": direct,
        "solutions": solutions,
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "ADJUST_PH",
                "description": "Adjust pH to 6.8.",
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": (
                    "Boil for a few minutes. Bubble with nitrogen, dispense 10 ml into "
                    "15 ml tubes with rubber septa under nitrogen, and autoclave at 121 C "
                    "for 15 minutes. Use sterile syringes for inoculation and sampling."
                ),
            },
            {
                "step_number": 3,
                "action": "MIX",
                "description": "Incubate in the light using a tungsten lamp.",
            },
        ],
        "sterilization": {"method": "AUTOCLAVE"},
    }


def _reference(relative_path: str, record_id: str, name: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{relative_path}",
        "relationship": "SOURCE_DUPLICATE",
        "id": record_id,
        "name": name,
        "notes": notes,
    }


CANONICAL_PATH = "bacterial/rhodospirillaceae_medium_modified.yaml"
KOMODO_PATH = "bacterial/KOMODO_27_RHODOSPIRILLACEAE_medium_modified.yaml"
DSMZ44_PATH = "bacterial/rhodocyclus_purpureus_medium.yaml"


def recipe_for(target: Target) -> dict[str, Any]:
    recipe = _base_recipe()
    canonical_ref = _reference(
        CANONICAL_PATH,
        "CultureMech:001375",
        "rhodospirillaceae_medium_modified",
        "DSMZ Medium 27 is the explicitly cited formulation source.",
    )
    if target.relative_path == CANONICAL_PATH:
        recipe["variant_children"] = [
            _reference(
                KOMODO_PATH,
                "CultureMech:004707",
                "rhodospirillaceae_medium_modified",
                "KOMODO Medium 27 explicitly cites DSMZ Medium 27.",
            ),
            _reference(
                DSMZ44_PATH,
                "CultureMech:001559",
                "rhodocyclus_purpureus_medium",
                "DSMZ Medium 44 states that it is the same as modified medium 27.",
            ),
        ]
    else:
        recipe["parent_media"] = canonical_ref
        recipe["variant_relationship"] = "SOURCE_DUPLICATE"
        if target.relative_path == KOMODO_PATH:
            modification = "KOMODO Medium 27 explicitly cites and duplicates DSMZ Medium 27."
        else:
            modification = "DSMZ Medium 44 states: Same as modified medium 27."
        recipe["variant_modifications"] = [modification]
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

FLATTENED_SIGNATURE = (
    ("Yeast extract", "0.3", "G_PER_L"),
    ("Disodium succinate", "1", "G_PER_L"),
    ("Ammonium acetate", "0.5", "G_PER_L"),
    ("Fe(III) citrate", "0.005", "G_PER_L"),
    ("KH2PO4", "0.5", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.4", "G_PER_L"),
    ("NaCl", "0.4", "G_PER_L"),
    ("NH4Cl", "0.4", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.05", "G_PER_L"),
    ("Vitamin B12", "0.4", "G_PER_L"),
    ("L-Cysteine HCl", "0.3", "G_PER_L"),
    ("Resazurin", "0.005", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.03", "G_PER_L"),
    ("H3BO3", "0.3", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.2", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.01", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.02", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.03", "G_PER_L"),
)


def _signature(rows: list[dict[str, Any]]) -> tuple[tuple[str, str, str], ...]:
    return tuple(
        (
            str(row.get("preferred_term") or ""),
            str((row.get("concentration") or {}).get("value") or ""),
            str((row.get("concentration") or {}).get("unit") or ""),
        )
        for row in rows
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
            raise ValueError(f"missing reviewed DSMZ source file: {path}")
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
    hash27 = SOURCE_FILES["DSMZ_Medium27.pdf"]
    if target.source_key == "44":
        hash44 = SOURCE_FILES["DSMZ_Medium44.pdf"]
        return (
            f"Composition verified against {SOURCE_URLS['44']} on 2026-08-25 "
            f"(SHA-256 {hash44}); that source delegates to {SOURCE_URLS['27']} "
            f"(SHA-256 {hash27})."
        )
    return (
        f"Composition verified against {SOURCE_URLS['27']} on 2026-08-25 "
        f"(SHA-256 {hash27})."
    )


def _validate_precondition(doc: dict[str, Any], target: Target) -> None:
    if str(doc.get("id") or "") != target.record_id:
        raise ValueError(f"{target.relative_path}: id {doc.get('id')!r}, expected {target.record_id}")
    if target.precondition == "flattened":
        if _signature(doc.get("ingredients") or []) != FLATTENED_SIGNATURE:
            raise ValueError(f"{target.relative_path}: flattened ingredient pre-state drifted")
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
        raise ValueError(f"{target.relative_path}: applied DSMZ recipe drifted")
    if "incomplete_composition" in (doc.get("data_quality_flags") or []):
        raise ValueError(f"{target.relative_path}: incomplete flag returned")
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
    kept_flags = [flag for flag in flags if flag != "incomplete_composition"]
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
            "curator": "repair_dsmz_27_44_compositions.py",
            "action": ACTION,
            "changes": (
                f"ingredients {len(doc.get('ingredients') or [])} -> "
                f"{len(recipe['ingredients'])}; solutions "
                f"{len(doc.get('solutions') or [])} -> {len(recipe['solutions'])}"
            ),
            "notes": (
                "Restored the reviewed DSMZ Medium 27 formulation while preserving four "
                "stock-solution boundaries. Corrected vitamin B12, SL-6, and resazurin "
                "concentration semantics; selected identities were verified in the MIM SSSOM."
            ),
        }
    )
    _assert_applied(repaired, target)
    return repaired, True


def _validate_inventory() -> None:
    if len(TARGETS) != 3 or len({target.relative_path for target in TARGETS}) != 3:
        raise ValueError("DSMZ 27/44 target inventory must contain three unique records")
    if len({target.record_id for target in TARGETS}) != 3:
        raise ValueError("DSMZ 27/44 target ids must be unique")


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
        raise ValueError("--apply requires --source-dir with the reviewed DSMZ PDFs")
    validate_mim_terms(args.sssom)

    pending = []
    for target in TARGETS:
        path = args.normalized_dir / target.relative_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            raise ValueError(f"{path}: expected a YAML mapping")
        repaired, changed = repair_document(doc, target)
        pending.append((path, repaired, changed, target))
        print(f"{'fix' if changed else 'skip':4s}  {target.relative_path}: DSMZ {target.source_key}")

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
