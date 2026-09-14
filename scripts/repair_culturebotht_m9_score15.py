#!/usr/bin/env python3
"""Normalize CultureBotHT M9 source provenance for score-15 review."""

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
TARGET = Path("specialized/m9.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_culturebotht_m9_score15.py"
ACTION = "NORMALIZED_CULTUREBOTHT_M9_SOURCE"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

EXPECTED_ID = "CultureMech:015542"
SOURCE_ID = "M9"
CULTUREBOTHT_URL = "https://github.com/CultureBotAI/CultureBotHT"
EXPECTED_INGREDIENTS = (
    "D-Glucose",
    "Magnesium sulfate",
    "Calcium chloride",
    "Sodium phosphate dibasic heptahydrate",
    "Potassium phosphate monobasic",
    "Sodium Chloride",
    "Ammonium chloride",
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    if key in doc:
        doc[key] = value
        return

    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True
    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _component_names(doc: dict[str, Any]) -> tuple[str, ...]:
    return tuple(
        str(row.get("preferred_term") or "")
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    )


def _has_culturebotht_source(doc: dict[str, Any]) -> bool:
    sources = doc.get("sources") or []
    if isinstance(sources, list):
        for source in sources:
            if (
                isinstance(source, dict)
                and source.get("database") == "CultureBotHT"
                and source.get("database_id") == SOURCE_ID
            ):
                return True

    source_data = doc.get("source_data")
    return (
        isinstance(source_data, dict)
        and source_data.get("origin") == "CultureBotHT"
        and f"database_id: {SOURCE_ID};" in str(source_data.get("notes") or "")
    )


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _component_names(doc) != EXPECTED_INGREDIENTS:
        raise ValueError(f"{TARGET}: CultureBotHT M9 ingredient list drifted")
    if not _has_culturebotht_source(doc):
        raise ValueError(f"{TARGET}: missing CultureBotHT source {SOURCE_ID!r}")


def _ensure_sources(doc: dict[str, Any]) -> None:
    source = {
        "database": "CultureBotHT",
        "database_id": SOURCE_ID,
        "url": CULTUREBOTHT_URL,
    }
    sources = doc.setdefault("sources", [])
    if not isinstance(sources, list):
        raise ValueError("sources is not a list")
    if source not in sources:
        sources.append(source)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in (f"CultureBotHT:{SOURCE_ID}", CULTUREBOTHT_URL):
        if reference not in existing:
            references.append({"reference": reference})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Normalized M9 CultureBotHT provenance",
        "source": f"CultureBotHT:{SOURCE_ID}; {CULTUREBOTHT_URL}",
        "notes": (
            "Copied the CultureBotHT M9 source identity from source_data into the "
            "structured sources slot recognized by review scoring."
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


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _require_target(doc)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "sources", [], "source_data")
    _ensure_sources(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_record(_load(path))}


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
