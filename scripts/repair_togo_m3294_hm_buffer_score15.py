#!/usr/bin/env python3
"""Repair TOGO M3294 HM Buffer."""

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
TARGET = Path("bacterial/hm_buffer.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m3294_hm_buffer_score15.py"
ACTION = "RESOLVED_TOGO_M3294_HM_BUFFER_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:009705"
EXPECTED_MEDIA_TERM = "TOGO:M3294"
TOGO_M3294 = "https://togomedium.org/medium/M3294"
NBRC_1663 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1663"
SOURCE = "NBRC Medium 1663"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("HEPES", "5", "G_PER_L"),
    ("UPW", "100", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("UPW", "1000.0", "ML_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    ("CaCl2 solution", "600", "G_PER_L", ()),
    ("MgCl2 solution", "333", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    ("0.5 M HEPES", "50.0", "ML_PER_L", (("HEPES", "0.5", "MOLAR"),)),
    ("0.5 M CaCl2 solution", "6.0", "ML_PER_L", (("CaCl2", "0.5", "MOLAR"),)),
    ("0.6 M MgCl2 solution", "3.33", "ML_PER_L", (("MgCl2", "0.6", "MOLAR"),)),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "CaCl2": ("CHEBI:3312", "calcium dichloride"),
    "HEPES": ("CHEBI:46756", "HEPES"),
    "MgCl2": ("CHEBI:6636", "magnesium dichloride"),
    "UPW": ("CHEBI:15377", "water"),
}

UNIT_LABELS = {
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
}

NOTES = (
    "TOGO M3294 imports NBRC Medium 1663 HM Buffer. NBRC 1663 prepares the "
    "buffer from 5 ml 0.5 M HEPES filled to 100 ml with UPW, adjusted to pH "
    "7.4, autoclaved, then supplemented with 600 ul 0.5 M CaCl2 and 333 ul "
    "0.6 M MgCl2. Volumes are normalized 10x from the 100 ml source recipe."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "FILTER_STERILIZE",
        "description": "Prepare filter-sterilized 0.5 M CaCl2 and 0.6 M MgCl2 stocks.",
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": "Dilute 50.0 ml/L 0.5 M HEPES to 1000.0 ml/L with UPW.",
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.4.",
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": "Sterilize the HEPES/UPW base by autoclaving.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "After autoclaving, add 6.0 ml/L 0.5 M CaCl2 stock and "
            "3.33 ml/L 0.6 M MgCl2 stock."
        ),
    },
)

STERILIZATION = {"method": "AUTOCLAVE"}


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
    source: str = SOURCE,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": (
            notes
            or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}."
        ),
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _stock(
    preferred_term: str,
    volume: str,
    solute: str,
    molarity: str,
    *,
    notes: str,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": volume, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": notes,
        "composition": [
            _component(
                solute,
                molarity,
                "MOLAR",
                notes=f"{SOURCE} uses a {molarity} M {solute} stock.",
            )
        ],
        "name": preferred_term,
    }
    if preparation_notes is not None:
        row["preparation_notes"] = preparation_notes
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "UPW",
        "1000.0",
        "ML_PER_L",
        notes=(
            f"{SOURCE} fills the 0.5 M HEPES dilution to 100 ml with UPW, "
            "normalized here as q.s. to 1000.0 ml/L."
        ),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock(
        "0.5 M HEPES",
        "50.0",
        "HEPES",
        "0.5",
        notes=(
            f"{SOURCE} dilutes 5 ml 0.5 M HEPES to 100 ml before pH "
            "adjustment and autoclaving."
        ),
    ),
    _stock(
        "0.5 M CaCl2 solution",
        "6.0",
        "CaCl2",
        "0.5",
        notes=(
            f"{SOURCE} adds 600 ul 0.5 M CaCl2 solution to the 100 ml "
            "autoclaved HEPES base."
        ),
        preparation_notes="Filter-sterilize before post-autoclave addition.",
    ),
    _stock(
        "0.6 M MgCl2 solution",
        "3.33",
        "MgCl2",
        "0.6",
        notes=(
            f"{SOURCE} adds 333 ul 0.6 M MgCl2 solution to the 100 ml "
            "autoclaved HEPES base."
        ),
        preparation_notes="Filter-sterilize before post-autoclave addition.",
    ),
)


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


def _solution_signature(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError(f"{label} is not a list")

    signature: list[SolutionSignature] = []
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
                _signature(row.get("composition"), f"{label} composition"),
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

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signature = _solution_signature(doc.get("solutions"), "solutions")
    if solution_signature not in (
        IMPORTED_SOLUTION_SIGNATURE,
        FINAL_SOLUTION_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "has_unmapped_ingredients",
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
    ):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in (TOGO_M3294, NBRC_1663):
        if reference not in existing:
            references.append({"reference": reference})


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": f"{TOGO_M3294}; {NBRC_1663}",
        "notes": (
            f"{NOTES} Converted the imported HEPES, UPW, CaCl2, and MgCl2 "
            "g/L artifacts to source volumes; expanded the salt stock "
            "solutions; added pH 7.4 and preparation steps; and grounded all "
            "disclosed chemical components."
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
    _put_after(repaired, "ph_value", 7.4, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(PREPARATION_STEPS)),
        "notes",
    )
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
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
