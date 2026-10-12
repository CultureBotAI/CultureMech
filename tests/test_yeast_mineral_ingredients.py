"""Exercise the pinned four-record application in isolated temporary repositories."""

import copy
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
import review_yeast_mineral_ingredients as repair

REPO = Path.cwd()


@pytest.fixture(scope="module")
def frozen():
    return repair.approved(REPO)


@pytest.fixture
def plan(frozen):
    return copy.deepcopy(frozen)


@pytest.fixture
def root(tmp_path, plan, monkeypatch):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for relative in (repair.SOURCE, repair.PLAN):
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((REPO / relative).read_bytes())
    for item in plan["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    monkeypatch.setattr(repair, "validate_recipe", lambda *args, **kwargs: [])
    return tmp_path


def snapshot(root, plan):
    return {item["path"]: (root / item["path"]).read_bytes() for item in plan["records"]}


def test_pinned_inventory(frozen):
    assert tuple(item["key"] for item in frozen["records"]) == repair.KEYS
    assert sum(r["counts"]["quantity_corrections"] for r in frozen["records"]) == 56
    assert sum(r["counts"]["new_evidence"] for r in frozen["records"]) == 218


@pytest.mark.parametrize("index", range(4))
def test_independent_counts_and_audit_content(frozen, index):
    item = dict(frozen["records"][index], action=repair.ACTION)
    before, after = (repair.runner.load_yaml(item[key]) for key in ("before_text", "after_text"))
    assert dict(repair.check(before, after, item, REPO)) == item["counts"]
    after["ingredients"][0]["notes"] += " forged"
    with pytest.raises(AssertionError, match="Unreviewed record content"):
        repair.check(before, after, item, REPO)


def test_default_is_read_only(root, plan):
    before = snapshot(root, plan)
    assert repair.apply(plan, root) == {"changed": 0, "pending": 4, "already_applied": 0}
    assert snapshot(root, plan) == before


def test_boolean_cannot_impersonate_integer_count(root, plan):
    before = snapshot(root, plan)
    plan["records"][0]["counts"]["new_curation_history"] = True
    with pytest.raises(AssertionError, match="exact reviewed plan"):
        repair.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == before


def test_apply_readback_noop_and_permissions(root, plan):
    first = root / plan["records"][0]["path"]
    first.chmod(0o640)
    assert repair.apply(plan, root, dry_run=False) == {
        "changed": 4,
        "pending": 0,
        "already_applied": 0,
    }
    assert all((root / r["path"]).read_text() == r["after_text"] for r in plan["records"])
    assert first.stat().st_mode & 0o777 == 0o640
    assert repair.apply(plan, root, dry_run=False) == {
        "changed": 0,
        "pending": 0,
        "already_applied": 4,
    }
    assert repair.apply(plan, root, verify=True) == {
        "changed": 0,
        "pending": 0,
        "already_applied": 4,
    }
    assert not list((root / "data").rglob("*.tmp"))


@pytest.mark.parametrize("index", range(4))
@pytest.mark.parametrize(
    "fault",
    ["amount", "quote", "history", "taxon", "identity", "claim", "counts", "path", "before"],
)
def test_rehashed_forgeries_rejected_before_writes(root, plan, index, fault):
    before = snapshot(root, plan)
    item = plan["records"][index]
    after = repair.runner.load_yaml(item["after_text"])
    if fault == "amount":
        after["ingredients"][1]["concentration"]["value"] = "999"
    elif fault == "quote":
        after["ingredients"][1]["evidence"][1]["snippet"] = "fabricated"
    elif fault == "history":
        after["curation_history"][0]["notes"] = "changed"
    elif fault == "taxon":
        after["target_organisms"] = [{"preferred_term": "unsupported"}]
    elif fault == "identity":
        after["ingredients"][0]["term"] = {"id": "CHEBI:1", "label": "invented"}
    elif fault == "claim":
        item["claims"][0]["status"] = "verified"
    elif fault == "counts":
        item["counts"]["new_evidence"] = 1000
    elif fault == "path":
        item["path"] = "../../outside.yaml"
    else:
        item["before_text"] += "\n# changed baseline\n"
        item["before_sha256"] = repair.runner.sha(item["before_text"].encode())
    item["after_text"] = json.dumps(after)
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())
    with pytest.raises(AssertionError, match="exact reviewed plan"):
        repair.apply(plan, root, dry_run=False)
    assert all((root / path).read_bytes() == raw for path, raw in before.items())


@pytest.mark.parametrize(
    "fault",
    [
        "drift",
        "case",
        "symlink",
        "parent_symlink",
        "hardlink",
        "untracked",
        "invalid_schema",
        "verify",
        "order",
        "duplicate",
        "source",
        "preview",
    ],
)
def test_failed_preflight_writes_nothing(root, plan, monkeypatch, fault):
    last = root / plan["records"][-1]["path"]
    if fault == "drift":
        last.write_bytes(last.read_bytes() + b"\n# edited elsewhere\n")
    elif fault == "case":
        subprocess.run(
            ["git", "rm", "--cached", "--", str(last.relative_to(root))], cwd=root, check=True
        )
        subprocess.run(
            [
                "git",
                "update-index",
                "--add",
                "--cacheinfo",
                "100644",
                subprocess.check_output(
                    ["git", "hash-object", "-w", str(last)], cwd=root, text=True
                ).strip(),
                str(last.relative_to(root)).replace("fungal", "FUNGAL"),
            ],
            cwd=root,
            check=True,
        )
    elif fault == "symlink":
        saved = root / "saved.yaml"
        last.rename(saved)
        last.symlink_to(saved)
    elif fault == "parent_symlink":
        saved = root / "saved-directory"
        last.parent.rename(saved)
        last.parent.symlink_to(saved, target_is_directory=True)
    elif fault == "hardlink":
        os.link(last, root / "saved.yaml")
    elif fault == "untracked":
        subprocess.run(
            ["git", "rm", "--cached", "--", str(last.relative_to(root))], cwd=root, check=True
        )
    elif fault == "invalid_schema":
        monkeypatch.setattr(repair, "validate_recipe", lambda *args, **kwargs: ["invalid"])
    elif fault == "order":
        plan["records"].reverse()
    elif fault == "duplicate":
        plan["records"][-1] = copy.deepcopy(plan["records"][0])
    elif fault in {"source", "preview"}:
        target = root / (repair.SOURCE if fault == "source" else repair.PLAN)
        target.write_bytes(target.read_bytes() + b"\n")
    before = {p: p.read_bytes() for p in (root / "data").rglob("*.yaml")}
    with pytest.raises(AssertionError):
        repair.apply(plan, root, dry_run=False, verify=fault == "verify")
    assert all(path.read_bytes() == raw for path, raw in before.items())


@pytest.mark.parametrize("failure_at", range(4))
def test_stage_failure_changes_nothing(root, plan, monkeypatch, failure_at):
    original = repair._stage
    calls = 0
    before = snapshot(root, plan)

    def fail(target, content):
        nonlocal calls
        calls += 1
        if calls == failure_at + 1:
            raise OSError("injected staging failure")
        return original(target, content)

    monkeypatch.setattr(repair, "_stage", fail)
    with pytest.raises(OSError, match="staging failure"):
        repair.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == before
    assert not list((root / "data").rglob("*.tmp"))


@pytest.mark.parametrize("failure_at", range(4))
def test_publish_failure_rolls_back_written_records(root, plan, monkeypatch, failure_at):
    original = repair.os.replace
    calls = 0
    before = snapshot(root, plan)

    def fail(temporary, target):
        nonlocal calls
        calls += 1
        if calls == failure_at + 1:
            raise OSError("injected replacement failure")
        return original(temporary, target)

    monkeypatch.setattr(repair.os, "replace", fail)
    with pytest.raises(OSError, match="replacement failure"):
        repair.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == before
    assert not list((root / "data").rglob("*.tmp"))


def test_drift_during_staging_prevents_all_writes(root, plan, monkeypatch):
    original = repair._stage
    last = root / plan["records"][-1]["path"]
    before = snapshot(root, plan)
    calls = 0

    def drift(target, content):
        nonlocal calls
        calls += 1
        result = original(target, content)
        if calls == 4:
            last.write_bytes(last.read_bytes() + b"\n# external edit\n")
        return result

    monkeypatch.setattr(repair, "_stage", drift)
    with pytest.raises(AssertionError, match="Concurrent record edit"):
        repair.apply(plan, root, dry_run=False)
    assert all((root / p).read_bytes() == raw for p, raw in before.items() if root / p != last)
    assert last.read_bytes() == before[str(last.relative_to(root))] + b"\n# external edit\n"


def test_rollback_preserves_concurrent_edit_and_reports_partial(root, plan, monkeypatch):
    original = repair.os.replace
    first = root / plan["records"][0]["path"]
    calls = 0

    def conflict(temporary, target):
        nonlocal calls
        calls += 1
        if calls == 2:
            first.write_bytes(first.read_bytes() + b"\n# external edit\n")
            raise OSError("injected failure with concurrency")
        return original(temporary, target)

    monkeypatch.setattr(repair.os, "replace", conflict)
    with pytest.raises(RuntimeError, match="Partial application; manual inspection required"):
        repair.apply(plan, root, dry_run=False)
    assert first.read_text() == plan["records"][0]["after_text"] + "\n# external edit\n"
    assert all(
        (root / item["path"]).read_text() == item["before_text"] for item in plan["records"][1:]
    )


def test_partial_batch_can_resume(root, plan):
    item = plan["records"][0]
    (root / item["path"]).write_text(item["after_text"])
    assert repair.apply(plan, root, dry_run=False) == {
        "changed": 3,
        "pending": 0,
        "already_applied": 1,
    }


def test_optimized_python_cannot_disable_guards(root):
    result = subprocess.run(
        [sys.executable, "-O", str(Path(repair.__file__)), "--root", str(root)],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0 and "do not use -O" in result.stderr
