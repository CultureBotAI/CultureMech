from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_sparse_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_sparse_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_sparse")


def _doc(repair, update) -> dict:
    return {
        "id": repair.EXPECTED_IDS[update.path],
        "name": Path(update.path).stem,
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": ingredient["preferred_term"].lower(),
                "concentration": {"value": "1", "unit": "G_PER_L"},
                "term": {"id": "CHEBI:2509", "label": "agar"},
                "mediaingredientmech_chebi_term": {
                    "id": "CHEBI:2509",
                    "label": "agar",
                },
            }
            for ingredient in update.recipe["ingredients"]
        ],
        "media_term": {
            "preferred_term": update.reference_urls[0],
            "term": {"id": repair.EXPECTED_SOURCE_TERMS[update.path]},
        },
        "data_quality_flags": ["incomplete_composition", "needs_manual_curation"],
        "curation_history": [],
    }


def _target(repair, path: str):
    return repair.UPDATE_BY_PATH[path]


def _write_minimal_tree(repair, root: Path) -> None:
    for update in repair.UPDATES:
        path = root / update.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(_doc(repair, update), sort_keys=False),
            encoding="utf-8",
        )


def test_all_reviewed_targets_are_guarded(repair_module) -> None:
    assert {update.path for update in repair_module.UPDATES} == {
        repair_module.M250_ME_AGAR,
        repair_module.M530_THIOGLYCOLLATE,
        repair_module.M2510_SHEEP_BLOOD,
        repair_module.M2684_GAM_BROTH,
        repair_module.M2858_CHOCOLATE,
        repair_module.M2859_BCYE,
    }
    assert set(repair_module.EXPECTED_IDS) == {
        update.path for update in repair_module.UPDATES
    }
    assert set(repair_module.EXPECTED_SOURCE_TERMS) == set(
        repair_module.EXPECTED_IDS
    )


def test_m250_normalizes_liter_water_and_autoclave(
    repair_module,
    scorer_module,
) -> None:
    update = _target(repair_module, repair_module.M250_ME_AGAR)

    repaired = repair_module.repair_record(_doc(repair_module, update), update)

    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ingredients"] == [
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "source": "TOGO M250",
            "notes": "TOGO M250 lists 1.0 L distilled water.",
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:15377",
                "label": "water",
            },
        },
        {
            "preferred_term": "Malt extract agar (Oxoid)",
            "concentration": {"value": "50", "unit": "G_PER_L"},
            "source": "TOGO M250",
            "notes": "TOGO M250 lists 50 g/L Malt extract agar from Oxoid.",
        },
    ]
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 115 C for 10 min.",
        }
    ]
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_m530_preserves_semisolid_thioglycollate_product(
    repair_module,
    scorer_module,
) -> None:
    update = _target(repair_module, repair_module.M530_THIOGLYCOLLATE)

    repaired = repair_module.repair_record(_doc(repair_module, update), update)

    assert repaired["physical_state"] == "SEMISOLID"
    assert repaired["ingredients"][1] == {
        "preferred_term": "Thioglycollate medium (Sigma)",
        "concentration": {"value": "29.8", "unit": "G_PER_L"},
        "source": "TOGO M530",
        "notes": "TOGO M530 lists 29.8 g/L Thioglycollate medium from Sigma.",
    }
    assert "preparation_steps" not in repaired
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_m2858_captures_temperature_and_five_percent_co2(
    repair_module,
    scorer_module,
) -> None:
    update = _target(repair_module, repair_module.M2858_CHOCOLATE)

    repaired = repair_module.repair_record(_doc(repair_module, update), update)

    assert repaired["temperature_value"] == 37.0
    assert repaired["ingredients"][0] == {
        "preferred_term": "Chocolate agar",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": "TOGO M2858",
        "notes": "TOGO M2858 names chocolate agar but does not state an amount.",
    }
    assert repaired["ingredients"][1] == {
        "preferred_term": "CO2",
        "concentration": {"value": "5", "unit": "PERCENT_V_V"},
        "source": "TOGO M2858",
        "notes": "TOGO M2858 records propagation in 5% CO2.",
        "term": {"id": "CHEBI:16526", "label": "carbon dioxide"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:16526",
            "label": "carbon dioxide",
        },
    }
    assert scorer_module.score_record(repaired) == (0, [])


def test_m2684_normalizes_liter_water_and_temperature(
    repair_module,
    scorer_module,
) -> None:
    update = _target(repair_module, repair_module.M2684_GAM_BROTH)

    repaired = repair_module.repair_record(_doc(repair_module, update), update)

    assert repaired["physical_state"] == "LIQUID"
    assert repaired["temperature_value"] == 37.0
    assert repaired["ingredients"] == [
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "source": "TOGO M2684",
            "notes": "TOGO M2684 lists 1.0 L distilled water.",
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:15377",
                "label": "water",
            },
        },
        {
            "preferred_term": "GAM broth (Nissui)",
            "concentration": {"value": "59", "unit": "G_PER_L"},
            "source": "TOGO M2684",
            "notes": "TOGO M2684 lists 59 g/L GAM broth from Nissui.",
        },
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_m2859_drops_false_agar_grounding_but_stays_opaque(
    repair_module,
    scorer_module,
) -> None:
    update = _target(repair_module, repair_module.M2859_BCYE)

    repaired = repair_module.repair_record(_doc(repair_module, update), update)

    assert repaired["temperature_value"] == 37.0
    assert repaired["ingredients"] == [
        {
            "preferred_term": "BCYE agar",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "source": "TOGO M2859",
            "notes": (
                "TOGO M2859 lists one liter of BCYE agar without spelling out "
                "the commercial product or formulation."
            ),
        }
    ]
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]
    assert scorer_module.score_record(repaired) == (
        20,
        ["no composition component is grounded"],
    )


def test_m2510_fixes_co2_unit_and_temperature(
    repair_module,
    scorer_module,
) -> None:
    update = _target(repair_module, repair_module.M2510_SHEEP_BLOOD)

    repaired = repair_module.repair_record(_doc(repair_module, update), update)

    assert repaired["temperature_value"] == 37.0
    assert repaired["ingredients"] == [
        {
            "preferred_term": "sheep blood agar",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": "TOGO M2510",
            "notes": "TOGO M2510 names sheep blood agar but does not state an amount.",
        },
        {
            "preferred_term": "CO2",
            "concentration": {"value": "5", "unit": "PERCENT_V_V"},
            "source": "TOGO M2510",
            "notes": "TOGO M2510 records propagation in 5% CO2.",
            "term": {"id": "CHEBI:16526", "label": "carbon dioxide"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:16526",
                "label": "carbon dioxide",
            },
        },
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_adds_review_metadata_once(repair_module) -> None:
    update = _target(repair_module, repair_module.M2858_CHOCOLATE)

    once = repair_module.repair_record(_doc(repair_module, update), update)
    twice = repair_module.repair_record(once, update)

    assert twice["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert twice["references"] == [{"reference": repair_module.TOGO_M2858}]

    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == repair_module.TOGO_M2858


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair_module, root)

    first = repair_module.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in second.items()
    } == {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in first.items()
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    update = _target(repair_module, repair_module.M250_ME_AGAR)
    doc = _doc(repair_module, update)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:009081'"):
        repair_module.repair_record(doc, update)


def test_repair_rejects_wrong_source(repair_module) -> None:
    update = _target(repair_module, repair_module.M2859_BCYE)
    doc = _doc(repair_module, update)
    doc["media_term"]["term"]["id"] = "TOGO:M111"

    with pytest.raises(ValueError, match="expected 'TOGO:M2859'"):
        repair_module.repair_record(doc, update)


def test_repair_rejects_wrong_components(repair_module) -> None:
    update = _target(repair_module, repair_module.M2858_CHOCOLATE)
    doc = _doc(repair_module, update)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="expected"):
        repair_module.repair_record(doc, update)
