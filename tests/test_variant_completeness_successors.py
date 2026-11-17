"""Exact completeness changes cannot exempt earlier recipe science (#683, 2026-11-16)."""

from __future__ import annotations

import copy
import json

import audit_variant_completeness_successor as audit
import pytest
import yaml

from tests import test_curate_variant_completeness as updater_tests
from tests.test_curate_variant_completeness import decisions_file, run

sample = updater_tests.sample


@pytest.fixture
def applied(sample):
    root, path, decision = sample
    before = yaml.safe_load(path.read_bytes())
    decisions = decisions_file(root, [decision])
    run(root, decisions, root / "applied.json", apply=True)
    return before, yaml.safe_load(path.read_bytes()), decision, audit.sha(decisions.read_bytes())


def test_native_application_reconstructs_exactly_and_keeps_prior_history(applied):
    before, after, decision, pin = applied
    assert audit.check_semantics(before, after, decision, pin) == {
        "new_variant_completeness_events": 1,
        "new_curation_history": 1,
    }
    assert after["curation_history"][:-1] == before["curation_history"]


@pytest.mark.parametrize(
    "mutation",
    [
        "base_field",
        "amount",
        "held_claim",
        "source_text",
        "old_history",
        "extra_history",
        "event_digest",
        "event_decision",
        "qualification",
        "curator",
        "identity",
    ],
)
def test_semantic_proof_rejects_unauthorized_science_and_history_changes(applied, mutation):
    before, original, decision, pin = applied
    after = copy.deepcopy(original)
    variant = after["variants"][0]
    event = after["curation_history"][-1]
    if mutation == "base_field":
        after["ingredients"][0]["preferred_term"] = "unreviewed base ingredient"
    elif mutation == "amount":
        variant["ingredient_changes"][0]["amount"]["value"] = "900"
    elif mutation == "held_claim":
        variant["ingredient_mentions"][0]["reason"] = "Invented source approval"
    elif mutation == "source_text":
        variant["modifications"][0] += " unsupported"
    elif mutation == "old_history":
        after["curation_history"][0]["notes"] = "Rewritten old evidence"
    elif mutation == "extra_history":
        after["curation_history"].append(copy.deepcopy(event))
    elif mutation in {"event_digest", "event_decision"}:
        payload = json.loads(event["changes"])
        if mutation == "event_digest":
            payload["decision_sha256"] = "0" * 64
        else:
            payload["decision"]["variants"][0]["append_changes"][0]["stage"] = "different assay"
        event["changes"] = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    elif mutation == "qualification":
        event["notes"] = "Human reviewed"
    elif mutation == "curator":
        event["curator"] = "unreviewed identity"
    else:
        after["id"] = "CultureMech:999999"
    with pytest.raises((AssertionError, ValueError)):
        audit.check_semantics(before, after, decision, pin)
