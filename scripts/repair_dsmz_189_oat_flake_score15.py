#!/usr/bin/env python3
"""Repair DSMZ Medium 189 Oat Flake Medium and its KOMODO duplicate."""

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

CURATOR = "repair_dsmz_189_oat_flake_score15.py"
ACTION = "RESOLVED_DSMZ_189_OAT_FLAKE_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

DSMZ_189 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium189.pdf"
SOURCE = "DSMZ Medium 189"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Oat flakes", "30", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
)


@dataclass(frozen=True)
class Target:
    path: str
    expected_id: str
    expected_source_term: str


TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/oat_flake_medium.yaml",
        expected_id="CultureMech:001281",
        expected_source_term="mediadive.medium:189",
    ),
    Target(
        path="bacterial/KOMODO_189_OAT_FLAKE_medium.yaml",
        expected_id="CultureMech:004213",
        expected_source_term="komodo.medium:189",
    ),
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _step(step_number: int, action: str, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": action,
        "description": description,
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Oat flakes",
        "30.0",
        "G_PER_L",
        notes="DSMZ Medium 189 lists 30.0 g oat flakes.",
    ),
    _component(
        "Agar",
        "15.0",
        "G_PER_L",
        notes="DSMZ Medium 189 lists 15.0 g agar.",
        term=("CHEBI:2509", "agar"),
    ),
    _component(
        "Distilled water",
        "1000.0",
        "ML_PER_L",
        notes="DSMZ Medium 189 lists 1000.0 ml distilled water.",
        term=("CHEBI:15377", "water"),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    _step(
        1,
        "HEAT",
        "Boil oat flakes in water for 10 min, fill to 1 L, and add agar.",
    ),
    _step(2, "AUTOCLAVE", "Autoclave for 20 min at 121 C, then shake before pouring."),
)

NOTES = (
    "DSMZ Medium 189 lists oat flakes, agar, and distilled water, with boiling "
    "and autoclaving instructions."
)
PARENT_VARIANT_NOTE = (
    "KOMODO record is an exact source duplicate of DSMZ Medium 189; local "
    "physical state, ingredient, and concentration signatures match."
)
CHILD_PARENT_NOTE = (
    "KOMODO record explicitly cites DSMZ Medium 189; the DSMZ parent has "
    "matching physical state, ingredient, and concentration signatures."
)

FINAL_INGREDIENT_SIGNATURE = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in INGREDIENTS
)
FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = ()


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


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != target.expected_source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.expected_source_term}, "
            f"found {source_term!r}"
        )

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    solution_signature = _signature(doc.get("solutions"), "solutions")
    if (ingredient_signature, solution_signature) not in {
        (IMPORTED_INGREDIENT_SIGNATURE, ()),
        (FINAL_INGREDIENT_SIGNATURE, FINAL_SOLUTION_SIGNATURE),
    }:
        raise ValueError(
            f"{target.path}: ingredient/solution signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to "
            f"{ingredient_signature!r} / {solution_signature!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    if DSMZ_189 not in existing:
        references.append({"reference": DSMZ_189})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_189,
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


def _ensure_duplicate_notes(doc: dict[str, Any], target: Target) -> None:
    if target.path == "bacterial/oat_flake_medium.yaml":
        children = doc.get("variant_children") or []
        if not isinstance(children, list):
            raise ValueError("variant_children is not a list")
        for child in children:
            if (
                isinstance(child, dict)
                and child.get("path")
                == "data/normalized_yaml/bacterial/KOMODO_189_OAT_FLAKE_medium.yaml"
            ):
                child["notes"] = PARENT_VARIANT_NOTE
        return

    parent_media = doc.get("parent_media")
    if not isinstance(parent_media, dict):
        raise ValueError("parent_media is not a mapping")
    parent_media["notes"] = CHILD_PARENT_NOTE


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired.pop("ph_value", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    _ensure_duplicate_notes(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_record(_load(path), target)
    return plans


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
