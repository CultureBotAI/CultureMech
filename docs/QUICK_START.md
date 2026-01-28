# CultureMech Quick Start Guide

## Installation

```bash
# Install dependencies
just install

# Optional: Install Koza for KG export
just install-koza
```

## Data Layers Architecture

CultureMech uses a 3-layer data architecture:

```
📁 raw/          ← Layer 1: Original source data (immutable)
   └─ mediadive/
      ├─ mediadive_media.json (3,327 recipes)
      ├─ mediadive_ingredients.json (1,234 mappings)
      └─ README.md (provenance)

📁 data/processed/    ← Layer 2: Intermediate transformations (regenerable)
   └─ (future enhancements)

📁 normalized_yaml/          ← Layer 3: Curated LinkML YAML (version controlled)
   ├─ bacterial/ (2,877 recipes)
   ├─ fungal/ (114 recipes)
   ├─ specialized/ (96 recipes)
   ├─ archaea/ (59 recipes)
   └─ algae/ (0 recipes, ready for future)
```

See [DATA_LAYERS.md](DATA_LAYERS.md) for complete architecture documentation.

---

## Basic Workflow

### 1. Fetch Raw Data

```bash
# Fetch all available raw data sources
just fetch-raw-data

# Or fetch specific sources
just fetch-mediadive-raw
just fetch-microbe-media-param-raw

# Check what you have
just show-raw-data-stats
```

**Result**:
```
MediaDive:
  📁 mediadive_media.json: 3,327 records
  📦 Size: 1.1M
```

### 2. Import to Knowledge Base

```bash
# Import all MediaDive recipes
just import-mediadive

# Or test with limited number
just import-mediadive 10
```

**Result**: Creates 3,146 validated YAML files in `normalized_yaml/`

### 3. Validate

```bash
# Validate a single recipe
just validate normalized_yaml/bacterial/LB_Broth.yaml

# Validate all recipes
just validate-all

# Full QC pipeline
just qc
```

### 4. Generate Outputs

```bash
# Faceted browser
just gen-browser-data
just serve-browser
# Open http://localhost:8000/app/

# HTML pages
just gen-pages
# Pages generated in pages/

# Knowledge graph export
just kgx-export
# KGX edges in output/kgx/
```

---

## Common Tasks

### View a Recipe in Browser

```bash
just serve-browser
# Navigate to http://localhost:8000/app/
# Search for "LB Broth" or filter by organism
```

### View a Recipe as HTML

```bash
just gen-page normalized_yaml/bacterial/LB_Broth.yaml
open pages/LB_Broth.html
```

### Search for Recipes

```bash
# Using grep
grep -r "Escherichia coli" normalized_yaml/

# Using the browser (best experience)
just serve-browser
```

### Add a New Recipe

```bash
# Create new file (follow template)
cp normalized_yaml/bacterial/LB_Broth.yaml normalized_yaml/bacterial/My_New_Medium.yaml

# Edit the file
# (Use CONTRIBUTING.md for guidelines)

# Validate
just validate normalized_yaml/bacterial/My_New_Medium.yaml

# If valid, commit
git add normalized_yaml/bacterial/My_New_Medium.yaml
git commit -m "Add My New Medium recipe"
```

### Update Data from Source

```bash
# Backup current data
cp -r normalized_yaml normalized_yaml.backup.$(date +%Y%m%d)

# Fetch latest raw data
just fetch-raw-data

# Re-import
just import-mediadive

# Validate
just validate-all

# Review changes
git diff normalized_yaml/

# Commit if satisfied
git add normalized_yaml/
git commit -m "Update MediaDive recipes"
```

---

## Chemical Mappings

Test ingredient name → CHEBI ID mappings:

```bash
# Test a specific ingredient
just test-chemical-mappings glucose

# Show coverage statistics
just chemical-mapping-stats
```

**Output**:
```
Lookup: glucose
  ✓ Found in MediaDive
  CHEBI ID: CHEBI:17234
  Label: glucose
  Formula: C6H12O6

Statistics:
  Total ingredients: 1,234
  With CHEBI IDs: 686 (56%)
```

---

## Troubleshooting

### Raw data not found

```bash
# Fetch the data
just fetch-mediadive-raw

# Check if path is correct
cat raw/mediadive/README.md

# Update path in project.justfile if needed
# Look for: cmm_automation_dir := "..."
```

### Validation errors

```bash
# Schema validation only (fastest)
just validate-schema normalized_yaml/bacterial/LB_Broth.yaml

# Term validation (requires ontologies)
just validate-terms normalized_yaml/bacterial/LB_Broth.yaml

# Check if ontologies are downloaded
ls ~/.data/oaklib/
```

### Browser not loading

```bash
# Regenerate browser data
just gen-browser-data

# Check if data.js exists
ls -lh app/data.js

# Serve and check console
just serve-browser
# Open browser console (F12) for errors
```

### Import failures

```bash
# Check import statistics
just import-mediadive-stats

# Test with small batch
just import-mediadive 5

# Check logs for specific errors
# Errors are printed during import
```

---

## File Locations

```
CultureMech/
├─ data/
│  ├─ raw/              # Original source data
│  │  ├─ mediadive/
│  │  └─ microbe-media-param/
│  └─ processed/        # Intermediate (future)
│
├─ kb/
│  └─ media/            # Curated YAML recipes ★
│     ├─ bacterial/
│     ├─ fungal/
│     ├─ archaea/
│     ├─ specialized/
│     └─ algae/
│
├─ src/
│  └─ culturemech/
│     ├─ schema/        # LinkML schema
│     ├─ import/        # Importers
│     ├─ export/        # KGX, browser exports
│     └─ templates/     # Jinja2 HTML templates
│
├─ app/                 # Faceted browser UI
│  ├─ index.html
│  ├─ schema.js
│  └─ data.js          # Generated
│
├─ pages/              # Generated HTML pages
├─ output/             # Generated KG exports
└─ tests/              # Test suite
```

---

## Available Commands

Run `just --list` to see all commands, organized by group:

```bash
just --list

Available recipes:
    [Data]      fetch-raw-data              # Fetch all raw data
    [Data]      fetch-mediadive-raw         # Fetch MediaDive
    [Data]      show-raw-data-stats         # Show statistics

    [Import]    import-mediadive [limit]    # Import from MediaDive
    [Import]    chemical-mapping-stats      # Chemical coverage

    [QC]        validate file               # 3-layer validation
    [QC]        validate-all                # Validate all recipes
    [QC]        qc                          # Full QC pipeline

    [Export]    kgx-export                  # Export to KG format

    [Browser]   gen-browser-data            # Generate browser data
    [Browser]   serve-browser               # Serve browser locally

    [Pages]     gen-pages                   # Generate HTML pages
    [Pages]     gen-page file               # Generate single page

    [Docs]      serve-docs                  # Serve documentation

    [Utils]     clean                       # Clean generated files
    [Utils]     count-recipes               # Count by category
```

---

## Next Steps

1. **Explore the browser**: `just serve-browser`
2. **Read a recipe**: `cat normalized_yaml/bacterial/LB_Broth.yaml`
3. **Understand the schema**: `cat src/culturemech/schema/culturemech.yaml`
4. **Add a recipe**: Follow [CONTRIBUTING.md](CONTRIBUTING.md)
5. **Export to KG**: `just kgx-export`

---

## Documentation

- **DATA_LAYERS.md**: Complete data architecture
- **CONTRIBUTING.md**: Curation guidelines
- **README.md**: Full project documentation
- **IMPORT_COMPLETE.md**: Import statistics and future roadmap
- **IMPLEMENTATION_SUMMARY.md**: Technical details

---

## Support

- **Issues**: File on GitHub (add repo link when available)
- **Questions**: Check documentation first
- **Contributing**: See CONTRIBUTING.md

---

**Status**: Production ready with 3,146 validated recipes!

**Last Updated**: 2026-01-21
