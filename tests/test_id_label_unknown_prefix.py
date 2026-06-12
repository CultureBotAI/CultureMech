"""Tests for the id-label validator's UNKNOWN_PREFIX gate.

A CURIE whose prefix is neither a configured ontology adapter NOR an explicit
``ignored_prefixes`` entry is a typo (``CHBEI:``) or an unexpected new prefix.
It must FAIL enforce (UNKNOWN_PREFIX, an ERROR verdict) rather than silently
passing as SKIPPED_NO_ADAPTER. Legit non-ontology prefixes (cas:, MIM: …) and
prefix-less ids (UNMAPPED_0001) stay benign skips.

Driven through ``run()`` end-to-end with a temp config + TSV using only
UNCONFIGURED prefixes, so no real OAK adapter / network is touched.
"""

import importlib.util
import textwrap
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "validate_id_label_correspondence",
    Path(__file__).parent.parent / "scripts" / "validate_id_label_correspondence.py",
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def _setup(tmp_path, monkeypatch, rows: str):
    monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
    (tmp_path / "products.tsv").write_text("ontology_id\tontology_label\n" + rows)
    cfg = tmp_path / "cfg.yaml"
    cfg.write_text(textwrap.dedent("""
        adapters: {}
        ignored_prefixes: [cas, MIM]
        synonym_scope: exact
        targets:
          - name: products
            kind: tabular
            format: tsv
            glob: products.tsv
            policy: canonical_or_synonym
            pairs:
              - [ontology_id, ontology_label]
    """))
    return cfg


def test_typoed_prefix_fails_enforce(tmp_path, monkeypatch):
    # CHBEI: is a typo of CHEBI: — neither adapter nor ignored → UNKNOWN_PREFIX.
    cfg = _setup(tmp_path, monkeypatch, "CHBEI:15377\twater\n")
    assert mod.run(cfg, report_path=None) == 2


def test_ignored_and_prefixless_pass_enforce(tmp_path, monkeypatch):
    # cas:/MIM: are explicitly ignored; UNMAPPED_1 has no CURIE prefix at all.
    cfg = _setup(
        tmp_path, monkeypatch,
        "cas:50-00-0\tformaldehyde\nMIM:000123\tfoo\nUNMAPPED_1\tmystery\n",
    )
    assert mod.run(cfg, report_path=None) == 0


def test_report_mode_still_exit_zero_but_records_unknown(tmp_path, monkeypatch):
    cfg = _setup(tmp_path, monkeypatch, "CHBEI:15377\twater\n")
    report = tmp_path / "drift.tsv"
    assert mod.run(cfg, report_path=report) == 0  # baseline mode never fails
    body = report.read_text()
    assert "UNKNOWN_PREFIX" in body and "CHBEI:15377" in body


def test_unknown_prefix_is_error_verdict():
    assert "UNKNOWN_PREFIX" in mod._ERROR_VERDICTS
