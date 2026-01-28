# MediaDive Concentrations Investigation

**Date**: 2026-01-25
**Question**: Does MediaDive provide ingredient concentrations?
**Answer**: No - concentrations come from MicroMediaParam's PDF parsing

---

## Summary

**MediaDive** (the MongoDB/JSON database) **does NOT include ingredient concentrations** in its main data export. Concentrations were extracted separately by the **MicroMediaParam** pipeline through PDF parsing of DSMZ media documents.

---

## Data Sources Breakdown

### 1. MediaDive Core Data (MongoDB)

**Location**: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/cmm-ai-automation/data/`

**Files**:
- `mediadive_media.json` (1.2 MB) - 3,327 media records
- `mediadive_ingredients.json` (322 KB) - 1,235 ingredients with ChEBI IDs
- `mediadive_solutions.json` (176 KB) - Solution compositions

**What's Included**:
- Media names, IDs, sources
- pH ranges (min/max)
- Links to DSMZ pages
- Ingredient names (no concentrations)
- ChEBI IDs for ingredients

**What's NOT Included**:
- ❌ Ingredient concentrations
- ❌ Detailed composition tables
- ❌ Preparation instructions

### 2. MicroMediaParam Extracted Compositions

**Location**: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MicroMediaParam/MicroMediaParam/media_compositions/`

**Count**: 3,223 total composition files
- **1,813 DSMZ** (MediaDive source)
- **1,410 other sources** (ATCC, CCAP, JCM, NBRC, etc.)

**Extraction Methods**:
1. **pdf_tabular_parsing** - Extract from PDF tables
2. **pdf_text_parsing** - Parse from PDF text
3. **atcc_dotted_line_parsing** - ATCC-specific parsing

**Example** (`dsmz_1_composition.json`):
```json
{
  "medium_id": "dsmz_1",
  "medium_name": "Medium dsmz_1",
  "source": "dsmz",
  "composition": [
    {
      "name": "Peptone",
      "concentration": 5.0,
      "unit": "g",
      "extraction_method": "pdf_tabular_parsing"
    },
    {
      "name": "Meat extract",
      "concentration": 3.0,
      "unit": "g",
      "extraction_method": "pdf_tabular_parsing"
    },
    {
      "name": "Agar, if necessary",
      "concentration": 15.0,
      "unit": "g",
      "extraction_method": "pdf_tabular_parsing"
    }
  ],
  "preparation_instructions": "",
  "extraction_method": "pdf_text_parsing"
}
```

### 3. CultureMech Integration (Already Active!)

**Location**: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/raw/mediadive/compositions/`

**Count**: 1,821 composition files (DSMZ subset)

**Status**: ✅ **Already integrated and working**

The MediaDive importer already uses these composition files:

```python
# From mediadive_importer.py lines 244-263
composition_ingredients = self._parse_composition_ingredients(medium_id)

if composition_ingredients:
    # Use actual composition data
    recipe["ingredients"] = composition_ingredients
else:
    # Fallback to placeholder
    recipe["ingredients"] = [{
        "preferred_term": "See source for composition",
        "concentration": {"value": "variable", "unit": "G_PER_L"},
        "notes": "Full composition available at source database"
    }]
```

---

## How MicroMediaParam Extracted Concentrations

### Pipeline Overview

From MicroMediaParam's CLAUDE.md:

**Stage 1-2: Data Acquisition & Conversion**
```
1. Download PDFs from DSMZ MediaDive REST API
2. Convert PDFs to markdown using pdf2txt.py
3. Extract compositions with tabular and text parsing
4. Store as JSON in media_compositions/
```

**Key Scripts** (from MicroMediaParam):
- `src/scripts/parse_*.py` - PDF parsing scripts
- `src/tools/enhanced_solution_parser.py` - Solution expansion
- PDF parsing libraries: pdfminer, pypdf2

**Extraction Methods**:
1. **Tabular Parsing**: Extracts data from PDF tables
   - Uses pdfminer.six to detect table structures
   - Parses rows with ingredient names, amounts, units

2. **Text Parsing**: Extracts from plain text
   - Pattern matching for "X g/L", "Y mg", etc.
   - Handles various formats and languages

3. **Solution Expansion**: Resolves "solution:241" references
   - Downloads referenced solution PDFs
   - Recursively parses sub-compositions
   - Adjusts concentrations based on dilution ratios

---

## Coverage Statistics

### MediaDive Composition Coverage

**Total MediaDive Media**: 3,327
**With Compositions in MicroMediaParam**: 1,813 (54.4%)
**Available in CultureMech**: 1,821 (54.7%)

**Coverage by Source**:
- DSMZ media: ~1,813 compositions
- Other sources: ~1,410 compositions (ATCC, CCAP, etc.)
- **Total**: 3,223 composition files

### Why Not 100% Coverage?

Some MediaDive entries lack compositions because:
1. **PDF not available** - Some media PDFs not downloaded
2. **Parsing failures** - Complex formats not parsed
3. **Historical media** - Older entries may lack detailed PDFs
4. **Reference-only media** - Some entries reference other sources

---

## Current CultureMech Usage

### Fetch Command

The composition files are automatically used when available:

```bash
# MediaDive import checks for compositions automatically
just import-mediadive

# Internally runs:
# uv run python -m culturemech.import.mediadive_importer \
#     -i data/raw/mediadive \
#     -o kb/media \
#     --compositions data/raw/mediadive/compositions
```

### Import Behavior

**If composition found** (54.4% of media):
```yaml
ingredients:
  - preferred_term: "Peptone"
    term:
      id: "CHEBI:8526"
      label: "peptone"
    concentration:
      value: "5.0"
      unit: "G_PER_L"
```

**If composition NOT found** (45.6% of media):
```yaml
ingredients:
  - preferred_term: "See source for composition"
    concentration:
      value: "variable"
      unit: "G_PER_L"
    notes: "Full composition available at source database"
```

---

## Improving Coverage

### Option 1: Update from MicroMediaParam

MicroMediaParam has more composition files (1,813) than currently in CultureMech (1,821 - some may be duplicates or updated).

**Action**:
```bash
# Copy updated composition files
cp -r /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MicroMediaParam/MicroMediaParam/media_compositions/dsmz_* \
      /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/raw/mediadive/compositions/

# Re-import MediaDive
just import-mediadive
```

### Option 2: Use MicroMediaParam Pipeline

Run the full MicroMediaParam pipeline to extract fresh compositions:

**Steps**:
1. Download DSMZ PDFs (Stage 1)
2. Convert to markdown (Stage 2)
3. Extract compositions (Stage 2)
4. Copy to CultureMech

**Requirements**:
- pdfminer.six, pypdf2
- DSMZ MediaDive API access
- ~30-60 minutes processing time

### Option 3: Use KOMODO for Concentrations

KOMODO provides molar concentrations which could complement MediaDive:
- KOMODO: ~3,335 media with mM concentrations
- MediaDive: ~3,327 media (54% with g/L concentrations)
- Overlap: ~90% (same DSMZ source)

**Strategy**: Import both, KOMODO enriches MediaDive with molar units

---

## Recommendations

### Immediate (No Action Needed)

✅ **Current system already works**:
- 1,821 composition files active
- 54% coverage with concentrations
- Automatic fallback for missing compositions

### Short-term (Optional Enhancement)

**Sync with latest MicroMediaParam data**:
```bash
# Update compositions from MicroMediaParam
cd /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MicroMediaParam/MicroMediaParam
make status  # Check if pipeline is up to date

# Copy to CultureMech
rsync -av media_compositions/dsmz_* \
    ../CultureMech/data/raw/mediadive/compositions/

# Re-import
cd ../CultureMech
just import-mediadive
```

### Long-term (Phase 3)

**Integrate KOMODO for enhanced concentrations**:
- KOMODO provides standardized mM concentrations
- Can backfill MediaDive media with quantitative data
- Enables metabolic modeling use cases

---

## Key Insights

1. **MediaDive ≠ Full Compositions**
   - MediaDive (MongoDB) has metadata only
   - Compositions extracted separately from PDFs

2. **MicroMediaParam is Critical**
   - All concentration data comes from this pipeline
   - PDF parsing is essential for quantitative data

3. **Already Integrated**
   - CultureMech already uses MicroMediaParam compositions
   - 54% coverage is reasonable for a scraped dataset

4. **KOMODO Complements MediaDive**
   - KOMODO: molar concentrations (mM)
   - MediaDive: mass concentrations (g/L)
   - Both from DSMZ source, high overlap

---

## Files Reference

### MediaDive Core (cmm-ai-automation)
- `data/mediadive_media.json` - Media metadata
- `data/mediadive_ingredients.json` - Ingredient names + ChEBI
- `data/mediadive_solutions.json` - Solution recipes

### MicroMediaParam Compositions
- `media_compositions/dsmz_*.json` - 1,813 DSMZ compositions
- `media_compositions/atcc_*.json` - ATCC compositions
- `media_compositions/ccap_*.json` - Algae compositions
- `media_texts/dsmz_*.md` - Markdown source files

### CultureMech Integration
- `data/raw/mediadive/compositions/` - Active composition files
- `src/culturemech/import/mediadive_importer.py` - Import logic
- `kb/media/bacterial/*.yaml` - Final recipes with concentrations

---

## Conclusion

**MediaDive does NOT provide concentrations** in its core database. All concentration data comes from **MicroMediaParam's PDF parsing pipeline**, which:

1. Downloads DSMZ media PDFs
2. Parses tables and text for compositions
3. Extracts concentrations (g, mg, mL, etc.)
4. Maps to ChEBI IDs
5. Stores as structured JSON

**CultureMech already uses this data** and has 54% coverage with concentrations. The system works well and no immediate action is needed.

**For better coverage**, consider:
- Syncing with latest MicroMediaParam data
- Integrating KOMODO for molar concentrations
- Running MicroMediaParam pipeline for fresh extractions

---

**Investigation Complete**: 2026-01-25
**Status**: ✅ System working as designed
**Coverage**: 1,821/3,327 media (54.7%) with concentrations
