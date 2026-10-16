"""Citation successors must not become hash exemptions for recipe drift."""

import copy
import hashlib
import json
from collections import Counter

import pytest
import yaml

from tests.test_medium_concentration_batch import AUDIT, FOLLOWUPS, ROOT


@pytest.fixture(autouse=True)
def isolated_counts(monkeypatch):
    monkeypatch.setattr(AUDIT, "counts", Counter())


def test_registered_citation_successors_preserve_historical_recipe():
    assert FOLLOWUPS.count(AUDIT.PAPER_CITATION_PLAN) == 1
    plan = json.loads(AUDIT.PAPER_CITATION_PLAN.read_text())
    assert len(plan["records"]) == 10
    assert len({row["path"] for row in plan["records"]}) == 10
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        assert AUDIT.invert_chain(raw, [item]) == yaml.safe_load(item["before_text"])


@pytest.mark.parametrize("mutation", ["amount", "identity", "history", "reference", "snippet"])
def test_rehashing_successor_cannot_hide_unreviewed_changes(mutation):
    item = copy.deepcopy(json.loads(AUDIT.PAPER_CITATION_PLAN.read_text())["records"][0])
    doc = yaml.safe_load(item["after_text"])
    if mutation == "amount":
        doc["ingredients"][0]["concentration"]["value"] = "9999"
    elif mutation == "identity":
        doc["ingredients"][0]["preferred_term"] = "Wrong chemical"
    elif mutation == "history":
        doc["curation_history"][0]["notes"] = "Overwritten history"
    elif mutation == "reference":
        doc["references"][0]["reference"] = "doi:10.0000/wrong"
    else:
        doc["evidence"][-1]["snippet"] = ""
    raw = yaml.safe_dump(doc).encode()
    item["after_text"] = raw.decode()
    item["after_sha256"] = hashlib.sha256(raw).hexdigest()
    with pytest.raises(AssertionError):
        AUDIT.invert_chain(raw, [item])


def test_consolidated_alias_must_remain_attributable():
    item = json.loads(AUDIT.PAPER_CITATION_PLAN.read_text())["records"][-1]
    doc = yaml.safe_load(item["after_text"])
    doc["references"][0]["notes"] = "Lost alternate DOI provenance"
    raw = yaml.safe_dump(doc).encode()
    item["after_text"] = raw.decode()
    item["after_sha256"] = hashlib.sha256(raw).hexdigest()
    with pytest.raises(AssertionError):
        AUDIT.invert_chain(raw, [item])
