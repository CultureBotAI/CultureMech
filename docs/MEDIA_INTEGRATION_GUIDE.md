# Media Source Integration Guide

This guide explains how to integrate new media data sources into CultureMech.

## Overview

Adding a new media source involves 4 steps:

1. **Tracking** - Add source to `MEDIA_SOURCES.tsv`
2. **Fetching** - Create fetcher to download raw data
3. **Importing** - Create importer to convert to CultureMech schema
4. **Building** - Add commands to `project.justfile`

## Step 1: Add to MEDIA_SOURCES.tsv

Before starting integration, document the source:

```tsv
source_id	source_name	url	api_url	record_count	data_format	access_method	priority
NEWSOURCE	New Source Database	https://...	https://api...	1000	JSON	REST API	1
```

Key fields:
- `source_id`: Short uppercase identifier (used in code)
- `download_status`: NOT_STARTED → IN_PROGRESS → COMPLETE
- `priority`: 1 (highest) to 5 (lowest)

## Step 2: Create Fetcher

### 2A. For API-based sources

Create `src/culturemech/fetch/{source}_fetcher.py`:

```python
"""
{Source Name} API fetcher.

Fetches media data from {Source} API/database.
"""

import argparse
import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class {Source}Fetcher:
    """Fetch data from {Source} API."""

    BASE_URL = "https://api.example.com"

    def __init__(self, output_dir: Path, delay: float = 0.5):
        """Initialize fetcher with rate limiting."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.delay = delay

        # Session with retry strategy
        self.session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

    def fetch_all_media(self, limit: Optional[int] = None) -> List[Dict]:
        """Fetch all media from API."""
        # Implementation here
        pass

    def save_json(self, data: Any, filename: str):
        """Save data to JSON file."""
        output_path = self.output_dir / filename
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved to {output_path}")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Fetch media from {Source}")
    parser.add_argument("-o", "--output", type=Path, default="data/raw/{source}")
    parser.add_argument("-l", "--limit", type=int, help="Limit for testing")
    args = parser.parse_args()

    fetcher = {Source}Fetcher(output_dir=args.output)
    media = fetcher.fetch_all_media(limit=args.limit)
    fetcher.save_json(media, "{source}_media.json")


if __name__ == "__main__":
    main()
```

### 2B. For web scraping

Add ethical scraping practices:

```python
import time
from bs4 import BeautifulSoup

class {Source}Scraper:
    def __init__(self, delay: float = 2.0):
        """Initialize with 2s delay for ethical scraping."""
        self.delay = delay
        # Check robots.txt first
        # Implement caching to avoid re-scraping
```

**Ethical Guidelines**:
- Check `robots.txt` before scraping
- Implement 1-2 second delays between requests
- Cache pages locally
- Provide attribution in README
- Contact site administrators if scraping large amounts

## Step 3: Create Importer

Create `src/culturemech/import/{source}_importer.py`:

```python
"""
{Source} to CultureMech Importer

Converts {Source} data to CultureMech YAML format.
"""

import json
import yaml
from pathlib import Path
from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)


class {Source}Importer:
    """Import {Source} data into CultureMech format."""

    def __init__(self, raw_data_dir: Path, output_dir: Path):
        """Initialize importer."""
        self.raw_dir = Path(raw_data_dir)
        self.output_dir = Path(output_dir)

        # Load raw data
        self.media = self._load_json("{source}_media.json")

    def _load_json(self, filename: str) -> dict:
        """Load JSON file from raw data directory."""
        with open(self.raw_dir / filename) as f:
            return json.load(f)

    def import_all(self, limit: Optional[int] = None) -> list[Path]:
        """Import all media to CultureMech format."""
        generated = []
        media_list = self.media[:limit] if limit else self.media

        for medium in media_list:
            try:
                yaml_path = self.import_medium(medium)
                if yaml_path:
                    generated.append(yaml_path)
                    logger.info(f"✓ Imported {yaml_path.name}")
            except Exception as e:
                logger.error(f"✗ Error: {e}")

        return generated

    def import_medium(self, medium: dict) -> Optional[Path]:
        """Convert single medium to CultureMech YAML."""
        # Map to CultureMech schema
        recipe = {
            "id": f"{source.upper()}_{medium['id']}",
            "name": medium['name'],
            "description": medium.get('description'),
            "ingredients": self._map_ingredients(medium),
            "preparation_steps": self._map_steps(medium),
            "provenance": self._create_provenance(medium),
        }

        # Save to YAML
        output_path = self._get_output_path(recipe)
        with open(output_path, "w") as f:
            yaml.dump(recipe, f, default_flow_style=False, sort_keys=False)

        return output_path

    def _map_ingredients(self, medium: dict) -> list[dict]:
        """Map ingredients to CultureMech format."""
        # Implementation here
        pass

    def _create_provenance(self, medium: dict) -> dict:
        """Create provenance record."""
        return {
            "source_database": "{Source}",
            "source_id": medium['id'],
            "source_url": f"https://example.com/{medium['id']}",
            "import_date": datetime.now().isoformat(),
        }


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Import {Source} media")
    parser.add_argument("-i", "--input", type=Path, default="data/raw/{source}")
    parser.add_argument("-o", "--output", type=Path, default="kb/media")
    parser.add_argument("-l", "--limit", type=int, help="Limit for testing")
    args = parser.parse_args()

    importer = {Source}Importer(args.input, args.output)
    importer.import_all(limit=args.limit)


if __name__ == "__main__":
    main()
```

## Step 4: Add Build Commands

Add to `project.justfile`:

```justfile
[group('Data')]
fetch-{source}-raw limit="":
    #!/usr/bin/env bash
    echo "Fetching {Source} data..."
    mkdir -p {{raw_data_dir}}/{source}

    if [ "{{limit}}" != "" ]; then
        uv run python -m culturemech.fetch.{source}_fetcher \
            --output {{raw_data_dir}}/{source} \
            --limit {{limit}}
    else
        uv run python -m culturemech.fetch.{source}_fetcher \
            --output {{raw_data_dir}}/{source}
    fi

[group('Import')]
import-{source} limit="":
    #!/usr/bin/env bash
    echo "Importing {Source} media..."

    if [ ! -f "{{raw_data_dir}}/{source}/{source}_media.json" ]; then
        echo "⚠ Raw data not found. Fetching..."
        just fetch-{source}-raw {{ if limit != "" { limit } else { "" } }}
    fi

    uv run python -m culturemech.import.{source}_importer \
        -i {{raw_data_dir}}/{source} \
        -o {{kb_dir}} \
        {{ if limit != "" { "--limit " + limit } else { "" } }}
```

## Step 5: Create README

Create `data/raw/{source}/README.md`:

```markdown
# {Source Name} Raw Data

## Source Information

- **Official Name**: {Full Name}
- **URL**: https://example.com
- **API Documentation**: https://api.example.com/docs
- **License**: {License Type}
- **Record Count**: ~{X} media recipes

## Data Files

- `{source}_media.json` - All media records
- `{source}_ingredients.json` - Ingredient mappings (optional)
- `fetch_stats.json` - Fetch metadata

## Provenance

**Fetch Date**: {YYYY-MM-DD}
**Fetcher**: `src/culturemech/fetch/{source}_fetcher.py`
**Fetch Command**: `just fetch-{source}-raw`

## Data Structure

```json
{
  "id": "unique_id",
  "name": "Media Name",
  "ingredients": [...],
  "description": "..."
}
```

## Notes

- {Any special considerations}
- {Known limitations}
- {Data quality issues}

## References

- {Citation to paper/database}
- {Link to terms of service}
```

## Data Quality Checklist

Before marking source as COMPLETE:

- [ ] Raw data fetched successfully
- [ ] Fetch stats recorded (date, count, version)
- [ ] Import creates valid YAML files
- [ ] Schema validation passes (`just validate-all`)
- [ ] Chemical mappings applied (CHEBI IDs where possible)
- [ ] Provenance documented in each recipe
- [ ] Cross-references checked (deduplicate against existing media)
- [ ] README created with full provenance
- [ ] Build commands tested
- [ ] Statistics updated in main README

## Cross-Referencing

To avoid duplicates, check against existing sources:

```python
def check_duplicates(new_media: dict, existing_sources: list[str]) -> bool:
    """Check if media already exists in CultureMech."""
    # 1. Exact name match
    # 2. Fuzzy name match (Levenshtein distance)
    # 3. Ingredient composition similarity (Jaccard index)
    # 4. Cross-reference IDs (e.g., DSMZ:1 appears in multiple sources)
```

Create `data/processed/media_crossref.tsv` to track equivalencies.

## Testing

Always test with small limits first:

```bash
# Test fetch (10 records)
just fetch-{source}-raw 10

# Test import (10 records)
just import-{source} 10

# Validate
just validate-all

# Check statistics
just count-recipes
just show-raw-data-stats
```

## Common Patterns

### Pattern 1: API with pagination

```python
def fetch_all_media(self):
    all_media = []
    page = 1
    while True:
        batch = self.fetch_page(page)
        if not batch:
            break
        all_media.extend(batch)
        page += 1
        time.sleep(self.delay)
    return all_media
```

### Pattern 2: Nested ingredient structures

```python
def flatten_ingredients(self, medium: dict) -> list:
    ingredients = []
    for comp in medium.get('composition', []):
        ingredients.append({
            "chemical": self.map_chemical(comp['name']),
            "quantity": comp.get('amount'),
            "units": comp.get('unit'),
        })
    return ingredients
```

### Pattern 3: Chemical mapping

```python
from culturemech.import.chemical_mappings import ChemicalMapper

mapper = ChemicalMapper(
    microbe_media_param_dir="data/raw/microbe-media-param",
    mediadive_dir="data/raw/mediadive"
)

chebi_id = mapper.lookup(ingredient_name)
```

## Troubleshooting

### API rate limiting

- Increase `--delay` parameter
- Implement exponential backoff
- Use caching to avoid re-fetching

### Web scraping blocked

- Check robots.txt compliance
- Add user-agent header
- Contact site administrator
- Consider manual curation instead

### Schema validation errors

- Check LinkML schema: `src/culturemech/schema/culturemech.yaml`
- Use `just validate-schema file.yaml` for debugging
- Common issues: missing required fields, wrong enum values

### Chemical mapping failures

- Fallback to name-only (no CHEBI ID)
- Log unmapped ingredients for manual curation
- Contribute mappings back to MicrobeMediaParam

## Resources

- **LinkML Schema**: `src/culturemech/schema/culturemech.yaml`
- **Existing Importers**: `src/culturemech/import/`
- **Chemical Mapper**: `src/culturemech/import/chemical_mappings.py`
- **MEDIA_SOURCES.tsv**: `data/MEDIA_SOURCES.tsv`

## Questions?

Open an issue or consult existing importers for patterns.
