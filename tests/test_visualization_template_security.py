from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATES = Path(__file__).parents[1] / "src" / "culturemech" / "templates"


def _environment() -> Environment:
    return Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html"]),
    )


def test_media_umap_serializes_hostile_values_safely() -> None:
    payload = "</script><img src=x onerror=alert(1)>"
    html = (
        _environment()
        .get_template("media_umap.html")
        .render(
            derived_data=[{"name": payload}],
            direct_data=[],
            derived_count=1,
            direct_count=0,
            unique_count=1,
        )
    )

    assert payload not in html
    assert "\\u003c/script\\u003e" in html
    assert "${escapeHtml(d.name)}" in html


def test_ingredient_umap_serializes_hostile_values_safely() -> None:
    payload = "</script><svg onload=alert(1)>"
    html = (
        _environment()
        .get_template("ingredient_umap.html")
        .render(
            ingredient_data=[{"name": payload}],
            projection={"label": "PaCMAP", "input_dimensions": 512},
            graph_receipt={
                "source": {"filename": payload},
                "coverage": {"projected": 1, "eligible": 1, "unresolved_occurrences": 0},
            },
            receipt_filename="ingredient_umap.metadata.json",
            total_count=1,
            tier_counts={"top100": 0, "top500": 0, "other": 1},
        )
    )

    assert payload not in html
    assert "\\u003c/script\\u003e" in html
    assert "${escapeHtml(d.name)}" in html
