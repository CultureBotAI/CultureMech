#!/usr/bin/env python3
"""Ground a fifth batch of exact bacterial score-10 ingredient mappings."""

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

MEDIUM_948_SIGNATURE = (
    "Nutrient broth",
    "Lab-Lemco beef extract",
    "Yeast extract",
    "Peptone",
    "NaCl",
)
ERYTHROBACTER_LONGUS_SIGNATURE = (
    "Peptone",
    "Soytone",
    "Yeast extract",
    "Proteose peptone no. 3",
    "Fe(III) citrate",
    "Sea water",
)
MICROCOCCUS_SIGNATURE = (
    "Peptone",
    "Beef extract",
    "Yeast extract",
    "Glucose",
    "Agar",
)
MICROVIRGA_HV12_SIGNATURE = (
    "Malt extract",
    "Yeast extract",
    "Peptone",
    "NaCl",
)
MODIFIED_LB_SIGNATURE = (
    "Peptone",
    "Yeast extract",
    "Sea Salt",
    "Agar",
)
MODIFIED_MEDIUM_514_SIGNATURE = (
    "Difco Marine Broth 2216",
    "Pancreatic digest of casein",
    "Soy peptone",
    "Malt extract",
    "Agar",
)
MODIFIED_MH_SIGNATURE = (
    "Yeast extract",
    "Proteose peptone no. 3",
    "Glucose",
    "X10 Jamarin S",
)
MODIFIED_NUTRIENT_AGAR_SIGNATURE = (
    "Peptone",
    "Meat extract",
    "Agar",
    "Sea water",
)
MODIFIED_PYES_SIGNATURE = (
    "Casein peptone",
    "Yeast extract",
    "Agar",
)
MODIFIED_THERMUS_SIGNATURE = (
    "Polypeptone",
    "Yeast extract",
    "Agar",
)
MRS_TOMATO_JUICE_SIGNATURE = (
    "MRS broth",
    "L-Cysteine HCl x H2O",
    "Tomato juice",
)


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    signature: tuple[str, ...]
    target_terms: tuple[str, ...]


TARGETS = (
    Target(
        Path("bacterial/medium_948_modified_for_dsm_16823.yaml"),
        "CultureMech:006885",
        MEDIUM_948_SIGNATURE,
        ("Lab-Lemco beef extract", "Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/medium_for_erythrobacter_longus.yaml"),
        "CultureMech:001832",
        ERYTHROBACTER_LONGUS_SIGNATURE,
        ("Peptone", "Proteose peptone no. 3", "Soytone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/micrococcus_medium.yaml"),
        "CultureMech:001462",
        MICROCOCCUS_SIGNATURE,
        ("Beef extract", "Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/microvirga_medium_hv12.yaml"),
        "CultureMech:001025",
        MICROVIRGA_HV12_SIGNATURE,
        ("Malt extract", "Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/modified_lb.yaml"),
        "CultureMech:001487",
        MODIFIED_LB_SIGNATURE,
        ("Peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/modified_medium_514_for_halomonas_sp.yaml"),
        "CultureMech:000982",
        MODIFIED_MEDIUM_514_SIGNATURE,
        ("Malt extract", "Pancreatic digest of casein", "Soy peptone"),
    ),
    Target(
        Path("bacterial/modified_mh_medium.yaml"),
        "CultureMech:002956",
        MODIFIED_MH_SIGNATURE,
        ("Proteose peptone no. 3", "Yeast extract"),
    ),
    Target(
        Path("bacterial/modified_nutrient_agar.yaml"),
        "CultureMech:000775",
        MODIFIED_NUTRIENT_AGAR_SIGNATURE,
        ("Peptone",),
    ),
    Target(
        Path("bacterial/modified_pyes_medium.yaml"),
        "CultureMech:002112",
        MODIFIED_PYES_SIGNATURE,
        ("Casein peptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/modified_thermus_medium.yaml"),
        "CultureMech:001038",
        MODIFIED_THERMUS_SIGNATURE,
        ("Yeast extract",),
    ),
    Target(
        Path("bacterial/mrs_medium_with_10_tomato_juice.yaml"),
        "CultureMech:003148",
        MRS_TOMATO_JUICE_SIGNATURE,
        ("Tomato juice",),
    ),
)
TARGET_BY_PATH = {target.path: target for target in TARGETS}
EXPECTED_TARGET_COUNT = 11

TERMS = {
    "Beef extract": {"id": "FOODON:03302088", "label": "Beef extract"},
    "Casein peptone": {"id": "FOODON:03315719", "label": "Casein peptone"},
    "Lab-Lemco beef extract": {"id": "FOODON:03302088", "label": "Beef extract"},
    "Malt extract": {"id": "FOODON:03301056", "label": "Malt extract"},
    "Pancreatic digest of casein": {"id": "MICRO:0000182", "label": "Tryptone"},
    "Peptone": {"id": "MICRO:0000178", "label": "Peptone"},
    "Proteose peptone no. 3": {"id": "MICRO:0000180", "label": "Proteose Peptone"},
    "Soy peptone": {"id": "FOODON:03315720", "label": "Soy peptone"},
    "Soytone": {"id": "FOODON:03315720", "label": "Soy peptone"},
    "Tomato juice": {"id": "FOODON:03301454", "label": "Tomato juice"},
    "Yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
}

CURATOR = "repair_bacterial_score10_exact_terms_batch5.py"
ACTION = "GROUNDED_BACTERIAL_SCORE10_EXACT_TERMS_BATCH5"
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
