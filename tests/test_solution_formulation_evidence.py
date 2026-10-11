"""Solution-level evidence survives validation and serialization without flattening."""

from __future__ import annotations

import copy
import hashlib
import inspect
import json
from pathlib import Path

import jsonschema
import pytest
import requests
import yaml
from linkml_reference_validator.models import ReferenceValidationConfig
from linkml_runtime.dumpers import yaml_dumper
from review_medium_concentration_evidence import json_excerpt
from validate_recipe_references import validate_data

from culturemech.schema.culturemech_dataclasses import EvidenceItem, SolutionRecipe
from culturemech.validation.recipe_references import (
    RecipeSourceCache,
    RecipeTextValidator,
    recipe_source,
)
from culturemech.validation.write_validated import (
    DEFAULT_SCHEMA_PATH,
    ValidationFailedError,
    infer_target_class,
    validate_recipe,
    write_validated_recipe,
)

FIXTURE = Path(__file__).parent / "fixtures" / "recipe_references" / "solution599.json"


def test_existing_constructor_positions_are_preserved():
    legacy_fields = [
        "id",
        "preferred_term",
        "composition",
        "id_lineage_token",
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
        "category",
        "solutions",
        "ingredients",
        "concentration",
        "preparation_notes",
        "storage_conditions",
        "shelf_life",
        "references",
        "source_data",
        "curation_history",
        "data_quality_flags",
        "sources",
        "notes",
    ]
    parameters = list(inspect.signature(SolutionRecipe).parameters)
    assert parameters[: len(legacy_fields)] == legacy_fields
    assert parameters[len(legacy_fields)] == "evidence"


@pytest.fixture
def capture():
    data = json.loads(FIXTURE.read_text())
    assert hashlib.sha256(data["raw"].encode()).hexdigest() == data["sha256"]
    return data


@pytest.fixture
def record(capture):
    def evidence(index, explanation):
        return {
            "reference": capture["url"],
            "supports": "SUPPORT",
            "snippet": json_excerpt(capture["raw"], ["data", "recipe", index]),
            "explanation": explanation,
        }

    return {
        "id": "CultureMech:999999",
        "preferred_term": "Main sol. 323",
        "term": {"id": "mediadive.solution:599", "label": "Main sol. 323"},
        "composition": [
            {
                "preferred_term": "CaCl2 x 2 H2O",
                "concentration": {"value": "0.11976", "unit": "G_PER_L"},
                "evidence": [evidence(0, "composition[0].concentration: provider g_l.")],
            }
        ],
        "solutions": [
            {
                "preferred_term": "Fatty acid mixture",
                "term": {"id": "mediadive.solution:6552", "label": "Fatty acid mixture"},
                "concentration": {"value": "0.0014", "unit": "L"},
            }
        ],
        "evidence": [
            evidence(
                8,
                "solutions[0].concentration: 1.4 ml / 1000 ml per L = 0.0014 L "
                "input to this stock preparation, not a universal working dose.",
            )
        ],
        "references": [{"reference": capture["url"], "title": "Main sol. 323"}],
    }


@pytest.fixture(scope="module")
def generated_validator():
    schema = json.loads(DEFAULT_SCHEMA_PATH.with_name("culturemech.schema.json").read_text())
    root = {
        "$schema": schema["$schema"],
        "$defs": schema["$defs"],
        "$ref": "#/$defs/SolutionRecipe",
    }
    cls = jsonschema.validators.validator_for(root)
    cls.check_schema(root)
    return cls(root)


@pytest.mark.parametrize("with_evidence", [False, True])
def test_optional_formulation_evidence_is_backwards_compatible(
    record, generated_validator, with_evidence
):
    if not with_evidence:
        record.pop("evidence")
    assert infer_target_class(record) == "SolutionRecipe"
    assert not validate_recipe(record)
    assert not list(generated_validator.iter_errors(record))
    assert "source_data" not in record


def test_dataclass_roundtrip_keeps_dose_and_ingredient_evidence_separate(record):
    obj = SolutionRecipe(**copy.deepcopy(record))
    assert isinstance(obj.evidence[0], EvidenceItem)
    restored = yaml.safe_load(yaml_dumper.dumps(obj))
    assert restored["evidence"] == record["evidence"]
    assert restored["composition"] == record["composition"]
    assert restored["solutions"] == record["solutions"]
    assert "source_data" not in restored
    assert not validate_recipe(restored)


@pytest.mark.parametrize(
    "defect",
    [
        "root_typo",
        "evidence_typo",
        "inline_evidence",
        "concentration_evidence",
        "missing_reference",
        "missing_explanation",
        "missing_supports",
        "bad_supports",
    ],
)
def test_malformed_and_misplaced_evidence_is_rejected(record, generated_validator, defect):
    if defect == "root_typo":
        record["unreviewed"] = True
    elif defect == "evidence_typo":
        record["evidence"][0]["unreviewed"] = True
    elif defect == "inline_evidence":
        record["solutions"][0]["evidence"] = copy.deepcopy(record["evidence"])
    elif defect == "concentration_evidence":
        record["solutions"][0]["concentration"]["evidence"] = copy.deepcopy(record["evidence"])
    elif defect == "bad_supports":
        record["evidence"][0]["supports"] = "INVENTED"
    else:
        record["evidence"][0].pop(defect.removeprefix("missing_"))
    assert validate_recipe(record)
    assert list(generated_validator.iter_errors(record))


def test_invalid_evidence_never_replaces_existing_output(record, tmp_path):
    target = tmp_path / "solution.yaml"
    write_validated_recipe(record, target)
    before = target.read_bytes()
    record["evidence"][0]["unreviewed"] = True
    with pytest.raises(ValidationFailedError):
        write_validated_recipe(record, target)
    assert target.read_bytes() == before


@pytest.mark.parametrize("corrupt_root_quote", [False, True])
def test_reference_walker_checks_root_and_composition_evidence(
    record, capture, tmp_path, monkeypatch, corrupt_root_quote
):
    def no_network(*args, **kwargs):
        pytest.fail("Offline source checks must not fetch network content")

    monkeypatch.setattr(requests.Session, "get", no_network)
    config = ReferenceValidationConfig(cache_dir=tmp_path, rate_limit_delay=0)
    cache = RecipeSourceCache(config)
    cache.directory.mkdir(parents=True, exist_ok=True)
    cache.path(recipe_source(capture["url"])).write_text(json.dumps(capture))
    if corrupt_root_quote:
        old = record["evidence"][0]["snippet"]
        record["evidence"][0]["snippet"] = old.replace('"amount": 1.4', '"amount": 14')
        assert record["evidence"][0]["snippet"] != old
    validator = RecipeTextValidator(config, cache=cache)
    issues = validate_data(record, DEFAULT_SCHEMA_PATH, validator)
    assert len(validator.results) == 3
    assert {r.path for r in validator.results} == {
        "evidence[0].snippet",
        "composition[0].evidence[0].snippet",
        "references[0].title",
    }
    failures = [r for r in validator.results if not r.is_valid]
    if corrupt_root_quote:
        assert len(issues) == len(failures) == 1
        assert failures[0].path == "evidence[0].snippet"
        assert "snippet_mismatch" in issues[0].message
    else:
        assert not issues and not failures
