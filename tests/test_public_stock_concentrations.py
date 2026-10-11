"""Offline source guards and whole-record invariants for P2/P8 curation."""

import copy
import html
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import review_public_stock_concentrations as review  # noqa: E402

BASELINE = "f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f"


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.DEVNULL)


def independent_auditor():
    spec = importlib.util.spec_from_file_location(
        "public_stock_audit",
        ROOT / "reports/ingredient_concentration_curation/20261007-public-stocks/audit.py",
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
    snapshot = json.loads(
        (
            ROOT
            / "reports/ingredient_concentration_curation/20261007-public-medium-source-pages.json"
        ).read_text()
    )
    for mid, spec in specs.items():
        source = next(r for r in snapshot["records"] if r["medium_id"] == mid)
        dataset = {
            "@type": "Dataset",
            "identifier": {"value": mid},
            "name": spec["title"],
            "url": review.BASE + mid,
        }
        # Synthetic offline HTML retains reviewed rows, not the appearance of a live capture.
        page = '<script type="application/ld+json">' + json.dumps(dataset) + "</script>"
        page += "<p>we do not curate or test the media; no valid reference is given</p>"
        for table in source["recipe_tables"]:
            page += f'<div class="solution" id="{table["container_id"]}">'
            if table["container_id"] == "sol-0":
                volume = "1000" if mid == "P2" else "6.1"
                page += f'<input id="main-sol-vol" value="{volume}" data-volume="{volume}"><span class="input-group-text">ml</span>'
            page += '<table class="solution-table">'
            for index, row in enumerate(table["rows"]):
                attrs = " ".join(f'{k}="{html.escape(v)}"' for k, v in row["attributes"].items())
                page += f"<tr {attrs}>"
                tag = "th" if index == 0 else "td"
                for ci, cell in enumerate(row["cells"]):
                    value = html.escape(cell)
                    if ci == 0:
                        for link in row["links"]:
                            value = f'<a href="{html.escape(link["href"])}">{value}</a>'
                    page += f"<{tag}>{value}</{tag}>"
                page += "</tr>"
            page += "</table></div>"
        page += "<table>"
        for row in source["metadata_rows"]:
            page += "<tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in row["cells"]) + "</tr>"
        page += "</table>"
        (cache / f"{mid}-medium-page.html").write_text(page)
        spec["source_sha256"] = review.runner.sha(page.encode())
        path = repo / spec["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(git(ROOT, "show", f"{BASELINE}:{spec['path']}"))
    # Fake PDF reader exercises identity, extraction and hash guards without a PDF dependency.
    method = "; ".join(
        [
            *[r[-1] for r in review.P8_DOSES],
            *[r[-1] for r in review.P8_COMPONENTS],
            "10 mL of M9-sinigrin medium",
            "SNG; Sinigrin hydrate",
        ]
    )
    texts = [""] * 42
    texts[0] = "hal-04370677v1 " + review.DOI.removeprefix("doi:")
    texts[1] = "A version published December 8th, 2022"
    texts[10] = method
    monkeypatch.setitem(
        sys.modules,
        "pypdf",
        SimpleNamespace(
            PdfReader=lambda path: SimpleNamespace(
                pages=[SimpleNamespace(extract_text=lambda t=t: t) for t in texts]
            )
        ),
    )
    (cache / review.PDF_FILE).write_bytes(b"synthetic offline PDF reader input")
    monkeypatch.setattr(
        review, "PDF_SHA", review.runner.sha((cache / review.PDF_FILE).read_bytes())
    )
    monkeypatch.setattr(review, "METHOD_SHA", review.runner.sha(method.encode()))
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
    return repo, cache, texts


def preview(fixture, tmp_path):
    repo, cache, _ = fixture
    path = tmp_path / "plan.json"
    plan, result = review.process(repo, cache, path, "preview")
    assert result["changed"] == 0
    return path, plan


def test_preview_apply_verify_noop_and_independent_diff(fixture, tmp_path):
    repo, cache, _ = fixture
    path, plan = preview(fixture, tmp_path)
    auditor = independent_auditor()
    for item in plan["records"]:
        before, after = (review.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
        counts = auditor.check(before, after, item)
        assert counts["new_evidence"] == (28 if item["medium_id"] == "P2" else 9)
        assert not review.runner.errors(after, "MediaRecipe")
        before_fields = {c["field"] for c in review.runner.all_claims(before)}
        assert before_fields <= {c["field"] for c in item["claims"]}
    assert review.process(repo, cache, path, "apply")[1]["changed"] == 2
    assert review.process(repo, cache, path, "verify")[1]["already_applied"] == 2
    git(
        repo,
        "-c",
        "user.name=Test",
        "-c",
        "user.email=test@example.org",
        "commit",
        "--allow-empty",
        "-qm",
        "unrelated",
    )
    assert review.process(repo, cache, path, "apply")[1]["changed"] == 0
    review.report(tmp_path / "reports", plan, True)
    for item in plan["records"]:
        text = (tmp_path / "reports/records" / (item["name"] + ".md")).read_text()
        assert [line for line in text.splitlines() if line.startswith("- Record:")] == [
            f"- Record: {item['path']}"
        ]
        assert text.count(" | applied |") == len(item["claims"])
        assert "Ingredient" in text and "DOI/PURL" in text


@pytest.mark.parametrize("mid", ["P2", "P8"])
def test_source_byte_drift_refused(fixture, tmp_path, mid):
    repo, cache, _ = fixture
    path, _ = preview(fixture, tmp_path)
    source = cache / f"{mid}-medium-page.html"
    source.write_bytes(source.read_bytes() + b" ")
    with pytest.raises(ValueError, match="hash drift"):
        review.process(repo, cache, path, "apply")
    assert git(repo, "diff", "--name-only") == b""


@pytest.mark.parametrize(
    "old,new",
    [
        ("1000", "999"),
        (">ml</span>", ">g</span>"),
        ("Compound", "Different header"),
        ("50 mg haemin", "50 g haemin"),
        ("make up to 100 ml", "add 100 ml"),
        ("192.00", "1920.0"),
        ("21.06.23", "21.06.24"),
        ("Taiyang Jin", "Other author"),
        ("we do not curate or test the media", "curated medium"),
        ("no valid reference is given", "reference supplied"),
        ('id="recipe-16"', 'id="recipe-14"'),
        ('id="sol-124"', 'id="sol-123"'),
        ("MgCl2 x 6 H2O", "MgCl2"),
        ('"value": "P2"', '"value": "P7"'),
    ],
)
def test_p2_semantic_drift_with_refreshed_test_hash(fixture, old, new):
    repo, cache, _ = fixture
    path = cache / "P2-medium-page.html"
    text = path.read_text()
    assert old in text
    text = text.replace(old, new)
    path.write_text(text)
    review.TARGETS["P2"]["source_sha256"] = review.runner.sha(text.encode())
    before = review.runner.load_yaml((repo / review.TARGETS["P2"]["path"]).read_bytes())
    with pytest.raises((ValueError, KeyError)):
        review.build(before, review.sources(cache, "P2"), "P2", "2026-10-07T00:00:00Z")


@pytest.mark.parametrize(
    "old,new",
    [("51.0", "15.0"), ("6.1", "10.0"), ("09.01.24", "09.01.25"), ('id="sol-NaN"', 'id="sol-2"')],
)
def test_p8_dataset_conflict_and_scale_guards(fixture, old, new):
    repo, cache, _ = fixture
    path = cache / "P8-medium-page.html"
    text = path.read_text().replace(old, new)
    path.write_text(text)
    review.TARGETS["P8"]["source_sha256"] = review.runner.sha(text.encode())
    before = review.runner.load_yaml((repo / review.TARGETS["P8"]["path"]).read_bytes())
    with pytest.raises(ValueError):
        review.build(before, review.sources(cache, "P8"), "P8", "2026-10-07T00:00:00Z")


@pytest.mark.parametrize("page", [0, 1, 10])
def test_pdf_identity_and_method_context(fixture, page):
    _, cache, texts = fixture
    texts[page] = "unreviewed manuscript content"
    with pytest.raises(ValueError):
        review.read_article(cache / review.PDF_FILE)


def test_pdf_bytes_guard(fixture):
    _, cache, _ = fixture
    path = cache / review.PDF_FILE
    path.write_bytes(b"other PDF")
    with pytest.raises(ValueError, match="hash drift"):
        review.read_article(path)


@pytest.mark.parametrize("mid", ["P2", "P8"])
@pytest.mark.parametrize("mutation", ["amount", "state", "variant", "stock_form"])
def test_unreviewed_local_changes(fixture, mid, mutation):
    repo, cache, _ = fixture
    before = review.runner.load_yaml((repo / review.TARGETS[mid]["path"]).read_bytes())
    if mutation == "amount":
        before["solutions"][0]["concentration"]["value"] = "999"
    elif mutation == "state":
        before["physical_state"] = "SOLID_AGAR" if mid == "P8" else "LIQUID"
    elif mutation == "variant":
        before["variants"] = [{"name": "unreviewed"}]
    else:
        before["solutions"][0]["composition"][0]["preferred_term"] = "different form"
    with pytest.raises(ValueError, match="formulation drift"):
        review.build(before, review.sources(cache, mid), mid, "2026-10-07T00:00:00Z")


@pytest.mark.parametrize(
    "part",
    [
        "before_text",
        "after_text",
        "after_sha256",
        "claims",
        "source_sha256",
        "path",
        "id",
        "medium_id",
    ],
)
def test_plan_tampering_even_after_apply(fixture, tmp_path, part):
    repo, cache, _ = fixture
    path, plan = preview(fixture, tmp_path)
    review.process(repo, cache, path, "apply")
    if part == "claims":
        plan["records"][0][part][0]["snippet"] = "fabricated"
    else:
        plan["records"][0][part] += "tampered"
    path.write_text(json.dumps(plan))
    with pytest.raises(ValueError):
        review.process(repo, cache, path, "verify")


def test_whole_batch_late_concurrent_edit(fixture, tmp_path, monkeypatch):
    repo, cache, _ = fixture
    path, _ = preview(fixture, tmp_path)
    first = repo / review.TARGETS["P2"]["path"]
    second = repo / review.TARGETS["P8"]["path"]
    before = first.read_bytes()
    reader = review.sources

    def changed(folder, mid):
        result = reader(folder, mid)
        if mid == "P8":
            second.write_bytes(second.read_bytes() + b"# concurrent edit\n")
        return result

    monkeypatch.setattr(review, "sources", changed)
    with pytest.raises(ValueError, match="Concurrent edit"):
        review.process(repo, cache, path, "apply")
    assert first.read_bytes() == before


def test_symlink_and_nonexact_path(fixture, tmp_path):
    repo, cache, _ = fixture
    path, _ = preview(fixture, tmp_path)
    target = repo / review.TARGETS["P2"]["path"]
    stored = target.with_suffix(".original")
    target.rename(stored)
    target.symlink_to(stored)
    with pytest.raises(ValueError, match="Symlink"):
        review.process(repo, cache, path, "apply")
    target.unlink()
    stored.rename(target)
    git(repo, "rm", "--cached", review.TARGETS["P2"]["path"])
    with pytest.raises(ValueError, match="non-exact"):
        review.process(repo, cache, path, "apply")


def test_independent_audit_rejects_unrelated_or_unsupported_edit(fixture, tmp_path):
    _, plan = preview(fixture, tmp_path)
    check = independent_auditor().check
    p2, p8 = plan["records"]
    before = review.runner.load_yaml(p2["before_text"])
    after = review.runner.load_yaml(p2["after_text"])
    after["solutions"][1]["composition"][2]["concentration"] = {"value": "0.100", "unit": "L"}
    with pytest.raises(AssertionError):
        check(before, after, p2)
    before = review.runner.load_yaml(p8["before_text"])
    after = review.runner.load_yaml(p8["after_text"])
    after["solutions"][0]["composition"][0]["term"]["id"] = "CHEBI:15377"
    with pytest.raises(AssertionError):
        check(before, after, p8)


def test_applied_frozen_plan_and_reports():
    folder = ROOT / "reports/ingredient_concentration_curation/20261007-public-stocks"
    plan = json.loads((folder / "plan.json").read_text())
    assert independent_auditor().audit()["new_evidence"] == 37
    for item in plan["records"]:
        assert (ROOT / item["path"]).read_text() == item["after_text"]
        text = (folder / "records" / (item["name"] + ".md")).read_text()
        assert text.count("- Record:") == 1
        assert f"- Record: {item['path']}" in text
        assert text.count(" | applied |") == len(item["claims"])
