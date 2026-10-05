"""Public record regressions for the October 2026 website audit."""

import importlib.util
from pathlib import Path

import pytest
import yaml

from culturemech import render_media_pages as render

ROOT = Path(__file__).resolve().parents[1]


def record_html(path, tmp_path):
    out = tmp_path / "pages"
    out.mkdir(exist_ok=True)
    status, data, slug = render.render_one(
        render.make_env(), path, out, out, render.build_signature(), force=True
    )
    assert status == "rendered"
    return (out / (slug + ".html")).read_text()


def test_2asw_identity_is_source_grounded_and_stock_scoped(tmp_path):
    source = ROOT / "data/normalized_yaml/algae/2asw.yaml"
    data = yaml.safe_load(source.read_text())
    ingredient = data["ingredients"][0]
    assert ingredient["preferred_term"] == "NaNO3"
    assert ingredient["term"] == {"id": "CHEBI:63005", "label": "sodium nitrate"}
    assert ingredient["concentration"] == {"value": "15.00", "unit": "G_PER_L"}
    assert "stock concentration, not the final medium" in ingredient["notes"]
    assert "historical version equivalence is not asserted" in data["curation_history"][-1]["notes"]
    text = record_html(source, tmp_path)
    assert "CHEBI:63005" in text and "457.962" not in text
    assert "Dunaliella salina" in text and "CCAP 19/18" in text
    assert "measurement conditions" in text.lower() and "20-35" in text
    assert "f_2asw" in text and "10.1104/pp.18.00453" in text
    assert "universal growth suitability" in text


def test_absent_evidence_and_variants_are_not_fabricated(tmp_path):
    source = tmp_path / "absent.yaml"
    source.write_text(yaml.safe_dump({"id": "CultureMech:999999", "name": "Empty test"}))
    text = record_html(source, tmp_path)
    assert "No target organisms are recorded." in text
    assert 'id="variants"' not in text
    assert "Measurement conditions" not in text


def test_resolvers_preserve_ids_without_fake_anchors():
    for curie in ["MICRO:0000178", "komodo.medium:381", "CommunityMech:999999"]:
        result = str(render.identifier_link(curie))
        assert curie in result and "source link unavailable" in result
        assert "href=" not in result
    assert "https://github.com/CultureBotAI/CommunityMech/blob/" in str(
        render.identifier_link("CommunityMech:000064")
    )
    assert "doi.org/10.1104/pp.18.00453" in str(render.linked_text("DOI:10.1104/pp.18.00453"))
    assert "<script>" not in str(render.structured({"reference": "<script>alert(1)</script>"}))


def test_normalized_sources_use_registry_identity_and_leave_unknowns_unresolved():
    index = render.normalized_source_index()
    assert index["1_1_dyiii_pea_gr_medium"] == "CultureMech:000001"
    assert "2asw" not in index  # two category records share this historical stem
    assert "/normalized/000001.html" in str(render.normalized_source("1_1_dyiii_pea_gr_medium"))
    assert "normalized source unresolved" in str(render.normalized_source("not-a-record"))


def test_normalized_index_growth_review_target_and_frame_assets(tmp_path):
    source = ROOT / "data/normalized_yaml/algae/2asw.yaml"
    out = tmp_path / "pages/normalized"
    assert render.render_pages(source_files=[source], out_dir=out, index_dir=out) == 0
    assert 'href="../media_growth_review.html"' in (out / "index.html").read_text()
    for name in ["composition-frame.html", "composition-frame.js", "composition-frame.css"]:
        assert (out / name).is_file()
    frame = (out / "composition-frame.html").read_text()
    assert "style-src 'self' 'unsafe-inline'" in frame
    record = (out / "000038.html").read_text()
    assert "style-src 'self';" in record


def test_growth_report_has_typed_links_and_snapshot_identity(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location(
        "growth_report", ROOT / "scripts/build_media_growth_review_html.py"
    )
    report = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(report)
    monkeypatch.setattr(report, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(report.subprocess, "check_output", lambda *a, **k: "a" * 40)
    monkeypatch.setattr(report.subprocess, "run", lambda *a, **k: type("Result", (), {"returncode": 1})())
    source = tmp_path / "data/normalized_yaml/algae/2asw.yaml"
    source.parent.mkdir(parents=True)
    source.write_text("id: CultureMech:000038")
    registry = tmp_path / "data/culturemech_id_registry.tsv"
    registry.write_text(
        "culturemech_id\tfile_path\nCultureMech:000038\tdata/normalized_yaml/algae/2asw.yaml\n"
    )
    manifest = tmp_path / "manifest.tsv"
    manifest.write_text("snapshot\n")
    rows = [
        {
            "id": "CultureMech:000038",
            "name": "2ASW",
            "review_status": "applied_growth_evidence",
            "category_dir": "algae",
        }
    ]
    text = report.build_report(rows, manifest)
    assert "normalized/000038.html" in text and "Manifest SHA256" in text
    assert "a" * 40 in text
    assert "normalized records modified locally" in text
    assert "No review artifact in this build" in text
    absent = report.build_report([{**rows[0], "id": "CultureMech:999999"}], manifest)
    assert "normalized/999999.html" not in absent
    wrong_layer = report.build_report(
        [{**rows[0], "yaml_path": "data/merge_yaml/merged/2ASW.yaml"}], manifest
    )
    assert "normalized/000038.html" not in wrong_layer
    with pytest.raises(ValueError):
        report.build_report(rows + rows, manifest)


def test_map_links_require_current_source_identity_and_disambiguate_category(tmp_path):
    from build_map_record_links import build_links

    root = tmp_path
    (root / "data/normalized_yaml/algae").mkdir(parents=True)
    (root / "data/normalized_yaml/bacterial").mkdir(parents=True)
    for name in ["algae/shared", "bacterial/shared", "algae/ambiguous", "bacterial/moved"]:
        (root / ("data/normalized_yaml/" + name + ".yaml")).write_text("name: example")
    registry = root / "data/culturemech_id_registry.tsv"
    registry.write_text(
        "culturemech_id\tfile_path\n"
        "CultureMech:000001\tdata/normalized_yaml/algae/shared.yaml\n"
        "CultureMech:000002\tdata/normalized_yaml/bacterial/shared.yaml\n"
        "CultureMech:000003\tdata/normalized_yaml/algae/missing.yaml\n"
        "CultureMech:000004\tdata/normalized_yaml/algae/ambiguous.yaml\n"
        "CultureMech:000005\tdata/normalized_yaml/algae/ambiguous.yaml\n"
        "CultureMech:000006\tdata/normalized_yaml/bacterial/moved.yaml\n"
    )
    links = build_links(root)["links"]
    assert links == {
        "algae/shared": "../pages/normalized/000001.html",
        "bacterial/shared": "../pages/normalized/000002.html",
        "bacterial/moved": "../pages/normalized/000006.html",
        "*/moved": "../pages/normalized/000006.html",
    }


def test_scientific_zero_and_false_are_preserved():
    text = str(render.structured({"measurement": 0, "growth": False, "empty": None}))
    assert "<dd>0</dd>" in text and "<dd>False</dd>" in text
    assert "<dt>Empty</dt>" not in text
    assert render.reference_url("CultureMech:999999") == ""
    assert "source link unavailable" in str(render.identifier_link("CultureMech:999999"))


def test_record_link_helper_is_part_of_incremental_build_signature(tmp_path, monkeypatch):
    original = Path(render.__file__)
    local_renderer = tmp_path / original.name
    local_renderer.write_bytes(original.read_bytes())
    helper = tmp_path / "record_links.py"
    helper.write_bytes(original.with_name("record_links.py").read_bytes())
    monkeypatch.setattr(render, "__file__", str(local_renderer))
    before = render.build_signature()
    helper.write_text(helper.read_text() + "\n# Different verified-identity rules\n")
    assert render.build_signature() != before
