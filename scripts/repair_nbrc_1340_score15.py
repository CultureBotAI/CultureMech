#!/usr/bin/env python3
"""Repair the recovered NBRC Medium 1339 M9-Phenanthrene record."""

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
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_nbrc_1340_score15.py"
ACTION = "RESOLVED_NBRC_1340_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TARGET_PATH = "bacterial/NBRC_1340.yaml"
TARGET_ID = "CultureMech:007473"
REQUIRED_ACTION = "Recovered composition from source HTML"

SOURCE = "NBRC Medium 1339"
NBRC_URL = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1339"
TITLE = "M9-Phenanthrene"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Agar solution*", "900", "ML_PER_L"),
    ("10xM9 solution**", "100", "ML_PER_L"),
    ("MgSO4 solution (1 M)***", "2.1", "ML_PER_L"),
    ("CaCl2 solution (0.1 M)***", "1", "ML_PER_L"),
    (
        "Phenanthrene solution (250 mM) in dimethyl sulfoxide (DMSO)****",
        "10",
        "ML_PER_L",
    ),
)

AGAR_SIGNATURE: tuple[Component, ...] = (
    ("Agar", "15", "G_PER_L"),
    ("Distilled water", "900", "ML_PER_L"),
)

M9_SIGNATURE: tuple[Component, ...] = (
    ("KH2PO4", "30", "G_PER_L"),
    ("Na2HPO4", "60", "G_PER_L"),
    ("NH4Cl", "10", "G_PER_L"),
    ("NaCl", "5", "G_PER_L"),
    ("Distilled water", "1", "L"),
)

MGSO4_SIGNATURE: tuple[Component, ...] = (("MgSO4", "1", "MOLAR"),)
CALCIUM_SIGNATURE: tuple[Component, ...] = (("CaCl2", "0.1", "MOLAR"),)
PHENANTHRENE_SIGNATURE: tuple[Component, ...] = (
    ("Phenanthrene", "250", "MILLIMOLAR"),
    ("Dimethyl sulfoxide (DMSO)", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (("10xM9 solution", M9_SIGNATURE),)
FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Agar solution", AGAR_SIGNATURE),
    ("10xM9 solution", M9_SIGNATURE),
    ("MgSO4 solution", MGSO4_SIGNATURE),
    ("CaCl2 solution", CALCIUM_SIGNATURE),
    ("Phenanthrene solution", PHENANTHRENE_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "CaCl2": ("CHEBI:3312", "calcium chloride"),
    "Dimethyl sulfoxide (DMSO)": ("CHEBI:28262", "dimethyl sulfoxide"),
    "Distilled water": ("CHEBI:15377", "water"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "MgSO4": ("CHEBI:32599", "magnesium sulfate"),
    "Na2HPO4": ("CHEBI:34683", "disodium hydrogenphosphate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Phenanthrene": ("CHEBI:28851", "phenanthrene"),
}


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    notes: str,
) -> dict[str, Any]:
    term = GROUNDINGS[preferred_term]
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
    }


SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Agar solution",
        "composition": [
            _component(
                "Agar",
                "15",
                "G_PER_L",
                "NBRC Medium 1339 dissolves 15 g agar in the 900 ml agar solution.",
            ),
            _component(
                "Distilled water",
                "900",
                "ML_PER_L",
                ("NBRC Medium 1339 prepares the agar solution in 900 ml " "distilled water."),
            ),
        ],
        "name": "Agar solution",
    },
    {
        "preferred_term": "10xM9 solution",
        "composition": [
            _component(
                name,
                value,
                unit,
                f"NBRC Medium 1339 lists {value} {unit} {name} in 10xM9 solution.",
            )
            for name, value, unit in M9_SIGNATURE
        ],
        "name": "10xM9 solution",
    },
    {
        "preferred_term": "MgSO4 solution",
        "composition": [
            _component(
                "MgSO4",
                "1",
                "MOLAR",
                "NBRC Medium 1339 adds 2.1 ml/L of 1 M MgSO4 solution.",
            ),
        ],
        "name": "MgSO4 solution",
    },
    {
        "preferred_term": "CaCl2 solution",
        "composition": [
            _component(
                "CaCl2",
                "0.1",
                "MOLAR",
                "NBRC Medium 1339 adds 1 ml/L of 0.1 M CaCl2 solution.",
            ),
        ],
        "name": "CaCl2 solution",
    },
    {
        "preferred_term": "Phenanthrene solution",
        "composition": [
            _component(
                "Phenanthrene",
                "250",
                "MILLIMOLAR",
                ("NBRC Medium 1339 adds 10 ml/L of 250 mM phenanthrene " "solution in DMSO."),
            ),
            _component(
                "Dimethyl sulfoxide (DMSO)",
                "variable",
                "VARIABLE",
                (
                    "NBRC Medium 1339 uses dimethyl sulfoxide as the solvent "
                    "for the 250 mM phenanthrene stock."
                ),
            ),
        ],
        "name": "Phenanthrene solution",
    },
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "DISSOLVE",
        "description": "Dissolve 15 g agar in 900 ml distilled water.",
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the agar solution.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Sterilize the 10xM9 solution separately by autoclaving.",
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": (
            "Dissolve MgSO4 and CaCl2 stocks in distilled water and " "sterilize by autoclaving."
        ),
    },
    {
        "step_number": 5,
        "action": "FILTER_STERILIZE",
        "description": (
            "Filter-sterilize the 250 mM phenanthrene solution in DMSO using " "DMSO-safe filters."
        ),
    },
    {
        "step_number": 6,
        "action": "MIX",
        "description": ("Aseptically mix autoclaved agar, 10xM9, MgSO4, and CaCl2 " "solutions."),
    },
    {
        "step_number": 7,
        "action": "MIX",
        "description": (
            "After cooling to 65 C, aseptically add phenanthrene solution, "
            "sonicate for approximately 30 seconds, and pour into plates."
        ),
    },
)

NOTES = (
    "Source: NBRC Medium 1339 | Link: "
    "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1339\n\n"
    "NBRC lists M9-Phenanthrene as an agar medium prepared from autoclaved agar, "
    "10xM9, 1 M MgSO4, and 0.1 M CaCl2 solutions plus filter-sterilized "
    "250 mM phenanthrene in dimethyl sulfoxide. Phenanthrene is added after "
    "cooling to 65 C, mixed by sonication, and poured into plates."
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


def _solution_signature(solution: dict[str, Any]) -> SolutionSignature:
    return (
        str(solution.get("preferred_term") or ""),
        _signature(solution.get("composition"), "solution composition"),
    )


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")
    if any(not isinstance(solution, dict) for solution in solutions):
        raise ValueError("solutions contains a non-mapping row")
    return tuple(_solution_signature(solution) for solution in solutions)


def _has_history_action(doc: dict[str, Any], action: str) -> bool:
    return any(
        isinstance(event, dict) and event.get("action") == action
        for event in doc.get("curation_history") or []
    )


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != TARGET_ID:
        raise ValueError(f"{TARGET_PATH}: found id {doc.get('id')!r}, expected {TARGET_ID!r}")
    if not _has_history_action(doc, REQUIRED_ACTION):
        raise ValueError(f"{TARGET_PATH}: missing recovery action {REQUIRED_ACTION!r}")
    if doc.get("name") not in {"1340", TITLE}:
        raise ValueError(f"{TARGET_PATH}: NBRC title/name drifted")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature != IMPORTED_INGREDIENT_SIGNATURE:
        raise ValueError(
            f"{TARGET_PATH}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in {
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    }:
        raise ValueError(f"{TARGET_PATH}: nested solution signature drifted")


def _iter_components(doc: dict[str, Any]):
    for solution in doc.get("solutions") or []:
        yield from solution.get("composition") or []


def _grounded(component: dict[str, Any]) -> bool:
    term = component.get("term")
    return isinstance(term, dict) and bool(term.get("id"))


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)

    if any(not _grounded(row) for row in _iter_components(doc)):
        raise ValueError(f"{TARGET_PATH}: not all stock solution rows were grounded")


def _ensure_reference(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    found = {row.get("reference") for row in references if isinstance(row, dict)}
    if NBRC_URL not in found:
        references.append({"reference": NBRC_URL})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Grounded recovered NBRC Medium 1339 M9-Phenanthrene formula",
        "source": NBRC_URL,
        "notes": (
            "Added the NBRC Medium 1339 source term and official title, "
            "expanded missing agar, MgSO4, CaCl2, and phenanthrene stock "
            "solutions, and converted M9-Phenanthrene sterilization "
            "instructions into structured steps."
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


def repair_document(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "name", TITLE, "id")
    _put_after(repaired, "original_name", TITLE, "name")
    _put_after(
        repaired,
        "media_term",
        {
            "preferred_term": SOURCE,
            "term": _term("nbrc.medium:1339", SOURCE),
        },
        "physical_state",
    )
    _put_after(repaired, "notes", NOTES, "description")
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["sterilization"] = {"method": "AUTOCLAVE"}

    _ensure_flags(repaired)
    _ensure_reference(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET_PATH
    return {path: repair_document(_load(path))}


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

    action = "Updated" if args.apply else "Would update"
    print(f"{action} {changed_count} NBRC 1340 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
