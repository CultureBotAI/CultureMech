#!/usr/bin/env python3
"""Repair TOGO M382 PYGV Agar and its JCM J387 duplicate."""

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
TARGET = Path("bacterial/TOGO_M382_PYGV_Agar.yaml")
PARENT = Path("bacterial/JCM_J387_PYGV_AGAR.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009763"
EXPECTED_PARENT_ID = "CultureMech:002744"
EXPECTED_MEDIA_TERM = "TOGO:M382"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:J387"

CURATOR = "repair_togo_m382_score15.py"
ACTION = "RESOLVED_TOGO_M382_SCORE15"
PARENT_ACTION = "RESOLVED_JCM_387_PYGV_AGAR"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M382 = "https://togomedium.org/medium/M382"
TOGO_M299 = "https://togomedium.org/medium/M299"
MEDIADIVE_J387 = "https://mediadive.dsmz.de/medium/J387"
JCM_387 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=387"
JCM_304 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=304"
JCM_149 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=149"

TOGO_SOURCE = "TOGO M382 / JCM Medium 387"
PARENT_SOURCE = "MediaDive J387 / JCM Medium 387"
TOGO_STOCK_SOURCE = "TOGO M299 / JCM Medium 304"
PARENT_STOCK_SOURCE = "MediaDive J387 / JCM Medium 304"
METALS_44_SOURCE = "JCM Medium 149"
TITLE = "PYGV Agar"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "960", "G_PER_L"),
    ("Yeast extract", "0.25", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Peptone", "0.25", "G_PER_L"),
    ("KOH", "variable", "VARIABLE"),
)

IMPORTED_PARENT_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "0.25", "G_PER_L"),
    ("Yeast extract", "0.25", "G_PER_L"),
    ("Glucose", "10", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("MgSO4 x 7 H2O", "29.7", "G_PER_L"),
    ("Nitrilotriacetic acid", "10", "G_PER_L"),
    ("CaCl2 x 2 H2O", "3.34", "G_PER_L"),
    ("FeSO4 x 7 H2O", "0.099", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.013", "G_PER_L"),
    ("Biotin", "0.002", "G_PER_L"),
    ("Folic acid", "0.002", "G_PER_L"),
    ("Pyridoxine hydrochloride", "0.01", "G_PER_L"),
    ("Riboflavin", "0.005", "G_PER_L"),
    ("Thiamine HCl", "0.005", "G_PER_L"),
    ("Nicotinamide", "0.005", "G_PER_L"),
    ("Calcium pantothenate", "0.005", "G_PER_L"),
    ("Vitamin B12", "0.0001", "G_PER_L"),
    ("p-Aminobenzoic acid", "0.005", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "0.25", "G_PER_L"),
    ("Yeast extract", "0.25", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Distilled water", "960.0", "ML_PER_L"),
    ("KOH", "variable", "VARIABLE"),
)

GLUCOSE_SIGNATURE: tuple[Component, ...] = (("Glucose", "2.5", "PERCENT_W_V"),)

MINERAL_SALT_SIGNATURE: tuple[Component, ...] = (
    ("MgSO4 x 7H2O", "29.7", "G_PER_L"),
    ("Nitrilotriacetic acid", "10.0", "G_PER_L"),
    ("CaCl2 x 2H2O", "3.34", "G_PER_L"),
    ("FeSO4 x 7H2O", "99.0", "MG_PER_L"),
    ("Na2MoO4 x 2H2O", "13.0", "MG_PER_L"),
    ("Metals 44", "50.0", "ML_PER_L"),
    ("Distilled water", "950.0", "ML_PER_L"),
)

VITAMIN_SIGNATURE: tuple[Component, ...] = (
    ("Biotin", "2.0", "MG_PER_L"),
    ("Folic acid", "2.0", "MG_PER_L"),
    ("Pyridoxine HCl", "10.0", "MG_PER_L"),
    ("Riboflavin", "5.0", "MG_PER_L"),
    ("Thiamine HCl", "5.0", "MG_PER_L"),
    ("Nicotinamide", "5.0", "MG_PER_L"),
    ("Calcium pantothenate", "5.0", "MG_PER_L"),
    ("Vitamin B12", "0.1", "MG_PER_L"),
    ("p-Aminobenzoic acid", "5.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("2.5% Glucose solution", "10", "G_PER_L", ()),
    ("Mineral salt solution (see Medium [M299])", "20", "G_PER_L", ()),
    ("Vitamin solution (see Medium [M299])", "10", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Mineral salt solution", "20.0", "ML_PER_L", MINERAL_SALT_SIGNATURE),
    ("2.5% Glucose solution", "10.0", "ML_PER_L", GLUCOSE_SIGNATURE),
    ("Vitamin solution", "10.0", "ML_PER_L", VITAMIN_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeSO4 x 7H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "KOH": ("CHEBI:32035", "potassium hydroxide"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Nicotinamide": ("CHEBI:17154", "nicotinamide"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
    "VARIABLE": "variable",
}

TARGET_REFERENCES = (TOGO_M382, JCM_387, MEDIADIVE_J387, TOGO_M299, JCM_304, JCM_149)
PARENT_REFERENCES = (MEDIADIVE_J387, JCM_387, JCM_304, JCM_149)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_PARENT_ID,
    "name": "pygv_agar",
    "notes": (
        "TOGO M382 imports the same JCM Medium 387 PYGV Agar formulation "
        "represented by MediaDive J387."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_ID,
    "name": "pygv_agar",
    "notes": (
        "TOGO M382 imports the same JCM Medium 387 PYGV Agar formulation "
        "represented by MediaDive J387."
    ),
}

VARIANT_MODIFICATIONS = (
    "Same JCM Medium 387 PYGV Agar formulation as the MediaDive J387 source record."
)

RECIPE_NOTES = (
    "JCM Medium 387 PYGV Agar lists, per liter, 0.25 g Peptone, 0.25 g "
    "Yeast extract, 20 ml Mineral salt solution from JCM Medium 304, 10 ml "
    "2.5% Glucose solution, 10 ml Vitamin solution from JCM Medium 304, "
    "15 g Agar, and 960 ml Distilled water. The final pH is 7.5. The base "
    "medium is mixed, gently heated to a boil, autoclaved, cooled to 45-50 "
    "degrees C, supplemented aseptically with filter-sterilized glucose and "
    "vitamin solutions, and adjusted to pH 7.5 with sterile KOH if necessary."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix peptone, yeast extract, mineral salt solution, agar, and "
            "distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "HEAT",
        "description": "Gently heat and bring to a boil.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 degrees C for 15 min.",
    },
    {
        "step_number": 4,
        "action": "COOL",
        "description": "Cool to 45-50 degrees C.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Aseptically add the filter-sterilized glucose solution and "
            "vitamin solution."
        ),
    },
    {
        "step_number": 6,
        "action": "ADJUST_PH",
        "description": "Adjust to pH 7.5 with sterile KOH, if necessary.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "Filter-sterilize glucose and vitamin solutions separately.",
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
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(source: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for preferred_term, value, unit in FINAL_INGREDIENT_SIGNATURE:
        rows.append(
            _component(
                preferred_term,
                value,
                unit,
                source=source,
                notes=(
                    "JCM Medium 387 adjusts the medium to pH 7.5 with sterile "
                    "KOH, if necessary."
                    if preferred_term == "KOH"
                    else None
                ),
                term=preferred_term not in {"Peptone", "Yeast extract"},
            )
        )
    return rows


def _solution(
    preferred_term: str,
    dose: str,
    composition: tuple[Component, ...],
    *,
    source: str,
    stock_source: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": dose, "unit": "ML_PER_L"},
        "source": source,
        "notes": f"{source} adds {dose} ml/L {preferred_term}.",
        "composition": [
            _component(
                name,
                value,
                unit,
                source=stock_source,
                notes=(
                    "JCM Medium 304 adds 50.0 ml/L Metals 44 from JCM Medium "
                    "149."
                    if name == "Metals 44"
                    else None
                ),
                term=name in GROUNDINGS,
            )
            for name, value, unit in composition
        ],
    }


def _solutions(source: str, stock_source: str) -> list[dict[str, Any]]:
    mineral = _solution(
        "Mineral salt solution",
        "20.0",
        MINERAL_SALT_SIGNATURE,
        source=source,
        stock_source=stock_source,
    )
    glucose = _solution(
        "2.5% Glucose solution",
        "10.0",
        GLUCOSE_SIGNATURE,
        source=source,
        stock_source=source,
    )
    glucose["preparation_notes"] = "Filter-sterilize before aseptic addition."
    vitamin = _solution(
        "Vitamin solution",
        "10.0",
        VITAMIN_SIGNATURE,
        source=source,
        stock_source=stock_source,
    )
    vitamin["preparation_notes"] = "Filter-sterilize before aseptic addition."

    return [mineral, glucose, vitamin]


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


def _solution_signatures(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signatures: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
        signatures.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), f"{label} composition"),
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
        raise ValueError(f"expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"expected media term {EXPECTED_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("target ingredient signature drifted")
    if _solution_signatures(doc.get("solutions"), "solutions") not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError("target solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"expected {EXPECTED_PARENT_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"expected media term {EXPECTED_PARENT_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_PARENT_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("parent ingredient signature drifted")
    if _solution_signatures(doc.get("solutions"), "solutions") not in (
        (),
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError("parent solution signature drifted")


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


def _ensure_references(doc: dict[str, Any], references_to_add: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in references_to_add:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(
    doc: dict[str, Any],
    *,
    action: str,
    references: tuple[str, ...],
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(references),
        "notes": RECIPE_NOTES,
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


def _ensure_child_link(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    filtered: list[Any] = []
    inserted = False
    for child in children:
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID or child.get("path") == TOGO_CHILD["path"]:
            if not inserted:
                filtered.append(copy.deepcopy(TOGO_CHILD))
                inserted = True
            continue
        filtered.append(child)

    if not inserted:
        filtered.append(copy.deepcopy(TOGO_CHILD))
    doc["variant_children"] = filtered


def _repair_common(
    doc: dict[str, Any],
    *,
    source: str,
    stock_source: str,
    references: tuple[str, ...],
    action: str,
) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.5, "physical_state")
    repaired.pop("ph_range", None)
    repaired["ingredients"] = _ingredients(source)
    repaired["solutions"] = _solutions(source, stock_source)
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, references)
    _append_curation_event(repaired, action=action, references=references)
    return repaired


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = _repair_common(
        doc,
        source=TOGO_SOURCE,
        stock_source=TOGO_STOCK_SOURCE,
        references=TARGET_REFERENCES,
        action=ACTION,
    )
    _put_after(repaired, "parent_media", copy.deepcopy(PARENT_MEDIA), "references")
    _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        [VARIANT_MODIFICATIONS],
        "variant_relationship",
    )
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = _repair_common(
        doc,
        source=PARENT_SOURCE,
        stock_source=PARENT_STOCK_SOURCE,
        references=PARENT_REFERENCES,
        action=PARENT_ACTION,
    )
    _ensure_child_link(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target = normalized / TARGET
    parent = normalized / PARENT
    return {
        target: repair_target(_load(target)),
        parent: repair_parent(_load(parent)),
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
