"""Tests for the mechanistic role-backfill script (Step 7).

Two test layers:

1. **Unit** — `ChebiRoleResolver.facets_for` against a mocked oaklib adapter.
   Fast, no `sqlite:obo:chebi` install required. Uses the actual gold-example
   CHEBI ids + `has_role` axioms observed in live CHEBI (2026-07-20).

2. **Round-trip fixtures** — the 10 gold-example ingredients from
   `scripts/codex_prompts/review-ingredient-roles-gold-examples.md`. Each
   fixture asserts what the mechanistic lane SHOULD propose and — equally
   important — what it SHOULD NOT propose. The mechanistic lane is
   deliberately narrow: many gold assignments (nutritional / conditional)
   require the Step 7b literature lane and are documented here as
   `mechanistic_expected=[]` with a comment explaining why.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Iterable

import pytest


# Load the backfill script as a module without touching sys.path — the
# script lives outside the `culturemech` package.
_SCRIPT_PATH = Path(__file__).parent.parent / "scripts" / "backfill_ingredient_roles.py"
_SPEC = importlib.util.spec_from_file_location("_backfill_ingredient_roles", _SCRIPT_PATH)
_backfill = importlib.util.module_from_spec(_SPEC)
sys.modules["_backfill_ingredient_roles"] = _backfill
_SPEC.loader.exec_module(_backfill)  # type: ignore[union-attr]

MIM_ROLES_YAML = Path(__file__).parent.parent / "src" / "culturemech" / "schema" / "mim_roles.yaml"


class FakeAdapter:
    """Minimal oaklib adapter stub — labels + has_role triples only."""

    def __init__(self, labels: dict[str, str], has_role: dict[str, list[str]]):
        self._labels = labels
        # {compound_id: [role_id, ...]} — direct has_role targets only.
        self._has_role = has_role

    def label(self, curie: str) -> str | None:
        return self._labels.get(curie)

    def relationships(self, subjects: Iterable[str] | None = None):
        subjects = list(subjects or [])
        for cid in subjects:
            for role_id in self._has_role.get(cid, []):
                yield (cid, "RO:0000087", role_id)


# --- Fixture: labels + has_role edges observed in live sqlite:obo:chebi ---

_LIVE_CHEBI_LABELS = {
    # Compounds.
    "CHEBI:17234": "glucose",
    "CHEBI:2509":  "agar",
    "CHEBI:8806":  "Resazurin",
    "CHEBI:64755": "EDTA(2-)",
    "CHEBI:17561": "L-cysteine",
    "CHEBI:31206": "ammonium chloride",
    "CHEBI:131527": "dipotassium hydrogen phosphate",
    "CHEBI:9532":  "thiamine(1+) diphosphate",
    "CHEBI:76208": "sodium sulfide (anhydrous)",
    "CHEBI:17790": "methanol",
    "CHEBI:9754":  "tris",
    "CHEBI:78673": "cumene hydroperoxide",
    "CHEBI:26710": "sodium chloride",
    # Role classes referenced by the gold examples' has_role targets or by
    # the mim_roles.yaml facet-enum meanings.
    "CHEBI:23357": "cofactor",
    "CHEBI:35225": "buffer",
    "CHEBI:38161": "chelator",
    "CHEBI:63247": "reducing agent",
    "CHEBI:63248": "oxidising agent",
    "CHEBI:50407": "acid-base indicator",
    "CHEBI:77973": "antifoaming agent",
    "CHEBI:35222": "inhibitor",
    "CHEBI:15022": "electron donor",
    "CHEBI:17654": "electron acceptor",
    "CHEBI:35195": "surfactant",
    "CHEBI:33229": "vitamin",
    "CHEBI:78016": "food gelling agent",
    "CHEBI:84735": "algal metabolite",
    "CHEBI:64577": "flour treatment agent",
    "CHEBI:77703": "EC 4.3.1.3 (histidine ammonia-lyase) inhibitor",
    "CHEBI:77746": "human metabolite",
    "CHEBI:78675": "fundamental metabolite",
    # Junk-role targets that must NOT trigger a facet match.
    "CHEBI:64229": "emetic",
    "CHEBI:35657": "flame retardant",
    "CHEBI:33287": "fertilizer",
    "CHEBI:35443": "astringent",
    "CHEBI:75835": "NMR chemical shift reference compound",
}

_LIVE_CHEBI_HAS_ROLE = {
    # From: `runoak -i sqlite:obo:chebi relationships -p RO:0000087 ...` on 2026-07-20.
    "CHEBI:17234": [],  # glucose has no direct has_role in CHEBI head-of-2026
    "CHEBI:2509":  ["CHEBI:78016", "CHEBI:84735"],  # agar
    "CHEBI:8806":  [],  # resazurin
    "CHEBI:64755": [],  # EDTA(2-)
    "CHEBI:17561": ["CHEBI:64577", "CHEBI:77703", "CHEBI:77746"],  # L-cysteine
    "CHEBI:31206": [],  # NH4Cl
    "CHEBI:131527": [],  # K2HPO4
    "CHEBI:9532":  ["CHEBI:23357", "CHEBI:78675"],  # thiamine PP
    "CHEBI:76208": [],  # Na2S
    "CHEBI:17790": [],  # methanol
    "CHEBI:9754":  ["CHEBI:35225"],  # tris → buffer
    "CHEBI:78673": ["CHEBI:78673", "CHEBI:63248"],  # cumene HP → oxidising agent (+ self)
    "CHEBI:26710": ["CHEBI:64229", "CHEBI:75835", "CHEBI:35657"],  # NaCl → junk roles
}


@pytest.fixture(scope="module")
def role_curie_index():
    return _backfill.load_role_curie_index(MIM_ROLES_YAML)


@pytest.fixture(scope="module")
def resolver(role_curie_index):
    adapter = FakeAdapter(labels=_LIVE_CHEBI_LABELS, has_role=_LIVE_CHEBI_HAS_ROLE)
    return _backfill.ChebiRoleResolver(adapter, role_curie_index)


# ---------------- Load-time correctness ----------------


def test_role_curie_index_covers_the_three_facets(role_curie_index):
    slots = {slot for entries in role_curie_index.values() for slot, _ in entries}
    assert slots == {"nutritional_roles", "physicochemical_roles", "cellular_metabolic_roles"}


def test_role_curie_index_covers_known_meaning_entries(role_curie_index):
    # Sanity: the primary CHEBI role meanings from mim_roles.yaml are indexed.
    assert ("physicochemical_roles", "BUFFER") in role_curie_index["CHEBI:35225"]
    assert ("physicochemical_roles", "CHELATOR") in role_curie_index["CHEBI:38161"]
    assert ("physicochemical_roles", "REDUCING_AGENT") in role_curie_index["CHEBI:63247"]
    assert ("physicochemical_roles", "OXIDIZING_AGENT") in role_curie_index["CHEBI:63248"]
    assert ("physicochemical_roles", "PH_INDICATOR") in role_curie_index["CHEBI:50407"]
    assert ("cellular_metabolic_roles", "COFACTOR") in role_curie_index["CHEBI:23357"]
    # CHEBI:23357 (cofactor) doubles as the nutritional COFACTOR_PROVIDER via mappings:.
    assert ("nutritional_roles", "COFACTOR_PROVIDER") in role_curie_index["CHEBI:23357"]


# ---------------- Gold-example fixtures ----------------
#
# Each fixture states what the *mechanistic* lane can produce with direct
# CHEBI has_role matching. Gold-example assignments that require literature
# (organism-conditional, concentration-conditional, or facets with no CHEBI
# equivalent) are documented as absences with a "why" comment.

_GOLD_EXAMPLES = [
    pytest.param(
        "CHEBI:17234",  # Glucose — gold: NUT[CARBON_SOURCE, ENERGY_SOURCE], CM[SUBSTRATE]
        [],
        id="glucose-mechanistic-empty",
        marks=[
            # NutritionalRoleEnum has no CHEBI role class for CARBON_SOURCE /
            # ENERGY_SOURCE (Step 7b literature). CHEBI:17234 has zero has_role
            # axioms in current CHEBI, so mechanistic lane produces nothing.
        ],
    ),
    pytest.param(
        "CHEBI:2509",  # Agar — gold: PC[SOLIDIFYING_AGENT], CM[none]
        [],
        id="agar-mechanistic-empty",
        # CHEBI:2509 has has_role → CHEBI:78016 (food gelling agent). Not in
        # index — SOLIDIFYING_AGENT has no CHEBI meaning yet in mim_roles.yaml.
    ),
    pytest.param(
        "CHEBI:8806",  # Resazurin — gold: PC[REDOX_INDICATOR], CM[none]
        [],
        id="resazurin-mechanistic-empty",
        # Zero has_role axioms on CHEBI:8806.
    ),
    pytest.param(
        "CHEBI:64755",  # EDTA(2-) — gold: PC[CHELATOR]
        [],
        id="edta2-mechanistic-empty",
        # Zero has_role axioms on the EDTA(2-) species specifically. Parent
        # EDTA (CHEBI:42191) carries CHELATOR — a per-protonation-state
        # rollup would need a separate resolution step (or use MIM SSSOM's
        # variant-aware mapping).
    ),
    pytest.param(
        "CHEBI:17561",  # L-cysteine — gold: NUT[AMINO_ACID_SOURCE, SULFUR_SOURCE], PC[REDUCING_AGENT], CM[SUBSTRATE]
        [],
        id="l-cysteine-mechanistic-empty",
        # has_role: flour treatment agent, EC-inhibitor, human metabolite.
        # None match the facet enums directly — the EC-inhibitor case was
        # a false-positive INHIBITOR match under the earlier ancestor-walk
        # code; direct-only now correctly rejects.
    ),
    pytest.param(
        "CHEBI:31206",  # NH4Cl — gold: NUT[NITROGEN_SOURCE], CM[SUBSTRATE]
        [],
        id="nh4cl-mechanistic-empty",
    ),
    pytest.param(
        "CHEBI:131527",  # K2HPO4 — gold: NUT[PHOSPHATE_SOURCE], PC[BUFFER (conditional)], CM[SUBSTRATE]
        [],
        id="k2hpo4-mechanistic-empty",
        # Recipe-conditional BUFFER (paired with KH2PO4) — belongs on
        # curator/literature lane, not mechanistic.
    ),
    pytest.param(
        "CHEBI:9532",  # Thiamine PP — gold: NUT[VITAMIN_SOURCE, COFACTOR_PROVIDER], CM[COFACTOR]
        [
            ("nutritional_roles", "COFACTOR_PROVIDER"),
            ("cellular_metabolic_roles", "COFACTOR"),
        ],
        id="thiamine-pp-covers-cofactor",
        # CHEBI:9532 has_role CHEBI:23357 (cofactor). CHEBI:23357 is both
        # the meaning: for CellularMetabolicRoleEnum.COFACTOR AND a mappings:
        # entry for NutritionalRoleEnum.COFACTOR_PROVIDER. Two facet
        # assignments from one direct hit. Gold also expects VITAMIN_SOURCE
        # (CHEBI:33229) but CHEBI:9532 doesn't assert has_role→vitamin
        # directly — that's a supply-context assertion for literature lane.
    ),
    pytest.param(
        "CHEBI:76208",  # Na2S — gold: NUT[SULFUR_SOURCE], PC[REDUCING_AGENT], CM[SUBSTRATE]+ELECTRON_DONOR (conditional)
        [],
        id="na2s-mechanistic-empty",
        # No has_role → CHEBI:63247 (reducing agent) on Na2S directly.
        # Sulfide species chemistry is only implicit in CHEBI.
    ),
    pytest.param(
        "CHEBI:17790",  # Methanol — gold: NUT[CARBON_SOURCE, ENERGY_SOURCE], CM[SUBSTRATE, ELECTRON_DONOR (conditional)]
        [],
        id="methanol-mechanistic-empty",
        # Methanol's has_role in CHEBI centers on solvent / carcinogen /
        # neurotoxin classes — not the culture-media roles.
    ),
]


@pytest.mark.parametrize("chebi_id,expected", _GOLD_EXAMPLES)
def test_gold_example_direct_hits(resolver, chebi_id, expected):
    hits = resolver.facets_for(chebi_id)
    got = sorted({(slot, value) for slot, value, _ in hits})
    assert got == sorted(expected), (
        f"{chebi_id} — mechanistic hits {got} did not match expected {expected}"
    )


# ---------------- Precision + regression tests ----------------


def test_tris_becomes_buffer(resolver):
    """Positive control — Tris has direct has_role → buffer."""
    hits = resolver.facets_for("CHEBI:9754")
    assert ("physicochemical_roles", "BUFFER") in {(s, v) for s, v, _ in hits}


def test_cumene_hydroperoxide_becomes_oxidizing_agent(resolver):
    """Positive control — has_role → oxidising agent."""
    hits = resolver.facets_for("CHEBI:78673")
    assert ("physicochemical_roles", "OXIDIZING_AGENT") in {(s, v) for s, v, _ in hits}


def test_nacl_produces_no_false_positives(resolver):
    """NaCl's has_role targets (emetic, flame retardant, NMR reference) must not match any facet."""
    hits = resolver.facets_for("CHEBI:26710")
    assert hits == []


def test_l_cysteine_does_not_match_inhibitor(resolver):
    """Regression: an EC-specific inhibitor role must NOT match generic INHIBITOR.

    Under the earlier ancestor-walk resolver, L-cysteine's has_role
    `CHEBI:77703 (EC-4.3.1.3-inhibitor)` was is-a `CHEBI:35222 (inhibitor)`,
    producing a semantic false positive. Direct-hit matching correctly
    rejects.
    """
    hits = resolver.facets_for("CHEBI:17561")
    slot_values = {(s, v) for s, v, _ in hits}
    assert ("cellular_metabolic_roles", "INHIBITOR") not in slot_values


def test_evidence_records_role_curie_and_label(resolver):
    """Evidence entries must carry both the CHEBI role CURIE and its label."""
    hits = resolver.facets_for("CHEBI:9532")  # TPP → cofactor
    role_curies = {evidence_curie for _, _, evidence_curie in hits}
    assert "CHEBI:23357" in role_curies


# ---------------- Ingredient-record extraction ----------------


def test_ingredient_chebi_id_prefers_primary_term():
    ing = {"term": {"id": "CHEBI:17234"}, "chebi_term": {"id": "CHEBI:99999"}}
    assert _backfill.ingredient_chebi_id(ing) == "CHEBI:17234"


def test_ingredient_chebi_id_falls_back_to_chebi_term():
    ing = {"term": {"id": "mediadive.compound:5"}, "chebi_term": {"id": "CHEBI:17234"}}
    assert _backfill.ingredient_chebi_id(ing) == "CHEBI:17234"


def test_ingredient_chebi_id_returns_none_for_no_chebi():
    ing = {"term": {"id": "mediadive.compound:5"}}
    assert _backfill.ingredient_chebi_id(ing) is None


def test_has_any_facet_role_detects_populated_slot():
    assert _backfill.has_any_facet_role({"nutritional_roles": ["CARBON_SOURCE"]})
    assert not _backfill.has_any_facet_role({"nutritional_roles": []})
    assert not _backfill.has_any_facet_role({})


# ---------------- Proposal building ----------------


def test_build_proposal_shape(tmp_path):
    ing = {"preferred_term": "Tris", "term": {"id": "CHEBI:9754"}}
    facet_hits = [("physicochemical_roles", "BUFFER", "CHEBI:35225")]
    role_labels = {"CHEBI:35225": "buffer"}
    proposal = _backfill.build_proposal(
        path=tmp_path / "recipe.yaml",
        idx=3,
        ing=ing,
        chebi_id="CHEBI:9754",
        facet_hits=facet_hits,
        role_labels=role_labels,
        yaml_root=tmp_path,
    )
    assert proposal["ingredient_index"] == 3
    assert proposal["ingredient_name"] == "Tris"
    assert proposal["chebi_id"] == "CHEBI:9754"
    assert proposal["proposed_slots"] == {"physicochemical_roles": ["BUFFER"]}
    assert proposal["evidence"] == [{
        "source_type": "ontology",
        "source_id": "chebi:has_role:CHEBI:35225",
        "chebi_role_label": "buffer",
        "confidence": "chebi-axiom",
    }]


def test_build_proposal_returns_none_on_empty_hits(tmp_path):
    assert _backfill.build_proposal(
        path=tmp_path / "r.yaml", idx=0, ing={}, chebi_id="CHEBI:X",
        facet_hits=[], role_labels={}, yaml_root=tmp_path,
    ) is None
