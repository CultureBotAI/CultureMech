#!/usr/bin/env python3
"""Ground exact KOMODO score-10 ingredient mappings."""

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
    Path("bacterial/KOMODO_368_KUNKEE_medium.yaml"): (
        "Tryptone",
        "Peptone",
        "Yeast extract",
        "Glucose",
        "Tween 80",
        "Tomato juice",
    ),
    Path("bacterial/KOMODO_381_LB_Luria-Bertani_medium.yaml"): (
        "Peptone",
        "Yeast extract",
        "Sea Salt",
        "Agar",
    ),
    Path("bacterial/KOMODO_393_YPD_medium.yaml"): (
        "Yeast extract",
        "Peptone",
        "Glucose",
    ),
    Path("bacterial/KOMODO_435_KDM-2_medium.yaml"): (
        "Peptone",
        "Yeast extract",
        "L-Cysteine HCl x H2O",
        "Agar",
        "Activated charcoal",
        "Fetal bovine serum",
    ),
    Path("bacterial/KOMODO_453_STANDARD_I_medium.yaml"): (
        "Meat peptone",
        "Casein peptone",
        "Yeast extract",
        "NaCl",
        "D(+)-Glucose",
    ),
    Path("bacterial/KOMODO_467_OTTOW_medium.yaml"): (
        "Glucose",
        "Peptone",
        "Meat extract",
        "Yeast extract",
        "Casamino acids",
        "NaCl",
        "Tap water",
    ),
    Path("bacterial/KOMODO_468_EXIGUOBACTERIUM_MEDIUM.yaml"): (
        "Nutrient broth No. 2",
        "Yeast extract",
        "Glucose",
    ),
    Path("bacterial/KOMODO_581_GLYCEROL_CORNSTEEP_AGAR.yaml"): (
        "Glycerol",
        "Corn steep powder",
        "Yeast extract",
        "Beef extract",
        "Casein peptone",
        "NaCl",
        "Agar",
    ),
    Path("bacterial/KOMODO_627_SEAWATER_LEMCO.yaml"): (
        "Beef extract",
        "Peptone",
        "Sea water",
        "Agar",
    ),
    Path("bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml"): (
        "Yeast extract",
        "NaCl",
        "Soil extract",
    ),
    Path("bacterial/KOMODO_695_medium_FOR_ERYTHROBACTER_LONGUS.yaml"): (
        "Peptone",
        "Soytone",
        "Yeast extract",
        "Proteose peptone no. 3",
        "Fe(III) citrate",
        "Sea water",
    ),
    Path("bacterial/KOMODO_736_RICH_medium.yaml"): (
        "Bacto peptone",
        "Yeast extract",
        "Casamino acids",
        "Meat extract",
        "Malt extract",
        "Glycerol",
        "MgSO4 x 7 H2O",
        "Tween 80",
        "Agar",
    ),
    Path("bacterial/KOMODO_80_GLYCEROL-SOIL_medium.yaml"): (
        "Peptone",
        "Beef extract",
        "Glycerol",
        "Soil extract",
        "Agar",
    ),
    Path("bacterial/KOMODO_948_OXOID_NUTRIENT_BROTH.yaml"): (
        "Nutrient broth",
        "Lab-Lemco beef extract",
        "Yeast extract",
        "Peptone",
        "NaCl",
    ),
    Path("bacterial/KOMODO_974_1_2_YTSS_medium.yaml"): (
        "Yeast extract",
        "Tryptone",
        "Sea Salt",
        "Agar",
    ),
}

EXPECTED_IDS = {
    Path("bacterial/KOMODO_368_KUNKEE_medium.yaml"): "CultureMech:005089",
    Path("bacterial/KOMODO_381_LB_Luria-Bertani_medium.yaml"): "CultureMech:005128",
    Path("bacterial/KOMODO_393_YPD_medium.yaml"): "CultureMech:005177",
    Path("bacterial/KOMODO_435_KDM-2_medium.yaml"): "CultureMech:005282",
    Path("bacterial/KOMODO_453_STANDARD_I_medium.yaml"): "CultureMech:005303",
    Path("bacterial/KOMODO_467_OTTOW_medium.yaml"): "CultureMech:005580",
    Path("bacterial/KOMODO_468_EXIGUOBACTERIUM_MEDIUM.yaml"): "CultureMech:005581",
    Path("bacterial/KOMODO_581_GLYCEROL_CORNSTEEP_AGAR.yaml"): "CultureMech:006052",
    Path("bacterial/KOMODO_627_SEAWATER_LEMCO.yaml"): "CultureMech:006133",
    Path("bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml"): ("CultureMech:006271"),
    Path("bacterial/KOMODO_695_medium_FOR_ERYTHROBACTER_LONGUS.yaml"): ("CultureMech:006313"),
    Path("bacterial/KOMODO_736_RICH_medium.yaml"): "CultureMech:006384",
    Path("bacterial/KOMODO_80_GLYCEROL-SOIL_medium.yaml"): "CultureMech:006527",
    Path("bacterial/KOMODO_948_OXOID_NUTRIENT_BROTH.yaml"): ("CultureMech:006886"),
    Path("bacterial/KOMODO_974_1_2_YTSS_medium.yaml"): "CultureMech:006932",
}

TARGET_TERMS = {
    Path("bacterial/KOMODO_368_KUNKEE_medium.yaml"): (
        "Peptone",
        "Tomato juice",
        "Tryptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_381_LB_Luria-Bertani_medium.yaml"): (
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_393_YPD_medium.yaml"): (
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_435_KDM-2_medium.yaml"): (
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_453_STANDARD_I_medium.yaml"): (
        "Casein peptone",
        "Meat peptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_467_OTTOW_medium.yaml"): (
        "Casamino acids",
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_468_EXIGUOBACTERIUM_MEDIUM.yaml"): ("Yeast extract",),
    Path("bacterial/KOMODO_581_GLYCEROL_CORNSTEEP_AGAR.yaml"): (
        "Beef extract",
        "Casein peptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_627_SEAWATER_LEMCO.yaml"): (
        "Beef extract",
        "Peptone",
    ),
    Path("bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml"): (
        "Soil extract",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_695_medium_FOR_ERYTHROBACTER_LONGUS.yaml"): (
        "Peptone",
        "Proteose peptone no. 3",
        "Soytone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_736_RICH_medium.yaml"): (
        "Bacto peptone",
        "Casamino acids",
        "Malt extract",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_80_GLYCEROL-SOIL_medium.yaml"): (
        "Beef extract",
        "Peptone",
        "Soil extract",
    ),
    Path("bacterial/KOMODO_948_OXOID_NUTRIENT_BROTH.yaml"): (
        "Lab-Lemco beef extract",
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/KOMODO_974_1_2_YTSS_medium.yaml"): (
        "Tryptone",
        "Yeast extract",
    ),
}

TERMS = {
    "Bacto peptone": {"id": "MICRO:0000178", "label": "Bacto peptone"},
    "Beef extract": {"id": "FOODON:03302088", "label": "Beef extract"},
    "Casamino acids": {"id": "FOODON:03315719", "label": "Casamino acids"},
    "Casein peptone": {"id": "FOODON:03315719", "label": "Casein peptone"},
    "Lab-Lemco beef extract": {"id": "FOODON:03302088", "label": "Beef extract"},
    "Malt extract": {"id": "FOODON:03301056", "label": "Malt extract"},
    "Meat peptone": {"id": "MICRO:0000176", "label": "Meat peptone"},
    "Peptone": {"id": "MICRO:0000178", "label": "Peptone"},
    "Proteose peptone no. 3": {
        "id": "MICRO:0000180",
        "label": "Proteose Peptone",
    },
    "Soil extract": {"id": "MICRO:0000457", "label": "Soil extract"},
    "Soytone": {"id": "FOODON:03315720", "label": "Soy peptone"},
    "Tomato juice": {"id": "FOODON:03301454", "label": "Tomato juice"},
    "Tryptone": {"id": "MICRO:0000182", "label": "Tryptone"},
    "Yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
}

CURATOR = "repair_komodo_score10_exact_terms_batch2.py"
ACTION = "GROUNDED_KOMODO_SCORE10_EXACT_TERMS_BATCH2"
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

        ingredient["term"] = copy.deepcopy(TERMS[preferred_term])
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
            "changes": "Grounded exact KOMODO score-10 ingredients",
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
