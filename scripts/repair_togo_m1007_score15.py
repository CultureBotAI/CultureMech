#!/usr/bin/env python3
"""Repair TOGO M1007 Sea Salts TYG Medium."""

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
TARGET = Path("bacterial/TOGO_M1007_Sea_Salts_TYG_Medium.yaml")
EXPECTED_ID = "CultureMech:007520"
EXPECTED_MEDIA_TERM = "TOGO:M1007"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1007_score15.py"
ACTION = "RESOLVED_TOGO_M1007_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1007 = "https://togomedium.org/medium/M1007"
TOGO_M471 = "https://togomedium.org/medium/M471"
JCM_958 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=958"
JCM_470 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=470"

SOURCE = "TOGO M1007 / JCM Medium 958"
WOLFE_SOURCE = "TOGO M471 / JCM Medium 470"
TITLE = "Sea Salts TYG Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("Resazurin", "0.5", "G_PER_L"),
    ("Na2CO3", "1", "G_PER_L"),
    ("Sea Salts (Sigma)", "50", "G_PER_L"),
    ("Glucose", "1", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "1", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("Yeast extract", "1.0", "G_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("Na2CO3", "1.0", "G_PER_L"),
    ("Sea Salts (Sigma)", "50.0", "G_PER_L"),
    ("Glucose", "1.0", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "1.0", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

WOLFE_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("MgSO4 x 7H2O", "30.0", "G_PER_L"),
    ("MnSO4 x H2O", "5.0", "G_PER_L"),
    ("NaCl", "10.0", "G_PER_L"),
    ("FeSO4 x 7H2O", "1.0", "G_PER_L"),
    ("CoCl2 x 6H2O", "1.8", "G_PER_L"),
    ("CaCl2 x 2H2O", "1.0", "G_PER_L"),
    ("ZnSO4 x 7H2O", "1.8", "G_PER_L"),
    ("CuSO4 x 5H2O", "0.1", "G_PER_L"),
    ("KAl(SO4)2 x 12H2O", "0.18", "G_PER_L"),
    ("H3BO3", "0.1", "G_PER_L"),
    ("Na2MoO4 x 2H2O", "0.1", "G_PER_L"),
    ("(NH4)2Ni(SO4)2 x 6H2O", "2.8", "G_PER_L"),
    ("Na2WO4 x 2H2O", "0.1", "G_PER_L"),
    ("Na2SeO4", "0.1", "G_PER_L"),
    ("H2SO4", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Wolfe's mineral elixir (see Medium [M471])", "2", "G_PER_L", ()),
    ("Na2CO3 solution", "variable", "VARIABLE", ()),
    ("5% Na2S\u30fb9H2O solution", "6", "G_PER_L", ()),
    ("5% L--Cysteine\u30fbHCl\u30fbH2O solution", "6", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Wolfe's mineral elixir", "2.0", "ML_PER_L", WOLFE_SIGNATURE),
    ("5% Na2CO3 solution", "variable", "VARIABLE", (("Na2CO3", "50.0", "G_PER_L"),)),
    (
        "5% Na2S x 9H2O solution",
        "6.0",
        "ML_PER_L",
        (("Na2S x 9H2O", "50.0", "G_PER_L"),),
    ),
    (
        "5% L-Cysteine HCl H2O solution",
        "6.0",
        "ML_PER_L",
        (("L-Cysteine HCl H2O", "50.0", "G_PER_L"),),
    ),
)

REFERENCES = (TOGO_M1007, JCM_958, TOGO_M471, JCM_470)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)2Ni(SO4)2 x 6H2O": ("CHEBI:86149", "ammonium nickel sulfate hexahydrate"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "CoCl2 x 6H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuSO4 x 5H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeSO4 x 7H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "H2SO4": ("CHEBI:26836", "sulfuric acid"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "KAl(SO4)2 x 12H2O": (
        "CHEBI:86465",
        "potassium aluminium sulfate dodecahydrate",
    ),
    "L-Cysteine HCl H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Na2SeO4": ("CHEBI:77775", "sodium selenate"),
    "Na2WO4 x 2H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Trypticase peptone (BD-BBL)": ("MICRO:0000178", "peptone"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
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


def _source_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    term: tuple[str, str] | None | bool = True,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=SOURCE,
        notes=f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        term=term,
    )


def _wolfe_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    term: tuple[str, str] | None | bool = True,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=WOLFE_SOURCE,
        notes=f"{WOLFE_SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        term=term,
    )


def _wolfe_solution() -> dict[str, Any]:
    return {
        "preferred_term": "Wolfe's mineral elixir",
        "concentration": {"value": "2.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds 2.0 ml/L Wolfe's mineral elixir from TOGO M471.",
        "composition": [
            _wolfe_component("Distilled water", "1.0", "L"),
            _wolfe_component("MgSO4 x 7H2O", "30.0", "G_PER_L"),
            _wolfe_component(
                "MnSO4 x H2O",
                "5.0",
                "G_PER_L",
                term=False,
            ),
            _wolfe_component("NaCl", "10.0", "G_PER_L"),
            _wolfe_component("FeSO4 x 7H2O", "1.0", "G_PER_L"),
            _wolfe_component("CoCl2 x 6H2O", "1.8", "G_PER_L"),
            _wolfe_component("CaCl2 x 2H2O", "1.0", "G_PER_L"),
            _wolfe_component("ZnSO4 x 7H2O", "1.8", "G_PER_L"),
            _wolfe_component("CuSO4 x 5H2O", "0.1", "G_PER_L"),
            _wolfe_component("KAl(SO4)2 x 12H2O", "0.18", "G_PER_L"),
            _wolfe_component("H3BO3", "0.1", "G_PER_L"),
            _wolfe_component("Na2MoO4 x 2H2O", "0.1", "G_PER_L"),
            _wolfe_component("(NH4)2Ni(SO4)2 x 6H2O", "2.8", "G_PER_L"),
            _wolfe_component("Na2WO4 x 2H2O", "0.1", "G_PER_L"),
            _wolfe_component("Na2SeO4", "0.1", "G_PER_L"),
            _component(
                "H2SO4",
                "variable",
                "VARIABLE",
                source=WOLFE_SOURCE,
                notes=(
                    f"{WOLFE_SOURCE} adjusts Wolfe's mineral elixir to pH 1.0 "
                    "with diluted H2SO4 before dissolving the salts."
                ),
            ),
        ],
        "preparation_notes": (
            "First adjust the stock to pH 1.0 with diluted H2SO4, then "
            "dissolve the salts."
        ),
    }


def _five_percent_solution(
    preferred_term: str,
    solute: str,
    volume_ml: str,
    *,
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": volume_ml, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": notes,
        "composition": [
            _component(
                solute,
                "50.0",
                "G_PER_L",
                source=SOURCE,
                notes=f"Solute of the {preferred_term} added by {SOURCE}.",
            )
        ],
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _source_component("Distilled water", "1.0", "L"),
    _source_component("Yeast extract", "1.0", "G_PER_L"),
    _source_component("Resazurin", "0.5", "MG_PER_L"),
    _source_component("Na2CO3", "1.0", "G_PER_L"),
    _source_component("Sea Salts (Sigma)", "50.0", "G_PER_L", term=False),
    _source_component("Glucose", "1.0", "G_PER_L"),
    _source_component("Trypticase peptone (BD-BBL)", "1.0", "G_PER_L"),
    _component(
        "Carbon dioxide gas",
        "variable",
        "VARIABLE",
        source=SOURCE,
        notes="TOGO M1007 lists CO2 in the N2-CO2 gas mixture used for autoclaving.",
    ),
    _component(
        "Nitrogen gas",
        "variable",
        "VARIABLE",
        source=SOURCE,
        notes="TOGO M1007 lists N2 in the N2-CO2 gas mixture used for autoclaving.",
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _wolfe_solution(),
    {
        "preferred_term": "5% Na2CO3 solution",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": SOURCE,
        "notes": (
            f"{SOURCE} uses 5% Na2CO3 solution to adjust the cooled medium "
            "to pH 7.2-7.5."
        ),
        "composition": [
            _component(
                "Na2CO3",
                "50.0",
                "G_PER_L",
                source=SOURCE,
                notes="Solute of the 5% Na2CO3 pH-adjustment stock.",
            )
        ],
        "preparation_notes": "Autoclave and store under N2.",
    },
    _five_percent_solution(
        "5% Na2S x 9H2O solution",
        "Na2S x 9H2O",
        "6.0",
        notes=(
            f"{SOURCE} adds 6.0 ml/L 5% Na2S x 9H2O solution after "
            "autoclaving and pH adjustment."
        ),
    ),
    _five_percent_solution(
        "5% L-Cysteine HCl H2O solution",
        "L-Cysteine HCl H2O",
        "6.0",
        notes=(
            f"{SOURCE} adds 6.0 ml/L 5% L-Cysteine HCl H2O solution after "
            "autoclaving and pH adjustment."
        ),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix Sea Salts, Wolfe's mineral elixir, Trypticase peptone, "
            "yeast extract, glucose, resazurin, Na2CO3, and distilled water "
            "thoroughly."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the mixed base under an N2-CO2 gas mixture.",
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": (
            "After cooling, adjust to pH 7.2-7.5 with 5% Na2CO3 solution "
            "that has been autoclaved and stored under N2."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Add 6.0 ml/L each of 5% Na2S x 9H2O solution and 5% "
            "L-Cysteine HCl H2O solution, both autoclaved and stored under N2."
        ),
    },
)

NOTES = (
    "TOGO M1007 and JCM Medium 958 define Sea Salts TYG Medium as Sea Salts "
    "(Sigma), Wolfe's mineral elixir from M471/JCM 470, Trypticase peptone, "
    "yeast extract, glucose, resazurin, Na2CO3, and distilled water, "
    "autoclaved under an N2-CO2 gas mixture, adjusted to pH 7.2-7.5 with 5% "
    "Na2CO3 solution, and amended with 5% sodium sulfide nonahydrate and "
    "5% L-cysteine hydrochloride hydrate solutions."
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
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_range", {"min": 7.2, "max": 7.5}, "physical_state")
    repaired.pop("ph_value", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    _put_after(repaired, "sterilization", {"method": "AUTOCLAVE"}, "preparation_steps")
    _put_after(
        repaired,
        "incubation_atmosphere",
        "ANAEROBIC",
        "applications",
    )
    _put_after(
        repaired,
        "aeration",
        "N2-CO2 gas mixture during autoclaving; stock additions stored under N2",
        "incubation_atmosphere",
    )
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
