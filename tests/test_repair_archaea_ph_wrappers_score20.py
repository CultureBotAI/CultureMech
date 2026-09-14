from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_archaea_ph_wrappers_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_archaea_ph_wrappers_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_archaea_ph_wrappers")


def _media_term(term_id: str) -> dict:
    return {"term": {"id": term_id}}


def _child_doc(repair, path: str, parent_solution_name: str) -> dict:
    return {
        "id": repair.EXPECTED_IDS[path],
        "name": "child",
        "category": "archaea",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": "H2SO4",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            }
        ],
        "media_term": _media_term(repair.EXPECTED_SOURCE_TERMS[path]),
        "solutions": [
            {
                "preferred_term": parent_solution_name,
                "composition": [],
                "concentration": {"value": "1", "unit": "G_PER_L"},
                "name": "Unknown solution",
            }
        ],
        "curation_history": [],
    }


def _parent_doc(repair, path: str) -> dict:
    return {
        "id": repair.EXPECTED_IDS[path],
        "name": "parent",
        "category": "archaea",
        "media_term": _media_term(repair.EXPECTED_SOURCE_TERMS[path]),
        "variant_children": [
            {
                "path": "data/normalized_yaml/archaea/existing_variant.yaml",
                "relationship": "PH_VARIANT",
                "id": "CultureMech:999999",
                "name": "existing_variant",
            }
        ],
        "curation_history": [],
    }


def _write_tree(repair, root: Path) -> None:
    docs = {
        repair.M165: _child_doc(
            repair,
            repair.M165,
            repair.TARGETS[0].parent_solution_name,
        ),
        repair.M345: _child_doc(
            repair,
            repair.M345,
            repair.TARGETS[1].parent_solution_name,
        ),
        repair.M156: _parent_doc(repair, repair.M156),
        repair.M273: _parent_doc(repair, repair.M273),
    }
    for relative_path, doc in docs.items():
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")


def test_repair_m165_models_sulfolobus_ph_variant(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_child(
        _child_doc(
            repair_module,
            repair_module.M165,
            repair_module.TARGETS[0].parent_solution_name,
        ),
        repair_module.TARGETS[0],
        _parent_doc(repair_module, repair_module.M156),
    )

    assert repaired["ph_value"] == 3.5
    assert repaired["ingredients"] == [
        {
            "preferred_term": "H2SO4",
            "concentration": {"value": "10 N", "unit": "VARIABLE"},
            "source": "TOGO Medium M165",
            "notes": (
                "TOGO lists 10 N H2SO4 for final pH adjustment. Normality "
                "is retained verbatim because the schema has no normality unit."
            ),
            "term": {"id": "CHEBI:26836", "label": "sulfuric acid"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:26836",
                "label": "sulfuric acid",
            },
        }
    ]
    assert repaired["solutions"] == [
        {
            "preferred_term": "Sulfolobus medium (see Medium [M156])",
            "composition": [],
            "concentration": {"value": "1", "unit": "L"},
            "notes": (
                "TOGO M165 uses one liter of TOGO M156 Sulfolobus Medium as "
                "the base medium."
            ),
            "culturemech_term": {
                "id": repair_module.EXPECTED_IDS[repair_module.M156],
                "label": "Sulfolobus Medium",
            },
        }
    ]
    assert repaired["parent_media"] == {
        "path": f"data/normalized_yaml/{repair_module.M156}",
        "relationship": repair_module.RELATIONSHIP,
        "id": repair_module.EXPECTED_IDS[repair_module.M156],
        "name": "parent",
        "notes": repair_module.TARGETS[0].parent_notes,
    }
    assert repaired["variant_relationship"] == repair_module.RELATIONSHIP
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_m345_models_thermococcus_reduction_readjustment(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_child(
        _child_doc(
            repair_module,
            repair_module.M345,
            repair_module.TARGETS[1].parent_solution_name,
        ),
        repair_module.TARGETS[1],
        _parent_doc(repair_module, repair_module.M273),
    )

    assert repaired["ph_value"] == 6.0
    assert repaired["ingredients"][0]["concentration"] == {
        "value": "1 N",
        "unit": "VARIABLE",
    }
    assert repaired["solutions"][0]["culturemech_term"] == {
        "id": repair_module.EXPECTED_IDS[repair_module.M273],
        "label": "Thermococcus Medium",
    }
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": repair_module.TARGETS[1].preparation_description,
        }
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_plan_repairs_adds_reciprocal_links_and_preserves_children(
    repair_module,
    tmp_path: Path,
) -> None:
    _write_tree(repair_module, tmp_path)

    plans = repair_module.plan_repairs(tmp_path)

    assert set(plans) == {
        tmp_path / repair_module.M165,
        tmp_path / repair_module.M345,
        tmp_path / repair_module.M156,
        tmp_path / repair_module.M273,
    }

    m156_children = {
        row["path"]
        for row in plans[tmp_path / repair_module.M156]["variant_children"]
    }
    m273_children = {
        row["path"]
        for row in plans[tmp_path / repair_module.M273]["variant_children"]
    }

    assert m156_children == {
        "data/normalized_yaml/archaea/existing_variant.yaml",
        f"data/normalized_yaml/{repair_module.M165}",
    }
    assert m273_children == {
        "data/normalized_yaml/archaea/existing_variant.yaml",
        f"data/normalized_yaml/{repair_module.M345}",
    }


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    _write_tree(repair_module, tmp_path)

    first = repair_module.plan_repairs(tmp_path)
    for path, doc in first.items():
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    second = repair_module.plan_repairs(tmp_path)

    assert second == first


def test_repair_child_rejects_wrong_source(repair_module) -> None:
    doc = _child_doc(
        repair_module,
        repair_module.M165,
        repair_module.TARGETS[0].parent_solution_name,
    )
    doc["media_term"]["term"]["id"] = "TOGO:M156"

    with pytest.raises(ValueError, match="expected 'TOGO:M165'"):
        repair_module.repair_child(
            doc,
            repair_module.TARGETS[0],
            _parent_doc(repair_module, repair_module.M156),
        )


def test_repair_child_rejects_missing_parent_solution(repair_module) -> None:
    doc = _child_doc(
        repair_module,
        repair_module.M165,
        repair_module.TARGETS[0].parent_solution_name,
    )
    doc["solutions"] = []

    with pytest.raises(ValueError, match="missing Sulfolobus Medium"):
        repair_module.repair_child(
            doc,
            repair_module.TARGETS[0],
            _parent_doc(repair_module, repair_module.M156),
        )


def test_repair_child_rejects_missing_h2so4(repair_module) -> None:
    doc = _child_doc(
        repair_module,
        repair_module.M165,
        repair_module.TARGETS[0].parent_solution_name,
    )
    doc["ingredients"] = []

    with pytest.raises(ValueError, match="expected exactly one H2SO4"):
        repair_module.repair_child(
            doc,
            repair_module.TARGETS[0],
            _parent_doc(repair_module, repair_module.M156),
        )


def test_target_records_have_expected_sources(repair_module) -> None:
    for path in repair_module.EXPECTED_IDS:
        doc = yaml.safe_load(
            (repair_module.NORMALIZED / path).read_text(encoding="utf-8")
        )

        assert doc["id"] == repair_module.EXPECTED_IDS[path]
        assert (
            doc["media_term"]["term"]["id"]
            == repair_module.EXPECTED_SOURCE_TERMS[path]
        )
