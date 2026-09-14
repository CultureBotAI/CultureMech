#!/usr/bin/env python3
"""Mark reviewed CCAP S/W + AMP and S/W + Ca recipes as curated sparse media."""

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

CURATOR = "repair_ccap_sw_flags_score20.py"
ACTION = "MARKED_CCAP_SW_SPARSE_SCORE20_GRAPH"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
SOURCE_ACTION = "SOURCE_CORRECTED_CCAP_DUPLICATE_RECIPE"

EXPECTED: dict[str, tuple[str, tuple[str, ...]]] = {
    "algae/s_w_amp.yaml": (
        "CultureMech:000136",
        (
            "Ammonium magnesium phosphate",
            "Air-dried sieved calcareous soil",
            "Deionized water",
        ),
    ),
    "bacterial/s_w_amp.yaml": (
        "CultureMech:000307",
        (
            "Ammonium magnesium phosphate",
            "Air-dried sieved calcareous soil",
            "Deionized water",
        ),
    ),
    "algae/s_w_ca.yaml": (
        "CultureMech:000137",
        (
            "Calcium carbonate",
            "Air-dried sieved calcareous soil",
            "Deionized water",
        ),
    ),
    "bacterial/s_w_ca.yaml": (
        "CultureMech:000308",
        (
            "Calcium carbonate",
            "Air-dried sieved calcareous soil",
            "Deionized water",
        ),
    ),
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _has_source_repair(doc: dict[str, Any]) -> bool:
    return any(
        isinstance(row, dict) and row.get("action") == SOURCE_ACTION
        for row in doc.get("curation_history") or []
    )


def _require_reviewed_sw_record(
    relative_path: str,
    doc: dict[str, Any],
    expected_id: str,
    expected_ingredients: tuple[str, ...],
) -> None:
    if doc.get("id") != expected_id:
        raise ValueError(
            f"{relative_path}: expected id {expected_id}, found {doc.get('id')!r}"
        )
    if not _has_source_repair(doc):
        raise ValueError(f"{relative_path}: missing reviewed CCAP PDF repair event")

    ingredient_names = tuple(
        str(row.get("preferred_term") or "")
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    )
    if ingredient_names != expected_ingredients:
        raise ValueError(f"{relative_path}: reviewed S/W ingredient signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    for flag in ("ingredients_curated", "has_unmapped_ingredients"):
        if flag not in flags:
            flags.append(flag)
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "notes": (
            "Marked reviewed CCAP S/W soil-water components as intentionally "
            "curated with unmapped bulk material identities."
        ),
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(
    relative_path: str,
    doc: dict[str, Any],
    expected_id: str,
    expected_ingredients: tuple[str, ...],
) -> dict[str, Any]:
    _require_reviewed_sw_record(relative_path, doc, expected_id, expected_ingredients)

    repaired = copy.deepcopy(doc)
    _ensure_flags(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for relative_path, (expected_id, expected_ingredients) in EXPECTED.items():
        path = normalized / relative_path
        plans[path] = repair_record(
            relative_path,
            _load(path),
            expected_id,
            expected_ingredients,
        )
    return plans


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
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
