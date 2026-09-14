from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_lb_family_score15.py"
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
    return _load_script(SCRIPT, "repair_lb_family_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_lb_family")


def _doc(target) -> dict:
    return {
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


def _by_name(doc: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in doc["ingredients"]}


def test_all_targets_score_below_review_threshold(repair_module, scorer_module) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(target), target)
        water = _by_name(repaired)["Distilled water"]
        expected_water = next(
            row for row in target.ingredients if row.preferred_term == "Distilled water"
        )

        assert water == {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
            "source": expected_water.source,
            "notes": expected_water.notes,
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
        }
        assert scorer_module.score_parsed([(target.path, repaired)]) == []


def test_generic_nbrc_lb_rows_are_grounded(repair_module, scorer_module) -> None:
    by_path = repair_module.TARGET_BY_PATH

    lb = repair_module.repair_record(
        _doc(by_path["bacterial/lb_medium.yaml"]), by_path["bacterial/lb_medium.yaml"]
    )
    third = repair_module.repair_record(
        _doc(by_path["bacterial/1_3_lb.yaml"]), by_path["bacterial/1_3_lb.yaml"]
    )

    assert _by_name(lb)["Peptone"]["term"] == {"id": "MICRO:0000178", "label": "peptone"}
    assert _by_name(lb)["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert lb["ph_value"] == 7.0
    assert scorer_module.score_record(lb) == (0, [])
    assert "ph_value" not in third
    assert scorer_module.score_record(third) == (5, ["no pH and no temperature"])


def test_difco_digest_rows_stay_unmapped(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/TOGO_M878_1_3_LB_Agar.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)
    by_name = _by_name(repaired)

    assert "term" not in by_name["Tryptone (BD-Difco)"]
    assert "term" not in by_name["Yeast extract (BD-Difco)"]
    assert by_name["NaCl"]["term"] == {"id": "CHEBI:26710", "label": "sodium chloride"}
    assert by_name["Agar"]["term"] == {"id": "CHEBI:2509", "label": "agar"}


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/TOGO_M878_1_3_LB_Agar.yaml"]
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
    target = repair_module.TARGET_BY_PATH["bacterial/lb_medium.yaml"]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/lb_medium.yaml"]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=target.source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_component_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/lb_medium.yaml"]
    doc = _doc(target)
    doc["ingredients"][1]["concentration"]["value"] = "6"

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
