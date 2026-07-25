#!/usr/bin/env python3
"""Structural classification of normalized_yaml records: medium vs stock solution.

`data/normalized_yaml/bacterial/` holds two different kinds of record. Most are
organism growth media. ~4,784 are standalone MediaDive stock-solution entries
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


def is_solution_record(instance: Any) -> bool:
    """True if `instance` is a standalone stock-solution record, not a medium.

    Deliberately keyed on `term.id` rather than on the presence of `composition:`
    or the absence of `ingredients:`: the id prefix is an explicit provenance
    assertion, whereas shape heuristics would also catch malformed media records
    and silently drop them from the research ranking.
    """
    if not isinstance(instance, dict):
        return False
    term = instance.get("term")
    if not isinstance(term, dict):
        return False
    tid = term.get("id")
    return isinstance(tid, str) and tid.startswith(SOLUTION_TERM_PREFIXES)
