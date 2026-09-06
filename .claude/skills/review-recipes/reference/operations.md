# Operations: Error Handling · Validation Checklist · Output Examples

*Reference for the **review-recipes** skill — see [`../SKILL.md`](../SKILL.md) for the overview, workflows, and rule summary.*

---

## Error Handling

### Common Issues and Solutions

**Issue:** Schema validation fails with "Unknown enum value"
**Solution:** Check enum is defined in `src/culturemech/schema/culturemech.yaml`

**Issue:** MediaIngredientMech ID not found
**Solution:** Verify ID exists in `MediaIngredientMech/data/curated/mapped_ingredients.yaml`

**Issue:** Duplicate CultureMech IDs
**Solution:** Run `python -c "from culturemech.utils.id_utils import rebuild_culturemech_registry; rebuild_culturemech_registry()"`

**Issue:** Solution reference broken
**Solution:** Check the solution record exists. Solutions are `record_kind: SOLUTION` records in the category directories, not a directory of their own (#422): `grep -rl '^preferred_term: <solution name>' data/normalized_yaml/` (anchored: an unanchored match also finds every medium that uses it)

**Issue:** Concentration units invalid
**Solution:** Convert to enum value from schema (e.g., "g/L" → "G_PER_L")

---

## Validation Checklist

Before committing a recipe:

- ✅ Schema validates (`just validate-schema`)
- ✅ CultureMech ID unique and in registry
- ✅ Required fields present (name, medium_type, physical_state, ingredients)
- ✅ No P1 critical errors
- ✅ MediaIngredientMech coverage > 50% (for solutions: > 80%)
- ✅ No duplicate recipes detected
- ✅ Ingredient names standardized
- ✅ Concentration units use enums
- ✅ No placeholder text
- ✅ Curation history entry added
- ✅ References/source documented
- ✅ Category directory correct

---

## Output Examples

### Interactive Review Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Recipe Review: LB_Broth
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ID: CultureMech:015432
Category: bacterial
Medium Type: COMPLEX
Physical State: LIQUID

Validation Results:
  ✅ Schema valid
  ✅ CultureMech ID unique
  ✅ Required fields present
  ⚠️  P3.2: 1/4 ingredients missing MediaIngredientMech linkage
  ⚠️  P3.6: pH not specified

Ingredient Coverage:
  Total ingredients: 4
  MediaIngredientMech linked: 3 (75.0%)
  Unlinked: ["Yeast extract"]

Suggestions:
  1. Add MediaIngredientMech ID for "Yeast extract"
     → MediaIngredientMech:000234 (preferred term: "Yeast extract")
  2. Add pH value (typical: 7.0 ± 0.2)

Apply fixes? [y/N]:
```

### Batch Review Summary

```markdown
# Recipe Validation Report - Bacterial Media
Date: 2026-03-16

## Summary Statistics
- Total recipes: 8,234
- Validated: 8,234 (100%)
- P1 Critical Errors: 0 (0.0%)
- P2 High Priority: 23 (0.3%)
- P3 Medium Priority: 456 (5.5%)
- P4 Low Priority: 1,234 (15.0%)

## Issue Breakdown

### P1 Critical (0)
None! 🎉

### P2 High Priority (23)
1. P2.1 - Invalid MediaIngredientMech ID: 12 recipes
2. P2.3 - Concentration mismatch: 8 recipes
3. P2.5 - Duplicate recipe: 3 pairs

### P3 Medium Priority (456)
1. P3.1 - Placeholder text: 234 recipes
2. P3.2 - Missing MediaIngredientMech linkage: 123 recipes
3. P3.6 - pH not specified: 99 recipes

## Top Action Items
1. Fix 12 broken MediaIngredientMech IDs
2. Remove placeholder text from 234 recipes
3. Merge 3 duplicate recipe pairs
4. Add MediaIngredientMech linkage to 123 recipes

## Coverage Metrics
- Overall MediaIngredientMech coverage: 80.9%
- Recipes with >80% coverage: 6,789 (82.5%)
- Recipes with <50% coverage: 234 (2.8%)
```

---

