---
name: manage-ingredient-hierarchy
description: Manage ingredient hierarchy integration from MediaIngredientMech
category: workflow
requires_database: false
requires_internet: true
version: 1.0.0
---

# Manage Ingredient Hierarchy

## Overview

**Purpose**: Import and manage ingredient hierarchy from MediaIngredientMech, enriching CultureMech recipes with parent-child relationships, variant types, and functional roles.

**Why**: Provides semantic structure to ingredient data, enables chemical variant tracking (hydrates, salt forms), supports knowledge graph integration, and maintains consistent ingredient classification across repositories.

**Scope**: Integration between MediaIngredientMech (source of truth for ingredient hierarchy) and CultureMech (consumer of hierarchy data).

## When to Use This Skill

Use this skill when:
- Importing ingredient hierarchy from MediaIngredientMech
- Enriching CultureMech recipes with parent/child relationships
- Assigning functional roles to ingredients
- Validating hierarchy integration
- Generating hierarchy reports
- Troubleshooting hierarchy-related issues
- Understanding ingredient variant relationships

## Architecture

### Data Flow

```
MediaIngredientMech Repository
  ├── ingredient_families.yaml    # Parent-child relationships
  ├── ingredient_roles.yaml       # Functional role assignments
  ├── ingredient_merges.yaml      # Merge mappings
  └── ingredient_variants.yaml    # Variant type definitions
         ↓
    Import & Index
         ↓
CultureMech Enrichment
  ├── Add parent_ingredient field
  ├── Add variant_type field
  └── Add role field
         ↓
CultureMech Recipes (enriched)
```

### Key Concepts

**Parent-Child Relationships**:
- Parent: Canonical chemical entity (e.g., "Calcium chloride")
- Child: Specific variant (e.g., "Calcium chloride dihydrate")
- Relationship tracked via `parent_ingredient` field

**Variant Types**:
- `HYDRATE`: Hydrated form
- `SALT_FORM`: Different salt form
- `ANHYDROUS`: Anhydrous form
- `NAMED_HYDRATE`: Named hydrate (monohydrate, heptahydrate)
- `CHEMICAL_VARIANT`: Other variant

**Functional Roles**:
- `MINERAL`, `SALT`, `BUFFER`, `CARBON_SOURCE`, `NITROGEN_SOURCE`
- `TRACE_ELEMENT`, `VITAMIN_SOURCE`, `COFACTOR_PROVIDER`
- And more (see schema)

## Available Actions

### 1. Import Hierarchy

Import ingredient hierarchy from MediaIngredientMech repository.

**Command**:
```bash
python scripts/enrich_with_hierarchy.py \
  --mim-repo /path/to/MediaIngredientMech \
  --yaml-dir data/normalized_yaml \
  --dry-run \
  --limit 10
```

**Options**:
- `--mim-repo`: Path to MediaIngredientMech repo (clones if not provided)
- `--yaml-dir`: Directory with CultureMech YAML files (default: data/normalized_yaml)
- `--category`: Process specific category (bacterial, fungal, algae, etc.)
- `--limit`: Limit number of files (for testing)
- `--dry-run`: Preview changes without modifying files
- `--report-output`: Save enrichment report to YAML

**What it does**:
1. Loads hierarchy from MediaIngredientMech YAML files
2. Builds lookup indexes (by CHEBI ID, name, MIM ID)
3. Matches CultureMech ingredients to hierarchy
4. Adds `parent_ingredient` and `variant_type` fields
5. Generates enrichment statistics

**Example output**:
```
============================================================
Ingredient Hierarchy Enrichment Pipeline
============================================================
Hierarchy loaded: 995 ingredients, 112 parents, 883 children
Found 15431 recipe files

============================================================
Hierarchy Enrichment Complete
============================================================
Files processed: 1500
Files modified: 450
Ingredients enriched: 3200
Solutions with enriched ingredients: 150
Hierarchy coverage: 85.2% (3200/3755)
```

### 2. Assign Roles

Assign functional roles to ingredients based on MediaIngredientMech data.

**Command**:
```bash
python scripts/assign_ingredient_roles.py \
  --mim-repo /path/to/MediaIngredientMech \
  --yaml-dir data/normalized_yaml \
  --dry-run
```

**Options**:
- `--mim-repo`: Path to MediaIngredientMech repo (required)
- `--yaml-dir`: Directory with CultureMech YAML files
- `--category`: Process specific category
- `--limit`: Limit number of files
- `--dry-run`: Preview changes without modifying files
- `--no-inherit`: Don't inherit roles from parent ingredients

**What it does**:
1. Loads role assignments from MediaIngredientMech
2. Matches ingredients by MediaIngredientMech ID
3. Adds `role` field (list of functional roles)
4. Optionally inherits roles from parent ingredients

**Role inheritance example**:
```yaml
# Child ingredient
preferred_term: Calcium chloride dihydrate
mediaingredientmech_term:
  id: MediaIngredientMech:000042
  label: Calcium chloride dihydrate
parent_ingredient:
  preferred_term: Calcium chloride
  mediaingredientmech_id: MediaIngredientMech:000041
role:  # Inherited from parent
  - MINERAL
  - SALT
```

### 3. Validate Integration

Validate hierarchy integration for correctness and completeness.

**Command**:
```bash
python scripts/validate_hierarchy_integration.py \
  --mim-repo /path/to/MediaIngredientMech \
  --yaml-dir data/normalized_yaml \
  --report-output validation_report.yaml
```

**Options**:
- `--mim-repo`: Path to MediaIngredientMech repo (required)
- `--yaml-dir`: Directory with CultureMech YAML files
- `--category`: Validate specific category
- `--limit`: Limit number of files
- `--report-output`: Save validation report to YAML

**Validation checks**:
- ✓ All parent references point to valid MediaIngredientMech IDs
- ✓ No orphaned or circular references
- ✓ Variant types are valid enum values
- ✓ Role assignments are valid enum values
- ✓ Parent-child relationships are consistent

**Example output**:
```
============================================================
Validation Complete
============================================================
Files checked: 1500
Ingredients checked: 8500
Ingredients with hierarchy: 7200
Ingredients with roles: 6800

Valid parent references: 7200
Invalid parent references: 0
Orphaned references: 0
Circular references: 0

Valid variant types: 7200
Invalid variant types: 0

Valid roles: 13500
Invalid roles: 0

Hierarchy coverage: 84.7%
Role coverage: 80.0%

✓ All validations passed!
```

### 4. Generate Report

Generate human-readable Markdown report showing hierarchy statistics.

**Command**:
```bash
python scripts/generate_hierarchy_report.py \
  --yaml-dir data/normalized_yaml \
  --output docs/ingredient_hierarchy.md
```

**Options**:
- `--yaml-dir`: Directory with CultureMech YAML files
- `--category`: Analyze specific category
- `--limit`: Limit number of files
- `--output`: Path to save Markdown report

**Report includes**:
- Overview statistics (coverage, counts)
- Variant type distribution
- Role distribution
- Top ingredient families by occurrence
- Unmatched ingredients needing curation

**Example report snippet**:
```markdown
## Overview

- **Files analyzed**: 15431
- **Total ingredients**: 45000
- **Ingredients with hierarchy**: 38000
- **Hierarchy coverage**: 84.4%
- **Role coverage**: 82.1%

## Variant Type Distribution

| Variant Type | Count | Percentage |
|--------------|-------|------------|
| HYDRATE | 15200 | 40.0% |
| SALT_FORM | 8500 | 22.4% |
| ANHYDROUS | 6800 | 17.9% |
```

## Complete Workflow Example

### Initial Setup & Enrichment

```bash
# Step 1: Import hierarchy (dry-run first)
python scripts/enrich_with_hierarchy.py \
  --mim-repo ~/MediaIngredientMech \
  --dry-run \
  --limit 10

# Step 2: Run full enrichment
python scripts/enrich_with_hierarchy.py \
  --mim-repo ~/MediaIngredientMech \
  --report-output enrichment_report.yaml

# Step 3: Assign roles
python scripts/assign_ingredient_roles.py \
  --mim-repo ~/MediaIngredientMech \
  --dry-run \
  --limit 10

# Step 4: Run full role assignment
python scripts/assign_ingredient_roles.py \
  --mim-repo ~/MediaIngredientMech

# Step 5: Validate integration
python scripts/validate_hierarchy_integration.py \
  --mim-repo ~/MediaIngredientMech \
  --report-output validation_report.yaml

# Step 6: Generate report
python scripts/generate_hierarchy_report.py \
  --output docs/ingredient_hierarchy.md
```

### Verification Commands

```bash
# Check enriched ingredients
grep -r "parent_ingredient:" data/normalized_yaml/ | wc -l

# Check variant types
grep -r "variant_type:" data/normalized_yaml/ | wc -l

# Check role assignments
grep -r "role:" data/normalized_yaml/ | head -20

# Find specific variant type
grep -r "variant_type: HYDRATE" data/normalized_yaml/ | wc -l
```

## Schema Integration

### New Fields Added to IngredientDescriptor

```yaml
# Example enriched ingredient
preferred_term: Calcium chloride dihydrate
term:
  id: CHEBI:86124
  label: calcium chloride dihydrate
mediaingredientmech_term:
  id: MediaIngredientMech:000042
  label: Calcium chloride dihydrate

# NEW: Hierarchy fields
parent_ingredient:
  preferred_term: Calcium chloride
  mediaingredientmech_id: MediaIngredientMech:000041

variant_type: HYDRATE

role:
  - MINERAL
  - SALT

concentration:
  value: "0.1"
  unit: G_PER_L
```

## Troubleshooting

### Issue: No hierarchy data loaded

**Symptom**: "Loaded 0 families" message

**Cause**: MediaIngredientMech repository missing hierarchy files

**Solution**:
```bash
# Check for hierarchy files
ls ~/MediaIngredientMech/ingredient_families.yaml
ls ~/MediaIngredientMech/ingredient_roles.yaml

# If missing, pull latest from GitHub
cd ~/MediaIngredientMech
git pull origin main
```

### Issue: Low enrichment coverage

**Symptom**: "Hierarchy coverage: 25.3%" (unexpectedly low)

**Cause**: Ingredients missing MediaIngredientMech IDs

**Solution**:
```bash
# First run MediaIngredientMech linking
python scripts/link_mediaingredientmech.py \
  --mim-repo ~/MediaIngredientMech \
  --dry-run

# Then run hierarchy enrichment
python scripts/enrich_with_hierarchy.py \
  --mim-repo ~/MediaIngredientMech
```

### Issue: Validation errors

**Symptom**: "Invalid parent references: 150"

**Cause**: MediaIngredientMech repository out of sync

**Solution**:
```bash
# Update MediaIngredientMech repository
cd ~/MediaIngredientMech
git pull origin main

# Re-run enrichment
python scripts/enrich_with_hierarchy.py \
  --mim-repo ~/MediaIngredientMech
```

### Issue: Orphaned references

**Symptom**: "Orphaned references: 50"

**Cause**: Parent IDs not found in MediaIngredientMech

**Solution**:
```bash
# Check validation report for details
cat validation_report.yaml | grep "orphaned_parent_reference"

# Report to MediaIngredientMech repository
# These may need to be added to the hierarchy
```

## Best Practices

### DO:
✓ **Run enrichment in order**: MIM linking → hierarchy → roles → validation
✓ **Test with --dry-run first** before making changes
✓ **Validate after enrichment** to catch issues early
✓ **Keep MediaIngredientMech repo updated** (git pull regularly)
✓ **Generate reports** for tracking coverage over time
✓ **Document manual curation** in issue tracker

### DON'T:
✗ **Don't skip validation** - catches critical issues
✗ **Don't manually edit hierarchy fields** - use scripts
✗ **Don't mix old and new data** - run full pipeline on all files
✗ **Don't ignore orphaned references** - report to MediaIngredientMech
✗ **Don't run on production without dry-run** - always test first

## Integration with Knowledge Graph

Hierarchy data enables semantic queries in the knowledge graph:

```sparql
# Find all hydrated forms of a chemical
SELECT ?ingredient ?parent WHERE {
  ?ingredient culturemech:parent_ingredient ?parent_ref .
  ?parent_ref culturemech:mediaingredientmech_id ?parent .
  ?ingredient culturemech:variant_type "HYDRATE" .
}

# Find media using minerals
SELECT ?medium ?ingredient WHERE {
  ?medium culturemech:has_ingredient ?ingredient .
  ?ingredient culturemech:role "MINERAL" .
}
```

## Summary

This skill provides complete workflow for importing and managing ingredient hierarchy from MediaIngredientMech into CultureMech. Use the provided scripts and validation tools to maintain consistent, semantic ingredient data that supports advanced querying and knowledge graph integration.

**Key Points**:
- MediaIngredientMech is source of truth for hierarchy
- CultureMech imports and applies hierarchy data
- Validation ensures data quality
- Reports track coverage and progress
- Schema extensions are backward compatible
