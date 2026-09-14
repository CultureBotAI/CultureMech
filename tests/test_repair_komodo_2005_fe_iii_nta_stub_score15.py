from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "repair_komodo_2005_fe_iii_nta_stub_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
TARGET = REPO / "data" / "normalized_yaml" / "bacterial" / "fe_iii_nta_solution_medium_1001.yaml"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def repair_module():
    return _load_script(SCRIPT, "repair_komodo_2005_fe_iii_nta_stub_score15")


@pytest.fixture
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_2005")


@pytest.fixture
def original_doc():
    with TARGET.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def test_repair_retypes_orphaned_solution_stub(repair_module, original_doc):
    repaired = repair_module.repair_record(original_doc)

    assert repaired["id"] == "CultureMech:004271"
    assert repaired["record_kind"] == "SOLUTION"
    assert "ph_value" not in repaired
    assert repaired["ingredients"] == []
    assert "source_information_unavailable" in repaired["data_quality_flags"]
    assert {row["reference"] for row in repaired["references"]} >= {
        repair_module.MEDIADIVE_1001,
        repair_module.DSMZ_1001_PDF,
    }
    assert repaired["curation_history"][-1]["curator"] == repair_module.CURATOR
    assert "NaOH pH-buffer pseudo-ingredient" in repaired["curation_history"][-1]["changes"]


def test_repair_is_idempotent(repair_module, original_doc):
    repaired = repair_module.repair_record(original_doc)

    assert repair_module.repair_record(repaired) == repaired


def test_repaired_solution_leaves_review_need_ranking(
    repair_module,
    scorer_module,
    original_doc,
):
    repaired = repair_module.repair_record(original_doc)

    assert (
        scorer_module.score_parsed([("bacterial/fe_iii_nta_solution_medium_1001.yaml", repaired)])
        == []
    )


def test_repair_guards_target_identity(repair_module, original_doc):
    wrong_id = copy.deepcopy(original_doc)
    wrong_id["id"] = "CultureMech:999999"

    with pytest.raises(ValueError, match="expected id CultureMech:004271"):
        repair_module.repair_record(wrong_id)

    wrong_term = copy.deepcopy(original_doc)
    wrong_term["media_term"]["term"]["id"] = "komodo.medium:1001"

    with pytest.raises(ValueError, match="expected media term komodo.medium:2005"):
        repair_module.repair_record(wrong_term)


def test_repair_guards_unexpected_composition_drift(repair_module, original_doc):
    drifted = copy.deepcopy(original_doc)
    drifted["ingredients"] = [
        {
            "preferred_term": "Fe(III)NTA",
            "concentration": {"value": "1", "unit": "G_PER_L"},
        }
    ]

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_record(drifted)
