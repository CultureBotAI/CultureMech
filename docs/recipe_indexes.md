# Recipe Index Files

**Purpose**: Catalog all recipes with searchable metadata
**Script**: `scripts/generate_recipe_indexes.py`
**Location**: Generated in the same directory as recipes

---

## Generated Index Files

### Master Index (`recipe_index.json`)
Complete catalog of all recipes with full metadata

**Structure**:
```json
{
  "generated": "2026-03-15T04:14:54Z",
  "total_recipes": 10657,
  "categories": {
    "bacterial": {"count": 10134, "index_file": "bacterial_index.json"},
    "algae": {"count": 242, "index_file": "algae_index.json"},
    ...
  },
  "recipes": {
    "CultureMech:000001": {
      "name": "LB Broth",
      "filename": "LB_Broth.yaml",
      "ingredient_count": 3,
      "source": "TOGO",
      "categories": ["bacterial"],
      ...
    }
  }
}
```

### Category Indexes (`{category}_index.json`)
Recipes grouped by organism type (bacterial, algae, archaea, fungal, specialized)

**Example**: `bacterial_index.json`, `algae_index.json`

### Source Indexes (`by_source_{source}_index.json`)
Recipes grouped by originating database

**Examples**:
- `by_source_togo_index.json` - 2,917 TOGO recipes
- `by_source_mediadive_index.json` - 3,327 MediaDive recipes
- `by_source_komodo_index.json` - 3,637 KOMODO recipes

### Statistics (`recipe_statistics.json`)
High-level statistics and breakdowns

**Structure**:
```json
{
  "total_recipes": 10657,
  "by_source": {
    "KOMODO": 3637,
    "MediaDive": 3327,
    "TOGO": 2917
  },
  "by_category": {
    "bacterial": 10134,
    "algae": 242,
    ...
  },
  "ingredient_statistics": {
    "min": 0,
    "max": 96,
    "avg": 14.2
  }
}
```

---

## Usage

### Generate Indexes (just commands)

```bash
# Generate for normalized recipes
just generate-indexes

# Generate for merged recipes
just generate-indexes data/merge_yaml/merged_2026

# Generate for all collections
just generate-all-indexes
```

### Direct Script Usage

```bash
source .venv/bin/activate

# Default (normalized_yaml)
python scripts/generate_recipe_indexes.py

# Specific directory
python scripts/generate_recipe_indexes.py \
  --recipe-dir data/merge_yaml/merged_2026

# Custom output location
python scripts/generate_recipe_indexes.py \
  --recipe-dir data/normalized_yaml \
  --output-dir indexes/

# Master index only (faster)
python scripts/generate_recipe_indexes.py --master-only

# Statistics only (requires existing indexes)
python scripts/generate_recipe_indexes.py --stats-only
```

---

## Metadata Fields

Each recipe entry includes:

| Field | Description | Example |
|-------|-------------|---------|
| `name` | Recipe name | "LB Broth" |
| `filename` | YAML file name | "LB_Broth.yaml" |
| `id` | CultureMech ID (if assigned) | "CultureMech:000001" |
| `source_id` | Original database ID | "TOGO:M3236" |
| `source` | Source database | "TOGO" |
| `ingredient_count` | Number of ingredients | 3 |
| `solution_count` | Number of solutions (if any) | 2 |
| `categories` | Recipe categories | ["bacterial"] |
| `organism_culture_type` | Pure/mixed culture | "PURE_CULTURE" |
| `merged_from_count` | If merged, source count | 5 |
| `merged_sources` | If merged, source list | ["TOGO", "MediaDive"] |
| `has_hierarchy_enrichment` | Has MIM enrichment | true |
| `category_dir` | Directory location | "bacterial" |

---

## Use Cases

### 1. Browse Recipes

```bash
# View all bacterial recipes
jq '.recipes | to_entries[] | select(.value.categories[] == "bacterial") | .value.name' \
  data/normalized_yaml/recipe_index.json
```

### 2. Find Recipes by Source

```bash
# All TOGO recipes
jq '.recipes | length' data/normalized_yaml/by_source_togo_index.json

# List TOGO recipe names
jq '.recipes[].name' data/normalized_yaml/by_source_togo_index.json
```

### 3. Statistics

```bash
# View recipe statistics
cat data/normalized_yaml/recipe_statistics.json | jq
```

### 4. API Development

Use indexes as data source for API endpoints:
```python
import json

# Load master index
with open('data/normalized_yaml/recipe_index.json') as f:
    index = json.load(f)

# Get recipe by ID
recipe_meta = index['recipes']['CultureMech:000001']

# Search by name
matches = [
    r for r in index['recipes'].values()
    if 'LB' in r['name']
]
```

### 5. Documentation

Generate recipe catalogs for documentation:
```bash
# List all categories with counts
jq '.categories' data/normalized_yaml/recipe_index.json
```

---

## Performance

**Indexing 10,657 recipes**:
- Time: ~30 seconds
- Master index: ~4 MB
- Category indexes: ~500 KB each
- Total disk space: ~10 MB

**Recommendation**: Regenerate indexes after:
- Adding new recipes
- Running cleanup pipeline
- Merging recipes
- Enrichment updates

---

## Integration

### In Pipeline

```bash
# After normalization
just normalize-all
just generate-indexes

# After merging
just merge-recipes
just generate-indexes data/merge_yaml/merged_2026

# After enrichment
just enrich-all
just generate-indexes
```

### Automated

Add to your workflow:
```bash
#!/bin/bash
# Process new data
just normalize-all
just fix-all-data-quality
just generate-indexes  # ← Generate fresh indexes
just merge-recipes
just generate-indexes data/merge_yaml/merged_2026  # ← Index merged recipes
```

---

## File Locations

### Normalized Recipes
```
data/normalized_yaml/
├── recipe_index.json          # Master index
├── recipe_statistics.json     # Statistics
├── algae_index.json          # Category index
├── bacterial_index.json      # Category index
├── by_source_togo_index.json # Source index
└── ...
```

### Merged Recipes
```
data/merge_yaml/merged_2026/
├── recipe_index.json          # Master index (merged)
├── recipe_statistics.json     # Statistics (merged)
└── ...
```

---

## Index Updates

Indexes are **static snapshots**. Regenerate after changes:

```bash
# Data changed? Regenerate
just generate-indexes

# Check freshness
jq '.generated' data/normalized_yaml/recipe_index.json
```

---

## Advanced Queries

### Find recipes with most ingredients

```bash
jq '.recipes | to_entries | sort_by(.value.ingredient_count) | reverse | .[0:10] | .[] | {name: .value.name, count: .value.ingredient_count}' \
  data/normalized_yaml/recipe_index.json
```

### Find merged recipes

```bash
jq '.recipes | to_entries[] | select(.value.merged_from_count > 1) | .value' \
  data/merge_yaml/merged_2026/recipe_index.json
```

### Count by source

```bash
jq '.by_source' data/normalized_yaml/recipe_statistics.json
```

---

## Related

- **Generate**: `just generate-indexes`
- **All indexes**: `just generate-all-indexes`
- **Statistics only**: `python scripts/generate_recipe_indexes.py --stats-only`
