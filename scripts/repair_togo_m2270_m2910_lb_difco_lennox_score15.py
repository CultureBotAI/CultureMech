#!/usr/bin/env python3
"""Repair TOGO M2270/M2910 LB Difco/Lennox base-media records."""

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

CURATOR = "repair_togo_m2270_m2910_lb_difco_lennox_score15.py"
ACTION = "RESOLVED_TOGO_M2270_M2910_LB_DIFCO_LENNOX_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class RecordSpec:
    target: Path
    expected_id: str
    expected_media_term: str
    original_name: str
    source_name: str
    togo_url: str
    ingredients: tuple[dict[str, Any], ...]
    signature: tuple[Component, ...]
    notes: str


GROUNDINGS: dict[str, tuple[str, str]] = {
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Sodium Chloride": ("CHEBI:26710", "sodium chloride"),
    "Yeast Extract": ("FOODON:03315426", "yeast extract"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
}


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    source: str,
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _tryptone(preferred_term: str, value: str, source: str) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        "G_PER_L",
        source,
        notes=(
            f"{source} lists {preferred_term} as a digest product not reducible "
            "to one ChEBI molecule."
        ),
    )


SOURCE_M2270 = "TOGO M2270"
SOURCE_M2910 = "TOGO M2910"
TOGO_M2270 = "https://togomedium.org/medium/M2270"
TOGO_M2910 = "https://togomedium.org/medium/M2910"

SPECS: tuple[RecordSpec, ...] = (
    RecordSpec(
        target=Path("bacterial/lb_medium_difco.yaml"),
        expected_id="CultureMech:008857",
        expected_media_term="TOGO:M2270",
        original_name="LB medium (Difco)",
        source_name=SOURCE_M2270,
        togo_url=TOGO_M2270,
        ingredients=(
            _component("Yeast Extract", "5", "G_PER_L", SOURCE_M2270),
            _component("Sodium Chloride", "10", "G_PER_L", SOURCE_M2270),
            _tryptone("Tryptone", "10", SOURCE_M2270),
        ),
        signature=(
            ("Yeast Extract", "5", "G_PER_L"),
            ("Sodium Chloride", "10", "G_PER_L"),
            ("Tryptone", "10", "G_PER_L"),
        ),
        notes=(
            "TOGO M2270 reports LB medium (Difco) with 5 g/L Yeast Extract, "
            "10 g/L Sodium Chloride, and 10 g/L Tryptone."
        ),
    ),
    RecordSpec(
        target=Path("bacterial/lb_medium_lennox.yaml"),
        expected_id="CultureMech:009447",
        expected_media_term="TOGO:M2910",
        original_name="LB medium (Lennox)",
        source_name=SOURCE_M2910,
        togo_url=TOGO_M2910,
        ingredients=(
            _component("Yeast extract", "5", "G_PER_L", SOURCE_M2910),
            _component("NaCl", "5", "G_PER_L", SOURCE_M2910),
            _tryptone("Tryptone", "10", SOURCE_M2910),
        ),
        signature=(
            ("Yeast extract", "5", "G_PER_L"),
            ("NaCl", "5", "G_PER_L"),
            ("Tryptone", "10", "G_PER_L"),
        ),
        notes=(
            "TOGO M2910 reports LB medium (Lennox) with 5 g/L Yeast extract, "
            "5 g/L NaCl, and 10 g/L Tryptone."
        ),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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


def _ensure_target(doc: dict[str, Any], spec: RecordSpec) -> None:
    if doc.get("id") != spec.expected_id:
        raise ValueError(f"{spec.target}: expected {spec.expected_id}, found {doc.get('id')}")
    if _source_term_id(doc) != spec.expected_media_term:
        raise ValueError(f"{spec.target}: expected media term {spec.expected_media_term}")
    if _signature(doc.get("ingredients"), "ingredients") != spec.signature:
        raise ValueError(f"{spec.target}: ingredient signature drifted")
    if doc.get("solutions") not in (None, []):
        raise ValueError(f"{spec.target}: expected no solutions")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation", "resolved_reference"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], spec: RecordSpec) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    if spec.togo_url not in existing:
        references.append({"reference": spec.togo_url})


def _append_event(doc: dict[str, Any], spec: RecordSpec) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": spec.togo_url,
        "notes": (
            f"{spec.notes} Added explicit FoodOn/ChEBI grounding for the two "
            "mappable components while leaving tryptone ungrounded as an "
            "undefined digest product."
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


def repair_target(doc: dict[str, Any], spec: RecordSpec) -> dict[str, Any]:
    _ensure_target(doc, spec)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ingredients"] = copy.deepcopy(list(spec.ingredients))
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("solutions", None)
    repaired["notes"] = spec.notes
    _ensure_flags(repaired)
    _ensure_references(repaired, spec)
    _append_event(repaired, spec)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / spec.target: repair_target(_load(normalized / spec.target), spec)
        for spec in SPECS
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
