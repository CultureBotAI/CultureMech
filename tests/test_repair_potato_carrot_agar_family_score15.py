from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_potato_carrot_agar_family_score15.py"
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
    return _load_script(SCRIPT, "repair_potato_carrot_agar_family_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_potato_carrot_agar")


def _doc(target) -> dict:
    doc = {
        "id": target.record_id,
        "name": Path(target.path).stem,
        "original_name": Path(target.path).stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": target.source_term,
            "term": {"id": target.source_term, "label": target.source_term},
        },
        "notes": "Source",
        "ingredients": [
            {
                "preferred_term": preferred_term,
                "concentration": {"value": value, "unit": unit},
            }
            for preferred_term, value, unit in target.imported_signature
        ],
        "curation_history": [],
    }
    if target.source_term == "mediadive.medium:1765":
        doc["ph_value"] = 7.0
    return doc


def _by_name(doc: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in doc["ingredients"]}


def test_repairs_add_water_and_clear_review_need(
    repair_module,
    scorer_module,
) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(target), target)
        by_name = _by_name(repaired)

        assert repaired["ingredients"][-1] == {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "source": target.ingredients[-1].source,
            "notes": target.ingredients[-1].notes,
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
        }
        assert "term" not in by_name[target.ingredients[0].preferred_term]
        assert "term" not in by_name[target.ingredients[1].preferred_term]
        assert scorer_module.score_parsed([(target.path, repaired)]) == []


def test_dsmz_variant_keeps_numeric_ph(repair_module, scorer_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/potato_carrot_agar.yaml"]

    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["ph_value"] == 7.0
    assert scorer_module.score_record(repaired) == (0, [])


def test_jcm_records_retain_ph_unadjusted_endpoint(repair_module, scorer_module) -> None:
    jcm_paths = [
        "bacterial/JCM_J54_POTATO-CARROT_AGAR.yaml",
        "bacterial/1_10_potato_carrot_agar.yaml",
    ]

    for path in jcm_paths:
        target = repair_module.TARGET_BY_PATH[path]
        repaired = repair_module.repair_record(_doc(target), target)

        assert "ph_value" not in repaired
        assert scorer_module.score_record(repaired) == (
            5,
            ["no pH and no temperature"],
        )


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/TOGO_M47_1_10_Potato-Carrot_Agar.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [{"reference": url} for url in target.reference_urls]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": "; ".join(target.reference_urls),
            "notes": target.notes,
        }
    ]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    for target in repair_module.TARGETS:
        path = tmp_path / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(target), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(tmp_path)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(tmp_path)

    assert {
        path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/JCM_J54_POTATO-CARROT_AGAR.yaml"]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/JCM_J54_POTATO-CARROT_AGAR.yaml"]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:J999"

    with pytest.raises(ValueError, match=target.source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_component_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/JCM_J54_POTATO-CARROT_AGAR.yaml"]
    doc = _doc(target)
    doc["ingredients"][0]["concentration"]["value"] = "301"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_reviewed_inputs(repair_module) -> None:
    for target in repair_module.TARGETS:
        doc = yaml.safe_load((repair_module.NORMALIZED / target.path).read_text(encoding="utf-8"))

        assert doc["id"] == target.record_id
        assert repair_module._component_signature(doc["ingredients"]) in {
            target.imported_signature,
            repair_module._recipe_signature(target.ingredients),
        }
