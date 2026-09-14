#!/usr/bin/env python3
"""Repair DSMZ/KOMODO 363 Phenylobacterium strain variant metadata."""

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

DSMZ_363 = "bacterial/phenylobacterium_medium.yaml"
KOMODO_363 = "bacterial/KOMODO_363_PHENYLOBACTERIUM_MEDIUM.yaml"
KOMODO_363_1 = "bacterial/for_dsm_2118.yaml"

EXPECTED_IDS = {
    DSMZ_363: "CultureMech:001464",
    KOMODO_363: "CultureMech:005086",
    KOMODO_363_1: "CultureMech:005085",
}

EXPECTED_SOURCE_TERMS = {
    KOMODO_363: "komodo.medium:363",
    KOMODO_363_1: "komodo.medium:363.1",
}

DSMZ_363_REST = "https://mediadive.dsmz.de/rest/medium/363"
DSMZ_363_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium363.pdf"
KOMODO_BASE = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
)
KOMODO_363_URL = f"{KOMODO_BASE}363"
KOMODO_363_1_URL = f"{KOMODO_BASE}363.1"

CURATOR = "repair_dsmz_363_phenylobacterium_score15.py"
ACTION = "RESOLVED_DSMZ_KOMODO_363_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"
DATA_QUALITY_FLAGS = ["has_ontology_mappings", "ingredients_curated"]
SUBSTITUTION_NOTES = (
    "KOMODO Medium 363.1 replaces 1.00 g/L Antipyrine from KOMODO Medium "
    "363 with 1.00 g/L L-phenylalanine."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _l_phenylalanine() -> dict[str, Any]:
    term = _term("CHEBI:17295", "L-phenylalanine")
    return {
        "preferred_term": "L-phenylalanine",
        "term": copy.deepcopy(term),
        "source": "KOMODO Medium 363.1",
        "notes": "KOMODO Medium 363.1 lists 1.00 g/L L-phenylalanine in the final-component table.",
        "concentration": {
            "value": "1.00",
            "unit": "G_PER_L",
        },
        "mediaingredientmech_chebi_term": copy.deepcopy(term),
    }


def _recipe_ref(path: str, relationship: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": EXPECTED_IDS[path],
        "name": Path(path).stem,
        "notes": notes,
    }


KOMODO_363_PARENT = _recipe_ref(
    KOMODO_363,
    "SUBSTITUTED_COMPONENT_VARIANT",
    SUBSTITUTION_NOTES,
)
KOMODO_363_1_CHILD = _recipe_ref(
    KOMODO_363_1,
    "SUBSTITUTED_COMPONENT_VARIANT",
    SUBSTITUTION_NOTES,
)


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    term = media_term.get("term") if isinstance(media_term, dict) else {}
    return str(term.get("id") or "") if isinstance(term, dict) else ""


def _require_path(doc: dict[str, Any], path: str) -> None:
    if doc.get("id") != EXPECTED_IDS[path]:
        raise ValueError(f"{path}: found id {doc.get('id')!r}, expected {EXPECTED_IDS[path]!r}")
    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[path]:
        raise ValueError(
            f"{path}: found source term {source_term!r}, expected "
            f"{EXPECTED_SOURCE_TERMS[path]!r}"
        )


def _ensure_references(doc: dict[str, Any], path: str, source_url: str) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{path}: references is not a list")

    seen = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in (source_url, DSMZ_363_PDF, DSMZ_363_REST):
        if url not in seen:
            references.append({"reference": url})


def _append_curation_event(
    doc: dict[str, Any],
    path: str,
    source_url: str,
    curation_notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved DSMZ/KOMODO Medium 363 Phenylobacterium variant metadata",
        "source": source_url,
        "notes": curation_notes,
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{path}: curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_komodo_363_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_path(doc, KOMODO_363)

    repaired = copy.deepcopy(doc)
    child_path = f"data/normalized_yaml/{KOMODO_363_1}"
    variant_children = [
        child
        for child in repaired.get("variant_children", [])
        if not isinstance(child, dict) or child.get("path") != child_path
    ]
    variant_children.append(copy.deepcopy(KOMODO_363_1_CHILD))
    repaired["variant_children"] = variant_children

    _ensure_references(repaired, KOMODO_363, KOMODO_363_URL)
    _append_curation_event(
        repaired,
        KOMODO_363,
        KOMODO_363_URL,
        "KOMODO Medium 363.1 was resolved as an Antipyrine-to-L-phenylalanine variant.",
    )
    _put_after(repaired, "references", repaired["references"], "curation_history")
    return repaired


def repair_for_dsm_2118(doc: dict[str, Any]) -> dict[str, Any]:
    _require_path(doc, KOMODO_363_1)

    repaired = copy.deepcopy(doc)
    ingredients = []
    found_substitution_site = False
    for ingredient in repaired.get("ingredients", []):
        if isinstance(ingredient, dict) and ingredient.get("preferred_term") in {
            "Antipyrine",
            "L-phenylalanine",
        }:
            ingredients.append(_l_phenylalanine())
            found_substitution_site = True
        else:
            ingredients.append(copy.deepcopy(ingredient))
    if not found_substitution_site:
        raise ValueError(f"{KOMODO_363_1}: expected an Antipyrine or L-phenylalanine row")

    repaired["ingredients"] = ingredients
    _put_after(repaired, "data_quality_flags", list(DATA_QUALITY_FLAGS), "ingredients")

    _ensure_references(repaired, KOMODO_363_1, KOMODO_363_1_URL)
    _append_curation_event(
        repaired,
        KOMODO_363_1,
        KOMODO_363_1_URL,
        SUBSTITUTION_NOTES,
    )
    _put_after(repaired, "references", repaired["references"], "data_quality_flags")

    for field in (
        "parent_media",
        "variant_relationship",
        "variant_modifications",
        "variant_children",
    ):
        repaired.pop(field, None)
    _put_after(repaired, "parent_media", copy.deepcopy(KOMODO_363_PARENT), "references")
    _put_after(
        repaired,
        "variant_relationship",
        "SUBSTITUTED_COMPONENT_VARIANT",
        "parent_media",
    )
    _put_after(
        repaired,
        "variant_modifications",
        [SUBSTITUTION_NOTES],
        "variant_relationship",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / KOMODO_363: repair_komodo_363_parent(_load(normalized / KOMODO_363)),
        normalized / KOMODO_363_1: repair_for_dsm_2118(_load(normalized / KOMODO_363_1)),
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
