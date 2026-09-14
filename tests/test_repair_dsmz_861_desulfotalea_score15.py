from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_861_desulfotalea_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_861_desulfotalea_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_861")


def _doc(repair, target) -> dict:
    return {
        "id": repair.EXPECTED_IDS[target.path],
        "name": Path(target.path).stem,
        "original_name": target.source_label.replace("KOMODO Medium 861.2", "For DSM 12341"),
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": target.source_label,
            "term": {
                "id": repair.EXPECTED_SOURCE_TERMS[target.path],
                "label": target.source_label,
            },
        },
        "notes": "Source: KOMODO ModelSEED | DSMZ Medium: 861",
        "ingredients": [
            {
                "preferred_term": "HCl",
                "concentration": {"value": "2.5", "unit": "G_PER_L"},
                "term": {"id": "CHEBI:17883", "label": "hydrogen chloride"},
            }
        ],
        "curation_history": [],
    }


def _write_minimal_tree(repair, root: Path) -> None:
    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(repair, target), sort_keys=False), encoding="utf-8")


def _target(repair, path: str):
    return repair.TARGET_BY_PATH[path]


def _solution_by_name(doc: dict) -> dict[str, dict]:
    return {solution["preferred_term"]: solution for solution in doc["solutions"]}


def _composition_by_name(solution: dict) -> dict[str, dict]:
    return {component["preferred_term"]: component for component in solution["composition"]}


def test_dsmz_861a_is_official_stock_solution_recipe(repair_module) -> None:
    target = _target(repair_module, repair_module.DSMZ_861A)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    solutions = _solution_by_name(repaired)
    assert repaired["ingredients"] == []
    assert list(solutions) == ["Solution A", "Solution B", "Solution C", "Solution D", "Solution E", "Solution F"]
    assert repaired["ph_range"] == {"min": 7.0, "max": 7.2}
    assert repaired["variant_children"] == [
        repair_module.DSMZ_861A_12341_CHILD,
        repair_module.DSMZ_861A_12342_CHILD,
        repair_module.DSMZ_861A_12343_CHILD,
        repair_module.DSMZ_861A_12344_CHILD,
    ]
    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "MIX",
        "FILTER_STERILIZE",
        "MIX",
        "ADJUST_PH",
    ]


def test_dsm_12341_uses_acetate_solution_c_and_leaves_ranking(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.KOMODO_861_2)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    components = _composition_by_name(_solution_by_name(repaired)["Solution C"])
    assert set(components) == {"Na-acetate", "Distilled water"}
    assert components["Na-acetate"]["concentration"] == {"value": "150", "unit": "G_PER_L"}
    assert "term" not in components["Na-acetate"]
    assert components["Na-acetate"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:32954",
        "label": "sodium acetate",
    }
    assert repaired["parent_media"] == repair_module.DSMZ_861A_PARENT
    assert repaired["variant_relationship"] == "SUBSTITUTED_COMPONENT_VARIANT"
    assert scorer_module.score_parsed([("bacterial/for_dsm_12341.yaml", repaired)]) == []


def test_dsm_12344_uses_propionate_solution_c_and_leaves_ranking(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.KOMODO_861_4)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    components = _composition_by_name(_solution_by_name(repaired)["Solution C"])
    assert set(components) == {"Na-propionate", "Distilled water"}
    assert "term" not in components["Na-propionate"]
    assert components["Na-propionate"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:132106",
        "label": "sodium propionate",
    }
    assert repaired["parent_media"] == repair_module.DSMZ_861A_PARENT
    assert repaired["variant_relationship"] == "SUBSTITUTED_COMPONENT_VARIANT"
    assert scorer_module.score_parsed([("bacterial/for_dsm_12344.yaml", repaired)]) == []


def test_dsm_12343_keeps_komodo_ph_variant(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_861_1)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["ph_range"] == {"min": 7.1, "max": 7.3}
    assert repaired["parent_media"] == repair_module.DSMZ_861A_PARENT
    assert repaired["variant_relationship"] == "PH_VARIANT"


def test_variant_links_are_directional(repair_module) -> None:
    repaired = {
        target.path: repair_module.repair_record(_doc(repair_module, target), target)
        for target in repair_module.TARGETS
    }

    assert repaired[repair_module.KOMODO_861]["parent_media"]["path"] == (
        f"data/normalized_yaml/{repair_module.DSMZ_861}"
    )

    for path in (
        repair_module.KOMODO_861_1,
        repair_module.KOMODO_861_2,
        repair_module.KOMODO_861_3,
        repair_module.KOMODO_861_4,
    ):
        assert repaired[path]["parent_media"]["path"] == f"data/normalized_yaml/{repair_module.DSMZ_861A}"

    for path, doc in repaired.items():
        parent_media = doc.get("parent_media")
        if parent_media is not None:
            assert parent_media["path"] != f"data/normalized_yaml/{path}"


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair_module, root)

    first = repair_module.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in second.items()
    } == {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in first.items()
    }


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_861_4)
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "komodo.medium:861.2"

    with pytest.raises(ValueError, match="expected 'komodo.medium:861.4'"):
        repair_module.repair_record(doc, target)
