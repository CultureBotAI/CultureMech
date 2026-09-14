#!/usr/bin/env python3
"""Repair the score-30 RS Medium NNM public MediaDive placeholder."""

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

CURATOR = "repair_mediadive_rs_nnm_score30.py"
ACTION = "RESOLVED_MEDIADIVE_RS_NNM_SCORE30"
TIMESTAMP = "2026-09-08T00:00:00-07:00"

P4_RS_NNM = "bacterial/rs_medium_non_nutrient_medium_nnm_component.yaml"
EXPECTED_ID = "CultureMech:010434"
EXPECTED_SOURCE_TERM = "mediadive.medium:P4"

P4_PUBLIC = "https://www.bacmedia.dsmz.de/medium/P4"
SRC_P4 = "MediaDive public Medium P4"

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
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
    source: str = SRC_P4,
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


INGREDIENTS = [
    _component("NaCl", "26.9", "G_PER_L", identifier="CHEBI:26710", label="sodium chloride"),
    _component("KCl", "0.6", "G_PER_L", identifier="CHEBI:32588", label="potassium chloride"),
    _component(
        "MgCl2 x 6 H2O",
        "3.0",
        "G_PER_L",
        identifier="CHEBI:86345",
        label="magnesium dichloride hexahydrate",
    ),
    _component(
        "MgSO4 x 7 H2O",
        "6.4",
        "G_PER_L",
        identifier="CHEBI:31795",
        label="magnesium sulfate heptahydrate",
    ),
    _component(
        "CaCl2 x 2 H2O",
        "1.2",
        "G_PER_L",
        identifier="CHEBI:86158",
        label="calcium chloride dihydrate",
    ),
    _component(
        "NaHCO3", "0.2", "G_PER_L", identifier="CHEBI:32139", label="sodium hydrogencarbonate"
    ),
    _component("NaBr", "1.05", "MG_PER_L", identifier="CHEBI:63004", label="NaBr"),
    _component("H3BO3", "0.01", "G_PER_L", identifier="CHEBI:33118", label="boric acid"),
    _component("SrCl2 x 6 H2O", "0.03", "G_PER_L", identifier="CHEBI:36383", label="SrCl2"),
    _component("NaF", "0.0004", "G_PER_L", identifier="CHEBI:28741", label="sodium fluoride"),
    _component("RbCl", "0.1", "MG_PER_L", identifier="CHEBI:78672", label="rubidium chloride"),
    _component("LiCl", "1.2", "MG_PER_L", identifier="CHEBI:48607", label="LiCl"),
    _component("ZnCl2", "5", "MG_PER_L", identifier="CHEBI:49976", label="zinc dichloride"),
    _component("KI", "30", "MG_PER_L", identifier="CHEBI:8346", label="KI"),
    _component(
        "AlCl3 x 6 H2O", "0.3", "MICROG_PER_L", identifier="CHEBI:30115", label="AlCl3 x 6 H2O"
    ),
    _component("Na2SiO3 x 5 H2O", "1.06", "MG_PER_L"),
    _component(
        "FeCl3 x 6 H2O", "0.02", "MICROG_PER_L", identifier="CHEBI:86254", label="FeCl3 x 6 H2O"
    ),
    _component("Na2EDTA x 2 H2O", "0.04", "MICROG_PER_L"),
    _component(
        "MnCl2 x 4 H2O", "0.2", "MICROG_PER_L", identifier="CHEBI:86368", label="MnCl2 x 4 H2O"
    ),
    _component("ZnSO4 x 7 H2O", "20", "MICROG_PER_L"),
    _component(
        "CoCl2 x 6 H2O",
        "0.01",
        "MICROG_PER_L",
        identifier="CHEBI:53503",
        label="Cobalt chloride hexahydrate",
    ),
    _component(
        "CuSO4 x 5 H2O",
        "2.6",
        "MICROG_PER_L",
        identifier="CHEBI:31440",
        label="copper(II) sulfate pentahydrate",
    ),
    _component(
        "NiSO4 x 6 H2O",
        "1",
        "MICROG_PER_L",
        identifier="CHEBI:53437",
        label="Nickel (II) sulfate hexahydrate",
    ),
    _component(
        "Na2MoO4 x 2 H2O",
        "20",
        "MICROG_PER_L",
        identifier="CHEBI:75213",
        label="sodium molybdate dihydrate",
    ),
    _component("H2SeO3", "1.4", "MICROG_PER_L", identifier="CHEBI:26642", label="H2SeO3"),
    _component("Na3VO4", "20", "MICROG_PER_L", identifier="CHEBI:35607", label="Na3VO4"),
    _component("K2CrO4", "1.2", "MICROG_PER_L", identifier="CHEBI:75249", label="K2CrO4"),
    _component(
        "BaCO3",
        "8",
        "MICROG_PER_L",
        notes="P4 adds 8 ul/L of a 1 mg/ml BaCO3 heavy-metal stock.",
    ),
    _component(
        "Cd(NO3)2 x 4 H2O",
        "0.1",
        "MICROG_PER_L",
        notes="P4 adds 0.1 ul/L of a 1 mg/ml Cd(NO3)2 x 4 H2O heavy-metal stock.",
    ),
    _component(
        "PbCl2",
        "0.02",
        "MICROG_PER_L",
        notes="P4 adds 0.02 ul/L of a 1 mg/ml PbCl2 heavy-metal stock.",
    ),
    _component(
        "AgNO3",
        "0.002",
        "MICROG_PER_L",
        notes="P4 adds 0.002 ul/L of a 1 mg/ml AgNO3 heavy-metal stock.",
    ),
    _component(
        "TiCl3",
        "0.0013",
        "ML_PER_L",
        notes=(
            "P4 adds 1.3 ul/L of TiCl3 stock prepared from Sigma-Aldrich "
            "14010 diluted 1:1000000; the commercial TiCl3 concentration "
            "basis is not a g/L stock."
        ),
    ),
]


UPDATE = RecipeUpdate(
    path=P4_RS_NNM,
    notes=(
        "MediaDive public Medium P4 provides the RS Medium Non-Nutrient "
        "Medium component as a 1 L defined marine recipe at pH 7 with 3.3% "
        "salinity. Microliter stock additions were converted to final "
        "mg/L or microg/L concentrations from the stock concentrations "
        "printed in the official recipe."
    ),
    recipe={
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.0,
        "salinity": "3.3%",
        "ingredients": INGREDIENTS,
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Prepare H2O stock solutions at the printed concentrations; "
                    "autoclave stocks except BaCO3, which is 0.22 um "
                    "filter-sterilized, and store heavy-metal stocks in the dark."
                ),
            },
            {
                "step_number": 2,
                "action": "MIX",
                "description": (
                    "In a 2 L bottle, combine each solid ingredient or liquid "
                    "stock and fill to 1 L with purified H2O."
                ),
            },
            {
                "step_number": 3,
                "action": "AUTOCLAVE",
                "description": (
                    "Assemble a sterile sparging apparatus on the 2 L bottle "
                    "and autoclave the 1 L medium with the apparatus attached."
                ),
            },
            {
                "step_number": 4,
                "action": "MIX",
                "description": "After cooling, sparge the medium with CO2 for 4 h.",
            },
            {
                "step_number": 5,
                "action": "MIX",
                "description": (
                    "Disconnect CO2, sparge with air for 12-24 h to remove "
                    "excess CO2, then replace the sparging apparatus with a "
                    "sterile non-vented cap and store at room temperature."
                ),
            },
        ],
    },
    reference_urls=(P4_PUBLIC,),
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


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{P4_RS_NNM}: found id {doc.get('id')!r}, expected {EXPECTED_ID!r}")
    if _source_term_id(doc) != EXPECTED_SOURCE_TERM:
        raise ValueError(
            f"{P4_RS_NNM}: found source term {_source_term_id(doc)!r}, "
            f"expected {EXPECTED_SOURCE_TERM!r}"
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
    if any(_grounded(component) for component in doc.get("ingredients") or []):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")
    if any(not _grounded(component) for component in doc.get("ingredients") or []):
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
        "changes": "Resolved score-30 RS NNM MediaDive placeholder graph",
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
    path = normalized / UPDATE.path
    doc = _load(path)
    _require_target(doc)
    return {path: _repair_with_recipe(doc, UPDATE)}


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
    print(f"{action} {changed_count} RS NNM public MediaDive score-30 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
