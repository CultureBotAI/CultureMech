"""The deep-research-client pin must stay new enough for the providers we rely on (#284).

We reach for this only when the corpus needs evidence — #150's remaining cocktails, #279's
ungroundable Se/Si compounds, #273's instruction rows all need source reading. It was
found six releases stale at 0.2.4, at which point `deep-research-client providers` listed
`cyberian` and nothing else. That is the wrong moment to discover it.

These assert the floor, not the installed version: CI resolves from the lock, and a
developer may legitimately be ahead.
"""

from __future__ import annotations

import re

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10
    import tomli as tomllib
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Below this, Edison is not a registered provider at all and `claude_code` does not exist.
MIN_DRC = (0, 2, 10)


def _dev_deps() -> list[str]:
    data = tomllib.loads((REPO / "pyproject.toml").read_text())
    return data["project"]["optional-dependencies"]["dev"]


def test_the_pin_floor_registers_edison_and_claude_code():
    spec = next(d for d in _dev_deps() if d.startswith("deep-research-client"))
    m = re.search(r">=\s*(\d+)\.(\d+)\.(\d+)", spec)
    assert m, (
        f"no lower bound in {spec!r} — an unpinned shared dependency is how two "
        "repos drift to 0.1.3 and 0.2.4 without anyone noticing"
    )
    assert tuple(int(g) for g in m.groups()) >= MIN_DRC, (
        f"{spec!r} is below {'.'.join(map(str, MIN_DRC))}, where `falcon` (Edison) and "
        "`claude_code` are not registered providers"
    )


def test_the_lockfile_agrees_with_the_floor():
    """A floor the lock does not satisfy is a floor in name only."""
    lock = (REPO / "uv.lock").read_text()
    m = re.search(r'name = "deep-research-client"\nversion = "(\d+)\.(\d+)\.(\d+)"', lock)
    assert m, "deep-research-client absent from uv.lock"
    assert tuple(int(g) for g in m.groups()) >= MIN_DRC


def test_the_edison_sdk_path_still_documents_why_it_exists():
    """Its original reason (DRC did not register Edison) expired at 0.2.10. It survives
    because DRC's falcon provider exposes no JOB selection. If someone removes that
    justification, the script should go with it rather than linger unexplained."""
    doc = (REPO / "scripts" / "research_media_edison.py").read_text()
    assert "job" in doc.lower() and "0.2.10" in doc, (
        "research_media_edison.py must say why it bypasses deep-research-client; the "
        "pre-0.2.10 reason is obsolete (#284)"
    )
