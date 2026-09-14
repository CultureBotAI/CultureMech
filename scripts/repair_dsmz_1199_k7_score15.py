#!/usr/bin/env python3
"""Repair DSMZ Medium 1199 K7 MEDIUM."""

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
PARENT = Path("bacterial/k7_medium.yaml")
KOMODO_CHILD = Path("bacterial/KOMODO_1199_K7_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_dsmz_1199_k7_score15.py"
ACTION = "RESOLVED_DSMZ_1199_K7_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_PARENT_ID = "CultureMech:000642"
EXPECTED_PARENT_TERM = "mediadive.medium:1199"
EXPECTED_CHILD_ID = "CultureMech:003938"
EXPECTED_CHILD_TERM = "komodo.medium:1199"
DSMZ_1199 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1199.pdf"
MEDIADIVE_1199 = "https://mediadive.dsmz.de/medium/1199"
SOURCE = "DSMZ Medium 1199 K7 MEDIUM"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Glucose", "1", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("Peptone", "1", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Glucose", "1.0", "G_PER_L"),
    ("Yeast extract", "1.0", "G_PER_L"),
    ("Peptone", "1.0", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

KOMODO_CHILD_SIGNATURE: tuple[Component, ...] = (
    ("Yeast extract", "1", "G_PER_L"),
    ("Distilled water", "variable", "VARIABLE"),
    ("Glucose", "1", "G_PER_L"),
    ("Peptone", "1", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

NOTES = (
    "DSMZ Medium 1199 K7 MEDIUM lists 1.0 g/L each of glucose, yeast extract, "
    "and peptone dissolved in 1000.0 ml/L distilled water."
)

KOMODO_CHILD_ENTRY = {
    "path": f"data/normalized_yaml/{KOMODO_CHILD}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_CHILD_ID,
    "name": "k7_medium",
    "notes": (
        "KOMODO Medium 1199 explicitly cites DSMZ Medium 1199; its imported "
        "water row is represented as variable because KOMODO reports null "
        "gram and molar amounts for water."
    ),
}

KOMODO_PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_PARENT_ID,
    "name": "k7_medium",
    "notes": (
        "DSMZ Medium 1199 is the cited source for KOMODO Medium 1199; the "
        "KOMODO import represents water as a variable-concentration row."
    ),
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": f"{SOURCE} lists {value} {'ml/L' if unit == 'ML_PER_L' else 'g/L'} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component("Glucose", "1.0", "G_PER_L"),
    _component("Yeast extract", "1.0", "G_PER_L"),
    _component("Peptone", "1.0", "G_PER_L"),
    _component("Distilled water", "1000.0", "ML_PER_L"),
)


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"{PARENT}: expected {EXPECTED_PARENT_ID}")
    if _source_term_id(doc) != EXPECTED_PARENT_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{PARENT}: ingredient signature drifted")


def _ensure_child(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_CHILD_ID:
        raise ValueError(f"{KOMODO_CHILD}: expected {EXPECTED_CHILD_ID}")
    if _source_term_id(doc) != EXPECTED_CHILD_TERM:
        raise ValueError(f"{KOMODO_CHILD}: expected media term {EXPECTED_CHILD_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") != KOMODO_CHILD_SIGNATURE:
        raise ValueError(f"{KOMODO_CHILD}: ingredient signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "has_unmapped_ingredients",
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
    ):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in (MEDIADIVE_1199, DSMZ_1199):
        if reference not in existing:
            references.append({"reference": reference})


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": f"{MEDIADIVE_1199}; {DSMZ_1199}",
        "notes": (
            f"{NOTES} Added DSMZ's explicit distilled-water volume and "
            "grounded yeast extract while leaving generic peptone ungrounded."
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


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["notes"] = NOTES
    repaired["variant_children"] = [copy.deepcopy(KOMODO_CHILD_ENTRY)]
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
    return repaired


def repair_child(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_child(doc)

    repaired = copy.deepcopy(doc)
    repaired["parent_media"] = copy.deepcopy(KOMODO_PARENT_MEDIA)
    repaired["variant_modifications"] = [
        "KOMODO records distilled water with a variable concentration where DSMZ Medium 1199 lists 1000.0 ml/L."
    ]
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    parent_path = normalized / PARENT
    child_path = normalized / KOMODO_CHILD
    return {
        parent_path: repair_parent(_load(parent_path)),
        child_path: repair_child(_load(child_path)),
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
