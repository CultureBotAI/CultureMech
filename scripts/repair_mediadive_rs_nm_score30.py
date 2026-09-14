#!/usr/bin/env python3
"""Repair the score-30 RS Medium NM public MediaDive placeholder."""

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

CURATOR = "repair_mediadive_rs_nm_score30.py"
ACTION = "RESOLVED_MEDIADIVE_RS_NM_SCORE30"
TIMESTAMP = "2026-09-08T00:00:00-07:00"

P5_RS_NM = "bacterial/rs_medium_nutrient_medium_nm_component.yaml"
EXPECTED_ID = "CultureMech:010435"
EXPECTED_SOURCE_TERM = "mediadive.medium:P5"

P5_PUBLIC = "https://www.bacmedia.dsmz.de/medium/P5"
SRC_P5 = "MediaDive public Medium P5"

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
    unit: str = "G_PER_L",
    *,
    source: str = SRC_P5,
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
    composition: list[dict[str, Any]],
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "notes": notes,
        "composition": composition,
    }


NNM_TERM = {
    "id": "CultureMech:010434",
    "label": "RS Medium - Non-Nutrient Medium (NNM) Component",
}


def _nnm_fill(value: str, notes: str) -> dict[str, Any]:
    component = _component(
        "RS Medium - Non-Nutrient Medium (NNM) Component",
        value,
        "ML_PER_L",
        notes=notes,
    )
    component["culturemech_term"] = dict(NNM_TERM)
    return component


NNM_COMPONENT = {
    "preferred_term": "RS Medium - Non-Nutrient Medium (NNM) Component",
    "concentration": {"value": "558", "unit": "ML_PER_L"},
    "notes": (
        "P5 fills the 150 ml final Nutrient Medium 1.0 component to volume "
        "with the RS Medium Non-Nutrient Medium component after adding the "
        "five mix solutions."
    ),
    "culturemech_term": NNM_TERM,
}

MIX_1 = _solution(
    "Mix solution 1 (Si and Fe+EDTA)",
    "26.667",
    [
        _component("Na2SiO3 x 5 H2O", "0.4086"),
        _component(
            "FeCl3 x 6 H2O",
            "0.05448",
            identifier="CHEBI:86254",
            label="FeCl3 x 6 H2O",
        ),
        _component("Na2EDTA x 2H2O", "0.08172"),
        _nnm_fill(
            "863.8",
            "P5 fills Mix solution 1 to 50 ml with NNM after adding 6.81 ml total single stocks.",
        ),
    ],
    (
        "P5 combines 2.27 ml each of the Na2SiO3 x 5 H2O, FeCl3 x 6 H2O, "
        "and Na2EDTA x 2H2O single stocks and fills to 50 ml with NNM."
    ),
)

MIX_2 = _solution(
    "Mix solution 2 (NO3-PO4)",
    "200",
    [
        _component("NaNO3", "1.362", identifier="CHEBI:63005", label="sodium nitrate"),
        _component("NaH2PO4 x H2O", "0.908"),
        _component(
            "K2HPO4",
            "1.816",
            identifier="CHEBI:131527",
            label="dipotassium hydrogen phosphate",
        ),
        _component("NH4Cl", "0.0454", identifier="CHEBI:31206", label="ammonium chloride"),
        _nnm_fill(
            "818.4",
            "P5 fills Mix solution 2 to 50 ml with NNM after adding 9.08 ml total single stocks.",
        ),
    ],
    (
        "P5 combines 2.27 ml each of the NaNO3, NaH2PO4 x H2O, K2HPO4, "
        "and NH4Cl single stocks and fills to 50 ml with NNM."
    ),
)

MIX_3 = _solution(
    "Mix solution 3 (Vitamins)",
    "71.333",
    [
        _component("Thiamine HCl (B1)", "0.0045"),
        _component("Biotin (B8)", "0.000009", identifier="CHEBI:15956", label="biotin"),
        _component("Cyanocobalamin (B12)", "0.00009", identifier="CHEBI:176843", label="vitamin B12"),
        _component("Folic acid (B9)", "0.00009"),
        _component("Pyridoxine (B6)", "0.00009"),
        _component("Riboflavin (B2)", "0.00009"),
        _component("Niacin (B3)", "0.00009"),
        _component("D-pantothenate acid hemicalcium salt (B5)", "0.00009"),
        _component("Myo-Inositol (B7)", "0.00009"),
        _component(
            "4-Aminobenzoic Acid",
            "0.00009",
            identifier="CHEBI:30753",
            label="4-aminobenzoic acid",
        ),
        _nnm_fill(
            "999.1",
            "P5 fills Mix solution 3 to 50 ml with NNM after adding 45 ul total vitamin stocks.",
        ),
    ],
    (
        "P5 adds 4.5 ul each from the listed vitamin single stocks and fills "
        "to 50 ml with NNM."
    ),
)

MIX_4 = _solution(
    "Mix solution 4 (Amino Acids)",
    "72.667",
    [
        _component("Arginine", "0.2844", identifier="CHEBI:29016", label="arginine"),
        _component(
            "Cysteine HCl",
            "0.0702",
            identifier="CHEBI:91247",
            label="L-cysteine hydrochloride",
        ),
        _component("Histidine", "0.0945", identifier="CHEBI:27570", label="histidine"),
        _component("L-Isoleucine", "0.11835", identifier="CHEBI:17191", label="L-isoleucine"),
        _component("L-Leucine", "0.1179", identifier="CHEBI:15603", label="L-leucine"),
        _component("Lysine HCl", "0.16335"),
        _component("L-Methionine", "0.0342", identifier="CHEBI:16643", label="L-methionine"),
        _component(
            "L-Phenylalanine",
            "0.07425",
            identifier="CHEBI:17295",
            label="L-phenylalanine",
        ),
        _component("L-Threonine", "0.1071", identifier="CHEBI:16857", label="L-threonine"),
        _component("L-Tryptophan", "0.02295", identifier="CHEBI:16828", label="L-tryptophan"),
        _component("L-Tyrosine", "0.081", identifier="CHEBI:17895", label="L-tyrosine"),
        _component("L-Valine", "0.1053", identifier="CHEBI:16414", label="L-valine"),
        _component("L-Alanine", "0.040406", identifier="CHEBI:16977", label="L-alanine"),
        _component("Glycine", "0.03405", identifier="CHEBI:15428", label="glycine"),
        _component("L-Proline", "0.05221", identifier="CHEBI:17203", label="L-proline"),
        _component("L-Asparagine*H2O", "0.0681"),
        _component("Aspartate", "0.060382", identifier="CHEBI:29995", label="aspartate(2-)"),
        _component("Glutamate", "0.066738"),
        _component("Serine", "0.04767", identifier="CHEBI:17822", label="serine"),
        _component("L-Glutamine", "0.5448", identifier="CHEBI:18050", label="L-glutamine"),
        _nnm_fill(
            "864.2",
            "P5 fills Mix solution 4 to 50 ml with NNM after adding MEM and glutamine stocks.",
        ),
    ],
    (
        "P5 adds 2.25 ml Sigma MEM 50X Amino Acids solution, 2.27 ml "
        "Sigma MEM 100X Amino Acids solution, and 2.27 ml L-Glutamine "
        "single stock, then fills to 50 ml with NNM; MEM amino-acid "
        "contents were flattened from the official P5 notes."
    ),
)

MIX_5 = _solution(
    "Mix solution 5 (Carbon Sources)",
    "71.333",
    [
        _component(
            "Glycerol",
            "1.134",
            identifier="CHEBI:17754",
            label="glycerol",
            notes="P5 adds 45 ul glycerol from Sigma at 1.26 g/ml to 50 ml Mix solution 5.",
        ),
        _component("Sodium pyruvate", "1.79784", identifier="CHEBI:50144", label="sodium pyruvate"),
        _component("D-Glucose", "1.79784", identifier="CHEBI:17634", label="D-glucose"),
        _component("N-acetyl-D-glucosamine", "1.44372"),
        _component("D-Ribose", "1.816", identifier="CHEBI:16988", label="D-ribose"),
        _component(
            "Sodium succinate",
            "2.46976",
            identifier="CHEBI:63675",
            label="sodium succinate (anhydrous)",
        ),
        _component("y-aminobutyric acid", "1.4074"),
        _component("Sodium acetate", "1.11684", identifier="CHEBI:32954", label="sodium acetate"),
        _component("Decanoic acid", "0.006356"),
        _component("L-Arabinose", "1.19856", identifier="CHEBI:30849", label="L-arabinose"),
        _component("L-Rhamnose", "1.64348", identifier="CHEBI:62345", label="L-rhamnose"),
        _component("Fucose", "3.27788", identifier="CHEBI:33984", label="fucose"),
        _component("D-Mannose", "3.59568", identifier="CHEBI:16024", label="D-mannose"),
        _component("Galactose", "1.79784", identifier="CHEBI:28260", label="galactose"),
        _component(
            "D-Xylose",
            "7.264",
            identifier="CHEBI:65327",
            label="D-xylose",
            notes="The official ingredient table names D-Xylose; a later P5 instruction says Xylan.",
        ),
        _component("Sodium alginate", "0.08172", identifier="CHEBI:53311", label="sodium alginate"),
        _component("Methyl-cellulose", "0.92616"),
        _component("Pectin", "1.816", identifier="CHEBI:17309", label="pectin"),
        _component("Guanosine", "0.02724", identifier="CHEBI:16750", label="guanosine"),
        _component("Uracil", "0.14528", identifier="CHEBI:17568", label="uracil"),
        _nnm_fill(
            "136.5",
            "P5 fills Mix solution 5 to 50 ml with NNM after adding glycerol and carbon-source stocks.",
        ),
    ],
    (
        "P5 adds glycerol directly plus 2.27 ml of each listed carbon-source "
        "single stock and fills to 50 ml with NNM; the viscous solution is "
        "vacuum-filtered through a 0.22 um filter."
    ),
)

UPDATE = RecipeUpdate(
    path=P5_RS_NM,
    notes=(
        "MediaDive public Medium P5 provides the RS Medium Nutrient Medium "
        "1.0 component as a 150 ml defined recipe at pH 7 with 3.3% salinity. "
        "The five 50 ml mix solutions and the final 150 ml assembly were "
        "curated separately so the printed single-stock concentrations are "
        "not mistaken for final medium concentrations."
    ),
    recipe={
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.0,
        "salinity": "3.3%",
        "ingredients": [],
        "solutions": [MIX_1, MIX_2, MIX_3, MIX_4, MIX_5, NNM_COMPONENT],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Prepare the printed single stocks in purified H2O or NNM "
                    "and sterilize each stock by autoclaving or 0.22 um "
                    "filtration as specified."
                ),
            },
            {
                "step_number": 2,
                "action": "MIX",
                "description": (
                    "Prepare the methyl-cellulose stock in cold H2O overnight "
                    "before autoclaving; prepare the pectin stock in H2O with "
                    "hot-plate stirring for 20 min before autoclaving."
                ),
            },
            {
                "step_number": 3,
                "action": "MIX",
                "description": (
                    "Prepare 50 ml Mix solution 1 from the Si and Fe/EDTA "
                    "stocks, fill with NNM, syringe-filter through 0.22 um, "
                    "and store at 4 C."
                ),
            },
            {
                "step_number": 4,
                "action": "MIX",
                "description": (
                    "Prepare 50 ml Mix solution 2 from the nitrate-phosphate "
                    "stocks, fill with NNM, syringe-filter through 0.22 um, "
                    "and prepare fresh each time."
                ),
            },
            {
                "step_number": 5,
                "action": "MIX",
                "description": (
                    "Prepare 50 ml Mix solution 3 from the vitamin stocks, "
                    "fill with NNM, syringe-filter through 0.22 um, and store "
                    "at 4 C."
                ),
            },
            {
                "step_number": 6,
                "action": "MIX",
                "description": (
                    "Prepare 50 ml Mix solution 4 from MEM 50X amino acids, "
                    "MEM 100X amino acids, and the glutamine stock; fill with "
                    "NNM, syringe-filter through 0.22 um, and store at 4 C."
                ),
            },
            {
                "step_number": 7,
                "action": "MIX",
                "description": (
                    "Prepare 50 ml Mix solution 5 from glycerol and the "
                    "carbon-source stocks, fill with NNM, vacuum-filter "
                    "through 0.22 um, and store at 4 C."
                ),
            },
            {
                "step_number": 8,
                "action": "FILTER",
                "description": (
                    "Combine 4 ml Mix solution 1, 30 ml Mix solution 2, "
                    "10.7 ml Mix solution 3, 10.9 ml Mix solution 4, and "
                    "10.7 ml Mix solution 5; fill to 150 ml with NNM, "
                    "vacuum-filter through 0.22 um, and store Nutrient Medium "
                    "1.0 at 4 C."
                ),
            },
        ],
    },
    reference_urls=(P5_PUBLIC,),
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
        raise ValueError(f"{P5_RS_NM}: found id {doc.get('id')!r}, expected {EXPECTED_ID!r}")
    if _source_term_id(doc) != EXPECTED_SOURCE_TERM:
        raise ValueError(
            f"{P5_RS_NM}: found source term {_source_term_id(doc)!r}, "
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


def _iter_graph_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    components: list[dict[str, Any]] = []
    ingredients = doc.get("ingredients") or []
    if isinstance(ingredients, list):
        components.extend(item for item in ingredients if isinstance(item, dict))

    solutions = doc.get("solutions") or []
    if isinstance(solutions, list):
        for solution in solutions:
            if not isinstance(solution, dict):
                continue
            components.append(solution)
            composition = solution.get("composition") or []
            if isinstance(composition, list):
                components.extend(item for item in composition if isinstance(item, dict))
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

    graph_components = _iter_graph_components(doc)
    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")
    if any(_grounded(component) for component in graph_components):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")
    if any(not _grounded(component) for component in graph_components):
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
        "changes": "Resolved score-30 RS NM MediaDive placeholder graph",
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
    print(f"{action} {changed_count} RS NM public MediaDive score-30 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
