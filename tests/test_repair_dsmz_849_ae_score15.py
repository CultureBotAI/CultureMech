from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_849_ae_score15.py"
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
    return _load_script(SCRIPT, "repair_dsmz_849_ae_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_849_ae")


def _doc(repair_module, target) -> dict:
    return {
        "id": target.expected_id,
        "name": "ae_medium",
        "original_name": "AE MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "DSMZ Medium 849",
            "term": {
                "id": target.expected_source_term,
                "label": "AE MEDIUM",
            },
        },
        "notes": "DSMZ 849",
        "ingredients": [
            {
                "preferred_term": preferred_term,
                "concentration": {"value": value, "unit": unit},
            }
            for preferred_term, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_leaves_review_ranking(repair_module, scorer_module) -> None:
    records = [
        (target.path, repair_module.repair_record(_doc(repair_module, target), target))
        for target in repair_module.TARGETS
    ]

    assert scorer_module.score_parsed(records) == []


def test_repair_adds_water_and_normalizes_concentrations(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert set(ingredients) == {
        "Glucose",
        "Yeast extract",
        "Peptone",
        "Absolute ethanol",
        "Glacial acetic acid",
        "Agar",
        "Distilled water",
    }
    assert ingredients["Absolute ethanol"]["concentration"] == {
        "value": "30.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Glacial acetic acid"]["concentration"] == {
        "value": "30.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "940.0",
        "unit": "ML_PER_L",
    }


def test_repair_grounds_organic_and_undefined_components(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Peptone"]["term"] == {"id": "MICRO:0000178", "label": "peptone"}
    assert ingredients["Absolute ethanol"]["term"] == {
        "id": "CHEBI:16236",
        "label": "ethanol",
    }
    assert ingredients["Glacial acetic acid"]["term"] == {
        "id": "CHEBI:15366",
        "label": "acetic acid",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients["Yeast extract"]
    assert "mediaingredientmech_chebi_term" not in ingredients["Peptone"]


def test_repair_adds_sterilization_steps_without_adding_ph(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert "ph_value" not in repaired
    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": (
                "Autoclave the medium without the addition of glacial acetic acid "
                "and absolute ethanol."
            ),
        },
        {
            "step_number": 2,
            "action": "FILTER_STERILIZE",
            "description": (
                "Sterilize glacial acetic acid and absolute ethanol by filtration "
                "through Teflon filters or by autoclaving in completely closed "
                "screw-cap glass bottles sealed with Teflon-coated septa."
            ),
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": "Add sterile glacial acetic acid and absolute ethanol.",
        },
        {
            "step_number": 4,
            "action": "MIX",
            "description": "Incubate plates in sealed containers to keep humidity high above 90%.",
        },
    ]


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert repaired["references"] == [{"reference": repair_module.DSMZ_849}]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.DSMZ_849,
            "notes": repair_module.NOTES,
        }
    ]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    for target in repair_module.TARGETS:
        path = tmp_path / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(_doc(repair_module, target), sort_keys=False),
            encoding="utf-8",
        )

    first = repair_module.plan_repairs(tmp_path)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(tmp_path)

    assert {
        path.relative_to(tmp_path): repair_module.dump_record(doc)
        for path, doc in second.items()
    } == {
        path.relative_to(tmp_path): repair_module.dump_record(doc)
        for path, doc in first.items()
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.expected_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:wrong"

    with pytest.raises(ValueError, match=target.expected_source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_component_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"][3]["concentration"]["unit"] = "ML_PER_L"

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_reviewed_input(repair_module) -> None:
    for target in repair_module.TARGETS:
        doc = yaml.safe_load(
            (repair_module.NORMALIZED / target.path).read_text(encoding="utf-8")
        )

        assert doc["id"] == target.expected_id
        assert (
            repair_module._signature(doc["ingredients"], "ingredients"),
            repair_module._signature(doc.get("solutions"), "solutions"),
        ) in {
            (repair_module.IMPORTED_INGREDIENT_SIGNATURE, ()),
            (
                repair_module.FINAL_INGREDIENT_SIGNATURE,
                repair_module.FINAL_SOLUTION_SIGNATURE,
            ),
        }
