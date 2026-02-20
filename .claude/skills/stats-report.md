# Stats Report Skill

**Name:** stats-report
**Version:** 1.0.0
**Invocation:** `/stats-report`

## What This Skill Does

Generates comprehensive statistics for the CultureMech repository, including:
- Recipe counts by category (algae, bacterial, fungal, archaea, specialized)
- Recipe counts by source (KOMODO, MediaDive, TOGO, MediaDB, UTEX, CCAP, SAG, etc.)
- Ingredient mapping coverage (CHEBI, PubChem, CAS-RN)
- Data quality metrics
- Medium composition distribution
- Physical state distribution

This skill produces reproducible, timestamped statistics reports in multiple formats.

## Usage

Basic usage (terminal output only):
```bash
uv run python scripts/generate_stats.py --terminal-only
```

Generate full report with both JSON and Markdown:
```bash
uv run python scripts/generate_stats.py --output-dir output/stats
```

Generate specific formats:
```bash
# JSON only
uv run python scripts/generate_stats.py --output-json output/stats/stats.json

# Markdown only
uv run python scripts/generate_stats.py --output-markdown output/stats/stats.md
```

Using justfile commands (recommended):
```bash
# Full report (JSON + Markdown)
just stats-report

# Terminal output only
just stats-terminal

# Specific formats
just stats-json
just stats-markdown
```

## Output Formats

### Terminal Output
Colorized summary with key metrics displayed in a box format for quick overview.

### JSON (`stats.json`)
Structured data suitable for programmatic access:
```json
{
  "metadata": {
    "generated_at": "2026-02-02T...",
    "repository": "KG-Microbe/CultureMech",
    "total_recipes": 10595
  },
  "recipes_by_category": {...},
  "recipes_by_source": {...},
  "ingredient_mapping": {
    "total_ingredients": 166242,
    "with_chebi": 55678,
    "with_chebi_pct": 33.5,
    "with_pubchem": 42000,
    "with_pubchem_pct": 25.3,
    "with_cas_rn": 38000,
    "with_cas_rn_pct": 22.9,
    "unmapped": 30564,
    "unmapped_pct": 18.4
  },
  "data_quality": {...},
  "medium_composition": {...},
  "physical_state": {...}
}
```

### Markdown (`stats.md`)
Human-readable report with formatted tables, perfect for documentation or README updates.

## Performance

- **Processing Time:** ~60-90 seconds for 10,595 recipes (cold start)
- **Memory Usage:** ~100MB (ChemicalMapper + recipe processing)
- **Output Size:** JSON ~50-100KB, Markdown ~10-20KB

## When to Use

Run this skill whenever you need to:
- Update repository statistics in README.md
- Generate reports for publications or presentations
- Track changes in data coverage over time
- Verify data quality after imports or enrichment operations
- Answer questions about repository contents

## Technical Details

The skill performs a single-pass analysis of all recipes in `data/normalized_yaml/`:
1. Loads ChemicalMapper with MicrobeMediaParam and MediaDive mappings
2. Iterates through all 10,595 YAML files once
3. Extracts metrics without modifying any files
4. Calculates derived statistics and percentages
5. Formats output in requested format(s)

Source detection logic:
1. Checks `curation_history[0].curator` field
2. Falls back to filename prefix parsing
3. Maps to canonical source names

Ingredient mapping analysis:
- **CHEBI:** Checks if `ingredient['term']['id']` starts with 'CHEBI:'
- **PubChem:** Uses `mapper.lookup(preferred_term)['pubchem_id']`
- **CAS-RN:** Uses `mapper.lookup(preferred_term)['cas_rn']`
- **Unmapped:** Counts ingredients with none of the above

## Dependencies

Required:
- Python 3.9+
- PyYAML
- ChemicalMapper (src/culturemech/import/chemical_mappings.py)
- MicrobeMediaParam mappings (data/raw/microbe-media-param/)
- MediaDive data (data/raw/mediadive/)

## Related Commands

- `just count-recipes` - Quick recipe count by category
- `just show-raw-data-stats` - Statistics for raw data sources
- `just import-*-stats` - Import statistics for specific sources
