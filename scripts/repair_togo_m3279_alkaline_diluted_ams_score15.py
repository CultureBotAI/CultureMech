#!/usr/bin/env python3
"""Repair TOGO M3279 / JCM Medium 1428 Alkaline Diluted AMS Medium."""

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
TARGET = Path("bacterial/alkaline_diluted_ams_medium.yaml")
EXPECTED_ID = "CultureMech:009693"
EXPECTED_MEDIA_TERM = "TOGO:M3279"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m3279_alkaline_diluted_ams_score15.py"
ACTION = "RESOLVED_TOGO_M3279_ALKALINE_DILUTED_AMS"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M3279 = "https://togomedium.org/medium/M3279"
JCM_1428 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428"
JCM_815 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815"
REFERENCES = (TOGO_M3279, JCM_1428, JCM_815)

SOURCE = "JCM Medium 1428"
BASE_SOURCE = "JCM Medium 815"
TITLE = "Alkaline Diluted AMS Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("MgSO4·7H2O", "0.1", "G_PER_L"),
    ("CaCl2·2H2O", "0.02", "G_PER_L"),
    ("NH4Cl", "0.1", "G_PER_L"),
    ("Methane gas", "variable", "VARIABLE"),
    ("Air", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("NH4Cl", "0.1", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.02", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

TRACE_ELEMENT_SIGNATURE: tuple[Component, ...] = (
    ("ZnSO4 x 7 H2O", "0.4", "G_PER_L"),
    ("EDTA x 2Na", "0.25", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.02", "G_PER_L"),
    ("H3BO3", "0.015", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.04", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.01", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.2", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.05", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

IRON_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("EDTA x Fe(III)", "4.5", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

PHOSPHATE_BUFFER_SIGNATURE: tuple[Component, ...] = (
    ("KH2PO4", "37.425", "G_PER_L"),
    ("Na2HPO4 x 2 H2O", "48.950", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Trace element solution (see Medium [M850])", "0.1", "G_PER_L", ()),
    ("Iron stock solution (see Medium [M850])", "0.1", "G_PER_L", ()),
    ("Phosphate buffer stock solution (see Medium [M850])", "1", "G_PER_L", ()),
    ("1 N HCl solution", "variable", "VARIABLE", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Trace element solution", "0.1", "ML_PER_L", TRACE_ELEMENT_SIGNATURE),
    ("Iron stock solution", "0.1", "ML_PER_L", IRON_STOCK_SIGNATURE),
    (
        "Phosphate buffer stock solution",
        "1.0",
        "ML_PER_L",
        PHOSPHATE_BUFFER_SIGNATURE,
    ),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CoCl2 x 6 H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "EDTA x 2Na": ("CHEBI:64734", "EDTA disodium salt (anhydrous)"),
    "EDTA x Fe(III)": ("CHEBI:30729", "ethylenediaminetetraacetatoferrate(1-)"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Na2HPO4 x 2 H2O": ("CHEBI:91258", "disodium hydrogenphosphate dihydrate"),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "NiCl2 x 6 H2O": ("CHEBI:53542", "nickel chloride hexahydrate"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}

NUTRITIONAL_ROLES = {
    "NH4Cl": ("NITROGEN_SOURCE",),
}

PHYSICOCHEMICAL_ROLES = {
    "KH2PO4": ("BUFFER",),
    "Na2HPO4 x 2 H2O": ("BUFFER",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "ML_PER_L": "ml/L",
}

NOTES = (
    "TOGO M3279 records JCM Medium 1428, which uses JCM Medium 815 with the "
    "final pH adjusted to 8.0, the phosphate buffer stock reduced to 1.0 "
    "ml/L, and the gas phase replaced by methane-air (80:20, v/v). JCM "
    "Medium 815 supplies the basal NH4Cl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, "
    "Trace element solution, Iron stock solution, and Phosphate buffer stock "
    "solution formulas."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "DISSOLVE",
        "description": (
            "Dissolve NH4Cl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O in distilled "
            "water with 0.1 ml/L Trace element solution and 0.1 ml/L Iron "
            "stock solution."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the basal medium.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the Phosphate buffer stock solution separately.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "After cooling, add 1.0 ml/L sterile Phosphate buffer stock "
            "solution to the basal medium."
        ),
    },
    {
        "step_number": 5,
        "action": "ADJUST_PH",
        "description": "Adjust the medium to pH 8.0.",
    },
    {
        "step_number": 6,
        "action": "ALIQUOT",
        "description": (
            "Distribute 20 ml aliquots into sterile 120 ml serum bottles and "
            "seal with butyl rubber stoppers."
        ),
    },
    {
        "step_number": 7,
        "action": "FILTER_STERILIZE",
        "description": (
            "Replace the gas phase with filter-sterilized methane-air "
            "(80:20, v/v)."
        ),
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": (
        "Autoclave the basal medium and Phosphate buffer stock solution "
        "separately; filter-sterilize the methane-air gas phase."
    ),
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
) -> dict[str, Any]:
    grounding = GROUNDINGS[preferred_term]
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
        "term": _term(*grounding),
        "mediaingredientmech_chebi_term": _term(*grounding),
    }

    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _direct_ingredient(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    return _ingredient(
        preferred_term,
        value,
        unit,
        source=f"{BASE_SOURCE} / {SOURCE}",
        notes=(
            f"{SOURCE} uses the {BASE_SOURCE} basal component "
            f"{preferred_term} at {value} {UNIT_LABELS[unit]}."
        ),
    )


def _stock_component(
    preferred_term: str,
    value: str,
    unit: str,
) -> dict[str, Any]:
    return _ingredient(
        preferred_term,
        value,
        unit,
        source=BASE_SOURCE,
        notes=(
            f"{BASE_SOURCE} lists {value} {UNIT_LABELS[unit]} "
            f"{preferred_term} in this stock solution."
        ),
    )


def _trace_element_solution() -> dict[str, Any]:
    return {
        "preferred_term": "Trace element solution",
        "concentration": {"value": "0.1", "unit": "ML_PER_L"},
        "source": f"{BASE_SOURCE} / {SOURCE}",
        "notes": (
            f"{SOURCE} uses the {BASE_SOURCE} 0.1 ml/L Trace element "
            "solution without modifying its composition."
        ),
        "composition": [
            _stock_component(preferred_term, value, unit)
            for preferred_term, value, unit in TRACE_ELEMENT_SIGNATURE
        ],
    }


def _iron_stock_solution() -> dict[str, Any]:
    return {
        "preferred_term": "Iron stock solution",
        "concentration": {"value": "0.1", "unit": "ML_PER_L"},
        "source": f"{BASE_SOURCE} / {SOURCE}",
        "notes": (
            f"{SOURCE} uses the {BASE_SOURCE} 0.1 ml/L Iron stock solution "
            "without modifying its composition."
        ),
        "term": _term("mediadive.solution:4767", "Iron stock solution 4.5 g/L"),
        "composition": [
            _stock_component(preferred_term, value, unit)
            for preferred_term, value, unit in IRON_STOCK_SIGNATURE
        ],
    }


def _phosphate_buffer_stock_solution() -> dict[str, Any]:
    return {
        "preferred_term": "Phosphate buffer stock solution",
        "concentration": {"value": "1.0", "unit": "ML_PER_L"},
        "source": f"{BASE_SOURCE} / {SOURCE}",
        "notes": (
            f"{SOURCE} reduces the {BASE_SOURCE} Phosphate buffer stock "
            "solution addition to 1.0 ml/L."
        ),
        "composition": [
            _stock_component(preferred_term, value, unit)
            for preferred_term, value, unit in PHOSPHATE_BUFFER_SIGNATURE
        ],
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _direct_ingredient("NH4Cl", "0.1", "G_PER_L"),
    _direct_ingredient("MgSO4 x 7 H2O", "0.1", "G_PER_L"),
    _direct_ingredient("CaCl2 x 2 H2O", "0.02", "G_PER_L"),
    _direct_ingredient("Distilled water", "1000.0", "ML_PER_L"),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _trace_element_solution(),
    _iron_stock_solution(),
    _phosphate_buffer_stock_solution(),
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
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signature = _solution_signatures(doc)
    if solution_signature not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "has_unmapped_ingredients",
        "resolved_reference",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    if "references" not in doc:
        _put_after(doc, "references", [], "notes")

    references = doc["references"]
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Verified TOGO M3279 against JCM Medium 1428 and its JCM Medium "
            "815 parent, corrected water to 1000.0 ml/L, converted imported "
            "JCM 815 stock references to 0.1 ml/L Trace element solution, "
            "0.1 ml/L Iron stock solution, and 1.0 ml/L Phosphate buffer "
            "stock solution, moved the methane-air gas phase out of "
            "ingredients, and removed the JCM 815 pH 3.0 HCl adjustment."
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
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("aeration", None)
    repaired.pop("incubation_atmosphere", None)
    _put_after(repaired, "ph_value", 8.0, "physical_state")
    _put_after(repaired, "aeration", "methane-air (80:20, v/v)", "ph_value")
    _put_after(repaired, "incubation_atmosphere", "MICROAEROPHILIC", "aeration")
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "solutions",
    )
    _put_after(
        repaired,
        "sterilization",
        copy.deepcopy(STERILIZATION),
        "preparation_steps",
    )

    _ensure_references(repaired)
    _ensure_flags(repaired)
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
        changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        if args.apply and changed:
            write_record(path, doc)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
