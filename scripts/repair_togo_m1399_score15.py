#!/usr/bin/env python3
"""Repair TOGO M1399 Sea Salts YTG Medium."""

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
TARGET = Path("bacterial/TOGO_M1399_Sea_Salts_YTG_Medium.yaml")
EXPECTED_ID = "CultureMech:007934"
EXPECTED_MEDIA_TERM = "TOGO:M1399"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1399_score15.py"
ACTION = "RESOLVED_TOGO_M1399_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1399 = "https://togomedium.org/medium/M1399"
JCM_1302 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1302"
JCM_151 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"
MEDIADIVE_J1302 = "https://mediadive.dsmz.de/rest/medium/J1302"

SOURCE = "TOGO M1399 / JCM Medium 1302"
TRACE_SOURCE = "JCM Medium 151"
VITAMIN_SOURCE = "JCM Medium 197"
TITLE = "Sea Salts YTG Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "0.5", "G_PER_L"),
    ("Resazurin", "0.5", "G_PER_L"),
    ("Sea salts (Sigma-Aldrich)", "30", "G_PER_L"),
    ("Glucose", "2.5", "G_PER_L"),
    ("L-Cysteine\u30fbHCl\u30fbH2O", "0.2", "G_PER_L"),
    ("Tryptone", "1", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Yeast extract", "0.5", "G_PER_L"),
    ("Tryptone", "1.0", "G_PER_L"),
    ("Glucose", "2.5", "G_PER_L"),
    ("Sea salts (Sigma-Aldrich)", "30.0", "G_PER_L"),
    ("L-Cysteine HCl H2O", "0.2", "G_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("N2", "variable", "VARIABLE"),
)

TRACE_MINERALS_SIGNATURE: tuple[Component, ...] = (
    ("Nitrilotriacetic acid", "1.5", "G_PER_L"),
    ("MgSO4 x 7 H2O", "3.0", "G_PER_L"),
    ("MnSO4 x n H2O", "0.5", "G_PER_L"),
    ("NaCl", "1.0", "G_PER_L"),
    ("FeSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("CoSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.1", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.01", "G_PER_L"),
    ("AlK(SO4)2", "0.01", "G_PER_L"),
    ("H3BO3", "0.01", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.01", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("KOH", "variable", "VARIABLE"),
)
SELENITE_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Na2SeO3", "0.1", "PERCENT_W_V"),
)
TRACE_VITAMIN_SIGNATURE: tuple[Component, ...] = (
    ("Biotin", "2.0", "MG_PER_L"),
    ("Folic acid", "2.0", "MG_PER_L"),
    ("Pyridoxine hydrochloride", "10.0", "MG_PER_L"),
    ("Thiamine HCl", "5.0", "MG_PER_L"),
    ("Riboflavin", "5.0", "MG_PER_L"),
    ("Nicotinic acid", "5.0", "MG_PER_L"),
    ("Calcium pantothenate", "5.0", "MG_PER_L"),
    ("Vitamin B12", "0.1", "MG_PER_L"),
    ("p-Aminobenzoic acid", "5.0", "MG_PER_L"),
    ("Lipoic acid", "5.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)
THIOSULFATE_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Sodium thiosulfate", "1.0", "MOLAR"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("0.1% Na2SeO3 solution", "1", "G_PER_L", ()),
    ("Trace minerals (see Medium [M142])", "1", "G_PER_L", ()),
    ("1M Sodium thiosulfate solution", "5", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Trace minerals", "1.0", "ML_PER_L", TRACE_MINERALS_SIGNATURE),
    ("0.1% Na2SeO3 solution", "1.0", "ML_PER_L", SELENITE_STOCK_SIGNATURE),
    ("Trace vitamins", "10.0", "ML_PER_L", TRACE_VITAMIN_SIGNATURE),
    (
        "1 M Sodium thiosulfate solution",
        "5.0",
        "ML_PER_L",
        THIOSULFATE_STOCK_SIGNATURE,
    ),
)

REFERENCES = (TOGO_M1399, JCM_1302, JCM_151, JCM_197, MEDIADIVE_J1302)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "AlK(SO4)2": ("CHEBI:86463", "potassium aluminium sulfate"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "CoSO4 x 7 H2O": ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "KOH": ("CHEBI:32035", "potassium hydroxide"),
    "L-Cysteine HCl H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnSO4 x n H2O": ("CHEBI:86360", "manganese(II) sulfate"),
    "N2": ("CHEBI:17997", "dinitrogen"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2SeO3": ("CHEBI:48843", "disodium selenite"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine hydrochloride": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Sodium thiosulfate": ("CHEBI:132112", "sodium thiosulfate"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Tryptone": ("MICRO:0000182", "tryptone"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
    "PERCENT_W_V": "% w/v",
    "VARIABLE": "variable",
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
    notes: str | None = None,
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _solution(
    preferred_term: str,
    value: str,
    signature: tuple[Component, ...],
    *,
    source: str,
    notes: str,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": [
            _component(
                component,
                amount,
                unit,
                source=source,
                notes=(
                    "JCM Medium 151 uses KOH solution to adjust the Trace minerals "
                    "stock to pH 6.5 before mineral addition and to final pH 7.0."
                    if component == "KOH"
                    else None
                ),
            )
            for component, amount, unit in signature
        ],
    }
    if preparation_notes:
        row["preparation_notes"] = preparation_notes
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component("Yeast extract", "0.5", "G_PER_L", source=SOURCE),
    _component("Tryptone", "1.0", "G_PER_L", source=SOURCE),
    _component("Glucose", "2.5", "G_PER_L", source=SOURCE),
    _component(
        "Sea salts (Sigma-Aldrich)",
        "30.0",
        "G_PER_L",
        source=SOURCE,
        notes=(
            "JCM Medium 1302 lists 30.0 g/L Sea salts (Sigma-Aldrich); this "
            "commercial mixture is source-disclosed but not reducible to one "
            "ChEBI molecule."
        ),
        term=False,
    ),
    _component("L-Cysteine HCl H2O", "0.2", "G_PER_L", source=SOURCE),
    _component("Resazurin", "0.5", "MG_PER_L", source=SOURCE),
    _component(
        "Distilled water",
        "1.0",
        "L",
        source=SOURCE,
        notes="JCM Medium 1302 brings the base medium to 1.0 L with distilled water.",
    ),
    _component(
        "N2",
        "variable",
        "VARIABLE",
        source=SOURCE,
        notes=(
            "JCM Medium 1302 dispenses the base into culture vessels under a "
            "N2 gas atmosphere and adds filter-sterilized stocks anaerobically "
            "after cooling."
        ),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _solution(
        "Trace minerals",
        "1.0",
        TRACE_MINERALS_SIGNATURE,
        source=TRACE_SOURCE,
        notes=(
            "JCM Medium 1302 adds 1.0 ml/L Trace minerals and links this stock "
            "to the Trace minerals recipe printed in JCM Medium 151."
        ),
        preparation_notes=(
            "Dissolve nitrilotriacetic acid and adjust to pH 6.5 with KOH "
            "solution; add minerals and adjust final pH to 7.0."
        ),
    ),
    _solution(
        "0.1% Na2SeO3 solution",
        "1.0",
        SELENITE_STOCK_SIGNATURE,
        source=SOURCE,
        notes="JCM Medium 1302 adds 1.0 ml/L 0.1% Na2SeO3 solution.",
    ),
    _solution(
        "Trace vitamins",
        "10.0",
        TRACE_VITAMIN_SIGNATURE,
        source=VITAMIN_SOURCE,
        notes=(
            "JCM Medium 1302 adds 10.0 ml/L filter-sterilized Trace vitamins "
            "from the stock recipe printed in JCM Medium 197 after autoclaving."
        ),
        preparation_notes="Filter-sterilize before aseptic and anaerobic addition.",
    ),
    _solution(
        "1 M Sodium thiosulfate solution",
        "5.0",
        THIOSULFATE_STOCK_SIGNATURE,
        source=SOURCE,
        notes=(
            "JCM Medium 1302 adds 5.0 ml/L filter-sterilized 1 M Sodium "
            "thiosulfate solution after autoclaving."
        ),
        preparation_notes="Filter-sterilize before aseptic and anaerobic addition.",
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix the base components with Trace minerals and 0.1% Na2SeO3 "
            "solution and bring the volume to 1.0 L."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the base medium to pH 7.0.",
    },
    {
        "step_number": 3,
        "action": "ALIQUOT",
        "description": (
            "Dispense the medium into culture vessels under N2 gas, for example "
            "10 ml medium in Hungate tubes, and seal with butyl rubber stoppers."
        ),
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 degrees C for 15 min.",
    },
    {
        "step_number": 5,
        "action": "COOL",
        "description": "Cool after autoclaving.",
    },
    {
        "step_number": 6,
        "action": "MIX",
        "description": (
            "Aseptically and anaerobically add filter-sterilized Trace vitamins "
            "and 1 M Sodium thiosulfate stocks per liter."
        ),
    },
)

NOTES = (
    "TOGO M1399 imports JCM Medium 1302. JCM 1302 records the pH 7.0 Sea "
    "Salts YTG base, 1.0 ml/L Trace minerals from JCM Medium 151, and "
    "filter-sterilized post-autoclave additions of 10.0 ml/L Trace vitamins "
    "from JCM Medium 197 and 5.0 ml/L 1 M Sodium thiosulfate."
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
        "notes": (
            f"{NOTES} MediaDive J1302 confirms the same post-autoclave 10.0 ml/L "
            "Trace vitamins and 5.0 ml/L Sodium thiosulfate additions; corrected "
            "the imported stock additions from g/L artifacts to ml/L volumes."
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
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    _put_after(
        repaired,
        "sterilization",
        {
            "method": "AUTOCLAVE",
            "temperature": {"value": 121.0, "unit": "CELSIUS"},
            "duration": "15 min",
            "notes": (
                "Autoclave the sealed base under N2. Add the filter-sterilized "
                "Trace vitamins and Sodium thiosulfate stocks aseptically and "
                "anaerobically after cooling."
            ),
        },
        "preparation_steps",
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
