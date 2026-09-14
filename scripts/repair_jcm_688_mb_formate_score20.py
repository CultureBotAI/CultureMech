#!/usr/bin/env python3
"""Repair JCM Medium 688 MB Medium With Formate from TOGO M708."""

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
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

PATH = Path("bacterial/mb_medium_with_formate.yaml")
EXPECTED_ID = "CultureMech:003033"
EXPECTED_SOURCE_TERM = "mediadive.medium:J688"

JCM_688 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=688"
TOGO_M708 = "https://togomedium.org/medium/M708"
TOGO_M142 = "https://togomedium.org/medium/M142"
TOGO_M190 = "https://togomedium.org/medium/M190"
TOGO_M431 = "https://togomedium.org/medium/M431"

SOURCE_M708 = "TOGO M708/JCM Medium 688"
SOURCE_M142 = "TOGO M142 trace minerals"
SOURCE_M190 = "TOGO M190 trace vitamins"
SOURCE_M431 = "TOGO M431 selenite-tungstate solution"

CURATOR = "repair_jcm_688_mb_formate_score20.py"
ACTION = "RESOLVED_JCM_688_MB_FORMATE_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "TOGO M708 records JCM Medium 688 as MB Medium With Formate: Solution "
    "A contains 920 ml distilled water plus salts, yeast extract, "
    "Trypticase peptone, 10 ml trace minerals from M142, and 1 ml "
    "selenite-tungstate solution from M431; per liter, add 5 ml each of "
    "5% Na2S x 9H2O and 5% L-cysteine x HCl x H2O, 50 ml of 136 g/L sodium "
    "formate stock, and 10 ml trace vitamins from M190."
)

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
)

IMPORTED_INGREDIENTS = frozenset({"Sodium formate"})


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _stock_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    term: tuple[str, str],
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"Component of {source}.",
        term=term,
    )


def _solution(
    preferred_term: str,
    value: str,
    *,
    notes: str,
    composition: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "notes": notes,
        "composition": copy.deepcopy(composition),
    }


def _m708(
    preferred_term: str,
    value: str,
    unit: str,
    amount: str,
    *,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=SOURCE_M708,
        notes=f"{SOURCE_M708} lists {amount} in Solution A.",
        term=term,
    )


RECIPE: dict[str, Any] = {
    "medium_type": "COMPLEX",
    "composition_type": "UNDEFINED",
    "physical_state": "LIQUID",
    "ingredients": [
        _m708(
            "Distilled water",
            "920",
            "ML_PER_L",
            "920 ml distilled water",
            term=("CHEBI:15377", "water"),
        ),
        _m708("Yeast extract", "2", "G_PER_L", "2 g yeast extract"),
        _m708("NaCl", "10", "G_PER_L", "10 g NaCl", term=("CHEBI:26710", "sodium chloride")),
        _m708(
            "CaCl2 x 2H2O",
            "0.4",
            "G_PER_L",
            "0.4 g CaCl2 x 2H2O",
            term=("CHEBI:86158", "calcium chloride dihydrate"),
        ),
        _m708(
            "NH4Cl",
            "1",
            "G_PER_L",
            "1 g NH4Cl",
            term=("CHEBI:31206", "ammonium chloride"),
        ),
        _m708(
            "K2HPO4",
            "0.4",
            "G_PER_L",
            "0.4 g K2HPO4",
            term=("CHEBI:131527", "dipotassium hydrogen phosphate"),
        ),
        _m708(
            "Resazurin",
            "0.0005",
            "G_PER_L",
            "0.5 mg resazurin",
            term=("CHEBI:8806", "Resazurin"),
        ),
        _m708(
            "MgCl2 x 6H2O",
            "1",
            "G_PER_L",
            "1 g MgCl2 x 6H2O",
            term=("CHEBI:86345", "magnesium dichloride hexahydrate"),
        ),
        _m708("KCl", "0.5", "G_PER_L", "0.5 g KCl", term=("CHEBI:32588", "potassium chloride")),
        _m708(
            "NaHCO3",
            "4",
            "G_PER_L",
            "4 g NaHCO3",
            term=("CHEBI:32139", "sodium hydrogencarbonate"),
        ),
        _m708("Trypticase peptone", "2", "G_PER_L", "2 g Trypticase peptone"),
        _m708(
            "CO2",
            "variable",
            "VARIABLE",
            "CO2 gas under N2-CO2 (80:20)",
            term=("CHEBI:16526", "carbon dioxide"),
        ),
        _m708(
            "N2",
            "variable",
            "VARIABLE",
            "N2 gas under N2-CO2 (80:20)",
            term=("CHEBI:17997", "dinitrogen"),
        ),
    ],
    "solutions": [
        _solution(
            "Trace minerals (TOGO Medium M142)",
            "10",
            notes=(f"{SOURCE_M708} adds 10 ml/L Trace minerals from TOGO M142."),
            composition=[
                _stock_component(
                    "MgSO4 x 7H2O",
                    "3",
                    "G_PER_L",
                    source=SOURCE_M142,
                    term=("CHEBI:31795", "magnesium sulfate heptahydrate"),
                ),
                _stock_component(
                    "NaCl",
                    "1",
                    "G_PER_L",
                    source=SOURCE_M142,
                    term=("CHEBI:26710", "sodium chloride"),
                ),
                _stock_component(
                    "CaCl2 x 2H2O",
                    "0.1",
                    "G_PER_L",
                    source=SOURCE_M142,
                    term=("CHEBI:86158", "calcium chloride dihydrate"),
                ),
                _stock_component(
                    "Na2MoO4 x 2H2O",
                    "0.01",
                    "G_PER_L",
                    source=SOURCE_M142,
                    term=("CHEBI:75213", "sodium molybdate dihydrate"),
                ),
                _stock_component(
                    "H3BO3",
                    "0.01",
                    "G_PER_L",
                    source=SOURCE_M142,
                    term=("CHEBI:33118", "boric acid"),
                ),
                _stock_component(
                    "FeSO4 x 7H2O",
                    "0.1",
                    "G_PER_L",
                    source=SOURCE_M142,
                    term=("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
                ),
                _stock_component(
                    "ZnSO4 x 7H2O",
                    "0.1",
                    "G_PER_L",
                    source=SOURCE_M142,
                    term=("CHEBI:32312", "zinc sulfate heptahydrate"),
                ),
                _stock_component(
                    "CuSO4 x 5H2O",
                    "0.01",
                    "G_PER_L",
                    source=SOURCE_M142,
                    term=("CHEBI:31440", "copper(II) sulfate pentahydrate"),
                ),
                _stock_component(
                    "CoSO4 x 7H2O",
                    "0.1",
                    "G_PER_L",
                    source=SOURCE_M142,
                    term=("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
                ),
                _stock_component(
                    "Nitrilotriacetic acid",
                    "1.5",
                    "G_PER_L",
                    source=SOURCE_M142,
                    term=("CHEBI:44557", "nitrilotriacetic acid"),
                ),
                _stock_component(
                    "MnSO4 x n H2O",
                    "0.5",
                    "G_PER_L",
                    source=SOURCE_M142,
                    term=("CHEBI:86360", "manganese(II) sulfate hydrate"),
                ),
                _stock_component(
                    "AlK(SO4)2",
                    "0.01",
                    "G_PER_L",
                    source=SOURCE_M142,
                    term=("CHEBI:86463", "potassium aluminium sulfate"),
                ),
                _stock_component(
                    "KOH solution",
                    "variable",
                    "VARIABLE",
                    source=SOURCE_M142,
                    term=("CHEBI:32035", "potassium hydroxide"),
                ),
            ],
        ),
        _solution(
            "Selenite--tungstate solution (TOGO Medium M431)",
            "1",
            notes=(f"{SOURCE_M708} adds 1 ml/L Selenite--tungstate solution " "from TOGO M431."),
            composition=[
                _stock_component(
                    "Na2SeO3 x 5H2O",
                    "0.006",
                    "G_PER_L",
                    source=SOURCE_M431,
                    term=("CHEBI:131361", "disodium selenite pentahydrate"),
                ),
                _stock_component(
                    "Na2WO4 x 2H2O",
                    "0.008",
                    "G_PER_L",
                    source=SOURCE_M431,
                    term=("CHEBI:63939", "sodium tungstate dihydrate"),
                ),
                _stock_component(
                    "NaOH",
                    "0.4",
                    "G_PER_L",
                    source=SOURCE_M431,
                    term=("CHEBI:32145", "sodium hydroxide"),
                ),
            ],
        ),
        _solution(
            "5% Na2S x 9H2O solution",
            "5",
            notes=f"{SOURCE_M708} adds 5 ml/L 5% Na2S x 9H2O solution.",
            composition=[
                _stock_component(
                    "Na2S x 9H2O",
                    "50",
                    "G_PER_L",
                    source=SOURCE_M708,
                    term=("CHEBI:76209", "sodium sulfide nonahydrate"),
                )
            ],
        ),
        _solution(
            "5% L-Cysteine x HCl x H2O solution",
            "5",
            notes=f"{SOURCE_M708} adds 5 ml/L 5% L-cysteine x HCl x H2O solution.",
            composition=[
                _stock_component(
                    "L-Cysteine x HCl x H2O",
                    "50",
                    "G_PER_L",
                    source=SOURCE_M708,
                    term=("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
                )
            ],
        ),
        _solution(
            "Sodium formate solution",
            "50",
            notes=(
                f"{SOURCE_M708} adds 50 ml/L filter-sterilized sodium "
                "formate stock containing 6.8 g sodium formate in 50 ml water."
            ),
            composition=[
                _stock_component(
                    "Sodium formate",
                    "136",
                    "G_PER_L",
                    source=SOURCE_M708,
                    term=("CHEBI:62965", "sodium formate"),
                )
            ],
        ),
        _solution(
            "Trace vitamins (TOGO Medium M190)",
            "10",
            notes=f"{SOURCE_M708} adds 10 ml/L Trace vitamins from TOGO M190.",
            composition=[
                _stock_component(
                    "Biotin",
                    "0.002",
                    "G_PER_L",
                    source=SOURCE_M190,
                    term=("CHEBI:15956", "Biotin"),
                ),
                _stock_component(
                    "p-Aminobenzoic acid",
                    "0.005",
                    "G_PER_L",
                    source=SOURCE_M190,
                    term=("CHEBI:30753", "4-aminobenzoic acid"),
                ),
                _stock_component(
                    "Thiamine-HCl",
                    "0.005",
                    "G_PER_L",
                    source=SOURCE_M190,
                    term=("CHEBI:49105", "thiamine hydrochloride"),
                ),
                _stock_component(
                    "Calcium pantothenate",
                    "0.005",
                    "G_PER_L",
                    source=SOURCE_M190,
                    term=("CHEBI:31345", "Calcium pantothenate"),
                ),
                _stock_component(
                    "Pyridoxine-HCl",
                    "0.01",
                    "G_PER_L",
                    source=SOURCE_M190,
                    term=("CHEBI:30961", "Pyridoxine hydrochloride"),
                ),
                _stock_component(
                    "Folic acid",
                    "0.002",
                    "G_PER_L",
                    source=SOURCE_M190,
                    term=("CHEBI:27470", "Folic acid"),
                ),
                _stock_component(
                    "Vitamin B12",
                    "0.0001",
                    "G_PER_L",
                    source=SOURCE_M190,
                    term=("CHEBI:176843", "Vitamin B12"),
                ),
                _stock_component(
                    "Riboflavin",
                    "0.005",
                    "G_PER_L",
                    source=SOURCE_M190,
                    term=("CHEBI:17015", "Riboflavin"),
                ),
                _stock_component(
                    "Nicotinic acid",
                    "0.005",
                    "G_PER_L",
                    source=SOURCE_M190,
                    term=("CHEBI:15940", "Nicotinic acid"),
                ),
                _stock_component(
                    "Lipoic acid",
                    "0.005",
                    "G_PER_L",
                    source=SOURCE_M190,
                    term=("CHEBI:16494", "lipoic acid"),
                ),
            ],
        ),
    ],
    "preparation_steps": [
        {
            "step_number": 1,
            "action": "MIX",
            "description": "Mix Solution A components except NaHCO3.",
        },
        {
            "step_number": 2,
            "action": "HEAT",
            "description": (
                "Bring to a boil for several seconds and cool under " "N2-CO2 (80:20)."
            ),
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": (
                "Add NaHCO3, mix thoroughly, and distribute the medium "
                "into culture vessels under N2-CO2 (80:20)."
            ),
        },
        {
            "step_number": 4,
            "action": "AUTOCLAVE",
            "description": "Seal with butyl rubber stoppers and autoclave.",
        },
        {
            "step_number": 5,
            "action": "FILTER_STERILIZE",
            "description": "Filter-sterilize the sodium formate solution.",
        },
        {
            "step_number": 6,
            "action": "MIX",
            "description": (
                "Finally, add the sterile 5% Na2S x 9H2O, 5% "
                "L-cysteine x HCl x H2O, sodium formate, and trace vitamin "
                "solutions per liter."
            ),
        },
    ],
}

REPAIRED_INGREDIENTS = frozenset(row["preferred_term"] for row in RECIPE["ingredients"])


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{PATH}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERM:
        raise ValueError(
            f"{PATH}: expected source term {EXPECTED_SOURCE_TERM}, " f"found {source_term!r}"
        )

    ingredient_names = {
        str(row.get("preferred_term") or "")
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    }
    if ingredient_names not in (IMPORTED_INGREDIENTS, REPAIRED_INGREDIENTS):
        raise ValueError(f"{PATH}: ingredient list drifted")


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in (JCM_688, TOGO_M708, TOGO_M142, TOGO_M190, TOGO_M431):
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": TOGO_M708,
        "notes": NOTES,
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
    _require_target(doc)

    repaired = copy.deepcopy(doc)
    for recipe_field in RECIPE_FIELDS:
        if recipe_field in RECIPE:
            repaired[recipe_field] = copy.deepcopy(RECIPE[recipe_field])
        else:
            repaired.pop(recipe_field, None)
    repaired["notes"] = NOTES
    repaired["data_quality_flags"] = [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repair(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / PATH
    return {path: repair_record(_load(path))}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repair(args.normalized_dir)
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
