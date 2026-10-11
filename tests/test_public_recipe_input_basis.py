"""Offline source-context, transaction and scientific-scope guards for P7/P10."""

import copy
import html
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_public_recipe_input_basis as review  # noqa: E402

BASELINE = "f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f"


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.DEVNULL)


def auditor():
    spec = importlib.util.spec_from_file_location(
        "input_audit",
        ROOT / "reports/ingredient_concentration_curation/20261007-public-input-basis/audit.py",
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def fixture(tmp_path, monkeypatch):
    repo, cache = tmp_path / "repo", tmp_path / "sources"
    repo.mkdir()
    cache.mkdir()
    specs = copy.deepcopy(review.TARGETS)
    monkeypatch.setattr(review, "TARGETS", specs)
    snapshot = json.loads(review.SNAPSHOT.read_text())
    for mid, spec in specs.items():
        source = next(r for r in snapshot["records"] if r["medium_id"] == mid)

        def attrs(values):
            return " ".join(f'{k}="{html.escape(v)}"' for k, v in values.items())

        # Synthetic offline fixture, not represented as a retrieved HTML capture.
        page = '<script type="application/ld+json">' + json.dumps(source["dataset"]) + "</script>"
        page += "<p>we do not curate or test the media; no valid reference is given</p>"
        for table in source["recipe_tables"]:
            page += f'<div class="solution" id="{table["container_id"]}">'
            for control in table["main_volume_controls"]:
                page += f'<input {attrs(control)}><span class="input-group-text">ml</span>'
            for badge in table["volume_badges"]:
                page += f"<span {attrs(badge)}>1000</span>"
            page += '<table class="solution-table">'
            for index, row in enumerate(table["rows"]):
                tag = "td" if index else "th"
                page += (
                    f'<tr {attrs(row["attributes"])}>'
                    + "".join(f"<{tag}>{html.escape(c)}</{tag}>" for c in row["cells"])
                    + "</tr>"
                )
            page += "</table></div>"
        page += (
            "<table>"
            + "".join(
                "<tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in row["cells"]) + "</tr>"
                for row in source["metadata_rows"]
            )
            + "</table>"
        )
        (cache / f"{mid}-medium-page.html").write_text(page)
        spec["source_sha256"] = review.runner.sha(page.encode())
        path = repo / spec["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(git(ROOT, "show", f"{BASELINE}:{spec['path']}"))
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
    return repo, cache


def preview(fixture, tmp_path):
    repo, cache = fixture
    path = tmp_path / "plan.json"
    plan, result = review.process(repo, cache, path, "preview")
    assert result["changed"] == 0
    return path, plan


def test_preview_apply_verify_noop_whole_record_inverse(fixture, tmp_path):
    repo, cache = fixture
    path, plan = preview(fixture, tmp_path)
    for item in plan["records"]:
        before, after = (review.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
        counts = auditor().check(before, after, item)
        assert counts["new_evidence"] == (23 if item["medium_id"] == "P7" else 16)
        assert not review.runner.errors(after, "MediaRecipe")
        assert {c["field"] for c in review.runner.all_claims(before)} <= {
            c["field"] for c in item["claims"]
        }
    assert review.process(repo, cache, path, "apply")[1]["changed"] == 2
    assert review.process(repo, cache, path, "verify")[1]["already_applied"] == 2
    assert review.process(repo, cache, path, "apply")[1]["changed"] == 0
    review.shared.report(tmp_path / "reports", plan, True)
    for item in plan["records"]:
        report = (tmp_path / "reports/records" / (item["name"] + ".md")).read_text()
        assert [line for line in report.splitlines() if line.startswith("- Record:")] == [
            f"- Record: {item['path']}"
        ]
        assert report.count(" | applied |") == len(item["claims"])


@pytest.mark.parametrize("mid", ["P7", "P10"])
def test_source_byte_drift_refuses_whole_batch(fixture, tmp_path, mid):
    repo, cache = fixture
    path, _ = preview(fixture, tmp_path)
    source = cache / f"{mid}-medium-page.html"
    source.write_bytes(source.read_bytes() + b" ")
    with pytest.raises(ValueError, match="hash drift"):
        review.process(repo, cache, path, "apply")
    assert git(repo, "diff", "--name-only") == b""


@pytest.mark.parametrize(
    "mid,old,new",
    [
        ("P7", "1000", "1001"),
        ("P10", ">ml</span>", ">g</span>"),
        ("P7", "0.1% in H2O", "0.1% w/v in H2O"),
        ("P7", "10 mg in 100 ml H2O", "10 mg made up to 100 ml"),
        ("P7", "MgSO4 x 7 H2O", "MgSO4"),
        ("P7", "0.50", "0.60"),
        ("P10", "trace", "1 ml"),
        ("P10", "Pesar 0.05 g.", "Pesar 0.5 g."),
        ("P10", "Medir 1 litro", "Medir 2 litros"),
        ("P10", "Final volume of this solution", "Starting water volume"),
        ("P10", "Conc. [g/L]", "Amount [g]"),
        ("P7", "Lorenz", "Someone else"),
        ("P10", "29.08.24", "29.08.25"),
        ("P7", "we do not curate or test the media", "curated medium"),
        ("P10", 'id="sol-1"', 'id="sol-2"'),
        ("P7", '"value": "P7"', '"value": "P2"'),
    ],
)
def test_rehashed_scientific_drift_still_refused(fixture, mid, old, new):
    repo, cache = fixture
    source = cache / f"{mid}-medium-page.html"
    text = source.read_text()
    assert old in text
    text = text.replace(old, new)
    source.write_text(text)
    review.TARGETS[mid]["source_sha256"] = review.runner.sha(text.encode())
    with pytest.raises((ValueError, AssertionError)):
        review.sources(cache, mid)
    assert git(repo, "diff", "--name-only") == b""


@pytest.mark.parametrize("mid", ["P7", "P10"])
def test_concurrent_target_edit_refused(fixture, tmp_path, mid):
    repo, cache = fixture
    path, _ = preview(fixture, tmp_path)
    target = repo / review.TARGETS[mid]["path"]
    target.write_bytes(target.read_bytes() + b"\n# concurrent edit\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        review.process(repo, cache, path, "apply")
    other = "P10" if mid == "P7" else "P7"
    assert (
        review.runner.sha((repo / review.TARGETS[other]["path"]).read_bytes())
        == review.TARGETS[other]["before_sha256"]
    )


@pytest.mark.parametrize("change", ["id", "name", "ingredients", "solutions", "history"])
def test_semantic_identity_and_membership_guard(fixture, change):
    repo, cache = fixture
    before = review.runner.load_yaml((repo / review.TARGETS["P7"]["path"]).read_bytes())
    if change in {"id", "name"}:
        before[change] = "wrong"
    elif change in {"ingredients", "solutions"}:
        before[change].reverse()
    else:
        before["curation_history"][0]["curator"] = "wrong"
    with pytest.raises(ValueError, match="baseline semantics"):
        review.build(before, review.sources(cache, "P7"), "P7", "2026-10-07T00:00:00Z")


def test_tampered_plan_and_preview_overwrite_refused(fixture, tmp_path):
    repo, cache = fixture
    path, plan = preview(fixture, tmp_path)
    with pytest.raises(ValueError, match="overwrite"):
        review.process(repo, cache, path, "preview")
    plan["records"][0]["claims"][0]["snippet"] = "Invented quote"
    path.write_text(json.dumps(plan))
    with pytest.raises(ValueError, match="Frozen plan"):
        review.process(repo, cache, path, "apply")
    assert git(repo, "diff", "--name-only") == b""


def test_applied_frozen_plan_inverts_and_preserves_ids():
    plan = json.loads(
        (
            ROOT / "reports/ingredient_concentration_curation/20261007-public-input-basis/plan.json"
        ).read_text()
    )
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert review.runner.sha(raw) == item["after_sha256"]
        auditor().check(
            review.runner.load_yaml(item["before_text"]), review.runner.load_yaml(raw), item
        )
