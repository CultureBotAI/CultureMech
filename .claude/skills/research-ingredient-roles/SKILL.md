---
name: research-ingredient-roles
description: Run the Step 7b literature backfill lane end-to-end (Edison is billing-blocked — use the claude_code or openscientist provider; see the deep-research-medium skill for provider choice) for ingredient role facets (nutritional / physicochemical / cellular-metabolic). Prioritize gaps, dispatch Edison, extract structured YAML, apply to both MIM ingredient records (rich, evidence-bearing) and CultureMech recipes (scalar tokens per descriptor).
version: 1.0.0
tags: [edison, deep-research, ingredients, roles, facets, literature]
author: CultureMech Team
created: 2026-07-21
category: enrichment
requires_database: false
requires_internet: true
---

# research-ingredient-roles

## Overview

Orchestrates the **literature lane** of Step 7b — the cross-repo pipeline that
fills the three ingredient role facets from primary literature via Edison
(PaperQA3) or the deep-research-client fallback. Complements the **mechanistic
lane** (Step 7: `scripts/backfill_ingredient_roles.py`, driven by CHEBI
`has_role` axioms via OAK).

The two lanes write into the SAME per-facet assignment classes but with
different confidence tiers — mechanistic lands `confidence: "chebi-axiom"`
automatically; literature lands `confidence: 0.85-0.95` with cited
DOIs/PMIDs. When they disagree, primary literature wins and a curator review
item opens.

## When to Use

| Scenario | Action |
| -------- | ------ |
| Top-of-corpus gap analysis: "which ingredients lack role facets and would benefit most from Edison spend?" | Step 1 (prioritize) alone |
| Full run against top-N: propose + verify + apply | Steps 1-5 |
| Post-mechanistic-backfill fill-in: only ingredients CHEBI didn't cover | Step 1 with default penalty on has_role axiom presence |
| Re-apply an already-extracted batch to a fresh checkout | Steps 4-5 only |

**Not for**: identity mapping (that's the existing `deep-research-ingredient` skill in MIM) or role assignments derivable from CHEBI axioms (Step 7 mechanistic).

## Runbook

### 1. Prioritize (CultureMech)

```
just prioritize-role-research-candidates --top 25
# → data/import_tracking/reports/role_research_priority.json (batch-ready)
```

Score = `(# empty facets) × log10(1 + occurrences) × mapped-mult × chebi-mult`.
Records with an existing Edison role-research meta yaml are excluded. The
output JSON is the exact batch shape MIM's `research_ingredient_edison.py
--batch` expects.

**Curator triage step:** open the top-25 and drop obvious skips (distilled
water, plain HCl/NaOH — structural entries where role research isn't
scientifically meaningful). Write a trimmed `role_research_priority_top10.json`.

### 2. Dispatch Edison (MIM)

```
cd ../MediaIngredientMech
just research-ingredient-roles-edison-batch \
  ../CultureMech/data/import_tracking/reports/role_research_priority_top10.json \
  --dry-run                                    # sanity — prints plan without spending credits
# then:
just research-ingredient-roles-edison-batch \
  ../CultureMech/data/import_tracking/reports/role_research_priority_top10.json
# → research/ingredients/roles/*-edison-literature.{md,-meta.yaml,-citations.md,...}
```

Uses the role-research template
(`MediaIngredientMech/templates/ingredient_role_research.md`) that asks Edison for the three
facets, cited primary evidence per role, organism-conditional caveats, and
a machine-readable fenced YAML block.

DRC fallback (deferred as a future MIM PR):

```
# just research-ingredient-roles ... --provider falcon
```

### 3. Extract to dual batch JSON (CultureMech)

```
just extract-roles-from-edison ../MediaIngredientMech/research/ingredients/roles
# → data/import_tracking/reports/edison_role_batch_mim.json  (rich, for MIM applier)
# → data/import_tracking/reports/edison_role_batch_cm.json   (scalar, for CM applier)
```

Robustness: the LAST `role_research:` fenced block wins (template's own
example is in an earlier fence). String-shorthand entries (`- SULFUR_SOURCE`)
are upgraded to dict form. Citations sidecar is cross-referenced to fill in
`reference_text:` when the model reported only a DOI/PMID.

### 4. Apply to MIM ingredient records (rich)

```
cd ../MediaIngredientMech
just apply-role-research-results \
  ../CultureMech/data/import_tracking/reports/edison_role_batch_mim.json \
  --curator edison-deep-research \
  --dry-run
# then:
just apply-role-research-results \
  ../CultureMech/data/import_tracking/reports/edison_role_batch_mim.json \
  --curator edison-deep-research
```

Writes full `RoleAssignment` records with per-citation `RoleCitation` evidence,
per-facet never-overwrite guard, curator-history event with `changes:` naming
the facets touched.

### 5. Apply to CultureMech recipes (scalar tokens)

```
just apply-ingredient-roles \
  data/import_tracking/reports/edison_role_batch_cm.json \
  --dry-run
# then:
just apply-ingredient-roles \
  data/import_tracking/reports/edison_role_batch_cm.json
```

Walks every recipe under `data/normalized_yaml/`, matches ingredient
descriptors by CHEBI id (prefers `mediaingredientmech_chebi_term.id`, falls
back to `term.id`), and populates the three facet slots on descriptors that
don't already carry them. Never overwrites curator assignments. Adds a
curation-history event per changed recipe.

### 6. Verify

```
just validate-strict src/culturemech/schema/culturemech.yaml
just test tests/test_apply_ingredient_roles.py
# Optional visualization spot-check on a touched recipe:
just render-media-role-graph data/normalized_yaml/bacterial/<recipe>.yaml
```

## Merge Policy (Two Evidence Lanes)

Both lanes write into the same per-facet assignment classes. Merge order:

1. **Mechanistic first** (Step 7, `chebi-axiom` confidence, fast/cheap/deterministic).
2. **Literature second** (Step 7b, `literature-*` confidence, DOI/PMID cited).
3. **On agreement**: literature assignment reinforces mechanistic — same facet-role tuple, evidence list is unioned, confidence lifts to literature tier.
4. **On disagreement**: literature-cited primary evidence beats ChEBI hierarchy inference. Curator review item opens (never silently overwritten).

The extractor detects overlap by facet+role tuple. The MediaIngredientMech
`apply_role_research_results.py` and CultureMech `apply_ingredient_roles.py`
both enforce the "never mutate a populated slot"
guard, so the merge decision happens BEFORE the applier — either at extraction
time or in a curator's manual review pass.

## Related Scripts

- `scripts/prioritize_role_research_candidates.py` — this skill's step 1
- `scripts/extract_roles_from_edison.py` — step 3
- `scripts/apply_ingredient_roles.py` — step 5
- MIM `MediaIngredientMech/scripts/research_ingredient_roles_edison.py` — step 2
- MIM `MediaIngredientMech/scripts/apply_role_research_results.py` — step 4
- MIM `MediaIngredientMech/templates/ingredient_role_research.md` — the template
- Step 7 mechanistic backfill: `scripts/backfill_ingredient_roles.py`

## Related Skills

- `render-media-role-graph` — visualize what roles a recipe carries after apply
- `deep-research-ingredient` (in MIM) — identity mapping (upstream of this skill)
- `audit-schema-gaps` — post-apply verification that schema constraints hold
