"""Tests for scripts/audit_domain_categories.py.

Covers the classification rules that decide whether a recipe is mis-filed by
domain (#114 / #116) and the target-naming rule that keeps a move from
overwriting another recipe.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    path = REPO_ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


audit = _load("audit_domain_categories")


def _evidence(taxa=(), binomials=(), words=r"(?!x)x"):
    return audit.Evidence(
        taxa=set(taxa), binomials=set(binomials), words=re.compile(words)
    )


def _classify(stem, archaea, bacteria):
    rec = audit.Recipe(path=Path(f"{stem}.yaml"))
    audit.classify(rec, archaea, bacteria)
    return rec


# --- taxon / binomial / generic-word evidence --------------------------------


def test_genus_in_filename_is_archaeal_evidence():
    rec = _classify(
        "methanogenium_medium", _evidence(taxa={"methanogenium"}), _evidence()
    )
    assert rec.archaeal == ["methanogenium"]
    assert rec.bacterial == []


def test_binomial_recovers_a_cross_domain_homonym_genus():
    """*Bacillus* is also a diatom genus, so the bare genus is dropped as a
    homonym; the full binomial still identifies the record as bacterial."""
    bacteria = _evidence(binomials={"bacillus stearothermophilus"})
    rec = _classify("medium_for_bacillus_stearothermophilus", _evidence(), bacteria)
    assert rec.bacterial == ["bacillus stearothermophilus"]
    assert rec.archaeal == []


def test_generic_wording_is_used_only_when_no_taxon_matches():
    archaea = _evidence(taxa={"methanogenium"}, words=r"\bmethanogen\b")
    rec = _classify("methanogen_high_salt_medium", archaea, _evidence())
    assert rec.archaeal == ["methanogen"]


def test_a_record_naming_both_domains_is_mixed():
    rec = _classify(
        "methanosaeta_brevibacterium_medium",
        _evidence(taxa={"methanosaeta"}),
        _evidence(taxa={"brevibacterium"}),
    )
    assert rec.mixed


def test_species_epithet_does_not_count_as_the_other_domains_genus():
    """*Methanocalculus alkaliphilus* is an archaeon. Matching the bacterial
    genus *Alkaliphilus* on its species epithet must not make it look mixed."""
    archaea = _evidence(
        taxa={"methanocalculus"}, binomials={"methanocalculus alkaliphilus"}
    )
    bacteria = _evidence(taxa={"alkaliphilus"})
    rec = _classify("methanocalculus_alkaliphilus_medium", archaea, bacteria)
    assert not rec.mixed
    assert rec.bacterial == []


def test_a_genuine_genus_match_survives_the_epithet_rule():
    """The epithet rule must not swallow a genus that appears on its own."""
    archaea = _evidence(taxa={"methanocalculus"}, binomials={"methanocalculus alkaliphilus"})
    bacteria = _evidence(taxa={"brevibacterium"})
    rec = _classify("methanocalculus_brevibacterium_medium", archaea, bacteria)
    assert rec.bacterial == ["brevibacterium"]
    assert rec.mixed


# --- target naming -----------------------------------------------------------


def test_free_target_keeps_the_original_filename(tmp_path):
    dest = tmp_path / "archaea"
    dest.mkdir()
    rec = audit.Recipe(path=tmp_path / "foo_medium.yaml")
    assert audit.target_path(rec, dest, set()).name == "foo_medium.yaml"


def test_taken_target_gets_a_source_prefix(tmp_path):
    dest = tmp_path / "archaea"
    dest.mkdir()
    (dest / "foo_medium.yaml").write_text("id: CultureMech:1\n")
    rec = audit.Recipe(
        path=tmp_path / "foo_medium.yaml",
        original_name="Foo Medium",
        source_id="TOGO_M1",
    )
    assert audit.target_path(rec, dest, set()).name == "TOGO_M1_Foo_Medium.yaml"


def test_targets_are_reserved_so_two_recipes_never_collide(tmp_path):
    """Every target is chosen before any file moves, so an existence check alone
    would hand the same name to two recipes and destroy one of them."""
    dest = tmp_path / "archaea"
    dest.mkdir()
    (dest / "foo_medium.yaml").write_text("id: CultureMech:1\n")
    reserved: set[Path] = set()

    def new_target():
        rec = audit.Recipe(
            path=tmp_path / "foo_medium.yaml",
            original_name="Foo Medium",
            source_id="TOGO_M1",
        )
        return audit.target_path(rec, dest, reserved)

    names = [new_target().name for _ in range(3)]
    assert len(set(names)) == 3, names


# --- provenance --------------------------------------------------------------


@pytest.mark.parametrize(
    ("notes", "expected"),
    [
        ("notes: 'Source: DSMZ | Link: x'", "DSMZ_74"),
        ("notes: 'Source: JCM | Link: x'", "JCM_74"),
        ("notes: 'Source: MediaDive'", "mediadive_74"),
    ],
)
def test_mediadive_ids_are_prefixed_by_the_originating_registry(
    tmp_path, notes, expected
):
    """MediaDive republishes DSMZ and JCM media; the corpus names them by the
    originating registry and reserves `mediadive_` for stock solutions."""
    path = tmp_path / "r.yaml"
    path.write_text(
        "id: CultureMech:1\nname: r\ncategory: archaea\n"
        f"media_term:\n  term:\n    id: mediadive.medium:74\n{notes}\n"
    )
    assert audit.read_recipe(path).source_id == expected


def test_record_level_notes_win_over_ingredient_notes(tmp_path):
    path = tmp_path / "r.yaml"
    path.write_text(
        "id: CultureMech:1\nname: r\ncategory: archaea\n"
        "ingredients:\n- preferred_term: x\n  notes: 'Source: KOMODO'\n"
        "notes: 'Source: DSMZ'\n"
    )
    assert audit.read_recipe(path).source == "DSMZ"


def test_restamp_category_reports_when_there_is_nothing_to_stamp(tmp_path):
    stamped = tmp_path / "a.yaml"
    stamped.write_text("id: CultureMech:1\ncategory: bacterial\n")
    assert audit.restamp_category(stamped, "archaea") is True
    assert "category: archaea" in stamped.read_text()

    bare = tmp_path / "b.yaml"
    bare.write_text("id: CultureMech:2\n")
    assert audit.restamp_category(bare, "archaea") is False
