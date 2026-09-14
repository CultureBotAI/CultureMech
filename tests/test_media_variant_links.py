from pathlib import Path
from types import SimpleNamespace

import yaml

from culturemech.schema.culturemech_dataclasses import (
    MediaRecipe,
    MediaRecipeReference,
    MediaVariantRelationshipEnum,
)
from scripts import apply_media_variant_links
from scripts.propose_media_variant_links import (
    build_proposals,
    choose_parent,
    collect_existing_links,
    confidence_for_group,
    existing_link_key,
    infer_relationship,
    status_for_group,
    write_tsv,
)
from scripts.validate_media_variant_links import RecipeIndex, validate_links

SCHEMA_PATH = Path(__file__).parent.parent / "src" / "culturemech" / "schema" / "culturemech.yaml"


def test_schema_has_parent_child_variant_slots():
    schema = yaml.safe_load(SCHEMA_PATH.read_text())
    media_recipe = schema["classes"]["MediaRecipe"]["attributes"]

    assert media_recipe["parent_media"]["range"] == "MediaRecipeReference"
    assert media_recipe["variant_children"]["range"] == "MediaRecipeReference"
    assert media_recipe["variant_children"]["multivalued"] is True
    assert media_recipe["variant_relationship"]["range"] == "MediaVariantRelationshipEnum"
    assert media_recipe["variant_modifications"]["multivalued"] is True


def test_schema_has_media_recipe_reference_class():
    schema = yaml.safe_load(SCHEMA_PATH.read_text())
    ref = schema["classes"]["MediaRecipeReference"]["attributes"]

    assert ref["id"]["pattern"] == "^CultureMech:\\d{6}$"
    assert ref["path"]["pattern"] == "^data/normalized_yaml/.+\\.ya?ml$"
    assert ref["relationship"]["range"] == "MediaVariantRelationshipEnum"


def test_dataclasses_accept_parent_child_variant_links():
    minimal_ingredient = {
        "preferred_term": "Water",
        "concentration": {
            "value": "1",
            "unit": "G_PER_L",
        },
    }

    child = MediaRecipe(
        id="CultureMech:000002",
        name="lb_low_salt_variant",
        medium_type="COMPLEX",
        physical_state="LIQUID",
        ingredients=[minimal_ingredient],
        parent_media=MediaRecipeReference(
            id="CultureMech:000001",
            name="lb_medium",
            path="data/normalized_yaml/bacterial/lb_medium.yaml",
            relationship="SALINITY_VARIANT",
        ),
        variant_relationship="SALINITY_VARIANT",
        variant_modifications=["Reduce sodium chloride relative to parent LB."],
    )

    parent = MediaRecipe(
        id="CultureMech:000001",
        name="lb_medium",
        medium_type="COMPLEX",
        physical_state="LIQUID",
        ingredients=[minimal_ingredient],
        variant_children=[
            {
                "id": "CultureMech:000002",
                "name": "lb_low_salt_variant",
                "path": "data/normalized_yaml/bacterial/lb_low_salt_variant.yaml",
                "relationship": "SALINITY_VARIANT",
            }
        ],
    )

    assert isinstance(child.parent_media, MediaRecipeReference)
    assert str(child.variant_relationship) == "SALINITY_VARIANT"
    assert MediaVariantRelationshipEnum.SALINITY_VARIANT.text == "SALINITY_VARIANT"
    assert isinstance(parent.variant_children[0], MediaRecipeReference)
    assert str(parent.variant_children[0].relationship) == "SALINITY_VARIANT"


def test_write_tsv_uses_lf_and_trims_only_trailing_empty_cells(tmp_path):
    out = tmp_path / "proposals.tsv"

    write_tsv(
        out,
        [
            {"left": "alpha", "middle": "", "right": ""},
            {"left": "beta", "middle": "", "right": "kept"},
        ],
        ["left", "middle", "right"],
    )

    assert out.read_bytes() == b"left\tmiddle\tright\nalpha\nbeta\t\tkept\n"


def test_variant_link_validator_checks_bidirectional_links():
    index = RecipeIndex(
        path_to_recipe={
            "data/normalized_yaml/bacterial/lb_medium.yaml": {
                "id": "CultureMech:000001",
                "variant_children": [
                    {
                        "id": "CultureMech:000002",
                        "path": "data/normalized_yaml/bacterial/lb_low_salt_variant.yaml",
                        "relationship": "SALINITY_VARIANT",
                    }
                ],
            },
            "data/normalized_yaml/bacterial/lb_low_salt_variant.yaml": {
                "id": "CultureMech:000002",
                "parent_media": {
                    "id": "CultureMech:000001",
                    "path": "data/normalized_yaml/bacterial/lb_medium.yaml",
                    "relationship": "SALINITY_VARIANT",
                },
                "variant_relationship": "SALINITY_VARIANT",
            },
        },
        id_to_path={
            "CultureMech:000001": "data/normalized_yaml/bacterial/lb_medium.yaml",
            "CultureMech:000002": "data/normalized_yaml/bacterial/lb_low_salt_variant.yaml",
        },
    )

    assert validate_links(index) == []

    index.path_to_recipe["data/normalized_yaml/bacterial/lb_medium.yaml"]["variant_children"] = []
    findings = validate_links(index)
    assert len(findings) == 1
    assert findings[0].field == "parent_media"
    assert "does not link back" in findings[0].message


def test_variant_proposal_prefers_base_parent_and_classifies_relationships():
    parent = {
        "yaml_path": "data/normalized_yaml/bacterial/KOMODO_11_MRS_medium.yaml",
        "id": "CultureMech:003940",
        "name": "mrs_medium",
        "original_name": "MRS medium",
        "media_term_id": "komodo.medium:11",
        "physical_state": "LIQUID",
        "total_component_count": "4",
        "ingredient_chebi_term_count": "4",
        "mediaingredientmech_count": "4",
        "missing_concentration_count": "0",
        "malformed_concentration_count": "0",
        "missing_concentration_value_count": "0",
        "missing_concentration_unit_count": "0",
        "non_schema_concentration_unit_count": "0",
        "ingredient_concentration_signature": "parent",
    }
    child = {
        **parent,
        "yaml_path": "data/normalized_yaml/bacterial/medium_11_modified_for_dsm_13613.yaml",
        "id": "CultureMech:003941",
        "name": "medium_11_modified_for_dsm_13613",
        "media_term_id": "",
        "ingredient_concentration_signature": "child",
    }
    salt_child = {
        **child,
        "yaml_path": "data/normalized_yaml/bacterial/mrs_medium_with_5_nacl.yaml",
        "name": "mrs_medium_with_5_nacl",
    }

    assert choose_parent([child, parent]) == parent
    assert infer_relationship(parent, child) == "CONCENTRATION_VARIANT"
    assert infer_relationship(parent, salt_child) == "SALINITY_VARIANT"


def test_variant_proposal_marks_large_variable_groups_for_review():
    parent = {
        "yaml_path": "data/normalized_yaml/bacterial/base.yaml",
        "id": "CultureMech:000001",
        "name": "base",
        "physical_state": "LIQUID",
        "total_component_count": "1",
        "ingredient_chebi_term_count": "0",
        "mediaingredientmech_count": "0",
        "missing_concentration_count": "0",
        "malformed_concentration_count": "0",
        "missing_concentration_value_count": "0",
        "missing_concentration_unit_count": "0",
        "non_schema_concentration_unit_count": "0",
        "concentration_units": "VARIABLE",
    }
    rows = [{**parent, "yaml_path": f"data/normalized_yaml/bacterial/r{i}.yaml"} for i in range(25)]

    confidence, reason = confidence_for_group(rows, parent)

    assert confidence == "LOW"
    assert status_for_group(confidence, len(rows)) == "REVIEW_REQUIRED"
    assert "VARIABLE" in reason


def test_variant_proposal_marks_algae_source_duplicates_for_review():
    parent = {
        "yaml_path": "data/normalized_yaml/algae/J_Medium.yaml",
        "id": "CultureMech:000001",
        "name": "J_Medium",
        "physical_state": "LIQUID",
        "category_dir": "algae",
        "total_component_count": "4",
        "ingredient_chebi_term_count": "4",
        "mediaingredientmech_count": "4",
        "missing_concentration_count": "0",
        "malformed_concentration_count": "0",
        "missing_concentration_value_count": "0",
        "missing_concentration_unit_count": "0",
        "non_schema_concentration_unit_count": "0",
        "ingredient_concentration_signature": "same",
    }
    child = {
        **parent,
        "yaml_path": "data/normalized_yaml/algae/TAP_Medium.yaml",
        "id": "CultureMech:000002",
        "name": "TAP_Medium",
    }

    confidence, reason = confidence_for_group([parent, child], parent)

    assert confidence == "LOW"
    assert status_for_group(confidence, 2) == "REVIEW_REQUIRED"
    assert "algae source-duplicate candidate" in reason


def test_variant_proposals_exclude_standalone_solution_records():
    media = {
        "yaml_path": "data/normalized_yaml/bacterial/media.yaml",
        "record_kind": "MEDIA",
        "ingredient_identity_signature": "same",
        "ingredient_concentration_signature": "same-concentration",
        "total_component_count": "1",
    }
    solution = {
        **media,
        "yaml_path": "data/normalized_yaml/bacterial/stock.yaml",
        "record_kind": "SOLUTION",
    }

    proposals, groups = build_proposals([media, solution])

    assert proposals == []
    assert groups == []


def test_variant_proposals_exclude_existing_parent_child_links(tmp_path):
    parent_path = "data/normalized_yaml/bacterial/lb_medium.yaml"
    child_path = "data/normalized_yaml/bacterial/lb_low_salt_variant.yaml"
    (tmp_path / "data/normalized_yaml/bacterial").mkdir(parents=True)
    (tmp_path / parent_path).write_text(
        yaml.safe_dump(
            {
                "id": "CultureMech:000001",
                "variant_children": [
                    {
                        "id": "CultureMech:000002",
                        "path": child_path,
                        "relationship": "SALINITY_VARIANT",
                    }
                ],
            }
        )
    )
    (tmp_path / child_path).write_text(
        yaml.safe_dump(
            {
                "id": "CultureMech:000002",
                "parent_media": {
                    "id": "CultureMech:000001",
                    "path": parent_path,
                    "relationship": "SALINITY_VARIANT",
                },
            }
        )
    )
    rows = [
        {
            "yaml_path": parent_path,
            "record_kind": "MEDIA",
            "ingredient_identity_signature": "same",
            "ingredient_concentration_signature": "same",
            "name": "lb_medium",
            "total_component_count": "1",
        },
        {
            "yaml_path": child_path,
            "record_kind": "MEDIA",
            "ingredient_identity_signature": "same",
            "ingredient_concentration_signature": "same",
            "name": "lb_low_salt_variant",
            "total_component_count": "1",
        },
    ]

    existing_links = collect_existing_links(rows, repo_root=tmp_path)
    proposals, groups = build_proposals(
        rows,
        existing_links={existing_link_key(child_path, parent_path)},
    )

    assert existing_links == {existing_link_key(parent_path, child_path)}
    assert proposals == []
    assert groups == []


def test_existing_links_fall_back_from_stale_paths_to_stable_ids(tmp_path):
    parent_path = "data/normalized_yaml/bacterial/base.yaml"
    child_path = "data/normalized_yaml/bacterial/current_child.yaml"
    (tmp_path / "data/normalized_yaml/bacterial").mkdir(parents=True)
    (tmp_path / parent_path).write_text(
        yaml.safe_dump(
            {
                "id": "CultureMech:000001",
                "variant_children": [
                    {
                        "id": "CultureMech:000002",
                        "path": "data/normalized_yaml/bacterial/stale_child.yaml",
                        "relationship": "SALINITY_VARIANT",
                    }
                ],
            }
        )
    )
    (tmp_path / child_path).write_text(
        yaml.safe_dump(
            {
                "id": "CultureMech:000002",
                "parent_media": {
                    "id": "CultureMech:000001",
                    "path": "data/normalized_yaml/bacterial/stale_base.yaml",
                    "relationship": "SALINITY_VARIANT",
                },
            }
        )
    )
    rows = [
        {
            "yaml_path": parent_path,
            "record_kind": "MEDIA",
            "ingredient_identity_signature": "same",
            "ingredient_concentration_signature": "same",
            "name": "base",
            "total_component_count": "1",
        },
        {
            "yaml_path": child_path,
            "record_kind": "MEDIA",
            "ingredient_identity_signature": "same",
            "ingredient_concentration_signature": "same",
            "name": "current_child",
            "total_component_count": "1",
        },
    ]

    existing_links = collect_existing_links(rows, repo_root=tmp_path)
    proposals, groups = build_proposals(rows, existing_links=existing_links)

    assert existing_links == {existing_link_key(parent_path, child_path)}
    assert proposals == []
    assert groups == []


def test_variant_proposals_exclude_curated_false_positive_pairs():
    dsmz_605 = {
        "yaml_path": "data/normalized_yaml/bacterial/nutrient_agar_oxoid_cm3.yaml",
        "record_kind": "MEDIA",
        "id": "CultureMech:001732",
        "name": "nutrient_agar_oxoid_cm3",
        "ingredient_identity_signature": "same",
        "ingredient_concentration_signature": "one",
        "physical_state": "SOLID_AGAR",
        "total_component_count": "6",
    }
    na_yeast = {
        **dsmz_605,
        "yaml_path": "data/normalized_yaml/bacterial/na_0_5_yeast_extract.yaml",
        "id": "CultureMech:008124",
        "name": "na_0_5_yeast_extract",
        "ingredient_concentration_signature": "two",
    }

    proposals, groups = build_proposals([dsmz_605, na_yeast])

    assert proposals == []
    assert groups == []


def test_apply_variant_links_plans_bidirectional_edits(tmp_path, monkeypatch):
    parent_path = "data/normalized_yaml/bacterial/lb_medium.yaml"
    child_path = "data/normalized_yaml/bacterial/lb_low_salt_variant.yaml"
    (tmp_path / "data/normalized_yaml/bacterial").mkdir(parents=True)
    (tmp_path / parent_path).write_text(
        yaml.safe_dump(
            {
                "id": "CultureMech:000001",
                "name": "lb_medium",
                "medium_type": "COMPLEX",
                "physical_state": "LIQUID",
                "ingredients": [
                    {
                        "preferred_term": "Water",
                        "concentration": {"value": "1", "unit": "G_PER_L"},
                    }
                ],
            }
        )
    )
    (tmp_path / child_path).write_text(
        yaml.safe_dump(
            {
                "id": "CultureMech:000002",
                "name": "lb_low_salt_variant",
                "medium_type": "COMPLEX",
                "physical_state": "LIQUID",
                "ingredients": [
                    {
                        "preferred_term": "Water",
                        "concentration": {"value": "1", "unit": "G_PER_L"},
                    }
                ],
            }
        )
    )
    monkeypatch.setattr(apply_media_variant_links, "REPO_ROOT", tmp_path)

    plans = apply_media_variant_links.plan_links(
        [
            {
                "status": "PROPOSED",
                "confidence": "HIGH",
                "relationship": "SALINITY_VARIANT",
                "parent_path": parent_path,
                "child_path": child_path,
                "modifications": "Reduce sodium chloride relative to parent LB.",
                "review_reason": "",
            }
        ],
        SimpleNamespace(
            status=["PROPOSED"],
            confidence=["HIGH"],
            relationship=None,
            signature=None,
            limit=None,
            apply=False,
        ),
    )

    assert [plan["action"] for plan in plans] == [
        "add_variant_child",
        "add_parent_media",
        "set_variant_relationship",
        "add_variant_modification",
    ]
    assert "variant_children" not in yaml.safe_load((tmp_path / parent_path).read_text())
    assert "parent_media" not in yaml.safe_load((tmp_path / child_path).read_text())
