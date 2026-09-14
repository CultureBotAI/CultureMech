from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_194_desulfobulbus_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_194_desulfobulbus_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_194")


def _target(repair, path: str):
    return repair.TARGET_BY_PATH[path]


def _doc(repair, target) -> dict:
    return {
        "id": repair.EXPECTED_IDS[target.path],
        "name": Path(target.path).stem,
        "original_name": target.source_label,
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
        "notes": "stale note",
        "ingredients": [
            {"preferred_term": "m-Xylene", "concentration": {"value": "0.3", "unit": "G_PER_L"}},
            {
                "preferred_term": "2,2,4,4,6,8,8-Heptamethylnonane",
                "concentration": {"value": "20", "unit": "G_PER_L"},
            },
            {"preferred_term": "FeSO4 x 7 H2O", "concentration": {"value": "80", "unit": "G_PER_L"}},
        ],
        "curation_history": [],
        "parent_media": {"path": "data/normalized_yaml/bacterial/KOMODO_194_DESULFOBULBUS_MEDIUM.yaml"},
        "variant_relationship": "SOURCE_DUPLICATE",
        "variant_children": [
            {
                "path": "data/normalized_yaml/bacterial/desulfovirga_medium.yaml",
                "relationship": "SOURCE_DUPLICATE",
            }
        ],
    }


def _write_minimal_tree(repair, root: Path) -> None:
    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(repair, target), sort_keys=False), encoding="utf-8")


def _by_name(doc: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in doc["ingredients"]}


def test_komodo_194_duplicate_uses_desulfobulbus_components(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_194)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired)

    assert repaired["ph_range"] == {"min": 7.1, "max": 7.4}
    assert len(repaired["ingredients"]) == 30
    assert ingredients["Sodium propionate"]["concentration"] == {"value": "1.50", "unit": "G_PER_L"}
    assert ingredients["NaHCO3"]["term"] == {
        "id": "CHEBI:32139",
        "label": "sodium hydrogencarbonate",
    }
    assert {
        "m-Xylene",
        "2,2,4,4,6,8,8-Heptamethylnonane",
        "FeSO4 x 7 H2O",
    }.isdisjoint(ingredients)
    assert repaired["parent_media"]["id"] == repair_module.EXPECTED_IDS[repair_module.DSMZ_194]


def test_dsm_14880_replaces_propionate_with_pyruvate_and_yeast(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.KOMODO_194_2)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired)

    assert repaired["composition_type"] == "UNDEFINED"
    assert "Sodium propionate" not in ingredients
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Sodium pyruvate"]["concentration"] == {"value": "2.20", "unit": "G_PER_L"}
    assert scorer_module.score_parsed([("bacterial/for_dsm_14880.yaml", repaired)]) == []


def test_dsmz_butyrate_and_putrescine_variants_use_official_replacements(
    repair_module,
    scorer_module,
) -> None:
    dsm_21556 = repair_module.repair_record(
        _doc(repair_module, _target(repair_module, repair_module.KOMODO_194_3)),
        _target(repair_module, repair_module.KOMODO_194_3),
    )
    dsm_13527 = repair_module.repair_record(
        _doc(repair_module, _target(repair_module, repair_module.KOMODO_194_13527)),
        _target(repair_module, repair_module.KOMODO_194_13527),
    )
    dsm_5092 = repair_module.repair_record(
        _doc(repair_module, _target(repair_module, repair_module.KOMODO_194_5092)),
        _target(repair_module, repair_module.KOMODO_194_5092),
    )

    assert _by_name(dsm_21556)["Na-butyrate"]["concentration"] == {
        "value": "1.00",
        "unit": "G_PER_L",
    }
    assert _by_name(dsm_13527)["Na-butyrate"]["concentration"] == {
        "value": "1.00",
        "unit": "G_PER_L",
    }
    assert _by_name(dsm_5092)["putrescine"]["term"] == {
        "id": "CHEBI:17148",
        "label": "putrescine",
    }
    assert "Sodium propionate" not in _by_name(dsm_5092)
    assert scorer_module.score_parsed([("bacterial/for_dsm_21556.yaml", dsm_21556)]) == []


def test_dsm_6523_uses_explicit_komodo_table(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_194_6523)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired)

    assert len(repaired["ingredients"]) == 33
    assert ingredients["Na2WO4 x 2 H2O"]["concentration"] == {
        "value": "0.000364",
        "unit": "G_PER_L",
    }
    assert ingredients["Na2SeO3 x 5 H2O"]["concentration"] == {
        "value": "0.000273",
        "unit": "G_PER_L",
    }


def test_official_194_links_children_and_194a_is_detached(repair_module) -> None:
    official = repair_module.repair_record(
        _doc(repair_module, _target(repair_module, repair_module.DSMZ_194)),
        _target(repair_module, repair_module.DSMZ_194),
    )
    desulfovirga = repair_module.repair_record(
        _doc(repair_module, _target(repair_module, repair_module.DSMZ_194A)),
        _target(repair_module, repair_module.DSMZ_194A),
    )

    assert [child["path"] for child in official["variant_children"]] == [
        f"data/normalized_yaml/{path}"
        for path in (
            repair_module.KOMODO_194,
            repair_module.KOMODO_194_1,
            repair_module.KOMODO_194_2,
            repair_module.KOMODO_194_3,
            repair_module.KOMODO_194_13527,
            repair_module.KOMODO_194_5092,
            repair_module.KOMODO_194_6523,
        )
    ]
    assert "parent_media" not in desulfovirga
    assert "variant_relationship" not in desulfovirga


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
    target = _target(repair_module, repair_module.KOMODO_194_2)
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "komodo.medium:194.3"

    with pytest.raises(ValueError, match="expected 'komodo.medium:194.2'"):
        repair_module.repair_record(doc, target)
