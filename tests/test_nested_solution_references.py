"""Every nested `mediadive.solution:` reference resolves to a solution record (#449).

A medium that names an upstream stock by id says what it means; the corpus
must hold that stock. On 2026-09-10 one of 1,229 such references did not
(solution 5059 in CultureMech:002236), because the importer skips upstream
solutions that carry prose steps and no recipe table. The exporter's index
(#441) is the same lookup, so the gate and the export cannot disagree.

Corpus tier by construction: it reads the session-parsed `corpus` fixture.
"""

from __future__ import annotations

import pytest

from culturemech.export.kgx_export import _index_records_under

REPO_NORMALIZED = "data/normalized_yaml"


@pytest.mark.corpus
def test_every_nested_upstream_solution_id_has_a_record(corpus):
    index = _index_records_under(REPO_NORMALIZED)
    assert len(index) > 4000, f"index holds only {len(index)} solution records"

    references, unresolved = 0, []
    for path, record in corpus:
        for solution in record.get("solutions") or []:
            term = solution.get("term") if isinstance(solution, dict) else None
            tid = term.get("id") if isinstance(term, dict) else None
            if not (isinstance(tid, str) and tid.startswith("mediadive.solution:")):
                continue
            references += 1
            if tid not in index:
                unresolved.append(f"{path.name}: {tid}")
    assert references > 1000, f"only {references} nested upstream references found"
    assert (
        not unresolved
    ), f"{len(unresolved)} nested mediadive.solution reference(s) have no record: " + ", ".join(
        unresolved[:10]
    )
