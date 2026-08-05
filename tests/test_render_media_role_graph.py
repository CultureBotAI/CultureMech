"""Tests for scripts/render_media_role_graph.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

_SCRIPT_PATH = Path(__file__).parent.parent / "scripts" / "render_media_role_graph.py"
_SPEC = importlib.util.spec_from_file_location("_render_media_role_graph", _SCRIPT_PATH)
_render = importlib.util.module_from_spec(_SPEC)
sys.modules["_render_media_role_graph"] = _render
_SPEC.loader.exec_module(_render)  # type: ignore[union-attr]


# ---------------- helpers ----------------


def _write(tmp_path: Path, doc: dict) -> Path:
    path = tmp_path / "recipe.yaml"
    path.write_text(yaml.safe_dump(doc, sort_keys=False))
    return path


# ---------------- unit helpers ----------------


def test_sanitize_id_strips_non_alphanum():
    assert _render._sanitize_id("CHEBI:12345") == "CHEBI_12345"
    assert _render._sanitize_id("mediadive.compound:5") == "mediadive_compound_5"
    assert _render._sanitize_id("has spaces & symbols!") == "has_spaces___symbols_"


def test_label_trims_and_collapses():
    assert _render._label("normal") == "normal"
    assert _render._label('with "quotes"\nand newlines') == "with 'quotes' and newlines"
    long = "x" * 100
    got = _render._label(long, max_len=20)
    assert got.endswith("...") and len(got) == 20


def test_ingredient_chebi_id_prefers_primary_term():
    ing = {"term": {"id": "CHEBI:17234"}, "chebi_term": {"id": "CHEBI:99999"}}
    assert _render.ingredient_chebi_id(ing) == "CHEBI:17234"


def test_ingredient_chebi_id_falls_back_to_chebi_term():
    ing = {"term": {"id": "mediadive.compound:5"}, "chebi_term": {"id": "CHEBI:17234"}}
    assert _render.ingredient_chebi_id(ing) == "CHEBI:17234"


def test_ingredient_display_id_prefers_chebi_then_any_term():
    assert _render.ingredient_display_id({"term": {"id": "CHEBI:17234"}}) == "CHEBI:17234"
    assert _render.ingredient_display_id({"term": {"id": "mediadive.compound:5"}}) == "mediadive.compound:5"
    assert _render.ingredient_display_id({"preferred_term": "Distilled water"}) == "ing:Distilled water"


# ---------------- single-recipe rendering ----------------


def test_single_recipe_empty_recipe_returns_bare_header(tmp_path):
    recipe = _write(tmp_path, {"preferred_term": "Empty medium", "ingredients": []})
    mmd = _render.render_single_recipe(recipe)
    assert mmd.startswith("flowchart LR")
    assert 'MEDIUM["`**Empty medium**`"]:::medium' in mmd
    # No ingredient nodes, no role edges.
    assert "-->" not in mmd or mmd.count("-->") == 0
    # Style block always emitted.
    assert "classDef medium" in mmd


def test_single_recipe_emits_medium_to_ingredient_edges(tmp_path):
    recipe = _write(tmp_path, {
        "preferred_term": "Small medium",
        "ingredients": [
            {"preferred_term": "Glucose", "term": {"id": "CHEBI:17234"}},
            {"preferred_term": "Sodium chloride", "term": {"id": "CHEBI:26710"}},
        ],
    })
    mmd = _render.render_single_recipe(recipe)
    assert "MEDIUM --> CHEBI_17234" in mmd
    assert "MEDIUM --> CHEBI_26710" in mmd
    assert "Glucose" in mmd and "Sodium chloride" in mmd


def test_single_recipe_emits_all_three_facet_edges(tmp_path):
    """An ingredient with values in all three facet slots produces one edge per facet."""
    recipe = _write(tmp_path, {
        "preferred_term": "Faceted medium",
        "ingredients": [{
            "preferred_term": "L-cysteine",
            "term": {"id": "CHEBI:17561"},
            "nutritional_roles": ["AMINO_ACID_SOURCE", "SULFUR_SOURCE"],
            "physicochemical_roles": ["REDUCING_AGENT"],
            "cellular_metabolic_roles": ["SUBSTRATE"],
        }],
    })
    mmd = _render.render_single_recipe(recipe)
    # Facet-value nodes present.
    assert "AMINO_ACID_SOURCE" in mmd
    assert "SULFUR_SOURCE" in mmd
    assert "REDUCING_AGENT" in mmd
    assert "SUBSTRATE" in mmd
    # Each facet has its own edge label.
    assert "|nut|" in mmd  # from FACET_STYLE
    assert "|phys|" in mmd
    assert "|cell|" in mmd


def test_single_recipe_role_value_nodes_dedup_across_ingredients(tmp_path):
    """Two ingredients sharing a facet value should point at the SAME role-value node."""
    recipe = _write(tmp_path, {
        "preferred_term": "Dedup medium",
        "ingredients": [
            {"preferred_term": "Glucose", "term": {"id": "CHEBI:17234"},
             "nutritional_roles": ["CARBON_SOURCE", "ENERGY_SOURCE"]},
            {"preferred_term": "Methanol", "term": {"id": "CHEBI:17790"},
             "nutritional_roles": ["CARBON_SOURCE", "ENERGY_SOURCE"]},
        ],
    })
    mmd = _render.render_single_recipe(recipe)
    # Node declaration for CARBON_SOURCE / ENERGY_SOURCE should appear exactly once each.
    assert mmd.count("CARBON_SOURCE\\n[nut]") == 1  # (both an occurrence and a label appearance)
    assert mmd.count("ENERGY_SOURCE\\n[nut]") == 1
    # Both ingredients edge to the same role nodes → 4 edges total for the 2×2 facet values.
    assert mmd.count("|nut|--> role_nutritional_roles_CARBON_SOURCE") == 2
    assert mmd.count("|nut|--> role_nutritional_roles_ENERGY_SOURCE") == 2


def test_single_recipe_role_curie_escape_hatch(tmp_path):
    recipe = _write(tmp_path, {
        "preferred_term": "Curie medium",
        "ingredients": [{
            "preferred_term": "Something", "term": {"id": "CHEBI:99999"},
            "role_curie": ["CHEBI:50906", "METPO:2000006"],
        }],
    })
    mmd = _render.render_single_recipe(recipe)
    assert "|curie|" in mmd
    assert "CHEBI:50906" in mmd
    assert "METPO:2000006" in mmd
    assert ":::role_curie" in mmd


def test_single_recipe_target_organisms_and_community_roles(tmp_path):
    recipe = _write(tmp_path, {
        "preferred_term": "Community medium",
        "ingredients": [{"preferred_term": "Glucose", "term": {"id": "CHEBI:17234"}}],
        "target_organisms": [{
            "preferred_term": "E. coli",
            "term": {"id": "NCBITaxon:562"},
            "community_role": ["PRIMARY_DEGRADER"],
        }],
    })
    mmd = _render.render_single_recipe(recipe)
    assert "NCBITaxon_562" in mmd
    assert "MEDIUM ==> NCBITaxon_562" in mmd
    assert "PRIMARY_DEGRADER" in mmd
    assert "|community-role|--> cor_PRIMARY_DEGRADER" in mmd


def test_single_recipe_nutrient_overrides(tmp_path):
    recipe = _write(tmp_path, {
        "preferred_term": "Override medium",
        "ingredients": [],
        "target_organisms": [{
            "preferred_term": "Test org",
            "term": {"id": "NCBITaxon:1"},
            "growth_metrics": [{
                "nutrient_overrides": [
                    {"role": "CARBON_SOURCE", "source": "succinate", "is_sole_source": True},
                ],
            }],
        }],
    })
    mmd = _render.render_single_recipe(recipe)
    assert "|nut-override|" in mmd
    assert "succinate (sole)" in mmd
    assert "[NutOverride: CARBON_SOURCE]" in mmd


def test_single_recipe_solutions_produce_solution_layer(tmp_path):
    recipe = _write(tmp_path, {
        "preferred_term": "Solution medium",
        "ingredients": [],
        "solutions": [{
            "preferred_term": "Vitamin mix",
            "term": {"id": "mediadive.solution:2227"},
            "composition": [
                {"preferred_term": "Biotin", "term": {"id": "CHEBI:15956"}},
                {"preferred_term": "Folic acid", "term": {"id": "CHEBI:27470"}},
            ],
        }],
    })
    mmd = _render.render_single_recipe(recipe)
    # Solution node styling.
    assert ":::solution" in mmd
    assert "MEDIUM -.-> mediadive_solution_2227" in mmd
    # Composition ingredients under the solution.
    assert "mediadive_solution_2227 --> CHEBI_15956" in mmd
    assert "mediadive_solution_2227 --> CHEBI_27470" in mmd


def test_single_recipe_max_ingredients_cap_emits_sentinel(tmp_path):
    ingredients = [
        {"preferred_term": f"ing_{i}", "term": {"id": f"CHEBI:{100 + i}"}}
        for i in range(50)
    ]
    recipe = _write(tmp_path, {"preferred_term": "Big medium", "ingredients": ingredients})
    mmd = _render.render_single_recipe(recipe, max_ingredients=10)
    # 10 ingredients rendered, 40 truncated.
    assert mmd.count(":::ingredient") == 10
    assert '...40 more ingredients (cap: 10)' in mmd
    assert ":::truncated" in mmd


def test_single_recipe_include_notes_flag(tmp_path):
    recipe = _write(tmp_path, {
        "preferred_term": "Noted medium",
        "ingredients": [{
            "preferred_term": "X", "term": {"id": "CHEBI:1"},
            "notes": "Role: Carbon source; From upstream MediaDive record 5",
        }],
    })
    without = _render.render_single_recipe(recipe, include_notes=False)
    assert "Role: Carbon source" not in without
    with_notes = _render.render_single_recipe(recipe, include_notes=True)
    assert "Role: Carbon source" in with_notes
    assert ":::note" in with_notes


def test_single_recipe_style_block_always_emitted(tmp_path):
    recipe = _write(tmp_path, {"preferred_term": "S", "ingredients": []})
    mmd = _render.render_single_recipe(recipe)
    for slot in ("nutritional_roles", "physicochemical_roles", "cellular_metabolic_roles"):
        assert f"classDef {slot}" in mmd


# ---------------- roll-up ----------------


def test_rollup_greenfield_corpus_reports_no_roles(tmp_path):
    """A corpus with no faceted role values renders an empty-state message, not a crash."""
    (tmp_path / "recipe.yaml").write_text(yaml.safe_dump({
        "preferred_term": "R",
        "ingredients": [
            {"preferred_term": "Glucose", "term": {"id": "CHEBI:17234"}},
        ],
    }))
    mmd = _render.render_rollup(tmp_path)
    assert "Corpus role roll-up" in mmd
    assert "No faceted role assignments found yet" in mmd


def test_rollup_aggregates_across_recipes(tmp_path):
    """Two recipes sharing CARBON_SOURCE on glucose → count == 2."""
    (tmp_path / "r1.yaml").write_text(yaml.safe_dump({
        "preferred_term": "R1",
        "ingredients": [{
            "preferred_term": "Glucose", "term": {"id": "CHEBI:17234"},
            "nutritional_roles": ["CARBON_SOURCE"],
        }],
    }))
    (tmp_path / "r2.yaml").write_text(yaml.safe_dump({
        "preferred_term": "R2",
        "ingredients": [{
            "preferred_term": "Glucose", "term": {"id": "CHEBI:17234"},
            "nutritional_roles": ["CARBON_SOURCE"],
        }],
    }))
    mmd = _render.render_rollup(tmp_path)
    assert "CHEBI:17234" in mmd
    assert "CARBON_SOURCE" in mmd
    # Weight-on-edge shows count.
    assert "nut: 2" in mmd


# ---------------- CLI smoke ----------------


def test_cli_requires_target_or_yaml_dir(capsys):
    with pytest.raises(SystemExit) as exc:
        _render.main([])
    assert exc.value.code == 2


def test_cli_single_stdout(tmp_path, capsys):
    recipe_yaml = _write(tmp_path, {
        "preferred_term": "CLI medium",
        "ingredients": [{"preferred_term": "X", "term": {"id": "CHEBI:1"}}],
    })
    rc = _render.main(["--target", str(recipe_yaml), "--stdout"])
    assert rc == 0
    captured = capsys.readouterr()
    assert "flowchart LR" in captured.out
    assert "CLI medium" in captured.out


def test_cli_batch_writes_files(tmp_path, capsys):
    (tmp_path / "a.yaml").write_text(yaml.safe_dump({
        "preferred_term": "A", "ingredients": [{"preferred_term": "x", "term": {"id": "CHEBI:1"}}],
    }))
    (tmp_path / "b.yaml").write_text(yaml.safe_dump({
        "preferred_term": "B", "ingredients": [{"preferred_term": "y", "term": {"id": "CHEBI:2"}}],
    }))
    out_dir = tmp_path / "out"
    rc = _render.main(["--yaml-dir", str(tmp_path), "--out-dir", str(out_dir), "--mode", "batch"])
    assert rc == 0
    assert (out_dir / "a.mmd").exists()
    assert (out_dir / "b.mmd").exists()
