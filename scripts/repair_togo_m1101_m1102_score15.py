#!/usr/bin/env python3
"""Repair TOGO M1101/M1102 MPYCY media."""

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

CURATOR = "repair_togo_m1101_m1102_score15.py"
ACTION = "RESOLVED_TOGO_MPYCY_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1100 = "https://togomedium.org/medium/M1100"
TOGO_M1101 = "https://togomedium.org/medium/M1101"
TOGO_M1102 = "https://togomedium.org/medium/M1102"
TOGO_M290 = "https://togomedium.org/medium/M290"
JCM_1037 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1037"
JCM_1036 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1036"
JCM_296 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=296"

SOURCE = "JCM Medium 1037"
SOLUTION_SOURCE = "TOGO M1100 / JCM Medium 1036"
VITAMIN_SOURCE = "TOGO M290 / JCM Medium 296"
TITLE = "MPYCY Agar Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

AGAR_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Sodium pyruvate", "0.4", "G_PER_L"),
    ("Maltose monohydrate", "0.5", "G_PER_L"),
    ("Agar (if necessary)", "12", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.3", "G_PER_L"),
    ("Casamino acids (BD-Difco)", "0.3", "G_PER_L"),
)

LIQUID_IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Sodium pyruvate", "0.4", "G_PER_L"),
    ("Maltose monohydrate", "0.5", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.3", "G_PER_L"),
    ("Casamino acids (BD-Difco)", "0.3", "G_PER_L"),
)

AGAR_FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Maltose monohydrate", "0.5", "G_PER_L"),
    ("Sodium pyruvate", "0.4", "G_PER_L"),
    ("Casamino acids (BD-Difco)", "0.3", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.3", "G_PER_L"),
    ("Agar (if necessary)", "12.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

LIQUID_FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Maltose monohydrate", "0.5", "G_PER_L"),
    ("Sodium pyruvate", "0.4", "G_PER_L"),
    ("Casamino acids (BD-Difco)", "0.3", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.3", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

SOLUTION_A_SIGNATURE: tuple[Component, ...] = (
    ("(NH4)2SO4", "20.0", "G_PER_L"),
    ("MgSO4 x 7H2O", "10.0", "G_PER_L"),
    ("KCl", "10.0", "G_PER_L"),
    ("CaCl2 x 2H2O", "4.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

SOLUTION_B_SIGNATURE: tuple[Component, ...] = (
    ("0.5 M Na2HPO4-NaH2PO4 buffer (pH 7.3)", "2.0", "ML_PER_L"),
    ("Vitamins mix solution", "5.0", "ML_PER_L"),
    ("FeCl3 solution", "1.0", "ML_PER_L"),
)

VITAMINS_SIGNATURE: tuple[Component, ...] = (
    ("Riboflavin", "20.0", "MG_PER_L"),
    ("Thiamine HCl", "20.0", "MG_PER_L"),
    ("Nicotinic acid", "20.0", "MG_PER_L"),
    ("Calcium pantothenate", "20.0", "MG_PER_L"),
    ("Myo-inositol", "20.0", "MG_PER_L"),
    ("p-Aminobenzoic acid", "20.0", "MG_PER_L"),
    ("Pyridoxine HCl", "20.0", "MG_PER_L"),
    ("Folic acid", "1.0", "MG_PER_L"),
    ("Vitamin B12", "1.0", "MG_PER_L"),
    ("Biotin", "1.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)

FECL3_SIGNATURE: tuple[Component, ...] = (("FeCl3 x 6H2O", "0.5", "G_PER_L"),)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Solution A (see Medium [M1100])", "5", "G_PER_L", ()),
    ("Solution B (see Medium [M1100])", "8", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Solution A", "5.0", "ML_PER_L", SOLUTION_A_SIGNATURE),
    ("Solution B", "8.0", "ML_PER_L", SOLUTION_B_SIGNATURE),
    ("Vitamins mix solution", "5.0", "ML_PER_L", VITAMINS_SIGNATURE),
    ("FeCl3 solution", "1.0", "ML_PER_L", FECL3_SIGNATURE),
)

REFERENCES = (JCM_1037, TOGO_M1100, JCM_1036, TOGO_M290, JCM_296)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)2SO4": ("CHEBI:62946", "ammonium sulfate"),
    "Agar (if necessary)": ("CHEBI:2509", "agar"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl3 x 6H2O": ("CHEBI:86254", "iron trichloride hexahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "Maltose monohydrate": ("CHEBI:17306", "maltose"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "Myo-inositol": ("CHEBI:17268", "myo-inositol"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Sodium pyruvate": ("CHEBI:50144", "sodium pyruvate"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
}


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    media_term: str
    togo_url: str
    imported_ingredients: tuple[Component, ...]
    final_ingredients: tuple[Component, ...]
    physical_state: str
    ph_range: dict[str, float]
    ph_note: str


TARGETS: tuple[Target, ...] = (
    Target(
        path=Path("bacterial/TOGO_M1101_MPYCY_Agar_Medium.yaml"),
        expected_id="CultureMech:007620",
        media_term="TOGO:M1101",
        togo_url=TOGO_M1101,
        imported_ingredients=AGAR_IMPORTED_INGREDIENT_SIGNATURE,
        final_ingredients=AGAR_FINAL_INGREDIENT_SIGNATURE,
        physical_state="SOLID_AGAR",
        ph_range={"min": 7.6, "max": 7.8},
        ph_note="agar-plate",
    ),
    Target(
        path=Path("bacterial/TOGO_M1102_MPYCY_Agar_Medium.yaml"),
        expected_id="CultureMech:007621",
        media_term="TOGO:M1102",
        togo_url=TOGO_M1102,
        imported_ingredients=LIQUID_IMPORTED_INGREDIENT_SIGNATURE,
        final_ingredients=LIQUID_FINAL_INGREDIENT_SIGNATURE,
        physical_state="LIQUID",
        ph_range={"min": 7.4, "max": 7.6},
        ph_note="liquid medium",
    ),
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
    source: str,
    notes: str,
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _listed_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    term: bool = True,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        term=term,
    )


def _stock_reference(
    preferred_term: str,
    value: str,
    *,
    exact: str,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        "ML_PER_L",
        source=SOLUTION_SOURCE,
        notes=(f"{SOLUTION_SOURCE} lists {exact} {preferred_term} per 8.0 ml " "Solution B."),
        term=False,
    )


def _ingredients(include_agar: bool) -> tuple[dict[str, Any], ...]:
    rows = [
        _listed_component("Maltose monohydrate", "0.5", "G_PER_L", source=SOURCE),
        _listed_component("Sodium pyruvate", "0.4", "G_PER_L", source=SOURCE),
        _listed_component(
            "Casamino acids (BD-Difco)",
            "0.3",
            "G_PER_L",
            source=SOURCE,
            term=False,
        ),
        _listed_component(
            "Yeast extract (BD-Difco)",
            "0.3",
            "G_PER_L",
            source=SOURCE,
            term=False,
        ),
    ]
    if include_agar:
        rows.append(
            _listed_component(
                "Agar (if necessary)",
                "12.0",
                "G_PER_L",
                source=SOURCE,
            )
        )
    rows.append(_listed_component("Distilled water", "1.0", "L", source=SOURCE))
    return tuple(rows)


def _solution_a() -> dict[str, Any]:
    return {
        "preferred_term": "Solution A",
        "concentration": {"value": "5.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds 5.0 ml/L Solution A from M1100/JCM 1036.",
        "composition": [
            _listed_component("(NH4)2SO4", "20.0", "G_PER_L", source=SOLUTION_SOURCE),
            _listed_component("MgSO4 x 7H2O", "10.0", "G_PER_L", source=SOLUTION_SOURCE),
            _listed_component("KCl", "10.0", "G_PER_L", source=SOLUTION_SOURCE),
            _listed_component("CaCl2 x 2H2O", "4.0", "G_PER_L", source=SOLUTION_SOURCE),
            _listed_component("Distilled water", "1.0", "L", source=SOLUTION_SOURCE),
        ],
    }


def _solution_b() -> dict[str, Any]:
    return {
        "preferred_term": "Solution B",
        "concentration": {"value": "8.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            f"{SOURCE} adds 8.0 ml/L filter-sterilized Solution B from "
            "M1100/JCM 1036 after autoclaving."
        ),
        "composition": [
            _component(
                "0.5 M Na2HPO4-NaH2PO4 buffer (pH 7.3)",
                "2.0",
                "ML_PER_L",
                source=SOLUTION_SOURCE,
                notes=(
                    f"{SOLUTION_SOURCE} mixes 2.0 ml 0.5 M "
                    "Na2HPO4-NaH2PO4 buffer at pH 7.3 into Solution B."
                ),
                term=False,
            ),
            _stock_reference("Vitamins mix solution", "5.0", exact="5.0 ml"),
            _stock_reference("FeCl3 solution", "1.0", exact="1.0 ml"),
        ],
        "preparation_notes": "Mix and filter-sterilize just before addition.",
    }


def _vitamins_mix() -> dict[str, Any]:
    return {
        "preferred_term": "Vitamins mix solution",
        "concentration": {"value": "5.0", "unit": "ML_PER_L"},
        "source": SOLUTION_SOURCE,
        "notes": (
            f"{SOLUTION_SOURCE} adds 5.0 ml Vitamins mix solution from "
            "M290/JCM 296 per 8.0 ml Solution B."
        ),
        "composition": [
            _listed_component("Riboflavin", "20.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Thiamine HCl", "20.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Nicotinic acid", "20.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component(
                "Calcium pantothenate",
                "20.0",
                "MG_PER_L",
                source=VITAMIN_SOURCE,
            ),
            _listed_component("Myo-inositol", "20.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component(
                "p-Aminobenzoic acid",
                "20.0",
                "MG_PER_L",
                source=VITAMIN_SOURCE,
            ),
            _listed_component("Pyridoxine HCl", "20.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Folic acid", "1.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Vitamin B12", "1.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Biotin", "1.0", "MG_PER_L", source=VITAMIN_SOURCE),
            _listed_component("Distilled water", "1.0", "L", source=VITAMIN_SOURCE),
        ],
    }


def _fecl3_solution() -> dict[str, Any]:
    return {
        "preferred_term": "FeCl3 solution",
        "concentration": {"value": "1.0", "unit": "ML_PER_L"},
        "source": SOLUTION_SOURCE,
        "notes": f"{SOLUTION_SOURCE} adds 1.0 ml FeCl3 solution per 8.0 ml Solution B.",
        "composition": [
            _component(
                "FeCl3 x 6H2O",
                "0.5",
                "G_PER_L",
                source=SOLUTION_SOURCE,
                notes=(
                    f"{SOLUTION_SOURCE} lists 0.15 g FeCl3 x 6H2O in "
                    "300.0 ml water, equivalent to 0.5 g/L."
                ),
            )
        ],
        "preparation_notes": "Prepare just before use.",
    }


SOLUTIONS: tuple[dict[str, Any], ...] = (
    _solution_a(),
    _solution_b(),
    _vitamins_mix(),
    _fecl3_solution(),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix maltose monohydrate, sodium pyruvate, Casamino acids, "
            "yeast extract, Solution A, optional agar, and distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": (
            "Before autoclaving, adjust to pH 7.6-7.8 for agar plates or "
            "pH 7.4-7.6 for liquid medium."
        ),
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 115 degrees C for 20 min.",
    },
    {
        "step_number": 4,
        "action": "FILTER_STERILIZE",
        "description": "Mix Solution B and filter-sterilize it just before addition.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": "Add filter-sterilized Solution B aseptically after autoclaving.",
    },
)

NOTES = (
    "TOGO M1101/M1102 record JCM Medium 1037 with maltose monohydrate, "
    "sodium pyruvate, Casamino acids, yeast extract, Solution A from "
    "M1100/JCM 1036, Solution B from M1100/JCM 1036, and distilled water; "
    "the M1101 agar variant also lists 12 g/L agar if necessary. JCM 1037 "
    "adjusts pH to 7.6-7.8 for agar plates or to 7.4-7.6 for liquid medium, "
    "autoclaves at 115 degrees C for 20 min, and adds Solution B aseptically "
    "after separate filter sterilization."
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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.media_term:
        raise ValueError(f"{target.path}: expected media term {target.media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        target.imported_ingredients,
        target.final_ingredients,
    ):
        raise ValueError(
            f"{target.path}: ingredient signature drifted from "
            f"{target.imported_ingredients!r} to {ingredient_signature!r}"
        )

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(f"{target.path}: solution signature drifted")


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


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in (target.togo_url, *REFERENCES):
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join((target.togo_url, *REFERENCES)),
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
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = target.physical_state
    _put_after(repaired, "ph_range", target.ph_range, "physical_state")
    repaired.pop("ph_value", None)
    include_agar = target.physical_state == "SOLID_AGAR"
    repaired["ingredients"] = copy.deepcopy(list(_ingredients(include_agar)))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    _put_after(
        repaired,
        "sterilization",
        {
            "method": "AUTOCLAVE",
            "temperature": {"value": 115.0, "unit": "CELSIUS"},
            "duration": "20 min",
            "notes": "Separately filter-sterilize Solution B and add aseptically.",
        },
        "preparation_steps",
    )
    notes = f"{NOTES} This record uses the {target.ph_note} pH range."
    _put_after(repaired, "notes", notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path), target)
        for target in TARGETS
    }


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
