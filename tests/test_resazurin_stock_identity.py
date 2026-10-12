"""Identity withdrawal preserves doses and discloses the remaining MIM conflict."""

import copy
import json
import subprocess

import pytest
import repair_resazurin_stock_identity as repair

pytestmark = pytest.mark.usefixtures("no_reference_cache_reads")


@pytest.fixture
def plan():
    return json.loads((repair.HERE / "plan.json").read_text())


@pytest.fixture(params=[0, 1, 2])
def reviewed(plan, request):
    item = plan["records"][request.param]
    return (
        repair.runner.load_yaml(item["before_text"]),
        repair.runner.load_yaml(item["after_text"]),
        item,
    )


def test_independent_review(reviewed):
    before, after, item = reviewed
    assert repair.audit.check(before, after, item) == {
        "unsupported_primary_identities_removed": 1,
        "ingredient_evidence_explanations_extended": 1,
        "new_curation_history": 1,
    }


@pytest.mark.parametrize(
    "change",
    [
        "dose",
        "term",
        "label",
        "snippet",
        "reference",
        "old_explanation",
        "new_explanation",
        "history",
        "notes",
        "publication",
        "unrelated",
    ],
)
def test_forged_plan_rejected(reviewed, change):
    before, after, item = reviewed
    spec = next(s for s in repair.audit.cohort() if s["record"] == item["path"])
    node = repair.runner.get_node(after, spec["pointer"][:-1])
    if change == "dose":
        node["concentration"]["value"] = "0.5"
    elif change == "term":
        node["term"] = {"id": "CHEBI:8806", "label": "Resazurin"}
    elif change == "label":
        node["preferred_term"] = "Resazurin"
    elif change == "snippet":
        node["evidence"][0]["snippet"] = "fabricated quote"
    elif change == "reference":
        node["evidence"][0]["reference"] += "#new"
    elif change == "old_explanation":
        node["evidence"][0]["explanation"] = node["evidence"][0]["explanation"][10:]
    elif change == "new_explanation":
        node["evidence"][0]["explanation"] = node["evidence"][0]["explanation"].replace(
            "still resolves", "no longer resolves"
        )
    elif change == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif change == "notes":
        node["notes"] = "different preparation"
    elif change == "publication":
        item["publication_identity_resolved"] = True
    else:
        after["name"] += " changed"
    # Rehash the forgery so rejection is about content, not just a stale digest.
    item["after_text"] = repair.runner.render(item["before_text"], after).decode()
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())
    with pytest.raises(AssertionError):
        repair.audit.check(before, after, item)


def tree(tmp_path, plan):
    root = tmp_path.resolve()
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    for item in plan["records"]:
        path = root / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "add", "data/normalized_yaml"], cwd=root, check=True)
    return root


def test_apply_verify_and_repeat_noop(tmp_path, plan):
    root = tree(tmp_path, plan)
    assert repair.apply(plan, root) == {"changed": 3, "already_applied": 0}
    assert repair.apply(plan, root, verify=True) == {"changed": 0, "already_applied": 3}
    assert repair.apply(plan, root) == {"changed": 0, "already_applied": 3}


@pytest.mark.parametrize(
    "change", ["drift", "duplicate", "case", "symlink", "parent_symlink", "verify"]
)
def test_entire_batch_preflight(tmp_path, plan, change):
    root = tree(tmp_path, plan)
    first = root / plan["records"][0]["path"]
    original = first.read_bytes()
    last = root / plan["records"][-1]["path"]
    if change == "drift":
        last.write_bytes(last.read_bytes() + b"\n# concurrent change\n")
    elif change == "duplicate":
        plan["records"][-1] = copy.deepcopy(plan["records"][0])
    elif change == "case":
        plan["records"][-1]["path"] = plan["records"][-1]["path"].replace(
            "synthrophomonas", "SYNTHROPHOMONAS"
        )
    elif change == "symlink":
        external = root / "outside.yaml"
        last.rename(external)
        last.symlink_to(external)
    elif change == "parent_symlink":
        parent = last.parent
        external = root / "outside"
        parent.rename(external)
        parent.symlink_to(external, target_is_directory=True)
    with pytest.raises((AssertionError, ValueError)):
        repair.apply(plan, root, verify=change == "verify")
    assert first.read_bytes() == original


def test_source_capture_tamper_rejected(tmp_path, monkeypatch):
    target = repair.audit.cohort()[0]
    capture = tmp_path / target["context"]
    capture.parent.mkdir(parents=True)
    capture.write_text("{}")
    monkeypatch.setattr(repair.audit, "ROOT", tmp_path)
    with pytest.raises(AssertionError, match="Source context drift"):
        repair.audit.source_for(target)
