# MediaDive Raw Data

## Source Information

**Source**: DSMZ MediaDive MongoDB Export via cmm-ai-automation
**Original Location**: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/cmm-ai-automation/data/`
**Date Obtained**: 2026-01-21
**Version**: cmm-ai-automation repository snapshot
**License**: DSMZ data - check https://mediadive.dsmz.de for terms
**Contact**: marcin

## Database Information

**Database**: MediaDive (DSMZ - Leibniz Institute)
**URL**: https://mediadive.dsmz.de
**Type**: MongoDB export to JSON
**API**: https://mediadive.dsmz.de/rest

## Files in this Directory

### mediadive_media.json
- **Description**: 3,327 microbial growth media recipes with metadata
- **Format**: JSON array of media objects
- **Size**: ~500 KB
- **Content**: Medium name, pH, type (complex/defined), source database, documentation link

**Schema**:
```json
{
  "id": "number",
  "name": "string",
  "source": "string (DSMZ/JCM/etc)",
  "link": "string (PDF URL)",
  "min_pH": "number or null",
  "max_pH": "number or null",
  "complex_medium": "boolean"
}
```

### mediadive_ingredients.json
- **Description**: Chemical ingredient mappings with CHEBI IDs
- **Format**: JSON object mapping ingredient names to metadata
- **Size**: ~200 KB
- **Content**: Ingredient names, CHEBI IDs, synonyms, formula

**Schema**:
```json
{
  "ingredient_name": {
    "chebi_id": "number",
    "chebi_label": "string",
    "formula": "string",
    "synonyms": ["array of strings"]
  }
}
```

## MongoDB Collections (Source)

The JSON files were exported from these MongoDB collections:

- `db.media_details`: Full recipe details with composition
- `db.ingredient_details`: Ingredient synonyms and CHEBI mappings
- `db.solution_details`: Stock solution compositions
- `db.strains`: Organism-medium relationships

## How to Update

To fetch the latest data:

```bash
# Option 1: Copy from cmm-ai-automation (if available)
just fetch-mediadive-raw

# Option 2: Export from MongoDB (if you have access)
# mongoexport --db=mediadive --collection=media_details --out=mediadive_media.json

# Option 3: Use MediaDive REST API (for specific records)
# curl https://mediadive.dsmz.de/rest/medium/:id
```

## Data Statistics

- Total media records: 3,327
- Successfully imported to CultureMech: 3,146 (94.6%)
- With CHEBI mappings: 686 ingredients (~56%)
- Categories:
  - Bacterial: 2,877
  - Fungal: 114
  - Specialized: 96
  - Archaea: 59

## Related Data Sources

- **kg-microbe MediaDive transform**: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/kg_microbe/transform_utils/mediadive/`
- **MicrobeMediaParam**: Additional chemical mappings at `../microbe-media-param/`

## Citations

If using MediaDive data, please cite:

> DSMZ MediaDive - Culture Media Database
> Leibniz Institute DSMZ - German Collection of Microorganisms and Cell Cultures
> https://mediadive.dsmz.de

## Notes

- Data represents a snapshot from 2026-01-21
- Some recipes may have been updated in the live database since export
- 181 recipes (5.4%) failed import due to name collisions or character encoding
- Full composition data requires additional API calls (not included in basic export)
