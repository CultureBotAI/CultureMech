#!/usr/bin/env python3
"""Correct the three source-duplicate DSMZ 833 records from the reviewed PDF.

The imported records flattened Solutions A-H, divided some quantities by the
wrong intermediate volume, merged distinct vitamin-stock ingredients, and kept
gas atmospheres as ingredients. This migration scales the direct Solution A
components to the printed 1003 ml final volume and preserves every separately
prepared stock addition at its final-medium ml/L amount.

Apply mode requires the exact reviewed DSMZ PDF and validates every selected
identity object against the MediaIngredientMech SSSOM. Dry-run is the default.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
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
ACTION = "CORRECTED_DSMZ_833_SOLUTION_STRUCTURE"
TIMESTAMP = "2026-08-25T00:00:00-07:00"
SOURCE_FILE = "DSMZ_Medium833.pdf"
SOURCE_HASH = "35bf0077611e781af17c24f3786b51fc5ac8719df60ea06d8eb4d754d0f2fc33"
SOURCE_URL = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium833.pdf"

CANONICAL_PATH = "bacterial/dehalospirillum_medium.yaml"
KOMODO_PATH = "bacterial/KOMODO_833_DEHALOSPIRILLUM_medium.yaml"
TOGO_PATH = "bacterial/TOGO_M2455_Dehalospirillum_Medium.yaml"


@dataclass(frozen=True)
class Target:
    relative_path: str
    record_id: str
    expected_pre_hash: str


TARGETS = (
    Target(
        CANONICAL_PATH,
        "CultureMech:001990",
        "e110a293628c86ba4d447d869c6303b523793ad460d36409f67b7d515bc6c03a",
    ),
    Target(
        KOMODO_PATH,
        "CultureMech:006625",
        "e110a293628c86ba4d447d869c6303b523793ad460d36409f67b7d515bc6c03a",
    ),
    Target(
        TOGO_PATH,
        "CultureMech:009034",
        "6b6fb385aa92ea65b3faab82d63253860feb496198f46964d8f148bebbc98c23",
    ),
)

MIM_TERMS: dict[str, tuple[str, str]] = {
    "Na2SO4": ("CHEBI:32149", "sodium sulfate"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "MgCl2 x 6 H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "Distilled water": ("CHEBI:15377", "water"),
    "HCl": ("CHEBI:17883", "hydrogen chloride"),
    "FeCl2 x 4 H2O": ("CHEBI:86249", "iron dichloride tetrahydrate"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2 H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "NiCl2 x 6 H2O": ("CHEBI:34887", "nickel dichloride"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "Na2SeO3 x 5 H2O": ("CHEBI:131361", "disodium selenite pentahydrate"),
    "Na2WO4 x 2 H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "Pyridoxine hydrochloride": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "Calcium D-(+)-pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "(DL)-alpha-Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "D-(+)-biotin": ("CHEBI:15956", "biotin"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Thiamine-HCl x 2 H2O": ("CHEBI:132751", "thiamine hydrochloride dihydrate"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "Na-pyruvate": ("CHEBI:50144", "sodium pyruvate"),
    "Na2-fumarate": ("CHEBI:115156", "disodium fumarate"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "H2SO4": ("CHEBI:26836", "sulfuric acid"),
    "L-Cysteine HCl x H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
}


def ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    mapping_key: str | None = None,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
    }
    identifier, label = MIM_TERMS[mapping_key or preferred_term]
    row["term"] = {"id": identifier, "label": label}
    if identifier.startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = {
            "id": identifier,
            "label": label,
        }
    if notes:
        row["notes"] = notes
    return row


def unmapped_ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "notes": notes,
    }


def solution(
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


def water(value: str = "1000") -> dict[str, Any]:
    return ingredient("Distilled water", value, "ML_PER_L")


DIRECT_INGREDIENTS = [
    ingredient("Na2SO4", "0.697906", "G_PER_L"),
    ingredient("KH2PO4", "0.199402", "G_PER_L"),
    ingredient("NH4Cl", "0.249252", "G_PER_L"),
    ingredient("NaCl", "0.249252", "G_PER_L"),
    ingredient("MgCl2 x 6 H2O", "0.398804", "G_PER_L"),
    ingredient("KCl", "0.498504", "G_PER_L"),
    ingredient("CaCl2 x 2 H2O", "0.149551", "G_PER_L"),
    ingredient("Yeast extract", "1.994018", "G_PER_L"),
    ingredient(
        "Distilled water",
        "887.337986",
        "ML_PER_L",
        notes=(
            "Solution A prints 890 ml water in a final medium volume of 1003 ml; "
            "scaled to a one-litre final basis."
        ),
    ),
]

TRACE_SL10 = solution(
    "Trace element solution SL-10",
    "0.997009",
    [
        ingredient("HCl (25%)", "10", "ML_PER_L", mapping_key="HCl"),
        ingredient("FeCl2 x 4 H2O", "1.50", "G_PER_L"),
        ingredient("ZnCl2", "0.070", "G_PER_L"),
        ingredient("MnCl2 x 4 H2O", "0.100", "G_PER_L"),
        ingredient("H3BO3", "0.006", "G_PER_L"),
        ingredient(
            "CoCl2 x 6 H2O",
            "0.190",
            "G_PER_L",
            notes="MIM maps the hydrated source label to cobalt dichloride.",
        ),
        ingredient("CuCl2 x 2 H2O", "0.002", "G_PER_L"),
        ingredient(
            "NiCl2 x 6 H2O",
            "0.024",
            "G_PER_L",
            notes="MIM maps the hydrated source label to nickel dichloride.",
        ),
        ingredient("Na2MoO4 x 2 H2O", "0.036", "G_PER_L"),
        water("990"),
    ],
    notes=(
        "Component of source Solution A: 1 ml in the printed 1003 ml final medium, "
        "scaled to 0.997009 ml/L. Stock formula is from DSMZ medium 320 as reproduced "
        "in the reviewed DSMZ 833 PDF."
    ),
)

SELENITE_TUNGSTATE = solution(
    "Selenite-tungstate solution",
    "0.997009",
    [
        ingredient("NaOH", "0.50", "G_PER_L"),
        ingredient("Na2SeO3 x 5 H2O", "0.003", "G_PER_L"),
        ingredient("Na2WO4 x 2 H2O", "0.004", "G_PER_L"),
        water(),
    ],
    notes=(
        "Component of source Solution A: 1 ml in 1003 ml final medium. Stock formula "
        "is from DSMZ medium 385 as reproduced in the reviewed PDF."
    ),
)

RESAZURIN = solution(
    "Sodium resazurin solution (0.1% w/v)",
    "0.498504",
    [ingredient("Resazurin", "1.0", "G_PER_L"), water()],
    notes="Component of source Solution A: 0.5 ml in 1003 ml final medium.",
)

PHOSPHATE_BUFFER = solution(
    "Solution B: potassium phosphate buffer",
    "9.970090",
    [
        unmapped_ingredient(
            "Potassium phosphate buffer (pH 7.5)",
            "0.1",
            "MOLAR",
            notes=(
                "MIM maps this label only to NCIT or kgmicrobe objects, neither of "
                "which is admitted by the current ingredient-term CURIE pattern."
            ),
        )
    ],
    notes="Source Solution B: 10 ml in 1003 ml final medium.",
)

WOLIN_VITAMINS = solution(
    "Solution C1: Wolin's vitamin solution (10x)",
    "0.997009",
    [
        ingredient("Biotin", "0.020", "G_PER_L"),
        ingredient("Folic acid", "0.020", "G_PER_L"),
        ingredient("Pyridoxine hydrochloride", "0.100", "G_PER_L"),
        ingredient("Thiamine HCl", "0.050", "G_PER_L"),
        ingredient("Riboflavin", "0.050", "G_PER_L"),
        ingredient("Nicotinic acid", "0.050", "G_PER_L"),
        ingredient("Calcium D-(+)-pantothenate", "0.050", "G_PER_L"),
        ingredient("Vitamin B12", "0.001", "G_PER_L"),
        ingredient("p-Aminobenzoic acid", "0.050", "G_PER_L"),
        ingredient("(DL)-alpha-Lipoic acid", "0.050", "G_PER_L"),
        water(),
    ],
    notes=(
        "First half of source Solution C: 1 ml in 1003 ml final medium. Stock formula "
        "is from DSMZ medium 120 as reproduced in the reviewed PDF."
    ),
)

SEVEN_VITAMINS = solution(
    "Solution C2: seven vitamins solution",
    "0.997009",
    [
        ingredient("Vitamin B12", "0.100", "G_PER_L"),
        ingredient("p-Aminobenzoic acid", "0.080", "G_PER_L"),
        ingredient("D-(+)-biotin", "0.020", "G_PER_L"),
        ingredient("Nicotinic acid", "0.200", "G_PER_L"),
        ingredient("Calcium pantothenate", "0.100", "G_PER_L"),
        ingredient("Pyridoxine hydrochloride", "0.300", "G_PER_L"),
        ingredient("Thiamine-HCl x 2 H2O", "0.200", "G_PER_L"),
        water(),
    ],
    notes=(
        "Second half of source Solution C: 1 ml in 1003 ml final medium. Stock formula "
        "is from DSMZ medium 503 as reproduced in the reviewed PDF."
    ),
)

CARBONATE = solution(
    "Solution D: Na2CO3 solution",
    "34.895314",
    [ingredient("Na2CO3", "50.0", "G_PER_L"), water()],
    notes="Source Solution D: 1.75 g Na2CO3 in 35 ml water; add 35 ml per 1003 ml.",
)

PYRUVATE = solution(
    "Solution E: Na-pyruvate solution",
    "19.940179",
    [ingredient("Na-pyruvate", "225.0", "G_PER_L"), water()],
    notes="Source Solution E: 4.50 g Na-pyruvate in 20 ml water; add 20 ml per 1003 ml.",
)

FUMARATE = solution(
    "Solution F: Na2-fumarate solution",
    "39.880359",
    [ingredient("Na2-fumarate", "160.0", "G_PER_L"), water()],
    notes="Source Solution F: 6.40 g Na2-fumarate in 40 ml water; add 40 ml per 1003 ml.",
)

IRON = solution(
    "Solution G: FeSO4 in 0.1 N H2SO4",
    "2.991027",
    [
        ingredient("FeSO4 x 7 H2O", "10.0", "G_PER_L"),
        ingredient(
            "H2SO4 (0.1 N)",
            "0.1 N",
            "VARIABLE",
            mapping_key="H2SO4",
            notes="Normality is retained verbatim because the schema has no normality unit.",
        ),
    ],
    notes="Source Solution G: 30 mg FeSO4.7H2O in 3 ml 0.1 N H2SO4; add all 3 ml.",
)

CYSTEINE = solution(
    "Solution H: L-Cysteine HCl solution",
    "0.997009",
    [ingredient("L-Cysteine HCl x H2O", "50.0", "G_PER_L"), water()],
    notes="Source Solution H: 50 mg in 1 ml water; add 1 ml per 1003 ml.",
)

SOLUTIONS = [
    TRACE_SL10,
    SELENITE_TUNGSTATE,
    RESAZURIN,
    PHOSPHATE_BUFFER,
    WOLIN_VITAMINS,
    SEVEN_VITAMINS,
    CARBONATE,
    PYRUVATE,
    FUMARATE,
    IRON,
    CYSTEINE,
]


def _reference(
    path: str,
    record_id: str,
    relationship: str,
    notes: str,
) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": record_id,
        "name": "dehalospirillum_medium",
        "notes": notes,
    }


def recipe_for(target: Target) -> dict[str, Any]:
    recipe: dict[str, Any] = {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_range": {"min": 7.3, "max": 7.6},
        "ingredients": copy.deepcopy(DIRECT_INGREDIENTS),
        "solutions": copy.deepcopy(SOLUTIONS),
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Prepare source Solution A from the direct components plus SL-10, "
                    "selenite-tungstate, and 0.1% resazurin stocks at the printed amounts."
                ),
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": (
                    "Sparge Solution A with 100% N2 for 30-45 minutes, dispense under "
                    "N2, and autoclave. Autoclave Solutions B and H separately under "
                    "100% N2. Autoclave Solution D under 80% N2 and 20% CO2."
                ),
            },
            {
                "step_number": 3,
                "action": "FILTER_STERILIZE",
                "description": (
                    "Prepare Solutions C, E, F, and G under 100% N2 and sterilize "
                    "them by filtration."
                ),
            },
            {
                "step_number": 4,
                "action": "MIX",
                "description": (
                    "Add Solutions B-H to sterile Solution A in the printed sequence. "
                    "The source batch final volume is 1003 ml."
                ),
            },
            {
                "step_number": 5,
                "action": "ADJUST_PH",
                "description": "Adjust the complete medium to pH 7.3-7.6 if necessary.",
            },
            {
                "step_number": 6,
                "action": "FILTER_STERILIZE",
                "description": (
                    "Before inoculation, ensure resazurin is colorless. If needed, add "
                    "10-20 mg/L sodium dithionite from freshly prepared, anoxic, "
                    "filter-sterilized 5% solution."
                ),
            },
            {
                "step_number": 7,
                "action": "DISSOLVE",
                "description": (
                    "For SL-10, first dissolve FeCl2 in 25% HCl, dilute in water, add "
                    "the other salts, and make to 1 litre."
                ),
            },
        ],
    }
    canonical = _reference(
        CANONICAL_PATH,
        "CultureMech:001990",
        "SOURCE_DUPLICATE",
        "DSMZ Medium 833 is the canonical reviewed formulation source.",
    )
    if target.relative_path == CANONICAL_PATH:
        recipe["variant_children"] = [
            _reference(
                KOMODO_PATH,
                "CultureMech:006625",
                "SOURCE_DUPLICATE",
                "KOMODO Medium 833 explicitly cites DSMZ Medium 833.",
            ),
            _reference(
                TOGO_PATH,
                "CultureMech:009034",
                "SOURCE_DUPLICATE",
                "TOGO M2455 links directly to the DSMZ Medium 833 PDF.",
            ),
        ]
    else:
        recipe["parent_media"] = canonical
        recipe["variant_relationship"] = "SOURCE_DUPLICATE"
        recipe["variant_modifications"] = [
            "Source-catalogue duplicate of DSMZ Medium 833; no formulation change."
        ]
    return recipe


RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
    "high_metal",
    "parent_media",
    "variant_relationship",
    "variant_modifications",
    "variant_children",
)


def _projection(doc: dict[str, Any]) -> dict[str, Any]:
    return {field: copy.deepcopy(doc[field]) for field in RECIPE_FIELDS if field in doc}


def composition_hash(doc: dict[str, Any]) -> str:
    payload = {"ingredients": doc.get("ingredients"), "solutions": doc.get("solutions")}
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def history_has_action(doc: dict[str, Any]) -> bool:
    return any(
        isinstance(row, dict) and row.get("action") == ACTION
        for row in doc.get("curation_history") or []
    )


def validate_source_file(source_dir: Path) -> None:
    path = source_dir / SOURCE_FILE
    if not path.is_file():
        raise ValueError(f"missing reviewed DSMZ source file: {path}")
    actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual_hash != SOURCE_HASH:
        raise ValueError(f"{path}: SHA-256 {actual_hash}, expected reviewed {SOURCE_HASH}")


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


def _source_note() -> str:
    return (
        f"Composition verified against {SOURCE_URL} on 2026-08-25 "
        f"(SHA-256 {SOURCE_HASH}). Direct Solution A quantities and all stock addition "
        "volumes were scaled from the printed 1003 ml batch to a one-litre final basis."
    )


def _validate_precondition(doc: dict[str, Any], target: Target) -> None:
    if str(doc.get("id") or "") != target.record_id:
        raise ValueError(
            f"{target.relative_path}: id {doc.get('id')!r}, expected {target.record_id}"
        )
    actual_hash = composition_hash(doc)
    if actual_hash != target.expected_pre_hash:
        raise ValueError(
            f"{target.relative_path}: composition pre-state hash {actual_hash} drifted "
            f"from expected {target.expected_pre_hash}"
        )


def _assert_applied(doc: dict[str, Any], target: Target) -> None:
    if _projection(doc) != _projection(recipe_for(target)):
        raise ValueError(f"{target.relative_path}: applied DSMZ 833 recipe drifted")
    if _source_note() not in str(doc.get("notes") or ""):
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

    note = _source_note()
    existing_notes = str(repaired.get("notes") or "").rstrip()
    repaired["notes"] = f"{existing_notes}\n{note}" if existing_notes else note
    history = repaired.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.relative_path}: curation_history is not a list")
    history.append(
        {
            "timestamp": TIMESTAMP,
            "curator": "repair_dsmz_833_family.py",
            "action": ACTION,
            "changes": (
                f"ingredients {len(doc.get('ingredients') or [])} -> "
                f"{len(recipe['ingredients'])}; solutions "
                f"{len(doc.get('solutions') or [])} -> {len(recipe['solutions'])}"
            ),
            "notes": (
                "Corrected final-volume scaling, restored Solutions A-H and embedded "
                "stock boundaries, separated the two vitamin stocks, and removed gas "
                "atmospheres from ingredients. Identity objects were verified against MIM."
            ),
        }
    )
    _assert_applied(repaired, target)
    return repaired, True


def _validate_inventory() -> None:
    if len(TARGETS) != 3 or len({target.relative_path for target in TARGETS}) != 3:
        raise ValueError("DSMZ 833 inventory must contain three unique records")
    if len({target.record_id for target in TARGETS}) != 3:
        raise ValueError("DSMZ 833 target ids must be unique")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--sssom", type=Path, default=MIM_SSSOM)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    _validate_inventory()
    if args.source_dir is not None:
        validate_source_file(args.source_dir)
    elif args.apply:
        raise ValueError("--apply requires --source-dir with the reviewed DSMZ PDF")
    validate_mim_terms(args.sssom)

    pending = []
    for target in TARGETS:
        path = args.normalized_dir / target.relative_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            raise ValueError(f"{path}: expected a YAML mapping")
        repaired, changed = repair_document(doc, target)
        pending.append((path, repaired, changed, target))
        print(f"{'fix' if changed else 'skip':4s}  {target.relative_path}: DSMZ 833")

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
