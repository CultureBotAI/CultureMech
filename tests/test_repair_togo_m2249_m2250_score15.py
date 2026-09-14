from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2249_m2250_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2249_m2250_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2249_m2250")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.expected_id,
        "name": "lactobacilli_mrs_agar_broth",
        "original_name": "Lactobacilli MRS Agar/Broth",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": target.physical_state,
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {target.expected_media_term.removeprefix('TOGO:')}",
            "term": {"id": target.expected_media_term, "label": "Lactobacilli MRS Agar/Broth"},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_expanded_mrs_scratch_formulas(
    repair_module,
) -> None:
    expected = (
        (
            repair_module.TARGET_M2249,
            "SOLID_AGAR",
            repair_module.M2249_FINAL_INGREDIENT_SIGNATURE,
        ),
        (
            repair_module.TARGET_M2250,
            "LIQUID",
            repair_module.M2250_FINAL_INGREDIENT_SIGNATURE,
        ),
    )

    for target, physical_state, signature in expected:
        repaired = repair_module.repair_record(_doc(target), target)

        assert repaired["medium_type"] == "COMPLEX"
        assert repaired["composition_type"] == "UNDEFINED"
        assert repaired["physical_state"] == physical_state
        assert repaired["ph_range"] == {"min": 6.3, "max": 6.7}
        assert repair_module._signature(repaired["ingredients"], "ingredients") == signature

        ingredients = _by_name(repaired["ingredients"])
        assert ingredients["DI Water"]["concentration"] == {
            "value": "1.0",
            "unit": "L",
        }
        assert "Lactobacilli MRS" not in ingredients


def test_repair_adds_variant_specific_preparation_steps(
    repair_module,
) -> None:
    agar = repair_module.repair_record(
        _doc(repair_module.TARGET_M2249),
        repair_module.TARGET_M2249,
    )
    broth = repair_module.repair_record(
        _doc(repair_module.TARGET_M2250),
        repair_module.TARGET_M2250,
    )

    assert agar["sterilization"] == {"method": "AUTOCLAVE"}
    assert agar["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "HEAT",
            "description": "Boil to dissolve agar.",
        },
        {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 C.",
        },
    ]

    assert broth["sterilization"] == {"method": "AUTOCLAVE"}
    assert broth["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 C.",
        }
    ]


def test_repair_grounds_disclosed_unambiguous_components(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module.TARGET_M2249),
        repair_module.TARGET_M2249,
    )
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["DI Water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["Dextrose"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17634",
        "label": "D-glucose",
    }
    assert ingredients["MnSO4 x H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:86364",
        "label": "manganese(II) sulfate monohydrate",
    }
    assert ingredients["Na2HPO4"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:34683",
        "label": "disodium hydrogenphosphate",
    }
    assert ingredients["Sodium Acetate"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:32954",
        "label": "sodium acetate",
    }
    assert ingredients["Beef Extract"]["term"] == {
        "id": "FOODON:03302088",
        "label": "Beef extract",
    }
    assert ingredients["Proteose Peptone #3"]["term"] == {
        "id": "MICRO:0000180",
        "label": "Proteose Peptone",
    }
    assert ingredients["Yeast Extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }


def test_repair_keeps_ambiguous_components_unmapped(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module.TARGET_M2250),
        repair_module.TARGET_M2250,
    )
    ingredients = _by_name(repaired["ingredients"])

    for name in ("Sorbitan Monooleate", "Ammonium Citrate"):
        assert "term" not in ingredients[name]
        assert "mediaingredientmech_chebi_term" not in ingredients[name]
        assert "retained without" in ingredients[name]["notes"]


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(target), target)

        assert scorer_module.score_record(repaired) == (0, [])
        assert scorer_module.score_parsed([(str(target.path), repaired)]) == []
        assert repaired["data_quality_flags"] == [
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    target = repair_module.TARGET_M2249
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice["references"] == [
        {"reference": url} for url in target.reference_urls
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
    assert "removed the duplicate Lactobacilli MRS wrapper" in matching_events[0]["notes"]


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGET_M2250
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.expected_id):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGET_M2250
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=target.expected_media_term):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGET_M2249
    doc = _doc(target)
    doc["ingredients"][0] = _ingredient("Water", "1000", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGET_M2249
    doc = _doc(target)
    doc["solutions"] = [
        {
            "preferred_term": "Tween solution",
            "concentration": {"value": "1", "unit": "G_PER_L"},
            "composition": [],
        }
    ]

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_repair_contract(
    repair_module,
) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == target.expected_id
        assert repair_module._source_term_id(doc) == target.expected_media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in (
            target.imported_signature,
            target.final_signature,
        )
        assert "solutions" not in doc
