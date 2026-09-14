#!/usr/bin/env python3
"""Resolve remaining score-10 non-strain grounding records."""

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
    signature: tuple[str, ...]
    exact_terms: tuple[str, ...] = ()
    reviewed_unmapped_terms: tuple[str, ...] = ()


TARGETS = (
    Target(
        Path("bacterial/KOMODO_425_OATMEAL_AGAR.yaml"),
        "CultureMech:005249",
        ("Oat flakes", "Oatmeal", "Agar"),
        reviewed_unmapped_terms=("Oat flakes", "Oatmeal"),
    ),
    Target(
        Path("bacterial/heart_infusion_blood_agar.yaml"),
        "CultureMech:001090",
        ("Bacto Heart Infusion Broth", "Agar", "Defibrinated Blood"),
        reviewed_unmapped_terms=("Bacto Heart Infusion Broth", "Defibrinated Blood"),
    ),
    Target(
        Path("bacterial/leptospira_medium.yaml"),
        "CultureMech:000549",
        ("Leptospira Medium Base EMJH", "Agarose", "Leptospira Enrichment EMJH"),
        reviewed_unmapped_terms=(
            "Leptospira Medium Base EMJH",
            "Leptospira Enrichment EMJH",
        ),
    ),
    Target(
        Path("bacterial/oatmeal_agar.yaml"),
        "CultureMech:001529",
        ("Oat flakes", "Oatmeal", "Agar"),
        reviewed_unmapped_terms=("Oat flakes", "Oatmeal"),
    ),
    Target(
        Path("bacterial/rcm_medium_with_sea_salts.yaml"),
        "CultureMech:001767",
        ("dehydrated RCM medium", "Sea salts", "Sodium resazurin"),
        reviewed_unmapped_terms=("dehydrated RCM medium", "Sea salts"),
    ),
    Target(
        Path("bacterial/widdel_freshwater_medium_with_pyruvate.yaml"),
        "CultureMech:002392",
        (
            "Distilled water",
            "NaCl",
            "CaCl2・2H2O",
            "KH2PO4",
            "NH4Cl",
            "Resazurin",
            "MgCl2・6H2O",
            "KCl",
            "Na2SO4",
            "N2",
        ),
        exact_terms=("CaCl2・2H2O", "MgCl2・6H2O"),
    ),
)
TARGET_BY_PATH = {target.path: target for target in TARGETS}
EXPECTED_TARGET_COUNT = 6

TERMS = {
    "CaCl2・2H2O": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"},
    "MgCl2・6H2O": {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate",
    },
}

CURATOR = "repair_remaining_score10_grounding_batch9.py"
ACTION = "RESOLVED_REMAINING_SCORE10_GROUNDING_BATCH9"
TIMESTAMP = "2026-09-13T00:00:00-07:00"
CURATED_UNMAPPED_FLAGS = ("ingredients_curated", "has_unmapped_ingredients")


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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for flag in CURATED_UNMAPPED_FLAGS:
        if flag not in flags:
            flags.append(flag)


def _target_terms(target: Target) -> str:
    terms = (*target.exact_terms, *target.reviewed_unmapped_terms)
    return ", ".join(terms)


def _event_changes(target: Target) -> str:
    changes: list[str] = []
    if target.exact_terms:
        changes.append("grounded exact hydrate terms")
    if target.reviewed_unmapped_terms:
        changes.append("marked reviewed opaque ingredients")
    return "; ".join(changes)


def _validate_targets() -> None:
    if len(TARGETS) != EXPECTED_TARGET_COUNT or len(TARGETS) != len(TARGET_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_TARGET_COUNT} unique targets, found "
            f"{len(TARGETS)} total and {len(TARGET_BY_PATH)} unique"
        )
    for target in TARGETS:
        missing = set(target.exact_terms) - set(TERMS)
        if missing:
            raise ValueError(f"{target.path}: missing term mapping(s): {sorted(missing)!r}")


def repair_record(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    target = TARGET_BY_PATH[path]

    if doc.get("id") != target.record_id:
        raise ValueError(f"{path}: expected {target.record_id}, found {doc.get('id')!r}")
    if _ingredient_signature(doc) != target.signature:
        raise ValueError(
            f"{path}: ingredient signature drifted: {_ingredient_signature(doc)!r}"
        )

    expected_terms = set(target.exact_terms)
    exact_terms_seen: set[str] = set()
    repaired = copy.deepcopy(doc)
    for ingredient in repaired["ingredients"]:
        preferred_term = ingredient["preferred_term"]
        if preferred_term not in expected_terms:
            continue

        ingredient["term"] = copy.deepcopy(TERMS[preferred_term])
        exact_terms_seen.add(preferred_term)

    if exact_terms_seen != expected_terms:
        missing = ", ".join(sorted(expected_terms - exact_terms_seen))
        raise ValueError(f"{path}: missing targeted ingredient(s): {missing}")

    if target.reviewed_unmapped_terms:
        _ensure_flags(repaired)

    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": _event_changes(target),
            "source": "official catalogue recipe and local exact label index",
            "notes": f"Reviewed remaining score-10 grounding rows: {_target_terms(target)}.",
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
