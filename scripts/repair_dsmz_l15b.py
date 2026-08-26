#!/usr/bin/env python3
"""Restore basal L-15B from the source delegated by DSMZ Medium 1591.

The DSMZ recipe delegates to ``Tick Cell Culture Methods``. That document gives
the complete undiluted basal L-15B formula, mineral stocks, vitamin stock, and
filtration protocol. The schema permits one stock-composition level, so source
stocks A-C are materialized at their exact effective concentrations within stock
D rather than flattened into the final medium. The source separately describes L-15B300 and optional
complete-growth supplements; those use-case variants are documented but are not
folded into the basal formulation.

Apply mode requires exact local copies of both reviewed PDFs and validates every
selected identity object against the MediaIngredientMech SSSOM. Dry-run is the
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
TARGET_PATH = "bacterial/l_15b_tick_cell_medium.yaml"
TARGET_ID = "CultureMech:001068"
ACTION = "RESTORED_DSMZ_1591_L15B"
TIMESTAMP = "2026-08-25T00:00:00-07:00"

SOURCE_FILES = {
    "DSMZ_Medium1591.pdf": "b4957b2953812ba39cb48d28097fe979b097355a3cc664c47462aac73902cf75",
    "TickCellCultureMethods-4.pdf": (
        "be6881f2290a4d364b6de79d1aaa9f88378ca82e54394b055d0ea5b1e5df477a"
    ),
}
DSMZ_URL = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1591.pdf"
METHODS_URL = (
    "https://www.dsmz.de/fileadmin/Bereiche/Microbiology/Dateien/"
    "Kultivierungshinweise/TickCellCultureMethods-4.pdf"
)

MIM_TERMS: dict[str, tuple[str, str]] = {
    "Cell culture grade water": ("CHEBI:15377", "water"),
    "L-aspartic acid": ("CHEBI:17053", "L-aspartic acid"),
    "L-glutamine": ("CHEBI:18050", "L-glutamine"),
    "L-proline": ("CHEBI:17203", "L-proline"),
    "L-glutamic acid": ("CHEBI:16015", "L-glutamic acid"),
    "alpha-ketoglutaric acid": ("CHEBI:30915", "2-oxoglutaric acid"),
    "D-glucose": ("CHEBI:17634", "D-glucose"),
    "Ascorbic acid": ("CHEBI:22652", "ascorbic acid"),
    "Glutathione (reduced)": ("CHEBI:16856", "glutathione"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "MnSO4 x H2O": ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2SeO3": ("CHEBI:48843", "disodium selenite"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Cyanocobalamin": ("CHEBI:17439", "cyanocob(III)alamin"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
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


MINERAL_STOCK_D = stock(
    "L-15B mineral stock solution D",
    "1",
    [
        ingredient("Ascorbic acid", "10.0", "G_PER_L"),
        ingredient("Glutathione (reduced)", "10.0", "G_PER_L"),
        ingredient("FeSO4 x 7 H2O", "0.50", "G_PER_L"),
        ingredient(
            "CoCl2 x 6 H2O",
            "0.002",
            "G_PER_L",
            notes=(
                "Effective concentration in stock D: stock A contains 0.20 g/L "
                "and is added at 1 ml per 100 ml (10 ml/L). MIM maps the hydrated "
                "source label to cobalt dichloride."
            ),
        ),
        ingredient(
            "CuSO4 x 5 H2O",
            "0.002",
            "G_PER_L",
            notes=(
                "Effective concentration in stock D: stock A contains 0.20 g/L "
                "and is added at 10 ml/L."
            ),
        ),
        ingredient(
            "MnSO4 x H2O",
            "0.016",
            "G_PER_L",
            notes=(
                "Effective concentration in stock D: stock A contains 1.60 g/L "
                "and is added at 10 ml/L."
            ),
        ),
        ingredient(
            "ZnSO4 x 7 H2O",
            "0.020",
            "G_PER_L",
            notes=(
                "Effective concentration in stock D: stock A contains 2.00 g/L "
                "and is added at 10 ml/L."
            ),
        ),
        ingredient(
            "Na2MoO4 x 2 H2O",
            "0.002",
            "G_PER_L",
            notes=(
                "Effective concentration in stock D: stock B contains 0.20 g/L "
                "and is added at 10 ml/L."
            ),
        ),
        ingredient(
            "Na2SeO3",
            "0.002",
            "G_PER_L",
            notes=(
                "Effective concentration in stock D: stock C contains 0.20 g/L "
                "and is added at 10 ml/L."
            ),
        ),
    ],
    notes=(
        "The source prints 1000 mg ascorbic acid, 1000 mg reduced glutathione, "
        "and 50 mg FeSO4.7H2O per 100 ml, plus 1 ml each of stocks A-C. Because "
        "the schema does not support a stock nested inside another stock, A-C are "
        "represented above at their exact effective concentrations within D. Add "
        "1 ml stock D per litre basal L-15B."
    ),
)

VITAMIN_STOCK = stock(
    "L-15B vitamin stock",
    "1",
    [
        ingredient("p-Aminobenzoic acid", "1.00", "G_PER_L"),
        ingredient("Cyanocobalamin", "0.50", "G_PER_L"),
        ingredient("Biotin", "0.10", "G_PER_L"),
    ],
    notes=(
        "The source prints 100, 50, and 10 mg per 100 ml, respectively. Add "
        "1 ml vitamin stock per litre basal L-15B."
    ),
)

NAOH_STOCK = stock(
    "10 N NaOH solution",
    "0.5",
    [
        ingredient(
            "NaOH",
            "10",
            "MOLAR",
            notes="For monovalent NaOH, the source's 10 N concentration is 10 M.",
        )
    ],
    notes="Add 0.5 ml per litre basal L-15B.",
)

RECIPE: dict[str, Any] = {
    "medium_type": "COMPLEX",
    "composition_type": "UNDEFINED",
    "physical_state": "LIQUID",
    "ph_range": {"min": 5.5, "max": 6.5},
    "ingredients": [
        ingredient(
            "Cell culture grade water",
            "1",
            "L",
            notes="Bring the basal medium to a final volume of 1 litre.",
        ),
        unmapped_ingredient(
            "Leibovitz's L-15 medium powder",
            "1 package",
            "VARIABLE",
            notes=(
                "One package of GIBCO Leibovitz L-15 powder, Cat. No. 41300039. "
                "No defensible identity object is present in the reviewed MIM SSSOM."
            ),
        ),
        ingredient("L-aspartic acid", "0.299", "G_PER_L"),
        ingredient("L-glutamine", "0.292", "G_PER_L"),
        ingredient("L-proline", "0.300", "G_PER_L"),
        ingredient("L-glutamic acid", "0.490", "G_PER_L"),
        ingredient("alpha-ketoglutaric acid", "0.299", "G_PER_L"),
        ingredient("D-glucose", "14.4105", "G_PER_L"),
    ],
    "solutions": [
        copy.deepcopy(MINERAL_STOCK_D),
        copy.deepcopy(VITAMIN_STOCK),
        copy.deepcopy(NAOH_STOCK),
    ],
    "preparation_steps": [
        {
            "step_number": 1,
            "action": "HEAT",
            "description": (
                "Use a volumetric flask dry-heat treated at 180 C or above for at "
                "least 2 hours to remove endotoxins."
            ),
        },
        {
            "step_number": 2,
            "action": "MIX",
            "description": (
                "Preload 500-700 ml sterile cell-culture-grade water, add components "
                "in the printed order, and bring the final volume to 1 litre."
            ),
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": (
                "Stir slowly for 1.5 hours, no longer, while protecting the medium "
                "from light."
            ),
        },
        {
            "step_number": 4,
            "action": "FILTER_STERILIZE",
            "description": "Filter through a 0.22 micrometre filter into storage bottles.",
        },
        {
            "step_number": 5,
            "action": "STORE",
            "description": (
                "Check a 4-5 ml aliquot from each bottle for sterility at 37 C. "
                "Confirm pH 5.5-6.5 and, if possible, 415 +/- 10 mOsm/L. Store "
                "protected from light at 4 C; the source states it keeps for months."
            ),
        },
    ],
    "sterilization": {"method": "FILTER"},
}

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


def _source_note() -> str:
    return (
        f"DSMZ Medium 1591 delegation verified against {DSMZ_URL} on 2026-08-25 "
        f"(SHA-256 {SOURCE_FILES['DSMZ_Medium1591.pdf']}); basal L-15B composition "
        f"verified against {METHODS_URL} (SHA-256 "
        f"{SOURCE_FILES['TickCellCultureMethods-4.pdf']}). Recipe encodes undiluted "
        "basal L-15B. L-15B300 dilution and optional FBS, TPB, lipoprotein, HEPES, "
        "and NaHCO3 supplements remain documented source variants, not base ingredients."
    )


def _validate_precondition(doc: dict[str, Any]) -> None:
    if str(doc.get("id") or "") != TARGET_ID:
        raise ValueError(f"{TARGET_PATH}: id {doc.get('id')!r}, expected {TARGET_ID}")
    if doc.get("ingredients") or doc.get("solutions"):
        raise ValueError(f"{TARGET_PATH}: record is no longer composition-empty")
    if "incomplete_composition" not in (doc.get("data_quality_flags") or []):
        raise ValueError(f"{TARGET_PATH}: missing incomplete_composition flag")


def _assert_applied(doc: dict[str, Any]) -> None:
    if _projection(doc) != _projection(RECIPE):
        raise ValueError(f"{TARGET_PATH}: applied L-15B recipe drifted")
    if "incomplete_composition" in (doc.get("data_quality_flags") or []):
        raise ValueError(f"{TARGET_PATH}: incomplete flag returned")
    if _source_note() not in str(doc.get("notes") or ""):
        raise ValueError(f"{TARGET_PATH}: source verification note is missing")


def repair_document(doc: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    if history_has_action(doc):
        _assert_applied(doc)
        return doc, False
    _validate_precondition(doc)

    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        if field in RECIPE:
            repaired[field] = copy.deepcopy(RECIPE[field])
        else:
            repaired.pop(field, None)

    flags = repaired.get("data_quality_flags") or []
    if not isinstance(flags, list):
        raise ValueError(f"{TARGET_PATH}: data_quality_flags is not a list")
    kept_flags = [flag for flag in flags if flag != "incomplete_composition"]
    if kept_flags:
        repaired["data_quality_flags"] = kept_flags
    else:
        repaired.pop("data_quality_flags", None)

    note = _source_note()
    existing_notes = str(repaired.get("notes") or "").rstrip()
    repaired["notes"] = f"{existing_notes}\n{note}" if existing_notes else note
    history = repaired.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET_PATH}: curation_history is not a list")
    history.append(
        {
            "timestamp": TIMESTAMP,
            "curator": "repair_dsmz_l15b.py",
            "action": ACTION,
            "changes": "ingredients 0 -> 8; solutions 0 -> 3",
            "notes": (
                "Restored basal undiluted L-15B with mineral stock D, vitamin "
                "stock, NaOH stock, filtration, and source pH range. Stock masses "
                "printed per 100 ml were converted to per-litre concentrations; "
                "stocks A-C were materialized within D because the schema permits "
                "only one stock-composition level. "
                "identity objects were verified against the MIM SSSOM."
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
        validate_source_files(args.source_dir)
    elif args.apply:
        raise ValueError("--apply requires --source-dir with the reviewed DSMZ PDFs")
    validate_mim_terms(args.sssom)

    path = args.normalized_dir / TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    repaired, changed = repair_document(doc)
    print(f"{'fix' if changed else 'skip':4s}  {TARGET_PATH}: DSMZ 1591")
    if args.apply and changed:
        write_record(path, repaired)
    verb = "updated" if args.apply else "would update"
    print(f"\n{verb} {int(changed)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
