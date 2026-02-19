# Data Quality Flags

## Overview

CultureMech recipes include `data_quality_flags` to provide transparency about known data quality limitations. These flags help users understand the provenance and completeness of recipe data.

## Quality Flag Types

### `incomplete_composition`
**Description**: Recipe has placeholder ingredients or incomplete composition data.

**Common causes**:
- PDF parsing failures (MediaDive, algae collections)
- Source data incomplete or unavailable
- Composition referenced but not provided

**Example**:
```yaml
name: Bacillariophycean Medium
ingredients:
  - preferred_term: "See source for composition"
    concentration:
      value: variable
      unit: VARIABLE
data_quality_flags:
  - incomplete_composition
```

**User guidance**:
- Refer to source URL in `notes` field for original composition
- Consider manual curation for high-priority media
- Flag indicates composition is not suitable for automated analysis

### `pending_curation`
**Description**: Recipe requires manual review or enrichment.

**Common causes**:
- Automated import flagged potential issues
- Missing critical metadata
- Conflicting information from multiple sources

**User guidance**:
- Recipe is structurally valid but needs human review
- Check `curation_history` for specific issues
- Contact maintainers if this is a priority recipe

### `low_confidence`
**Description**: Data source has lower reliability or confidence.

**Common causes**:
- Secondary or tertiary sources
- Automated web scraping
- Historical recipes without validation

**User guidance**:
- Use with caution for critical applications
- Cross-reference with authoritative sources when possible
- Recipe may require experimental validation

## Finding Flagged Recipes

### Command Line
```bash
# Find all recipes with quality flags
grep -r "data_quality_flags" data/normalized_yaml/

# Count incomplete compositions
grep -r "incomplete_composition" data/normalized_yaml/ | wc -l

# List all flagged recipes
find data/normalized_yaml -name "*.yaml" -exec grep -l "incomplete_composition" {} \;
```

### Python
```python
from pathlib import Path
import yaml

def find_flagged_recipes(normalized_dir, flag="incomplete_composition"):
    """Find recipes with specific quality flag."""
    flagged = []

    for recipe_path in Path(normalized_dir).rglob("*.yaml"):
        with open(recipe_path) as f:
            recipe = yaml.safe_load(f)

        flags = recipe.get('data_quality_flags', [])
        if flag in flags:
            flagged.append(recipe_path)

    return flagged

# Usage
flagged = find_flagged_recipes('data/normalized_yaml', 'incomplete_composition')
print(f"Found {len(flagged)} recipes with incomplete compositions")
```

## Statistics

### Current Quality Status
(As of last pipeline run)

```
Total recipes:           10,595
Flagged recipes:         339 (3.2%)
  - incomplete_composition: 339
  - pending_curation:       0
  - low_confidence:         0

Unfixable issues:        377 (3.6%)
  (KOMODO recipes without matching DSMZ media)
```

## Policy

### When to Add Flags

Flags are added automatically by quality pipeline:
1. **During import**: Importers add flags for known limitations
2. **During validation**: Quality tagger detects placeholder ingredients
3. **During enrichment**: Resolvers flag unresolvable issues

### When NOT to Remove Flags

Quality flags should **not** be removed unless:
- Composition data has been manually curated and verified
- Source data has been updated and re-imported
- Flag was added in error (rare)

Simply disliking a flag is not sufficient reason to remove it - flags provide important provenance information.

## Improving Quality

### For Users

If you need a high-quality version of a flagged recipe:

1. **Check source**: Visit URL in `notes` field for original composition
2. **Manual curation**: Extract composition from source and submit PR
3. **Alternative sources**: Search for same medium in other databases
4. **Contact maintainers**: Request prioritization for critical recipes

### For Contributors

To improve flagged recipes:

1. **Find flagged recipes**: Use commands above
2. **Curate composition**: Extract from authoritative source
3. **Update recipe file**: Replace placeholder ingredients
4. **Add provenance**: Update `curation_history` with source
5. **Remove flag**: Delete from `data_quality_flags` list
6. **Submit PR**: Include evidence of curation quality

### For Data Sources

To prevent flags on new imports:

1. **Improve PDF parsing**: Use better extraction tools
2. **Structured data**: Provide machine-readable formats (JSON, TSV)
3. **Complete records**: Include full composition in source database
4. **Validation**: Verify completeness before publication

## Future Enhancements

Planned improvements to quality system:

1. **Confidence scores**: Numeric quality scores (0-100)
2. **Severity levels**: WARN, INFO, ERROR classifications
3. **Automated fixes**: ML-based composition inference
4. **Quality dashboard**: Web UI showing quality metrics
5. **Validation rules**: Custom quality checks per domain

## References

- **Implementation**: `docs/DATA_QUALITY_FIXES.md`
- **Tagger script**: `scripts/tag_placeholder_recipes.py`
- **Schema**: `src/culturemech/schema/culturemech.yaml`
- **Validation**: `src/culturemech/validation/`
