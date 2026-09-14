from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_j481_j482_sea_salt_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_j481_j482_sea_salt")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_j481")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _media_term(term_id: str) -> dict:
    return {
        "preferred_term": f"source {term_id}",
        "term": {"id": term_id, "label": "source"},
    }


def _doc(repair_module, target) -> dict:
    return {
        "id": target.expected_id,
        "name": target.path.stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": _media_term(target.expected_media_term),
        "notes": "Source",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_signature
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


@pytest.mark.parametrize("target", list(_load_script(SCRIPT, "jcm_j481_params").TARGETS))
def test_repair_normalizes_family_and_leaves_review_ranking(
    repair_module,
    scorer_module,
    target,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        target.final_signature
    )
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert repaired["sterilization"] == repair_module.STERILIZATION
    assert "solutions" not in repaired
    assert "kg_microbe_match" not in repaired
    assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


@pytest.mark.parametrize("target", list(_load_script(SCRIPT, "jcm_j481_params2").TARGETS))
def test_repair_grounds_water_and_agar_only(repair_module, target) -> None:
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["Agar"]["physicochemical_roles"] == ["SOLIDIFYING_AGENT"]
    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert "term" not in ingredients["Reinforced clostridial medium (BD-Difco)"]
    assert "term" not in ingredients["Sea salts (Sigma)"]


@pytest.mark.parametrize("target", list(_load_script(SCRIPT, "jcm_j481_params3").TARGETS))
def test_repair_adds_flags_references_and_event_once(repair_module, target) -> None:
    once = repair_module.repair_record(_doc(repair_module, target), target)
    twice = repair_module.repair_record(once, target)

    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert twice["references"] == [
        {"reference": reference} for reference in target.references
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


def test_plan_repairs_targets_four_source_records(repair_module) -> None:
    plans = repair_module.plan_repairs()

    assert set(plans) == {
        repair_module.NORMALIZED / target.path for target in repair_module.TARGETS
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=f"expected id {target.expected_id}"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:J999"

    with pytest.raises(ValueError, match=f"expected media term {target.expected_media_term}"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"][0] = _ingredient("Reinforced clostridial medium", "30", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_corpus_records_match_repair_contract(repair_module) -> None:
    for target in repair_module.TARGETS:
        doc = yaml.safe_load(
            (repair_module.NORMALIZED / target.path).read_text(encoding="utf-8")
        )

        assert doc["id"] == target.expected_id
        assert repair_module._source_term_id(doc) == target.expected_media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in (
            target.imported_signature,
            target.final_signature,
        )
        assert "solutions" not in doc
