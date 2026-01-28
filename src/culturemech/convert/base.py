"""Base classes for raw format converters."""

import json
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

import yaml


class RawYAMLConverter(ABC):
    """Base class for converting raw sources to raw YAML.

    This converter performs mechanical format conversion without any
    normalization or validation. It preserves the original structure
    and field names exactly as they appear in the source.

    Subclasses should implement:
    - convert_file() to handle single file conversion
    - _process_record() to add source metadata (optional)
    """

    def __init__(self, verbose: bool = False):
        """Initialize converter.

        Args:
            verbose: Enable verbose logging
        """
        self.verbose = verbose

    def log(self, message: str, force: bool = False):
        """Log message if verbose mode enabled.

        Args:
            message: Message to log
            force: Log even if not verbose
        """
        if self.verbose or force:
            print(message)

    def add_source_metadata(self, record: Dict[str, Any], source_file: Path) -> Dict[str, Any]:
        """Add source tracking metadata to record.

        Args:
            record: Original record data
            source_file: Source file path

        Returns:
            Record with added _source metadata
        """
        record['_source'] = {
            'file': str(source_file.resolve()),
            'timestamp': datetime.now().isoformat(),
            'layer': 'raw_yaml'
        }
        return record

    @abstractmethod
    def convert_file(self, input_file: Path, output_dir: Path):
        """Convert a single raw file to raw YAML format.

        Args:
            input_file: Path to input file (JSON, TSV, etc.)
            output_dir: Directory to write output YAML files
        """
        pass

    def convert_directory(self, input_dir: Path, output_dir: Path, pattern: str = "*"):
        """Convert all matching files in a directory.

        Args:
            input_dir: Input directory containing raw files
            output_dir: Output directory for raw YAML files
            pattern: Glob pattern for files to convert (e.g., "*.json")
        """
        input_dir = Path(input_dir)
        output_dir = Path(output_dir)

        if not input_dir.exists():
            raise FileNotFoundError(f"Input directory not found: {input_dir}")

        output_dir.mkdir(parents=True, exist_ok=True)

        files = list(input_dir.glob(pattern))
        if not files:
            self.log(f"No files matching '{pattern}' in {input_dir}", force=True)
            return

        self.log(f"Found {len(files)} file(s) to convert", force=True)

        for file_path in files:
            if file_path.is_file():
                self.log(f"Converting: {file_path.name}")
                try:
                    self.convert_file(file_path, output_dir)
                except Exception as e:
                    self.log(f"Error converting {file_path}: {e}", force=True)


class JSONToRawYAMLConverter(RawYAMLConverter):
    """Convert JSON files to raw YAML format.

    Performs direct 1:1 conversion of JSON to YAML with no transformations.
    Preserves all field names and nested structures exactly.
    """

    def convert_file(self, input_file: Path, output_dir: Path):
        """Convert JSON file to raw YAML.

        Args:
            input_file: Path to JSON file
            output_dir: Directory to write YAML files
        """
        with open(input_file) as f:
            data = json.load(f)

        # Handle different JSON structures
        if isinstance(data, dict):
            # Single record
            records = [data]
        elif isinstance(data, list):
            # Array of records
            records = data
        else:
            raise ValueError(f"Unexpected JSON structure in {input_file}")

        output_dir.mkdir(parents=True, exist_ok=True)

        for i, record in enumerate(records):
            # Add source metadata
            record = self.add_source_metadata(record, input_file)

            # Generate output filename
            if 'id' in record:
                filename = f"{record['id']}.yaml"
            elif 'ID' in record:
                filename = f"{record['ID']}.yaml"
            else:
                filename = f"{input_file.stem}_{i:04d}.yaml"

            output_file = output_dir / filename

            # Write YAML (preserve order, don't sort keys)
            with open(output_file, 'w') as f:
                yaml.dump(record, f, sort_keys=False, allow_unicode=True, default_flow_style=False)

        self.log(f"  Wrote {len(records)} record(s)")


class TSVToRawYAMLConverter(RawYAMLConverter):
    """Convert TSV files to raw YAML format.

    Converts each TSV row into a YAML file, preserving column names
    as field names and values as-is (no type conversion).
    """

    def convert_file(self, input_file: Path, output_dir: Path):
        """Convert TSV file to raw YAML files.

        Args:
            input_file: Path to TSV file
            output_dir: Directory to write YAML files
        """
        import csv

        output_dir.mkdir(parents=True, exist_ok=True)

        with open(input_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            records = list(reader)

        if not records:
            self.log(f"  No records found in {input_file}")
            return

        for i, record in enumerate(records):
            # Remove None values from empty cells
            record = {k: v for k, v in record.items() if v is not None and v != ''}

            # Add source metadata
            record = self.add_source_metadata(record, input_file)

            # Generate output filename
            if 'id' in record:
                filename = f"{record['id']}.yaml"
            elif 'ID' in record:
                filename = f"{record['ID']}.yaml"
            elif 'name' in record:
                # Sanitize name for filename
                safe_name = record['name'].replace(' ', '_').replace('/', '_')
                filename = f"{safe_name}.yaml"
            else:
                filename = f"{input_file.stem}_{i:04d}.yaml"

            output_file = output_dir / filename

            # Write YAML
            with open(output_file, 'w') as f:
                yaml.dump(record, f, sort_keys=False, allow_unicode=True, default_flow_style=False)

        self.log(f"  Wrote {len(records)} record(s)")
