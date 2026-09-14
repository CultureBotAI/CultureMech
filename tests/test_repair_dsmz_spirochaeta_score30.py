from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load_repair():
    path = REPO_ROOT / "scripts" / "repair_dsmz_spirochaeta_score30.py"
    spec = importlib.util.spec_from_file_location(
        "repair_dsmz_spirochaeta_score30",
        path,
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["repair_dsmz_spirochaeta_score30"] = mod
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc(repair, update) -> dict:
    return {
        "id": repair.EXPECTED_IDS[update.path],
        "name": Path(update.path).stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 5.0,
        "ingredients": [],
        "media_term": {
            "preferred_term": repair.EXPECTED_SOURCE_TERMS[update.path],
            "term": {
                "id": repair.EXPECTED_SOURCE_TERMS[update.path],
                "label": repair.EXPECTED_SOURCE_TERMS[update.path],
            },
        },
        "data_quality_flags": ["incomplete_composition"],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _write_targets(repair, root: Path) -> dict[Path, dict]:
    docs = {}
    for update in repair.UPDATES:
        path = root / update.path
        path.parent.mkdir(parents=True, exist_ok=True)
        docs[path] = _minimal_doc(repair, update)
        path.write_text(
            yaml.safe_dump(docs[path], sort_keys=False),
            encoding="utf-8",
        )
    return docs


def _solution_by_name(doc: dict, name: str) -> dict:
    return next(solution for solution in doc["solutions"] if solution["preferred_term"] == name)


def _ingredient_by_name(doc: dict, name: str) -> dict:
    return next(
        ingredient for ingredient in doc["ingredients"] if ingredient["preferred_term"] == name
    )


def test_all_reviewed_targets_have_expected_ids_and_source_terms():
    repair = _load_repair()

    assert len(repair.UPDATES) == 2
    assert {update.path for update in repair.UPDATES} == set(repair.EXPECTED_IDS)
    assert set(repair.EXPECTED_IDS) == set(repair.EXPECTED_SOURCE_TERMS)


def test_plan_repairs_adds_spirochaeta_aurantia_recipe(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_targets(repair, root)

    plans = repair.plan_repairs(root)
    aurantia = plans[root / repair.DSMZ_168_SPIROCHAETA_AURANTIA]

    assert aurantia["ph_range"] == {"min": 7.0, "max": 7.3}
    assert aurantia["incubation_atmosphere"] == "ANAEROBIC"
    assert [ingredient["preferred_term"] for ingredient in aurantia["ingredients"]] == [
        "D-Glucose",
        "Yeast extract",
        "Trypticase peptone (BD BBL)",
    ]
    assert _ingredient_by_name(aurantia, "D-Glucose")["term"] == {
        "id": "CHEBI:17634",
        "label": "D-glucose",
    }

    phosphate = _solution_by_name(aurantia, "1 M K-phosphate buffer, pH 7.0")
    assert phosphate["concentration"] == {"value": "10", "unit": "ML_PER_L"}
    assert phosphate["composition"] == [
        {
            "preferred_term": "K2HPO4",
            "concentration": {"value": "615", "unit": "MILLIMOLAR"},
            "source": repair.SRC_168,
            "term": {
                "id": "CHEBI:131527",
                "label": "dipotassium hydrogen phosphate",
            },
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:131527",
                "label": "dipotassium hydrogen phosphate",
            },
        },
        {
            "preferred_term": "KH2PO4",
            "concentration": {"value": "385", "unit": "MILLIMOLAR"},
            "source": repair.SRC_168,
            "term": {
                "id": "CHEBI:63036",
                "label": "potassium dihydrogen phosphate",
            },
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:63036",
                "label": "potassium dihydrogen phosphate",
            },
        },
    ]


def test_plan_repairs_adds_spirochaeta_isovalerica_recipe(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_targets(repair, root)

    plans = repair.plan_repairs(root)
    isovalerica = plans[root / repair.DSMZ_273_SPIROCHAETA_ISOVALERICA]

    assert isovalerica["ph_value"] == 7.5
    assert isovalerica["incubation_atmosphere"] == "ANAEROBIC"
    assert "solutions" not in isovalerica
    assert _ingredient_by_name(isovalerica, "Tris-HCl-buffer (0.2 M; pH 7.5)")["concentration"] == {
        "value": "250",
        "unit": "ML_PER_L",
    }
    assert _ingredient_by_name(isovalerica, "Sea water")["concentration"] == {
        "value": "750",
        "unit": "ML_PER_L",
    }
    assert _ingredient_by_name(isovalerica, "Cysteine-HCl x H2O")["term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }
    assert _ingredient_by_name(isovalerica, "Resazurin")["concentration"] == {
        "value": "0.001",
        "unit": "G_PER_L",
    }


def test_plan_repairs_adds_review_metadata_once(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    _write_targets(repair, root)

    first = repair.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    second = repair.plan_repairs(root)
    aurantia = second[root / repair.DSMZ_168_SPIROCHAETA_AURANTIA]

    assert second == first
    assert aurantia["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert aurantia["references"] == [{"reference": repair.DSMZ_168_PDF}]

    matching_events = [
        event
        for event in aurantia["curation_history"]
        if (event.get("curator") == repair.CURATOR and event.get("action") == repair.ACTION)
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == repair.DSMZ_168_PDF


def test_plan_repairs_rejects_unexpected_target_id(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    docs = _write_targets(repair, root)
    target = root / repair.DSMZ_273_SPIROCHAETA_ISOVALERICA
    docs[target]["id"] = "CultureMech:wrong"
    target.write_text(yaml.safe_dump(docs[target], sort_keys=False), encoding="utf-8")

    with pytest.raises(ValueError, match="expected 'CultureMech:004701'"):
        repair.plan_repairs(root)
