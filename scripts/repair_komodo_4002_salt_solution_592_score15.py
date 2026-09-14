#!/usr/bin/env python3
"""Repair KOMODO 4002 salt solution from DSMZ Medium 592."""

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
TARGET = Path("bacterial/salt_solution_medium_592.yaml")
EXPECTED_ID = "CultureMech:005192"
EXPECTED_MEDIA_TERM = "komodo.medium:4002"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_4002_salt_solution_592_score15.py"
ACTION = "RESOLVED_KOMODO_4002_SALT_SOLUTION_592_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

DSMZ_592 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium592.pdf"

SOURCE = "DSMZ Medium 592"
TITLE = "Salt solution (medium 592)"

Component = tuple[str, str, str]
Term = tuple[str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (("H2SO4", "variable", "VARIABLE"),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("MnCl2 x 4 H2O", "18", "G_PER_L"),
    ("Na2B4O7 x 10 H2O", "44", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "2.2", "G_PER_L"),
    ("CuCl2 x H2O", "0.5", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.3", "G_PER_L"),
    ("VOSO4 x 2 H2O", "0.3", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
    ("H2SO4", "variable", "VARIABLE"),
)

REFERENCES = (DSMZ_592,)

NOTES = (
    "KOMODO Medium 4002 is a SubMedium import labeled Salt solution "
    "(medium 592). The DSMZ Medium 592 PDF has one embedded stock adjusted "
    "to pH 2.0 with H2SO4, Trace elements, prepared in 100.000 ml distilled "
    "water; this repair uses that stock formula. The local unrelated "
    "mediadive.solution:4002 Main sol. J298 record was not used."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    term: Term,
    source_amount: str,
) -> dict[str, Any]:
    term_ref = _term(*term)
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": (
            f"DSMZ Medium 592 Trace elements lists {source_amount} per "
            "100.000 ml; concentration scaled to per-litre units."
        ),
        "term": term_ref,
        "mediaingredientmech_chebi_term": copy.deepcopy(term_ref),
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        "MnCl2 x 4 H2O",
        "18",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        "1.800 g MnCl2 x 4 H2O",
    ),
    _ingredient(
        "Na2B4O7 x 10 H2O",
        "44",
        "G_PER_L",
        ("CHEBI:131366", "disodium tetraborate decahydrate"),
        "4.400 g Na2B4O7 x 10 H2O",
    ),
    _ingredient(
        "ZnSO4 x 7 H2O",
        "2.2",
        "G_PER_L",
        ("CHEBI:32312", "zinc sulfate heptahydrate"),
        "0.220 g ZnSO4 x 7 H2O",
    ),
    _ingredient(
        "CuCl2 x H2O",
        "0.5",
        "G_PER_L",
        ("CHEBI:49553", "copper(II) chloride"),
        "0.050 g CuCl2 x H2O",
    ),
    _ingredient(
        "Na2MoO4 x 2 H2O",
        "0.3",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        "0.030 g Na2MoO4 x 2 H2O",
    ),
    _ingredient(
        "VOSO4 x 2 H2O",
        "0.3",
        "G_PER_L",
        ("CHEBI:87009", "vanadyl sulfate dihydrate"),
        "0.030 g VOSO4 x 2 H2O",
    ),
    {
        "preferred_term": "Distilled water",
        "concentration": {"value": "1000.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": ("DSMZ Medium 592 Trace elements lists distilled water brought to 100.000 ml."),
        "term": _term("CHEBI:15377", "water"),
        "mediaingredientmech_chebi_term": _term("CHEBI:15377", "water"),
    },
    {
        "preferred_term": "H2SO4",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": SOURCE,
        "notes": (
            "DSMZ Medium 592 Trace elements instructs adjustment to pH 2.0 "
            "with H2SO4 and gives no amount."
        ),
        "term": _term("CHEBI:26836", "sulfuric acid"),
        "mediaingredientmech_chebi_term": _term("CHEBI:26836", "sulfuric acid"),
    },
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Dissolve the trace-elements stock components in distilled water "
            "and bring to 100.000 ml."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust to pH 2.0 with H2SO4.",
    },
)


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
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    if doc.get("solutions"):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
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
            f"{NOTES} Replaced the imported H2SO4-only pH-buffer stub with "
            "the complete DSMZ trace-elements stock formula, explicit water, "
            "the variable H2SO4 pH-adjustment row, and DSMZ preparation steps."
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
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ph_value"] = 2.0
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
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
