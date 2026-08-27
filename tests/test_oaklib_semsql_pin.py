"""The oaklib pin must keep `sqlite:obo:` off the retiring semantic-sql S3 bucket (#362).

INCATools/semantic-sql is removing public read from the raw S3 bucket
(semantic-sql#112). oaklib below 0.7.2 resolves `sqlite:obo:` selectors against
it; 0.7.2 moved the default to the CDN. Fifteen files here call
`get_adapter("sqlite:obo:...")`, and `label-correspondence` — a per-PR gate —
downloads through that path on a cache miss.

The reversion is invisible until it is catastrophic: on 0.6.23 every ChEBI
lookup still succeeds today, so no test, gate or error distinguishes a correct
pin from a reverted one right up until the bucket goes away and all of them fail
at once. Same shape as `test_deep_research_client_pin.py`, which exists because a
shared pin was found six releases stale.

These assert the floor, not the installed version: CI resolves from the lock and
a developer may legitimately be ahead.
"""

from __future__ import annotations

import re

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10
    import tomli as tomllib
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# 0.7.2 introduced the CDN default, but declares `requires_python <3.14` while
# this project supports <3.15 and runs 3.14 in CI. 0.7.3 widened it, so 0.7.3 is
# the lowest version installable across our whole matrix — the reason is not
# visible from the version number, which is why it is recorded here.
MIN_OAKLIB = (0, 7, 3)

S3_HOST = "s3.amazonaws.com"


def _spec() -> str:
    data = tomllib.loads((REPO / "pyproject.toml").read_text())
    return next(d for d in data["project"]["dependencies"] if d.startswith("oaklib"))


def test_the_pin_floor_keeps_the_cdn_default():
    spec = _spec()
    match = re.search(r">=\s*(\d+)\.(\d+)\.(\d+)", spec)
    assert match, (
        f"no lower bound in {spec!r} — below 0.7.2, `sqlite:obo:` resolves against "
        "the raw S3 bucket semantic-sql is retiring"
    )
    assert tuple(int(g) for g in match.groups()) >= MIN_OAKLIB, (
        f"{spec!r} is below {'.'.join(map(str, MIN_OAKLIB))}; 0.7.2 carries the CDN "
        "default but declares requires_python <3.14, which the 3.14 CI job needs"
    )


def test_the_lockfile_agrees_with_the_floor():
    """A floor the lock does not satisfy is a floor in name only."""
    lock = (REPO / "uv.lock").read_text()
    match = re.search(r'name = "oaklib"\nversion = "(\d+)\.(\d+)\.(\d+)"', lock)
    assert match, "oaklib absent from uv.lock"
    assert tuple(int(g) for g in match.groups()) >= MIN_OAKLIB


def test_the_resolved_default_is_not_the_retiring_bucket():
    """Pin the property, not a proxy for it.

    The two tests above track a version number, which is what we can control but
    not what we care about. This reads the constant oaklib will actually use, so
    it keeps working if upstream renames or re-defaults it again.
    """
    from oaklib.constants import SEMSQL_SQLITE_URL_BASE

    assert S3_HOST not in SEMSQL_SQLITE_URL_BASE, (
        f"oaklib resolves sqlite:obo: against {SEMSQL_SQLITE_URL_BASE}, the raw S3 "
        "bucket INCATools/semantic-sql is retiring (semantic-sql#112)"
    )
    assert SEMSQL_SQLITE_URL_BASE.startswith("https://"), SEMSQL_SQLITE_URL_BASE
