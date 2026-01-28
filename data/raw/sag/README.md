# SAG Raw Data

**Source**: Sammlung von Algenkulturen Göttingen (Culture Collection of Algae at Göttingen University)
**URL**: https://sagdb.uni-goettingen.de/
**Media Recipes**: https://www.uni-goettingen.de/de/186449.html
**Date Obtained**: 2026-01-27
**Records**: ~45 media recipes
**License**: Academic/Research use
**Command**: `just fetch-sag`

## About SAG

SAG is one of the oldest and largest algal culture collections in the world, established in 1954 at the University of Göttingen, Germany. It maintains approximately 2,300 strains representing all major algal groups and cyanobacteria.

## Files

- `sag_media.json`: Complete media recipe metadata
- `fetch_stats.json`: Fetch statistics
- `pdfs/`: Downloaded PDF recipe files (if --download-pdfs used)

## Data Structure

```json
{
  "source": "SAG",
  "source_url": "https://www.uni-goettingen.de/de/186449.html",
  "fetched_date": "2026-01-27T...",
  "count": 45,
  "pdfs_downloaded": 0,
  "recipes": [
    {
      "id": "BG_11",
      "name": "BG 11",
      "pdf_url": "http://sagdb.uni-goettingen.de/culture_media/20 BG11 Medium.pdf",
      "filename": "20 BG11 Medium.pdf",
      "source": "SAG",
      "category": "algae",
      "format": "pdf"
    }
  ]
}
```

## Media Format

SAG provides media recipes as PDF files with detailed formulations including:
- Chemical composition
- Preparation procedures
- pH adjustments
- Autoclavesterilization instructions

## Fetching Data

```bash
# Fetch recipe metadata only
just fetch-sag

# Fetch with PDF downloads (warning: downloads ~45 PDF files)
# Edit project.justfile and uncomment --download-pdfs flag

# Fetch limited set for testing
just fetch-sag 10
```

## Next Steps

After fetching:
1. Convert to raw_yaml: `just convert-sag-raw-yaml` (requires PDF parsing)
2. Import to normalized format: `just import-sag`
3. Validate: `just validate normalized_yaml/algae/*.yaml`

## Notes

- Media recipes numbered (e.g., "20 BG11 Medium.pdf")
- Comprehensive formulations for diverse algal groups
- PDFs hosted on SAG database server
- PDF extraction required for automated processing (not yet implemented)
- No public API available; metadata obtained via web scraping
- Rate limiting applied to respect server resources

## Common Media

Core SAG media include:
- **BG 11**: Cyanobacteria
- **3N-BBM+V**: Bold's Basal with vitamins
- **f/2**: Enriched seawater
- **WC**: Woods Hole MBL medium
- **Spirul**: Spirulina medium

## Database

SAG maintains a comprehensive online database at https://sagdb.uni-goettingen.de/ with:
- Strain catalogue
- Taxonomic information
- Culture conditions
- Media recommendations

## Contact

For questions about SAG data:
- Email: epsag@uni-goettingen.de
- Website: https://www.uni-goettingen.de/de/45175.html
