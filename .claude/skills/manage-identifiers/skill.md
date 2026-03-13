---
name: manage-identifiers
description: Generic identifier management for X-Mech repositories - finding highest IDs, minting new IDs, and adding records with proper ID placement
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
---

# Identifier Management for X-Mech Repositories

## Overview

**Purpose**: Maintain stable, sequential identifiers across X-Mech repositories (MediaIngredientMech, CultureMech, CommunityMech, and future projects) to ensure data integrity, enable cross-references, and support knowledge graph integration.

**Why**: Identifiers provide persistent references for records, enable semantic linking in knowledge graphs, support data provenance tracking, and maintain consistency across datasets.

**Scope**: All X-Mech repositories that use the standard identifier format `RepoName:NNNNNN` where NNNNNN is a zero-padded 6-digit sequential number.

## When to Use This Skill

Use this skill when:
- Adding new records to any X-Mech repository
- Finding the next available ID for a new record
- Understanding how to mint IDs for different collection types
- Running batch ID assignment operations
- Validating ID sequences and checking for duplicates or gaps
- Setting up a new X-Mech repository with identifier infrastructure
- Troubleshooting ID-related issues (conflicts, formatting, gaps)

## Identifier Format

### Standard Format

```
RepoName:NNNNNN
```

**Components:**
- `RepoName`: Repository name (e.g., MediaIngredientMech, CultureMech, CommunityMech)
- `:`: Separator (colon)
- `NNNNNN`: Zero-padded 6-digit sequential number (000001 to 999999)

**Examples:**
- `MediaIngredientMech:000001` - First ingredient
- `CultureMech:015431` - 15,431st medium
- `CommunityMech:000078` - 78th community

### Why This Format?

1. **Human-readable**: Easy to recognize and parse
2. **Sortable**: Alphabetical sort = numerical sort (due to zero-padding)
3. **Stable**: Never changes once assigned (independent of content)
4. **Unique**: Guaranteed uniqueness within repository
5. **Cross-referenceable**: Easy to link between repositories
6. **KG-compatible**: Works as RDF subject/object in knowledge graphs

## Collection Types

X-Mech repositories use two main patterns for organizing records:

### Type 1: Single-File Collection

**Pattern**: All records stored in one YAML file with a collection key

**Example Repository**: MediaIngredientMech

**Structure**:
```yaml
generation_date: '2026-03-09T06:54:18.022301+00:00'
total_count: 112
mapped_count: 65
unmapped_count: 47
ingredients:  # <-- Collection key
  - id: MediaIngredientMech:000001
    preferred_term: Sodium chloride
    mapping_status: MAPPED
    # ... other fields

  - id: MediaIngredientMech:000002
    preferred_term: Glucose
    mapping_status: MAPPED
    # ... other fields
```

**Characteristics**:
- ✓ Simple to manage (one file)
- ✓ Easy to see all records at once
- ✓ Good for <1000 records
- ✗ Large files can be slow to load/edit
- ✗ Git merge conflicts more likely

**Files**:
- Data: `data/curated/unmapped_ingredients.yaml`
- ID script: `scripts/add_mediaingredientmech_ids.py`

### Type 2: Multi-File Collection

**Pattern**: Each record is a separate YAML file in a directory hierarchy

**Example Repositories**: CultureMech, CommunityMech

**Structure**:
```
data/normalized_yaml/
├── bacterial/
│   ├── LB_Medium.yaml        # id: CultureMech:000001
│   ├── TSA_Medium.yaml       # id: CultureMech:000002
│   └── ...
├── algae/
│   ├── BG11_Medium.yaml      # id: CultureMech:000500
│   └── ...
└── fungi/
    └── PDA_Medium.yaml       # id: CultureMech:001000
```

**Each file contains**:
```yaml
id: CultureMech:000001
name: LB Medium
category: bacterial
# ... other fields
```

**Characteristics**:
- ✓ Scales well (1000s of records)
- ✓ Smaller git diffs (one file per change)
- ✓ Parallel editing easier
- ✗ More complex to manage
- ✗ Need to scan all files to find highest ID

**CultureMech adds**: ID registry file (`data/culturemech_id_registry.tsv`)
```tsv
culturemech_id	file_path
CultureMech:000001	data/normalized_yaml/bacterial/LB_Medium.yaml
CultureMech:000002	data/normalized_yaml/bacterial/TSA_Medium.yaml
```

**Files**:
- Data: `data/normalized_yaml/**/*.yaml`
- ID script: `scripts/assign_culturemech_ids.py` (with registry)
- Registry: `data/culturemech_id_registry.tsv` (CultureMech only)

### Comparison Table

| Feature | Single-File | Multi-File | Multi-File + Registry |
|---------|-------------|------------|----------------------|
| **Repo Example** | MediaIngredientMech | CommunityMech | CultureMech |
| **Record Count** | 112 | 78 | 15,431 |
| **Find Highest ID** | Parse YAML once | Scan all files | Read registry file |
| **Add New Record** | Append to list | Create new file | Create file + update registry |
| **Git Conflicts** | More likely | Rare | Rare |
| **Scalability** | <1000 records | <10,000 records | 10,000+ records |
| **Complexity** | Low | Medium | Medium-High |

## Finding the Highest ID

Before minting a new ID, you need to find the current maximum ID number.

### Method 1: Single-File Collection (MediaIngredientMech)

**Python approach**:
```python
import yaml
import re
from pathlib import Path

def find_highest_id_single_file(
    yaml_path: Path,
    prefix: str = "MediaIngredientMech",
    collection_key: str = "ingredients"
) -> int:
    """Find highest ID in single-file YAML collection.

    Args:
        yaml_path: Path to YAML file
        prefix: ID prefix (e.g., "MediaIngredientMech")
        collection_key: YAML key for collection (e.g., "ingredients")

    Returns:
        Highest ID number (0 if none found)
    """
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    max_id = 0
    for record in data.get(collection_key, []):
        id_str = record.get('id', '')
        if match := re.match(rf'{prefix}:(\d+)', id_str):
            max_id = max(max_id, int(match.group(1)))

    return max_id

# Usage
yaml_path = Path('data/curated/unmapped_ingredients.yaml')
highest = find_highest_id_single_file(yaml_path, 'MediaIngredientMech', 'ingredients')
print(f"Highest ID: {highest}")  # Output: 112
```

**Quick bash one-liner**:
```bash
# MediaIngredientMech
grep -o 'MediaIngredientMech:[0-9]\+' data/curated/unmapped_ingredients.yaml | \
  cut -d: -f2 | sort -n | tail -1
```

### Method 2: Multi-File Collection (CommunityMech)

**Python approach**:
```python
import yaml
import re
from pathlib import Path

def find_highest_id_multi_file(
    directory: Path,
    prefix: str = "CommunityMech",
    pattern: str = "*.yaml"
) -> int:
    """Find highest ID across multiple YAML files.

    Args:
        directory: Directory to search
        prefix: ID prefix (e.g., "CommunityMech")
        pattern: Glob pattern for files (default: "*.yaml")

    Returns:
        Highest ID number (0 if none found)
    """
    max_id = 0

    for yaml_file in directory.glob(pattern):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            id_str = data.get('id', '')
            if match := re.match(rf'{prefix}:(\d+)', id_str):
                max_id = max(max_id, int(match.group(1)))
        except Exception as e:
            print(f"Error reading {yaml_file}: {e}")
            continue

    return max_id

# Usage
communities_dir = Path('kb/communities')
highest = find_highest_id_multi_file(communities_dir, 'CommunityMech')
print(f"Highest ID: {highest}")  # Output: 78
```

**Recursive search** (for nested directories):
```python
def find_highest_id_recursive(
    base_dir: Path,
    prefix: str = "CultureMech"
) -> int:
    """Recursively find highest ID in directory tree."""
    max_id = 0

    for yaml_file in base_dir.rglob('*.yaml'):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            id_str = data.get('id', '')
            if match := re.match(rf'{prefix}:(\d+)', id_str):
                max_id = max(max_id, int(match.group(1)))
        except Exception:
            continue

    return max_id

# Usage for CultureMech with nested dirs
base_dir = Path('data/normalized_yaml')
highest = find_highest_id_recursive(base_dir, 'CultureMech')
print(f"Highest ID: {highest}")  # Output: 15431
```

**Quick bash approach**:
```bash
# CommunityMech (single directory)
grep -rh 'id: CommunityMech:' kb/communities/ | \
  cut -d: -f3 | sort -n | tail -1

# CultureMech (nested directories)
find data/normalized_yaml -name "*.yaml" -exec grep -h 'id: CultureMech:' {} \; | \
  cut -d: -f3 | sort -n | tail -1
```

### Method 3: Using Registry File (CultureMech)

**Python approach**:
```python
import pandas as pd
import re

def find_highest_id_from_registry(
    registry_path: Path,
    prefix: str = "CultureMech"
) -> int:
    """Find highest ID from TSV registry file.

    Args:
        registry_path: Path to registry TSV
        prefix: ID prefix (e.g., "CultureMech")

    Returns:
        Highest ID number (0 if none found)
    """
    registry = pd.read_csv(registry_path, sep='\t')

    max_id = 0
    for id_str in registry['culturemech_id']:
        if match := re.match(rf'{prefix}:(\d+)', id_str):
            max_id = max(max_id, int(match.group(1)))

    return max_id

# Usage
registry_path = Path('data/culturemech_id_registry.tsv')
highest = find_highest_id_from_registry(registry_path, 'CultureMech')
print(f"Highest ID: {highest}")  # Output: 15431
```

**Bash approach**:
```bash
# Quick lookup from registry
tail -n +2 data/culturemech_id_registry.tsv | \
  cut -f1 | cut -d: -f2 | sort -n | tail -1
```

## Minting New IDs

Once you know the highest ID, minting a new ID is straightforward.

### Basic ID Generation

**Python function**:
```python
def generate_xmech_id(prefix: str, number: int) -> str:
    """Generate formatted X-Mech ID.

    Args:
        prefix: Repository name (e.g., "CultureMech")
        number: Sequential number (1-999999)

    Returns:
        Formatted ID (e.g., "CultureMech:000001")

    Examples:
        >>> generate_xmech_id("MediaIngredientMech", 1)
        'MediaIngredientMech:000001'

        >>> generate_xmech_id("CultureMech", 15431)
        'CultureMech:015431'
    """
    return f"{prefix}:{number:06d}"

# Usage
new_id = generate_xmech_id("CultureMech", 15432)
print(new_id)  # Output: CultureMech:015432
```

### Complete Minting Workflow

**Generic mint function**:
```python
from pathlib import Path

def mint_next_id(
    source: Path,
    prefix: str,
    collection_type: str = "single_file",
    collection_key: str = "ingredients"
) -> str:
    """Mint next available ID for a collection.

    Args:
        source: Path to YAML file or directory
        prefix: ID prefix (repo name)
        collection_type: "single_file" or "multi_file"
        collection_key: Collection key name (for single_file type)

    Returns:
        Next available ID string

    Examples:
        >>> # Single-file collection
        >>> mint_next_id(
        ...     Path('data/curated/unmapped_ingredients.yaml'),
        ...     'MediaIngredientMech',
        ...     'single_file',
        ...     'ingredients'
        ... )
        'MediaIngredientMech:000113'

        >>> # Multi-file collection
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
        raise ValueError(f"Unknown collection_type: {collection_type}")

    next_number = highest + 1
    return generate_xmech_id(prefix, next_number)
```

### Quick Mint Examples

**CultureMech** (multi-file + registry):
```python
from pathlib import Path

# Option 1: From registry (fastest)
registry_path = Path('data/culturemech_id_registry.tsv')
highest = find_highest_id_from_registry(registry_path, 'CultureMech')
next_id = generate_xmech_id('CultureMech', highest + 1)
print(f"Next ID: {next_id}")  # CultureMech:015432

# Option 2: Scan files (slower but works if registry is missing)
base_dir = Path('data/normalized_yaml')
highest = find_highest_id_multi_file(base_dir, 'CultureMech')
next_id = generate_xmech_id('CultureMech', highest + 1)
print(f"Next ID: {next_id}")  # CultureMech:015432
```

## Adding New Records

### Workflow: Multi-File + Registry (CultureMech)

**Step-by-step process**:

```python
import yaml
import pandas as pd
from pathlib import Path
from datetime import datetime, timezone

# Step 1: Find next ID from registry
registry_path = Path('data/culturemech_id_registry.tsv')
registry = pd.read_csv(registry_path, sep='\t')
highest = find_highest_id_from_registry(registry_path, 'CultureMech')
next_id = generate_xmech_id('CultureMech', highest + 1)

# Step 2: Create new record
new_medium = {
    'id': next_id,  # ALWAYS first field
    'name': 'New Medium Name',
    'original_name': 'New Medium Name',
    'category': 'bacterial',  # bacterial, algae, fungi, etc.
    'medium_type': 'COMPLEX',
    'physical_state': 'SOLID_AGAR',
    'ph_value': 7.0,
    'ingredients': [],
    'applications': ['Microbial cultivation'],
    'curation_history': [
        {
            'timestamp': datetime.now(timezone.utc).isoformat() + 'Z',
            'curator': 'manual_addition',
            'action': 'Created new medium',
            'notes': f'Manually added medium with ID {next_id}'
        }
    ]
}

# Step 3: Determine output path (based on category)
category = new_medium['category']
safe_name = new_medium['name'].replace(' ', '_').replace('/', '_')
output_path = Path(f'data/normalized_yaml/{category}/{safe_name}.yaml')

# Ensure category directory exists
output_path.parent.mkdir(parents=True, exist_ok=True)

# Step 4: Save to new file
with open(output_path, 'w') as f:
    yaml.dump(
        new_medium,
        f,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True
    )

# Step 5: Update registry
new_entry = pd.DataFrame({
    'culturemech_id': [next_id],
    'file_path': [str(output_path)]
})
registry = pd.concat([registry, new_entry], ignore_index=True)
registry.to_csv(registry_path, sep='\t', index=False)

print(f"✓ Created {next_id} → {output_path}")
print(f"✓ Updated registry: {registry_path}")
```

**Key points**:
- ✓ Read registry to find highest ID
- ✓ Create file in category-specific directory
- ✓ Update registry with new ID and path
- ✓ Registry columns: `culturemech_id`, `file_path`
- ✓ `id` field ALWAYS first in YAML

## Batch ID Assignment

For bulk operations, use the existing repository-specific scripts.

### CultureMech Batch Assignment

**Script**: `scripts/assign_culturemech_ids.py`

**Usage**:
```bash
# Preview changes (dry-run)
python scripts/assign_culturemech_ids.py --dry-run

# Execute assignment
python scripts/assign_culturemech_ids.py

# Custom start ID
python scripts/assign_culturemech_ids.py --start-id 15432

# Custom paths
python scripts/assign_culturemech_ids.py \
  --input-dir data/normalized_yaml \
  --registry-output data/culturemech_id_registry.tsv
```

**Features**:
- ✓ Scans all YAML files recursively
- ✓ Finds highest existing ID automatically
- ✓ Assigns IDs to files without them
- ✓ Generates ID registry TSV
- ✓ Sorted processing for deterministic ordering
- ✓ Comprehensive reporting

## Validation and Troubleshooting

### Validating ID Format

**Python validator**:
```python
import re

def validate_id_format(id_string: str, prefix: str) -> bool:
    """Validate ID matches expected format.

    Args:
        id_string: ID to validate (e.g., "CultureMech:000001")
        prefix: Expected prefix (e.g., "CultureMech")

    Returns:
        True if valid, False otherwise

    Examples:
        >>> validate_id_format("CultureMech:000001", "CultureMech")
        True

        >>> validate_id_format("CultureMech:1", "CultureMech")
        False  # Not zero-padded

        >>> validate_id_format("MediaIngredientMech:000001", "CultureMech")
        False  # Wrong prefix
    """
    pattern = rf'^{re.escape(prefix)}:\d{{6}}$'
    return bool(re.match(pattern, id_string))

# Usage
is_valid = validate_id_format("CultureMech:015431", "CultureMech")
print(f"Valid: {is_valid}")  # True
```

### Finding Duplicate IDs

**Multi-file collection**:
```python
from collections import defaultdict

def find_duplicate_ids_multi_file(directory: Path) -> dict[str, list[Path]]:
    """Find duplicate IDs across multiple files."""
    id_to_files = defaultdict(list)

    for yaml_file in directory.rglob('*.yaml'):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            id_str = data.get('id')
            if id_str:
                id_to_files[id_str].append(yaml_file)
        except Exception:
            continue

    # Filter to only duplicates
    duplicates = {id_str: files for id_str, files in id_to_files.items() if len(files) > 1}
    return duplicates

# Usage
base_dir = Path('data/normalized_yaml')
duplicates = find_duplicate_ids_multi_file(base_dir)
if duplicates:
    for id_str, files in duplicates.items():
        print(f"⚠️  {id_str} found in {len(files)} files:")
        for file in files:
            print(f"   - {file}")
else:
    print("✓ No duplicates")
```

### Common Issues and Solutions

#### Issue 1: Registry Out of Sync (CultureMech)

**Symptom**: Registry missing IDs or has wrong file paths

**Cause**: Manual file moves or registry not updated

**Solution**:
```python
# Rebuild registry from scratch
import pandas as pd
from pathlib import Path

def rebuild_registry(base_dir: Path, output_path: Path):
    """Rebuild CultureMech ID registry from YAML files."""
    records = []

    for yaml_file in base_dir.rglob('*.yaml'):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

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
    print(f"✓ Rebuilt registry with {len(df)} entries")

# Usage
rebuild_registry(
    Path('data/normalized_yaml'),
    Path('data/culturemech_id_registry.tsv')
)
```

#### Issue 2: Gaps in Sequence

**Symptom**: Missing IDs (e.g., 1, 2, 4, 5 - missing 3)

**Cause**: Deleted record, manual ID assignment, or migration

**Solution**:
```
This is usually fine! IDs are persistent - once assigned, they should never be reused.
If a record is deleted, its ID should remain unused (tombstone).

To fill gaps (NOT RECOMMENDED):
- Only if absolutely necessary for migration/cleanup
- Re-run batch assignment with sequential ordering
- Document the renumbering in changelog
```

## Best Practices

### DO:
✓ **Always run `--dry-run` first** before batch operations
✓ **Validate after changes** using validation functions
✓ **Use zero-padding** (`{number:06d}`)
✓ **Place `id` field first** in YAML for readability
✓ **Update registry** when adding/moving files (CultureMech)
✓ **Preserve ID history** - never reuse deleted IDs
✓ **Use existing scripts** for batch operations
✓ **Document manual additions** in curation history

### DON'T:
✗ **Don't manually assign IDs** without checking highest ID first
✗ **Don't reuse IDs** from deleted records (breaks references)
✗ **Don't use `sort_keys=True`** when saving YAML (breaks field order)
✗ **Don't skip registry updates** (CultureMech)
✗ **Don't force-overwrite** existing IDs unless absolutely necessary
✗ **Don't create gaps intentionally** (sequential is better)
✗ **Don't use non-standard formats** (stick to `Prefix:NNNNNN`)

## CultureMech Quick Reference

**Current state**: 15,431 media (`CultureMech:000001` to `CultureMech:015431`)

**Add single medium**:
```python
# 1. Find next ID from registry
registry_path = Path('data/culturemech_id_registry.tsv')
highest = find_highest_id_from_registry(registry_path, 'CultureMech')
next_id = generate_xmech_id('CultureMech', highest + 1)

# 2. Create record (see workflow above)
# 3. Save to category directory
# 4. Update registry
```

**Batch operation**:
```bash
python scripts/assign_culturemech_ids.py --dry-run
python scripts/assign_culturemech_ids.py
```

**Rebuild registry**:
```python
rebuild_registry(
    Path('data/normalized_yaml'),
    Path('data/culturemech_id_registry.tsv')
)
```

**Verify no duplicates**:
```python
from culturemech.utils.id_utils import find_duplicate_ids_multi_file

duplicates = find_duplicate_ids_multi_file(Path('data/normalized_yaml'))
print(f"Duplicates: {len(duplicates)}")
```

## Integration with Other Tools

### Using in Knowledge Graph Export

IDs serve as RDF subjects in KG exports:

```python
# Example KGX export
from kgx import Transformer

# CultureMech:000001 becomes RDF subject
subject = "CultureMech:000001"
predicate = "biolink:has_part"
object = "MediaIngredientMech:000001"  # Sodium chloride

# Cross-repository reference
edge = {
    "subject": "CultureMech:000001",  # LB Medium
    "predicate": "biolink:has_part",
    "object": "MediaIngredientMech:000001"  # Ingredient reference
}
```

## Summary

This skill provides complete coverage of identifier management for CultureMech and other X-Mech repositories. Use the provided code examples, best practices, and workflows to maintain stable, sequential IDs that support data integrity and knowledge graph integration.

**Remember**: IDs are persistent references - treat them with care, validate before committing, and never reuse deleted IDs.
