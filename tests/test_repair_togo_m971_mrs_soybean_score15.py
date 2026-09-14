from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m971_mrs_soybean_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m971_mrs_soybean_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m971")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _target(repair_module, path: Path):
    return next(target for target in repair_module.TARGETS if target.path == path)


def _medium_doc(repair_module, path: Path) -> dict:
    target = _target(repair_module, path)
    return {
        "id": target.record_id,
        "name": "mrs_medium_with_soybean_peptone",
        "original_name": "MRS MEDIUM WITH SOYBEAN PEPTONE",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _component(name, value, unit) for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": "JCM Medium J925",
            "term": {
                "id": target.media_term_id,
                "label": "MRS MEDIUM WITH SOYBEAN PEPTONE",
            },
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": repair_module.FALSE_KG_MATCH,
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def _repair(repair_module, path: Path) -> dict:
    target = _target(repair_module, path)
    return repair_module.repair_record(_medium_doc(repair_module, path), target)


@pytest.mark.parametrize(
    "path",
    [
        pytest.param("JCM_J925_PATH", id="mediadive-j925"),
        pytest.param("TOGO_M971_PATH", id="togo-m971"),
    ],
)
def test_m971_water_unit_groundings_and_autoclaving_are_repaired(
    repair_module,
    scorer_module,
    path: str,
) -> None:
    repaired = _repair(repair_module, getattr(repair_module, path))
    ingredients = _by_name(repaired["ingredients"])

    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_SIGNATURE
    )
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["Phytone peptone (BD-BBL)"]["term"] == {
        "id": "FOODON:03315720",
        "label": "Soy peptone",
    }
    assert ingredients["Bacto agar (BD-Difco)"]["physicochemical_roles"] == ["SOLIDIFYING_AGENT"]
    assert "term" not in ingredients["Lactobacilli MRS broth (BD-Difco)"]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["preparation_steps"] == repair_module.PREPARATION_STEPS
    assert repaired["sterilization"] == repair_module.STERILIZATION
    assert "kg_microbe_match" not in repaired
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([("bacterial/m971.yaml", repaired)]) == []


def test_repair_links_source_duplicates(repair_module) -> None:
    j925 = _repair(repair_module, repair_module.JCM_J925_PATH)
    m971 = _repair(repair_module, repair_module.TOGO_M971_PATH)

    assert j925["parent_media"] == repair_module.TOGO_M971_PARENT
    assert j925["variant_relationship"] == "SOURCE_DUPLICATE"
    assert j925["variant_modifications"] == [repair_module.TOGO_M971_PARENT["notes"]]
    assert "variant_children" not in j925

    assert m971["variant_children"] == [repair_module.JCM_J925_CHILD]
    assert "parent_media" not in m971


def test_repair_adds_source_specific_references(repair_module) -> None:
    j925 = _repair(repair_module, repair_module.JCM_J925_PATH)
    m971 = _repair(repair_module, repair_module.TOGO_M971_PATH)

    assert j925["references"] == [{"reference": repair_module.JCM_925}]
    assert m971["references"] == [
        {"reference": repair_module.TOGO_M971},
        {"reference": repair_module.JCM_925},
    ]


@pytest.mark.parametrize(
    "path",
    [
        pytest.param("JCM_J925_PATH", id="mediadive-j925"),
        pytest.param("TOGO_M971_PATH", id="togo-m971"),
    ],
)
def test_repair_is_idempotent(repair_module, path: str) -> None:
    target_path = getattr(repair_module, path)
    target = _target(repair_module, target_path)
    once = repair_module.repair_record(
        _medium_doc(repair_module, target_path),
        target,
    )
    twice = repair_module.repair_record(once, target)

    assert twice == once


def test_m971_rejects_wrong_source(repair_module) -> None:
    doc = _medium_doc(repair_module, repair_module.TOGO_M971_PATH)
    doc["media_term"]["term"]["id"] = "TOGO:wrong"

    with pytest.raises(ValueError, match="TOGO:M971"):
        repair_module.repair_record(
            doc,
            _target(repair_module, repair_module.TOGO_M971_PATH),
        )


def test_m971_rejects_ingredient_drift(repair_module) -> None:
    doc = _medium_doc(repair_module, repair_module.TOGO_M971_PATH)
    doc["ingredients"][0]["preferred_term"] = "Tap water"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(
            doc,
            _target(repair_module, repair_module.TOGO_M971_PATH),
        )


def test_j925_rejects_unexpected_kg_microbe_match(repair_module) -> None:
    doc = _medium_doc(repair_module, repair_module.JCM_J925_PATH)
    doc["kg_microbe_match"] = "mediadive.medium:925"

    with pytest.raises(ValueError, match="unexpected kg_microbe_match"):
        repair_module.repair_record(
            doc,
            _target(repair_module, repair_module.JCM_J925_PATH),
        )
