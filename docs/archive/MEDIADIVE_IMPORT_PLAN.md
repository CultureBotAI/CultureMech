# MediaDive Import Plan for CultureMech

## Overview

Import 3,327 media recipes from MediaDive MongoDB into CultureMech format, with cross-referencing to ATCC, NCIT, and TOGO Medium databases.

## Data Sources

### Primary: MediaDive (DSMZ)
- **Location**: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/cmm-ai-automation/data/`
- **Source**: MongoDB collections exported to JSON
- **Records**: 3,327 media recipes
- **Components**:
  - `mediadive_media.json` - Media metadata
  - `mediadive_ingredients.json` - 1,235 ingredients (some with ChEBI IDs)
  - `mediadive_solutions.json` - 1,514 solutions
  - `mediadive-schemas/medium_composition.json` - Ingredient relationships
  - `mediadive-schemas/medium_strains.json` - Organism growth data

**Statistics**:
- Defined media: 660 (20%)
- Complex media: 2,667 (80%)
- pH distribution: Peak at pH 7 (1,501 recipes)
- Source: DSMZ MediaDive database

### Secondary: ATCC Media Database
- **URL**: https://www.atcc.org/
- **Approach**: Web scraping or API (if available)
- **Integration**: Cross-reference ATCC IDs with MediaDive records

### Tertiary: TOGO Medium
- **API**: http://togodb.org/db/medium/
- **File**: `togomedium-api.yaml` already available in cmm-ai-automation
- **Records**: ~several hundred media
- **Integration**: API queries for enrichment

### Quaternary: NCI Thesaurus (NCIT)
- **Focus**: C64371 (Complex Medium), C64372 (Defined Medium)
- **Approach**: Use existing NCIT ontology terms for medium_type classification

## Implementation Phases

### Phase 1: Basic MediaDive Import (Current)

**Status**: ✅ Implemented in `src/culturemech/import/mediadive_importer.py`

**Features**:
- Load MediaDive JSON exports
- Convert to CultureMech YAML schema
- Auto-categorize (bacterial/fungal/archaea/specialized)
- Map medium types (COMPLEX/DEFINED)
- Extract pH values
- Link to DSMZ database
- Generate curation history

**Limitations**:
- Ingredients not yet populated (needs medium_composition integration)
- Organism targets not extracted (needs medium_strains data)
- ChEBI mappings not applied
- Solutions not expanded

**Output**: 3,327 YAML files in `kb/media/{category}/`

### Phase 2: Full Composition Import (Next)

**Goal**: Populate complete ingredient lists with concentrations and ChEBI terms

**Data Flow**:
```
mediadive-schemas/medium_composition.json
    ↓
  medium_id → [ingredient_id, amount, unit]
    ↓
mediadive_ingredients.json
    ↓
  ingredient_id → {name, ChEBI, CAS-RN, PubChem}
    ↓
CultureMech IngredientDescriptor
```

**Implementation**:
```python
def get_medium_composition(medium_id: int) -> list[dict]:
    """
    Extract full ingredient list for a medium.

    Returns:
        [
            {
                "preferred_term": "Glucose",
                "term": {"id": "CHEBI:17234", "label": "D-glucose"},
                "concentration": {"value": "10", "unit": "G_PER_L"}
            },
            ...
        ]
    """
```

**Tasks**:
- [ ] Load `medium_composition.json` schema
- [ ] Parse nested JSON structure
- [ ] Map units to CultureMech enums
- [ ] Apply ChEBI mappings where available
- [ ] Handle missing ingredients gracefully

### Phase 3: Organism Enrichment

**Goal**: Add target organisms from medium_strains data

**Data Flow**:
```
mediadive-schemas/medium_strains.json
    ↓
  medium_id → [strain_id, growth_type]
    ↓
NCBITaxon lookup (via kg-microbe?)
    ↓
CultureMech OrganismDescriptor
```

**Growth Types** (from mediadive_stats.json):
- B = Bacteria (54,795 growth records)
- F = Fungi (6,794 records)
- Y = Yeast (5,880 records)
- A = Archaea (1,386 records)
- AL = Algae (2,190 records)
- P = Protozoa (748 records)
- PH = Phage (747 records)

**Implementation**:
- Extract strain→medium relationships
- Map strain IDs to NCBITaxon via BacDive or kg-microbe
- Add to `target_organisms` field

### Phase 4: Solution Expansion

**Goal**: Expand stock solutions into full composition

**Challenge**: Solutions can reference other solutions (5 levels deep, 42% recursive)

**Approach**:
- Use flattened `medium_composition` data (already resolved by cmm-ai-automation)
- OR: Recursively expand solutions up to depth limit
- Store as nested `SolutionDescriptor` in YAML

### Phase 5: Cross-Reference to ATCC

**Data Sources**:
1. **ATCC Website** - https://www.atcc.org/products/all
2. **Potential API** - Check for REST endpoints
3. **Fallback** - Manual curation for high-value media

**Mapping Strategy**:
- Match by medium name (fuzzy matching)
- Match by composition similarity
- Manual review for ambiguous cases

**Output**: Enrich `media_term` with ATCC IDs where available

### Phase 6: TOGO Medium Integration

**API**: http://togodb.org/db/medium/

**File**: `togomedium-api.yaml` (OpenAPI spec)

**Implementation**:
```python
import requests

def fetch_togo_medium(medium_id: str) -> dict:
    """Fetch medium from TOGO API."""
    url = f"http://togodb.org/db/medium/{medium_id}"
    response = requests.get(url)
    return response.json()

def find_togo_matches(medium_name: str) -> list[str]:
    """Search TOGO for matching media by name."""
    # Implement search logic
    pass
```

**Tasks**:
- Parse OpenAPI spec from `togomedium-api.yaml`
- Implement API client
- Add TOGO IDs to `media_term`
- Enrich with TOGO-specific metadata

### Phase 7: Validation and Quality Control

**Validation Layers**:
1. **Schema Validation**: `just validate-schema`
2. **Term Validation**: Verify ChEBI, NCBITaxon IDs
3. **Cross-Reference Validation**: Check DSMZ, ATCC, TOGO links
4. **Completeness Scoring**: Port compliance dashboard from dismech

**Quality Metrics**:
- % recipes with full ingredient lists
- % recipes with ChEBI terms
- % recipes with target organisms
- % recipes with multiple database IDs
- % recipes with preparation steps

**Target**: 80%+ completeness for all fields

### Phase 8: Enrichment and Curation

**AI-Assisted Enrichment**:
- Use Claude Code to suggest:
  - Missing preparation steps
  - Standard sterilization methods
  - Common applications
  - Variant recipes

**Human Curation**:
- Review high-value media (LB, TSB, etc.)
- Add detailed protocols
- Link to literature (PMIDs)
- Add evidence items

## Build System Integration

**New Justfile Targets**:

```makefile
[group('Import')]
import-mediadive limit="":
    #!/usr/bin/env bash
    echo "Importing MediaDive recipes..."
    uv run python -m culturemech.import.mediadive_importer \
        -i /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/cmm-ai-automation/data \
        -o kb/media \
        {{if limit != "" { "--limit " + limit } else { "" } }}

[group('Import')]
import-mediadive-stats:
    #!/usr/bin/env bash
    uv run python -m culturemech.import.mediadive_importer \
        -i /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/cmm-ai-automation/data \
        --stats

[group('Import')]
import-atcc:
    #!/usr/bin/env bash
    echo "Importing ATCC media..."
    uv run python -m culturemech.import.atcc_importer

[group('Import')]
import-togo:
    #!/usr/bin/env bash
    echo "Importing TOGO Medium..."
    uv run python -m culturemech.import.togo_importer

[group('Import')]
crossref-all:
    #!/usr/bin/env bash
    echo "Cross-referencing all databases..."
    uv run python -m culturemech.import.crossref

[group('Import')]
import-all: import-mediadive import-atcc import-togo crossref-all
    #!/usr/bin/env bash
    echo "✓ All imports complete!"
    just validate-all
```

## File Organization

After full import:

```
kb/media/
├── bacterial/           # ~2,000 recipes
│   ├── LB_Broth.yaml
│   ├── DSMZ_Medium_1.yaml
│   └── ...
├── fungal/              # ~800 recipes
│   ├── Potato_Dextrose_Agar.yaml
│   └── ...
├── archaea/             # ~200 recipes
├── specialized/         # ~300 recipes
└── imported/            # Uncategorized imports
```

## Database Cross-Reference Matrix

| Database | Prefix | Count | Coverage | Status |
|----------|--------|-------|----------|--------|
| DSMZ MediaDive | DSMZ | 3,327 | 100% | ✅ Ready |
| ATCC | ATCC | TBD | ~30%? | ⏳ Planned |
| TOGO Medium | TOGO | ~300? | ~10%? | ⏳ Planned |
| NCIT | NCIT | 2 | 100% | ✅ Schema ready |

## Success Criteria

### Phase 1 (MVP)
- [x] Import all 3,327 MediaDive recipes
- [x] Auto-categorize by organism type
- [x] Link to DSMZ database
- [x] Generate valid YAML files
- [ ] Test with `just import-mediadive --limit 10`

### Phase 2 (Full Import)
- [ ] Complete ingredient lists (80%+ coverage)
- [ ] ChEBI term mappings (50%+ coverage)
- [ ] Target organisms (30%+ coverage)
- [ ] Pass schema validation

### Phase 3 (Cross-Referenced)
- [ ] ATCC IDs for 30% of recipes
- [ ] TOGO IDs for 10% of recipes
- [ ] Multiple database IDs for 40% of recipes

### Phase 4 (Production)
- [ ] All recipes validated
- [ ] Browser integrated
- [ ] KGX export working
- [ ] Documentation complete

## Timeline Estimate

- **Phase 1**: 1-2 hours (DONE)
- **Phase 2**: 4-6 hours (composition parsing)
- **Phase 3**: 2-3 hours (organism enrichment)
- **Phase 4**: 3-4 hours (solution expansion)
- **Phase 5**: 6-8 hours (ATCC integration)
- **Phase 6**: 3-4 hours (TOGO API)
- **Phase 7**: 2-3 hours (validation)
- **Phase 8**: Ongoing (curation)

**Total**: ~25-35 hours for full implementation

## Next Steps

1. **Test basic import** (Phase 1):
   ```bash
   just import-mediadive --limit 10
   just validate kb/media/imported/*.yaml
   ```

2. **Implement composition parsing** (Phase 2):
   - Load `medium_composition.json` from cmm-ai-automation
   - Parse nested structure
   - Map to IngredientDescriptor

3. **Add organism enrichment** (Phase 3):
   - Load `medium_strains.json`
   - Query NCBITaxon via kg-microbe or BioRegistry

4. **Start ATCC research**:
   - Check for ATCC API
   - Test web scraping approach
   - Build mapping table

## Integration with cmm-ai-automation

**Reusable Components**:
- MediaDive MongoDB client (`mediadive_mongodb.py`)
- KGX export logic (`export_mediadive_kgx.py`)
- ChEBI mappings (from `mediadive_ingredients.json`)
- Organism mappings (from kg-microbe integration)

**Data Dependencies**:
- Read-only access to MediaDive JSON exports
- No modifications to cmm-ai-automation codebase
- CultureMech operates as downstream consumer

## References

- **cmm-ai-automation**: https://github.com/CultureBotAI/CMM-AI
- **MediaDive**: https://mediadive.dsmz.de/
- **ATCC**: https://www.atcc.org/
- **TOGO Medium**: http://togodb.org/db/medium/
- **NCIT**: https://ncit.nci.nih.gov/

---

**Status**: Phase 1 implemented, ready for testing
**Next Action**: `just import-mediadive --limit 10`
