#!/usr/bin/env python3
"""Repair TOGO M1099 VXG Gellan."""

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
TARGET = Path("bacterial/TOGO_M1099_VXG_Gellan.yaml")
EXPECTED_ID = "CultureMech:007616"
EXPECTED_MEDIA_TERM = "TOGO:M1099"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1099_score15.py"
ACTION = "RESOLVED_TOGO_M1099_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1099 = "https://togomedium.org/medium/M1099"
TOGO_M558 = "https://togomedium.org/medium/M558"
TOGO_M433 = "https://togomedium.org/medium/M433"
JCM_1035 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1035"
JCM_554 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=554"
JCM_433 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433"

SOURCE = "TOGO M1099 / JCM Medium 1035"
SELENITE_SOURCE = "TOGO M558 / JCM Medium 554"
TRACE_SOURCE = "TOGO M433 / JCM Medium 433"
TITLE = "VXG Gellan"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "960", "G_PER_L"),
    ("MES", "1.95", "G_PER_L"),
    ("Gellan gum", "8", "G_PER_L"),
    ("Xylan", "0.5", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "960.0", "ML_PER_L"),
    ("MES", "1.95", "G_PER_L"),
    ("Gellan gum", "8.0", "G_PER_L"),
    ("Xylan", "0.5", "G_PER_L"),
)

CACL2_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("CaCl2 x 2H2O", "30.0", "MILLIMOLAR"),
)
MGCL2_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("MgCl2 x 6H2O", "1.0", "MOLAR"),
)
MGSO4_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("MgSO4 x 7H2O", "20.0", "MILLIMOLAR"),
)
AMMONIUM_HPO4_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("(NH4)2HPO4", "20.0", "MILLIMOLAR"),
)

SELENITE_TUNGSTATE_SIGNATURE: tuple[Component, ...] = (
    ("NaOH", "0.5", "G_PER_L"),
    ("Na2SeO3 x 5H2O", "0.003", "G_PER_L"),
    ("Na2WO4 x 2H2O", "0.004", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

TRACE_ELEMENT_SIGNATURE: tuple[Component, ...] = (
    ("HCl (25%, 7.7 M)", "10.0", "ML_PER_L"),
    ("FeCl2 x 4H2O", "1.5", "G_PER_L"),
    ("ZnCl2", "70.0", "MG_PER_L"),
    ("MnCl2 x 4H2O", "100.0", "MG_PER_L"),
    ("H3BO3", "6.0", "MG_PER_L"),
    ("CoCl2 x 6H2O", "190.0", "MG_PER_L"),
    ("CuCl2 x 2H2O", "2.0", "MG_PER_L"),
    ("NiCl2 x 6H2O", "24.0", "MG_PER_L"),
    ("Na2MoO4 x 2H2O", "36.0", "MG_PER_L"),
    ("Distilled water", "990.0", "ML_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("30 mM CaCl2\u30fb2H2O solution", "10", "G_PER_L", ()),
    ("1 M MgCl2\u30fb6H2O solution", "10", "G_PER_L", ()),
    ("20 mM MgSO4\u30fb7H2O solution", "10", "G_PER_L", ()),
    ("20 mM (NH4)2HPO4 solution", "10", "G_PER_L", ()),
    ("Selenite--tungstate solution (see Medium [M558])", "1", "G_PER_L", ()),
    ("Trace element solution SL--10 (see Medium [M433])", "1", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("30 mM CaCl2 x 2H2O solution", "10.0", "ML_PER_L", CACL2_STOCK_SIGNATURE),
    ("1 M MgCl2 x 6H2O solution", "10.0", "ML_PER_L", MGCL2_STOCK_SIGNATURE),
    ("20 mM MgSO4 x 7H2O solution", "10.0", "ML_PER_L", MGSO4_STOCK_SIGNATURE),
    (
        "20 mM (NH4)2HPO4 solution",
        "10.0",
        "ML_PER_L",
        AMMONIUM_HPO4_STOCK_SIGNATURE,
    ),
    ("Selenite-tungstate solution", "1.0", "ML_PER_L", SELENITE_TUNGSTATE_SIGNATURE),
    ("Trace element solution SL-10", "1.0", "ML_PER_L", TRACE_ELEMENT_SIGNATURE),
)

REFERENCES = (TOGO_M1099, JCM_1035, TOGO_M558, JCM_554, TOGO_M433, JCM_433)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)2HPO4": ("CHEBI:63051", "diammonium hydrogen phosphate"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CoCl2 x 6H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl2 x 4H2O": ("CHEBI:86249", "iron dichloride tetrahydrate"),
    "Gellan gum": ("CHEBI:85248", "gellan gum"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "HCl (25%, 7.7 M)": ("CHEBI:17883", "hydrogen chloride"),
    "MES": ("CHEBI:39010", "MES"),
    "MgCl2 x 6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnCl2 x 4H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2SeO3 x 5H2O": ("CHEBI:131361", "disodium selenite pentahydrate"),
    "Na2WO4 x 2H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "NiCl2 x 6H2O": ("CHEBI:53542", "nickel chloride hexahydrate"),
    "Xylan": ("CHEBI:37166", "xylan"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "MILLIMOLAR": "mM",
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
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
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }

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
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    )


def _salt_stock(
    preferred_term: str,
    solute: str,
    stock_value: str,
    stock_unit: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds 10.0 ml/L {preferred_term}.",
        "composition": [
            _component(
                solute,
                stock_value,
                stock_unit,
                source=SOURCE,
                notes=(
                    f"{SOURCE} lists {preferred_term}; the {stock_value} "
                    f"{UNIT_LABELS[stock_unit]} stock concentration is recorded "
                    "on this solute."
                ),
            )
        ],
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _listed_component("Distilled water", "960.0", "ML_PER_L", source=SOURCE),
    _listed_component("MES", "1.95", "G_PER_L", source=SOURCE),
    _listed_component("Gellan gum", "8.0", "G_PER_L", source=SOURCE),
    _listed_component("Xylan", "0.5", "G_PER_L", source=SOURCE),
)


def _selenite_tungstate_solution() -> dict[str, Any]:
    return {
        "preferred_term": "Selenite-tungstate solution",
        "concentration": {"value": "1.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            f"{SOURCE} adds 1.0 ml/L Selenite-tungstate solution from "
            "M558/JCM 554."
        ),
        "composition": [
            _listed_component("NaOH", "0.5", "G_PER_L", source=SELENITE_SOURCE),
            _listed_component(
                "Na2SeO3 x 5H2O",
                "0.003",
                "G_PER_L",
                source=SELENITE_SOURCE,
            ),
            _listed_component(
                "Na2WO4 x 2H2O",
                "0.004",
                "G_PER_L",
                source=SELENITE_SOURCE,
            ),
            _listed_component("Distilled water", "1.0", "L", source=SELENITE_SOURCE),
        ],
    }


def _trace_element_solution() -> dict[str, Any]:
    return {
        "preferred_term": "Trace element solution SL-10",
        "concentration": {"value": "1.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            f"{SOURCE} adds 1.0 ml/L Trace element solution SL-10 from "
            "M433/JCM 433."
        ),
        "composition": [
            _listed_component("HCl (25%, 7.7 M)", "10.0", "ML_PER_L", source=TRACE_SOURCE),
            _listed_component("FeCl2 x 4H2O", "1.5", "G_PER_L", source=TRACE_SOURCE),
            _listed_component("ZnCl2", "70.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("MnCl2 x 4H2O", "100.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("H3BO3", "6.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("CoCl2 x 6H2O", "190.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("CuCl2 x 2H2O", "2.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("NiCl2 x 6H2O", "24.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("Na2MoO4 x 2H2O", "36.0", "MG_PER_L", source=TRACE_SOURCE),
            _listed_component("Distilled water", "990.0", "ML_PER_L", source=TRACE_SOURCE),
        ],
        "preparation_notes": (
            "Dissolve FeCl2 x 4H2O first in HCl, then dilute in distilled "
            "water and add the remaining salts."
        ),
    }


SOLUTIONS: tuple[dict[str, Any], ...] = (
    _salt_stock(
        "30 mM CaCl2 x 2H2O solution",
        solute="CaCl2 x 2H2O",
        stock_value="30.0",
        stock_unit="MILLIMOLAR",
    ),
    _salt_stock(
        "1 M MgCl2 x 6H2O solution",
        solute="MgCl2 x 6H2O",
        stock_value="1.0",
        stock_unit="MOLAR",
    ),
    _salt_stock(
        "20 mM MgSO4 x 7H2O solution",
        solute="MgSO4 x 7H2O",
        stock_value="20.0",
        stock_unit="MILLIMOLAR",
    ),
    _salt_stock(
        "20 mM (NH4)2HPO4 solution",
        solute="(NH4)2HPO4",
        stock_value="20.0",
        stock_unit="MILLIMOLAR",
    ),
    _selenite_tungstate_solution(),
    _trace_element_solution(),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare VXG Gellan with distilled water, MES, gellan gum, "
            "xylan, the four molar salt stocks, Selenite-tungstate solution, "
            "and Trace element solution SL-10."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the medium to pH 5.5.",
    },
)

NOTES = (
    "TOGO M1099 records JCM Medium 1035 with 960 ml distilled water, MES, "
    "gellan gum, xylan, four 10 ml/L molar salt stocks, 1 ml/L "
    "Selenite-tungstate solution from M558/JCM 554, and 1 ml/L Trace "
    "element solution SL-10 from M433/JCM 433. TOGO records the original "
    "source comment to adjust the medium to pH 5.5."
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
    for flag in ("has_ontology_mappings", "ingredients_curated"):
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
    _put_after(repaired, "ph_value", 5.5, "physical_state")
    repaired.pop("ph_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
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
