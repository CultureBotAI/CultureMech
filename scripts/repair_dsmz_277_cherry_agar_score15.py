#!/usr/bin/env python3
"""Repair DSMZ Medium 277 Cherry Agar by nesting its cherry extract."""

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
PATH = Path("bacterial/cherry_agar_cbs_formula.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_dsmz_277_cherry_agar_score15.py"
ACTION = "RESOLVED_DSMZ_277_CHERRY_AGAR_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

RECORD_ID = "CultureMech:001374"
MEDIA_TERM = "mediadive.medium:277"
DSMZ_277 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium277.pdf"
SOURCE = "DSMZ Medium 277"

IMPORTED_INGREDIENTS = (
    ("Agar", "20", "G_PER_L"),
    ("Pulp of sour stone cherries", "200", "G_PER_L"),
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
        "Agar",
        "20.0",
        "G_PER_L",
        "DSMZ Medium 277 dissolves 20.0 g agar in the final agar base.",
        term=("CHEBI:2509", "agar"),
    ),
    _ingredient(
        "Distilled water",
        "800.0",
        "ML_PER_L",
        "DSMZ Medium 277 dissolves agar in 800 ml water before adding cherry extract.",
        term=("CHEBI:15377", "water"),
    ),
)

CHERRY_EXTRACT_COMPOSITION: tuple[dict[str, Any], ...] = (
    _ingredient(
        "Pulp of sour stone cherries",
        "200.0",
        "G_PER_L",
        "DSMZ Medium 277 extracts 200.0 g pulp of sour stone cherries in water.",
    ),
    _ingredient(
        "Distilled water",
        "1000.0",
        "ML_PER_L",
        "DSMZ Medium 277 adds 1 l water while preparing the cherry extract.",
        term=("CHEBI:15377", "water"),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Cherry extract",
        "concentration": {"value": "200.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": "DSMZ Medium 277 adds 200 ml sterilized cherry extract.",
        "composition": list(copy.deepcopy(CHERRY_EXTRACT_COMPOSITION)),
        "preparation_notes": (
            "Add 1 l water to 200.0 g pulp of sour stone cherries, heat to "
            "boiling, simmer gently for 2 h, strain through cloth, and "
            "sterilize at 110 C for 30 min."
        ),
    },
)

FINAL_INGREDIENTS = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in INGREDIENTS
)
FINAL_SOLUTIONS = (
    (
        "Cherry extract",
        "200.0",
        "ML_PER_L",
        tuple(
            (
                str(row["preferred_term"]),
                str(row["concentration"]["value"]),
                str(row["concentration"]["unit"]),
            )
            for row in CHERRY_EXTRACT_COMPOSITION
        ),
    ),
)

PREPARATION_STEPS = (
    {
        "step_number": 1,
        "action": "HEAT",
        "description": (
            "Add 1 l water to 200.0 g pulp of sour stone cherries, heat to "
            "boiling, simmer gently for 2 h, and strain through cloth."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Sterilize the cherry extract at 110 C for 30 min.",
    },
    {
        "step_number": 3,
        "action": "DISSOLVE",
        "description": "Dissolve 20.0 g agar in 800 ml water and sterilize.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Add 200 ml cherry extract, distribute in presterilized tubes, "
            "and sterilize for 5 min at 120 C."
        ),
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": (
        "DSMZ Medium 277 sterilizes the cherry extract at 110 C for 30 min "
        "and the distributed final medium at 120 C for 5 min."
    ),
}

NOTES = (
    "DSMZ Medium 277 prepares CHERRY AGAR (CBS formula) from a cherry extract "
    "made by simmering 200.0 g pulp of sour stone cherries in 1 l water, then "
    "adds 200 ml sterilized cherry extract to 20.0 g agar dissolved in 800 ml "
    "water. Final pH is 3.8-4.6."
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


def _solution_signatures(solutions: Any) -> tuple[tuple[str, str, str, tuple], ...]:
    if solutions is None:
        solutions = []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")
    signatures: list[tuple[str, str, str, tuple]] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"solution {solution.get('preferred_term')!r} lacks concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(solution.get("composition"), "solutions.composition"),
            )
        )
    return tuple(signatures)


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != RECORD_ID:
        raise ValueError(f"expected id {RECORD_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != MEDIA_TERM:
        raise ValueError(f"expected media term {MEDIA_TERM}, found {_source_term_id(doc)!r}")

    signature = (
        _signature(doc.get("ingredients"), "ingredients"),
        _solution_signatures(doc.get("solutions")),
    )
    if signature not in {
        (IMPORTED_INGREDIENTS, ()),
        (FINAL_INGREDIENTS, FINAL_SOLUTIONS),
    }:
        raise ValueError(f"{PATH}: composition signature drifted to {signature!r}")


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
    if DSMZ_277 not in existing:
        references.append({"reference": DSMZ_277})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_277,
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
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["sterilization"] = copy.deepcopy(STERILIZATION)
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
