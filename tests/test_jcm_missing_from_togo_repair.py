from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_missing_from_togo.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_jcm_missing_from_togo", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return load_script()


def source_payload() -> dict:
    return {
        "meta": {
            "gm": "https://togomedium.org/medium/M1",
            "original_media_id": "JCM_M2",
        },
        "components": [
            {
                "paragraph_index": 1,
                "subcomponent_name": "main solution 1",
                "items": [
                    {"component_name": "NaCl", "volume": 2, "unit": "g"},
                    {
                        "component_name": "Trace stock",
                        "volume": 5,
                        "unit": "ml",
                        "reference_media_id": "M9",
                    },
                    {
                        "component_name": "Nitrogen gas",
                        "gmo_id": "GMO_N2",
                        "properties": [{"id": "GMO_000077", "label": "Gas"}],
                    },
                ],
            }
        ],
        "comments": [{"paragraph_index": 2, "comment": "Mix and autoclave."}],
    }


def target_for(repair_module, payload: dict):
    output = repair_module.extract_payload(payload)
    return repair_module.Target(
        jcm_id="J2",
        togo_id="M1",
        relative_path="bacterial/example.yaml",
        raw_sha256=repair_module.canonical_hash(repair_module.raw_projection(payload)),
        output_sha256=repair_module.canonical_hash(repair_module.output_projection(output)),
        ingredient_count=len(output["ingredients"]),
        solution_count=len(output["solutions"]),
        preparation_step_count=len(output["preparation_steps"]),
    )


def empty_record() -> dict:
    return {
        "id": "CultureMech:test",
        "media_term": {"term": {"id": "mediadive.medium:J2"}},
        "notes": "Source: JCM",
        "ingredients": [],
        "preparation_steps": [{"step_number": 1, "action": "MIX", "description": "See source."}],
        "curation_history": [],
        "data_quality_flags": [
            "resolved_reference",
            "incomplete_composition",
            "source_information_unavailable",
        ],
    }


def test_repair_restores_layers_flags_steps_and_provenance(repair_module) -> None:
    payload = source_payload()
    target = target_for(repair_module, payload)

    repaired, changed = repair_module.repair_document(empty_record(), payload, target)

    assert changed
    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        "NaCl",
        "Nitrogen gas",
    ]
    assert repaired["solutions"] == [
        {
            "preferred_term": "Trace stock",
            "composition": [],
            "concentration": {"value": "5", "unit": "ML_PER_L"},
            "notes": "Defined in TOGO medium M9.",
        }
    ]
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Mix and autoclave.",
        }
    ]
    assert repaired["data_quality_flags"] == ["resolved_reference"]
    assert repair_module.provenance_note(target) in repaired["notes"]
    assert repaired["curation_history"][-1]["action"] == repair_module.ACTION


def test_applied_repair_is_idempotent_after_ontology_enrichment(repair_module) -> None:
    payload = source_payload()
    target = target_for(repair_module, payload)
    repaired, _ = repair_module.repair_document(empty_record(), payload, target)
    repaired["ingredients"][0]["term"] = {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }

    second, changed = repair_module.repair_document(repaired, payload, target)

    assert not changed
    assert second == repaired


def test_source_fingerprint_rejects_payload_drift(repair_module) -> None:
    payload = source_payload()
    target = target_for(repair_module, payload)
    drifted = copy.deepcopy(payload)
    drifted["components"][0]["items"][0]["volume"] = 3

    with pytest.raises(ValueError, match="source projection drifted"):
        repair_module.repair_document(empty_record(), drifted, target)


def test_nonempty_precondition_is_rejected(repair_module) -> None:
    payload = source_payload()
    target = target_for(repair_module, payload)
    doc = empty_record()
    doc["ingredients"] = [{"preferred_term": "existing"}]

    with pytest.raises(ValueError, match="no longer empty"):
        repair_module.repair_document(doc, payload, target)


def test_reviewed_target_inventory_is_exact(repair_module) -> None:
    expected = {
        ("J94", "M86"),
        ("J179", "M172"),
        ("J210", "M203"),
        ("J260", "M252"),
        ("J313", "M308"),
        ("J361", "M355"),
        ("J376", "M370"),
        ("J382", "M377"),
        ("J390", "M385"),
        ("J400", "M396"),
        ("J426", "M426"),
        ("J477", "M478"),
        ("J490", "M491"),
        ("J522", "M523"),
        ("J630", "M643"),
        ("J635", "M649"),
        ("J703", "M725"),
        ("J738", "M763"),
        ("J773", "M802"),
        ("J792", "M824"),
        ("J806", "M841"),
        ("J816", "M851"),
        ("J856", "M892"),
        ("J939", "M985"),
        ("J1145", "M1227"),
        ("J1195", "M1280"),
        ("J1224", "M1316"),
        ("J1225", "M1317"),
    }
    actual = {(target.jcm_id, target.togo_id) for target in repair_module.TARGETS}

    assert actual == expected
    assert ("J249", "M241") not in actual
    assert ("J867", "M904") not in actual
    repair_module._validate_inventory()


def test_target_records_are_in_guarded_pre_or_post_state(repair_module) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.relative_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert repair_module.media_term_id(doc) == f"mediadive.medium:{target.jcm_id}"
        if repair_module.history_has_action(doc):
            repair_module._assert_applied(doc, target)
        else:
            assert not (doc.get("ingredients") or [])
            assert not (doc.get("solutions") or [])
            assert "incomplete_composition" in (doc.get("data_quality_flags") or [])
