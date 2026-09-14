from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm188_m1428_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
sys.path.insert(0, str(REPO / "src"))
from culturemech.ingredients import resolve_ingredient  # noqa: E402


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_jcm188_m1428")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm188_m1428")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _recipe_doc(spec, signature) -> dict:
    return {
        "id": spec.expected_id,
        "name": spec.path.stem,
        "original_name": spec.path.stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [_ingredient(name, value, unit) for name, value, unit in signature],
        "media_term": {
            "preferred_term": spec.expected_media_term,
            "term": {"id": spec.expected_media_term, "label": spec.path.stem},
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _solution_doc(repair_module, signature) -> dict:
    return {
        "id": repair_module.EXPECTED_SOLUTION_ID,
        "preferred_term": "Main sol. J188",
        "term": {
            "id": repair_module.EXPECTED_JCM_SOLUTION_TERM,
            "label": "Main sol. J188",
        },
        "composition": [_ingredient(name, value, unit) for name, value, unit in signature],
        "ingredients": [_ingredient("See source for composition", "variable", "VARIABLE")],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_formula_and_exits_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    docs = [
        repair_module.repair_recipe(
            _recipe_doc(spec, spec.legacy_signature),
            spec,
        )
        for spec in repair_module.SPECS
    ]

    assert [doc["ph_value"] for doc in docs] == [6.0, 6.0, 5.6]
    for doc in docs:
        assert repair_module._signature(doc["ingredients"], "ingredients") == (
            repair_module.FINAL_SIGNATURE
        )
        assert scorer_module.score_record(doc) == (0, [])

    assert (
        scorer_module.score_parsed(
            [
                (str(repair_module.JCM_PATH), docs[0]),
                (str(repair_module.TOGO_JCM_PATH), docs[1]),
                (str(repair_module.TOGO_NBRC_PATH), docs[2]),
            ]
        )
        == []
    )


def test_repair_adds_groundings_and_resolvable_ingredients(repair_module) -> None:
    repaired = repair_module.repair_recipe(
        _recipe_doc(repair_module.TOGO_NBRC_SPEC, repair_module.TOGO_LEGACY_SIGNATURE),
        repair_module.TOGO_NBRC_SPEC,
    )

    ingredients = _by_name(repaired["ingredients"])
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "peptone",
    }
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Malt extract"]["term"] == {
        "id": "FOODON:03301056",
        "label": "malt extract",
    }
    assert ingredients["Olive oil"]["term"] == {
        "id": "CHEBI:752944",
        "label": "olive oil",
    }
    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    for ingredient in repaired["ingredients"]:
        assert resolve_ingredient(ingredient).is_resolved


def test_repair_rewrites_variant_links(repair_module) -> None:
    parent = repair_module.repair_recipe(
        _recipe_doc(repair_module.JCM_SPEC, repair_module.JCM_LEGACY_SIGNATURE),
        repair_module.JCM_SPEC,
    )
    togo_jcm = repair_module.repair_recipe(
        _recipe_doc(repair_module.TOGO_JCM_SPEC, repair_module.TOGO_LEGACY_SIGNATURE),
        repair_module.TOGO_JCM_SPEC,
    )
    togo_nbrc = repair_module.repair_recipe(
        _recipe_doc(repair_module.TOGO_NBRC_SPEC, repair_module.TOGO_LEGACY_SIGNATURE),
        repair_module.TOGO_NBRC_SPEC,
    )

    assert parent["variant_children"] == [
        {
            "path": "data/normalized_yaml/bacterial/togo_medium_m181.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:008391",
            "name": "togo_medium_m181",
            "notes": repair_module.TOGO_JCM_SPEC.parent_notes,
        },
        {
            "path": "data/normalized_yaml/bacterial/togo_medium_m1428.yaml",
            "relationship": "PH_VARIANT",
            "id": "CultureMech:007966",
            "name": "togo_medium_m1428",
            "notes": repair_module.TOGO_NBRC_SPEC.parent_notes,
        },
    ]
    assert "variant_children" not in togo_jcm
    assert togo_jcm["parent_media"]["id"] == "CultureMech:002549"
    assert togo_jcm["variant_relationship"] == "SOURCE_DUPLICATE"
    assert togo_nbrc["parent_media"]["id"] == "CultureMech:002549"
    assert togo_nbrc["variant_relationship"] == "PH_VARIANT"


def test_solution_repair_removes_placeholder_and_corrects_water(repair_module) -> None:
    repaired = repair_module.repair_solution(
        _solution_doc(repair_module, repair_module.SOLUTION_LEGACY_SIGNATURE)
    )
    components = _by_name(repaired["composition"])

    assert "ingredients" not in repaired
    assert repair_module._signature(repaired["composition"], "composition") == (
        repair_module.FINAL_SIGNATURE
    )
    assert components["Distilled water"]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    for component in repaired["composition"]:
        assert resolve_ingredient(component).is_resolved


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_recipe(
        _recipe_doc(repair_module.TOGO_NBRC_SPEC, repair_module.TOGO_LEGACY_SIGNATURE),
        repair_module.TOGO_NBRC_SPEC,
    )
    twice = repair_module.repair_recipe(once, repair_module.TOGO_NBRC_SPEC)

    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.TOGO_NBRC_SPEC.references
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": "; ".join(repair_module.TOGO_NBRC_SPEC.references),
            "notes": (
                "Curated TOGO:M1428 from TOGO M1428 / NBRC Medium 103; corrected "
                "the imported distilled-water unit, added pH, grounded all "
                "disclosed components, and repaired the JCM Medium 188 "
                "source-duplicate / pH-variant relationships."
            ),
        }
    ]


def test_plan_repairs_all_jcm188_family_records(repair_module) -> None:
    expected = {}
    for spec in repair_module.SPECS:
        path = repair_module.NORMALIZED / spec.path
        expected[path] = repair_module.repair_recipe(
            yaml.safe_load(path.read_text(encoding="utf-8")),
            spec,
        )
    solution_path = repair_module.NORMALIZED / repair_module.JCM_SOLUTION_PATH
    expected[solution_path] = repair_module.repair_solution(
        yaml.safe_load(solution_path.read_text(encoding="utf-8"))
    )

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _recipe_doc(repair_module.JCM_SPEC, repair_module.JCM_LEGACY_SIGNATURE)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_JCM_ID):
        repair_module.repair_recipe(doc, repair_module.JCM_SPEC)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _recipe_doc(repair_module.TOGO_NBRC_SPEC, repair_module.TOGO_LEGACY_SIGNATURE)
    doc["media_term"]["term"]["id"] = "TOGO:M1427"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_TOGO_NBRC_MEDIA_TERM):
        repair_module.repair_recipe(doc, repair_module.TOGO_NBRC_SPEC)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _recipe_doc(repair_module.TOGO_JCM_SPEC, repair_module.TOGO_LEGACY_SIGNATURE)
    doc["ingredients"][1] = _ingredient("Beef extract", "3", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_recipe(doc, repair_module.TOGO_JCM_SPEC)


def test_corpus_records_match_repair_contract(repair_module) -> None:
    for spec in repair_module.SPECS:
        path = repair_module.NORMALIZED / spec.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == spec.expected_id
        assert repair_module._source_term_id(doc) == spec.expected_media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in {
            spec.legacy_signature,
            repair_module.FINAL_SIGNATURE,
        }

    solution_path = repair_module.NORMALIZED / repair_module.JCM_SOLUTION_PATH
    solution = yaml.safe_load(solution_path.read_text(encoding="utf-8"))
    assert solution["id"] == repair_module.EXPECTED_SOLUTION_ID
    assert repair_module._record_term_id(solution) == (repair_module.EXPECTED_JCM_SOLUTION_TERM)
    assert repair_module._signature(solution["composition"], "composition") in {
        repair_module.SOLUTION_LEGACY_SIGNATURE,
        repair_module.FINAL_SIGNATURE,
    }
