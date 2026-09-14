from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_jcm_archaea_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_jcm_archaea_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_jcm_archaea")


def _doc(update) -> dict:
    old_names = sorted(next(iter(update.accepted_names - {repair_new_names(update)})))
    return {
        "id": update.record_id,
        "name": Path(update.path).stem,
        "original_name": Path(update.path).stem,
        "category": "archaea",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": update.source_term,
            "term": {"id": update.source_term, "label": update.source_term},
        },
        "notes": "Source: TOGO",
        "ingredients": [{"preferred_term": name} for name in old_names],
        "curation_history": [],
    }


def repair_new_names(update) -> frozenset[str]:
    return frozenset(
        row["preferred_term"]
        for key in ("ingredients", "solutions")
        for row in update.recipe.get(key, [])
    )


def _solution(doc: dict, preferred_term: str) -> dict:
    for row in doc["solutions"]:
        if row["preferred_term"] == preferred_term:
            return row
    raise AssertionError(f"missing solution {preferred_term!r}")


def test_all_targets_score_below_review_threshold(repair_module, scorer_module) -> None:
    for update in repair_module.UPDATES.values():
        repaired = repair_module.repair_document(_doc(update), update)

        score, reasons = scorer_module.score_record(repaired)

        assert score <= 5
        assert reasons in ([], ["no pH and no temperature"])


def test_m1265_and_m1266_share_cellulolytic_stocks(repair_module) -> None:
    liquid = repair_module.repair_document(
        _doc(
            repair_module.UPDATES[
                "archaea/TOGO_M1265_Modified_Cellulolytic_Haloarchaea_Medium.yaml"
            ]
        ),
        repair_module.UPDATES["archaea/TOGO_M1265_Modified_Cellulolytic_Haloarchaea_Medium.yaml"],
    )
    solid = repair_module.repair_document(
        _doc(
            repair_module.UPDATES[
                "archaea/TOGO_M1266_Modified_Cellulolytic_Haloarchaea_Medium.yaml"
            ]
        ),
        repair_module.UPDATES["archaea/TOGO_M1266_Modified_Cellulolytic_Haloarchaea_Medium.yaml"],
    )

    assert liquid["physical_state"] == "LIQUID"
    assert solid["physical_state"] == "SOLID_AGAR"
    assert [row["preferred_term"] for row in solid["ingredients"]] == [
        "Distilled water",
        "Agar",
        "Yeast extract (BD-Difco)",
    ]
    assert [row["preferred_term"] for row in liquid["solutions"]] == [
        row["preferred_term"] for row in solid["solutions"]
    ]
    assert _solution(solid, "MDS salt water")["concentration"] == {
        "value": "833.0",
        "unit": "ML_PER_L",
    }


def test_m970_scales_tube_additions_to_ml_per_l(repair_module) -> None:
    update = repair_module.UPDATES["archaea/TOGO_M970_Peat_Medium_2_For_Methanobacteria.yaml"]
    repaired = repair_module.repair_document(_doc(update), update)

    assert _solution(repaired, "83 mM TiNTA solution")["concentration"] == {
        "value": "10.0",
        "unit": "ML_PER_L",
    }
    assert _solution(repaired, "1.0 M MES solution")["concentration"] == {
        "value": "20.0",
        "unit": "ML_PER_L",
    }
    assert _solution(repaired, "50 mM Coenzyme M solution")["concentration"] == {
        "value": "5.0",
        "unit": "ML_PER_L",
    }
    assert _solution(repaired, "10 mM Sodium acetate")["concentration"] == {
        "value": "3.0",
        "unit": "ML_PER_L",
    }


def test_m1162_expands_soda_and_gas_phase(repair_module) -> None:
    update = repair_module.UPDATES["archaea/TOGO_M1162_Natronolimnobius_AHT32_Medium_B.yaml"]
    repaired = repair_module.repair_document(_doc(update), update)

    assert [row["preferred_term"] for row in repaired["ingredients"]] == ["N2", "O2"]
    soda = _solution(repaired, "Soda based mineral medium")
    assert soda["concentration"] == {"value": "1000.0", "unit": "ML_PER_L"}
    assert [row["preferred_term"] for row in soda["composition"]][:5] == [
        "Na2CO3",
        "NaHCO3",
        "NaCl",
        "K2HPO4",
        "KCl",
    ]


def test_solution_compositions_are_flat_ingredients(repair_module) -> None:
    for update in repair_module.UPDATES.values():
        repaired = repair_module.repair_document(_doc(update), update)

        for solution in repaired["solutions"]:
            for component in solution.get("composition", []):
                assert "composition" not in component
                assert "preparation_notes" not in component


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    update = repair_module.UPDATES["archaea/TOGO_M1371_Sulfolobus_Medium_With_Tryptone.yaml"]
    repaired = repair_module.repair_document(_doc(update), update)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [
        {"reference": repair_module.TOGO_M1371},
        {"reference": repair_module.JCM_1275},
        {"reference": repair_module.JCM_165},
    ]
    assert repaired["curation_history"][-1] == {
        "timestamp": repair_module.TIMESTAMP,
        "curator": repair_module.CURATOR,
        "action": repair_module.ACTION,
        "source": f"{repair_module.TOGO_M1371}; {repair_module.JCM_1275}; {repair_module.JCM_165}",
        "notes": update.notes,
    }


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    for update in repair_module.UPDATES.values():
        path = tmp_path / update.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(update), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(tmp_path)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(tmp_path)

    assert {
        path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    update = repair_module.UPDATES["archaea/TOGO_M1150_Natranaeroarchaeum_Medium.yaml"]
    doc = _doc(update)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=update.record_id):
        repair_module.repair_document(doc, update)


def test_repair_rejects_wrong_source(repair_module) -> None:
    update = repair_module.UPDATES["archaea/TOGO_M1150_Natranaeroarchaeum_Medium.yaml"]
    doc = _doc(update)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=update.source_term):
        repair_module.repair_document(doc, update)


def test_repair_rejects_component_drift(repair_module) -> None:
    update = repair_module.UPDATES["archaea/TOGO_M1150_Natranaeroarchaeum_Medium.yaml"]
    doc = _doc(update)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="component signature drifted"):
        repair_module.repair_document(doc, update)
