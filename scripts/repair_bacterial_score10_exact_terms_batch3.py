#!/usr/bin/env python3
"""Ground another batch of exact bacterial score-10 ingredient mappings."""

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
    Path("bacterial/enriched_cytophaga_agar.yaml"): (
        "Tryptone",
        "Beef extract",
        "Yeast extract",
        "Sodium acetate",
        "Agar",
    ),
    Path("bacterial/enriched_cytophaga_agar_medium.yaml"): (
        "Tryptone",
        "Beef extract",
        "Yeast extract",
        "Sodium acetate",
        "Agar",
    ),
    Path("bacterial/exiguobacterium_medium.yaml"): (
        "Nutrient broth No. 2",
        "Yeast extract",
        "Glucose",
    ),
    Path("bacterial/flavobacterium_aquatile_medium.yaml"): (
        "Na-caseinate",
        "Yeast extract",
        "Proteose peptone",
        "K2HPO4",
        "Agar",
    ),
    Path("bacterial/flavobacterium_m1_agar.yaml"): (
        "Proteose peptone",
        "Yeast extract",
        "Beef extract",
        "NaCl",
        "Agar",
    ),
    Path("bacterial/flavobacterium_medium.yaml"): (
        "Tryptone",
        "Yeast extract",
        "Na2SO4",
    ),
    Path("bacterial/glycerol_cornsteep_agar.yaml"): (
        "Glycerol",
        "Corn steep powder",
        "Yeast extract",
        "Beef extract",
        "Casein peptone",
        "NaCl",
        "Agar",
    ),
    Path("bacterial/glycerol_soil_medium.yaml"): (
        "Peptone",
        "Beef extract",
        "Glycerol",
        "Soil extract",
        "Agar",
    ),
    Path("bacterial/gyps_medium.yaml"): (
        "Glucose",
        "Yeast extract",
        "Peptone",
        "Sea Salt",
        "MES",
    ),
    Path("bacterial/hyphomonas_medium.yaml"): (
        "Casitone",
        "Yeast extract",
        "MgCl2 x 6 H2O",
    ),
    Path("bacterial/isp_1_medium.yaml"): (
        "Yeast extract",
        "Tryptone",
        "Agar",
    ),
    Path("bacterial/jcm_medium_no_116.yaml"): (
        "Potato",
        "Glucose",
        "Yeast extract",
    ),
    Path("bacterial/jxt_medium.yaml"): (
        "Yeast extract",
        "Trypticase peptone",
        "Na2S2O3 x 5 H2O",
        "Sea water",
    ),
    Path("bacterial/kdm_2_medium.yaml"): (
        "Peptone",
        "Yeast extract",
        "L-Cysteine HCl x H2O",
        "Agar",
        "Activated charcoal",
        "Fetal bovine serum",
    ),
    Path("bacterial/kunkee_medium.yaml"): (
        "Tryptone",
        "Peptone",
        "Yeast extract",
        "Glucose",
        "Tween 80",
        "Tomato juice",
    ),
    Path("bacterial/lactobacillus_medium_i.yaml"): (
        "Tryptone",
        "Tryptose",
        "Yeast extract",
        "Tomato juice",
        "Liver extract concentrate",
        "Tween 80",
        "Glucose",
        "Lactose",
        "Agar",
    ),
}

EXPECTED_IDS = {
    Path("bacterial/enriched_cytophaga_agar.yaml"): "CultureMech:003082",
    Path("bacterial/enriched_cytophaga_agar_medium.yaml"): "CultureMech:000569",
    Path("bacterial/exiguobacterium_medium.yaml"): "CultureMech:001597",
    Path("bacterial/flavobacterium_aquatile_medium.yaml"): "CultureMech:000451",
    Path("bacterial/flavobacterium_m1_agar.yaml"): "CultureMech:002882",
    Path("bacterial/flavobacterium_medium.yaml"): "CultureMech:002378",
    Path("bacterial/glycerol_cornsteep_agar.yaml"): "CultureMech:001707",
    Path("bacterial/glycerol_soil_medium.yaml"): "CultureMech:001954",
    Path("bacterial/gyps_medium.yaml"): "CultureMech:002799",
    Path("bacterial/hyphomonas_medium.yaml"): "CultureMech:001377",
    Path("bacterial/isp_1_medium.yaml"): "CultureMech:001232",
    Path("bacterial/jcm_medium_no_116.yaml"): "CultureMech:002342",
    Path("bacterial/jxt_medium.yaml"): "CultureMech:002586",
    Path("bacterial/kdm_2_medium.yaml"): "CultureMech:001543",
    Path("bacterial/kunkee_medium.yaml"): "CultureMech:001469",
    Path("bacterial/lactobacillus_medium_i.yaml"): "CultureMech:002368",
}

TARGET_TERMS = {
    Path("bacterial/enriched_cytophaga_agar.yaml"): (
        "Beef extract",
        "Tryptone",
        "Yeast extract",
    ),
    Path("bacterial/enriched_cytophaga_agar_medium.yaml"): (
        "Beef extract",
        "Tryptone",
        "Yeast extract",
    ),
    Path("bacterial/exiguobacterium_medium.yaml"): (
        "Nutrient broth No. 2",
        "Yeast extract",
    ),
    Path("bacterial/flavobacterium_aquatile_medium.yaml"): (
        "Proteose peptone",
        "Yeast extract",
    ),
    Path("bacterial/flavobacterium_m1_agar.yaml"): (
        "Beef extract",
        "Proteose peptone",
        "Yeast extract",
    ),
    Path("bacterial/flavobacterium_medium.yaml"): (
        "Tryptone",
        "Yeast extract",
    ),
    Path("bacterial/glycerol_cornsteep_agar.yaml"): (
        "Beef extract",
        "Casein peptone",
        "Yeast extract",
    ),
    Path("bacterial/glycerol_soil_medium.yaml"): (
        "Beef extract",
        "Peptone",
        "Soil extract",
    ),
    Path("bacterial/gyps_medium.yaml"): (
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/hyphomonas_medium.yaml"): (
        "Casitone",
        "Yeast extract",
    ),
    Path("bacterial/isp_1_medium.yaml"): (
        "Tryptone",
        "Yeast extract",
    ),
    Path("bacterial/jcm_medium_no_116.yaml"): ("Yeast extract",),
    Path("bacterial/jxt_medium.yaml"): (
        "Trypticase peptone",
        "Yeast extract",
    ),
    Path("bacterial/kdm_2_medium.yaml"): (
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/kunkee_medium.yaml"): (
        "Peptone",
        "Tomato juice",
        "Tryptone",
        "Yeast extract",
    ),
    Path("bacterial/lactobacillus_medium_i.yaml"): (
        "Liver extract concentrate",
        "Tomato juice",
        "Tryptone",
        "Tryptose",
        "Yeast extract",
    ),
}

TERMS = {
    "Beef extract": {"id": "FOODON:03302088", "label": "Beef extract"},
    "Casein peptone": {"id": "FOODON:03315719", "label": "Casein peptone"},
    "Casitone": {"id": "MICRO:0000606", "label": "Casitone"},
    "Liver extract concentrate": {
        "id": "MICRO:0001363",
        "label": "Liver extract concentrate",
    },
    "Nutrient broth No. 2": {
        "id": "MICRO:0000082",
        "label": "Nutrient broth No. 2",
    },
    "Peptone": {"id": "MICRO:0000178", "label": "Peptone"},
    "Proteose peptone": {"id": "MICRO:0000180", "label": "Proteose Peptone"},
    "Soil extract": {"id": "MICRO:0000457", "label": "Soil extract"},
    "Tomato juice": {"id": "FOODON:03301454", "label": "Tomato juice"},
    "Trypticase peptone": {
        "id": "MICRO:0000175",
        "label": "Trypticase peptone",
    },
    "Tryptone": {"id": "MICRO:0000182", "label": "Tryptone"},
    "Tryptose": {"id": "MICRO:0000183", "label": "Tryptose"},
    "Yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
}

CURATOR = "repair_bacterial_score10_exact_terms_batch3.py"
ACTION = "GROUNDED_BACTERIAL_SCORE10_EXACT_TERMS_BATCH3"
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
            "changes": "Grounded exact bacterial score-10 ingredients",
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
