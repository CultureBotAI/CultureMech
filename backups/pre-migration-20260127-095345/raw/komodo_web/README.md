# KOMODO Web Table Raw Data

## Source Information

**Source**: KOMODO ModelSEED Web Interface
**URL**: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
**Date Fetched**: 2026-01-27T01:12:18Z
**Fetched By**: komodo_web_fetcher.py
**License**: ModelSEED - check source for terms

## Database Information

**Database**: KOMODO (Knowledge base Of Microbial and Mammalian cells Defined and Optimized media)
**Type**: Web table scraping
**Purpose**: Media metadata extraction with DSMZ recipe mappings

## Data Coverage

**Total Records**: 3637
**DSMZ Mappings**: 3637 (100.0%)
**Medium Types**:
- Complex: 2570
- Defined: 1067

**Aerobic Classification**:
- Aerobic: 721
- Anaerobic: 2916

**Submedia**: 300

## Files in this Directory

### komodo_web_media.json
- **Description**: All KOMODO media records with metadata
- **Format**: JSON with `count` and `data` array
- **Structure**:
  ```json
  {
    "count": 3637,
    "data": [
      {
        "id": "1",
        "name": "NUTRIENT AGAR",
        "ph_info": "7.0",
        "ph_value": "7.0",
        "ph_range": null,
        "ph_buffer": null,
        "is_complex": true,
        "is_aerobic": false,
        "is_submedium": false,
        "dsmz_medium_number": "1"
      }
    ]
  }
  ```

### komodo_dsmz_mappings.json
- **Description**: KOMODO ID to DSMZ medium number mappings
- **Format**: JSON with mappings array
- **Purpose**: Enable merging KOMODO metadata with DSMZ recipes
- **Count**: 3637 mappings

### fetch_stats.json
- **Description**: Fetch metadata and statistics
- **Format**: JSON with coverage metrics

## KOMODO ID Formats

KOMODO uses various ID formats:
- Simple numbers: `1`, `10`, `1000`
- Decimal variants: `1004.1`, `1004.2`, `1004.3`
- Underscore variants: `1008_19205`, `104_15597`
- Letter suffixes: `1011a`, `104a`, `104b`

## DSMZ Mapping Strategy

The `dsmz_medium_number` field links KOMODO media to DSMZ recipes:
- Extracted from Instructions column (DSMZ PDF links)
- Format: DSMZ_Medium[NUMBER].pdf
- Used for future merge with MediaDive/DSMZ composition data
- Coverage: 100.0% of KOMODO media

## How to Fetch Data

```bash
# Fetch KOMODO web table
just fetch-komodo-web

# Or use script directly
uv run python -m culturemech.fetch.komodo_web_fetcher \
    --output data/raw/komodo_web
```

## Integration Workflow

1. **Fetch KOMODO metadata** (this fetcher)
   - Extracts KOMODO IDs, names, pH, types
   - Extracts DSMZ recipe mappings

2. **Import KOMODO to YAML** (komodo_web_importer.py)
   - Creates YAML files with KOMODO metadata
   - Uses KOMODO IDs as primary identifiers

3. **Merge with DSMZ data** (future step)
   - Match KOMODO records to DSMZ recipes using `dsmz_medium_number`
   - Enrich KOMODO metadata with DSMZ compositions
   - Create cross-references between databases

## Data Quality Notes

**Strengths**:
- ✅ Complete KOMODO metadata
- ✅ High DSMZ mapping coverage (100.0%)
- ✅ Medium type classification
- ✅ pH information (where available)

**Limitations**:
- ⚠️ No composition data (will be merged from DSMZ later)
- ⚠️ Some records have generic names (e.g., "For DSM 16554")
- ⚠️ pH info format varies (single values, ranges, buffers)

## Citations

> KOMODO - Knowledge base Of Microbial and Mammalian cells Defined and Optimized media
> ModelSEED Project
> https://komodo.modelseed.org
