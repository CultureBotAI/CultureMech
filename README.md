# ⚗️ CultureMech

**Comprehensive Microbial Culture Media Knowledge Graph**

A production-ready knowledge base containing **10,657 culture media recipes** from 10 major international repositories, with LinkML schema validation, ontology grounding, and browser-based exploration.

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## 📊 Current Coverage

**Total Recipes**: **10,657** culture media formulations

| Category | Recipes | Sources |
|----------|---------|---------|
| **Bacterial** | 10,134 | MediaDive, TOGO, BacDive, ATCC, NBRC, KOMODO, MediaDB |
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
- Biological materials: FOODON (Food Ontology), UBERON (Anatomy), ENVO (Environment)
- Organisms: NCBITaxon (NCBI Taxonomy)
- Media databases: DSMZ, TOGO, ATCC prefixes

**Unmapped Ingredients Tracking System** (2026-03-05):
- 🎯 **136 unmapped ingredients** identified across 522 media (4.9% of total)
- 📊 **3,084 total instances** requiring ontology term mapping
- 🔍 Automated detection of numeric placeholders ('1', '2', '3'), generic terms, and empty values
- 🧪 Chemical name extraction from notes fields for mapping assistance
- 📈 Priority-based mapping recommendations (critical: 51+ occurrences)
- See [UNMAPPED_INGREDIENTS_SUMMARY.md](UNMAPPED_INGREDIENTS_SUMMARY.md) and [docs/unmapped_ingredients_guide.md](docs/unmapped_ingredients_guide.md)

**Advanced Normalization & SSSOM Enrichment** (2026-02):
- ✨ Integrated MicroMediaParam's production-grade 16-step chemical normalization pipeline
- 📚 100+ curated biological products (yeast extract, peptone, serum, DNA, agar, etc.)
- 🧪 100+ chemical formula mappings (Fe2(SO4)3 → iron(III) sulfate)
- 🔬 15+ buffer abbreviations (HEPES, MES, Tris)
- 💨 11 common laboratory gases (CO2, N2, O2, H2, CH4, etc.)
- 🔤 Unicode dot normalization (5 variants: ·, ・, •, ∙, ⋅)
- 📊 **Coverage achieved**: 45.6% (2,302 / 5,048 ingredients) - **+935 new mappings** from baseline
- 📈 **68.4% increase** in coverage (27.1% → 45.6%)
- See [PROJECT_STATUS_SUMMARY.md](PROJECT_STATUS_SUMMARY.md) and [GAS_MAPPING_SUMMARY.md](GAS_MAPPING_SUMMARY.md) for details

**Enum Normalization** (2026-02-20):
- 🔧 Normalized **10,657 YAML files** for schema compliance
- ✅ Fixed capitalization: `medium_type` (COMPLEX, DEFINED), `physical_state` (LIQUID, SOLID_AGAR)
- 📁 Recategorized all "imported" files to proper organism types (bacterial, fungal, archaea, algae, specialized)
- 🎯 **100% schema compliance** across all enum fields

## ✨ Features

✅ **10,657 recipes** - Production-ready dataset from 10 authoritative sources
✅ **Four-tier architecture** - Clean separation: raw → raw_yaml → normalized_yaml → merge_yaml
✅ **Recipe deduplication** - Merge recipes with same ingredient sets (~344 unique base formulations)
✅ **LinkML schema validation** - Comprehensive data quality enforcement
✅ **Ontology grounding** - CHEBI for chemicals, NCBITaxon for organisms
✅ **Full provenance tracking** - Complete source attribution and curation history
✅ **Automated pipelines** - Fetchers, converters, and importers for all sources
✅ **Browser interface** - Faceted search and filtering
✅ **UMAP visualization** - Interactive 2D embeddings visualization for exploring media similarity
✅ **Knowledge graph export** - Biolink-compliant KGX format
✅ **Literature verification** - 6-tier cascading PDF retrieval for cross-reference validation
✅ **ATCC cross-references** - Automated equivalency detection with DSMZ media
✅ **Unmapped ingredients tracking** - Automated detection and prioritization of ingredients needing ontology mapping
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

### Generate UMAP Visualization

```bash
# Generate interactive UMAP visualization (requires KG-Microbe embeddings)
just gen-media-umap /path/to/embeddings.tsv.gz

# View locally
open docs/media_umap.html

# See docs/MEDIA_UMAP_GUIDE.md for detailed instructions
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
│   │   ├── culturemech.yaml     # Main schema (1800+ lines)
│   │   └── unmapped_ingredients_schema.yaml  # Unmapped ingredients schema
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
├── scripts/                      # Utility scripts
│   ├── aggregate_unmapped_ingredients.py  # Aggregate unmapped ingredients
│   └── unmapped_ingredients_stats.py      # Generate statistics reports
│
├── output/                       # Generated outputs
│   └── unmapped_ingredients.yaml # Aggregated unmapped ingredients (502KB)
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

### Data Quality & Enrichment
- **[Enrichment Guide](docs/ENRICHMENT_GUIDE.md)** - Data quality improvement workflow
- **[Implementation Summary](IMPLEMENTATION_SUMMARY.md)** - Literature verification & enum normalization
- **[Unmapped Ingredients Guide](docs/unmapped_ingredients_guide.md)** - System for tracking ingredients needing ontology mapping
- **[Unmapped Ingredients Summary](UNMAPPED_INGREDIENTS_SUMMARY.md)** - Executive summary with statistics and priorities

## 🧬 Recipe Format

Recipes are stored as YAML files following the LinkML schema:

```yaml
name: BG-11 Medium
category: algae
medium_type: COMPLEX
physical_state: LIQUID

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

## 🔬 Literature Verification

**NEW** (2026-02-20): CultureMech now includes a comprehensive literature verification system for validating cross-references through scientific papers.

### 6-Tier Cascading PDF Retrieval

The system attempts to retrieve PDFs from multiple sources in order:

1. **Direct Publisher Access** - ASM, PLOS, Frontiers, MDPI, Nature, Science, Elsevier
2. **PubMed Central (PMC)** - NCBI idconv API
3. **Unpaywall API** - Open access aggregator
4. **Semantic Scholar** - Open PDF endpoint
5. **Sci-Hub Fallback** - Optional, disabled by default (requires explicit opt-in)
6. **Web Search** - arXiv, bioRxiv, Europe PMC

### Key Features

- ✅ **Legal sources first** - Always tries publisher, PMC, Unpaywall, and Semantic Scholar before fallback
- ✅ **Sci-Hub opt-in only** - Disabled by default, requires `--enable-scihub-fallback` flag
- ✅ **Full provenance** - Tracks which tier successfully retrieved each PDF
- ✅ **Evidence extraction** - 8 regex patterns for detecting media equivalencies
- ✅ **Batch processing** - Verify multiple candidates efficiently
- ✅ **Caching layer** - Metadata and PDFs cached locally to avoid repeated requests

### Usage Examples

```bash
# Generate ATCC-DSMZ cross-reference candidates (name-based matching only)
python -m culturemech.enrich.atcc_crossref_builder generate

# Verify candidates using legal sources only (no Sci-Hub)
python -m culturemech.enrich.atcc_crossref_builder generate \
    --verify-literature

# Verify with Sci-Hub fallback enabled (explicit opt-in)
python -m culturemech.enrich.atcc_crossref_builder generate \
    --verify-literature \
    --enable-scihub-fallback

# Configure via environment variables
export ENABLE_SCIHUB_FALLBACK=true
export LITERATURE_EMAIL="your@email.com"
export FALLBACK_PDF_MIRRORS="https://sci-hub.se,https://sci-hub.st"
python -m culturemech.enrich.atcc_crossref_builder generate --verify-literature
```

### Institutional Compliance

⚠️ **Important**: The Sci-Hub fallback tier is disabled by default and requires explicit opt-in. Use may violate publisher agreements or local laws. Users are responsible for compliance with institutional policies.

**Safety features:**
- Default: `use_fallback_pdf=False`
- Legal sources exhausted first
- Clear warnings when Sci-Hub is enabled
- Full provenance tracking
- No auto-distribution of PDFs

See [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) for complete documentation.

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

### Cross-Reference & Enrichment

```bash
# Generate ATCC-DSMZ cross-reference candidates
python -m culturemech.enrich.atcc_crossref_builder generate \
    --output data/curation/atcc_candidates.json

# Verify candidates via literature search (legal sources only)
python -m culturemech.enrich.atcc_crossref_builder generate \
    --verify-literature

# Verify with Sci-Hub fallback (opt-in, requires explicit flag)
python -m culturemech.enrich.atcc_crossref_builder generate \
    --verify-literature \
    --enable-scihub-fallback

# Normalize enum values (medium_type, physical_state, category)
python -m culturemech.enrich.normalize_enums --dry-run  # Preview changes
python -m culturemech.enrich.normalize_enums            # Apply changes

# Aggregate unmapped ingredients for mapping prioritization
python scripts/aggregate_unmapped_ingredients.py --verbose --min-occurrences 2

# View unmapped ingredients statistics
python scripts/unmapped_ingredients_stats.py --top 20

# View full aggregated data
less output/unmapped_ingredients.yaml

# Read the comprehensive guide
cat docs/unmapped_ingredients_guide.md

# Read the executive summary
cat UNMAPPED_INGREDIENTS_SUMMARY.md
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

  algae:        242
  archaea:       63
  bacterial:  10,134
  fungal:       119
  specialized:   99

Total recipes:  10,657
```

**Data Quality**:
- ✅ 100% schema-validated
- ✅ 100% enum compliance (10,657 files normalized)
- ✅ Full source attribution
- ✅ Comprehensive provenance tracking
- ✅ LinkML compliance

**Pipeline Coverage**:
- ✅ 10 data sources integrated
- ✅ 11 import pipelines operational
- ✅ 3 algae collections (UTEX, CCAP, SAG)
- ✅ Automated fetch → convert → import workflow

**Enrichment Features**:
- ✅ Literature verification with 6-tier PDF retrieval
- ✅ ATCC-DSMZ cross-reference detection
- ✅ Automated enum normalization
- ✅ Evidence extraction from scientific papers
- ✅ Unmapped ingredients aggregation and tracking (136 ingredients, 3,084 instances)

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

**10,657 recipes** • **10 sources** • **Production ready** • **Public domain**
