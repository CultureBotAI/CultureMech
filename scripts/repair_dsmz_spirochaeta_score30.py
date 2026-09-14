#!/usr/bin/env python3
"""Repair score-30 Spirochaeta records from legacy DSMZ PDFs."""

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

CURATOR = "repair_dsmz_spirochaeta_score30.py"
ACTION = "RESOLVED_DSMZ_LEGACY_SCORE30"
TIMESTAMP = "2026-09-08T00:00:00-07:00"

DSMZ_168_SPIROCHAETA_AURANTIA = "bacterial/spirochaeta_aurantia_medium.yaml"
DSMZ_273_SPIROCHAETA_ISOVALERICA = "bacterial/spirochaeta_isovalerica_medium.yaml"

EXPECTED_IDS = {
    DSMZ_168_SPIROCHAETA_AURANTIA: "CultureMech:004195",
    DSMZ_273_SPIROCHAETA_ISOVALERICA: "CultureMech:004701",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ_168_SPIROCHAETA_AURANTIA: "komodo.medium:168",
    DSMZ_273_SPIROCHAETA_ISOVALERICA: "komodo.medium:273",
}

DSMZ_168_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium168.pdf"
DSMZ_273_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium273.pdf"

SRC_168 = "DSMZ Medium 168 PDF"
SRC_273 = "DSMZ Medium 273 PDF"

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
    "incubation_atmosphere",
    "salinity",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
    "parent_media",
    "variant_relationship",
    "variant_modifications",
    "variant_children",
)


@dataclass(frozen=True)
class RecipeUpdate:
    path: str
    notes: str
    recipe: dict[str, Any]
    reference_urls: tuple[str, ...]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    identifier: str | None = None,
    label: str | None = None,
    notes: str | None = None,
) -> dict[str, Any]:
    component: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
    }
    if notes:
        component["notes"] = notes
    if identifier and label:
        component["term"] = _term(identifier, label)
        if identifier.startswith("CHEBI:"):
            component["mediaingredientmech_chebi_term"] = _term(identifier, label)
    return component


def _solution(
    preferred_term: str,
    value: str,
    *,
    composition: list[dict[str, Any]],
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "notes": notes,
        "composition": composition,
    }


UPDATES = (
    RecipeUpdate(
        path=DSMZ_168_SPIROCHAETA_AURANTIA,
        notes=(
            "DSMZ Medium 168 provides the Spirochaeta aurantia liquid recipe "
            "with Solution A, a 1 M K-phosphate buffer stock, final pH "
            "7.0-7.3, and anaerobic N2 handling. The PDF's optional 12 g/L "
            "agar addition for solid medium was not imported into this liquid "
            "base record."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_range": {"min": 7.0, "max": 7.3},
            "incubation_atmosphere": "ANAEROBIC",
            "ingredients": [
                _component("D-Glucose", "2", "G_PER_L", source=SRC_168, identifier="CHEBI:17634", label="D-glucose"),
                _component(
                    "Yeast extract",
                    "2",
                    "G_PER_L",
                    source=SRC_168,
                    identifier="FOODON:03315426",
                    label="yeast extract",
                ),
                _component("Trypticase peptone (BD BBL)", "5", "G_PER_L", source=SRC_168),
            ],
            "solutions": [
                _solution(
                    "1 M K-phosphate buffer, pH 7.0",
                    "10",
                    notes=(
                        "DSMZ 168 combines 6.15 ml 1 M K2HPO4 and 3.85 ml "
                        "1 M KH2PO4 stock to produce the pH 7.0 buffer, then "
                        "adds 10 ml of this Solution B to Solution A."
                    ),
                    composition=[
                        _component(
                            "K2HPO4",
                            "615",
                            "MILLIMOLAR",
                            source=SRC_168,
                            identifier="CHEBI:131527",
                            label="dipotassium hydrogen phosphate",
                        ),
                        _component(
                            "KH2PO4",
                            "385",
                            "MILLIMOLAR",
                            source=SRC_168,
                            identifier="CHEBI:63036",
                            label="potassium dihydrogen phosphate",
                        ),
                    ],
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Prepare Solution A and adjust its pH to 7.5 with KOH.",
                },
                {
                    "step_number": 2,
                    "action": "MIX",
                    "description": (
                        "Prepare the 1 M K-phosphate buffer at about pH 7.0 "
                        "from 1 M K2HPO4 and 1 M KH2PO4 stocks."
                    ),
                },
                {
                    "step_number": 3,
                    "action": "MIX",
                    "description": (
                        "For anaerobic cultivation, sparge Solutions A and B "
                        "for 30-45 min with 100% N2 gas and distribute "
                        "Solution A into anoxic Hungate-type tubes or serum "
                        "vials."
                    ),
                },
                {
                    "step_number": 4,
                    "action": "AUTOCLAVE",
                    "description": (
                        "Autoclave Solutions A and B separately at 121 C for "
                        "15 min and combine them after sterilization."
                    ),
                },
            ],
        },
        reference_urls=(DSMZ_168_PDF,),
    ),
    RecipeUpdate(
        path=DSMZ_273_SPIROCHAETA_ISOVALERICA,
        notes=(
            "DSMZ Medium 273 provides the Spirochaeta isovalerica liquid "
            "recipe with glucose, Trypticase, yeast extract, Tris-HCl buffer, "
            "seawater, cysteine-HCl, resazurin, pH 7.5, and anaerobic N2 "
            "preparation."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_value": 7.5,
            "incubation_atmosphere": "ANAEROBIC",
            "ingredients": [
                _component("Glucose", "2", "G_PER_L", source=SRC_273, identifier="CHEBI:17234", label="glucose"),
                _component("Trypticase (BBL)", "1", "G_PER_L", source=SRC_273),
                _component(
                    "Yeast extract",
                    "0.5",
                    "G_PER_L",
                    source=SRC_273,
                    identifier="FOODON:03315426",
                    label="yeast extract",
                ),
                _component(
                    "Tris-HCl-buffer (0.2 M; pH 7.5)",
                    "250",
                    "ML_PER_L",
                    source=SRC_273,
                    notes="DSMZ 273 lists 250 ml of Tris-HCl-buffer (0.2 M; pH 7.5).",
                ),
                _component("Sea water", "750", "ML_PER_L", source=SRC_273),
                _component(
                    "Cysteine-HCl x H2O",
                    "0.05",
                    "G_PER_L",
                    source=SRC_273,
                    identifier="CHEBI:91248",
                    label="L-cysteine hydrochloride hydrate",
                ),
                _component("Resazurin", "0.001", "G_PER_L", source=SRC_273, identifier="CHEBI:8806", label="Resazurin"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Mix the medium components and adjust pH to 7.5.",
                },
                {
                    "step_number": 2,
                    "action": "MIX",
                    "description": "Prepare the medium anaerobically under a 100% nitrogen atmosphere.",
                },
            ],
        },
        reference_urls=(DSMZ_273_PDF,),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term") or {}
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _require_target(doc: dict[str, Any], relative_path: str) -> None:
    expected_id = EXPECTED_IDS[relative_path]
    if doc.get("id") != expected_id:
        raise ValueError(
            f"{relative_path}: found id {doc.get('id')!r}, expected {expected_id!r}"
        )

    expected_source_term = EXPECTED_SOURCE_TERMS[relative_path]
    if _source_term_id(doc) != expected_source_term:
        raise ValueError(
            f"{relative_path}: found source term {_source_term_id(doc)!r}, "
            f"expected {expected_source_term!r}"
        )


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _composition_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    components = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        nested = solution.get("composition") or []
        nested_components = (
            [i for i in nested if isinstance(i, dict)]
            if isinstance(nested, list)
            else []
        )
        components.extend(nested_components or [solution])
    return components


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
        if obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    components = _composition_components(doc)
    if any(_grounded(component) for component in components):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")

    has_unmapped = any(not _grounded(component) for component in components)
    if has_unmapped:
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    if flags:
        doc["data_quality_flags"] = flags
    else:
        doc.pop("data_quality_flags", None)


def _ensure_references(doc: dict[str, Any], update: RecipeUpdate) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{update.path}: references is not a list")

    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in update.reference_urls:
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _append_curation_event(doc: dict[str, Any], update: RecipeUpdate) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved score-30 DSMZ legacy placeholder graph",
        "source": "; ".join(update.reference_urls),
        "notes": update.notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{update.path}: curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def _repair_with_recipe(doc: dict[str, Any], update: RecipeUpdate) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        if field in update.recipe:
            repaired[field] = copy.deepcopy(update.recipe[field])
        else:
            repaired.pop(field, None)
    repaired["notes"] = update.notes
    _ensure_flags(repaired)
    _ensure_references(repaired, update)
    _append_curation_event(repaired, update)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for update in UPDATES:
        path = normalized / update.path
        doc = _load(path)
        _require_target(doc, update.path)
        plans[path] = _repair_with_recipe(doc, update)
    return plans


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
        if args.apply:
            changed = write_record(path, doc)
        else:
            changed = dump_record(doc) != path.read_text(encoding="utf-8")
        if changed:
            changed_count += 1
            print(path.relative_to(args.normalized_dir))

    action = "Updated" if args.apply else "Would update"
    print(f"{action} {changed_count} DSMZ Spirochaeta score-30 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
