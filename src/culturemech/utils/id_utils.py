"""Generic ID utilities for X-Mech repositories.

This module provides reusable functions for managing stable, sequential identifiers
across X-Mech repositories (MediaIngredientMech, CultureMech, CommunityMech, etc.).

Standard ID format: RepoName:NNNNNN (e.g., CultureMech:000001)

Usage:
    from culturemech.utils.id_utils import mint_next_id, generate_xmech_id

    # Mint next ID for multi-file collection with registry
    next_id = mint_next_id(
        Path('data/normalized_yaml'),
        'CultureMech',
        'multi_file'
    )

    # Or use registry for faster lookup
    from culturemech.utils.id_utils import find_highest_id_from_registry
    registry_path = Path('data/culturemech_id_registry.tsv')
    highest = find_highest_id_from_registry(registry_path, 'CultureMech')
    next_id = generate_xmech_id('CultureMech', highest + 1)

This module can be copied to other X-Mech repositories with minimal modifications.
"""

import re
import yaml
from pathlib import Path
from typing import Optional


def parse_xmech_id(id_string: str, expected_prefix: str) -> Optional[int]:
    """Parse X-Mech ID and return number part.

    Args:
        id_string: ID to parse (e.g., "CultureMech:000001")
        expected_prefix: Expected prefix (e.g., "CultureMech")

    Returns:
        ID number (e.g., 1) or None if invalid

    Examples:
        >>> parse_xmech_id("CultureMech:000001", "CultureMech")
        1

        >>> parse_xmech_id("CultureMech:015431", "CultureMech")
        15431

        >>> parse_xmech_id("InvalidID", "CultureMech")
        None

        >>> parse_xmech_id("MediaIngredientMech:000001", "CultureMech")
        None
    """
    if not id_string or not id_string.startswith(f"{expected_prefix}:"):
        return None

    try:
        return int(id_string.split(':', 1)[1])
    except (IndexError, ValueError):
        return None


def generate_xmech_id(prefix: str, number: int) -> str:
    """Generate formatted X-Mech ID with zero-padding.

    Args:
        prefix: Repository name (e.g., "CultureMech")
        number: Sequential number (1-999999)

    Returns:
        Formatted ID (e.g., "CultureMech:000001")

    Examples:
        >>> generate_xmech_id("CultureMech", 1)
        'CultureMech:000001'

        >>> generate_xmech_id("CultureMech", 15431)
        'CultureMech:015431'

        >>> generate_xmech_id("MediaIngredientMech", 113)
        'MediaIngredientMech:000113'
    """
    return f"{prefix}:{number:06d}"


def validate_id_format(id_string: str, prefix: str) -> bool:
    """Validate ID matches expected format.

    Args:
        id_string: ID to validate
        prefix: Expected prefix

    Returns:
        True if valid, False otherwise

    Examples:
        >>> validate_id_format("CultureMech:000001", "CultureMech")
        True

        >>> validate_id_format("CultureMech:1", "CultureMech")
        False  # Not zero-padded

        >>> validate_id_format("MediaIngredientMech:000001", "CultureMech")
        False  # Wrong prefix

        >>> validate_id_format("Invalid:ID", "Invalid")
        False  # Wrong format
    """
    pattern = rf'^{re.escape(prefix)}:\d{{6}}$'
    return bool(re.match(pattern, id_string))


def find_highest_id_single_file(
    yaml_path: Path,
    prefix: str,
    collection_key: str = "ingredients"
) -> int:
    """Find highest ID in single-file YAML collection.

    For repositories that store all records in a single YAML file with a
    collection key (e.g., MediaIngredientMech).

    Args:
        yaml_path: Path to YAML file
        prefix: ID prefix (e.g., "MediaIngredientMech")
        collection_key: YAML key for collection (e.g., "ingredients")

    Returns:
        Highest ID number (0 if none found)

    Examples:
        >>> # For MediaIngredientMech
        >>> find_highest_id_single_file(
        ...     Path('data/curated/unmapped_ingredients.yaml'),
        ...     'MediaIngredientMech',
        ...     'ingredients'
        ... )
        112
    """
    try:
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        return 0

    if not data:
        return 0

    max_id = 0
    for record in data.get(collection_key, []):
        id_str = record.get('id', '')
        if id_num := parse_xmech_id(id_str, prefix):
            max_id = max(max_id, id_num)

    return max_id


def find_highest_id_multi_file(
    directory: Path,
    prefix: str,
    pattern: str = "*.yaml"
) -> int:
    """Find highest ID across multiple YAML files.

    For repositories that store each record in a separate YAML file
    (e.g., CultureMech, CommunityMech).

    Args:
        directory: Directory to search (recursive)
        prefix: ID prefix (e.g., "CultureMech")
        pattern: Glob pattern for files (default: "*.yaml")

    Returns:
        Highest ID number (0 if none found)

    Examples:
        >>> # For CommunityMech
        >>> find_highest_id_multi_file(
        ...     Path('kb/communities'),
        ...     'CommunityMech'
        ... )
        78

        >>> # For CultureMech with nested directories
        >>> find_highest_id_multi_file(
        ...     Path('data/normalized_yaml'),
        ...     'CultureMech'
        ... )
        15431
    """
    if not directory.exists():
        return 0

    max_id = 0

    for yaml_file in directory.rglob(pattern):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            if not data:
                continue

            id_str = data.get('id', '')
            if id_num := parse_xmech_id(id_str, prefix):
                max_id = max(max_id, id_num)
        except Exception:
            # Skip files that can't be parsed
            continue

    return max_id


def find_highest_id_from_registry(
    registry_path: Path,
    prefix: str = "CultureMech",
    id_column: str = "culturemech_id"
) -> int:
    """Find highest ID from TSV registry file.

    For CultureMech which maintains an ID registry for faster lookups.

    Args:
        registry_path: Path to registry TSV
        prefix: ID prefix (e.g., "CultureMech")
        id_column: Column name containing IDs (default: "culturemech_id")

    Returns:
        Highest ID number (0 if none found)

    Examples:
        >>> find_highest_id_from_registry(
        ...     Path('data/culturemech_id_registry.tsv'),
        ...     'CultureMech'
        ... )
        15431
    """
    try:
        import pandas as pd
        registry = pd.read_csv(registry_path, sep='\t')
    except (FileNotFoundError, ImportError):
        return 0

    max_id = 0
    for id_str in registry[id_column]:
        if id_num := parse_xmech_id(str(id_str), prefix):
            max_id = max(max_id, id_num)

    return max_id


def mint_next_id(
    source: Path,
    prefix: str,
    collection_type: str = "multi_file",
    collection_key: str = "ingredients"
) -> str:
    """Mint next available ID for a collection.

    This is the main function for generating new IDs. It automatically
    finds the highest existing ID and returns the next sequential ID.

    Args:
        source: Path to YAML file (single_file) or directory (multi_file)
        prefix: ID prefix / repository name
        collection_type: "single_file" or "multi_file"
        collection_key: Collection key name (for single_file type only)

    Returns:
        Next available ID string

    Raises:
        ValueError: If collection_type is invalid

    Examples:
        >>> # CultureMech (multi-file with nested dirs)
        >>> mint_next_id(
        ...     Path('data/normalized_yaml'),
        ...     'CultureMech',
        ...     'multi_file'
        ... )
        'CultureMech:015432'

        >>> # MediaIngredientMech (single-file)
        >>> mint_next_id(
        ...     Path('data/curated/unmapped_ingredients.yaml'),
        ...     'MediaIngredientMech',
        ...     'single_file',
        ...     'ingredients'
        ... )
        'MediaIngredientMech:000113'

        >>> # CommunityMech (multi-file)
        >>> mint_next_id(
        ...     Path('kb/communities'),
        ...     'CommunityMech',
        ...     'multi_file'
        ... )
        'CommunityMech:000079'
    """
    if collection_type == "single_file":
        highest = find_highest_id_single_file(source, prefix, collection_key)
    elif collection_type == "multi_file":
        highest = find_highest_id_multi_file(source, prefix)
    else:
        raise ValueError(
            f"Unknown collection_type: {collection_type}. "
            f"Must be 'single_file' or 'multi_file'"
        )

    return generate_xmech_id(prefix, highest + 1)


def find_duplicate_ids_single_file(
    yaml_path: Path,
    collection_key: str = "ingredients"
) -> list[str]:
    """Find duplicate IDs in single-file collection.

    Args:
        yaml_path: Path to YAML file
        collection_key: Collection key name

    Returns:
        List of duplicate IDs (empty if none found)

    Examples:
        >>> find_duplicate_ids_single_file(
        ...     Path('data/curated/unmapped_ingredients.yaml')
        ... )
        []  # No duplicates
    """
    from collections import Counter

    try:
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        return []

    if not data:
        return []

    ids = [record.get('id') for record in data.get(collection_key, [])]
    counts = Counter(ids)

    duplicates = [id_str for id_str, count in counts.items() if count > 1 and id_str is not None]
    return duplicates


def find_duplicate_ids_multi_file(
    directory: Path,
    pattern: str = "*.yaml"
) -> dict[str, list[Path]]:
    """Find duplicate IDs across multiple files.

    Args:
        directory: Directory to search (recursive)
        pattern: Glob pattern for files

    Returns:
        Dict mapping duplicate IDs to list of files containing them

    Examples:
        >>> duplicates = find_duplicate_ids_multi_file(
        ...     Path('data/normalized_yaml')
        ... )
        >>> if duplicates:
        ...     for id_str, files in duplicates.items():
        ...         print(f"{id_str} in {len(files)} files")
    """
    from collections import defaultdict

    if not directory.exists():
        return {}

    id_to_files = defaultdict(list)

    for yaml_file in directory.rglob(pattern):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            if not data:
                continue

            id_str = data.get('id')
            if id_str:
                id_to_files[id_str].append(yaml_file)
        except Exception:
            continue

    # Filter to only duplicates
    duplicates = {id_str: files for id_str, files in id_to_files.items() if len(files) > 1}
    return duplicates


def find_id_gaps(
    yaml_path: Path,
    prefix: str,
    collection_key: str = "ingredients"
) -> list[int]:
    """Find gaps in ID sequence for single-file collection.

    Args:
        yaml_path: Path to YAML file
        prefix: ID prefix
        collection_key: Collection key name

    Returns:
        List of missing ID numbers in sequence

    Examples:
        >>> # If IDs are 1, 2, 4, 5 (missing 3)
        >>> find_id_gaps(
        ...     Path('data/curated/unmapped_ingredients.yaml'),
        ...     'MediaIngredientMech'
        ... )
        [3]
    """
    try:
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        return []

    if not data:
        return []

    ids = []
    for record in data.get(collection_key, []):
        id_str = record.get('id', '')
        if id_num := parse_xmech_id(id_str, prefix):
            ids.append(id_num)

    if not ids:
        return []

    ids.sort()

    # Find gaps
    expected = set(range(ids[0], ids[-1] + 1))
    actual = set(ids)
    gaps = sorted(expected - actual)

    return gaps


def rebuild_culturemech_registry(
    base_dir: Path = Path('data/normalized_yaml'),
    output_path: Path = Path('data/culturemech_id_registry.tsv')
) -> int:
    """Rebuild CultureMech ID registry from YAML files.

    Scans all YAML files in the directory tree and creates a fresh
    registry mapping CultureMech IDs to file paths.

    Args:
        base_dir: Base directory to scan
        output_path: Output path for registry TSV

    Returns:
        Number of records added to registry

    Examples:
        >>> count = rebuild_culturemech_registry()
        >>> print(f"Rebuilt registry with {count} entries")
    """
    try:
        import pandas as pd
    except ImportError:
        print("Error: pandas is required for registry operations")
        return 0

    records = []

    for yaml_file in base_dir.rglob('*.yaml'):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            if not data:
                continue

            id_str = data.get('id')
            if id_str and id_str.startswith('CultureMech:'):
                records.append({
                    'culturemech_id': id_str,
                    'file_path': str(yaml_file)
                })
        except Exception:
            continue

    df = pd.DataFrame(records).sort_values('culturemech_id')
    df.to_csv(output_path, sep='\t', index=False)

    return len(df)


# Example usage and tests
if __name__ == "__main__":
    """Example usage for CultureMech and other X-Mech repositories."""

    print("=== X-Mech ID Utilities Example Usage ===\n")

    # Example 1: CultureMech (multi-file with registry)
    print("1. CultureMech (multi-file collection with registry)")

    # Option 1: Use registry for fast lookup
    registry_path = Path('data/culturemech_id_registry.tsv')
    if registry_path.exists():
        highest = find_highest_id_from_registry(registry_path, 'CultureMech')
        next_id = generate_xmech_id('CultureMech', highest + 1)
        print(f"   Registry lookup:")
        print(f"   - Highest ID: {highest}")
        print(f"   - Next ID: {next_id}")
    else:
        print(f"   Registry not found: {registry_path}")

    # Option 2: Scan files directly (slower but works without registry)
    base_dir = Path('data/normalized_yaml')
    if base_dir.exists():
        highest = find_highest_id_multi_file(base_dir, 'CultureMech')
        next_id = generate_xmech_id('CultureMech', highest + 1)
        print(f"   File scan:")
        print(f"   - Highest ID: {highest}")
        print(f"   - Next ID: {next_id}")

        # Check for duplicates
        duplicates = find_duplicate_ids_multi_file(base_dir)
        print(f"   - Duplicates: {len(duplicates) if duplicates else 'None'}")
    else:
        print(f"   Directory not found: {base_dir}")

    print()

    # Example 2: Validation
    print("2. ID Validation Examples")
    test_ids = [
        ("CultureMech:000001", "CultureMech"),
        ("CultureMech:015431", "CultureMech"),
        ("CultureMech:1", "CultureMech"),  # Invalid (no padding)
        ("MediaIngredientMech:000001", "CultureMech"),  # Wrong prefix
    ]

    for id_str, prefix in test_ids:
        is_valid = validate_id_format(id_str, prefix)
        status = "✓" if is_valid else "✗"
        print(f"   {status} {id_str} (prefix: {prefix})")

    print()

    # Example 3: Parsing IDs
    print("3. ID Parsing Examples")
    test_parse = [
        ("CultureMech:000001", "CultureMech"),
        ("CultureMech:015431", "CultureMech"),
        ("MediaIngredientMech:000113", "MediaIngredientMech"),
    ]

    for id_str, prefix in test_parse:
        number = parse_xmech_id(id_str, prefix)
        print(f"   {id_str} → {number}")

    print()

    # Example 4: Minting function
    print("4. Complete Minting Workflow")
    print("   # Multi-file collection with registry")
    print("   next_id = mint_next_id(")
    print("       Path('data/normalized_yaml'),")
    print("       'CultureMech',")
    print("       'multi_file'")
    print("   )")
    print()
    print("   # Or use registry for faster lookup:")
    print("   registry_path = Path('data/culturemech_id_registry.tsv')")
    print("   highest = find_highest_id_from_registry(registry_path, 'CultureMech')")
    print("   next_id = generate_xmech_id('CultureMech', highest + 1)")
