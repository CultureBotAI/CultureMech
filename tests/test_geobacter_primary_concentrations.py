"""Conservative source scope and adversarial write guards for freshwater variants."""

import collections
import copy
import json
import subprocess

import pytest
import review_geobacter_primary_concentrations as repair


@pytest.fixture(scope="module")
def frozen_plan():
    return json.loads(repair.PLAN.read_text())


@pytest.fixture
def plan(frozen_plan):
    return copy.deepcopy(frozen_plan)


@pytest.fixture(params=sorted(repair.KEYS))
def reviewed(frozen_plan, request):
    item = copy.deepcopy(next(r for r in frozen_plan["records"] if r["key"] == request.param))
    return tuple(repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")) + (item,)


def rehash(item, doc):
    # JSON is valid YAML; forged inputs need semantic checks, not production formatting.
    item["after_text"] = json.dumps(doc, ensure_ascii=False)
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())


def test_full_inventory_and_totals(frozen_plan):
    counts, statuses = collections.Counter(), collections.Counter()
    for item in frozen_plan["records"]:
        counts.update(item["counts"])
        statuses.update(c["status"] for c in item["claims"])
    assert sum(statuses.values()) == 1628
    assert statuses["correct"] == 238 and statuses["evidence_only"] == 34
    assert counts == {
        "new_evidence": 350,
        "new_references": 74,
        "new_curation_history": 56,
        "preparation_actions_corrected": 56,
        "preparation_descriptions_corrected": 56,
        "quantity_corrections": 238,
        "supplied_hydrate_identities_corrected": 56,
        "ingredient_labels_corrected": 18,
    }


def test_each_record_preserves_unreviewed_claims(reviewed):
    before, after, item = reviewed
    assert dict(repair.check(before, after, item)) == item["counts"]
    assert len(item["claims"]) == len(before["ingredients"]) == len(after["ingredients"])
    assert "&id" not in item["after_text"] and "*id" not in item["after_text"]
    for old, new, claim in zip(
        before["ingredients"], after["ingredients"], item["claims"], strict=True
    ):
        if claim["status"] in {"conflict", "unsupported"} and claim["identity_status"] != "correct":
            assert new == old
        else:
            assert new.get("evidence", [])[: len(old.get("evidence", []))] == old.get(
                "evidence", []
            )
            assert all(
                e["snippet"] and e["reference"].startswith(("doi:", "https://"))
                for e in claim["evidence"]
            )
        if old["preferred_term"] == "Sodium dihydrogen phosphate":
            assert new["term"]["id"] == "CHEBI:114249"
            assert new["concentration"] == {"value": "0.6", "unit": "G_PER_L"}
        if old["preferred_term"] == "Acetate":
            if old["concentration"]["value"] == "113.2":
                assert new["term"]["id"] == "CHEBI:32954"
                assert new["concentration"] == {"value": "6.8", "unit": "G_PER_L"}
                assert len(claim["evidence"]) == 2
            else:
                assert claim["status"] == "unsupported"
                assert claim["identity_status"] == "correct"
                assert new["concentration"] == old["concentration"]
                assert new["term"]["id"] == "CHEBI:32954"
                assert len(claim["evidence"]) == 2
                assert all(".term," in e["explanation"] for e in claim["evidence"])
                assert all("do not verify it" in e["explanation"] for e in claim["evidence"])
    for key in (
        "id",
        "original_name",
        "media_term",
        "target_organisms",
        "medium_type",
        "composition_type",
        "parent_media",
        "variant_children",
        "variant_modifications",
    ):
        assert before.get(key) == after.get(key)
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["preparation_steps"][:2] == before["preparation_steps"][:2]
    assert after["preparation_steps"][2]["action"] == "AUTOCLAVE"


def test_forgery_serialization_preserves_every_record(reviewed):
    before, after, item = reviewed
    rehash(item, after)
    assert repair.runner.load_yaml(item["after_text"]) == after
    # A valid JSON/YAML document must pass, so formatting cannot cause a false rejection.
    assert dict(repair.check(before, after, item)) == item["counts"]


def test_variant_identity_regression_and_endpoint_scope(frozen_plan):
    assert len(repair.check_variant_identities(frozen_plan)) == 10
    endpoints = [
        (r["key"], c)
        for r in frozen_plan["records"]
        for c in r["claims"]
        if c["ingredient"] == "Acetate" and c["status"] == "unsupported"
    ]
    assert {key for key, _ in endpoints} == {"423", "424", "451", "455"}
    assert all(c["old"] == c["proposed"] for _, c in endpoints)
    original = json.loads((repair.HERE / "plan.json").read_text())
    with pytest.raises(AssertionError, match="identities diverge"):
        repair.check_variant_identities(original)


@pytest.mark.parametrize("key", ["423", "424", "451", "455"])
def test_identity_only_correction_cannot_certify_endpoint(plan, key):
    item = next(r for r in plan["records"] if r["key"] == key)
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    claim = next(c for c in item["claims"] if c["ingredient"] == "Acetate")
    claim["status"] = "evidence_only"
    with pytest.raises(AssertionError, match="semantic change"):
        repair.check(before, after, item)


@pytest.mark.parametrize("key", ["423", "424", "451", "455"])
def test_parent_child_salt_identity_drift_rejected(plan, key):
    item = next(r for r in plan["records"] if r["key"] == key)
    doc = repair.runner.load_yaml(item["after_text"])
    node = next(n for n in doc["ingredients"] if n["preferred_term"] == "Sodium acetate")
    node["term"]["id"] = "CHEBI:30089"
    rehash(item, doc)
    with pytest.raises(AssertionError, match="identities diverge"):
        repair.check_variant_identities(plan)


@pytest.mark.parametrize(
    "field,value", [("value", "999"), ("unit", "MOLAR"), ("per_volume", "100 mL")]
)
def test_any_rehashed_quantity_forgery_is_rejected(reviewed, field, value):
    before, after, item = reviewed
    # Every ingredient is exercised, including unsupported trace and acceptor nodes.
    for index in range(len(after["ingredients"])):
        changed = copy.deepcopy(after)
        changed["ingredients"][index]["concentration"][field] = value
        forged = copy.deepcopy(item)
        rehash(forged, changed)
        with pytest.raises(AssertionError):
            repair.check(before, changed, forged)


@pytest.mark.parametrize(
    "kind",
    [
        "identity",
        "quote",
        "reference",
        "scope",
        "history",
        "preparation",
        "classification",
        "order",
        "claim",
    ],
)
def test_rehashed_semantic_forgery_is_rejected(reviewed, kind):
    before, after, item = reviewed
    node = next(
        n
        for n in after["ingredients"]
        if n["preferred_term"] == "Sodium dihydrogen phosphate monohydrate"
    )
    entry = node["evidence"][-1]
    if kind == "identity":
        node["term"] = {"id": "CHEBI:15377", "label": "water"}
    elif kind in {"quote", "reference", "scope"}:
        entry[{"quote": "snippet", "reference": "reference", "scope": "explanation"}[kind]] = (
            "unreviewed"
        )
    elif kind == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif kind == "preparation":
        after["preparation_steps"][2]["description"] += " at 121 C for 15 minutes"
    elif kind == "classification":
        after["physical_state"] = "SOLID"
    elif kind == "order":
        after["ingredients"].reverse()
    else:
        item["claims"][0]["status"] = "verified"
    rehash(item, after)
    with pytest.raises(AssertionError):
        repair.check(before, after, item)


def make_repo(tmp_path, plan, monkeypatch):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for item in plan["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    # Real baseline/proposed schema CLI checks run on every record separately.
    monkeypatch.setattr(repair, "validate_recipe", lambda *a, **k: [])
    return tmp_path


def test_guarded_write_readback_and_noop(plan, tmp_path, monkeypatch):
    root = make_repo(tmp_path, plan, monkeypatch)
    assert repair.apply(plan, root) == {"changed": 56, "already_applied": 0}
    assert repair.apply(plan, root) == {"changed": 0, "already_applied": 56}
    assert repair.apply(plan, root, verify=True) == {"changed": 0, "already_applied": 56}


@pytest.mark.parametrize(
    "kind",
    [
        "late_drift",
        "duplicate",
        "outside",
        "symlink",
        "source",
        "version",
        "case",
        "counts",
        "verify_before_apply",
    ],
)
def test_preflight_rejects_before_any_write(plan, tmp_path, monkeypatch, kind):
    root = make_repo(tmp_path, plan, monkeypatch)
    original = {r["path"]: (root / r["path"]).read_bytes() for r in plan["records"]}
    last = plan["records"][-1]
    if kind == "late_drift":
        target = root / last["path"]
        target.write_bytes(target.read_bytes() + b"\n# concurrent edit\n")
        original[last["path"]] = target.read_bytes()
    elif kind == "duplicate":
        plan["records"][-1] = copy.deepcopy(plan["records"][0])
    elif kind == "outside":
        last["path"] = "../../outside.yaml"
    elif kind == "symlink":
        target = root / last["path"]
        saved = root / "elsewhere.yaml"
        target.rename(saved)
        target.symlink_to(saved)
    elif kind == "source":
        plan["source_sha256"] = "0" * 64
    elif kind == "version":
        plan["version"] = 999
    elif kind == "case":
        last["path"] = last["path"].replace("MEDIADB", "mediadb")
    elif kind == "counts":
        last["counts"]["new_evidence"] = 999
    with pytest.raises((AssertionError, ValueError)):
        repair.apply(plan, root, verify=kind == "verify_before_apply")
    assert all((root / p).read_bytes() == raw for p, raw in original.items())
