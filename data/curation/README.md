# Organism Data Curation

This directory contains files for curating organism metadata in CultureMech YAML files.

## Files

- `organism_candidates.json` - Extracted organism data from pattern matching (2,104 high-confidence candidates)
- `organism_review.csv` - Human-reviewable spreadsheet for approving/rejecting extractions

## Workflow

### Step 1: Pattern Extraction ✅ COMPLETED

Extracted 2,104 high-confidence organism candidates from 10,595 YAML files using conservative patterns:

```bash
uv run python -m culturemech.curate.organism_extractor \
  --input data/normalized_yaml \
  --output data/curation/organism_candidates.json \
  --confidence-threshold high \
  --skip-ncbi
```

**Initial extraction**: 2,488 candidates
**False positives removed**: 384 entries (algae media, medium types, strain codes, chemical names)
**Final curated data**: 2,104 organism-specific media (19.9% of all media)

**Results by category:**
- 2,052 bacterial media (97.5%)
- 41 archaea media (1.9%)
- 7 specialized media (0.3%)
- 4 fungal media (0.2%)

### Step 2: Generate Review CSV ✅ COMPLETED

Created a CSV for manual review:

```bash
uv run python -m culturemech.curate.curation_validator \
  --input data/curation/organism_candidates.json \
  --output data/curation/organism_review.csv
```

### Step 3: Manual Review (OPTIONAL)

The automated filtering removed 384 false positives. The remaining 2,104 entries are high-confidence organism-specific media. Manual review is optional but recommended to catch any edge cases.

Open `organism_review.csv` in a spreadsheet editor and:

1. Review the `extracted_organism` column
2. Set `approve` to `FALSE` for any remaining incorrect extractions
3. Save the file

**Examples of correctly extracted organisms:**
- "BACILLUS PASTEURII"
- "Escherichia coli"
- "RHODOBACTER SPHAEROIDES"
- "METHANOCALDOCOCCUS JANNASCHII"
- "Thermotoga maritima"

### Step 4: Apply Approved Curations (TODO)

After optional manual review, apply curations to YAML files:

```bash
# Dry run to preview changes
uv run python -m culturemech.curate.yaml_updater \
  --input data/curation/organism_review.csv \
  --yaml-dir data/normalized_yaml \
  --dry-run

# Apply changes
uv run python -m culturemech.curate.yaml_updater \
  --input data/curation/organism_review.csv \
  --yaml-dir data/normalized_yaml
```

### Step 5: Add NCBI Taxon IDs (OPTIONAL)

After applying curations, you can add NCBI taxon IDs in a separate pass to avoid rate limiting:

```bash
# Re-run with NCBI lookups for approved organisms
uv run python -m culturemech.curate.organism_extractor \
  --input data/normalized_yaml \
  --output data/curation/organisms_with_ncbi.json \
  --confidence-threshold high \
  --ncbi-email your@email.com
```

### Step 6: Regenerate Browser & Commit (TODO)

```bash
just gen-browser-data
just gen-pages

git add data/normalized_yaml/ app/data.js
git commit -m "Add organism curation for 2,104 organism-specific media

Populated target_organisms and organism_culture_type fields based on:
- Conservative pattern-based extraction from medium names
- Automated filtering of 384 false positives (medium types, strains, chemicals)
- High-confidence organism name identification

Covers 19.9% of all media (2,104 of 10,595 files).

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"

git push
```

## Extraction Patterns Used

### High-confidence patterns:

1. **[Genus species] MEDIUM** - e.g., "Escherichia coli Medium"
2. **MEDIUM FOR [Genus species]** - e.g., "Medium for Halorhodospira"
3. **DSMZ_###_GENUS_SPECIES_MEDIUM** - e.g., "DSMZ 1457 ALCALILIMNICOLA EHRLICHII MEDIUM"

### Culture type classification:

- **isolate**: Medium name contains specific organism name (2,104 media)
- **community**: Contains "co-culture", "consortium", "mixed culture" (0 found with high confidence)

## Automated False Positive Filtering

**Removed 384 entries** including:

- **Algae media** (16): "Bold Basal", "Artificial Seawater" (medium formulation names)
- **Medium types** (134): "Chopped Meat", "Reinforced Clostridial", "Tryptic SOY"
- **Medium components** (84): "Yeast Extract", "Tryptone", "Peptone"
- **Medium codes** (77): "Modified YMA", "Modified HNW", "Alkali A"
- **Strain designations** (48): "strain JA", "Strain Pf12B"
- **Chemical names** (25): "Nicotinic acid", "Levulinic acid", "Diethyl phosphonate"

## Conservative Approach

✅ Only populated where evidence is unambiguous
✅ Automated filtering for common false positive patterns
✅ Manual review optional (most FPs already removed)
✅ Dry-run mode for safety
✅ Preserve original data (don't overwrite existing fields)
✅ Track curation history
✅ Skip NCBI lookups initially (avoid rate limits)

## Expected Outcomes

- **~2,100 files** with `target_organisms` populated (actual: 2,104)
- **~2,100 files** with `organism_culture_type = "isolate"` (actual: 2,104)
- **~8,500 files** remain blank (generic/ambiguous media)
- **NCBITaxon coverage**: Can be added in future pass with NCBI API lookups
- **Strain coverage**: 9 media have strain IDs (DSM, ATCC, JCM patterns)

## Future Work

1. **NCBI Taxonomy enrichment** - Batch lookup with caching
2. **GTDB genome mapping** - Requires GTDB database integration
3. **Source DB API enrichment** - Query DSMZ/JCM/ATCC APIs for additional metadata
4. **Community media detection** - Better patterns for co-culture media
5. **Strain catalog integration** - Link to strain databases
