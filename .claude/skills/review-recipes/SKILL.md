---
name: review-recipes
description: Use this skill to quality-check CultureMech growth-media and solution recipes — verify schema/structure, MediaIngredientMech ingredient linkages and CHEBI mappings, solution references, data quality (placeholders, units, concentrations), and categorization. Use after creating/editing a recipe, before a KG export, or for periodic maintenance. Issues are graded P1 (blocking) → P4 (optional); P3/P4 can be auto-fixed.
version: 1.1.0
tags: [validation, quality-assurance, recipes, media, solutions, ingredients, linkage]
author: CultureMech Team
created: 2026-03-16
---

# Review Recipes Skill

## Structured Review Output

For every new review or audit, follow
[docs/record-reviews.md](../../../docs/record-reviews.md) and
[the local profile](../../../docs/record-review-profile.md).
Capture exact targets and input hashes before judging, preserve this skill's
native rubric, rule IDs, scores and evidence requirements, then author the
structured assessment and run:

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
uv run python scripts/record_review.py validate /tmp/completed-review.yaml
uv run python scripts/record_review.py save --content /tmp/completed-review.yaml
```

Choose session-unique temporary paths. Save authoritative YAML and derived
Markdown under `reviews/structured/<timestamp>-<slug>/`; link both in the
final response. This output contract supersedes prose-only report examples.
A single record uses `kind: record`; batches declare exact selection,
population, reviewed targets and limits. Categories also state boundary decisions.
Every reviewed target must have an assessment. Keep P1-P4 and other native
severity/rule information with a justified common severity, and metric definitions,
scales and denominators. Do not infer scientific approval from a native score.

Raw provider drafts and deterministic validator/scan reports are diagnostic
inputs, not completed scientific reviews. Use `scientific_review: false`
for deterministic-only or provenance-only assessments; mark required unavailable
checks and incomplete coverage explicitly. A valid bundle does not change native
status, clear release holds, authorize edits, or append curation history.
For audit-only requests, stop after assessment and persistence; any application
steps below require curation intent.

## Overview

The **Review Recipes** skill provides quality assurance for growth-media and solution
recipes in CultureMech. It verifies that:

1. **Recipe structure is valid** — schema compliance, required fields present
2. **Ingredient linkages are correct** — MediaIngredientMech IDs exist, CHEBI mappings valid
3. **Solution references are valid** — solutions exist, proper composition
4. **Data quality is high** — no placeholders, concentrations/units specified
5. **Preparation steps are logical** — proper sequencing, sterilization appropriate
6. **Categorization is correct** — medium type, physical state, category match content

**Technology stack:** LinkML schema validation, MediaIngredientMech integration (ID
linkages), recipe fingerprinting (duplicate detection), an auto-fix data-quality pipeline,
and cross-reference (solution → ingredient) validation.

**Dataset:** ~15,450 records — ~15,360 media recipes across 5 categories (bacterial, algae,
archaea, fungal, specialized) + ~90 solutions; ~118k ingredient instances; ~1,048
MediaIngredientMech linkages (84.1% solution coverage).

---

## When to Use This Skill

| Scenario | Workflow | Priority |
|----------|----------|----------|
| **Post-creation QA** | Validate newly created recipes before committing | High |
| **Batch validation** | Review all recipes in a category | High |
| **Pre-export check** | Ensure KG export quality before release | Critical |
| **Periodic maintenance** | Monthly validation after updates | Medium |
| **Ingredient enrichment** | Check MediaIngredientMech coverage | Medium |
| **Duplicate detection** | Find potential merge candidates | Low |
| **Data quality cleanup** | Fix placeholders and missing data | High |

```
IF newly created recipe   → interactive review
IF full category check    → batch review
IF data quality issues    → auto-fix pipeline
IF critical errors        → batch review with P1 filter
IF ingredient linkage     → validate_ingredients.py
IF duplicate detection    → recipe fingerprinting
```

---

## Review Workflows

### 1. Focused review (single recipe)

```bash
just validate data/normalized_yaml/bacterial/LB_Broth.yaml
just assign-ids-check
```

Inspect the recipe directly using this skill's validation rules and run any
domain-specific checks relevant to the changed fields. Apply corrections only
after showing the proposed YAML diff, then append `curation_history`.

### 2. Batch Review (category or all)

```bash
PYTHONPATH=src python scripts/batch_review_recipes.py \
  --category bacterial --output reports/validation_bacterial

PYTHONPATH=src python scripts/batch_review_recipes.py --category solutions --priority P1,P2
PYTHONPATH=src python scripts/batch_review_recipes.py --output reports/validation_all
PYTHONPATH=src python scripts/batch_review_recipes.py --limit 100
```

The actual script emits TSV, Markdown and JSON at the output prefix. These
are deterministic scan diagnostics, not final scientific reviews. Assess exact
targets, then validate/save the final bundle with `scripts/record_review.py`.

### 3. Data quality fixes

```bash
just fix-all-data-quality true  # preview
# Review the preview before applying the individual scoped recipes.
```

**Safe (auto-applied):** standardize concentration units (g/L → G_PER_L), remove placeholder
text, normalize ingredient names to MIM preferred terms, fix whitespace/capitalization, add
obvious missing water.
**Unsafe (manual review):** change `medium_type`, merge duplicates, modify preparation steps,
change categorization.

### 4. Claude Code-Assisted Review

```bash
/review-recipes                       # interactive
/review-recipes "LB_Broth"            # specific recipe
/review-recipes "DAS_Vitamin_Cocktail" # a solution
```

Claude loads the YAML, uses the available `RecipeValidator` diagnostics, explains issues, checks MIM
linkages and solution references, proposes corrections with rationale, applies on approval,
and updates `curation_history`.

---

## Validation Rules

Issues are graded by priority. Full definitions (checks, impact, fixes) are in
[`reference/validation-rules.md`](reference/validation-rules.md).

| Level | Meaning | Action | Target |
|-------|---------|--------|--------|
| **P1** | Critical errors blocking KG export | Fix immediately | 0 |
| **P2** | High-priority warnings needing review | Manual review | < 1% |
| **P3** | Medium-priority data quality issues | Auto-correct when possible | < 5% |
| **P4** | Low-priority info/suggestions | Optional | Any |

| Rule | Summary |
|------|---------|
| **P1.1** | Schema validation failure |
| **P1.2** | Invalid CultureMech ID |
| **P1.3** | Missing required fields |
| **P1.4** | Invalid enum values |
| **P1.5** | Broken solution reference |
| **P2.1** | Invalid MediaIngredientMech ID |
| **P2.2** | Invalid CHEBI ID |
| **P2.3** | Concentration mismatch |
| **P2.4** | Category mismatch |
| **P2.5** | Duplicate recipe |
| **P3.1** | Placeholder text |
| **P3.2** | Missing MediaIngredientMech linkage |
| **P3.3** | Non-standard ingredient name |
| **P3.4** | Missing preparation steps |
| **P3.5** | Sterilization not specified |
| **P3.6** | pH not specified |
| **P4.1** | Low MediaIngredientMech coverage |
| **P4.2** | Missing target organisms |
| **P4.3** | Missing references |
| **P4.4** | Incomplete curation history |
| **P4.5** | Solution could be extracted |

---

## Related Skills

- [`create-recipe`](../create-recipe/SKILL.md) — create new media/solution YAML records
- [`manage-identifiers`](../manage-identifiers/SKILL.md) — CultureMech ID assignment

---

## Script Support

`scripts/batch_review_recipes.py` (batch + reports),
`scripts/enrich_with_mediaingredientmech.py` (add MIM IDs), and the scoped
validation/migration recipes in `project.justfile`.

---

## Quick Reference

```bash
/review-recipes "recipe_name"                                              # single review
PYTHONPATH=src python scripts/batch_review_recipes.py --category {category} # batch
just fix-all-data-quality                                                  # auto-fix
just validate-recipes                                                      # corpus review
just validate-strict && just assign-ids-check                              # corpus gates
```

> **Remember:** validate before committing, keep solution MediaIngredientMech coverage
> above 80%, and keep P1 errors at zero.

---

## Reference Files

| File | Contents |
|------|----------|
| [`reference/validation-rules.md`](reference/validation-rules.md) | Full definitions for all 21 P1–P4 rules: checks, impact, fixes |
| [`reference/linkage-and-duplicates.md`](reference/linkage-and-duplicates.md) | MediaIngredientMech coverage checks (single + batch report), cross-reference validation, and recipe fingerprinting / duplicate detection |
| [`reference/pipeline-and-patterns.md`](reference/pipeline-and-patterns.md) | Data-quality pipeline (justfile) integration, the four validation patterns (new recipe, solution, batch category, pre-export), and MediaIngredientMech enrichment/sync workflows |
| [`reference/operations.md`](reference/operations.md) | Error handling, the validation checklist, and interactive/batch output examples |
