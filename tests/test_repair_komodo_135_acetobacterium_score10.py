from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_135_acetobacterium_score10.py"
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
    return _load_script(SCRIPT, "repair_komodo_135_acetobacterium")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_135")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize(
    "child_path",
    [Path("bacterial/for_dsm_1974.yaml"), Path("bacterial/for_dsm_4132.yaml")],
)
def test_ranked_strain_records_exit_review_ranking(
    repair_module,
    scorer_module,
    child_path: Path,
) -> None:
    child = repair_module.CHILD_BY_PATH[child_path]
    repaired = repair_module.repair_child(
        child.path,
        _load_yaml(repair_module.NORMALIZED / child.path),
    )

    assert repaired["parent_media"] == repair_module._parent_ref()
    assert repaired["variant_relationship"] == "PH_VARIANT"
    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(child.path), repaired)]) == []


def test_parent_lists_all_135_children(repair_module) -> None:
    repaired = repair_module.repair_parent(
        _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    )

    assert "parent_media" not in repaired
    assert "variant_relationship" not in repaired
    assert "variant_modifications" not in repaired
    assert repaired["variant_children"] == [
        repair_module._child_entry(child) for child in repair_module.CHILDREN
    ]
    assert "ingredients_curated" in repaired["data_quality_flags"]


@pytest.mark.parametrize("child", tuple(_load_script(SCRIPT, "komodo_135").CHILDREN))
def test_children_link_to_135a_parent(repair_module, child) -> None:
    repaired = repair_module.repair_child(
        child.path,
        _load_yaml(repair_module.NORMALIZED / child.path),
    )

    assert repaired["parent_media"] == repair_module._parent_ref()
    assert repaired["variant_relationship"] == "PH_VARIANT"
    assert repaired["variant_modifications"] == [child.notes]


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.plan_repairs()
    twice = {
        path: (
            repair_module.repair_parent(doc)
            if path == repair_module.NORMALIZED / repair_module.PARENT
            else repair_module.repair_child(
                path.relative_to(repair_module.NORMALIZED),
                doc,
            )
        )
        for path, doc in once.items()
    }

    assert twice == once
    for path in once:
        assert repair_module.dump_record(twice[path]) == repair_module.dump_record(once[path])


def test_plan_repairs_targets_current_records(repair_module) -> None:
    expected = {
        repair_module.NORMALIZED
        / repair_module.PARENT: repair_module.repair_parent(
            _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
        ),
    }
    for child in repair_module.CHILDREN:
        path = repair_module.NORMALIZED / child.path
        expected[path] = repair_module.repair_child(child.path, _load_yaml(path))

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_parent_source(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    doc["media_term"]["term"]["id"] = "mediadive.medium:wrong"

    with pytest.raises(ValueError, match=repair_module.PARENT_SOURCE_TERM):
        repair_module.repair_parent(doc)


def test_repair_rejects_wrong_child_id(repair_module) -> None:
    child = repair_module.CHILD_BY_PATH[Path("bacterial/for_dsm_1974.yaml")]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=child.record_id):
        repair_module.repair_child(child.path, doc)


def test_repair_rejects_wrong_child_ph(repair_module) -> None:
    child = repair_module.CHILD_BY_PATH[Path("bacterial/for_dsm_4132.yaml")]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["ph_value"] = 6.5

    with pytest.raises(ValueError, match="expected pH"):
        repair_module.repair_child(child.path, doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    child = repair_module.CHILD_BY_PATH[Path("bacterial/for_dsm_1974.yaml")]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["ingredients"][0]["preferred_term"] = "Glucose"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_child(child.path, doc)
