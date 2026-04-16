# CultureMech Import Tracking & Versioning System

## Overview

This directory contains the infrastructure for versioning, tracking, and managing imports of culture media from external databases into CultureMech.

**Purpose**: Enable reproducible imports, provenance tracking, and systematic updates from source databases.

## Directory Structure

```
import_tracking/
├── README.md                    # This file
├── manifests/                   # Version manifests by source
│   ├── mediadive/
│   │   └── v1.0.0_2026-01-27.yaml
│   ├── togo/
│   ├── komodo/
│   ├── mediadb/
│   ├── utex/
│   ├── ccap/
│   ├── sag/
│   ├── culturebotht/
│   ├── communitymech/
│   ├── bacdive/
│   ├── nbrc/
│   └── atcc/
├── reports/                     # Import execution reports
├── logs/                        # Detailed import logs
├── cache/                       # Cached source data
└── schemas/
    └── manifest_v1.schema.json  # Manifest validation schema
```

## Version Manifests

Each import from a source database generates a **version manifest** that tracks:

- **Import version** (e.g., `v1.0.0_2026-01-27`)
- **Source metadata** (database URL, version, access method)
- **Import statistics** (media imported, skipped, errors)
- **Category breakdown** (bacterial, fungal, algae, etc.)
- **ID assignments** (CultureMech ID range)
- **Validation status** (PASSED, PASSED_WITH_WARNINGS, FAILED)
- **Data quality metrics** (completeness, mapping rates)
- **Files created/updated**

### Manifest Naming Convention

Format: `{source}/{version}.yaml`

Example: `mediadive/v1.0.0_2026-01-27.yaml`

### Version Format

Format: `vMAJOR.MINOR.PATCH_YYYY-MM-DD`

**Semantic Versioning**:
- **MAJOR**: Schema breaking changes, major structural updates
- **MINOR**: New media added, enrichment changes, non-breaking updates
- **PATCH**: Bug fixes, metadata corrections, minor corrections

**Date**: Date when import was executed (for temporal tracking)

**Examples**:
- `v1.0.0_2026-01-27` - Initial baseline import
- `v1.1.0_2026-03-15` - Added 75 new media from source update
- `v1.0.1_2026-02-10` - Fixed pH value parsing bug

## Import Metadata in Recipes

Each imported recipe includes an `import_metadata` field:

```yaml
import_metadata:
  source_database: MEDIADIVE
  source_id: "Medium 1234"
  import_version: v1.0.0_2026-01-27
  import_date: '2026-01-27T06:35:57Z'
  import_skill: import-mediadive
  last_updated: '2026-01-27T06:35:57Z'
  update_history:
    - timestamp: '2026-01-27T06:35:57Z'
      import_version: v1.0.0_2026-01-27
      action: INITIAL_IMPORT
      notes: "Baseline import from MediaDive"
```

### Update History

When a recipe is updated, the `update_history` tracks changes:

```yaml
update_history:
  - timestamp: '2026-01-27T06:35:57Z'
    import_version: v1.0.0_2026-01-27
    action: INITIAL_IMPORT
    notes: "Baseline import from MediaDive"

  - timestamp: '2026-03-15T10:30:00Z'
    import_version: v1.1.0_2026-03-15
    action: REFRESHED
    fields_changed: [ingredients, ph_value]
    notes: "Updated from source database refresh"
```

## Using Import Skills

Import skills automate the entire import workflow:

### Available Skills

Tier 1 (High-Volume):
- `import-mediadive` - MediaDive (3,327 media)
- `import-togo` - TOGO Medium (2,917 media)
- `import-komodo` - KOMODO (3,637 media)
- `import-mediadb` - MediaDB (469 media)

Tier 2 (Algae):
- `import-ccap` - CCAP (113 media)
- `import-utex` - UTEX (99 media)
- `import-sag` - SAG (30 media)

Tier 3 (Integration):
- `import-culturebotht` - CultureBotHT (381 media)
- `import-communitymech` - CommunityMech (8 media)

### Basic Workflow

```bash
# 1. Run import with versioning
python scripts/import_from_mediadive.py \
  --version v1.0.0_2026-03-18 \
  --output-dir data/normalized_yaml

# 2. Validate imports
just validate-recipes

# 3. Check manifest
cat data/import_tracking/manifests/mediadive/v1.0.0_2026-03-18.yaml

# 4. Regenerate indexes
just generate-indexes
```

### Update Workflow (Refreshing)

```bash
# 1. Run in update mode
python scripts/import_from_mediadive.py \
  --version v1.1.0_2026-03-18 \
  --update-mode \
  --previous-manifest data/import_tracking/manifests/mediadive/v1.0.0_2026-01-27.yaml

# 2. Review changes
git diff data/normalized_yaml/

# 3. Validate and commit
just validate-recipes
git commit -m "Update MediaDive media to v1.1.0"
```

## Grandfathering Existing Imports

All existing imports have been retroactively versioned with baseline `v1.0.0` manifests:

```bash
# Generate baseline manifests for all sources
python scripts/generate_baseline_manifests.py \
  --yaml-dir data/normalized_yaml \
  --output-dir data/import_tracking/manifests

# Backfill import_metadata to existing recipes
python scripts/backfill_import_metadata.py
```

This creates a baseline from which future updates can be tracked.

## Validation

### Pre-Import Validation

```bash
# Check readiness before import
python scripts/validate_pre_import.py --source MEDIADIVE
```

Checks:
- Source accessible
- Schema up-to-date
- No uncommitted changes
- ID range available

### Post-Import Validation

```bash
# Verify import integrity
python scripts/validate_import_integrity.py \
  --manifest data/import_tracking/manifests/mediadive/v1.0.0_2026-03-18.yaml
```

Checks:
- Manifest matches files
- IDs sequential and unique
- All records validate against schema
- No duplicates

### Quality Reports

```bash
# Generate data quality report
python scripts/generate_import_quality_report.py \
  --manifest data/import_tracking/manifests/mediadive/v1.0.0_2026-03-18.yaml
```

Generates:
- Coverage metrics
- Mapping quality (CHEBI, organisms)
- Completeness scores
- Validation errors

## Source Database Coverage

| Source | Media | Status | Latest Version |
|--------|-------|--------|----------------|
| KOMODO | 3,637 | ✓ Baseline | v1.0.0_2026-01-28 |
| MediaDive | 3,327 | ✓ Baseline | v1.0.0_2026-01-27 |
| TOGO | 2,917 | ✓ Baseline | v1.0.0_2026-01-27 |
| MediaDB | 469 | ✓ Baseline | v1.0.0_2026-01-27 |
| CultureBotHT | 381 | ✓ Baseline | v1.0.0_2026-02-10 |
| CCAP | 113 | ✓ Baseline | v1.0.0_2026-01-27 |
| UTEX | 99 | ✓ Baseline | v1.0.0_2026-01-27 |
| SAG | 30 | ✓ Baseline | v1.0.0_2026-01-27 |
| CommunityMech | 8 | ✓ Baseline | v1.0.0_2026-01-27 |
| BacDive | Partial | ○ Planned | - |
| NBRC | Partial | ○ Planned | - |
| ATCC | Partial | ○ Planned | - |

**Total**: 10,981+ versioned media

## Adding New Import Sources

To add a new source database:

1. **Create source directory**: `mkdir manifests/{source_name}/`

2. **Add to SourceDatabaseEnum**: Edit `src/culturemech/schema/culturemech.yaml`

3. **Create import script**: `scripts/import_from_{source}.py`
   - Support `--version` parameter
   - Generate manifest after import
   - Add import_metadata to each recipe

4. **Create import skill**: `.claude/skills/import-{source}/skill.md`
   - Document workflow
   - Include source-specific quirks

5. **Test workflow**:
   ```bash
   python scripts/import_from_{source}.py --dry-run --version v1.0.0_YYYY-MM-DD
   ```

6. **Document in this README**

## Schema

Import metadata uses the following LinkML classes:

- **ImportMetadata**: Top-level import tracking
- **UpdateEvent**: Individual update records
- **SourceDatabaseEnum**: Valid source databases
- **UpdateActionEnum**: Update action types

See: `src/culturemech/schema/culturemech.yaml`

## Related Documentation

- **Import Summary**: `IMPORT_SUMMARY.md` - Overview of all imports
- **Import Guide**: `docs/IMPORT_GUIDE.md` - Contributor guide
- **Skills Documentation**: `.claude/skills/import-*/skill.md`

## Questions?

For issues or questions about import tracking:
- Check the import skill documentation (`.claude/skills/import-{source}/skill.md`)
- Review existing manifests for examples
- See `docs/IMPORT_GUIDE.md` for detailed guidance
