#!/usr/bin/env python3
"""Repair TOGO M1070 Acidithrix Ferrooydans Medium."""

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
TARGET = Path("bacterial/TOGO_M1070_Acidithrix_Ferrooydans_Medium.yaml")
EXPECTED_ID = "CultureMech:007588"
EXPECTED_MEDIA_TERM = "TOGO:M1070"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1070_score15.py"
ACTION = "RESOLVED_TOGO_M1070_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1070 = "https://togomedium.org/medium/M1070"
TOGO_M752 = "https://togomedium.org/medium/M752"
TOGO_M142 = "https://togomedium.org/medium/M142"
TOGO_M236 = "https://togomedium.org/medium/M236"
JCM_1012 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1012"
JCM_729 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=729"
JCM_151 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151"
JCM_244 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244"

SOURCE = "TOGO M1070 / JCM Medium 1012"
UBS_SOURCE = "TOGO M752 / JCM Medium 729"
TRACE_SOURCE = "TOGO M142 / JCM Medium 151"
NISEW_SOURCE = "TOGO M236 / JCM Medium 244"
TITLE = "Acidithrix Ferrooydans Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "0.2", "G_PER_L"),
    ("Glucose", "0.9", "G_PER_L"),
    ("H2SO4", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("Yeast extract", "0.2", "G_PER_L"),
    ("Glucose", "0.9", "G_PER_L"),
    ("H2SO4", "variable", "VARIABLE"),
)

UBS_SIGNATURE: tuple[Component, ...] = (
    ("Na2SO4", "14.0", "G_PER_L"),
    ("(NH4)2SO4", "30.0", "G_PER_L"),
    ("KCl", "1.0", "G_PER_L"),
    ("MgSO4 x 7H2O", "5.0", "G_PER_L"),
    ("K2HPO4", "0.5", "G_PER_L"),
    ("Ca(NO3)2 x 4H2O", "0.14", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

TRACE_MINERALS_SIGNATURE: tuple[Component, ...] = (
    ("Nitrilotriacetic acid", "1.5", "G_PER_L"),
    ("MgSO4 x 7H2O", "3.0", "G_PER_L"),
    ("MnSO4 x n H2O", "0.5", "G_PER_L"),
    ("NaCl", "1.0", "G_PER_L"),
    ("FeSO4 x 7H2O", "0.1", "G_PER_L"),
    ("CoSO4 x 7H2O", "0.1", "G_PER_L"),
    ("CaCl2 x 2H2O", "0.1", "G_PER_L"),
    ("ZnSO4 x 7H2O", "0.1", "G_PER_L"),
    ("CuSO4 x 5H2O", "0.01", "G_PER_L"),
    ("AlK(SO4)2", "0.01", "G_PER_L"),
    ("H3BO3", "0.01", "G_PER_L"),
    ("Na2MoO4 x 2H2O", "0.01", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("KOH solution", "variable", "VARIABLE"),
)

NISEW_SIGNATURE: tuple[Component, ...] = (
    ("NiCl2 x 6H2O", "25.0", "MG_PER_L"),
    ("(NH4)2Ni(SO4)2 x 6H2O", "2.0", "G_PER_L"),
    ("Na2SeO3", "0.3", "MG_PER_L"),
    ("Na2SeO4", "10.0", "MG_PER_L"),
    ("Na2WO4 x 2H2O", "10.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)

FESO4_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("FeSO4", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("UBS solution (see Medium [M752])", "100", "G_PER_L", ()),
    ("Trace minerals (see Medium [M142])", "10", "G_PER_L", ()),
    ("Ni-Se-W solution (see Medium [M236])", "10", "G_PER_L", ()),
    ("1 M FeSO4 solution (pH 2.0)", "5", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("UBS solution", "100.0", "ML_PER_L", UBS_SIGNATURE),
    ("Trace minerals", "10.0", "ML_PER_L", TRACE_MINERALS_SIGNATURE),
    ("Ni-Se-W solution", "10.0", "ML_PER_L", NISEW_SIGNATURE),
    ("1 M FeSO4 solution (pH 2.0)", "5.0", "ML_PER_L", FESO4_STOCK_SIGNATURE),
)

REFERENCES = (
    TOGO_M1070,
    JCM_1012,
    TOGO_M752,
    JCM_729,
    TOGO_M142,
    JCM_151,
    TOGO_M236,
    JCM_244,
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)2SO4": ("CHEBI:62946", "ammonium sulfate"),
    "AlK(SO4)2": ("CHEBI:86463", "potassium aluminium sulfate"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CoSO4 x 7H2O": ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    "CuSO4 x 5H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeSO4": ("CHEBI:75832", "iron(2+) sulfate (anhydrous)"),
    "FeSO4 x 7H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "H2SO4": ("CHEBI:26836", "sulfuric acid"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "KOH solution": ("CHEBI:32035", "potassium hydroxide"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnSO4 x n H2O": ("CHEBI:86360", "manganese(II) sulfate hydrate"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2SeO4": ("CHEBI:77775", "sodium selenate"),
    "Na2SO4": ("CHEBI:32149", "sodium sulfate"),
    "Na2WO4 x 2H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NiCl2 x 6H2O": ("CHEBI:53542", "nickel chloride hexahydrate"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "ZnSO4 x 7H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
}


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
    source: str,
    notes: str,
    term: tuple[str, str] | None | bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }

    grounding: tuple[str, str] | None
    if term is True:
        grounding = GROUNDINGS.get(preferred_term)
    elif term is False:
        grounding = None
    else:
        grounding = term

    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)

    return row


def _listed_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    term: tuple[str, str] | None | bool = True,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        term=term,
    )


def _adjustment_component(
    preferred_term: str,
    *,
    source: str,
    notes: str,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        "variable",
        "VARIABLE",
        source=source,
        notes=notes,
    )


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _listed_component("Distilled water", "1.0", "L", source=SOURCE),
    _listed_component(
        "Yeast extract",
        "0.2",
        "G_PER_L",
        source=SOURCE,
        term=False,
    ),
    _listed_component("Glucose", "0.9", "G_PER_L", source=SOURCE),
    _adjustment_component(
        "H2SO4",
        source=SOURCE,
        notes=f"{SOURCE} adjusts the medium to pH 2.5 with H2SO4.",
    ),
)


def _ubs_solution() -> dict[str, Any]:
    return {
        "preferred_term": "UBS solution",
        "concentration": {"value": "100.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds 100.0 ml/L UBS solution from M752/JCM 729.",
        "composition": [
            _listed_component("Na2SO4", "14.0", "G_PER_L", source=UBS_SOURCE),
            _listed_component("(NH4)2SO4", "30.0", "G_PER_L", source=UBS_SOURCE),
            _listed_component("KCl", "1.0", "G_PER_L", source=UBS_SOURCE),
            _listed_component("MgSO4 x 7H2O", "5.0", "G_PER_L", source=UBS_SOURCE),
            _listed_component("K2HPO4", "0.5", "G_PER_L", source=UBS_SOURCE),
            _listed_component(
                "Ca(NO3)2 x 4H2O",
                "0.14",
                "G_PER_L",
                source=UBS_SOURCE,
                term=False,
            ),
            _listed_component("Distilled water", "1.0", "L", source=UBS_SOURCE),
        ],
    }


def _trace_minerals() -> dict[str, Any]:
    return {
        "preferred_term": "Trace minerals",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds 10.0 ml/L Trace minerals from M142/JCM 151.",
        "composition": [
            _listed_component(
                "Nitrilotriacetic acid",
                "1.5",
                "G_PER_L",
                source=TRACE_SOURCE,
            ),
            _listed_component("MgSO4 x 7H2O", "3.0", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("MnSO4 x n H2O", "0.5", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("NaCl", "1.0", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("FeSO4 x 7H2O", "0.1", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("CoSO4 x 7H2O", "0.1", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("CaCl2 x 2H2O", "0.1", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("ZnSO4 x 7H2O", "0.1", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("CuSO4 x 5H2O", "0.01", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("AlK(SO4)2", "0.01", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("H3BO3", "0.01", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("Na2MoO4 x 2H2O", "0.01", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("Distilled water", "1.0", "L", source=TRACE_SOURCE),
            _adjustment_component(
                "KOH solution",
                source=TRACE_SOURCE,
                notes=(
                    f"{TRACE_SOURCE} adjusts nitrilotriacetic acid to pH 6.5 "
                    "with KOH solution before adding minerals."
                ),
            ),
        ],
        "preparation_notes": (
            "Dissolve nitrilotriacetic acid, adjust pH to 6.5 with KOH "
            "solution, add minerals, then adjust final pH to 7.0."
        ),
    }


def _nisew_solution() -> dict[str, Any]:
    return {
        "preferred_term": "Ni-Se-W solution",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds 10.0 ml/L Ni-Se-W solution from M236/JCM 244.",
        "composition": [
            _listed_component("NiCl2 x 6H2O", "25.0", "MG_PER_L", source=NISEW_SOURCE),
            _listed_component(
                "(NH4)2Ni(SO4)2 x 6H2O",
                "2.0",
                "G_PER_L",
                source=NISEW_SOURCE,
                term=False,
            ),
            _listed_component(
                "Na2SeO3",
                "0.3",
                "MG_PER_L",
                source=NISEW_SOURCE,
                term=False,
            ),
            _listed_component("Na2SeO4", "10.0", "MG_PER_L", source=NISEW_SOURCE),
            _listed_component("Na2WO4 x 2H2O", "10.0", "MG_PER_L", source=NISEW_SOURCE),
            _listed_component("Distilled water", "1.0", "L", source=NISEW_SOURCE),
        ],
    }


def _ferrous_sulfate_solution() -> dict[str, Any]:
    return {
        "preferred_term": "1 M FeSO4 solution (pH 2.0)",
        "concentration": {"value": "5.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            f"{SOURCE} adds 5.0 ml/L filter-sterilized 1 M FeSO4 solution "
            "at pH 2.0 after cooling."
        ),
        "composition": [
            _component(
                "FeSO4",
                "variable",
                "VARIABLE",
                source=SOURCE,
                notes=(
                    f"{SOURCE} lists a 1 M FeSO4 solution at pH 2.0; "
                    "the molar stock concentration is preserved in this note."
                ),
            )
        ],
        "preparation_notes": "Filter-sterilize.",
    }


SOLUTIONS: tuple[dict[str, Any], ...] = (
    _ubs_solution(),
    _trace_minerals(),
    _nisew_solution(),
    _ferrous_sulfate_solution(),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix UBS solution, Trace minerals, Ni-Se-W solution, glucose, "
            "yeast extract, and distilled water thoroughly."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the medium to pH 2.5 with H2SO4.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the acidified base medium.",
    },
    {
        "step_number": 4,
        "action": "FILTER_STERILIZE",
        "description": "Filter-sterilize 1 M FeSO4 solution at pH 2.0.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "After cooling, add 5.0 ml/L filter-sterilized 1 M FeSO4 "
            "solution at pH 2.0."
        ),
    },
)

NOTES = (
    "TOGO M1070 records JCM Medium 1012 with 100 ml/L UBS solution from "
    "M752/JCM 729, 10 ml/L Trace minerals from M142/JCM 151, 10 ml/L "
    "Ni-Se-W solution from M236/JCM 244, glucose, yeast extract, and "
    "distilled water. JCM 1012 adjusts the base to pH 2.5 with H2SO4, "
    "autoclaves it, then adds filter-sterilized 1 M FeSO4 solution at "
    "pH 2.0 after cooling."
)


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
        raise ValueError(f"{TARGET}: solution signature drifted")


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
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 2.5, "physical_state")
    repaired.pop("ph_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    _put_after(repaired, "sterilization", {"method": "AUTOCLAVE"}, "preparation_steps")
    _put_after(repaired, "notes", NOTES, "media_term")
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
