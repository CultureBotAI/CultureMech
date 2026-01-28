# ATCC Media Raw Data

## Source Information

**Source**: ATCC (American Type Culture Collection)
**URL**: https://www.atcc.org/
**Media Formulations**: https://www.atcc.org/resources/microbial-media-formulations
**Date Obtained**: 2026-01-21
**Version**: No versioning available (web-based catalog)
**License**: ATCC Terms of Use - https://www.atcc.org/about/terms-of-use
**Contact**: marcin
**Organization**: ATCC (American Type Culture Collection), Manassas, Virginia, USA

## Database Information

**Organization**: ATCC - Leading biological materials repository
**Country**: United States
**Type**: Commercial catalog (no public API)
**Catalog System**: Numeric medium numbers (e.g., ATCC Medium 1306)
**Total Media**: "Thousands" according to ATCC website (exact count not public)

## Data Availability Challenges

### No Public API or Bulk Download

Unlike MediaDive and TOGO Medium, ATCC does not provide:
- ❌ Public REST API for media data
- ❌ Bulk data downloads
- ❌ SPARQL endpoint
- ❌ Structured database exports

### Access Methods

**Current Available Options**:

1. **Individual Product Pages** (Limited)
   - Media formulations embedded in strain product pages
   - Access via search: "ATCC Medium [number]"
   - Example: https://www.atcc.org/products?keywords=ATCC%20Medium%201306
   - Format: HTML pages (requires web scraping)

2. **PDF Documents** (Very Limited)
   - Some media available as PDFs from historical requests
   - Example: `ATCC Medium 1306.pdf` (NMS medium)
   - Example: `ATCC Medium 2099.pdf`
   - Location: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/cmm-ai-automation/papers/`

3. **MicroMediaParam Extractions** (Very Limited)
   - 4 ATCC media extracted from PDFs
   - Location: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MicroMediaParam/`
   - Files: `atcc_2432_composition.json`, `atcc_D3547D63F887423DAFB39841A5B588B9_composition.json`

4. **Cross-References** (Indirect)
   - Many ATCC media are identical to DSMZ media
   - Example: ATCC 1306 = DSMZ 632 (NMS medium)
   - Can import via MediaDive with ATCC cross-reference

## Files in this Directory

### atcc_media_manual.json
- **Description**: Manually curated ATCC media from PDFs and web sources
- **Format**: JSON array of media objects
- **Content**: Medium ID, name, ingredients with concentrations, preparation notes

**Schema**:
```json
{
  "atcc_id": "1306",
  "name": "Nitrate Mineral Salts Medium (NMS)",
  "ingredients": [
    {
      "name": "MgSO4·7H2O",
      "concentration": 1.0,
      "unit": "g/L"
    }
  ],
  "ph": 7.0,
  "source_pdf": "ATCC Medium 1306.pdf",
  "cross_references": {
    "dsmz": "632"
  }
}
```

### atcc_crossref.json
- **Description**: Mapping of ATCC IDs to other database IDs
- **Format**: JSON object mapping ATCC → DSMZ/TOGO/etc.
- **Purpose**: Avoid duplication, leverage existing imports

**Schema**:
```json
{
  "1306": {
    "dsmz": "632",
    "name": "NMS Medium",
    "verified": true
  }
}
```

### atcc_extracted/ (subdirectory)
- **Description**: Media extracted from MicroMediaParam
- **Format**: Individual JSON files per medium
- **Content**: Copied from MicroMediaParam pipeline output

## Known ATCC Media

From available data and documentation:

| ATCC ID | Name | Status | Source |
|---------|------|--------|--------|
| 1306 | Nitrate Mineral Salts (NMS) | ✅ PDF + Verified | = DSMZ 632 |
| 2099 | Unknown | ✅ PDF Available | cmm-ai-automation |
| 2432 | Unknown | ✅ JSON Available | MicroMediaParam |
| D3547... | Unknown | ✅ JSON Available | MicroMediaParam |

## Data Collection Strategies

### Strategy 1: Manual Curation from PDFs (Current)

**Approach**:
1. Collect PDF documents for specific ATCC media
2. Extract composition using PDF parsing
3. Manually verify and create JSON entries
4. Import to CultureMech

**Pros**: High quality, verified data
**Cons**: Very slow, limited coverage
**Estimated Coverage**: ~10-50 media

### Strategy 2: Cross-Reference Leveraging (Recommended)

**Approach**:
1. Identify ATCC media that are identical to DSMZ media
2. Import via MediaDive with ATCC cross-reference
3. Add ATCC ID as alternative identifier
4. Verify composition matches when possible

**Pros**: Fast, leverages existing imports, good coverage
**Cons**: Only works for duplicated media
**Estimated Coverage**: ~200-500 media (estimated overlap)

### Strategy 3: Web Scraping (Future, Requires Approval)

**Approach**:
1. Programmatically search ATCC website for "ATCC Medium [1-9999]"
2. Parse HTML product pages for formulation data
3. Extract ingredients, concentrations, preparation
4. Respect robots.txt and rate limits

**Pros**: Comprehensive coverage
**Cons**:
- May violate ATCC Terms of Service
- Requires legal review
- Fragile (breaks if website changes)
- Slow (rate limiting required)
**Estimated Coverage**: Could reach 1,000+ media
**Status**: ⚠️ NOT IMPLEMENTED - Requires approval

### Strategy 4: ATCC Partnership (Ideal, Long-term)

**Approach**:
1. Contact ATCC directly
2. Request bulk data export or API access
3. Negotiate data sharing agreement
4. Import comprehensive dataset

**Pros**: Complete, authoritative, legal
**Cons**: Requires institutional relationship, may have costs
**Estimated Coverage**: Complete ATCC catalog
**Status**: ⏳ Future consideration

## Current Implementation: Strategy 1 + 2

**Strategy 1**: Manual curation of available PDFs and JSON files
**Strategy 2**: Cross-reference with MediaDive imports

**Data Sources**:
1. PDFs in cmm-ai-automation/papers/
2. JSON files from MicroMediaParam
3. Verified cross-references (like ATCC 1306 = DSMZ 632)

## Cross-Reference Database

### ATCC ↔ DSMZ Equivalents

Known verified equivalents:

| ATCC | DSMZ | Medium Name | Verification |
|------|------|-------------|--------------|
| 1306 | 632 | NMS (Nitrate Mineral Salts) | ✅ Verified 2026-01-06 |
| (TBD) | (TBD) | (Add as verified) | |

**Verification Process**:
1. Compare ingredient lists
2. Match concentrations
3. Check pH and preparation
4. Document in verification notes

## Data Quality Notes

### Strengths
- High-quality, authoritative formulations
- Used by research institutions worldwide
- Commercial quality control
- Well-documented for purchased media

### Limitations
- No public API or bulk access
- Limited free data availability
- Proprietary catalog
- Requires manual extraction or partnerships
- Some media are proprietary formulations

### Coverage Expectations

**Realistic Goals**:
- Manual curation: 10-50 media
- Cross-references: 200-500 media
- Total ATCC coverage in CultureMech: **~250-550 media**

**For Comparison**:
- MediaDive: 3,327 media (3,146 imported)
- TOGO Medium: 2,917 media (5 test imported)
- ATCC: "Thousands" but limited public access

## Integration with CultureMech

### Import Strategy

1. **Import from MicroMediaParam** (Immediate)
   - Copy 4 existing JSON files
   - Convert to CultureMech YAML
   - Validate against schema

2. **Import from PDFs** (Manual)
   - Extract composition from available PDFs
   - Create JSON intermediate format
   - Convert to CultureMech YAML

3. **Add Cross-References to MediaDive Imports** (Recommended)
   - Update existing DSMZ 632 (NMS) with ATCC:1306 cross-ref
   - Add ATCC IDs to media_term for equivalent media
   - Maintain provenance of both sources

4. **Future Expansion** (As Data Available)
   - Add media as PDFs/data become available
   - Consider partnership for bulk data
   - Expand cross-reference database

### ID Mapping

**ATCC Medium IDs** use format: Numeric (e.g., `1306`, `2099`)
- Map to: `media_term.term.id: "ATCC:1306"`
- Cross-reference: Add to existing DSMZ media when equivalent

**Example YAML**:
```yaml
media_term:
  preferred_term: ATCC Medium 1306
  term:
    id: ATCC:1306
    label: Nitrate Mineral Salts Medium (NMS)
  cross_references:
    - id: DSMZ:632
      label: DSMZ Medium 632
      notes: Verified equivalent composition
```

## Comparison with Other Sources

| Feature | MediaDive | TOGO Medium | ATCC |
|---------|-----------|-------------|------|
| Media count | 3,327 | 2,917 | Thousands (unknown) |
| Public access | ✅ API/export | ✅ REST/SPARQL | ❌ Web only |
| Bulk download | ✅ Yes | ✅ Yes | ❌ No |
| Data format | JSON | JSON/RDF | HTML pages |
| Ingredients | ✅ Full | ✅ Full | ⚠️ Varies |
| Geographic focus | Europe | Japan | USA |
| Institution type | Public research | Public research | Commercial |
| Import status | ✅ 3,146 | ✅ 5 test | ⏳ Pending |

## Citations

If using ATCC media data, please cite:

> ATCC - American Type Culture Collection
> https://www.atcc.org/
> Accessed: 2026-01-21

**Note**: Check ATCC Terms of Use for any data usage restrictions.

## Notes

- ATCC is a **commercial organization**, data access is limited
- Most comprehensive approach is **cross-referencing with DSMZ media**
- Manual curation is viable for **project-specific media** (e.g., ATCC 1306 for methylotroph research)
- **Do not implement web scraping** without legal review and ATCC approval
- Consider **data sharing agreement** for long-term comprehensive coverage

## Update Workflow

To add new ATCC media:

```bash
# 1. Obtain PDF or structured data for specific medium
# (From ATCC website, research papers, or institutional access)

# 2. Extract to JSON format
# (Manual or using PDF parser)

# 3. Add to atcc_media_manual.json
nano data/raw/atcc/atcc_media_manual.json

# 4. Import to CultureMech
just import-atcc

# 5. Validate
just validate kb/media/bacterial/[medium_name].yaml

# 6. Document in this README
# Update "Known ATCC Media" table above
```

## Troubleshooting

### Cannot Find ATCC Medium Data

**Solutions**:
1. Search ATCC website: https://www.atcc.org/products?keywords=ATCC%20Medium%20[NUMBER]
2. Check if equivalent exists in MediaDive (cross-reference)
3. Request PDF from institution with ATCC access
4. Check research papers citing the medium

### Cross-Reference Verification

To verify if ATCC medium = DSMZ medium:

```bash
# 1. Get both formulations
# 2. Compare ingredient by ingredient
# 3. Check concentrations match
# 4. Document in atcc_crossref.json

# Example verification:
cat data/raw/mediadive/mediadive_media.json | jq '.data[] | select(.id == "632")'
# Compare with ATCC 1306 PDF
```

---

**Last Updated**: 2026-01-21
**Status**: Directory created, awaiting data collection
**Next Steps**:
1. Copy MicroMediaParam ATCC JSON files
2. Extract data from available PDFs
3. Create cross-reference database
4. Implement basic importer for manual data
