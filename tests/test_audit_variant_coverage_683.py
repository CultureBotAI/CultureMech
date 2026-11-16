"""Falsify permissive accounting/preservation audits using synthetic #683 data."""

import copy
import csv
import importlib.util
import io
import json
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "audit_variant_coverage_683",
    Path(__file__).resolve().parents[1] / "scripts/adhoc/audit_variant_coverage_683.py",
)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


@pytest.fixture
def records():
    base = {
        "ingredients": [{"preferred_term": "base component"}],
        "variants": [
            {"name": "study A", "modifications": ["Add component A."]},
            {"name": "study B", "modifications": ["Add component B."]},
        ],
        "curation_history": [{"action": "OLD", "notes": "Retain original event."}],
    }
    variants = [
        {
            "variant_index": index,
            "variant_name": variant["name"],
            "ingredient_changes": [
                {
                    "action": "ADD",
                    "ingredient": {"preferred_term": "component " + str(index)},
                    "source_modification_index": 0,
                    "source_text": variant["modifications"][0],
                }
            ],
        }
        for index, variant in enumerate(base["variants"])
    ]
    proposal = {"variants": variants}
    current = copy.deepcopy(base)
    for item in variants:
        current["variants"][item["variant_index"]]["ingredient_changes"] = copy.deepcopy(
            item["ingredient_changes"]
        )
    current["curation_history"].append(
        {
            "timestamp": "2026-01-01T00:00:00Z",
            "curator": "codex",
            "action": "STRUCTURED_VARIANT_INGREDIENTS",
            "notes": audit.NOTES,
            "source": audit.SOURCE,
            "changes": json.dumps({"decision_sha256": "a" * 64, "variants": variants}),
        }
    )
    return base, current, proposal


def test_preapply_accepts_base_but_postapply_requires_additions(records):
    base, current, proposal = records
    assert audit.check_preservation(base, base, proposal, "a" * 64, "preapply") == "NOT_APPLIED"
    with pytest.raises(ValueError, match="not applied"):
        audit.check_preservation(base, base, proposal, "a" * 64, "postapply")
    before = copy.deepcopy(current)
    assert audit.check_preservation(base, current, proposal, "a" * 64, "postapply") == "APPLIED"
    assert current == before


@pytest.mark.parametrize("change", ["base", "prose", "history", "extra", "dose", "partial"])
def test_unrelated_drift_or_wrong_assertions_never_disappear_during_stripping(records, change):
    base, current, proposal = records
    if change == "base":
        current["ingredients"][0]["preferred_term"] = "different base component"
    elif change == "prose":
        current["variants"][0]["modifications"][0] = "Different original prose."
    elif change == "history":
        current["curation_history"][0]["notes"] = "Rewritten old event."
    elif change == "extra":
        current["variants"][0]["unproposed_field"] = "unrelated addition"
    elif change == "dose":
        current["variants"][0]["ingredient_changes"][0]["ingredient"]["concentration"] = {
            "value": "999",
            "unit": "G_PER_L",
        }
    else:
        del current["variants"][1]["ingredient_changes"]
    with pytest.raises(ValueError):
        audit.check_preservation(base, current, proposal, "a" * 64, "postapply")


def test_history_must_bind_exact_original_proposal(records):
    base, current, proposal = records
    with pytest.raises(ValueError, match="exact proposal"):
        audit.check_preservation(base, current, proposal, "b" * 64, "postapply")
    current["curation_history"].append(copy.deepcopy(current["curation_history"][-1]))
    with pytest.raises(ValueError, match="event count"):
        audit.check_preservation(base, current, proposal, "a" * 64, "postapply")


def queue_bytes(duplicate=False, count=396):
    stream = io.StringIO()
    writer = csv.writer(stream, delimiter="\t")
    writer.writerow(
        ["row_kind", "source_path", "variant_index", "modification_index", "modification_text"]
    )
    for index in range(count):
        writer.writerow(
            [
                "modification",
                "algae/example.yaml",
                0,
                0 if duplicate else index,
                'quoted "text"\n' + "x" * (140000 if index == 0 else 1),
            ]
        )
    return stream.getvalue().encode()


def test_queue_csv_handles_large_multiline_fields_and_restores_global_limit(monkeypatch):
    raw = queue_bytes()
    monkeypatch.setattr(audit, "QUEUE_SHA", audit.digest(raw))
    previous = csv.field_size_limit()
    rows, coordinates = audit.read_queue(raw)
    assert len(rows) == len(coordinates) == 396
    assert rows[0]["modification_text"].startswith('quoted "text"\n')
    assert len(rows[0]["modification_text"]) > 140000
    assert csv.field_size_limit() == previous


@pytest.mark.parametrize(
    "duplicate,count,expected", [(True, 396, "duplicate"), (False, 395, "396")]
)
def test_queue_does_not_accept_duplicate_or_missing_rows(monkeypatch, duplicate, count, expected):
    raw = queue_bytes(duplicate=duplicate, count=count)
    monkeypatch.setattr(audit, "QUEUE_SHA", audit.digest(raw))
    with pytest.raises(ValueError, match=expected):
        audit.read_queue(raw)
