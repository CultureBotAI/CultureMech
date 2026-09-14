#!/usr/bin/env python3
"""Ground low-hanging exact JCM score-10 ingredient mappings."""

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
    Path("archaea/JCM_J1423_METHANOBREVIBACTER_CURVATUS_MEDIUM.yaml"): (
        "Rumen fluid, clarified (see Medium No. 266)",
        "NaCl",
        "KCl",
        "MgCl2\u00b76H2O",
        "CaCl2\u00b72H2O",
        "NH4Cl",
        "KH2PO4",
        "Na2SO4",
        "Casamino acids (BD Difco)",
        "Yeast extract (Oxoid)",
        "Nutrient broth (BD Difco)",
        "FeCl2 solution (see Medium No. 187 )",
        "Trace element solution (see Medium No. 187 )",
        "Selenite-tungstate solution (see Medium No. 431 )",
        "Resazurin",
        "Distilled water",
        "8% NaHCO3 solution*",
        "1.0 M HEPES solution (pH 7.2)",
        "Vitamin solution (see Medium No. 898 )",
        "0.1 M Dithiothreitol solution",
    ),
    Path("archaea/JCM_J1424_METHANOBREVIBACTER_CUTICULARIS_MEDIUM.yaml"): (
        "Rumen fluid, clarified (see Medium No. 266)",
        "NaCl",
        "KCl",
        "MgCl2\u00b76H2O",
        "CaCl2\u00b72H2O",
        "NH4Cl",
        "KH2PO4",
        "Na2SO4",
        "Casamino acids (BD Difco)",
        "Yeast extract (Oxoid)",
        "FeCl2 solution (see Medium No. 187 )",
        "Trace element solution (see Medium No. 187 )",
        "Selenite-tungstate solution (see Medium No. 431 )",
        "Resazurin",
        "Distilled water",
        "8% NaHCO3 solution*",
        "1.0 M HEPES solution (pH 7.7)",
        "Vitamin solution (see Medium No. 898 )",
        "0.1 M Dithiothreitol solution",
    ),
    Path("bacterial/JCM_J1404_MINERAL_CARBONATE_MEDIUM_WITH_CELLOBIOSE.yaml"): (
        "Na2CO3",
        "NaHCO3",
        "NaCl",
        "K2HPO4",
        "Yeast extract",
        "1 M MgSO4 solution",
        "1 M NH4Cl solution",
        "Trace element solution (see Medium No. 1079 )",
        "Trace vitamins* (see Medium No. 197 )",
        "10% Cellobiose solution*",
    ),
    Path("bacterial/JCM_J1429_M1H_NAG_ASW.yaml"): (
        "HEPES",
        "Peptone",
        "Yeast extract (BD-Difco)",
        "Wolfe's mineral solution (see Medium No. 265 )",
        "Modified Hutner's basal salts (see Medium No. 900 )",
        "Artificial seawater",
        "Distilled water",
        "Glucose",
        "N -Acetyl-D-glucosamine",
        "Trace vitamins (see Medium No. 197 )",
        "Distilled water",
    ),
    Path("bacterial/JCM_J1444_DESULFOSPOROSINUS_SB140_MEDIUM.yaml"): (
        "(NH4)2SO4",
        "KH2PO4",
        "MgSO4-7H2O",
        "KCl",
        "Yeast extract",
        "Ca(NO3)2\u20224H2O",
        "Na2SO4",
        "Trace element solution (see Medium No. 439 )",
        "L-Cysteine\u2022HCl\u2022H2O",
        "Resazurin",
        "Distilled water",
        "5% Na2HPO4 solution",
        "5% KH2PO4 solution",
        "1M Glycerin solution",
        "Trace vitamins* (see Medium No. 197 )",
    ),
    Path("bacterial/JCM_J1468_FRESHWATER_R2A_MEDIUM.yaml"): (
        "Yeast extract (BD-Difco)",
        "Proteose peptone No. 3 (BD-Difco)",
        "Casamino acids (BD-Difco)",
        "Glucose",
        "KH2PO4",
        "Soluble starch",
        "Sodium pyruvate",
        "NH4Cl",
        "FeCl2 solution (see Medium No. 187 )",
        "Trace element solution (see Medium No. 187 )",
        "Selenite tungstate solution (see Medium No. 431 )",
        "Vitamin solution* (see Medium No. 403 )",
        "Thiamine solution* (see Medium No. 403 )",
        "Vitamin B12 solution* (see Medium No. 403 )",
        "Resazurin",
        "Distilled water",
        "1 M NaHCO3 solution",
        "1 M Coenzyme M solution",
        "5% Na2S\u00b79H2O solution",
    ),
}

EXPECTED_IDS = {
    Path("archaea/JCM_J1423_METHANOBREVIBACTER_CURVATUS_MEDIUM.yaml"): "CultureMech:015860",
    Path("archaea/JCM_J1424_METHANOBREVIBACTER_CUTICULARIS_MEDIUM.yaml"): "CultureMech:015861",
    Path("bacterial/JCM_J1404_MINERAL_CARBONATE_MEDIUM_WITH_CELLOBIOSE.yaml"): (
        "CultureMech:015854"
    ),
    Path("bacterial/JCM_J1429_M1H_NAG_ASW.yaml"): "CultureMech:015864",
    Path("bacterial/JCM_J1444_DESULFOSPOROSINUS_SB140_MEDIUM.yaml"): (
        "CultureMech:015868"
    ),
    Path("bacterial/JCM_J1468_FRESHWATER_R2A_MEDIUM.yaml"): "CultureMech:015874",
}

TARGET_TERMS = {
    Path("archaea/JCM_J1423_METHANOBREVIBACTER_CURVATUS_MEDIUM.yaml"): (
        "Casamino acids (BD Difco)",
        "Yeast extract (Oxoid)",
    ),
    Path("archaea/JCM_J1424_METHANOBREVIBACTER_CUTICULARIS_MEDIUM.yaml"): (
        "Casamino acids (BD Difco)",
        "Yeast extract (Oxoid)",
    ),
    Path("bacterial/JCM_J1404_MINERAL_CARBONATE_MEDIUM_WITH_CELLOBIOSE.yaml"): (
        "Yeast extract",
    ),
    Path("bacterial/JCM_J1429_M1H_NAG_ASW.yaml"): (
        "Peptone",
        "Yeast extract (BD-Difco)",
    ),
    Path("bacterial/JCM_J1444_DESULFOSPOROSINUS_SB140_MEDIUM.yaml"): (
        "MgSO4-7H2O",
        "Yeast extract",
        "L-Cysteine\u2022HCl\u2022H2O",
    ),
    Path("bacterial/JCM_J1468_FRESHWATER_R2A_MEDIUM.yaml"): (
        "Yeast extract (BD-Difco)",
        "Proteose peptone No. 3 (BD-Difco)",
        "Casamino acids (BD-Difco)",
    ),
}

TERMS = {
    "Casamino acids (BD Difco)": {
        "id": "FOODON:03315719",
        "label": "Casamino acids",
    },
    "Casamino acids (BD-Difco)": {
        "id": "FOODON:03315719",
        "label": "Casamino acids",
    },
    "L-Cysteine\u2022HCl\u2022H2O": {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    },
    "MgSO4-7H2O": {
        "id": "CHEBI:31795",
        "label": "magnesium sulfate heptahydrate",
    },
    "Peptone": {"id": "MICRO:0000178", "label": "Peptone"},
    "Proteose peptone No. 3 (BD-Difco)": {
        "id": "MICRO:0000180",
        "label": "Proteose Peptone",
    },
    "Yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
    "Yeast extract (BD-Difco)": {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    },
    "Yeast extract (Oxoid)": {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    },
}

CURATOR = "repair_jcm_score10_exact_terms.py"
ACTION = "GROUNDED_JCM_SCORE10_EXACT_TERMS"
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

        term = copy.deepcopy(TERMS[preferred_term])
        ingredient["term"] = term
        grounded_terms.add(preferred_term)
        if term["id"].startswith("CHEBI:"):
            ingredient["mediaingredientmech_chebi_term"] = copy.deepcopy(term)

    if grounded_terms != expected_terms:
        missing = ", ".join(sorted(expected_terms - grounded_terms))
        raise ValueError(f"{path}: missing targeted ingredient(s): {missing}")

    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Grounded direct JCM score-10 ingredients",
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
