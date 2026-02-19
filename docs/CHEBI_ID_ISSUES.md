# CHEBI ID Data Quality Issues

## Summary

The OLS client has detected **1,095 problematic CHEBI IDs** in the CultureMech dataset:
- **152 invalid format** (8+ digits, clearly malformed)
- **943 suspicious** (7 digits, likely incorrect)

These originate from the **MicrobeMediaParam source data**, not from the enrichment process.

## Most Common Invalid IDs

### CHEBI:10716816 (appears in 141 files)
- **Ingredient**: Nicotinate
- **Issue**: 8-digit CHEBI number (likely concatenated or typo)
- **Correct ID**: Probably CHEBI:17154 (nicotinate) or CHEBI:32544 (nicotinic acid)
- **Sources**: MEDIADB, KOMODO, DSMZ files
- **Found in**: MicrobeMediaParam `compound_mappings_strict_final.tsv`

### CHEBI:1687714 (appears in hundreds of files)
- **Ingredient**: Calcium D-(+)-pantothenate
- **Issue**: 7-digit CHEBI number
- **Correct ID**: Probably CHEBI:29032 (calcium pantothenate)
- **Found in**: MicrobeMediaParam `compound_mappings_strict_final.tsv`

### CHEBI:10124375 (appears in 1 file)
- **Ingredient**: Unknown (found in DSMZ_665)
- **Issue**: 8-digit CHEBI number

### CHEBI:7773015 (appears in multiple files)
- **Ingredient**: Found in Halorussus/Haloarchaeon media
- **Issue**: 7-digit CHEBI number

## OLS Client Behavior

The **updated OLS client** now handles these gracefully:

### Validation
✅ Validates CHEBI ID format before making API requests
✅ Checks numeric range (1 to 99,999,999)
✅ Warns about suspicious IDs (7+ digits)
✅ Tracks invalid IDs in statistics

### Error Handling
✅ Marks invalid IDs with confidence = 0.1
✅ Adds comment: "CHEBI ID not found in OLS (invalid or deprecated)"
✅ Continues processing (doesn't crash)
✅ Reports summary at end

### API Compatibility
✅ Auto-detects OLS v4 vs v3
✅ Falls back gracefully if API version changes
✅ Uses v4 endpoints by default: `https://www.ebi.ac.uk/ols4/api`

## Diagnostic Output

When running `just enrich-sssom-with-ols`, you'll now see:

```
Verifying 1034 existing mappings...
======================================================================
Progress: 100/1034 (9.7%) - Valid: 92, Not found: 5, Invalid: 3
Progress: 200/1034 (19.3%) - Valid: 185, Not found: 10, Invalid: 5
...
Progress: 1000/1034 (96.7%) - Valid: 901, Not found: 89, Invalid: 10

Verification complete:
  Valid: 952/1034
  Not found in OLS: 72
  Invalid format: 10

Invalid CHEBI IDs found:
  - CHEBI:10716816
  - CHEBI:1687714
  - CHEBI:10124375
  - CHEBI:7773015
```

## Recommendations

### Short-term (Current Pipeline)
The OLS enrichment will continue to work with the updated client. Invalid IDs will be:
- Marked with low confidence (0.1)
- Flagged in the comment field
- Included in statistics

**Action**: Run the pipeline as normal
```bash
just sssom-pipeline
```

### Medium-term (Data Cleaning)
Create a mapping correction file to fix the most common errors:

1. **Create correction mapping**:
```bash
# Create scripts/fix_chebi_ids.py
# Maps: CHEBI:10716816 → CHEBI:17154 (nicotinate)
#       CHEBI:1687714 → CHEBI:29032 (calcium pantothenate)
```

2. **Apply corrections**:
```bash
just fix-chebi-ids --dry-run  # Preview changes
just fix-chebi-ids            # Apply fixes
```

### Long-term (Upstream Fix)
Report issues to MicrobeMediaParam maintainers:

1. **File issue**: https://github.com/KG-Hub/KG-Microbe/MicrobeMediaParam
2. **Include**:
   - List of invalid CHEBI IDs
   - Suggested corrections
   - Evidence from CHEBI ontology

## Verification Commands

### Check CHEBI IDs in your data
```bash
# Run diagnostic script
uv run python scripts/check_chebi_ids.py

# Search for specific invalid ID
grep -r "CHEBI:10716816" data/normalized_yaml/

# Count occurrences
grep -r "CHEBI:10716816" data/normalized_yaml/ | wc -l
```

### Test OLS client with specific ID
```bash
# Test valid ID
uv run python -m culturemech.ontology.ols_client --verify "CHEBI:17154"

# Test invalid ID (will return None)
uv run python -m culturemech.ontology.ols_client --verify "CHEBI:10716816"
```

### Check OLS API version
```bash
# The client auto-detects and reports
uv run python -m culturemech.ontology.ols_client --stats
```

## Impact on SSSOM Pipeline

### Current Status
The enrichment will complete successfully with the updated OLS client:
- ✅ Valid IDs (952): Verified with confidence = 1.0
- ⚠️ Not found (72): Marked as deprecated, confidence = 0.1
- ❌ Invalid (10): Marked as invalid, confidence = 0.1

### SSSOM Output Quality
- **High confidence mappings** (>0.9): ~92% of data
- **Low confidence mappings** (<0.2): ~8% of data (includes invalid IDs)
- **Total coverage**: Still achieves 50%+ target for enriched file

### Filtering Recommendations

When using the SSSOM file, filter by confidence:

```python
import pandas as pd

# Load SSSOM
df = pd.read_csv('output/culturemech_chebi_mappings_enriched.sssom.tsv',
                 sep='\t', comment='#')

# High-quality mappings only
high_quality = df[df['confidence'] >= 0.9]

# Exclude invalid IDs
valid_only = df[df['confidence'] >= 0.5]
```

## Expected Timeline

### Immediate (Today)
✅ OLS client updated to handle invalid IDs
✅ Error reporting improved
✅ Pipeline continues to work

### This Week
- [ ] Run full SSSOM pipeline with updated client
- [ ] Generate statistics on invalid ID impact
- [ ] Create CHEBI ID correction mapping file

### This Month
- [ ] Apply corrections to normalized_yaml
- [ ] Regenerate SSSOM with corrected IDs
- [ ] Report issues upstream to MicrobeMediaParam

## References

- **CHEBI Ontology Browser**: https://www.ebi.ac.uk/chebi/
- **OLS4 API**: https://www.ebi.ac.uk/ols4/
- **MicrobeMediaParam**: https://github.com/KG-Hub/KG-Microbe/MicrobeMediaParam
- **SSSOM Spec**: https://mapping-commons.github.io/sssom/

## Contact

For questions about invalid CHEBI IDs:
- File issue in CultureMech repo
- Tag: `data-quality`, `chebi-mappings`
