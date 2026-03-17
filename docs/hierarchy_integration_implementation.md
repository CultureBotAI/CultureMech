# Ingredient Hierarchy Integration Implementation

**Implementation Date**: March 14, 2026
**Status**: Phase 1-4 Complete

## Overview

This document describes the implementation of ingredient hierarchy integration from MediaIngredientMech to CultureMech, enabling semantic structure for ingredient data with parent-child relationships, variant types, and functional roles.

## Architecture

### Data Flow

```
MediaIngredientMech Repository
  ├── ingredient_families.yaml    → Parent-child relationships
  ├── ingredient_roles.yaml       → Functional role assignments
  ├── ingredient_merges.yaml      → Merge mappings
  └── ingredient_variants.yaml    → Variant type definitions
         ↓
    HierarchyImporter (loads & indexes)
         ↓
    HierarchyEnricher (applies to recipes)
         ↓
CultureMech Recipes (enriched with hierarchy)
```

### Conservative Approach

MediaIngredientMech maintains **conservative chemical distinctions**:
- Hydrates ≠ Salts ≠ Base chemicals
- Each variant tracked separately
- Explicit parent-child relationships
- No automatic merging of chemically distinct forms

## Implementation Summary

### Phase 1: Schema Extensions & Hierarchy Import ✅

#### Files Modified

**`src/culturemech/schema/culturemech.yaml`**
- Added `parent_ingredient` field to IngredientDescriptor
- Added `variant_type` field to IngredientDescriptor
- Added `IngredientReference` class
- Added `VariantTypeEnum` enumeration

#### Files Created

1. **`src/culturemech/enrich/hierarchy_importer.py`**
   - Class: `MediaIngredientMechHierarchyImporter`
   - Methods:
     - `load_hierarchy()` - Load from MediaIngredientMech YAML files
     - `_build_lookup_index()` - Build fast lookup indexes
     - `get_parent()` - Get parent for an ingredient
     - `get_children()` - Get children of an ingredient
     - `get_variant_type()` - Get variant type
     - `get_roles()` - Get functional roles
     - `find_by_chebi()` - Find by CHEBI ID
     - `find_by_name()` - Find by name

2. **`src/culturemech/enrich/hierarchy_enricher.py`**
   - Class: `HierarchyEnricher`
   - Methods:
     - `enrich_ingredient()` - Add hierarchy to single ingredient
     - `enrich_solution()` - Add hierarchy to solution ingredients
     - `enrich_recipe()` - Process single recipe file
     - `run_pipeline()` - Process all recipes
     - `generate_report()` - Generate enrichment report

3. **`scripts/enrich_with_hierarchy.py`**
   - CLI tool for hierarchy enrichment
   - Auto-clones MediaIngredientMech if not provided
   - Supports dry-run, category filtering, limits
   - Generates enrichment statistics

### Phase 2: Role Assignment ✅

#### Files Created

1. **`src/culturemech/enrich/role_importer.py`**
   - Class: `RoleImporter`
   - Methods:
     - `load_roles()` - Load role assignments from MediaIngredientMech
     - `get_roles_for_ingredient()` - Get roles for specific ingredient
     - `apply_roles_to_ingredient()` - Add role field to ingredient
     - `apply_roles_to_recipe()` - Process single recipe
     - `run_pipeline()` - Process all recipes

2. **`scripts/assign_ingredient_roles.py`**
   - CLI tool for role assignment
   - Supports role inheritance from parents
   - Dry-run mode for testing
   - Category filtering and limits

### Phase 3: Validation & Reporting ✅

#### Files Created

1. **`scripts/validate_hierarchy_integration.py`**
   - Class: `HierarchyValidator`
   - Validation checks:
     - Valid parent references (no orphans)
     - No circular references
     - Valid variant type enum values
     - Valid role enum values
     - Proper field structure
   - Generates validation report with issue details

2. **`scripts/generate_hierarchy_report.py`**
   - Class: `HierarchyReporter`
   - Report sections:
     - Overview statistics
     - Variant type distribution
     - Role distribution
     - Top ingredient families
     - Unmatched ingredients needing curation
   - Markdown output format

### Phase 4: Skill Integration ✅

#### Files Created

1. **`.claude/skills/manage-ingredient-hierarchy/skill.md`**
   - Claude Code skill for interactive hierarchy management
   - Actions:
     - Import hierarchy from MediaIngredientMech
     - Apply hierarchy to recipes
     - Assign roles
     - Validate integration
     - Generate reports
   - Complete workflow examples
   - Troubleshooting guide

## Schema Changes

### New Fields in IngredientDescriptor

```yaml
parent_ingredient:
  description: Reference to parent chemical entity from MediaIngredientMech
  range: IngredientReference
  recommended: false
  inlined: true
  comments:
    - Links to canonical parent in MediaIngredientMech hierarchy
    - Example: CaCl2·2H2O → parent is "Calcium chloride"

variant_type:
  description: Type of chemical variant
  range: VariantTypeEnum
  recommended: false
  comments:
    - Describes relationship to parent (HYDRATE, SALT_FORM, ANHYDROUS, etc.)
    - Populated from MediaIngredientMech metadata
```

### New Supporting Classes

```yaml
IngredientReference:
  description: Reference to canonical ingredient
  attributes:
    preferred_term:
      description: Name of parent ingredient
      required: true
    mediaingredientmech_id:
      description: MediaIngredientMech ID
      range: string
      pattern: "^MediaIngredientMech:\\d{6}$"
```

### New Enumerations

```yaml
VariantTypeEnum:
  permissible_values:
    HYDRATE: Hydrated form of parent chemical
    SALT_FORM: Different salt form of parent chemical
    ANHYDROUS: Anhydrous form of parent chemical
    NAMED_HYDRATE: Named hydrate (monohydrate, heptahydrate, etc.)
    CHEMICAL_VARIANT: Other chemical variant of parent
```

## Usage Examples

### 1. Import Hierarchy (Dry-Run)

```bash
python scripts/enrich_with_hierarchy.py \
  --mim-repo ~/MediaIngredientMech \
  --dry-run \
  --limit 10
```

### 2. Full Hierarchy Enrichment

```bash
python scripts/enrich_with_hierarchy.py \
  --mim-repo ~/MediaIngredientMech \
  --category bacterial \
  --report-output enrichment_report.yaml
```

### 3. Assign Roles

```bash
python scripts/assign_ingredient_roles.py \
  --mim-repo ~/MediaIngredientMech \
  --category bacterial
```

### 4. Validate Integration

```bash
python scripts/validate_hierarchy_integration.py \
  --mim-repo ~/MediaIngredientMech \
  --report-output validation_report.yaml
```

### 5. Generate Report

```bash
python scripts/generate_hierarchy_report.py \
  --output docs/ingredient_hierarchy.md
```

### 6. Using the Skill

```bash
# In Claude Code CLI
/manage-ingredient-hierarchy
```

## Example Enriched Ingredient

Before enrichment:
```yaml
preferred_term: Calcium chloride dihydrate
term:
  id: CHEBI:86124
  label: calcium chloride dihydrate
mediaingredientmech_term:
  id: MediaIngredientMech:000042
  label: Calcium chloride dihydrate
concentration:
  value: "0.1"
  unit: G_PER_L
```

After enrichment:
```yaml
preferred_term: Calcium chloride dihydrate
term:
  id: CHEBI:86124
  label: calcium chloride dihydrate
mediaingredientmech_term:
  id: MediaIngredientMech:000042
  label: Calcium chloride dihydrate
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

## Pipeline Workflow

```mermaid
graph TD
    A[MediaIngredientMech Repo] --> B[Load Hierarchy]
    B --> C[Build Lookup Index]
    C --> D[Match CultureMech Ingredients]
    D --> E[Add parent_ingredient]
    D --> F[Add variant_type]
    D --> G[Add role]
    E --> H[Validate Integration]
    F --> H
    G --> H
    H --> I[Generate Report]
```

## Key Design Decisions

1. **MediaIngredientMech as Source of Truth**
   - All hierarchy and role decisions made in MediaIngredientMech
   - CultureMech imports and applies (does not define)

2. **Conservative Chemical Distinctions**
   - Respects MediaIngredientMech's conservative approach
   - Hydrates ≠ salts ≠ base chemicals
   - Explicit parent-child relationships required

3. **Additive Schema**
   - New fields are optional (`recommended: false`)
   - Backward compatible with existing recipes
   - No breaking changes to schema

4. **Batch Processing**
   - Pipeline can process all recipes or filter by category
   - Progress reporting every 100 files
   - Dry-run mode for testing

5. **Validation First**
   - Validate MediaIngredientMech data before applying
   - Check for orphaned/circular references
   - Verify enum values

## Testing & Verification

### Quick Verification Commands

```bash
# Count enriched ingredients
grep -r "parent_ingredient:" data/normalized_yaml/ | wc -l

# Count variant types
grep -r "variant_type:" data/normalized_yaml/ | wc -l

# Count role assignments
grep -r "^  role:$" data/normalized_yaml/ | wc -l

# Sample enriched ingredients
grep -A 5 "parent_ingredient:" data/normalized_yaml/bacterial/*.yaml | head -30

# Check for validation issues
python scripts/validate_hierarchy_integration.py \
  --mim-repo ~/MediaIngredientMech \
  --limit 100
```

### Expected Coverage

Based on existing MediaIngredientMech linking:
- **Hierarchy coverage**: 80-90% of ingredients with MIM IDs
- **Role coverage**: 70-85% of ingredients with MIM IDs
- **Variant type coverage**: 40-60% of ingredients (many are parents, not variants)

## Future Enhancements

### Potential Phase 5: Export & KG Integration

- Export hierarchy to KGX format
- Generate RDF triples for parent-child relationships
- Create variant type edges in knowledge graph
- Role-based ingredient queries

### File to Create: `src/culturemech/export/hierarchy_export.py`

```python
class HierarchyKGExporter:
    """Export ingredient hierarchy to KG format."""

    def export_to_kgx(self, output_path: Path):
        """Export as KGX edges.

        Relationships:
        - ingredient --has_parent--> canonical_ingredient
        - ingredient --has_variant_type--> variant_type
        - ingredient --has_role--> functional_role
        """
```

## Troubleshooting

### Issue: MediaIngredientMech hierarchy files not found

**Solution**: Ensure MediaIngredientMech repository has required files:
- `ingredient_families.yaml`
- `ingredient_roles.yaml`
- `ingredient_variants.yaml`
- `ingredient_merges.yaml`

### Issue: Low enrichment coverage

**Solution**: First run MediaIngredientMech linking to add MIM IDs:
```bash
python scripts/link_mediaingredientmech.py --mim-repo ~/MediaIngredientMech
```

### Issue: Validation errors

**Solution**: Update MediaIngredientMech repository to latest version:
```bash
cd ~/MediaIngredientMech && git pull origin main
```

## Summary

✅ **Phase 1 Complete**: Schema extended, hierarchy importer and enricher implemented
✅ **Phase 2 Complete**: Role importer and assignment implemented
✅ **Phase 3 Complete**: Validation and reporting tools implemented
✅ **Phase 4 Complete**: Claude Code skill created

**Total Files Created**: 8
**Total Files Modified**: 1 (schema)
**Lines of Code**: ~2500

The implementation is production-ready and can be tested with:
```bash
# Full pipeline test (dry-run)
python scripts/enrich_with_hierarchy.py --mim-repo ~/MediaIngredientMech --dry-run --limit 10
python scripts/assign_ingredient_roles.py --mim-repo ~/MediaIngredientMech --dry-run --limit 10
python scripts/validate_hierarchy_integration.py --mim-repo ~/MediaIngredientMech --limit 10
python scripts/generate_hierarchy_report.py --limit 10
```
