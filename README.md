# 🧫 CultureMech

**Microbial Growth Media Knowledge Base**

A comprehensive, ontology-grounded knowledge base for microbial culture media recipes and formulations. Built following the proven [dismech](https://github.com/monarch-initiative/dismech) architecture with rich YAML data, semantic validation, and knowledge graph export.

## Features

✅ **Rich YAML recipes** - Detailed formulations with ingredients, preparation steps, and evidence
✅ **Ontology-grounded** - CHEBI for chemicals, NCBITaxon for organisms, multiple media databases
✅ **3-layer validation** - Schema → Terms → References (anti-hallucination safeguards)
✅ **Knowledge graph export** - Biolink-compliant KGX edges via Koza transforms
✅ **Faceted browser** - Client-side search and filtering for scientist discovery
✅ **HTML page generation** - Beautiful recipe pages with CURIE resolution
✅ **Comprehensive testing** - 25+ unit tests for data quality

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/KG-Hub/CultureMech.git
cd CultureMech

# Install dependencies (requires uv or pip)
just install

# Optional: Install Koza for KG export
just install-koza
```

### View the Browser

```bash
# Generate browser data
just gen-browser-data

# Serve locally
just serve-browser

# Open http://localhost:8000/app/
```

### Validate Recipes

```bash
# Validate a single recipe (3 layers)
just validate data/normalized_yaml/bacterial/LB_Broth.yaml

# Validate all recipes
just validate-all

# Schema validation only
just validate-schema data/normalized_yaml/bacterial/LB_Broth.yaml
```

### Generate HTML Pages

```bash
# Generate pages for all recipes
just gen-pages

# Generate page for single recipe
just gen-page data/normalized_yaml/bacterial/LB_Broth.yaml

# View generated pages in pages/
```

### Export to Knowledge Graph

```bash
# Export to KGX format
just kgx-export

# Output in output/kgx/*.jsonl
```

## Data Sources

CultureMech integrates media recipes from multiple authoritative sources:

### Integrated Sources ✅

| Source | Records | Coverage | Status |
|--------|---------|----------|--------|
| **MediaDive** (DSMZ) | 3,327 | Bacteria, Fungi, Archaea | ✅ Complete |
| **TogoMedium** | 2,917 | Japanese BRCs | ✅ Complete |
| **MicrobeMediaParam** | ~5,000 mappings | Chemical entity mappings | ✅ Complete |
| **ATCC** | ~300 | Manual curation | 🔄 Partial |

### Available for Integration 🆕

| Source | Records | Integration Guide | Command |
|--------|---------|------------------|---------|
| **BacDive** | 66,570 cultivation datasets | `data/raw/bacdive/README.md` | `just fetch-bacdive-raw` |
| **NBRC** | 400+ media | `data/raw/nbrc/README.md` | `just scrape-nbrc-raw` |
| **KOMODO** | 3,335 media variants | Planned | - |
| **MediaDB** | 65 defined media | Planned | - |
| **UTEX** | 68 algae media | Planned | - |

**Total Coverage (Current)**: ~3,500 unique media recipes
**Projected Coverage (After Integration)**: ~6,400 unique recipes + 70,000 organism associations

See `data/MEDIA_SOURCES.tsv` for complete source tracking and `docs/DATA_SOURCES_SUMMARY.md` for detailed integration strategy.

### Fetching Data

```bash
# Fetch core sources
just fetch-raw-data

# Optional: Fetch BacDive (requires free registration)
just fetch-bacdive-raw 10  # Test with 10 strains
just import-bacdive

# Optional: Scrape NBRC (ethical web scraping)
just scrape-nbrc-raw 5  # Test with 5 media
just import-nbrc
```

## Project Structure

```
CultureMech/
├── src/culturemech/              # Python package
│   ├── schema/                   # LinkML schema definitions
│   ├── fetch/                    # Data fetchers (10 sources)
│   ├── convert/                  # Raw YAML converters
│   ├── import/                   # Normalized importers
│   ├── export/                   # Browser & KGX exporters
│   ├── templates/                # HTML templates
│   └── render.py                 # Page generator
├── data/                         # Three-tier data architecture
│   ├── raw/                      # Layer 1: Source files (git ignored)
│   ├── raw_yaml/                 # Layer 2: Unnormalized YAML (git ignored)
│   └── normalized_yaml/          # Layer 3: Curated recipes (version controlled)
│       ├── algae/               # 242 algae media recipes
│       ├── bacterial/           # 10,072 bacterial media recipes
│       ├── fungal/              # 119 fungal media recipes
│       ├── archaea/             # 63 archaeal media recipes
│       └── specialized/         # 99 specialized media recipes
├── docs/                         # Documentation
│   ├── DATA_LAYERS.md           # Three-tier architecture guide
│   ├── QUICK_START.md           # Getting started guide
│   └── *.md                     # Additional documentation
├── app/                          # Browser interface
│   ├── index.html               # Faceted search UI
│   └── schema.js                # Browser configuration
├── tests/                        # Test suite
├── conf/                         # Configuration files
├── project.justfile              # Build automation
└── pyproject.toml               # Python project config
```

## Documentation

Comprehensive documentation is available in the `docs/` directory:

- **[Quick Start Guide](docs/QUICK_START.md)** - Get up and running in 5 minutes
- **[Quick Reference](docs/QUICK_REFERENCE.md)** - Command cheat sheet
- **[Data Layers](docs/DATA_LAYERS.md)** - Three-tier architecture explained
- **[Implementation Status](docs/IMPLEMENTATION_STATUS.md)** - Current integration progress
- **[Contributing Guide](docs/CONTRIBUTING.md)** - How to contribute recipes and code
- **[Enrichment Guide](docs/ENRICHMENT_GUIDE.md)** - Data quality improvement workflow

### Key Documentation

- **Algae Pipeline**: [ALGAE_PIPELINE_COMPLETE.md](docs/ALGAE_PIPELINE_COMPLETE.md) - Full algae collections integration
- **Three-Tier Migration**: [MIGRATION_GUIDE.md](docs/MIGRATION_GUIDE.md) - Old to new directory structure
- **Data Sources**: [DATA_SOURCES_SUMMARY.md](docs/DATA_SOURCES_SUMMARY.md) - Source repository details

## Recipe Format

Recipes are stored as YAML files following the LinkML schema. Here's a minimal example:

```yaml
name: LB Broth
category: bacterial

medium_type: COMPLEX
physical_state: LIQUID

target_organisms:
  - preferred_term: Escherichia coli
    term:
      id: NCBITaxon:562
      label: Escherichia coli

ingredients:
  - preferred_term: Tryptone
    concentration:
      value: "10"
      unit: G_PER_L

  - preferred_term: Sodium Chloride
    term:
      id: CHEBI:26710
      label: sodium chloride
    concentration:
      value: "10"
      unit: G_PER_L

preparation_steps:
  - step_number: 1
    action: DISSOLVE
    description: Dissolve all ingredients in 1 L distilled water

  - step_number: 2
    action: AUTOCLAVE
    description: Autoclave at 121°C for 20 minutes
    temperature:
      value: 121
      unit: CELSIUS
    duration: "20 minutes"

sterilization:
  method: AUTOCLAVE
  temperature:
    value: 121
    unit: CELSIUS
  duration: "20 minutes"

applications:
  - Routine cultivation of E. coli
  - Plasmid amplification

curation_history:
  - timestamp: "2026-01-21T20:00:00Z"
    curator: your-name
    action: Initial creation
```

See `kb/media/bacterial/` for complete examples.

## Data Model

### Key Classes

- **MediaRecipe** - Root entity (one per YAML file)
- **IngredientDescriptor** - Chemicals with CHEBI terms
- **OrganismDescriptor** - Target organisms with NCBITaxon IDs
- **SolutionDescriptor** - Stock solutions
- **PreparationStep** - Ordered protocol steps
- **MediaVariant** - Related formulations

### Ontology Bindings

- **CHEBI** - Chemical ingredients
- **NCBITaxon** - Target organisms
- **DSMZ, TOGO, ATCC, NCIT** - Media database references
- **UO** - Units of measurement
- **NCIT** - Medium type classification

### Enums

- `MediumTypeEnum`: DEFINED, COMPLEX, MINIMAL, SELECTIVE, DIFFERENTIAL, ENRICHMENT
- `PhysicalStateEnum`: LIQUID, SOLID_AGAR, SEMISOLID, BIPHASIC
- `PreparationActionEnum`: DISSOLVE, MIX, HEAT, AUTOCLAVE, FILTER_STERILIZE, etc.
- `SterilizationMethodEnum`: AUTOCLAVE, FILTER, DRY_HEAT, TYNDALLIZATION

## Validation Strategy

### Three-Layer Pipeline

1. **Schema Validation** - YAML structure, required fields, data types
2. **Term Validation** - Ontology IDs exist and labels match (via OAK)
3. **Reference Validation** - Evidence snippets match PubMed abstracts (optional)

```bash
# Full validation
just validate kb/media/bacterial/LB_Broth.yaml

# Individual layers
just validate-schema kb/media/bacterial/LB_Broth.yaml
just validate-terms kb/media/bacterial/LB_Broth.yaml
just validate-references kb/media/bacterial/LB_Broth.yaml
```

### Anti-Hallucination Safeguards

- **Term validation** prevents fake ontology IDs
- **Label matching** catches copy-paste errors
- **Reference validation** ensures evidence accuracy
- **Required ontology terms** for key entities (organisms, chemicals)

## Knowledge Graph Export

Recipes are transformed into Biolink-compliant KGX edges:

1. **Medium → has_part → Chemical** (CHEBI)
2. **Medium → affects → Organism** (NCBITaxon)
3. **Medium → has_attribute → Application**
4. **Medium → has_attribute → Physical State**
5. **Dataset → related_to → Medium**
6. **Medium → same_as → Database ID** (DSMZ, TOGO, etc.)
7. **Variant → subclass_of → Base Medium**

```bash
just kgx-export
# Output: output/kgx/*.jsonl
```

### Lossy Transform

The KG export is **intentionally lossy** - rich preparation details, notes, and nested structures remain in YAML for agent consumption. The KG captures semantic relationships for querying.

## Browser Features

The faceted search browser (`app/index.html`) provides:

- **Full-text search** - Name, organism, ingredient, application
- **Faceted filtering** - Category, type, state, organisms, ingredients, sterilization
- **Real-time filtering** - Instant results
- **External links** - CHEBI, NCBITaxon, media databases
- **Mobile responsive** - Works on all devices

## Development

### Running Tests

```bash
# All tests
just test

# KGX export tests only
just test-kgx

# With coverage
just test-cov
```

### Adding a New Recipe

1. Create YAML file in appropriate category (e.g., `kb/media/bacterial/`)
2. Follow schema structure (see examples)
3. Validate: `just validate kb/media/bacterial/Your_Recipe.yaml`
4. Add ontology terms (CHEBI, NCBITaxon)
5. Regenerate browser data: `just gen-browser-data`
6. Generate HTML page: `just gen-page kb/media/bacterial/Your_Recipe.yaml`

### Build Commands

```bash
just --list              # Show all commands
just install             # Install dependencies
just validate FILE       # Validate recipe (3 layers)
just validate-all        # Validate all recipes
just gen-browser-data    # Generate browser data
just gen-pages           # Generate HTML pages
just kgx-export          # Export to KGX
just serve-browser       # Serve browser locally
just test                # Run tests
just clean               # Clean generated files
just count-recipes       # Count recipes by category
just build-all           # Full build pipeline
```

## Architecture Decisions

| Decision | Rationale | Trade-off |
|----------|-----------|-----------|
| Multi-source media IDs | Links to authoritative databases (DSMZ, TOGO, ATCC) | Requires custom OAK adapters or skip validation |
| Evidence optional | Supports historical recipes | Less rigorous provenance for some recipes |
| Nested solutions | Keeps related data together | Solutions not first-class entities in KG |
| Start with enum for prep steps | Fast iteration, add OBI later | Less semantic precision initially |
| Lossy KG transform | Standard graph format for queries | Agents must use YAML for full detail |
| One file per recipe | Simple validation, clear ownership | Can't share solutions across files |
| CHEBI for all chemicals | Standardized, validated | Some obscure chemicals may lack IDs |

## Contributing

We welcome contributions! To add recipes:

1. Fork the repository
2. Create recipe YAML following schema
3. Validate with `just validate`
4. Submit pull request

For major changes, please open an issue first to discuss.

## Ontology Resources

- **CHEBI**: https://www.ebi.ac.uk/chebi/
- **NCBITaxon**: https://www.ncbi.nlm.nih.gov/taxonomy
- **DSMZ Media Database**: https://mediadive.dsmz.de/
- **TOGO Medium**: http://togodb.org/db/medium/
- **ATCC**: https://www.atcc.org/

## License

This project is licensed under CC0 1.0 Universal (Public Domain Dedication).

Data is freely available for any use without restriction.

## Citation

If you use CultureMech in your research, please cite:

```
CultureMech: A Knowledge Base for Microbial Growth Media
KG-Hub Project, 2026
https://github.com/KG-Hub/CultureMech
```

## Related Projects

- **dismech** - Disease mechanism knowledge base (reference architecture)
- **KG-Microbe** - Microbial knowledge graph hub
- **KG-Hub** - Knowledge graph construction toolkit

## Contact

For questions or issues, please open a GitHub issue.

## Acknowledgments

Built following the proven dismech architecture pattern.
Inspired by DSMZ, TOGO, and ATCC media databases.
Part of the KG-Hub knowledge graph ecosystem.

---

Made with ❤️ for microbiology research
