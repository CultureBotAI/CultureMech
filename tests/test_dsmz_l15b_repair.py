from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_l15b.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_dsmz_l15b", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return load_script()


def _solution(rows: list[dict], name: str) -> dict:
    return next(row for row in rows if row["preferred_term"] == name)


def test_selected_identities_exist_in_actual_mim_sssom(repair_module) -> None:
    assert len(repair_module.MIM_TERMS) == 20
    if not repair_module.MIM_SSSOM.is_file():
        pytest.skip("authoritative MIM SSSOM sibling is unavailable")
    repair_module.validate_mim_terms(repair_module.MIM_SSSOM)


def test_basal_l15b_formula_and_unmapped_powder(repair_module) -> None:
    recipe = repair_module.RECIPE
    values = {row["preferred_term"]: row["concentration"] for row in recipe["ingredients"]}
    assert values["L-aspartic acid"] == {"value": "0.299", "unit": "G_PER_L"}
    assert values["D-glucose"] == {"value": "14.4105", "unit": "G_PER_L"}
    assert values["Cell culture grade water"] == {"value": "1", "unit": "L"}
    powder = next(
        row
        for row in recipe["ingredients"]
        if row["preferred_term"] == "Leibovitz's L-15 medium powder"
    )
    assert powder["concentration"] == {"value": "1 package", "unit": "VARIABLE"}
    assert "term" not in powder


def test_mineral_stock_materializes_source_substocks_within_d(repair_module) -> None:
    mineral_d = _solution(repair_module.RECIPE["solutions"], "L-15B mineral stock solution D")
    assert mineral_d["concentration"] == {"value": "1", "unit": "ML_PER_L"}
    values = {row["preferred_term"]: row["concentration"] for row in mineral_d["composition"]}
    assert values["CoCl2 x 6 H2O"] == {"value": "0.002", "unit": "G_PER_L"}
    assert values["MnSO4 x H2O"] == {"value": "0.016", "unit": "G_PER_L"}
    assert values["ZnSO4 x 7 H2O"] == {"value": "0.020", "unit": "G_PER_L"}
    assert 0.20 * 10 / 1000 == pytest.approx(0.002)
    assert 0.002 * 1 / 1000 == pytest.approx(2e-6)


def test_vitamin_and_naoh_stocks_preserve_source_units(repair_module) -> None:
    vitamin = _solution(repair_module.RECIPE["solutions"], "L-15B vitamin stock")
    assert vitamin["concentration"] == {"value": "1", "unit": "ML_PER_L"}
    assert vitamin["composition"][0]["concentration"] == {
        "value": "1.00",
        "unit": "G_PER_L",
    }
    naoh = _solution(repair_module.RECIPE["solutions"], "10 N NaOH solution")
    assert naoh["concentration"] == {"value": "0.5", "unit": "ML_PER_L"}
    assert naoh["composition"][0]["concentration"] == {
        "value": "10",
        "unit": "MOLAR",
    }


def test_protocol_metadata_matches_methods_document(repair_module) -> None:
    recipe = repair_module.RECIPE
    assert recipe["ph_range"] == {"min": 5.5, "max": 6.5}
    assert recipe["sterilization"] == {"method": "FILTER"}
    descriptions = " ".join(row["description"] for row in recipe["preparation_steps"])
    assert "1.5 hours" in descriptions
    assert "0.22 micrometre" in descriptions
    assert "415 +/- 10 mOsm/L" in descriptions


def test_repair_is_guarded_and_idempotent(repair_module) -> None:
    doc = {
        "id": repair_module.TARGET_ID,
        "notes": "Source retained",
        "ingredients": [],
        "data_quality_flags": ["incomplete_composition"],
        "curation_history": [],
    }
    repaired, changed = repair_module.repair_document(doc)
    second, changed_again = repair_module.repair_document(copy.deepcopy(repaired))
    assert changed
    assert not changed_again
    assert second == repaired
    assert "data_quality_flags" not in repaired


def test_source_hash_mismatch_is_rejected(repair_module, tmp_path: Path) -> None:
    for file_name in repair_module.SOURCE_FILES:
        (tmp_path / file_name).write_bytes(b"not the reviewed source")
    with pytest.raises(ValueError, match="SHA-256"):
        repair_module.validate_source_files(tmp_path)


def test_target_record_is_in_guarded_pre_or_post_state(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert doc["id"] == repair_module.TARGET_ID
    if repair_module.history_has_action(doc):
        repair_module._assert_applied(doc)
    else:
        repair_module._validate_precondition(copy.deepcopy(doc))
