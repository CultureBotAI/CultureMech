#!/usr/bin/env python3
"""Repair TOGO M1539 / NBRC Medium 331 SP5 Medium."""

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
TARGET = Path("bacterial/sp5_medium.yaml")
EXPECTED_ID = "CultureMech:008086"
EXPECTED_MEDIA_TERM = "TOGO:M1539"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1539_sp5_score15.py"
ACTION = "RESOLVED_TOGO_M1539_SP5_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1539 = "https://togomedium.org/medium/M1539"
NBRC_331 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=331"
REFERENCES = (TOGO_M1539, NBRC_331)
SOURCE = "TOGO M1539 / NBRC Medium 331"
TITLE = "SP5 Medium"

BACTO_CASITONE = "Bacto Casitone (Difco)"
YEAST_EXTRACT = "Yeast extract"
AGAR = "Agar (if needed)"
SEAWATER = "Seawater"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (YEAST_EXTRACT, "1", "G_PER_L"),
    (AGAR, "15", "G_PER_L"),
    (BACTO_CASITONE, "9", "G_PER_L"),
)
IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (("Seawater*", "1", "G_PER_L", ()),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (BACTO_CASITONE, "9.0", "G_PER_L"),
    (YEAST_EXTRACT, "1.0", "G_PER_L"),
    (AGAR, "15.0", "G_PER_L"),
    (SEAWATER, "1000.0", "ML_PER_L"),
)
FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = ()

GROUNDINGS: dict[str, tuple[str, str]] = {
    YEAST_EXTRACT: ("FOODON:03315426", "yeast extract"),
    AGAR: ("CHEBI:2509", "agar"),
}

NOTES = (
    "TOGO M1539 imports SP5 Medium from NBRC Medium 331. NBRC Medium 331 lists "
    "9 g Bacto Casitone from Difco, 1 g Yeast extract, optional 15 g Agar, "
    "and 1 L Seawater per liter, with the final pH at 7.2. The NBRC footnote "
    "defines the seawater as filtered, aged seawater or artificial seawater "
    "from Daigo's Artificial Seawater SP."
)


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
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }

    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        term = _term(*grounding)
        row["term"] = term
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        BACTO_CASITONE,
        "9.0",
        "G_PER_L",
        notes=(
            f"{SOURCE} lists 9 g/L Bacto Casitone from Difco; this commercial "
            "casein digest is retained as an opaque complex component."
        ),
    ),
    _component(
        YEAST_EXTRACT,
        "1.0",
        "G_PER_L",
        notes=f"{SOURCE} lists 1 g/L Yeast extract.",
    ),
    _component(
        AGAR,
        "15.0",
        "G_PER_L",
        notes=f"{SOURCE} lists 15 g/L Agar as an optional solidifying agent.",
    ),
    _component(
        SEAWATER,
        "1000.0",
        "ML_PER_L",
        notes=(
            f"{SOURCE} lists 1 L/L Seawater and allows either filtered, aged "
            "seawater or Daigo's Artificial Seawater SP; the exact salt "
            "composition is source-variable."
        ),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Dissolve Bacto Casitone and Yeast extract in Seawater.",
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": "Add Agar when a solid SP5 medium is needed.",
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": "Bring SP5 Medium to pH 7.2.",
    },
)


def _put_after(doc: dict[str, Any], key: str, value: Any, after_key: str) -> None:
    if key in doc:
        doc[key] = value
        return

    rebuilt: dict[str, Any] = {}
    placed = False
    for existing_key, existing_value in doc.items():
        rebuilt[existing_key] = existing_value
        if existing_key == after_key:
            rebuilt[key] = value
            placed = True
    if not placed:
        rebuilt[key] = value

    doc.clear()
    doc.update(rebuilt)


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


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError("solution row lacks concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(solution.get("composition"), "solution composition"),
            )
        )
    return tuple(signatures)


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

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(
            f"{TARGET}: solution signature drifted from "
            f"{IMPORTED_SOLUTION_SIGNATURES!r} to {solution_signatures!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag
        not in {
            "incomplete_composition",
            "needs_manual_curation",
        }
    ]
    flags.extend(
        (
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        )
    )
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected the imported seawater unit, replaced the "
            "MediaDive seawater stock reference with the official NBRC "
            "source-level seawater input, grounded yeast extract and optional "
            "agar, and kept Bacto Casitone and seawater as sourced unmapped "
            "complex inputs."
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
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.2, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(PREPARATION_STEPS)),
        "ingredients",
    )
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
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
