from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_score10_stock_solutions.py"
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
    return _load_script(SCRIPT, "repair_jcm_score10_stock_solutions")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_score10_stock_solutions")


def _ingredient(name: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": "1", "unit": "G_PER_L"}}


def _doc(repair_module, target: Path) -> dict:
    return {
        "id": repair_module.TARGETS[target]["id"],
        "name": target.stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "JCM Medium",
            "term": {
                "id": repair_module.TARGETS[target]["source_id"],
                "label": target.stem,
            },
        },
        "notes": "Source: JCM",
        "ph_value": 7.0,
        "ingredients": [
            _ingredient(name) for name in repair_module.IMPORTED_SIGNATURES[target]
        ],
        "curation_history": [],
    }


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


@pytest.mark.parametrize("target", tuple(_load_script(SCRIPT, "stock_targets").TARGETS))
def test_score10_stock_records_exit_review_ranking(
    repair_module,
    scorer_module,
    target: Path,
) -> None:
    repaired = repair_module.repair_record(
        target,
        _load_yaml(repair_module.NORMALIZED / target),
    )

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(target), repaired)]) == []


def test_j1334_moves_neutral_base_to_nested_solution(repair_module) -> None:
    target = Path("archaea/JCM_J1334_NATRONOARCHAEA_MEDIUM_II.yaml")
    repaired = repair_module.repair_record(target, _doc(repair_module, target))
    solutions = _by_name(repaired["solutions"])
    neutral = _by_name(solutions["Neutral base salt medium"]["composition"])

    assert repaired["ingredients"] == []
    assert solutions["Base soda medium (JCM Medium 1207)"]["source"].endswith(
        "JCM Medium 1207"
    )
    assert "composition" not in solutions["Base soda medium (JCM Medium 1207)"]
    assert neutral["NaCl"]["concentration"] == {"value": "240.0", "unit": "G_PER_L"}
    assert neutral["(NH4)2SO4"]["term"] == {
        "id": "CHEBI:62946",
        "label": "ammonium sulfate",
    }


def test_j1405_splits_simple_defined_stocks(repair_module) -> None:
    target = Path("bacterial/JCM_J1405_THIOHALORHABDUS_METHYLOTROPHUS_MEDIUM.yaml")
    repaired = repair_module.repair_record(target, _doc(repair_module, target))
    solutions = _by_name(repaired["solutions"])

    assert solutions["0.002% CuCl2 x 2H2O solution"]["composition"] == [
        {
            "preferred_term": "CuCl2 x 2H2O",
            "concentration": {"value": "0.002", "unit": "PERCENT_W_V"},
            "source": "JCM Medium 1405",
            "notes": "JCM Medium 1405 lists 0.002 % w/v CuCl2 x 2H2O.",
            "term": {
                "id": "CHEBI:86318",
                "label": "copper dichloride dihydrate",
            },
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:86318",
                "label": "copper dichloride dihydrate",
            },
        }
    ]
    assert solutions["2 M Sodium thiosulfate solution"]["composition"][0]["term"] == {
        "id": "CHEBI:132112",
        "label": "sodium thiosulfate",
    }
    assert "composition" not in solutions["3% Trimethylamine solution"]


def test_repair_adds_references_and_history(repair_module) -> None:
    target = Path("bacterial/JCM_J1392_ATRIBACTEROTA_M15_MEDIUM.yaml")
    repaired = repair_module.repair_record(target, _doc(repair_module, target))

    assert repaired["references"] == [
        {"reference": repair_module._jcm_url(number)}
        for number in repair_module.REFERENCES[target]
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "changes": "Moved flat JCM stock additions into solutions",
            "source": repair_module._jcm_url(1392),
            "notes": repair_module.REPAIRS[target]()[2],
        }
    ]


def test_repair_is_idempotent(repair_module) -> None:
    target = next(iter(repair_module.TARGETS))
    once = repair_module.repair_record(
        target,
        _load_yaml(repair_module.NORMALIZED / target),
    )
    twice = repair_module.repair_record(target, once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)


def test_plan_repairs_targets_current_records(repair_module) -> None:
    expected = {}
    for relative in repair_module.TARGETS:
        path = repair_module.NORMALIZED / relative
        expected[path] = repair_module.repair_record(relative, _load_yaml(path))

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = next(iter(repair_module.TARGETS))
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.TARGETS[target]["id"]):
        repair_module.repair_record(target, doc)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = next(iter(repair_module.TARGETS))
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "jcm.grmd:wrong"

    with pytest.raises(ValueError, match=repair_module.TARGETS[target]["source_id"]):
        repair_module.repair_record(target, doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = next(iter(repair_module.TARGETS))
    doc = _doc(repair_module, target)
    doc["ingredients"][0]["preferred_term"] = "Yeast extract"

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_record(target, doc)
