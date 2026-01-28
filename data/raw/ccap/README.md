# CCAP Raw Data

**Source**: Culture Collection of Algae and Protozoa (SAMS, Scotland, UK)
**URL**: https://www.ccap.ac.uk/
**Media Recipes**: https://www.ccap.ac.uk/index.php/media-recipes/
**Date Obtained**: 2026-01-27
**Records**: ~110 media recipes
**License**: Academic/Research use
**Command**: `just fetch-ccap`

## About CCAP

The Culture Collection of Algae and Protozoa (CCAP) is one of the world's largest service collections of microalgae and protozoa. Based at the Scottish Association for Marine Science (SAMS), it maintains over 3,000 strains with ISO 9001:2015 accreditation.

## Files

- `ccap_media.json`: Complete media recipe metadata
- `fetch_stats.json`: Fetch statistics
- `pdfs/`: Downloaded PDF recipe files (if --download-pdfs used)

## Data Structure

```json
{
  "source": "CCAP",
  "source_url": "https://www.ccap.ac.uk/index.php/media-recipes/",
  "fetched_date": "2026-01-27T...",
  "count": 110,
  "pdfs_downloaded": 0,
  "recipes": [
    {
      "id": "BG11",
      "name": "BG11 (Blue-Green Medium)",
      "pdf_url": "https://www.ccap.ac.uk/wp-content/uploads/MR_BG11.pdf",
      "source": "CCAP",
      "category": "algae",
      "format": "pdf",
      "pdf_downloaded": false
    }
  ]
}
```

## Media Format

CCAP provides media recipes as PDF files following ISO quality standards. Each recipe includes:
- Chemical composition with quantities
- Preparation instructions
- Stock solution details
- Quality assurance notes (QA marked recipes)

## Fetching Data

```bash
# Fetch recipe metadata only
just fetch-ccap

# Fetch with PDF downloads (warning: downloads ~110 PDF files)
# Edit project.justfile and uncomment --download-pdfs flag

# Fetch limited set for testing
just fetch-ccap 10
```

## Next Steps

After fetching:
1. Convert to raw_yaml: `just convert-ccap-raw-yaml` (requires PDF parsing)
2. Import to normalized format: `just import-ccap`
3. Validate: `just validate normalized_yaml/algae/*.yaml`

## Notes

- Media recipes provided as professionally formatted PDF files
- Many recipes marked with (QA) indicating ISO quality assurance
- Recipes cover freshwater, marine, and specialized media
- PDFs require extraction for automated processing (not yet implemented)
- No public API available; metadata obtained via web scraping

## Common Media

Popular CCAP media include:
- **BG11**: Cyanobacteria/blue-green algae
- **f/2**: Marine phytoplankton
- **BB (Bold's Basal)**: Green algae
- **JM (Jaworski's)**: Freshwater algae
- **TAP Medium**: Chlamydomonas and relatives

## Contact

For questions about CCAP data:
- Email: ccap@sams.ac.uk
- Website: https://www.ccap.ac.uk/pages/contact
