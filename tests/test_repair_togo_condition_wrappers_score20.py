from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_condition_wrappers_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_condition_wrappers_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_condition_wrappers")


def _doc(repair, update) -> dict:
    return {
        "id": repair.EXPECTED_IDS[update.path],
        "name": Path(update.path).stem,
        "media_term": {
            "preferred_term": update.reference_url,
            "term": {"id": repair.EXPECTED_SOURCE_TERMS[update.path]},
        },
        "ingredients": [
            {
                "preferred_term": ingredient["preferred_term"],
                "concentration": {"value": "1", "unit": "G_PER_L"},
            }
            for ingredient in update.recipe["ingredients"]
        ],
        "curation_history": [],
    }


def _target(repair, path: str):
    return repair.UPDATE_BY_PATH[path]


def _write_minimal_tree(repair, root: Path) -> None:
    for update in repair.UPDATES:
        path = root / update.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(_doc(repair, update), sort_keys=False),
            encoding="utf-8",
        )


@pytest.mark.parametrize(
    ("path", "temperature"),
    [
        ("M2194_NUTRIENT_DIFCO", 30.0),
        ("M2225_MRS_BIOKAR", 37.0),
        ("M2490_MRS_ERYTHROMYCIN", 37.0),
        ("M2795_MRS_CYSTEINE", 37.0),
        ("M2891_PPLO_CO2", 37.0),
        ("M2896_THB_CO2", 37.0),
    ],
)
def test_wrappers_score_cleanly_after_repair(
    repair_module,
    scorer_module,
    path: str,
    temperature: float,
) -> None:
    update = _target(repair_module, getattr(repair_module, path))

    repaired = repair_module.repair_wrapper(_doc(repair_module, update), update)

    assert repaired["temperature_value"] == temperature
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_mrs_erythromycin_converts_ug_per_ml_to_mg_per_l(repair_module) -> None:
    update = _target(repair_module, repair_module.M2490_MRS_ERYTHROMYCIN)

    repaired = repair_module.repair_wrapper(_doc(repair_module, update), update)

    assert repaired["ingredients"][0] == {
        "preferred_term": "erythromycin",
        "concentration": {"value": "5", "unit": "MG_PER_L"},
        "source": "TOGO M2490",
        "notes": (
            "TOGO M2490 lists erythromycin at 5 ug/ml; this is stored as the " "equivalent 5 mg/L."
        ),
        "term": {"id": "CHEBI:48923", "label": "erythromycin"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:48923",
            "label": "erythromycin",
        },
        "cellular_metabolic_roles": ["INHIBITOR"],
    }


def test_mrs_powder_rows_keep_ph_ranges(repair_module) -> None:
    nutrient = repair_module.repair_wrapper(
        _doc(repair_module, _target(repair_module, repair_module.M2194_NUTRIENT_DIFCO)),
        _target(repair_module, repair_module.M2194_NUTRIENT_DIFCO),
    )
    mrs = repair_module.repair_wrapper(
        _doc(repair_module, _target(repair_module, repair_module.M2225_MRS_BIOKAR)),
        _target(repair_module, repair_module.M2225_MRS_BIOKAR),
    )

    assert nutrient["ph_range"] == {"min": 6.6, "max": 7.0}
    assert mrs["ph_range"] == {"min": 6.2, "max": 6.6}


def test_pplo_and_todd_hewitt_capture_five_percent_co2(repair_module) -> None:
    for path in (repair_module.M2891_PPLO_CO2, repair_module.M2896_THB_CO2):
        update = _target(repair_module, path)
        repaired = repair_module.repair_wrapper(_doc(repair_module, update), update)

        assert repaired["ingredients"][1] == {
            "preferred_term": "CO2",
            "concentration": {"value": "5", "unit": "PERCENT_V_V"},
            "source": update.reference_url.replace("https://togomedium.org/medium/", "TOGO "),
            "notes": (
                f'{update.reference_url.replace("https://togomedium.org/medium/", "TOGO ")} '
                "lists 5% CO2 as the incubation atmosphere."
            ),
            "term": {"id": "CHEBI:16526", "label": "carbon dioxide"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:16526",
                "label": "carbon dioxide",
            },
        }


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


def test_repair_rejects_wrong_source(repair_module) -> None:
    update = _target(repair_module, repair_module.M2891_PPLO_CO2)
    doc = _doc(repair_module, update)
    doc["media_term"]["term"]["id"] = "TOGO:M2896"

    with pytest.raises(ValueError, match="expected 'TOGO:M2891'"):
        repair_module.repair_wrapper(doc, update)


def test_repair_rejects_wrong_components(repair_module) -> None:
    update = _target(repair_module, repair_module.M2490_MRS_ERYTHROMYCIN)
    doc = _doc(repair_module, update)
    doc["ingredients"][0]["preferred_term"] = "ampicillin"

    with pytest.raises(ValueError, match="expected"):
        repair_module.repair_wrapper(doc, update)
