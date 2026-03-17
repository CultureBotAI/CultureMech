---
name: review-recipes
description: Quality assurance and validation for growth media recipes, solutions, and ingredient linkages
version: 1.0.0
tags: [validation, quality-assurance, recipes, media, solutions, ingredients, linkage]
author: CultureMech Team
created: 2026-03-16
---

# Review Recipes Skill

## Overview

The **Review Recipes** skill provides comprehensive quality assurance and validation for growth media and solution recipes in CultureMech. It systematically verifies that:

1. **Recipe structure is valid** - Schema compliance, required fields present
2. **Ingredient linkages are correct** - MediaIngredientMech IDs exist, CHEBI mappings valid
3. **Solution references are valid** - Solutions exist, proper composition
4. **Data quality is high** - No placeholders, concentrations specified, units valid
5. **Preparation steps are logical** - Proper sequencing, sterilization appropriate
6. **Categorization is correct** - Medium type, physical state, category match content

**Technology Stack:**
- **LinkML Schema**: Validate YAML structure and field constraints
- **MediaIngredientMech Integration**: Verify ingredient ID linkages
- **Recipe Fingerprinting**: Detect duplicates and variants
- **Data Quality Pipeline**: Automated fixes for common issues
- **Cross-reference Validation**: Solution → Ingredient traceability

**Current Dataset:** 15,450 total records
- 15,360 media recipes across 5 categories (bacterial, algae, archaea, fungal, specialized)
- 90 solution records (stock solutions, buffers, trace metals)
- ~118k ingredient instances across all recipes
- 1,048 MediaIngredientMech linkages (84.1% coverage for solutions)

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

**Decision Table:**

```
IF newly created recipe → Use interactive review
IF full category check → Use batch review
IF data quality issues → Use auto-fix pipeline
IF critical errors → Use batch review with P1 filter
IF ingredient linkage check → Use validate_ingredients.py
IF duplicate detection → Use recipe fingerprinting
```

---

## Review Workflows

### 1. Interactive Review (Single Recipe)

**Use case:** Verify a specific recipe after creation or modification

```bash
# Review by recipe name
PYTHONPATH=src python scripts/review_recipe.py "LB_Broth"

# Review by file path
PYTHONPATH=src python scripts/review_recipe.py data/normalized_yaml/bacterial/LB_Broth.yaml

# Review by CultureMech ID
PYTHONPATH=src python scripts/review_recipe.py --id CultureMech:015432

# Review with auto-correction suggestions
PYTHONPATH=src python scripts/review_recipe.py "TAP_Medium" --suggest-fixes
```

**Output:**
- Rich UI panel showing current recipe structure
- Validation results (P1-P4 issues)
- Suggested corrections with apply/skip options
- Ingredient linkage status (% MediaIngredientMech coverage)
- Solution reference validation

### 2. Batch Review (Category or All Recipes)

**Use case:** Validate entire dataset or category, generate comprehensive report

```bash
# Review all bacterial media
PYTHONPATH=src python scripts/batch_review_recipes.py \
  --category bacterial \
  --output reports/validation_bacterial_$(date +%Y%m%d) \
  --format md,json,html

# Review all solutions
PYTHONPATH=src python scripts/batch_review_recipes.py \
  --category solutions \
  --priority P1,P2

# Review all recipes
PYTHONPATH=src python scripts/batch_review_recipes.py \
  --output reports/validation_all \
  --threads 8

# Filter by medium type
PYTHONPATH=src python scripts/batch_review_recipes.py \
  --medium-type DEFINED \
  --limit 100 --dry-run
```

**Output:**
- `validation_report.md`: Human-readable summary with statistics
- `validation_data.json`: Machine-readable issues + corrections
- `dashboard.html`: Interactive sortable/filterable dashboard
- Category-level statistics (% valid, common issues, coverage metrics)

### 3. Automated Data Quality Fixes

**Use case:** Auto-fix common issues that don't require human review

```bash
# Dry-run to preview changes
PYTHONPATH=src python scripts/fix_data_quality.py --dry-run

# Apply safe corrections (P3/P4 only)
PYTHONPATH=src python scripts/fix_data_quality.py --apply

# Fix specific issue types
PYTHONPATH=src python scripts/fix_data_quality.py --apply --types concentration_units

# Fix placeholder text
PYTHONPATH=src python scripts/fix_data_quality.py --apply --types placeholders

# Standardize chemical names
PYTHONPATH=src python scripts/fix_data_quality.py --apply --types ingredient_names
```

**Safe corrections (auto-applied):**
- Standardize concentration units (g/L → G_PER_L)
- Remove placeholder text ("See source for composition")
- Normalize ingredient names to MediaIngredientMech preferred terms
- Fix whitespace/capitalization issues
- Add missing water ingredient where obvious

**Unsafe corrections (manual review required):**
- Change medium_type classification
- Merge duplicate recipes
- Modify preparation steps
- Change categorization

### 4. Claude Code-Assisted Review

**Use case:** Interactive validation with Claude's assistance

```bash
# Use this skill
/review-recipes

# Or invoke via Skill tool with specific recipe
/review-recipes "LB_Broth"

# Review a solution
/review-recipes "DAS_Vitamin_Cocktail"
```

**Claude will:**
1. Load recipe from YAML
2. Run validation via `RecipeReviewer`
3. Explain issues in plain language
4. Check ingredient linkages to MediaIngredientMech
5. Validate solution references
6. Propose corrections with rationale
7. Apply fixes if user approves
8. Update curation_history

---

## Validation Rule Catalog

### Priority Levels

| Level | Description | Action Required | Count Target |
|-------|-------------|-----------------|--------------|
| **P1** | Critical errors blocking KG export | Fix immediately | 0 |
| **P2** | High-priority warnings needing review | Manual review | < 1% |
| **P3** | Medium-priority data quality issues | Auto-correct when possible | < 5% |
| **P4** | Low-priority info/suggestions | Optional improvements | Any |

### Rule Definitions

#### P1 - Critical Errors

**Rule P1.1: Schema Validation Failure**
```yaml
id: P1.1
description: Recipe does not validate against LinkML schema
check: linkml-validate fails
impact: Cannot parse or export to KG
fix: Add missing required fields or correct field types
```

**Rule P1.2: Invalid CultureMech ID**
```yaml
id: P1.2
description: CultureMech ID missing, malformed, or duplicate
check: Regex ^CultureMech:\d{6}$, uniqueness check
impact: Identifier conflicts in KG
fix: Mint new ID or correct format
```

**Rule P1.3: Missing Required Fields**
```yaml
id: P1.3
description: Required fields missing (name, medium_type, physical_state)
check: Schema validation via LinkML
impact: Invalid YAML structure
fix: Add missing required fields
```

**Rule P1.4: Invalid Enum Values**
```yaml
id: P1.4
description: Enum values not in schema (medium_type, physical_state, units)
check: Compare against schema enums
impact: Parser failures
fix: Correct to valid enum value
```

**Rule P1.5: Broken Solution Reference**
```yaml
id: P1.5
description: Referenced solution does not exist
check: Solution CultureMech ID lookup fails
impact: Incomplete recipe composition
fix: Create missing solution or update reference
```

#### P2 - High-Priority Warnings

**Rule P2.1: Invalid MediaIngredientMech ID**
```yaml
id: P2.1
description: MediaIngredientMech ID does not exist
check: Lookup in MediaIngredientMech mapped_ingredients.yaml
impact: Broken ingredient linkage
fix: Update to correct MediaIngredientMech ID or remove
```

**Rule P2.2: Invalid CHEBI ID**
```yaml
id: P2.2
description: CHEBI term ID does not exist
check: OAK/OLS lookup returns 404
impact: Broken ontology linkage
fix: Update to correct CHEBI ID or remove
```

**Rule P2.3: Concentration Mismatch**
```yaml
id: P2.3
description: Concentration units incompatible with physical_state
check: E.g., G_PER_L for SOLID medium (should be percentage)
impact: Incorrect concentration interpretation
fix: Convert to appropriate units
```

**Rule P2.4: Category Mismatch**
```yaml
id: P2.4
description: File category doesn't match target_organisms
check: E.g., bacterial/ directory but target is algae
impact: Organizational confusion
fix: Move to correct category directory
```

**Rule P2.5: Duplicate Recipe**
```yaml
id: P2.5
description: Recipe fingerprint matches existing recipe
check: Ingredient composition + concentrations fingerprinting
threshold: > 95% similarity
impact: Data redundancy
fix: Merge duplicates or document as variant
```

#### P3 - Medium-Priority Warnings

**Rule P3.1: Placeholder Text**
```yaml
id: P3.1
description: Placeholder text in ingredients or notes
patterns: "See source", "original amount:", "Unknown", "TBD"
impact: Incomplete data
fix: Extract actual data from source or research
```

**Rule P3.2: Missing MediaIngredientMech Linkage**
```yaml
id: P3.2
description: Ingredient has no mediaingredientmech_term field
check: Ingredient lacks mediaingredientmech_term.id
impact: Reduced traceability to ontologies
fix: Enrich with MediaIngredientMech ID
```

**Rule P3.3: Non-Standard Ingredient Name**
```yaml
id: P3.3
description: Ingredient preferred_term doesn't match MediaIngredientMech
check: Fuzzy match against MediaIngredientMech preferred terms
impact: Inconsistent naming across recipes
fix: Standardize to MediaIngredientMech preferred term
```

**Rule P3.4: Missing Preparation Steps**
```yaml
id: P3.4
description: No preparation_steps field for complex media
check: medium_type = COMPLEX and preparation_steps empty
impact: Incomplete protocol information
fix: Extract from source or add basic steps
```

**Rule P3.5: Sterilization Not Specified**
```yaml
id: P3.5
description: No sterilization method specified
check: sterilization field missing
impact: Critical safety information missing
fix: Add sterilization from preparation_steps or source
```

**Rule P3.6: pH Not Specified**
```yaml
id: P3.6
description: No pH value for DEFINED or SEMI_DEFINED media
check: medium_type in [DEFINED, SEMI_DEFINED] and ph_value missing
impact: Important growth parameter missing
fix: Extract from source or mark as "not specified"
```

#### P4 - Low-Priority Info

**Rule P4.1: Low MediaIngredientMech Coverage**
```yaml
id: P4.1
description: < 50% of ingredients have MediaIngredientMech IDs
check: Count linked vs total ingredients
impact: Potential enrichment opportunity
fix: Run enrichment script on unmapped ingredients
```

**Rule P4.2: Missing Target Organisms**
```yaml
id: P4.2
description: No target_organisms specified
check: target_organisms field empty
impact: Reduced searchability
fix: Extract from source or media name
```

**Rule P4.3: Missing References**
```yaml
id: P4.3
description: No source references (DOI, URL, citation)
check: references field empty
impact: Reduced provenance
fix: Add source reference
```

**Rule P4.4: Incomplete Curation History**
```yaml
id: P4.4
description: Curation history has only creation event
check: curation_history length = 1
impact: No change tracking
fix: Add curation events as changes are made
```

**Rule P4.5: Solution Could Be Extracted**
```yaml
id: P4.5
description: Complex ingredient used in multiple recipes
check: Same multi-component ingredient in 3+ recipes
impact: Duplication instead of reusable solution
fix: Extract to shared solution record
```

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

## Error Handling

### Common Issues and Solutions

**Issue:** Schema validation fails with "Unknown enum value"
**Solution:** Check enum is defined in `src/culturemech/schema/culturemech.yaml`

**Issue:** MediaIngredientMech ID not found
**Solution:** Verify ID exists in `MediaIngredientMech/data/curated/mapped_ingredients.yaml`

**Issue:** Duplicate CultureMech IDs
**Solution:** Run `python -c "from culturemech.utils.id_utils import rebuild_culturemech_registry; rebuild_culturemech_registry()"`

**Issue:** Solution reference broken
**Solution:** Check solution exists in `data/normalized_yaml/solutions/`

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

## Related Skills

- `create-recipe` - Create new media/solution YAML records
- `manage-identifiers` - CultureMech ID assignment and management
- `manage-ingredient-hierarchy` - MediaIngredientMech integration

---

## Script Support

Helper scripts available:
- `scripts/review_recipe.py` - Interactive single recipe review
- `scripts/batch_review_recipes.py` - Batch validation with reports
- `scripts/fix_data_quality.py` - Automated corrections
- `scripts/detect_duplicate_recipes.py` - Fingerprinting and duplicate detection
- `scripts/generate_coverage_report.py` - MediaIngredientMech coverage analysis
- `scripts/validate_ingredients.py` - Ingredient linkage validation
- `scripts/enrich_with_mediaingredientmech.py` - Add MediaIngredientMech IDs

---

## Quick Reference

```bash
# Single recipe review
/review-recipes "recipe_name"

# Batch validation
PYTHONPATH=src python scripts/batch_review_recipes.py --category {category}

# Auto-fix data quality
just fix-all-data-quality

# Coverage report
PYTHONPATH=src python scripts/generate_coverage_report.py

# Detect duplicates
PYTHONPATH=src python scripts/detect_duplicate_recipes.py

# Full validation workflow
just validate-recipes && just validate-schema && just generate-indexes
```

---

**Remember**: Always validate recipes before committing, maintain >80% MediaIngredientMech coverage for solutions, and keep P1 errors at zero!
