"""Tests for the id-label validator's empty-adapter detection.

A configured OAK adapter that loads but holds no terms (OAK's ``sqlite:obo:micro``
selector points at a 0-byte stub whose tables don't exist) must NOT flag every id
under that prefix as a false ``ID_NOT_FOUND`` — it is reclassified as the benign
``SKIPPED_EMPTY_ADAPTER``.

Crucially, a PARTIALLY-MIGRATED or corrupt LIVE ontology (real tables, one
missing) raises the same ``no such table`` error but must NOT be masked as a
benign skip — that would let real drift pass an enforce run. So "empty" is
decided by a POSITIVE stub check (0-byte / 0-table backing sqlite), never by the
error text alone. These pin that distinction with fake adapters + tiny on-disk
sqlite files (CI-safe, no OAK / network).
"""

import importlib.util
import sqlite3
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "validate_id_label_correspondence",
    Path(__file__).parent.parent / "scripts" / "validate_id_label_correspondence.py",
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


class _URL:
    def __init__(self, database):
        self.database = database


class _Engine:
    def __init__(self, database):
        self.url = _URL(database)


class _Adapter:
    """Fake OAK adapter: entities() yields `items` or raises `exc`; optional
    `db` path exposed via .engine.url.database (mimics OAK's SqlImplementation)."""

    def __init__(self, items=(), exc=None, db=None):
        self._items, self._exc = list(items), exc
        self.engine = _Engine(db) if db is not None else None

    def entities(self):
        if self._exc:
            raise self._exc
        return iter(self._items)


_NO_SUCH_TABLE = Exception("(sqlite3.OperationalError) no such table: node")


# -- _is_uninitialized_stub: the positive empty-stub check ------------------

def test_stub_true_for_zero_byte_file(tmp_path):
    p = tmp_path / "micro.db"
    p.touch()  # 0 bytes
    assert mod.AdapterPool._is_uninitialized_stub(_Adapter(db=str(p))) is True


def test_stub_true_for_tableless_sqlite(tmp_path):
    p = tmp_path / "empty.db"
    sqlite3.connect(str(p)).close()  # valid sqlite, no tables
    assert mod.AdapterPool._is_uninitialized_stub(_Adapter(db=str(p))) is True


def test_stub_false_for_sqlite_with_tables(tmp_path):
    p = tmp_path / "live.db"
    con = sqlite3.connect(str(p))
    con.execute("CREATE TABLE statements (subject TEXT)")
    con.commit()
    con.close()
    # has tables → a real (possibly broken) db, never a benign stub
    assert mod.AdapterPool._is_uninitialized_stub(_Adapter(db=str(p))) is False


def test_stub_false_for_missing_path(tmp_path):
    assert mod.AdapterPool._is_uninitialized_stub(_Adapter(db=str(tmp_path / "nope.db"))) is False


def test_stub_false_when_no_engine():
    assert mod.AdapterPool._is_uninitialized_stub(_Adapter()) is False


# -- _is_empty: combines the probe with the positive stub check -------------

def test_empty_when_no_entities():
    assert mod.AdapterPool._is_empty(_Adapter(items=[]), "x") is True


def test_empty_when_probe_raises_and_db_is_zero_byte(tmp_path):
    p = tmp_path / "micro.db"
    p.touch()
    assert mod.AdapterPool._is_empty(_Adapter(exc=_NO_SUCH_TABLE, db=str(p)), "micro") is True


def test_NOT_empty_when_probe_raises_but_db_has_tables(tmp_path):
    # THE REGRESSION GUARD: partially-migrated live db (tables present, one
    # missing) raises "no such table" yet must NOT be masked as empty.
    p = tmp_path / "chebi.db"
    con = sqlite3.connect(str(p))
    con.execute("CREATE TABLE statements (subject TEXT)")
    con.commit()
    con.close()
    assert mod.AdapterPool._is_empty(_Adapter(exc=_NO_SUCH_TABLE, db=str(p)), "chebi") is False


def test_NOT_empty_on_no_such_table_without_resolvable_db():
    # error text alone is never enough — no path to confirm a stub → not empty.
    assert mod.AdapterPool._is_empty(_Adapter(exc=_NO_SUCH_TABLE), "chebi") is False


def test_empty_vs_nonempty_with_arbitrary_error(tmp_path):
    p = tmp_path / "x.db"
    p.touch()  # 0-byte stub still wins regardless of error text
    assert mod.AdapterPool._is_empty(_Adapter(exc=Exception("disk I/O error"), db=str(p)), "x") is True
    con = sqlite3.connect(str(p))  # now give it a table
    con.execute("CREATE TABLE t (x)")
    con.commit()
    con.close()
    # non-stub db + arbitrary probe error → stays non-empty (not masked)
    assert mod.AdapterPool._is_empty(_Adapter(exc=Exception("disk I/O error"), db=str(p)), "x") is False


def test_populated_adapter_not_empty():
    assert mod.AdapterPool._is_empty(_Adapter(items=["CHEBI:15377"]), "chebi") is False


def test_pool_get_returns_empty_sentinel(monkeypatch, tmp_path):
    p = tmp_path / "micro.db"
    p.touch()  # 0-byte stub
    import oaklib

    monkeypatch.setattr(oaklib, "get_adapter", lambda sel: _Adapter(exc=_NO_SUCH_TABLE, db=str(p)))
    pool = mod.AdapterPool({"MICRO": "sqlite:obo:micro"})
    assert pool.get("MICRO") is mod.EMPTY_ADAPTER
    assert pool.get("micro") is mod.EMPTY_ADAPTER  # case-insensitive


def test_empty_adapter_not_an_error_verdict():
    assert "SKIPPED_EMPTY_ADAPTER" not in mod._ERROR_VERDICTS
