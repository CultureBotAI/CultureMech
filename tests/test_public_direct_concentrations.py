"""Direct public recipes: source/formulation scope and evidence-only replay."""

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
import review_public_direct_concentrations as review  # noqa: E402

BASELINE = "f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f"


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.DEVNULL)


@pytest.fixture
def fixture(tmp_path, monkeypatch):
    cache, repo = tmp_path / "sources", tmp_path / "repo"
    cache.mkdir()
    repo.mkdir()
    targets = copy.deepcopy(review.TARGETS)
    monkeypatch.setattr(review, "TARGETS", targets)
    for mid, spec in targets.items():
        dataset = {
            "@type": "Dataset",
            "identifier": {"value": mid},
            "name": spec["title"],
            "url": review.BASE + mid,
        }
        rows = (
            "<tr>"
            + "".join(
                f"<th>{cell}</th>"
                for cell in ["Compound", "Amount", "Unit", "Conc. [g/L]", "Conc. [mM]"]
            )
            + "</tr>"
        )
        for i, row in enumerate(spec["rows"]):
            rows += f'<tr id="recipe-{i}"><td><a href="/ingredients/{row[-1]}">{html.escape(row[0])}</a></td>'
            rows += "".join(f"<td>{html.escape(c)}</td>" for c in row[1:-1]) + "</tr>"
        metadata = "".join(
            "<tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in row) + "</tr>"
            for row in [
                ["Creator:", spec["creator"]],
                ["Published:", spec["published"]],
                ["Last modified:", spec["published"]],
                ["Source:", "MediaDive: public"],
                ["Final pH:", "7.2"],
            ]
        )
        page = (
            '<html><script type="application/ld+json">' + json.dumps(dataset) + "</script>"
            '<div class="solution" id="sol-0"><input id="main-sol-vol" value="1000" data-volume="1000">'
            '<span class="input-group-text">ml</span><table class="solution-table">'
            + rows
            + "</table></div><table>"
            + metadata
            + "</table></html>"
        ).replace("K2HPO4", "K<sub>2</sub>HPO<sub>4</sub>")
        (cache / f"{mid}-medium-page.html").write_text(page)
        spec["source_sha256"] = review.runner.sha(page.encode())
        path = repo / spec["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(git(ROOT, "show", f"{BASELINE}:{spec['path']}"))
        assert review.runner.sha(path.read_bytes()) == spec["before_sha256"]
    # Synthetic offline parser fixtures are not represented as live source captures.
    base = ", ".join(review.ARTICLE_QUOTES)
    monkeypatch.setattr(review, "ARTICLE_BASE_SHA", review.runner.sha(base.encode()))
    article = (
        "".join(
            f'<meta name="citation_{key}" content="{html.escape(value)}">'
            for key, value in [
                ("doi", review.ARTICLE.removeprefix("doi:")),
                ("title", review.TITLE),
                *[("author", a) for a in review.AUTHORS],
                ("publication_date", "2020 Sep 4"),
            ]
        )
        + f'<section id="{review.SECTION}"><p>Intro. Three medias were tested, mTA10 ('
        + base
        + "), mTA10 replacing the KH2PO4 and Na2HPO4 by MOPS (separate variant).</p></section>"
    )
    correction = '<meta name="citation_doi" content="10.3390/microorganisms9071482"><p>There is a mistake in the primer sequences provided in Table 2</p>'
    hashes = {}
    for name, text in zip(review.ARTICLE_HASHES, (article, correction), strict=True):
        (cache / name).write_text(text)
        hashes[name] = review.runner.sha(text.encode())
    monkeypatch.setattr(review, "ARTICLE_HASHES", hashes)
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


def preview(repo, cache):
    items = [
        {**{k: s[k] for k in ("path", "id", "name", "before_sha256")}, "medium_id": mid}
        for mid, s in review.TARGETS.items()
    ]
    plan = review.runner.preview(repo, items, cache, BASELINE, adapter=review.adapter())
    for item in plan["records"]:
        item["before_text"] = (repo / item["path"]).read_text()
    review.rebuild(plan, cache)
    return plan


def assert_evidence_only(before, after, mid):
    restored = copy.deepcopy(after)
    expected_count = 2 if mid == "P6" else 1
    for old, new in zip(before["ingredients"], restored["ingredients"], strict=True):
        assert len(new["evidence"]) == expected_count
        for entry in new["evidence"]:
            assert entry["supports"] == "SUPPORT" and entry["snippet"]
            assert "concentration" in entry["explanation"]
        del new["evidence"]
        assert new == old
    assert restored["references"][:-expected_count] == before["references"]
    del restored["references"][-expected_count:]
    event = restored["curation_history"].pop()
    assert event["curator"] == "codex" and event["action"] == review.ACTION
    assert restored == before


def test_preview_apply_readback_noop_and_unrelated_commit(fixture, tmp_path):
    repo, cache = fixture
    plan = preview(repo, cache)
    assert review.runner.summary(plan)["claims"] == {"evidence_only": 17}
    assert all(not r["failure"] and not r["post_errors"] for r in plan["records"])
    review.runner.apply(repo, plan, cache, adapter=review.adapter())
    review.rebuild(plan, cache)
    outcome = review.runner.verify(repo, plan, cache, adapter=review.adapter())
    assert outcome == {"checked_record_hashes": 2, "verified_new_snippets": 17}
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
    assert review.runner.apply(repo, plan, cache, adapter=review.adapter()) == {
        "changed": 0,
        "already_applied": 2,
    }
    review.reports(tmp_path / "reports", plan, True)
    for item in plan["records"]:
        after = review.runner.load_yaml((repo / item["path"]).read_bytes())
        assert_evidence_only(review.runner.load_yaml(item["before_text"]), after, item["medium_id"])
        report = (tmp_path / "reports/records" / (item["name"] + ".md")).read_text()
        assert [line for line in report.splitlines() if line.startswith("- Record:")] == [
            f"- Record: {item['path']}"
        ]
        assert report.count(" | applied |") == len(item["claims"])
        refs = after["references"][-(2 if item["medium_id"] == "P6" else 1) :]
        assert all(all(k in r for k in ("title", "authors", "year", "notes")) for r in refs)
    king = review.runner.load_yaml((repo / review.TARGETS["P3"]["path"]).read_bytes())
    assert king["ingredients"][3]["concentration"] == {"value": "10", "unit": "ML_PER_L"}


@pytest.mark.parametrize(
    "old,new",
    [
        ("1000", "900"),
        (">ml</span>", ">g</span>"),
        ("Conc. [g/L]", "Conc. [mg/L]"),
        ("1.5", "15"),
        ("MgSO4 x 7 H2O", "MgSO4"),
        ("Proteose peptone no. 3", "Peptone"),
        ("/ingredients/72", "/ingredients/43"),
        (">ml</td>", ">g</td>"),
        ("21.06.23", "22.06.23"),
        ("MediaDive: public", "DSMZ"),
        ("Perrine Portier", "Different creator"),
        ('"value": "P3"', '"value": "P4"'),
        ('id="sol-0"', 'id="sol-1"'),
        ('id="recipe-0"', 'id="recipe-4"'),
    ],
)
def test_source_semantic_drift_even_if_capture_hash_is_refreshed(fixture, old, new):
    _, cache = fixture
    path = cache / "P3-medium-page.html"
    raw = path.read_text()
    assert old in raw
    raw = raw.replace(old, new)
    path.write_text(raw)
    review.TARGETS["P3"]["source_sha256"] = review.runner.sha(raw.encode())
    with pytest.raises((ValueError, KeyError)):
        review.read_sources(cache, "P3")


@pytest.mark.parametrize("change", ["extra", "missing", "duplicate", "stock", "steps"])
def test_table_membership_drift(fixture, change):
    _, cache = fixture
    path = cache / "P3-medium-page.html"
    raw = path.read_text()
    if change == "stock":
        raw = raw.replace(
            "</html>",
            '<div class="solution" id="sol-1"><table class="solution-table"></table></div></html>',
        )
    elif change == "steps":
        raw = raw.replace("</table></div>", "<tr><td>Add a supplement.</td></tr></table></div>")
    else:
        start = raw.index('<tr id="recipe-4"')
        stop = raw.index("</tr>", start) + len("</tr>")
        row = raw[start:stop]
        raw = (
            raw[:start]
            + (
                {
                    "missing": "",
                    "duplicate": row + row,
                    "extra": row + row.replace("Agar", "Glucose"),
                }[change]
            )
            + raw[stop:]
        )
    with pytest.raises(ValueError):
        review.inspect_page(raw, "P3")


@pytest.mark.parametrize(
    "old,new",
    [
        ("10.3390/microorganisms8091359", "10.3390/microorganisms9071482"),
        ("2020 Sep 4", "2021 Sep 4"),
        ("Sarah Azinheiro", "Different author"),
        ("10 g/L Tryptose", "10 mg/L Tryptose"),
        ("Na2HPO4", "Na2HPO4 x 12 H2O"),
        ("Three medias were tested, mTA10 (", "Only supplemented mTA10 ("),
        ("), mTA10 replacing", "), mTA10 also containing"),
        ("19.3 g/L Na2HPO4)", "19.3 g/L Na2HPO4, 5 g/L Glucose)"),
    ],
)
def test_article_scope_drift(fixture, old, new):
    _, cache = fixture
    path = cache / "P6-article-PMC7564587.html"
    raw = path.read_text()
    assert old in raw
    raw = raw.replace(old, new)
    path.write_text(raw)
    review.ARTICLE_HASHES[path.name] = review.runner.sha(raw.encode())
    with pytest.raises(ValueError):
        review.read_sources(cache, "P6")


@pytest.mark.parametrize(
    "name", ["P3-medium-page.html", "P6-article-PMC7564587.html", "P6-correction-PMC8306464.html"]
)
def test_capture_byte_drift(fixture, name):
    _, cache = fixture
    path = cache / name
    path.write_text(path.read_text() + " ")
    with pytest.raises(ValueError, match="hash drift"):
        review.read_sources(cache, name[:2])


@pytest.mark.parametrize("field", ["value", "unit", "identity", "ordering", "variant", "solution"])
def test_local_formulation_drift(fixture, field):
    repo, cache = fixture
    doc = review.runner.load_yaml((repo / review.TARGETS["P3"]["path"]).read_bytes())
    if field in {"value", "unit"}:
        doc["ingredients"][3]["concentration"][field] = "wrong"
    elif field == "identity":
        doc["ingredients"][0]["preferred_term"] = "KH2PO4"
    elif field == "ordering":
        doc["ingredients"].reverse()
    else:
        doc["variants" if field == "variant" else "solutions"] = [{"name": "unreviewed"}]
    raw, meta = review.read_sources(cache, "P3")
    with pytest.raises(ValueError):
        review.review(doc, raw, meta, "2026-10-07T00:00:00Z")


@pytest.mark.parametrize("field", ["claim", "hash", "source", "before", "path", "set"])
def test_frozen_plan_tampering(fixture, field):
    repo, cache = fixture
    plan = preview(repo, cache)
    item = plan["records"][0]
    if field == "claim":
        item["claims"][0]["snippet"] = "Invented quotation"
    elif field == "hash":
        item["after_sha256"] = "0" * 64
    elif field == "source":
        item["source_sha256"] = "0" * 64
    elif field == "before":
        item["before_text"] += "# unreviewed\n"
    elif field == "path":
        item["path"] = item["path"].upper()
    else:
        plan["records"].pop()
    with pytest.raises(ValueError):
        review.rebuild(plan, cache)


def test_late_target_concurrent_edit_does_not_partially_apply(fixture):
    repo, cache = fixture
    plan = preview(repo, cache)
    first, last = [repo / r["path"] for r in plan["records"]]
    before = first.read_bytes()
    last.write_text(last.read_text() + "# concurrent user change\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        review.runner.apply(repo, plan, cache, adapter=review.adapter())
    assert first.read_bytes() == before


def test_symlink_and_case_mismatch_refused(fixture):
    repo, cache = fixture
    plan = preview(repo, cache)
    path = repo / plan["records"][1]["path"]
    target = repo / "elsewhere.yaml"
    path.rename(target)
    path.symlink_to(target)
    with pytest.raises(ValueError, match="Symlink"):
        review.runner.apply(repo, plan, cache, adapter=review.adapter())
    plan["records"][1]["path"] = plan["records"][1]["path"].upper()
    with pytest.raises(ValueError, match="Non-authoritative or non-exact"):
        review.runner.apply(repo, plan, cache, adapter=review.adapter())


def test_actual_applied_records_reports_and_independent_diff():
    here = ROOT / "reports/ingredient_concentration_curation/20261007-public-direct"
    spec = importlib.util.spec_from_file_location("public_direct_audit", here / "audit.py")
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    assert audit.audit() == {
        "edited_records": 2,
        "new_evidence": 17,
        "new_references": 3,
        "new_curation_history": 2,
    }
    plan = json.loads((here / "plan.json").read_text())
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert review.runner.sha(raw) == item["after_sha256"]
        assert_evidence_only(
            review.runner.load_yaml(item["before_text"]),
            review.runner.load_yaml(raw),
            item["medium_id"],
        )
        report = (here / "records" / (item["name"] + ".md")).read_text()
        assert [line for line in report.splitlines() if line.startswith("- Record:")] == [
            f"- Record: {item['path']}"
        ]
        assert report.count(" | applied |") == len(item["claims"])
