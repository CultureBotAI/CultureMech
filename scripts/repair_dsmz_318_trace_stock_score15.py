#!/usr/bin/env python3
"""Repair DSMZ Medium 318 trace-element stock KOMODO wrappers."""

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

CURATOR = "repair_dsmz_318_trace_stock_score15.py"
ACTION = "RESOLVED_DSMZ_318_TRACE_STOCK_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

DSMZ_318 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318.pdf"
SOURCE = "DSMZ Medium 318 trace element solution"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (("KOH", "variable", "VARIABLE"),)


@dataclass(frozen=True)
class Target:
    path: str
    expected_id: str
    expected_source_term: str


TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/trace_element_solution_medium_318.yaml",
        expected_id="CultureMech:004400",
        expected_source_term="komodo.medium:2118",
    ),
    Target(
        path="bacterial/KOMODO_3073_Trace_element_solution_medium_318.yaml",
        expected_id="CultureMech:004859",
        expected_source_term="komodo.medium:3073",
    ),
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    term: tuple[str, str],
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
    }


def _step(step_number: int, action: str, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": action,
        "description": description,
    }


def _stock_note(name: str, amount: str) -> str:
    return f"DSMZ Medium 318 lists {amount} {name} in 1000.00 ml distilled water."


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Nitrilotriacetic acid (NTA)",
        "12.80",
        "G_PER_L",
        ("CHEBI:44557", "nitrilotriacetic acid"),
        _stock_note("Nitrilotriacetic acid", "12.80 g"),
    ),
    _component(
        "FeCl2 x 4 H2O",
        "1.00",
        "G_PER_L",
        ("CHEBI:86249", "iron dichloride tetrahydrate"),
        _stock_note("FeCl2 x 4 H2O", "1.00 g"),
    ),
    _component(
        "MnCl2 x 4 H2O",
        "0.10",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        _stock_note("MnCl2 x 4 H2O", "0.10 g"),
    ),
    _component(
        "CoCl2 x 6 H2O",
        "0.03",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        _stock_note("CoCl2 x 6 H2O", "0.03 g"),
    ),
    _component(
        "CaCl2 x 2 H2O",
        "0.10",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        _stock_note("CaCl2 x 2 H2O", "0.10 g"),
    ),
    _component(
        "ZnCl2",
        "0.10",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        _stock_note("ZnCl2", "0.10 g"),
    ),
    _component(
        "CuCl2",
        "0.02",
        "G_PER_L",
        ("CHEBI:49553", "copper(II) chloride"),
        _stock_note("CuCl2", "0.02 g"),
    ),
    _component(
        "H3BO3",
        "0.01",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        _stock_note("H3BO3", "0.01 g"),
    ),
    _component(
        "Na2MoO4 x 2 H2O",
        "0.03",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        _stock_note("Na2MoO4 x 2 H2O", "0.03 g"),
    ),
    _component(
        "NiCl2 x 6 H2O",
        "0.10",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        _stock_note("NiCl2 x 6 H2O", "0.10 g"),
    ),
    _component(
        "NaCl",
        "1.00",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        _stock_note("NaCl", "1.00 g"),
    ),
    _component(
        "Na2SeO3 x 5 H2O",
        "0.03",
        "G_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        _stock_note("Na2SeO3 x 5 H2O", "0.03 g"),
    ),
    _component(
        "Na2WO4 x 2 H2O",
        "0.04",
        "G_PER_L",
        ("CHEBI:63939", "sodium tungstate dihydrate"),
        _stock_note("Na2WO4 x 2 H2O", "0.04 g"),
    ),
    _component(
        "Distilled water",
        "1000.00",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        "DSMZ Medium 318 makes the trace element solution up to 1000.00 ml.",
    ),
    _component(
        "KOH",
        "variable",
        "VARIABLE",
        ("CHEBI:32035", "potassium hydroxide"),
        "DSMZ Medium 318 adjusts the trace element solution to pH 6.5 with KOH.",
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    _step(
        1,
        "MIX",
        "Dissolve NTA in 200 ml distilled water and adjust to pH 6.5 with KOH.",
    ),
    _step(
        2,
        "MIX",
        "Dissolve the mineral salts, adjust to pH 6.5 with KOH, and make up to 1000.00 ml.",
    ),
)

NOTES = (
    "DSMZ Medium 318 defines this trace element solution as NTA, mineral salts, "
    "distilled water, and KOH for adjustment to pH 6.5."
)

FINAL_INGREDIENT_SIGNATURE = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in INGREDIENTS
)
FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = ()

SOURCE_NOTES: dict[str, str] = {
    target.path: (
        f"Source: KOMODO ModelSEED | ID: {target.expected_source_term.removeprefix('komodo.medium:')} "
        "| Resolved as Trace element solution from DSMZ Medium 318 | SubMedium: Yes"
    )
    for target in TARGETS
}


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


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != target.expected_source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.expected_source_term}, "
            f"found {source_term!r}"
        )

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    solution_signature = _signature(doc.get("solutions"), "solutions")
    if (ingredient_signature, solution_signature) not in {
        (IMPORTED_INGREDIENT_SIGNATURE, ()),
        (FINAL_INGREDIENT_SIGNATURE, FINAL_SOLUTION_SIGNATURE),
    }:
        raise ValueError(
            f"{target.path}: ingredient/solution signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to "
            f"{ingredient_signature!r} / {solution_signature!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for flag in (
        "has_ontology_mappings",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    if DSMZ_318 not in existing:
        references.append({"reference": DSMZ_318})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_318,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["notes"] = SOURCE_NOTES[target.path]
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["ph_value"] = 6.5
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_record(_load(path), target)
    return plans


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
