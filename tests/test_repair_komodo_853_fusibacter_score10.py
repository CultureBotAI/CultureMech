from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_853_fusibacter_score10.py"
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
    return _load_script(SCRIPT, "repair_komodo_853_fusibacter")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_853")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_strain_pointer_exits_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_variant(
        repair_module.STRAIN_CHILD.path,
        _load_yaml(repair_module.NORMALIZED / repair_module.STRAIN_CHILD.path),
    )

    assert repaired["parent_media"]["relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert repaired["variant_modifications"] == [
        repair_module._variant_notes(repair_module.STRAIN_CHILD)
    ]
    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed(
        [(str(repair_module.STRAIN_CHILD.path), repaired)]
    ) == []


def test_parent_is_promoted_and_lists_expected_variants(repair_module) -> None:
    repaired = repair_module.repair_parent(
        _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    )

    assert "parent_media" not in repaired
    assert "variant_relationship" not in repaired
    assert "variant_modifications" not in repaired
    assert repaired["variant_children"] == [
        repair_module._variant_entry(variant) for variant in repair_module.VARIANTS
    ]


@pytest.mark.parametrize(
    "variant",
    tuple(_load_script(SCRIPT, "komodo_853_variants").VARIANTS),
)
def test_variants_link_to_parent(repair_module, variant) -> None:
    repaired = repair_module.repair_variant(
        variant.path,
        _load_yaml(repair_module.NORMALIZED / variant.path),
    )

    assert repaired["parent_media"]["relationship"] == variant.relationship
    assert repaired["variant_relationship"] == variant.relationship
    assert repaired["variant_modifications"] == [
        repair_module._variant_notes(variant)
    ]
    assert "ingredients_curated" in repaired["data_quality_flags"]


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.plan_repairs()
    twice = {
        path: repair_module.repair_parent(doc)
        if path == repair_module.NORMALIZED / repair_module.PARENT
        else repair_module.repair_variant(
            path.relative_to(repair_module.NORMALIZED),
            doc,
        )
        for path, doc in once.items()
    }

    assert twice == once
    for path in once:
        assert repair_module.dump_record(twice[path]) == repair_module.dump_record(
            once[path]
        )


def test_plan_repairs_targets_current_records(repair_module) -> None:
    expected = {
        repair_module.NORMALIZED / repair_module.PARENT: repair_module.repair_parent(
            _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
        )
    }
    for variant in repair_module.VARIANTS:
        path = repair_module.NORMALIZED / variant.path
        expected[path] = repair_module.repair_variant(variant.path, _load_yaml(path))

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_strain_child_source(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.STRAIN_CHILD.path)
    doc["media_term"]["term"]["id"] = "komodo.medium:wrong"

    with pytest.raises(ValueError, match=repair_module.STRAIN_CHILD.source_term):
        repair_module.repair_variant(repair_module.STRAIN_CHILD.path, doc)


def test_repair_rejects_concentration_variant_ingredient_drift(
    repair_module,
) -> None:
    variant = repair_module.VARIANTS[2]
    doc = _load_yaml(repair_module.NORMALIZED / variant.path)
    doc["ingredients"][0]["preferred_term"] = "Glucose"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_variant(variant.path, doc)
