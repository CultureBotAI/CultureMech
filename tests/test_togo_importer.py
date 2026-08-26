from __future__ import annotations

import importlib
from pathlib import Path

TogoImporter = importlib.import_module("culturemech.import.togo_importer").TogoImporter


def importer() -> TogoImporter:
    return TogoImporter.__new__(TogoImporter)


def assembled_payload() -> dict:
    return {
        "meta": {"gm": "http://togomedium.org/medium/M1", "name": "Two-batch medium"},
        "components": [
            {
                "paragraph_index": 1,
                "subcomponent_name": "",
                "items": [
                    {
                        "component_name": "Solution A:",
                        "volume": 100,
                        "unit": "ml",
                        "reference_media_id": "M1",
                    },
                    {
                        "component_name": "Solution B:",
                        "volume": 200,
                        "unit": "ml",
                        "reference_media_id": "M1",
                    },
                ],
            },
            {
                "paragraph_index": 3,
                "subcomponent_name": "Solution A",
                "items": [
                    {"component_name": "Water", "volume": 100, "unit": "ml"},
                    {"component_name": "Salt", "volume": 10, "unit": "g"},
                    {"component_name": "NaOH", "conc_value": 5, "conc_unit": "M"},
                ],
            },
            {
                "paragraph_index": 6,
                "subcomponent_name": "Solution B",
                "items": [{"component_name": "Water", "volume": 200, "unit": "ml"}],
            },
        ],
        "comments": [
            {"paragraph_index": 4, "comment": "Adjust pH and filter sterilize."},
            {"paragraph_index": 7, "comment": "Combine both solutions."},
        ],
    }


def test_bare_millilitres_map_to_volume_per_litre() -> None:
    assert importer()._parse_unit("ml") == "ML_PER_L"
    assert importer()._parse_unit("ml/L") == "ML_PER_L"


def test_complete_local_batches_are_not_flattened() -> None:
    recipe = importer()._convert_to_culturemech(assembled_payload())

    assert recipe is not None
    assert recipe["ingredients"] == []
    assert [row["preferred_term"] for row in recipe["solutions"]] == [
        "Solution A",
        "Solution B",
    ]
    assert [row["concentration"] for row in recipe["solutions"]] == [
        {"value": "333.333", "unit": "ML_PER_L"},
        {"value": "666.667", "unit": "ML_PER_L"},
    ]
    assert recipe["solutions"][0]["composition"] == [
        {
            "preferred_term": "Water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
        },
        {
            "preferred_term": "Salt",
            "concentration": {"value": "100", "unit": "G_PER_L"},
        },
    ]
    assert "NaOH" not in {row["preferred_term"] for row in recipe["solutions"][0]["composition"]}
    assert len(recipe["preparation_steps"]) == 2


def test_local_stock_addition_is_not_mistaken_for_a_complete_batch() -> None:
    payload = assembled_payload()
    payload["components"][0]["items"][0]["volume"] = 10

    assert importer()._extract_assembled_solutions(payload) == []
    recipe = importer()._convert_to_culturemech(payload)
    assert recipe is not None
    assert recipe.get("ingredients") in (None, [])
    assert [row["preferred_term"] for row in recipe["solutions"]] == [
        "Solution A",
        "Solution B",
    ]
    assert recipe["solutions"][0]["composition"] == []
    assert recipe["solutions"][1]["composition"] == [
        {
            "preferred_term": "Water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
        }
    ]


def test_main_solution_sections_define_the_final_recipe_layer() -> None:
    payload = {
        "meta": {"gm": "http://togomedium.org/medium/M2", "name": "Layered medium"},
        "components": [
            {
                "paragraph_index": 1,
                "subcomponent_name": "main solution 1",
                "items": [
                    {"component_name": "NaCl", "volume": 2, "unit": "g"},
                    {
                        "component_name": "Trace stock",
                        "volume": 3,
                        "unit": "ml",
                        "reference_media_id": "M2",
                    },
                    {
                        "component_name": "Nitrogen gas",
                        "gmo_id": "GMO_1",
                        "properties": [{"label": "Gas"}],
                    },
                    {
                        "component_name": "KOH",
                        "gmo_id": "GMO_KOH",
                        "properties": [{"label": "Solution"}],
                    },
                    {
                        "component_name": "sodium pyruvate",
                        "gmo_id": "GMO_PYRUVATE",
                        "conc_value": 20,
                        "conc_unit": "mM",
                        "properties": [{"label": "Solution"}],
                    },
                    {
                        "component_name": "NaHCO3 stock solution",
                        "gmo_id": "GMO_BICARBONATE",
                        "properties": [{"label": "Solution"}],
                    },
                ],
            },
            {
                "paragraph_index": 2,
                "subcomponent_name": "main solution 2",
                "items": [
                    {
                        "component_name": "Nitrogen gas",
                        "gmo_id": "GMO_1",
                        "properties": [{"id": "GMO_000077", "label": "Gas"}],
                    }
                ],
            },
            {
                "paragraph_index": 3,
                "subcomponent_name": "Trace stock",
                "items": [
                    {
                        "component_name": "Water",
                        "volume": 3,
                        "unit": "ml",
                        "gmo_id": "GMO_001001",
                    },
                    {"component_name": "ZnCl2", "volume": 1, "unit": "g"},
                ],
            },
        ],
    }

    recipe = importer()._convert_to_culturemech(payload)

    assert recipe is not None
    assert [row["preferred_term"] for row in recipe["ingredients"]] == [
        "NaCl",
        "Nitrogen gas",
        "sodium pyruvate",
    ]
    assert recipe["ingredients"][1]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert recipe["ingredients"][2]["concentration"] == {
        "value": "20",
        "unit": "MILLIMOLAR",
    }
    assert recipe["solutions"] == [
        {
            "preferred_term": "Trace stock",
            "composition": [
                {
                    "preferred_term": "Water",
                    "concentration": {"value": "1000", "unit": "ML_PER_L"},
                },
                {
                    "preferred_term": "ZnCl2",
                    "concentration": {
                        "value": "333.333333333",
                        "unit": "G_PER_L",
                    },
                },
            ],
            "concentration": {"value": "3", "unit": "ML_PER_L"},
            "notes": (
                "Defined in TOGO medium M2. Local TOGO stock formulation is represented "
                "as an inline composition; it is not flattened into final-medium ingredients."
            ),
        }
    ]
    assert "ZnCl2" not in {row["preferred_term"] for row in recipe["ingredients"]}


def test_importer_module_is_repo_local() -> None:
    module_path = Path(importlib.import_module("culturemech.import.togo_importer").__file__)
    assert module_path.name == "togo_importer.py"
