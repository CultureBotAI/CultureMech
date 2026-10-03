from html.parser import HTMLParser
from pathlib import Path


class Elements(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.items = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.items.append((tag, dict(attrs)))

    def find(self, tag=None, **attrs):
        return [
            a
            for t, a in self.items
            if (tag is None or t == tag)
            and all(a.get(k.rstrip("_").replace("_", "-")) == v for k, v in attrs.items())
        ]


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = "https://culturebotai.github.io/mechs/"


def test_browser_names_search_and_announces_result_changes():
    dom = Elements((ROOT / "app/browser.html").read_text())
    assert dom.find("label", for_="searchInput")
    assert dom.find(id="resultsCount", role="status", aria_live="polite")
    assert dom.find("a", href=DIRECTORY)


def test_generated_record_shell_has_mobile_landmarks_and_resolvable_theme(tmp_path):
    import yaml

    from culturemech.render_media_pages import render_pages

    source = tmp_path / "source.yaml"
    source.write_text(
        yaml.safe_dump({"id": "CultureMech:123456", "name": "Test", "ingredients": []})
    )
    index = tmp_path / "site/pages"
    output = index / "normalized"
    assert render_pages(source_files=[source], out_dir=output, index_dir=index) == 0
    for page in [index / "index.html", output / "123456.html"]:
        dom = Elements(page.read_text())
        assert dom.find("meta", name="viewport", content="width=device-width, initial-scale=1")
        assert dom.find("main", id="main-content")
        assert dom.find("button", id="record-theme")
        assert dom.find("a", href=DIRECTORY)
        theme = [
            a["src"] for a in dom.find("script") if a.get("src", "").endswith("record-theme.js")
        ]
        assert len(theme) == 1 and (page.parent / theme[0]).is_file()
        assert "unsafe-inline" not in page.read_text()


def test_browser_javascript_parses(tmp_path):
    import re
    import shutil
    import subprocess

    import pytest

    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required for the browser JavaScript syntax check")
    html = (ROOT / "app/browser.html").read_text()
    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, re.DOTALL)
    assert scripts
    for number, script in enumerate(scripts):
        source = tmp_path / f"inline-{number}.js"
        source.write_text(script)
        checked = subprocess.run([node, "--check", str(source)], capture_output=True, text=True)
        assert checked.returncode == 0, checked.stderr
