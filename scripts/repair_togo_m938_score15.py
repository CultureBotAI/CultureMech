#!/usr/bin/env python3
"""Repair TOGO M938 5% Salt Water Growth Medium and its MDS stock."""

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
M938_PATH = Path("bacterial/TOGO_M938_5_Salt_Water_Growth_Medium.yaml")
MDS_HELPER_PATH = Path("bacterial/mediadive_4404_MDS_salt_water.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m938_score15.py"
ACTION_M938 = "RESOLVED_TOGO_M938_MDS_SALT_WATER"
ACTION_MDS = "RESOLVED_MEDIADIVE_4404_MDS_SALT_WATER"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M938 = "https://togomedium.org/medium/M938"
TOGO_M578 = "https://togomedium.org/medium/M578"
JCM_897 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=897"
JCM_574 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=574"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

M938_IMPORTED_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "500", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.6", "G_PER_L"),
    ("Peptone (Oxoid)", "3", "G_PER_L"),
    ("Tris base", "variable", "VARIABLE"),
)
M938_INGREDIENTS: tuple[Component, ...] = (
    ("Distilled water", "500.0", "ML_PER_L"),
    ("Yeast extract (BD-Difco)", "0.6", "G_PER_L"),
    ("Peptone (Oxoid)", "3.0", "G_PER_L"),
)
M938_IMPORTED_SOLUTION: SolutionSignature = (
    "MDS salt water (see Medium [M578])",
    "100",
    "G_PER_L",
    (),
)
M938_FINAL_SOLUTION: SolutionSignature = (
    "MDS salt water",
    "100.0",
    "ML_PER_L",
    (
        ("NaCl", "240.0", "G_PER_L"),
        ("MgCl2 x 6H2O", "30.0", "G_PER_L"),
        ("MgSO4 x 7H2O", "35.0", "G_PER_L"),
        ("KCl", "7.0", "G_PER_L"),
        ("1 M CaCl2 solution", "5.0", "ML_PER_L"),
        ("Distilled water", "1.0", "L"),
    ),
)
MDS_IMPORTED_COMPOSITION: tuple[Component, ...] = (
    ("NaCl", "240", "G_PER_L"),
    ("MgCl2 x 6 H2O", "30", "G_PER_L"),
    ("MgSO4 x 7 H2O", "35", "G_PER_L"),
    ("KCl", "7", "G_PER_L"),
    ("CaCl2", "0.5549", "G_PER_L"),
)
PLACEHOLDER_INGREDIENTS: tuple[Component, ...] = (
    ("See source for composition", "variable", "VARIABLE"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "1 M CaCl2 solution": ("CHEBI:3312", "calcium dichloride"),
    "Distilled water": ("CHEBI:15377", "water"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "MgCl2 x 6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Peptone (Oxoid)": ("MICRO:0000178", "peptone"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "yeast extract"),
}


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
    term = GROUNDINGS[preferred_term]
    row["term"] = _term(*term)
    if term[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _medium_component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    label = "ml" if unit == "ML_PER_L" else "g"
    return _component(
        preferred_term,
        value,
        unit,
        source="TOGO M938 / JCM Medium 897",
        notes=f"JCM Medium 897 lists {value} {label} {preferred_term}.",
    )


def _mds_component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    label = {"G_PER_L": "g", "ML_PER_L": "ml", "L": "L"}[unit]
    return _component(
        preferred_term,
        value,
        unit,
        source="TOGO M578 / JCM Medium 574",
        notes=f"JCM Medium 574 lists {value} {label} {preferred_term} in MDS salt water.",
    )


def _mds_composition() -> list[dict[str, Any]]:
    return [
        _mds_component("NaCl", "240.0", "G_PER_L"),
        _mds_component("MgCl2 x 6H2O", "30.0", "G_PER_L"),
        _mds_component("MgSO4 x 7H2O", "35.0", "G_PER_L"),
        _mds_component("KCl", "7.0", "G_PER_L"),
        _component(
            "1 M CaCl2 solution",
            "5.0",
            "ML_PER_L",
            source="TOGO M578 / JCM Medium 574",
            notes="JCM Medium 574 adds 5 ml 1 M CaCl2 solution to MDS salt water.",
        ),
        _mds_component("Distilled water", "1.0", "L"),
    ]


def _mds_salt_water(value: str = "100.0") -> dict[str, Any]:
    return {
        "preferred_term": "MDS salt water",
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": "TOGO M938 / JCM Medium 897",
        "notes": "JCM Medium 897 adds 100.0 ml MDS salt water from TOGO M578/JCM 574.",
        "composition": _mds_composition(),
        "preparation_notes": (
            "JCM Medium 574 brings the MDS salt water stock to 1.0 L with "
            "distilled water and adjusts it to pH 7.5 with 1 M Tris base."
        ),
    }


def _preparation_steps() -> list[dict[str, Any]]:
    return [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Mix distilled water, Yeast extract (BD-Difco), Peptone (Oxoid), "
                "and MDS salt water."
            ),
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust to pH 7.5 with 1 M Tris base.",
        },
    ]


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
    signatures: list[SolutionSignature] = []
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation", "has_unmapped_ingredients"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], references: tuple[str, ...]) -> None:
    existing_references = doc.setdefault("references", [])
    if not isinstance(existing_references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in existing_references if isinstance(row, dict)}
    for url in references:
        if url not in existing:
            existing_references.append({"reference": url})


def _append_curation_event(
    doc: dict[str, Any],
    *,
    action: str,
    references: tuple[str, ...],
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(references),
        "notes": notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
        ):
            history[index] = event
            return
    history.append(event)


def _ensure_m938(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:010360":
        raise ValueError(f"{M938_PATH}: expected id CultureMech:010360, found {doc.get('id')!r}")
    if _source_term_id(doc) != "TOGO:M938":
        raise ValueError(f"{M938_PATH}: expected media term TOGO:M938")

    ingredient_signature = _signature(doc.get("ingredients"), "M938 ingredients")
    if ingredient_signature not in (M938_IMPORTED_INGREDIENTS, M938_INGREDIENTS):
        raise ValueError(f"{M938_PATH}: ingredient signature drifted")

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in ((M938_IMPORTED_SOLUTION,), (M938_FINAL_SOLUTION,)):
        raise ValueError(f"{M938_PATH}: MDS solution signature drifted")


def _ensure_mds_helper(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:013393":
        raise ValueError(
            f"{MDS_HELPER_PATH}: expected id CultureMech:013393, found {doc.get('id')!r}"
        )
    term = doc.get("term")
    if not isinstance(term, dict) or term.get("id") != "mediadive.solution:4404":
        raise ValueError(f"{MDS_HELPER_PATH}: expected mediadive solution 4404")

    composition_signature = _signature(doc.get("composition"), "MDS helper composition")
    if composition_signature not in (MDS_IMPORTED_COMPOSITION, M938_FINAL_SOLUTION[3]):
        raise ValueError(f"{MDS_HELPER_PATH}: MDS helper composition drifted")

    ingredient_signature = _signature(doc.get("ingredients"), "MDS helper ingredients")
    if ingredient_signature not in (PLACEHOLDER_INGREDIENTS, ()):
        raise ValueError(f"{MDS_HELPER_PATH}: MDS helper ingredients drifted")


def repair_m938(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_m938(doc)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "ph_value", 7.5, "physical_state")
    repaired["ingredients"] = [
        _medium_component("Distilled water", "500.0", "ML_PER_L"),
        _medium_component("Yeast extract (BD-Difco)", "0.6", "G_PER_L"),
        _medium_component("Peptone (Oxoid)", "3.0", "G_PER_L"),
    ]
    repaired["solutions"] = [_mds_salt_water()]
    _put_after(repaired, "preparation_steps", _preparation_steps(), "solutions")
    notes = (
        "TOGO M938 records JCM_M897 5% Salt Water Growth Medium with 500 ml "
        "distilled water, 0.6 g Yeast extract (BD-Difco), 3.0 g Peptone "
        "(Oxoid), 100.0 ml MDS salt water from TOGO M578/JCM Medium 574, and "
        "final adjustment to pH 7.5 with 1 M Tris base."
    )
    _put_after(repaired, "notes", notes, "media_term")
    _ensure_flags(repaired)
    references = (TOGO_M938, TOGO_M578, JCM_897, JCM_574)
    _ensure_references(repaired, references)
    _append_curation_event(
        repaired,
        action=ACTION_M938,
        references=references,
        notes=notes,
    )
    return repaired


def repair_mds_helper(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_mds_helper(doc)

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _mds_composition()
    repaired.pop("ingredients", None)
    repaired["preparation_notes"] = (
        "Add NaCl, MgCl2 x 6H2O, MgSO4 x 7H2O, KCl, and 5.0 ml/L 1 M CaCl2 "
        "solution to distilled water, bring to 1.0 L, and adjust to pH 7.5 "
        "with 1 M Tris base."
    )
    repaired["category"] = "bacterial"
    notes = (
        "MediaDive solution 4404 is the MDS salt-water stock from TOGO M578/JCM "
        "Medium 574, used by 5% Salt Water Growth Medium and other salt-water "
        "media."
    )
    repaired["notes"] = notes
    _ensure_flags(repaired)
    references = (TOGO_M578, JCM_574)
    _ensure_references(repaired, references)
    _append_curation_event(
        repaired,
        action=ACTION_MDS,
        references=references,
        notes=(
            "Replaced the placeholder top-level ingredient and flattened CaCl2 "
            "mass row with the JCM Medium 574 MDS stock formula."
        ),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / M938_PATH: repair_m938(_load(normalized / M938_PATH)),
        normalized / MDS_HELPER_PATH: repair_mds_helper(_load(normalized / MDS_HELPER_PATH)),
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
    print(f"\n{verb} {changed_count} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
