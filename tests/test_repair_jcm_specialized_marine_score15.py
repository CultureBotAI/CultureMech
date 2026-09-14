from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_specialized_marine_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_jcm_specialized_marine_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_specialized_marine")


def _term(identifier: str, label: str) -> dict:
    return {"id": identifier, "label": label}


def _ingredient(name: str, value: str, unit: str) -> dict:
    row = {"preferred_term": name, "concentration": {"value": value, "unit": unit}}
    if name in {"Agar", "Marine agar 2216"}:
        row["term"] = _term("CHEBI:2509", "agar")
        row["mediaingredientmech_chebi_term"] = _term("CHEBI:2509", "agar")
    return row


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def _diluted_doc(repair_module) -> dict:
    return {
        "id": repair_module.DILUTED.identifier,
        "name": "diluted_marine_agar",
        "original_name": "DILUTED MARINE AGAR",
        "category": "specialized",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "JCM Medium J644",
            "term": {
                "id": repair_module.DILUTED.media_term_id,
                "label": "DILUTED MARINE AGAR",
            },
        },
        "notes": f"Source: JCM | Link: {repair_module.DILUTED.jcm_url}",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.DILUTED_IMPORTED_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _ph_doc(repair_module, target) -> dict:
    return {
        "id": target.identifier,
        "name": target.path.stem,
        "original_name": f"MARINE AGAR 2216 (pH {target.ph_value:.1f})",
        "category": "specialized",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": target.ph_value,
        "media_term": {
            "preferred_term": f"JCM Medium J{target.medium_no}",
            "term": {
                "id": target.media_term_id,
                "label": f"MARINE AGAR 2216 (pH {target.ph_value:.1f})",
            },
        },
        "notes": f"Source: JCM | Link: {target.jcm_url}",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.MARINE_AGAR_IMPORTED_SIGNATURE
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "ADJUST_PH",
                "description": (
                    f"Prepare Marine agar 2216 (see Medium No. 118). After "
                    f"autoclaving, adjust pH to {target.ph_value:.1f} with "
                    "sterilized 10% Na2CO3 solution."
                ),
            }
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": ["resolved_reference"],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.PARENT_ID,
        "name": repair_module.PARENT_NAME,
        "curation_history": [],
        "variant_children": [
            {
                "path": "data/normalized_yaml/specialized/marine_agar_2216_with_1_nacl.yaml",
                "relationship": "SALINITY_VARIANT",
                "id": "CultureMech:015426",
                "name": "marine_agar_2216_with_1_nacl",
                "notes": "Adds 10 g/L NaCl to JCM Medium 118 Marine Agar 2216.",
            }
        ],
    }


def test_repair_diluted_marine_agar_adds_jcm_water_and_seawater(repair_module) -> None:
    repaired = repair_module.repair_diluted_record(_diluted_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"]) == (
        repair_module.DILUTED_FINAL_SIGNATURE
    )
    assert ingredients["Filtered seawater"]["concentration"] == {
        "value": "750",
        "unit": "ML_PER_L",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "250",
        "unit": "ML_PER_L",
    }
    assert ingredients["Agar"]["term"] == _term("CHEBI:2509", "agar")
    assert ingredients["Distilled water"]["term"] == _term("CHEBI:15377", "water")
    assert "term" not in ingredients["Marine broth 2216 (BD-Difco)"]
    assert "term" not in ingredients["Filtered seawater"]
    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert "kg_microbe_match" not in repaired


@pytest.mark.parametrize(
    "target",
    tuple(_load_script(SCRIPT, "repair_jcm_specialized_marine_targets").PH_TARGETS),
)
def test_repair_ph_variants_copy_parent_recipe_and_add_carbonate_solution(
    repair_module,
    scorer_module,
    target,
) -> None:
    repaired = repair_module.repair_ph_record(target, _ph_doc(repair_module, target))
    ingredients = _by_name(repaired["ingredients"])
    sodium_carbonate = repaired["solutions"][0]["composition"][0]

    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repair_module._signature(repaired["ingredients"]) == (
        repair_module.MARINE_AGAR_FINAL_SIGNATURE
    )
    assert "term" not in ingredients["Marine agar 2216 (BD-Difco)"]
    assert ingredients["Distilled water"]["term"] == _term("CHEBI:15377", "water")
    assert sodium_carbonate["term"] == _term("CHEBI:29377", "sodium carbonate")
    assert sodium_carbonate["concentration"] == {
        "value": "10.0",
        "unit": "PERCENT_W_V",
    }
    assert repaired["parent_media"] == repair_module._parent_media(target)
    assert repaired["variant_relationship"] == "PH_VARIANT"
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


def test_repaired_diluted_record_exits_score_report(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_diluted_record(_diluted_doc(repair_module))

    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(repair_module.DILUTED.path), repaired)]) == []


@pytest.mark.parametrize(
    "target",
    tuple(_load_script(SCRIPT, "repair_jcm_specialized_marine_refs").PH_TARGETS),
)
def test_repair_ph_variants_add_references_flags_and_event_once(
    repair_module,
    target,
) -> None:
    once = repair_module.repair_ph_record(target, _ph_doc(repair_module, target))
    twice = repair_module.repair_ph_record(target, once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)
    assert once["references"] == [{"reference": reference} for reference in target.references]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.PH_ACTION
        )
    ]
    assert len(matching_events) == 1


def test_repair_diluted_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_diluted_record(_diluted_doc(repair_module))
    twice = repair_module.repair_diluted_record(once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)
    assert once["references"] == [
        {"reference": reference} for reference in repair_module.DILUTED.references
    ]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.DILUTED_ACTION
        )
    ]
    assert len(matching_events) == 1


def test_repair_parent_adds_ph_children_once(repair_module) -> None:
    once = repair_module.repair_parent(_parent_doc(repair_module))
    twice = repair_module.repair_parent(once)

    child_paths = {child["path"] for child in once["variant_children"]}
    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)
    assert {
        f"data/normalized_yaml/{target.path}" for target in repair_module.PH_TARGETS
    }.issubset(child_paths)
    assert once["variant_children"] == sorted(
        once["variant_children"],
        key=lambda child: child["path"],
    )
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.PARENT_ACTION
        )
    ]
    assert len(matching_events) == 1


def test_plan_repairs_target_records(repair_module) -> None:
    expected = {
        repair_module.NORMALIZED / repair_module.DILUTED.path: (
            repair_module.repair_diluted_record(
                yaml.safe_load(
                    (repair_module.NORMALIZED / repair_module.DILUTED.path).read_text(
                        encoding="utf-8"
                    )
                )
            )
        ),
        repair_module.NORMALIZED / repair_module.PARENT_PATH: (
            repair_module.repair_parent(
                yaml.safe_load(
                    (repair_module.NORMALIZED / repair_module.PARENT_PATH).read_text(
                        encoding="utf-8"
                    )
                )
            )
        ),
    }
    for target in repair_module.PH_TARGETS:
        target_path = repair_module.NORMALIZED / target.path
        expected[target_path] = repair_module.repair_ph_record(
            target,
            yaml.safe_load(target_path.read_text(encoding="utf-8")),
        )

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_diluted_id(repair_module) -> None:
    doc = _diluted_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.DILUTED.identifier):
        repair_module.repair_diluted_record(doc)


def test_repair_rejects_wrong_ph_media_term(repair_module) -> None:
    target = repair_module.PH_TARGETS[0]
    doc = _ph_doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:J999"

    with pytest.raises(ValueError, match=target.media_term_id):
        repair_module.repair_ph_record(target, doc)


def test_repair_rejects_diluted_ingredient_drift(repair_module) -> None:
    doc = _diluted_doc(repair_module)
    doc["ingredients"][2]["preferred_term"] = "Seawater"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_diluted_record(doc)


def test_repair_parent_rejects_wrong_id(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.PARENT_ID):
        repair_module.repair_parent(doc)
