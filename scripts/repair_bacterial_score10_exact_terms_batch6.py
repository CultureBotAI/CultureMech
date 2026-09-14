#!/usr/bin/env python3
"""Ground a sixth batch of exact bacterial score-10 ingredient mappings."""

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

NBRC_274_SIGNATURE = (
    "Bacto Tryptone",
    "Beef extract",
    "Yeast extract",
    "Sodium acetate",
    "Agar",
)
NEOMYCIN_AGAR_SIGNATURE = (
    "Beef extract",
    "Yeast extract",
    "Peptone",
    "Glucose",
    "Casitone",
    "Neomycin",
)
NUTRIENT_AGAR_SIGNATURE = (
    "Peptone",
    "Meat extract",
    "Agar",
)
NUTRIENT_BROTH_SIGNATURE = (
    "Bacto peptone",
    "Beef extract",
    "NaCl",
)
NUTRIMENT_AGAR_SIGNATURE = (
    "Peptone",
    "Meat extract",
    "Yeast extract",
    "NaCl",
    "Agar",
)
NY_AGAR_SIGNATURE = (
    "Peptone",
    "Meat extract",
    "Agar",
    "Yeast extract",
)
OXOID_NUTRIENT_BROTH_SIGNATURE = (
    "Nutrient broth",
    "Lab-Lemco beef extract",
    "Yeast extract",
    "Peptone",
    "NaCl",
)
PARACRAUROCOCCUS_BENNET_SIGNATURE = (
    "Glucose",
    "Yeast extract",
    "Beef extract",
    "Bacto peptone",
    "Agar",
)
PEREDIBACTER_DN_SIGNATURE = (
    "Nutrient broth",
    "Casamino acids",
    "Yeast extract",
    "CaCl2 x 2 H2O",
    "MgCl2 x 6 H2O",
)
R_AGAR_PH_9_SIGNATURE = (
    "Bacto peptone",
    "Yeast extract",
    "Malt extract",
    "Casamino acids",
    "Beef extract",
    "Glycerol",
    "Tween 80",
    "MgSO4 x 7 H2O",
    "Agar",
)
STANDARD_I_SIGNATURE = (
    "Meat peptone",
    "Casein peptone",
    "Yeast extract",
    "NaCl",
    "D(+)-Glucose",
)
SUCROSE_BENNETTS_SIGNATURE = (
    "Yeast extract",
    "Beef extract",
    "N-Z amine",
    "Sucrose",
    "Agar",
)
THERMUS_SP_SIGNATURE = (
    "Peptone",
    "Yeast extract",
    "NaCl",
)
THERMUS_THERMOPHILUS_SIGNATURE = (
    "Yeast extract",
    "Proteose peptone no. 3",
    "NaCl",
)
TOMATO_JUICE_SIGNATURE = (
    "Casein peptone",
    "Yeast extract",
    "Tomato juice",
    "Tween 80",
)
TRIS_YP_SIGNATURE = (
    "Yeast extract",
    "Peptone",
    "Tris-HCl buffer",
)
YM_AGAR_SIGNATURE = (
    "Glucose",
    "Peptone",
    "Yeast extract",
    "Malt extract",
    "Agar",
)
YPD_SIGNATURE = (
    "Yeast extract",
    "Peptone",
    "Glucose",
)


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    signature: tuple[str, ...]
    target_terms: tuple[str, ...]


TARGETS = (
    Target(
        Path("bacterial/nbrc_274_medium.yaml"),
        "CultureMech:000832",
        NBRC_274_SIGNATURE,
        ("Bacto Tryptone", "Beef extract", "Yeast extract"),
    ),
    Target(
        Path("bacterial/neomycin_agar.yaml"),
        "CultureMech:001407",
        NEOMYCIN_AGAR_SIGNATURE,
        ("Beef extract", "Casitone", "Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/nutrient_agar.yaml"),
        "CultureMech:001297",
        NUTRIENT_AGAR_SIGNATURE,
        ("Peptone",),
    ),
    *(
        Target(
            Path(f"bacterial/nutrient_broth_with_{salt}_nacl.yaml"),
            record_id,
            NUTRIENT_BROTH_SIGNATURE,
            ("Bacto peptone", "Beef extract"),
        )
        for salt, record_id in (
            ("0_5", "CultureMech:002463"),
            ("1_0", "CultureMech:003145"),
        )
    ),
    *(
        Target(
            Path(f"bacterial/{slug}.yaml"),
            record_id,
            NUTRIMENT_AGAR_SIGNATURE,
            ("Peptone", "Yeast extract"),
        )
        for slug, record_id in (
            ("nutriment_agar", "CultureMech:000717"),
            ("nutriment_agar_with_150_g_l_nacl", "CultureMech:000716"),
        )
    ),
    Target(
        Path("bacterial/ny_agar.yaml"),
        "CultureMech:001405",
        NY_AGAR_SIGNATURE,
        ("Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/oxoid_nutrient_broth.yaml"),
        "CultureMech:002127",
        OXOID_NUTRIENT_BROTH_SIGNATURE,
        ("Lab-Lemco beef extract", "Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/paracraurococcus_medium_bennet.yaml"),
        "CultureMech:001116",
        PARACRAUROCOCCUS_BENNET_SIGNATURE,
        ("Bacto peptone", "Beef extract", "Yeast extract"),
    ),
    Target(
        Path("bacterial/peredibacter_dn_medium.yaml"),
        "CultureMech:000432",
        PEREDIBACTER_DN_SIGNATURE,
        ("Casamino acids", "Yeast extract"),
    ),
    Target(
        Path("bacterial/r_agar_ph_9_0.yaml"),
        "CultureMech:002269",
        R_AGAR_PH_9_SIGNATURE,
        (
            "Bacto peptone",
            "Beef extract",
            "Casamino acids",
            "Malt extract",
            "Yeast extract",
        ),
    ),
    Target(
        Path("bacterial/standard_i_medium.yaml"),
        "CultureMech:001563",
        STANDARD_I_SIGNATURE,
        ("Casein peptone", "Meat peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/sucrose_bennetts_agar.yaml"),
        "CultureMech:001230",
        SUCROSE_BENNETTS_SIGNATURE,
        ("Beef extract", "Yeast extract"),
    ),
    Target(
        Path("bacterial/thermus_sp_medium.yaml"),
        "CultureMech:000468",
        THERMUS_SP_SIGNATURE,
        ("Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/thermus_thermophilus_medium.yaml"),
        "CultureMech:006401",
        THERMUS_THERMOPHILUS_SIGNATURE,
        ("Proteose peptone no. 3", "Yeast extract"),
    ),
    Target(
        Path("bacterial/tomato_juice_medium.yaml"),
        "CultureMech:001363",
        TOMATO_JUICE_SIGNATURE,
        ("Casein peptone", "Tomato juice", "Yeast extract"),
    ),
    Target(
        Path("bacterial/tris_yp_medium.yaml"),
        "CultureMech:004661",
        TRIS_YP_SIGNATURE,
        ("Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/ym_agar.yaml"),
        "CultureMech:002617",
        YM_AGAR_SIGNATURE,
        ("Malt extract", "Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/ypd_medium.yaml"),
        "CultureMech:001500",
        YPD_SIGNATURE,
        ("Peptone", "Yeast extract"),
    ),
)
TARGET_BY_PATH = {target.path: target for target in TARGETS}
EXPECTED_TARGET_COUNT = 20

TERMS = {
    "Bacto peptone": {"id": "MICRO:0000178", "label": "Bacto peptone"},
    "Bacto Tryptone": {"id": "MICRO:0000182", "label": "Tryptone"},
    "Beef extract": {"id": "FOODON:03302088", "label": "Beef extract"},
    "Casamino acids": {"id": "FOODON:03315719", "label": "Casamino acids"},
    "Casein peptone": {"id": "FOODON:03315719", "label": "Casein peptone"},
    "Casitone": {"id": "MICRO:0000606", "label": "Casitone"},
    "Lab-Lemco beef extract": {"id": "FOODON:03302088", "label": "Beef extract"},
    "Malt extract": {"id": "FOODON:03301056", "label": "Malt extract"},
    "Meat peptone": {"id": "MICRO:0000176", "label": "Meat peptone"},
    "Peptone": {"id": "MICRO:0000178", "label": "Peptone"},
    "Proteose peptone no. 3": {"id": "MICRO:0000180", "label": "Proteose Peptone"},
    "Tomato juice": {"id": "FOODON:03301454", "label": "Tomato juice"},
    "Yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
}

CURATOR = "repair_bacterial_score10_exact_terms_batch6.py"
ACTION = "GROUNDED_BACTERIAL_SCORE10_EXACT_TERMS_BATCH6"
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
