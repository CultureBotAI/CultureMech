#!/usr/bin/env python3
"""Structural classification of normalized_yaml records: medium vs stock solution.

`data/normalized_yaml/bacterial/` holds two different kinds of record. Most are
organism growth media. ~4,986 are standalone stock-solution entries
(`Solution B`, `Main_sol_493`, `SL10_elements`, …) that carry a top-level
`composition:` and `preferred_term:` instead of `name:`/`ingredients:`.

`category` cannot express the difference. `CategoryEnum` has exactly five real
values — bacterial / fungal / archaea / specialized / algae (plus `imported`) —
and no `solutions` member, so a solution record has no honest value to carry. It
is stamped `bacterial` because that is the directory it sits in. The domain axis
does not apply to a stock solution at all: `SL10_elements` is neither bacterial
nor archaeal.

So the kind has to be read off the record's structure, not its category. The
signal is the `term.id` prefix, which is what `validate_strict.py` already used
to route these records to `SolutionRecipe` instead of false-failing them against
`MediaRecipe`. This module is that rule, lifted to one place so the validator and
the deep-research prioritizer cannot drift apart (#124).

Counts at the time of writing (2026-07-24):

    bacterial/    9493 media   4782 solutions
    archaea/       771 media      2 solutions   (moved by #120 — named for archaea)
    algae/         249 media
    fungal/        126 media
    specialized/   455 media
"""

from __future__ import annotations

from typing import Any

# A standalone stock-solution record is identified by its `term.id` prefix.
# `mediadive.solution:*` is the MediaDive-native solution namespace;
# `MediaIngredientMech:*` records are ingredient-identity anchors that share the
# same shape.
SOLUTION_TERM_PREFIXES = ("mediadive.solution:", "MediaIngredientMech:")

# A CURATED assertion, for stock/base solutions that carry no upstream solution id.
#
# These include stock solutions imported as media — "Trace element solution
# (medium 929)", "Solution C, medium 1275", "10 x M9 salts" — and empty KOMODO
# `SubMedium: Yes` rows like "Artificial sea water (medium 600)". They have no
# `mediadive.solution:` id to key on, and the `mediadive.medium:N` id some carry
# cannot be reused: those values collide coincidentally with unrelated entries in
# the solutions namespace, so `mediadive.medium:3145` ("100x Vitamin solution")
# resolves to solution 3145, "SODIUM CHLORIDE". Only 3 of the first 202
# name-obvious records had a name-agreeing id; asserting the other 170 would
# record a false identity.
#
# So the kind is stated directly instead of inferred from a borrowed identifier.
# This is deliberately NOT a name heuristic: the value is written once, by a
# curation script, into a slot a human can review in the diff — whereas matching
# "*solution*" at read time would silently reclassify any genuine medium that
# happens to be named "Ringer's solution".
RECORD_KIND_SOLUTION = "SOLUTION"


def has_solution_shape(instance: Any) -> bool:
    """True if the record is STRUCTURED as a SolutionRecipe.

    Distinct from `is_solution_record`, and the distinction is load-bearing.

    `is_solution_record` answers "should media-level audits and rankings skip
    this?" — a question about what the record IS. This one answers "which schema
    class does this record's SHAPE match?", which is what `validate_strict` needs.

    Records carrying a curated `record_kind: SOLUTION` are stock/base solutions
    conceptually, but they were imported with MediaRecipe shape — `name`,
    `original_name`, `ingredients` — not the `preferred_term` / `composition` /
    `term` shape of a SolutionRecipe. Validating the first batch as
    SolutionRecipe produced 606 spurious errors.

    So shape routing keys on the upstream `term.id` prefix only. A curated
    assertion about what a record means cannot change what it structurally is.
    """
    if not isinstance(instance, dict):
        return False
    term = instance.get("term")
    if not isinstance(term, dict):
        return False
    tid = term.get("id")
    return isinstance(tid, str) and tid.startswith(SOLUTION_TERM_PREFIXES)


def is_solution_record(instance: Any) -> bool:
    """True if `instance` is a standalone stock-solution record, not a medium.

    Two signals, both EXPLICIT assertions rather than shape heuristics — the latter
    would also catch malformed media records and silently drop them from the
    research ranking:

      * `term.id` prefix — an upstream provenance assertion (4,784 records).
      * `record_kind: SOLUTION` — a curated assertion, for solutions that have no
        upstream solution id to point at.
    """
    if not isinstance(instance, dict):
        return False
    if str(instance.get("record_kind") or "") == RECORD_KIND_SOLUTION:
        return True
    term = instance.get("term")
    if not isinstance(term, dict):
        return False
    tid = term.get("id")
    return isinstance(tid, str) and tid.startswith(SOLUTION_TERM_PREFIXES)
