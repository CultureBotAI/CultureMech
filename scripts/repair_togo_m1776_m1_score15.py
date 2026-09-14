#!/usr/bin/env python3
"""Repair TOGO M1776 / NBRC 992 M1 Medium."""

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
TARGET = Path("bacterial/m1_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1776_m1_score15.py"
ACTION = "RESOLVED_TOGO_M1776_M1_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:008342"
EXPECTED_MEDIA_TERM = "TOGO:M1776"
TOGO_M1776 = "https://togomedium.org/medium/M1776"
NBRC_992 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=992"
TOGO_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1776"
SOURCE = "TOGO M1776 / NBRC Medium 992"

Component = tuple[str, str, str]
Term = tuple[str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Yeast extract", "4", "G_PER_L"),
    ("Starch", "10", "G_PER_L"),
    ("Agar (if needed)", "18", "G_PER_L"),
    ("Peptone", "2", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = (("Seawater*", "1", "G_PER_L"),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Starch", "10", "G_PER_L"),
    ("Yeast extract", "4", "G_PER_L"),
    ("Peptone", "2", "G_PER_L"),
    ("Agar (if needed)", "18", "G_PER_L"),
    ("Seawater", "1000", "ML_PER_L"),
)

REFERENCES = (TOGO_M1776, NBRC_992, TOGO_API)

GROUNDINGS: dict[str, Term] = {
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "Peptone": ("MICRO:0000178", "peptone"),
    "Starch": ("CHEBI:28017", "starch"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

COMPONENT_NOTES = {
    "Starch": f"{SOURCE} lists 10 g/L starch.",
    "Yeast extract": f"{SOURCE} lists 4 g/L yeast extract.",
    "Peptone": f"{SOURCE} lists 2 g/L generic peptone.",
    "Agar (if needed)": f"{SOURCE} lists 18 g/L agar if needed.",
    "Seawater": (
        "NBRC Medium 992 lists 1 L seawater and specifies filtered, aged "
        "seawater or artificial seawater such as Daigo's Artificial Seawater SP."
    ),
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "DISSOLVE",
        "description": (
            "Combine 10 g starch, 4 g yeast extract, 2 g peptone, 18 g agar "
            "if needed, and 1 L filtered aged or artificial seawater."
        ),
    },
)

NOTES = (
    "TOGO M1776 imports NBRC Medium 992 M1 Medium. NBRC 992 lists 10 g "
    "starch, 4 g yeast extract, 2 g peptone, 18 g agar if needed, and 1 L "
    "seawater, with seawater supplied as filtered aged seawater or artificial "
    "seawater such as Daigo's Artificial Seawater SP."
)


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
        "notes": COMPONENT_NOTES[preferred_term],
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(
    _component(name, value, unit) for name, value, unit in FINAL_INGREDIENT_SIGNATURE
)


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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")
    if _signature(doc.get("solutions"), "solutions") not in (
        IMPORTED_SOLUTION_SIGNATURE,
        (),
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
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
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Moved the imported Seawater* placeholder solution into "
            "the main recipe as 1000 ml/L seawater, grounded the other four "
            "ingredients, and retained seawater as the one intentionally "
            "unmapped complex component."
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


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("solutions", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["notes"] = NOTES
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    return {target_path: repair_target(_load(target_path))}


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
