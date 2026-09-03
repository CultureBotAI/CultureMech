"""The batch reviewer must read the schema, not a copy of it (#401, #402).

Running it over all 15,877 recipes reported two P1 criticals and 0.8%
MediaIngredientMech coverage. Both were artifacts of the script having drifted
from the repository it validates:

* `valid_medium_types` was a hardcoded list that rejected `BUFFER` and
  `NEGATIVE_CONTROL` (which the schema permits) while accepting `SEMI_DEFINED`
  and `UNDEFINED` (which belong to `MediumCompositionTypeEnum`, a different
  axis). The comment directly above it said "DO NOT hardcode, derive from
  schema".
* coverage counted `mediaingredientmech_term`, the field MIM's id-scheme
  deprecation migrated the corpus *off*. The live field sits at 67.2%.

These tests pin the derivation rather than the values, so the next schema change
cannot silently reintroduce either.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml
from batch_review_recipes import (
    LEGACY_MIM_LINK_FIELD,
    MIM_LINK_FIELD,
    RecipeValidator,
    mim_link_id,
    permissible_values,
)

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "batch_review_recipes.py"
SCHEMA = Path(__file__).resolve().parents[1] / "src" / "culturemech" / "schema" / "culturemech.yaml"


# --- the enums come from the schema -------------------------------------


@pytest.mark.parametrize(
    "enum_name", ["MediumTypeEnum", "MediumCompositionTypeEnum", "PhysicalStateEnum"]
)
def test_permissible_values_match_the_schema_exactly(enum_name):
    schema = yaml.safe_load(SCHEMA.read_text())
    expected = list(schema["enums"][enum_name]["permissible_values"])
    assert permissible_values(enum_name) == expected


def test_the_two_values_that_produced_false_criticals_are_accepted():
    """`PBS` is a BUFFER and `Water` is a NEGATIVE_CONTROL. Both are valid."""
    medium_types = permissible_values("MediumTypeEnum")
    assert "BUFFER" in medium_types
    assert "NEGATIVE_CONTROL" in medium_types


def test_the_composition_axis_is_not_mistaken_for_the_medium_axis():
    """`SEMI_DEFINED` and `UNDEFINED` are composition_type values only.

    The old list put them in `medium_type`, so a genuinely invalid
    `medium_type: UNDEFINED` would have passed.
    """
    medium_types = permissible_values("MediumTypeEnum")
    composition_types = permissible_values("MediumCompositionTypeEnum")
    assert "SEMI_DEFINED" not in medium_types
    assert "UNDEFINED" not in medium_types
    assert {"SEMI_DEFINED", "UNDEFINED"} <= set(composition_types)


def test_no_enum_list_is_restated_in_the_script():
    """The regression guard. A literal list of these values is the defect."""
    source = SCRIPT.read_text()
    for spelling in (
        "['DEFINED', 'COMPLEX'",
        '["DEFINED", "COMPLEX"',
        "['LIQUID', 'SOLID_AGAR'",
        '["LIQUID", "SOLID_AGAR"',
    ):
        assert spelling not in source, f"enum values are hardcoded again: {spelling}"


# --- the MIM link field --------------------------------------------------


def test_the_live_field_is_preferred():
    assert mim_link_id({MIM_LINK_FIELD: {"id": "CHEBI:17234"}}) == "CHEBI:17234"


def test_the_retired_field_still_counts_when_it_is_all_there_is():
    """1,677 instances carry only the retired field; dropping them would
    understate coverage in the opposite direction to the bug being fixed."""
    assert mim_link_id({LEGACY_MIM_LINK_FIELD: {"id": "MediaIngredientMech:1"}}) == (
        "MediaIngredientMech:1"
    )


def test_the_live_field_wins_when_both_are_present():
    assert (
        mim_link_id(
            {
                MIM_LINK_FIELD: {"id": "CHEBI:17234"},
                LEGACY_MIM_LINK_FIELD: {"id": "MediaIngredientMech:1"},
            }
        )
        == "CHEBI:17234"
    )


@pytest.mark.parametrize(
    "ingredient", [{}, None, "x", {MIM_LINK_FIELD: {}}, {MIM_LINK_FIELD: "not-a-dict"}]
)
def test_an_unlinked_ingredient_yields_no_id(ingredient):
    assert mim_link_id(ingredient) is None


def test_the_retired_field_is_not_what_coverage_counts():
    """The #402 defect: coverage read the deprecated field and reported 0.8%."""
    assert MIM_LINK_FIELD == "mediaingredientmech_chebi_term"
    assert LEGACY_MIM_LINK_FIELD != MIM_LINK_FIELD


# --- the pH rule ---------------------------------------------------------


@pytest.fixture(scope="module")
def validator() -> RecipeValidator:
    """One instance for the module: the constructor loads MIM ids, which costs
    seconds and is identical for every case here."""
    return RecipeValidator()


def _validate(validator: RecipeValidator, tmp_path: Path, record: dict) -> list[str]:
    path = tmp_path / "r.yaml"
    path.write_text(yaml.safe_dump(record))
    result = validator.validate_recipe(path)
    return [issue["rule"] for issue in result.get("issues", [])]


def test_a_ph_range_counts_as_a_ph(validator, tmp_path):
    """920 records state `ph_range` and no `ph_value`, and were reported as
    having no pH while stating one."""
    rules = _validate(
        validator,
        tmp_path,
        {
            "name": "x",
            "medium_type": "DEFINED",
            "composition_type": "DEFINED",
            "physical_state": "LIQUID",
            "ph_range": {"minimum": 6.8, "maximum": 7.2},
        },
    )
    assert "P3.6" not in rules


def test_a_record_with_neither_ph_form_is_still_reported(validator, tmp_path):
    rules = _validate(
        validator,
        tmp_path,
        {
            "name": "x",
            "medium_type": "DEFINED",
            "composition_type": "DEFINED",
            "physical_state": "LIQUID",
        },
    )
    assert "P3.6" in rules


def test_the_ph_rule_keys_on_the_composition_axis(validator, tmp_path):
    """`SEMI_DEFINED` exists only on `composition_type`, so the old condition's
    second arm matched nothing and 620 records were never checked."""
    rules = _validate(
        validator,
        tmp_path,
        {
            "name": "x",
            "medium_type": "COMPLEX",
            "composition_type": "SEMI_DEFINED",
            "physical_state": "LIQUID",
        },
    )
    assert "P3.6" in rules


# --- enum validation end to end -----------------------------------------


def test_a_buffer_medium_is_not_a_critical_error(validator, tmp_path):
    """PBS, CultureMech:015675 — one of the two false P1s."""
    rules = _validate(
        validator,
        tmp_path,
        {"name": "PBS", "medium_type": "BUFFER", "physical_state": "LIQUID"},
    )
    assert "P1.4" not in rules


def test_an_invalid_medium_type_is_still_a_critical_error(validator, tmp_path):
    rules = _validate(
        validator,
        tmp_path,
        {"name": "x", "medium_type": "NOT_A_REAL_TYPE", "physical_state": "LIQUID"},
    )
    assert "P1.4" in rules


def test_an_invalid_composition_type_is_now_caught(validator, tmp_path):
    """The composition axis existed but no rule looked at it."""
    rules = _validate(
        validator,
        tmp_path,
        {
            "name": "x",
            "medium_type": "DEFINED",
            "composition_type": "NOT_A_REAL_TYPE",
            "physical_state": "LIQUID",
        },
    )
    assert "P1.4" in rules
