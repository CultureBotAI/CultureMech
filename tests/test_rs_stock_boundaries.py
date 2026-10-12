"""Offline scientific-scope and guarded-transaction tests for the P4/P5 repair."""

import copy
import html
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261007-rs-stock-boundaries"
sys.path.insert(0, str(ROOT / "scripts"))
import repair_rs_stock_boundaries as review  # noqa: E402

BASELINE = "f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f"


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.DEVNULL)


def auditor():
    spec = importlib.util.spec_from_file_location("rs_audit", HERE / "audit.py")
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

        # Synthetic offline HTML, not a purported retrieval from MediaDive.
        page = '<script type="application/ld+json">' + json.dumps(source["dataset"]) + "</script>"
        page += "<p>we do not curate or test the media; no valid reference is given</p>"
        for table in source["recipe_tables"]:
            page += f'<div class="solution" id="{table["container_id"]}">'
            for control in table["main_volume_controls"]:
                page += f'<input {attrs(control)}><span class="input-group-text">ml</span>'
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
        figure = b"synthetic test figure " + mid.encode()
        (cache / f"{mid}-preparation-figure.png").write_bytes(figure)
        spec["figure_sha256"] = review.runner.sha(figure)
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


def test_preview_apply_verify_noop_and_independent_arithmetic(fixture, tmp_path):
    repo, cache = fixture
    path, plan = preview(fixture, tmp_path)
    for item in plan["records"]:
        before, after = (review.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
        counts = auditor().check(before, after, item)
        assert counts["new_evidence"] == (57 if item["medium_id"] == "P4" else 98)
        assert not review.runner.errors(after, "MediaRecipe")
        assert {c["field"] for c in review.runner.all_claims(before)} <= {
            c["old_field"] for c in item["claims"]
        }
        assert {c["field"] for c in review.runner.all_claims(after)} <= {
            c["field"] for c in item["claims"]
        }
    assert review.process(repo, cache, path, "apply")[1]["changed"] == 2
    assert review.process(repo, cache, path, "verify")[1]["already_applied"] == 2
    assert review.process(repo, cache, path, "apply")[1]["changed"] == 0
    review.report(tmp_path / "reports", plan, True)
    for item in plan["records"]:
        report = (tmp_path / "reports/records" / (item["name"] + ".md")).read_text()
        assert [line for line in report.splitlines() if line.startswith("- Record:")] == [
            f"- Record: {item['path']}"
        ]
        assert report.count(" | applied |") == len(item["claims"])
        for claim in item["claims"]:
            for quote in [claim, *claim["extra_excerpts"]]:
                assert quote["snippet"].replace("|", "\\|") in report
                assert quote["locator"] in report


@pytest.mark.parametrize("mid", ["P4", "P5"])
@pytest.mark.parametrize("suffix", ["medium-page.html", "preparation-figure.png"])
def test_source_byte_drift_refuses_whole_batch(fixture, tmp_path, mid, suffix):
    repo, cache = fixture
    path, _ = preview(fixture, tmp_path)
    source = cache / f"{mid}-{suffix}"
    source.write_bytes(source.read_bytes() + b" ")
    with pytest.raises(ValueError, match="hash drift|figure drift"):
        review.process(repo, cache, path, "apply")
    assert git(repo, "diff", "--name-only") == b""


@pytest.mark.parametrize(
    "mid,old,new",
    [
        ("P4", "0.5g/mL", "0.6g/mL"),
        ("P4", "MgCl2 x 6 H2O", "MgCl2"),
        ("P4", "1:1000000", "1:100000"),
        ("P4", "10-15% TiCl3 basis", "10-15% w/v"),
        ("P4", "total volume of 1 liter", "1 liter of starting water"),
        ("P5", "L-mannose", "D-mannose"),
        ("P5", "Xylan", "D-Xylose"),
        ("P5", "g/50ml", "g/150ml"),
        ("P5", "1.26 g/mL", "1.00 g/mL"),
        ("P5", "4.5 \u00b5l", "4.5 ml"),
        ("P5", "Single stock in NNM.", "Single stock in H2O."),
        ("P5", "Fill to 50 ml", "Fill to 150 ml"),
        ("P5", "Fill to 150 ml", "Add 150 ml"),
        ("P5", 'value="150"', 'value="1000"'),
        ("P4", ">ml</span>", ">g</span>"),
        ("P4", "we do not curate or test the media", "curated medium"),
        ("P4", "Cristiana Sigona", "Someone else"),
        ("P5", "07.10.25", "08.10.25"),
        ("P4", '"value": "P4"', '"value": "P5"'),
    ],
)
def test_rehashed_scientific_source_drift_refused(fixture, mid, old, new):
    repo, cache = fixture
    source = cache / f"{mid}-medium-page.html"
    text = source.read_text()
    assert old in text
    text = text.replace(old, new)
    source.write_text(text)
    review.TARGETS[mid]["source_sha256"] = review.runner.sha(text.encode())
    with pytest.raises(ValueError):
        review.sources(cache, mid)
    assert git(repo, "diff", "--name-only") == b""


@pytest.mark.parametrize("mid", ["P4", "P5"])
def test_concurrent_target_edit_refuses_whole_batch(fixture, tmp_path, mid):
    repo, cache = fixture
    path, _ = preview(fixture, tmp_path)
    target = repo / review.TARGETS[mid]["path"]
    target.write_bytes(target.read_bytes() + b"\n# concurrent edit\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        review.process(repo, cache, path, "apply")
    other = "P5" if mid == "P4" else "P4"
    assert (
        review.runner.sha((repo / review.TARGETS[other]["path"]).read_bytes())
        == review.TARGETS[other]["before_sha256"]
    )


@pytest.mark.parametrize(
    "mid,change", [("P4", "id"), ("P4", "ingredients"), ("P5", "solutions"), ("P5", "history")]
)
def test_semantic_identity_membership_history_guard(fixture, mid, change):
    repo, cache = fixture
    before = review.runner.load_yaml((repo / review.TARGETS[mid]["path"]).read_bytes())
    if change == "id":
        before[change] = "CultureMech:000001"
    elif change in {"ingredients", "solutions"}:
        before[change].reverse()
    else:
        before["curation_history"][0]["curator"] = "wrong"
    with pytest.raises(ValueError, match="formulation drift"):
        review.build(before, review.sources(cache, mid), mid, "2026-10-07T00:00:00Z")


def test_tampered_plan_and_preview_overwrite_refused(fixture, tmp_path):
    repo, cache = fixture
    path, plan = preview(fixture, tmp_path)
    with pytest.raises(ValueError, match="overwrite"):
        review.process(repo, cache, path, "preview")
    plan["records"][0]["claims"][0]["extra_excerpts"][0]["snippet"] = "Invented quote"
    path.write_text(json.dumps(plan))
    with pytest.raises(ValueError, match="Frozen plan"):
        review.process(repo, cache, path, "apply")
    assert git(repo, "diff", "--name-only") == b""


@pytest.mark.parametrize("kind", ["symlink", "untracked", "case"])
def test_exact_tracked_path_and_symlink_guard(fixture, tmp_path, kind):
    repo, cache = fixture
    spec = review.TARGETS["P4"]
    target = repo / spec["path"]
    if kind == "symlink":
        other = target.with_suffix(".backup")
        target.rename(other)
        target.symlink_to(other.name)
    elif kind == "untracked":
        git(repo, "rm", "--cached", spec["path"])
    else:
        spec["path"] = spec["path"].replace("rs_medium_", "RS_medium_", 1)
    with pytest.raises((ValueError, FileNotFoundError)):
        review.process(repo, cache, tmp_path / "plan.json", "preview")


@pytest.mark.parametrize(
    "mid,kind",
    [
        ("P4", "stock_strength"),
        ("P4", "dose"),
        ("P4", "water_amount"),
        ("P4", "ti_strength"),
        ("P4", "chemical_id"),
        ("P5", "carrier"),
        ("P5", "mix_basis"),
        ("P5", "conflict_amount"),
        ("P5", "mem_solvent"),
        ("P5", "duplicate_solute"),
        ("P5", "old_history"),
    ],
)
def test_independent_audit_rejects_scientific_drift_even_with_updated_claims(mid, kind):
    item = next(
        i for i in json.loads((HERE / "plan.json").read_text())["records"] if i["medium_id"] == mid
    )
    before, after = (review.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    if kind == "stock_strength":
        after["solutions"][0]["composition"][0]["concentration"]["value"] = "1"
    elif kind == "dose":
        after["solutions"][0]["concentration"]["value"] = "2.1"
    elif kind == "water_amount":
        after["ingredients"][-1]["concentration"] = {"value": "1", "unit": "L"}
    elif kind == "ti_strength":
        after["solutions"][-1]["composition"][0]["concentration"] = {
            "value": "10",
            "unit": "PERCENT_W_V",
        }
    elif kind == "chemical_id":
        after["ingredients"][0]["term"]["id"] = "CHEBI:15377"
    elif kind == "carrier":
        after["solutions"][0]["solutions"][2]["composition"][1]["culturemech_term"][
            "id"
        ] = "CultureMech:010435"
    elif kind == "mix_basis":
        after["solutions"][0]["concentration"]["unit"] = "ML_PER_L"
    elif kind == "conflict_amount":
        after["solutions"][4]["composition"][1]["concentration"] = {
            "value": "3.59568",
            "unit": "G_PER_L",
        }
    elif kind == "mem_solvent":
        after["solutions"][3]["solutions"][0]["composition"].append({"preferred_term": "Water"})
    elif kind == "duplicate_solute":
        node = after["solutions"][0]["solutions"][0]["composition"][0]
        after["solutions"][0]["composition"].append(copy.deepcopy(node))
    else:
        after["curation_history"][0]["curator"] = "wrong"
    for c in item["claims"]:
        c["new"] = copy.deepcopy(auditor().get(after, c["pointer"]))
    with pytest.raises(AssertionError):
        auditor().check(before, after, item)


def test_applied_frozen_plan_inverts_preserving_scientific_history():
    for item in json.loads((HERE / "plan.json").read_text())["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert review.runner.sha(raw) == item["after_sha256"]
        auditor().check(
            review.runner.load_yaml(item["before_text"]), review.runner.load_yaml(raw), item
        )
