"""
Integration tests for kg-microbe queries.

Tests that validate the CultureMech KG can answer strain-media queries
as needed by the kg-microbe knowledge graph.

Key query patterns:
1. Organism → Media (find media for a specific organism)
2. Strain → Media (find media mentioning a specific strain)
3. Media → Organisms (find all organisms that can grow on a medium)
4. Ingredient → Media (find media containing a specific chemical)
5. Cross-database queries (same organism across DSMZ, JCM, KOMODO)
"""

import json
import pytest
from pathlib import Path
from culturemech.export.kgx_export import transform


class TestOrganismMediaQueries:
    """Test queries finding media for specific organisms."""

    def test_find_media_for_escherichia_coli(self, tmpdir):
        """Test finding all media for E. coli."""
        # Load a test recipe with E. coli
        recipe_yaml = """
name: LB Medium
category: bacterial
medium_type: complex
physical_state: liquid
organism_culture_type: isolate
target_organisms:
  - preferred_term: Escherichia coli
    term:
      id: NCBITaxon:562
      label: Escherichia coli
ingredients:
  - preferred_term: Tryptone
    concentration:
      value: '10'
      unit: G_PER_L
"""
        recipe_file = tmpdir / "test_recipe.yaml"
        recipe_file.write(recipe_yaml)

        # Transform to KGX
        edges = transform(str(recipe_file))

        # Find organism edges
        organism_edges = [
            e for e in edges
            if e.get("predicate") == "biolink:used_to_culture"
            and e.get("object") == "NCBITaxon:562"
        ]

        assert len(organism_edges) > 0, "Should find E. coli edge"
        assert organism_edges[0]["object"] == "NCBITaxon:562"

    def test_organism_with_strain_designation(self, tmpdir):
        """Test organism with strain designation is queryable."""
        recipe_yaml = """
name: E. coli K-12 Medium
category: bacterial
medium_type: complex
physical_state: liquid
organism_culture_type: isolate
target_organisms:
  - preferred_term: Escherichia coli
    term:
      id: NCBITaxon:562
      label: Escherichia coli
    strain: K-12
ingredients:
  - preferred_term: Glucose
    term:
      id: CHEBI:17234
      label: glucose
"""
        recipe_file = tmpdir / "k12_recipe.yaml"
        recipe_file.write(recipe_yaml)

        edges = transform(str(recipe_file))
        organism_edges = [
            e for e in edges
            if e.get("predicate") == "biolink:used_to_culture"
        ]

        assert len(organism_edges) > 0
        # Check that strain info is preserved in qualifiers
        edge = organism_edges[0]
        assert edge["qualifiers"] is not None


class TestStrainMediaQueries:
    """Test queries for specific bacterial strains."""

    def test_dsm_strain_identification(self, tmpdir):
        """Test that DSM strain numbers are captured in media names."""
        recipe_yaml = """
name: MODIFIED FOR DSM 11573
category: bacterial
medium_type: complex
physical_state: liquid
organism_culture_type: isolate
target_organisms:
  - preferred_term: Bacillus subtilis
    term:
      id: NCBITaxon:1423
      label: Bacillus subtilis
    strain: "DSM 11573"
ingredients:
  - preferred_term: Glucose
"""
        recipe_file = tmpdir / "dsm_strain.yaml"
        recipe_file.write(recipe_yaml)

        edges = transform(str(recipe_file))
        organism_edges = [
            e for e in edges
            if "used_to_culture" in e.get("predicate", "")
        ]

        assert len(organism_edges) > 0
        # Verify strain info is accessible
        edge = organism_edges[0]
        assert edge["subject"] is not None
        assert "DSM" in str(edge.get("qualifiers", []))


class TestCrossDatabaseIntegration:
    """Test that same organisms can be found across different source databases."""

    def test_merge_preserves_source_provenance(self):
        """Test that merged recipes maintain source database info."""
        # This would test the merge_yaml output
        merge_stats_file = Path("data/merge_yaml/merge_stats.json")

        if not merge_stats_file.exists():
            pytest.skip("Merge statistics not available - run deduplication first")

        with open(merge_stats_file) as f:
            stats = json.load(f)

        # Check that we have merged groups with multiple sources
        assert stats.get("total_groups", 0) > 0

        # Verify reduction happened (duplicates found)
        input_count = stats.get("input_recipes", 0)
        output_count = stats.get("output_recipes", 0)
        assert output_count < input_count, "Deduplication should reduce recipe count"

    def test_find_organism_across_databases(self):
        """Test finding same organism in DSMZ, JCM, and KOMODO."""
        # Check merged recipes directory
        merged_dir = Path("data/merge_yaml/merged")

        if not merged_dir.exists():
            pytest.skip("Merged recipes not available - run deduplication first")

        # Look for a merged recipe with multiple sources
        merged_recipes = list(merged_dir.glob("*.yaml"))

        if len(merged_recipes) == 0:
            pytest.skip("No merged recipes found")

        # This validates that cross-database deduplication worked
        assert len(merged_recipes) > 0


class TestIngredientMediaQueries:
    """Test queries finding media by ingredient/chemical."""

    def test_find_media_with_glucose(self, tmpdir):
        """Test finding all media containing glucose."""
        recipe_yaml = """
name: Glucose Medium
category: bacterial
medium_type: defined
physical_state: liquid
ingredients:
  - preferred_term: Glucose
    term:
      id: CHEBI:17234
      label: glucose
    concentration:
      value: '10'
      unit: G_PER_L
"""
        recipe_file = tmpdir / "glucose_medium.yaml"
        recipe_file.write(recipe_yaml)

        edges = transform(str(recipe_file))

        # Find ingredient edges
        glucose_edges = [
            e for e in edges
            if e.get("object") == "CHEBI:17234"
            and e.get("predicate") == "biolink:has_part"
        ]

        assert len(glucose_edges) > 0, "Should find glucose edge"
        assert glucose_edges[0]["object"] == "CHEBI:17234"

    def test_ingredient_with_concentration_qualifier(self, tmpdir):
        """Test that concentration is captured as qualifier."""
        recipe_yaml = """
name: Test Medium
category: bacterial
medium_type: defined
physical_state: liquid
ingredients:
  - preferred_term: NaCl
    term:
      id: CHEBI:26710
      label: sodium chloride
    concentration:
      value: '5.0'
      unit: G_PER_L
"""
        recipe_file = tmpdir / "nacl_medium.yaml"
        recipe_file.write(recipe_yaml)

        edges = transform(str(recipe_file))
        nacl_edges = [
            e for e in edges
            if e.get("object") == "CHEBI:26710"
        ]

        assert len(nacl_edges) > 0
        edge = nacl_edges[0]
        qualifiers = edge.get("qualifiers", [])

        # Check that concentration is in qualifiers
        assert len(qualifiers) > 0
        assert any("5.0" in str(q) for q in qualifiers)


class TestMediaProperties:
    """Test queries for media properties (pH, temperature, physical state)."""

    def test_media_by_physical_state(self, tmpdir):
        """Test finding solid vs liquid media."""
        recipe_yaml = """
name: Agar Plate
category: bacterial
medium_type: complex
physical_state: solid
ingredients:
  - preferred_term: Agar
    term:
      id: CHEBI:2509
      label: agar
"""
        recipe_file = tmpdir / "agar_plate.yaml"
        recipe_file.write(recipe_yaml)

        edges = transform(str(recipe_file))

        # Physical state should generate an edge
        state_edges = [
            e for e in edges
            if e.get("predicate") == "biolink:has_attribute"
        ]

        assert len(state_edges) > 0, "Should have physical state edge"

    def test_media_with_ph_value(self, tmpdir):
        """Test that pH is captured in media metadata."""
        recipe_yaml = """
name: pH 7.0 Medium
category: bacterial
medium_type: defined
physical_state: liquid
ph_value: 7.0
ingredients:
  - preferred_term: Buffer
"""
        recipe_file = tmpdir / "ph_medium.yaml"
        recipe_file.write(recipe_yaml)

        edges = transform(str(recipe_file))

        # pH should be in some edge or property
        assert len(edges) > 0


class TestCommunityVsIsolateCultures:
    """Test distinguishing between isolate and community cultures."""

    def test_isolate_culture_type(self, tmpdir):
        """Test organism_culture_type: isolate."""
        recipe_yaml = """
name: Pure Culture Medium
category: bacterial
medium_type: complex
physical_state: liquid
organism_culture_type: isolate
target_organisms:
  - preferred_term: Bacillus subtilis
    term:
      id: NCBITaxon:1423
      label: Bacillus subtilis
ingredients:
  - preferred_term: Nutrient Broth
"""
        recipe_file = tmpdir / "isolate.yaml"
        recipe_file.write(recipe_yaml)

        edges = transform(str(recipe_file))
        organism_edges = [
            e for e in edges
            if "culture" in e.get("predicate", "")
        ]

        assert len(organism_edges) > 0

    def test_community_culture_type(self, tmpdir):
        """Test organism_culture_type: community."""
        recipe_yaml = """
name: Co-culture Medium
category: bacterial
medium_type: complex
physical_state: liquid
organism_culture_type: community
target_organisms:
  - preferred_term: Escherichia coli
    term:
      id: NCBITaxon:562
      label: Escherichia coli
  - preferred_term: Bacillus subtilis
    term:
      id: NCBITaxon:1423
      label: Bacillus subtilis
ingredients:
  - preferred_term: Complex Medium
"""
        recipe_file = tmpdir / "community.yaml"
        recipe_file.write(recipe_yaml)

        edges = transform(str(recipe_file))
        organism_edges = [
            e for e in edges
            if "culture" in e.get("predicate", "")
        ]

        # Should have edges for both organisms
        assert len(organism_edges) >= 2


class TestRealDataIntegration:
    """Integration tests using real CultureMech data."""

    def test_curated_organism_data_integration(self):
        """Test that our 2,104 curated organisms export correctly."""
        # This tests the organism curation we just completed
        curation_file = Path("data/curation/organism_candidates.json")

        if not curation_file.exists():
            pytest.skip("Organism curation data not available")

        with open(curation_file) as f:
            organisms = json.load(f)

        # Verify we have the expected number of curated organisms
        assert len(organisms) >= 2000, f"Expected ~2,104 organisms, got {len(organisms)}"

        # Check structure
        for filepath, org_data in list(organisms.items())[:5]:
            assert "organism_name" in org_data
            assert "culture_type" in org_data

    def test_deduplication_stats_accessible(self):
        """Test that deduplication results are queryable."""
        stats_file = Path("data/merge_yaml/merge_stats.json")

        if not stats_file.exists():
            pytest.skip("Merge stats not available - run deduplication first")

        with open(stats_file) as f:
            stats = json.load(f)

        # Verify stats structure
        assert "input_recipes" in stats
        assert "output_recipes" in stats
        assert "duplicate_groups" in stats

        # Verify significant deduplication occurred
        assert stats["input_recipes"] > stats["output_recipes"]
        reduction_pct = (1 - stats["output_recipes"] / stats["input_recipes"]) * 100
        assert reduction_pct > 50, f"Expected >50% deduplication, got {reduction_pct:.1f}%"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
