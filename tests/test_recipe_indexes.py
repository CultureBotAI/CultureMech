"""Guard that the committed recipe indexes match the directories they describe (#125).

`data/normalized_yaml/*_index.json` are committed artifacts, so staleness is not
visible as staleness — they look authoritative. They sat at their 2026-03-16
generation for four months while the corpus grew, ending up ~5,000 recipes short
(bacterial indexed 10,136 vs 14,275 actual; archaea 63 vs 773). Anything
enumerating recipes through an index rather than globbing silently saw about a
third less corpus.

Each entry also records a `filename`, so the bulk category moves in #115 and #120
left stale paths even where the id was still present — hence the path check, not
just a count check.

Regenerate with `just generate-indexes data/normalized_yaml`.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
NORMALIZED = REPO_ROOT / "data" / "normalized_yaml"

# Category indexes describe a sibling directory of the same name. The
# by_source_*/recipe/statistics indexes are cross-cutting and have no single
# directory to compare against.
CATEGORY_INDEXES = sorted(
    p for p in NORMALIZED.glob("*_index.json")
    if not p.name.startswith(("by_source_", "recipe_"))
    and (NORMALIZED / p.name.replace("_index.json", "")).is_dir()
)

STALE_HINT = "stale index — regenerate with `just generate-indexes data/normalized_yaml`"


def _load(index_path: Path) -> tuple[dict, Path]:
    doc = json.loads(index_path.read_text())
    category_dir = NORMALIZED / index_path.name.replace("_index.json", "")
    return doc, category_dir


def test_category_indexes_were_discovered():
    """Guards the parametrization itself — an empty list would vacuously pass."""
    assert len(CATEGORY_INDEXES) >= 5, f"expected the category indexes, found {CATEGORY_INDEXES}"


@pytest.mark.parametrize("index_path", CATEGORY_INDEXES, ids=lambda p: p.name)
def test_index_count_matches_directory(index_path: Path):
    doc, category_dir = _load(index_path)
    actual = len(list(category_dir.glob("*.yaml")))
    assert doc["count"] == actual, (
        f"{index_path.name} reports {doc['count']} recipes but "
        f"{category_dir.name}/ holds {actual} — {STALE_HINT}"
    )


@pytest.mark.parametrize("index_path", CATEGORY_INDEXES, ids=lambda p: p.name)
def test_index_entry_count_matches_count_field(index_path: Path):
    doc, _ = _load(index_path)
    assert len(doc["recipes"]) == doc["count"], (
        f"{index_path.name} `count` disagrees with the number of entries it holds"
    )


@pytest.mark.parametrize("index_path", CATEGORY_INDEXES, ids=lambda p: p.name)
def test_index_filenames_all_exist(index_path: Path):
    """A renamed or moved recipe leaves a stale `filename` even when its id is present."""
    doc, category_dir = _load(index_path)
    missing = [
        entry["filename"]
        for entry in doc["recipes"].values()
        if not (category_dir / entry["filename"]).is_file()
    ]
    assert not missing, (
        f"{index_path.name} points at {len(missing)} file(s) not present in "
        f"{category_dir.name}/ (e.g. {missing[:3]}) — {STALE_HINT}"
    )


@pytest.mark.parametrize("index_path", CATEGORY_INDEXES, ids=lambda p: p.name)
def test_every_yaml_in_the_directory_is_indexed(index_path: Path):
    """The failure mode that actually bit: recipes present on disk, absent from the index."""
    doc, category_dir = _load(index_path)
    indexed = {entry["filename"] for entry in doc["recipes"].values()}
    on_disk = {p.name for p in category_dir.glob("*.yaml")}
    unindexed = sorted(on_disk - indexed)
    assert not unindexed, (
        f"{len(unindexed)} recipe(s) in {category_dir.name}/ are missing from "
        f"{index_path.name} (e.g. {unindexed[:3]}) — {STALE_HINT}"
    )
