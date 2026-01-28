# CultureMech: Next Steps & Quick Start

## 🎉 What's Been Built

### Core Infrastructure (✅ Complete)
1. **LinkML Schema** - Complete data model for media recipes
2. **2 Example Recipes** - LB Broth and M9 Minimal Medium
3. **Validation Pipeline** - 3-layer validation (schema, terms, references)
4. **KGX Export** - 7 edge types for knowledge graph
5. **Faceted Browser** - Client-side search and filtering
6. **Page Generator** - Beautiful HTML recipe pages
7. **Test Suite** - 25+ unit tests

### Import Infrastructure (✅ Ready)
1. **MediaDive Importer** - Convert 3,327 DSMZ recipes to CultureMech format
2. **Chemical Mappings** - Unified lookup using:
   - MicrobeMediaParam: 3,000+ compound mappings with CHEBI IDs
   - MediaDive: 1,235 ingredients
   - High-confidence chemical term annotations
3. **Build System** - Just targets for import, validation, export

## 🚀 Quick Start Guide

### 1. Test the Chemical Mappings

```bash
cd /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech

# Show mapping statistics
just chemical-mapping-stats

# Test specific ingredient lookup
just test-chemical-mappings "glucose"
just test-chemical-mappings "sodium chloride"
just test-chemical-mappings "yeast extract"
```

**Expected Output**:
```json
{
  "total_mappings": 3000+,
  "with_chebi_id": 2000+,
  "sources": {
    "MicrobeMediaParam": 3000+,
    "MediaDive": 1235
  }
}
```

### 2. Test MediaDive Import (Small Scale)

```bash
# Show MediaDive statistics
just import-mediadive-stats

# Import first 10 recipes (test run)
just import-mediadive 10

# Check generated files
ls kb/media/*/

# Validate imported recipes
just validate kb/media/imported/*.yaml
```

**Expected**: 10 YAML files in `kb/media/{category}/`, all passing schema validation

### 3. Full MediaDive Import (3,327 Recipes)

```bash
# Import all MediaDive recipes
just import-mediadive

# This will generate:
# - ~2,000 bacterial media in kb/media/bacterial/
# - ~800 fungal media in kb/media/fungal/
# - ~200 archaeal media in kb/media/archaea/
# - ~300 specialized media in kb/media/specialized/

# Validate all
just validate-all
```

**Estimated Time**: 10-15 minutes for full import

### 4. Generate Browser Data

```bash
# Generate browser data with all imported recipes
just gen-browser-data

# Generate HTML pages
just gen-pages

# Serve browser locally
just serve-browser

# Open http://localhost:8000/app/
```

**Expected**: Browser shows 3,300+ recipes, faceted search works

### 5. Export to Knowledge Graph

```bash
# Export all recipes to KGX format
just kgx-export

# Check output
wc -l output/kgx/*.jsonl
```

**Expected**: Thousands of edges exported

## 📊 Data Source Overview

| Source | Records | Integration | Status |
|--------|---------|-------------|--------|
| **MediaDive (DSMZ)** | 3,327 media | ✅ Ready | Importer built |
| **MicrobeMediaParam** | 3,000+ mappings | ✅ Ready | ChemicalMapper |
| **ATCC** | TBD | ⏳ Planned | Need API/scraper |
| **TOGO Medium** | ~300 | ⏳ Planned | API available |
| **NCIT** | 2 terms | ✅ Ready | Schema integrated |

## 🔄 Integration Flow

```
MediaDive MongoDB
    ↓
cmm-ai-automation/data/*.json
    ↓
MediaDiveImporter (CultureMech)
    ├→ Chemical Mappings (MicrobeMediaParam)
    ├→ ChEBI term lookup
    └→ CultureMech YAML
            ↓
        Validation (3 layers)
            ↓
        Browser + KGX Export
```

## 🛠️ Development Workflow

### Adding Enhancements

1. **Enhance Chemical Mappings**:
   - Update `chemical_mappings.py` to use composition data
   - Load `medium_composition.json` for full ingredient lists
   - Apply ChEBI terms to all ingredients

2. **Add Organism Data**:
   - Load `medium_strains.json`
   - Map strain IDs to NCBITaxon
   - Add to `target_organisms` field

3. **Expand Solutions**:
   - Parse `solution_details.json`
   - Recursively expand nested solutions
   - Add as `SolutionDescriptor` objects

### File Paths Reference

```bash
# CultureMech
/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/

# MediaDive Data
/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/cmm-ai-automation/data/

# MicrobeMediaParam Mappings
/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MicrobeMediaParam/MicroMediaParam/pipeline_output/merge_mappings/

# Key Files:
# - mediadive_media.json (3,327 records)
# - mediadive_ingredients.json (1,235 records)
# - compound_mappings_strict_final.tsv (3,000+ mappings)
# - compound_mappings_strict_final_hydrate.tsv (hydration states)
```

## 📝 Next Implementation Priorities

### Priority 1: Full Composition Import (4-6 hours)
**Goal**: Populate complete ingredient lists with ChEBI terms

**Files to Create**:
- `src/culturemech/import/composition_parser.py`
- Update `mediadive_importer.py` to use composition data

**Tasks**:
- [ ] Load `mediadive-schemas/medium_composition.json`
- [ ] Parse ingredient relationships (medium_id → ingredients)
- [ ] Apply chemical mappings from MicrobeMediaParam
- [ ] Map units to CultureMech enums
- [ ] Handle concentrations and optional ingredients

**Test Command**:
```bash
just import-mediadive-full 10  # New target with composition
just validate kb/media/imported/*.yaml
```

### Priority 2: Organism Enrichment (2-3 hours)
**Goal**: Add target organisms from strain data

**Files to Create**:
- `src/culturemech/import/organism_mapper.py`

**Tasks**:
- [ ] Load `mediadive-schemas/medium_strains.json`
- [ ] Extract medium → organism relationships
- [ ] Map organism types (B=Bacteria, F=Fungi, etc.)
- [ ] Query NCBITaxon IDs (via kg-microbe or BioRegistry)
- [ ] Add to `target_organisms` field

### Priority 3: ATCC Integration (6-8 hours)
**Goal**: Cross-reference with ATCC media database

**Research Needed**:
- Check for ATCC API availability
- Test web scraping feasibility
- Build name→ID mapping table

**Files to Create**:
- `src/culturemech/import/atcc_fetcher.py`
- `src/culturemech/import/crossref.py`

### Priority 4: TOGO Medium API (3-4 hours)
**Goal**: Integrate TOGO Medium database

**Resources**:
- API spec: `cmm-ai-automation/data/togomedium-api.yaml`
- Endpoint: http://togodb.org/db/medium/

**Files to Create**:
- `src/culturemech/import/togo_client.py`

## 🧪 Testing Strategy

### Unit Tests
```bash
# Test chemical mappings
pytest tests/test_chemical_mappings.py

# Test import logic
pytest tests/test_mediadive_importer.py

# Test KGX export
pytest tests/test_kgx_export.py
```

### Integration Tests
```bash
# Import → Validate → Export pipeline
just import-mediadive 10
just validate-all
just kgx-export
```

### QA Checklist
- [ ] All imported recipes pass schema validation
- [ ] ChEBI IDs resolve correctly (term validation)
- [ ] Browser displays all recipes
- [ ] Search and filtering work
- [ ] KGX export generates valid edges
- [ ] HTML pages render correctly

## 📚 Documentation

### For Users
- `README.md` - Overview and quick start
- `CONTRIBUTING.md` - How to add recipes
- `MEDIADIVE_IMPORT_PLAN.md` - Import architecture

### For Developers
- `IMPLEMENTATION_SUMMARY.md` - What was built
- `NEXT_STEPS.md` - This file
- Schema docs: `just gen-docs`

## 🎯 Success Metrics

### Phase 1 (Current)
- ✅ 2 example recipes validated
- ✅ Browser functional
- ✅ Import infrastructure ready

### Phase 2 (Target: 1 week)
- [ ] 3,327 MediaDive recipes imported
- [ ] 80% with full ingredient lists
- [ ] 50% with ChEBI terms
- [ ] All recipes validated

### Phase 3 (Target: 2 weeks)
- [ ] 30% with target organisms
- [ ] 30% with ATCC cross-references
- [ ] 10% with TOGO cross-references
- [ ] Preparation steps for top 100 recipes

### Phase 4 (Target: 1 month)
- [ ] Full compliance dashboard
- [ ] CI/CD pipeline
- [ ] Public browser deployment
- [ ] KG-Microbe integration

## 💡 Pro Tips

### Fast Iteration
```bash
# Test import with small dataset
just import-mediadive 5

# Quick validation
just validate-schema kb/media/imported/*.yaml

# Regenerate browser without re-importing
just gen-browser-data
```

### Debugging
```bash
# Check import logs
tail -f import.log

# Validate single file
just validate kb/media/bacterial/specific_medium.yaml

# Test KGX export standalone
python src/culturemech/export/kgx_export.py kb/media/bacterial/LB_Broth.yaml
```

### Performance
```bash
# Parallel validation (future enhancement)
find kb/media -name "*.yaml" | xargs -P 4 -I {} just validate-schema {}

# Batch processing for large imports
# Consider chunking 3,327 recipes into batches of 100
```

## 🆘 Troubleshooting

### Issue: Import fails
```bash
# Check Python dependencies
uv pip install -e .

# Verify data paths
ls /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/cmm-ai-automation/data/
```

### Issue: Validation fails
```bash
# Check schema is valid
just validate-schema-file

# Check specific error
just validate kb/media/imported/problematic.yaml
```

### Issue: Browser doesn't load
```bash
# Regenerate data
just gen-browser-data

# Check data.js exists
ls -lh app/data.js

# Check browser console for JavaScript errors
```

## 📞 Contact & Support

- **Issues**: GitHub Issues
- **Questions**: README.md or CONTRIBUTING.md
- **Architecture**: IMPLEMENTATION_SUMMARY.md
- **Import Details**: MEDIADIVE_IMPORT_PLAN.md

---

**Current Status**: ✅ Infrastructure complete, ready for bulk import
**Next Action**: `just import-mediadive 10` to test import pipeline
**Timeline**: Full import (3,327 recipes) can be done in ~30 minutes
