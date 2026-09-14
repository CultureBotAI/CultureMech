from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_215c_strict_anaerobes_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_komodo_215c_strict_anaerobes_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_215c")


def _doc(repair, target) -> dict:
    return {
        "id": repair.EXPECTED_IDS[target.path],
        "name": Path(target.path).stem,
        "original_name": (
            "For DSM 10643" if target.path == repair.KOMODO_215C_1 else target.source_label
        ),
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": target.source_label,
            "term": {
                "id": repair.EXPECTED_SOURCE_TERMS[target.path],
                "label": target.source_label,
            },
        },
        "notes": "Commercial Product: Brain Heart Infusion\nSource: https://microbenotes.com/brain-heart-infusion-bhi-agar/",
        "ingredients": [
            {
                "preferred_term": "Calf brains",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            }
        ],
        "curation_history": [],
    }


def _write_minimal_tree(repair, root: Path) -> None:
    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(_doc(repair, target), sort_keys=False),
            encoding="utf-8",
        )


def _target(repair, path: str):
    return repair.TARGET_BY_PATH[path]


def _ingredient_by_name(doc: dict) -> dict[str, dict]:
    return {ingredient["preferred_term"]: ingredient for ingredient in doc["ingredients"]}


def test_dsmz_215c_is_official_four_component_recipe(repair_module) -> None:
    target = _target(repair_module, repair_module.DSMZ_215C)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        "Brain heart infusion",
        "L-Cysteine HCl x H2O",
        "Na2S x 9 H2O",
        "Distilled water",
    ]
    assert repaired["ph_range"] == {"min": 7.2, "max": 7.6}
    assert "MicrobeNotes" not in repaired["notes"]
    assert repaired["variant_children"] == [repair_module.DSMZ_CHILD]


def test_komodo_215c_materializes_n2_and_links_to_dsmz(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_215C)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    ingredients = _ingredient_by_name(repaired)
    assert ingredients["N2"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert repaired["parent_media"] == repair_module.DSMZ_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_children"] == [
        repair_module.KOMODO_10643_CHILD,
        repair_module.KOMODO_15692_CHILD,
        repair_module.KOMODO_19851_CHILD,
    ]


def test_for_dsm_10643_gets_glycerol_and_leaves_review_ranking(
    repair_module, scorer_module
) -> None:
    target = _target(repair_module, repair_module.KOMODO_215C_1)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    ingredients = _ingredient_by_name(repaired)
    assert ingredients["glycerol"]["concentration"] == {"value": "8.70", "unit": "G_PER_L"}
    assert repaired["parent_media"] == repair_module.KOMODO_PARENT
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert scorer_module.score_parsed([("bacterial/for_dsm_10643.yaml", repaired)]) == []


def test_for_dsm_15692_keeps_ph_and_adds_bicarbonate_context(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_215C_2)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    ingredients = _ingredient_by_name(repaired)
    assert repaired["ph_value"] == 7.2
    assert ingredients["NaHCO3"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert repaired["parent_media"] == repair_module.KOMODO_PARENT
    assert ingredients["CO2"]["term"] == {"id": "CHEBI:16526", "label": "carbon dioxide"}


def test_for_dsm_19851_restores_komodo_specific_supplements(repair_module, scorer_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_215C_3)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    ingredients = _ingredient_by_name(repaired)
    assert ingredients["Brain heart infusion"]["concentration"] == {
        "value": "36.63",
        "unit": "G_PER_L",
    }
    assert ingredients["ethanol"]["term"] == {"id": "CHEBI:16236", "label": "ethanol"}
    assert ingredients["Vitamin K1"]["term"] == {"id": "CHEBI:18067", "label": "phylloquinone"}
    assert ingredients["haemin"]["term"] == {"id": "CHEBI:50385", "label": "hemin"}
    assert repaired["parent_media"] == repair_module.KOMODO_PARENT
    assert scorer_module.score_parsed([("bacterial/for_dsm_19851.yaml", repaired)]) == []


def test_variant_links_are_directional(repair_module) -> None:
    repaired = {
        target.path: repair_module.repair_record(_doc(repair_module, target), target)
        for target in repair_module.TARGETS
    }

    assert repaired[repair_module.KOMODO_215C]["parent_media"]["path"] == (
        f"data/normalized_yaml/{repair_module.DSMZ_215C}"
    )

    strain_variants = (
        repair_module.KOMODO_215C_1,
        repair_module.KOMODO_215C_2,
        repair_module.KOMODO_215C_3,
    )
    for path in strain_variants:
        assert repaired[path]["parent_media"]["path"] == (
            f"data/normalized_yaml/{repair_module.KOMODO_215C}"
        )

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
        path.relative_to(root): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(root): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_215C_1)
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:004422'"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_215C_3)
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "komodo.medium:215c.1"

    with pytest.raises(ValueError, match="expected 'komodo.medium:215c.3'"):
        repair_module.repair_record(doc, target)
