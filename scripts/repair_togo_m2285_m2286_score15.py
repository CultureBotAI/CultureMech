#!/usr/bin/env python3
"""Repair TOGO M2285/M2286 Vibrio Natriegens Medium records."""

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

CURATOR = "repair_togo_m2285_m2286_score15.py"
ACTION = "RESOLVED_TOGO_M2285_M2286_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M2285 = "https://togomedium.org/medium/M2285"
TOGO_M2286 = "https://togomedium.org/medium/M2286"
DSMZ_115 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium115.pdf"
DSMZ_1 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1.pdf"

PH_VALUE = 7.0
PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0.",
    },
)

Component = tuple[str, str, str]

M2285_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1000", "G_PER_L"),
    ("NaCl", "1.5", "PERCENT_W_V"),
    ("Agar, if necessary", "15", "G_PER_L"),
    ("Meat extract", "3", "G_PER_L"),
    ("Peptone", "5", "G_PER_L"),
)

M2286_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1000", "G_PER_L"),
    ("NaCl", "1.5", "PERCENT_W_V"),
    ("MnSO4 x H2O", "10", "G_PER_L"),
    ("Agar, if necessary", "15", "G_PER_L"),
    ("Meat extract", "3", "G_PER_L"),
    ("Peptone", "5", "G_PER_L"),
)

M2285_FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "5.0", "G_PER_L"),
    ("Meat extract", "3.0", "G_PER_L"),
    ("NaCl", "1.5", "PERCENT_W_V"),
    ("Agar, if necessary", "15.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

M2286_FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "5.0", "G_PER_L"),
    ("Meat extract", "3.0", "G_PER_L"),
    ("NaCl", "1.5", "PERCENT_W_V"),
    ("MnSO4 x H2O", "10.0", "MG_PER_L"),
    ("Agar, if necessary", "15.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    expected_media_term: str
    source: str
    imported_signature: tuple[Component, ...]
    final_signature: tuple[Component, ...]
    include_sporulation_manganese: bool
    reference_urls: tuple[str, ...]


TARGET_M2285 = Target(
    path=Path("bacterial/TOGO_M2285_Vibrio_Natriegens_Medium.yaml"),
    expected_id="CultureMech:008871",
    expected_media_term="TOGO:M2285",
    source="TOGO M2285 / DSMZ Medium 115",
    imported_signature=M2285_IMPORTED_INGREDIENT_SIGNATURE,
    final_signature=M2285_FINAL_INGREDIENT_SIGNATURE,
    include_sporulation_manganese=False,
    reference_urls=(TOGO_M2285, DSMZ_115, DSMZ_1),
)

TARGET_M2286 = Target(
    path=Path("bacterial/vibrio_natriegens_medium_for_sporulation.yaml"),
    expected_id="CultureMech:008872",
    expected_media_term="TOGO:M2286",
    source="TOGO M2286 / DSMZ Medium 115",
    imported_signature=M2286_IMPORTED_INGREDIENT_SIGNATURE,
    final_signature=M2286_FINAL_INGREDIENT_SIGNATURE,
    include_sporulation_manganese=True,
    reference_urls=(TOGO_M2286, DSMZ_115, DSMZ_1),
)

TARGETS = (TARGET_M2285, TARGET_M2286)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar, if necessary": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "MnSO4 x H2O": ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Peptone": ("MICRO:0000178", "Peptone"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "PERCENT_W_V": "% w/v",
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"DSMZ Medium 115 lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(target: Target) -> tuple[dict[str, Any], ...]:
    rows = [
        _component(
            "Peptone",
            "5.0",
            "G_PER_L",
            source=target.source,
            notes="DSMZ Medium 1 lists 5 g/L Peptone.",
        ),
        _component(
            "Meat extract",
            "3.0",
            "G_PER_L",
            source=target.source,
            notes=(
                "DSMZ Medium 1 lists 3 g/L Meat extract; this generic complex "
                "extract is retained without an ontology grounding."
            ),
        ),
        _component(
            "NaCl",
            "1.5",
            "PERCENT_W_V",
            source=target.source,
            notes="DSMZ Medium 115 lists DSMZ Medium 1 with 1.5% NaCl.",
        ),
    ]
    if target.include_sporulation_manganese:
        rows.append(
            _component(
                "MnSO4 x H2O",
                "10.0",
                "MG_PER_L",
                source=target.source,
                notes=(
                    "DSMZ Medium 1 recommends adding 10 mg/L MnSO4 x H2O for "
                    "Bacillus-strain sporulation."
                ),
            )
        )
    rows.extend(
        (
            _component(
                "Agar, if necessary",
                "15.0",
                "G_PER_L",
                source=target.source,
                notes="DSMZ Medium 1 lists 15 g/L Agar, if necessary.",
            ),
            _component(
                "Distilled water",
                "1.0",
                "L",
                source=target.source,
                notes="DSMZ Medium 1 lists 1000 ml distilled water.",
            ),
        )
    )
    return tuple(rows)


def _notes(target: Target) -> str:
    supplement = (
        " The TOGO M2286 sporulation variant also adds 10 mg/L MnSO4 x H2O."
        if target.include_sporulation_manganese
        else ""
    )
    return (
        "DSMZ Medium 115 defines Vibrio Natriegens Medium as DSMZ Medium 1 "
        "with 1.5% NaCl. DSMZ Medium 1 lists, per liter, 5 g Peptone, 3 g "
        "Meat extract, 15 g Agar if necessary, and 1000 ml distilled water, "
        f"with pH adjusted to 7.0.{supplement}"
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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected id {target.expected_id}, " f"found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.expected_media_term:
        raise ValueError(f"{target.path}: expected media term {target.expected_media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        target.imported_signature,
        target.final_signature,
    ):
        raise ValueError(
            f"{target.path}: ingredient signature drifted from "
            f"{target.imported_signature!r} to {ingredient_signature!r}"
        )

    if doc.get("solutions"):
        raise ValueError(f"{target.path}: solution signature drifted")


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


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.reference_urls:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.reference_urls),
        "notes": (
            f"{_notes(target)} Corrected distilled water and sporulation MnSO4 x H2O "
            "unit artifacts, grounded the disclosed simple and protein-hydrolysate "
            "components, and kept Meat extract intentionally unmapped."
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(_ingredients(target)))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", _notes(target), "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
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
