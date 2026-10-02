from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "import_nbrc_live_candidates.py"


def load_script():
    spec = importlib.util.spec_from_file_location("import_nbrc_live_candidates", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_parse_composition_uses_adjust_ph_to_rows_as_final_ph() -> None:
    module = load_script()

    rows = [
        ["NaCl", "1", "g"],
        ["pH 2.0"],
        ["Adjust pH to 3.0 with 10N H2SO4"],
        [
            "For solid medium, equal volumes of separately autoclaved double-strength "
            "liquid medium (pH 2.0) and 1.6% Gelrite are mixed."
        ],
    ]

    _, _, steps, ph = module.parse_composition(rows)

    assert ph == 3.0
    assert steps == [
        "Adjust pH to 3.0 with 10N H2SO4",
        (
            "For solid medium, equal volumes of separately autoclaved double-strength "
            "liquid medium (pH 2.0) and 1.6% Gelrite are mixed."
        ),
    ]


def test_parse_composition_preserves_ph_range_preparation_rows() -> None:
    module = load_script()

    row = (
        "Dissolve and neutralize the nitrilotriacetic acid with KOH (7.3 g); "
        "add the other ingredients and adjust the pH to 6.6-6.8 before "
        "bringing the volume to 1000 ml."
    )

    _, _, steps, ph = module.parse_composition([[row]])

    assert ph == {"min": 6.6, "max": 6.8}
    assert steps == [row]


def test_solution_ph_rows_do_not_override_medium_ph() -> None:
    module = load_script()

    stock_step = (
        "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, "
        "then add minerals. Final pH 7.0 (with KOH)."
    )
    rows = [
        ["NaCl", "1", "g"],
        ["Adjust pH to 7.0 with NaOH"],
        ["*Trace minerals"],
        ["Nitrilotriacetic acid", "1", "g"],
        [stock_step],
    ]

    _, _, steps, ph = module.parse_composition(rows)

    assert ph == 7.0
    assert steps == ["Adjust pH to 7.0 with NaOH", stock_step]


def test_ingredient_maps_resazurin_to_current_chebi() -> None:
    module = load_script()

    assert module.ingredient("Resazurin", "1", "mg")["term"] == {
        "id": "CHEBI:8806",
        "label": "Resazurin",
    }


def test_ingredient_maps_l_arginine_to_packaged_chebi() -> None:
    module = load_script()

    assert module.ingredient("L-Arginine", "2.1", "g")["term"] == {
        "id": "CHEBI:16467",
        "label": "L-arginine",
    }


def test_merged_recipe_stamps_recomputable_fingerprint() -> None:
    module = load_script()

    recipe = {
        "id": "CultureMech:099999",
        "name": "fingerprinted_nbrc_record",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            module.ingredient("NaCl", "1", "g"),
            module.ingredient("Distilled water", "1", "l"),
        ],
        "curation_history": [],
    }

    merged = module.merged_recipe(
        recipe,
        "fingerprinted_nbrc_record.yaml",
        "2026-10-01T00:00:00+00:00",
    )

    assert re.fullmatch(r"[0-9a-f]{64}", merged["merge_fingerprint"])
    assert merged["merge_fingerprint"] in merged["curation_history"][-1]["notes"]
    assert merged["merged_from"] == ["fingerprinted_nbrc_record"]
