# ⚗️ CultureMech

**Comprehensive Microbial Culture Media Knowledge Graph**

A production-ready knowledge base containing **10,595 culture media recipes** from 10 major international repositories, with LinkML schema validation, ontology grounding, and browser-based exploration.

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## 📊 Current Coverage

**Total Recipes**: **10,595** culture media formulations

| Category | Recipes | Sources |
|----------|---------|---------|
| **Bacterial** | 10,072 | MediaDive, TOGO, BacDive, ATCC, NBRC, KOMODO, MediaDB |
| **Algae** | 242 | UTEX, CCAP, SAG |
| **Fungal** | 119 | MediaDive, TOGO |
| **Specialized** | 99 | KOMODO |
| **Archaea** | 63 | MediaDive, TOGO |

## 📈 Detailed Statistics

### Recipes by Source

| Source | Recipes | Type | Description |
|--------|---------|------|-------------|
| **KOMODO** | 3,637 | Bacterial | Korean microbial media database |
| **MediaDive** | 3,327 | Multi-kingdom | DSMZ comprehensive collection |
| **TOGO Medium** | 2,917 | Multi-kingdom | Japanese BRCs curated database |
| **MediaDB** | 469 | Defined | Chemically defined media |
| **CCAP** | 113 | Algae | UK algae & protozoa collection |
| **UTEX** | 99 | Algae | University of Texas algae |
| **SAG** | 30 | Algae | German algae culture collection |
| **NBRC** | 2 | Bacterial | Japanese biological resources |
| **BacDive** | 1 | Bacterial | DSMZ cultivation conditions |

### Medium Composition

| Medium Type | Recipes | Percentage |
|-------------|---------|------------|
| **Complex** | 8,399 | 79.3% |
| **Defined** | 2,196 | 20.7% |

Complex media contain undefined components (e.g., yeast extract, peptone), while defined media have all components chemically specified.

### Physical State

| State | Recipes | Percentage |
|-------|---------|------------|
| **Liquid** | 10,593 | 99.98% |
| **Solid (Agar)** | 2 | 0.02% |

### Data Quality Metrics

| Metric | Value | Percentage |
|--------|-------|------------|
| **Recipes with ingredients** | 6,815 | 64.3% |
| **CHEBI-grounded ingredients** | 3,548 | 33.5% |
| **Average ingredients/recipe** | 15.7 | - |
| **LinkML validated** | 10,595 | 100% |

**Ontology Grounding:**
- Chemicals: CHEBI (Chemical Entities of Biological Interest)
- Organisms: NCBITaxon (NCBI Taxonomy)
- Media databases: DSMZ, TOGO, ATCC prefixes

## ✨ Features

✅ **10,595 recipes** - Production-ready dataset from 10 authoritative sources
✅ **Three-tier architecture** - Clean separation: raw → raw_yaml → normalized_yaml
✅ **LinkML schema validation** - Comprehensive data quality enforcement
✅ **Ontology grounding** - CHEBI for chemicals, NCBITaxon for organisms
✅ **Full provenance tracking** - Complete source attribution and curation history
✅ **Automated pipelines** - Fetchers, converters, and importers for all sources
✅ **Browser interface** - Faceted search and filtering
✅ **Knowledge graph export** - Biolink-compliant KGX format
✅ **Comprehensive documentation** - 30+ guides in `docs/`

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/CultureBotAI/CultureMech.git
cd CultureMech

# Install dependencies (requires uv)
just install

# Optional: Install Koza for KG export
just install-koza
```

### View the Browser

```bash
# Generate browser data from recipes
just gen-browser-data

# Serve locally
just serve-browser

# Open http://localhost:8000/app/
```

### Count Recipes

```bash
just count-recipes
# Output:
#   algae:      242
#   bacterial:  10,072
#   fungal:     119
#   archaea:    63
#   specialized: 99
#   Total:      10,595
```

### Validate Recipes

```bash
# Validate a single recipe
just validate data/normalized_yaml/bacterial/LB_Broth.yaml

# Validate all recipes
just validate-all

# Schema validation only
just validate-schema data/normalized_yaml/bacterial/LB_Broth.yaml
```

## 📚 Data Sources

CultureMech integrates culture media recipes from 10 major international repositories:

### Integrated Sources ✅

| Source | Recipes | Description | Status |
|--------|---------|-------------|--------|
| **KOMODO** | 3,637 | Korean microbial media database | ✅ Complete |
| **MediaDive** (DSMZ) | 3,327 | German Collection, comprehensive bacterial/fungal media | ✅ Complete |
| **TOGO Medium** | 2,917 | Japanese BRCs, curated media database | ✅ Complete |
| **MediaDB** | 469 | Chemically defined media database | ✅ Complete |
| **CCAP** | 113 | UK Culture Collection of Algae and Protozoa | ✅ Complete |
| **UTEX** | 99 | University of Texas algae collection | ✅ Complete |
| **SAG** | 30 | German algae culture collection (Göttingen) | ✅ Complete |
| **NBRC** | 2 | Japanese NITE Biological Resource Center | 🔄 Initial |
| **BacDive** | 1 | DSMZ cultivation conditions database | 🔄 Initial |

### Planned Expansions 🚀

| Source | Potential | Description | Notes |
|--------|-----------|-------------|-------|
| **BacDive** | ~2,500+ | Additional organism-specific cultivation conditions | Requires API access |
| **ATCC** | ~900 | American Type Culture Collection media | Web scraping needed |
| **NBRC** | ~420 | Additional NITE media formulations | Incremental import |

### Algae Collections (New! 🎉)

Three major algae culture collections fully integrated:

- **UTEX** (Austin, TX): 99 recipes - Full composition details
- **CCAP** (Oban, Scotland): 113 recipes - Metadata + PDF references
- **SAG** (Göttingen, Germany): 30 recipes - Metadata + PDF references

**Total**: 242 algae media recipes covering:
- Freshwater algae (BG-11, Bold's Basal, TAP)
- Marine phytoplankton (f/2, Erdschreiber's)
- Cyanobacteria (Spirulina, BG-11 variants)
- Specialized media (diatoms, euglenoids, volvocales)

See [docs/ALGAE_PIPELINE_COMPLETE.md](docs/ALGAE_PIPELINE_COMPLETE.md) for details.

### Fetching Data

```bash
# Fetch all available sources
just fetch-algae-collections    # UTEX, CCAP, SAG
just fetch-bacdive 100          # BacDive (requires registration)
just fetch-nbrc 50              # NBRC web scraping

# Import to normalized format
just import-algae-collections
just import-bacdive
just import-nbrc
```

## 🏗️ Project Structure

```
CultureMech/
├── src/culturemech/              # Python package
│   ├── schema/                   # LinkML schema definitions
│   │   └── culturemech.yaml     # Main schema (1800+ lines)
│   ├── fetch/                    # Data fetchers (10 sources)
│   │   ├── utex_fetcher.py      # UTEX algae media
│   │   ├── ccap_fetcher.py      # CCAP algae media
│   │   ├── sag_fetcher.py       # SAG algae media
│   │   └── ... (7 more fetchers)
│   ├── convert/                  # Raw YAML converters
│   ├── import/                   # Normalized importers (11 total)
│   │   ├── utex_importer.py     # Full UTEX pipeline
│   │   ├── ccap_importer.py     # CCAP metadata importer
│   │   ├── sag_importer.py      # SAG metadata importer
│   │   └── ... (8 more importers)
│   ├── export/                   # Export modules
│   │   ├── browser_export.py    # Browser data generator
│   │   └── kgx_export.py        # Knowledge graph export
│   └── render.py                 # HTML page generator
│
├── data/                         # Three-tier data architecture
│   ├── raw/                      # Layer 1: Source files (git ignored)
│   │   ├── utex/                # UTEX raw data
│   │   ├── ccap/                # CCAP raw data
│   │   ├── sag/                 # SAG raw data
│   │   └── ... (10+ sources)
│   ├── raw_yaml/                 # Layer 2: Unnormalized YAML (git ignored)
│   └── normalized_yaml/          # Layer 3: Curated recipes (in git)
│       ├── algae/               # 242 algae recipes
│       ├── bacterial/           # 10,072 bacterial recipes
│       ├── fungal/              # 119 fungal recipes
│       ├── archaea/             # 63 archaeal recipes
│       └── specialized/         # 99 specialized recipes
│
├── docs/                         # Comprehensive documentation
│   ├── QUICK_START.md           # 5-minute getting started
│   ├── DATA_LAYERS.md           # Three-tier architecture
│   ├── ALGAE_PIPELINE_COMPLETE.md  # Algae integration guide
│   └── ... (27 more docs)
│
├── app/                          # Browser interface
│   ├── index.html               # Faceted search UI
│   └── schema.js                # Browser configuration
│
├── tests/                        # Test suite
├── conf/                         # Configuration files
├── project.justfile              # Build automation (80+ commands)
└── pyproject.toml               # Python project config
```

## 📖 Documentation

Comprehensive documentation is available in the [`docs/`](docs/) directory:

### Getting Started
- **[Quick Start Guide](docs/QUICK_START.md)** - Get up and running in 5 minutes
- **[Quick Reference](docs/QUICK_REFERENCE.md)** - Command cheat sheet
- **[Contributing Guide](docs/CONTRIBUTING.md)** - How to contribute

### Architecture
- **[Data Layers](docs/DATA_LAYERS.md)** - Three-tier architecture explained
- **[Migration Guide](docs/MIGRATION_GUIDE.md)** - Directory structure reference
- **[Implementation Status](docs/IMPLEMENTATION_STATUS.md)** - Integration progress

### Integration Guides
- **[Algae Pipeline](docs/ALGAE_PIPELINE_COMPLETE.md)** - UTEX/CCAP/SAG integration (242 recipes)
- **[UTEX Deployment](docs/UTEX_PRODUCTION_DEPLOYMENT.md)** - Full UTEX pipeline details
- **[CCAP/SAG Deployment](docs/CCAP_SAG_PRODUCTION_DEPLOYMENT.md)** - Metadata import details
- **[Data Sources Summary](docs/DATA_SOURCES_SUMMARY.md)** - All source repositories

### Data Quality
- **[Enrichment Guide](docs/ENRICHMENT_GUIDE.md)** - Data quality improvement workflow

## 🧬 Recipe Format

Recipes are stored as YAML files following the LinkML schema:

```yaml
name: BG-11 Medium
category: algae
medium_type: complex
physical_state: liquid

description: Standard cyanobacteria medium from UTEX Culture Collection

ingredients:
  - agent_term:
      preferred_term: NaNO3
    amount: 1.5 g/L

  - agent_term:
      preferred_term: K2HPO4
    amount: 0.04 g/L

preparation_steps:
  - step_number: 1
    instruction: Dissolve all ingredients in distilled water

  - step_number: 2
    instruction: Autoclave at 121°C for 20 minutes

# Algae-specific fields
light_intensity: 50-100 µmol photons m⁻² s⁻¹
light_cycle: 12:12 or 16:8 light:dark
temperature_range: 15-30°C depending on species

applications:
  - Algae cultivation
  - Cyanobacteria culture
  - Phytoplankton research

curation_history:
  - curator: utex-import
    date: '2026-01-28'
    action: Imported from UTEX Culture Collection

references:
  - reference_id: UTEX:bg-11-medium
  - reference_id: https://utex.org/products/bg-11-medium
```

See [`data/normalized_yaml/`](data/normalized_yaml/) for complete examples.

## 🔬 Data Model

### LinkML Schema

The schema (`src/culturemech/schema/culturemech.yaml`) defines:

**Key Classes**:
- `MediaRecipe` - Root entity (one per YAML file)
- `IngredientDescriptor` - Chemicals with CHEBI terms
- `OrganismDescriptor` - Target organisms with NCBITaxon IDs
- `SolutionDescriptor` - Stock solutions
- `PreparationStep` - Ordered protocol steps
- `MediaVariant` - Related formulations

**Ontology Bindings**:
- **CHEBI** - Chemical ingredients
- **NCBITaxon** - Target organisms
- **UO** - Units of measurement
- **Source databases** - DSMZ, TOGO, ATCC, UTEX, CCAP, SAG

**Enums**:
- `MediumTypeEnum`: DEFINED, COMPLEX, MINIMAL, SELECTIVE, DIFFERENTIAL, ENRICHMENT
- `PhysicalStateEnum`: LIQUID, SOLID_AGAR, SEMISOLID, BIPHASIC
- `PreparationActionEnum`: DISSOLVE, MIX, HEAT, AUTOCLAVE, FILTER_STERILIZE
- `SterilizationMethodEnum`: AUTOCLAVE, FILTER, DRY_HEAT, TYNDALLIZATION

### Algae-Specific Extensions

Added fields for algae culture conditions:
- `light_intensity` - µmol photons m⁻² s⁻¹
- `light_cycle` - Photoperiod (e.g., "16:8 light:dark")
- `light_quality` - Light source type
- `temperature_range` - Cultivation temperature
- `salinity` - Marine vs freshwater
- `aeration` - CO₂ supplementation
- `culture_vessel` - Flask, tube, bioreactor

## ✅ Data Quality

### Three-Tier Architecture

```
Layer 1: raw/          → Raw source files (JSON, TSV, SQL)
         ↓
Layer 2: raw_yaml/     → Unnormalized YAML (preserves original structure)
         ↓
Layer 3: normalized_yaml/ → LinkML-validated, ontology-grounded recipes
```

**Benefits**:
- Reproducible pipeline from source to curated data
- Easy to re-import with schema changes
- Clear separation of concerns
- Version control on curated layer only

### Validation

```bash
# Full validation (schema + ontologies)
just validate data/normalized_yaml/algae/BG-11_Medium.yaml

# Schema validation only
just validate-schema data/normalized_yaml/algae/BG-11_Medium.yaml

# Validate all recipes
just validate-all
```

### Provenance

Every recipe includes:
- Source database attribution
- Fetch date and version
- Import date and curator
- Cross-references to original sources
- PDF URLs for detailed protocols (CCAP/SAG)

## 🌐 Browser Interface

The faceted search browser (`app/index.html`) provides:

- **Full-text search** - Name, organism, ingredient, application
- **Faceted filtering** - Category, type, state, organisms, sterilization
- **Real-time filtering** - Instant results from 10,595 recipes
- **External links** - CHEBI, NCBITaxon, source databases
- **Mobile responsive** - Works on all devices

Generate browser data:
```bash
just gen-browser-data
just serve-browser
# Open http://localhost:8000/app/
```

## 🔧 Development

### Common Commands

```bash
just --list              # Show all 80+ commands
just count-recipes       # Count recipes by category
just fetch-utex          # Fetch UTEX algae media
just import-utex         # Import UTEX to normalized format
just validate-all        # Validate all recipes
just gen-browser-data    # Generate browser search data
just test                # Run test suite
```

### Adding New Recipes

1. Create YAML file in appropriate category:
   ```bash
   cp data/normalized_yaml/bacterial/LB_Broth.yaml \
      data/normalized_yaml/bacterial/Your_Medium.yaml
   ```

2. Edit following schema structure

3. Validate:
   ```bash
   just validate data/normalized_yaml/bacterial/Your_Medium.yaml
   ```

4. Regenerate browser:
   ```bash
   just gen-browser-data
   ```

### Running Tests

```bash
# All tests
just test

# With coverage
just test-cov

# Specific test
pytest tests/test_kgx_export.py
```

## 🎯 Use Cases

### For Researchers
- **Find media recipes** for specific organisms
- **Compare formulations** across culture collections
- **Access detailed protocols** with preparation steps
- **Discover alternatives** through variant relationships

### For Culture Collections
- **Standardize** media recipe formats
- **Cross-reference** with other collections
- **Track provenance** and curation history
- **Export to knowledge graphs** for integration

### For Bioinformaticians
- **Query via KG** using Biolink model
- **Link organisms** to cultivation conditions
- **Analyze ingredients** with CHEBI ontology
- **Build applications** on structured data

## 📊 Statistics

```bash
$ just count-recipes
Recipe count by category:

  algae:      242
  archaea:       63
  bacterial:    10072
  fungal:      119
  specialized:       99

Total recipes:    10595
```

**Data Quality**:
- ✅ 100% schema-validated
- ✅ Full source attribution
- ✅ Comprehensive provenance tracking
- ✅ LinkML compliance

**Pipeline Coverage**:
- ✅ 10 data sources integrated
- ✅ 11 import pipelines operational
- ✅ 3 algae collections (UTEX, CCAP, SAG)
- ✅ Automated fetch → convert → import workflow

## 🤝 Contributing

We welcome contributions! Ways to contribute:

1. **Add recipes** - Create YAML files following the schema
2. **Enhance existing recipes** - Add ontology terms, preparation details
3. **Report issues** - Found errors or have suggestions?
4. **Improve documentation** - Help make guides clearer
5. **Add data sources** - Know of other culture media databases?

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

### Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Validate: `just validate-all`
5. Test: `just test`
6. Submit pull request

## 🔗 Related Resources

### Culture Collections
- **DSMZ MediaDive**: https://mediadive.dsmz.de/
- **TOGO Medium**: http://togodb.org/db/medium/
- **ATCC**: https://www.atcc.org/
- **UTEX**: https://utex.org/
- **CCAP**: https://www.ccap.ac.uk/
- **SAG**: https://sagdb.uni-goettingen.de/

### Ontologies
- **CHEBI**: https://www.ebi.ac.uk/chebi/
- **NCBITaxon**: https://www.ncbi.nlm.nih.gov/taxonomy
- **UO (Units)**: https://github.com/bio-ontology-research-group/unit-ontology

### Related Projects
- **KG-Hub**: https://github.com/Knowledge-Graph-Hub
- **LinkML**: https://linkml.io/
- **Biolink Model**: https://biolink.github.io/biolink-model/

## 📄 License

<a href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" alt="CC0" />
</a>

This work is dedicated to the public domain under [CC0 1.0 Universal](LICENSE).

**You are free to**:
- Use for any purpose
- Modify and distribute
- Use commercially
- No attribution required (but appreciated!)

## 📝 Citation

If you use CultureMech in your research, please cite:

```bibtex
@software{culturemech2026,
  title = {CultureMech: A Comprehensive Microbial Culture Media Knowledge Graph},
  author = {CultureBotAI},
  year = {2026},
  url = {https://github.com/CultureBotAI/CultureMech},
  note = {10,595 culture media recipes from 10 international repositories}
}
```

## 🙏 Acknowledgments

**Data Sources**: DSMZ, TOGO, ATCC, NBRC, BacDive, KOMODO, UTEX, CCAP, SAG, MediaDB

**Architecture**: Inspired by the [dismech](https://github.com/monarch-initiative/dismech) project

**Ontologies**: CHEBI, NCBITaxon, UO

**Community**: KG-Hub, LinkML, Biolink Model

## 📧 Contact

- **Issues**: [GitHub Issues](https://github.com/CultureBotAI/CultureMech/issues)
- **Discussions**: [GitHub Discussions](https://github.com/CultureBotAI/CultureMech/discussions)

---

**Built with ❤️ for microbiology research**

**10,595 recipes** • **10 sources** • **Production ready** • **Public domain**
