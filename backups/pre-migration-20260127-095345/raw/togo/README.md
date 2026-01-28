# TOGO Medium Raw Data

## Source Information

**Source**: TogoMedium - Database of Microbial Culture Media
**URL**: https://togomedium.org/
**REST API**: https://togomedium.org/sparqlist/api/
**SPARQL Endpoint**: https://togomedium.org/sparql
**Date Obtained**: 2026-01-21
**Version**: Live API data (no versioning available)
**License**: Check https://togomedium.org/about/ for terms
**Contact**: marcin
**Maintainer**: DBCLS (Database Center for Life Science), Japan

## Database Information

**Organization**: DBCLS (Database Center for Life Science)
**Country**: Japan
**Type**: REST API + SPARQL endpoint (RDF triplestore)
**Data Model**: Growth Medium Ontology (GMO)
**Ontology**: http://purl.jp/bio/10/gmo/

## Data Statistics

| Class | Count | Description |
|-------|------:|-------------|
| **Media** | **2,917** | Culture media recipes |
| Components | 50,202 | Ingredient definitions |
| Ingredient Usage | 31,541 | Ingredient-in-medium links |
| Organisms | 81,130 | Organism/strain instances |
| NCBI Taxon | 223,586 | Taxonomy entries |
| Comments | 9,607 | Recipe notes |

### Media Sources

TogoMedium aggregates from multiple biological resource centers:

| Source | Count | Description |
|--------|------:|-------------|
| **JCM** | 1,376 | RIKEN BioResource Center |
| **NBRC** | 749 | NITE Biological Resource Center |
| **Manual** | 709 | Research papers |
| **Other** | 83 | Various sources |
| **Total** | **2,917** | |

## Files in this Directory

### togo_media.json
- **Description**: 2,917 media recipes with metadata
- **Format**: JSON array of media objects
- **Size**: ~2-5 MB (estimated)
- **Content**: Medium ID, name, source (JCM/NBRC), ingredients, organisms

**Schema**:
```json
{
  "gm_id": "M443",
  "name": "LB (Luria-Bertani) Medium",
  "source": "JCM",
  "original_id": "M1",
  "ph": 7.0,
  "ingredients": [
    {
      "component_id": "GMO_001234",
      "name": "Tryptone",
      "amount": "10 g",
      "unit": "g/L"
    }
  ],
  "organisms": [
    {
      "taxon_id": "NCBITaxon:562",
      "name": "Escherichia coli"
    }
  ],
  "cross_references": {
    "mediadive": "https://mediadive.dsmz.de/ingredient/...",
    "chebi": "CHEBI:xxxxx"
  }
}
```

### togo_components.json
- **Description**: 50,202 ingredient/component definitions
- **Format**: JSON array of component objects
- **Size**: ~10-20 MB (estimated)
- **Content**: Component IDs, names, ChEBI/PubChem cross-refs

**Schema**:
```json
{
  "gmo_id": "GMO_001234",
  "name": "Tryptone",
  "synonyms": ["Bacto Tryptone", "Peptone from casein"],
  "chebi_id": "CHEBI:xxxxx",
  "pubchem_cid": "xxxxx",
  "role": "nitrogen source",
  "property": "organic"
}
```

## API Endpoints

### REST API (SPARQList)

Base URL: `https://togomedium.org/sparqlist/api/`

**Key Endpoints**:

1. **List All Media** (paginated)
   ```bash
   curl "https://togomedium.org/sparqlist/api/list_media?limit=100&offset=0"
   ```
   Returns: Array of media with IDs and names

2. **Get Medium Details by ID**
   ```bash
   curl "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M443"
   ```
   Returns: Complete medium details with ingredients

3. **List All Components**
   ```bash
   curl "https://togomedium.org/sparqlist/api/list_components"
   ```
   Returns: Array of all ingredient components

4. **Get Component Details**
   ```bash
   curl "https://togomedium.org/sparqlist/api/gmdb_component_by_gmoid?gmo_id=GMO_001234"
   ```
   Returns: Component details with cross-references

5. **List Organisms**
   ```bash
   curl "https://togomedium.org/sparqlist/api/list_organisms"
   ```
   Returns: Array of organisms cultivated in media

### Rate Limiting

- No documented rate limits
- Recommended: 0.5s delay between requests (2 requests/second)
- For bulk downloads, use paginated endpoints
- Cache responses to avoid repeated calls

## How to Fetch Data

### Using the Fetcher Script

```bash
# Fetch all media and components
just fetch-togo-raw

# Or manually
cd /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech
uv run python -m culturemech.fetch.togo_fetcher \
    --output data/raw/togo \
    --media \
    --components
```

### Manual Download (for testing)

```bash
# Get first 100 media
curl "https://togomedium.org/sparqlist/api/list_media?limit=100&offset=0" \
    > data/raw/togo/togo_media_sample.json

# Get specific medium
curl "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M443" \
    > data/raw/togo/M443_LB_medium.json
```

## Data Quality Notes

### Strengths
- Comprehensive ingredient lists (50K components)
- Organism associations (81K organisms)
- Cross-references to ChEBI, PubChem, NCBI Taxonomy
- Ontology-based (GMO)
- Active maintenance by DBCLS

### Limitations
- No bulk data dumps (API-only access)
- No versioning (live data changes)
- Smaller media count than MediaDive (2,917 vs 3,327)
- Some media lack complete composition
- JCM/NBRC-focused (Japan BRCs)

### Unique Media in TOGO
- LB Medium (not in MediaDive)
- Complete NMS medium (MediaDive only has stock)
- Standard JCM/NBRC media with organism associations

## Comparison with MediaDive

| Feature | MediaDive | TOGO Medium |
|---------|-----------|-------------|
| Media count | 3,327 | 2,917 |
| Ingredient count | 1,234 | 50,202 |
| Strain associations | 47,264 | 81,130 organisms |
| Has LB medium | No | Yes (M443, M2476) |
| Has NMS medium | Stock only | Complete (M1871) |
| API type | MongoDB export | REST + SPARQL |
| Data format | JSON | RDF/JSON-LD |
| Geographic focus | Europe (DSMZ) | Japan (JCM/NBRC) |

## Integration with CultureMech

### Import Strategy

1. **Fetch raw data** (this directory)
   - API calls to get all media (paginated)
   - API calls to get component details
   - Store as JSON in `data/raw/togo/`

2. **Process to intermediate** (`data/processed/`)
   - Enrich with ChEBI IDs
   - Map to CultureMech schema
   - Merge overlaps with MediaDive

3. **Import to KB** (`kb/media/`)
   - Convert to LinkML YAML
   - Validate against schema
   - Categorize by organism type

### ID Mapping

**TOGO Medium IDs** use format: `M####`
- Example: `M443` = LB Medium
- Map to: `media_term.term.id: "TOGO:M443"`

**Cross-references**:
- MediaDive: Via ingredient URL matching
- ChEBI: Direct component mappings
- NCBITaxon: Direct organism links
- PubChem: Component CID mappings

## Growth Medium Ontology (GMO)

**Ontology IRI**: http://purl.jp/bio/10/gmo/
**BioPortal**: https://bioportal.bioontology.org/ontologies/GMO
**Version**: 0.24 Beta (2024-08-28)

### Key Classes

| Class ID | Label | Description |
|----------|-------|-------------|
| GMO_000001 | Medium | Culture medium |
| GMO_000002 | Component | Media ingredient |
| GMO_000003 | Defined medium | Chemically defined |
| GMO_000004 | Undefined medium | Complex medium |

### Key Properties

- `gmo:has_component` - Links medium to ingredients
- `gmo:has_role` - Ingredient role (carbon source, etc.)
- `gmo:has_property` - Ingredient properties
- `gmo:gmo_id` - GMO identifier

## Citations

If using TogoMedium data, please cite:

> TogoMedium: A Database of Microbial Culture Media
> Database Center for Life Science (DBCLS)
> https://togomedium.org/
> Accessed: 2026-01-21

## Notes

- Data represents live API snapshot from 2026-01-21
- No version control available (API returns current data)
- Some media may be updated/removed in live database
- Full ingredient lists require per-medium API calls (2,917 calls)
- Fetcher script implements caching and rate limiting
- Update frequency: Run fetcher periodically to sync with upstream

## Update Workflow

To update with latest TOGO data:

```bash
# 1. Fetch latest data from API
just fetch-togo-raw

# 2. Check statistics
just show-raw-data-stats

# 3. Re-import
just import-togo

# 4. Validate
just validate-all

# 5. Review changes
git diff kb/media/

# 6. Commit
git add kb/media/ data/raw/togo/README.md
git commit -m "Update TOGO Medium recipes from API"
```

## Troubleshooting

### API Connection Issues
```bash
# Test API connectivity
curl -I "https://togomedium.org/sparqlist/api/list_media?limit=1"

# Expected: HTTP 200 OK
```

### Rate Limiting
If you encounter errors, increase delay in fetcher:
```python
# In togo_fetcher.py
time.sleep(0.5)  # Increase to 1.0 or 2.0
```

### Incomplete Data
Some media may lack complete composition. Check:
```bash
# Count media with ingredients
jq '[.[] | select(.ingredients | length > 0)] | length' data/raw/togo/togo_media.json
```

---

**Last Updated**: 2026-01-21
**Status**: Directory created, awaiting data fetch
**Next Steps**: Run `just fetch-togo-raw` to download media data
