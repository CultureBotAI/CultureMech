#!/usr/bin/env python3
"""Source-correct ten pairs of duplicate CCAP records.

Each pair consists of an empty collection-import record and a composed MediaDive
record with the same CCAP PDF URL. Direct copying is unsafe: the composed CH,
MErds, and SES records flatten stock formulations, and several process media use
grams per litre for per-vessel or geometric quantities. This migration rebuilds
both records in every pair from the authoritative CCAP document.

Apply mode requires the ten reviewed PDFs and validates their SHA-256 hashes
before checking every target and writing any YAML. Dry-run is the default.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import write_record  # noqa: E402
from repair_ccap_missing_compositions import (  # noqa: E402
    descriptor_projection,
    ingredient_signature,
    mapped_ingredient,
    step,
)

NORMALIZED = REPO / "data" / "normalized_yaml"
ACTION = "SOURCE_CORRECTED_CCAP_DUPLICATE_RECIPE"
TIMESTAMP = "2026-08-25T00:00:00-07:00"

SOURCE_FILES = {
    "MR_CH.pdf": "44b2cf7784d6842d2c6b1c8e182a3406f64ccc18069ddf60283ce236f7dff8e0",
    "MR_MErds.pdf": "1c83aea4b6acdfefe472fcf6788e859e3f5365680f0931b3c7e85dc8d340cb26",
    "MR_MW.pdf": "736e22d1edb03b3db7c89abed298a58275bd1b60923d1b56c2824787f6371db3",
    "MR_SW.pdf": "b0cb6a3a1d847bf76d493abfa45c7f3bde173b0e21b06649ac0033c7f79b182d",
    "MR_SW_AMP.pdf": "24401db0ea427c9eae87de96a7227718766d8c268101304d6e2ad94ccf0a9117",
    "MR_SW_Ca.pdf": "ed53074bcec95c3aff5ba2ebdcf0202d65c1fe66aeee43771d7634d6c3f2f73c",
    "MR_SE1_Marine.pdf": "a1aa6a7de8c76d20ee216b828beddae6f94bd94b7e154ef657f7863f562a8934",
    "MR_SE2_Freshwater.pdf": "63b8f356f55aae82c10f2400f5698b224518dac2a81914d46a10162979275572",
    "MR_SES.pdf": "e85f5343863684cd26e4f17c4c35b57a69c7e895af5f8d4b2f4280a7ef493fbd",
    "MR_YEL.pdf": "92b1c322a4efa498c230db7a8d7f95b73c4926f9cba7855d4f2f6d076cef1603",
}

SOURCE_URLS = {
    "ch": "https://www.ccap.ac.uk/wp-content/uploads/MR_CH.pdf",
    "merds": "https://www.ccap.ac.uk/wp-content/uploads/MR_MErds.pdf",
    "mw": "https://www.ccap.ac.uk/wp-content/uploads/MR_MW.pdf",
    "sw": "https://www.ccap.ac.uk/wp-content/uploads/MR_SW.pdf",
    "sw_amp": "https://www.ccap.ac.uk/wp-content/uploads/MR_SW_AMP.pdf",
    "sw_ca": "https://www.ccap.ac.uk/wp-content/uploads/MR_SW_Ca.pdf",
    "se1": "https://www.ccap.ac.uk/wp-content/uploads/MR_SE1_Marine.pdf",
    "se2": "https://www.ccap.ac.uk/wp-content/uploads/MR_SE2_Freshwater.pdf",
    "ses": "https://www.ccap.ac.uk/wp-content/uploads/MR_SES.pdf",
    "yel": "https://www.ccap.ac.uk/wp-content/uploads/MR_YEL.pdf",
}


@dataclass(frozen=True)
class Target:
    relative_path: str
    record_id: str
    recipe_key: str
    precondition: str


TARGETS = (
    Target("algae/ch.yaml", "CultureMech:000059", "ch", "empty"),
    Target("bacterial/ch.yaml", "CultureMech:000330", "ch", "existing"),
    Target("algae/merds.yaml", "CultureMech:000089", "merds", "empty"),
    Target("bacterial/merds.yaml", "CultureMech:000364", "merds", "existing"),
    Target("algae/mw.yaml", "CultureMech:000093", "mw", "empty"),
    Target("bacterial/mw.yaml", "CultureMech:000369", "mw", "existing"),
    Target("algae/s_w.yaml", "CultureMech:000138", "sw", "empty"),
    Target("bacterial/s_w.yaml", "CultureMech:000414", "sw", "existing"),
    Target("algae/s_w_amp.yaml", "CultureMech:000136", "sw_amp", "empty"),
    Target("bacterial/s_w_amp.yaml", "CultureMech:000307", "sw_amp", "existing"),
    Target("algae/s_w_ca.yaml", "CultureMech:000137", "sw_ca", "empty"),
    Target("bacterial/s_w_ca.yaml", "CultureMech:000308", "sw_ca", "existing"),
    Target("algae/se1.yaml", "CultureMech:000128", "se1", "empty"),
    Target("bacterial/se1.yaml", "CultureMech:000405", "se1", "existing"),
    Target("algae/se2.yaml", "CultureMech:000129", "se2", "empty"),
    Target("bacterial/se2.yaml", "CultureMech:000406", "se2", "existing"),
    Target("algae/ses.yaml", "CultureMech:000130", "ses", "empty"),
    Target("bacterial/ses.yaml", "CultureMech:000407", "ses", "existing"),
    Target("algae/yel.yaml", "CultureMech:000144", "yel", "empty"),
    Target("bacterial/yel.yaml", "CultureMech:000314", "yel", "existing"),
)

EXISTING_SIGNATURES = {
    "bacterial/ch.yaml": (
        ("NaCl", "5", "G_PER_L"),
        ("KCl", "5", "G_PER_L"),
        ("CaCl2", "5", "G_PER_L"),
    ),
    "bacterial/merds.yaml": (
        ("NaNO3", "1", "G_PER_L"),
        ("Na2HPO4", "1", "G_PER_L"),
        ("Natural sea water", "1000", "G_PER_L"),
        ("K2HPO4", "20", "G_PER_L"),
        ("MgSO4 x 7 H2O", "20", "G_PER_L"),
        ("KNO3", "20", "G_PER_L"),
        ("Soil", "variable", "VARIABLE"),
    ),
    "bacterial/mw.yaml": (("Mineral water", "1000", "G_PER_L"),),
    "bacterial/s_w.yaml": (("Soil", "variable", "VARIABLE"),),
    "bacterial/s_w_amp.yaml": (
        ("Soil", "variable", "VARIABLE"),
        ("(NH4)MgPO4", "0.01", "G_PER_L"),
    ),
    "bacterial/s_w_ca.yaml": (
        ("Soil", "variable", "VARIABLE"),
        ("CaCO3", "0.01", "G_PER_L"),
    ),
    "bacterial/se1.yaml": (("Soil", "variable", "VARIABLE"),),
    "bacterial/se2.yaml": (("Soil", "159.091", "G_PER_L"),),
    "bacterial/ses.yaml": (
        ("K2HPO4", "20", "G_PER_L"),
        ("MgSO4 x 7 H2O", "20", "G_PER_L"),
        ("KNO3", "20", "G_PER_L"),
        ("Soil", "variable", "VARIABLE"),
    ),
    "bacterial/yel.yaml": (
        ("Yeast extract", "4", "G_PER_L"),
        ("Liver digest", "4", "G_PER_L"),
    ),
}


def stock(
    name: str,
    addition_ml: str,
    composition: list[dict[str, Any]],
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": name,
        "composition": composition,
        "concentration": {"value": addition_ml, "unit": "ML_PER_L"},
        "notes": notes,
    }


def water(value: str = "1", unit: str = "L") -> dict[str, Any]:
    return mapped_ingredient("Deionized water", value, unit, "CHEBI:15377", "water")


def variable_material(name: str, notes: str) -> dict[str, Any]:
    return mapped_ingredient(name, "variable", "VARIABLE", notes=notes)


def ch_recipe() -> dict[str, Any]:
    return {
        "ingredients": [water()],
        "solutions": [
            stock(
                "NaCl stock solution",
                "5.0",
                [mapped_ingredient("NaCl", "20", "G_PER_L", "CHEBI:26710", "sodium chloride")],
                "Prepare with 2.0 g NaCl per 100 ml; add 5 ml/L.",
            ),
            stock(
                "KCl stock solution",
                "5.0",
                [mapped_ingredient("KCl", "0.8", "G_PER_L", "CHEBI:32588", "potassium chloride")],
                "Prepare with 0.08 g KCl per 100 ml; add 5 ml/L.",
            ),
            stock(
                "CaCl2 stock solution",
                "5.0",
                [
                    mapped_ingredient(
                        "CaCl2",
                        "1.2",
                        "G_PER_L",
                        "CHEBI:3312",
                        "calcium dichloride",
                    )
                ],
                "Prepare with 0.12 g CaCl2 per 100 ml; add 5 ml/L.",
            ),
        ],
        "preparation_steps": [
            step(
                1, "MIX", "Add 5 ml of each stock solution and make up to 1 L with deionized water."
            ),
            step(2, "AUTOCLAVE", "Autoclave at 15 psi for 15 minutes."),
        ],
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "sterilization": {"method": "AUTOCLAVE"},
    }


def merds_recipe() -> dict[str, Any]:
    return {
        "ingredients": [
            mapped_ingredient(
                "Filtered natural seawater",
                "1",
                "L",
                notes="Make the final medium up to 1 L after adding the stocks.",
            )
        ],
        "solutions": [
            stock(
                "SES medium",
                "100.00",
                [],
                "Use the separately defined CCAP SES recipe.",
            ),
            stock(
                "NaNO3 stock solution",
                "2.65",
                [mapped_ingredient("NaNO3", "75", "G_PER_L", "CHEBI:63005", "sodium nitrate")],
                "Prepare with 7.5 g NaNO3 per 100 ml; add 2.65 ml/L.",
            ),
            stock(
                "Na2HPO4.2H2O stock solution",
                "0.62",
                [
                    mapped_ingredient(
                        "Na2HPO4.2H2O",
                        "20",
                        "G_PER_L",
                        "CHEBI:91258",
                        "disodium hydrogenphosphate dihydrate",
                    )
                ],
                "Prepare with 2.0 g Na2HPO4.2H2O per 100 ml; add 0.62 ml/L.",
            ),
        ],
        "preparation_steps": [
            step(
                1,
                "MIX",
                "Add SES medium and both salt stocks, then make up to 1 L with filtered natural seawater.",
            ),
            step(2, "AUTOCLAVE", "Autoclave at 15 psi for 15 minutes."),
            step(3, "FILTER_STERILIZE", "Filter the final medium if precipitation is problematic."),
        ],
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "sterilization": {"method": "AUTOCLAVE"},
    }


def mw_recipe() -> dict[str, Any]:
    return {
        "ingredients": [
            mapped_ingredient(
                "Volvic mineral water",
                "1",
                "L",
                notes="CCAP currently uses this proprietary bottled mineral water.",
            )
        ],
        "solutions": [],
        "preparation_steps": [
            step(1, "ALIQUOT", "Dispense the mineral water into suitable vessels."),
            step(2, "AUTOCLAVE", "Autoclave at 15 psi for 15 minutes."),
        ],
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "sterilization": {"method": "AUTOCLAVE"},
    }


def sw_base_ingredients() -> list[dict[str, Any]]:
    return [
        variable_material(
            "Air-dried sieved calcareous soil",
            "Add a layer approximately 1 cm deep to each vessel.",
        ),
        variable_material(
            "Deionized water",
            "Add carefully to a depth of 7-10 cm above the soil layer.",
        ),
    ]


def sw_steps() -> list[dict[str, Any]]:
    return [
        step(
            1, "ALIQUOT", "Place a 1 cm layer of air-dried, sieved calcareous soil in each vessel."
        ),
        step(2, "MIX", "Optionally add one grain for organisms that benefit from it."),
        step(
            3, "ALIQUOT", "Add deionized water carefully to a depth of 7-10 cm, then plug or cover."
        ),
        step(4, "AUTOCLAVE", "Autoclave at 15 psi for 15 minutes on each of two consecutive days."),
        step(5, "STORE", "Let stand for at least one further day before inoculation."),
    ]


def sw_recipe() -> dict[str, Any]:
    return {
        "ingredients": sw_base_ingredients(),
        "solutions": [],
        "preparation_steps": sw_steps(),
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "BIPHASIC",
        "sterilization": {"method": "AUTOCLAVE"},
    }


def sw_variant_recipe(kind: str) -> dict[str, Any]:
    if kind == "sw_amp":
        additive = mapped_ingredient(
            "Ammonium magnesium phosphate",
            "0.01 g per vessel",
            "VARIABLE",
            "CHEBI:149425",
            "ammonium magnesium phosphate",
            notes="Place in the base of each vessel before adding soil and water.",
        )
    else:
        additive = mapped_ingredient(
            "Calcium carbonate",
            "0.01 g per vessel",
            "VARIABLE",
            "CHEBI:3311",
            "calcium carbonate",
            notes="Place in the base of each vessel before adding soil and water.",
        )
    steps = sw_steps()
    steps.insert(
        0,
        step(
            1,
            "ALIQUOT",
            f"Place approximately 0.01 g {additive['preferred_term'].lower()} in the base of each vessel.",
        ),
    )
    for number, row in enumerate(steps, start=1):
        row["step_number"] = number
    return {
        "ingredients": [additive, *sw_base_ingredients()],
        "solutions": [],
        "preparation_steps": steps,
        "ph_range": {"min": 7.0, "max": 8.0},
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "BIPHASIC",
        "sterilization": {"method": "AUTOCLAVE"},
    }


def soil_extract_recipe(kind: str) -> dict[str, Any]:
    is_se2 = kind == "se2"
    soil_description = (
        "Use air-dried, sieved calcareous garden loam."
        if is_se2
        else "Use air-dried, sieved rich loam from undisturbed deciduous woodland."
    )
    recipe = {
        "ingredients": [
            variable_material("Prepared dried soil", soil_description),
            variable_material(
                "Deionized water", "Use twice the volume of water relative to dried soil."
            ),
        ],
        "solutions": [],
        "preparation_steps": [
            step(
                1,
                "MIX",
                "Remove stones, roots, and large invertebrates; air-dry and sieve the soil.",
            ),
            step(
                2, "MIX", "Combine dried soil with twice its volume of supernatant deionized water."
            ),
            step(
                3,
                "AUTOCLAVE",
                "Autoclave at 15 psi and 126 C for 20 minutes; cool and repeat once.",
            ),
            step(4, "STORE", "Seal and leave undisturbed for 2-3 weeks so sediment settles."),
            step(
                5,
                "ALIQUOT",
                "Aseptically decant the supernatant into sterile containers without disturbing sediment.",
            ),
            step(
                6,
                "AUTOCLAVE",
                "Autoclave the final soil extract at 15 psi and 121 C for 15 minutes.",
            ),
            step(7, "STORE", "Cool, seal, and store refrigerated."),
        ],
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "sterilization": {"method": "AUTOCLAVE"},
    }
    if is_se2:
        recipe["ph_value"] = 7.1
    return recipe


def ses_recipe() -> dict[str, Any]:
    return {
        "ingredients": [water()],
        "solutions": [
            stock(
                "K2HPO4 stock solution",
                "20.0",
                [
                    mapped_ingredient(
                        "K2HPO4",
                        "1.0",
                        "G_PER_L",
                        "CHEBI:131527",
                        "dipotassium hydrogen phosphate",
                    )
                ],
                "CCAP SES stock solution 1; add 20 ml/L.",
            ),
            stock(
                "MgSO4.7H2O stock solution",
                "20.0",
                [
                    mapped_ingredient(
                        "MgSO4.7H2O",
                        "1.0",
                        "G_PER_L",
                        "CHEBI:31795",
                        "magnesium sulfate heptahydrate",
                    )
                ],
                "CCAP SES stock solution 2; add 20 ml/L.",
            ),
            stock(
                "KNO3 stock solution",
                "20.0",
                [mapped_ingredient("KNO3", "10.0", "G_PER_L", "CHEBI:63043", "potassium nitrate")],
                "CCAP SES stock solution 3; add 20 ml/L.",
            ),
            stock(
                "Soil Extract 2 (SE2)",
                "100.0",
                [],
                "Use the separately defined CCAP SE2 recipe.",
            ),
        ],
        "preparation_steps": [
            step(1, "MIX", "Add the four stock solutions and make up to 1 L with deionized water."),
            step(2, "AUTOCLAVE", "Autoclave at 15 psi for 15 minutes."),
        ],
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "sterilization": {"method": "AUTOCLAVE"},
    }


def yel_recipe() -> dict[str, Any]:
    return {
        "ingredients": [
            mapped_ingredient(
                "Yeast extract",
                "4.0",
                "G_PER_L",
                "FOODON:03315426",
                "yeast extract",
            ),
            mapped_ingredient(
                "Liver digest",
                "4.0",
                "G_PER_L",
                "MICRO:0001668",
                "liver digest",
            ),
            water(),
        ],
        "solutions": [],
        "preparation_steps": [
            step(1, "MIX", "Add the constituents and mix thoroughly."),
            step(2, "AUTOCLAVE", "Autoclave at 15 psi for 15 minutes."),
        ],
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "sterilization": {"method": "AUTOCLAVE"},
    }


RECIPES = {
    "ch": ch_recipe(),
    "merds": merds_recipe(),
    "mw": mw_recipe(),
    "sw": sw_recipe(),
    "sw_amp": sw_variant_recipe("sw_amp"),
    "sw_ca": sw_variant_recipe("sw_ca"),
    "se1": soil_extract_recipe("se1"),
    "se2": soil_extract_recipe("se2"),
    "ses": ses_recipe(),
    "yel": yel_recipe(),
}


def recipe_projection(doc: dict[str, Any]) -> dict[str, Any]:
    return {
        "ingredients": [descriptor_projection(row) for row in doc.get("ingredients") or []],
        "solutions": [descriptor_projection(row) for row in doc.get("solutions") or []],
        "preparation_steps": copy.deepcopy(doc.get("preparation_steps") or []),
        "ph_value": doc.get("ph_value"),
        "ph_range": copy.deepcopy(doc.get("ph_range")),
        "medium_type": doc.get("medium_type"),
        "composition_type": doc.get("composition_type"),
        "physical_state": doc.get("physical_state"),
        "sterilization": copy.deepcopy(doc.get("sterilization")),
    }


def source_note(target: Target) -> str:
    return f"Composition verified against {SOURCE_URLS[target.recipe_key]} on 2026-08-25."


def history_has_action(doc: dict[str, Any]) -> bool:
    return any(
        isinstance(row, dict) and row.get("action") == ACTION
        for row in doc.get("curation_history") or []
    )


def validate_source_files(source_dir: Path) -> None:
    for name, expected_hash in SOURCE_FILES.items():
        path = source_dir / name
        if not path.is_file():
            raise ValueError(f"missing reviewed source file: {path}")
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            raise ValueError(f"{path}: SHA-256 {actual_hash}, expected reviewed {expected_hash}")


def _validate_precondition(doc: dict[str, Any], target: Target) -> None:
    if str(doc.get("id") or "") != target.record_id:
        raise ValueError(
            f"{target.relative_path}: id {doc.get('id')!r}, expected {target.record_id}"
        )
    if target.precondition == "empty":
        if doc.get("ingredients") or doc.get("solutions"):
            raise ValueError(f"{target.relative_path}: record is no longer empty")
        if "incomplete_composition" not in (doc.get("data_quality_flags") or []):
            raise ValueError(f"{target.relative_path}: missing incomplete flag")
    elif target.precondition == "existing":
        actual = ingredient_signature(doc.get("ingredients") or [])
        expected = EXISTING_SIGNATURES[target.relative_path]
        if actual != expected or doc.get("solutions"):
            raise ValueError(f"{target.relative_path}: existing composition drifted")
    else:
        raise ValueError(f"unknown precondition {target.precondition}")


def _assert_applied(doc: dict[str, Any], target: Target) -> None:
    if recipe_projection(doc) != recipe_projection(RECIPES[target.recipe_key]):
        raise ValueError(f"{target.relative_path}: applied source recipe drifted")
    if "incomplete_composition" in (doc.get("data_quality_flags") or []):
        raise ValueError(f"{target.relative_path}: incomplete flag returned")
    if source_note(target) not in str(doc.get("notes") or ""):
        raise ValueError(f"{target.relative_path}: source verification note is missing")


def repair_document(doc: dict[str, Any], target: Target) -> tuple[dict[str, Any], bool]:
    if history_has_action(doc):
        _assert_applied(doc, target)
        return doc, False
    _validate_precondition(doc, target)

    recipe = RECIPES[target.recipe_key]
    repaired = copy.deepcopy(doc)
    fields = (
        "ingredients",
        "solutions",
        "preparation_steps",
        "ph_value",
        "ph_range",
        "medium_type",
        "composition_type",
        "physical_state",
        "sterilization",
    )
    for field in fields:
        value = recipe.get(field)
        if value in (None, []):
            repaired.pop(field, None)
        else:
            repaired[field] = copy.deepcopy(value)

    flags = repaired.get("data_quality_flags") or []
    if not isinstance(flags, list):
        raise ValueError(f"{target.relative_path}: data_quality_flags is not a list")
    kept_flags = [flag for flag in flags if flag != "incomplete_composition"]
    if kept_flags:
        repaired["data_quality_flags"] = kept_flags
    else:
        repaired.pop("data_quality_flags", None)

    note = source_note(target)
    existing_notes = str(repaired.get("notes") or "").rstrip()
    repaired["notes"] = f"{existing_notes}\n{note}" if existing_notes else note

    history = repaired.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.relative_path}: curation_history is not a list")
    history.append(
        {
            "timestamp": TIMESTAMP,
            "curator": "repair_ccap_duplicate_compositions.py",
            "action": ACTION,
            "changes": (
                f"ingredients {len(doc.get('ingredients') or [])} -> "
                f"{len(recipe['ingredients'])}; solutions "
                f"{len(doc.get('solutions') or [])} -> {len(recipe['solutions'])}"
            ),
            "notes": (
                f"Rebuilt {target.recipe_key} from the reviewed CCAP PDF. Preserved "
                "stock boundaries and per-vessel quantities; ingredient identities "
                "follow the MediaIngredientMech SSSOM."
            ),
        }
    )
    _assert_applied(repaired, target)
    return repaired, True


def _validate_inventory() -> None:
    paths = [target.relative_path for target in TARGETS]
    ids = [target.record_id for target in TARGETS]
    pairs = {(Path(target.relative_path).stem, target.recipe_key) for target in TARGETS}
    if (
        len(TARGETS) != 20
        or len(paths) != len(set(paths))
        or len(ids) != len(set(ids))
        or len(pairs) != 10
    ):
        raise ValueError("CCAP duplicate inventory is not ten unique record pairs")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    _validate_inventory()
    if args.apply:
        if args.source_dir is None:
            raise ValueError("--apply requires --source-dir with reviewed CCAP PDFs")
        validate_source_files(args.source_dir)

    pending = []
    for target in TARGETS:
        path = args.normalized_dir / target.relative_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            raise ValueError(f"{path}: expected a YAML mapping")
        repaired, changed = repair_document(doc, target)
        pending.append((path, repaired, changed, target))
        print(f"{'fix' if changed else 'skip':4s}  {target.relative_path}: {target.recipe_key}")

    changed_count = sum(changed for _, _, changed, _ in pending)
    if args.apply:
        for path, repaired, changed, _ in pending:
            if changed:
                write_record(path, repaired)
    verb = "updated" if args.apply else "would update"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
