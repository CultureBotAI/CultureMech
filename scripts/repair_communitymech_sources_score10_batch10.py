#!/usr/bin/env python3
"""Add structured CommunityMech source attribution to score-10 imports."""

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


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    community_ids: tuple[str, ...]


TARGETS = (
    Target(
        Path("bacterial/Nitrogen_Free_Medium_for_Leptospirillum_ferrodiazotrophum.yaml"),
        "CultureMech:015436",
        ("CommunityMech:000059",),
    ),
    Target(
        Path("bacterial/PCS_FP_medium_for_thermophilic_cellulose_degradation.yaml"),
        "CultureMech:015439",
        ("CommunityMech:000061",),
    ),
    Target(
        Path("specialized/Glycerol_Fermentation_Medium_for_DIET_Coculture.yaml"),
        "CultureMech:015432",
        ("CommunityMech:000031",),
    ),
    Target(
        Path("specialized/Half_strength_Murashige_Skoog_medium_for_Arabidopsis_growth.yaml"),
        "CultureMech:015433",
        ("CommunityMech:000003", "CommunityMech:000022"),
    ),
    Target(
        Path("specialized/Modified_DSM_120_Medium_for_DIET_Coculture.yaml"),
        "CultureMech:015434",
        ("CommunityMech:000033",),
    ),
    Target(
        Path("specialized/Modified_Freshwater_Medium_for_DIET_Coculture.yaml"),
        "CultureMech:015435",
        ("CommunityMech:000032",),
    ),
    Target(
        Path("specialized/Nitrogen_free_plant_nutrient_solution_for_soybean_growth.yaml"),
        "CultureMech:015438",
        ("CommunityMech:000064",),
    ),
    Target(
        Path("specialized/nitrogen_free_b_d_medium_for_lotus_japonicus_growth.yaml"),
        "CultureMech:015437",
        ("CommunityMech:000040",),
    ),
)
TARGET_BY_PATH = {target.path: target for target in TARGETS}
EXPECTED_TARGET_COUNT = 8

CURATOR = "repair_communitymech_sources_score10_batch10.py"
ACTION = "ADDED_COMMUNITYMECH_STRUCTURED_SOURCES_BATCH10"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True
    if not inserted:
        updated[key] = value
    doc.clear()
    doc.update(updated)


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


def _validate_targets() -> None:
    if len(TARGETS) != EXPECTED_TARGET_COUNT or len(TARGETS) != len(TARGET_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_TARGET_COUNT} unique targets, found "
            f"{len(TARGETS)} total and {len(TARGET_BY_PATH)} unique"
        )


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')!r}")

    source_data = doc.get("source_data") or {}
    if not isinstance(source_data, dict):
        raise ValueError(f"{target.path}: source_data is not a mapping")
    if source_data.get("origin") != "CommunityMech":
        raise ValueError(f"{target.path}: expected CommunityMech source_data.origin")

    community_ids = tuple(source_data.get("community_ids") or ())
    if community_ids != target.community_ids:
        raise ValueError(
            f"{target.path}: expected community_ids {target.community_ids!r}, "
            f"found {community_ids!r}"
        )


def _sources(target: Target) -> list[dict[str, str]]:
    return [
        {
            "database": "CommunityMech",
            "database_id": community_id,
        }
        for community_id in target.community_ids
    ]


def repair_record(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    target = TARGET_BY_PATH[path]
    _require_target(doc, target)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "sources", _sources(target), "source_data")
    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Added structured CommunityMech sources",
            "source": "source_data.community_ids",
            "notes": (
                "Promoted CommunityMech upstream IDs into sources[] for "
                "source-provenance scoring."
            ),
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
