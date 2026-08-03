"""Shared fixtures — chiefly one parse of the corpus for the whole session.

Several corpus-level guards each walked `data/normalized_yaml/**` independently,
parsing ~15,900 YAML files per test. Four of them cost ~105s apiece locally, which
is roughly 7 minutes of a 10-minute suite spent re-reading the same files — and in
CI that was enough to hit the 40-minute job timeout and cancel the run.

Raising the timeout would have hidden it; the cost is real and grows with every
guard added. A session-scoped parse pays it once.

Use `corpus` (every record) or `media_records` (media only, stock solutions
excluded) instead of writing another `rglob`. The dicts are shared, so **treat
them as read-only** — mutating one would leak into every later test.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
NORMALIZED = REPO_ROOT / "data" / "normalized_yaml"

sys.path.insert(0, str(REPO_ROOT / "scripts"))


@pytest.fixture(scope="session")
def corpus() -> list[tuple[Path, dict[str, Any]]]:
    """Every parseable record under data/normalized_yaml, parsed once per session."""
    out: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(NORMALIZED.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        if isinstance(doc, dict):
            out.append((path, doc))
    return out


@pytest.fixture(scope="session")
def media_records(corpus) -> list[tuple[Path, dict[str, Any]]]:
    """Media only — stock-solution records excluded, as every guard wants (#124)."""
    from record_kinds import is_solution_record

    return [(p, d) for p, d in corpus if not is_solution_record(d)]
