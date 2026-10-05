"""Composition-diagram node geometry is set in JS, not CSS.

The diagrams rendered with very large nodes for short chemical labels. The fix
has to live in `mermaid.initialize`, because mermaid measures each label box in
JavaScript during layout and writes the result as SVG width/height attributes —
a stylesheet rule applies afterwards and restyles the text inside a box whose
size is already fixed.

`htmlLabels: false` is the load-bearing setting. With HTML labels mermaid
measures a `<foreignObject>` div, but the page's CSP is `style-src 'self'`
(see media.html.j2), which blocks the inline stylesheet mermaid injects to size
that div, so the measurement falls back to unstyled browser defaults.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

INIT = Path(__file__).resolve().parents[1] / "src/culturemech/templates/composition-frame.js"
TEMPLATE = Path(__file__).resolve().parents[1] / "src/culturemech/templates/media.html.j2"


@pytest.fixture(scope="module")
def mermaid_config():
    """Evaluate the actual frame config, retaining its top-level/nested shape."""
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node is required to inspect JavaScript configuration")
    body = re.search(r"mermaid\.initialize\((\{.*?\})\);", INIT.read_text(), re.S)
    assert body, "could not find the mermaid.initialize call"
    script = "const data={dark:false}; console.log(JSON.stringify(" + body.group(1) + "));"
    return json.loads(subprocess.check_output([node, "-e", script], text=True))


def test_html_labels_are_off_at_the_TOP_level(mermaid_config):
    """Flowchart-only configuration previously produced oversized foreignObjects."""
    assert mermaid_config["htmlLabels"] is False
    assert mermaid_config["flowchart"]["htmlLabels"] is False


def test_the_page_csp_still_blocks_inline_styles():
    """The reason htmlLabels must stay off. If this ever changes, revisit it."""
    csp = re.search(r'Content-Security-Policy" content="([^"]+)"', TEMPLATE.read_text())
    assert csp, "media.html.j2 no longer declares a CSP"
    assert "style-src 'self'" in csp.group(1)
    assert "unsafe-inline" not in csp.group(1)


def test_the_font_size_is_smaller_than_mermaids_default(mermaid_config):
    """Mermaid's default is 16px."""
    assert int(mermaid_config["themeVariables"]["fontSize"].removesuffix("px")) < 16


def test_the_padding_is_tighter_than_mermaids_default(mermaid_config):
    """Mermaid's flowchart default is 15."""
    assert mermaid_config["flowchart"]["padding"] < 15


def test_the_diagram_still_scales_to_the_page(mermaid_config):
    assert mermaid_config["flowchart"]["useMaxWidth"] is True


def test_the_security_level_is_still_strict(mermaid_config):
    """Shrinking nodes must not have loosened sanitization."""
    assert mermaid_config["securityLevel"] == "strict"
