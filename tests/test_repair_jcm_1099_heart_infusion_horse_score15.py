from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_1099_heart_infusion_horse_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_1099_heart_infusion_horse")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_1099")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _target(repair_module, path: Path):
    for target in repair_module.TARGETS:
        if target.path == path:
            return target
    raise AssertionError(f"unknown target: {path}")


def _doc(repair_module, target) -> dict:
    return {
        "id": target.expected_id,
        "name": target.path.stem,
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": str(target.path),
            "term": {
                "id": target.expected_media_term,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: JCM",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_adds_jcm_water_and_corrects_horse_blood(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.JCM_TARGET)
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert ingredients["Horse blood"]["concentration"] == {
        "value": "50.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "950.0",
        "unit": "ML_PER_L",
    }
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )
    assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


def test_repair_corrects_togo_ml_unit_artifacts(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.TOGO_TARGET)
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "950.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Horse blood"]["concentration"] == {
        "value": "50.0",
        "unit": "ML_PER_L",
    }
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )
    assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


def test_repair_grounds_machine_usable_components(repair_module) -> None:
    target = _target(repair_module, repair_module.JCM_TARGET)
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Heart infusion broth (BD-Difco)"] == {
        "preferred_term": "Heart infusion broth (BD-Difco)",
        "concentration": {"value": "25.0", "unit": "G_PER_L"},
        "source": repair_module.SOURCE,
        "notes": (
            "JCM Medium 1099 lists 25.0 g/L Heart infusion broth from "
            "BD-Difco; this commercial base is retained as an opaque "
            "component."
        ),
    }
    assert ingredients["Horse blood"]["term"] == {
        "id": "UBERON:0000178",
        "label": "blood",
    }
    assert ingredients["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }


def test_repair_adds_jcm_preparation_and_default_sterilization(
    repair_module,
) -> None:
    target = _target(repair_module, repair_module.JCM_TARGET)
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "MIX",
        "AUTOCLAVE",
        "MIX",
        "POUR_PLATES",
    ]
    assert repaired["sterilization"] == repair_module.STERILIZATION


def test_repair_links_togo_as_source_duplicate(repair_module) -> None:
    jcm = _target(repair_module, repair_module.JCM_TARGET)
    togo = _target(repair_module, repair_module.TOGO_TARGET)

    jcm_repaired = repair_module.repair_record(_doc(repair_module, jcm), jcm)
    togo_repaired = repair_module.repair_record(_doc(repair_module, togo), togo)

    assert jcm_repaired["variant_children"] == [repair_module.TOGO_CHILD_REF]
    assert "parent_media" not in jcm_repaired
    assert togo_repaired["parent_media"] == repair_module.JCM_PARENT_REF
    assert togo_repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert "variant_children" not in togo_repaired


def test_repair_adds_references_flags_and_events_once(repair_module) -> None:
    for target in repair_module.TARGETS:
        once = repair_module.repair_record(_doc(repair_module, target), target)
        twice = repair_module.repair_record(once, target)

        assert twice["references"] == [
            {"reference": reference} for reference in target.references
        ]
        assert twice["data_quality_flags"] == [
            "ingredients_curated",
            "has_ontology_mappings",
            "has_unmapped_ingredients",
        ]
        matching_events = [
            event
            for event in twice["curation_history"]
            if (
                event.get("curator") == repair_module.CURATOR
                and event.get("action") == repair_module.ACTION
            )
        ]
        assert len(matching_events) == 1


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = _target(repair_module, repair_module.JCM_TARGET)
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.expected_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    target = _target(repair_module, repair_module.TOGO_TARGET)
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "TOGO:M1099"

    with pytest.raises(ValueError, match=target.expected_media_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = _target(repair_module, repair_module.JCM_TARGET)
    doc = _doc(repair_module, target)
    doc["ingredients"][0] = _ingredient("Heart infusion broth (BD-Difco)", "25", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = _target(repair_module, repair_module.TOGO_TARGET)
    doc = _doc(repair_module, target)
    doc["solutions"] = [{"preferred_term": "extra"}]

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_jcm_1099_repair_contract(repair_module) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == target.expected_id
        assert repair_module._source_term_id(doc) == target.expected_media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in (
            target.imported_signature,
            repair_module.FINAL_INGREDIENT_SIGNATURE,
        )
        assert "solutions" not in doc
