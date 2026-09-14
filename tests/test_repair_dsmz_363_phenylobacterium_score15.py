from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_363_phenylobacterium_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_363_phenylobacterium_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_363")


def _doc(repair, path: str) -> dict:
    return {
        "id": repair.EXPECTED_IDS[path],
        "name": Path(path).stem,
        "original_name": "For DSM 2118",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "stale",
            "term": {
                "id": repair.EXPECTED_SOURCE_TERMS[path],
                "label": "stale",
            },
        },
        "notes": "Source: KOMODO ModelSEED",
        "ingredients": [
            {
                "preferred_term": "Antipyrine",
                "term": {
                    "id": "CHEBI:31225",
                    "label": "antipyrine",
                },
                "concentration": {
                    "value": "1",
                    "unit": "G_PER_L",
                },
            },
            {
                "preferred_term": "KH2PO4",
                "term": {
                    "id": "CHEBI:63036",
                    "label": "potassium dihydrogen phosphate",
                },
                "concentration": {
                    "value": "0.3",
                    "unit": "G_PER_L",
                },
            },
        ],
        "curation_history": [],
        "parent_media": {
            "path": "data/normalized_yaml/bacterial/KOMODO_363_PHENYLOBACTERIUM_MEDIUM.yaml",
            "relationship": "SOURCE_DUPLICATE",
        },
        "variant_relationship": "SOURCE_DUPLICATE",
        "variant_modifications": [
            "Same ingredient and concentration signature; review as possible duplicate source record.",
        ],
    }


def _by_name(doc: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in doc["ingredients"]}


def test_dsm_2118_substitutes_l_phenylalanine(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_for_dsm_2118(_doc(repair_module, repair_module.KOMODO_363_1))
    ingredients = _by_name(repaired)

    assert "Antipyrine" not in ingredients
    assert ingredients["L-phenylalanine"]["concentration"] == {
        "value": "1.00",
        "unit": "G_PER_L",
    }
    assert ingredients["L-phenylalanine"]["term"] == {
        "id": "CHEBI:17295",
        "label": "L-phenylalanine",
    }
    assert repaired["parent_media"] == repair_module.KOMODO_363_PARENT
    assert repaired["variant_relationship"] == "SUBSTITUTED_COMPONENT_VARIANT"
    assert repaired["variant_modifications"] == [repair_module.SUBSTITUTION_NOTES]
    assert "ph_value" not in repaired
    assert "preparation_steps" not in repaired
    assert scorer_module.score_parsed([(repair_module.KOMODO_363_1, repaired)]) == []


def test_komodo_363_parent_links_child_as_substitution(repair_module) -> None:
    doc = _doc(repair_module, repair_module.KOMODO_363)
    doc["variant_children"] = [
        {
            "path": "data/normalized_yaml/bacterial/for_dsm_2118.yaml",
            "relationship": "SOURCE_DUPLICATE",
        },
    ]

    repaired = repair_module.repair_komodo_363_parent(doc)

    assert repaired["variant_children"] == [repair_module.KOMODO_363_1_CHILD]


def test_refuses_unexpected_source_term(repair_module) -> None:
    doc = _doc(repair_module, repair_module.KOMODO_363_1)
    doc["media_term"]["term"]["id"] = "komodo.medium:363"

    with pytest.raises(ValueError, match="expected 'komodo.medium:363.1'"):
        repair_module.repair_for_dsm_2118(doc)


def test_plan_repairs_is_idempotent(tmp_path: Path, repair_module) -> None:
    root = tmp_path / "normalized_yaml"
    for path in (repair_module.KOMODO_363, repair_module.KOMODO_363_1):
        yaml_path = root / path
        yaml_path.parent.mkdir(parents=True, exist_ok=True)
        yaml_path.write_text(yaml.safe_dump(_doc(repair_module, path), sort_keys=False))

    for path, doc in repair_module.plan_repairs(root).items():
        path.write_bytes(repair_module.dump_record(doc).encode("utf-8"))

    assert repair_module.plan_repairs(root) == {
        path: yaml.load(path.read_text(), Loader=repair_module.YAML_LOADER)
        for path in sorted(root.rglob("*.yaml"))
    }
