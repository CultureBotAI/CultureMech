#!/usr/bin/env python3
"""Repair TOGO M2041 / NBRC 1339 M9-Phenanthrene."""

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
TARGET = Path("bacterial/m9_phenanthrene.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2041_m9_phenanthrene_score15.py"
ACTION = "RESOLVED_TOGO_M2041_M9_PHENANTHRENE_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:008631"
EXPECTED_MEDIA_TERM = "TOGO:M2041"
TOGO_M2041 = "https://togomedium.org/medium/M2041"
NBRC_1339 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1339"
TOGO_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2041"
SOURCE = "TOGO M2041 / NBRC Medium 1339"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("distilled water", "901.0", "G_PER_L"),
    ("agar", "15", "G_PER_L"),
    ("NaCl", "5", "G_PER_L"),
    ("KH2PO4", "30", "G_PER_L"),
    ("NH4Cl", "10", "G_PER_L"),
    ("Na2HPO4", "60", "G_PER_L"),
    ("dimethyl sulfoxide (DMSO)", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    ("CaCl2 solution (0.1 M)***", "1", "G_PER_L", ()),
    ("MgSO4 solution (1 M)***", "2.1", "G_PER_L", ()),
    ("Agar solution*", "900", "G_PER_L", ()),
    ("10xM9 solution**", "100", "G_PER_L", ()),
    (
        "Phenanthrene solution (250 mM) in dimethyl sulfoxide (DMSO)****",
        "10",
        "G_PER_L",
        (),
    ),
    ("Phenanthrene solution", "variable", "VARIABLE", ()),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Agar solution", "900", "ML_PER_L"),
    ("10xM9 solution", "100", "ML_PER_L"),
    ("MgSO4 solution", "2.1", "ML_PER_L"),
    ("CaCl2 solution", "1", "ML_PER_L"),
    ("Phenanthrene solution", "10", "ML_PER_L"),
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

FINAL_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    ("Agar solution", "900", "ML_PER_L", AGAR_SIGNATURE),
    ("10xM9 solution", "100", "ML_PER_L", M9_SIGNATURE),
    ("MgSO4 solution", "2.1", "ML_PER_L", MGSO4_SIGNATURE),
    ("CaCl2 solution", "1", "ML_PER_L", CALCIUM_SIGNATURE),
    ("Phenanthrene solution", "10", "ML_PER_L", PHENANTHRENE_SIGNATURE),
)

PREVIOUS_FINAL_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    ("Agar solution", "", "", AGAR_SIGNATURE),
    ("10xM9 solution", "", "", M9_SIGNATURE),
    ("MgSO4 solution", "", "", MGSO4_SIGNATURE),
    ("CaCl2 solution", "", "", CALCIUM_SIGNATURE),
    ("Phenanthrene solution", "", "", PHENANTHRENE_SIGNATURE),
)

REFERENCES = (TOGO_M2041, NBRC_1339, TOGO_API)

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
    grounding = GROUNDINGS[preferred_term]
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
        "term": _term(*grounding),
        "mediaingredientmech_chebi_term": _term(*grounding),
    }


def _stock(preferred_term: str, value: str, unit: str, notes: str) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _stock(
        "Agar solution",
        "900",
        "ML_PER_L",
        f"{SOURCE} adds 900 ml/L autoclaved agar solution.",
    ),
    _stock(
        "10xM9 solution",
        "100",
        "ML_PER_L",
        f"{SOURCE} adds 100 ml/L separately autoclaved 10xM9 solution.",
    ),
    _stock(
        "MgSO4 solution",
        "2.1",
        "ML_PER_L",
        f"{SOURCE} adds 2.1 ml/L 1 M MgSO4 stock.",
    ),
    _stock(
        "CaCl2 solution",
        "1",
        "ML_PER_L",
        f"{SOURCE} adds 1 ml/L 0.1 M CaCl2 stock.",
    ),
    _stock(
        "Phenanthrene solution",
        "10",
        "ML_PER_L",
        f"{SOURCE} adds 10 ml/L 250 mM phenanthrene solution in DMSO.",
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Agar solution",
        "concentration": {"value": "900", "unit": "ML_PER_L"},
        "composition": [
            _component(
                "Agar",
                "15",
                "G_PER_L",
                "NBRC Medium 1339 dissolves 15 g agar in 900 ml distilled water.",
            ),
            _component(
                "Distilled water",
                "900",
                "ML_PER_L",
                "NBRC Medium 1339 prepares the agar solution in 900 ml water.",
            ),
        ],
        "name": "Agar solution",
    },
    {
        "preferred_term": "10xM9 solution",
        "concentration": {"value": "100", "unit": "ML_PER_L"},
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
        "concentration": {"value": "2.1", "unit": "ML_PER_L"},
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
        "concentration": {"value": "1", "unit": "ML_PER_L"},
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
        "concentration": {"value": "10", "unit": "ML_PER_L"},
        "composition": [
            _component(
                "Phenanthrene",
                "250",
                "MILLIMOLAR",
                "NBRC Medium 1339 adds 10 ml/L of 250 mM phenanthrene solution.",
            ),
            _component(
                "Dimethyl sulfoxide (DMSO)",
                "variable",
                "VARIABLE",
                "NBRC Medium 1339 uses DMSO as the phenanthrene stock solvent.",
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
            "Dissolve MgSO4 and CaCl2 stocks in distilled water and sterilize " "by autoclaving."
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
    "TOGO M2041 imports NBRC Medium 1339 M9-Phenanthrene. NBRC 1339 lists "
    "900 ml agar solution, 100 ml 10xM9 solution, 2.1 ml 1 M MgSO4, 1 ml "
    "0.1 M CaCl2, and 10 ml 250 mM phenanthrene in DMSO per liter. Agar, "
    "10xM9, MgSO4, and CaCl2 are autoclaved; the phenanthrene stock is "
    "filter-sterilized, added after cooling to 65 C, sonicated for about "
    "30 seconds, and poured into plates."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration") or {}
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} has bad concentration")
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
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration") or {}
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} has bad concentration")
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
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")
    if _solution_signature(doc.get("solutions"), "solutions") not in (
        IMPORTED_SOLUTION_SIGNATURE,
        PREVIOUS_FINAL_SOLUTION_SIGNATURE,
        FINAL_SOLUTION_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)
    while "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


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
            f"{NOTES} Removed the flattening artifact that merged agar water "
            "with 10xM9 water, restored five stock additions in ml/L, and "
            "expanded their nested compositions."
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
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    repaired["notes"] = NOTES
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["sterilization"] = {"method": "AUTOCLAVE"}
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
