"""Evidence scope, null semantics, semantic diff and guarded MediaDB writes."""

import copy
import json
import subprocess

import pytest
import repair_mediadb_ingredient_exceptions as repair


@pytest.fixture
def plan():
    return json.loads(repair.PLAN.read_text())


@pytest.fixture(params=sorted(repair.KEYS))
def reviewed(plan, request):
    item = next(r for r in plan["records"] if r["key"] == request.param)
    return (
        repair.runner.load_yaml(item["before_text"]),
        repair.runner.load_yaml(item["after_text"]),
        item,
    )


def rehash(item, doc):
    item["after_text"] = repair.runner.render(item["before_text"], doc).decode()
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())


def test_source_amount_membership_and_history(reviewed):
    before, after, item = reviewed
    assert repair.check(before, after, item) == item["counts"]
    assert after["curation_history"][:-1] == before["curation_history"]
    assert before.get("target_organisms") == after.get("target_organisms")


@pytest.mark.parametrize(
    "kind",
    [
        "amount",
        "unit",
        "basis",
        "identity",
        "quote",
        "scope",
        "history",
        "category",
        "reorder",
        "remove",
        "reference",
        "wrong_accession",
    ],
)
def test_rehashed_forgery_rejected(reviewed, kind):
    before, after, item = reviewed
    node = next(n for n in after["ingredients"] if "concentration" in n)
    if kind == "amount":
        node["concentration"]["value"] = "999"
    elif kind == "unit":
        node["concentration"]["unit"] = "G_PER_L"
    elif kind == "basis":
        node["concentration"]["per_volume"] = "100 mL"
    elif kind == "identity":
        node["term"] = {"id": "CHEBI:15377", "label": "water"}
    elif kind == "quote":
        node["evidence"][-1]["snippet"] = "Invented amount"
    elif kind == "scope":
        node["evidence"][-1]["explanation"] = "Proves a different medium"
    elif kind == "history":
        after["curation_history"][0]["notes"] = "Changed historical event"
    elif kind == "category":
        after["category"] = "fungal"
    elif kind == "reorder":
        after["ingredients"].reverse()
    elif kind == "remove":
        after["ingredients"].pop()
    elif kind == "reference":
        after["references"][0]["authors"] = "Invented author"
    else:
        after["media_term"]["term"]["id"] = "MEDIADB:109"
    rehash(item, after)
    with pytest.raises((AssertionError, ValueError, KeyError)):
        repair.check(before, after, item)


@pytest.mark.parametrize("key", ["288", "289"])
@pytest.mark.parametrize("amount", ["0", "1", "variable"])
def test_unknown_never_becomes_zero_or_variable(plan, key, amount):
    item = next(r for r in plan["records"] if r["key"] == key)
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    after["ingredients"][0]["concentration"] = {
        "value": amount,
        "unit": "VARIABLE" if amount == "variable" else "MILLIMOLAR",
    }
    rehash(item, after)
    with pytest.raises(AssertionError):
        repair.check(before, after, item)


def test_counts_and_exact_variant_values(plan):
    total = sum(
        (repair.collections.Counter(r["counts"]) for r in plan["records"]),
        repair.collections.Counter(),
    )
    assert total == {
        "new_evidence": 156,
        "new_references": 12,
        "new_curation_history": 6,
        "new_quantity_slots": 6,
        "unsupported_quantity_slots_removed": 31,
        "copied_ingredient_nodes_removed": 12,
        "recipe_context_notes_corrected": 4,
    }
    docs = {r["key"]: repair.runner.load_yaml(r["after_text"]) for r in plan["records"]}
    for key, n in {"430": 29, "460": 29, "473": 26, "474": 27, "288": 17, "289": 24}.items():
        assert len(docs[key]["ingredients"]) == n
    cobalt = [
        [n["preferred_term"] for n in docs[k]["ingredients"] if "Cobalt" in n["preferred_term"]]
        for k in ("430", "460")
    ]
    assert cobalt == [["Cobaltous sulfate"], ["Cobalt chloride"]]
    for key, rate in (("288", "0.0383"), ("289", "0.0282")):
        assert (
            next(n for n in docs[key]["ingredients"] if n["preferred_term"] == "Zinc sulfate")[
                "concentration"
            ]["value"]
            == rate
        )


def make_repo(tmp_path, plan, monkeypatch):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for item in plan["records"]:
        target = tmp_path / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(item["before_text"])
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    # Shape validation is covered by the actual-record checkpoint, not these write-guard tests.
    monkeypatch.setattr(repair, "validate_recipe", lambda *a, **k: [])
    return tmp_path


def test_guarded_apply_readback_noop(plan, tmp_path, monkeypatch):
    root = make_repo(tmp_path, plan, monkeypatch)
    assert repair.apply(plan, root) == {"changed": 6, "already_applied": 0}
    assert repair.apply(plan, root) == {"changed": 0, "already_applied": 6}
    assert repair.apply(plan, root, verify=True) == {"changed": 0, "already_applied": 6}
    for item in plan["records"]:
        assert (root / item["path"]).read_text() == item["after_text"]


@pytest.mark.parametrize(
    "kind",
    ["late_drift", "duplicate", "outside", "symlink", "verify_before_apply", "version", "source"],
)
def test_preflight_rejects_without_partial_write(plan, tmp_path, monkeypatch, kind):
    root = make_repo(tmp_path, plan, monkeypatch)
    original = {r["path"]: (root / r["path"]).read_bytes() for r in plan["records"]}
    if kind == "late_drift":
        target = root / plan["records"][-1]["path"]
        target.write_bytes(target.read_bytes() + b"\n# independent change\n")
        original[plan["records"][-1]["path"]] = target.read_bytes()
    elif kind == "duplicate":
        plan["records"][-1] = copy.deepcopy(plan["records"][0])
    elif kind == "outside":
        plan["records"][-1]["path"] = "../../outside.yaml"
    elif kind == "symlink":
        target = root / plan["records"][-1]["path"]
        saved = root / "symlink-target.yaml"
        target.rename(saved)
        target.symlink_to(saved)
    elif kind == "version":
        plan["version"] = 999
    elif kind == "source":
        plan["source_sha256"] = "0" * 64
    with pytest.raises((AssertionError, ValueError)):
        repair.apply(plan, root, verify=kind == "verify_before_apply")
    assert all((root / path).read_bytes() == raw for path, raw in original.items())
