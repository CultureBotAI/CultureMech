from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_archaeoglobus_mcr_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_archaeoglobus_mcr_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_archaeoglobus_mcr")


def _media_term(term_id: str) -> dict:
    return {"term": {"id": term_id}}


def _child_doc(repair, path: str) -> dict:
    return {
        "id": repair.EXPECTED_IDS[path],
        "name": "archaeoglobus_mcr_medium",
        "category": "archaea",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": "Na2SO4",
                "concentration": {"value": "2.8", "unit": "G_PER_L"},
            }
        ],
        "media_term": _media_term(repair.EXPECTED_SOURCE_TERMS[path]),
        "solutions": [
            {
                "preferred_term": repair.METHANOTHERMOCOCCUS_HHB,
                "composition": [],
                "concentration": {"value": "1", "unit": "G_PER_L"},
                "name": "Unknown solution",
            }
        ],
        "data_quality_flags": [
            "incomplete_composition",
            "source_information_unavailable",
        ],
        "curation_history": [],
    }


def _parent_doc(repair, path: str) -> dict:
    return {
        "id": repair.EXPECTED_IDS[path],
        "name": "methanothermococcus_hhb_medium",
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
        repair.TOGO_M1280: _child_doc(repair, repair.TOGO_M1280),
        repair.JCM_J1195: _child_doc(repair, repair.JCM_J1195),
        repair.TOGO_M1279: _parent_doc(repair, repair.TOGO_M1279),
        repair.JCM_J1194: _parent_doc(repair, repair.JCM_J1194),
    }
    for relative_path, doc in docs.items():
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")


def test_repair_togo_child_keeps_m1280_sparse_and_grounded(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_child(
        _child_doc(repair_module, repair_module.TOGO_M1280),
        repair_module.TARGETS[0],
        _parent_doc(repair_module, repair_module.TOGO_M1279),
    )

    assert repaired["ingredients"] == [
        {
            "preferred_term": "Na2SO4",
            "concentration": {"value": "2.8", "unit": "G_PER_L"},
            "source": "TOGO Medium M1280",
            "notes": (
                "TOGO M1280 supplements one liter of Methanothermococcus HHB "
                "Medium with 2.8 g/L Na2SO4."
            ),
            "term": {"id": "CHEBI:32149", "label": "sodium sulfate"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:32149",
                "label": "sodium sulfate",
            },
        }
    ]
    assert repaired["solutions"] == [
        {
            "preferred_term": repair_module.METHANOTHERMOCOCCUS_HHB,
            "composition": [],
            "concentration": {"value": "1", "unit": "L"},
            "notes": (
                "TOGO M1280 uses one liter of TOGO M1279 "
                "Methanothermococcus HHB Medium as the base medium."
            ),
            "culturemech_term": {
                "id": repair_module.EXPECTED_IDS[repair_module.TOGO_M1279],
                "label": "Methanothermococcus HHB Medium",
            },
        }
    ]
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]
    assert repaired["parent_media"] == {
        "path": f"data/normalized_yaml/{repair_module.TOGO_M1279}",
        "relationship": repair_module.RELATIONSHIP,
        "id": repair_module.EXPECTED_IDS[repair_module.TOGO_M1279],
        "name": "methanothermococcus_hhb_medium",
        "notes": repair_module.TARGETS[0].parent_notes,
    }
    assert repaired["variant_relationship"] == repair_module.RELATIONSHIP
    assert repaired["variant_modifications"] == [
        repair_module.TARGETS[0].variant_modification
    ]
    assert repaired["references"] == [{"reference": repair_module.TOGO_M1280_URL}]
    assert scorer_module.score_record(repaired)[1] == ["no pH and no temperature"]


def test_repair_jcm_child_links_recovered_j1195_to_j1194(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_child(
        _child_doc(repair_module, repair_module.JCM_J1195),
        repair_module.TARGETS[1],
        _parent_doc(repair_module, repair_module.JCM_J1194),
    )

    assert repaired["solutions"][0]["culturemech_term"] == {
        "id": repair_module.EXPECTED_IDS[repair_module.JCM_J1194],
        "label": "METHANOTHERMOCOCCUS HHB MEDIUM",
    }
    assert repaired["solutions"][0]["concentration"] == {
        "value": "1",
        "unit": "L",
    }
    assert repaired["parent_media"] == {
        "path": f"data/normalized_yaml/{repair_module.JCM_J1194}",
        "relationship": repair_module.RELATIONSHIP,
        "id": repair_module.EXPECTED_IDS[repair_module.JCM_J1194],
        "name": "methanothermococcus_hhb_medium",
        "notes": repair_module.TARGETS[1].parent_notes,
    }
    assert scorer_module.score_record(repaired)[1] == ["no pH and no temperature"]


def test_plan_repairs_adds_reciprocal_links_and_preserves_children(
    repair_module,
    tmp_path: Path,
) -> None:
    _write_tree(repair_module, tmp_path)

    plans = repair_module.plan_repairs(tmp_path)

    assert set(plans) == {
        tmp_path / repair_module.TOGO_M1280,
        tmp_path / repair_module.JCM_J1195,
        tmp_path / repair_module.TOGO_M1279,
        tmp_path / repair_module.JCM_J1194,
    }

    togo_children = plans[tmp_path / repair_module.TOGO_M1279]["variant_children"]
    jcm_children = plans[tmp_path / repair_module.JCM_J1194]["variant_children"]

    assert {
        row["path"]
        for row in togo_children
    } == {
        "data/normalized_yaml/archaea/existing_variant.yaml",
        f"data/normalized_yaml/{repair_module.TOGO_M1280}",
    }
    assert {
        row["path"]
        for row in jcm_children
    } == {
        "data/normalized_yaml/archaea/existing_variant.yaml",
        f"data/normalized_yaml/{repair_module.JCM_J1195}",
    }


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    _write_tree(repair_module, tmp_path)

    first = repair_module.plan_repairs(tmp_path)
    for path, doc in first.items():
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    second = repair_module.plan_repairs(tmp_path)

    assert second == first


def test_repair_child_rejects_wrong_source(repair_module) -> None:
    doc = _child_doc(repair_module, repair_module.TOGO_M1280)
    doc["media_term"]["term"]["id"] = "TOGO:M1279"

    with pytest.raises(ValueError, match="expected 'TOGO:M1280'"):
        repair_module.repair_child(
            doc,
            repair_module.TARGETS[0],
            _parent_doc(repair_module, repair_module.TOGO_M1279),
        )


def test_repair_child_rejects_missing_parent_solution(repair_module) -> None:
    doc = _child_doc(repair_module, repair_module.TOGO_M1280)
    doc["solutions"] = []

    with pytest.raises(ValueError, match="missing Methanothermococcus HHB"):
        repair_module.repair_child(
            doc,
            repair_module.TARGETS[0],
            _parent_doc(repair_module, repair_module.TOGO_M1279),
        )


def test_repair_child_rejects_sulfate_concentration_drift(repair_module) -> None:
    doc = _child_doc(repair_module, repair_module.TOGO_M1280)
    doc["ingredients"][0]["concentration"]["value"] = "2.0"

    with pytest.raises(ValueError, match="Na2SO4 concentration drifted"):
        repair_module.repair_child(
            doc,
            repair_module.TARGETS[0],
            _parent_doc(repair_module, repair_module.TOGO_M1279),
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
