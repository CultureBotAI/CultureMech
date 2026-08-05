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

# A CURATED assertion, for solutions that carry no upstream solution id (#175).
#
# 202 records are stock solutions imported as media — "Trace element solution
# (medium 929)", "Solution C, medium 1275", "10 x M9 salts". They have no
# `mediadive.solution:` id to key on, and the id they DO carry cannot be reused:
# their `mediadive.medium:N` values collide coincidentally with unrelated entries
# in the solutions namespace, so `mediadive.medium:3145` ("100x Vitamin solution")
# resolves to solution 3145, "SODIUM CHLORIDE". Only 3 of 202 have a
# name-agreeing id; asserting the other 170 would record a false identity.
#
# So the kind is stated directly instead of inferred from a borrowed identifier.
# This is deliberately NOT a name heuristic: the value is written once, by a
# curation script, into a slot a human can review in the diff — whereas matching
# "*solution*" at read time would silently reclassify any genuine medium that
# happens to be named "Ringer's solution".
RECORD_KIND_SOLUTION = "SOLUTION"


def is_solution_record(instance: Any) -> bool:
    """True if `instance` is a standalone stock-solution record, not a medium.

    Two signals, both EXPLICIT assertions rather than shape heuristics — the latter
    would also catch malformed media records and silently drop them from the
    research ranking:

      * `term.id` prefix — an upstream provenance assertion (4,784 records).
      * `record_kind: SOLUTION` — curated, for the 202 with no upstream id.
      * `record_kind: SOLUTION` — a curated assertion, for solutions that have no
        upstream solution id to point at (#175).
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
