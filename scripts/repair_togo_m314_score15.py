#!/usr/bin/env python3
"""Repair score-15 TOGO M314 using its M298 stock-solution references."""

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
TARGET = Path("bacterial/togo_medium_m314.yaml")
M298 = Path("bacterial/TOGO_M298_PE_Medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009614"
EXPECTED_MEDIA_TERM = "TOGO:M314"
EXPECTED_M298_ID = "CultureMech:009509"
EXPECTED_M298_MEDIA_TERM = "TOGO:M298"

CURATOR = "repair_togo_m314_score15.py"
ACTION = "RESOLVED_TOGO_M314_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M314_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M314"
TOGO_M298_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M298"
JCM_319 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=319"
SOURCE = "TOGO M314 / JCM Medium 319"
M298_SOURCE = "TOGO M298 / JCM Medium 303"

DISTILLED_WATER = "Distilled water"
AMMONIUM_SULFATE = "(NH4)2SO4"
SODIUM_SUCCINATE = "Sodium succinate"
YEAST_EXTRACT = "Yeast extract (BD-Difco)"
SODIUM_THIOSULFATE = "Na2S2O3\u30fb5H2O"
CASAMINO_ACIDS = "Casamino acids (BD-Difco)"

BASAL_SALTS = "Basal salts solution"
PHOSPHATE = "Phosphate solution"
VITAMIN = "Vitamin solution"
TRACE_ELEMENTS = "Trace elements solution"

Component = tuple[str, str, str]
SolutionSignature = tuple[
    str,
    str,
    str,
    tuple[Component, ...],
    tuple["SolutionSignature", ...],
]

LEGACY_INGREDIENTS: tuple[Component, ...] = (
    (DISTILLED_WATER, "1", "G_PER_L"),
    (AMMONIUM_SULFATE, "0.5", "G_PER_L"),
    (SODIUM_SUCCINATE, "2", "G_PER_L"),
    (YEAST_EXTRACT, "2", "G_PER_L"),
    (SODIUM_THIOSULFATE, "2.48", "G_PER_L"),
    (CASAMINO_ACIDS, "2", "G_PER_L"),
)

FINAL_INGREDIENTS: tuple[Component, ...] = (
    (DISTILLED_WATER, "1.0", "L"),
    (AMMONIUM_SULFATE, "0.5", "G_PER_L"),
    (SODIUM_SUCCINATE, "2", "G_PER_L"),
    (YEAST_EXTRACT, "2", "G_PER_L"),
    (SODIUM_THIOSULFATE, "2.48", "G_PER_L"),
    (CASAMINO_ACIDS, "2", "G_PER_L"),
)

LEGACY_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("Basal salts solution (see Medium [M298])", "5", "G_PER_L", (), ()),
    ("Phosphate solution (see Medium [M298])", "10", "G_PER_L", (), ()),
    ("Vitamin solution (see Medium [M298])", "1", "G_PER_L", (), ()),
)

M298_REQUIRED_SOLUTIONS = {
    BASAL_SALTS: "5",
    PHOSPHATE: "5",
    VITAMIN: "1",
    TRACE_ELEMENTS: "10",
}

M314_SOLUTION_ADDITIONS = {
    BASAL_SALTS: "5",
    PHOSPHATE: "10",
    VITAMIN: "1",
}

GROUNDINGS: dict[str, tuple[str, str]] = {
    AMMONIUM_SULFATE: ("CHEBI:62946", "ammonium sulfate"),
    DISTILLED_WATER: ("CHEBI:15377", "water"),
    SODIUM_SUCCINATE: ("CHEBI:63675", "sodium succinate (anhydrous)"),
    SODIUM_THIOSULFATE: ("CHEBI:32150", "sodium thiosulfate pentahydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
}

REFERENCES = (TOGO_M314_API, TOGO_M298_API, JCM_319)

RECIPE_NOTES = (
    "TOGO M314 preserves JCM Medium 319. It combines 5 mL Basal salts "
    "solution, 10 mL Phosphate solution, and 1 mL Vitamin solution from "
    "Medium M298 with ammonium sulfate, sodium succinate, BD-Difco yeast "
    "extract, sodium thiosulfate pentahydrate, BD-Difco Casamino acids, and "
    "distilled water to 1 L. TOGO reports pH 7.2; the current JCM Medium 319 "
    "URL no longer returns the legacy formulation."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare the Basal salts, Phosphate, Vitamin, and Trace elements stock "
            "solutions described by TOGO Medium M298."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Combine 5 mL Basal salts solution, 10 mL Phosphate solution, 1 mL "
            "Vitamin solution, the direct TOGO M314 ingredients, and distilled "
            "water; bring the final volume to 1 L."
        ),
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": "Adjust the complete medium to pH 7.2.",
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


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


def _component_signature(rows: Any, label: str) -> tuple[Component, ...]:
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


def _solution_signature(row: dict[str, Any]) -> SolutionSignature:
    concentration = row.get("concentration")
    if not isinstance(concentration, dict):
        raise ValueError(f"solutions row {row.get('preferred_term')!r} lacks concentration")
    child_solutions = row.get("solutions") or []
    if not isinstance(child_solutions, (list, tuple)):
        raise ValueError(f"solutions row {row.get('preferred_term')!r} has invalid child solutions")
    return (
        str(row.get("preferred_term") or ""),
        str(concentration.get("value") or ""),
        str(concentration.get("unit") or ""),
        _component_signature(row.get("composition"), "solutions composition"),
        tuple(_solution_signature(child) for child in child_solutions if isinstance(child, dict)),
    )


def _solution_signatures(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")
    if any(not isinstance(row, dict) for row in rows):
        raise ValueError(f"{label} contains a non-mapping row")
    return tuple(_solution_signature(row) for row in rows)


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if preferred_term == DISTILLED_WATER:
        row["notes"] = "TOGO M314 lists 1 L Distilled water for JCM Medium 319."

    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients() -> list[dict[str, Any]]:
    return [_component(name, value, unit) for name, value, unit in FINAL_INGREDIENTS]


def _by_name(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(row.get("preferred_term") or ""): row for row in rows}


def _ensure_m298(m298: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if m298.get("id") != EXPECTED_M298_ID:
        raise ValueError(f"{M298}: expected id {EXPECTED_M298_ID}, found {m298.get('id')!r}")
    if _source_term_id(m298) != EXPECTED_M298_MEDIA_TERM:
        raise ValueError(f"{M298}: expected media term {EXPECTED_M298_MEDIA_TERM}")

    solutions = m298.get("solutions")
    if not isinstance(solutions, list):
        raise ValueError(f"{M298}: expected solutions")
    by_name = _by_name([row for row in solutions if isinstance(row, dict)])

    for name, expected_value in M298_REQUIRED_SOLUTIONS.items():
        solution = by_name.get(name)
        if solution is None:
            raise ValueError(f"{M298}: expected solution {name!r}")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{M298}: solution {name!r} lacks concentration")
        actual = (str(concentration.get("value") or ""), str(concentration.get("unit") or ""))
        if actual != (expected_value, "ML_PER_L"):
            raise ValueError(f"{M298}: solution {name!r} drifted to {actual!r}")
        if not solution.get("composition"):
            raise ValueError(f"{M298}: solution {name!r} lacks composition")

    return by_name


def _retarget_component_notes(solution: dict[str, Any]) -> None:
    for component in solution.get("composition") or []:
        if not isinstance(component, dict):
            continue
        component["source"] = M298_SOURCE
        component["notes"] = (
            f"{SOURCE} references Medium M298 for {solution['preferred_term']}; "
            "concentration is normalized per liter of that stock."
        )


def _retarget_solution(solution: dict[str, Any], addition: str) -> dict[str, Any]:
    retargeted = copy.deepcopy(solution)
    name = str(retargeted["preferred_term"])
    retargeted["concentration"] = {"value": addition, "unit": "ML_PER_L"}
    retargeted["source"] = M298_SOURCE
    retargeted["notes"] = f"{SOURCE} adds {addition} mL {name} per final liter."
    retargeted["name"] = name
    _retarget_component_notes(retargeted)
    return retargeted


def _solutions(m298: dict[str, Any]) -> list[dict[str, Any]]:
    by_name = _ensure_m298(m298)

    basal = _retarget_solution(by_name[BASAL_SALTS], M314_SOLUTION_ADDITIONS[BASAL_SALTS])
    trace = _retarget_solution(by_name[TRACE_ELEMENTS], M298_REQUIRED_SOLUTIONS[TRACE_ELEMENTS])
    trace["notes"] = (
        f"{M298_SOURCE} adds 10 mL Trace elements solution per liter of Basal salts solution."
    )
    basal["solutions"] = [trace]
    basal["preparation_notes"] = (
        "Prepare Trace elements solution separately and add 10 mL to the 1 L Basal "
        "salts stock before adding 5 mL Basal salts solution per final liter of "
        "TOGO M314."
    )

    phosphate = _retarget_solution(by_name[PHOSPHATE], M314_SOLUTION_ADDITIONS[PHOSPHATE])
    vitamin = _retarget_solution(by_name[VITAMIN], M314_SOLUTION_ADDITIONS[VITAMIN])
    return [basal, phosphate, vitamin]


def _ensure_target(doc: dict[str, Any], m298: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _component_signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in {LEGACY_INGREDIENTS, FINAL_INGREDIENTS}:
        raise ValueError(f"{TARGET}: ingredient signature drifted to {ingredient_signature!r}")

    solution_signatures = _solution_signatures(doc.get("solutions"), "solutions")
    expected_final = _solution_signatures(_solutions(m298), "solutions")
    if solution_signatures not in {LEGACY_SOLUTIONS, expected_final}:
        raise ValueError(f"{TARGET}: solution signature drifted to {solution_signatures!r}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag for flag in flags if flag not in {"incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(
        (
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
            "legacy_source_url_unavailable",
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


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Curated TOGO:M314 from the preserved TOGO M314 formula and its Medium "
            "M298 stock-solution references; expanded Basal salts, Phosphate, "
            "Vitamin, and nested Trace elements stocks from M298; corrected water "
            "to a 1 L solvent row; set pH 7.2; and retained BD-Difco Yeast extract "
            "and Casamino acids as sourced opaque components."
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


def repair_target(doc: dict[str, Any], m298: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc, m298)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.2, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients()
    _put_after(repaired, "solutions", _solutions(m298), "ingredients")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "solutions")
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    m298 = _load(normalized / M298)
    return {target_path: repair_target(_load(target_path), m298)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
        changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        if args.apply and changed:
            write_record(path, doc)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
