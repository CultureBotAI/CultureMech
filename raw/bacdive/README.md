# BacDive Raw Data

## Source Information

- **Official Name**: BacDive - Bacterial Diversity Metadatabase
- **URL**: https://bacdive.dsmz.de
- **API Documentation**: https://bacdive.dsmz.de/api/bacdive/
- **Python Client**: https://github.com/DSMZ-de/bacdive
- **License**: CC BY 4.0
- **Record Count**:
  - 100,000+ bacterial and archaeal strains
  - 66,570+ cultivation datasets
  - ~500-1,000 unique media references

## What is BacDive?

BacDive is the world's largest database for standardized bacterial strain information. It provides:
- Taxonomic classification
- Morphology and physiology
- **Culture and growth conditions** (our primary interest)
- Geographic origin
- Application information

## Integration Strategy

### Primary Value: Organism→Media Associations

BacDive's main contribution to CultureMech is enriching existing recipes with organism growth data:
- **66,000+ organism-media links** to add to existing MediaDive/TOGO recipes
- Growth conditions (temperature, pH, incubation time)
- Strain-specific cultivation preferences

### Secondary Value: New Media Recipes

BacDive references many media:
- **~70% are DSMZ media** (overlap with MediaDive)
- **~30% are unique or lab-specific** (~500 new recipes)
- Media are referenced by name, not full recipe

**Note**: BacDive provides media *references*, not complete formulations. Full recipes must be obtained from DSMZ or other sources.

## Data Files

After fetching, this directory will contain:

- `bacdive_strain_ids.json` - All strain IDs from BacDive (~100,000 records)
- `bacdive_cultivation.json` - Strains with cultivation data (~66,570 records)
- `bacdive_media_refs.json` - Unique media extracted from cultivation data
- `fetch_stats.json` - Fetch metadata (date, counts, etc.)

## API Access Requirements

**Registration Required** (Free):
1. Visit https://bacdive.dsmz.de/
2. Create free account
3. Obtain API credentials (email + password)

**Rate Limits**:
- Reasonable usage (~10 requests/second)
- No hard limits for registered users
- Be respectful of server resources

## Fetch Commands

### Install BacDive Python Client

```bash
# Using uv
uv pip install bacdive

# Or with pip
pip install bacdive
```

### Set Credentials

Option 1: Environment variables (recommended)
```bash
export BACDIVE_EMAIL="your.email@example.com"
export BACDIVE_PASSWORD="your_password"
```

Option 2: Command-line arguments
```bash
just fetch-bacdive-raw --email your.email@example.com --password your_password
```

### Fetch Data

```bash
# Test with 10 strains
just fetch-bacdive-raw 10

# Full fetch (may take hours!)
just fetch-bacdive-raw
```

**Warning**: Fetching all 100,000+ strains may take several hours. Start with a small limit for testing.

## Data Structure

### Strain Cultivation Data

```json
{
  "BacDive-ID": 12345,
  "Name and taxonomic classification": {
    "species": "Escherichia coli",
    "strain designation": "DSM 30083"
  },
  "culture and growth conditions": [
    {
      "medium": "DSMZ Medium 1 (Nutrient Agar)",
      "temp": "37°C",
      "pH": "7.0",
      "time": "24-48 h",
      "oxygen": "aerobic"
    }
  ]
}
```

### Media References

```json
{
  "DSMZ_1": {
    "media_id": "DSMZ_1",
    "media_name": "DSMZ Medium 1 (Nutrient Agar)",
    "growth_temperature": "37°C",
    "growth_ph": "7.0",
    "growth_time": "24-48 h"
  }
}
```

## Integration with CultureMech

### Import Pipeline

1. **Fetch**: Download cultivation data via API
   ```bash
   just fetch-bacdive-raw
   ```

2. **Import New Media**: Create recipes for non-DSMZ media
   ```bash
   just import-bacdive
   ```

3. **Export Associations**: Generate organism→media links
   ```bash
   uv run python -m culturemech.import.bacdive_importer \
       --export-associations
   ```

4. **Enrich Existing Recipes**: Backfill organism data to MediaDive recipes
   ```bash
   just bacdive-enrich-existing  # Future feature
   ```

### Cross-Referencing with MediaDive

Many BacDive media reference DSMZ media:
- "DSMZ Medium 1" → Already in MediaDive as `MEDIADIVE_1`
- "DSM 53" → Already in MediaDive as `MEDIADIVE_53`

**Strategy**:
1. Parse DSMZ media numbers from BacDive references
2. Link to existing MediaDive recipes
3. Add organism growth data to existing recipes
4. Only import media NOT in MediaDive

## Provenance

**Fetch Date**: Run `cat fetch_stats.json` after fetching
**Fetcher Script**: `src/culturemech/fetch/bacdive_fetcher.py`
**Importer Script**: `src/culturemech/import/bacdive_importer.py`

## Known Limitations

1. **Media References Only**: BacDive doesn't provide full media recipes, only names
2. **Heterogeneous Naming**: Media names vary (e.g., "DSMZ 1", "DSM Medium 1", "Medium 1")
3. **Missing Data**: Not all strains have cultivation conditions
4. **Growth Conditions**: Format varies (free text vs. structured)

## Quality Metrics

Target after integration:
- **New media recipes**: ~500 unique (non-DSMZ)
- **Organism associations**: ~66,000 links to existing recipes
- **Coverage improvement**: +200 bacterial species
- **Growth conditions**: Temperature, pH, time for most recipes

## References

- **BacDive Publication**: Reimer et al. (2019). "BacDive in 2019: bacterial phenotypic data for High-throughput biodiversity analysis." Nucleic Acids Research. https://doi.org/10.1093/nar/gky879
- **API Documentation**: https://bacdive.dsmz.de/api/bacdive/
- **Python Client**: https://github.com/DSMZ-de/bacdive
- **Terms of Service**: https://bacdive.dsmz.de/terms

## Contact

For questions about BacDive data:
- **Support**: contact@dsmz.de
- **API Issues**: Open issue at https://github.com/DSMZ-de/bacdive

---

**Last Updated**: 2025-01-24
**Status**: NOT_STARTED (awaiting fetch)
