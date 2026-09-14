from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_141_methanogenium_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_141_methanogenium_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_141")


def _ingredient(name: str) -> dict:
    return {
        "preferred_term": name,
        "term": {
            "id": "CHEBI:32588",
            "label": "potassium chloride",
        },
        "concentration": {
            "value": "999",
            "unit": "G_PER_L",
        },
        "notes": " [Merged 2 duplicates: stale]",
    }


def _doc(repair, path: str) -> dict:
    return {
        "id": repair.EXPECTED_IDS[path],
        "name": Path(path).stem,
        "original_name": "For DSM 21626",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
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
            _ingredient("MgSO4 x 7 H2O"),
            _ingredient("CaCl2 x 2 H2O"),
            _ingredient("NaCl"),
            _ingredient("Nitrilotriacetic acid"),
            _ingredient("MnSO4 x H2O"),
            _ingredient("FeSO4 x 7 H2O"),
            _ingredient("CoSO4 x 7 H2O"),
            _ingredient("ZnSO4 x 7 H2O"),
            _ingredient("CuSO4 x 5 H2O"),
            _ingredient("AlK(SO4)2 x 12 H2O"),
            _ingredient("H3BO3"),
            _ingredient("Na2MoO4 x 2 H2O"),
            _ingredient("NiCl2 x 6 H2O"),
            _ingredient("Na2SeO3 x 5 H2O"),
            _ingredient("Na2WO4 x 2 H2O"),
            _ingredient("Biotin"),
            _ingredient("Folic acid"),
            _ingredient("Pyridoxine hydrochloride"),
            _ingredient("Thiamine HCl"),
            _ingredient("Riboflavin"),
            _ingredient("Nicotinic acid"),
            _ingredient("Calcium D-(+)-pantothenate"),
            _ingredient("Vitamin B12"),
            _ingredient("p-Aminobenzoic acid"),
            _ingredient("(DL)-alpha-Lipoic acid"),
            _ingredient("Trypticase peptone"),
        ],
        "curation_history": [],
    }


def _by_name(doc: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in doc["ingredients"]}


def test_repair_dilutes_trace_and_vitamin_stock_rows(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.KOMODO_141),
        repair_module.TARGET_BY_PATH[repair_module.KOMODO_141],
    )
    ingredients = _by_name(repaired)

    assert ingredients["MgSO4 x 7 H2O"]["concentration"] == {
        "value": "3.43535",
        "unit": "G_PER_L",
    }
    assert ingredients["NaCl"]["concentration"] == {
        "value": "17.7789",
        "unit": "G_PER_L",
    }
    assert ingredients["Biotin"]["concentration"] == {
        "value": "0.0000197433",
        "unit": "G_PER_L",
    }
    assert "notes" not in ingredients["MgSO4 x 7 H2O"]
    assert repaired["ph_range"] == {"min": 6.8, "max": 7.0}
    assert repaired["parent_media"] == repair_module.DSMZ_141_SOURCE_PARENT


def test_dsm_21626_reduces_nacl_and_leaves_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.KOMODO_141_11),
        repair_module.TARGET_BY_PATH[repair_module.KOMODO_141_11],
    )
    ingredients = _by_name(repaired)

    assert ingredients["NaCl"]["concentration"] == {
        "value": "6.00",
        "unit": "G_PER_L",
    }
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert scorer_module.score_parsed([(repair_module.KOMODO_141_11, repaired)]) == []


@pytest.mark.parametrize(
    "path",
    (
        "KOMODO_141_3",
        "KOMODO_141_6",
        "KOMODO_141_8",
    ),
)
def test_exact_strain_wrappers_leave_ranking(
    repair_module,
    scorer_module,
    path: str,
) -> None:
    target_path = getattr(repair_module, path)
    repaired = repair_module.repair_record(
        _doc(repair_module, target_path),
        repair_module.TARGET_BY_PATH[target_path],
    )

    assert repaired["parent_media"] == repair_module.DSMZ_141_PARENT
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert repaired["ph_range"] == repair_module.PH_RANGE
    assert scorer_module.score_parsed([(target_path, repaired)]) == []


def test_dsm_2373_increases_trypticase(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.KOMODO_141_5),
        repair_module.TARGET_BY_PATH[repair_module.KOMODO_141_5],
    )
    ingredients = _by_name(repaired)

    assert repaired["ph_value"] == 7.0
    assert "ph_range" not in repaired
    assert ingredients["Trypticase peptone"]["concentration"] == {
        "value": "6.00",
        "unit": "G_PER_L",
    }


def test_dsm_4254_adds_l_histidine(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.KOMODO_141_7),
        repair_module.TARGET_BY_PATH[repair_module.KOMODO_141_7],
    )
    ingredients = _by_name(repaired)

    assert ingredients["L-histidine"]["term"] == {
        "id": "CHEBI:15971",
        "label": "L-histidine",
    }
    assert ingredients["L-histidine"]["concentration"] == {
        "value": "0.08",
        "unit": "G_PER_L",
    }


def test_variant_children_are_bidirectional(repair_module) -> None:
    repaired = {
        target.path: repair_module.repair_record(_doc(repair_module, target.path), target)
        for target in repair_module.TARGETS
    }

    assert [child["path"] for child in repaired[repair_module.DSMZ_141]["variant_children"]] == [
        f"data/normalized_yaml/{repair_module.KOMODO_141}",
        f"data/normalized_yaml/{repair_module.KOMODO_141_3}",
        f"data/normalized_yaml/{repair_module.KOMODO_141_5}",
        f"data/normalized_yaml/{repair_module.KOMODO_141_6}",
        f"data/normalized_yaml/{repair_module.KOMODO_141_7}",
        f"data/normalized_yaml/{repair_module.KOMODO_141_8}",
        f"data/normalized_yaml/{repair_module.KOMODO_141_11}",
    ]
    for path in (
        repair_module.KOMODO_141,
        repair_module.KOMODO_141_3,
        repair_module.KOMODO_141_5,
        repair_module.KOMODO_141_6,
        repair_module.KOMODO_141_7,
        repair_module.KOMODO_141_8,
        repair_module.KOMODO_141_11,
    ):
        assert (
            repaired[path]["parent_media"]["path"]
            == f"data/normalized_yaml/{repair_module.DSMZ_141}"
        )


def test_refuses_unexpected_source_term(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.KOMODO_141_5]
    doc = _doc(repair_module, target.path)
    doc["media_term"]["term"]["id"] = "komodo.medium:141.7"

    with pytest.raises(ValueError, match="expected 'komodo.medium:141.5'"):
        repair_module.repair_record(doc, target)


def test_plan_repairs_is_idempotent(tmp_path: Path, repair_module) -> None:
    root = tmp_path / "normalized_yaml"
    for target in repair_module.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(repair_module, target.path), sort_keys=False))

    for path, doc in repair_module.plan_repairs(root).items():
        path.write_bytes(repair_module.dump_record(doc).encode("utf-8"))

    assert repair_module.plan_repairs(root) == {
        path: yaml.load(path.read_text(), Loader=repair_module.YAML_LOADER)
        for path in sorted(root.rglob("*.yaml"))
    }
