import json
from pathlib import Path

from culturemech.export.browser_export import BrowserExporter
from culturemech.render_media_pages import render_pages
from culturemech.web_artifacts import validate_web_coverage


def _write_recipe(path: Path, recipe_id: str, name: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"id: {recipe_id}\nname: {name}\ncategory: bacterial\ningredients: []\n")


def test_browser_export_and_pages_have_exact_source_coverage(tmp_path: Path) -> None:
    corpus = tmp_path / "corpus"
    _write_recipe(corpus / "b" / "two.yaml", "CultureMech:000002", "Second")
    _write_recipe(corpus / "a" / "one.yaml", "CultureMech:000001", "First")
    data_file = tmp_path / "app" / "data.js"
    pages = tmp_path / "pages"

    exporter = BrowserExporter(corpus)
    exporter.load_recipes()
    exporter.export(data_file)
    assert (
        render_pages(
            yaml_dir=corpus,
            out_dir=pages / "normalized",
            index_dir=pages / "normalized",
        )
        == 0
    )

    assert validate_web_coverage(corpus, data_file, pages) == []
    content = data_file.read_text()
    payload = json.loads(content.split(" = ", 1)[1].split(";\n", 1)[0])
    assert [record["source_file"] for record in payload] == ["a/one.yaml", "b/two.yaml"]
    assert [record["html_page"] for record in payload] == [
        "normalized/000001.html",
        "normalized/000002.html",
    ]


def test_coverage_reports_stale_and_missing_artifacts(tmp_path: Path) -> None:
    corpus = tmp_path / "corpus"
    _write_recipe(corpus / "one.yaml", "CultureMech:000001", "First")
    data_file = tmp_path / "app" / "data.js"
    exporter = BrowserExporter(corpus)
    exporter.load_recipes()
    exporter.export(data_file)
    pages = tmp_path / "pages"
    (pages / "normalized").mkdir(parents=True)
    (pages / "normalized" / "stale.html").write_text("stale")

    errors = validate_web_coverage(corpus, data_file, pages)

    assert any("missing 1 rendered page" in error for error in errors)
    assert any("stale rendered page" in error for error in errors)


def test_browser_export_refuses_partial_or_empty_output(tmp_path: Path) -> None:
    corrupt = tmp_path / "corrupt"
    _write_recipe(corrupt / "valid.yaml", "CultureMech:000001", "Valid")
    (corrupt / "bad.yaml").write_text("- not\n- a\n- recipe\n")

    exporter = BrowserExporter(corrupt)
    try:
        exporter.load_recipes()
    except ValueError as error:
        assert "failed to load 1 recipe" in str(error)
    else:
        raise AssertionError("corrupt recipe was accepted")

    empty = tmp_path / "empty"
    empty.mkdir()
    try:
        BrowserExporter(empty).load_recipes()
    except ValueError as error:
        assert "no recipe YAML files" in str(error)
    else:
        raise AssertionError("empty corpus was accepted")
