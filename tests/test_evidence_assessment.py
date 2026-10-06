"""Claim assessments are typed, backward-compatible and never defaulted."""

from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "src/culturemech/schema/culturemech.yaml"
CLASSES = ["EvidenceItem"]
SUPPORT = {"SUPPORT", "REFUTE", "PARTIAL", "NO_EVIDENCE", "WRONG_STATEMENT"}
SOURCES = {
    "FIELD_STUDY",
    "MESOCOSM",
    "LABORATORY",
    "IN_VITRO",
    "IN_VIVO",
    "COMPUTATIONAL",
    "META_ANALYSIS",
    "REVIEW",
    "REMOTE_SENSING",
    "LONG_TERM_MONITORING",
    "EXPERT_OPINION",
    "DATABASE",
    "OTHER",
}
REQUIRED = {"EvidenceItem": {"supports": True, "evidence_source": False}}


@pytest.fixture(scope="module")
def assessment_view():
    return SchemaView(str(SCHEMA))


@pytest.fixture(scope="module")
def assessment_validator():
    return Validator(str(SCHEMA), validation_plugins=[JsonschemaValidationPlugin(closed=True)])


def baseline(view, cls):
    values = {
        "reference": "PMID:12345678",
        "snippet": "A verbatim test fixture passage.",
        "explanation": "Fixture assessment, not a curated scientific assertion.",
        "source": "fixture",
        "supports": "SUPPORT",
        "evidence_source": "IN_VITRO",
    }
    result = {}
    for slot in view.class_induced_slots(cls):
        if slot.required:
            if slot.name in values:
                result[slot.name] = values[slot.name]
            elif slot.range in view.all_enums():
                result[slot.name] = next(iter(view.get_enum(slot.range).permissible_values))
            else:
                raise AssertionError(f"Add an explicit fixture for {cls}.{slot.name}")
    return result


@pytest.mark.parametrize("cls", CLASSES)
def test_assessments_preserve_legacy_requiredness_and_have_no_default(
    assessment_view, assessment_validator, cls
):
    for name in ("supports", "evidence_source"):
        slot = assessment_view.induced_slot(name, cls)
        assert bool(slot.required) == REQUIRED[cls][name]
        assert slot.ifabsent is None
        expected = SUPPORT if name == "supports" else SOURCES
        assert set(assessment_view.get_enum(slot.range).permissible_values) == expected
    old = baseline(assessment_view, cls)
    assert not list(assessment_validator.iter_results(old, target_class=cls))


@pytest.mark.parametrize("cls", CLASSES)
@pytest.mark.parametrize("support", sorted(SUPPORT))
def test_all_support_assessments_validate(assessment_view, assessment_validator, cls, support):
    data = {**baseline(assessment_view, cls), "supports": support, "evidence_source": "DATABASE"}
    assert not list(assessment_validator.iter_results(data, target_class=cls))


@pytest.mark.parametrize("cls", CLASSES)
@pytest.mark.parametrize("source", sorted(SOURCES))
def test_study_types_validate_without_changing_support(
    assessment_view, assessment_validator, cls, source
):
    data = {**baseline(assessment_view, cls), "supports": "REFUTE", "evidence_source": source}
    assert not list(assessment_validator.iter_results(data, target_class=cls))
    assert data["supports"] == "REFUTE"


@pytest.mark.parametrize("cls", CLASSES)
@pytest.mark.parametrize(
    "field,value",
    [
        ("supports", "HIGH_CONFIDENCE"),
        ("supports", "support"),
        ("evidence_source", "abstract"),
        ("evidence_source", "LLM_ASSISTED"),
        ("evidence_source", "PMID:123"),
    ],
)
def test_rejects_conflating_assessment_source_and_curation(
    assessment_view, assessment_validator, cls, field, value
):
    valid = {
        **baseline(assessment_view, cls),
        "supports": "PARTIAL",
        "evidence_source": "LABORATORY",
    }
    assert not list(assessment_validator.iter_results(valid, target_class=cls))  # positive control
    invalid = {**valid, field: value}
    assert list(assessment_validator.iter_results(invalid, target_class=cls))


@pytest.mark.parametrize("cls", CLASSES)
def test_unknown_fields_still_fail_closed_validation(assessment_view, assessment_validator, cls):
    data = {**baseline(assessment_view, cls), "invented_evidence_field": "not allowed"}
    assert list(assessment_validator.iter_results(data, target_class=cls))


def test_shared_reference_location_keeps_its_legacy_meaning(assessment_validator):
    data = {"reference": "PMID:12345678", "supports": "PARTIAL", "evidence_source": "abstract"}
    assert not list(assessment_validator.iter_results(data, target_class="SupportingReference"))


@pytest.mark.parametrize("source", sorted(SOURCES))
def test_generated_dataclass_preserves_assessment(assessment_view, source):
    import json
    import sys

    from linkml_runtime.dumpers import json_dumper

    sys.path.insert(0, str(ROOT / "src"))
    from culturemech.schema.culturemech_dataclasses import EvidenceItem

    payload = {
        **baseline(assessment_view, "EvidenceItem"),
        "supports": "REFUTE",
        "evidence_source": source,
    }
    result = json.loads(json_dumper.dumps(EvidenceItem(**payload)))
    assert result["supports"] == "REFUTE"
    assert result["evidence_source"] == source
