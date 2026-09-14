#!/usr/bin/env python3
"""Repair DSMZ Medium 1550 EX-LM."""

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
TARGET = Path("bacterial/ex_lm_medium.yaml")
EXPECTED_ID = "CultureMech:001028"
EXPECTED_MEDIA_TERM = "mediadive.medium:1550"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_dsmz_1550_ex_lm_score15.py"
ACTION = "RESOLVED_DSMZ_1550_EX_LM_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

DSMZ_1550_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1550.pdf"
MEDIADIVE_1550 = "https://mediadive.dsmz.de/medium/1550"
SOURCE = "DSMZ Medium 1550"
TITLE = "EX-LM MEDIUM"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Casitone", "5", "G_PER_L"),
    ("Yeast extract", "5", "G_PER_L"),
    ("MgSO4 x 7 H2O", "2", "G_PER_L"),
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _grounded_component(
    preferred_term: str,
    value: str,
    unit: str,
    term: tuple[str, str],
    notes: str,
) -> dict[str, Any]:
    row = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
        "term": _term(*term),
    }
    if term[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Casitone",
        "concentration": {"value": "5.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": (
            "DSMZ Medium 1550 lists 5.0 g/L Casitone; this casein digest is "
            "retained as an opaque complex component."
        ),
    },
    _grounded_component(
        "Yeast extract",
        "5.0",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        "DSMZ Medium 1550 lists 5.0 g/L yeast extract.",
    ),
    _grounded_component(
        "MgSO4 x 7 H2O",
        "2.0",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        "DSMZ Medium 1550 lists 2.0 g/L MgSO4 x 7 H2O.",
    ),
    _grounded_component(
        "Distilled water",
        "1000.0",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        "DSMZ Medium 1550 makes the recipe with 1000.0 ml distilled water.",
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "pH needs no adjustment.",
    },
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in INGREDIENTS
)
REFERENCES = (MEDIADIVE_1550, DSMZ_1550_PDF)
NOTES = (
    "DSMZ Medium 1550 defines EX-LM Medium as 5.0 g/L Casitone, 5.0 g/L yeast "
    "extract, 2.0 g/L MgSO4 x 7 H2O, and 1000.0 ml distilled water, with no pH "
    "adjustment."
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


def _ingredient_signature(rows: Any) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("ingredients is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("ingredients contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"ingredient {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_MEDIA_TERM:
        raise ValueError(
            f"{TARGET}: expected source term {EXPECTED_MEDIA_TERM}, found {source_term!r}"
        )

    signature = _ingredient_signature(doc.get("ingredients"))
    if signature not in {IMPORTED_INGREDIENT_SIGNATURE, FINAL_INGREDIENT_SIGNATURE}:
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {signature!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for flag in ("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_1550_PDF,
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
    _require_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repair(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_record(_load(path))}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repair(args.normalized_dir)
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
