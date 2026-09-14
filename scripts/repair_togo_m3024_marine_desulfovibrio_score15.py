#!/usr/bin/env python3
"""Repair TOGO M3024 Marine Desulfovibrio Complex Medium."""

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
TARGET = Path("bacterial/marine_desulfovibrio_complex_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m3024_marine_desulfovibrio_score15.py"
ACTION = "RESOLVED_TOGO_M3024_MARINE_DESULFOVIBRIO_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:009535"
EXPECTED_MEDIA_TERM = "TOGO:M3024"

TOGO_M3024 = "https://togomedium.org/medium/M3024"
JCM_1367 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1367"
JCM_470 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=470"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"
REFERENCES = (TOGO_M3024, JCM_1367, JCM_470, JCM_197)
SOURCE = "TOGO M3024 / JCM Medium 1367"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "945", "G_PER_L"),
    ("Resazurin", "0.5", "G_PER_L"),
    ("Sea salts (Sigma)", "35", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "1", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    ("Wolfe's mineral elixir (see Medium [M471])", "1", "G_PER_L", ()),
    ("8% NaHCO3 solution*", "25", "G_PER_L", ()),
    ("1 M Sodium lactate solution", "20", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
    ("5% Na2S\u00b79H2O solution", "6", "G_PER_L", ()),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "945.0", "ML_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("Sea salts (Sigma)", "35.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "1.0", "G_PER_L"),
)

WOLFE_COMPOSITION: tuple[Component, ...] = (
    ("MgSO4 x 7 H2O", "30.0", "G_PER_L"),
    ("MnSO4 x n H2O", "5.0", "G_PER_L"),
    ("NaCl", "10.0", "G_PER_L"),
    ("FeSO4 x 7 H2O", "1.0", "G_PER_L"),
    ("CoCl2 x 6 H2O", "1.8", "G_PER_L"),
    ("CaCl2 x 2 H2O", "1.0", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "1.8", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.1", "G_PER_L"),
    ("AlK(SO4)2 x 12 H2O", "0.18", "G_PER_L"),
    ("H3BO3", "0.1", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.1", "G_PER_L"),
    ("(NH4)2Ni(SO4)2 x 6 H2O", "2.8", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.1", "G_PER_L"),
    ("Na2SeO4", "0.1", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

TRACE_VITAMIN_COMPOSITION: tuple[Component, ...] = (
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
    ("Distilled water", "1000.0", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    ("Wolfe's mineral elixir", "1.0", "ML_PER_L", WOLFE_COMPOSITION),
    ("8% NaHCO3 solution", "25.0", "ML_PER_L", (("NaHCO3", "80.0", "G_PER_L"),)),
    (
        "1 M Sodium lactate solution",
        "20.0",
        "ML_PER_L",
        (("Sodium lactate", "1.0", "MOLAR"),),
    ),
    ("Trace vitamins", "10.0", "ML_PER_L", TRACE_VITAMIN_COMPOSITION),
    (
        "5% Na2S x 9 H2O solution",
        "6.0",
        "ML_PER_L",
        (("Na2S x 9 H2O", "50.0", "G_PER_L"),),
    ),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "Yeast extract"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnSO4 x n H2O": ("CHEBI:86360", "manganese(II) sulfate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "AlK(SO4)2 x 12 H2O": (
        "CHEBI:86465",
        "potassium aluminium sulfate dodecahydrate",
    ),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "(NH4)2Ni(SO4)2 x 6 H2O": (
        "CHEBI:86149",
        "ammonium nickel sulfate hexahydrate",
    ),
    "Na2WO4 x 2 H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "Na2SeO4": ("CHEBI:77775", "sodium selenate"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "Sodium lactate": ("CHEBI:75228", "sodium lactate"),
    "Na2S x 9 H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "Pyridoxine hydrochloride": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Yeast extract (BD-Difco)": ("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
    "Sodium lactate": ("CARBON_SOURCE",),
    "Na2S x 9 H2O": ("SULFUR_SOURCE",),
    "FeSO4 x 7 H2O": ("IRON_SOURCE",),
    "MnSO4 x n H2O": ("TRACE_ELEMENT",),
    "CoCl2 x 6 H2O": ("TRACE_ELEMENT",),
    "ZnSO4 x 7 H2O": ("TRACE_ELEMENT",),
    "CuSO4 x 5 H2O": ("TRACE_ELEMENT",),
    "AlK(SO4)2 x 12 H2O": ("TRACE_ELEMENT",),
    "H3BO3": ("TRACE_ELEMENT",),
    "Na2MoO4 x 2 H2O": ("TRACE_ELEMENT",),
    "(NH4)2Ni(SO4)2 x 6 H2O": ("TRACE_ELEMENT",),
    "Na2WO4 x 2 H2O": ("TRACE_ELEMENT",),
    "Na2SeO4": ("TRACE_ELEMENT",),
    "Biotin": ("VITAMIN_SOURCE",),
    "Folic acid": ("VITAMIN_SOURCE",),
    "Pyridoxine hydrochloride": ("VITAMIN_SOURCE",),
    "Thiamine HCl": ("VITAMIN_SOURCE",),
    "Riboflavin": ("VITAMIN_SOURCE",),
    "Nicotinic acid": ("VITAMIN_SOURCE",),
    "Calcium pantothenate": ("VITAMIN_SOURCE",),
    "Vitamin B12": ("VITAMIN_SOURCE", "COFACTOR_PROVIDER"),
    "p-Aminobenzoic acid": ("VITAMIN_SOURCE",),
    "Lipoic acid": ("VITAMIN_SOURCE", "COFACTOR_PROVIDER"),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Resazurin": ("REDOX_INDICATOR",),
    "NaHCO3": ("BUFFER",),
    "Na2S x 9 H2O": ("REDUCING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
}

NOTES = (
    "TOGO M3024 imports JCM Medium 1367 as Marine Desulfovibrio Complex "
    "Medium. JCM 1367 lists 35.0 g Sea salts (Sigma), 1.0 ml Wolfe's "
    "mineral elixir from JCM Medium 470, 1.0 g Yeast extract (BD-Difco), "
    "0.5 mg Resazurin, and 945.0 ml distilled water in the N2-autoclaved "
    "base. Aseptically and anaerobically add 20.0 ml 1 M sodium lactate "
    "solution, 10.0 ml filter-sterilized Trace vitamins from JCM Medium 197, "
    "25.0 ml filter-sterilized 8% NaHCO3 solution, and 6.0 ml 5% Na2S x 9 "
    "H2O solution per liter."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix Sea salts (Sigma), Wolfe's mineral elixir, Yeast extract "
            "(BD-Difco), Resazurin, and 945 ml distilled water thoroughly."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the base medium under an N2 atmosphere.",
    },
    {
        "step_number": 3,
        "action": "FILTER_STERILIZE",
        "description": (
            "Filter-sterilize 8% NaHCO3 solution and Trace vitamins as sterile "
            "anaerobic stock solutions."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Aseptically and anaerobically add 20 ml 1 M sodium lactate "
            "solution, 10 ml Trace vitamins, and 25 ml 8% NaHCO3 solution "
            "per liter."
        ),
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Distribute under an N2-CO2 (4:1, v/v) gas stream, seal culture "
            "vessels with butyl rubber stoppers, and finally add 6 ml/L "
            "5% Na2S x 9 H2O solution autoclaved and stored under N2."
        ),
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": (
        "JCM Medium 1367 autoclaves the base under N2 and uses sterile "
        "anaerobic stock solutions; NaHCO3 and Trace vitamins are "
        "filter-sterilized."
    ),
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str, source: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }

    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)

    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _composition(source: str, rows: tuple[Component, ...]) -> list[dict[str, Any]]:
    return [_component(name, value, unit, source) for name, value, unit in rows]


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(_composition(SOURCE, FINAL_INGREDIENT_SIGNATURE))


def _stock_solution(
    preferred_term: str,
    value: str,
    source: str,
    composition: tuple[Component, ...],
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": _composition(source, composition),
    }


SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock_solution(
        "Wolfe's mineral elixir",
        "1.0",
        "JCM Medium 470",
        WOLFE_COMPOSITION,
        "JCM Medium 1367 adds 1.0 ml/L Wolfe's mineral elixir from JCM Medium 470.",
    ),
    _stock_solution(
        "8% NaHCO3 solution",
        "25.0",
        SOURCE,
        (("NaHCO3", "80.0", "G_PER_L"),),
        (
            "JCM Medium 1367 adds 25.0 ml/L sterile anaerobic "
            "filter-sterilized 8% NaHCO3 solution."
        ),
    ),
    _stock_solution(
        "1 M Sodium lactate solution",
        "20.0",
        SOURCE,
        (("Sodium lactate", "1.0", "MOLAR"),),
        "JCM Medium 1367 adds 20.0 ml/L 1 M sodium lactate solution.",
    ),
    _stock_solution(
        "Trace vitamins",
        "10.0",
        "JCM Medium 197",
        TRACE_VITAMIN_COMPOSITION,
        ("JCM Medium 1367 adds 10.0 ml/L filter-sterilized Trace " "vitamins from JCM Medium 197."),
    ),
    _stock_solution(
        "5% Na2S x 9 H2O solution",
        "6.0",
        SOURCE,
        (("Na2S x 9 H2O", "50.0", "G_PER_L"),),
        (
            "JCM Medium 1367 finally adds 6.0 ml/L 5% Na2S x 9 H2O "
            "solution autoclaved and stored under N2."
        ),
    ),
)


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


def _solution_signature(rows: Any) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError("solutions is not a list")

    signature: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"solution row {row.get('preferred_term')!r} lacks concentration")
        composition = row.get("composition") or []
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(composition, "solution composition"),
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
    if _solution_signature(doc.get("solutions")) not in (
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
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
    ):
        while obsolete in flags:
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
            f"{NOTES} Removed duplicated gas-atmosphere ingredient rows, "
            "corrected water and resazurin units, and converted empty stock "
            "solution placeholders from g/L to ml/L stock additions with "
            "inline compositions."
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
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "solutions", copy.deepcopy(list(SOLUTIONS)), "ingredients")
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "solutions",
    )
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_target(_load(path))}


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
