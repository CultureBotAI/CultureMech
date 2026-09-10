"""Every solution record with a resolvable composition reaches the graph (#442).

Corpus tier by construction (it reads data/normalized_yaml). The unit case lives
in tests/test_kgx_node_ids.py; this is the gate that the 0-of-4,986 figure
cannot come back: a solution record whose `composition` carries at least one
row the MIM resolver gives an identity to must be the subject of a has_part.

It reads the session-parsed `corpus` fixture rather than walking the tree: the
first version parsed all 15,877 files itself, twice, and cost the CI corpus job
nine minutes under coverage (run 34445132327), enough to hit its 40-minute
timeout on a slow runner.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from record_kinds import is_solution_record  # noqa: E402

from culturemech.export.kgx_export import resolve_ingredient, transform  # noqa: E402


def _resolvable(record: dict) -> bool:
    """At least one composition row the MIM resolver gives an identity to.

    A record whose only row MIM explicitly leaves unmapped (10 today, e.g. the
    single-row `OXOID Legionella CYE-Agar base` solutions) correctly emits
    nothing; that is the resolver's decision, not a missing walk. The same
    `identifier` the edge builder reads (`_resolved_ingredient_id`).
    """
    return any(
        getattr(resolve_ingredient(row), "identifier", None)
        for row in record["composition"]
        if isinstance(row, dict)
    )


@pytest.mark.corpus
def test_every_solution_record_with_a_resolvable_composition_emits_a_has_part(corpus):
    population = [
        (path, record)
        for path, record in corpus
        if is_solution_record(record) and record.get("composition")
    ]
    # Guards against passing vacuously: the corpus holds 4,784 of these today.
    assert len(population) > 1000, f"only {len(population)} solution records with a composition"

    silent, suppressed = [], 0
    for path, record in population:
        if any(e["predicate"] == "biolink:has_part" for e in transform(record)):
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
