"""Adversarial checks for per-liter doses, base inheritance and literal evidence."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_togo_methanogen_concentrations as repair

spec = importlib.util.spec_from_file_location("methanogen_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())


@pytest.mark.parametrize("item", PLAN["records"], ids=lambda r: r["key"])
def test_source_arithmetic_and_semantic_inversion(item):
    before = repair.runner.load_yaml(item["before_text"])
    after, claims = repair.build(before, item["key"], PLAN["created_at"])
    assert after == repair.runner.load_yaml(item["after_text"])
    assert claims == item["claims"]
    assert audit.check(before, after, item)["new_curation_history"] == 1


@pytest.mark.parametrize("item", PLAN["records"], ids=lambda r: r["key"])
def test_whole_baseline_drift_rejected(item):
    before = repair.runner.load_yaml(item["before_text"])
    before["ingredients"][0]["concentration"]["value"] = "wrong"
    with pytest.raises(ValueError, match="baseline"):
        repair.build(before, item["key"], PLAN["created_at"])


@pytest.mark.parametrize("field", ["url", "response_url", "http_status", "sha256"])
def test_capture_drift_rejected(field):
    context = copy.deepcopy(repair.frozen())
    context["sources"]["M1038"]["metadata"][field] = "wrong"
    with pytest.raises(ValueError, match="Capture drift"):
        repair.sources(context)


@pytest.mark.parametrize(
    "mutation", ["per_liter", "resazurin", "strength", "supplement", "identity"]
)
def test_source_semantics_checked_independently_of_capture_hash(mutation):
    context = copy.deepcopy(repair.frozen())
    key = "M1039" if mutation == "supplement" else "J985" if mutation == "strength" else "M1038"
    source = context["sources"][key]
    body = json.loads(source["raw"])
    if mutation == "per_liter":
        body["comments"][1]["comment"] = body["comments"][1]["comment"].replace(
            "per liter", "per batch"
        )
    elif mutation == "resazurin":
        body["components"][0]["items"][5]["unit"] = "g"
    elif mutation == "strength":
        body["data"]["solutions"][0]["recipe"][12]["attribute"] = "*, 3%"
    elif mutation == "supplement":
        body["components"][0]["items"][0]["unit"] = "g"
    else:
        body["meta"]["original_media_id"] = "JCM_M986"
    source["raw"] = json.dumps(body)
    source["metadata"]["sha256"] = repair.runner.sha(source["raw"].encode())
    with pytest.raises(ValueError, match="drift"):
        repair.sources(context)


@pytest.mark.parametrize(
    "mutation",
    [
        "per_liter",
        "batch",
        "resazurin",
        "strength",
        "conflict",
        "quote",
        "history",
        "year",
        "gas",
        "ph",
    ],
)
def test_independent_audit_rejects_wrong_science(mutation):
    item = copy.deepcopy(PLAN["records"][0])
    before, after = [repair.runner.load_yaml(item[k + "_text"]) for k in ("before", "after")]
    if mutation == "per_liter":
        after["solutions"][6]["concentration"] = {"value": "0.008", "unit": "L"}
    elif mutation == "batch":
        after["solutions"][0]["concentration"] = {"value": "20", "unit": "ML_PER_L"}
    elif mutation == "resazurin":
        after["ingredients"][5]["concentration"] = {"value": "1", "unit": "MG_PER_L"}
    elif mutation == "strength":
        after["solutions"][1]["composition"] = [
            {
                "preferred_term": "Trimethylamine hydrochloride",
                "concentration": {"value": "3", "unit": "PERCENT_W_V"},
            }
        ]
    elif mutation == "conflict":
        after["solutions"][1]["notes"] = after["solutions"][1]["notes"].replace("30%", "3%")
    elif mutation == "quote":
        after["ingredients"][0]["evidence"][0]["snippet"] = "invented"
    elif mutation == "history":
        after["curation_history"][0]["curator"] = "rewritten"
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "gas":
        after["ingredients"][8]["concentration"] = {"value": "20", "unit": "PERCENT_V_V"}
    else:
        after["ph_value"] = 7
    for c in item["claims"]:
        if c["pointer"]:
            c["new"] = audit.get(after, c["pointer"][:-1]).get(c["pointer"][-1])
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


@pytest.mark.parametrize("mutation", ["dose", "base_id", "supplement", "copied", "base_scope"])
def test_base_medium_is_referenced_not_discarded_or_recertified(mutation):
    item = copy.deepcopy(PLAN["records"][2])
    before, after = [repair.runner.load_yaml(item[k + "_text"]) for k in ("before", "after")]
    if mutation == "dose":
        after["solutions"][0]["concentration"] = {"value": "1", "unit": "L"}
    elif mutation == "base_id":
        after["solutions"][0]["culturemech_term"]["id"] = "CultureMech:003335"
    elif mutation == "supplement":
        after["ingredients"][0]["concentration"]["unit"] = "MOLAR"
    elif mutation == "copied":
        after["ingredients"].append(before["ingredients"][0])
    else:
        after["solutions"][0]["notes"] = "All base concentrations are verified."
    for c in item["claims"]:
        if c["pointer"]:
            c["new"] = audit.get(after, c["pointer"][:-1]).get(c["pointer"][-1])
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


def fixture_repo(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for item in PLAN["records"] + repair.frozen()["dependencies"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "-C", str(tmp_path), "add", "data"], check=True)
    path = tmp_path / "plan.json"
    path.write_text(json.dumps(PLAN))
    return path


def test_apply_noop_verify(tmp_path):
    plan = fixture_repo(tmp_path)
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 3
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 3


def test_concurrent_edit_prevents_all_writes(tmp_path):
    plan = fixture_repo(tmp_path)
    target = tmp_path / PLAN["records"][-1]["path"]
    target.write_text(target.read_text() + "\n# concurrent edit\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    for item in PLAN["records"][:-1]:
        assert (tmp_path / item["path"]).read_text() == item["before_text"]


def test_dependency_drift_prevents_apply(tmp_path):
    plan = fixture_repo(tmp_path)
    target = tmp_path / repair.frozen()["dependencies"][1]["path"]
    target.write_text(target.read_text() + "\n# changed base\n")
    with pytest.raises(ValueError, match="Dependency drift"):
        repair.process(tmp_path, plan, "apply")


def test_symlink_target_refused(tmp_path):
    plan = fixture_repo(tmp_path)
    target = tmp_path / PLAN["records"][0]["path"]
    original = tmp_path / "saved.yaml"
    target.rename(original)
    target.symlink_to(original)
    with pytest.raises(ValueError, match="Symlink"):
        repair.process(tmp_path, plan, "apply")
