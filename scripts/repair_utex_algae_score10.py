#!/usr/bin/env python3
"""Repair the two remaining score-10 UTEX algae records."""

from __future__ import annotations

import argparse
import copy
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

SOIL_EXTRACT = Path("algae/Soil_Extract_Medium.yaml")
SOILWATER_PEAT = Path("algae/Soilwater_Peat_Medium.yaml")

SOIL_EXTRACT_ID = "CultureMech:000223"
SOILWATER_PEAT_ID = "CultureMech:000230"
GREEN_HOUSE_SOIL_TERM = {
    "id": "ENVO:00001998",
    "label": "soil",
}

CURATOR = "repair_utex_algae_score10.py"
SOURCE_ACTION = "NORMALIZED_UTEX_SOIL_EXTRACT_SOURCE_SCORE10"
GROUNDING_ACTION = "GROUNDED_UTEX_SOILWATER_PEAT_SCORE10"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

UTEX_SOURCE = re.compile(
    r"Source ID: (?P<source_id>[^,]+), URL: (?P<url>https://utex\.org/products/[^' ]+)"
)
SOILWATER_PEAT_SIGNATURE = ("Organic Peat", "Green House Soil", "dH2O")


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


def _require_id(doc: dict[str, Any], expected: str) -> None:
    if doc.get("id") != expected:
        raise ValueError(f"expected {expected}, found {doc.get('id')!r}")


def _references(doc: dict[str, Any]) -> list[str]:
    rows = doc.get("references") or []
    if not isinstance(rows, list):
        raise ValueError("references is not a list")
    return [
        str(row.get("reference") or "")
        for row in rows
        if isinstance(row, dict) and row.get("reference")
    ]


def _utex_import(doc: dict[str, Any]) -> tuple[str, str]:
    history = doc.get("curation_history") or []
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")

    matches: list[tuple[str, str]] = []
    for event in history:
        if not isinstance(event, dict) or event.get("curator") != "utex-import":
            continue
        match = UTEX_SOURCE.search(str(event.get("notes") or ""))
        if match:
            matches.append((match.group("source_id"), match.group("url")))

    if len(matches) != 1:
        raise ValueError(f"expected one utex-import Source ID/URL, found {matches!r}")
    return matches[0]


def _require_utex_source(path: Path, doc: dict[str, Any]) -> tuple[str, str]:
    utex_refs = []
    url_refs = []
    for reference in _references(doc):
        if reference.startswith("UTEX:"):
            utex_refs.append(reference.removeprefix("UTEX:"))
        if reference.startswith("https://utex.org/products/"):
            url_refs.append(reference)

    if len(utex_refs) != 1 or len(url_refs) != 1:
        raise ValueError(
            f"expected one UTEX reference and one UTEX URL, found "
            f"{utex_refs!r} and {url_refs!r}"
        )

    import_source_id, import_url = _utex_import(doc)
    source_id, url = utex_refs[0], url_refs[0]
    if (source_id, url) != (import_source_id, import_url):
        raise ValueError(
            f"{path}: UTEX reference {(source_id, url)!r} does not match "
            f"utex-import {(import_source_id, import_url)!r}"
        )
    return source_id, url


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


def repair_soil_extract(doc: dict[str, Any]) -> dict[str, Any]:
    _require_id(doc, SOIL_EXTRACT_ID)
    source_id, url = _require_utex_source(SOIL_EXTRACT, doc)

    repaired = copy.deepcopy(doc)
    _put_after(
        repaired,
        "sources",
        [{"database": "UTEX", "database_id": source_id, "url": url}],
        "category",
    )
    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": SOURCE_ACTION,
            "changes": "Normalized UTEX Soil Extract Medium provenance",
            "source": f"UTEX:{source_id}; {url}",
            "notes": (
                "Copied the UTEX source identity from references and the original "
                "utex-import event into the structured sources slot recognized by "
                "review scoring."
            ),
        },
    )
    return repaired


def _ingredient_signature(doc: dict[str, Any]) -> tuple[str, ...]:
    ingredients = doc.get("ingredients") or []
    if not isinstance(ingredients, list):
        raise ValueError("ingredients is not a list")
    return tuple(
        str(row.get("preferred_term") or "")
        for row in ingredients
        if isinstance(row, dict)
    )


def repair_soilwater_peat(doc: dict[str, Any]) -> dict[str, Any]:
    _require_id(doc, SOILWATER_PEAT_ID)
    if _ingredient_signature(doc) != SOILWATER_PEAT_SIGNATURE:
        raise ValueError(
            f"Soilwater Peat ingredient signature drifted: {_ingredient_signature(doc)!r}"
        )

    repaired = copy.deepcopy(doc)
    for ingredient in repaired["ingredients"]:
        if ingredient["preferred_term"] == "Green House Soil":
            ingredient["term"] = copy.deepcopy(GREEN_HOUSE_SOIL_TERM)
            break
    else:
        raise ValueError("Green House Soil ingredient not found")

    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": GROUNDING_ACTION,
            "changes": "Grounded UTEX Soilwater Peat Green House Soil",
            "source": "src/culturemech/data/mediaingredientmech/label_index.csv",
            "notes": (
                "Applied the existing MediaIngredientMech mapping from Green House "
                "Soil to ENVO:00001998 soil."
            ),
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    soil_extract = normalized / SOIL_EXTRACT
    soilwater_peat = normalized / SOILWATER_PEAT
    return {
        soil_extract: repair_soil_extract(_load(soil_extract)),
        soilwater_peat: repair_soilwater_peat(_load(soilwater_peat)),
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
