"""Historical coordinates survive source-backed link repair and rejected inputs."""

import json
from pathlib import Path

import pytest
import yaml

from culturemech.historical_map_links import MAPS, POPULATIONS, read_population, repair


def write_current(root, records):
    corpus = root / "data/normalized_yaml"
    rows = []
    for i, source in enumerate(records, 1):
        path = corpus / source
        path.parent.mkdir(parents=True, exist_ok=True)
        identity = f"CultureMech:{i:06}"
        path.write_text(yaml.safe_dump({"id": identity, "name": "Same display name"}))
        page = f"normalized/{i:06}.html"
        target = root / "pages" / page
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(identity)
        rows.append({"id": identity, "source_file": source, "html_page": page})
    app = root / "app"
    app.mkdir(exist_ok=True)
    (app / "browser.html").write_text("browser")
    write_browser(root, rows)
    return rows


def write_browser(root, rows):
    (root / "app/data.js").write_text(
        "window.culturemechData = " + json.dumps(rows) + ";\n\n// Dispatch event\n"
    )


def write_maps(root, points):
    for offset, name in enumerate(MAPS):
        groups = {
            p: [
                dict(row, x=i + 0.125 + offset, y=-i - 0.25, url="pages/old.html")
                for i, row in enumerate(points)
            ]
            for p in POPULATIONS
        }
        content = "<header><h1>Historical map</h1><p>Old description</p></header><script>"
        for p, rows in groups.items():
            content += f"const {p} = {json.dumps(rows)};\n"
        content += "tooltip.html(`Source: ${d.source_database}`);</script>"
        (root / "app" / name).write_text(content)


@pytest.fixture
def populated(tmp_path):
    rows = write_current(
        tmp_path, ["algae/exact.yaml", "new/moved.yaml", "a/same.yaml", "b/same.yaml"]
    )
    write_maps(
        tmp_path,
        [
            {"id": "exact", "category": "algae", "name": "old name"},
            {"id": "moved", "category": "old", "name": "different label"},
            {"id": "same", "category": "old", "name": "Same display name"},
            {"id": "gone", "category": "a", "name": "Same display name"},
        ],
    )
    return tmp_path, rows


def test_exact_identity_fallback_preservation_and_idempotence(populated):
    root, _ = populated
    before = {n: (root / "app" / n).read_text() for n in MAPS}
    preview = repair(root)
    assert len(preview["changed"]) == 2
    assert before == {n: (root / "app" / n).read_text() for n in MAPS}
    with pytest.raises(ValueError, match="need repair"):
        repair(root, check=True)
    report = repair(root, apply=True)
    assert report["current_records"] == 4
    for name in MAPS:
        content = (root / "app" / name).read_text()
        assert "lineage are unverified" in content
        assert "Media browser (historical record unresolved or ambiguous)" in content
        for p in POPULATIONS:
            old, *_ = read_population(before[name], p)
            points, *_ = read_population(content, p)
            assert len(points) == len(old) == 4
            assert [x["record_link_status"] for x in points] == [
                "exact-category-source",
                "unique-source",
                "ambiguous",
                "unresolved",
            ]
            assert [x["url"] for x in points] == [
                "../pages/normalized/000001.html",
                "../pages/normalized/000002.html",
                "browser.html",
                "browser.html",
            ]
            for previous, current in zip(old, points, strict=True):
                assert {k: v for k, v in previous.items() if k != "url"} == {
                    k: v
                    for k, v in current.items()
                    if k not in {"url", "record_link_status", "record_source_file"}
                }
                assert ((root / "app") / current["url"]).resolve().is_file()
    first = {n: (root / "app" / n).read_bytes() for n in MAPS}
    assert repair(root, check=True)["changed"] == []
    assert repair(root, apply=True)["changed"] == []
    assert first == {n: (root / "app" / n).read_bytes() for n in MAPS}


@pytest.mark.parametrize(
    "corruption",
    [
        "id",
        "route",
        "missing-page",
        "duplicate-source",
        "missing-source",
        "ignored-source",
        "second-map",
    ],
)
def test_failed_preflight_preserves_both_old_maps(populated, corruption):
    root, rows = populated
    if corruption == "id":
        rows[0]["id"] = "CultureMech:999999"
    elif corruption == "route":
        rows[0]["html_page"] = "normalized/000002.html"
    elif corruption == "missing-page":
        (root / "pages/normalized/000001.html").unlink()
    elif corruption == "duplicate-source":
        rows[0] = rows[1]
    elif corruption == "missing-source":
        rows.pop()
    elif corruption == "ignored-source":
        (root / ".gitignore").write_text("data/normalized_yaml/a/hidden.yaml\n")
        (root / "data/normalized_yaml/a/hidden.yaml").write_text("id: CultureMech:999999\n")
    elif corruption == "second-map":
        (root / "app" / MAPS[1]).write_text("invalid second map")
    write_browser(root, rows)
    before = {n: (root / "app" / n).read_bytes() for n in MAPS}
    with pytest.raises(ValueError):
        repair(root, apply=True)
    assert before == {n: (root / "app" / n).read_bytes() for n in MAPS}


def test_inline_payload_cannot_terminate_script(populated):
    root, _ = populated
    write_maps(
        root,
        [{"id": "exact", "category": "algae", "name": "</script><script>bad()</script>\u2028"}],
    )
    repair(root, apply=True)
    for name in MAPS:
        content = (root / "app" / name).read_text()
        assert "</script><script>bad()" not in content
        assert (
            read_population(content, POPULATIONS[0])[0][0]["name"]
            == "</script><script>bad()</script>\u2028"
        )


def test_pages_workflow_repairs_after_render_and_before_copy():
    repo = Path(__file__).resolve().parents[1]
    workflow = yaml.safe_load((repo / ".github/workflows/generate-pages.yaml").read_text())
    steps = workflow["jobs"]["build"]["steps"]
    names = [s.get("name") for s in steps]
    i = names.index("Repair retained historical map links")
    assert names.index("Build browser data and normalized pages") < i
    assert names.index("Render canonical merged pages") < i < names.index("Stage site")
    assert steps[i]["run"] == "uv run python scripts/repair_historical_map_links.py --apply"
