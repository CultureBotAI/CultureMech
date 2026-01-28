"""
KOMODO (Known Media Database) Fetcher

Fetches media data from KOMODO - a standardized media database from DSMZ.
KOMODO contains 3,335 media with standardized molar concentrations integrated
with the SEED compound database.

Data Sources:
- SQL database dump (preferred)
- ModelSEED GitHub repository
- Web scraping fallback (https://komodo.modelseed.org/)

Reference:
- Zarecki et al. (2015) Nature Communications
- https://komodo.modelseed.org/
"""

import argparse
import json
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime
import logging
import urllib.request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Optional dependencies for Excel parsing
try:
    import openpyxl
    HAS_OPENPYXL = True
except ImportError:
    HAS_OPENPYXL = False
    logger.warning("openpyxl not installed - Excel file parsing unavailable")

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    logger.debug("pandas not installed - will use openpyxl for Excel parsing")


class KOMODOFetcher:
    """
    Fetch media data from KOMODO database.

    KOMODO provides:
    - 3,335 standardized media formulations
    - Molar concentrations for all components
    - SEED compound database integration
    - High-confidence organism-media associations
    """

    def __init__(self, output_dir: Path):
        """
        Initialize KOMODO fetcher.

        Args:
            output_dir: Directory to save fetched data
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.media = []
        self.compounds = {}
        self.organisms = {}

    def parse_sql_dump(self, sql_file: Path) -> bool:
        """
        Parse KOMODO SQL dump to extract media, compounds, and organisms.

        Args:
            sql_file: Path to SQL dump file

        Returns:
            True if successful, False otherwise
        """
        logger.info(f"Parsing SQL dump: {sql_file}")

        if not sql_file.exists():
            logger.error(f"SQL file not found: {sql_file}")
            return False

        try:
            import sqlparse
        except ImportError:
            logger.error("sqlparse not installed. Install with: pip install sqlparse")
            return False

        with open(sql_file, 'r', encoding='utf-8', errors='ignore') as f:
            sql_content = f.read()

        # Parse SQL statements
        statements = sqlparse.split(sql_content)

        logger.info(f"Parsing {len(statements)} SQL statements...")

        for stmt in statements:
            stmt = stmt.strip()
            if not stmt:
                continue

            # Look for INSERT statements
            if stmt.upper().startswith('INSERT INTO'):
                self._parse_insert_statement(stmt)

        logger.info(f"✓ Parsed SQL dump:")
        logger.info(f"  Media: {len(self.media)}")
        logger.info(f"  Compounds: {len(self.compounds)}")
        logger.info(f"  Organisms: {len(self.organisms)}")

        return len(self.media) > 0

    def _parse_insert_statement(self, stmt: str):
        """Parse INSERT statement to extract data."""
        # Extract table name
        table_match = re.match(r'INSERT INTO\s+`?(\w+)`?', stmt, re.IGNORECASE)
        if not table_match:
            return

        table_name = table_match.group(1).lower()

        # Extract values
        values_match = re.search(r'VALUES\s*(\(.*\));?$', stmt, re.IGNORECASE | re.DOTALL)
        if not values_match:
            return

        values_str = values_match.group(1)

        # Parse based on table type
        if 'media' in table_name or 'medium' in table_name:
            self._parse_media_insert(values_str)
        elif 'compound' in table_name or 'chemical' in table_name:
            self._parse_compound_insert(values_str)
        elif 'organism' in table_name or 'species' in table_name:
            self._parse_organism_insert(values_str)

    def _parse_media_insert(self, values_str: str):
        """Parse media table INSERT values."""
        # Simple parsing - extract comma-separated values within parentheses
        # This is a simplified parser; adjust based on actual SQL structure
        try:
            # Extract individual records
            records = re.findall(r'\(([^)]+)\)', values_str)
            for record in records:
                # Split by comma (handle quoted strings)
                parts = self._split_sql_values(record)
                if len(parts) >= 2:
                    medium = {
                        'id': self._clean_sql_value(parts[0]),
                        'name': self._clean_sql_value(parts[1]) if len(parts) > 1 else '',
                        'composition': []
                    }
                    self.media.append(medium)
        except Exception as e:
            logger.debug(f"Error parsing media insert: {e}")

    def _parse_compound_insert(self, values_str: str):
        """Parse compound table INSERT values."""
        try:
            records = re.findall(r'\(([^)]+)\)', values_str)
            for record in records:
                parts = self._split_sql_values(record)
                if len(parts) >= 2:
                    compound_id = self._clean_sql_value(parts[0])
                    compound_name = self._clean_sql_value(parts[1])
                    self.compounds[compound_id] = {
                        'id': compound_id,
                        'name': compound_name,
                        'seed_id': compound_id
                    }
        except Exception as e:
            logger.debug(f"Error parsing compound insert: {e}")

    def _parse_organism_insert(self, values_str: str):
        """Parse organism table INSERT values."""
        try:
            records = re.findall(r'\(([^)]+)\)', values_str)
            for record in records:
                parts = self._split_sql_values(record)
                if len(parts) >= 2:
                    organism_id = self._clean_sql_value(parts[0])
                    organism_name = self._clean_sql_value(parts[1])
                    self.organisms[organism_id] = {
                        'id': organism_id,
                        'name': organism_name
                    }
        except Exception as e:
            logger.debug(f"Error parsing organism insert: {e}")

    def _split_sql_values(self, values: str) -> List[str]:
        """Split SQL values by comma, respecting quoted strings."""
        parts = []
        current = ''
        in_quotes = False
        quote_char = None

        for char in values:
            if char in ('"', "'") and (not in_quotes or char == quote_char):
                in_quotes = not in_quotes
                quote_char = char if in_quotes else None
            elif char == ',' and not in_quotes:
                parts.append(current.strip())
                current = ''
                continue
            current += char

        if current.strip():
            parts.append(current.strip())

        return parts

    def _clean_sql_value(self, value: str) -> str:
        """Clean SQL value (remove quotes, handle NULL, etc.)."""
        value = value.strip()

        # Handle NULL
        if value.upper() == 'NULL':
            return ''

        # Remove quotes
        if (value.startswith("'") and value.endswith("'")) or \
           (value.startswith('"') and value.endswith('"')):
            value = value[1:-1]

        # Unescape
        value = value.replace("\\'", "'").replace('\\"', '"')

        return value

    def fetch_from_pmc_supplementary(self) -> bool:
        """
        Fetch KOMODO data from PubMed Central supplementary files.

        Downloads Excel files from the Nature Communications paper (PMC4633754).

        Returns:
            True if successful, False otherwise
        """
        logger.info("Fetching KOMODO supplementary data from PMC...")

        if not HAS_OPENPYXL and not HAS_PANDAS:
            logger.error("Neither openpyxl nor pandas is installed")
            logger.info("Install with: uv pip install openpyxl")
            return False

        # PMC supplementary file URLs
        base_url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4633754/bin/"
        files_to_download = {
            "ncomms9493-s5.xlsx": "SEED compounds",
            # Add other supplementary files as needed
            # "ncomms9493-s3.xlsx": "Collaborative filtering predictions",
            # "ncomms9493-s4.xlsx": "Organism richness preferences",
        }

        downloaded_files = []

        for filename, description in files_to_download.items():
            url = base_url + filename
            output_path = self.output_dir / filename

            logger.info(f"Downloading {description} from {url}...")

            try:
                urllib.request.urlretrieve(url, output_path)
                logger.info(f"✓ Downloaded {filename} ({description})")
                downloaded_files.append(output_path)
            except Exception as e:
                logger.error(f"✗ Failed to download {filename}: {e}")
                continue

        if not downloaded_files:
            logger.error("No files downloaded successfully")
            return False

        # Parse downloaded Excel files
        logger.info("Parsing Excel files...")

        for excel_file in downloaded_files:
            self._parse_excel_file(excel_file)

        logger.info(f"✓ Parsed {len(downloaded_files)} Excel files")
        return len(self.compounds) > 0

    def _parse_excel_file(self, excel_path: Path):
        """
        Parse an Excel file from KOMODO supplementary data.

        Args:
            excel_path: Path to Excel file
        """
        logger.info(f"Parsing {excel_path.name}...")

        try:
            if HAS_PANDAS:
                # Use pandas for easier parsing
                sheets = pd.read_excel(excel_path, sheet_name=None, engine='openpyxl')

                for sheet_name, df in sheets.items():
                    logger.info(f"  Sheet: {sheet_name} ({len(df)} rows)")

                    # Check if this is a compounds sheet
                    if 'SEED' in sheet_name.upper() or 'COMPOUND' in sheet_name.upper():
                        self._parse_compounds_from_dataframe(df)

                    # Check if this is a media sheet
                    elif 'MEDIA' in sheet_name.upper() or 'MEDIUM' in sheet_name.upper():
                        self._parse_media_from_dataframe(df)

            elif HAS_OPENPYXL:
                # Use openpyxl for basic parsing
                wb = openpyxl.load_workbook(excel_path, read_only=True)

                for sheet_name in wb.sheetnames:
                    ws = wb[sheet_name]
                    rows = list(ws.values)
                    logger.info(f"  Sheet: {sheet_name} ({len(rows)} rows)")

                    # Try to parse as compounds or media
                    if len(rows) > 1:
                        header = rows[0]
                        data_rows = rows[1:]

                        # Check if this looks like compounds data
                        if any('SEED' in str(col).upper() or 'COMPOUND' in str(col).upper()
                               for col in header if col):
                            self._parse_compounds_from_rows(header, data_rows)

        except Exception as e:
            logger.error(f"Error parsing {excel_path.name}: {e}")

    def _parse_compounds_from_dataframe(self, df):
        """Parse compounds from pandas DataFrame."""
        # Try to identify SEED ID column
        seed_col = None
        name_col = None

        for col in df.columns:
            col_str = str(col).upper()
            if 'SEED' in col_str and 'ID' in col_str:
                seed_col = col
            elif 'NAME' in col_str or 'COMPOUND' in col_str:
                name_col = col

        if seed_col is None:
            logger.warning("Could not find SEED ID column in DataFrame")
            return

        # Extract compounds
        for idx, row in df.iterrows():
            seed_id = row.get(seed_col)
            if pd.isna(seed_id):
                continue

            seed_id = str(seed_id).strip()
            if not seed_id:
                continue

            compound_name = row.get(name_col, seed_id) if name_col else seed_id
            if pd.isna(compound_name):
                compound_name = seed_id

            self.compounds[seed_id] = {
                'id': seed_id,
                'name': str(compound_name).strip(),
                'seed_id': seed_id
            }

        logger.info(f"  Extracted {len(self.compounds)} compounds")

    def _parse_compounds_from_rows(self, header, data_rows):
        """Parse compounds from raw rows (openpyxl)."""
        # Find SEED ID and name columns
        seed_idx = None
        name_idx = None

        for idx, col in enumerate(header):
            if col is None:
                continue
            col_str = str(col).upper()
            if 'SEED' in col_str and 'ID' in col_str:
                seed_idx = idx
            elif 'NAME' in col_str or 'COMPOUND' in col_str:
                name_idx = idx

        if seed_idx is None:
            logger.warning("Could not find SEED ID column in Excel sheet")
            return

        # Extract compounds
        for row in data_rows:
            if not row or len(row) <= seed_idx:
                continue

            seed_id = row[seed_idx]
            if seed_id is None:
                continue

            seed_id = str(seed_id).strip()
            if not seed_id:
                continue

            compound_name = row[name_idx] if (name_idx is not None and len(row) > name_idx) else seed_id
            if compound_name is None:
                compound_name = seed_id

            self.compounds[seed_id] = {
                'id': seed_id,
                'name': str(compound_name).strip(),
                'seed_id': seed_id
            }

        logger.info(f"  Extracted {len(self.compounds)} compounds")

    def _parse_media_from_dataframe(self, df):
        """Parse media from pandas DataFrame."""
        logger.info("  Parsing media data (structure to be determined)")
        # This will need to be implemented based on actual data structure
        # For now, just log that we found a media sheet

    def fetch_from_modelseed_github(self) -> bool:
        """
        Fetch KOMODO data from ModelSEED GitHub repository.

        Returns:
            True if successful, False otherwise
        """
        logger.info("Fetching from ModelSEED GitHub...")
        logger.info("Note: ModelSEED repository contains biochemistry data, not KOMODO media")
        logger.info("      Use --pmc option to download from PubMed Central instead")

        logger.warning("GitHub fetch not implemented for KOMODO")
        logger.info("Recommendation: use --pmc to fetch supplementary data")

        return False

    def scrape_web(self, limit: Optional[int] = None) -> bool:
        """
        Scrape KOMODO website as fallback.

        Args:
            limit: Optional limit for testing

        Returns:
            True if successful, False otherwise
        """
        logger.info("Web scraping not yet implemented")
        logger.info("Please contact KOMODO maintainers for SQL dump")
        logger.info("Contact: raphy.zarecki@gmail.com")

        return False

    def export_to_json(self):
        """Export fetched data to JSON files."""
        logger.info("Exporting to JSON...")

        # Export media
        media_file = self.output_dir / "komodo_media.json"
        with open(media_file, 'w', encoding='utf-8') as f:
            json.dump({
                'count': len(self.media),
                'data': self.media
            }, f, indent=2, ensure_ascii=False)
        logger.info(f"✓ Saved {len(self.media)} media to {media_file}")

        # Export compounds
        compounds_file = self.output_dir / "komodo_compounds.json"
        with open(compounds_file, 'w', encoding='utf-8') as f:
            json.dump({
                'count': len(self.compounds),
                'data': list(self.compounds.values())
            }, f, indent=2, ensure_ascii=False)
        logger.info(f"✓ Saved {len(self.compounds)} compounds to {compounds_file}")

        # Export organisms
        organisms_file = self.output_dir / "komodo_organisms.json"
        with open(organisms_file, 'w', encoding='utf-8') as f:
            json.dump({
                'count': len(self.organisms),
                'data': list(self.organisms.values())
            }, f, indent=2, ensure_ascii=False)
        logger.info(f"✓ Saved {len(self.organisms)} organisms to {organisms_file}")

        # Export statistics
        stats = {
            'fetch_date': datetime.utcnow().isoformat() + 'Z',
            'source': 'KOMODO',
            'total_media': len(self.media),
            'total_compounds': len(self.compounds),
            'total_organisms': len(self.organisms),
            'url': 'https://komodo.modelseed.org/'
        }

        stats_file = self.output_dir / "fetch_stats.json"
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2)
        logger.info(f"✓ Saved statistics to {stats_file}")

    def fetch_all(
        self,
        sql_file: Optional[Path] = None,
        use_pmc: bool = False,
        use_github: bool = False,
        scrape: bool = False
    ):
        """
        Fetch all KOMODO data using specified method.

        Args:
            sql_file: Path to SQL dump
            use_pmc: Fetch from PubMed Central supplementary files (recommended)
            use_github: Fetch from ModelSEED GitHub
            scrape: Web scraping fallback
        """
        logger.info("=" * 60)
        logger.info("KOMODO Media Database Fetcher")
        logger.info("=" * 60)

        success = False

        # Try PMC supplementary files first (recommended)
        if use_pmc:
            success = self.fetch_from_pmc_supplementary()

        # Try SQL dump
        elif sql_file:
            success = self.parse_sql_dump(sql_file)

        # Fallback to GitHub (not recommended for KOMODO)
        elif use_github:
            success = self.fetch_from_modelseed_github()

        # Fallback to web scraping
        elif scrape:
            success = self.scrape_web()

        else:
            logger.error("No data source specified!")
            logger.info("\nUsage:")
            logger.info("  --pmc            Fetch from PubMed Central (RECOMMENDED)")
            logger.info("  --sql PATH       Parse SQL dump")
            logger.info("  --github         Fetch from ModelSEED GitHub (compounds only)")
            logger.info("  --scrape         Web scraping (fallback)")
            logger.info("\nRecommended:")
            logger.info("  python -m culturemech.fetch.komodo_fetcher --pmc -o raw/komodo")
            return

        if not success:
            logger.error("✗ Failed to fetch KOMODO data")
            return

        # Export to JSON
        self.export_to_json()

        logger.info("\n" + "=" * 60)
        logger.info("✓ Fetch complete!")
        logger.info(f"  Media: {len(self.media)}")
        logger.info(f"  Compounds: {len(self.compounds)}")
        logger.info(f"  Organisms: {len(self.organisms)}")
        logger.info(f"  Output: {self.output_dir}")
        logger.info("=" * 60)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch KOMODO media database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Fetch from PubMed Central (recommended)
  python -m culturemech.fetch.komodo_fetcher --pmc -o raw/komodo

  # Parse SQL dump (if you have one)
  python -m culturemech.fetch.komodo_fetcher --sql komodo.sql -o raw/komodo

Data sources:
  --pmc        PubMed Central supplementary files (PMC4633754)
               Downloads Excel files with SEED compounds and media data
               RECOMMENDED - No additional files needed

  --sql PATH   Parse SQL database dump
               Requires obtaining dump from KOMODO maintainers

  --github     ModelSEED GitHub repository
               Note: Contains biochemistry data, not KOMODO media

  --scrape     Web scraping from komodo.modelseed.org
               Not recommended - incomplete data
"""
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default="raw/komodo",
        help="Output directory for fetched data"
    )
    parser.add_argument(
        "--pmc",
        action="store_true",
        help="Fetch from PubMed Central supplementary files (RECOMMENDED)"
    )
    parser.add_argument(
        "--sql",
        type=Path,
        help="Path to KOMODO SQL dump file"
    )
    parser.add_argument(
        "--github",
        action="store_true",
        help="Fetch from ModelSEED GitHub repository (biochemistry only)"
    )
    parser.add_argument(
        "--scrape",
        action="store_true",
        help="Web scraping fallback (not recommended)"
    )

    args = parser.parse_args()

    fetcher = KOMODOFetcher(output_dir=args.output)
    fetcher.fetch_all(
        sql_file=args.sql,
        use_pmc=args.pmc,
        use_github=args.github,
        scrape=args.scrape
    )


if __name__ == "__main__":
    main()
