#!/usr/bin/env python3
"""Ground bacterial/KOMODO score-10 exact ingredient mappings."""

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

LB_LENNOX_SIGNATURE = (
    "Tryptone",
    "Yeast extract",
    "NaCl",
)
MALT_EXTRACT_PEPTONE_SIGNATURE = (
    "Malt extract",
    "Soy peptone",
    "Agar",
)
MEDIUM_381_SIGNATURE = (
    "Peptone",
    "Yeast extract",
    "Sea Salt",
    "Agar",
)
MEDIUM_453_SIGNATURE = (
    "Meat peptone",
    "Casein peptone",
    "Yeast extract",
    "NaCl",
    "D(+)-Glucose",
)
MEDIUM_548_SIGNATURE = (
    "Beef extract",
    "Glucose",
    "N-Z amine",
    "Yeast extract",
    "Agar",
)
MEDIUM_736_SIGNATURE = (
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
MEDIUM_1143_SIGNATURE = (
    "Tryptone",
    "Yeast extract",
    "CaCl2 x 2 H2O",
)
HALOPHILIC_BACILLI_SIGNATURE = (
    "Casamino acids",
    "Yeast extract",
    "NaCl",
)


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    signature: tuple[str, ...]
    target_terms: tuple[str, ...]


TARGETS = (
    Target(
        Path("bacterial/lb_luria_bertani_medium_lennox.yaml"),
        "CultureMech:002403",
        LB_LENNOX_SIGNATURE,
        ("Tryptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/malt_extract_peptone_agar.yaml"),
        "CultureMech:006782",
        MALT_EXTRACT_PEPTONE_SIGNATURE,
        ("Malt extract", "Soy peptone"),
    ),
    Target(
        Path("bacterial/medium_1143_modified_for_dsm_23293.yaml"),
        "CultureMech:003853",
        MEDIUM_1143_SIGNATURE,
        ("Tryptone", "Yeast extract"),
    ),
    Target(
        Path("bacterial/medium_548_modified_for_dsm_41755.yaml"),
        "CultureMech:005992",
        MEDIUM_548_SIGNATURE,
        ("Beef extract", "Yeast extract"),
    ),
    Target(
        Path("bacterial/medium_736_modified_for_dsm_22413.yaml"),
        "CultureMech:006383",
        MEDIUM_736_SIGNATURE,
        ("Bacto peptone", "Casamino acids", "Malt extract", "Yeast extract"),
    ),
    Target(
        Path("bacterial/medium_for_halophilic_bacilli.yaml"),
        "CultureMech:006389",
        HALOPHILIC_BACILLI_SIGNATURE,
        ("Casamino acids", "Yeast extract"),
    ),
    *(
        Target(
            Path(f"bacterial/medium_381_modified_for_dsm_{dsm}.yaml"),
            record_id,
            MEDIUM_381_SIGNATURE,
            ("Peptone", "Yeast extract"),
        )
        for dsm, record_id in (
            ("12449", "CultureMech:005117"),
            ("15370", "CultureMech:005118"),
            ("17298", "CultureMech:005119"),
            ("18339", "CultureMech:005120"),
            ("22074", "CultureMech:005121"),
            ("2304", "CultureMech:005122"),
            ("23293", "CultureMech:005123"),
            ("6188", "CultureMech:005124"),
            ("6256", "CultureMech:005125"),
            ("7123", "CultureMech:005126"),
            ("7144", "CultureMech:005127"),
        )
    ),
    *(
        Target(
            Path(f"bacterial/medium_453_modified_for_dsm_{dsm}.yaml"),
            record_id,
            MEDIUM_453_SIGNATURE,
            ("Casein peptone", "Meat peptone", "Yeast extract"),
        )
        for dsm, record_id in (
            ("43934", "CultureMech:005292"),
            ("6341", "CultureMech:005293"),
            ("6349", "CultureMech:005294"),
            ("6364", "CultureMech:005295"),
            ("6366", "CultureMech:005296"),
            ("6406", "CultureMech:005297"),
            ("6453", "CultureMech:005298"),
            ("6454", "CultureMech:005299"),
            ("6455", "CultureMech:005300"),
            ("6458", "CultureMech:005301"),
            ("6472", "CultureMech:005302"),
        )
    ),
)
TARGET_BY_PATH = {target.path: target for target in TARGETS}
EXPECTED_TARGET_COUNT = 28

TERMS = {
    "Bacto peptone": {"id": "MICRO:0000178", "label": "Bacto peptone"},
    "Beef extract": {"id": "FOODON:03302088", "label": "Beef extract"},
    "Casamino acids": {"id": "FOODON:03315719", "label": "Casamino acids"},
    "Casein peptone": {"id": "FOODON:03315719", "label": "Casein peptone"},
    "Malt extract": {"id": "FOODON:03301056", "label": "Malt extract"},
    "Meat peptone": {"id": "MICRO:0000176", "label": "Meat peptone"},
    "Peptone": {"id": "MICRO:0000178", "label": "Peptone"},
    "Soy peptone": {"id": "FOODON:03315720", "label": "Soy peptone"},
    "Tryptone": {"id": "MICRO:0000182", "label": "Tryptone"},
    "Yeast extract": {"id": "FOODON:03315426", "label": "Yeast extract"},
}

CURATOR = "repair_bacterial_komodo_score10_exact_terms_batch4.py"
ACTION = "GROUNDED_BACTERIAL_KOMODO_SCORE10_EXACT_TERMS_BATCH4"
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
            "changes": "Grounded bacterial/KOMODO score-10 exact ingredients",
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
