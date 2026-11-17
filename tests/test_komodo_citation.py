"""Regression tests for KOMODO source citation metadata (#784)."""

from __future__ import annotations

import csv
import inspect
import json
from importlib import import_module
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.fast
def test_media_sources_tsv_komodo_row_citation_and_columns() -> None:
    """Verify MEDIA_SOURCES.tsv retains 13 columns per row and points to ncomms9493."""
    tsv_path = ROOT / "data" / "MEDIA_SOURCES.tsv"
    with tsv_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle, delimiter="\t"))

    assert rows, "MEDIA_SOURCES.tsv must not be empty"
    header = rows[0]
    assert len(header) == 13
    for idx, row in enumerate(rows[1:], start=2):
        assert len(row) == 13, f"Row {idx} has {len(row)} columns instead of 13"

    komodo_rows = [row for row in rows[1:] if row[0] == "KOMODO"]
    assert len(komodo_rows) == 1
    komodo = dict(zip(header, komodo_rows[0], strict=True))
    assert komodo["synonyms"] == "KOMODO|Known Media Database"
    assert komodo["url"] == "https://www.nature.com/articles/ncomms9493"


@pytest.mark.fast
def test_komodo_modules_cite_oberhardt_2015(tmp_path: Path) -> None:
    """Verify KOMODO importer and fetchers carry the canonical Oberhardt et al. (2015) citation."""
    komodo_importer_mod = import_module("culturemech.import.komodo_importer")
    komodo_fetcher_mod = import_module("culturemech.fetch.komodo_fetcher")
    komodo_web_fetcher_mod = import_module("culturemech.fetch.komodo_web_fetcher")

    for mod in (komodo_importer_mod, komodo_fetcher_mod):
        doc = mod.__doc__ or ""
        assert "Oberhardt et al. (2015)" in doc
        assert "10.1038/ncomms9493" in doc
        assert "Zarecki et al. (2015)" not in doc
        assert "Knowledge base Of Microbial" not in doc

    web_source = inspect.getsource(komodo_web_fetcher_mod)
    assert "Oberhardt et al. (2015)" in web_source
    assert "KOMODO (Known Media Database)" in web_source
    assert "Zarecki et al. (2015)" not in web_source
    assert "Knowledge base Of Microbial" not in web_source

    for name in ("komodo_media.json", "komodo_compounds.json", "komodo_organisms.json"):
        (tmp_path / name).write_text(json.dumps({"data": []}), encoding="utf-8")

    out_dir = tmp_path / "out"
    out_dir.mkdir()

    class DummyMapper:
        pass

    importer = komodo_importer_mod.KOMODOImporter(
        komodo_data_dir=tmp_path,
        output_dir=out_dir,
        chemical_mapper=DummyMapper(),
    )
    history = importer._create_curation_history({"id": "1"})
    assert len(history) == 1
    notes = history[0]["notes"]
    assert "Source: KOMODO (Known Media Database)" in notes
    assert (
        "Reference: Oberhardt et al. (2015), Nature Communications 6:8493 "
        "(doi:10.1038/ncomms9493; PMID:26460590)"
    ) in notes
    assert "Zarecki" not in notes
