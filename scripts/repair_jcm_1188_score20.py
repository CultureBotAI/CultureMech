#!/usr/bin/env python3
"""Repair TOGO M1273/JCM 1188 Marine Chloroflexi score-20 composition."""

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
TARGET = Path("bacterial/marine_chloroflexi_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_1188_score20.py"
ACTION = "RESOLVED_JCM_1188_SCORE20_GRAPH"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
TOGO_M1273 = "https://togomedium.org/medium/M1273"
JCM_1188 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1188"
JCM_284 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=284"
JCM_852 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=852"

EXPECTED_ID = "CultureMech:007806"
EXPECTED_MEDIA_TERM = "TOGO:M1273"

NOTES = (
    "TOGO M1273 points to JCM Medium 1188; the current JCM Medium 1188 "
    "formulation contains mineral salts, yeast extract, peptone, referenced "
    "trace vitamin/mineral/Se-W solutions, four post-autoclave anaerobic "
    "stocks, distilled water, and pH 7.0."
)

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


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    term: tuple[str, str] | None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": "JCM Medium 1188",
        "notes": f"JCM Medium 1188 lists {value} {unit.lower().replace('_per_l', '/L')}.",
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _solution(
    preferred_term: str,
    value: str,
    notes: str,
    *,
    composition: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "notes": notes,
    }
    if composition is not None:
        row["composition"] = copy.deepcopy(composition)
    return row


def _stock_component(
    preferred_term: str,
    value: str,
    unit: str,
    term: tuple[str, str],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
    }


RECIPE: dict[str, Any] = {
    "medium_type": "COMPLEX",
    "composition_type": "UNDEFINED",
    "physical_state": "LIQUID",
    "ph_value": 7.0,
    "ingredients": [
        _ingredient(
            "KH2PO4",
            "0.1",
            "G_PER_L",
            term=("CHEBI:63036", "potassium dihydrogen phosphate"),
        ),
        _ingredient(
            "MgCl2 x 6 H2O",
            "4.0",
            "G_PER_L",
            term=("CHEBI:86345", "magnesium dichloride hexahydrate"),
        ),
        _ingredient(
            "CaCl2 x 2 H2O",
            "1.0",
            "G_PER_L",
            term=("CHEBI:86158", "calcium chloride dihydrate"),
        ),
        _ingredient("NH4Cl", "0.5", "G_PER_L", term=("CHEBI:31206", "ammonium chloride")),
        _ingredient("NaCl", "5.0", "G_PER_L", term=("CHEBI:26710", "sodium chloride")),
        _ingredient(
            "Yeast extract",
            "1.0",
            "G_PER_L",
            term=("FOODON:03315426", "yeast extract"),
        ),
        _ingredient("Peptone", "1.0", "G_PER_L", term=None),
        _ingredient("Distilled water", "1000", "ML_PER_L", term=("CHEBI:15377", "water")),
    ],
    "solutions": [
        _solution(
            "Trace vitamins solution",
            "2.0",
            "JCM Medium 1188 lists 2.0 ml/L Trace vitamins solution from JCM Medium 284.",
        ),
        _solution(
            "Trace mineral solution",
            "1.0",
            "JCM Medium 1188 lists 1.0 ml/L Trace mineral solution from JCM Medium 852.",
        ),
        _solution(
            "Se/W solution",
            "1.0",
            "JCM Medium 1188 lists 1.0 ml/L Se/W solution from JCM Medium 852.",
        ),
        _solution(
            "1 M Sodium pyruvate",
            "10.0",
            "JCM Medium 1188 adds 10.0 ml/L filter-sterilized 1 M Sodium pyruvate.",
            composition=[
                _stock_component(
                    "Sodium pyruvate",
                    "1.0",
                    "MOLAR",
                    ("CHEBI:50144", "sodium pyruvate"),
                )
            ],
        ),
        _solution(
            "8% NaHCO3 solution",
            "25.0",
            "JCM Medium 1188 adds 25.0 ml/L filter-sterilized 8% NaHCO3 solution.",
            composition=[
                _stock_component(
                    "NaHCO3",
                    "80.0",
                    "G_PER_L",
                    ("CHEBI:32139", "sodium hydrogencarbonate"),
                )
            ],
        ),
        _solution(
            "5% L-Cysteine x HCl x H2O solution",
            "6.0",
            "JCM Medium 1188 adds 6.0 ml/L 5% L-Cysteine x HCl x H2O solution.",
            composition=[
                _stock_component(
                    "L-Cysteine x HCl x H2O",
                    "50.0",
                    "G_PER_L",
                    ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
                )
            ],
        ),
        _solution(
            "5% Na2S x 9H2O solution",
            "6.0",
            "JCM Medium 1188 adds 6.0 ml/L 5% Na2S x 9H2O solution.",
            composition=[
                _stock_component(
                    "Na2S x 9H2O",
                    "50.0",
                    "G_PER_L",
                    ("CHEBI:76209", "sodium sulfide nonahydrate"),
                )
            ],
        ),
    ],
    "preparation_steps": [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Mix KH2PO4, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, NaCl, "
                "yeast extract, peptone, trace stocks, and distilled water."
            ),
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 7.0.",
        },
        {
            "step_number": 3,
            "action": "HEAT",
            "description": "Bring to a boil and cool under an N2-CO2 (4:1, v/v) gas stream.",
        },
        {
            "step_number": 4,
            "action": "AUTOCLAVE",
            "description": (
                "Distribute the medium into culture vessels under the same gas "
                "mixture, seal with butyl rubber stoppers, and autoclave."
            ),
        },
        {
            "step_number": 5,
            "action": "MIX",
            "description": (
                "After cooling, aseptically and anaerobically add sodium "
                "pyruvate, NaHCO3, L-cysteine, and Na2S stock solutions."
            ),
        },
    ],
    "sterilization": {"method": "AUTOCLAVE"},
}


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


def _components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        row
        for rows in (doc.get("ingredients") or [], doc.get("solutions") or [])
        for row in rows
        if isinstance(row, dict)
    ]


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "placeholder_composition",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    if any(_grounded(component) for component in _components(doc)):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")

    if any(not _grounded(component) for component in _components(doc)):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    doc["data_quality_flags"] = list(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in (TOGO_M1273, JCM_1188, JCM_284, JCM_852):
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join((TOGO_M1273, JCM_1188, JCM_284, JCM_852)),
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
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    repaired = copy.deepcopy(doc)
    for recipe_field in RECIPE_FIELDS:
        if recipe_field in RECIPE:
            repaired[recipe_field] = copy.deepcopy(RECIPE[recipe_field])
        else:
            repaired.pop(recipe_field, None)
    repaired["notes"] = NOTES
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repair(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
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
    sys.exit(main())
