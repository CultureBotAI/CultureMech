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

### Detect Duplicates

```bash
# Find potential duplicate recipes
PYTHONPATH=src python scripts/detect_duplicate_recipes.py \
  --threshold 0.95 \
  --output reports/duplicates_$(date +%Y%m%d).json

# Check specific category
PYTHONPATH=src python scripts/detect_duplicate_recipes.py \
  --category bacterial \
  --threshold 0.90
```

**Fingerprinting Algorithm:**
1. Extract sorted ingredient list with concentrations
2. Normalize ingredient names (case-insensitive, whitespace)
3. Normalize concentration units
4. Generate hash of normalized composition
5. Calculate Jaccard similarity between ingredient sets
6. Flag pairs with similarity > threshold

**Output:**
```json
{
  "duplicate_pairs": [
    {
      "recipe1": {
        "id": "CultureMech:001234",
        "name": "LB Broth",
        "path": "data/normalized_yaml/bacterial/LB_Broth.yaml"
      },
      "recipe2": {
        "id": "CultureMech:005678",
        "name": "Luria-Bertani Medium",
        "path": "data/normalized_yaml/bacterial/Luria_Bertani_Medium.yaml"
      },
      "similarity": 0.98,
      "differences": [
        "recipe1 has pH 7.0, recipe2 has pH 7.2"
      ],
      "recommendation": "MERGE - Near-identical recipes"
    }
  ]
}
```

---

