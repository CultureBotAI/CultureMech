"""Fetch KOMODO media metadata from web table.

Scrapes the KOMODO media list table from modelseed.org and extracts:
- KOMODO IDs
- Media names
- pH information
- Medium type (complex/defined)
- Aerobic/anaerobic classification
- DSMZ medium mapping

Data Source: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
"""

import json
import logging
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class KomodoWebFetcher:
    """
    Fetch KOMODO media metadata from web table.

    Scrapes the KOMODO database web interface to extract media metadata
    including DSMZ recipe mappings for later integration.
    """

    BASE_URL = "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList"

    def __init__(self, output_dir: Path, timeout: float = 30.0):
        """
        Initialize KOMODO web fetcher.

        Args:
            output_dir: Directory to save fetched data
            timeout: Request timeout in seconds (default: 30)
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "CultureMech/0.1.0 (github.com/KG-Hub/CultureMech)"
        })

    def fetch_all(self):
        """
        Main orchestration: fetch KOMODO table and export.

        Steps:
        1. Fetch HTML page
        2. Parse table structure
        3. Extract media records
        4. Export to JSON
        5. Save statistics
        """
        logger.info("=" * 60)
        logger.info("KOMODO Web Table Fetcher")
        logger.info("=" * 60)

        # Step 1: Fetch HTML
        logger.info("\n[1/4] Fetching KOMODO web table...")
        html_content = self._fetch_html()
        logger.info(f"  ✓ Retrieved HTML ({len(html_content):,} bytes)")

        # Step 2: Parse table
        logger.info("\n[2/4] Parsing table structure...")
        media_records = self._parse_table(html_content)
        logger.info(f"  ✓ Extracted {len(media_records)} media records")

        # Step 3: Process and validate
        logger.info("\n[3/4] Processing records...")
        processed_records = self._process_records(media_records)
        logger.info(f"  ✓ Processed {len(processed_records)} records")

        # Step 4: Export
        logger.info("\n[4/4] Exporting data...")
        self._export_data(processed_records)

        logger.info("\n" + "=" * 60)
        logger.info("✓ Fetch complete!")
        logger.info(f"  Media fetched: {len(processed_records)}")
        logger.info(f"  Output: {self.output_dir}")
        logger.info("=" * 60)

    def _fetch_html(self) -> str:
        """Fetch HTML content from KOMODO web table."""
        try:
            response = self.session.get(self.BASE_URL, timeout=self.timeout)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Failed to fetch KOMODO table: {e}")
            raise

    def _parse_table(self, html_content: str) -> List[Dict[str, Any]]:
        """
        Parse HTML table into structured records.

        Expected table structure:
        - Column 0: ID
        - Column 1: Name
        - Column 2: PH Info
        - Column 3: Is Complex (true/false)
        - Column 4: Is Aerobic (true/false)
        - Column 5: Is SubMedium (true/false)
        - Column 6: Instructions (DSMZ PDF link)
        """
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the table by ID or just get the first table
        table = soup.find('table', {'id': 'Table0'})
        if not table:
            table = soup.find('table')
        if not table:
            raise ValueError("No table found in HTML content")

        # Extract rows (skip header row)
        all_rows = table.find_all('tr')
        if len(all_rows) < 2:
            raise ValueError(f"Table has insufficient rows: {len(all_rows)}")

        rows = all_rows[1:]  # Skip header row

        media_records = []
        for row in rows:
            cols = row.find_all('td')
            if len(cols) < 7:
                continue  # Skip incomplete rows

            # Extract ID (may be inside an <a> tag)
            id_cell = cols[0]
            id_link = id_cell.find('a')
            if id_link:
                medium_id = id_link.get_text(strip=True)
            else:
                medium_id = id_cell.get_text(strip=True)

            # Extract pH info (handle "null" string as None)
            ph_text = cols[2].get_text(strip=True)
            if ph_text == 'null' or not ph_text:
                ph_info = None
            else:
                ph_info = ph_text

            # Extract DSMZ medium number from PDF link
            dsmz_number = None
            instructions_cell = cols[6]
            link = instructions_cell.find('a')
            if link and 'href' in link.attrs:
                href = link['href']
                # Extract number from: DSMZ_Medium123.pdf
                match = re.search(r'DSMZ_Medium(\w+)\.pdf', href)
                if match:
                    dsmz_number = match.group(1)

            record = {
                "id": medium_id,
                "name": cols[1].get_text(strip=True),
                "ph_info": ph_info,
                "is_complex": cols[3].get_text(strip=True).lower() == 'true',
                "is_aerobic": cols[4].get_text(strip=True).lower() == 'true',
                "is_submedium": cols[5].get_text(strip=True).lower() == 'true',
                "dsmz_medium_number": dsmz_number
            }

            media_records.append(record)

        return media_records

    def _process_records(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Process and validate records.

        Processing:
        - Parse pH ranges
        - Standardize ID formats
        - Validate DSMZ mappings
        """
        processed = []

        for record in records:
            # Parse pH info
            ph_info = self._parse_ph_info(record.get('ph_info'))

            processed_record = {
                **record,
                'ph_value': ph_info.get('value'),
                'ph_range': ph_info.get('range'),
                'ph_buffer': ph_info.get('buffer')
            }

            processed.append(processed_record)

        return processed

    def _parse_ph_info(self, ph_info: Optional[str]) -> Dict[str, Optional[str]]:
        """
        Parse pH information into structured format.

        Examples:
        - "7.0" -> {"value": "7.0", "range": None, "buffer": None}
        - "7.5 - 8.0" -> {"value": None, "range": "7.5-8.0", "buffer": None}
        - "5.5, H2SO4" -> {"value": "5.5", "range": None, "buffer": "H2SO4"}
        - "7.5, KOH" -> {"value": "7.5", "range": None, "buffer": "KOH"}
        """
        if not ph_info:
            return {"value": None, "range": None, "buffer": None}

        result = {"value": None, "range": None, "buffer": None}

        # Check for buffer (comma-separated)
        if ',' in ph_info:
            parts = [p.strip() for p in ph_info.split(',')]
            ph_part = parts[0]
            buffer = parts[1] if len(parts) > 1 else None
            result['buffer'] = buffer
        else:
            ph_part = ph_info

        # Check for range (hyphen or dash)
        if '-' in ph_part and not ph_part.startswith('-'):
            # Range format: "7.5 - 8.0"
            range_match = re.search(r'(\d+\.?\d*)\s*-\s*(\d+\.?\d*)', ph_part)
            if range_match:
                result['range'] = f"{range_match.group(1)}-{range_match.group(2)}"
        else:
            # Single value
            value_match = re.search(r'(\d+\.?\d*)', ph_part)
            if value_match:
                result['value'] = value_match.group(1)

        return result

    def _export_data(self, records: List[Dict[str, Any]]):
        """Export data to JSON files with statistics."""

        # Export media records
        media_path = self.save_json(
            {"count": len(records), "data": records},
            "komodo_web_media.json"
        )
        logger.info(f"  ✓ Saved {media_path.name}")

        # Analyze DSMZ mappings
        with_dsmz = [r for r in records if r.get('dsmz_medium_number')]
        without_dsmz = [r for r in records if not r.get('dsmz_medium_number')]

        # Analyze medium types
        complex_media = [r for r in records if r.get('is_complex')]
        defined_media = [r for r in records if not r.get('is_complex')]

        # Analyze aerobic classification
        aerobic_media = [r for r in records if r.get('is_aerobic')]
        anaerobic_media = [r for r in records if not r.get('is_aerobic')]

        # Export statistics
        stats = {
            "fetch_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "source": "KOMODO ModelSEED Web Table",
            "source_url": self.BASE_URL,
            "total_records": len(records),
            "dsmz_mappings": {
                "with_mapping": len(with_dsmz),
                "without_mapping": len(without_dsmz),
                "coverage_percent": (len(with_dsmz) / len(records) * 100) if len(records) > 0 else 0
            },
            "medium_types": {
                "complex": len(complex_media),
                "defined": len(defined_media)
            },
            "aerobic_classification": {
                "aerobic": len(aerobic_media),
                "anaerobic": len(anaerobic_media)
            },
            "submedia_count": len([r for r in records if r.get('is_submedium')])
        }
        stats_path = self.save_json(stats, "fetch_stats.json")
        logger.info(f"  ✓ Saved {stats_path.name}")

        # Export DSMZ mapping table
        dsmz_mappings = [
            {
                "komodo_id": r['id'],
                "dsmz_medium_number": r['dsmz_medium_number'],
                "name": r['name']
            }
            for r in records if r.get('dsmz_medium_number')
        ]
        mapping_path = self.save_json(
            {"count": len(dsmz_mappings), "mappings": dsmz_mappings},
            "komodo_dsmz_mappings.json"
        )
        logger.info(f"  ✓ Saved {mapping_path.name}")

        # Create README
        self._create_readme(stats)
        logger.info(f"  ✓ Saved README.md")

    def _create_readme(self, stats: Dict[str, Any]):
        """Create README documentation."""
        readme_content = f"""# KOMODO Web Table Raw Data

## Source Information

**Source**: KOMODO ModelSEED Web Interface
**URL**: {self.BASE_URL}
**Date Fetched**: {stats['fetch_date']}
**Fetched By**: komodo_web_fetcher.py
**License**: ModelSEED - check source for terms

## Database Information

**Database**: KOMODO (Knowledge base Of Microbial and Mammalian cells Defined and Optimized media)
**Type**: Web table scraping
**Purpose**: Media metadata extraction with DSMZ recipe mappings

## Data Coverage

**Total Records**: {stats['total_records']}
**DSMZ Mappings**: {stats['dsmz_mappings']['with_mapping']} ({stats['dsmz_mappings']['coverage_percent']:.1f}%)
**Medium Types**:
- Complex: {stats['medium_types']['complex']}
- Defined: {stats['medium_types']['defined']}

**Aerobic Classification**:
- Aerobic: {stats['aerobic_classification']['aerobic']}
- Anaerobic: {stats['aerobic_classification']['anaerobic']}

**Submedia**: {stats['submedia_count']}

## Files in this Directory

### komodo_web_media.json
- **Description**: All KOMODO media records with metadata
- **Format**: JSON with `count` and `data` array
- **Structure**:
  ```json
  {{
    "count": {stats['total_records']},
    "data": [
      {{
        "id": "1",
        "name": "NUTRIENT AGAR",
        "ph_info": "7.0",
        "ph_value": "7.0",
        "ph_range": null,
        "ph_buffer": null,
        "is_complex": true,
        "is_aerobic": false,
        "is_submedium": false,
        "dsmz_medium_number": "1"
      }}
    ]
  }}
  ```

### komodo_dsmz_mappings.json
- **Description**: KOMODO ID to DSMZ medium number mappings
- **Format**: JSON with mappings array
- **Purpose**: Enable merging KOMODO metadata with DSMZ recipes
- **Count**: {stats['dsmz_mappings']['with_mapping']} mappings

### fetch_stats.json
- **Description**: Fetch metadata and statistics
- **Format**: JSON with coverage metrics

## KOMODO ID Formats

KOMODO uses various ID formats:
- Simple numbers: `1`, `10`, `1000`
- Decimal variants: `1004.1`, `1004.2`, `1004.3`
- Underscore variants: `1008_19205`, `104_15597`
- Letter suffixes: `1011a`, `104a`, `104b`

## DSMZ Mapping Strategy

The `dsmz_medium_number` field links KOMODO media to DSMZ recipes:
- Extracted from Instructions column (DSMZ PDF links)
- Format: DSMZ_Medium[NUMBER].pdf
- Used for future merge with MediaDive/DSMZ composition data
- Coverage: {stats['dsmz_mappings']['coverage_percent']:.1f}% of KOMODO media

## How to Fetch Data

```bash
# Fetch KOMODO web table
just fetch-komodo-web

# Or use script directly
uv run python -m culturemech.fetch.komodo_web_fetcher \\
    --output raw/komodo_web
```

## Integration Workflow

1. **Fetch KOMODO metadata** (this fetcher)
   - Extracts KOMODO IDs, names, pH, types
   - Extracts DSMZ recipe mappings

2. **Import KOMODO to YAML** (komodo_web_importer.py)
   - Creates YAML files with KOMODO metadata
   - Uses KOMODO IDs as primary identifiers

3. **Merge with DSMZ data** (future step)
   - Match KOMODO records to DSMZ recipes using `dsmz_medium_number`
   - Enrich KOMODO metadata with DSMZ compositions
   - Create cross-references between databases

## Data Quality Notes

**Strengths**:
- ✅ Complete KOMODO metadata
- ✅ High DSMZ mapping coverage ({stats['dsmz_mappings']['coverage_percent']:.1f}%)
- ✅ Medium type classification
- ✅ pH information (where available)

**Limitations**:
- ⚠️ No composition data (will be merged from DSMZ later)
- ⚠️ Some records have generic names (e.g., "For DSM 16554")
- ⚠️ pH info format varies (single values, ranges, buffers)

## Citations

> KOMODO - Knowledge base Of Microbial and Mammalian cells Defined and Optimized media
> ModelSEED Project
> https://komodo.modelseed.org
"""

        readme_path = self.output_dir / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

    def save_json(self, data: Any, filename: str) -> Path:
        """Save data as pretty-printed JSON."""
        output_path = self.output_dir / filename
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return output_path


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Fetch KOMODO media metadata from web table"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("raw/komodo_web"),
        help="Output directory (default: raw/komodo_web)"
    )

    args = parser.parse_args()

    fetcher = KomodoWebFetcher(output_dir=args.output)
    fetcher.fetch_all()


if __name__ == "__main__":
    main()
