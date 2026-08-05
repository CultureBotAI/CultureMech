"""Tests for scripts/apply_ingredient_roles.py — Step 7b CultureMech applier."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

_REPO_ROOT = Path(__file__).resolve().parent.parent
_SCRIPT_PATH = _REPO_ROOT / "scripts" / "apply_ingredient_roles.py"

_SPEC = importlib.util.spec_from_file_location("_apply_roles", _SCRIPT_PATH)
_ap = importlib.util.module_from_spec(_SPEC)
sys.modules["_apply_roles"] = _ap
_SPEC.loader.exec_module(_ap)  # type: ignore[union-attr]


# ---------------- helpers ----------------


def _sample_proposal(chebi: str, slug: str, **roles) -> dict:
    return {
        "ingredient_identifier": chebi,
        "ingredient_slug": slug,
        "source_run": f"{slug}-edison-literature",
        "roles": roles,
    }


def _write_batch(tmp_path: Path, proposals: list[dict]) -> Path:
    p = tmp_path / "batch.json"
    p.write_text(json.dumps({"proposals": proposals}))
    return p


def _sample_recipe(*descriptor_terms: tuple[str, str]) -> dict:
    """Build a minimal recipe with N ingredients keyed by (chebi_id, preferred_term)."""
    return {
        "id": "CultureMech:test",
        "name": "test_recipe",
        "ingredients": [
            {
                "preferred_term": name,
                "term": {"id": chebi, "label": name},
                "mediaingredientmech_chebi_term": {"id": chebi, "label": name},
                "concentration": {"value": "1.0", "unit": "G_PER_L"},
            }
            for chebi, name in descriptor_terms
        ],
    }


# ---------------- _index_by_identifier ----------------


def test_index_by_identifier_keys_on_ingredient_identifier():
    props = [
        _sample_proposal("CHEBI:1", "a", nutritional_roles=["CARBON_SOURCE"]),
        _sample_proposal("CHEBI:2", "b", nutritional_roles=["NITROGEN_SOURCE"]),
    ]
    idx = _ap._index_by_identifier(props)
    assert set(idx.keys()) == {"CHEBI:1", "CHEBI:2"}


def test_index_by_identifier_drops_proposals_without_identifier():
    props = [
        _sample_proposal("CHEBI:1", "a", nutritional_roles=["CARBON_SOURCE"]),
        {"ingredient_slug": "orphan", "roles": {}},  # no identifier
    ]
    idx = _ap._index_by_identifier(props)
    assert list(idx.keys()) == ["CHEBI:1"]


def test_index_by_identifier_merges_duplicate_ids_by_facet_union():
    """Two proposals for same CHEBI should union their facet contributions."""
    props = [
        _sample_proposal("CHEBI:1", "a", nutritional_roles=["CARBON_SOURCE"]),
        _sample_proposal("CHEBI:1", "a", physicochemical_roles=["BUFFER"]),
    ]
    idx = _ap._index_by_identifier(props)
    roles = idx["CHEBI:1"]["roles"]
    assert "nutritional_roles" in roles
    assert "physicochemical_roles" in roles


# ---------------- _descriptor_identifier ----------------


def test_descriptor_identifier_prefers_mim_chebi_term():
    ing = {"term": {"id": "CHEBI:1"},
           "mediaingredientmech_chebi_term": {"id": "CHEBI:2"}}
    assert _ap._descriptor_identifier(ing) == "CHEBI:2"


def test_descriptor_identifier_falls_back_to_term():
    ing = {"term": {"id": "CHEBI:1"}}
    assert _ap._descriptor_identifier(ing) == "CHEBI:1"


def test_descriptor_identifier_returns_none_when_no_term():
    assert _ap._descriptor_identifier({"preferred_term": "x"}) is None


def test_descriptor_identifier_returns_none_when_ids_missing():
    ing = {"term": {"label": "x"}}
    assert _ap._descriptor_identifier(ing) is None


# ---------------- _apply_to_descriptor ----------------


def test_apply_to_descriptor_sets_empty_facet_slots():
    ing = {"preferred_term": "L-cysteine", "term": {"id": "CHEBI:17561"}}
    proposal = _sample_proposal("CHEBI:17561", "L-cysteine",
                                 nutritional_roles=["AMINO_ACID_SOURCE", "SULFUR_SOURCE"],
                                 physicochemical_roles=["REDUCING_AGENT"],
                                 cellular_metabolic_roles=["SUBSTRATE"])
    changed = _ap._apply_to_descriptor(ing, proposal)
    assert set(changed) == {"nutritional_roles", "physicochemical_roles", "cellular_metabolic_roles"}
    assert ing["nutritional_roles"] == ["AMINO_ACID_SOURCE", "SULFUR_SOURCE"]
    assert ing["physicochemical_roles"] == ["REDUCING_AGENT"]
    assert ing["cellular_metabolic_roles"] == ["SUBSTRATE"]


def test_apply_to_descriptor_never_overwrites_populated_slot():
    ing = {
        "preferred_term": "X",
        "nutritional_roles": ["CARBON_SOURCE"],  # already set by curator
    }
    proposal = _sample_proposal("CHEBI:1", "x",
                                 nutritional_roles=["NITROGEN_SOURCE"],  # would overwrite
                                 physicochemical_roles=["BUFFER"])       # empty; fills
    changed = _ap._apply_to_descriptor(ing, proposal)
    assert changed == ["physicochemical_roles"]
    # Preserved curator's choice:
    assert ing["nutritional_roles"] == ["CARBON_SOURCE"]
    # Filled the empty facet:
    assert ing["physicochemical_roles"] == ["BUFFER"]


def test_apply_to_descriptor_dedups_tokens():
    ing = {"preferred_term": "X"}
    proposal = _sample_proposal("CHEBI:1", "x",
                                 nutritional_roles=["CARBON_SOURCE", "CARBON_SOURCE", "NITROGEN_SOURCE"])
    _ap._apply_to_descriptor(ing, proposal)
    assert ing["nutritional_roles"] == ["CARBON_SOURCE", "NITROGEN_SOURCE"]


def test_apply_to_descriptor_ignores_empty_role_list():
    ing = {"preferred_term": "X"}
    proposal = _sample_proposal("CHEBI:1", "x", nutritional_roles=[])
    changed = _ap._apply_to_descriptor(ing, proposal)
    assert changed == []
    assert "nutritional_roles" not in ing


# ---------------- apply_to_recipe ----------------


def test_apply_to_recipe_walks_top_level_ingredients():
    recipe = _sample_recipe(("CHEBI:17561", "L-cysteine"), ("CHEBI:26710", "NaCl"))
    proposals = [
        _sample_proposal("CHEBI:17561", "L-cysteine",
                          nutritional_roles=["SULFUR_SOURCE"]),
        _sample_proposal("CHEBI:26710", "NaCl",
                          physicochemical_roles=["OSMOTIC_AGENT"]),
    ]
    idx = _ap._index_by_identifier(proposals)
    fields, touched = _ap.apply_to_recipe(recipe, idx, "test-curator")
    assert set(fields) == {"nutritional_roles", "physicochemical_roles"}
    assert set(touched) == {"CHEBI:17561", "CHEBI:26710"}
    assert recipe["ingredients"][0]["nutritional_roles"] == ["SULFUR_SOURCE"]
    assert recipe["ingredients"][1]["physicochemical_roles"] == ["OSMOTIC_AGENT"]


def test_apply_to_recipe_walks_solution_ingredients():
    recipe = {
        "id": "x",
        "solutions": [{
            "name": "trace metals",
            "ingredients": [
                {"preferred_term": "FeCl3", "term": {"id": "CHEBI:30808"}},
            ],
        }],
    }
    proposals = [_sample_proposal("CHEBI:30808", "FeCl3", nutritional_roles=["IRON_SOURCE"])]
    idx = _ap._index_by_identifier(proposals)
    fields, touched = _ap.apply_to_recipe(recipe, idx, "test-curator")
    assert fields == ["nutritional_roles"]
    assert touched == ["CHEBI:30808"]
    assert recipe["solutions"][0]["ingredients"][0]["nutritional_roles"] == ["IRON_SOURCE"]


def test_apply_to_recipe_adds_curation_event_when_changed():
    recipe = _sample_recipe(("CHEBI:17561", "L-cysteine"))
    proposals = [_sample_proposal("CHEBI:17561", "L-cysteine", nutritional_roles=["SULFUR_SOURCE"])]
    idx = _ap._index_by_identifier(proposals)
    _ap.apply_to_recipe(recipe, idx, "test-curator")
    events = recipe["curation_history"]
    assert len(events) == 1
    assert events[0]["curator"] == "test-curator"
    assert events[0]["action"] == "ANNOTATED"
    assert events[0]["changes"] == "nutritional_roles"
    assert "L-cysteine-edison-literature" in events[0]["notes"]


def test_curation_event_keys_are_all_curation_event_slots():
    """Every key we emit must be a declared CurationEvent slot.

    `validate-strict` runs linkml-validate with closed=True, so an undeclared key
    (e.g. the `fields_changed` this script originally wrote) fails CI on every
    recipe the applier touches — and nothing else in this suite would catch it,
    since the applier's own tests never validate against the schema.
    """
    schema = yaml.safe_load(
        (Path(__file__).resolve().parent.parent
         / "src" / "culturemech" / "schema" / "culturemech.yaml").read_text()
    )
    allowed = set(schema["classes"]["CurationEvent"]["attributes"])
    assert "changes" in allowed and "fields_changed" not in allowed  # guards the fixture itself

    recipe = _sample_recipe(("CHEBI:17561", "L-cysteine"))
    proposals = [_sample_proposal("CHEBI:17561", "L-cysteine", nutritional_roles=["SULFUR_SOURCE"])]
    _ap.apply_to_recipe(recipe, _ap._index_by_identifier(proposals), "test-curator")

    emitted = set(recipe["curation_history"][0])
    assert emitted <= allowed, f"undeclared CurationEvent key(s): {sorted(emitted - allowed)}"


def test_proposals_without_identifier_are_reported_not_silently_dropped():
    skipped = []
    proposals = [
        _sample_proposal("CHEBI:17561", "L-cysteine", nutritional_roles=["SULFUR_SOURCE"]),
        {"ingredient_slug": "mystery", "source_run": "mystery-edison-literature",
         "roles": {"nutritional_roles": ["CARBON_SOURCE"]}},  # no ingredient_identifier
    ]
    idx = _ap._index_by_identifier(proposals, skipped=skipped)
    assert set(idx) == {"CHEBI:17561"}
    assert [p["ingredient_slug"] for p in skipped] == ["mystery"]


def test_apply_to_recipe_no_change_no_curation_event():
    recipe = _sample_recipe(("CHEBI:17561", "L-cysteine"))
    recipe["ingredients"][0]["nutritional_roles"] = ["CARBON_SOURCE"]  # already populated
    proposals = [_sample_proposal("CHEBI:17561", "L-cysteine", nutritional_roles=["SULFUR_SOURCE"])]
    idx = _ap._index_by_identifier(proposals)
    fields, touched = _ap.apply_to_recipe(recipe, idx, "test-curator")
    assert fields == []
    assert "curation_history" not in recipe


def test_apply_to_recipe_skips_ingredients_without_matching_identifier():
    recipe = _sample_recipe(("CHEBI:99999", "unknown_thing"))
    proposals = [_sample_proposal("CHEBI:17561", "L-cysteine", nutritional_roles=["SULFUR_SOURCE"])]
    idx = _ap._index_by_identifier(proposals)
    fields, touched = _ap.apply_to_recipe(recipe, idx, "test-curator")
    assert fields == []
    assert touched == []


# ---------------- CLI main ----------------


def test_main_dry_run_makes_no_writes(tmp_path):
    yaml_dir = tmp_path / "yaml"
    yaml_dir.mkdir()
    recipe = _sample_recipe(("CHEBI:17561", "L-cysteine"))
    recipe_path = yaml_dir / "recipe.yaml"
    recipe_path.write_text(yaml.safe_dump(recipe))
    original_bytes = recipe_path.read_bytes()

    batch = _write_batch(tmp_path, [
        _sample_proposal("CHEBI:17561", "L-cysteine", nutritional_roles=["SULFUR_SOURCE"])
    ])

    rc = _ap.main([str(batch), "--yaml-dir", str(yaml_dir), "--dry-run"])
    assert rc == 0
    assert recipe_path.read_bytes() == original_bytes


def test_main_writes_recipe_and_round_trips(tmp_path):
    yaml_dir = tmp_path / "yaml"
    yaml_dir.mkdir()
    recipe = _sample_recipe(("CHEBI:17561", "L-cysteine"))
    recipe_path = yaml_dir / "recipe.yaml"
    recipe_path.write_text(yaml.safe_dump(recipe))

    batch = _write_batch(tmp_path, [
        _sample_proposal("CHEBI:17561", "L-cysteine",
                         nutritional_roles=["AMINO_ACID_SOURCE", "SULFUR_SOURCE"],
                         cellular_metabolic_roles=["SUBSTRATE"])
    ])

    rc = _ap.main([str(batch), "--yaml-dir", str(yaml_dir), "--curator", "edison-deep-research"])
    assert rc == 0
    updated = yaml.safe_load(recipe_path.read_text())
    ing = updated["ingredients"][0]
    assert ing["nutritional_roles"] == ["AMINO_ACID_SOURCE", "SULFUR_SOURCE"]
    assert ing["cellular_metabolic_roles"] == ["SUBSTRATE"]
    assert updated["curation_history"][0]["curator"] == "edison-deep-research"


def test_main_missing_batch_returns_2(tmp_path):
    yaml_dir = tmp_path / "yaml"
    yaml_dir.mkdir()
    rc = _ap.main([str(tmp_path / "missing.json"), "--yaml-dir", str(yaml_dir)])
    assert rc == 2


def test_main_missing_yaml_dir_returns_2(tmp_path):
    batch = _write_batch(tmp_path, [
        _sample_proposal("CHEBI:1", "x", nutritional_roles=["CARBON_SOURCE"])
    ])
    rc = _ap.main([str(batch), "--yaml-dir", str(tmp_path / "nope")])
    assert rc == 2


def test_main_limit_caps_writes_but_dry_run_counts_all(tmp_path):
    """--limit only caps writes, dry-run always reports total touched."""
    yaml_dir = tmp_path / "yaml"
    yaml_dir.mkdir()
    for i in range(3):
        recipe = _sample_recipe(("CHEBI:17561", "L-cysteine"))
        (yaml_dir / f"r{i}.yaml").write_text(yaml.safe_dump(recipe))
    batch = _write_batch(tmp_path, [
        _sample_proposal("CHEBI:17561", "L-cysteine", nutritional_roles=["SULFUR_SOURCE"])
    ])
    rc = _ap.main([str(batch), "--yaml-dir", str(yaml_dir), "--limit", "1"])
    assert rc == 0
    # Two of three recipes should still have empty nutritional_roles.
    written = sum(1 for p in yaml_dir.glob("*.yaml")
                  if yaml.safe_load(p.read_text())["ingredients"][0].get("nutritional_roles"))
    assert written == 1


def test_main_bad_batch_shape_raises_systemexit(tmp_path):
    batch = tmp_path / "bad.json"
    batch.write_text(json.dumps({"not_proposals": []}))
    yaml_dir = tmp_path / "yaml"
    yaml_dir.mkdir()
    with pytest.raises(SystemExit, match="'proposals' list"):
        _ap.main([str(batch), "--yaml-dir", str(yaml_dir)])
