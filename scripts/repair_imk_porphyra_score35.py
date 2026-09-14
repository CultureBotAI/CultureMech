#!/usr/bin/env python3
"""Repair the opaque NBRC 984 IMK with Porphyra recipe."""

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

TOGO_M1769 = "https://togomedium.org/medium/M1769"
NBRC_984 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=984"

SOURCE = "NBRC Medium 984"

CURATOR = "repair_imk_porphyra_score35.py"
ACTION = "RESOLVED_IMK_PORPHYRA_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
)


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    source_term: str
    recipe: dict[str, Any]
    references: tuple[str, ...]
    notes: str
    accepted_signatures: frozenset[frozenset[str]]


def _recipe() -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": (
                    "Porphyra yezoensis thalli cultivated in IMK medium with seawater"
                ),
                "concentration": {"value": "variable", "unit": "VARIABLE"},
                "source": SOURCE,
                "notes": (
                    "NBRC Medium 984 lists the disclosed composition as "
                    "Thalli of Porphyra yezoensis cultivated in IMK medium "
                    "(with seawater)."
                ),
            },
        ],
    }


def _signature(recipe: dict[str, Any]) -> frozenset[str]:
    return frozenset(
        str(row.get("preferred_term") or "")
        for key in ("ingredients", "solutions")
        for row in recipe.get(key, [])
        if isinstance(row, dict)
    )


RECIPE = _recipe()

TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/imk_with_porphyra.yaml",
        record_id="CultureMech:008334",
        source_term="TOGO:M1769",
        recipe=RECIPE,
        references=(TOGO_M1769, NBRC_984),
        notes=(
            "NBRC Medium 984 records IMK with Porphyra as the disclosed "
            "opaque composition of Porphyra yezoensis thalli cultivated in IMK "
            "medium with seawater."
        ),
        accepted_signatures=frozenset({frozenset(), _signature(RECIPE)}),
    ),
)
TARGET_BY_PATH: dict[str, Target] = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _top_level_signature(doc: dict[str, Any]) -> frozenset[str]:
    return frozenset(
        str(row.get("preferred_term") or "")
        for key in ("ingredients", "solutions")
        for row in doc.get(key) or []
        if isinstance(row, dict)
    )


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != target.source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.source_term}, " f"found {source_term!r}"
        )

    if _top_level_signature(doc) not in target.accepted_signatures:
        raise ValueError(f"{target.path}: component signature drifted")


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.references:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.references),
        "notes": target.notes,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    for recipe_field in RECIPE_FIELDS:
        if recipe_field in target.recipe:
            repaired[recipe_field] = copy.deepcopy(target.recipe[recipe_field])
        else:
            repaired.pop(recipe_field, None)
    repaired["notes"] = target.notes
    repaired["data_quality_flags"] = [
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path), target)
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
