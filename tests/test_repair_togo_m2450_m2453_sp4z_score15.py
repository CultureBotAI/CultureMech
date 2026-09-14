from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2450_m2453_sp4z_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2450_m2453_sp4z_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2450_m2453_sp4z")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.expected_id,
        "name": "sp4_z_medium",
        "original_name": "SP4-Z Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": target.physical_state,
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {target.expected_media_term.removeprefix('TOGO:')}",
            "term": {"id": target.expected_media_term, "label": "SP4-Z Medium"},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_solution_signature
        ],
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "sp4_z_medium",
        "original_name": "SP4-Z MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 7.4,
        "media_term": {
            "preferred_term": "DSMZ Medium 1076b",
            "term": {
                "id": repair_module.EXPECTED_PARENT_MEDIA_TERM,
                "label": "SP4-Z MEDIUM",
            },
        },
        "notes": "Source: DSMZ",
        "ingredients": [],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_200_ml_amounts_and_moves_energy_solution(
    repair_module,
) -> None:
    expected = (
        (repair_module.TARGET_M2450, "650.0", False),
        (repair_module.TARGET_M2451, "650.0", False),
        (repair_module.TARGET_M2452, "630.0", True),
        (repair_module.TARGET_M2453, "630.0", True),
    )

    for target, water_volume, has_agar in expected:
        repaired = repair_module.repair_target(_doc(target), target)
        ingredients = _by_name(repaired["ingredients"])

        assert repaired["physical_state"] == target.physical_state
        assert repaired["ph_value"] == 7.4
        assert "solutions" not in repaired
        assert (
            repair_module._signature(
                repaired["ingredients"],
                "ingredients",
            )
            == target.final_signature
        )
        assert ingredients["distilled water"]["concentration"] == {
            "value": water_volume,
            "unit": "ML_PER_L",
        }
        assert ("agar" in ingredients) is has_agar
        assert ingredients[target.energy_source.preferred_term]["concentration"] == {
            "value": "10.0",
            "unit": "ML_PER_L",
        }


def test_repair_grounds_disclosed_unambiguous_components(repair_module) -> None:
    m2453 = repair_module.repair_target(
        _doc(repair_module.TARGET_M2453),
        repair_module.TARGET_M2453,
    )
    ingredients = _by_name(m2453["ingredients"])

    assert ingredients["agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["DNA (fish sperm; SERVA)"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:16991",
        "label": "deoxyribonucleic acid",
    }
    assert ingredients["Tryptone"]["term"] == {
        "id": "MICRO:0000182",
        "label": "tryptone",
    }
    assert ingredients["Arginine HCl (50% aqueous solution)"]["term"] == {
        "id": "CHEBI:31235",
        "label": "L-Arginine x HCl",
    }


def test_repair_keeps_opaque_products_unmapped(repair_module) -> None:
    repaired = repair_module.repair_target(
        _doc(repair_module.TARGET_M2450),
        repair_module.TARGET_M2450,
    )
    ingredients = _by_name(repaired["ingredients"])

    for name in (
        "PPLO broth",
        "Fetal bovine serum (heat-inactivated)",
        "Yeastolate (BD; 2%, autoclaved)",
        "Swine serum (heat-inactivated)",
        "CMRL-1066 medium (10x concentrated; GIBCO)",
    ):
        assert "term" not in ingredients[name]
        assert "mediaingredientmech_chebi_term" not in ingredients[name]
        assert "without an ontology grounding" in ingredients[name]["notes"]


def test_repair_adds_ph_and_disclosed_preparation_steps(repair_module) -> None:
    liquid = repair_module.repair_target(
        _doc(repair_module.TARGET_M2450),
        repair_module.TARGET_M2450,
    )
    agar = repair_module.repair_target(
        _doc(repair_module.TARGET_M2452),
        repair_module.TARGET_M2452,
    )

    assert [step["action"] for step in liquid["preparation_steps"]] == [
        "ADJUST_PH",
        "AUTOCLAVE",
        "MIX",
    ]
    assert [step["action"] for step in agar["preparation_steps"]] == [
        "ADJUST_PH",
        "AUTOCLAVE",
        "HEAT",
        "MIX",
    ]
    assert "121 degrees C for 15 minutes" in agar["preparation_steps"][1]["description"]
    assert "55 degrees C" in agar["preparation_steps"][2]["description"]
    assert "temperature_value" not in liquid
    assert "temperature_range" not in agar
    assert "sterilization" not in agar


def test_repair_links_targets_to_dsmz_sp4z_parent(repair_module) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_target(_doc(target), target)

        assert repaired["parent_media"] == repair_module._parent_media(target)
        assert repaired["variant_relationship"] == "DERIVED_FROM"
        assert repaired["variant_modifications"] == [target.variant_modification]


def test_repair_records_drop_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_target(_doc(target), target)

        assert scorer_module.score_record(repaired) == (0, [])
        assert scorer_module.score_parsed([(str(target.path), repaired)]) == []
        assert repaired["data_quality_flags"] == [
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    target = repair_module.TARGET_M2452
    once = repair_module.repair_target(_doc(target), target)
    twice = repair_module.repair_target(once, target)

    assert twice["references"] == [{"reference": url} for url in target.reference_urls]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "200 ml source amounts" in matching_events[0]["notes"]


def test_repair_parent_adds_four_togo_children_once(repair_module) -> None:
    once = repair_module.repair_parent(_parent_doc(repair_module))
    twice = repair_module.repair_parent(once)

    assert twice["variant_children"] == [
        repair_module._variant_child(repair_module.TARGET_M2450),
        repair_module._variant_child(repair_module.TARGET_M2451),
        repair_module._variant_child(repair_module.TARGET_M2452),
        repair_module._variant_child(repair_module.TARGET_M2453),
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.LINK_ACTION
        )
    ]
    assert len(matching_events) == 1


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGET_M2450
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.expected_id):
        repair_module.repair_target(doc, target)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGET_M2451
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=target.expected_media_term):
        repair_module.repair_target(doc, target)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGET_M2452
    doc = _doc(target)
    doc["ingredients"][0] = _ingredient("distilled water", "630.0", "ML_PER_L")

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_target(doc, target)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGET_M2453
    doc = _doc(target)
    doc["solutions"][0] = _ingredient("Glucose (50% aqueous solution)", "2", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_target(doc, target)


def test_repair_parent_rejects_wrong_parent_id(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_PARENT_ID):
        repair_module.repair_parent(doc)


def test_target_records_match_repair_contract(repair_module) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == target.expected_id
        assert repair_module._source_term_id(doc) == target.expected_media_term
        assert (
            repair_module._signature(doc["ingredients"], "ingredients"),
            repair_module._signature(doc.get("solutions"), "solutions"),
        ) in (
            (target.imported_signature, target.imported_solution_signature),
            (target.final_signature, ()),
        )
