from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_318_trace_stock_score15.py"
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
    return _load_script(SCRIPT, "repair_dsmz_318_trace_stock_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_318_trace_stock")


def _doc(repair_module, target) -> dict:
    return {
        "id": target.expected_id,
        "name": "trace_element_solution_medium_318",
        "original_name": "Trace element solution (medium 318)",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.5,
        "media_term": {
            "preferred_term": "KOMODO Medium 3073",
            "term": {
                "id": target.expected_source_term,
                "label": "Trace element solution (medium 318)",
            },
        },
        "notes": "pH buffer: KOH",
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


def test_repair_expands_trace_element_stock(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert len(ingredients) == 15
    assert ingredients["Nitrilotriacetic acid (NTA)"]["concentration"] == {
        "value": "12.80",
        "unit": "G_PER_L",
    }
    assert ingredients["FeCl2 x 4 H2O"]["term"] == {
        "id": "CHEBI:86249",
        "label": "iron dichloride tetrahydrate",
    }
    assert ingredients["Na2WO4 x 2 H2O"]["concentration"] == {
        "value": "0.04",
        "unit": "G_PER_L",
    }


def test_repair_adds_water_and_keeps_koh_variable(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.00",
        "unit": "ML_PER_L",
    }
    assert ingredients["Distilled water"]["term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["KOH"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert ingredients["KOH"]["term"] == {
        "id": "CHEBI:32035",
        "label": "potassium hydroxide",
    }


def test_repair_updates_ph_and_preparation_steps(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["ph_value"] == 6.5
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Dissolve NTA in 200 ml distilled water and adjust to pH 6.5 with KOH."
            ),
        },
        {
            "step_number": 2,
            "action": "MIX",
            "description": (
                "Dissolve the mineral salts, adjust to pH 6.5 with KOH, and make up "
                "to 1000.00 ml."
            ),
        },
    ]


def test_repair_normalizes_importer_notes(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["notes"] == repair_module.SOURCE_NOTES[target.path]
    assert "mediadive.medium:2118" not in repaired["notes"]


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert repaired["references"] == [{"reference": repair_module.DSMZ_318}]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.DSMZ_318,
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
    doc["media_term"]["term"]["id"] = "komodo.medium:wrong"

    with pytest.raises(ValueError, match=target.expected_source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_component_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"][0]["concentration"]["value"] = "1.0"

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
