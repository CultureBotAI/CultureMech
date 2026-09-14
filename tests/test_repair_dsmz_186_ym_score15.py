from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_186_ym_score15.py"
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
    return _load_script(SCRIPT, "repair_dsmz_186_ym_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_186_ym")


def _doc(repair_module, target) -> dict:
    return {
        "id": target.expected_id,
        "name": "universal_medium_for_yeasts_ym",
        "original_name": "UNIVERSAL MEDIUM FOR YEASTS (YM)",
        "category": "fungal" if target.path == repair_module.PARENT_PATH else "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 6.2,
        "media_term": {
            "preferred_term": "DSMZ Medium 186",
            "term": {
                "id": target.expected_source_term,
                "label": "UNIVERSAL MEDIUM FOR YEASTS (YM)",
            },
        },
        "notes": "DSMZ Medium 186",
        "ingredients": [
            {
                "preferred_term": preferred_term,
                "concentration": {"value": value, "unit": unit},
            }
            for preferred_term, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "data_quality_flags": ["has_unmapped_ingredients"],
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


def test_repair_reconstructs_dsmz_medium_186_components(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert list(ingredients) == [
        "Yeast extract",
        "Malt extract",
        "Soy peptone",
        "Glucose",
        "Agar",
        "Distilled water",
    ]
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Malt extract"]["term"] == {
        "id": "FOODON:03301056",
        "label": "malt extract",
    }
    assert ingredients["Soy peptone"]["term"] == {
        "id": "FOODON:03315720",
        "label": "Soy peptone",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }


def test_repair_preserves_glucose_and_marks_agar_role(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Glucose"]["concentration"] == {
        "value": "10.0",
        "unit": "G_PER_L",
    }
    assert ingredients["Glucose"]["term"] == {"id": "CHEBI:17234", "label": "glucose"}
    assert ingredients["Agar"]["term"] == {"id": "CHEBI:2509", "label": "agar"}
    assert ingredients["Agar"]["physicochemical_roles"] == ["SOLIDIFYING_AGENT"]


def test_repair_removes_unlisted_ph_and_preparation_steps(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["preparation_steps"] = [{"step_number": 1, "action": "AUTOCLAVE", "description": "stale"}]

    repaired = repair_module.repair_record(doc, target)

    assert "ph_value" not in repaired
    assert "ph_range" not in repaired
    assert "preparation_steps" not in repaired
    assert "sterilization" not in repaired


def test_repair_adds_duplicate_links(repair_module) -> None:
    parent = repair_module.repair_record(
        _doc(repair_module, repair_module.TARGETS[0]),
        repair_module.TARGETS[0],
    )
    child = repair_module.repair_record(
        _doc(repair_module, repair_module.TARGETS[1]),
        repair_module.TARGETS[1],
    )

    assert parent["variant_children"] == [repair_module.PARENT_VARIANT_CHILD]
    assert "parent_media" not in parent
    assert child["parent_media"] == repair_module.CHILD_PARENT
    assert child["variant_relationship"] == "SOURCE_DUPLICATE"
    assert "variant_children" not in child


def test_repair_updates_stale_duplicate_child(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["variant_children"] = [
        {
            "path": repair_module.PARENT_VARIANT_CHILD["path"],
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:004210",
            "name": "stale",
            "notes": "stale",
        }
    ]

    repaired = repair_module.repair_record(doc, target)

    assert repaired["variant_children"] == [repair_module.PARENT_VARIANT_CHILD]


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert repaired["references"] == [{"reference": repair_module.DSMZ_186}]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.DSMZ_186,
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
    doc["ingredients"][0]["concentration"]["value"] = "3.1"

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
