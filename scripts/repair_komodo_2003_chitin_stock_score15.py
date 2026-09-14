#!/usr/bin/env python3
"""Repair KOMODO 2003 Chitin stock solution from DSMZ Medium 766."""

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
PATH = Path("bacterial/chitin_stock_solution_medium_766.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_2003_chitin_stock_score15.py"
ACTION = "RESOLVED_KOMODO_2003_CHITIN_STOCK_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

RECORD_ID = "CultureMech:004269"
MEDIA_TERM = "komodo.medium:2003"
DSMZ_766 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium766.pdf"
SOURCE = "DSMZ Medium 766"

IMPORTED_INGREDIENTS = (("KOH", "variable", "VARIABLE"),)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    notes: str,
    *,
    term: tuple[str, str],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        "Chitin",
        "16.6667",
        "G_PER_L",
        "DSMZ Medium 766 mixes 20 g practical-grade crab-shell chitin in the 1.2 L "
        "acidified starting suspension.",
        term=("CHEBI:17029", "chitin"),
    ),
    _ingredient(
        "Hydrochloric acid, 37%",
        "166.6667",
        "ML_PER_L",
        "DSMZ Medium 766 mixes 200 ml of 37% HCl in the 1.2 L acidified starting " "suspension.",
        term=("CHEBI:17883", "hydrogen chloride"),
    ),
    _ingredient(
        "Distilled water",
        "833.3333",
        "ML_PER_L",
        "DSMZ Medium 766 pours the acidified chitin suspension into 1 L pre-cooled "
        "distilled water before filtration.",
        term=("CHEBI:15377", "water"),
    ),
    _ingredient(
        "Potassium hydroxide, 5 M",
        "8.3333",
        "ML_PER_L",
        "DSMZ Medium 766 neutralises the resuspended chitin with 10 ml of 5 M KOH.",
        term=("CHEBI:32035", "potassium hydroxide"),
    ),
)

FINAL_INGREDIENTS = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in INGREDIENTS
)

PREPARATION_STEPS = (
    {
        "step_number": 1,
        "action": "COOL",
        "description": "Pre-cool the 37% HCl and distilled water to 4 C.",
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Mix 20 g practical-grade chitin from crab shells with 200 ml 37% HCl "
            "and stir for 1 h at 4 C."
        ),
    },
    {
        "step_number": 3,
        "action": "FILTER",
        "description": (
            "Pour the suspension into 1 L distilled water pre-cooled to 4 C and "
            "filter through filter paper."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Wash the residue five times with 500 ml distilled water and resuspend "
            "it in 1 L distilled water."
        ),
    },
    {
        "step_number": 5,
        "action": "ADJUST_PH",
        "description": "Neutralise the suspension to pH 6.5 with 10 ml of 5 M KOH.",
    },
    {
        "step_number": 6,
        "action": "FILTER",
        "description": "Filter and wash with 3 L distilled water to remove KCl.",
    },
)

NOTES = (
    "DSMZ Medium 766 prepares its chitin stock solution by acid-treating 20 g "
    "practical-grade crab-shell chitin with 200 ml 37% HCl at 4 C, pouring the "
    "suspension into 1 L cold distilled water, filtering and washing the residue, "
    "resuspending it in 1 L water, neutralising it with 10 ml 5 M KOH to pH 6.5, "
    "and washing with 3 L water to remove KCl."
)


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


def _signature(rows: Any, label: str) -> tuple[tuple[str, str, str], ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError(f"{label} is not a list")
    signature: list[tuple[str, str, str]] = []
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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != RECORD_ID:
        raise ValueError(f"expected id {RECORD_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != MEDIA_TERM:
        raise ValueError(f"expected media term {MEDIA_TERM}, found {_source_term_id(doc)!r}")

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in {IMPORTED_INGREDIENTS, FINAL_INGREDIENTS}:
        raise ValueError(f"{PATH}: composition signature drifted to {signature!r}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    if DSMZ_766 not in existing:
        references.append({"reference": DSMZ_766})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_766,
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


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["notes"] = NOTES
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / PATH
    return {path: repair_record(_load(path))}


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
