"""Exact reviewed additions must not exempt historical recipe science (#772)."""

from __future__ import annotations

import copy
import json

import pytest
import yaml
from audit_variant_ingredient_successor import (
    BASE,
    PLAN,
    RESULT,
    check,
    expected_item,
    proposal_records,
    restore_before,
    sha,
)

from tests.test_medium_concentration_batch import AUDIT, FOLLOWUPS


@pytest.fixture(scope="module")
def plan():
    return json.loads(PLAN.read_text(encoding="utf-8"))


def test_exact_successor_membership_and_independent_inversion(plan):
    assert plan["base_commit"] == BASE and plan["applied_commit"] == RESULT
    assert len(plan["records"]) == 87
    assert {item["path"] for item in plan["records"]} == set(proposal_records())
    assert FOLLOWUPS.count(PLAN) == 1
    for item in plan["records"]:
        assert item == expected_item(item["path"])
        before = yaml.load(item["before_text"], Loader=yaml.CSafeLoader)
        after = yaml.load(item["after_text"], Loader=yaml.CSafeLoader)
        assert check(before, after, item)["new_curation_history"] == 1
        raw = item["after_text"].encode()
        assert restore_before(raw, item["path"]) == item["before_text"].encode()
        assert AUDIT.invert_chain(raw, [item]) == before


@pytest.mark.parametrize(
    "mutation",
    [
        "base_field",
        "base_snapshot",
        "variant_claim",
        "source_binding",
        "old_history",
        "event_digest",
        "event_payload",
        "extra_history",
        "proposal_digest",
        "proposal_path",
    ],
)
def test_rehashing_cannot_authorize_unreviewed_successor_changes(plan, mutation):
    item = copy.deepcopy(plan["records"][0])
    before = yaml.load(item["before_text"], Loader=yaml.CSafeLoader)
    after = yaml.load(item["after_text"], Loader=yaml.CSafeLoader)
    variant = next(v for v in after["variants"] if "ingredient_changes" in v)
    if mutation == "base_field":
        after["ingredients"][0]["preferred_term"] = "unreviewed base ingredient"
    elif mutation == "base_snapshot":
        before["name"] = "rewritten historical name"
        item["before_text"] = yaml.safe_dump(before)
        item["before_sha256"] = sha(item["before_text"].encode())
    elif mutation == "variant_claim":
        variant["ingredient_changes"][0]["ingredient"]["preferred_term"] = "unreviewed claim"
    elif mutation == "source_binding":
        variant["ingredient_changes"][0]["source_text"] += " unsupported"
    elif mutation == "old_history":
        after["curation_history"][0]["notes"] = "rewritten earlier evidence"
    elif mutation == "event_digest":
        event = json.loads(after["curation_history"][-1]["changes"])
        event["decision_sha256"] = "0" * 64
        after["curation_history"][-1]["changes"] = json.dumps(event)
    elif mutation == "event_payload":
        after["curation_history"][-1]["changes"] = "{}"
    elif mutation == "extra_history":
        after["curation_history"].append(copy.deepcopy(after["curation_history"][-1]))
    elif mutation == "proposal_digest":
        item["proposal_sha256"] = "0" * 64
    else:
        item["proposal_path"] = "conf/unreviewed.json"
    item["after_text"] = yaml.safe_dump(after)
    item["after_sha256"] = sha(item["after_text"].encode())
    with pytest.raises((AssertionError, ValueError)):
        check(before, after, item)
    with pytest.raises((AssertionError, ValueError)):
        AUDIT.invert_chain(item["after_text"].encode(), [item])


def test_current_byte_drift_is_refused_and_unrelated_records_are_not_exempted(plan):
    item = plan["records"][0]
    with pytest.raises(AssertionError, match="hash mismatch"):
        restore_before((item["after_text"] + "\n").encode(), item["path"])
    unrelated = b"id: CultureMech:999999\n"
    assert restore_before(unrelated, "data/normalized_yaml/unregistered.yaml") == unrelated
