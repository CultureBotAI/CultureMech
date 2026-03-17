# Recipe Ingredient Cleanup

**Script**: `scripts/cleanup_recipe_ingredients.py`
**Purpose**: Fix data quality issues within individual recipe files
**When**: Runs BEFORE merging as part of the data quality pipeline

---

## What It Fixes

### 1. Duplicate Ingredient Entries ✅

**Problem**: Same ingredient appears multiple times in a recipe
```yaml
# BEFORE
ingredients:
  - preferred_term: Water
    concentration: 1000 G_PER_L
  - preferred_term: Water
    concentration: 500 G_PER_L
  - preferred_term: Water
    concentration: 500 G_PER_L
```

**Solution**: Merges duplicates, keeping first non-zero concentration
```yaml
# AFTER
ingredients:
  - preferred_term: Water
    concentration: 1000 G_PER_L
    notes: "Merged duplicate entries with concentrations: 1000 G_PER_L, 500 G_PER_L"
    data_quality_flags:
      - merged_duplicate_concentrations
```

### 2. Missing pH Buffers ✅

**Problem**: pH buffers mentioned in notes but not in ingredients
```yaml
# BEFORE
ingredients:
  - preferred_term: Glucose
notes: "pH buffer: NaOH. Adjust to pH 7.2"
```

**Solution**: Extracts and adds as ingredient
```yaml
# AFTER
ingredients:
  - preferred_term: Glucose
  - preferred_term: NaOH
    notes: "Extracted from recipe notes (pH buffer)"
    data_quality_flags:
      - extracted_from_notes
notes: "pH buffer: NaOH. Adjust to pH 7.2"
```

**Patterns detected**:
- `pH buffer: X`
- `adjust pH with X`
- `using X for pH`

### 3. Concentration Normalization ✅

**Problem**: Inconsistent concentration formats
```yaml
# BEFORE
concentration: "10 g/L"  # String
```

**Solution**: Normalizes to structured format
```yaml
# AFTER
concentration:
  value: 10.0
  unit: G_PER_L
```

---

## Usage

### As Part of Pipeline (Recommended)

```bash
# Dry run to preview changes
just fix-all-data-quality dry_run=true

# Apply all quality fixes including cleanup
just fix-all-data-quality
```

### Standalone

```bash
source .venv/bin/activate

# Dry run - see what would change
python scripts/cleanup_recipe_ingredients.py --dry-run --verbose

# Apply changes
python scripts/cleanup_recipe_ingredients.py

# Generate report
python scripts/cleanup_recipe_ingredients.py \
  --report reports/cleanup_report.yaml

# Test on subset
python scripts/cleanup_recipe_ingredients.py --limit 100 --dry-run
```

---

## Command-Line Options

| Option | Default | Description |
|--------|---------|-------------|
| `--normalized-dir` | `data/normalized_yaml` | Directory with recipe files |
| `--dry-run` | False | Preview changes without modifying files |
| `--verbose` | False | Show detailed changes for each recipe |
| `--limit` | None | Process only first N recipes (testing) |
| `--report` | None | Write cleanup report to YAML file |

---

## Integration with Pipeline

The cleanup step runs automatically in the full data quality pipeline:

```bash
just fix-all-data-quality
```

**Pipeline order**:
1. Fix YAML/schema errors
2. Resolve KOMODO compositions
3. **Cleanup recipe ingredients** ← NEW
4. Tag placeholder recipes
5. Generate validation report

---

## Examples

### Example 1: HD-MEDIUM Issue

**Before** (`data/normalized_yaml/bacterial/KOMODO_HD-MEDIUM.yaml`):
```yaml
name: HD-MEDIUM
ingredients:
  - preferred_term: Water
    concentration: 1000 G_PER_L
  - preferred_term: Water
    concentration: 500 G_PER_L
  - preferred_term: Water
    concentration: 500 G_PER_L
  - preferred_term: Glucose
    concentration: 10 G_PER_L
notes: "pH buffer: NaOH to adjust pH to 7.0"
```

**After cleanup**:
```yaml
name: HD-MEDIUM
ingredients:
  - preferred_term: Water
    concentration: 1000 G_PER_L
    notes: "Merged duplicate entries with concentrations: 1000 G_PER_L, 500 G_PER_L, 500 G_PER_L"
    data_quality_flags:
      - merged_duplicate_concentrations
  - preferred_term: Glucose
    concentration: 10 G_PER_L
  - preferred_term: NaOH
    notes: "Extracted from recipe notes (pH buffer)"
    data_quality_flags:
      - extracted_from_notes
notes: "pH buffer: NaOH to adjust pH to 7.0"
```

### Example 2: Preview Changes (Dry Run)

```bash
$ python scripts/cleanup_recipe_ingredients.py --dry-run --verbose

======================================================================
Recipe Ingredient Cleanup
======================================================================

*** DRY RUN MODE - No files will be modified ***

Scanning data/normalized_yaml...
Found 10657 recipes

Processing recipes...

HD-MEDIUM.yaml:
  • Merged 3 duplicate entries of 'Water'
  • Added pH buffer 'NaOH' from notes

LB_Broth.yaml:
  • Normalized 'NaCl' concentration: '10 g/L' → {'value': 10.0, 'unit': 'G_PER_L'}

...

======================================================================
Summary
======================================================================
Recipes processed:  10657
Recipes modified:   47
Total changes:      89

Change breakdown:
  Duplicate ingredients merged: 32
  pH buffers extracted: 15
  Concentrations normalized: 42

DRY RUN: No files were modified. Run without --dry-run to apply changes.
```

---

## Report Format

When using `--report`, generates YAML report:

```yaml
summary:
  recipes_processed: 10657
  recipes_modified: 47
  total_changes: 89

changes_by_recipe:
  - file: HD-MEDIUM.yaml
    changes:
      - "Merged 3 duplicate entries of 'Water'"
      - "Added pH buffer 'NaOH' from notes"

  - file: LB_Broth.yaml
    changes:
      - "Normalized 'NaCl' concentration: '10 g/L' → {'value': 10.0, 'unit': 'G_PER_L'}"
```

---

## Quality Flags

The cleanup script adds quality flags for transparency:

| Flag | Meaning |
|------|---------|
| `merged_duplicate_concentrations` | Multiple instances of ingredient had different concentrations |
| `extracted_from_notes` | Ingredient was extracted from recipe notes |

These flags help track data provenance and quality.

---

## Best Practices

1. **Always dry-run first**
   ```bash
   just cleanup-recipe-ingredients dry_run=true
   ```

2. **Review changes before committing**
   ```bash
   git diff data/normalized_yaml/
   ```

3. **Generate report for audit trail**
   ```bash
   just cleanup-recipe-ingredients report=reports/cleanup.yaml
   ```

4. **Run as part of full pipeline**
   ```bash
   just fix-all-data-quality
   ```

---

## Testing

Test on small subset before full run:

```bash
# Test on 100 recipes
python scripts/cleanup_recipe_ingredients.py --limit 100 --dry-run --verbose

# Test on specific category
python scripts/cleanup_recipe_ingredients.py \
  --normalized-dir data/normalized_yaml/bacterial \
  --dry-run
```

---

## Troubleshooting

### Issue: Script finds no recipes
**Solution**: Check `--normalized-dir` path is correct

### Issue: Changes not being applied
**Solution**: Remove `--dry-run` flag

### Issue: Too many changes
**Solution**: Review with `--verbose`, adjust patterns if needed

### Issue: Script crashes on specific recipe
**Solution**: Check YAML syntax, fix with `just fix-validation-errors`

---

## Future Enhancements

Potential additions:
- Unit conversion (e.g., mg/L → G_PER_L)
- Outlier detection for concentrations
- Ingredient name standardization
- pH value extraction from notes
- Temperature extraction

---

## Related

- **Full pipeline**: `just fix-all-data-quality`
- **Validation**: `just validate-recipes`
- **Schema**: `src/culturemech/schema/culturemech.yaml`
- **Other quality tools**: `scripts/tag_placeholder_recipes.py`, `scripts/resolve_komodo_compositions.py`
