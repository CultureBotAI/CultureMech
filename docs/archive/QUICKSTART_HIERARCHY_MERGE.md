# Quick Start: Hierarchy-Aware Recipe Merging

**Status**: ✅ Infrastructure complete | ⏳ Baseline merge running
**Last Updated**: March 14, 2026

---

## 🚀 Quick Start

### Prerequisites

1. **Virtual Environment**: Activate the project venv
   ```bash
   source .venv/bin/activate
   ```

2. **MediaIngredientMech** (for hierarchy features): Clone the repository
   ```bash
   # Outside this project
   git clone https://github.com/microbiomedata/MediaIngredientMech.git
   ```

---

## 📊 Current Status

### Baseline Merge (Phase 1)
**Running now**: Processing 15,431 recipes → `data/merge_yaml/merged_2026/`

**Previous baseline** (Feb 2026):
- Input: 10,595 recipes
- Output: 1,350 merged recipes
- Reduction: 87.3%

**Expected new baseline**:
- Input: 15,431 recipes
- Output: ~2,000 merged recipes (estimate)
- Reduction: ~87% (estimate)

### Infrastructure Complete ✅

All core scripts and modules are ready to use:
- ✅ Hierarchy-aware fingerprinting
- ✅ Merge rule engine
- ✅ Quality validation
- ✅ Rollback capability
- ✅ Monitoring dashboard

---

## 🎯 Common Workflows

### 1. Compare Fingerprint Modes

```bash
# Requires MediaIngredientMech repository
source .venv/bin/activate

python scripts/compare_fingerprints.py \
  --mim-repo /path/to/MediaIngredientMech \
  --output reports/fingerprint_comparison.yaml \
  --limit 5000  # Optional: test on subset first

# View results
cat reports/fingerprint_comparison.yaml
```

**Output**: Shows how many recipes would merge differently in `chemical` vs `variant` vs `original` modes.

---

### 2. Test Different Merge Modes

```bash
source .venv/bin/activate

python scripts/test_merge_modes.py \
  --mim-repo /path/to/MediaIngredientMech \
  --modes conservative,aggressive,variant-aware \
  --fingerprint-mode chemical \
  --output reports/mode_comparison.yaml

# View results
cat reports/mode_comparison.yaml
```

**Output**: Statistics for each merge mode (group counts, reduction %, confidence scores).

---

### 3. Validate Merge Quality

```bash
source .venv/bin/activate

# Validate current baseline merge
python scripts/validate_merge_quality.py \
  --merged-dir data/merge_yaml/merged_2026 \
  --mim-repo /path/to/MediaIngredientMech \
  --output reports/merge_quality.yaml

# View quality report
cat reports/merge_quality.yaml
```

**Checks**:
- ❌ **Variant contamination** (e.g., CaCl₂·2H₂O merged with CaCl₂)
- ⚠️ **Parent mismatches** (conflicting hierarchy relationships)
- ℹ️ **Concentration outliers** (wildly different amounts)

---

### 4. Undo Problematic Merges

```bash
source .venv/bin/activate

# Preview what would be undone (dry run)
python scripts/undo_merge.py \
  --merged-dir data/merge_yaml/merged_2026 \
  --normalized-dir data/normalized_yaml \
  --filter variant_contamination \
  --quality-report reports/merge_quality.yaml \
  --dry-run

# Actually undo (remove --dry-run)
python scripts/undo_merge.py \
  --merged-dir data/merge_yaml/merged_2026 \
  --normalized-dir data/normalized_yaml \
  --filter variant_contamination \
  --quality-report reports/merge_quality.yaml \
  --output-dir data/merge_yaml/restored
```

---

### 5. Generate Monitoring Dashboard

```bash
source .venv/bin/activate

python scripts/monitor_merges.py \
  --merged-dir data/merge_yaml/merged_2026 \
  --quality-report reports/merge_quality.yaml \
  --output reports/merge_dashboard.yaml

# View dashboard
cat reports/merge_dashboard.yaml
```

**Output**: Comprehensive quality dashboard with actionable recommendations.

---

## 📁 Key Files & Locations

### Input Data
- `data/normalized_yaml/` - 15,431 normalized recipes (organized by category)

### Output Data
- `data/merge_yaml/merged_2026/` - New baseline merge (running now)
- `data/merge_yaml/merged/` - Previous merge (Feb 2026, 1,350 recipes)
- `data/merge_yaml/merge_stats_2026.json` - New baseline statistics

### Reports
- `reports/fingerprint_comparison.yaml` - Fingerprint mode analysis
- `reports/mode_comparison.yaml` - Merge mode comparison
- `reports/merge_quality.yaml` - Quality validation results
- `reports/merge_dashboard.yaml` - Monitoring dashboard

### Core Modules
- `src/culturemech/merge/hierarchy_fingerprint.py` - Hierarchy-aware fingerprinting
- `src/culturemech/merge/merge_rules.py` - Merge rule engine
- `src/culturemech/merge/fingerprint.py` - Original fingerprinter (baseline)
- `src/culturemech/merge/merger.py` - Recipe merger
- `src/culturemech/merge/merge_recipes.py` - Main CLI script

---

## 🧪 Testing on Small Subsets

All scripts support `--limit` to test on smaller datasets:

```bash
# Test fingerprint comparison on 1000 recipes
python scripts/compare_fingerprints.py \
  --mim-repo /path/to/MediaIngredientMech \
  --limit 1000

# Test merge modes on 1000 recipes
python scripts/test_merge_modes.py \
  --mim-repo /path/to/MediaIngredientMech \
  --modes all \
  --limit 1000

# Test quality validation on 500 recipes
python scripts/validate_merge_quality.py \
  --merged-dir data/merge_yaml/merged_2026 \
  --mim-repo /path/to/MediaIngredientMech \
  --limit 500
```

---

## 🔍 Checking Baseline Merge Progress

The baseline merge is running in the background. To check status:

```bash
# Check if output directory exists
ls -la data/merge_yaml/merged_2026/

# Count recipes processed so far
find data/merge_yaml/merged_2026 -name "*.yaml" | wc -l

# Check statistics file
cat data/merge_yaml/merge_stats_2026.json 2>/dev/null || echo "Not ready yet"
```

**Expected completion**: 2-5 minutes for 15,431 recipes

---

## 📖 Merge Modes Explained

### Conservative Mode
- **Strategy**: Only merge with explicit rules or exact fingerprint match
- **Use case**: Maximum safety, preserve all distinctions
- **Expected reduction**: ~85%

### Aggressive Mode
- **Strategy**: Merge all variants with same parent ingredient
- **Use case**: Maximum deduplication, ignore variant differences
- **Expected reduction**: ~92%

### Variant-Aware Mode ⭐ **(Recommended)**
- **Strategy**: Merge hydration variants only (CaCl₂·2H₂O = CaCl₂), preserve other distinctions
- **Use case**: Balanced approach - good deduplication while preserving important chemistry
- **Expected reduction**: ~88%

---

## 🎯 Recommended Workflow

**Step 1**: Wait for baseline merge to complete
```bash
# Check if complete
ls data/merge_yaml/merge_stats_2026.json
```

**Step 2**: Validate baseline quality
```bash
source .venv/bin/activate
python scripts/verify_merges.py \
  --normalized-dir data/normalized_yaml \
  --merged-dir data/merge_yaml/merged_2026 \
  --stats-file data/merge_yaml/merge_stats_2026.json
```

**Step 3**: Test hierarchy-aware features (requires MediaIngredientMech)
```bash
# Compare fingerprint modes
python scripts/compare_fingerprints.py \
  --mim-repo /path/to/MediaIngredientMech \
  --limit 5000

# Test merge modes
python scripts/test_merge_modes.py \
  --mim-repo /path/to/MediaIngredientMech \
  --modes all \
  --limit 5000

# Validate quality
python scripts/validate_merge_quality.py \
  --merged-dir data/merge_yaml/merged_2026 \
  --mim-repo /path/to/MediaIngredientMech
```

**Step 4**: Review results and choose mode
```bash
# Compare reports
ls -lh reports/

# View key metrics
cat reports/mode_comparison.yaml | grep -A5 "summary"
cat reports/merge_quality.yaml | grep -A5 "summary"
```

**Step 5**: Deploy chosen mode (see full implementation guide)

---

## 🆘 Troubleshooting

### "ModuleNotFoundError: No module named 'culturemech'"
**Solution**: Activate virtual environment first
```bash
source .venv/bin/activate
```

### "MediaIngredientMech repo not found"
**Solution**: Clone the repository
```bash
git clone https://github.com/microbiomedata/MediaIngredientMech.git
# Then use --mim-repo /path/to/MediaIngredientMech
```

### Scripts run too slowly
**Solution**: Use `--limit` to test on smaller subsets
```bash
python scripts/compare_fingerprints.py --limit 1000 ...
```

### Need to undo a merge
**Solution**: Use rollback script with dry-run first
```bash
python scripts/undo_merge.py --dry-run --recipe-id "CM:123456" ...
```

---

## 📚 More Information

- **Full Implementation Guide**: `HIERARCHY_MERGE_IMPLEMENTATION.md`
- **Hierarchy Integration**: `HIERARCHY_INTEGRATION_SUMMARY.md`
- **Original Plan**: See plan mode transcript
- **Script Help**: Run any script with `--help`

---

## ✅ Next Actions

1. ✅ **Wait for baseline merge** to complete (~2-5 min)
2. ⏳ **Validate baseline** with verify_merges.py
3. ⏳ **Get MediaIngredientMech** repository
4. ⏳ **Test fingerprint modes** (requires MediaIngredientMech)
5. ⏳ **Compare merge modes** (requires MediaIngredientMech)
6. ⏳ **Choose production mode** based on results

**Status check**:
```bash
# Is baseline merge complete?
ls -lh data/merge_yaml/merge_stats_2026.json

# How many recipes merged?
find data/merge_yaml/merged_2026 -name "*.yaml" | wc -l
```

---

**Questions?** Check the full implementation guide or script `--help` output.
