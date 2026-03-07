# Culture Media UMAP Visualization Guide

## Overview

The UMAP (Uniform Manifold Approximation and Projection) visualization provides an interactive way to explore culture media recipes through semantic similarity. Media with similar ingredients, organisms, or purposes cluster together in 2D space, making it easy to discover related formulations and identify patterns.

## What is UMAP?

UMAP is a dimensionality reduction technique that maps high-dimensional embeddings (512D vectors from KG-Microbe) to 2D coordinates while preserving local and global structure. Points that are close together in 2D space represent media with similar semantic properties.

## Two Visualization Approaches

### 1. Derived Media Embeddings

**Method**: Aggregates ingredient (CHEBI) and organism (NCBITaxon) embeddings from the knowledge graph to create media-level vectors.

**Aggregation Strategy**:
- Extract CHEBI IDs from ingredients
- Extract NCBITaxon IDs from target organisms
- Lookup embeddings for each component
- Weighted mean pooling: `0.6 × ingredient_mean + 0.4 × organism_mean`
- Only include media with ≥50% component coverage

**Coverage**: ~8,000-9,000 media (out of 10,657 total)

**Advantages**:
- Works for any media with ontology-grounded ingredients/organisms
- Captures composition-based similarity
- Transparent aggregation logic

**Use Cases**:
- Finding media with similar ingredient profiles
- Identifying formulation alternatives
- Discovering composition patterns

### 2. Direct Media Embeddings

**Method**: Uses pre-computed `mediadive.medium` node embeddings directly from KG-Microbe.

**Coverage**: 3,343 DSMZ media (from MediaDive database)

**Advantages**:
- Captures full semantic context from knowledge graph structure
- Includes relationships beyond just ingredients/organisms
- Higher-quality embeddings from graph neural network training

**Use Cases**:
- Exploring DSMZ/MediaDive media relationships
- Validating derived embeddings
- Discovering knowledge graph patterns

## Interactive Features

### Visualization

- **Scatter Plot**: Each point represents one medium
- **Colors**: Categorical coloring by media category (bacterial, algae, fungal, etc.)
- **Size**: Fixed size for clarity
- **Opacity**: Semi-transparent to show overlapping clusters

### Interactions

1. **Zoom/Pan**: Use mouse wheel to zoom, drag to pan
2. **Hover**: Shows tooltip with metadata:
   - Name
   - Category
   - Medium type (complex, defined, minimal)
   - Physical state (liquid, solid_agar)
   - Number of ingredients
   - Number of organisms
   - Coverage (derived only)
   - Source database
3. **Click**: Navigates to detailed recipe page
4. **Search**: Filter by media name in real-time

### Legend

- Shows category distribution with counts
- Color-coded to match plot points
- Updates based on visible points

## Interpreting the Visualization

### Cluster Patterns

**Tight clusters** indicate:
- Similar ingredient compositions
- Common target organisms
- Shared functional purposes
- Related formulation approaches

**Separated points** indicate:
- Unique or specialized formulations
- Novel ingredient combinations
- Different functional categories

### Expected Clusters

You should observe separation by:
- **Category**: bacterial vs algae vs fungal media form distinct regions
- **Medium type**: complex vs defined vs minimal media
- **Ingredient richness**: nutrient-rich vs minimal media
- **Specialization**: general-purpose vs selective media

## How to Use

### Generate Visualization

```bash
# Using justfile (recommended)
just gen-media-umap

# Or with custom embeddings path
just gen-media-umap /path/to/embeddings.tsv.gz

# With custom parameters
just gen-media-umap-custom /path/to/embeddings.tsv.gz 30 0.05 0.3
```

### CLI Commands

```bash
# Basic usage
uv run culturemech umap generate \
    --embeddings-path /path/to/embeddings.tsv.gz \
    --output docs/media_umap.html

# With custom UMAP parameters
uv run culturemech umap generate \
    --embeddings-path /path/to/embeddings.tsv.gz \
    --n-neighbors 30 \
    --min-dist 0.05 \
    --min-coverage 0.3 \
    --force-reload
```

### View Locally

```bash
# Start local server
just serve-browser

# Open in browser
open http://localhost:8000/docs/media_umap.html

# Or directly
open docs/media_umap.html
```

### Deploy to GitHub Pages

```bash
git add docs/media_umap.html
git commit -m "Add UMAP visualization"
git push origin main
```

Access at: `https://kg-hub.github.io/CultureMech/media_umap.html`

## Parameters

### UMAP Parameters

**n_neighbors** (default: 15)
- Controls local vs global structure
- Lower values: emphasize local structure, tighter clusters
- Higher values: emphasize global structure, better separation
- Range: 5-50

**min_dist** (default: 0.1)
- Controls cluster compactness
- Lower values: tighter, more compact clusters
- Higher values: looser, more spread out points
- Range: 0.0-1.0

**min_coverage** (default: 0.5)
- Minimum fraction of components with embeddings (derived only)
- Lower values: include more media with partial coverage
- Higher values: only high-confidence aggregations
- Range: 0.0-1.0

### When to Adjust Parameters

**Increase n_neighbors** (e.g., 30) when:
- Plot looks too fragmented
- Want better global separation
- Have many media (>5000)

**Decrease n_neighbors** (e.g., 10) when:
- Want to emphasize local relationships
- Have fewer media (<1000)

**Decrease min_dist** (e.g., 0.05) when:
- Clusters are too spread out
- Want tighter groupings

**Increase min_dist** (e.g., 0.2) when:
- Clusters overlap too much
- Want better separation

**Decrease min_coverage** (e.g., 0.3) when:
- Want to include more media
- Accept partial ingredient coverage

## Performance

### Generation Time

| Step | First Run | Cached |
|------|-----------|--------|
| Load embeddings | 90-120s | 5s |
| Aggregate media | 20-30s | 20-30s |
| UMAP reduction | 20-30s | 20-30s |
| HTML generation | 5s | 5s |
| **Total** | **2-3 min** | **1 min** |

### File Sizes

- Cache directory: ~2.5GB (gitignored)
- Output HTML: ~300-500KB (committed)

### Caching

Embeddings are cached as pickle files in `.umap_cache/`:
- `CHEBI_FOODON_mediadive.medium_NCBITaxon_embeddings.pkl`

Cache is automatically used on subsequent runs. Use `--force-reload` to bypass.

## Technical Details

### Embedding Sources

**KG-Microbe Embeddings**:
- Algorithm: DeepWalk with SkipGram
- Dimensions: 512
- Training: Degree-normalized random walks
- Nodes: 882,939 NCBITaxon + 204,736 CHEBI + 3,343 mediadive.medium

**Node Types**:
- `CHEBI:*` - Chemical ingredients
- `FOODON:*` - Biological material ingredients
- `NCBITaxon:*` - Target organisms
- `mediadive.medium:DSMZ_*` - Direct media nodes

### Aggregation Algorithm

```python
# For each medium:
1. Extract ingredient IDs (CHEBI/FOODON)
2. Extract organism IDs (NCBITaxon)
3. Lookup embeddings for each ID
4. Calculate coverage = found / total
5. If coverage >= min_coverage:
   - ingredient_mean = mean(ingredient_embeddings)
   - organism_mean = mean(organism_embeddings)
   - media_vector = 0.6 * ingredient_mean + 0.4 * organism_mean
```

### Color Scheme

Uses consistent category colors from `app/schema.js`:
- Bacterial: Blue (#3b82f6)
- Fungal: Purple (#8b5cf6)
- Archaea: Orange (#f59e0b)
- Algae: Green (#10b981)
- Specialized: Indigo (#6366f1)

## Troubleshooting

### "No such file or directory: embeddings.tsv.gz"

**Solution**: Provide correct path to KG-Microbe embeddings:
```bash
just gen-media-umap /path/to/embeddings.tsv.gz
```

### "No media with sufficient coverage"

**Cause**: min_coverage too high or embeddings missing

**Solution**: Lower min_coverage or check embeddings contain CHEBI/NCBITaxon nodes:
```bash
just gen-media-umap-custom /path/to/embeddings.tsv.gz 15 0.1 0.3
```

### Very sparse plot

**Cause**: n_neighbors too low or insufficient data

**Solution**: Increase n_neighbors:
```bash
just gen-media-umap-custom /path/to/embeddings.tsv.gz 30 0.1 0.5
```

### Plot too compact

**Cause**: min_dist too low

**Solution**: Increase min_dist:
```bash
just gen-media-umap-custom /path/to/embeddings.tsv.gz 15 0.2 0.5
```

## Future Enhancements

Potential improvements for future versions:

1. **Multi-panel comparison**: Side-by-side derived vs direct
2. **Faceting**: Separate plots by category
3. **3D visualization**: Interactive 3D UMAP with three.js
4. **Temporal evolution**: Animate how embeddings change over time
5. **Ingredient highlighting**: Show media with specific ingredients
6. **Cluster analysis**: Automatic cluster detection and labeling
7. **Similarity search**: Click one medium to find similar ones
8. **Export functionality**: Save filtered subsets or cluster assignments

## References

- **UMAP Algorithm**: McInnes, L., Healy, J., & Melville, J. (2018). UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction. arXiv:1802.03426
- **KG-Microbe**: Knowledge graph of microbial life
- **DeepWalk**: Perozzi, B., Al-Rfou, R., & Skiena, S. (2014). DeepWalk: Online Learning of Social Representations. KDD 2014.

## Questions?

For issues or feature requests, please open an issue on the GitHub repository.
