"""MediaDB SQL rows must survive parentheses and escaped quotes.

Chemical names are full of both — oxidation states (`Iron(III) chloride`),
stereo descriptors (`(S)-Malate`), and primes (`Pantetheine 4'-phosphate`) —
and two parsing bugs cut them in half.

`_parse_*_insert` split records with `re.findall(r'\\(([^)]+)\\)', ...)`, whose
`[^)]+` stops at the FIRST closing paren, so

    (16413,NULL,NULL,'Iron(III) chloride','','24380','30808','FeCl3')

became the four fields `16413, NULL, NULL, 'Iron(III`. That fragment reached
the corpus as an ingredient name in 75 recipes (#387).

`_split_sql_values` then tracked quotes without honouring backslash escapes, so
a prime written `4\\'-phosphate` read as the end of the string and every later
comma in the row split in the wrong place — 48 more compound names.

Every literal here is copied from `data/raw/mediadb/media_database.07Oct2015.sql`.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from culturemech.fetch.mediadb_fetcher import MediaDBFetcher


@pytest.fixture
def fetcher(tmp_path) -> MediaDBFetcher:
    return MediaDBFetcher(output_dir=tmp_path)


# --- record splitting ----------------------------------------------------


def test_a_value_containing_a_paren_does_not_truncate_the_record(fetcher):
    records = fetcher._split_sql_records(
        "(16413,NULL,NULL,'Iron(III) chloride','','24380','30808','FeCl3')"
    )
    assert records == ["16413,NULL,NULL,'Iron(III) chloride','','24380','30808','FeCl3'"]


def test_consecutive_records_are_separated(fetcher):
    records = fetcher._split_sql_records("(1,'a'),(2,'b(c)'),(3,'d')")
    assert records == ["1,'a'", "2,'b(c)'", "3,'d'"]


def test_a_paren_inside_quotes_does_not_open_a_record(fetcher):
    """`m7G(5')pppAn` carries an unbalanced-looking paren and a prime."""
    records = fetcher._split_sql_records("(1714,'C01973','','m7G(5')pppAn','cpd11982')")
    assert len(records) == 1


def test_an_escaped_quote_does_not_end_the_string(fetcher):
    records = fetcher._split_sql_records("(1039,'Pantetheine 4\\'-phosphate','x')")
    assert records == ["1039,'Pantetheine 4\\'-phosphate','x'"]


# --- field splitting -----------------------------------------------------


def test_an_escaped_quote_keeps_the_field_boundaries(fetcher):
    parts = fetcher._split_sql_values(
        "1039,'C01134','pan4p','Pantetheine 4\\'-phosphate','cpd00834'"
    )
    assert len(parts) == 5
    assert fetcher._clean_sql_value(parts[3]) == "Pantetheine 4'-phosphate"


def test_a_comma_inside_a_quoted_field_is_not_a_separator(fetcher):
    """`chebi_ids` legitimately holds `'16858,4222'`."""
    parts = fetcher._split_sql_values("1039,'16858,4222','C11H23N2O7PS'")
    assert len(parts) == 3
    assert fetcher._clean_sql_value(parts[1]) == "16858,4222"


# --- the compounds column mapping ---------------------------------------


def test_the_compound_columns_follow_the_dumps_own_schema(fetcher):
    """`compID | KEGG_ID | BiGG_ID | name | seed_id | pubchem | chebi | formula`.

    The old mapping read parts[1] as the name — that is KEGG_ID — and parts[3],
    the real name, as the ChEBI id. On row 1 that gave name='C00001' and
    chebi_id='Water'.
    """
    fetcher._parse_compound_insert("(1,'C00001','h2o','Water','cpd00001','444718','15377','H2O')")
    assert fetcher.compounds["1"] == {
        "id": "1",
        "name": "Water",
        "kegg_id": "C00001",
        "bigg_id": "h2o",
        "chebi_id": "15377",
        "formula": "H2O",
    }


def test_a_null_column_becomes_empty_not_the_string_NULL(fetcher):
    fetcher._parse_compound_insert(
        "(16413,NULL,NULL,'Iron(III) chloride','','24380','30808','FeCl3')"
    )
    compound = fetcher.compounds["16413"]
    assert compound["name"] == "Iron(III) chloride"
    assert compound["kegg_id"] == ""
    assert compound["formula"] == "FeCl3"


# --- against the real dump ----------------------------------------------

DUMP = Path(__file__).resolve().parents[1] / "data/raw/mediadb/media_database.07Oct2015.sql"


@pytest.mark.skipif(not DUMP.exists(), reason="raw MediaDB dump is not present locally")
def test_the_real_dump_parses_without_fragmenting_names(fetcher):
    """The end-to-end check: no compound name may look like a cut-off fragment.

    Four names legitimately end in a prime (`Premithramycin A2'`,
    `Nebramycin factor 5'`, `Nebramycin factor 4'`, `R'C(R)S-S(R)CR'`), so the
    assertion is about fragments — a name still carrying a field separator, or
    one opening with a quote it never closes.
    """
    assert fetcher.parse_sql_dump(DUMP)
    assert len(fetcher.compounds) > 14000

    fragments = [
        compound
        for compound in fetcher.compounds.values()
        if compound["name"].startswith("'") or "','" in compound["name"]
    ]
    assert fragments == [], f"{len(fragments)} names are still fragments"

    # The three the corpus damage came from.
    by_id = fetcher.compounds
    assert by_id["16413"]["name"] == "Iron(III) chloride"
    assert by_id["16416"]["name"] == "Chromium(III) Chloride"
    assert by_id["1"]["name"] == "Water"


# --- the importer's stale-export guard ----------------------------------


def _importer_class():
    from importlib import import_module

    module = import_module("culturemech.import.mediadb_importer")
    return next(
        value
        for name, value in vars(module).items()
        if name.endswith("Importer") and isinstance(value, type)
    )


def _export(tmp_path: Path, compounds: list[dict]) -> Path:
    import json

    directory = tmp_path / "mediadb"
    directory.mkdir()
    for name, payload in (
        ("mediadb_compounds.json", compounds),
        ("mediadb_media.json", []),
        ("mediadb_organisms.json", []),
    ):
        (directory / name).write_text(json.dumps({"count": len(payload), "data": payload}))
    return directory


def test_a_correct_export_is_accepted(tmp_path):
    directory = _export(
        tmp_path,
        [{"id": "1", "name": "Water", "kegg_id": "C00001", "bigg_id": "h2o", "chebi_id": "15377"}],
    )
    assert _importer_class()(str(directory), str(tmp_path / "out")).compounds


def test_an_unnamed_compound_is_not_mistaken_for_damage(tmp_path):
    """Four MediaDB compounds genuinely carry their KEGG id as the name.

    `{'name': 'C15810', 'kegg_id': 'C15810'}` is real data. A guard that counted
    KEGG-shaped names alone refused the correct export — verified, it did.
    """
    directory = _export(
        tmp_path,
        [{"id": "14209", "name": "C15810", "kegg_id": "C15810", "bigg_id": "", "chebi_id": ""}],
    )
    assert _importer_class()(str(directory), str(tmp_path / "out")).compounds


def test_a_shifted_export_is_refused(tmp_path):
    """The pre-#387 shape: name holds the KEGG id, kegg_id holds the BiGG id."""
    directory = _export(
        tmp_path,
        [{"id": "145", "name": "C00149", "kegg_id": "mal-L", "chebi_id": "'(S"}],
    )
    with pytest.raises(RuntimeError, match="pre-#387 SQL parser"):
        _importer_class()(str(directory), str(tmp_path / "out"))


def test_a_truncated_chebi_id_alone_is_enough_to_refuse(tmp_path):
    directory = _export(
        tmp_path,
        [{"id": "16413", "name": "Iron", "kegg_id": "", "chebi_id": "'Iron(III"}],
    )
    with pytest.raises(RuntimeError, match="truncated"):
        _importer_class()(str(directory), str(tmp_path / "out"))


# --- medium-name damage -------------------------------------------------


def test_a_leading_quote_marks_a_truncated_medium_name():
    from repair_mediadb_names import damaged_medium_name

    assert damaged_medium_name("'Defined freshwater medium (CoSO4")


def test_a_glued_field_tail_marks_a_damaged_medium_name():
    """From the escaped-quote bug: `Spizizen's medium` glued the next field on."""
    from repair_mediadb_names import damaged_medium_name

    assert damaged_medium_name("Spizizen's medium ... Nakano et al','N")


def test_a_healthy_medium_name_is_left_alone():
    from repair_mediadb_names import damaged_medium_name

    assert not damaged_medium_name("M9 (gupta) with lactose")
    assert not damaged_medium_name("Defined freshwater medium (CoSO4) + 100 mM Fe2O3")


def test_trailing_whitespace_is_not_damage():
    """`'Supplemented BG11 + Glucose '` is the dump's own value, space and all."""
    from repair_mediadb_names import damaged_medium_name

    assert not damaged_medium_name("Supplemented BG11 + Glucose ")


def test_the_medium_name_repair_touches_only_the_two_damaged_fields():
    from repair_mediadb_names import repair_medium_name

    record = {
        "name": "m9_gupta",
        "original_name": "'M9 (gupta",
        "media_term": {
            "preferred_term": "MediaDB Medium 109",
            "term": {"id": "MEDIADB:109", "label": "'M9 (gupta"},
        },
    }
    changed = repair_medium_name(record, "M9 (gupta) with lactose")

    assert sorted(changed) == ["media_term.term.label", "original_name"]
    assert record["original_name"] == "M9 (gupta) with lactose"
    assert record["media_term"]["term"]["label"] == "M9 (gupta) with lactose"
    # The id and the record slug are identifiers; the repair must not touch them.
    assert record["media_term"]["term"]["id"] == "MEDIADB:109"
    assert record["media_term"]["preferred_term"] == "MediaDB Medium 109"
    assert record["name"] == "m9_gupta"


def test_an_undamaged_record_is_not_rewritten():
    from repair_mediadb_names import repair_medium_name

    record = {
        "original_name": "M9 (gupta) with lactose",
        "media_term": {"term": {"id": "MEDIADB:109", "label": "M9 (gupta) with lactose"}},
    }
    assert repair_medium_name(record, "Something Else Entirely") == []
    assert record["original_name"] == "M9 (gupta) with lactose"
