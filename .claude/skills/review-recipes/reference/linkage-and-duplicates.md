# Ingredient Linkage Validation & Recipe Fingerprinting

*Reference for the **review-recipes** skill — see [`../SKILL.md`](../SKILL.md) for the overview, workflows, and rule summary.*

---

## Ingredient Linkage Validation

### MediaIngredientMech Coverage Check

```python
from culturemech.utils.ingredient_validator import IngredientValidator

validator = IngredientValidator()

# Check single recipe
recipe_path = "data/normalized_yaml/bacterial/LB_Broth.yaml"
coverage = validator.check_mediaingredientmech_coverage(recipe_path)

print(f"Total ingredients: {coverage['total']}")
print(f"Linked: {coverage['linked']} ({coverage['percentage']:.1f}%)")
print(f"Unlinked: {', '.join(coverage['unlinked_terms'])}")
```

### Batch Coverage Report

```bash
# Generate coverage report for all recipes
PYTHONPATH=src python scripts/generate_coverage_report.py \
  --output reports/mediaingredientmech_coverage_$(date +%Y%m%d).md

# Check specific category
PYTHONPATH=src python scripts/generate_coverage_report.py \
  --category solutions \
  --output reports/solutions_coverage.md
```

**Output Example:**
```markdown
# MediaIngredientMech Coverage Report

## Overall Statistics
- Total recipes: 15,450
- Total ingredient instances: 118,818
- Linked instances: 99,547 (83.8%)
- Unlinked instances: 19,271 (16.2%)

## By Category
| Category | Recipes | Ingredients | Linked | Coverage |
|----------|---------|-------------|--------|----------|
| bacterial | 8,234 | 67,123 | 54,321 | 80.9% |
| algae | 4,567 | 32,456 | 28,901 | 89.0% |
| solutions | 90 | 456 | 384 | 84.2% |

## Top Unlinked Ingredients
1. Soil extract (1,234 instances, 45 recipes)
2. Beef extract (987 instances, 23 recipes)
3. Malt extract (765 instances, 34 recipes)
```

### Cross-Reference Validation

```python
from culturemech.utils.cross_reference_validator import CrossReferenceValidator

validator = CrossReferenceValidator()

# Check all solution references in a recipe
recipe_path = "data/normalized_yaml/algae/J_Medium.yaml"
issues = validator.validate_solution_references(recipe_path)

for issue in issues:
    print(f"P{issue['priority']}: {issue['description']}")
    if issue['suggested_fix']:
        print(f"  Fix: {issue['suggested_fix']}")
```

---

## Recipe Fingerprinting

### Exact Ingredient-Set Merge Fingerprinting

The maintained exact merge path fingerprints ingredient identity sets with
`src/culturemech/merge/fingerprint.py` and groups recipes through
`python -m culturemech.merge.merge_recipes`. The fingerprint is
concentration-independent: same-ingredient-set recipes group together even when
pH, concentration, temperature, or preparation differ.

```bash
# Preview exact ingredient-set merge groups
PYTHONPATH=src python -m culturemech.merge.merge_recipes \
  --dry-run \
  --min-group-size 2

# Show exact merge stats without rewriting data/merge_yaml
PYTHONPATH=src python -m culturemech.merge.merge_recipes \
  --stats-only
```

**Exact ingredient-set fingerprinting algorithm:**
1. Extract ingredient identifiers from direct ingredients and solution
   compositions
2. Prefer CHEBI IDs, falling back to normalized ingredient names
3. Ignore concentration amounts and ingredient order
4. Sort and hash the unique ingredient identifiers

### Close Variant Proposals

Close variants are reviewed through the manifest-driven media variant workflow,
not through exact merge fingerprints:

```bash
just review-media-content
just propose-media-variant-links
just apply-media-variant-links --limit <n>
just validate-media-variant-links
```

`scripts/propose_media_variant_links.py` groups candidate records by ingredient
identity signature, compares concentration and physical-state signatures, and
infers parent/child relationships such as `SOURCE_DUPLICATE`,
`PHYSICAL_STATE_VARIANT`, `CONCENTRATION_VARIANT`, `PH_VARIANT`,
`SALINITY_VARIANT`, `SUPPLEMENTED_VARIANT`, `OMITTED_COMPONENT_VARIANT`, and
`SUBSTITUTED_COMPONENT_VARIANT`.

---
