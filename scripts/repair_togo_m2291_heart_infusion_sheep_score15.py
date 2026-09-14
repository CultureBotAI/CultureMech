#!/usr/bin/env python3
"""Repair TOGO M2291 Heart Infusion Agar with sheep blood."""

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
TARGET = Path("bacterial/heart_infusion_agar_supplemented_with_5_sheep_blood.yaml")
EXPECTED_ID = "CultureMech:008877"
EXPECTED_MEDIA_TERM = "TOGO:M2291"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2291_heart_infusion_sheep_score15.py"
ACTION = "RESOLVED_TOGO_M2291_HEART_INFUSION_SHEEP_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2291 = "https://togomedium.org/medium/M2291"
TOGO_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2291"
SOURCE = "TOGO M2291"
TITLE = "Heart Infusion Agar (supplemented with 5% sheep blood)"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("sheep blood", "5", "PERCENT_W_V"),
    ("CO2", "variable", "VARIABLE"),
    ("Heart Infusion Agar (Difco)", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Heart Infusion Agar (Difco)", "95", "PERCENT_V_V"),
    ("Sheep blood", "5", "PERCENT_V_V"),
)

VARIABLE_BASE_SIGNATURE: tuple[Component, ...] = (
    ("Heart Infusion Agar (Difco)", "variable", "VARIABLE"),
    ("Sheep blood", "5", "PERCENT_V_V"),
)

REFERENCES = (TOGO_M2291, TOGO_API)
AERATION = "5% CO2 in an incubator"

NOTES = (
    "TOGO M2291 reports routine growth on Heart Infusion Agar (Difco) "
    "supplemented with 5% sheep blood (Oxoid) for 2 days at 37 C in an "
    "incubator containing 5% CO2. CO2 is retained as the incubation aeration "
    "condition instead of as a medium ingredient."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Supplement Heart Infusion Agar (Difco) with 5% sheep blood (Oxoid)."
        ),
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


INGREDIENTS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Heart Infusion Agar (Difco)",
        "concentration": {"value": "95", "unit": "PERCENT_V_V"},
        "source": SOURCE,
        "notes": (
            "TOGO M2291 lists the commercial Difco Heart Infusion Agar base "
            "with 5% sheep blood as the final supplement; the base is the "
            "remaining 95% v/v and is retained as an opaque component."
        ),
    },
    {
        "preferred_term": "Sheep blood",
        "concentration": {"value": "5", "unit": "PERCENT_V_V"},
        "source": SOURCE,
        "notes": "TOGO M2291 lists 5% sheep blood from Oxoid as the supplement.",
        "term": _term("UBERON:0000178", "blood"),
    },
)


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


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        VARIABLE_BASE_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    if doc.get("solutions"):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
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
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected sheep blood from %w/v to %v/v, grounded it "
            "to UBERON blood, represented the prepared Difco agar base as "
            "the remaining 95% v/v, removed CO2 from the ingredients, and "
            "kept Heart Infusion Agar (Difco) intentionally unmapped as a "
            "source-disclosed commercial base."
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
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "temperature_value", 37.0, "physical_state")
    _put_after(repaired, "aeration", AERATION, "temperature_value")
    repaired.pop("temperature_range", None)
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    return {target_path: repair_record(_load(target_path))}


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
