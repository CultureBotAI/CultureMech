#!/usr/bin/env python3
"""Repair DSMZ/KOMODO 604 BACTO MARINE AGAR product rows."""

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

CURATOR = "repair_dsmz_604_bacto_marine_score20.py"
ACTION = "RESOLVED_DSMZ_604_BACTO_MARINE_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

DSMZ_604_URL = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium604.pdf"
SOURCE = "DSMZ Medium 604"

MARINE_AGAR_2216 = {
    "id": "CultureMech:015393",
    "label": "Marine Agar 2216",
}


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    expected_media_term: str


TARGETS: tuple[Target, ...] = (
    Target(
        path=Path("bacterial/bacto_marine_agar.yaml"),
        expected_id="CultureMech:006092",
        expected_media_term="komodo.medium:604",
    ),
    Target(
        path=Path("specialized/bacto_marine_agar.yaml"),
        expected_id="CultureMech:015364",
        expected_media_term="mediadive.medium:604",
    ),
)

INGREDIENT_NAMES = frozenset(
    {
        "Marine agar 2216",
        "Marine agar 2216 (Difco 0979)",
    }
)

NOTES = (
    "DSMZ Medium 604 defines BACTO MARINE AGAR as the opaque commercial "
    "Marine Agar 2216 (Difco 0979) product and does not state a product mass; "
    "this repair removes the false agar grounding and the imported 1000 g/L "
    "placeholder amount."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _media_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _check_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected immutable id {target.expected_id}, "
            f"found {doc.get('id')!r}"
        )

    media_term_id = _media_term_id(doc)
    if media_term_id != target.expected_media_term:
        raise ValueError(
            f"{target.path}: expected media term {target.expected_media_term}, "
            f"found {media_term_id!r}"
        )

    ingredients = doc.get("ingredients")
    if not isinstance(ingredients, list) or len(ingredients) != 1:
        raise ValueError(f"{target.path}: expected one Marine agar 2216 ingredient")
    ingredient = ingredients[0]
    if (
        not isinstance(ingredient, dict)
        or ingredient.get("preferred_term") not in INGREDIENT_NAMES
    ):
        raise ValueError(f"{target.path}: ingredient list drifted")


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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "placeholder_composition",
        "source_information_unavailable",
        "has_unmapped_ingredients",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    if not any(
        isinstance(row, dict) and row.get("reference") == DSMZ_604_URL
        for row in references
    ):
        references.append({"reference": DSMZ_604_URL})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_604_URL,
        "notes": NOTES,
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
    _check_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(
        repaired,
        "notes",
        (
            "DSMZ Medium 604 records BACTO MARINE AGAR as Marine Agar 2216 "
            "(Difco 0979)."
        ),
        "media_term",
    )
    repaired["ingredients"] = [
        {
            "preferred_term": "Marine agar 2216 (Difco 0979)",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": SOURCE,
            "notes": (
                "DSMZ Medium 604 names Marine Agar 2216 (Difco 0979) as the "
                "only component but does not state an amount."
            ),
            "culturemech_term": copy.deepcopy(MARINE_AGAR_2216),
        }
    ]
    repaired["preparation_steps"] = [
        {
            "step_number": 1,
            "action": "MIX",
            "description": "Prepare the Marine Agar 2216 (Difco 0979) product.",
        }
    ]

    for field in (
        "solutions",
        "parent_media",
        "variant_relationship",
        "variant_modifications",
    ):
        repaired.pop(field, None)

    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(
            _load(normalized / target.path),
            target,
        )
        for target in TARGETS
    }


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
