#!/usr/bin/env python3
"""Ground exact bacterial score-10 ingredient mappings."""

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
    Path("bacterial/acidomonas_medium.yaml"): (
        "Glucose",
        "Peptone",
        "Yeast extract",
        "Malt extract",
        "Agar",
    ),
    Path("bacterial/alifodinibius_medium_tsa_mod.yaml"): (
        "Tryptone",
        "Bacto Soytone",
        "NaCl",
    ),
    Path("bacterial/antarctic_bacterial_medium.yaml"): (
        "Bacto peptone",
        "Yeast extract",
        "Agar",
    ),
    Path("bacterial/antibiotic_medium_1.yaml"): (
        "Yeast extract",
        "Beef extract",
        "Pancreatic digest of casein",
        "Peptone",
        "Glucose",
        "Agar",
    ),
    Path("bacterial/bacillus_thermantarcticus_medium.yaml"): (
        "Yeast extract",
        "NaCl",
        "Soil extract",
    ),
    Path("bacterial/bdellovibrio_yp_medium.yaml"): (
        "Yeast extract",
        "Peptone",
        "Tris-HCl buffer",
    ),
    Path("bacterial/beer_medium.yaml"): (
        "MgSO4・7H2O",
        "K2HPO4",
        "Sodium acetate",
        "Tween 80",
        "MnSO4・xH2O",
        "Diammonium citrate",
        "Glucose",
        "hopped beer",
        "Yeast extract (BD-Difco)",
        "Beef extract (BD-Difco)",
        "Casein peptone, tryptic digest",
    ),
    Path("bacterial/bennetts_agar.yaml"): (
        "Beef extract",
        "Glucose",
        "N-Z amine",
        "Yeast extract",
        "Agar",
    ),
    Path("bacterial/blood_agar_ii.yaml"): (
        "Defibrinated sheep blood",
        "Casein peptone",
        "Soy peptone",
        "NaCl",
        "Agar",
    ),
    Path("bacterial/bsw3_agar.yaml"): (
        "Yeast extract",
        "Malt extract",
        "Glucose",
        "Agar",
        "Sea water",
    ),
    Path("bacterial/btt_medium.yaml"): (
        "Glucose",
        "Yeast extract",
        "Meat extract",
        "Casitone",
        "Agar",
    ),
    Path("bacterial/columbia_agar_with_5_sheep_blood.yaml"): (
        "Defibrinated Blood",
        "Bacto peptone",
        "Tryptic Digest of beef heart",
        "Corn starch",
        "NaCl",
        "Agar",
        "Casein peptone",
        "Soy peptone",
    ),
    Path("bacterial/cyc_agar.yaml"): (
        "Czapek-Dox liquid medium",
        "Yeast extract",
        "Casamino acids",
        "Agar",
    ),
    Path("bacterial/cyc_agar_ph_8_0.yaml"): (
        "Czapek-Dox liquid medium",
        "Yeast extract",
        "Casamino acids",
        "Agar",
    ),
}

EXPECTED_IDS = {
    Path("bacterial/acidomonas_medium.yaml"): "CultureMech:002396",
    Path("bacterial/alifodinibius_medium_tsa_mod.yaml"): "CultureMech:001024",
    Path("bacterial/antarctic_bacterial_medium.yaml"): "CultureMech:002690",
    Path("bacterial/antibiotic_medium_1.yaml"): "CultureMech:001010",
    Path("bacterial/bacillus_thermantarcticus_medium.yaml"): "CultureMech:001815",
    Path("bacterial/bdellovibrio_yp_medium.yaml"): "CultureMech:001356",
    Path("bacterial/beer_medium.yaml"): "CultureMech:002778",
    Path("bacterial/bennetts_agar.yaml"): "CultureMech:001682",
    Path("bacterial/blood_agar_ii.yaml"): "CultureMech:001345",
    Path("bacterial/bsw3_agar.yaml"): "CultureMech:002385",
    Path("bacterial/btt_medium.yaml"): "CultureMech:000543",
    Path("bacterial/columbia_agar_with_5_sheep_blood.yaml"): (
        "CultureMech:000788"
    ),
    Path("bacterial/cyc_agar.yaml"): "CultureMech:002851",
    Path("bacterial/cyc_agar_ph_8_0.yaml"): "CultureMech:002580",
}

TARGET_TERMS = {
    Path("bacterial/acidomonas_medium.yaml"): (
        "Malt extract",
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/alifodinibius_medium_tsa_mod.yaml"): (
        "Bacto Soytone",
        "Tryptone",
    ),
    Path("bacterial/antarctic_bacterial_medium.yaml"): (
        "Bacto peptone",
        "Yeast extract",
    ),
    Path("bacterial/antibiotic_medium_1.yaml"): (
        "Beef extract",
        "Pancreatic digest of casein",
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/bacillus_thermantarcticus_medium.yaml"): (
        "Soil extract",
        "Yeast extract",
    ),
    Path("bacterial/bdellovibrio_yp_medium.yaml"): (
        "Peptone",
        "Yeast extract",
    ),
    Path("bacterial/beer_medium.yaml"): (
        "Beef extract (BD-Difco)",
        "Casein peptone, tryptic digest",
        "Yeast extract (BD-Difco)",
    ),
    Path("bacterial/bennetts_agar.yaml"): (
        "Beef extract",
        "Yeast extract",
    ),
    Path("bacterial/blood_agar_ii.yaml"): (
        "Casein peptone",
        "Soy peptone",
    ),
    Path("bacterial/bsw3_agar.yaml"): (
        "Malt extract",
        "Yeast extract",
    ),
    Path("bacterial/btt_medium.yaml"): (
        "Casitone",
        "Yeast extract",
    ),
    Path("bacterial/columbia_agar_with_5_sheep_blood.yaml"): (
        "Bacto peptone",
        "Casein peptone",
        "Soy peptone",
    ),
    Path("bacterial/cyc_agar.yaml"): (
        "Casamino acids",
        "Yeast extract",
    ),
    Path("bacterial/cyc_agar_ph_8_0.yaml"): (
        "Casamino acids",
        "Yeast extract",
    ),
}

TERMS = {
    "Bacto peptone": {"id": "MICRO:0000178", "label": "Bacto peptone"},
    "Bacto Soytone": {"id": "FOODON:03315720", "label": "Soy peptone"},
    "Beef extract": {"id": "FOODON:03302088", "label": "Beef extract"},
    "Beef extract (BD-Difco)": {
        "id": "FOODON:03302088",
        "label": "Beef extract",
    },
    "Casamino acids": {"id": "FOODON:03315719", "label": "Casamino acids"},
    "Casein peptone": {"id": "FOODON:03315719", "label": "Casein peptone"},
    "Casein peptone, tryptic digest": {
        "id": "FOODON:03315719",
        "label": "Casein peptone",
    },
    "Casitone": {"id": "MICRO:0000606", "label": "Casitone"},
    "Malt extract": {"id": "FOODON:03301056", "label": "Malt extract"},
    "Pancreatic digest of casein": {
        "id": "MICRO:0000182",
        "label": "Tryptone",
    },
    "Peptone": {"id": "MICRO:0000178", "label": "Peptone"},
    "Soil extract": {"id": "MICRO:0000457", "label": "Soil extract"},
    "Soy peptone": {"id": "FOODON:03315720", "label": "Soy peptone"},
    "Tryptone": {"id": "MICRO:0000182", "label": "Tryptone"},
    "Yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
    "Yeast extract (BD-Difco)": {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    },
}

CURATOR = "repair_bacterial_score10_exact_terms_batch2.py"
ACTION = "GROUNDED_BACTERIAL_SCORE10_EXACT_TERMS_BATCH2"
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
        str(row.get("preferred_term") or "")
        for row in ingredients
        if isinstance(row, dict)
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
