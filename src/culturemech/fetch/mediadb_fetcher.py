"""
MediaDB Fetcher

Fetches media data from MediaDB - a database of chemically-defined media
for genome-sequenced organisms.

MediaDB contains 65 defined media across 57 species with focus on organisms
with completed genome sequences and metabolic models.

Data Sources:
- MySQL/SQL database dump (preferred)
- TSV exports from mediadb.systemsbiology.net
- Web scraping fallback

Reference:
- Mazumdar et al. (2014) PLOS One
- https://mediadb.systemsbiology.net/ (formerly mediadb.org)
"""

import argparse
import csv
import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MediaDBFetcher:
    """
    Fetch media data from MediaDB.

    MediaDB provides:
    - 65 chemically-defined media
    - 57 organisms with genome sequences
    - 14,795 chemical compounds with cross-database IDs
    - Integration with KEGG, BiGG, SEED, ChEBI, PubChem
    """

    def __init__(self, output_dir: Path):
        """
        Initialize MediaDB fetcher.

        Args:
            output_dir: Directory to save fetched data
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.media = []
        self.compounds = {}
        self.organisms = {}
        self.media_compositions = {}  # Temporary storage for compositions

    def parse_sql_dump(self, sql_file: Path) -> bool:
        """
        Parse MediaDB SQL dump to extract media, compounds, and organisms.

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

        with open(sql_file, encoding="utf-8", errors="ignore") as f:
            sql_content = f.read()

        # Parse SQL statements
        statements = sqlparse.split(sql_content)

        logger.info(f"Parsing {len(statements)} SQL statements...")

        for stmt in statements:
            stmt = stmt.strip()
            if not stmt:
                continue

            # Look for INSERT statements
            if stmt.upper().startswith("INSERT INTO"):
                self._parse_insert_statement(stmt)

        # Link compositions to media after all parsing is done
        self._link_compositions_to_media()

        logger.info("✓ Parsed SQL dump:")
        logger.info(f"  Media: {len(self.media)}")
        logger.info(f"  Compounds: {len(self.compounds)}")
        logger.info(f"  Organisms: {len(self.organisms)}")

        return len(self.media) > 0

    def parse_tsv_exports(self, tsv_dir: Path) -> bool:
        """
        Parse MediaDB TSV export files.

        Expected files:
        - organisms.txt or organisms.tsv
        - media_names.txt or media.tsv
        - compounds.txt or compounds.tsv
        - media_compositions.txt or compositions.tsv

        Args:
            tsv_dir: Directory containing TSV files

        Returns:
            True if successful, False otherwise
        """
        logger.info(f"Parsing TSV files from: {tsv_dir}")

        tsv_dir = Path(tsv_dir)
        if not tsv_dir.exists():
            logger.error(f"TSV directory not found: {tsv_dir}")
            return False

        # Try to find and parse each file type
        self._parse_organisms_tsv(tsv_dir)
        self._parse_compounds_tsv(tsv_dir)
        self._parse_media_tsv(tsv_dir)
        self._parse_compositions_tsv(tsv_dir)

        logger.info("✓ Parsed TSV files:")
        logger.info(f"  Media: {len(self.media)}")
        logger.info(f"  Compounds: {len(self.compounds)}")
        logger.info(f"  Organisms: {len(self.organisms)}")

        return len(self.media) > 0

    def _parse_insert_statement(self, stmt: str):
        """Parse INSERT statement to extract data."""
        # Extract table name
        table_match = re.match(r"INSERT INTO\s+`?(\w+)`?", stmt, re.IGNORECASE)
        if not table_match:
            return

        table_name = table_match.group(1).lower()

        # Extract values
        values_match = re.search(r"VALUES\s*(\(.*\));?$", stmt, re.IGNORECASE | re.DOTALL)
        if not values_match:
            return

        values_str = values_match.group(1)

        # Parse based on table type (use exact table names to avoid conflicts)
        if table_name == "media_names":
            self._parse_media_insert(values_str)
        elif table_name == "media_compounds":
            self._parse_media_compounds_insert(values_str)
        elif table_name == "compounds":
            self._parse_compound_insert(values_str)
        elif table_name == "organisms":
            self._parse_organism_insert(values_str)

    def _parse_media_insert(self, values_str: str):
        """Parse media_names table INSERT values."""
        try:
            records = self._split_sql_records(values_str)
            for record in records:
                parts = self._split_sql_values(record)
                if len(parts) >= 2:
                    medium = {
                        "id": self._clean_sql_value(parts[0]),
                        "name": self._clean_sql_value(parts[1]),
                        "is_minimal": self._clean_sql_value(parts[2]) if len(parts) > 2 else "",
                        "composition": [],
                    }
                    self.media.append(medium)
        except Exception as e:
            logger.debug(f"Error parsing media insert: {e}")

    def _parse_media_compounds_insert(self, values_str: str):
        """Parse media_compounds table INSERT values (stores for later linking)."""
        try:
            records = self._split_sql_records(values_str)

            for record in records:
                parts = self._split_sql_values(record)
                if len(parts) >= 4:
                    # Format: (medcompID, medID, compID, Amount_mM)
                    med_id = self._clean_sql_value(parts[1])
                    comp_id = self._clean_sql_value(parts[2])
                    amount_mm = self._clean_sql_value(parts[3])

                    if med_id not in self.media_compositions:
                        self.media_compositions[med_id] = []

                    self.media_compositions[med_id].append(
                        {
                            "compound_id": comp_id,
                            "concentration": (
                                float(amount_mm) if amount_mm and amount_mm != "NULL" else 0.0
                            ),
                            "unit": "mM",
                        }
                    )

        except Exception as e:
            logger.debug(f"Error parsing media_compounds insert: {e}")

    def _link_compositions_to_media(self):
        """Link stored compositions to media after all parsing is complete."""
        linked_count = 0
        for medium in self.media:
            if medium["id"] in self.media_compositions:
                medium["composition"] = self.media_compositions[medium["id"]]
                linked_count += 1

        logger.info(f"Linked compositions to {linked_count}/{len(self.media)} media")

    def _parse_compound_insert(self, values_str: str):
        """Parse compound table INSERT values."""
        try:
            records = self._split_sql_records(values_str)
            for record in records:
                parts = self._split_sql_values(record)
                # Column order is the `compounds` CREATE TABLE in the dump:
                #   compID | KEGG_ID | BiGG_ID | name | seed_id | pubchem_ids
                #   | chebi_ids | formula
                # The previous mapping read parts[1] as the name, which is
                # KEGG_ID, and parts[3] (the real name) as the ChEBI id. On the
                # very first row — (1,'C00001','h2o','Water',...) — that gave
                # name='C00001' and chebi_id='Water'.
                if len(parts) >= 4:
                    compound_id = self._clean_sql_value(parts[0])
                    self.compounds[compound_id] = {
                        "id": compound_id,
                        "name": self._clean_sql_value(parts[3]),
                        "kegg_id": self._clean_sql_value(parts[1]),
                        "bigg_id": self._clean_sql_value(parts[2]),
                        "chebi_id": self._clean_sql_value(parts[6]) if len(parts) > 6 else "",
                        "formula": self._clean_sql_value(parts[7]) if len(parts) > 7 else "",
                    }
        except Exception as e:
            logger.debug(f"Error parsing compound insert: {e}")

    def _parse_organism_insert(self, values_str: str):
        """Parse organism table INSERT values."""
        try:
            records = self._split_sql_records(values_str)
            for record in records:
                parts = self._split_sql_values(record)
                if len(parts) >= 2:
                    organism_id = self._clean_sql_value(parts[0])
                    self.organisms[organism_id] = {
                        "id": organism_id,
                        "name": self._clean_sql_value(parts[1]),
                    }
        except Exception as e:
            logger.debug(f"Error parsing organism insert: {e}")

    def _parse_organisms_tsv(self, tsv_dir: Path):
        """Parse organisms TSV file."""
        for filename in ["organisms.txt", "organisms.tsv", "species.txt"]:
            file_path = tsv_dir / filename
            if not file_path.exists():
                continue

            logger.info(f"Loading {filename}...")
            with open(file_path, encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter="\t")
                for row in reader:
                    org_id = row.get("id") or row.get("organism_id")
                    if org_id:
                        self.organisms[org_id] = {
                            "id": org_id,
                            "name": row.get("name") or row.get("organism_name", ""),
                            "ncbi_taxonomy_id": row.get("ncbi_taxonomy_id", ""),
                        }
            return

    def _parse_compounds_tsv(self, tsv_dir: Path):
        """Parse compounds TSV file."""
        for filename in ["compounds.txt", "compounds.tsv", "chemicals.txt"]:
            file_path = tsv_dir / filename
            if not file_path.exists():
                continue

            logger.info(f"Loading {filename}...")
            with open(file_path, encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter="\t")
                for row in reader:
                    comp_id = row.get("id") or row.get("compound_id")
                    if comp_id:
                        self.compounds[comp_id] = {
                            "id": comp_id,
                            "name": row.get("name") or row.get("compound_name", ""),
                            "kegg_id": row.get("kegg_id", ""),
                            "chebi_id": row.get("chebi_id", ""),
                            "pubchem_id": row.get("pubchem_id", ""),
                            "bigg_id": row.get("bigg_id", ""),
                            "seed_id": row.get("seed_id", ""),
                        }
            return

    def _parse_media_tsv(self, tsv_dir: Path):
        """Parse media TSV file."""
        for filename in ["media_names.txt", "media.tsv", "media_names.tsv"]:
            file_path = tsv_dir / filename
            if not file_path.exists():
                continue

            logger.info(f"Loading {filename}...")
            with open(file_path, encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter="\t")
                for row in reader:
                    medium = {
                        "id": row.get("id") or row.get("media_id"),
                        "name": row.get("name") or row.get("media_name", ""),
                        "composition": [],
                    }
                    self.media.append(medium)
            return

    def _parse_compositions_tsv(self, tsv_dir: Path):
        """Parse media compositions TSV file."""
        for filename in ["media_compositions.txt", "compositions.tsv", "media_composition.tsv"]:
            file_path = tsv_dir / filename
            if not file_path.exists():
                continue

            logger.info(f"Loading {filename}...")
            with open(file_path, encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter="\t")
                for row in reader:
                    media_id = row.get("media_id") or row.get("medium_id")
                    compound_id = row.get("compound_id")

                    # Find the medium and add composition
                    for medium in self.media:
                        if medium["id"] == media_id:
                            medium["composition"].append(
                                {
                                    "compound_id": compound_id,
                                    "concentration": row.get("concentration", ""),
                                    "unit": row.get("unit", ""),
                                }
                            )
                            break
            return

    def _split_sql_records(self, values_str: str) -> list[str]:
        """Split `(...),(...),(...)` into records, respecting quotes and parens.

        This replaces `re.findall(r'\\(([^)]+)\\)', ...)`, whose `[^)]+` stopped at
        the FIRST closing paren. Any value containing one was truncated there,
        and the remaining columns of that row were lost:

            (16413,NULL,NULL,'Iron(III) chloride','','24380','30808','FeCl3')

        became the four fields `16413, NULL, NULL, 'Iron(III`, which is how
        `'Iron(III` ended up as an ingredient name in 75 recipes. Chemical
        names carry parentheses constantly — oxidation states, stereo
        descriptors — so this hit exactly the compounds hardest to re-derive.
        """
        records: list[str] = []
        field_start = None
        depth = 0
        in_quotes = False
        index = 0
        while index < len(values_str):
            char = values_str[index]
            if in_quotes:
                # MySQL dumps escape a quote as \' inside a quoted string.
                if char == "\\":
                    index += 2
                    continue
                if char == "'":
                    in_quotes = False
                index += 1
                continue
            if char == "'":
                in_quotes = True
            elif char == "(":
                depth += 1
                if depth == 1:
                    field_start = index + 1
            elif char == ")":
                depth -= 1
                if depth == 0 and field_start is not None:
                    records.append(values_str[field_start:index])
                    field_start = None
            index += 1
        return records

    def _split_sql_values(self, values: str) -> list[str]:
        """Split SQL values by comma, respecting quoted strings."""
        parts = []
        current = ""
        in_quotes = False
        quote_char = None

        index = 0
        while index < len(values):
            char = values[index]
            # A backslash escape. The dump writes chemical primes this way —
            # `'Pantetheine 4\\'-phosphate'` — and without this the escaped quote
            # was read as the end of the string, so quote tracking inverted and
            # every later comma in the row split in the wrong place. That is why
            # 48 compound names came out as fragments like
            # `'Pantetheine 4'-phosphate','cpd00834','115254','16858`.
            if in_quotes and char == "\\" and index + 1 < len(values):
                current += values[index : index + 2]
                index += 2
                continue
            if char in ('"', "'") and (not in_quotes or char == quote_char):
                in_quotes = not in_quotes
                quote_char = char if in_quotes else None
            elif char == "," and not in_quotes:
                parts.append(current.strip())
                current = ""
                index += 1
                continue
            current += char
            index += 1

        if current.strip():
            parts.append(current.strip())

        return parts

    def _clean_sql_value(self, value: str) -> str:
        """Clean SQL value (remove quotes, handle NULL, etc.)."""
        value = value.strip()

        # Handle NULL
        if value.upper() == "NULL":
            return ""

        # Remove quotes
        if (value.startswith("'") and value.endswith("'")) or (
            value.startswith('"') and value.endswith('"')
        ):
            value = value[1:-1]

        # Unescape
        value = value.replace("\\'", "'").replace('\\"', '"')

        return value

    def export_to_json(self):
        """Export fetched data to JSON files."""
        logger.info("Exporting to JSON...")

        # Export media
        media_file = self.output_dir / "mediadb_media.json"
        with open(media_file, "w", encoding="utf-8") as f:
            json.dump(
                {"count": len(self.media), "data": self.media}, f, indent=2, ensure_ascii=False
            )
        logger.info(f"✓ Saved {len(self.media)} media to {media_file}")

        # Export compounds
        compounds_file = self.output_dir / "mediadb_compounds.json"
        with open(compounds_file, "w", encoding="utf-8") as f:
            json.dump(
                {"count": len(self.compounds), "data": list(self.compounds.values())},
                f,
                indent=2,
                ensure_ascii=False,
            )
        logger.info(f"✓ Saved {len(self.compounds)} compounds to {compounds_file}")

        # Export organisms
        organisms_file = self.output_dir / "mediadb_organisms.json"
        with open(organisms_file, "w", encoding="utf-8") as f:
            json.dump(
                {"count": len(self.organisms), "data": list(self.organisms.values())},
                f,
                indent=2,
                ensure_ascii=False,
            )
        logger.info(f"✓ Saved {len(self.organisms)} organisms to {organisms_file}")

        # Export statistics
        stats = {
            "fetch_date": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "source": "MediaDB",
            "total_media": len(self.media),
            "total_compounds": len(self.compounds),
            "total_organisms": len(self.organisms),
            "url": "https://mediadb.systemsbiology.net/",
        }

        stats_file = self.output_dir / "fetch_stats.json"
        with open(stats_file, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)
        logger.info(f"✓ Saved statistics to {stats_file}")

    def fetch_all(self, sql_file: Path | None = None, tsv_dir: Path | None = None):
        """
        Fetch all MediaDB data using specified method.

        Args:
            sql_file: Path to SQL dump (preferred method)
            tsv_dir: Path to directory containing TSV exports
        """
        logger.info("=" * 60)
        logger.info("MediaDB Fetcher")
        logger.info("=" * 60)

        success = False

        # Try SQL dump first
        if sql_file:
            success = self.parse_sql_dump(sql_file)

        # Fallback to TSV
        elif tsv_dir:
            success = self.parse_tsv_exports(tsv_dir)

        else:
            logger.error("No data source specified!")
            logger.info("\nUsage:")
            logger.info("  --sql PATH       Parse SQL dump (recommended)")
            logger.info("  --tsv PATH       Parse TSV export directory")
            logger.info("\nNote: Download data from https://mediadb.systemsbiology.net/")
            return

        if not success:
            logger.error("✗ Failed to fetch MediaDB data")
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
    parser = argparse.ArgumentParser(description="Fetch MediaDB media database")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default="data/raw/mediadb",
        help="Output directory for fetched data",
    )
    parser.add_argument("--sql", type=Path, help="Path to MediaDB SQL dump file")
    parser.add_argument("--tsv", type=Path, help="Path to directory containing MediaDB TSV exports")

    args = parser.parse_args()

    fetcher = MediaDBFetcher(output_dir=args.output)
    fetcher.fetch_all(sql_file=args.sql, tsv_dir=args.tsv)


if __name__ == "__main__":
    main()
