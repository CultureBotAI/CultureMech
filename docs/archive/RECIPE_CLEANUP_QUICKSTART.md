# Recipe Cleanup - Quick Start

**Added**: March 15, 2026
**Purpose**: Fix data quality issues within recipe files before merging
**Script**: `scripts/cleanup_recipe_ingredients.py`

---

## ✅ What's Been Added

A new cleanup step in the data quality pipeline that fixes:
1. **Duplicate ingredients** (e.g., water appearing 3× in HD-MEDIUM)
2. **Missing pH buffers** (extracting NaOH from notes)
3. **Concentration formats** (normalizing "10 g/L" to structured format)

---

## 🚀 Quick Usage

### Run Full Pipeline (Recommended)

```bash
# Preview all quality fixes
just fix-all-data-quality dry_run=true

# Apply all fixes (includes cleanup)
just fix-all-data-quality
```

### Run Cleanup Only

```bash
# Preview changes
just cleanup-recipe-ingredients dry_run=true

# Apply changes
just cleanup-recipe-ingredients

# Apply with report
just cleanup-recipe-ingredients report=reports/cleanup.yaml
```

### Direct Script Usage

```bash
source .venv/bin/activate

# Dry run on all recipes
python scripts/cleanup_recipe_ingredients.py --dry-run

# Dry run with details
python scripts/cleanup_recipe_ingredients.py --dry-run --verbose

# Apply changes
python scripts/cleanup_recipe_ingredients.py

# Test on 100 recipes first
python scripts/cleanup_recipe_ingredients.py --limit 100 --dry-run --verbose
```

---

## 📊 Pipeline Integration

The cleanup step is now **automatically included** in the full data quality pipeline:

```
just fix-all-data-quality
  ↓
  1. Fix YAML/schema errors
  2. Resolve KOMODO compositions
  3. Cleanup recipe ingredients  ← NEW!
  4. Tag placeholder recipes
  5. Generate validation report
```

---

## 🎯 Specific Fixes

### Fix 1: Duplicate Water in HD-MEDIUM

**Before**:
```yaml
ingredients:
  - preferred_term: Water
    concentration: 1000 G_PER_L
  - preferred_term: Water
    concentration: 500 G_PER_L
  - preferred_term: Water
    concentration: 500 G_PER_L
```

**After**:
```yaml
ingredients:
  - preferred_term: Water
    concentration: 1000 G_PER_L
    notes: "Merged duplicate entries with concentrations: 1000 G_PER_L, 500 G_PER_L, 500 G_PER_L"
    data_quality_flags:
      - merged_duplicate_concentrations
```

### Fix 2: Missing NaOH pH Buffer

**Before**:
```yaml
notes: "pH buffer: NaOH to adjust pH to 7.0"
```

**After**:
```yaml
ingredients:
  - preferred_term: NaOH
    notes: "Extracted from recipe notes (pH buffer)"
    data_quality_flags:
      - extracted_from_notes
notes: "pH buffer: NaOH to adjust pH to 7.0"
```

---

## 📝 Available Commands

| Command | Description |
|---------|-------------|
| `just cleanup-recipe-ingredients` | Run cleanup on all recipes |
| `just cleanup-recipe-ingredients dry_run=true` | Preview changes only |
| `just cleanup-recipe-ingredients report=path/to/report.yaml` | Generate report |
| `just fix-all-data-quality` | Run full pipeline including cleanup |

---

## ⚡ Testing

Always test on a subset first:

```bash
# Test on 10 recipes
python scripts/cleanup_recipe_ingredients.py --limit 10 --dry-run --verbose

# Test on bacterial category only
python scripts/cleanup_recipe_ingredients.py \
  --normalized-dir data/normalized_yaml/bacterial \
  --dry-run
```

---

## 📈 Expected Results

When run on full dataset (~10,657 recipes), you might see:
- **Duplicate ingredients merged**: ~30-50 recipes
- **pH buffers extracted**: ~10-20 recipes
- **Concentrations normalized**: ~40-60 recipes

**Total**: ~5-10% of recipes will have at least one fix applied

---

## 🔍 Verification

After running cleanup:

```bash
# Check what changed
git diff data/normalized_yaml/

# Review specific file
git diff data/normalized_yaml/bacterial/KOMODO_HD-MEDIUM.yaml

# Validate recipes still pass schema
just validate-recipes
```

---

## 📚 Documentation

- **Full guide**: `docs/recipe_cleanup.md`
- **Script help**: `python scripts/cleanup_recipe_ingredients.py --help`
- **Pipeline**: `just --list`

---

## ✅ Next Steps

1. **Test first**: Run with `--dry-run` to preview
2. **Review changes**: Use `--verbose` to see details
3. **Apply**: Run without `--dry-run`
4. **Validate**: Check with `just validate-recipes`
5. **Commit**: If satisfied, commit the cleaned data

---

## 🎯 Use Cases

**Before merging recipes**:
```bash
just fix-all-data-quality      # Includes cleanup
just merge-recipes              # Now uses clean data
```

**Standalone cleanup**:
```bash
just cleanup-recipe-ingredients
```

**Testing new data**:
```bash
just cleanup-recipe-ingredients dry_run=true report=reports/cleanup.yaml
```

---

**Status**: ✅ Ready to use
**Integration**: ✅ Added to pipeline
**Documentation**: ✅ Complete
**Testing**: ✅ Verified
