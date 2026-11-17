"""Invert exact reviewed completeness successors without weakening prior audits.

Purpose: #683 follow-up, 2026-11-16. Inputs: digest-pinned retained proposal and
before/after evidence; output: structural proof or exact restored prior bytes.
Runtime verification never reads historical Git objects or mutable proposals.
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
from collections import Counter
from functools import lru_cache
from pathlib import Path

import yaml
from curate_variant_completeness import apply_decision

ROOT = Path(__file__).resolve().parents[1]
BASE = "b2652f7c7197aef33162ac9a721d21a16d528249"
ACTION = "REGISTERED_VARIANT_COMPLETENESS_SUCCESSOR"
APPLICATION_ACTION = "VARIANT_INGREDIENT_COMPLETENESS"
NOTES = (
    "LLM-assisted reviewed variant ingredient amounts, unresolved names and exact source "
    "corrections; no human review status asserted."
)
PLAN = (
    ROOT
    / "reports/ingredient_concentration_curation/20261116-variant-ingredient-completeness/plan.json"
)
CAPSULE = PLAN.parent / "evidence-capsule"
# Set only after the final reviewed application and original-Git authentication.
PLAN_SHA256 = "1ac0749ed3c1ae52211d669ff9ea8c6dc0c9db771203f1acf169a98bc1e5f44d"
CAPSULE_SHA256 = "8b388038f7e433915ce8f1655100acb7407b3be98d76c0763a7fd79a9ae8fcc9"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def check_semantics(before, after, decision, decision_sha256):
    """Reconstruct exact authorized edits and require one fully bound history event."""
    assert before["id"] == after["id"] == decision["recipe_id"], "Completeness identity changed"
    desired, _ = apply_decision(before, decision)
    prior = before.get("curation_history", [])
    history = after.get("curation_history")
    assert isinstance(prior, list) and isinstance(history, list), "Invalid completeness history"
    assert len(history) == len(prior) + 1 and history[:-1] == prior, "Prior history changed"
    event = history[-1]
    assert isinstance(event, dict) and set(event) == {
        "timestamp",
        "curator",
        "action",
        "notes",
        "source",
        "changes",
    }, "Unexpected completeness event fields"
    assert isinstance(event["timestamp"], str) and re.match(r"^20[0-9]{2}-", event["timestamp"])
    assert event["curator"] == "codex" and event["action"] == APPLICATION_ACTION
    assert event["source"] == "https://github.com/CultureBotAI/CultureMech/issues/683"
    assert event["notes"] == NOTES, "Completeness event qualification changed"
    assert event["changes"] == json.dumps(
        {"decision_sha256": decision_sha256, "decision": decision},
        ensure_ascii=False,
        sort_keys=True,
    ), "Completeness event is not bound to the exact reviewed decision"
    desired["curation_history"] = copy.deepcopy(history)
    assert desired == after, "Completeness successor differs from exact reviewed operations"
    return Counter({"new_variant_completeness_events": 1, "new_curation_history": 1})


@lru_cache(maxsize=1)
def retained_evidence():
    assert not CAPSULE.is_symlink(), "Completeness capsule cannot be a symlink"
    manifest_raw = (CAPSULE / "manifest.json").read_bytes()
    assert sha(manifest_raw) == CAPSULE_SHA256, "Reviewed completeness capsule changed"
    manifest = json.loads(manifest_raw)
    assert manifest["contract"] == "culturemech-variant-completeness-successors-v1"
    assert manifest["base_commit"] == BASE
    plan_raw = PLAN.read_bytes()
    assert sha(plan_raw) == PLAN_SHA256, "Reviewed completeness plan changed"
    assert manifest["plan"] == {
        "path": PLAN.relative_to(ROOT).as_posix(),
        "sha256": PLAN_SHA256,
        "bytes": len(plan_raw),
    }
    proposal_raw = (CAPSULE / "decisions.json").read_bytes()
    assert manifest["decisions"] == {
        "path": "decisions.json",
        "sha256": sha(proposal_raw),
        "bytes": len(proposal_raw),
    }, "Reviewed completeness decisions changed"
    files = set()
    for path in CAPSULE.rglob("*"):
        assert not path.is_symlink(), "Completeness capsule contains a symlink"
        if path.is_file():
            files.add(path.relative_to(CAPSULE).as_posix())
    assert files == {"manifest.json", "decisions.json"}, "Completeness capsule membership changed"
    plan, document = json.loads(plan_raw), json.loads(proposal_raw)
    assert document["schema_version"] == 1 and document["records"]
    records = {item["path"]: item for item in plan["records"]}
    decisions = {item["path"]: item for item in document["records"]}
    assert len(records) == len(plan["records"]) == len(decisions) == len(document["records"])
    assert len(records) == manifest["records"] and sorted(records) == manifest["record_paths"]
    assert set(records) == set(decisions), "Completeness proposal/edge membership differs"
    assert plan["base_commit"] == BASE
    assert plan["decision_sha256"] == sha(proposal_raw)
    assert plan["source_receipt_sha256"] == manifest["source_receipt_sha256"]
    for path in records:
        relative = Path(path)
        assert not relative.is_absolute() and ".." not in relative.parts
        assert path.startswith("data/normalized_yaml/") and path.endswith(".yaml")
    return records, decisions, manifest


def expected_item(path):
    records, decisions, manifest = retained_evidence()
    frozen, decision = records[path], decisions[path]
    item = {
        "path": path,
        "id": decision["recipe_id"],
        "action": ACTION,
        "decision_sha256": manifest["decisions"]["sha256"],
        "source_receipt_sha256": manifest["source_receipt_sha256"],
    }
    for label in ("before", "after"):
        raw = frozen[label + "_text"].encode("utf-8")
        assert sha(raw) == frozen[label + "_sha256"], "Completeness snapshot hash mismatch"
        item[label + "_text"], item[label + "_sha256"] = raw.decode("utf-8"), sha(raw)
    assert item["before_sha256"] == decision["expected_sha256"], "Completeness beforeimage changed"
    assert item["before_sha256"] != item["after_sha256"], "No-op completeness successor"
    return item


def check(before, after, item):
    assert item == expected_item(item["path"]), "Completeness edge differs from retained evidence"
    assert before == yaml.load(item["before_text"], Loader=yaml.CSafeLoader), "Baseline changed"
    assert after == yaml.load(item["after_text"], Loader=yaml.CSafeLoader), "Successor changed"
    return check_semantics(
        before, after, retained_evidence()[1][item["path"]], item["decision_sha256"]
    )


def restore_before(raw, path):
    """Authenticate this exact new layer before older registered inversions run."""
    if path not in retained_evidence()[0]:
        return raw
    item = expected_item(path)
    assert sha(raw) == item["after_sha256"], "Current completeness successor hash mismatch"
    before = yaml.load(item["before_text"], Loader=yaml.CSafeLoader)
    after = yaml.load(raw, Loader=yaml.CSafeLoader)
    check(before, after, item)
    return item["before_text"].encode("utf-8")
