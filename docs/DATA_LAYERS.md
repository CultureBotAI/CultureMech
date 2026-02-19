# CultureMech Data Layers

## Overview

CultureMech uses a **four-tier data architecture** for reproducibility, provenance, and clear data flow:

```
raw/                # Layer 1: Original source data (immutable)
raw_yaml/           # Layer 2: Unnormalized YAML (mechanical conversion)
normalized_yaml/    # Layer 3: LinkML-validated, curated recipes
merge_yaml/         # Layer 4: Deduplicated recipes (canonical records)
```

This structure provides:
- **Clear separation** between raw, intermediate, and validated data
- **Reproducibility** - each layer can be regenerated from the previous
- **Provenance** - track data from source to knowledge base
- **Quality gates** - validation enforced at layer boundaries

---

## Layer 1: Raw Data (`raw/`)

**Purpose**: Store original source data exactly as obtained, without modifications.

**Characteristics**:
- Immutable - never edited after initial download/copy
- Preserves original format (JSON, TSV, HTML, SQL, etc.)
- Includes metadata about source, date, version
- Large files excluded from git (see `.gitignore`)

### Structure

```
raw/
  mediadive/
    mediadive_media.json           # DSMZ MediaDive metadata (3,327 recipes)
    mediadive_ingredients.json     # MediaDive ingredient mappings
    README.md                      # Source provenance
  mediadive_api/
    mediadive_api_media.json       # API-fetched compositions
    README.md
  togo/
    togo_media.json                # TOGO Medium database (~2,917 media)
    README.md
  atcc/
    atcc_media.json                # ATCC media database
    README.md
  bacdive/
    bacdive_media.json             # BacDive culture media
    README.md
  nbrc/
    nbrc_media.json                # NBRC media database
    README.md
  komodo/
    komodo_media.json              # KOMODO media database
    README.md
  komodo_web/
    komodo_web_media.json          # KOMODO web scrape
    README.md
  mediadb/
    mediadb.json                   # MediaDB SQL exports
    README.md
  microbe-media-param/
    compound_mappings_strict.tsv   # CHEBI mappings
    README.md
```

### Fetching Raw Data

Use `just` commands to fetch raw data:

```bash
# Fetch all core sources
just fetch-raw-data

# Fetch individual sources
just fetch-mediadive-raw
just fetch-togo-raw 50         # Limit to 50 for testing
just fetch-mediadive-api
just fetch-komodo-web
just fetch-mediadb
```

### Provenance Documentation

Each `raw/*/README.md` documents:
- **Source**: URL, database, API endpoint
- **Date obtained**: When data was downloaded
- **Version**: Database version, API version, or git commit
- **License**: Data license (e.g., CC0, CC-BY)
- **Contact**: Who obtained the data
- **Command**: Exact command used to fetch data

**Example**: `raw/togo/README.md`
```markdown
# TOGO Medium Raw Data

**Source**: TOGO Medium REST API
**URL**: https://togodb.org/db/togo_medium/api
**Date Obtained**: 2026-01-23
**Records**: ~2,917 media
**License**: Public domain
**Command**: `just fetch-togo-raw`
```

---

## Layer 2: Raw YAML (`raw_yaml/`)

**Purpose**: Mechanical conversion of raw data to YAML format **without any normalization**.

**Characteristics**:
- **Direct 1:1 conversion** from JSON/TSV/etc to YAML
- **Preserves original field names** exactly (e.g., "medium_name", not "name")
- **Preserves original values** (e.g., "55.5 mM NaCl" as string, not parsed)
- **No LinkML validation** - structure may not match schema
- **No ontology resolution** - no CHEBI/NCBITaxon lookups
- **Regenerable** from Layer 1 via converters

This layer serves as:
- **Human-readable version** of raw data for inspection
- **Intermediate format** for debugging import issues
- **Unnormalized baseline** to compare against normalized output

### Structure

```
raw_yaml/
  mediadive/
    673e1234abcd5678.yaml         # One file per MediaDive record
    673e5678efab9012.yaml
    ...
  togo/
    TM001.yaml                     # One file per TOGO medium
    TM002.yaml
    ...
  atcc/
    ATCC_Medium_001.yaml
    ...
  (similar structure for other sources)
```

### Generating Raw YAML

Convert raw data to raw YAML using converters:

```bash
# Convert all sources
just convert-to-raw-yaml all

# Convert specific sources
just convert-to-raw-yaml mediadive
just convert-to-raw-yaml togo
just convert-to-raw-yaml atcc

# Or use individual commands
just convert-mediadive-raw-yaml
just convert-togo-raw-yaml
```

### Example Raw YAML File

`raw_yaml/togo/TM001.yaml`:
```yaml
# Unnormalized - preserves original field names
media_id: TM001
medium_name: LB Medium (Lennox)
organism: Escherichia coli
description: General purpose medium for E. coli
composition:
  - compound: Tryptone
    amount: 10 g/L
  - compound: Yeast Extract
    amount: 5 g/L
  - compound: NaCl
    amount: 5 g/L
_source:
  file: /path/to/raw/togo/togo_media.json
  timestamp: '2026-01-27T10:30:00'
  layer: raw_yaml
```

Note: Field names differ from normalized schema (`media_id` vs `id`, `medium_name` vs `name`, etc.)

---

## Layer 3: Normalized YAML (`normalized_yaml/`)

**Purpose**: LinkML-validated, ontology-grounded, curated media recipes.

**Characteristics**:
- **LinkML schema compliance** - matches `culturemech.yaml` structure
- **Ontology grounded** - CHEBI for chemicals, NCBITaxon for organisms
- **Normalized values** - parsed quantities, standardized units
- **Curated** - reviewed, enhanced, corrected
- **Version controlled** - committed to git for tracking changes
- **Validated** - passes schema, term, and reference validation

This is the **knowledge base** - the authoritative source of truth for CultureMech data.

### Structure

```
normalized_yaml/
  bacterial/
    LB_Broth.yaml
    M9_Minimal_Medium.yaml
    Brain_Heart_Infusion.yaml
    ...
  fungal/
    Potato_Dextrose_Agar.yaml
    Sabouraud_Dextrose_Agar.yaml
    ...
  archaea/
    JCM_Medium_168.yaml
    ...
  algae/
    F_2_Medium.yaml
    ...
  specialized/
    Anaerobic_Medium.yaml
    Marine_Broth.yaml
    ...
```

### Importing from Raw to Normalized

Use importers to transform raw data into normalized, validated YAML:

```bash
# Import from different sources
just import-mediadive 50       # Import 50 MediaDive recipes
just import-togo 100           # Import 100 TOGO recipes
just import-atcc
just import-komodo-web
just import-mediadb

# Import all sources (caution: may take a while)
just import-all
```

Importers perform:
1. **Schema mapping** - Map source fields to LinkML schema
2. **Ontology resolution** - Lookup CHEBI IDs, NCBITaxon IDs
3. **Value normalization** - Parse "10 g/L" → `value: 10, unit: g/L`
4. **Categorization** - Assign to bacterial/fungal/archaea/etc.
5. **Validation** - Ensure LinkML compliance
6. **File naming** - Human-readable filenames

### Example Normalized YAML File

`normalized_yaml/bacterial/LB_Broth.yaml`:
```yaml
id: CULTUREMECH:000001
name: LB Broth (Lysogeny Broth)
description: General-purpose rich medium for bacterial culture
category: bacterial
organisms:
  - NCBITaxon:562  # Escherichia coli
components:
  - agent: CHEBI:16199  # tryptone
    concentration:
      value: 10.0
      unit: g/L
  - agent: CHEBI:83937  # yeast extract
    concentration:
      value: 5.0
      unit: g/L
  - agent: CHEBI:26710  # sodium chloride
    concentration:
      value: 5.0
      unit: g/L
ph:
  value: 7.0
  range: 6.8-7.2
preparation_steps:
  - Dissolve components in distilled water
  - Adjust pH to 7.0
  - Autoclave at 121°C for 15 minutes
xrefs:
  - TOGO:TM001
  - MediaDive:673e1234abcd5678
curation:
  - curator: mediadive-import
    date: '2026-01-23'
  - curator: manual-review
    date: '2026-01-27'
    note: Verified concentrations against ATCC
```

Note: Standardized field names, ontology CURIEs, parsed values.

### Validation

All normalized YAML must pass three validation layers:

```bash
# Full 3-layer validation (schema + terms + refs)
just validate normalized_yaml/bacterial/LB_Broth.yaml

# Validate all recipes
just validate-all

# Individual validation layers
just validate-schema normalized_yaml/bacterial/LB_Broth.yaml
just validate-terms normalized_yaml/bacterial/LB_Broth.yaml
just validate-refs normalized_yaml/bacterial/LB_Broth.yaml
```

**Validation layers**:
1. **Schema validation** - LinkML structure compliance
2. **Term validation** - Ontology term existence (CHEBI, NCBITaxon)
3. **Reference validation** - External database cross-references

---

## Layer 4: Merged YAML (`merge_yaml/`)

**Purpose**: Deduplicated recipes with identical ingredient sets consolidated into canonical records.

**Characteristics**:
- **Ingredient set matching** - Recipes with the same chemicals are merged (regardless of amounts)
- **Fingerprint-based** - SHA256 hash of sorted ingredient CHEBI IDs + names
- **Synonym tracking** - All alternate names preserved with provenance
- **Cross-category merging** - Recipes merged across categories
- **Provenance preservation** - All source recipe IDs tracked
- **Concentration-independent** - Matches ignore concentration, pH, temperature differences

**Important**: This layer identifies recipes with the **same base formulation** (same chemicals), not identical recipes. Recipes merged here may differ in concentrations, pH, preparation methods, and other parameters. This is useful for identifying that "LB Medium" exists across multiple databases even with slight formulation variations.

This layer reduces redundancy and provides a cleaner view of unique media formulations.

### Structure

```
merge_yaml/
  merged/
    LB_Medium.yaml                 # Canonical LB recipe
    M9_Minimal_Medium.yaml
    Potato_Dextrose_Agar.yaml
    ...
  merge_stats.json                 # Merge statistics
```

Note: Unlike normalized_yaml, merge_yaml uses a single flat directory since recipes span multiple categories.

### Merging Algorithm

Recipes are matched using ingredient fingerprints:

1. **Extract identifiers** - CHEBI IDs (preferred) or normalized ingredient names
2. **Generate fingerprint** - SHA256 hash of sorted ingredient set
3. **Group duplicates** - Recipes with identical fingerprints
4. **Select canonical** - Most common name (with source priority tie-breaking)
5. **Build synonyms** - Track all non-canonical names with provenance
6. **Merge categories** - Combine all original categories into multivalued field

**What IS considered in matching**:
- ✅ Chemical identity (CHEBI IDs or ingredient names)
- ✅ Presence/absence of each ingredient
- ✅ Solution compositions (ingredients within stock solutions)

**What is NOT considered in matching**:
- ❌ Ingredient concentrations (10 g/L vs 20 g/L = same)
- ❌ pH values
- ❌ Temperature settings
- ❌ Preparation steps
- ❌ Physical state (liquid vs solid agar)
- ❌ Medium type (complex vs defined)
- ❌ Other metadata fields

**Fingerprint generation details**:
- Includes both direct ingredients and solution compositions
- Order-independent (sorted before hashing)
- Concentration-independent (only ingredient identity matters)
- Hydration notation normalized (MgSO4·7H2O → MgSO4)

**Example**: These recipes would merge:
- "LB Medium (5 g/L NaCl, pH 7.0, liquid)"
- "LB Broth (10 g/L NaCl, pH 7.5, solid agar)"
- "Luria-Bertani (8 g/L NaCl, pH 6.8, liquid)"

All have the same ingredients (Tryptone, Yeast Extract, NaCl) so they match.

### Merging Recipes

```bash
# Perform merge (full dataset)
just merge-recipes

# Dry run (see what would be merged)
just merge-recipes true

# Generate statistics only
just merge-stats

# Verify merged recipes
just verify-merges

# Check recipe count reduction
just count-unique-recipes
```

### Example Merged Recipe

`merge_yaml/merged/LB_Medium.yaml`:
```yaml
name: LB medium                    # Canonical (most common)
original_name: LB medium
categories:                        # NEW: Multivalued
  - bacterial
  - specialized

medium_type: COMPLEX
physical_state: LIQUID

ingredients:
  - preferred_term: Tryptone
    concentration: {value: '10', unit: G_PER_L}
    term: {id: CHEBI:36316, label: tryptone}
    notes: 'Concentration may vary across sources (8-12 g/L)'

  - preferred_term: NaCl
    concentration: {value: '10', unit: G_PER_L}
    term: {id: CHEBI:26710, label: sodium chloride}
    notes: 'Concentration varies: 5-10 g/L depending on source'

# NEW: Synonym tracking
synonyms:
  - name: Luria-Bertani medium
    source: TOGO
    source_id: TOGO:M3236
    original_category: bacterial

  - name: LB Broth
    source: MediaDive
    source_id: mediadive.medium:673e1234
    original_category: bacterial

  - name: Lysogeny broth
    source: KOMODO
    source_id: KOMODO:LB_001
    original_category: specialized

# NEW: Provenance tracking
merged_from:
  - TOGO_M3236_Luria-Bertani_LB_medium
  - MediaDive_673e1234_LB_Broth
  - KOMODO_LB_001_Lysogeny_broth

merge_fingerprint: 8f3d2a1b9c4e5f6a7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0

curation_history:
  - timestamp: '2026-02-03T14:23:45.123456Z'
    curator: recipe-merger
    action: Merged 3 duplicate recipes into canonical record
    notes: 'Sources: TOGO:M3236, MediaDive:673e1234, KOMODO:LB_001'
```

### Merge Statistics

`merge_yaml/merge_stats.json`:
```json
{
  "timestamp": "2026-02-03T08:00:00Z",
  "input_recipes": 10595,
  "output_recipes": 344,
  "reduction": 10251,
  "reduction_percentage": 96.8,
  "cross_category_merges": 12,
  "largest_group_size": 17,
  "top_duplicates": [
    {
      "name": "LB medium",
      "count": 8,
      "sources": ["TOGO", "MediaDive", "KOMODO"],
      "categories": ["bacterial", "specialized"]
    }
  ]
}
```

### Validation

Merged recipes undergo verification:

```bash
just verify-merges
```

**Verification checks**:
1. **Schema validity** - All recipes validate against LinkML schema
2. **No duplicate names** - Canonical names are unique
3. **Completeness** - All input recipes accounted for
4. **Fingerprint consistency** - Stored fingerprints match recomputed
5. **Synonym completeness** - Multi-source merges have synonyms
6. **Category tracking** - All original categories preserved

---

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        LAYER 1: raw/                             │
│  Original source files (JSON, TSV, SQL, HTML)                   │
│  Immutable, includes README.md provenance                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ just convert-to-raw-yaml
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     LAYER 2: raw_yaml/                           │
│  Mechanical YAML conversion (unnormalized)                       │
│  Preserves original field names and values                       │
│  Regenerable from Layer 1                                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ just import-*
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  LAYER 3: normalized_yaml/                       │
│  LinkML-validated, ontology-grounded recipes                     │
│  Curated, normalized, version controlled                         │
│  ~10,595 recipes                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ just merge-recipes
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   LAYER 4: merge_yaml/                           │
│  Deduplicated recipes (identical ingredients merged)             │
│  Canonical records with synonym tracking                         │
│  ~344 unique recipes (96.8% reduction)                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Exports & Applications
                              ▼
                    ┌─────────────────────┐
                    │  Browser (app/)     │
                    │  HTML Pages         │
                    │  KGX Export         │
                    │  API Endpoints      │
                    └─────────────────────┘
```

---

## Commands Summary

### Fetch Raw Data (Layer 1)
```bash
just fetch-raw-data              # Fetch all core sources
just fetch-mediadive-raw         # Fetch MediaDive
just fetch-togo-raw [limit]      # Fetch TOGO Medium
just fetch-mediadive-api [limit] # Fetch MediaDive compositions
just fetch-komodo-web            # Fetch KOMODO web data
just fetch-mediadb <path>        # Fetch MediaDB SQL dump
```

### Convert to Raw YAML (Layer 1 → Layer 2)
```bash
just convert-to-raw-yaml all     # Convert all sources
just convert-to-raw-yaml mediadive  # Convert specific source
just convert-mediadive-raw-yaml  # Individual converter
```

### Import to Normalized (Layer 1 → Layer 3)
```bash
just import-mediadive [limit]    # Import MediaDive recipes
just import-togo [limit]         # Import TOGO recipes
just import-atcc                 # Import ATCC recipes
just import-komodo-web           # Import KOMODO recipes
just import-all                  # Import from all sources
```

### Validate Normalized (Layer 3)
```bash
just validate <file>             # 3-layer validation
just validate-all                # Validate all recipes
just validate-schema <file>      # Schema only
just validate-terms <file>       # Terms only
just validate-refs <file>        # References only
```

### Merge Recipes (Layer 3 → Layer 4)
```bash
just merge-recipes               # Perform merge
just merge-recipes true          # Dry run (preview merges)
just merge-stats                 # Generate statistics only
just verify-merges               # Validate merged recipes
just count-unique-recipes        # Show reduction
```

### Statistics
```bash
just show-raw-data-stats         # Raw data counts
just count-recipes               # Normalized recipe counts
just list-recipes                # List all recipes
```

---

## Version Control Strategy

### Included in Git

✅ **Layer 3: `normalized_yaml/`** - Full version control
- All `.yaml` files committed
- Track changes over time
- Enable collaborative curation
- Support diffs and reviews

✅ **Layer 4: `merge_yaml/`** - Deduplicated recipes
- All merged `.yaml` files committed
- `merge_stats.json` tracked
- Regenerable from Layer 3 but version controlled for stability

✅ **Provenance** - README files in all layers
- `raw/*/README.md` - Source documentation
- `raw_yaml/*/README.md` - Conversion notes

### Excluded from Git

❌ **Layer 1: `raw/`** - Too large, regenerable
- `.json`, `.tsv`, `.html`, `.sql` files ignored
- Fetch on demand with `just fetch-*` commands
- Keep README.md for provenance

❌ **Layer 2: `raw_yaml/`** - Regenerable from Layer 1
- All `.yaml` files ignored
- Regenerate with `just convert-to-raw-yaml`

See `.gitignore` for complete patterns.

---

## Best Practices

### Adding New Data Sources

1. **Create raw/ directory**: `mkdir -p raw/newsource/`
2. **Document provenance**: Create `raw/newsource/README.md`
3. **Fetch raw data**: Add `just fetch-newsource` command
4. **Create converter**: Add `src/culturemech/convert/newsource_raw_yaml.py`
5. **Create importer**: Add `src/culturemech/import/newsource_importer.py`
6. **Add commands**: Update `project.justfile` with fetch/convert/import commands
7. **Test pipeline**: Fetch → Convert → Import → Validate

### Updating Existing Data

1. **Re-fetch raw**: `just fetch-<source>-raw` (updates Layer 1)
2. **Reconvert**: `just convert-<source>-raw-yaml` (regenerates Layer 2)
3. **Reimport**: `just import-<source>` (updates Layer 3)
4. **Validate**: `just validate-all` (verify changes)
5. **Review diffs**: `git diff normalized_yaml/` (check what changed)
6. **Commit**: Commit updated normalized recipes

### Data Quality

- **Always validate** before committing normalized recipes
- **Document changes** in curation history
- **Review diffs** carefully when reimporting
- **Keep provenance** up to date in README files
- **Test imports** on small samples first (`--limit 10`)

---

## See Also

- **QUICK_START.md** - Getting started guide
- **IMPLEMENTATION_STATUS.md** - Current data coverage
- **ENRICHMENT_GUIDE.md** - Enhancing recipes with ontology terms
- **CONTRIBUTING.md** - Contributing new recipes or sources
