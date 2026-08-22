from pathlib import Path

import yaml
from click.testing import CliRunner

import culturemech.render_media_pages as renderer
from culturemech.cli import cli
from culturemech.render_media_pages import render_pages, safe_mermaid


def _write_recipe(
    path: Path,
    *,
    recipe_id: str,
    name: str,
    category: str = "bacterial",
    ingredients: list[dict] | None = None,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(
            {
                "id": recipe_id,
                "name": name,
                "category": category,
                "physical_state": "LIQUID",
                "ingredients": ingredients or [],
            },
            sort_keys=False,
        )
    )


def test_safe_mermaid_keeps_graph_source_as_text() -> None:
    rendered = str(safe_mermaid("graph TD; A[</pre><script>alert(1)</script>]"))

    assert "<script>" not in rendered
    assert "&lt;/pre&gt;&lt;script&gt;" in rendered
    assert rendered.startswith('<pre class="mermaid">')


def test_index_autoescapes_imported_values(tmp_path: Path) -> None:
    source = tmp_path / "source" / "hostile.yaml"
    _write_recipe(
        source,
        recipe_id='CultureMech:000001"><img src=x onerror=alert(1)>',
        name="</a><script>alert(2)</script>",
        category="<svg onload=alert(3)>",
        ingredients=[
            {
                "preferred_term": '<img src=x onerror="alert(4)"> &lt;script&gt;',
                "notes": "</td><script>alert(5)</script>",
            }
        ],
    )
    pages = tmp_path / "site" / "media"
    index = tmp_path / "site"

    assert render_pages(source_files=[source], out_dir=pages, index_dir=index) == 0

    html = (index / "index.html").read_text()
    assert "<script>alert" not in html
    assert "<svg" not in html
    assert "<img" not in html
    assert "&lt;/a&gt;&lt;script&gt;" in html
    assert "Content-Security-Policy" in html

    page = next(pages.glob("*.html")).read_text()
    assert "<script>alert" not in page
    assert "<img src=x" not in page
    assert 'onerror="alert(4)"' not in page
    assert "&amp;lt;script&amp;gt;" in page


def test_render_pages_preserves_valid_mermaid_as_escaped_text(tmp_path: Path, monkeypatch) -> None:
    source = tmp_path / "source" / "recipe.yaml"
    _write_recipe(source, recipe_id="CultureMech:000006", name="Graph record")
    monkeypatch.setattr(
        renderer,
        "build_ingredient_composition_graph",
        lambda _medium: "```mermaid\ngraph TD; A[water] --> B[salt]\n```",
    )
    pages = tmp_path / "site" / "media"

    assert render_pages(source_files=[source], out_dir=pages, index_dir=tmp_path / "site") == 0

    page = (pages / "000006.html").read_text()
    assert '<pre class="mermaid">' in page
    assert "graph TD; A[water] --&gt; B[salt]" in page
    assert '<script type="module" src="../mermaid-init.js"></script>' in page


def test_render_pages_sanitizes_id_before_building_output_path(tmp_path: Path) -> None:
    source = tmp_path / "source" / "recipe.yaml"
    _write_recipe(
        source,
        recipe_id="CultureMech:../../outside",
        name="Path traversal record",
    )
    pages = tmp_path / "site" / "media"

    assert render_pages(source_files=[source], out_dir=pages, index_dir=tmp_path / "site") == 0

    assert not (tmp_path / "outside.html").exists()
    assert [path.name for path in pages.glob("*.html")] == ["outside.html"]


def test_single_file_render_selects_the_requested_file(tmp_path: Path) -> None:
    source_dir = tmp_path / "source"
    first = source_dir / "aaa.yaml"
    requested = source_dir / "zzz.yaml"
    _write_recipe(first, recipe_id="CultureMech:000001", name="Wrong record")
    _write_recipe(requested, recipe_id="CultureMech:000002", name="Requested record")
    site = tmp_path / "single"

    assert render_pages(source_files=[requested], out_dir=site, index_dir=site) == 0

    assert (site / "000002.html").is_file()
    assert not (site / "000001.html").exists()
    assert 'href="000002.html"' in (site / "index.html").read_text()
    page = (site / "000002.html").read_text()
    assert 'href="style.css"' in page
    assert 'href="index.html"' in page


def test_nested_page_layout_uses_relative_links(tmp_path: Path) -> None:
    source = tmp_path / "source.yaml"
    _write_recipe(source, recipe_id="CultureMech:000003", name="Nested record")
    index = tmp_path / "site"
    pages = index / "media"

    assert render_pages(source_files=[source], out_dir=pages, index_dir=index) == 0

    assert 'href="media/000003.html"' in (index / "index.html").read_text()
    page = (pages / "000003.html").read_text()
    assert 'href="../style.css"' in page
    assert 'href="../index.html"' in page
    assert 'src="../mermaid-init.js"' not in page  # no graph, so no script needed


def test_click_render_uses_the_shared_renderer(tmp_path: Path) -> None:
    source = tmp_path / "recipe.yaml"
    _write_recipe(source, recipe_id="CultureMech:000004", name="CLI record")
    site = tmp_path / "site"

    result = CliRunner().invoke(
        cli,
        [
            "render",
            "--file",
            str(source),
            "--output-dir",
            str(site / "media"),
            "--index-dir",
            str(site),
        ],
    )

    assert result.exit_code == 0, result.output
    assert (site / "media" / "000004.html").is_file()
    assert (site / "index.html").is_file()
