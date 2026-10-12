"""Primary-source amount, preparation-stage and provenance regression checks."""

import copy
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import review_halobacteria_variant_concentrations as review
import yaml

pytestmark = [pytest.mark.corpus, pytest.mark.usefixtures("no_workstation_receipt_reads")]
SPEC = importlib.util.spec_from_file_location(
    "halobacteria_variant_audit", review.HERE / "audit.py"
)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)
PLAN = json.loads((review.HERE / "plan-v2.json").read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}


def row(key):
    return copy.deepcopy(ITEMS[key])


def check(item):
    frozen = ITEMS[item["key"]]
    assert Path(frozen["path"]).read_text() in (frozen["before_text"], frozen["after_text"])
    # Mutation tests must reach the scientific assertions, not fail on readback equality.
    return audit.check(item, current_text=frozen["before_text"])


def damage(key, mutate):
    item = row(key)
    doc = review.runner.load_yaml(item["after_text"])
    mutate(doc)
    # Rehashed forgeries exercise semantics, not production formatting.
    item["after_text"] = json.dumps(doc, ensure_ascii=False)
    item["after_sha256"] = hashlib.sha256(item["after_text"].encode()).hexdigest()
    return item


@pytest.mark.parametrize("key", ITEMS)
def test_forgery_serialization_accepts_every_unchanged_record(key):
    item = damage(key, lambda doc: None)
    assert review.runner.load_yaml(item["after_text"]) == yaml.safe_load(ITEMS[key]["after_text"])
    assert check(item) == check(row(key))


@pytest.mark.parametrize("key", ITEMS)
def test_independent_projection(key):
    assert check(row(key))["claims"] > 0


def test_full_cohort_quantity_scope():
    results = {key: check(row(key)) for key in ITEMS}
    assert len(results) == 16
    assert sum(r["old_quantities_reviewed"] for r in results.values()) == 127
    assert sum(r["old_quantities"] for r in results.values()) == 155
    assert sum(r["claims"] for r in results.values()) == 575
    assert {k for k, r in results.items() if r["old_quantities_reviewed"] == 0} == {
        "J168",
        "M159",
        "M160",
    }


@pytest.mark.parametrize("key", ITEMS)
def test_rebuild_matches_frozen_preview(key):
    item = ITEMS[key]
    after, claims, lineage = review.build(
        review.runner.load_yaml(item["before_text"]), key, PLAN["created_at"]
    )
    assert review.runner.render(item["before_text"], after).decode() == item["after_text"]
    assert claims == item["claims"] and lineage == item["lineage"]


QUANTITIES = [
    (key, pointer)
    for key, item in ITEMS.items()
    for pointer, node in audit.walk(yaml.safe_load(item["after_text"]))
    if "concentration" in node
]


@pytest.mark.parametrize("key,pointer", QUANTITIES)
def test_rehashed_quantity_change_rejected(key, pointer):
    item = damage(key, lambda doc: audit.get(doc, pointer)["concentration"].update(value="9999"))
    with pytest.raises(AssertionError):
        check(item)


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "kind", ["water", "snippet", "history", "identity", "high_metal", "unrelated"]
)
def test_rehashed_semantic_and_evidence_attacks(key, kind):
    def mutate(doc):
        nodes = [node for pointer, node in audit.walk(doc) if pointer]
        if kind == "water":
            next(n for n in nodes if audit.label(n["preferred_term"]) == "distilled water")[
                "concentration"
            ] = {"value": "1", "unit": "L"}
        elif kind == "snippet":
            next(n for n in nodes if n.get("evidence"))["evidence"][0][
                "snippet"
            ] = "invented evidence"
        elif kind == "history":
            doc["curation_history"][0]["curator"] = "rewritten"
        elif kind == "identity":
            next(n for n in nodes if n.get("term"))["term"]["id"] = "CHEBI:99999"
        elif kind == "high_metal":
            doc["high_metal"] = not doc.get("high_metal", False)
        else:
            doc["unreviewed_field"] = True

    with pytest.raises(AssertionError):
        check(damage(key, mutate))


@pytest.mark.parametrize("key", ["J1132", "M1212"])
@pytest.mark.parametrize("kind", ["flat", "dose_basis", "ph_order", "carbonate", "agar", "roles"])
def test_prepared_base_boundary_attacks(key, kind):
    def mutate(doc):
        stock = doc["solutions"][0]
        if kind == "flat":
            doc["ingredients"] = copy.deepcopy(stock["composition"])
        elif kind == "dose_basis":
            stock["concentration"] = {"value": "1000", "unit": "ML_PER_L"}
        elif kind == "ph_order":
            doc["preparation_steps"].append(
                {"step_number": 2, "action": "ADJUST_PH", "description": "Adjust pH to 7.0-7.2."}
            )
        elif kind == "carbonate":
            doc["solutions"].append({"preferred_term": "Na2CO3 solution", "composition": []})
        elif kind == "agar":
            stock["composition"].append(
                {"preferred_term": "agar", "concentration": {"value": "20", "unit": "G_PER_L"}}
            )
        else:
            stock["composition"][0]["nutritional_roles"] = ["CARBON_SOURCE"]

    with pytest.raises(AssertionError):
        check(damage(key, mutate))


@pytest.mark.parametrize("key", review.LINKS)
def test_duplicate_relationship_cannot_return(key):
    def mutate(doc):
        doc["parent_media"]["relationship"] = "SOURCE_DUPLICATE"
        doc["variant_relationship"] = "SOURCE_DUPLICATE"

    with pytest.raises(AssertionError):
        check(damage(key, mutate))


@pytest.mark.parametrize("key", ["J168", "M159", "M160"])
def test_reciprocal_path_cannot_drift(key):
    with pytest.raises(AssertionError):
        check(damage(key, lambda doc: doc["variant_children"][0].update(path="wrong.yaml")))


@pytest.mark.parametrize("key", [k for k in ITEMS if k not in review.PARENTS])
def test_quantity_claims_cannot_be_dropped(key):
    item = row(key)
    item["claims"] = [
        c for c in item["claims"] if not c["old_pointer"] or c["old_pointer"][-1] != "concentration"
    ]
    with pytest.raises(AssertionError):
        check(item)


@pytest.mark.parametrize("key", [k for k in ITEMS if k not in review.PARENTS])
def test_iron_unit_change_rejected(key):
    def mutate(doc):
        node = next(
            n
            for p, n in audit.walk(doc)
            if p and audit.label(n["preferred_term"]) == "FeCl2\u00b74H2O"
        )
        node["concentration"]["unit"] = (
            "G_PER_L" if node["concentration"]["unit"] == "MG_PER_L" else "MG_PER_L"
        )

    with pytest.raises(AssertionError):
        check(damage(key, mutate))


@pytest.mark.parametrize("key", ["J1008", "M1065"])
@pytest.mark.parametrize(
    "name,amount",
    [("MgSO4\u00b77H2O", "35"), ("MgSO4\u00b77H2O", "20"), ("NaCl", "470"), ("NaCl", "200")],
)
def test_modified_formula_not_sum_or_copied_base(key, name, amount):
    def mutate(doc):
        next(n for n in doc["ingredients"] if audit.label(n["preferred_term"]) == name)[
            "concentration"
        ]["value"] = amount

    with pytest.raises(AssertionError):
        check(damage(key, mutate))


@pytest.mark.parametrize("key", [k for k in ITEMS if k not in review.PARENTS])
def test_lineage_cannot_be_dropped(key):
    item = row(key)
    item["lineage"].pop()
    with pytest.raises(AssertionError):
        check(item)


def test_invalid_mode_rejected(tmp_path):
    with pytest.raises(ValueError, match="Invalid mode"):
        review.process(tmp_path, tmp_path / "plan.json", "invalid")


def test_plan_symlink_rejected(tmp_path):
    link = tmp_path / "plan.json"
    link.symlink_to(review.HERE / "plan.json")
    with pytest.raises(ValueError, match="Plan symlink"):
        review.process(review.ROOT, link)


def test_existing_plan_not_overwritten():
    with pytest.raises(ValueError, match="overwrite"):
        review.process(review.ROOT, review.HERE / "plan.json")


def test_current_records_match_baseline_or_applied_result():
    for item in ITEMS.values():
        applied = Path(item["path"]).read_text() == item["after_text"]
        assert audit.check(item, applied=applied)["claims"] > 0


def fixture_repo(tmp_path, monkeypatch):
    for item in ITEMS.values():
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
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
        item = ITEMS[key]
        assert (
            before == review.runner.load_yaml(item["before_text"])
            and timestamp == PLAN["created_at"]
        )
        return copy.deepcopy(
            (review.runner.load_yaml(item["after_text"]), item["claims"], item["lineage"])
        )

    monkeypatch.setattr(review, "build", builder)
    plan = tmp_path / "plan.json"
    plan.write_bytes(review.PLAN_PATH.read_bytes())
    return plan, {r["key"]: tmp_path / r["path"] for r in PLAN["records"]}


def test_guarded_apply_readback_and_noop(tmp_path, monkeypatch):
    plan, paths = fixture_repo(tmp_path, monkeypatch)
    assert review.process(tmp_path, plan, "apply")[1]["changed"] == 16
    assert review.process(tmp_path, plan, "verify")[1]["already_applied"] == 16
    before = {key: path.read_bytes() for key, path in paths.items()}
    assert review.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert before == {key: path.read_bytes() for key, path in paths.items()}


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize("kind", ["concurrent", "symlink"])
def test_changed_target_prevents_all_writes(tmp_path, monkeypatch, key, kind):
    plan, paths = fixture_repo(tmp_path, monkeypatch)
    if kind == "concurrent":
        paths[key].write_text(paths[key].read_text() + "# concurrent change\n")
    else:
        outside = tmp_path / "outside.yaml"
        outside.write_bytes(paths[key].read_bytes())
        paths[key].unlink()
        paths[key].symlink_to(outside)
    before = {key: path.read_bytes() for key, path in paths.items()}
    with pytest.raises(ValueError, match="Concurrent edit|symlink"):
        review.process(tmp_path, plan, "apply")
    assert before == {key: path.read_bytes() for key, path in paths.items()}


@pytest.mark.parametrize("kind", ["record", "snippet", "symlink"])
def test_altered_plan_prevents_all_writes(tmp_path, monkeypatch, kind):
    plan, paths = fixture_repo(tmp_path, monkeypatch)
    if kind == "symlink":
        plan.unlink()
        plan.symlink_to(review.PLAN_PATH)
    else:
        proposal = copy.deepcopy(PLAN)
        if kind == "record":
            proposal["records"].pop()
        else:
            proposal["records"][0]["claims"][0]["snippet"] = "invented"
        plan.write_text(json.dumps(proposal))
    before = {key: path.read_bytes() for key, path in paths.items()}
    with pytest.raises(ValueError, match="Unreviewed plan|Plan symlink"):
        review.process(tmp_path, plan, "apply")
    assert before == {key: path.read_bytes() for key, path in paths.items()}


def test_review_receipt_drift_rejected(tmp_path, monkeypatch):
    plan, _ = fixture_repo(tmp_path, monkeypatch)
    monkeypatch.setattr(review, "REVIEW_SHA", "0" * 64)
    with pytest.raises(ValueError, match="review receipt drift"):
        review.process(tmp_path, plan, "apply")


def test_review_log_drift_rejected(tmp_path, monkeypatch):
    plan, _ = fixture_repo(tmp_path, monkeypatch)
    gate = json.loads((review.HERE / "validation-preview.json").read_text())
    log = tmp_path / "changed.log"
    log.write_text("changed")
    gate["checks"][0]["log"] = str(log)
    folder = tmp_path / "review"
    folder.mkdir()
    receipt = folder / "validation-preview.json"
    receipt.write_text(json.dumps(gate))
    monkeypatch.setattr(review, "HERE", folder)
    monkeypatch.setattr(review, "REVIEW_SHA", hashlib.sha256(receipt.read_bytes()).hexdigest())
    with pytest.raises(ValueError, match="Validation log drift"):
        review.process(tmp_path, plan, "apply")
