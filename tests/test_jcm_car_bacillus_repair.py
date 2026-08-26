from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_car_bacillus.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_jcm_car_bacillus", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return load_script()


def test_selected_fbs_identity_exists_in_mim_sssom(repair_module) -> None:
    solution = repair_module.RECIPE["solutions"][0]
    fbs = solution["composition"][1]
    assert "term" not in fbs
    assert "NCIT:C113696" in fbs["notes"]
    if not repair_module.MIM_SSSOM.is_file():
        pytest.skip("authoritative MIM SSSOM sibling is unavailable")
    repair_module.validate_mim_term(repair_module.MIM_SSSOM)


def test_conditioned_medium_structure_matches_source(repair_module) -> None:
    recipe = repair_module.RECIPE
    assert recipe["ingredients"] == []
    solution = recipe["solutions"][0]
    assert solution["concentration"] == {"value": "100", "unit": "PERCENT_V_V"}
    assert [row["concentration"] for row in solution["composition"]] == [
        {"value": "90", "unit": "PERCENT_V_V"},
        {"value": "10", "unit": "PERCENT_V_V"},
    ]
    descriptions = " ".join(row["description"] for row in recipe["preparation_steps"])
    assert "Vero E6" in descriptions
    assert "centrifuge" in descriptions
    assert "56 C for 30 minutes" in descriptions


def test_unmapped_imdm_identity_is_not_invented(repair_module) -> None:
    imdm = repair_module.RECIPE["solutions"][0]["composition"][0]
    assert "term" not in imdm
    assert "mediaingredientmech_chebi_term" not in imdm


def test_repair_is_guarded_and_idempotent(repair_module) -> None:
    doc = {
        "id": repair_module.TARGET_ID,
        "notes": "Source retained",
        "ingredients": [],
        "data_quality_flags": ["incomplete_composition", "source_information_unavailable"],
        "curation_history": [],
    }
    repaired, changed = repair_module.repair_document(doc)
    second, changed_again = repair_module.repair_document(copy.deepcopy(repaired))
    assert changed
    assert not changed_again
    assert second == repaired
    assert "data_quality_flags" not in repaired


def test_nonempty_precondition_is_rejected(repair_module) -> None:
    doc = {
        "id": repair_module.TARGET_ID,
        "ingredients": [{"preferred_term": "unexpected"}],
        "data_quality_flags": ["incomplete_composition", "source_information_unavailable"],
    }
    with pytest.raises(ValueError, match="no longer composition-empty"):
        repair_module.repair_document(doc)


def test_source_hash_mismatch_is_rejected(repair_module, tmp_path: Path) -> None:
    (tmp_path / repair_module.SOURCE_FILE).write_bytes(b"not the reviewed source")
    with pytest.raises(ValueError, match="SHA-256"):
        repair_module.validate_source_file(tmp_path)


def test_target_record_is_in_guarded_pre_or_post_state(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert doc["id"] == repair_module.TARGET_ID
    if repair_module.history_has_action(doc):
        repair_module._assert_applied(doc)
    else:
        repair_module._validate_precondition(copy.deepcopy(doc))
