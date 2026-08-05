"""Guard test: the schema's `ChemicalEntityTerm.id` pattern must stay in sync with the id-label config prefix declarations.

Motivating incident: PR #96 added `MICRO` to `conf/id_label_targets.yaml`
`ignored_prefixes:` (so the id-label validator would stop warning on MICRO
ids), but did NOT update the schema's `ChemicalEntityTerm.id` regex
pattern. Two PRs later, #99 introduced `MICRO:XXXX` ids into the corpus
via FOODON→MICRO reroutes for enzymatic protein digests, and
`validate-strict` blew up with 847 `pattern_mismatch` errors — a classic
split-responsibility bug caught only when the drift landed in data.

This test would have failed on PR #96 as soon as MICRO was added to
`ignored_prefixes`, forcing the schema pattern update in the same PR.

Invariants asserted:

1. Every OAK **adapter** (`CHEBI`, `FOODON`, `UBERON`, `ENVO`, `NCIT`, …)
   declared in `id_label_targets.yaml` must appear in the
   `ChemicalEntityTerm.id` schema regex. Rationale: an adapter is by definition
   a namespace the validator will look ids up in; if it looks them up we
   expect them on ingredient `term.id` values.

2. Every prefix in the schema's `ChemicalEntityTerm.id` regex must be
   declared somewhere in `id_label_targets.yaml` (either an adapter
   entry OR the `ignored_prefixes:` list). Rationale: catches a stray
   typo or a stale prefix the schema still knows about that the
   validator no longer expects.

The test is DIRECTIONAL asymmetrically to accommodate `ignored_prefixes`
noise: many entries there (`cas:`, `komodo.medium`, `jcm.grmd`, `MEDIADB`)
are for slots OTHER than `ChemicalEntityTerm.id` and legitimately have no
place in the ingredient-id pattern.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path

import yaml

_REPO_ROOT = Path(__file__).resolve().parent.parent
_SCHEMA_PATH = _REPO_ROOT / "src" / "culturemech" / "schema" / "culturemech.yaml"
_CONFIG_PATH = _REPO_ROOT / "conf" / "id_label_targets.yaml"

# Class we're guarding. The ChemicalEntityTerm class carries the pattern
# accepted for any `term.id` that grounds an ingredient (CHEBI/FOODON/…).
_GUARDED_CLASS = "ChemicalEntityTerm"

# Adapters declared in id_label_targets.yaml which are NOT expected on an
# ingredient's `term.id`. These are legitimate adapters for OTHER schema
# classes (OrganismTerm carries NCBITaxon, MediaDatabaseTerm carries NCIT,
# etc.). If a new adapter belongs here, add it — but the addition should be
# a considered decision: "this adapter is for X class, not for ingredients."
#
# The corollary: an adapter NOT in this list is expected to appear on
# ingredient term.id values and must be included in ChemicalEntityTerm's
# pattern regex. That's the guard that would have caught the PR #96 → #99
# MICRO drift, applied prospectively — a curator adding a new adapter (or,
# in the actual PR #96 case, an ignored_prefix that becomes
# ingredient-relevant) would be forced to also update the schema pattern
# in the same PR to keep the test green.
_NON_INGREDIENT_ADAPTERS = frozenset({
    "NCBITaxon",   # OrganismTerm.id
    "NCIT",        # MediaDatabaseTerm.id (National Cancer Institute Thesaurus, medium classifications)
})


def _load_schema_ingredient_pattern() -> str:
    """Extract the `ChemicalEntityTerm.id` `slot_usage.id.pattern` value from the schema."""
    schema = yaml.safe_load(_SCHEMA_PATH.read_text())
    classes = schema.get("classes") or {}
    if _GUARDED_CLASS not in classes:
        raise AssertionError(
            f"{_GUARDED_CLASS} not in schema — has the class been renamed or removed? "
            "Update this test to name the current class."
        )
    slot_usage = classes[_GUARDED_CLASS].get("slot_usage") or {}
    id_usage = slot_usage.get("id") or {}
    pattern = id_usage.get("pattern")
    if not pattern:
        raise AssertionError(
            f"{_GUARDED_CLASS}.slot_usage.id.pattern is empty — the ingredient-id pattern "
            "must be declared explicitly; a missing pattern would silently accept anything."
        )
    return pattern


def _prefixes_from_pattern(pattern: str) -> frozenset[str]:
    """Extract the prefix alternation from a `^(A|B|C):\\w+$`-style pattern.

    Supports escapes: `mediadive\\.compound` → `mediadive.compound`.
    """
    m = re.match(r"^\^\(([^)]+)\):", pattern)
    if not m:
        raise AssertionError(
            f"Ingredient-id pattern {pattern!r} does not match the "
            "expected `^(A|B|C):\\w+$` alternation shape — update this test if the "
            "schema convention changes."
        )
    return frozenset(alt.replace(r"\.", ".") for alt in m.group(1).split("|"))


def _config_adapter_prefixes() -> frozenset[str]:
    """Prefixes declared under `adapters:` (case-preserving) — case-insensitive comparisons downstream."""
    cfg = yaml.safe_load(_CONFIG_PATH.read_text())
    adapters = cfg.get("adapters") or {}
    return frozenset(adapters.keys())


def _config_ignored_prefixes() -> frozenset[str]:
    """Prefixes declared under `ignored_prefixes:`."""
    cfg = yaml.safe_load(_CONFIG_PATH.read_text())
    return frozenset(cfg.get("ignored_prefixes") or [])


def _norm(s: str) -> str:
    """Case-insensitive normalization (some configs write `chebi`, schema writes `CHEBI`)."""
    return s.upper()


def _norm_set(items: Iterable[str]) -> frozenset[str]:
    return frozenset(_norm(x) for x in items)


# ---------------------------- tests ----------------------------


def test_ingredient_pattern_is_declared():
    pattern = _load_schema_ingredient_pattern()
    prefixes = _prefixes_from_pattern(pattern)
    assert prefixes, f"{_GUARDED_CLASS} pattern has zero prefixes"


def test_every_ingredient_adapter_is_accepted_by_ingredient_pattern():
    """Adapters expected on ingredient.term.id must be in the ChemicalEntityTerm pattern.

    Guard against the PR #96 → #99 drift class: any new adapter added to
    id_label_targets.yaml that isn't explicitly declared organism-only or
    media-only via `_NON_INGREDIENT_ADAPTERS` must appear in the schema
    regex. A new adapter forces a considered decision: either it's
    ingredient-relevant (update the pattern) or it isn't (add it to
    `_NON_INGREDIENT_ADAPTERS` with a comment explaining which class it
    belongs on).
    """
    schema_prefixes = _norm_set(_prefixes_from_pattern(_load_schema_ingredient_pattern()))
    all_adapters = _config_adapter_prefixes()
    ingredient_adapters = _norm_set(all_adapters - _NON_INGREDIENT_ADAPTERS)

    missing = ingredient_adapters - schema_prefixes
    assert not missing, (
        f"Adapters expected on ingredient.term.id missing from {_GUARDED_CLASS} pattern: "
        f"{sorted(missing)}. Either (a) add each to `{_GUARDED_CLASS}.slot_usage.id.pattern` "
        f"AND `{_GUARDED_CLASS}.id_prefixes:` in `src/culturemech/schema/culturemech.yaml`, "
        f"OR (b) if this adapter is for a NON-ingredient class (organism / medium / "
        f"solution / etc.), add it to `_NON_INGREDIENT_ADAPTERS` in this test file with "
        f"a comment explaining which class it belongs on."
    )


def test_every_schema_prefix_is_declared_in_config():
    """A schema prefix that isn't an adapter or ignored_prefix is dead code.

    Catches a stray/typo prefix in the schema pattern that the validator
    has no rules for. Would fire on e.g. `^(CHEBI|FODON|...)` (typo).
    """
    schema_prefixes = _norm_set(_prefixes_from_pattern(_load_schema_ingredient_pattern()))
    adapters = _norm_set(_config_adapter_prefixes())
    ignored = _norm_set(_config_ignored_prefixes())
    known = adapters | ignored

    unknown = schema_prefixes - known
    assert not unknown, (
        f"Schema pattern references prefixes the id-label config doesn't know about: "
        f"{sorted(unknown)}. Either add each to `conf/id_label_targets.yaml adapters:` "
        f"(if OAK can look them up) or to `ignored_prefixes:` (if it's a legitimate "
        f"non-ontology identifier), or remove it from the schema pattern."
    )


def test_prefixes_list_matches_pattern():
    """`id_prefixes:` on ChemicalEntityTerm should be the same set as the pattern's alternation.

    LinkML supports both a regex and a discrete `id_prefixes:` list on a class;
    they should mean the same thing. If they diverge, downstream generators
    (JSON Schema, docs, dataclasses) can silently pick one and drop the other.
    """
    schema = yaml.safe_load(_SCHEMA_PATH.read_text())
    cls = schema["classes"][_GUARDED_CLASS]
    pattern_prefixes = _norm_set(_prefixes_from_pattern(cls["slot_usage"]["id"]["pattern"]))
    declared_prefixes = _norm_set(cls.get("id_prefixes") or [])

    assert pattern_prefixes == declared_prefixes, (
        f"ChemicalEntityTerm.slot_usage.id.pattern prefixes {sorted(pattern_prefixes)} "
        f"disagree with ChemicalEntityTerm.id_prefixes: {sorted(declared_prefixes)}. "
        f"The two must be kept in sync — update both together."
    )


def test_specific_ingredient_id_prefixes_present():
    """Positive regression: the specific prefixes we've historically supported are all present.

    Guards against a well-intentioned refactor that "simplifies" the pattern
    but silently drops one of these. Each one has been used by real corpus
    ingredients or targeted PRs.
    """
    pattern = _load_schema_ingredient_pattern()
    prefixes = _norm_set(_prefixes_from_pattern(pattern))

    required = {
        _norm("CHEBI"),        # primary ontology
        _norm("FOODON"),       # food / yeast-extract / etc.
        _norm("MICRO"),        # protein digests (added in the MICRO backfill PR #99)
        _norm("UBERON"),       # anatomical tissue ingredients
        _norm("ENVO"),         # environmental sample ingredients
        _norm("mediadive.compound"),  # MediaDive upstream grounding
    }
    missing = required - prefixes
    assert not missing, (
        f"Historically-supported ingredient prefixes missing from schema pattern: "
        f"{sorted(missing)}. Removing any of these breaks existing corpus records."
    )
