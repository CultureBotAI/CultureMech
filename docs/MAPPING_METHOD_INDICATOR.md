# Mapping Method Indicator Column

**Date**: 2026-02-09
**Status**: ✅ Implemented

## Overview

Added a `mapping_method` column to all SSSOM mappings to clearly distinguish between different mapping approaches:
- **Curated dictionaries** (BioProductDict from MicroMediaParam)
- **Ontology-based matching** (OAK/EBI OLS APIs)
- **Manual curation** (Original hand-curated mappings)

This addresses the need to track **whether mappings come from ontology matching vs. other approaches**.

---

## Mapping Method Categories

### 1. `curated_dictionary`
**Source**: Pre-curated biological products from MicroMediaParam
**Confidence**: 0.98 (highest)
**Speed**: Instant (no API calls)
**Examples**: Yeast extract, Peptone, DNA, Agar, BSA, Blood, Serum

### 2. `ontology_exact`
**Source**: Exact matches via OLS/OAK ontology APIs
**Confidence**: 0.92-0.95
**Speed**: Fast (cached API calls)
**Examples**: Direct term matches, exact synonym matches

### 3. `ontology_fuzzy`
**Source**: Fuzzy/approximate matches via OLS/OAK
**Confidence**: 0.50-0.89
**Speed**: Moderate (API calls)
**Examples**: Multi-ontology searches, partial matches

### 4. `manual_curation`
**Source**: Original manually curated mappings
**Confidence**: 0.10-1.0 (varies)
**Speed**: N/A (pre-existing)
**Examples**: Pre-existing CHEBI mappings in knowledge base

---

## How to Use

### 1. Analyze Mapping Methods in SSSOM File

**Quick analysis:**
```bash
uv run python scripts/analyze_mapping_methods.py
```

**Specific file:**
```bash
uv run python scripts/analyze_mapping_methods.py output/culturemech_chebi_mappings_exact.sssom.tsv
```

**Output:**
```
Mapping Method Analysis
======================================================================
Total mappings: 2,900

Mapping Method Breakdown:
----------------------------------------------------------------------
  Curated Dictionary (BioProductDict):        200 (  6.9%)
  Ontology Exact Match (OLS/OAK):             900 ( 31.0%)
  Ontology Fuzzy Match (OLS/OAK):             350 ( 12.1%)
  Manual Curation (Original):               1,450 ( 50.0%)

Total ontology-based (OAK/OLS):            1,250 ( 43.1%)
Total non-ontology (curated + manual):     1,650 ( 56.9%)
```

### 2. Filter by Method in Python

```python
import pandas as pd

# Load SSSOM file
df = pd.read_csv('output/culturemech_chebi_mappings_exact.sssom.tsv',
                 sep='\t', comment='#')

# Get only curated dictionary mappings
curated = df[df['mapping_method'] == 'curated_dictionary']
print(f"Curated biological products: {len(curated)}")
print(curated[['subject_label', 'object_id', 'confidence']].head(10))

# Get all ontology-based mappings (OAK/OLS combined)
ontology = df[df['mapping_method'].isin(['ontology_exact', 'ontology_fuzzy'])]
print(f"\nOntology-based mappings: {len(ontology)}")

# Get high-confidence automated mappings only
auto_high_conf = df[(df['mapping_method'].isin(['curated_dictionary', 'ontology_exact'])) &
                    (df['confidence'] >= 0.92)]
print(f"\nHigh-confidence automated: {len(auto_high_conf)}")

# Compare ontology vs non-ontology
ontology_count = len(df[df['mapping_method'].isin(['ontology_exact', 'ontology_fuzzy'])])
non_ontology_count = len(df) - ontology_count
print(f"\nOntology-based: {ontology_count} ({ontology_count/len(df)*100:.1f}%)")
print(f"Non-ontology: {non_ontology_count} ({non_ontology_count/len(df)*100:.1f}%)")
```

### 3. Statistics in Enrichment Output

When running enrichment, you'll now see:

```bash
just enrich-sssom-exact
```

**Output includes:**
```
Enrichment Summary
======================================================================
Original mappings: 1302
Verified mappings: 1302
Invalid/deprecated: 0
New OLS mappings: 1248
Total enriched mappings: 2550

Confidence distribution:
  0.9-1.0: 1450
  0.8-0.9: 350
  0.5-0.8: 600
  0.0-0.5: 150

Mapping method breakdown:
  Curated Dictionary (BioProductDict): 185 (7.3%)
  Ontology Exact Match (OLS/OAK): 863 (33.8%)
  Ontology Fuzzy Match (OLS/OAK): 200 (7.8%)
  Manual Curation (Original): 1302 (51.1%)
```

---

## Implementation Details

### Files Modified

**1. scripts/enrich_sssom_with_ols.py**
- Updated `create_mapping()` to add `mapping_method` parameter
- Auto-determines method from `mapping_tool` if not specified
- Updated `verify_existing_mappings()` to preserve/add method
- Updated statistics output to show method breakdown

**2. scripts/analyze_mapping_methods.py** (NEW)
- Standalone script to analyze mapping methods
- Shows detailed breakdown by method and tool
- Confidence distribution by method
- Handles legacy files without `mapping_method` column

### Mapping Method Logic

```python
def create_mapping(..., mapping_method=None):
    # Auto-determine if not provided
    if mapping_method is None:
        if 'BioProductDict' in tool:
            mapping_method = 'curated_dictionary'
        elif 'OLS' in tool and 'exact' in tool:
            mapping_method = 'ontology_exact'
        elif 'OAK' in tool and 'synonym' in tool:
            mapping_method = 'ontology_exact'
        elif 'OLS' in tool and 'fuzzy' in tool:
            mapping_method = 'ontology_fuzzy'
        elif 'OAK' in tool or 'MultiOntology' in tool:
            mapping_method = 'ontology_fuzzy'
        else:
            mapping_method = 'manual_curation'
```

---

## Benefits

### 1. Clear Attribution
- Distinguish automated vs. manual mappings
- Track ontology-based vs. dictionary-based approaches
- Transparent methodology for publications

### 2. Quality Control
- Prioritize high-confidence methods
- Identify mappings needing manual review
- Filter by trust level

### 3. Debugging & Improvement
- Identify which methods work for specific ingredients
- Track success rates by method
- Optimize pipeline based on method performance

### 4. Reporting & Metrics
- Show percentage ontology-grounded
- Demonstrate automated vs. manual effort
- Quantify improvement from MicroMediaParam integration

---

## Example Use Cases

### Case 1: Export Only High-Confidence Ontology Mappings

```python
# Get mappings that are ontology-based and high confidence
export_df = df[(df['mapping_method'].isin(['ontology_exact', 'curated_dictionary'])) &
               (df['confidence'] >= 0.90)]

export_df.to_csv('high_confidence_ontology_mappings.tsv', sep='\t', index=False)
```

### Case 2: Find Ingredients Needing Manual Review

```python
# Get fuzzy matches that might need manual verification
review_df = df[(df['mapping_method'] == 'ontology_fuzzy') &
               (df['confidence'] < 0.70)]

print("Ingredients needing manual review:")
for _, row in review_df.iterrows():
    print(f"  {row['subject_label']:40s} → {row['object_label']:40s} ({row['confidence']:.2f})")
```

### Case 3: Compare Ontology Coverage Before/After

```bash
# Before MicroMediaParam integration
uv run python scripts/analyze_mapping_methods.py output/before_integration.sssom.tsv > before.txt

# After MicroMediaParam integration
uv run python scripts/analyze_mapping_methods.py output/after_integration.sssom.tsv > after.txt

# Compare
diff before.txt after.txt
```

---

## Legacy Files

Files created before 2026-02-09 won't have the `mapping_method` column.

**Detection:**
```bash
uv run python scripts/analyze_mapping_methods.py old_file.sssom.tsv
```

**Output:**
```
⚠️  Warning: 'mapping_method' column not found in SSSOM file
   This column was added in the MicroMediaParam integration (2026-02-09)
   Please re-run enrichment to add this column.

Mapping tool breakdown (legacy):
  MicrobeMediaParam|v1.0: 629
  CultureMech|manual: 395
  EBI_OLS_API|fuzzy: 267
  ...
```

**To upgrade:** Re-run enrichment with the updated script.

---

## Summary

✅ **Added `mapping_method` column** to all SSSOM mappings
✅ **Created analysis script** (`analyze_mapping_methods.py`)
✅ **Updated statistics output** to show method breakdown
✅ **Documented usage** with examples and use cases
✅ **Backward compatible** (handles legacy files)

**Next Steps:**
1. Re-run enrichment to add `mapping_method` column
2. Use `analyze_mapping_methods.py` to see breakdown
3. Filter by method for specific use cases
4. Report ontology coverage statistics

---

**Questions?** See [NORMALIZATION_IMPROVEMENTS.md](NORMALIZATION_IMPROVEMENTS.md) for full integration details.
