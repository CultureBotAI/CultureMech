from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_189_oat_flake_score15.py"
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
    return _load_script(SCRIPT, "repair_dsmz_189_oat_flake_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_189_oat_flake")


def _doc(repair_module, target) -> dict:
    doc = {
        "id": target.expected_id,
        "name": "oat_flake_medium",
        "original_name": "OAT FLAKE MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 6.0,
        "media_term": {
            "preferred_term": "DSMZ Medium 189",
            "term": {
                "id": target.expected_source_term,
                "label": "OAT FLAKE MEDIUM",
            },
        },
        "notes": "DSMZ 189",
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

    if target.path == "bacterial/oat_flake_medium.yaml":
        doc["variant_children"] = [
            {
                "path": "data/normalized_yaml/bacterial/KOMODO_189_OAT_FLAKE_medium.yaml",
                "relationship": "SOURCE_DUPLICATE",
                "id": "CultureMech:004213",
                "name": "oat_flake_medium",
                "notes": "stale pH note",
            }
        ]
    else:
        doc["parent_media"] = {
            "path": "data/normalized_yaml/bacterial/oat_flake_medium.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:001281",
            "name": "oat_flake_medium",
            "notes": "stale pH note",
        }
        doc["variant_relationship"] = "SOURCE_DUPLICATE"

    return doc


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_leaves_review_ranking(repair_module, scorer_module) -> None:
    records = [
        (target.path, repair_module.repair_record(_doc(repair_module, target), target))
        for target in repair_module.TARGETS
    ]

    assert scorer_module.score_parsed(records) == []


def test_repair_adds_missing_water_and_normalizes_agar(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert set(ingredients) == {"Oat flakes", "Agar", "Distilled water"}
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


def test_repair_leaves_oat_flakes_unmapped_and_removes_ph(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Oat flakes"]["concentration"] == {
        "value": "30.0",
        "unit": "G_PER_L",
    }
    assert "term" not in ingredients["Oat flakes"]
    assert "mediaingredientmech_chebi_term" not in ingredients["Oat flakes"]
    assert "ph_value" not in repaired


def test_repair_updates_preparation_steps(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "HEAT",
            "description": "Boil oat flakes in water for 10 min, fill to 1 L, and add agar.",
        },
        {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave for 20 min at 121 C, then shake before pouring.",
        },
    ]


def test_repair_updates_duplicate_notes(repair_module) -> None:
    parent = repair_module.repair_record(
        _doc(repair_module, repair_module.TARGETS[0]),
        repair_module.TARGETS[0],
    )
    child = repair_module.repair_record(
        _doc(repair_module, repair_module.TARGETS[1]),
        repair_module.TARGETS[1],
    )

    assert parent["variant_children"][0]["notes"] == repair_module.PARENT_VARIANT_NOTE
    assert child["parent_media"]["notes"] == repair_module.CHILD_PARENT_NOTE


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [{"reference": repair_module.DSMZ_189}]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.DSMZ_189,
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
        path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in first.items()}


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
    doc["ingredients"][0]["concentration"]["value"] = "30.1"

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_reviewed_input(repair_module) -> None:
    for target in repair_module.TARGETS:
        doc = yaml.safe_load((repair_module.NORMALIZED / target.path).read_text(encoding="utf-8"))

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
