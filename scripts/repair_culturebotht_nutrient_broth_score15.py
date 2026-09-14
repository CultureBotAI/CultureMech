#!/usr/bin/env python3
"""Repair the sparse CultureBotHT nutrient broth score-15 record."""

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

TARGET_PATH = Path("bacterial/nutrient_broth.yaml")
EXPECTED_ID = "CultureMech:015471"
SOURCE_ID = "nutrient broth"
EXPECTED_INGREDIENTS = ("Bacto Peptone", "Yeast Extract", "D-Glucose", "Sodium Chloride")
INVALID_KG_MICROBE_MATCHES = {"mediadive.medium:681"}

CURATOR = "repair_culturebotht_nutrient_broth_score15.py"
ACTION = "MARKED_CULTUREBOTHT_NUTRIENT_BROTH_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"
CULTUREBOTHT_URL = "https://github.com/CultureBotAI/CultureBotHT"

NOTES = (
    "Source: FEBA media definitions via CultureBotHT. CultureBotHT imports nutrient "
    "broth as 15 g/L Bacto Peptone, 3 g/L yeast extract, 1 g/L D-glucose, and "
    "6 g/L sodium chloride."
)

GROUNDINGS = {
    "Bacto Peptone": ("MICRO:0000178", "Bacto peptone"),
    "Yeast Extract": ("FOODON:03315426", "Yeast extract"),
}


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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


def _grounded(component: dict[str, Any]) -> bool:
    term = component.get("term")
    return isinstance(term, dict) and bool(term.get("id"))


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
        raise ValueError(f"{TARGET_PATH}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _component_names(doc) != EXPECTED_INGREDIENTS:
        raise ValueError(f"{TARGET_PATH}: CultureBotHT nutrient broth ingredient list drifted")
    if not _has_culturebotht_source(doc):
        raise ValueError(f"{TARGET_PATH}: missing CultureBotHT source {SOURCE_ID!r}")


def _ensure_sources(doc: dict[str, Any]) -> None:
    source = {
        "database": "CultureBotHT",
        "database_id": SOURCE_ID,
        "url": CULTUREBOTHT_URL,
    }
    sources = doc.setdefault("sources", [])
    if not isinstance(sources, list):
        raise ValueError(f"{TARGET_PATH}: sources is not a list")
    if source not in sources:
        sources.append(source)


def _ensure_flags(doc: dict[str, Any]) -> None:
    components = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    flags = doc.setdefault("data_quality_flags", [])
    if not components:
        raise ValueError(f"{TARGET_PATH}: expected a non-empty ingredient list")
    if not isinstance(flags, list):
        raise ValueError(f"{TARGET_PATH}: data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)

    if any(not _grounded(component) for component in components):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{TARGET_PATH}: references is not a list")

    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in (f"CultureBotHT:{SOURCE_ID}", CULTUREBOTHT_URL):
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Marked CultureBotHT nutrient broth formula as curated",
        "source": f"CultureBotHT:{SOURCE_ID}; {CULTUREBOTHT_URL}",
        "notes": (
            "Grounded Bacto Peptone and Yeast Extract with exact "
            "MediaIngredientMech label-index mappings. Removed stale KG-Microbe "
            "match to MediaDive 681."
        ),
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET_PATH}: curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_document(doc: dict[str, Any]) -> dict[str, Any]:
    _require_target(doc)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "notes", NOTES, "description")
    _put_after(repaired, "sources", [], "category")
    _ensure_sources(repaired)

    for ingredient in repaired.get("ingredients") or []:
        if not isinstance(ingredient, dict):
            continue
        grounding = GROUNDINGS.get(str(ingredient.get("preferred_term") or ""))
        if grounding:
            ingredient["term"] = _term(*grounding)

    if repaired.get("kg_microbe_match") in INVALID_KG_MICROBE_MATCHES:
        del repaired["kg_microbe_match"]

    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repair(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET_PATH
    return {path: repair_document(_load(path))}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    changed_count = 0
    for path, doc in plan_repair(args.normalized_dir).items():
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
