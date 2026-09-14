#!/usr/bin/env python3
"""Ground Tryptone and Yeast extract in duplicate Pyrobaculum score-10 records."""

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

TARGETS = (
    Path("archaea/JCM_J338_PYROBACULUM_CALIDIFONTIS_MEDIUM.yaml"),
    Path("archaea/pyrobaculum_calidifontis_medium.yaml"),
)
EXPECTED_IDS = {
    TARGETS[0]: "CultureMech:002697",
    TARGETS[1]: "CultureMech:000522",
}
IMPORTED_SIGNATURE = ("Tryptone", "Yeast extract", "Na2S2O3 x 5 H2O")

TRYPTONE_TERM = {"id": "MICRO:0000182", "label": "Tryptone"}
YEAST_EXTRACT_TERM = {"id": "FOODON:03315426", "label": "Yeast extract"}

CURATOR = "repair_pyrobaculum_score10.py"
ACTION = "GROUNDED_PYROBACULUM_SCORE10"
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


def repair_record(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_IDS[path]:
        raise ValueError(f"{path}: expected {EXPECTED_IDS[path]}, found {doc.get('id')!r}")
    if _ingredient_signature(doc) != IMPORTED_SIGNATURE:
        raise ValueError(f"{path}: ingredient signature drifted: {_ingredient_signature(doc)!r}")

    repaired = copy.deepcopy(doc)
    for ingredient in repaired["ingredients"]:
        if ingredient["preferred_term"] == "Tryptone":
            ingredient["term"] = copy.deepcopy(TRYPTONE_TERM)
        elif ingredient["preferred_term"] == "Yeast extract":
            ingredient["term"] = copy.deepcopy(YEAST_EXTRACT_TERM)

    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Grounded Pyrobaculum Tryptone and Yeast extract",
            "source": "src/culturemech/data/mediaingredientmech/label_index.csv",
            "notes": (
                "Applied exact MediaIngredientMech mappings: Tryptone to "
                "MICRO:0000182 and Yeast extract to FOODON:03315426."
            ),
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    paths = tuple(normalized / path for path in TARGETS)
    return {path: repair_record(path.relative_to(normalized), _load(path)) for path in paths}


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
