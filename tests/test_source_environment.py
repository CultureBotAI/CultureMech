"""Validation tests for CultureMech source_environment field.

Tests schema validation of the SourceEnvironmentDescriptor and EnvironmentTerm
classes added for environmental linking (issue #2).
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

SCHEMA_PATH = Path(__file__).parent.parent / "src" / "culturemech" / "schema" / "culturemech.yaml"
TEST_DATA_DIR = Path(__file__).parent / "data" / "test_source_environment"

ENVO_PATTERN = re.compile(r"^ENVO:\d{7,8}$")


class TestSourceEnvironmentYAML:
    """Test that source_environment YAML examples are well-formed."""

    def test_valid_single_environment_loads(self):
        data = yaml.safe_load((TEST_DATA_DIR / "valid_single_environment.yaml").read_text())
        assert data["name"] == "Acidic Peatland Medium"
        assert len(data["source_environment"]) == 1
        env = data["source_environment"][0]
        assert env["preferred_term"] == "peatland"
        assert ENVO_PATTERN.match(env["term"]["id"])

    def test_valid_multiple_environments_loads(self):
        data = yaml.safe_load((TEST_DATA_DIR / "valid_multiple_environments.yaml").read_text())
        assert len(data["source_environment"]) == 2
        for env in data["source_environment"]:
            assert "preferred_term" in env
            assert ENVO_PATTERN.match(env["term"]["id"])

    def test_valid_no_environment_loads(self):
        data = yaml.safe_load((TEST_DATA_DIR / "valid_no_environment.yaml").read_text())
        assert data["name"] == "LB Broth"
        assert "source_environment" not in data

    def test_valid_no_envo_term_loads(self):
        data = yaml.safe_load((TEST_DATA_DIR / "valid_no_envo_term.yaml").read_text())
        env = data["source_environment"][0]
        assert env["preferred_term"] == "unspecified marine environment"
        assert "term" not in env
        assert "notes" in env

    def test_invalid_envo_id_detected(self):
        data = yaml.safe_load((TEST_DATA_DIR / "invalid_envo_id.yaml").read_text())
        env = data["source_environment"][0]
        assert not ENVO_PATTERN.match(env["term"]["id"]), \
            "ENVO:123 should not match the valid ENVO pattern"


class TestSchemaLoads:
    """Test that the schema itself is valid."""

    def test_schema_is_valid_yaml(self):
        data = yaml.safe_load(SCHEMA_PATH.read_text())
        assert "classes" in data
        assert "MediaRecipe" in data["classes"]

    def test_schema_has_source_environment_field(self):
        data = yaml.safe_load(SCHEMA_PATH.read_text())
        media_recipe = data["classes"]["MediaRecipe"]
        assert "source_environment" in media_recipe["attributes"]
        field = media_recipe["attributes"]["source_environment"]
        assert field["range"] == "SourceEnvironmentDescriptor"
        assert field["multivalued"] is True
        assert field["required"] is False

    def test_schema_has_source_environment_descriptor(self):
        data = yaml.safe_load(SCHEMA_PATH.read_text())
        cls = data["classes"]["SourceEnvironmentDescriptor"]
        assert cls["is_a"] == "Descriptor"
        attrs = cls["attributes"]
        assert "preferred_term" in attrs
        assert attrs["preferred_term"]["required"] is True
        assert "term" in attrs
        assert attrs["term"]["range"] == "EnvironmentTerm"
        assert "notes" in attrs

    def test_schema_has_environment_term(self):
        data = yaml.safe_load(SCHEMA_PATH.read_text())
        cls = data["classes"]["EnvironmentTerm"]
        assert cls["is_a"] == "Term"
        assert "ENVO" in cls["id_prefixes"]
        assert "ENVO:\\d{7,8}" in cls["slot_usage"]["id"]["pattern"]

    def test_gen_linkml_validates(self):
        """Verify schema passes gen-linkml validation."""
        result = subprocess.run(
            ["gen-linkml", str(SCHEMA_PATH), "-o", "/dev/null"],
            capture_output=True, text=True
        )
        assert result.returncode == 0, f"gen-linkml failed: {result.stderr}"


class TestDataclassGeneration:
    """Test that generated dataclasses work correctly."""

    def test_dataclasses_import(self):
        import sys
        src_path = str(SCHEMA_PATH.parent.parent.parent)
        if src_path not in sys.path:
            sys.path.insert(0, src_path)
        from culturemech.schema.culturemech_dataclasses import (
            SourceEnvironmentDescriptor,
            EnvironmentTerm,
            MediaRecipe,
        )
        assert SourceEnvironmentDescriptor is not None
        assert EnvironmentTerm is not None

    def test_source_environment_descriptor_instantiation(self):
        import sys
        src_path = str(SCHEMA_PATH.parent.parent.parent)
        if src_path not in sys.path:
            sys.path.insert(0, src_path)
        from culturemech.schema.culturemech_dataclasses import (
            SourceEnvironmentDescriptor,
        )
        desc = SourceEnvironmentDescriptor(preferred_term="peatland")
        assert desc.preferred_term == "peatland"

    def test_environment_term_instantiation(self):
        import sys
        src_path = str(SCHEMA_PATH.parent.parent.parent)
        if src_path not in sys.path:
            sys.path.insert(0, src_path)
        from culturemech.schema.culturemech_dataclasses import EnvironmentTerm
        term = EnvironmentTerm(id="ENVO:00000044", label="peatland")
        assert str(term.id) == "ENVO:00000044"
        assert term.label == "peatland"
