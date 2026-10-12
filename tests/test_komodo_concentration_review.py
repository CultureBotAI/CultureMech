"""Exact mapping, variant boundaries, source provenance and guarded writes."""

import copy
import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import inventory_komodo_concentration_sources as inventory
import review_komodo_concentration_evidence as komodo
import review_solution_concentration_evidence as runner

from tests.test_medium_concentration_batch import AUDIT, FOLLOWUPS
from tests.test_medium_concentration_review import capture, sample, withholding  # noqa: F401


def table(sid="1", name="Example"):
    link = "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1.pdf"
    header = (
        "<tr>"
        + "".join(
            f"<td>{s}</td>"
            for s in (
                "ID",
                "Name",
                "PH Info",
                "Is Complex",
                "Is Aerobic",
                "Is SubMedium",
                "Instructions",
            )
        )
        + "</tr>"
    )
    row = (
        f"<TR><TD><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo={sid}'>{sid}</a></TD>"
        f"<TD>{name}</TD><TD>7.0</TD><TD>false</TD><TD>false</TD><TD>false</TD>"
        f"<TD><a href='{link}'>{link}</a></TD></TR>"
    )
    return f"<table><tr><td>Layout</td></tr>{header}\n{row}</table>"


def mapping(tmp_path, raw):
    path = tmp_path / "mapping.html"
    path.write_text(raw)
    meta = {
        "reference": inventory.MAPPING_URL,
        "sha256": runner.sha(raw.encode()),
        "http_status": 200,
        "accessed_at": "2026-10-07T08:00:00+00:00",
    }
    return path, meta, inventory.read_mapping(path, meta)


@pytest.fixture
def case(tmp_path, sample):  # noqa: F811
    doc, data = sample
    doc["media_term"]["term"]["id"] = "komodo.medium:1"
    path, meta, rows = mapping(tmp_path, table())
    item = {
        "path": "data/normalized_yaml/bacterial/example.yaml",
        "id": doc["id"],
        "name": doc["original_name"],
        "komodo_id": "1",
        "medium_id": "1",
        "mapping": rows["1"],
        "exact_base_accession": True,
        "exact_mapping_name": True,
        "variant_relationship": None,
    }
    return doc, data, item, path, meta


def review(case, decisions=()):
    doc, data, item, _, meta = case
    raw, source_meta = capture(data)
    return komodo.review(
        doc,
        raw,
        source_meta,
        "2026-10-07T08:01:00+00:00",
        records={item["id"]: item},
        metadata=meta,
        withholdings=decisions,
    )


def test_mapping_is_identity_evidence_not_amount_evidence(case):
    doc, data, item, path, metadata = case
    before = copy.deepcopy(doc)
    after, claims = review(case)
    assert doc == before
    assert claims[0]["status"] == "evidence_only"
    assert claims[0]["snippet"] in capture(data)[0]
    assert after["evidence"] == [komodo.mapping_evidence(item, metadata)]
    assert after["evidence"][0]["snippet"] in path.read_text()
    assert after["ingredients"][0]["evidence"][0]["reference"] != inventory.MAPPING_URL
    assert "Source identity only" in after["evidence"][0]["explanation"]
    assert after["references"][-1] == komodo.mapping_reference(metadata)
    assert "discovery_mode=cross_reference" in after["references"][0]["notes"]
    assert after["curation_history"][-1]["action"] == komodo.ACTION
    assert not runner.errors(after, "MediaRecipe")
    for key in ("id", "original_name", "media_term", "notes", "physical_state"):
        assert after[key] == doc[key]


def test_captured_mapping_title_is_source_pinned_and_decoded(tmp_path):
    path, metadata, _ = mapping(tmp_path, "<title> Known &amp; Media\n Database </title>" + table())
    assert komodo.captured_mapping_title(path, metadata) == "Known & Media Database"
    plan = {"mapping_source": metadata, "mapping_title": "Known & Media Database"}
    komodo.check_mapping_title(path, plan)
    plan["mapping_title"] = "Invented title"
    with pytest.raises(ValueError, match="Frozen mapping title"):
        komodo.check_mapping_title(path, plan)
    path.write_text(path.read_text().replace("Known", "Changed"))
    with pytest.raises(ValueError):
        komodo.captured_mapping_title(path, metadata)


@pytest.mark.parametrize(
    "markup",
    [
        "",
        "<title> </title>",
        "<title>A</title><title>B</title>",
        "<title>Open",
        "</title>",
    ],
)
def test_missing_or_malformed_mapping_titles_are_not_invented(tmp_path, markup):
    path, metadata, _ = mapping(tmp_path, table() + markup)
    with pytest.raises(ValueError):
        komodo.captured_mapping_title(path, metadata)


def test_explicit_mapping_title_preserves_legacy_reproduction(case):
    doc, data, item, path, metadata = case
    old, claims = review(case)
    raw, source_meta = capture(data)
    new, new_claims = komodo.review(
        doc,
        raw,
        source_meta,
        "2026-10-07T08:01:00+00:00",
        records={item["id"]: item},
        metadata=metadata,
        mapping_title="Actual source title",
    )
    assert new_claims == claims
    assert new["references"][-1]["title"] == "Actual source title"
    assert old["references"][-1]["title"] == "KOMODO media list: original-recipe mappings"
    new["references"][-1]["title"] = old["references"][-1]["title"]
    assert new == old
    komodo.check_mapping_title(path, {"mapping_source": metadata})


@pytest.mark.parametrize("sid", ["1.1", "1_12", "1_replace_glucose", "1_DSM 2 (3,4)"])
def test_variant_cannot_inherit_base_amounts_even_with_duplicate_annotation(case, tmp_path, sid):
    doc, data, item, _, metadata = case
    path, metadata, rows = mapping(tmp_path, table(sid))
    doc["media_term"]["term"]["id"] = "komodo.medium:" + sid
    doc["variant_relationship"] = "SOURCE_DUPLICATE"
    item.update(komodo_id=sid, mapping=rows[sid])
    after, claims = review((doc, data, item, path, metadata))
    assert after == doc
    assert claims[0]["status"] == "conflict" and "variant requires" in claims[0]["explanation"]


@pytest.mark.parametrize(
    "damage",
    [
        "name",
        "label",
        "accession",
        "id",
        "collection",
        "link",
        "source_id",
        "local_variant",
        "existing_mapping",
        "stock",
        "missing_ingredient",
        "preparation",
    ],
)
def test_identity_and_formulation_guards_cannot_be_bypassed(case, damage):
    doc, data, _, _, _ = case
    if damage == "name":
        doc["original_name"] += " other"
    elif damage == "label":
        doc["media_term"]["term"]["label"] += " other"
    elif damage == "accession":
        doc["media_term"]["term"]["id"] = "komodo.medium:2"
    elif damage == "id":
        case[2]["id"] = "CultureMech:000999"
        with pytest.raises(KeyError):
            review(case)
        return
    elif damage == "collection":
        data["medium"]["source"] = "JCM"
    elif damage == "link":
        data["medium"]["link"] += "?other"
    elif damage == "source_id":
        data["medium"]["id"] = "2"
    elif damage == "local_variant":
        doc["variant_relationship"] = "CONCENTRATION_VARIANT"
    elif damage == "existing_mapping":
        doc["references"] = [{"reference": inventory.MAPPING_URL}]
    elif damage == "stock":
        doc["solutions"] = [{"preferred_term": "Stock"}]
    elif damage == "missing_ingredient":
        data["solutions"][0]["recipe"].append({"compound": "KCl", "compound_id": 44})
    else:
        data["solutions"][0]["steps"].append({"step": "Do not combine both in one medium."})
    after, claims = review(case)
    assert after == doc and claims[0]["status"] == "conflict"
    assert not any(c["status"] in runner.SUPPORTED for c in claims)


def test_missing_amount_can_be_added_but_conflicting_amount_not_overwritten(case):
    doc = case[0]
    del doc["ingredients"][0]["concentration"]
    after, claims = review(case)
    assert claims[0]["status"] == "add"
    assert after["ingredients"][0]["concentration"] == {"value": "2", "unit": "G_PER_L"}
    doc["ingredients"][0]["concentration"] = {"value": "20", "unit": "G_PER_L"}
    after, claims = review(case)
    assert after == doc and claims[0]["status"] == "conflict"


def test_source_pinned_veto_preserves_entire_record(case):
    decision = withholding(case[:2])
    after, claims = review(case, [decision])
    assert after == case[0] and claims[0]["status"] == "conflict"
    decision["snippet"] = "Invented quote"
    with pytest.raises(ValueError, match="does not match"):
        review(case, [decision])


@pytest.mark.parametrize("local", [{"ph_value": 7.8}, {"ph_range": {"min": 6.8, "max": 7.8}}])
def test_mismatched_ph_conditions_require_formulation_review(case, local):
    case[0].update(local)
    case[1]["medium"].update(min_pH=6.8, max_pH=7.5)
    after, claims = review(case)
    assert after == case[0] and claims[0]["status"] == "conflict"
    assert "pH conditions differ" in claims[0]["explanation"]


def test_unavailable_source_cannot_support_any_amount(case, tmp_path):
    doc, _, item, _, metadata = case
    cache = tmp_path / "missing"
    cache.mkdir()
    raw = '{"status":404,"message":"Not found"}'
    source_meta = {
        "url": komodo.API + "1",
        "response_url": komodo.API + "1",
        "http_status": 404,
        "sha256": runner.sha(raw.encode()),
        "accessed_at": "2026-10-07T08:00:00+00:00",
    }
    (cache / "1.unavailable.body").write_text(raw)
    (cache / "1.unavailable.metadata.json").write_text(json.dumps(source_meta))
    assert komodo.read_source(cache, "1") == (raw, source_meta)
    after, claims = komodo.review(
        doc, raw, source_meta, "2026-10-07", records={item["id"]: item}, metadata=metadata
    )
    assert after == doc
    assert all(c["status"] == "unsupported" and c["new"] is None for c in claims)
    assert "HTTP 404" in claims[0]["explanation"]
    source_meta["http_status"] = 200
    (cache / "1.unavailable.metadata.json").write_text(json.dumps(source_meta))
    with pytest.raises(ValueError, match="Invalid unavailable"):
        komodo.read_source(cache, "1")


@pytest.mark.parametrize(
    "damage", ["hash", "url", "status", "duplicate", "pdf", "id_link", "header", "columns"]
)
def test_mapping_capture_corruption_rejected(tmp_path, damage):
    path, metadata, _ = mapping(tmp_path, table())
    raw = path.read_text()
    if damage == "hash":
        metadata["sha256"] = "0" * 64
    elif damage == "url":
        metadata["reference"] += "="
    elif damage == "status":
        metadata["http_status"] = 404
    else:
        if damage == "duplicate":
            raw += table()
        elif damage == "pdf":
            raw = raw.replace("www.dsmz.de", "example.org")
        elif damage == "id_link":
            raw = raw.replace("MediaInfo=1", "MediaInfo=2")
        elif damage == "header":
            raw = raw.replace("PH Info", "Wrong column")
        elif damage == "columns":
            raw = raw.replace("<TD>7.0</TD>", "")
        path.write_text(raw)
        metadata["sha256"] = runner.sha(raw.encode())
    with pytest.raises(ValueError):
        inventory.read_mapping(path, metadata)


@pytest.mark.parametrize("title", [None, "KOMODO - the Known Media Database"])
def test_preview_apply_verify_noop_and_mapping_tampering(case, tmp_path, monkeypatch, title):
    doc, data, item, mapping_path, metadata = case
    if title is not None:
        mapping_path.write_text(f"<title>{title}</title>" + mapping_path.read_text())
        metadata["sha256"] = runner.sha(mapping_path.read_bytes())
    path = tmp_path / item["path"]
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(doc, sort_keys=False))
    item["before_sha256"] = runner.sha(path.read_bytes())
    cache = tmp_path / "cache"
    cache.mkdir()
    raw, source_meta = capture(data)
    (cache / "1.json").write_text(raw)
    (cache / "1.metadata.json").write_text(json.dumps(source_meta))
    monkeypatch.setattr(
        runner.subprocess, "check_output", lambda *a, **k: (item["path"] + "\0").encode()
    )
    manifest = {"records": [item], "mapping_source": metadata}
    reviewer = komodo.adapter([item], metadata, mapping_title=title)
    plan = runner.preview(tmp_path, [item], cache, "f" * 40, adapter=reviewer)
    plan["mapping_source"] = metadata
    if title is not None:
        plan["mapping_title"] = title
    komodo.check_mapping_title(mapping_path, plan)
    assert not plan["records"][0]["failure"]
    komodo.context(manifest, mapping_path, plan["records"])
    komodo.check_sources(plan["records"], cache)
    assert runner.apply(tmp_path, plan, cache, adapter=reviewer)["changed"] == 1
    assert runner.verify(tmp_path, plan, cache, adapter=reviewer)["verified_new_snippets"] == 1
    assert komodo.verify_mapping(tmp_path, plan)["verified_mapping_snippets"] == 1
    assert runner.apply(tmp_path, plan, cache, adapter=reviewer)["already_applied"] == 1
    reports = tmp_path / "reports"
    komodo.reports(reports, plan, True)
    lines = (reports / "bacterial/example.yaml.md").read_text().splitlines()
    assert [s for s in lines if s.startswith("- Record:")] == ["- Record: " + item["path"]]
    assert sum(s.startswith("| `") for s in lines) == len(plan["records"][0]["claims"])
    bad = copy.deepcopy(plan)
    bad["records"][0]["mapping"]["snippet"] = "Invented mapping"
    with pytest.raises(ValueError, match="inventory changed"):
        komodo.context(manifest, mapping_path, bad["records"])
    source_meta["accessed_at"] = "2026-10-08T08:00:00+00:00"
    (cache / "1.metadata.json").write_text(json.dumps(source_meta))
    with pytest.raises(ValueError, match="Source capture changed"):
        komodo.check_sources(plan["records"], cache)
    after = runner.load_yaml(path.read_bytes())
    after["evidence"][0]["snippet"] = "Invented mapping"
    path.write_text(yaml.safe_dump(after, sort_keys=False))
    with pytest.raises(ValueError, match="provenance mismatch"):
        komodo.verify_mapping(tmp_path, plan)


@pytest.mark.parametrize(
    "batch,changed,claims_count",
    [
        ("0000-0500", 25, 137),
        ("0500-1000", 24, 141),
        ("1000-1500", 46, 264),
        ("1500-2000", 6, 25),
    ],
)
def test_applied_komodo_batch_hashes_reports_and_scoped_evidence(batch, changed, claims_count):
    root = Path(__file__).resolve().parents[1]
    folder = root / f"reports/ingredient_concentration_curation/20261007-komodo-media-{batch}"
    plan = json.loads((folder / "plan.json").read_text())
    assert len(plan["records"]) == 500
    counts = {"evidence_only": 0, "changed": 0}
    successors = [
        r
        for path in FOLLOWUPS
        for r in json.loads(path.read_text())["records"]
        if r["before_sha256"] != r["after_sha256"]
    ]
    assert komodo.verify_mapping(root, plan, successors)["verified_mapping_snippets"] == changed
    for item in plan["records"]:
        raw = (root / item["path"]).read_bytes()
        expected, _ = runner.followup_result_hash(item, successors)
        assert runner.sha(raw) == expected
        chain = runner.followup_chain(item, successors)
        # Current changes require independent source audits, not hash exemptions.
        doc = AUDIT.invert_chain(raw, chain) if chain else runner.load_yaml(raw)
        assert doc["id"] == item["id"]
        report = folder / "records" / (item["path"].removeprefix("data/normalized_yaml/") + ".md")
        lines = report.read_text().splitlines()
        assert [s for s in lines if s.startswith("- Record:")] == ["- Record: " + item["path"]]
        assert sum(s.startswith("| `") for s in lines) == len(item["claims"])
        assert not any(s.startswith("- State: preview") for s in lines)
        assert not item["failure"] and not item["baseline_errors"] and not item["post_errors"]
        accepted = [c for c in item["claims"] if c["status"] in runner.SUPPORTED]
        counts["changed"] += bool(accepted)
        for claim in accepted:
            counts["evidence_only"] += 1
            assert claim["status"] == "evidence_only" and claim["old"] == claim["new"]
            assert item["komodo_id"] == item["medium_id"]
            node = runner.get_node(doc, claim["pointer"])
            assert node["concentration"] == claim["new"]
            entries = [e for e in node["evidence"] if e["reference"] == claim["reference"]]
            assert len(entries) == 1 and entries[0]["snippet"] == claim["snippet"]
            assert entries[0]["supports"] == "SUPPORT"
            assert claim["field"] in entries[0]["explanation"]
            assert item["source_sha256"] in entries[0]["explanation"]
            assert plan["mapping_source"]["sha256"] in entries[0]["explanation"]
    assert counts == {"evidence_only": claims_count, "changed": changed}


def test_second_batch_preserves_source_pinned_preparation_withholdings():
    root = Path(__file__).resolve().parents[1]
    folder = root / "reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000"
    plan = json.loads((folder / "plan.json").read_text())
    contexts = {
        r["local"]["id"]: r
        for r in json.loads((folder / "inspected-candidate-context.json").read_text())
    }
    assert {r["medium_id"] for r in plan["withholdings"]} == {"111", "125", "187"}
    successors = json.loads((folder.parent / "20261007-dsmz111-preparation/plan.json").read_text())[
        "records"
    ]
    successors += json.loads(
        (folder.parent / "20261007-dsmz125-alternatives/plan.json").read_text()
    )["records"]
    for decision in plan["withholdings"]:
        item = next(r for r in plan["records"] if r["id"] == decision["id"])
        context = contexts[item["id"]]
        assert decision["snippet"] == runner.get_node(
            {"data": context["source"]}, decision["source_pointer"]
        )
        assert decision["source_sha256"] == context["source_metadata"]["sha256"]
        assert item["before_sha256"] == item["after_sha256"]
        expected, depth = runner.followup_result_hash(item, successors)
        assert runner.sha((root / item["path"]).read_bytes()) == expected
        assert depth == int(item["medium_id"] in {"111", "125"})
        assert all(c["status"] == "conflict" for c in item["claims"] if c["pointer"] is not None)


@pytest.mark.parametrize(
    "mid",
    [
        "226",
        "232",
        "232b",
        "239",
        "255",
        "262",
        "265",
        "266",
        "268",
        "303",
        "338",
        "368",
        "393",
        "394",
        "435",
    ],
)
def test_third_batch_preserves_source_pinned_withholdings(mid):
    root = Path(__file__).resolve().parents[1]
    folder = root / "reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500"
    plan = json.loads((folder / "plan.json").read_text())
    assert len(plan["withholdings"]) == 15
    decision = next(d for d in plan["withholdings"] if d["medium_id"] == mid)
    item = next(r for r in plan["records"] if r["id"] == decision["id"])
    context = next(
        r
        for r in json.loads((folder / "inspected-candidate-context.json").read_text())
        if r["medium_id"] == mid
    )
    assert decision["fields"] == ["*"]
    assert decision["reference"] == komodo.API + mid
    assert (
        decision["source_sha256"] == item["source_sha256"] == context["source_metadata"]["sha256"]
    )
    assert decision["snippet"] == runner.get_node(
        {"data": context["source"]}, decision["source_pointer"]
    )
    raw = (root / item["path"]).read_bytes()
    assert item["before_sha256"] == item["after_sha256"]
    successors = json.loads(
        (folder.parent / "20261007-dsmz265-preparations/plan.json").read_text()
    )["records"]
    expected, depth = runner.followup_result_hash(item, successors)
    assert runner.sha(raw) == expected and depth == int(mid == "265")
    if depth:
        successor = next(r for r in successors if r["path"] == item["path"])
        assert runner.load_yaml(successor["before_text"]) == context["local"]
    else:
        assert runner.load_yaml(raw) == context["local"]
    assert not any(c["status"] in runner.SUPPORTED for c in item["claims"])
    assert all(c["status"] == "conflict" for c in item["claims"] if c["pointer"] is not None)
    assert any(c["status"] == "evidence_only" for c in context["claims"])


@pytest.mark.parametrize("mid", ["469", "489"])
def test_fourth_batch_preserves_source_pinned_stock_findings(mid):
    root = Path(__file__).resolve().parents[1]
    folder = root / "reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000"
    plan = json.loads((folder / "plan.json").read_text())
    assert len(plan["withholdings"]) == 2
    decision = next(d for d in plan["withholdings"] if d["medium_id"] == mid)
    item = next(r for r in plan["records"] if r["id"] == decision["id"])
    context = next(
        r
        for r in json.loads((folder / "inspected-candidate-context.json").read_text())
        if r["medium_id"] == mid
    )
    assert decision["fields"] == ["*"]
    assert decision["reference"] == komodo.API + mid
    assert decision["source_sha256"] == item["source_sha256"]
    assert decision["source_sha256"] == context["source_metadata"]["sha256"]
    assert decision["snippet"] == runner.get_node(
        {"data": context["source"]}, decision["source_pointer"]
    )
    raw = (root / item["path"]).read_bytes()
    successors = json.loads((folder.parent / "20261007-dsmz467-469-inputs/plan.json").read_text())[
        "records"
    ]
    successors += json.loads((folder.parent / "20261007-dsmz489-stocks/plan.json").read_text())[
        "records"
    ]
    expected, depth = runner.followup_result_hash(item, successors)
    assert runner.sha(raw) == expected and item["before_sha256"] == item["after_sha256"]
    assert depth == 1
    baseline = (
        next(r["before_text"] for r in successors if r["path"] == item["path"]) if depth else raw
    )
    assert runner.load_yaml(baseline) == context["local"]
    assert not any(c["status"] in runner.SUPPORTED for c in item["claims"])
    assert any(c["status"] == "evidence_only" for c in context["claims"])


def test_fourth_batch_exact_variant_source_remains_an_unresolved_finding():
    root = Path(__file__).resolve().parents[1]
    folder = root / "reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000"
    finding = json.loads((folder / "variant-457_7098-source-finding.json").read_text())
    assert finding["http_status"] == 200 and finding["action"] == "unresolved_no_edit"
    assert runner.sha(finding["source_html"].encode()) == finding["sha256"]
    assert "<b>ID:</b></TD><TD>457_7098</TD>" in finding["source_html"]
    assert "Gram & Mol amounts are per Liter of medium." in finding["source_html"]
    assert "<TD>pentachlorophenol</TD>" in finding["source_html"]
    raw = (root / finding["path"]).read_bytes()
    assert runner.sha(raw) == finding["before_sha256"]
    assert runner.load_yaml(raw) == finding["current_record"]
    plan = json.loads((folder / "plan.json").read_text())
    item = next(r for r in plan["records"] if r["path"] == finding["path"])
    assert item["before_sha256"] == item["after_sha256"]
    assert not any(c["status"] in runner.SUPPORTED for c in item["claims"])
