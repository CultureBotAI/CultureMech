#!/usr/bin/env python3
"""Ground exact KOMODO/JCM score-10 ingredient mappings."""

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

TARGET_SIGNATURES = {
    Path("bacterial/JCM_J44_BENNETT_S_AGAR.yaml"): (
        "Yeast extract",
        "Beef extract",
        "N-Z amine",
        "Glucose",
        "Agar",
    ),
    Path("bacterial/KOMODO_102_FLAVOBACTERIUM_AQUATILE_medium.yaml"): (
        "Na-caseinate",
        "Yeast extract",
        "Proteose peptone",
        "K2HPO4",
        "Agar",
    ),
    Path("bacterial/KOMODO_1076_SP4_MEDIUM.yaml"): (
        "Tryptone",
        "Peptone",
        "PPLO broth",
        "Fetal bovine serum",
        "CMRL 1066",
        "Yeast extract",
        "Phenol red",
        "L-Glutamine",
    ),
    Path("bacterial/KOMODO_1076b_SP4-Z_medium.yaml"): (
        "Tryptone",
        "Peptone",
        "PPLO broth",
        "Fetal bovine serum",
        "CMRL 1066",
        "Yeast extract",
        "Phenol red",
        "L-Glutamine",
    ),
    Path("bacterial/KOMODO_1109_BTT_medium.yaml"): (
        "Glucose",
        "Yeast extract",
        "Meat extract",
        "Casitone",
        "Agar",
    ),
    Path("bacterial/KOMODO_1133_ENRICHED_CYTOPHAGA_AGAR_medium.yaml"): (
        "Tryptone",
        "Beef extract",
        "Yeast extract",
        "Sodium acetate",
        "Agar",
    ),
    Path("bacterial/KOMODO_1143_TY_medium.yaml"): (
        "Tryptone",
        "Yeast extract",
        "CaCl2 x 2 H2O",
    ),
    Path("bacterial/KOMODO_21_SARCINA_medium.yaml"): (
        "Glucose",
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_238_STREPTOMYCIN_NUTRIENT_AGAR.yaml"): (
        "Peptone",
        "Meat extract",
        "Agar",
        "Streptomycin sulfate",
    ),
    Path("bacterial/KOMODO_245_BLOOD_AGAR_II.yaml"): (
        "Defibrinated sheep blood",
        "Casein peptone",
        "Soy peptone",
        "NaCl",
        "Agar",
    ),
    Path("bacterial/KOMODO_251_Peptone_-_MEAT_EXTRACT_-_SOIL_EXTRACT_AGAR_PFE.yaml"): (
        "Proteose peptone no. 3",
        "Meat extract",
        "Glycerol",
        "Soil extract",
        "Agar",
    ),
    Path("bacterial/KOMODO_264_TOMATO_JUICE_medium.yaml"): (
        "Casein peptone",
        "Yeast extract",
        "Tomato juice",
        "Tween 80",
    ),
    Path("bacterial/KOMODO_281_HYPHOMONAS_medium.yaml"): (
        "Casitone",
        "Yeast extract",
        "MgCl2 x 6 H2O",
    ),
    Path("bacterial/KOMODO_302_NUTRIENT_BROTH_WITH_10_HORSE_SERUM.yaml"): (
        "Peptone",
        "Meat extract",
        "Agar",
        "Horse serum",
    ),
    Path("bacterial/KOMODO_306_NY-AGAR.yaml"): (
        "Peptone",
        "Meat extract",
        "Agar",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_309_NEOMYCIN_AGAR.yaml"): (
        "Beef extract",
        "Yeast extract",
        "Peptone",
        "Glucose",
        "Casitone",
        "Neomycin",
    ),
}

EXPECTED_IDS = {
    Path("bacterial/JCM_J44_BENNETT_S_AGAR.yaml"): "CultureMech:002800",
    Path("bacterial/KOMODO_102_FLAVOBACTERIUM_AQUATILE_medium.yaml"): ("CultureMech:003542"),
    Path("bacterial/KOMODO_1076_SP4_MEDIUM.yaml"): "CultureMech:003664",
    Path("bacterial/KOMODO_1076b_SP4-Z_medium.yaml"): "CultureMech:003729",
    Path("bacterial/KOMODO_1109_BTT_medium.yaml"): "CultureMech:003810",
    Path("bacterial/KOMODO_1133_ENRICHED_CYTOPHAGA_AGAR_medium.yaml"): ("CultureMech:003843"),
    Path("bacterial/KOMODO_1143_TY_medium.yaml"): "CultureMech:003854",
    Path("bacterial/KOMODO_21_SARCINA_medium.yaml"): "CultureMech:004430",
    Path("bacterial/KOMODO_238_STREPTOMYCIN_NUTRIENT_AGAR.yaml"): ("CultureMech:004611"),
    Path("bacterial/KOMODO_245_BLOOD_AGAR_II.yaml"): "CultureMech:004616",
    Path("bacterial/KOMODO_251_Peptone_-_MEAT_EXTRACT_-_SOIL_EXTRACT_AGAR_PFE.yaml"): (
        "CultureMech:004623"
    ),
    Path("bacterial/KOMODO_264_TOMATO_JUICE_medium.yaml"): "CultureMech:004667",
    Path("bacterial/KOMODO_281_HYPHOMONAS_medium.yaml"): "CultureMech:004734",
    Path("bacterial/KOMODO_302_NUTRIENT_BROTH_WITH_10_HORSE_SERUM.yaml"): ("CultureMech:004809"),
    Path("bacterial/KOMODO_306_NY-AGAR.yaml"): "CultureMech:004854",
    Path("bacterial/KOMODO_309_NEOMYCIN_AGAR.yaml"): "CultureMech:004886",
}

TARGET_TERMS = {
    Path("bacterial/JCM_J44_BENNETT_S_AGAR.yaml"): (
        "Beef extract",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_102_FLAVOBACTERIUM_AQUATILE_medium.yaml"): (
        "Proteose peptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_1076_SP4_MEDIUM.yaml"): (
        "Peptone",
        "Tryptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_1076b_SP4-Z_medium.yaml"): (
        "Peptone",
        "Tryptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_1109_BTT_medium.yaml"): (
        "Casitone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_1133_ENRICHED_CYTOPHAGA_AGAR_medium.yaml"): (
        "Beef extract",
        "Tryptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_1143_TY_medium.yaml"): (
        "Tryptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_21_SARCINA_medium.yaml"): (
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_238_STREPTOMYCIN_NUTRIENT_AGAR.yaml"): ("Peptone",),
    Path("bacterial/KOMODO_245_BLOOD_AGAR_II.yaml"): (
        "Casein peptone",
        "Soy peptone",
    ),
    Path("bacterial/KOMODO_251_Peptone_-_MEAT_EXTRACT_-_SOIL_EXTRACT_AGAR_PFE.yaml"): (
        "Proteose peptone no. 3",
        "Soil extract",
    ),
    Path("bacterial/KOMODO_264_TOMATO_JUICE_medium.yaml"): (
        "Casein peptone",
        "Tomato juice",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_281_HYPHOMONAS_medium.yaml"): (
        "Casitone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_302_NUTRIENT_BROTH_WITH_10_HORSE_SERUM.yaml"): (
        "Horse serum",
        "Peptone",
    ),
    Path("bacterial/KOMODO_306_NY-AGAR.yaml"): (
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_309_NEOMYCIN_AGAR.yaml"): (
        "Beef extract",
        "Casitone",
        "Peptone",
        "Yeast extract",
    ),
}

TERMS = {
    "Beef extract": {"id": "FOODON:03302088", "label": "Beef extract"},
    "Casein peptone": {"id": "FOODON:03315719", "label": "Casein peptone"},
    "Casitone": {"id": "MICRO:0000606", "label": "Casitone"},
    "Horse serum": {"id": "MICRO:0001235", "label": "Horse serum"},
    "Peptone": {"id": "MICRO:0000178", "label": "Peptone"},
    "Proteose peptone": {"id": "MICRO:0000180", "label": "Proteose Peptone"},
    "Proteose peptone no. 3": {
        "id": "MICRO:0000180",
        "label": "Proteose Peptone",
    },
    "Soil extract": {"id": "MICRO:0000457", "label": "Soil extract"},
    "Soy peptone": {"id": "FOODON:03315720", "label": "Soy peptone"},
    "Tomato juice": {"id": "FOODON:03301454", "label": "Tomato juice"},
    "Tryptone": {"id": "MICRO:0000182", "label": "Tryptone"},
    "Yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
}

CURATOR = "repair_komodo_jcm_score10_exact_terms.py"
ACTION = "GROUNDED_KOMODO_JCM_SCORE10_EXACT_TERMS"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _ingredient_signature(doc: dict[str, Any]) -> tuple[str, ...]:
    ingredients = doc.get("ingredients") or []
    if not isinstance(ingredients, list):
        raise ValueError("ingredients is not a list")
    return tuple(
        str(row.get("preferred_term") or "") for row in ingredients if isinstance(row, dict)
    )


def _ensure_event(doc: dict[str, Any], event: dict[str, Any]) -> None:
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == event["curator"]
            and existing.get("action") == event["action"]
        ):
            history[index] = event
            return
    history.append(event)


def _targeted_terms(path: Path) -> str:
    return ", ".join(TARGET_TERMS[path])


def repair_record(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_IDS[path]:
        raise ValueError(f"{path}: expected {EXPECTED_IDS[path]}, found {doc.get('id')!r}")
    if _ingredient_signature(doc) != TARGET_SIGNATURES[path]:
        raise ValueError(f"{path}: ingredient signature drifted: {_ingredient_signature(doc)!r}")

    expected_terms = set(TARGET_TERMS[path])
    grounded_terms: set[str] = set()
    repaired = copy.deepcopy(doc)
    for ingredient in repaired["ingredients"]:
        preferred_term = ingredient["preferred_term"]
        if preferred_term not in expected_terms:
            continue

        term = copy.deepcopy(TERMS[preferred_term])
        ingredient["term"] = term
        grounded_terms.add(preferred_term)

    if grounded_terms != expected_terms:
        missing = ", ".join(sorted(expected_terms - grounded_terms))
        raise ValueError(f"{path}: missing targeted ingredient(s): {missing}")

    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Grounded exact KOMODO/JCM score-10 ingredients",
            "source": "src/culturemech/data/mediaingredientmech/label_index.csv",
            "notes": f"Applied local mappings for {_targeted_terms(path)}.",
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / relative: repair_record(relative, _load(normalized / relative))
        for relative in TARGET_SIGNATURES
    }


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
