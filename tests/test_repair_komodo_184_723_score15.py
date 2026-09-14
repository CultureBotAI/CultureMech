from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_184_723_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_komodo_184_723_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_184_723")


def _doc(target) -> dict:
    label = target.media_term_id.removeprefix("komodo.medium:")
    return {
        "id": target.record_id,
        "name": Path(target.path).stem,
        "original_name": "PICROPHILUS medium" if label == "723" else "DESULFUROCOCCUS medium",
        "category": "archaea",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 1.0 if label == "723" else 5.5,
        "media_term": {
            "preferred_term": f"KOMODO Medium {label}",
            "term": {"id": target.media_term_id, "label": f"KOMODO {label}"},
        },
        "notes": "Source: KOMODO ModelSEED",
        "ingredients": [
            {
                "preferred_term": "H2SO4",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            }
        ],
        "curation_history": [],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing {preferred_term!r}")


def test_repair_expands_desulfurococcus_table(repair_module, scorer_module) -> None:
    target = repair_module.TARGET_BY_PATH[
        "archaea/KOMODO_184_DESULFUROCOCCUS_medium.yaml"
    ]

    repaired = repair_module.repair_record(_doc(target), target)

    assert len(repaired["ingredients"]) == 20
    assert _ingredient(repaired, "Sulfur")["concentration"] == {
        "value": "5.00",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2S x 9 H2O")["term"] == {
        "id": "CHEBI:76209",
        "label": "sodium sulfide nonahydrate",
    }
    assert _ingredient(repaired, "N2")["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert _ingredient(repaired, "H2SO4")["source"] == "KOMODO Medium 184"
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_expands_picrophilus_table(repair_module, scorer_module) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/KOMODO_723_PICROPHILUS_medium.yaml"]

    repaired = repair_module.repair_record(_doc(target), target)

    assert len(repaired["ingredients"]) == 15
    assert _ingredient(repaired, "Yeast extract")["concentration"] == {
        "value": "3.00",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "H2O")["term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert _ingredient(repaired, "H2SO4")["source"] == "KOMODO Medium 723"
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/KOMODO_723_PICROPHILUS_medium.yaml"]

    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [
        {"reference": repair_module.KOMODO_723_URL},
        {"reference": repair_module.DSMZ_723_PDF},
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.KOMODO_723_URL,
            "notes": (
                "Replaced the one-row H2SO4 placeholder with the KOMODO Medium "
                "723 metabolite table and kept the DSMZ PDF linked from KOMODO "
                "as a reference."
            ),
        }
    ]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    for target in repair_module.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(target), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(root)
    for repaired_path, doc in first.items():
        repaired_path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in second.items()
    } == {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in first.items()
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/KOMODO_723_PICROPHILUS_medium.yaml"]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/KOMODO_723_PICROPHILUS_medium.yaml"]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "komodo.medium:184"

    with pytest.raises(ValueError, match=target.media_term_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/KOMODO_723_PICROPHILUS_medium.yaml"]
    doc = _doc(target)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)
