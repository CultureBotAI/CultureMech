"""Source amounts, preparation boundaries and guarded-application regressions."""

import copy
import hashlib
import importlib.util
import json
import subprocess
from dataclasses import replace
from pathlib import Path

import pytest
import review_halobacteria_ingredient_family as repair
import yaml

pytestmark = pytest.mark.usefixtures("no_workstation_receipt_reads")

SPEC = importlib.util.spec_from_file_location("halobacteria_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan-v2.json").read_text())
KEYS = [r["key"] for r in PLAN["records"]]
ITEMS = {r["key"]: r for r in PLAN["records"]}


def check(row):
    frozen = ITEMS[row["key"]]
    current_at_review_boundary(frozen)
    return audit.check(row, current_text=frozen["before_text"])


def current_at_review_boundary(row):
    actual = Path(row["path"]).read_text()
    if actual in (row["before_text"], row["after_text"]):
        return actual
    successor = repair.HERE.parent / "20261009-halobacteria-variants/plan-v2.json"
    raw = successor.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "c9611e131c0bc87eb0ffca52aa596859e29f5a66e3b2b39349ff961ffe4f7b78"
    )
    (item,) = [r for r in json.loads(raw)["records"] if r["path"] == row["path"]]
    assert item["key"] in {"J168", "M159", "M160"}
    assert item["before_text"] == row["after_text"] and actual == item["after_text"]
    assert yaml.safe_load(actual)["ingredients"] == yaml.safe_load(row["after_text"])["ingredients"]
    return row["after_text"]


def item(key):
    return copy.deepcopy(next(r for r in PLAN["records"] if r["key"] == key))


def tampered(key, mutate):
    row = item(key)
    doc = repair.runner.load_yaml(row["after_text"])
    mutate(doc)
    # Rehashed forgeries exercise semantics, not production formatting.
    row["after_text"] = json.dumps(doc, ensure_ascii=False)
    row["after_sha256"] = hashlib.sha256(row["after_text"].encode()).hexdigest()
    return row


@pytest.mark.parametrize("key", KEYS)
def test_forgery_serialization_accepts_every_unchanged_record(key):
    row = tampered(key, lambda doc: None)
    assert repair.runner.load_yaml(row["after_text"]) == yaml.safe_load(ITEMS[key]["after_text"])
    assert check(row) == check(item(key))


@pytest.mark.parametrize("key", KEYS)
def test_independent_primary_source_projection(key):
    result = check(item(key))
    assert result["old_quantities"] > 0 and result["claims"] > 0


def test_complete_old_and_new_ingredient_inventory():
    results = [check(r) for r in PLAN["records"]]
    assert sum(r["old_quantities"] for r in results) == 51
    assert sum(r["nodes"] for r in results) == 55
    assert sum(r["claims"] for r in results) == 171


@pytest.mark.parametrize("key", KEYS)
def test_rebuild_matches_frozen_successor(key):
    row = item(key)
    actual, claims, lineage = repair.build(
        repair.runner.load_yaml(row["before_text"]), key, PLAN["created_at"]
    )
    assert repair.runner.render(row["before_text"], actual).decode() == row["after_text"]
    assert claims == row["claims"] and lineage == row["lineage"]


def test_unreviewed_mim_index_bytes_are_rejected(tmp_path, monkeypatch):
    relative = "src/culturemech/data/mediaingredientmech/label_index.csv"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    path.write_bytes((repair.ROOT / relative).read_bytes() + b"\n")
    monkeypatch.setattr(repair, "ROOT", tmp_path)
    with pytest.raises(ValueError, match="MIM drift"):
        repair.frozen()


def test_mim_compatibility_assessment_hash_is_mandatory(monkeypatch):
    monkeypatch.setattr(repair, "INDEX_COMPATIBILITY_SHA", "0" * 64)
    with pytest.raises(ValueError, match="MIM compatibility drift"):
        repair.frozen()


def test_mim_compatibility_verifies_every_reviewed_lookup(monkeypatch):
    original = repair.MIMLabelIndex.resolve_label

    def changed(index, label):
        decision = original(index, label)
        return replace(decision, identifier="CHEBI:123") if label == "water" else decision

    monkeypatch.setattr(repair.MIMLabelIndex, "resolve_label", changed)
    with pytest.raises(ValueError, match="MIM resolution drift"):
        repair.frozen()


QUANTITIES = [
    (r["key"], i)
    for r in PLAN["records"]
    for i, node in enumerate(yaml.safe_load(r["after_text"])["ingredients"])
    if node.get("concentration")
]


@pytest.mark.parametrize("key,index", QUANTITIES)
def test_rehashed_quantity_mutation_is_rejected(key, index):
    row = tampered(key, lambda d: d["ingredients"][index]["concentration"].update(value="9999"))
    with pytest.raises(AssertionError):
        check(row)


@pytest.mark.parametrize("key", KEYS)
@pytest.mark.parametrize(
    "damage", ["water", "snippet", "history", "high_metal", "physical_state", "unrelated"]
)
def test_rehashed_semantic_or_provenance_mutation_is_rejected(key, damage):
    def mutate(doc):
        if damage == "water":
            water = next(n for n in doc["ingredients"] if n["preferred_term"] == "distilled water")
            water["concentration"] = {"value": "1", "unit": "L"}
        elif damage == "snippet":
            doc["ingredients"][0]["evidence"][0]["snippet"] = "invented quantity evidence"
        elif damage == "history":
            doc["curation_history"][0]["curator"] = "changed"
        elif damage == "high_metal":
            doc["high_metal"] = not doc.get("high_metal", False)
        elif damage == "physical_state":
            doc["physical_state"] = "SEMISOLID"
        else:
            doc["unreviewed_field"] = True

    with pytest.raises(AssertionError):
        check(tampered(key, mutate))


@pytest.mark.parametrize("key", ["J1007", "M1064"])
@pytest.mark.parametrize("value", ["20", "21"])
def test_modified_magnesium_is_source_stated_final_target_not_sum(key, value):
    def mutate(doc):
        next(n for n in doc["ingredients"] if n["preferred_term"].startswith("MgSO4"))[
            "concentration"
        ]["value"] = value

    with pytest.raises(AssertionError):
        check(tampered(key, mutate))


@pytest.mark.parametrize("key", KEYS)
def test_source_claims_cannot_be_removed(key):
    row = item(key)
    row["claims"] = [
        c for c in row["claims"] if not c["old_pointer"] or c["old_pointer"][-1] != "concentration"
    ]
    with pytest.raises(AssertionError):
        check(row)


def test_invalid_mode_is_rejected(tmp_path):
    with pytest.raises(ValueError, match="Invalid mode"):
        repair.process(tmp_path, tmp_path / "plan.json", "invalid")


def test_symlink_plan_rejected(tmp_path):
    target = tmp_path / "target.json"
    target.write_text("{}")
    plan = tmp_path / "plan.json"
    plan.symlink_to(target)
    with pytest.raises(ValueError, match="Plan symlink"):
        repair.process(repair.ROOT, plan)


def test_authoritative_inputs_match_reviewed_baseline_or_applied_result():
    for row in PLAN["records"]:
        current_at_review_boundary(row)


def fixture_repo(tmp_path, monkeypatch):
    for row in PLAN["records"]:
        path = tmp_path / row["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(row["before_text"])
    subprocess.run(["git", "init", "--quiet"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "data/normalized_yaml"], cwd=tmp_path, check=True)
    original = subprocess.check_output
    monkeypatch.setattr(
        subprocess,
        "check_output",
        lambda args, **kwargs: (
            PLAN["commit"] + "\n"
            if args == ["git", "rev-parse", "HEAD"]
            else original(args, **kwargs)
        ),
    )

    def builder(before, key, timestamp):
        row = ITEMS[key]
        assert (
            before == repair.runner.load_yaml(row["before_text"])
            and timestamp == PLAN["created_at"]
        )
        return copy.deepcopy(
            (repair.runner.load_yaml(row["after_text"]), row["claims"], row["lineage"])
        )

    monkeypatch.setattr(repair, "build", builder)
    plan = tmp_path / "plan.json"
    plan.write_bytes(repair.PLAN_PATH.read_bytes())
    return plan, {r["key"]: tmp_path / r["path"] for r in PLAN["records"]}


def test_guarded_apply_readback_and_noop(tmp_path, monkeypatch):
    plan, paths = fixture_repo(tmp_path, monkeypatch)
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 5
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 5
    before = {key: path.read_bytes() for key, path in paths.items()}
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert before == {key: path.read_bytes() for key, path in paths.items()}


@pytest.mark.parametrize("key", KEYS)
@pytest.mark.parametrize("damage", ["concurrent", "symlink"])
def test_changed_target_blocks_all_writes(tmp_path, monkeypatch, key, damage):
    plan, paths = fixture_repo(tmp_path, monkeypatch)
    if damage == "concurrent":
        paths[key].write_text(paths[key].read_text() + "# concurrent change\n")
    else:
        outside = tmp_path / "outside.yaml"
        outside.write_bytes(paths[key].read_bytes())
        paths[key].unlink()
        paths[key].symlink_to(outside)
    before = {key: path.read_bytes() for key, path in paths.items()}
    with pytest.raises(ValueError, match="Concurrent edit|symlink"):
        repair.process(tmp_path, plan, "apply")
    assert before == {key: path.read_bytes() for key, path in paths.items()}


@pytest.mark.parametrize("damage", ["removed_record", "claim", "symlink"])
def test_unreviewed_plan_blocks_all_writes(tmp_path, monkeypatch, damage):
    plan, paths = fixture_repo(tmp_path, monkeypatch)
    if damage == "symlink":
        plan.unlink()
        plan.symlink_to(repair.PLAN_PATH)
    else:
        proposed = copy.deepcopy(PLAN)
        if damage == "removed_record":
            proposed["records"].pop()
        else:
            proposed["records"][0]["claims"][0]["snippet"] = "invented"
        plan.write_text(json.dumps(proposed))
    before = {key: path.read_bytes() for key, path in paths.items()}
    with pytest.raises(ValueError, match="Unreviewed plan|Plan symlink"):
        repair.process(tmp_path, plan, "apply")
    assert before == {key: path.read_bytes() for key, path in paths.items()}


def test_changed_review_receipt_is_rejected(tmp_path, monkeypatch):
    plan, _ = fixture_repo(tmp_path, monkeypatch)
    monkeypatch.setattr(repair, "REVIEW_SHA", "0" * 64)
    with pytest.raises(ValueError, match="review receipt drift"):
        repair.process(tmp_path, plan, "apply")


def test_changed_validation_log_is_rejected(tmp_path, monkeypatch):
    plan, _ = fixture_repo(tmp_path, monkeypatch)
    gate = json.loads((repair.HERE / "validation-preview.json").read_text())
    log = tmp_path / "changed.log"
    log.write_text("changed")
    gate["checks"][0]["log"] = str(log)
    folder = tmp_path / "review"
    folder.mkdir()
    receipt = folder / "validation-preview.json"
    receipt.write_text(json.dumps(gate))
    monkeypatch.setattr(repair, "HERE", folder)
    monkeypatch.setattr(repair, "REVIEW_SHA", hashlib.sha256(receipt.read_bytes()).hexdigest())
    with pytest.raises(ValueError, match="Validation log drift"):
        repair.process(tmp_path, plan, "apply")
