"""Base classes for raw format converters."""

import argparse
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class ConversionSummary:
    """Machine-readable outcome for a directory conversion."""

    matched: int = 0
    converted: int = 0
    skipped: int = 0
    failed: int = 0
    failures: list[str] = field(default_factory=list)


class ConversionBatchError(RuntimeError):
    """Raised after a batch has produced one or more conversion failures."""

    def __init__(self, summary: ConversionSummary):
        self.summary = summary
        super().__init__(
            f"conversion failed for {summary.failed} of {summary.matched} matched file(s)"
        )


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
        self._source_root: Path | None = None

    def log(self, message: str, force: bool = False):
        """Log message if verbose mode enabled.

        Args:
            message: Message to log
            force: Log even if not verbose
        """
        if self.verbose or force:
            print(message)

    def add_source_metadata(self, record: dict[str, Any], source_file: Path) -> dict[str, Any]:
        """Add source tracking metadata to record.

        Args:
            record: Original record data
            source_file: Source file path

        Returns:
            Record with added _source metadata
        """
        source_path = source_file
        if self._source_root is not None:
            try:
                source_path = source_file.resolve().relative_to(self._source_root.parent)
            except ValueError:
                source_path = Path(source_file.name)
        record["_source"] = {
            "file": source_path.as_posix(),
            "layer": "raw_yaml",
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

    def convert_directory(
        self,
        input_dir: Path,
        output_dir: Path,
        pattern: str = "*",
        *,
        keep_going: bool = False,
        allow_empty: bool = False,
    ) -> ConversionSummary:
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

        files = sorted(input_dir.glob(pattern))
        summary = ConversionSummary(matched=len(files))
        if not files:
            message = f"No files matching '{pattern}' in {input_dir}"
            self.log(message, force=True)
            if allow_empty:
                self._log_summary(summary)
                return summary
            raise FileNotFoundError(f"{message}; pass --allow-empty only when this is expected")

        self.log(f"Found {len(files)} file(s) to convert", force=True)
        self._source_root = input_dir.resolve()

        for index, file_path in enumerate(files):
            if not file_path.is_file():
                summary.skipped += 1
                continue
            self.log(f"Converting: {file_path.name}")
            try:
                self.convert_file(file_path, output_dir)
                summary.converted += 1
            except Exception as error:
                summary.failed += 1
                summary.failures.append(f"{file_path}: {type(error).__name__}: {error}")
                self.log(f"Error converting {file_path}: {error}", force=True)
                if not keep_going:
                    summary.skipped += len(files) - index - 1
                    break

        self._log_summary(summary)
        if summary.failed:
            raise ConversionBatchError(summary)
        return summary

    def _log_summary(self, summary: ConversionSummary) -> None:
        self.log(
            "Conversion summary: "
            f"matched={summary.matched}, converted={summary.converted}, "
            f"skipped={summary.skipped}, failed={summary.failed}",
            force=True,
        )


def add_batch_arguments(parser: argparse.ArgumentParser) -> None:
    """Add consistent directory-conversion controls to an argparse parser."""
    parser.add_argument(
        "--keep-going",
        action="store_true",
        help="attempt remaining files after an error (the command still exits nonzero)",
    )
    parser.add_argument(
        "--allow-empty",
        action="store_true",
        help="succeed when no input files match",
    )


def batch_options(args: argparse.Namespace) -> dict[str, bool]:
    """Return keyword options shared by all converter entry points."""
    return {"keep_going": args.keep_going, "allow_empty": args.allow_empty}


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
            if "id" in record:
                filename = f"{record['id']}.yaml"
            elif "ID" in record:
                filename = f"{record['ID']}.yaml"
            else:
                filename = f"{input_file.stem}_{i:04d}.yaml"

            output_file = output_dir / filename

            # Write YAML (preserve order, don't sort keys)
            with open(output_file, "w") as f:
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

        with open(input_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter="\t")
            records = list(reader)

        if not records:
            self.log(f"  No records found in {input_file}")
            return

        for i, record in enumerate(records):
            # Remove None values from empty cells
            record = {k: v for k, v in record.items() if v is not None and v != ""}

            # Add source metadata
            record = self.add_source_metadata(record, input_file)

            # Generate output filename
            if "id" in record:
                filename = f"{record['id']}.yaml"
            elif "ID" in record:
                filename = f"{record['ID']}.yaml"
            elif "name" in record:
                # Sanitize name for filename
                safe_name = record["name"].replace(" ", "_").replace("/", "_")
                filename = f"{safe_name}.yaml"
            else:
                filename = f"{input_file.stem}_{i:04d}.yaml"

            output_file = output_dir / filename

            # Write YAML
            with open(output_file, "w") as f:
                yaml.dump(record, f, sort_keys=False, allow_unicode=True, default_flow_style=False)

        self.log(f"  Wrote {len(records)} record(s)")
