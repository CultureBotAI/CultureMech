"""Guard that the id registry matches the corpus (#144).

`data/culturemech_id_registry.tsv` maps each CultureMech id to the file holding
it. A category move changes the path but not the id, so every bulk
recategorization rots it silently — #115 (629 records), #120 (73), #137, #143 —
until it held **5,511 rows pointing at files that did not exist**.

Nothing caught that. The equivalent staleness in `*_index.json` was caught within
seconds by tests/test_recipe_indexes.py, because that artifact has a guard and
this one did not. These tests close the asymmetry.

Refresh with `just refresh-id-registry`.
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY = REPO_ROOT / "data" / "culturemech_id_registry.tsv"
CORPUS = REPO_ROOT / "data" / "normalized_yaml"

ID_RE = re.compile(
    r"^id:\s*(?P<quote>['\"]?)(?P<id>CultureMech:(?!000000)\d{6})(?P=quote)\s*$",
    re.M,
)
STALE_HINT = "stale registry — refresh with `just refresh-id-registry`"


def _registry() -> dict[str, str]:
    rows: dict[str, str] = {}
    for i, line in enumerate(REGISTRY.read_text().splitlines()):
        if i == 0 or not line.strip():
            continue
        cid, _, path = line.partition("\t")
        rows[cid] = path
    return rows


def _corpus() -> dict[str, list[Path]]:
    found: dict[str, list[Path]] = defaultdict(list)
    for path in CORPUS.rglob("*.yaml"):
        match = ID_RE.search(path.read_text(errors="replace"))
        if match:
            found[match.group("id")].append(path)
    return found


@pytest.fixture(scope="module")
def registry():
    return _registry()


@pytest.fixture(scope="module")
def corpus():
    return _corpus()


def test_registry_is_not_empty(registry):
    """Guards the other tests — an empty parse would make them vacuous."""
    assert len(registry) > 10_000, f"only parsed {len(registry)} rows"


def test_every_yaml_has_exactly_one_canonical_id():
    """The dedicated ID gate must not silently skip missing or malformed IDs."""
    bad = []
    for path in CORPUS.rglob("*.yaml"):
        ids = [match.group("id") for match in ID_RE.finditer(path.read_text(errors="replace"))]
        if len(ids) != 1:
            bad.append(f"{path.relative_to(REPO_ROOT)}: {ids or 'no canonical id'}")
    assert not bad, f"{len(bad)} record(s) lack exactly one CultureMech:NNNNNN id: {bad[:3]}"


def test_every_registry_path_exists(registry):
    """The failure that actually happened: 5,511 rows pointing at moved files."""
    missing = [
        f"{cid} -> {path}" for cid, path in registry.items() if not (REPO_ROOT / path).is_file()
    ]
    assert not missing, (
        f"{len(missing)} registry row(s) point at files that do not exist "
        f"(e.g. {missing[:3]}) — {STALE_HINT}"
    )


def test_every_corpus_record_is_registered(registry, corpus):
    """The mirror failure: records added but never registered (51 of them)."""
    unregistered = sorted(set(corpus) - set(registry))
    assert not unregistered, (
        f"{len(unregistered)} record(s) carry an id absent from the registry "
        f"(e.g. {unregistered[:3]}) — {STALE_HINT}"
    )


def test_registry_paths_agree_with_where_the_id_actually_lives(registry, corpus):
    """A path can exist and still be wrong — two records swapping files would
    leave both rows resolvable but each pointing at the other's record."""
    wrong = []
    for cid, path in registry.items():
        actual = corpus.get(cid)
        if actual and (REPO_ROOT / path) != actual[0]:
            wrong.append(f"{cid}: registry={path} actual={actual[0].relative_to(REPO_ROOT)}")
    assert not wrong, f"{len(wrong)} row(s) point at the wrong record: {wrong[:3]}"


def test_no_id_appears_in_two_records(corpus):
    """Duplicate ids would make the registry ambiguous; `just assign-ids-check`
    is the dedicated gate, but the registry depends on this holding."""
    dupes = {
        cid: [str(p.relative_to(REPO_ROOT)) for p in paths]
        for cid, paths in corpus.items()
        if len(paths) > 1
    }
    assert not dupes, f"id(s) in more than one file: {dict(list(dupes.items())[:3])}"


def test_no_registered_id_is_missing_from_the_corpus(registry, corpus):
    """A row whose id exists nowhere means the record was deleted; the registry
    should not keep resolving it."""
    orphaned = sorted(set(registry) - set(corpus))
    assert not orphaned, (
        f"{len(orphaned)} registry id(s) have no record in the corpus "
        f"(e.g. {orphaned[:3]}) — {STALE_HINT}"
    )
