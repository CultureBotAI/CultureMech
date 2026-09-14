#!/usr/bin/env python3
"""Ground exact extract mappings in simple bacterial score-10 records."""

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
    Path("bacterial/1_2_ytss_medium.yaml"): (
        "Yeast extract",
        "Tryptone",
        "Sea Salt",
        "Agar",
    ),
    Path("bacterial/2_x_yt_medium.yaml"): (
        "Tryptone",
        "Yeast extract",
        "NaCl",
    ),
    Path("bacterial/DSMZ_1405_PYG_MEDIUM_MODIFIED.yaml"): (
        "Peptone",
        "Meat extract",
        "Yeast extract",
        "Glucose",
        "Agar",
    ),
    Path("bacterial/DSMZ_73_MEDIUM_FOR_HALOPHILIC_BACILLI.yaml"): (
        "Casamino acids",
        "Yeast extract",
        "NaCl",
    ),
    Path("bacterial/DSMZ_74_THERMUS_THERMOPHILUS_MEDIUM.yaml"): (
        "Yeast extract",
        "Proteose peptone no. 3",
        "NaCl",
    ),
    Path("bacterial/JCM_J104_SUCROSE-BENNETT_S_AGAR.yaml"): (
        "Yeast extract",
        "Beef extract",
        "N-Z amine",
        "Sucrose",
        "Agar",
    ),
    Path("bacterial/JCM_J1178_BTT_MEDIUM.yaml"): (
        "Glucose",
        "Yeast extract",
        "Meat extract",
        "Casitone",
        "Agar",
    ),
    Path("bacterial/JCM_J1303_UREAPLASMA_MEDIUM.yaml"): (
        "PPLO broth",
        "Phenol red",
        "Hipolypepton",
        "Bovine calf serum",
        "Urea",
        "Yeast extract",
    ),
    Path("bacterial/JCM_J1351_PELOSINUS_BKL1_MEDIUM.yaml"): (
        "NaCl",
        "MgCl2·6H2O",
        "NaH2PO4·2H2O",
        "CaCl2·2H2O",
        "NH4Cl",
        "Yeast extract (BD-Difco)",
        "FeCl2 solution (see Medium No. 187 )",
        "Trace element solution (see Medium No. 187 )",
        "Distilled water",
        "8.0% NaHCO3 solution*",
        "Trace vitamins* (see Medium No. 197 )",
        "1.0 M Sodium lactate solution",
        "5% L-Cysteine·HCl·H2O solution",
    ),
}
EXPECTED_IDS = {
    Path("bacterial/1_2_ytss_medium.yaml"): "CultureMech:002156",
    Path("bacterial/2_x_yt_medium.yaml"): "CultureMech:002679",
    Path("bacterial/DSMZ_1405_PYG_MEDIUM_MODIFIED.yaml"): "CultureMech:000866",
    Path("bacterial/DSMZ_73_MEDIUM_FOR_HALOPHILIC_BACILLI.yaml"): "CultureMech:000280",
    Path("bacterial/DSMZ_74_THERMUS_THERMOPHILUS_MEDIUM.yaml"): "CultureMech:000282",
    Path("bacterial/JCM_J104_SUCROSE-BENNETT_S_AGAR.yaml"): "CultureMech:002232",
    Path("bacterial/JCM_J1178_BTT_MEDIUM.yaml"): "CultureMech:002349",
    Path("bacterial/JCM_J1303_UREAPLASMA_MEDIUM.yaml"): "CultureMech:002467",
    Path("bacterial/JCM_J1351_PELOSINUS_BKL1_MEDIUM.yaml"): "CultureMech:015835",
}

TERMS = {
    "Tryptone": {"id": "MICRO:0000182", "label": "Tryptone"},
    "Yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
    "Yeast extract (BD-Difco)": {"id": "FOODON:03315426", "label": "Yeast extract"},
}

CURATOR = "repair_bacterial_score10_extracts.py"
ACTION = "GROUNDED_BACTERIAL_EXTRACTS_SCORE10"
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


def repair_record(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_IDS[path]:
        raise ValueError(f"{path}: expected {EXPECTED_IDS[path]}, found {doc.get('id')!r}")
    if _ingredient_signature(doc) != TARGET_SIGNATURES[path]:
        raise ValueError(f"{path}: ingredient signature drifted: {_ingredient_signature(doc)!r}")

    repaired = copy.deepcopy(doc)
    grounded_names: list[str] = []
    for ingredient in repaired["ingredients"]:
        term = TERMS.get(ingredient["preferred_term"])
        if term is None:
            continue
        ingredient["term"] = copy.deepcopy(term)
        grounded_names.append(ingredient["preferred_term"])

    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Grounded exact bacterial extract mappings",
            "source": "src/culturemech/data/mediaingredientmech/label_index.csv",
            "notes": (
                "Applied exact MediaIngredientMech mappings for "
                f"{', '.join(sorted(grounded_names))}."
            ),
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
