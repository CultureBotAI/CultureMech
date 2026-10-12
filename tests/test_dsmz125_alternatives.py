"""Guarded, source-pinned review of medium 125's alternative preparations."""

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz125-alternatives"
sys.path.insert(0, str(ROOT / "scripts"))
import repair_dsmz125_alternatives as repair  # noqa: E402


def frozen():
    return json.loads((HERE / "plan.json").read_text())


def auditor():
    spec = importlib.util.spec_from_file_location("dsmz125_audit", HERE / "audit.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.DEVNULL)


@pytest.fixture
def fixture(tmp_path, monkeypatch):
    plan = frozen()
    repo, medium, solution = (tmp_path / name for name in ("repo", "medium", "solution"))
    for folder in (repo, medium, solution):
        folder.mkdir()
    for ref, cache, sid in ((repair.MEDIUM, medium, "125"), (repair.SOLUTION, solution, "223")):
        (cache / (sid + ".json")).write_text(plan["sources"][ref]["raw"])
        (cache / (sid + ".metadata.json")).write_text(json.dumps(plan["sources"][ref]["metadata"]))
    # Synthetic wrapper around the captured row exercises the mapping parser.
    headers = ["ID", "Name", "PH Info", "Is Complex", "Is Aerobic", "Is SubMedium", "Instructions"]
    html = (
        "<table><tr>"
        + "".join("<td>" + h + "</td>" for h in headers)
        + "</tr>"
        + plan["sources"]["mapping"]["snippet"]
        + "</table>"
    )
    mapping = tmp_path / "mapping.html"
    mapping.write_text(html)
    metadata = copy.deepcopy(repair.MAPPING_META)
    metadata["sha256"] = repair.runner.sha(html.encode())
    monkeypatch.setattr(repair, "MAPPING_META", metadata)
    for item in plan["records"]:
        path = repo / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    git(repo, "init", "-q")
    git(repo, "add", "data")
    git(
        repo,
        "-c",
        "user.name=Test",
        "-c",
        "user.email=test@example.org",
        "commit",
        "-qm",
        "baseline",
    )
    return repo, medium, solution, mapping


def preview(fixture, tmp_path):
    path = tmp_path / "plan.json"
    plan, result = repair.process(*fixture, path, "preview")
    assert result["changed"] == 0 and result["scoped_claims"] == 48
    return path, plan


def test_preview_apply_verify_idempotence_and_inversion(fixture, tmp_path):
    path, plan = preview(fixture, tmp_path)
    counts = []
    for item in plan["records"]:
        before, after = [
            repair.runner.load_yaml(item[key]) for key in ("before_text", "after_text")
        ]
        counts.append(auditor().check(before, after, item, plan["sources"]))
        assert not repair.runner.errors(after, item["target_class"])
        field = "composition" if item["key"] == "solution" else "ingredients"
        assert [n["preferred_term"] for n in after[field]] == [r[0] for r in repair.ROWS]
        assert all(n["preferred_term"].lower() not in {"methanol", "methane"} for n in after[field])
    assert sum(c["new_evidence"] for c in counts) == 23
    assert repair.process(*fixture, path, "apply")[1]["changed"] == 3
    assert repair.process(*fixture, path, "verify")[1]["already_applied"] == 3
    assert repair.process(*fixture, path, "apply")[1]["changed"] == 0


@pytest.mark.parametrize(
    "damage",
    [
        "water",
        "basal",
        "ratio",
        "combined",
        "missing_option",
        "snippet",
        "mapping",
        "history",
        "link",
    ],
)
def test_independent_auditor_rejects_semantic_or_provenance_damage(damage):
    plan = frozen()
    item = plan["records"][0]
    before, after = [repair.runner.load_yaml(item[key]) for key in ("before_text", "after_text")]
    if damage == "water":
        after["ingredients"][-1]["concentration"]["unit"] = "PERCENT_V_V"
    elif damage == "basal":
        after["ingredients"].append(
            {"preferred_term": "Methanol", "concentration": {"value": "5", "unit": "ML_PER_L"}}
        )
    elif damage == "ratio":
        after["variants"][1]["modifications"][0] = "Incubate under methane-air (1:4)."
    elif damage == "combined":
        after["variants"][0]["modifications"][
            0
        ] = "Add 5 ml methanol and incubate under methane-air (4:1)."
    elif damage == "missing_option":
        after["variants"].pop()
    elif damage == "snippet":
        after["ingredients"][0]["evidence"][0]["snippet"] = "unsupported"
    elif damage == "mapping":
        after["ingredients"][0]["term"]["id"] = "CHEBI:15377"
    elif damage == "history":
        after["curation_history"].pop(0)
    else:
        after["variant_children"][0]["id"] = "CultureMech:999999"
    with pytest.raises(AssertionError):
        auditor().check(before, after, item, plan["sources"])


@pytest.mark.parametrize("damage", ["target", "source", "plan", "symlink", "untracked"])
def test_whole_batch_refuses_drift_before_any_write(fixture, tmp_path, damage):
    plan_path, plan = preview(fixture, tmp_path)
    repo, medium, _, _ = fixture
    last = repo / plan["records"][-1]["path"]
    if damage == "target":
        last.write_text(last.read_text() + "# concurrent edit\n")
    elif damage == "source":
        (medium / "125.json").write_text("{}")
    elif damage == "plan":
        plan["records"][0]["after_sha256"] = "0" * 64
        plan_path.write_text(json.dumps(plan))
    elif damage == "symlink":
        backup = tmp_path / "linked.yaml"
        last.rename(backup)
        last.symlink_to(backup)
    else:
        git(repo, "rm", "--cached", "--", plan["records"][-1]["path"])
    baseline = {r["path"]: (repo / r["path"]).read_bytes() for r in plan["records"]}
    with pytest.raises((ValueError, KeyError)):
        repair.process(*fixture, plan_path, "apply")
    assert {p: (repo / p).read_bytes() for p in baseline} == baseline


@pytest.mark.parametrize("damage", ["and", "water", "hydrate", "condition", "mapping"])
def test_rehashed_source_semantics_still_need_review(monkeypatch, damage):
    sources = copy.deepcopy(frozen()["sources"])
    if damage == "mapping":
        sources["mapping"]["cells"][0] = "125_23675"
    else:
        data = json.loads(sources[repair.MEDIUM]["raw"])
        main = data["data"]["solutions"][0]
        if damage == "and":
            main["steps"][0]["step"] = repair.STEP.replace(" or ", " and ")
        elif damage == "water":
            main["recipe"][-1]["amount"] = 995
        elif damage == "hydrate":
            main["recipe"][1]["compound"] = "MgSO4"
        else:
            main["recipe"][0]["condition"] = "optional"
        raw = json.dumps(data)
        sources[repair.MEDIUM]["raw"] = raw
        sources[repair.MEDIUM]["metadata"]["sha256"] = repair.runner.sha(raw.encode())
        monkeypatch.setitem(repair.HASHES, repair.MEDIUM, repair.runner.sha(raw.encode()))
    with pytest.raises(ValueError):
        repair.check_sources(sources)


def test_applied_records_match_plan_and_keep_prior_evidence():
    plan = frozen()
    for item in plan["records"]:
        current = (ROOT / item["path"]).read_bytes()
        assert repair.runner.sha(current) == item["after_sha256"]
        assert current.decode() == item["after_text"]
        auditor().check(
            repair.runner.load_yaml(item["before_text"]),
            repair.runner.load_yaml(current),
            item,
            plan["sources"],
        )
