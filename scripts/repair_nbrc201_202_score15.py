#!/usr/bin/env python3
"""Repair score-15 NBRC Medium 201/202 records imported through TOGO."""

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
M201_PATH = Path("bacterial/togo_medium_m1441.yaml")
M202_PATH = Path("bacterial/togo_medium_m1442.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_M201_ID = "CultureMech:007981"
EXPECTED_M202_ID = "CultureMech:007982"
EXPECTED_M201_MEDIA_TERM = "TOGO:M1441"
EXPECTED_M202_MEDIA_TERM = "TOGO:M1442"
FALSE_KG_MATCH = "mediadive.medium:J505"

TOGO_M1441 = "https://togomedium.org/medium/M1441"
TOGO_M1442 = "https://togomedium.org/medium/M1442"
NBRC_201 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=201"
NBRC_202 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=202"

CURATOR = "repair_nbrc201_202_score15.py"
ACTION = "RESOLVED_NBRC201_202_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

DISTILLED_WATER_201 = "Distilled water make up to"
DISTILLED_WATER_202 = "Distilled water, make up to"
DISTILLED_WATER = "Distilled water"
POTATO = "Potato"
PRESS_YEAST = "Press yeast"
LIVER_INFUSION = "Liver infusion"
MEAT_EXTRACT = "Meat extract"
THIOGLYCOLATE = "Thioglycolate Medium Dehydrated"
GLUCOSE = "Glucose"
GLYCEROL = "Glycerol"
AGAR_IF_NEEDED = "Agar (if needed)"
CACO3 = "CaCO3"

Component = tuple[str, str, str]

M201_LEGACY_INGREDIENTS: tuple[Component, ...] = (
    (DISTILLED_WATER_201, "1", "G_PER_L"),
    (GLYCEROL, "15", "G_PER_L"),
    (PRESS_YEAST, "30", "G_PER_L"),
    (GLUCOSE, "5", "G_PER_L"),
    (AGAR_IF_NEEDED, "15", "G_PER_L"),
    (MEAT_EXTRACT, "5", "G_PER_L"),
)
M202_LEGACY_INGREDIENTS: tuple[Component, ...] = (
    (DISTILLED_WATER_202, "1", "G_PER_L"),
    (CACO3, "15", "G_PER_L"),
    (GLYCEROL, "15", "G_PER_L"),
    (PRESS_YEAST, "30", "G_PER_L"),
    (GLUCOSE, "5", "G_PER_L"),
    (AGAR_IF_NEEDED, "15", "G_PER_L"),
    (MEAT_EXTRACT, "5", "G_PER_L"),
)
LEGACY_SOLUTIONS: tuple[Component, ...] = (
    ("Potato*", "200", "G_PER_L"),
    ("Liver infusion from*", "25", "G_PER_L"),
    ("Thioglycolate Medium Dehydrated**", "10", "G_PER_L"),
)

M201_FINAL_INGREDIENTS: tuple[Component, ...] = (
    (POTATO, "200", "G_PER_L"),
    (PRESS_YEAST, "30", "G_PER_L"),
    (LIVER_INFUSION, "25", "G_PER_L"),
    (MEAT_EXTRACT, "5", "G_PER_L"),
    (THIOGLYCOLATE, "10", "G_PER_L"),
    (GLUCOSE, "5", "G_PER_L"),
    (GLYCEROL, "15", "G_PER_L"),
    (DISTILLED_WATER, "1000", "ML_PER_L"),
    (AGAR_IF_NEEDED, "15", "G_PER_L"),
)
M202_FINAL_INGREDIENTS: tuple[Component, ...] = (
    (POTATO, "200", "G_PER_L"),
    (PRESS_YEAST, "30", "G_PER_L"),
    (LIVER_INFUSION, "25", "G_PER_L"),
    (MEAT_EXTRACT, "5", "G_PER_L"),
    (THIOGLYCOLATE, "10", "G_PER_L"),
    (GLUCOSE, "5", "G_PER_L"),
    (GLYCEROL, "15", "G_PER_L"),
    (CACO3, "15", "G_PER_L"),
    (DISTILLED_WATER, "1000", "ML_PER_L"),
    (AGAR_IF_NEEDED, "15", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    AGAR_IF_NEEDED: ("CHEBI:2509", "agar"),
    CACO3: ("CHEBI:3311", "calcium carbonate"),
    DISTILLED_WATER: ("CHEBI:15377", "water"),
    GLUCOSE: ("CHEBI:17234", "glucose"),
    GLYCEROL: ("CHEBI:17754", "glycerol"),
}
NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    GLUCOSE: ("CARBON_SOURCE",),
    GLYCEROL: ("CARBON_SOURCE",),
}
PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    AGAR_IF_NEEDED: ("SOLIDIFYING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}


@dataclass(frozen=True)
class RecipeSpec:
    path: Path
    expected_id: str
    expected_media_term: str
    legacy_ingredients: tuple[Component, ...]
    final_ingredients: tuple[Component, ...]
    source_label: str
    togo_url: str
    nbrc_url: str
    notes: str
    has_child: bool = False
    parent_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()

    @property
    def references(self) -> tuple[str, str]:
        return (self.togo_url, self.nbrc_url)


M201_SPEC = RecipeSpec(
    path=M201_PATH,
    expected_id=EXPECTED_M201_ID,
    expected_media_term=EXPECTED_M201_MEDIA_TERM,
    legacy_ingredients=M201_LEGACY_INGREDIENTS,
    final_ingredients=M201_FINAL_INGREDIENTS,
    source_label="NBRC Medium 201",
    togo_url=TOGO_M1441,
    nbrc_url=NBRC_201,
    notes=(
        "TOGO M1441 imports NBRC Medium 201: 200 g/L potato, 30 g/L press "
        "yeast, liver infusion from 25 g/L liver, 5 g/L meat extract, 10 g/L "
        "Thioglycolate Medium Dehydrated from Wako Pure Chemical Industries, "
        "5 g/L glucose, 15 g/L glycerol, distilled water to 1 L, and 15 g/L "
        "agar if needed. Adjust pH to 7.0."
    ),
    has_child=True,
)

M202_SPEC = RecipeSpec(
    path=M202_PATH,
    expected_id=EXPECTED_M202_ID,
    expected_media_term=EXPECTED_M202_MEDIA_TERM,
    legacy_ingredients=M202_LEGACY_INGREDIENTS,
    final_ingredients=M202_FINAL_INGREDIENTS,
    source_label="NBRC Medium 202",
    togo_url=TOGO_M1442,
    nbrc_url=NBRC_202,
    notes=(
        "TOGO M1442 imports NBRC Medium 202: NBRC Medium 201 supplemented "
        "with 15 g/L CaCO3. The formula lists 200 g/L potato, 30 g/L press "
        "yeast, liver infusion from 25 g/L liver, 5 g/L meat extract, "
        "10 g/L Thioglycolate Medium Dehydrated from Wako Pure Chemical "
        "Industries, 5 g/L glucose, 15 g/L glycerol, distilled water to 1 L, "
        "15 g/L agar if needed, and pH 7.0."
    ),
    parent_relationship="SUPPLEMENTED_VARIANT",
    variant_modifications=("Adds 15 g/L CaCO3 to NBRC Medium 201.",),
)

SPECS: tuple[RecipeSpec, ...] = (M201_SPEC, M202_SPEC)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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


def _component(preferred_term: str, value: str, unit: str, source: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": _notes(preferred_term, value, unit, source),
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles is not None:
        row["nutritional_roles"] = list(nutritional_roles)
    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles is not None:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


def _notes(preferred_term: str, value: str, unit: str, source: str) -> str:
    if preferred_term == POTATO:
        return (
            f"{source} lists {value} {UNIT_LABELS[unit]} potato; the source "
            "footnote says to gently boil sliced potatoes in 500 ml water for "
            "30 min and remove solids by filtration through cloth."
        )
    if preferred_term == LIVER_INFUSION:
        return (
            f"{source} lists liver infusion from {value} {UNIT_LABELS[unit]} "
            "liver; the source footnote says to gently boil sliced liver in "
            "150 ml water for 30 min and remove solids by filtration through "
            "cloth."
        )
    if preferred_term == THIOGLYCOLATE:
        return (
            f"{source} lists {value} {UNIT_LABELS[unit]} Thioglycolate Medium "
            "Dehydrated from Wako Pure Chemical Industries."
        )
    if preferred_term == AGAR_IF_NEEDED:
        return f"{source} lists {value} {UNIT_LABELS[unit]} agar if needed."
    if preferred_term == DISTILLED_WATER:
        return f"{source} lists distilled water to 1 L."
    return f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}."


def _ingredients(spec: RecipeSpec) -> list[dict[str, Any]]:
    return [
        _component(name, value, unit, spec.source_label)
        for name, value, unit in spec.final_ingredients
    ]


def _preparation_steps() -> list[dict[str, Any]]:
    return [
        {
            "step_number": 1,
            "action": "FILTER",
            "description": (
                "Gently boil sliced potatoes in 500 ml water for 30 min, then "
                "remove solids by filtration through cloth."
            ),
        },
        {
            "step_number": 2,
            "action": "FILTER",
            "description": (
                "Gently boil sliced liver in 150 ml water for 30 min, then "
                "remove solids by filtration through cloth."
            ),
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": (
                "Mix the potato filtrate, liver infusion, remaining components, "
                "and distilled water."
            ),
        },
        {"step_number": 4, "action": "ADJUST_PH", "description": "Adjust pH to 7.0."},
    ]


def _child_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{M202_PATH}",
        "relationship": "SUPPLEMENTED_VARIANT",
        "id": EXPECTED_M202_ID,
        "name": M202_PATH.stem,
        "notes": "NBRC Medium 202 adds 15 g/L CaCO3 to NBRC Medium 201.",
    }


def _parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{M201_PATH}",
        "relationship": "SUPPLEMENTED_VARIANT",
        "id": EXPECTED_M201_ID,
        "name": M201_PATH.stem,
        "notes": "NBRC Medium 202 adds 15 g/L CaCO3 to NBRC Medium 201.",
    }


def _ensure_target(doc: dict[str, Any], spec: RecipeSpec) -> None:
    if doc.get("id") != spec.expected_id:
        raise ValueError(f"{spec.path}: expected id {spec.expected_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != spec.expected_media_term:
        raise ValueError(f"{spec.path}: expected media term {spec.expected_media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in {spec.legacy_ingredients, spec.final_ingredients}:
        raise ValueError(f"{spec.path}: ingredient signature drifted to {ingredient_signature!r}")

    solution_signature = _signature(doc.get("solutions"), "solutions")
    if solution_signature and solution_signature != LEGACY_SOLUTIONS:
        raise ValueError(f"{spec.path}: solution signature drifted to {solution_signature!r}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag for flag in flags if flag not in {"incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], spec: RecipeSpec) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in spec.references:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_event(doc: dict[str, Any], spec: RecipeSpec) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(spec.references),
        "notes": (
            f"Curated {spec.expected_media_term} from TOGO and {spec.source_label}; "
            "corrected the imported distilled-water unit, moved footnoted "
            "potato, liver, and thioglycolate rows out of empty solution "
            "wrappers, added pH 7.0, grounded disclosed simple components, "
            "and linked the NBRC 202 CaCO3 variant."
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


def repair_record(doc: dict[str, Any], spec: RecipeSpec) -> dict[str, Any]:
    _ensure_target(doc, spec)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(spec)
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", spec.notes, "media_term")
    repaired["preparation_steps"] = _preparation_steps()
    if spec.has_child:
        repaired["variant_children"] = [_child_ref()]
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
        repaired.pop("variant_modifications", None)
    else:
        _put_after(repaired, "parent_media", _parent_ref(), "curation_history")
        _put_after(
            repaired,
            "variant_relationship",
            spec.parent_relationship,
            "parent_media",
        )
        _put_after(
            repaired,
            "variant_modifications",
            list(spec.variant_modifications),
            "variant_relationship",
        )
    _ensure_flags(repaired)
    _ensure_references(repaired, spec)
    _ensure_event(repaired, spec)

    kg_match = repaired.get("kg_microbe_match")
    if kg_match not in (None, FALSE_KG_MATCH):
        raise ValueError(f"{spec.path}: unexpected kg_microbe_match {kg_match!r}")
    repaired.pop("kg_microbe_match", None)

    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / spec.path: repair_record(_load(normalized / spec.path), spec) for spec in SPECS
    }


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
