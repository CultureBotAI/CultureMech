"""Static-site status must only expose successfully staged, validated maps."""

from __future__ import annotations

import json
import shutil
import subprocess
from contextlib import contextmanager
from pathlib import Path

import pytest

from culturemech import text_map_publish as publish

REPO = Path(__file__).resolve().parents[1]


def configure(root, enabled):
    (root / "conf").mkdir()
    (root / "conf" / "text_map.yaml").write_text(f"enabled: {str(enabled).lower()}\n")


def test_disabled_status_clears_prior_enabled_navigation(tmp_path):
    configure(tmp_path, False)
    status = tmp_path / "app" / "text_map_status.json"
    status.parent.mkdir(parents=True)
    status.write_text('{"enabled":true}')
    assert publish.publish(tmp_path) == {"enabled": False}
    assert json.loads(status.read_text()) == {"enabled": False}


def test_invalid_enabled_map_preserves_prior_site_and_status(tmp_path):
    configure(tmp_path, True)
    status = tmp_path / "app" / "text_map_status.json"
    status.parent.mkdir(parents=True)
    status.write_text('{"enabled":true}')
    page = tmp_path / "app" / "index.html"
    page.write_text("previous site")
    with pytest.raises(ValueError, match="current.json"):
        publish.publish(tmp_path)
    assert status.read_text() == '{"enabled":true}'
    assert page.read_text() == "previous site"


def test_navigation_enabled_only_after_successful_staging(tmp_path, monkeypatch):
    status = tmp_path / "app" / "text_map_status.json"

    class Prepared:
        def stage(self, site):
            assert site == tmp_path / "pages"
            assert not status.exists()
            site.mkdir()
            (site / "text-map").mkdir()

    @contextmanager
    def ready(root):
        assert root == tmp_path
        yield Prepared()

    monkeypatch.setattr(publish, "prepare_text_map", ready)
    assert publish.publish(tmp_path) == {"enabled": True}
    assert json.loads(status.read_text()) == {"enabled": True}


def test_staging_failure_cannot_enable_navigation(tmp_path, monkeypatch):
    class Prepared:
        def stage(self, site):
            raise OSError("staging failed")

    @contextmanager
    def ready(_root):
        yield Prepared()

    monkeypatch.setattr(publish, "prepare_text_map", ready)
    with pytest.raises(OSError, match="staging failed"):
        publish.publish(tmp_path)
    assert not (tmp_path / "pages").exists()


def test_status_write_failure_preserves_old_status_and_removes_temporary(tmp_path, monkeypatch):
    configure(tmp_path, False)
    status = tmp_path / "app" / "text_map_status.json"
    status.parent.mkdir(parents=True)
    status.write_text('{"enabled":true}')

    def fail(_source, _target):
        raise OSError("replace failed")

    monkeypatch.setattr(publish.os, "replace", fail)
    with pytest.raises(OSError, match="replace failed"):
        publish.publish(tmp_path)
    assert status.read_text() == '{"enabled":true}'
    assert list(status.parent.iterdir()) == [status]


@pytest.mark.parametrize("name", ["index.html"])
def test_static_landing_links_are_hidden_until_status_arrives(name):
    page = (REPO / "app" / name).read_text()
    assert '<div class="card" data-text-map-link hidden>' in page
    assert 'href="../pages/text-map/"' in page
    assert '<script src="text-map-nav.js"></script>' in page


@pytest.mark.skipif(shutil.which("node") is None, reason="Node is needed for the browser harness")
@pytest.mark.parametrize(
    "status,ok,expected",
    [
        ({"enabled": True}, True, False),
        ({"enabled": False}, True, True),
        ({"enabled": "true"}, True, True),
        (None, True, True),
        ({"enabled": True}, False, True),
    ],
)
def test_navigation_script_only_reveals_an_explicit_success(status, ok, expected):
    script = (REPO / "app" / "text-map-nav.js").read_text()
    fixture = f"""
      import {{runInNewContext}} from 'node:vm';
      const link = {{hidden: true}};
      const fixture = {{
        fetch: async (url, options) => {{
          if (url !== 'text_map_status.json' || options.cache !== 'no-store')
            throw new Error('unexpected status request');
          return {{ok: {json.dumps(ok)}, json: async () => ({json.dumps(status)})}};
        }},
        document: {{querySelectorAll: (selector) => {{
          if (selector !== '[data-text-map-link]') throw new Error('unexpected selector');
          return [link];
        }}}}
      }};
      runInNewContext({json.dumps(script)}, fixture);
      await new Promise(resolve => setTimeout(resolve, 0));
      if (link.hidden !== {json.dumps(expected)}) throw new Error('wrong link visibility');
    """
    subprocess.run(["node", "--input-type=module", "-e", fixture], check=True, capture_output=True)


def test_shared_card_precedes_and_preserves_the_graph_views():
    index = (REPO / "app" / "index.html").read_text()
    assert index.index('href="../pages/text-map/"') < index.index('href="umap.html#umap-derived"')
    for target in ("umap.html#umap-derived", "umap.html#umap-direct", "umap_graph.html"):
        assert f'href="{target}"' in index
    assert "Graph embedding browser" in index


def test_deployment_stages_the_map_before_browser_and_both_page_builds():
    import yaml

    workflow = yaml.safe_load((REPO / ".github/workflows/generate-pages.yaml").read_text())
    steps = workflow["jobs"]["build"]["steps"]
    names = [step.get("name") for step in steps]
    stage = names.index("Stage validated common semantic text map")
    assert stage < names.index("Build browser data and normalized pages")
    assert stage < names.index("Render canonical merged pages")
    assert steps[stage]["run"] == "uv run python scripts/stage_text_map.py"
