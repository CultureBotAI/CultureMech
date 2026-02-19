# Organism Data Curation Implementation

## Overview

Implemented a conservative, pattern-based organism data extraction system for CultureMech YAML files with manual review workflow.

## Implementation Summary

### Created Scripts

1. **`src/culturemech/curate/organism_extractor.py`** - Pattern-based organism extraction
   - Extracts organism names from medium names using regex patterns
   - Identifies culture type (isolate/community)
   - Extracts strain IDs (DSM, ATCC, JCM)
   - Optional NCBI Taxonomy API lookups
   - Filters generic media names

2. **`src/culturemech/curate/curation_validator.py`** - Review CSV generation
   - Converts JSON extractions to human-reviewable CSV
   - Supports approval workflow (TRUE/FALSE column)
   - Loads approved curations for YAML updating

3. **`src/culturemech/curate/yaml_updater.py`** - YAML file updater
   - Adds `target_organisms` with OrganismDescriptor entries
   - Sets `organism_culture_type` (isolate/community)
   - Adds curation history entries
   - Dry-run mode for preview
   - Skips files with existing organism data

### Extraction Patterns

#### High-confidence (genus + species):
- `[Genus species] MEDIUM` - "Escherichia coli Medium"
- `MEDIUM FOR [Genus species]` - "Medium for Halorhodospira"
- `DSMZ_###_GENUS_SPECIES_MEDIUM` - "DSMZ 1457 ALCALILIMNICOLA EHRLICHII MEDIUM"

#### Medium-confidence (genus only):
- `[Genus] MEDIUM` - "Azotobacter Medium" (could be generic)

#### Culture type indicators:
- **isolate**: Organism name in title + (strain-specific OR single organism)
- **community**: Explicit "co-culture", "consortium", "mixed culture"

### Filtered Generic Media

Avoided false positives by filtering:
- NUTRIENT, LB, R2A, TSA, TSB, M9, MINIMAL, RICH, STANDARD, GENERAL, BASIC, COMPLEX

Uses word boundaries to prevent false positives (e.g., "coli" doesn't match "LB").

## Current Results

### Extraction Statistics

Processed **10,595 YAML files**, extracted **2,472 high-confidence candidates**:

- **2,377** bacterial media (96.2%)
- **44** archaea media (1.8%)
- **39** specialized media (1.6%)
- **12** fungal media (0.5%)
- **0** algae media (16 false positives removed - medium formulation names like "Bold Basal", not organisms)

**Culture types:**
- 2,487 isolate
- 1 community

**With strain IDs:** 9 media

**NCBI taxon IDs:** 0 (skipped to avoid rate limiting)

### Quality Assessment

**Good extractions (bacterial/archaea):**
- "BACILLUS SCHLEGELII"
- "RHODOBACA BARGUZINENSIS"
- "THERMODESULFOBACTERIUM AUXILIATOTRIS"
- "DESULFOVIBRIO INOPINATUS"
- "ALCALILIMNICOLA EHRLICHII"

**False positives (still need manual review):**
- "Reinforced Clostridial" (RCM medium type)
- "Tryptic SOY" (medium type)
- "Alkali A" (medium formulation)
- "Modified Schaedler" (medium variant)
- "Chopped meat" (medium ingredient)

**Note:** 16 algae media false positives (like "Bold Basal", "Artificial Seawater") already removed

## Workflow

### Step 1: Extract Patterns ✅ COMPLETED

```bash
uv run python -m culturemech.curate.organism_extractor \
  --input data/normalized_yaml \
  --output data/curation/organism_candidates.json \
  --confidence-threshold high \
  --skip-ncbi
```

**Output:** `data/curation/organism_candidates.json` (2,488 entries)

### Step 2: Generate Review CSV ✅ COMPLETED

```bash
uv run python -m culturemech.curate.curation_validator \
  --input data/curation/organism_candidates.json \
  --output data/curation/organism_review.csv
```

**Output:** `data/curation/organism_review.csv` (ready for review)

### Step 3: Manual Review 🔲 TODO

1. Open `data/curation/organism_review.csv`
2. Review `extracted_organism` column
3. Set `approve` to `FALSE` for false positives
4. Save file

**Focus areas:**
- Media with descriptive names ("Modified", "Reinforced", "Alkali")
- Generic media types that slipped through filters ("Chopped meat", "Tryptic SOY")
- Medium formulation names vs organism names

### Step 4: Apply Approved Curations 🔲 TODO

```bash
# Preview changes
uv run python -m culturemech.curate.yaml_updater \
  --input data/curation/organism_review.csv \
  --yaml-dir data/normalized_yaml \
  --dry-run

# Apply changes
uv run python -m culturemech.curate.yaml_updater \
  --input data/curation/organism_review.csv \
  --yaml-dir data/normalized_yaml
```

### Step 5: Add NCBI Taxon IDs (OPTIONAL) 🔲 TODO

Can be done in a separate pass after manual review to:
- Avoid NCBI API rate limiting during extraction
- Only lookup approved organisms
- Cache results efficiently

### Step 6: Regenerate & Commit 🔲 TODO

```bash
just gen-browser-data
just gen-pages
git add data/normalized_yaml/ app/data.js
git commit -m "Add conservative organism curation for ~2,000 high-confidence media"
git push
```

## YAML Structure

### Before:
```yaml
name: BACILLUS PASTEURII MEDIUM
original_name: BACILLUS PASTEURII MEDIUM
category: imported
medium_type: COMPLEX
# ... ingredients, prep steps, etc.
```

### After:
```yaml
name: BACILLUS PASTEURII MEDIUM
original_name: BACILLUS PASTEURII MEDIUM
category: imported
medium_type: COMPLEX
organism_culture_type: isolate
target_organisms:
- preferred_term: BACILLUS PASTEURII
  term:
    id: NCBITaxon:492670
    label: Sporosarcina pasteurii
  strain: DSM 33
# ... ingredients, prep steps, etc.
curation_history:
- timestamp: '2026-02-18T...'
  curator: organism-extractor
  action: Added organism data from pattern extraction
  notes: 'Pattern: genus_species_medium, Confidence: high'
```

## Conservative Approach

✅ **Only populate where evidence is unambiguous**
✅ **Manual review required before committing**
✅ **Dry-run mode for safety**
✅ **Preserve original data (don't overwrite existing fields)**
✅ **Track curation history**
✅ **Skip NCBI lookups initially (avoid rate limits)**
✅ **Filter generic media names**
✅ **Default to approve=TRUE for curator convenience**

## Known Limitations

1. **False positives** - Medium names can be ambiguous (e.g., "Bold Basal Medium")
2. **Single-word genus names** - Medium confidence only (could be generic)
3. **Algae media** - High false positive rate (medium type names vs organisms)
4. **NCBI coverage** - Needs separate pass with rate limiting/caching
5. **Strain extraction** - Limited patterns (DSM/ATCC/JCM only)
6. **GTDB mapping** - Deferred to future work

## Expected Final Outcomes

After manual review filtering false positives:

- **~1,500-2,000 files** with validated `target_organisms`
- **~1,400-1,900 files** with `organism_culture_type = "isolate"`
- **~1-10 files** with `organism_culture_type = "community"`
- **~8,500-9,000 files** remain blank (generic/ambiguous)

## Future Enhancements

1. **NCBI Taxonomy enrichment** - Batch lookup with caching
2. **GTDB genome mapping** - Requires GTDB database integration
3. **Source DB API enrichment** - Query DSMZ/JCM/ATCC APIs
4. **Machine learning** - Train classifier on approved data
5. **Community detection** - Better patterns for co-culture media
6. **Strain catalog integration** - Link to strain databases

## Files Created

```
src/culturemech/curate/
├── __init__.py
├── organism_extractor.py      # Pattern extraction engine
├── curation_validator.py      # CSV review workflow
└── yaml_updater.py            # YAML file updater

data/curation/
├── README.md                  # Curation workflow documentation
├── organism_candidates.json   # 2,488 extracted organisms
└── organism_review.csv        # Human review spreadsheet

docs/
└── organism-curation-implementation.md  # This file
```

## Usage Examples

### Extract with NCBI lookups (slow):
```bash
uv run python -m culturemech.curate.organism_extractor \
  --input data/normalized_yaml \
  --output data/curation/organisms_with_ncbi.json \
  --confidence-threshold high \
  --ncbi-email your@email.com
```

### Extract medium-confidence organisms:
```bash
uv run python -m culturemech.curate.organism_extractor \
  --input data/normalized_yaml \
  --output data/curation/organisms_medium.json \
  --confidence-threshold medium \
  --skip-ncbi
```

### Preview updates without writing:
```bash
uv run python -m culturemech.curate.yaml_updater \
  --input data/curation/organism_review.csv \
  --yaml-dir data/normalized_yaml \
  --dry-run | grep "Would update"
```

## Testing

Tested patterns on:
- ✅ "BACILLUS PASTEURII MEDIUM" → "BACILLUS PASTEURII"
- ✅ "Escherichia coli Medium" → "Escherichia coli"
- ✅ "MEDIUM FOR Halorhodospira" → "Halorhodospira"
- ✅ "DSMZ 1457 ALCALILIMNICOLA EHRLICHII MEDIUM" → "Alcalilimnicola Ehrlichii"
- ✅ "NUTRIENT AGAR" → None (filtered)
- ✅ "LB MEDIUM" → None (filtered)
- ✅ Generic filters with word boundaries

## Success Criteria

- [x] Pattern extraction implemented
- [x] Conservative filtering applied
- [x] Manual review workflow created
- [x] YAML updater with dry-run mode
- [x] Documentation complete
- [ ] Manual review completed (~2,488 entries)
- [ ] False positives removed
- [ ] YAML files updated
- [ ] Browser regenerated
- [ ] Changes committed
