#!/usr/bin/env python3
"""Ground a seventh batch of exact bacterial score-10 ingredient mappings."""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

NUTRIENT_BROTH_HORSE_SERUM_SIGNATURE = (
    "Peptone",
    "Meat extract",
    "Agar",
    "Horse serum",
)
OTTOW_SIGNATURE = (
    "Glucose",
    "Peptone",
    "Meat extract",
    "Yeast extract",
    "Casamino acids",
    "NaCl",
    "Tap water",
)
PEPTONE_MEAT_SOIL_SIGNATURE = (
    "Proteose peptone no. 3",
    "Meat extract",
    "Glycerol",
    "Soil extract",
    "Agar",
)
RCM_CASAMINO_SIGNATURE = (
    "dehydrated RCM medium",
    "Casamino acids",
    "Sodium resazurin",
)
REACTIVATION_SIGNATURE = (
    "Peptone",
    "Meat extract",
    "Agar",
)
KDM2_SIGNATURE = (
    "Bacto peptone",
    "Yeast extract",
    "L-Cysteine HCl x H2O",
    "Agar",
    "Fetal bovine serum",
)
RICH_SIGNATURE = (
    "Bacto peptone",
    "Yeast extract",
    "Casamino acids",
    "Meat extract",
    "Malt extract",
    "Glycerol",
    "MgSO4 x 7 H2O",
    "Tween 80",
    "Agar",
)
SALT_SIGNATURE = (
    "Tryptone",
    "Proteose peptone",
    "NaCl",
)
SARCINA_SIGNATURE = (
    "Glucose",
    "Peptone",
    "Yeast extract",
)
SEA_WATER_LB_SIGNATURE = (
    "Tryptone",
    "Yeast extract",
    "NaCl",
    "Sea water",
)
SEAWATER_LEMCO_SIGNATURE = (
    "Beef extract",
    "Peptone",
    "Sea water",
    "Agar",
)
SP4_SIGNATURE = (
    "Tryptone",
    "Peptone",
    "PPLO broth",
    "Fetal bovine serum",
    "CMRL 1066",
    "Yeast extract",
    "Phenol red",
    "L-Glutamine",
)
SP4_GLUCOSE_SIGNATURE = (
    "Glucose",
    "Tryptone",
    "Peptone",
    "PPLO broth",
    "Fetal bovine serum",
    "CMRL 1066",
    "Yeast extract",
    "Phenol red",
    "L-Glutamine",
)
SP4_Z_SIGNATURE = (
    "PPLO broth",
    "Tryptone",
    "Bacto peptone",
    "DNA",
    "CMRL 1066",
    "Yeast extract",
    "Fetal bovine serum",
    "Swine serum",
    "Glucose",
    "Urea",
    "Agar",
)
STREPTOMYCIN_NUTRIENT_SIGNATURE = (
    "Peptone",
    "Meat extract",
    "Agar",
    "Streptomycin sulfate",
)
SYP_SW_SIGNATURE = (
    "Starch",
    "Yeast extract",
    "Peptone",
    "Artificial Sea Salt",
    "Agar",
)
TSSY_SIGNATURE = (
    "Trypticase peptone",
    "Phytone peptone",
    "Yeast Nitrogen Base",
    "NaCl",
    "Agar",
)
TY_SIGNATURE = (
    "Tryptone",
    "Yeast extract",
    "CaCl2 x 2 H2O",
)
YTC_SIGNATURE = (
    "CaCl2 x 2 H2O",
    "Tryptone",
    "Yeast extract",
)


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    signature: tuple[str, ...]
    target_terms: tuple[str, ...]


TARGETS = (
    Target(
        Path("bacterial/nutrient_broth_with_10_horse_serum.yaml"),
        "CultureMech:001402",
        NUTRIENT_BROTH_HORSE_SERUM_SIGNATURE,
        ("Peptone",),
    ),
    Target(
        Path("bacterial/ottow_medium.yaml"),
        "CultureMech:001596",
        OTTOW_SIGNATURE,
        ("Casamino acids", "Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/peptone_meat_extract_soil_extract_agar_pfe.yaml"),
        "CultureMech:001350",
        PEPTONE_MEAT_SOIL_SIGNATURE,
        ("Proteose peptone no. 3", "Soil extract"),
    ),
    Target(
        Path("bacterial/rcm_medium_with_casamino_acids.yaml"),
        "CultureMech:001766",
        RCM_CASAMINO_SIGNATURE,
        ("Casamino acids",),
    ),
    Target(
        Path("bacterial/reactivation_with_liquid_medium_1.yaml"),
        "CultureMech:001298",
        REACTIVATION_SIGNATURE,
        ("Peptone",),
    ),
    Target(
        Path("bacterial/renibacterium_kdm_2_medium.yaml"),
        "CultureMech:002685",
        KDM2_SIGNATURE,
        ("Bacto peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/rich_medium.yaml"),
        "CultureMech:001872",
        RICH_SIGNATURE,
        ("Bacto peptone", "Casamino acids", "Malt extract", "Yeast extract"),
    ),
    Target(
        Path("bacterial/salt_medium.yaml"),
        "CultureMech:001328",
        SALT_SIGNATURE,
        ("Proteose peptone", "Tryptone"),
    ),
    Target(
        Path("bacterial/sarcina_medium.yaml"),
        "CultureMech:001322",
        SARCINA_SIGNATURE,
        ("Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/sea_water_luria_bertani_medium.yaml"),
        "CultureMech:001039",
        SEA_WATER_LB_SIGNATURE,
        ("Tryptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/seawater_lemco.yaml"),
        "CultureMech:001758",
        SEAWATER_LEMCO_SIGNATURE,
        ("Beef extract", "Peptone"),
    ),
    Target(
        Path("bacterial/sp4_medium.yaml"),
        "CultureMech:000508",
        SP4_SIGNATURE,
        ("Peptone", "Tryptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/sp4_medium_with_glucose.yaml"),
        "CultureMech:000509",
        SP4_GLUCOSE_SIGNATURE,
        ("Peptone", "Tryptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/sp4_z_medium.yaml"),
        "CultureMech:000510",
        SP4_Z_SIGNATURE,
        ("Bacto peptone", "Tryptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/streptomycin_nutrient_agar.yaml"),
        "CultureMech:001340",
        STREPTOMYCIN_NUTRIENT_SIGNATURE,
        ("Peptone",),
    ),
    Target(
        Path("bacterial/syp_sw_medium.yaml"),
        "CultureMech:000806",
        SYP_SW_SIGNATURE,
        ("Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/tssy_medium.yaml"),
        "CultureMech:002601",
        TSSY_SIGNATURE,
        ("Phytone peptone", "Trypticase peptone"),
    ),
    Target(
        Path("bacterial/ty_medium.yaml"),
        "CultureMech:000581",
        TY_SIGNATURE,
        ("Tryptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/ytc_medium.yaml"),
        "CultureMech:000844",
        YTC_SIGNATURE,
        ("Tryptone", "Yeast extract"),
    ),
)
TARGET_BY_PATH = {target.path: target for target in TARGETS}
EXPECTED_TARGET_COUNT = 19

TERMS = {
    "Bacto peptone": {"id": "MICRO:0000178", "label": "Bacto peptone"},
    "Beef extract": {"id": "FOODON:03302088", "label": "Beef extract"},
    "Casamino acids": {"id": "FOODON:03315719", "label": "Casamino acids"},
    "Malt extract": {"id": "FOODON:03301056", "label": "Malt extract"},
    "Peptone": {"id": "MICRO:0000178", "label": "Peptone"},
    "Phytone peptone": {"id": "FOODON:03315720", "label": "Soy peptone"},
    "Proteose peptone": {"id": "MICRO:0000180", "label": "Proteose Peptone"},
    "Proteose peptone no. 3": {"id": "MICRO:0000180", "label": "Proteose Peptone"},
    "Soil extract": {"id": "MICRO:0000457", "label": "Soil extract"},
    "Trypticase peptone": {
        "id": "MICRO:0000175",
        "label": "Trypticase peptone",
    },
    "Tryptone": {"id": "MICRO:0000182", "label": "Tryptone"},
    "Yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
}

CURATOR = "repair_bacterial_score10_exact_terms_batch7.py"
ACTION = "GROUNDED_BACTERIAL_SCORE10_EXACT_TERMS_BATCH7"
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


def _targeted_terms(target: Target) -> str:
    return ", ".join(target.target_terms)


def _validate_targets() -> None:
    if len(TARGETS) != EXPECTED_TARGET_COUNT or len(TARGETS) != len(TARGET_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_TARGET_COUNT} unique targets, found "
            f"{len(TARGETS)} total and {len(TARGET_BY_PATH)} unique"
        )


def repair_record(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    target = TARGET_BY_PATH[path]

    if doc.get("id") != target.record_id:
        raise ValueError(f"{path}: expected {target.record_id}, found {doc.get('id')!r}")
    if _ingredient_signature(doc) != target.signature:
        raise ValueError(
            f"{path}: ingredient signature drifted: {_ingredient_signature(doc)!r}"
        )

    expected_terms = set(target.target_terms)
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
            "changes": "Grounded bacterial score-10 exact ingredients",
            "source": "src/culturemech/data/mediaingredientmech/label_index.csv",
            "notes": f"Applied local mappings for {_targeted_terms(target)}.",
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    _validate_targets()
    return {
        normalized / target.path: repair_record(target.path, _load(normalized / target.path))
        for target in TARGETS
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
