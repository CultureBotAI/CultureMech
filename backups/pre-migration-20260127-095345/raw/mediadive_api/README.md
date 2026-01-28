# MediaDive API Raw Data

## Source Information

**Source**: DSMZ MediaDive REST API
**URL**: https://mediadive.dsmz.de/rest
**API Documentation**: https://mediadive.dsmz.de/doc/
**Fetched By**: mediadive_api_fetcher.py
**License**: DSMZ data - check https://mediadive.dsmz.de for terms

## Database Information

**Database**: MediaDive (DSMZ - Leibniz Institute)
**Type**: REST API with JSON responses
**Key Endpoints**:
- `GET /media` - Bulk list (metadata only)
- `GET /medium/:id` - Individual medium with full composition
- `GET /solution/:id` - Solution recipe details
- `GET /ingredient/:id` - Ingredient chemical data

## Why This Approach?

**Previous Approach**: PDF parsing via MicroMediaParam
- Coverage: 54.7% (1,821/3,327 media)
- Method: Download PDFs, parse tables/text
- Issues: Parsing failures, complex layouts

**Current Approach**: REST API
- Coverage: ~100% (all 3,327 media)
- Method: Direct API calls to `/rest/medium/:id`
- Benefits: Structured JSON, normalized concentrations, no parsing errors

## Files in this Directory

### mediadive_api_media.json
- **Description**: 3,327 media with full compositions
- **Format**: JSON with `count` and `data` array
- **Size**: ~15-20 MB
- **Structure**:
  ```json
  {
    "count": 3327,
    "data": [
      {
        "medium": {
          "id": 1,
          "name": "NUTRIENT AGAR",
          "complex_medium": "yes",
          "min_pH": 7,
          "max_pH": 7,
          "source": "DSMZ",
          "link": "https://..."
        },
        "solutions": [
          {
            "id": 1,
            "name": "Main sol. 1",
            "volume": 1000,
            "recipe": [
              {
                "compound": "Peptone",
                "compound_id": 1,
                "amount": 5.0,
                "unit": "g",
                "g_l": 5.0,
                "optional": 0
              }
            ]
          }
        ]
      }
    ]
  }
  ```

### mediadive_api_solutions.json
- **Description**: 1,514 unique solutions with recipes
- **Format**: JSON with solution details

### mediadive_api_ingredients.json
- **Description**: Ingredient ID-to-name mapping
- **Format**: JSON with ingredient metadata
- **Note**: Full ingredient details (ChEBI, CAS, etc.) would require additional `/ingredient/:id` API calls

### fetch_stats.json
- **Description**: Fetch metadata and statistics
- **Format**: JSON with fetch date, counts, success rate

## Data Coverage

**Expected Coverage**: ~100% (3,327/3,327 media)
**Success Rate**: ~99%+ (some media may have API errors)

**Comparison**:
| Method | Coverage | Source |
|--------|----------|--------|
| PDF Parsing | 54.7% (1,821) | MicroMediaParam |
| REST API | ~100% (3,327) | This fetcher |

## How to Fetch Data

### Using the Fetcher Script

```bash
# Full fetch (all 3,327 media, ~13 minutes)
just fetch-mediadive-api

# Test with 10 media
just fetch-mediadive-api 10

# Custom delay (default: 0.25s)
uv run python -m culturemech.fetch.mediadive_api_fetcher \
    --output data/raw/mediadive_api \
    --delay 0.5
```

### Manual API Call

```bash
# Get single medium
curl "https://mediadive.dsmz.de/rest/medium/1" | jq '.'

# Get bulk list
curl "https://mediadive.dsmz.de/rest/media" | jq '.data[0]'
```

## API Rate Limiting

**Default Delay**: 0.25 seconds (4 requests/second)
**Total Time**: ~13 minutes for 3,327 media
**No API Key Required**: Public API

## Integration with CultureMech

### Import Workflow

1. **Fetch**: `just fetch-mediadive-api`
2. **Import**: `just import-mediadive` (auto-detects API data)
3. **Validate**: `just validate-all`

### Priority System

The importer checks data sources in this priority:
1. **API data** (data/raw/mediadive_api/) - Preferred
2. **PDF compositions** (data/raw/mediadive/compositions/) - Fallback

### Data Quality

**Strengths**:
- ✅ Structured JSON (no parsing errors)
- ✅ Normalized concentrations (`g_l` field)
- ✅ Complete solution hierarchies
- ✅ Preparation steps included
- ✅ ~100% coverage

**Limitations**:
- ⚠️ Ingredient details minimal (compound_id and name only)
- ⚠️ Full chemical data (ChEBI, CAS) requires additional API calls
- ⚠️ Network-dependent (requires internet)

### ChEBI Mapping

Ingredient names are mapped to ChEBI IDs using:
1. CultureMech's ChemicalMapper (from MicroMediaParam)
2. Existing MediaDive ingredient lookup table

## Update Workflow

```bash
# Refresh data
rm -rf data/raw/mediadive_api/
just fetch-mediadive-api

# Re-import
just import-mediadive

# Validate
just validate-all
```

## Troubleshooting

### API Timeout
**Issue**: Requests timing out
**Solution**: Increase `--delay` or check network

### Rate Limiting
**Issue**: Too many requests error
**Solution**: Increase `--delay` to 0.5 or 1.0 seconds

### Partial Data
**Issue**: Some media missing
**Solution**: Check `fetch_stats.json` for success rate, retry failed IDs

### Import Errors
**Issue**: Importer fails on API data
**Solution**: Check ingredient name matching, update ChemicalMapper

## Citations

> DSMZ MediaDive - Culture Media Database
> Leibniz Institute DSMZ - German Collection of Microorganisms and Cell Cultures
> https://mediadive.dsmz.de

## Contact

For API issues: https://mediadive.dsmz.de
For fetcher issues: CultureMech GitHub Issues
