"""Every solution record with a grounded composition reaches the graph (#442).

Corpus tier by construction (it reads data/normalized_yaml). The unit case lives
in tests/test_kgx_node_ids.py; this is the gate that the 0-of-4,986 figure
cannot come back: a solution record whose `composition` carries at least one
resolvable id must be the subject of at least one has_part edge.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from record_kinds import is_solution_record  # noqa: E402

from culturemech.export.kgx_export import resolve_ingredient, transform  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"


def _solution_records_with_composition():
    for path in sorted(NORMALIZED.glob("*/*.yaml")):
        record = yaml.safe_load(path.read_text())
        if isinstance(record, dict) and is_solution_record(record) and record.get("composition"):
            yield path, record


def test_the_population_is_not_empty():
    """Guards the gate below against passing vacuously."""
    assert sum(1 for _ in _solution_records_with_composition()) > 1000


def _resolvable(record) -> bool:
    """At least one composition row the MIM resolver gives an identity to.

    A record whose only row MIM explicitly leaves unmapped (10 today, e.g. the
    single-row `OXOID Legionella CYE-Agar base` solutions) correctly emits
    nothing; that is the resolver's decision, not a missing walk.
    """
    return any(
        getattr(resolve_ingredient(row), "identifier", None)
        for row in record["composition"]
        if isinstance(row, dict)
    )


@pytest.mark.corpus
def test_every_solution_record_with_a_resolvable_composition_emits_a_has_part():
    silent, suppressed = [], 0
    for path, record in _solution_records_with_composition():
        emits = any(e["predicate"] == "biolink:has_part" for e in transform(record))
        if emits:
            continue
        if _resolvable(record):
            silent.append(path.name)
        else:
            suppressed += 1
    # Pinned, not bounded: the count is a property of the MIM pin, so a bump that
    # changes it should show up here rather than slide under a loose ceiling (#417).
    assert suppressed == 10, (
        f"{suppressed} solution records have no resolvable composition row (baseline 10, "
        "all single-row solutions MIM leaves unmapped); re-measure after a MIM pin bump"
    )
    assert not silent, (
        f"{len(silent)} solution record(s) carry a resolvable composition but emit no "
        f"has_part (#442): " + ", ".join(silent[:10])
    )
