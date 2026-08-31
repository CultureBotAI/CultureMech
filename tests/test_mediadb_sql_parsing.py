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
