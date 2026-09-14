from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_host_cell_score25.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_host_cell_score25")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_host_cells")


def _doc(target) -> dict:
    dsmz_number = target.dsmz_number
    return {
        "id": target.expected_id,
        "name": Path(target.path).stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": f"DSMZ Medium {dsmz_number}",
            "term": {"id": target.expected_source, "label": f"DSMZ Medium {dsmz_number}"},
        },
        "ingredients": [
            {
                "preferred_term": "stale",
                "concentration": {"value": "45", "unit": "G_PER_L"},
            }
        ],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def _write_targets(repair, root: Path) -> None:
    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(target), sort_keys=False), encoding="utf-8")


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for row in doc["ingredients"]:
        if row["preferred_term"] == preferred_term:
            return row
    raise AssertionError(f"missing ingredient {preferred_term!r}")


def test_repair_scales_dsmz_1193_volumes_and_adds_mediadive_terms(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(target), target)

    imdm = _ingredient(repaired, "IMDM-Medium")
    assert imdm["concentration"] == {"value": "891.089109", "unit": "ML_PER_L"}
    assert imdm["term"] == {"id": "mediadive.compound:1069", "label": "IMDM-Medium"}

    fbs = _ingredient(repaired, "Fetal bovine serum")
    assert fbs["concentration"] == {"value": "99.009901", "unit": "ML_PER_L"}
    assert fbs["term"] == {
        "id": "mediadive.compound:954",
        "label": "Fetal bovine serum",
    }

    aminoacids = _ingredient(repaired, "Aminoacids (100 x)")
    assert aminoacids["concentration"] == {"value": "9.90099", "unit": "ML_PER_L"}
    assert aminoacids["chebi_term"] == {"id": "CHEBI:33709", "label": "amino acid"}

    assert repaired["temperature_value"] == 37.0
    assert repaired["sterilization"] == {"method": "FILTER"}
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_uses_mem_for_dsmz_1503(repair_module) -> None:
    target = repair_module.TARGETS[1]
    repaired = repair_module.repair_record(_doc(target), target)

    assert _ingredient(repaired, "MEM-Medium")["term"] == {
        "id": "mediadive.compound:1377",
        "label": "MEM-Medium",
    }


def test_repair_splits_dsmz_1311_culture_and_infection_media(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[-1]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["ingredients"] == []
    assert [solution["preferred_term"] for solution in repaired["solutions"]] == [
        "XTC-2 cell culture medium",
        "XTC-2 infection medium",
    ]
    assert [
        row["concentration"]
        for row in repaired["solutions"][0]["composition"]
        if row["preferred_term"] == "Leibovitz's L-15 medium"
    ] == [{"value": "930.0", "unit": "ML_PER_L"}]
    assert [
        row["concentration"]
        for row in repaired["solutions"][1]["composition"]
        if row["preferred_term"] == "Fetal bovine serum"
    ] == [{"value": "20.0", "unit": "ML_PER_L"}]
    assert [
        row["chebi_term"]
        for row in repaired["solutions"][1]["composition"]
        if row["preferred_term"] == "Glutamine"
    ] == [{"id": "CHEBI:18050", "label": "L-glutamine"}]
    assert scorer_module.score_record(repaired) == (0, [])


def test_plan_repairs_adds_references_and_is_idempotent(
    repair_module,
    tmp_path: Path,
) -> None:
    root = tmp_path / "normalized"
    _write_targets(repair_module, root)

    first = repair_module.plan_repairs(root)
    assert {path.relative_to(root).as_posix() for path in first} == {
        target.path for target in repair_module.TARGETS
    }

    for path, doc in first.items():
        assert doc["data_quality_flags"] == [
            "ingredients_curated",
            "has_ontology_mappings",
        ]
        assert doc["references"] == [
            {
                "reference": next(
                    target.source_url
                    for target in repair_module.TARGETS
                    if target.path == path.relative_to(root).as_posix()
                )
            }
        ]
        assert doc["curation_history"][-1]["action"] == repair_module.ACTION
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    assert repair_module.plan_repairs(root) == {}


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:000636'"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:9999"

    with pytest.raises(ValueError, match="expected 'mediadive.medium:1193'"):
        repair_module.repair_record(doc, target)
