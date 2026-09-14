#!/usr/bin/env python3
"""Repair TOGO M2974 BHI-TT from a one-liter source component."""

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
PATH = Path(
    "bacterial/"
    "brain_heart_infusion_broth_supplemented_with_0_1_tris_base_and_0_001_"
    "thiamine_monophosphate.yaml"
)
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2974_bhi_tt_score15.py"
ACTION = "RESOLVED_TOGO_M2974_BHI_TT_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

RECORD_ID = "CultureMech:009497"
MEDIA_TERM = "TOGO:M2974"
TOGO_M2974 = "https://togomedium.org/medium/M2974"
SOURCE = "TOGO M2974"

IMPORTED_INGREDIENTS = (
    ("Tris", "0.1", "PERCENT_W_V"),
    ("thiamine monophosphate", "0.001", "PERCENT_W_V"),
    ("brain-heart infusion broth (Difco Laboratories)", "1", "G_PER_L"),
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    notes: str,
    *,
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


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        "brain-heart infusion broth (Difco Laboratories)",
        "1000.0",
        "ML_PER_L",
        (
            "TOGO M2974 lists 1 L prepared brain-heart infusion broth from "
            "Difco Laboratories; the source does not spell out the commercial "
            "broth composition."
        ),
    ),
    _ingredient(
        "Tris",
        "0.1",
        "PERCENT_W_V",
        "TOGO M2974 supplements BHI broth with 0.1% Tris base.",
        term=("CHEBI:9754", "tris"),
    ),
    _ingredient(
        "thiamine monophosphate",
        "0.001",
        "PERCENT_W_V",
        "TOGO M2974 supplements BHI broth with 0.001% thiamine monophosphate.",
        term=("CHEBI:9533", "thiamine(1+) monophosphate"),
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
        "action": "MIX",
        "description": (
            "Supplement 1 L prepared brain-heart infusion broth with 0.1% "
            "Tris base and 0.001% thiamine monophosphate."
        ),
    },
)

NOTES = (
    "TOGO M2974 records BHI-TT as 1 L brain-heart infusion broth from Difco "
    "Laboratories supplemented with 0.1% Tris base and 0.001% thiamine "
    "monophosphate; the source does not spell out the commercial broth "
    "composition."
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
        raise ValueError(
            f"expected media term {MEDIA_TERM}, found {_source_term_id(doc)!r}"
        )

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in {IMPORTED_INGREDIENTS, FINAL_INGREDIENTS}:
        raise ValueError(
            f"{PATH}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENTS!r} to {signature!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    for flag in (
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    if TOGO_M2974 not in existing:
        references.append({"reference": TOGO_M2974})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": TOGO_M2974,
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
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["notes"] = NOTES
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
