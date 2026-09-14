#!/usr/bin/env python3
"""Ground a mixed eighth batch of exact score-10 ingredient mappings."""

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

MC_SIGNATURE = (
    "Casein",
    "Na2HPO4 x 7 H2O",
    "KH2PO4",
    "Yeast extract",
    "D-Glucose",
    "Liver digest",
    "Calf serum",
)
METHANOSAETA_SIGNATURE = (
    "Distilled water",
    "yeast extract",
    "NaCl",
    "CaCl2\u30fb2H2O",
    "KH2PO4",
    "NH4Cl",
    "Resazurin",
    "MgCl2\u30fb6H2O",
    "Na2S\u30fb9H2O",
    "Sodium acetate",
    "KHCO3",
    "tryptone (BD-Difco)",
    "L--Cysteine\u30fbHCl\u30fbH2O",
    "peptone",
    "Carbon dioxide gas",
    "Nitrogen gas",
)
MALT_EXTRACT_PEPTONE_SIGNATURE = (
    "Malt extract",
    "Soy peptone",
    "Agar",
)
MALTOSE_BENNETTS_SIGNATURE = (
    "Yeast extract",
    "Beef extract",
    "N-Z amine",
    "Maltose",
    "Agar",
)
SEA_SALTS_YP_SIGNATURE = (
    "Sea Salt",
    "NaCl",
    "Yeast extract",
    "Peptone",
    "Ferric citrate",
)
TRYPTICASE_SOY_YEAST_SIGNATURE = (
    "Trypticase soy broth",
    "Yeast extract",
    "Agar",
)
TRYPTONE_YEAST_MG_SIGNATURE = (
    "Tryptone",
    "Yeast extract",
    "MgSO4 x 7 H2O",
)
TRYPTONE_YEAST_AGAR_SIGNATURE = (
    "Tryptone",
    "Yeast extract",
    "Agar",
)
TRYPTONE_YEAST_NACL_SIGNATURE = (
    "Tryptone",
    "Yeast extract",
    "NaCl",
)
TRYPTONE_YEAST_CACL_SIGNATURE = (
    "Tryptone",
    "Yeast extract",
    "CaCl2 x 2 H2O",
)
JCM_J913_MARINE_SIGNATURE = (
    "Marine agar 2216",
    "Casitone",
    "Soytone",
    "Malt extract",
)
MODIFIED_BACTO_MARINE_SIGNATURE = (
    "Difco marine broth",
    "Pancreatic digest of casein",
    "Soy peptone",
    "Malt extract",
    "Agar",
)
MODIFIED_MARINE_1251_SIGNATURE = (
    "Marine agar 2216",
    "Casitone",
    "Phytone peptone",
    "Malt extract",
)


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    signature: tuple[str, ...]
    target_terms: tuple[str, ...]


TARGETS = (
    Target(
        Path("bacterial/mc.yaml"),
        "CultureMech:000359",
        MC_SIGNATURE,
        ("Casein", "Yeast extract"),
    ),
    Target(
        Path("bacterial/methanosaeta_brevibacterium_medium.yaml"),
        "CultureMech:002826",
        METHANOSAETA_SIGNATURE,
        ("tryptone (BD-Difco)", "yeast extract"),
    ),
    Target(
        Path("fungal/malt_extract_peptone_agar.yaml"),
        "CultureMech:010481",
        MALT_EXTRACT_PEPTONE_SIGNATURE,
        ("Malt extract", "Soy peptone"),
    ),
    Target(
        Path("fungal/maltose_bennetts_agar.yaml"),
        "CultureMech:010530",
        MALTOSE_BENNETTS_SIGNATURE,
        ("Beef extract", "Yeast extract"),
    ),
    Target(
        Path("fungal/sea_salts_yeast_extract_peptone_medium.yaml"),
        "CultureMech:010492",
        SEA_SALTS_YP_SIGNATURE,
        ("Peptone", "Yeast extract"),
    ),
    Target(
        Path("fungal/trypticase_soy_yeast_extract_medium.yaml"),
        "CultureMech:010482",
        TRYPTICASE_SOY_YEAST_SIGNATURE,
        ("Yeast extract",),
    ),
    Target(
        Path(
            "fungal/"
            "tryptone_yeast_extract_broth_isp_1_with_0_2_mgso_sub_4_sub_183_"
            "7h_sub_2_sub_o.yaml"
        ),
        "CultureMech:010545",
        TRYPTONE_YEAST_MG_SIGNATURE,
        ("Tryptone", "Yeast extract"),
    ),
    Target(
        Path("fungal/tryptone_yeast_extract_isp_1_agar.yaml"),
        "CultureMech:010551",
        TRYPTONE_YEAST_AGAR_SIGNATURE,
        ("Tryptone", "Yeast extract"),
    ),
    Target(
        Path("fungal/tryptone_yeast_extract_medium.yaml"),
        "CultureMech:010471",
        TRYPTONE_YEAST_NACL_SIGNATURE,
        ("Tryptone", "Yeast extract"),
    ),
    Target(
        Path("fungal/tryptone_yeast_extract_medium_modified.yaml"),
        "CultureMech:010460",
        TRYPTONE_YEAST_NACL_SIGNATURE,
        ("Tryptone", "Yeast extract"),
    ),
    Target(
        Path("fungal/tryptone_yeastextrakt_medium.yaml"),
        "CultureMech:010450",
        TRYPTONE_YEAST_CACL_SIGNATURE,
        ("Tryptone", "Yeast extract"),
    ),
    Target(
        Path("specialized/JCM_J913_MODIFIED_MARINE_AGAR_2216.yaml"),
        "CultureMech:015424",
        JCM_J913_MARINE_SIGNATURE,
        ("Casitone", "Malt extract", "Soytone"),
    ),
    Target(
        Path("specialized/modified_bacto_marine_broth.yaml"),
        "CultureMech:015359",
        MODIFIED_BACTO_MARINE_SIGNATURE,
        ("Malt extract", "Pancreatic digest of casein", "Soy peptone"),
    ),
    Target(
        Path("specialized/modified_marine_agar_2216.yaml"),
        "CultureMech:015396",
        MODIFIED_MARINE_1251_SIGNATURE,
        ("Casitone", "Malt extract", "Phytone peptone"),
    ),
)
TARGET_BY_PATH = {target.path: target for target in TARGETS}
EXPECTED_TARGET_COUNT = 14

TERMS = {
    "Beef extract": {"id": "FOODON:03302088", "label": "Beef extract"},
    "Casein": {"id": "FOODON:03420180", "label": "Casein"},
    "Casitone": {"id": "MICRO:0000606", "label": "Casitone"},
    "Malt extract": {"id": "FOODON:03301056", "label": "Malt extract"},
    "Pancreatic digest of casein": {"id": "MICRO:0000182", "label": "Tryptone"},
    "Peptone": {"id": "MICRO:0000178", "label": "Peptone"},
    "Phytone peptone": {"id": "FOODON:03315720", "label": "Soy peptone"},
    "Soy peptone": {"id": "FOODON:03315720", "label": "Soy peptone"},
    "Soytone": {"id": "FOODON:03315720", "label": "Soy peptone"},
    "Tryptone": {"id": "MICRO:0000182", "label": "Tryptone"},
    "Yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
    "tryptone (BD-Difco)": {"id": "MICRO:0000182", "label": "Tryptone"},
    "yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
}

CURATOR = "repair_mixed_score10_exact_terms_batch8.py"
ACTION = "GROUNDED_MIXED_SCORE10_EXACT_TERMS_BATCH8"
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
        raise ValueError(f"{path}: ingredient signature drifted: {_ingredient_signature(doc)!r}")

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
            "changes": "Grounded exact score-10 ingredients",
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
