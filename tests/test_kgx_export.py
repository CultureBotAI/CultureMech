"""
Unit tests for KGX export module.

Tests the transform functions that extract edges from recipe YAML.
"""

import pytest
from culturemech.export.kgx_export import (
    transform,
    ingredient_to_edge,
    organism_to_edge,
    application_to_edge,
    physical_state_to_edge,
    database_reference_to_edge,
    variant_to_edge,
    _get_term_id,
    _format_evidence,
    _sanitize_id,
    _make_edge_id,
)


class TestIngredientToEdge:
    """Test ingredient to edge conversion."""

    def test_with_valid_chebi_term(self):
        """Test ingredient with CHEBI term generates edge."""
        medium_id = "culturemech:LB_Broth"
        ingredient = {
            "preferred_term": "Glucose",
            "term": {"id": "CHEBI:17234", "label": "glucose"},
            "concentration": {"value": "10", "unit": "G_PER_L"},
        }
        edge = ingredient_to_edge(medium_id, ingredient)

        assert edge is not None
        assert edge["subject"] == medium_id
        assert edge["object"] == "CHEBI:17234"
        assert edge["predicate"] == "biolink:has_part"
        assert edge["qualifiers"] is not None
        assert any("10 G_PER_L" in str(q) for q in edge["qualifiers"])

    def test_without_term_returns_none(self):
        """Test ingredient without term is skipped."""
        ingredient = {
            "preferred_term": "Yeast Extract",
            "concentration": {"value": "5", "unit": "G_PER_L"},
        }
        edge = ingredient_to_edge("culturemech:LB", ingredient)
        assert edge is None

    def test_with_evidence(self):
        """Test ingredient with evidence includes publications."""
        medium_id = "culturemech:LB_Broth"
        ingredient = {
            "preferred_term": "Glucose",
            "term": {"id": "CHEBI:17234"},
            "concentration": {"value": "10", "unit": "G_PER_L"},
            "evidence": [
                {
                    "reference": "PMID:12345678",
                    "supports": "SUPPORT",
                    "explanation": "Test evidence"
                }
            ]
        }
        edge = ingredient_to_edge(medium_id, ingredient)

        assert edge is not None
        assert edge["publications"] is not None
        assert "PMID:12345678" in edge["publications"]


class TestOrganismToEdge:
    """Test organism to edge conversion."""

    def test_with_ncbitaxon(self):
        """Test organism with NCBITaxon generates edge."""
        organism = {
            "preferred_term": "Escherichia coli",
            "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
        }
        edge = organism_to_edge("culturemech:LB", organism)

        assert edge is not None
        assert edge["subject"] == "culturemech:LB"
        assert edge["object"] == "NCBITaxon:562"
        assert edge["predicate"] == "biolink:affects"

    def test_without_term_returns_none(self):
        """Test organism without term is skipped."""
        organism = {
            "preferred_term": "Escherichia coli",
            "strain": "K-12"
        }
        edge = organism_to_edge("culturemech:LB", organism)
        assert edge is None


class TestApplicationToEdge:
    """Test application to edge conversion."""

    def test_creates_application_edge(self):
        """Test application string creates edge."""
        edge = application_to_edge("culturemech:LB", "Plasmid amplification")

        assert edge is not None
        assert edge["subject"] == "culturemech:LB"
        assert edge["predicate"] == "biolink:has_attribute"
        assert "application" in edge["object"]

    def test_sanitizes_application_name(self):
        """Test application name is sanitized in ID."""
        edge = application_to_edge("culturemech:LB", "Protein expression (high yield)")

        assert edge is not None
        assert "(" not in edge["object"]
        assert ")" not in edge["object"]


class TestPhysicalStateToEdge:
    """Test physical state to edge conversion."""

    def test_creates_state_edge(self):
        """Test physical state creates edge."""
        edge = physical_state_to_edge("culturemech:LB", "LIQUID")

        assert edge is not None
        assert edge["subject"] == "culturemech:LB"
        assert edge["object"] == "culturemech:state_liquid"
        assert edge["predicate"] == "biolink:has_attribute"


class TestDatabaseReferenceToEdge:
    """Test database reference to edge conversion."""

    def test_creates_sameas_edge(self):
        """Test database reference creates same_as edge."""
        term = {"id": "DSMZ:1", "label": "DSMZ Medium 1"}
        edge = database_reference_to_edge("culturemech:LB", term)

        assert edge is not None
        assert edge["subject"] == "culturemech:LB"
        assert edge["object"] == "DSMZ:1"
        assert edge["predicate"] == "biolink:same_as"

    def test_without_id_returns_none(self):
        """Test term without ID returns None."""
        term = {"label": "Some medium"}
        edge = database_reference_to_edge("culturemech:LB", term)
        assert edge is None


class TestVariantToEdge:
    """Test variant to edge conversion."""

    def test_creates_variant_edge(self):
        """Test variant creates subclass_of edge."""
        variant = {
            "name": "LB Agar",
            "description": "Solidified LB"
        }
        edge = variant_to_edge("culturemech:LB_Broth", variant)

        assert edge is not None
        assert edge["object"] == "culturemech:LB_Broth"
        assert "LB_Agar" in edge["subject"]
        assert edge["predicate"] == "biolink:subclass_of"

    def test_without_name_returns_none(self):
        """Test variant without name returns None."""
        variant = {"description": "Some variant"}
        edge = variant_to_edge("culturemech:LB", variant)
        assert edge is None


class TestTransform:
    """Test complete recipe transformation."""

    def test_full_recipe_transform(self):
        """Test complete recipe with multiple edge types."""
        record = {
            "name": "LB Broth",
            "medium_type": "COMPLEX",
            "physical_state": "LIQUID",
            "ingredients": [
                {
                    "preferred_term": "Glucose",
                    "term": {"id": "CHEBI:17234"},
                    "concentration": {"value": "10", "unit": "G_PER_L"},
                }
            ],
            "target_organisms": [
                {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562"},
                }
            ],
            "applications": ["Plasmid amplification"],
        }

        edges = list(transform(record))

        # Should have: ingredient + organism + application + physical_state
        assert len(edges) >= 3
        subjects = [e["subject"] for e in edges]
        assert "culturemech:LB_Broth" in subjects

    def test_minimal_recipe(self):
        """Test recipe with minimal required fields."""
        record = {
            "name": "Minimal Medium",
            "medium_type": "DEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                {
                    "preferred_term": "Water",
                    "concentration": {"value": "1", "unit": "G_PER_L"},
                }
            ],
        }

        edges = list(transform(record))

        # Should at least have physical_state edge
        assert len(edges) >= 1


class TestHelperFunctions:
    """Test helper utility functions."""

    def test_get_term_id_simple(self):
        """Test extracting term ID from nested dict."""
        data = {"term": {"id": "CHEBI:12345"}}
        term_id = _get_term_id(data, ["term", "id"])
        assert term_id == "CHEBI:12345"

    def test_get_term_id_missing(self):
        """Test extracting missing term ID returns None."""
        data = {"term": {}}
        term_id = _get_term_id(data, ["term", "id"])
        assert term_id is None

    def test_format_evidence_empty(self):
        """Test formatting empty evidence."""
        pubs, text = _format_evidence(None)
        assert pubs == []
        assert text == []

    def test_format_evidence_with_refs(self):
        """Test formatting evidence with references."""
        evidence = [
            {"reference": "PMID:12345", "explanation": "Test"},
            {"reference": "DOI:10.1234/test", "explanation": "Test 2"}
        ]
        pubs, _ = _format_evidence(evidence)
        assert len(pubs) == 2
        assert "PMID:12345" in pubs
        assert "DOI:10.1234/test" in pubs

    def test_sanitize_id(self):
        """Test ID sanitization."""
        assert _sanitize_id("Test Name") == "Test_Name"
        assert _sanitize_id("Test (variant)") == "Test_variant"
        assert _sanitize_id("Test/Path") == "Test_Path"

    def test_make_edge_id_deterministic(self):
        """Test edge ID generation is deterministic."""
        id1 = _make_edge_id("subj", "pred", "obj")
        id2 = _make_edge_id("subj", "pred", "obj")
        assert id1 == id2
        assert id1.startswith("urn:uuid:")

    def test_make_edge_id_unique(self):
        """Test different edges get different IDs."""
        id1 = _make_edge_id("subj1", "pred", "obj")
        id2 = _make_edge_id("subj2", "pred", "obj")
        assert id1 != id2


class TestEdgeMetadata:
    """Test edge metadata fields."""

    def test_edge_has_knowledge_source(self):
        """Test edges include knowledge source."""
        ingredient = {
            "preferred_term": "Glucose",
            "term": {"id": "CHEBI:17234"},
            "concentration": {"value": "10", "unit": "G_PER_L"},
        }
        edge = ingredient_to_edge("culturemech:LB", ingredient)

        assert edge["primary_knowledge_source"] == "infores:culturemech"

    def test_edge_has_knowledge_level(self):
        """Test edges include knowledge level."""
        ingredient = {
            "preferred_term": "Glucose",
            "term": {"id": "CHEBI:17234"},
            "concentration": {"value": "10", "unit": "G_PER_L"},
        }
        edge = ingredient_to_edge("culturemech:LB", ingredient)

        assert edge["knowledge_level"] == "knowledge_assertion"

    def test_edge_has_agent_type(self):
        """Test edges include agent type."""
        ingredient = {
            "preferred_term": "Glucose",
            "term": {"id": "CHEBI:17234"},
            "concentration": {"value": "10", "unit": "G_PER_L"},
        }
        edge = ingredient_to_edge("culturemech:LB", ingredient)

        assert edge["agent_type"] == "manual_validation_of_automated_agent"
