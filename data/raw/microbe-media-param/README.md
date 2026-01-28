# MicrobeMediaParam Raw Data

## Source Information

**Source**: MicrobeMediaParam Chemical Compound Mappings
**Original Location**: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MicrobeMediaParam/MicroMediaParam/pipeline_output/merge_mappings/`
**Date Obtained**: 2026-01-21
**Version**: MicrobeMediaParam pipeline output
**License**: Check MicrobeMediaParam repository for license
**Contact**: marcin

## Project Information

**Project**: MicrobeMediaParam
**Purpose**: Chemical compound mappings for microbial culture media ingredients
**Repository**: (add if available)
**Type**: TSV files with CHEBI mappings

## Files in this Directory

### compound_mappings_strict.tsv
- **Description**: Strict chemical compound mappings to CHEBI
- **Format**: TSV (tab-separated values)
- **Content**: Ingredient names mapped to CHEBI IDs with high confidence

**Schema**:
```tsv
ingredient_name\tchebi_id\tchebi_label\tformula\tmolecular_weight
```

**Example**:
```tsv
Glucose	17234	glucose	C6H12O6	180.16
Sodium Chloride	26710	sodium chloride	NaCl	58.44
```

### compound_mappings_strict_hydrate.tsv
- **Description**: Strict mappings including hydrated forms
- **Format**: TSV (tab-separated values)
- **Content**: Chemical compounds with hydration states (e.g., CaCl2·2H2O)

**Schema**:
```tsv
ingredient_name\tchebi_id\tchebi_label\tformula\thydration_state
```

**Example**:
```tsv
Calcium Chloride Dihydrate	86418	calcium chloride dihydrate	CaCl2·2H2O	dihydrate
```

## Data Statistics

- Total compound mappings: ~3,000 (estimated)
- With CHEBI IDs: High coverage (strict mapping criteria)
- Overlaps with MediaDive: ~40%
- Unique to MicrobeMediaParam: ~1,800 compounds

## Integration with CultureMech

The mappings are loaded by `src/culturemech/import/chemical_mappings.py`:

```python
from culturemech.import.chemical_mappings import ChemicalMappingLoader

loader = ChemicalMappingLoader(
    microbe_media_param_dir="raw/microbe-media-param",
    mediadive_dir="raw/mediadive"
)

# Unified lookup
mapping = loader.lookup("Glucose")
# Returns: {'chebi_id': 'CHEBI:17234', 'chebi_label': 'glucose', ...}
```

## Mapping Priority

When multiple sources have mappings for the same ingredient:
1. **HYDRATES** (compound_mappings_strict_final_hydrate.tsv) - HIGHEST PRIORITY
2. **STRICT** (compound_mappings_strict_final.tsv) - Base compounds
3. **MediaDive** (mediadive_ingredients.json) - Fallback

**Rationale**: Hydrated forms are more specific (e.g., CaCl2·2H2O vs CaCl2). When an
ingredient is listed with its hydration state, we should prefer the hydrated CHEBI ID
for maximum accuracy.

## How to Update

To fetch the latest mappings:

```bash
# Copy from MicrobeMediaParam repository
just fetch-microbe-media-param-raw

# Or manually:
cp /path/to/MicrobeMediaParam/pipeline_output/merge_mappings/*.tsv raw/microbe-media-param/
```

## Usage in Pipeline

1. **Load mappings**: `ChemicalMappingLoader` merges MediaDive + MicrobeMediaParam
2. **Lookup during import**: Ingredient names → CHEBI IDs
3. **Enrich recipes**: Add `term: {id: CHEBI:xxxxx}` to ingredients
4. **Validate**: OAK validates CHEBI IDs exist and labels match

## Data Quality

**Mapping Quality Levels**:
- `strict`: High confidence, manually curated (this dataset)
- `fuzzy`: Lower confidence, algorithmic matches (not included)

**Coverage Analysis**:
```bash
just chemical-mapping-stats
```

## Related Projects

- **MediaDive**: DSMZ culture media database mappings
- **MicrobeDB**: Microbial growth conditions database
- **CHEBI**: Chemical Entities of Biological Interest ontology

## Citations

If using MicrobeMediaParam data, please cite:

> (Add citation when available)

## Notes

- Mappings focus on common culture media ingredients
- Hydrate forms are treated separately (e.g., CaCl2 vs CaCl2·2H2O)
- Some ingredients may have multiple CHEBI IDs (isomers, forms)
- Priority is given to specific forms over general terms
- Files are expected at this location but may need to be copied/symlinked
