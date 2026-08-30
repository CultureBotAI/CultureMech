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

import re
from pathlib import Path

INIT = Path(__file__).resolve().parents[1] / "src/culturemech/templates/mermaid-init.js"
TEMPLATE = Path(__file__).resolve().parents[1] / "src/culturemech/templates/media.html.j2"


def test_html_labels_are_off_at_the_TOP_level():
    """Nesting it only under `flowchart` does not work, and looks like it does.

    Measured under the page CSP with mermaid 11, on the CultureMech:000001
    diagram: `flowchart.htmlLabels: false` alone still emits 5 foreignObjects
    and 64px nodes; the top-level key emits 0 and 26px nodes. A test that only
    grepped for the string would have passed on the broken config.
    """
    text = INIT.read_text()
    body = re.search(r"mermaid\.initialize\(\{(.*)\n\}\);", text, re.S)
    assert body, "could not find the mermaid.initialize call"
    # Two-space indent = a direct member of the config object, not nested.
    assert re.search(r"^  htmlLabels:\s*false,", body.group(1), re.M), (
        "htmlLabels: false is not set at the top level of mermaid.initialize"
    )


def test_the_page_csp_still_blocks_inline_styles():
    """The reason htmlLabels must stay off. If this ever changes, revisit it."""
    csp = re.search(r'Content-Security-Policy" content="([^"]+)"', TEMPLATE.read_text())
    assert csp, "media.html.j2 no longer declares a CSP"
    assert "style-src 'self'" in csp.group(1)
    assert "unsafe-inline" not in csp.group(1)


def test_the_font_size_is_smaller_than_mermaids_default():
    """Mermaid's default is 16px."""
    match = re.search(r"fontSize:\s*\"(\d+)px\"", INIT.read_text())
    assert match, "no fontSize set; nodes fall back to mermaid's 16px default"
    assert int(match.group(1)) < 16


def test_the_padding_is_tighter_than_mermaids_default():
    """Mermaid's flowchart default is 15."""
    match = re.search(r"padding:\s*(\d+)", INIT.read_text())
    assert match, "no flowchart padding set"
    assert int(match.group(1)) < 15


def test_the_diagram_still_scales_to_the_page():
    text = INIT.read_text()
    assert re.search(r"useMaxWidth:\s*true", text)


def test_the_security_level_is_still_strict():
    """Shrinking nodes must not have loosened sanitization."""
    assert re.search(r'securityLevel:\s*"strict"', INIT.read_text())
