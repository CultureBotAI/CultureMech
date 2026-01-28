# CultureMech Data Sources Summary

## Overview

CultureMech integrates microbial culture media data from multiple international biological resource centers, databases, and ontologies. This document provides a high-level overview of all data sources.

**Current Status** (as of 2025-01):
- **Unique Media**: ~6,000+ recipes
- **Total Records**: ~80,000+ (including duplicates and organism associations)
- **Sources Integrated**: 3 complete, 5 in progress, 10 planned
- **Coverage**: Bacteria, Fungi, Archaea, Algae

## Data Architecture

### 3-Layer Data Pipeline

```
Layer 1: Raw Data       → Layer 2: Processed     → Layer 3: Knowledge Base
data/raw/{source}/        data/processed/          kb/media/{category}/
- Original formats        - Enriched               - CultureMech YAML
- Immutable archives     - Cross-referenced       - LinkML validated
- Full provenance        - Standardized           - Ontology-annotated
```

### Master Tracking Table

All sources are tracked in `data/MEDIA_SOURCES.tsv` with:
- Source metadata (name, URL, API endpoint)
- Record counts and data formats
- Download status and priority
- Integration notes

## Integrated Sources (Complete)

### 1. DSMZ MediaDive ✅
- **Records**: 3,327 media recipes
- **Coverage**: Bacteria, Fungi, Archaea
- **Format**: JSON via REST API
- **Status**: COMPLETE
- **Location**: `data/raw/mediadive/`
- **Primary Value**: Largest well-structured bacterial media collection
- **Integration**: Full import with CHEBI mappings

### 2. TogoMedium ✅
- **Records**: 2,917 media recipes
- **Coverage**: Bacteria, Fungi, Archaea (Japanese BRCs)
- **Format**: JSON via REST API + SPARQL
- **Status**: COMPLETE
- **Location**: `data/raw/togo/`
- **Primary Value**: Aggregates JCM, NBRC, and other Japanese sources
- **Integration**: Full import with ~900 overlaps with MediaDive

### 3. MicrobeMediaParam ✅
- **Records**: ~5,000 chemical mappings
- **Coverage**: All domains
- **Format**: TSV files
- **Status**: COMPLETE
- **Location**: `data/raw/microbe-media-param/`
- **Primary Value**: CHEBI mappings for ingredient annotation
- **Integration**: Used by all importers for chemical entity resolution

## In Progress Sources

### 4. ATCC (Partial) 🔄
- **Records**: ~300 media (manually curated)
- **Coverage**: Bacteria, Fungi, Archaea, Algae
- **Format**: HTML/PDF (no bulk API)
- **Status**: PARTIAL
- **Location**: `data/raw/atcc/`
- **Primary Value**: U.S. culture collection reference
- **Challenge**: No bulk download - manual curation required

## Priority 1 Sources (Next to Integrate)

### 5. BacDive
- **Records**: 66,570 cultivation datasets
- **Coverage**: Bacteria, Archaea
- **Format**: JSON via REST API + Python client
- **Status**: NOT_STARTED
- **Planned Location**: `data/raw/bacdive/`
- **Primary Value**: Largest cultivation dataset with organism-media associations
- **Expected New Media**: ~500 unique recipes (most reference existing DSMZ media)
- **Expected Enrichments**: 66,000+ organism-media links to existing recipes

### 6. KOMODO
- **Records**: 3,335 media variants
- **Coverage**: Bacteria (primarily E. coli and model organisms)
- **Format**: SQL database
- **Status**: NOT_STARTED
- **Planned Location**: `data/raw/komodo/`
- **Primary Value**: Standardized molar concentrations for all compounds
- **Expected New Media**: ~300 unique variants
- **Expected Enrichments**: Backfill concentrations to ~3,000 existing MediaDive recipes

### 7. MediaDB
- **Records**: 65 defined media
- **Coverage**: Bacteria (model organisms)
- **Format**: MySQL dump + TSV
- **Status**: NOT_STARTED
- **Planned Location**: `data/raw/mediadb/`
- **Primary Value**: Chemically defined media for computational biology
- **Expected New Media**: ~50-60 recipes (high overlap with existing sources)

### 8. NBRC
- **Records**: 400+ media recipes
- **Coverage**: Bacteria, Fungi, Archaea
- **Format**: HTML (web scraping)
- **Status**: NOT_STARTED
- **Planned Location**: `data/raw/nbrc/`
- **Primary Value**: Japanese BRC media not in TogoMedium
- **Expected New Media**: ~200 recipes (overlap with TOGO expected)
- **Note**: Requires ethical web scraping with rate limiting

## Priority 2 Sources (Medium-term)

### 9. JCM (Japan Collection of Microorganisms)
- **Records**: ~500 media
- **Access**: SPARQL endpoint + manual curation
- **Note**: Partially included in TogoMedium

### 10. UTEX (Algae)
- **Records**: 68 algae media
- **Access**: Web scraping (structured HTML)
- **Value**: Fills algae coverage gap

### 11. CCAP (Algae)
- **Records**: ~100 algae media
- **Access**: PDF parsing
- **Value**: UK algae collection

### 12. SAG (Algae)
- **Records**: ~30 algae media
- **Access**: Web scraping
- **Value**: German algae collection

## Priority 3 Sources (Long-term)

### 13-18. Other Collections
- NCTC (UK bacteria)
- NCIMB (UK industrial microbes)
- BioCyc/MetaCyc (subscription required)
- Additional culture collections worldwide

## Semantic/Reference Sources

### MicrO Ontology ✅
- **Classes**: 14,550 culture condition terms
- **Format**: OWL ontology
- **Use**: Semantic annotation of media properties

### MCO Ontology
- **Purpose**: Culture media classification framework
- **Format**: OWL ontology
- **Status**: Planned integration

## Expected Coverage After Full Integration

| Domain | Current | After Priority 1 | After Priority 2 | Target |
|--------|---------|------------------|------------------|--------|
| Bacteria | ~3,053 | ~5,500 | ~6,000 | ~6,500 |
| Fungi | ~114 | ~400 | ~450 | ~500 |
| Archaea | ~63 | ~200 | ~250 | ~300 |
| Algae | 0 | ~60 | ~300 | ~500 |
| Specialized | ~97 | ~200 | ~400 | ~500 |
| **Total Unique** | **~3,327** | **~6,400** | **~7,400** | **~8,300** |

## Data Quality Standards

All integrated sources must meet:

1. **Schema Validation**: 100% LinkML compliance
2. **Provenance**: Full source tracking and dates
3. **Chemical Mapping**: CHEBI IDs where possible (target >80%)
4. **Cross-referencing**: Deduplication against existing recipes
5. **Documentation**: Complete README with fetch instructions

## Integration Timeline

**Phase 1 (Weeks 1-2)**: Infrastructure + BacDive
- Create tracking table ✅
- Documentation ✅
- BacDive fetcher + importer

**Phase 2 (Week 2)**: KOMODO + MediaDB
- SQL parsers
- Concentration enrichment pipeline

**Phase 3 (Week 3)**: NBRC + validation
- Ethical web scraping
- Cross-reference deduplication

**Phase 4 (Week 4)**: Algae collections
- UTEX, CCAP, SAG integration
- Final documentation updates

## Data Governance

### Licenses
- MediaDive: CC BY 4.0
- TogoMedium: CC BY 4.0
- BacDive: CC BY 4.0
- ATCC: Fair use (limited data)
- Web-scraped sources: Cite and attribute properly

### Ethical Considerations
- Respect robots.txt for all web scraping
- Implement rate limiting (1-2s delays)
- Cache to minimize server load
- Provide proper attribution
- Contact administrators for large-scale scraping

### Data Updates
- MediaDive: Updated regularly via API
- TogoMedium: Quarterly updates recommended
- BacDive: API access allows incremental updates
- Manual sources: Update as needed

## References

- **MEDIA_SOURCES.tsv**: Master tracking table
- **MEDIA_INTEGRATION_GUIDE.md**: How to add new sources
- **Individual README files**: `data/raw/{source}/README.md`

## Contact

For questions about data sources or to suggest new integrations, open an issue on GitHub.

---

**Last Updated**: 2025-01-24
**Maintained By**: CultureMech Development Team
