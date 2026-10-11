"""URI-only repair scope, drift rejection, rollback and repeat-run behavior."""

import subprocess
from copy import deepcopy
from pathlib import Path

import pytest
import repair_yeast_chebi_references as repair

REPO = Path.cwd()


@pytest.fixture(scope="module")
def frozen():
    return repair.approved(REPO)


@pytest.fixture
def plan(frozen):
    return deepcopy(frozen)


@pytest.fixture
def root(tmp_path, plan, monkeypatch):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    source = tmp_path / repair.SOURCE
    source.parent.mkdir(parents=True)
    source.write_bytes((REPO / repair.SOURCE).read_bytes())
    for item in plan["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    monkeypatch.setattr(repair, "validate_recipe", lambda *args, **kwargs: [])
    return tmp_path


def snapshot(root, plan):
    return {r["path"]: (root / r["path"]).read_bytes() for r in plan["records"]}


def test_default_preview_apply_and_repeat(root, plan):
    baseline = snapshot(root, plan)
    assert repair.apply(plan, root) == {"changed": 0, "pending": 4, "already_applied": 0}
    assert snapshot(root, plan) == baseline
    assert repair.apply(plan, root, dry_run=False)["changed"] == 4
    after = snapshot(root, plan)
    assert all(after[r["path"]] == r["after_text"].encode() for r in plan["records"])
    assert repair.apply(plan, root, dry_run=False)["changed"] == 0
    assert repair.apply(plan, root, verify=True)["already_applied"] == 4
    assert snapshot(root, plan) == after


@pytest.mark.parametrize("index", range(4))
def test_independent_inverse_scope(frozen, index):
    item = frozen["records"][index]
    before, after = (repair.runner.load_yaml(item[key]) for key in ("before_text", "after_text"))
    assert repair.check(before, after, item, REPO) == {
        "new_curation_history": 1,
        "evidence_reference_urls_corrected": 10,
        "bibliography_reference_urls_corrected": 10,
    }
    assert after["curation_history"][:-1] == before["curation_history"]
    assert all(
        a.get("concentration") == b.get("concentration")
        for a, b in zip(after["ingredients"], before["ingredients"], strict=True)
    )


@pytest.mark.parametrize("index", range(4))
@pytest.mark.parametrize(
    "fault", ["quantity", "snippet", "identity", "history", "reference", "path", "count"]
)
def test_rehashed_forgeries_rejected(root, plan, index, fault):
    baseline = snapshot(root, plan)
    item = plan["records"][index]
    after = repair.runner.load_yaml(item["after_text"])
    if fault == "quantity":
        after["ingredients"][0]["concentration"]["value"] = "999"
    elif fault == "snippet":
        after["ingredients"][2]["evidence"][2]["snippet"] = "invented"
    elif fault == "identity":
        after["ingredients"][2]["term"]["id"] = "CHEBI:1"
    elif fault == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif fault == "reference":
        after["ingredients"][2]["evidence"][2]["reference"] += "#invented"
    elif fault == "path":
        item["path"] = item["path"].upper()
    elif fault == "count":
        item["counts"]["new_curation_history"] = True
    item["after_text"] = repair.runner.render(item["before_text"], after).decode()
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())
    with pytest.raises(AssertionError, match="reviewed plan"):
        repair.apply(plan, root, dry_run=False)
    assert {p: (root / p).read_bytes() for p in baseline} == baseline


@pytest.mark.parametrize("index", range(4))
def test_current_record_drift_blocks_entire_batch(root, plan, index):
    path = root / plan["records"][index]["path"]
    path.write_text(path.read_text() + "# concurrent edit\n")
    baseline = snapshot(root, plan)
    with pytest.raises(AssertionError, match="Concurrent edit"):
        repair.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == baseline


def test_source_drift(root, plan):
    path = root / repair.SOURCE
    path.write_text(path.read_text() + "\n")
    baseline = snapshot(root, plan)
    with pytest.raises(AssertionError, match="Source ledger drift"):
        repair.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == baseline


def test_schema_failure_before_write(root, plan, monkeypatch):
    baseline = snapshot(root, plan)
    monkeypatch.setattr(repair, "validate_recipe", lambda *args, **kwargs: ["invalid"])
    with pytest.raises(AssertionError, match="Invalid baseline"):
        repair.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == baseline


def test_rollback_on_second_write_failure(root, plan, monkeypatch):
    baseline = snapshot(root, plan)
    original = repair.os.replace
    calls = 0

    def fail_second(*args):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("injected")
        return original(*args)

    monkeypatch.setattr(repair.os, "replace", fail_second)
    with pytest.raises(OSError, match="injected"):
        repair.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == baseline
    assert not list((root / "data").rglob("*.tmp"))


def test_concurrent_changes_survive_rollback(root, plan, monkeypatch):
    target = root / plan["records"][0]["path"]
    original = repair.os.replace
    calls = 0

    def change_before_failure(*args):
        nonlocal calls
        calls += 1
        if calls == 2:
            target.write_text("concurrent user edit\n")
            raise OSError("injected")
        return original(*args)

    monkeypatch.setattr(repair.os, "replace", change_before_failure)
    with pytest.raises(RuntimeError, match="Partial application"):
        repair.apply(plan, root, dry_run=False)
    assert target.read_text() == "concurrent user edit\n"


def test_symlink_rejected(root, plan, tmp_path):
    path = root / plan["records"][0]["path"]
    moved = tmp_path / "outside.yaml"
    path.rename(moved)
    path.symlink_to(moved)
    with pytest.raises(AssertionError):
        repair.apply(plan, root, dry_run=False)
    assert moved.read_text() == plan["records"][0]["before_text"]
