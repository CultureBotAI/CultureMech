from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_wrappers_direct_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc(target) -> dict:
    return {
        "id": target.expected_id,
        "name": target.path.rsplit("/", 1)[-1].removesuffix(".yaml"),
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [],
        "media_term": {
            "preferred_term": target.expected_media_term,
            "term": {"id": target.expected_media_term, "label": target.expected_media_term},
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def test_wrappers_direct_score_only_on_norm_signal() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_wrappers_direct_score20")
    scorer = _load_script(SCORER, "score_review_need_for_jcm_wrappers_direct")

    by_path = {target.path: target for target in repair.TARGETS}

    for path in (repair.M749_RAVOT_R8, repair.M750_RAVOT_G60):
        repaired = repair.repair_record(_minimal_doc(by_path[path]), by_path[path])
        assert scorer.score_record(repaired) == (0, [])

    for path in (
        repair.M775_DESULFOVIBRIO_MARINE,
        repair.M777_OPITUTUS,
        repair.M828_M_TGE_BROTH,
        repair.M829_M_TGE_AGAR,
    ):
        repaired = repair.repair_record(_minimal_doc(by_path[path]), by_path[path])
        assert scorer.score_record(repaired) == (5, ["no pH and no temperature"])


def test_ravot_salt_wrappers_keep_distinct_ph_values() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_wrappers_direct_score20_ravot")
    by_path = {target.path: target for target in repair.TARGETS}

    r8 = repair.repair_record(
        _minimal_doc(by_path[repair.M749_RAVOT_R8]), by_path[repair.M749_RAVOT_R8]
    )
    g60 = repair.repair_record(
        _minimal_doc(by_path[repair.M750_RAVOT_G60]), by_path[repair.M750_RAVOT_G60]
    )

    assert r8["ph_value"] == 6.3
    assert g60["ph_value"] == 7.0
    assert r8["ingredients"][0]["concentration"] == {"value": "5.0", "unit": "G_PER_L"}
    assert g60["ingredients"][0]["concentration"] == {"value": "20.0", "unit": "G_PER_L"}
    assert r8["parent_media"] == {
        "path": "data/normalized_yaml/bacterial/TOGO_M748_Ravot_Modified_Medium_For_Thermoanaerovibrio_SP._R101.yaml",
        "relationship": "SALINITY_VARIANT",
        "id": "CultureMech:010153",
        "name": "ravot_modified_medium_for_thermoanaerovibrio_sp_r101",
        "notes": "Uses Medium 725 with 5.0 g/L NaCl and pH adjusted to 6.3.",
    }


def test_m_tge_water_units_and_solid_agar_split() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_wrappers_direct_score20_mtge")
    by_path = {target.path: target for target in repair.TARGETS}

    broth = repair.repair_record(
        _minimal_doc(by_path[repair.M828_M_TGE_BROTH]),
        by_path[repair.M828_M_TGE_BROTH],
    )
    agar = repair.repair_record(
        _minimal_doc(by_path[repair.M829_M_TGE_AGAR]),
        by_path[repair.M829_M_TGE_AGAR],
    )

    assert broth["physical_state"] == "LIQUID"
    assert agar["physical_state"] == "SOLID_AGAR"
    assert broth["sterilization"] == {"method": "AUTOCLAVE"}
    assert [ingredient["preferred_term"] for ingredient in broth["ingredients"]] == [
        "Bacto m TGE broth (BD-Difco)",
        "Distilled water",
    ]
    assert [ingredient["preferred_term"] for ingredient in agar["ingredients"]] == [
        "Bacto m TGE broth (BD-Difco)",
        "Distilled water",
        "agar",
    ]
    assert broth["ingredients"][1]["concentration"] == {"value": "1000", "unit": "ML_PER_L"}
    assert agar["ingredients"][1]["concentration"] == {"value": "1000", "unit": "ML_PER_L"}
    assert agar["ingredients"][2]["concentration"] == {"value": "15.0", "unit": "G_PER_L"}


def test_plan_repairs_is_idempotent(tmp_path: Path) -> None:
    repair = _load_script(SCRIPT, "repair_jcm_wrappers_direct_score20_idempotent")
    root = tmp_path / "normalized"

    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_minimal_doc(target), sort_keys=False), encoding="utf-8")

    first = repair.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    assert repair.plan_repairs(root) == first
