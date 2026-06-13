"""Tests for the id-label validator's ``exceptions`` allow-list (OK_EXCEPTION).

A curator-accepted residual — an exact ``(id, label)`` pair the ontology
disagrees with because the canonical term is wrong/obsolete/unminted, or the id
is absent from the current snapshot — is listed under a target's ``exceptions``
and accepted as ``OK_EXCEPTION`` (non-error). The match is EXACT, so:

* a residual on the list overrides MISMATCH and ID_NOT_FOUND → enforce passes;
* a DIFFERENT wrong label on the same id is NOT on the list → still MISMATCH
  (the allow-list can't mask drift it didn't explicitly accept);
* with no ``exceptions`` configured the residual fails as before.

Driven through ``run()`` end-to-end with a fake adapter + temp config, so no
real OAK adapter / network is touched.
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


class _Adapter:
    """Fake OAK adapter: CHEBI:33104 resolves to a canonical label that differs
    from the curator's; everything else is absent (label() -> None)."""

    _LABELS = {"CHEBI:33104": "chromium hydroxide"}

    def label(self, curie):
        return self._LABELS.get(curie)

    def entities(self):
        return iter(self._LABELS)

    def entity_alias_map(self, curie):
        return {}


def _setup(tmp_path, monkeypatch, body_yaml, exceptions_block):
    import oaklib

    monkeypatch.setattr(oaklib, "get_adapter", lambda sel: _Adapter())
    monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
    (tmp_path / "f.yaml").write_text(body_yaml)
    cfg = tmp_path / "cfg.yaml"
    cfg.write_text(textwrap.dedent("""
            adapters: {CHEBI: 'sqlite:obo:chebi'}
            ignored_prefixes: []
            synonym_scope: exact
            targets:
              - name: t
                kind: yaml
                glob: f.yaml
                policy: canonical
                pairs: [[id, label]]
                exceptions:
            """) + exceptions_block)
    return cfg


_EXC = "      - { id: 'CHEBI:33104', label: 'chromium(III) hydroxide', reason: 'no clean term' }\n"


def test_residual_on_allowlist_passes_enforce(tmp_path, monkeypatch):
    # id resolves but canonical != curator label; pair IS on the allow-list.
    cfg = _setup(
        tmp_path, monkeypatch, "x:\n  id: CHEBI:33104\n  label: chromium(III) hydroxide\n", _EXC
    )
    assert mod.run(cfg, report_path=None) == 0


def test_different_wrong_label_same_id_still_fails(tmp_path, monkeypatch):
    # same id, a DIFFERENT label that is NOT on the list -> must still MISMATCH.
    cfg = _setup(tmp_path, monkeypatch, "x:\n  id: CHEBI:33104\n  label: totally wrong\n", _EXC)
    assert mod.run(cfg, report_path=None) == 2


def test_absent_id_on_allowlist_passes_enforce(tmp_path, monkeypatch):
    # id absent from the snapshot (ID_NOT_FOUND) but on the list -> OK_EXCEPTION.
    exc = "      - { id: 'CHEBI:99999', label: 'absent thing', reason: 'absent from snapshot' }\n"
    cfg = _setup(tmp_path, monkeypatch, "x:\n  id: CHEBI:99999\n  label: absent thing\n", exc)
    assert mod.run(cfg, report_path=None) == 0


def test_no_exceptions_residual_fails(tmp_path, monkeypatch):
    cfg = _setup(
        tmp_path,
        monkeypatch,
        "x:\n  id: CHEBI:33104\n  label: chromium(III) hydroxide\n",
        "      []\n",
    )
    assert mod.run(cfg, report_path=None) == 2


def test_ok_exception_is_not_an_error_verdict():
    assert "OK_EXCEPTION" not in mod._ERROR_VERDICTS
    assert "OK_EXCEPTION" in mod._OK_VERDICTS
