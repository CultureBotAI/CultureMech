from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_mediadb_tap_score15.py"
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
    return _load_script(SCRIPT, "repair_mediadb_tap")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_mediadb_tap")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module, spec) -> dict:
    return {
        "id": spec.expected_id,
        "name": spec.target.stem,
        "original_name": "TAP (auto)" if spec is repair_module.AUTO_SPEC else "TAP (hetero/mixo)",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in spec.ingredient_signature
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "DISSOLVE",
                "description": "Dissolve all ingredients in distilled water.",
            }
        ],
        "curation_history": [],
        "media_term": {
            "preferred_term": f"MediaDB Medium {spec.expected_media_term.split(':', 1)[1]}",
            "term": {
                "id": spec.expected_media_term,
                "label": "TAP (auto)" if spec is repair_module.AUTO_SPEC else "TAP (hetero/mixo)",
            },
        },
        "notes": "Source: MediaDB",
        "applications": ["Cultivation of genome-sequenced organisms"],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_grounds_all_components_and_exits_ranking(
    repair_module,
    scorer_module,
) -> None:
    auto = repair_module.repair_auto_parent(_doc(repair_module, repair_module.AUTO_SPEC))
    hetero = repair_module.repair_record(
        _doc(repair_module, repair_module.HETERO_SPEC),
        repair_module.HETERO_SPEC,
    )

    for repaired, spec in (
        (auto, repair_module.AUTO_SPEC),
        (hetero, repair_module.HETERO_SPEC),
    ):
        assert repaired["ph_value"] == 7.0
        assert repaired["temperature_value"] == 25.0
        assert "preparation_steps" not in repaired
        assert repair_module._signature(repaired["ingredients"], "ingredients") == (
            spec.ingredient_signature
        )
        assert all("mediaingredientmech_chebi_term" in row for row in repaired["ingredients"])
        assert scorer_module.score_record(repaired) == (0, [])

    assert (
        scorer_module.score_parsed(
            [
                (str(repair_module.TAP_AUTO), auto),
                (str(repair_module.TAP_HETERO_MIXO), hetero),
            ]
        )
        == []
    )


def test_repair_uses_expected_chebi_terms(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.HETERO_SPEC),
        repair_module.HETERO_SPEC,
    )
    ingredients = _by_name(repaired["ingredients"])

    for name, expected in repair_module.GROUNDINGS.items():
        assert ingredients[name]["term"] == {
            "id": expected[0],
            "label": expected[1],
        }
        assert ingredients[name]["mediaingredientmech_chebi_term"] == {
            "id": expected[0],
            "label": expected[1],
        }


def test_repair_adds_growth_metrics(repair_module) -> None:
    auto = repair_module.repair_record(
        _doc(repair_module, repair_module.AUTO_SPEC),
        repair_module.AUTO_SPEC,
    )
    hetero = repair_module.repair_record(
        _doc(repair_module, repair_module.HETERO_SPEC),
        repair_module.HETERO_SPEC,
    )

    auto_metrics = auto["target_organisms"][0]["growth_metrics"]
    hetero_metrics = hetero["target_organisms"][0]["growth_metrics"]

    assert auto["organism_culture_type"] == "isolate"
    assert auto["target_organisms"][0]["term"] == {
        "id": "NCBITaxon:3055",
        "label": "Chlamydomonas reinhardtii",
    }
    assert [metric["growth_rate_per_hour"] for metric in auto_metrics] == [0.059]
    assert [metric["growth_rate_per_hour"] for metric in hetero_metrics] == [0.035, 0.066]
    assert {metric["evidence"][0]["reference"] for metric in hetero_metrics} == {
        repair_module.GROWTH_HETERO,
        repair_module.GROWTH_MIXO,
    }


def test_repair_adds_variant_links_references_flags_and_events_once(
    repair_module,
) -> None:
    auto_once = repair_module.repair_auto_parent(_doc(repair_module, repair_module.AUTO_SPEC))
    auto_twice = repair_module.repair_auto_parent(auto_once)
    hetero_once = repair_module.repair_record(
        _doc(repair_module, repair_module.HETERO_SPEC),
        repair_module.HETERO_SPEC,
    )
    hetero_twice = repair_module.repair_record(hetero_once, repair_module.HETERO_SPEC)

    assert auto_twice["variant_children"] == [repair_module.AUTO_CHILD]
    assert hetero_twice["parent_media"] == repair_module.HETERO_PARENT
    assert hetero_twice["variant_relationship"] == "SUPPLEMENTED_VARIANT"
    assert hetero_twice["variant_modifications"] == ["Adds 17.4 mM acetate to MediaDB TAP (auto)."]
    assert auto_twice["references"] == [
        {"reference": reference} for reference in repair_module.AUTO_SPEC.references
    ]
    assert hetero_twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert [
        event
        for event in auto_twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.PARENT_ACTION
        )
    ] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.PARENT_ACTION,
            "source": f"{repair_module.MEDIA_AUTO}; {repair_module.MEDIA_HETERO_MIXO}",
            "notes": (
                "Linked TAP (hetero/mixo) as the 17.4 mM acetate-supplemented TAP (auto) variant."
            ),
        }
    ]


def test_plan_repairs_targets_both_tap_records(repair_module) -> None:
    auto = repair_module.NORMALIZED / repair_module.TAP_AUTO
    hetero = repair_module.NORMALIZED / repair_module.TAP_HETERO_MIXO

    assert repair_module.plan_repairs() == {
        auto: repair_module.repair_auto_parent(yaml.safe_load(auto.read_text(encoding="utf-8"))),
        hetero: repair_module.repair_record(
            yaml.safe_load(hetero.read_text(encoding="utf-8")),
            repair_module.HETERO_SPEC,
        ),
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module, repair_module.AUTO_SPEC)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_AUTO_ID):
        repair_module.repair_record(doc, repair_module.AUTO_SPEC)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module, repair_module.HETERO_SPEC)
    doc["media_term"]["term"]["id"] = "MEDIADB:35"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_HETERO_MEDIA_TERM):
        repair_module.repair_record(doc, repair_module.HETERO_SPEC)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.HETERO_SPEC)
    doc["ingredients"][1] = _ingredient("Glucose", "17.4", "MILLIMOLAR")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, repair_module.HETERO_SPEC)


def test_corpus_records_match_repair_contract(repair_module) -> None:
    for spec in repair_module.SPECS:
        path = repair_module.NORMALIZED / spec.target
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == spec.expected_id
        assert repair_module._source_term_id(doc) == spec.expected_media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") == (
            spec.ingredient_signature
        )
