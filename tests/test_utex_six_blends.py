"""Adversarial checks of the unapplied six-record prepared-blend guard."""

import subprocess
from copy import deepcopy
from pathlib import Path

import pytest
import review_utex_six_blends as review

REPO = Path.cwd()


@pytest.fixture(scope="module")
def frozen():
    return review.approved(REPO)


@pytest.fixture
def plan(frozen):
    return deepcopy(frozen)


@pytest.fixture
def root(tmp_path, plan, monkeypatch):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    source = tmp_path / review.SOURCE
    source.parent.mkdir(parents=True)
    source.write_bytes((REPO / review.SOURCE).read_bytes())
    for item in plan["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    monkeypatch.setattr(review, "validate_recipe", lambda *args, **kwargs: [])
    return tmp_path


def snapshot(root, plan):
    return {r["path"]: (root / r["path"]).read_bytes() for r in plan["records"]}


def first_component(doc):
    return doc["solutions"][0]


def test_preview_apply_verify_and_noop(root, plan):
    baseline = snapshot(root, plan)
    assert review.apply(plan, root) == {"changed": 0, "pending": 6, "already_applied": 0}
    assert snapshot(root, plan) == baseline
    with pytest.raises(AssertionError):
        review.apply(plan, root, verify=True)
    assert review.apply(plan, root, dry_run=False)["changed"] == 6
    assert review.apply(plan, root, dry_run=False)["changed"] == 0
    assert review.apply(plan, root, verify=True)["already_applied"] == 6
    assert all((root / r["path"]).read_text() == r["after_text"] for r in plan["records"])


@pytest.mark.parametrize("index", range(6))
def test_inverse_scope_and_preserved_amounts(frozen, index):
    item = frozen["records"][index]
    before, after = (review.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    assert review.check(before, after, item, REPO) == item["counts"]
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["id"] == before["id"] and after["category"] == before["category"]
    assert len(before["ingredients"]) == len(after["ingredients"])
    assert "variants" not in after
    for field, node in review._nodes(after).items():
        old = review._nodes(before)[field]
        assert node["concentration"] == old["concentration"]


@pytest.mark.parametrize("index", range(6))
@pytest.mark.parametrize(
    "fault",
    (
        "quantity",
        "unit",
        "snippet",
        "support",
        "identity",
        "history",
        "reference",
        "path",
        "count",
        "year",
        "notes",
        "basis",
    ),
)
def test_rehashed_forgeries_rejected(root, plan, index, fault):
    baseline = snapshot(root, plan)
    item = plan["records"][index]
    after = review.runner.load_yaml(item["after_text"])
    node = first_component(after)
    if fault in {"quantity", "unit", "basis"}:
        node.setdefault("concentration", {"value": "1", "unit": "ML_PER_L"})
    if fault == "quantity":
        node["concentration"]["value"] = "999"
    elif fault == "unit":
        node["concentration"]["unit"] = "MICROMOLAR"
    elif fault == "snippet":
        after["evidence"][0]["snippet"] = "invented"
    elif fault == "support":
        after["evidence"][0]["supports"] = "PARTIAL"
    elif fault == "identity":
        node["term"] = {"id": "CHEBI:1", "label": "invented"}
    elif fault == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif fault == "reference":
        after["evidence"][0]["reference"] += "#invented"
    elif fault == "path":
        item["path"] = item["path"].upper()
    elif fault == "count":
        item["counts"]["new_curation_history"] = True
    elif fault == "year":
        after["references"][0]["year"] = 2026
    elif fault == "basis":
        node["concentration"]["per_volume"] = "per liter of final medium"
    else:
        after["notes"] += " Autoclave at an invented temperature."
    item["after_text"] = review.runner.render(item["before_text"], after).decode()
    item["after_sha256"] = review.runner.sha(item["after_text"].encode())
    assert review.serialized(plan) != review.serialized(review.approved(REPO))
    with pytest.raises(AssertionError, match="reviewed plan"):
        review.apply(plan, root, dry_run=False)
    assert {path: (root / path).read_bytes() for path in baseline} == baseline


@pytest.mark.parametrize("index", range(6))
def test_current_record_drift_blocks_entire_batch(root, plan, index):
    path = root / plan["records"][index]["path"]
    path.write_text(path.read_text() + "# concurrent edit\n")
    baseline = snapshot(root, plan)
    with pytest.raises(AssertionError, match="Concurrent edit"):
        review.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == baseline


def test_source_drift(root, plan):
    path = root / review.SOURCE
    path.write_text(path.read_text() + "\n")
    baseline = snapshot(root, plan)
    with pytest.raises(AssertionError, match="proposal drift"):
        review.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == baseline


@pytest.mark.parametrize("invalid_after", [False, True])
def test_schema_failure_blocks_writes(root, plan, monkeypatch, invalid_after):
    baseline = snapshot(root, plan)
    monkeypatch.setattr(
        review,
        "validate_recipe",
        lambda doc, **kwargs: (
            ["invalid"]
            if (doc["curation_history"][-1]["action"] == review.ACTION) == invalid_after
            else []
        ),
    )
    with pytest.raises(
        AssertionError, match="Invalid proposal" if invalid_after else "Invalid baseline"
    ):
        review.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == baseline


@pytest.mark.parametrize("concurrent", [False, True])
def test_rollback_preserves_concurrent_edit(root, plan, monkeypatch, concurrent):
    baseline = snapshot(root, plan)
    target = root / plan["records"][0]["path"]
    original = review.os.replace
    calls = 0

    def fail_second(*args):
        nonlocal calls
        calls += 1
        if calls == 2:
            if concurrent:
                target.write_text("concurrent user edit\n")
            raise OSError("injected")
        return original(*args)

    monkeypatch.setattr(review.os, "replace", fail_second)
    with pytest.raises(RuntimeError if concurrent else OSError):
        review.apply(plan, root, dry_run=False)
    if concurrent:
        assert target.read_text() == "concurrent user edit\n"
        assert all(
            (root / p).read_bytes() == data for p, data in baseline.items() if root / p != target
        )
    else:
        assert snapshot(root, plan) == baseline
    assert not list((root / "data").rglob("*.tmp"))


@pytest.mark.parametrize("hardlink", [False, True])
def test_link_rejected(root, plan, hardlink):
    path = root / plan["records"][0]["path"]
    moved = root / "outside.yaml"
    path.rename(moved)
    if hardlink:
        path.hardlink_to(moved)
    else:
        path.symlink_to(moved)
    with pytest.raises(AssertionError):
        review.apply(plan, root, dry_run=False)
    assert moved.read_text() == plan["records"][0]["before_text"]
