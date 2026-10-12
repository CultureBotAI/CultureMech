"""Failure-closed checks for the three-record UTEX concentration application."""

from copy import deepcopy
from pathlib import Path

import pytest
import review_utex_volvocacean_bg11 as review

REPO = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def frozen():
    return review.approved(REPO)


@pytest.fixture
def plan(frozen):
    return deepcopy(frozen)


@pytest.fixture
def root(tmp_path, plan, monkeypatch):
    source = tmp_path / review.SOURCE
    source.parent.mkdir(parents=True)
    source.write_bytes((REPO / review.SOURCE).read_bytes())
    for item in plan["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    paths = "\0".join(item["path"] for item in plan["records"]) + "\0"
    monkeypatch.setattr(review.subprocess, "check_output", lambda *args, **kwargs: paths)
    monkeypatch.setattr(review, "validate_recipe", lambda *args, **kwargs: [])
    return tmp_path


def snapshot(root, plan):
    return {r["path"]: (root / r["path"]).read_bytes() for r in plan["records"]}


def test_preview_apply_verify_noop(root, plan):
    baseline = snapshot(root, plan)
    assert review.apply(plan, root) == {"changed": 0, "pending": 3, "already_applied": 0}
    assert snapshot(root, plan) == baseline
    with pytest.raises(AssertionError):
        review.apply(plan, root, verify=True)
    assert review.apply(plan, root, dry_run=False)["changed"] == 3
    assert review.apply(plan, root, dry_run=False)["changed"] == 0
    assert review.apply(plan, root, verify=True)["already_applied"] == 3
    assert all((root / r["path"]).read_text() == r["after_text"] for r in plan["records"])


@pytest.mark.parametrize("index", range(3))
def test_scope_counts_and_scientific_boundaries(frozen, index):
    item = frozen["records"][index]
    before, after = (review.runner.load_yaml(item[key]) for key in ("before_text", "after_text"))
    assert review.check(before, after, item, REPO) == item["counts"]
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["physical_state"] == "LIQUID"
    assert after["variants"][0]["relationship"] == "PHYSICAL_STATE_VARIANT"
    assert after["parent_media"]["id"] == before["parent_media"]["id"]
    if item["id"] == "CultureMech:000236":
        assert "removed" not in after["curation_history"][-1]["notes"]
        assert [n["concentration"] for n in after["solutions"]] == [
            n["concentration"] for n in before["solutions"]
        ]
        assert "without pH adjustment" in after["preparation_steps"][0]["description"]
        assert after["preparation_steps"][2]["action"] == "AUTOCLAVE"
        assert "10.0 g" in after["variants"][0]["modifications"][0]
        assert item["counts"]["new_evidence"] == 2
    else:
        assert "concentration" not in after["solutions"][0]
        assert after["ingredients"][0]["concentration"] == before["ingredients"][0]["concentration"]
        assert "not an exact" in after["ingredients"][0]["notes"]
        mods = " ".join(after["variants"][0]["modifications"])
        assert "15 g" in mods and "500 mL" in mods and "45-50" in mods
        assert "does not specify a thiosulfate dose" in mods
        assert item["counts"]["new_evidence"] == 3
        assert not any("not represented" in finding for finding in item["unresolved"])


@pytest.mark.parametrize("index", range(3))
@pytest.mark.parametrize(
    "fault",
    (
        "quantity",
        "unit",
        "snippet",
        "history",
        "identity",
        "year",
        "variant",
        "basis",
        "count",
        "path",
    ),
)
def test_rehashed_forgery_rejected(root, plan, index, fault):
    baseline = snapshot(root, plan)
    item = plan["records"][index]
    doc = review.runner.load_yaml(item["after_text"])
    if fault == "quantity":
        doc["solutions"][0]["concentration"] = {"value": "1000", "unit": "ML_PER_L"}
    elif fault == "unit":
        doc["solutions"][0]["concentration"] = {"value": "800", "unit": "MOLAR"}
    elif fault == "snippet":
        doc["evidence"][0]["snippet"] = "invented"
    elif fault == "history":
        doc["curation_history"][0]["notes"] = "rewritten"
    elif fault == "identity":
        doc["solutions"][0]["culturemech_term"]["id"] = "CultureMech:000001"
    elif fault == "year":
        doc["references"][1]["year"] = 2026
    elif fault == "variant":
        doc["variants"][0]["modifications"].append("Add 1 mL sodium thiosulfate stock.")
    elif fault == "basis":
        doc["solutions"][0]["concentration"] = {
            "value": "1",
            "unit": "ML_PER_L",
            "per_volume": "per 500 mL",
        }
    elif fault == "count":
        item["counts"]["new_curation_history"] = True
    else:
        item["path"] = item["path"].upper()
    item["after_text"] = review.runner.render(item["before_text"], doc).decode()
    item["after_sha256"] = review.runner.sha(item["after_text"].encode())
    with pytest.raises(AssertionError, match="reviewed plan"):
        review.apply(plan, root, dry_run=False)
    assert {path: (root / path).read_bytes() for path in baseline} == baseline


@pytest.mark.parametrize("index", range(3))
def test_concurrent_record_change_blocks_batch(root, plan, index):
    target = root / plan["records"][index]["path"]
    target.write_text(target.read_text() + "# concurrent edit\n")
    baseline = snapshot(root, plan)
    with pytest.raises(AssertionError, match="Concurrent edit"):
        review.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == baseline


def test_proposal_change_blocks_batch(root, plan):
    target = root / review.SOURCE
    target.write_text(target.read_text() + "\n")
    baseline = snapshot(root, plan)
    with pytest.raises(AssertionError, match="proposal drift"):
        review.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == baseline


@pytest.mark.parametrize("after", (False, True))
def test_schema_failure_blocks_batch(root, plan, monkeypatch, after):
    baseline = snapshot(root, plan)
    monkeypatch.setattr(
        review,
        "validate_recipe",
        lambda doc, **kwargs: (
            ["invalid"] if (doc["curation_history"][-1]["action"] == review.ACTION) == after else []
        ),
    )
    with pytest.raises(AssertionError, match="Invalid proposal" if after else "Invalid baseline"):
        review.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == baseline


@pytest.mark.parametrize("concurrent", (False, True))
def test_write_failure_rolls_back_without_clobber(root, plan, monkeypatch, concurrent):
    baseline = snapshot(root, plan)
    target = root / plan["records"][0]["path"]
    replace = review.os.replace
    calls = 0

    def fail_second(*args):
        nonlocal calls
        calls += 1
        if calls == 2:
            if concurrent:
                target.write_text("concurrent user edit\n")
            raise OSError("injected")
        return replace(*args)

    monkeypatch.setattr(review.os, "replace", fail_second)
    with pytest.raises(RuntimeError if concurrent else OSError):
        review.apply(plan, root, dry_run=False)
    for path, original in baseline.items():
        expected = b"concurrent user edit\n" if concurrent and root / path == target else original
        assert (root / path).read_bytes() == expected
    assert not list((root / "data").rglob("*.tmp"))


@pytest.mark.parametrize("hardlink", (False, True))
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


def test_untracked_target_rejected(root, plan, monkeypatch):
    baseline = snapshot(root, plan)
    monkeypatch.setattr(review.subprocess, "check_output", lambda *args, **kwargs: "")
    with pytest.raises(AssertionError, match="Untracked"):
        review.apply(plan, root, dry_run=False)
    assert snapshot(root, plan) == baseline
