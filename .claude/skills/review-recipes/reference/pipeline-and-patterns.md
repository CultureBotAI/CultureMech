# Data-Quality Pipeline · Validation Patterns · MediaIngredientMech Integration

*Reference for the **review-recipes** skill — see [`../SKILL.md`](../SKILL.md) for the overview, workflows, and rule summary.*

---

## Data Quality Pipeline Integration

### Current Pipeline (justfile)

```bash
# Full quality pipeline
just fix-all-data-quality

# Individual steps
just cleanup-ingredients          # Standardize ingredient names
just fix-placeholder-text         # Remove "See source" patterns
just standardize-units            # Convert to enum units
just enrich-mediaingredientmech   # Add MediaIngredientMech IDs
```

### Adding Recipe Review to Pipeline

```bash
# Add to .justfile
validate-recipes:
    PYTHONPATH=src python scripts/batch_review_recipes.py \
      --output reports/validation_latest \
      --format md,json \
      --priority P1,P2,P3

# Run as part of pre-commit
pre-commit: validate-recipes validate-schema
```

---

## Common Validation Patterns

### Pattern 1: New Recipe Validation

**Scenario:** Created LB_Broth.yaml, need to validate before commit

**Workflow:**
```bash
# 1. Schema validation
just validate-schema data/normalized_yaml/bacterial/LB_Broth.yaml

# 2. Interactive review
/review-recipes "LB_Broth"

# 3. Check for duplicates
PYTHONPATH=src python scripts/detect_duplicate_recipes.py \
  --target data/normalized_yaml/bacterial/LB_Broth.yaml

# 4. Coverage check
PYTHONPATH=src python scripts/generate_coverage_report.py \
  --single data/normalized_yaml/bacterial/LB_Broth.yaml
```

### Pattern 2: Solution Validation

**Scenario:** Created DAS_Vitamin_Cocktail.yaml solution

**Workflow:**
```bash
# 1. Validate composition
/review-recipes "DAS_Vitamin_Cocktail"

# 2. Check ingredient linkages
PYTHONPATH=src python scripts/validate_ingredients.py \
  data/normalized_yaml/solutions/DAS_Vitamin_Cocktail.yaml

# 3. Find usage in media
grep -r "DAS_Vitamin_Cocktail" data/normalized_yaml/algae/

# 4. Validate cross-references
PYTHONPATH=src python scripts/validate_solution_references.py \
  --solution "DAS_Vitamin_Cocktail"
```

### Pattern 3: Batch Category Review

**Scenario:** Review all algae media for quality issues

**Workflow:**
```bash
# 1. Batch review
PYTHONPATH=src python scripts/batch_review_recipes.py \
  --category algae \
  --output reports/algae_validation \
  --priority P1,P2,P3

# 2. Fix auto-correctable issues
PYTHONPATH=src python scripts/fix_data_quality.py \
  --category algae \
  --apply --types placeholders,units

# 3. Generate coverage report
PYTHONPATH=src python scripts/generate_coverage_report.py \
  --category algae

# 4. Regenerate indexes
just generate-indexes data/normalized_yaml/algae
```

### Pattern 4: Pre-Export KG Check

**Scenario:** Validate all recipes before KG export

**Workflow:**
```bash
# 1. Full batch review (P1 only)
PYTHONPATH=src python scripts/batch_review_recipes.py \
  --priority P1 \
  --output reports/pre_export_validation

# 2. Check for critical errors
grep "^P1" reports/pre_export_validation.md

# 3. Fix blocking errors
# (Manual fixes for P1 issues)

# 4. Re-validate
PYTHONPATH=src python scripts/batch_review_recipes.py --priority P1

# 5. Export when P1 count = 0
just export-kg
```

---

## Integration with MediaIngredientMech

### Enrichment Workflow

```bash
# 1. Check current coverage
PYTHONPATH=src python scripts/generate_coverage_report.py

# 2. Run enrichment
PYTHONPATH=src python scripts/enrich_with_mediaingredientmech.py \
  --category solutions \
  --mediaingredientmech-repo /path/to/MediaIngredientMech

# 3. Validate linkages
PYTHONPATH=src python scripts/validate_ingredients.py \
  --check-mediaingredientmech

# 4. Re-check coverage
PYTHONPATH=src python scripts/generate_coverage_report.py
```

### Syncing with MediaIngredientMech Updates

When MediaIngredientMech adds new ingredients:

```bash
# 1. Pull latest MediaIngredientMech
cd /path/to/MediaIngredientMech && git pull

# 2. Re-run enrichment on CultureMech
cd /path/to/CultureMech
PYTHONPATH=src python scripts/enrich_with_mediaingredientmech.py \
  --incremental \
  --mediaingredientmech-repo /path/to/MediaIngredientMech

# 3. Check improvement
PYTHONPATH=src python scripts/generate_coverage_report.py \
  --compare-with reports/mediaingredientmech_coverage_previous.md
```

---

