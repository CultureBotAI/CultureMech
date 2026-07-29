"""Tests for deciding a medium's domain from observed growth (#138).

The name-based audit leaves a residue whose names carry only a physiology —
"HALOPHILE MEDIUM" — and halophiles span both domains. Growth evidence answers it
from observation, and is decisive precisely where the name misleads:
Halobacillus/Virgibacillus are Bacillota, Halorubrum/Haladaptatus are
Halobacteriales.

These tests use synthetic lineages so they run without kg-microbe or the 13 GB
NCBITaxon build; the corpus-level check is skipped when those are absent.
"""
from __future__ import annotations

import importlib.util
import sqlite3
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def dge():
    return _load("domain_growth_evidence")


@pytest.fixture
def resolver(dge):
    """In-memory NCBITaxon slice: two real archaeal and two real bacterial genera."""
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE edge (subject TEXT, predicate TEXT, object TEXT)")
    edges = [
        # archaea: Halorubrum -> Halobacteriaceae -> ... -> Archaea
        ("NCBITaxon:1051914", "rdfs:subClassOf", "NCBITaxon:2236"),
        ("NCBITaxon:2236", "rdfs:subClassOf", "NCBITaxon:2157"),
        ("NCBITaxon:1179627", "rdfs:subClassOf", "NCBITaxon:2236"),
        # bacteria: Halobacillus / Salinicoccus -> Bacillota -> Bacteria
        ("NCBITaxon:45667", "rdfs:subClassOf", "NCBITaxon:1239"),
        ("NCBITaxon:1239", "rdfs:subClassOf", "NCBITaxon:2"),
        ("NCBITaxon:45669", "rdfs:subClassOf", "NCBITaxon:1239"),
        # a taxon whose lineage goes nowhere
        ("NCBITaxon:999999", "rdfs:subClassOf", "NCBITaxon:888888"),
    ]
    con.executemany("INSERT INTO edge VALUES (?,?,?)", edges)
    return dge.DomainResolver(con)


ARCH_A, ARCH_B = "NCBITaxon:1051914", "NCBITaxon:1179627"
BACT_A, BACT_B = "NCBITaxon:45667", "NCBITaxon:45669"
ORPHAN = "NCBITaxon:999999"


# --- lineage walk ---------------------------------------------------------


def test_resolves_archaeal_lineage(resolver):
    assert resolver.domain_of(ARCH_A) == "archaea"


def test_resolves_bacterial_lineage(resolver):
    assert resolver.domain_of(BACT_A) == "bacterial"


def test_unrooted_lineage_is_none(resolver):
    assert resolver.domain_of(ORPHAN) is None


def test_unknown_taxon_is_none(resolver):
    assert resolver.domain_of("NCBITaxon:404404") is None


def test_lineage_walk_is_memoised(resolver):
    assert resolver.domain_of(ARCH_A) == "archaea"
    assert resolver.domain_of(ARCH_A) == "archaea"
    assert resolver._cache[ARCH_A] == "archaea"


def test_cyclic_lineage_terminates(dge):
    """A malformed ontology must not hang the audit."""
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE edge (subject TEXT, predicate TEXT, object TEXT)")
    con.executemany("INSERT INTO edge VALUES (?,?,?)", [
        ("NCBITaxon:1", "rdfs:subClassOf", "NCBITaxon:2000"),
        ("NCBITaxon:2000", "rdfs:subClassOf", "NCBITaxon:1"),
    ])
    assert dge.DomainResolver(con).domain_of("NCBITaxon:1") is None


# --- verdicts -------------------------------------------------------------


def test_all_archaeal_growth_decides_archaea(dge, resolver):
    dom, detail = dge.domain_from_growth("m:1", {"m:1": {ARCH_A, ARCH_B}}, resolver)
    assert dom == "archaea"
    assert detail["n_taxa"] == 2 and detail["archaea"] == 2


def test_all_bacterial_growth_decides_bacterial(dge, resolver):
    dom, _ = dge.domain_from_growth("m:1", {"m:1": {BACT_A, BACT_B}}, resolver)
    assert dom == "bacterial"


def test_both_domains_refuses_to_decide(dge, resolver):
    """A medium supporting both is a curator's call, not an automatic move."""
    dom, detail = dge.domain_from_growth("m:1", {"m:1": {ARCH_A, BACT_A}}, resolver)
    assert dom is None
    assert "both domains" in detail["reason"]


def test_no_growth_evidence_is_none(dge, resolver):
    dom, detail = dge.domain_from_growth("m:absent", {}, resolver)
    assert dom is None and detail["n_taxa"] == 0


def test_orphan_taxa_never_decide(dge, resolver):
    dom, detail = dge.domain_from_growth("m:1", {"m:1": {ORPHAN}}, resolver)
    assert dom is None
    assert detail["unresolved"] == 1


def test_orphan_taxon_does_not_veto_a_clear_majority(dge, resolver):
    """The real moderate_halophile_medium case: 2 bacteria + 1 unresolvable."""
    dom, detail = dge.domain_from_growth("m:1", {"m:1": {BACT_A, BACT_B, ORPHAN}}, resolver)
    assert dom == "bacterial"
    assert detail["bacterial"] == 2 and detail["unresolved"] == 1


# --- graceful degradation -------------------------------------------------


def test_resolver_returns_none_when_kg_microbe_absent(dge, monkeypatch, tmp_path):
    """CI has no kg-microbe checkout; the audit must degrade, not error."""
    monkeypatch.setenv("KG_MICROBE_DIR", str(tmp_path / "nope"))
    monkeypatch.setattr(dge, "__file__", str(tmp_path / "a" / "b" / "scripts" / "x.py"))
    assert dge.resolve_kg_microbe_dir() is None


def test_env_override_is_honoured(dge, monkeypatch, tmp_path):
    md = tmp_path / "data" / "transformed" / "mediadive"
    md.mkdir(parents=True)
    (md / "edges.tsv").write_text("subject\tpredicate\tobject\n")
    monkeypatch.setenv("KG_MICROBE_DIR", str(tmp_path))
    assert dge.resolve_kg_microbe_dir() == tmp_path


def test_load_growth_edges_filters_predicate_and_subject(dge, tmp_path):
    md = tmp_path / "data" / "transformed" / "mediadive"
    md.mkdir(parents=True)
    (md / "edges.tsv").write_text(
        "subject\tpredicate\tobject\n"
        "NCBITaxon:1\tMETPO:2000517\tmediadive.medium:9\n"       # keep
        "NCBITaxon:2\tbiolink:has_phenotype\tMETPO:1\n"          # wrong predicate
        "mediadive.solution:5\tMETPO:2000517\tmediadive.medium:9\n"  # not a taxon
    )
    edges = dge.load_growth_edges(tmp_path)
    assert edges == {"mediadive.medium:9": {"NCBITaxon:1"}}


# --- against the real corpus ----------------------------------------------


def test_growth_evidence_contradicts_the_halophile_naming(dge):
    """The finding that motivates this: names read archaeal, organisms are not.

    Skipped without kg-microbe + the NCBITaxon build.
    """
    kg = dge.resolve_kg_microbe_dir()
    db = Path.home() / ".data" / "oaklib" / "ncbitaxon.db"
    if kg is None or not db.is_file():
        pytest.skip("kg-microbe checkout and/or NCBITaxon sqlite not available")

    growth = dge.load_growth_edges(kg)
    resolver = dge.DomainResolver(sqlite3.connect(db))

    # JCM_J464_HP_101_HALOPHILE_MEDIUM — Halobacillus/Virgibacillus, i.e. bacteria
    dom, detail = dge.domain_from_growth("mediadive.medium:J464", growth, resolver)
    assert dom == "bacterial", detail

    # DSMZ_1399_HALOPHILIC_MEDIUM — Halogeometricum/Halomicrobium, i.e. archaea
    dom, detail = dge.domain_from_growth("mediadive.medium:1399", growth, resolver)
    assert dom == "archaea", detail
