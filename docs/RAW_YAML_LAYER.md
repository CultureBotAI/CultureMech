# Raw YAML Layer (Layer 2)

## Purpose

The `raw_yaml/` directory contains YAML representations of raw source data with **NO normalization or validation** applied. This is an intermediate layer that makes raw data human-readable while preserving its original structure.

## What Goes Here

✅ **Direct 1:1 YAML conversions** of JSON/TSV/SQL source files
✅ **Original field names** preserved exactly (e.g., "medium_name", not "name")
✅ **Original value formats** preserved (e.g., "55.5 mM" as string, not parsed)
✅ **Original structure** maintained (nested objects, arrays as-is)
✅ **Source metadata** added (`_source` field with file path and timestamp)

## What Does NOT Go Here

❌ **Normalized values** (those go in `normalized_yaml/`)
❌ **Validated recipes** (those go in `normalized_yaml/`)
❌ **LinkML schema compliance** (enforced in `normalized_yaml/`)
❌ **Ontology term resolution** (CHEBI/NCBITaxon lookups in `normalized_yaml/`)
❌ **Enriched data** with added fields (enrichment in `normalized_yaml/`)

## Why This Layer Exists

1. **Human-readable inspection** - View raw data in YAML instead of JSON
2. **Debugging imports** - Compare unnormalized vs normalized data
3. **Data archaeology** - Understand original source structure
4. **Baseline for comparison** - See what changed during normalization
5. **Regenerable intermediate** - Can always recreate from Layer 1

## Directory Structure

```
raw_yaml/
  mediadive/
    673e1234abcd5678.yaml         # One file per MediaDive record
    673e5678efab9012.yaml         # Uses MongoDB ObjectId as filename
    ...
  togo/
    TM001.yaml                     # One file per TOGO medium
    TM002.yaml                     # Uses media ID from source
    ...
  atcc/
    ATCC_Medium_001.yaml
    ATCC_Medium_002.yaml
    ...
  bacdive/
    BacDive_123.yaml
    ...
  nbrc/
    NBRC_001.yaml
    ...
  komodo/
    KOMODO_001.yaml
    ...
  komodo_web/
    KOMODO_Web_001.yaml
    ...
  mediadb/
    MediaDB_001.yaml
    ...
```

## Example: MediaDive Raw YAML

`raw_yaml/mediadive/673e1234abcd5678.yaml`:

```yaml
# Unnormalized - preserves MediaDive's original structure
_id:
  $oid: 673e1234abcd5678
medium_name: LB Medium (Lysogeny Broth)
organism: Escherichia coli
description: General-purpose rich medium for bacterial culture
growth_type: General
dsmz_number: M001
composition:
  - ingredient_name: Tryptone
    amount: 10 g/L
    chebi_id: CHEBI:16199
  - ingredient_name: Yeast Extract
    amount: 5 g/L
    chebi_id: CHEBI:83937
  - ingredient_name: NaCl
    amount: 5 g/L
    chebi_id: CHEBI:26710
ph_value: "7.0"
sterilization: "Autoclave at 121°C for 15 minutes"
_source:
  file: /path/to/raw/mediadive/mediadive_media.json
  timestamp: '2026-01-27T10:30:00'
  layer: raw_yaml
```

**Note**: Field names are MediaDive-specific, values are strings, structure mirrors the original JSON.

## Example: TOGO Raw YAML

`raw_yaml/togo/TM001.yaml`:

```yaml
# Unnormalized - preserves TOGO's original structure
media_id: TM001
medium_name: LB Medium (Lennox)
category: General purpose
organism: Escherichia coli
description: Commonly used medium for cultivation of E. coli
composition:
  - compound: Tryptone
    amount: 10 g/L
    cas_number: 91079-40-2
  - compound: Yeast Extract
    amount: 5 g/L
    cas_number: 8013-01-2
  - compound: Sodium Chloride
    amount: 5 g/L
    cas_number: 7647-14-5
ph: "7.0"
preparation: |
  1. Dissolve components in distilled water
  2. Adjust pH to 7.0
  3. Autoclave at 121°C for 15 minutes
references:
  - PMID:12345678
  - doi:10.1234/example
_source:
  file: /path/to/raw/togo/togo_media.json
  timestamp: '2026-01-27T10:31:00'
  layer: raw_yaml
```

**Note**: Field names differ from MediaDive, CAS numbers instead of CHEBI IDs, multi-line preparation text.

## How to Generate

### Convert All Sources

```bash
# Convert all raw sources to raw_yaml
just convert-to-raw-yaml all
```

This runs converters for:
- MediaDive
- TOGO
- ATCC
- BacDive
- NBRC
- KOMODO
- KOMODO web
- MediaDB

### Convert Specific Sources

```bash
# Convert individual sources
just convert-to-raw-yaml mediadive
just convert-to-raw-yaml togo
just convert-to-raw-yaml atcc

# Or use source-specific commands
just convert-mediadive-raw-yaml
just convert-togo-raw-yaml
just convert-atcc-raw-yaml
```

### Converter Options

Most converters support:
- `-i, --input` - Input directory (default: `raw/<source>/`)
- `-o, --output` - Output directory (default: `raw_yaml/<source>/`)
- `-v, --verbose` - Enable verbose logging

Example:
```bash
uv run python -m culturemech.convert.mediadive_raw_yaml \
    -i raw/mediadive \
    -o raw_yaml/mediadive \
    -v
```

## Conversion Process

Converters perform these steps:

1. **Read raw files** - Load JSON/TSV from `raw/<source>/`
2. **Parse records** - Extract individual records from file
3. **Add metadata** - Append `_source` tracking information
4. **Generate filename** - Use ID from record or sequence number
5. **Write YAML** - Save to `raw_yaml/<source>/<filename>.yaml`

**No transformations applied** - This is purely format conversion.

## Comparison: Raw YAML vs Normalized YAML

### Raw YAML (Layer 2)

```yaml
# Unnormalized
medium_name: LB Medium (Lysogeny Broth)
organism: Escherichia coli
composition:
  - ingredient_name: Tryptone
    amount: 10 g/L
    chebi_id: CHEBI:16199
ph_value: "7.0"
```

### Normalized YAML (Layer 3)

```yaml
# Normalized, validated, curated
id: CULTUREMECH:000001
name: LB Broth (Lysogeny Broth)
organisms:
  - NCBITaxon:562  # Escherichia coli
components:
  - agent: CHEBI:16199  # tryptone
    concentration:
      value: 10.0
      unit: g/L
ph:
  value: 7.0
```

**Differences**:
- Field names standardized to LinkML schema
- Organism text → NCBITaxon CURIE
- Amount string → structured concentration object
- pH string → numeric value
- Added CultureMech ID
- Removed source-specific fields

## Use Cases

### 1. Inspecting Raw Data

```bash
# View raw data in YAML format
cat raw_yaml/mediadive/673e1234abcd5678.yaml

# Compare multiple sources
diff raw_yaml/togo/TM001.yaml raw_yaml/mediadive/673e1234abcd5678.yaml
```

### 2. Debugging Imports

When an importer fails:

```bash
# 1. Check raw_yaml to see what the source data looks like
cat raw_yaml/togo/TM001.yaml

# 2. Compare with normalized output
cat normalized_yaml/bacterial/LB_Broth.yaml

# 3. Identify mapping issues
```

### 3. Data Quality Analysis

```bash
# Count records by source
find raw_yaml/ -name "*.yaml" | wc -l

# Check for missing fields
grep -r "chebi_id" raw_yaml/mediadive/ | wc -l

# Find records with specific properties
grep -r "ph_value: \"7.0\"" raw_yaml/
```

### 4. Custom Processing

```python
# Read raw_yaml for custom analysis
import yaml
from pathlib import Path

for file in Path("raw_yaml/mediadive").glob("*.yaml"):
    with open(file) as f:
        data = yaml.safe_load(f)
        # Process unnormalized data
        print(f"{data['medium_name']}: {len(data['composition'])} ingredients")
```

## Maintenance

### Regenerating Raw YAML

If raw data is updated, regenerate raw_yaml:

```bash
# 1. Re-fetch raw data (if needed)
just fetch-mediadive-raw

# 2. Regenerate raw_yaml
just convert-to-raw-yaml mediadive

# 3. Verify output
ls -la raw_yaml/mediadive/
```

### Cleaning Raw YAML

Raw YAML is regenerable, so it can be safely deleted:

```bash
# Remove all raw_yaml
rm -rf raw_yaml/*/

# Regenerate from raw/
just convert-to-raw-yaml all
```

### Version Control

Raw YAML is **NOT version controlled** (excluded by `.gitignore`):

```gitignore
# .gitignore
raw_yaml/**/*.yaml
raw_yaml/**/.DS_Store
```

Reason: Regenerable from Layer 1, would bloat repository size.

## See Also

- **DATA_LAYERS.md** - Complete three-tier architecture
- **MIGRATION_GUIDE.md** - Migrating to new directory structure
- **src/culturemech/convert/** - Converter implementations
- **project.justfile** - Conversion commands
