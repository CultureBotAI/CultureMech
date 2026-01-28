# KOMODO Media Data

**Source**: KOMODO (Known Media Database)
**URL**: https://komodo.modelseed.org/
**Status**: Fetcher/Importer Implemented - Needs SQL Dump

---

## Overview

KOMODO is a standardized media database developed by DSMZ (Leibniz Institute) containing 3,335 media formulations with standardized molar concentrations integrated with the SEED compound database.

### Key Features

- **3,335 media** with complete compositions
- **Standardized molar concentrations** (mM) for all components
- **SEED compound database** integration for systems biology
- **High-confidence organism-media associations**
- **Derived from DSMZ PDFs** (same source as MediaDive)

### Reference

**Publication**: Zarecki et al. (2015)
**Title**: "A novel nutritional predictor links microbial fastidiousness with lowered ubiquity, growth rate, and cooperativeness"
**Journal**: Nature Communications
**DOI**: https://doi.org/10.1038/ncomms7859
**URL**: https://www.nature.com/articles/s41467-019-08888-8

---

## Data Acquisition

### Option 1: Supplementary Data Files (Recommended) ✅

**Direct Download from PubMed Central**:

The KOMODO data is available as supplementary Excel files from the original Nature Communications paper (PMC4633754).

**Available Files**:
- **ncomms9493-s5.xlsx** (171.4KB) - SEED compounds with IDs and mappings
- **ncomms9493-s1.pdf** (1.2MB) - Supplementary figures, tables, and notes

**Download Links**:
1. Visit PMC article: https://pmc.ncbi.nlm.nih.gov/articles/PMC4633754/
2. Download supplementary files from the "Supplementary Materials" section
3. Save Excel files to a local directory

**Automated Download** (using wget or curl):
```bash
# SEED compounds
wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4633754/bin/ncomms9493-s5.xlsx

# Supplementary information (contains media details)
wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4633754/bin/ncomms9493-s1.pdf

# Or all supplementary files
wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4633754/bin/ncomms9493-s2.xlsx
wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4633754/bin/ncomms9493-s3.xlsx
wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4633754/bin/ncomms9493-s4.xlsx
```

### Option 2: KOMODO Website Database Export

**Website**: https://komodo.modelseed.org/

The KOMODO website contains ~1,500 media formulations that can be browsed online. For bulk export:
- Contact: raphy.zarecki@gmail.com
- Request: Database export or API access

### Option 3: ModelSEED Database Repository

**Repository**: https://github.com/ModelSEED/ModelSEEDDatabase

The ModelSEED repository contains biochemistry data (33,978 compounds, 36,645 reactions) but **does not directly include KOMODO media formulations**. However, it provides:
- SEED compound definitions (Biochemistry/compounds.tsv)
- Reaction database for metabolic modeling
- Integration framework for ModelSEED tools

Note: You'll need to combine ModelSEED compounds with KOMODO media data from supplementary files.

### Option 4: SQL Database Dump (Legacy)

**Contact KOMODO Maintainers**:
- Email: raphy.zarecki@gmail.com
- Request: KOMODO SQL database dump (if available)

This was the original planned approach but supplementary files (Option 1) are now preferred.

---

## Fetch Command

### Quick Start (Recommended)

Download supplementary Excel files and use the fetcher:

```bash
# 1. Download Excel files
mkdir -p downloads/komodo
cd downloads/komodo
wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4633754/bin/ncomms9493-s5.xlsx
# Download other supplementary files as needed

# 2. Run fetcher with Excel files
cd /path/to/CultureMech
just fetch-komodo-raw downloads/komodo/

# OR with SQL dump (if you have one)
just fetch-komodo-raw path/to/komodo.sql
```

### What the Fetcher Does

The fetcher auto-detects the input format:

**For Excel Files** (.xlsx):
1. Parse Excel supplementary data files
2. Extract SEED compounds and media information
3. Build media-compound relationships
4. Export to JSON format

**For SQL Dumps** (.sql):
1. Parse SQL dump using sqlparse
2. Extract media, compounds, and organisms tables
3. Convert to JSON format
4. Save to this directory

**For Directories**:
1. Scan for Excel (.xlsx) or SQL (.sql) files
2. Process all found files
3. Merge data into unified JSON output

### Expected Output Files

After fetching, this directory will contain:

```
komodo_media.json          # 3,335 media records with compositions
komodo_compounds.json      # SEED compound mappings
komodo_organisms.json      # Organism-media associations
fetch_stats.json           # Metadata (date, count, source)
README.md                  # This file (provenance)
```

---

## Import Command

After fetching, import to CultureMech:

```bash
# Test with 10 media
just import-komodo 10

# Full import (~300 new + ~3,000 enriched expected)
just import-komodo
```

### Import Process

1. **Load JSON data** from this directory
2. **Map SEED compounds to ChEBI** via ChemicalMapper
3. **Convert molar concentrations** to MM unit enum
4. **Deduplicate** against existing MediaDive recipes
5. **Generate YAML files** in `kb/media/` directory

### Expected Outcomes

- **~300 new unique media** after deduplication (KOMODO overlaps with MediaDive)
- **~3,000 existing MediaDive recipes enriched** with molar concentrations
- **100% schema validation** pass rate
- **High ChEBI coverage** via ChemicalMapper

---

## Data Format

### Media Record Structure

```json
{
  "id": "medium_1",
  "name": "LB Medium",
  "composition": [
    {
      "seed_id": "cpd00001",
      "compound_name": "H2O",
      "concentration_mM": 1000.0
    },
    {
      "seed_id": "cpd00023",
      "compound_name": "L-glutamate",
      "concentration_mM": 10.5
    }
  ]
}
```

### Compound Record Structure

```json
{
  "id": "cpd00023",
  "name": "L-glutamate",
  "seed_id": "cpd00023",
  "formula": "C5H9NO4",
  "charge": -1
}
```

---

## Integration with CultureMech

### Advantages

1. **Standardized Units**: All concentrations in molar units (mM) - ideal for metabolic modeling
2. **SEED Integration**: Links to BiGG, KEGG, and other metabolic databases
3. **Backfill Existing Data**: Enriches MediaDive recipes with quantitative concentrations
4. **High Confidence**: Curated from authoritative DSMZ sources

### Overlaps

- **DSMZ Source**: Both KOMODO and MediaDive use DSMZ as primary source
- **Expected Overlap**: ~90% of KOMODO media already in MediaDive
- **Value Add**: Molar concentrations and SEED compound IDs

---

## Statistics

View fetch statistics:

```bash
just import-komodo-stats
```

Example output:
```json
{
  "fetch_date": "2026-01-24T12:00:00Z",
  "source": "KOMODO",
  "total_media": 3335,
  "total_compounds": 1200,
  "total_organisms": 500,
  "url": "https://komodo.modelseed.org/"
}
```

---

## Troubleshooting

### SQL Parsing Issues

If SQL parsing fails:
1. Check SQL file encoding (should be UTF-8)
2. Ensure sqlparse is installed: `uv pip install sqlparse`
3. Try different SQL dump formats (MySQL vs PostgreSQL)

### Missing Compounds

If SEED compounds are missing:
- ChemicalMapper will attempt fallback to name-based lookup
- Some SEED IDs may not have ChEBI mappings
- Manual curation may be needed for unmapped compounds

### High Duplication Rate

If >95% of media are duplicates:
- This is expected due to MediaDive overlap
- KOMODO's value is in molar concentrations, not new recipes
- Focus on enrichment statistics

---

## License & Attribution

**KOMODO License**: Check with maintainers for current license terms
**Citation**: Zarecki et al. (2015) Nature Communications
**Integration**: CultureMech (CC0-1.0)

When using KOMODO data, please cite the original publication.

---

## See Also

- [MediaDive](../mediadive/README.md) - Overlapping DSMZ source
- [MicrobeMediaParam](../microbe-media-param/README.md) - ChEBI mappings
- [MEDIA_SOURCES.tsv](../MEDIA_SOURCES.tsv) - All data sources
- [Implementation Plan](../../docs/IMPLEMENTATION_STATUS.md) - Integration roadmap
