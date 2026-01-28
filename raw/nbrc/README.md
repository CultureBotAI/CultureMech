# NBRC Raw Data

## Source Information

- **Official Name**: NITE Biological Resource Center (NBRC)
- **URL**: https://www.nite.go.jp/en/nbrc
- **Media List**: https://www.nite.go.jp/en/nbrc/cultures/media/culture-list-e.html
- **License**: Public access (fair use with attribution)
- **Record Count**: 400+ media recipes
- **Coverage**: Bacteria, Fungi, Archaea

## What is NBRC?

NBRC is one of Japan's largest biological resource centers, providing:
- 90,000+ microbial strains
- 400+ culture media recipes
- Free public access to media formulations
- English and Japanese documentation

## Integration Strategy

### Primary Value: Japanese Media Not in TogoMedium

NBRC provides:
- **~400 media recipes** available publicly
- **~50% overlap** with TogoMedium expected (TOGO includes some NBRC data)
- **~200 unique recipes** not available in other sources
- **Japanese BRC perspective** complementing DSMZ/ATCC

### Data Quality

- Complete ingredient lists
- Preparation protocols
- Some media have pH and sterilization instructions
- Mix of defined and complex media

## Data Files

After scraping, this directory will contain:

- `nbrc_media.json` - All scraped media recipes (~400 records)
- `scrape_stats.json` - Scraping metadata (date, count)
- `scraped/` - Cached HTML pages (for verification and re-parsing)
  - `media_list.html` - Main media list page
  - `media_*.html` - Individual media recipe pages

## Ethical Scraping Guidelines

**Important**: This data is obtained via web scraping. We follow strict ethical guidelines:

### 1. Legal Compliance
- ✓ Check `robots.txt` before scraping
- ✓ No authentication bypass
- ✓ Public pages only
- ✓ Fair use for research

### 2. Technical Ethics
- ✓ 2-second delay between requests (default)
- ✓ Respectful user agent
- ✓ Caching to avoid re-scraping
- ✓ Error handling to avoid hammering server

### 3. Attribution
- ✓ Cite NBRC in all derivatives
- ✓ Preserve provenance in YAML files
- ✓ Link back to original sources

### 4. Responsible Use
- ✓ One-time scrape, not continuous monitoring
- ✓ Cache locally for analysis
- ✓ Share results openly

## Scraping Commands

### Install Dependencies

```bash
# Using uv
uv pip install requests beautifulsoup4

# Or with pip
pip install requests beautifulsoup4
```

### Scrape Data

```bash
# Test with 5 media (recommended first)
just scrape-nbrc-raw 5

# Full scrape (~400 media, takes ~15 minutes with 2s delay)
just scrape-nbrc-raw

# Custom delay (in seconds)
uv run python -m culturemech.fetch.nbrc_scraper \
    --output raw/nbrc \
    --delay 3.0
```

**Time Estimate**:
- 400 media × 2 seconds delay = ~13-15 minutes
- Includes page fetching, parsing, and caching

## Data Structure

### Scraped Media

```json
{
  "media_number": "No. 802",
  "media_name": "YPG Medium",
  "url": "https://www.nite.go.jp/en/nbrc/...",
  "ingredients": [
    {
      "name": "Yeast extract",
      "quantity": "5.0",
      "unit": "g"
    },
    {
      "name": "Peptone",
      "quantity": "5.0",
      "unit": "g"
    }
  ],
  "preparation": [
    "Dissolve ingredients in 1000 ml distilled water",
    "Adjust pH to 7.0",
    "Autoclave at 121°C for 15 minutes"
  ],
  "notes": "General purpose medium for yeasts"
}
```

## Integration with CultureMech

### Import Pipeline

1. **Scrape**: Download media recipes from NBRC website
   ```bash
   just scrape-nbrc-raw
   ```

2. **Import**: Convert to CultureMech YAML
   ```bash
   just import-nbrc
   ```

3. **Cross-reference**: Check for duplicates with TOGO
   ```bash
   just nbrc-crossref-togo  # Future feature
   ```

4. **Validate**: Ensure all recipes pass schema validation
   ```bash
   just validate-all
   ```

### Cross-Referencing with TOGO

Expected overlaps:
- NBRC media appear in TogoMedium (TOGO aggregates NBRC)
- Need fuzzy name matching to identify duplicates
- Strategy: Import unique media only

**Duplicate Detection**:
1. Exact name match with TOGO media
2. Fuzzy name matching (Levenshtein distance)
3. Ingredient composition similarity
4. Manual review of high-overlap candidates

## Provenance

**Scrape Date**: Run `cat scrape_stats.json` after scraping
**Scraper Script**: `src/culturemech/fetch/nbrc_scraper.py`
**Importer Script**: `src/culturemech/import/nbrc_importer.py`

## Known Limitations

1. **HTML Structure Changes**: Website updates may break scraper
2. **Language Barriers**: Some media have Japanese-only names
3. **Incomplete Data**: Not all media have full preparation protocols
4. **No API**: Must rely on web scraping (fragile)

## Quality Metrics

Target after integration:
- **Total scraped**: ~400 media
- **After deduplication**: ~200 unique (not in TOGO)
- **Schema validation**: 100% pass rate
- **Chemical mappings**: Target >70% ingredients with CHEBI IDs

## Verification Steps

After scraping:

```bash
# Check file sizes
ls -lh raw/nbrc/*.json

# Count recipes
jq 'length' raw/nbrc/nbrc_media.json

# Sample inspection
jq '.[0]' raw/nbrc/nbrc_media.json

# Check cached pages
ls raw/nbrc/scraped/ | wc -l
```

## Troubleshooting

### Scraper fails with 403/404
- Website structure may have changed
- Check URL in browser first
- Update selectors in `nbrc_scraper.py`

### Missing ingredients
- Some media may not have full recipes
- Log warnings for incomplete data
- Skip or create minimal recipe

### Encoding issues (Japanese characters)
- Ensure UTF-8 encoding
- Python 3 handles Unicode well
- Check BeautifulSoup parser

## Alternative Sources

If web scraping fails, alternatives:
1. **TogoMedium**: Already includes some NBRC data
2. **Manual curation**: Download individual PDFs
3. **Contact NBRC**: Request bulk data export

## References

- **NBRC Homepage**: https://www.nite.go.jp/en/nbrc
- **Media List**: https://www.nite.go.jp/en/nbrc/cultures/media/culture-list-e.html
- **Terms of Use**: https://www.nite.go.jp/en/nbrc/terms.html
- **Contact**: nbrc-info@nite.go.jp

## Citation

When using NBRC data, cite:
```
NITE Biological Resource Center (NBRC), National Institute of Technology
and Evaluation (NITE), Japan. Media recipes accessed from
https://www.nite.go.jp/en/nbrc/cultures/media/culture-list-e.html
```

---

**Last Updated**: 2025-01-24
**Status**: NOT_STARTED (awaiting scraping)
