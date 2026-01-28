# MediaDive API Composition Data Investigation

**Date**: 2026-01-25
**Question**: Does the MediaDive API provide concentration data?
**Answer**: **YES**, but only through individual endpoint calls, NOT the bulk export

---

## Executive Summary

The MediaDive REST API **DOES provide ingredient concentrations**, but:

1. ✅ **Individual endpoint** (`/rest/medium/:id`) - **HAS full composition data** with concentrations
2. ❌ **Bulk endpoint** (`/rest/media`) - **NO composition data** (metadata only)
3. ⚠️ **Current CultureMech data** - Uses **bulk export only** (no concentrations from API)
4. ✅ **MicroMediaParam** - Fills the gap by **parsing PDFs** (54.7% coverage)

**Key Insight**: The 54.7% coverage limitation is **NOT because the API doesn't provide data** - it's because:
- cmm-ai-automation used the **bulk export** (fast, but no compositions)
- MicroMediaParam used **PDF parsing** (slow, but gets compositions)
- Nobody fetched compositions from the **individual API endpoints**

---

## API Architecture Discovery

### Endpoint 1: Bulk Media List (Currently Used)

**URL**: `https://mediadive.dsmz.de/rest/media`

**Returns**: Metadata only (3,327 media)

**Structure**:
```json
{
  "status": 200,
  "count": 3327,
  "data": [
    {
      "id": 1,
      "name": "NUTRIENT AGAR",
      "complex_medium": 1,
      "source": "DSMZ",
      "link": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1.pdf",
      "min_pH": 7,
      "max_pH": 7,
      "reference": null,
      "description": null
    }
  ]
}
```

**What's Included**:
- ✅ Media names, IDs
- ✅ pH ranges
- ✅ Links to PDFs
- ❌ **NO ingredient lists**
- ❌ **NO concentrations**

**Usage**: This is what cmm-ai-automation exported to `mediadive_media.json`

---

### Endpoint 2: Individual Medium Details (NOT Currently Used)

**URL**: `https://mediadive.dsmz.de/rest/medium/:id`

**Example**: `https://mediadive.dsmz.de/rest/medium/1`

**Returns**: Full composition with concentrations!

**Structure**:
```json
{
  "status": 200,
  "count": 1,
  "data": {
    "medium": {
      "id": 1,
      "name": "NUTRIENT AGAR",
      "complex_medium": "yes",
      "min_pH": 7,
      "max_pH": 7,
      "source": "DSMZ",
      "link": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1.pdf"
    },
    "solutions": [
      {
        "id": 1,
        "name": "Main sol. 1",
        "volume": 1000,
        "recipe": [
          {
            "recipe_order": 1,
            "compound": "Peptone",
            "compound_id": 1,
            "amount": 5,           // ← CONCENTRATION!
            "unit": "g",           // ← UNIT!
            "g_l": 5,              // ← NORMALIZED g/L!
            "optional": 0
          },
          {
            "recipe_order": 2,
            "compound": "Meat extract",
            "compound_id": 2,
            "amount": 3,
            "unit": "g",
            "g_l": 3,
            "optional": 0
          },
          {
            "recipe_order": 3,
            "compound": "Agar",
            "compound_id": 3,
            "condition": "for solid medium",
            "amount": 15,
            "unit": "g",
            "g_l": 15,
            "optional": 0
          },
          {
            "recipe_order": 4,
            "compound": "Distilled water",
            "compound_id": 4,
            "amount": 1000,
            "unit": "ml",
            "optional": 0
          }
        ],
        "steps": [
          {
            "step": "Adjust pH to 7.0."
          },
          {
            "step": "For Bacillus strains the addition of 10.0 mg MnSO4 x H2O is recommended for sporulation."
          }
        ]
      }
    ]
  }
}
```

**What's Included**:
- ✅ Full ingredient lists
- ✅ **Concentrations** (`amount`, `unit`, `g_l`)
- ✅ Solution hierarchies
- ✅ Preparation steps
- ✅ Optional ingredients
- ✅ Conditions

**Cost**: Requires 3,327 individual API calls (one per medium)

---

### Endpoint 3: Flattened Composition (Alternative)

**URL**: `https://mediadive.dsmz.de/rest/medium-composition/:id`

**Purpose**: Returns flattened ingredient list (expands solutions into ingredients)

**Not verified in this investigation** - but documented in `load_mediadive_details.py` line 9

---

## Evidence from cmm-ai-automation Code

### File: `clients/mediadive.py`

**Lines 78-105**: Data class for `SolutionRecipeItem` includes:
```python
@dataclass
class SolutionRecipeItem:
    """A single item in a solution recipe."""
    order: int
    compound: str
    compound_id: int | None = None
    solution_id: int | None = None
    amount: float | None = None       # ← CONCENTRATION
    unit: str | None = None           # ← UNIT
    g_l: float | None = None          # ← GRAMS PER LITER
    mmol_l: float | None = None       # ← MILLIMOLES PER LITER
    condition: str | None = None
    attribute: str | None = None
    optional: bool = False
```

**Analysis**: The client library **CAN handle composition data** - it has data structures for it!

---

### File: `scripts/load_mediadive_details.py`

**Lines 7-12**: Documents detail endpoints:
```python
"""
Detail endpoints:
- /medium/:id - Full medium recipe with solutions and steps
- /medium-composition/:id - Flattened ingredient composition
- /medium-strains/:id - Strains that grow on this medium
- /solution/:id - Solution recipe details
- /ingredient/:id - Ingredient details with synonyms, media usage
"""
```

**Lines 76-100**: Function to fetch and store details:
```python
def fetch_and_store_details(
    source_collection: Collection[dict[str, Any]],
    target_collection: Collection[dict[str, Any]],
    endpoint_template: str,
    id_field: str = "id",
    limit: int | None = None,
) -> int:
    """Fetch details for all items in source collection and store in target."""
```

**Analysis**: Script EXISTS to fetch detailed compositions, but was **NOT run for the export used by CultureMech**

---

## Why cmm-ai-automation Used Bulk Export Only

### Actual Files Exported

**Location**: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/cmm-ai-automation/data/`

**Files**:
1. `mediadive_media.json` - 3,327 media (metadata only, 1.1 MB)
2. `mediadive_ingredients.json` - 1,235 ingredients (315 KB)
3. `mediadive_solutions.json` - 1,514 solutions (172 KB, metadata only)

**What's Missing**:
- ❌ `mediadive_media_details.json` - Individual medium details with compositions
- ❌ `mediadive_compositions.json` - Flattened compositions

### Solutions File Analysis

**Structure of `mediadive_solutions.json`**:
```json
{
  "status": 200,
  "count": 1514,
  "data": [
    {
      "id": 20,
      "name": "Trace element solution SL-4",
      "volume": 1000
      // ← NO recipe ingredients!
      // ← NO concentrations!
    }
  ]
}
```

**Analysis**: Solutions file is from **bulk endpoint**, NOT detail endpoint

---

## Why MicroMediaParam Used PDF Parsing

### The Alternative Approach

MicroMediaParam pipeline chose to parse PDFs instead of using the MediaDive API.

**Possible Reasons**:

1. **Timing**: Pipeline may predate the detail endpoints
2. **Discovery**: May not have known about `/medium/:id` endpoint
3. **Rate Limiting**: 3,327 API calls may have been too slow/risky
4. **Offline Processing**: PDFs allow offline batch processing
5. **Fallback**: PDFs work even if API is down
6. **Validation**: PDFs are the authoritative source (API may lag)

**Result**: PDF parsing achieved 54.7% success rate (1,813/3,327 media)

---

## Coverage Analysis: API vs PDF

### Theoretical Maximum Coverage

**If using `/rest/medium/:id` for all 3,327 media**:

**Assumptions**:
- All media have detail endpoints
- All detail endpoints return composition data
- No rate limiting issues

**Expected Coverage**: Potentially **100%** (3,327/3,327)

**Advantages**:
- ✅ Structured data (JSON)
- ✅ Normalized units (`g_l` field)
- ✅ Machine-readable
- ✅ No PDF parsing errors
- ✅ Includes preparation steps
- ✅ Solution hierarchies preserved

**Disadvantages**:
- ⚠️ Requires 3,327 individual API calls
- ⚠️ Time: ~13 minutes (0.25s delay between requests)
- ⚠️ Risk of rate limiting
- ⚠️ Network dependency
- ⚠️ API version changes could break pipeline

### Actual PDF Parsing Coverage

**MicroMediaParam approach**: Parse DSMZ PDFs

**Coverage**: 54.7% (1,813/3,327)

**Why Not 100%?**
1. **PDF not available** - Not all media have downloadable PDFs
2. **Parsing failures** - Complex layouts, tables, formatting
3. **Historical media** - Older entries with incomplete documentation
4. **Reference-only** - Some say "Same as Medium 141"

**Advantages**:
- ✅ Offline processing
- ✅ Batch processing
- ✅ Authoritative source
- ✅ Works without API

**Disadvantages**:
- ❌ Only 54.7% success rate
- ❌ PDF parsing errors
- ❌ Complex pipeline (12 stages)
- ❌ Requires manual curation

---

## Recommendation: Hybrid Approach

### Optimal Strategy for Maximum Coverage

**Phase 1: Fetch from API** (Priority)
```bash
# Fetch all 3,327 media compositions from API
for medium_id in 1..3327:
    curl "https://mediadive.dsmz.de/rest/medium/{medium_id}"
    sleep 0.25  # Rate limiting

# Expected: ~100% coverage (assuming all endpoints exist)
# Time: ~13 minutes for 3,327 media
```

**Phase 2: PDF Parsing Fallback**
```bash
# For any media that failed API fetch:
# - Parse PDF from link field
# - Use MicroMediaParam pipeline

# Expected: Fill gaps from Phase 1
```

**Phase 3: Validation**
```bash
# Cross-check API data against PDFs
# - PDFs are authoritative source
# - Flag discrepancies
# - Use for quality control
```

### Expected Coverage

| Method | Coverage | Time | Reliability |
|--------|----------|------|-------------|
| API only | **~100%**? | 13 min | High |
| PDF only | **54.7%** | Hours | Medium |
| **Hybrid** | **~95-100%** | 15 min | Highest |

### Implementation Plan

**Step 1: Test API Endpoint Coverage**
```bash
# Sample 100 random media IDs
for id in $(shuf -i 1-3327 -n 100); do
    curl -s "https://mediadive.dsmz.de/rest/medium/$id" | \
        jq -r '.status, .data.solutions[0].recipe[0].compound' 2>/dev/null
done

# Count success rate
# If >90%, proceed with full fetch
```

**Step 2: Full API Fetch**
```python
# Use cmm-ai-automation client
from cmm_ai_automation.scripts.load_mediadive_details import fetch_and_store_details

# Fetch all media details
# Expected output: mediadive_media_details.json
```

**Step 3: Parse and Convert to CultureMech Format**
```python
# New importer: mediadive_api_importer.py
# Similar to mediadive_importer.py but reads API JSON instead of MicroMediaParam
```

**Step 4: Validate Against MicroMediaParam**
```bash
# Compare API concentrations vs PDF concentrations
# Use for quality control
```

---

## Impact on CultureMech

### Current State

**Data Source**: MicroMediaParam PDF parsing only
- Coverage: 54.7% (1,821/3,327 media)
- Source: PDFs downloaded and parsed offline

**Missing**: 45.3% of media (1,506) have no composition data

### Potential Improvement

**New Data Source**: MediaDive API `/rest/medium/:id`
- Expected coverage: ~95-100%?
- Source: Direct API calls
- Time: ~13 minutes for full fetch

**Improvement**: +40-45% coverage (potentially +1,300-1,500 media with compositions)

### Implementation Effort

**Low Effort** (2-3 hours):
1. Test API endpoint coverage (sample 100 media)
2. Create fetch script using cmm-ai-automation client
3. Export to JSON format

**Medium Effort** (1 day):
4. Create new importer for API JSON format
5. Validate schema compliance
6. Test import with 10 media

**High Effort** (2-3 days):
7. Full import all 3,327 media
8. Cross-validate with MicroMediaParam data
9. Update documentation
10. Add to build system

---

## Answers to Key Questions

### Q1: Does the MediaDive API provide concentration data?

**A1**: **YES** - The `/rest/medium/:id` endpoint provides full composition data including:
- Ingredient names
- Concentrations (`amount`, `unit`)
- Normalized g/L values (`g_l` field)
- Solution hierarchies
- Preparation steps

### Q2: Why does CultureMech only have 54.7% coverage?

**A2**: Because cmm-ai-automation used the **bulk export endpoint** (`/rest/media`) which only returns metadata. The **individual detail endpoint** (`/rest/medium/:id`) was not used.

### Q3: Why did MicroMediaParam use PDF parsing instead of the API?

**A3**: Unknown - possible reasons:
- Pipeline predates detail endpoints
- Didn't know about `/medium/:id` endpoint
- Chose authoritative source (PDFs) over API
- Offline processing preference

### Q4: Can we get 100% concentration coverage?

**A4**: **Potentially YES** - by fetching from `/rest/medium/:id` for all 3,327 media. Need to verify:
1. All media have detail endpoints
2. All detail endpoints return composition data
3. No rate limiting issues

### Q5: Should we switch from PDF parsing to API?

**A5**: **Hybrid approach is best**:
- Primary: API fetch (fast, structured)
- Fallback: PDF parsing (handles API failures)
- Validation: Cross-check API vs PDF

---

## Action Items

### Immediate (Verification)

- [ ] Test API endpoint coverage (sample 100 random media IDs)
- [ ] Check rate limiting behavior
- [ ] Verify `/rest/medium-composition/:id` endpoint
- [ ] Count how many media have detail endpoints

### Short-term (Implementation)

- [ ] Create API fetch script using cmm-ai-automation client
- [ ] Export all 3,327 media details to JSON
- [ ] Create `mediadive_api_importer.py` for CultureMech
- [ ] Test import with 10 media

### Long-term (Integration)

- [ ] Full import all API compositions
- [ ] Cross-validate API vs MicroMediaParam data
- [ ] Update MicroGrowAgents database schema
- [ ] Document API as primary source, PDFs as fallback

---

## Conclusion

**Key Finding**: The MediaDive API **DOES provide ingredient concentrations**, but only through individual endpoint calls that were **not used** by cmm-ai-automation.

**Coverage Gap Cause**:
- ❌ NOT because API lacks data
- ❌ NOT because PDFs are the only source
- ✅ Because **bulk export was used instead of detail endpoints**

**Opportunity**: Fetching from `/rest/medium/:id` could potentially achieve **~100% coverage** vs current 54.7%.

**Recommendation**: Implement hybrid approach (API primary, PDF fallback) for maximum coverage and reliability.

---

**Investigation Date**: 2026-01-25
**API Endpoints Tested**:
- ✅ `/rest/media` - Bulk metadata (confirmed: NO compositions)
- ✅ `/rest/medium/1` - Individual details (confirmed: HAS compositions)
- ⏸ `/rest/medium-composition/:id` - Flattened (not tested, but documented)

**Next Step**: Test endpoint coverage on sample of 100 media to verify 100% hypothesis.
