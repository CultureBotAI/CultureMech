from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_51_sphaerotilus_score15.py"
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
    return _load_script(SCRIPT, "repair_dsmz_51_sphaerotilus_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_51_sphaerotilus")


def _doc(repair_module, target) -> dict:
    return {
        "id": target.expected_id,
        "name": "sphaerotilus_medium",
        "original_name": "SPHAEROTILUS MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "DSMZ Medium 51",
            "term": {
                "id": target.expected_source_term,
                "label": "SPHAEROTILUS MEDIUM",
            },
        },
        "notes": "DSMZ 51",
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


def test_repair_adds_missing_water_and_normalizes_beef_extract(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert set(ingredients) == {
        "Beef extract (Lab Lemco, Oxoid)",
        "Agar",
        "Distilled water",
    }
    beef_extract = ingredients["Beef extract (Lab Lemco, Oxoid)"]
    assert beef_extract["concentration"] == {"value": "5.0", "unit": "G_PER_L"}
    assert beef_extract["term"] == {
        "id": "FOODON:03302088",
        "label": "beef extract",
    }
    assert "mediaingredientmech_chebi_term" not in beef_extract


def test_repair_keeps_optional_agar_and_adds_distilled_water(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Agar"]["concentration"] == {
        "value": "15.0",
        "unit": "G_PER_L",
    }
    assert ingredients["Agar"]["term"] == {"id": "CHEBI:2509", "label": "agar"}
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Distilled water"]["term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }


def test_repair_adds_ph_preparation_steps_and_sterilization(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["ph_value"] == 7.0
    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert repaired["preparation_steps"] == [
        {"step_number": 1, "action": "ADJUST_PH", "description": "Adjust pH to 7.0."},
        {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Prepare sterile agar slants by autoclaving.",
        },
        {
            "step_number": 3,
            "action": "COOL",
            "description": "Cool the slants in a sloping position.",
        },
        {
            "step_number": 4,
            "action": "MIX",
            "description": (
                "Cover solid slants with 2 ml sterile tap water, inoculate into the "
                "covering tap water, and incubate at 20 to 25 C for at least 48 h."
            ),
        },
    ]


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert repaired["references"] == [{"reference": repair_module.DSMZ_51}]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.DSMZ_51,
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
    doc["ingredients"][0]["concentration"]["value"] = "6"

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
