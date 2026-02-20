"""Integration tests for enrichment pipeline."""

import json
import tempfile
from pathlib import Path

import pytest
import yaml

from culturemech.enrich.backfill_pipeline import EnrichmentBackfillPipeline
from culturemech.enrich.multi_database_crossref import MultiDatabaseCrossRef


class TestATCCCrossRefBackfill:
    """Test ATCC cross-reference backfill functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.pipeline = EnrichmentBackfillPipeline()

    def create_test_yaml(self, filename: str, data: dict) -> Path:
        """Create a test YAML file."""
        path = self.temp_dir / filename
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        return path

    def create_test_crossref(self) -> Path:
        """Create a test ATCC cross-reference file."""
        crossref_data = {
            "1": {
                "dsmz": "1",
                "name": "NUTRIENT AGAR",
                "verified": True,
                "verification_date": "2026-02-19",
                "composition_match": "verified"
            },
            "325": {
                "dsmz": "130",
                "name": "CZAPEK-DOX AGAR",
                "verified": True,
                "verification_date": "2026-02-19",
                "composition_match": "verified"
            }
        }

        path = self.temp_dir / "atcc_crossref.json"
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(crossref_data, f, indent=2)
        return path

    def test_atcc_crossref_backfill_adds_reference(self):
        """Test that ATCC cross-references are correctly added to DSMZ files."""
        # Create DSMZ file without ATCC reference
        dsmz_data = {
            "name": "NUTRIENT AGAR",
            "category": "bacterial",
            "medium_type": "SOLID",
            "physical_state": "SOLID",
            "ingredients": [
                {"preferred_term": "Peptone"},
                {"preferred_term": "NaCl"}
            ],
            "notes": "Original notes here"
        }

        yaml_file = self.create_test_yaml("DSMZ_1_NUTRIENT_AGAR.yaml", dsmz_data)
        crossref_file = self.create_test_crossref()

        # Apply backfill
        self.pipeline.apply_atcc_crossrefs(self.temp_dir, crossref_file, dry_run=False)

        # Load updated file
        with open(yaml_file, 'r', encoding='utf-8') as f:
            updated = yaml.safe_load(f)

        # Verify ATCC reference added to notes
        assert "ATCC:1" in updated["notes"]
        assert "Cross-reference" in updated["notes"]
        assert "Original notes here" in updated["notes"]

        # Verify curation history entry
        assert "curation_history" in updated
        history = updated["curation_history"]
        assert len(history) > 0
        last_entry = history[-1]
        assert last_entry["curator"] == "atcc-crossref-backfill"
        assert "ATCC:1" in last_entry["notes"]

    def test_atcc_crossref_backfill_skips_existing(self):
        """Test that ATCC backfill skips files that already have the reference."""
        # Create DSMZ file WITH ATCC reference
        dsmz_data = {
            "name": "NUTRIENT AGAR",
            "category": "bacterial",
            "medium_type": "SOLID",
            "physical_state": "SOLID",
            "ingredients": [{"preferred_term": "Peptone"}],
            "notes": "Already has Cross-reference: ATCC:1 (NUTRIENT AGAR)",
            "curation_history": [
                {
                    "timestamp": "2026-02-18T12:00:00.000000Z",
                    "curator": "previous-curator",
                    "action": "Initial import"
                }
            ]
        }

        yaml_file = self.create_test_yaml("DSMZ_1_NUTRIENT_AGAR.yaml", dsmz_data)
        crossref_file = self.create_test_crossref()

        # Apply backfill
        self.pipeline.apply_atcc_crossrefs(self.temp_dir, crossref_file, dry_run=False)

        # Load file
        with open(yaml_file, 'r', encoding='utf-8') as f:
            updated = yaml.safe_load(f)

        # Should not have duplicate entry
        assert updated["notes"].count("ATCC:1") == 1

        # Curation history should NOT have new entry
        assert len(updated["curation_history"]) == 1
        assert updated["curation_history"][0]["curator"] == "previous-curator"

    def test_atcc_crossref_dry_run(self):
        """Test that dry run mode doesn't modify files."""
        dsmz_data = {
            "name": "NUTRIENT AGAR",
            "category": "bacterial",
            "medium_type": "SOLID",
            "physical_state": "SOLID",
            "ingredients": [{"preferred_term": "Peptone"}]
        }

        yaml_file = self.create_test_yaml("DSMZ_1_NUTRIENT_AGAR.yaml", dsmz_data)
        crossref_file = self.create_test_crossref()

        # Apply backfill in dry run mode
        self.pipeline.apply_atcc_crossrefs(self.temp_dir, crossref_file, dry_run=True)

        # Load file
        with open(yaml_file, 'r', encoding='utf-8') as f:
            updated = yaml.safe_load(f)

        # Should be unchanged
        assert "ATCC" not in updated.get("notes", "")
        assert "curation_history" not in updated


class TestOrganismDataBackfill:
    """Test organism data backfill functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.pipeline = EnrichmentBackfillPipeline()

    def create_test_yaml(self, filename: str, data: dict) -> Path:
        """Create a test YAML file."""
        path = self.temp_dir / filename
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        return path

    def create_test_organism_data(self) -> Path:
        """Create test organism curation data."""
        # Use just the filename as the key (pipeline will resolve paths)
        organism_data = {
            "DSMZ_105_GLUCONOBACTER_OXYDANS_MEDIUM.yaml": {
                "organism_name": "Gluconobacter oxydans",
                "ncbi_taxon_id": "442",
                "culture_type": "isolate",
                "strain": "DSM 3503"
            },
            "TOGO_M123_ESCHERICHIA_COLI.yaml": {
                "organism_name": "Escherichia coli",
                "ncbi_taxon_id": "562",
                "culture_type": "isolate"
            }
        }

        path = self.temp_dir / "organism_candidates.json"
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(organism_data, f, indent=2)
        return path

    def test_organism_data_backfill_adds_complete_data(self):
        """Test that organism data is correctly added with all fields."""
        # Create recipe without organism data
        recipe_data = {
            "name": "GLUCONOBACTER OXYDANS MEDIUM",
            "category": "bacterial",
            "medium_type": "COMPLEX",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "Glucose"}]
        }

        yaml_file = self.create_test_yaml("DSMZ_105_GLUCONOBACTER_OXYDANS_MEDIUM.yaml", recipe_data)
        organism_file = self.create_test_organism_data()

        # Apply backfill
        self.pipeline.apply_organism_data(self.temp_dir, organism_file, dry_run=False)

        # Load updated file
        with open(yaml_file, 'r', encoding='utf-8') as f:
            updated = yaml.safe_load(f)

        # Verify organism_culture_type added
        assert updated["organism_culture_type"] == "isolate"

        # Verify target_organisms added
        assert "target_organisms" in updated
        organisms = updated["target_organisms"]
        assert len(organisms) == 1

        org = organisms[0]
        assert org["preferred_term"] == "Gluconobacter oxydans"
        assert org["term"]["id"] == "NCBITaxon:442"
        assert org["term"]["label"] == "Gluconobacter oxydans"
        assert org["strain"] == "DSM 3503"

        # Verify curation history
        assert "curation_history" in updated
        history = updated["curation_history"]
        assert len(history) > 0
        last_entry = history[-1]
        assert last_entry["curator"] == "organism-data-backfill"
        assert "Gluconobacter oxydans" in last_entry["notes"]

    def test_organism_data_backfill_skips_existing(self):
        """Test that organism backfill skips files with existing organism data."""
        # Create recipe WITH organism data
        recipe_data = {
            "name": "ESCHERICHIA COLI MEDIUM",
            "category": "bacterial",
            "medium_type": "COMPLEX",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "Glucose"}],
            "organism_culture_type": "isolate",
            "target_organisms": [
                {
                    "preferred_term": "Existing organism",
                    "term": {"id": "NCBITaxon:999", "label": "Existing"}
                }
            ]
        }

        yaml_file = self.create_test_yaml("TOGO_M123_ESCHERICHIA_COLI.yaml", recipe_data)
        organism_file = self.create_test_organism_data()

        # Apply backfill
        self.pipeline.apply_organism_data(self.temp_dir, organism_file, dry_run=False)

        # Load file
        with open(yaml_file, 'r', encoding='utf-8') as f:
            updated = yaml.safe_load(f)

        # Should NOT overwrite existing data
        assert updated["target_organisms"][0]["preferred_term"] == "Existing organism"
        assert updated["target_organisms"][0]["term"]["id"] == "NCBITaxon:999"

    def test_organism_data_backfill_filters_invalid_names(self):
        """Test that invalid organism names are filtered out."""
        # Create organism data with invalid entry
        organism_data = {
            "test_file.yaml": {
                "organism_name": "Strain",  # Invalid - should be filtered
                "ncbi_taxon_id": "999",
                "culture_type": "isolate"
            }
        }

        organism_file = self.temp_dir / "organism_candidates.json"
        with open(organism_file, 'w', encoding='utf-8') as f:
            json.dump(organism_data, f, indent=2)

        recipe_data = {
            "name": "Test Medium",
            "category": "bacterial",
            "ingredients": [{"preferred_term": "NaCl"}]
        }

        self.create_test_yaml("test_file.yaml", recipe_data)

        # Apply backfill
        self.pipeline.apply_organism_data(self.temp_dir, organism_file, dry_run=False)

        # File should remain unchanged (invalid name skipped)
        with open(self.temp_dir / "test_file.yaml", 'r', encoding='utf-8') as f:
            updated = yaml.safe_load(f)

        assert "target_organisms" not in updated
        assert "organism_culture_type" not in updated


class TestMultiDatabaseCrossRef:
    """Test multi-database cross-reference generation."""

    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.builder = MultiDatabaseCrossRef()

    def create_test_yaml(self, filename: str, data: dict) -> Path:
        """Create a test YAML file."""
        path = self.temp_dir / filename
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        return path

    def test_name_similarity_exact_match(self):
        """Test name similarity with exact match."""
        similarity = self.builder.name_similarity(
            "LB MEDIUM",
            "LB MEDIUM"
        )
        assert similarity == 1.0

    def test_name_similarity_high_match(self):
        """Test name similarity with high similarity."""
        similarity = self.builder.name_similarity(
            "TRYPTONE SOYA AGAR",
            "TRYPTICASE SOY AGAR"
        )
        # These are similar but not identical (different spellings)
        assert similarity > 0.7
        assert similarity < 0.9

    def test_name_normalization(self):
        """Test name normalization removes prefixes and suffixes."""
        normalized = self.builder.normalize_name("DSMZ MEDIUM 1: LB AGAR")
        assert "LB" in normalized
        assert "DSMZ" not in normalized

    def test_ingredient_similarity_identical(self):
        """Test ingredient similarity with identical lists."""
        ingredients1 = ["GLUCOSE", "NACL", "PEPTONE"]
        ingredients2 = ["GLUCOSE", "NACL", "PEPTONE"]

        similarity = self.builder.ingredient_similarity(ingredients1, ingredients2)
        assert similarity == 1.0

    def test_ingredient_similarity_partial(self):
        """Test ingredient similarity with partial overlap."""
        ingredients1 = ["GLUCOSE", "NACL", "PEPTONE"]
        ingredients2 = ["GLUCOSE", "NACL", "YEAST EXTRACT"]

        similarity = self.builder.ingredient_similarity(ingredients1, ingredients2)
        # 2 shared / 4 total = 0.5
        assert similarity == 0.5

    def test_ingredient_similarity_empty(self):
        """Test ingredient similarity with empty lists."""
        similarity = self.builder.ingredient_similarity([], ["GLUCOSE"])
        assert similarity == 0.0

    def test_cross_reference_detection_by_name(self):
        """Test cross-reference detection based on name similarity."""
        # Create TOGO file
        togo_data = {
            "name": "LB MEDIUM",
            "media_term": {"term": {"id": "TOGO:M001", "label": "LB Medium"}},
            "ingredients": [
                {"preferred_term": "TRYPTONE"},
                {"preferred_term": "YEAST EXTRACT"},
                {"preferred_term": "NACL"}
            ]
        }
        self.create_test_yaml("TOGO_M001_LB.yaml", togo_data)

        # Create DSMZ file with same name
        dsmz_data = {
            "name": "LB MEDIUM",
            "media_term": {"term": {"id": "DSMZ:1", "label": "LB Medium"}},
            "ingredients": [
                {"preferred_term": "TRYPTONE"},
                {"preferred_term": "YEAST EXTRACT"},
                {"preferred_term": "NACL"}
            ]
        }
        self.create_test_yaml("DSMZ_1_LB.yaml", dsmz_data)

        # Load files
        self.builder.load_media_files(self.temp_dir)

        # Verify files were loaded
        assert "TOGO" in self.builder.media_by_source
        assert "DSMZ" in self.builder.media_by_source
        assert len(self.builder.media_by_source["TOGO"]) > 0
        assert len(self.builder.media_by_source["DSMZ"]) > 0

        # Find cross-references
        candidates = self.builder.find_cross_references("TOGO", "DSMZ")

        # Should find at least one candidate
        assert len(candidates) > 0

        # First candidate should have high confidence (exact match)
        assert candidates[0]["confidence"] == "high"
        # Verify it found the right pair (check that IDs are present)
        assert "TOGO_id" in candidates[0]
        assert "DSMZ_id" in candidates[0]
        # Both name and ingredient similarity should be very high for exact match
        assert candidates[0]["name_similarity"] >= 0.95
        assert candidates[0]["ingredient_similarity"] >= 0.95

    def test_cross_reference_detection_by_ingredients(self):
        """Test cross-reference detection based on ingredient similarity."""
        # Create files with different names but identical ingredients
        togo_data = {
            "name": "TOGO SPECIAL MEDIUM",
            "media_term": {"term": {"id": "TOGO:M999", "label": "Special"}},
            "ingredients": [
                {"preferred_term": "RARE_COMPOUND_A"},
                {"preferred_term": "RARE_COMPOUND_B"},
                {"preferred_term": "RARE_COMPOUND_C"}
            ]
        }
        self.create_test_yaml("TOGO_M999_SPECIAL.yaml", togo_data)

        dsmz_data = {
            "name": "DSMZ UNIQUE FORMULATION",
            "media_term": {"term": {"id": "DSMZ:999", "label": "Unique"}},
            "ingredients": [
                {"preferred_term": "RARE_COMPOUND_A"},
                {"preferred_term": "RARE_COMPOUND_B"},
                {"preferred_term": "RARE_COMPOUND_C"}
            ]
        }
        self.create_test_yaml("DSMZ_999_UNIQUE.yaml", dsmz_data)

        # Load files
        self.builder.load_media_files(self.temp_dir)

        # Find cross-references
        candidates = self.builder.find_cross_references("TOGO", "DSMZ")

        # Should find match based on ingredients
        assert len(candidates) > 0

        # Check that ingredient similarity is high
        match = candidates[0]
        assert match["ingredient_similarity"] >= 0.75


class TestEnrichmentPipelineIntegration:
    """End-to-end integration tests for enrichment pipeline."""

    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.pipeline = EnrichmentBackfillPipeline()

    def create_test_yaml(self, filename: str, data: dict) -> Path:
        """Create a test YAML file."""
        path = self.temp_dir / filename
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        return path

    def test_full_pipeline_execution(self):
        """Test complete pipeline with ATCC and organism enrichments."""
        # Create ATCC cross-reference data
        atcc_crossref = {
            "1": {
                "dsmz": "1",
                "name": "NUTRIENT AGAR",
                "verified": True,
                "verification_date": "2026-02-19"
            }
        }
        atcc_file = self.temp_dir / "atcc_crossref.json"
        with open(atcc_file, 'w', encoding='utf-8') as f:
            json.dump(atcc_crossref, f, indent=2)

        # Create organism data
        organism_data = {
            "DSMZ_1_NUTRIENT_AGAR.yaml": {
                "organism_name": "Bacillus subtilis",
                "ncbi_taxon_id": "1423",
                "culture_type": "isolate"
            }
        }
        organism_file = self.temp_dir / "organism_candidates.json"
        with open(organism_file, 'w', encoding='utf-8') as f:
            json.dump(organism_data, f, indent=2)

        # Create DSMZ YAML file
        dsmz_data = {
            "name": "NUTRIENT AGAR",
            "category": "bacterial",
            "medium_type": "SOLID",
            "physical_state": "SOLID",
            "ingredients": [{"preferred_term": "Peptone"}]
        }
        self.create_test_yaml("DSMZ_1_NUTRIENT_AGAR.yaml", dsmz_data)

        # Run full pipeline
        self.pipeline.run_full_pipeline(
            self.temp_dir,
            atcc_crossref_file=atcc_file,
            organism_file=organism_file,
            dry_run=False
        )

        # Load enriched file
        with open(self.temp_dir / "DSMZ_1_NUTRIENT_AGAR.yaml", 'r', encoding='utf-8') as f:
            enriched = yaml.safe_load(f)

        # Verify ATCC cross-reference added
        assert "ATCC:1" in enriched["notes"]

        # Verify organism data added
        assert enriched["organism_culture_type"] == "isolate"
        assert "target_organisms" in enriched
        assert enriched["target_organisms"][0]["preferred_term"] == "Bacillus subtilis"

        # Verify multiple curation history entries
        assert "curation_history" in enriched
        assert len(enriched["curation_history"]) == 2

        curators = [entry["curator"] for entry in enriched["curation_history"]]
        assert "atcc-crossref-backfill" in curators
        assert "organism-data-backfill" in curators

        # Verify statistics
        assert self.pipeline.stats["atcc_refs_added"] == 1
        assert self.pipeline.stats["organism_data_added"] == 1
        assert self.pipeline.stats["errors"] == 0

    def test_schema_validation_after_enrichment(self):
        """Test that enriched files maintain schema compliance."""
        # Create minimal valid recipe
        recipe_data = {
            "name": "TEST MEDIUM",
            "category": "bacterial",
            "medium_type": "COMPLEX",
            "physical_state": "LIQUID",
            "ingredients": [
                {
                    "preferred_term": "Glucose",
                    "term": {
                        "id": "CHEBI:17234",
                        "label": "glucose"
                    }
                }
            ]
        }

        # Create organism data
        organism_data = {
            "TEST_MEDIUM.yaml": {
                "organism_name": "Escherichia coli",
                "ncbi_taxon_id": "562",
                "culture_type": "isolate",
                "strain": "K-12"
            }
        }
        organism_file = self.temp_dir / "organism_candidates.json"
        with open(organism_file, 'w', encoding='utf-8') as f:
            json.dump(organism_data, f, indent=2)

        yaml_file = self.create_test_yaml("TEST_MEDIUM.yaml", recipe_data)

        # Apply enrichment
        self.pipeline.apply_organism_data(self.temp_dir, organism_file, dry_run=False)

        # Load enriched file
        with open(yaml_file, 'r', encoding='utf-8') as f:
            enriched = yaml.safe_load(f)

        # Verify required schema fields are present
        assert "name" in enriched
        assert "category" in enriched
        assert "medium_type" in enriched
        assert "physical_state" in enriched
        assert "ingredients" in enriched

        # Verify enriched fields have correct structure
        assert isinstance(enriched["organism_culture_type"], str)
        assert enriched["organism_culture_type"] in ["isolate", "community"]

        assert isinstance(enriched["target_organisms"], list)
        assert len(enriched["target_organisms"]) > 0

        org = enriched["target_organisms"][0]
        assert "preferred_term" in org
        assert "term" in org
        assert "id" in org["term"]
        assert org["term"]["id"].startswith("NCBITaxon:")
        assert "strain" in org

        # Verify curation history structure
        assert isinstance(enriched["curation_history"], list)
        entry = enriched["curation_history"][0]
        assert "timestamp" in entry
        assert "curator" in entry
        assert "action" in entry
        assert "notes" in entry
