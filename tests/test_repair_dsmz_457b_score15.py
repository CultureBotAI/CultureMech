from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_457b_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_457b_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_457b")


def _target(repair, path: str):
    return repair.TARGET_BY_PATH[path]


def _doc(repair, target) -> dict:
    return {
        "id": repair.EXPECTED_IDS[target.path],
        "name": Path(target.path).stem,
        "original_name": target.source_label.replace("KOMODO Medium 457b.1", "For DSM 7526"),
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": target.source_label,
            "term": {
                "id": repair.EXPECTED_SOURCE_TERMS[target.path],
                "label": target.source_label,
            },
        },
        "notes": "Stale commercial TSB/TSA note",
        "ingredients": [
            {"preferred_term": "Dibenzofuran", "concentration": {"value": "8.4", "unit": "G_PER_L"}},
            {"preferred_term": "Dimethyl sulfoxide", "concentration": {"value": "1000", "unit": "G_PER_L"}},
            {"preferred_term": "Agar", "concentration": {"value": "50.0", "unit": "G_PER_L"}},
            {"preferred_term": "Pancreatic digest of casein", "concentration": {"value": "17", "unit": "G_PER_L"}},
        ],
        "curation_history": [],
    }


def _write_minimal_tree(repair, root: Path) -> None:
    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(repair, target), sort_keys=False), encoding="utf-8")


def _by_name(doc: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in doc["ingredients"]}


def test_komodo_457b_duplicate_drops_unrelated_import_rows(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_457B)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired)

    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_value"] == 6.9
    assert len(repaired["ingredients"]) == 15
    assert "Tween 80" in ingredients
    assert {
        "Dibenzofuran",
        "Dimethyl sulfoxide",
        "Agar",
        "Pancreatic digest of casein",
    }.isdisjoint(ingredients)
    assert "wikipedia.org" not in repaired["notes"]


def test_dsm_7526_keeps_fluoranthene_and_leaves_ranking(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.KOMODO_457B_1)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired)

    assert ingredients["Fluoranthene"]["term"] == {
        "id": "CHEBI:33083",
        "label": "fluoranthene",
    }
    assert ingredients["Fluoranthene"]["concentration"] == {
        "value": "0.10",
        "unit": "G_PER_L",
    }
    assert repaired["parent_media"] == repair_module.DSMZ_457B_PARENT
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert scorer_module.score_parsed([("bacterial/for_dsm_7526.yaml", repaired)]) == []


def test_dsm_13022_uses_phenanthrene_and_casamino_acids(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.KOMODO_457B_2)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired)

    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert ingredients["Phenanthrene"]["term"] == {
        "id": "CHEBI:28851",
        "label": "phenanthrene",
    }
    assert ingredients["Casamino acids (DIFCO)"]["term"] == {
        "id": "FOODON:03315719",
        "label": "mammalian milk protein (hydrolyzed)",
    }
    assert scorer_module.score_parsed([("bacterial/for_dsm_13022.yaml", repaired)]) == []


def test_variant_links_are_directional(repair_module) -> None:
    repaired = {
        target.path: repair_module.repair_record(_doc(repair_module, target), target)
        for target in repair_module.TARGETS
    }

    assert [child["path"] for child in repaired[repair_module.DSMZ_457B]["variant_children"]] == [
        f"data/normalized_yaml/{path}"
        for path in (
            repair_module.KOMODO_457B,
            repair_module.KOMODO_457B_1,
            repair_module.KOMODO_457B_2,
        )
    ]
    for path in (repair_module.KOMODO_457B, repair_module.KOMODO_457B_1, repair_module.KOMODO_457B_2):
        assert repaired[path]["parent_media"]["path"] == f"data/normalized_yaml/{repair_module.DSMZ_457B}"
        assert repaired[path]["parent_media"]["path"] != f"data/normalized_yaml/{path}"


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
    target = _target(repair_module, repair_module.KOMODO_457B_1)
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "komodo.medium:457b.2"

    with pytest.raises(ValueError, match="expected 'komodo.medium:457b.1'"):
        repair_module.repair_record(doc, target)
