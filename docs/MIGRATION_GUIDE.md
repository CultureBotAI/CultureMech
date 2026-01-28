# Migration Guide: Three-Tier Directory Structure

## Overview

CultureMech has migrated from a two-layer system to a **three-tier system** with clearer naming:

**Old Structure** (2 layers):
```
data/raw/     → Layer 1: Raw source files
kb/media/     → Layer 3: Normalized recipes
```

**New Structure** (3 tiers):
```
raw/              → Layer 1: Raw source files (renamed from data/raw/)
raw_yaml/         → Layer 2: Unnormalized YAML (NEW)
normalized_yaml/  → Layer 3: Normalized recipes (renamed from kb/media/)
```

## Quick Reference: Path Changes

| Old Path | New Path | Description |
|----------|----------|-------------|
| `data/raw/` | `raw/` | Raw source files |
| (none) | `raw_yaml/` | **NEW** unnormalized YAML layer |
| `kb/media/` | `normalized_yaml/` | Validated recipes |
| `data/processed/` | `data/processed/` | Unchanged (for future use) |

## Command Changes

### Fetch Commands (unchanged functionality, new paths)

| Old Command | New Command | Notes |
|-------------|-------------|-------|
| Same | Same | Outputs to `raw/` instead of `data/raw/` |

**Example**:
```bash
# Commands are the same, but now write to raw/
just fetch-mediadive-raw      # Now writes to raw/mediadive/
just fetch-togo-raw 50        # Now writes to raw/togo/
```

### NEW: Convert Commands

These are **new commands** for generating Layer 2 (raw_yaml):

```bash
# Convert all sources to raw_yaml
just convert-to-raw-yaml all

# Convert specific sources
just convert-to-raw-yaml mediadive
just convert-to-raw-yaml togo
just convert-to-raw-yaml atcc

# Individual source commands
just convert-mediadive-raw-yaml
just convert-togo-raw-yaml
just convert-atcc-raw-yaml
# ... (one for each source)
```

### Import Commands (unchanged functionality, new paths)

| Old Command | New Command | Notes |
|-------------|-------------|-------|
| Same | Same | Reads from `raw/`, writes to `normalized_yaml/` |

**Example**:
```bash
# Commands are the same
just import-mediadive 50      # Now: raw/ → normalized_yaml/
just import-togo 100          # Now: raw/ → normalized_yaml/
```

### Validate Commands (new paths)

| Old Command | New Command |
|-------------|-------------|
| `just validate kb/media/bacterial/LB_Broth.yaml` | `just validate normalized_yaml/bacterial/LB_Broth.yaml` |
| `just validate-all` | `just validate-all` (unchanged) |
| `just validate-schema kb/media/...` | `just validate-schema normalized_yaml/...` |

### Export Commands (new paths)

| Old Command | New Command |
|-------------|-------------|
| `just gen-browser-data` | `just gen-browser-data` (reads from `normalized_yaml/`) |
| `just gen-pages` | `just gen-pages` (reads from `normalized_yaml/`) |
| `just gen-page kb/media/...` | `just gen-page normalized_yaml/...` |
| `just kgx-export` | `just kgx-export` (reads from `normalized_yaml/`) |

### Utility Commands (new paths)

| Old Command | New Command |
|-------------|-------------|
| `just count-recipes` | `just count-recipes` (counts `normalized_yaml/`) |
| `just list-recipes` | `just list-recipes` (lists `normalized_yaml/`) |
| `just show-raw-data-stats` | `just show-raw-data-stats` (shows `raw/` stats) |

## Code Changes

### Python Script Arguments

Default paths have changed for all importers, fetchers, and exporters:

**Importers** (8 files):
```python
# OLD
parser.add_argument("-i", "--input", default="data/raw/mediadive")
parser.add_argument("-o", "--output", default="kb/media")

# NEW
parser.add_argument("-i", "--input", default="raw/mediadive")
parser.add_argument("-o", "--output", default="normalized_yaml")
```

**Fetchers** (7 files):
```python
# OLD
parser.add_argument("-o", "--output", default="data/raw/togo")

# NEW
parser.add_argument("-o", "--output", default="raw/togo")
```

**Exporters** (2 files):
```python
# OLD
parser.add_argument("-i", "--input", default="kb/media")

# NEW
parser.add_argument("-i", "--input", default="normalized_yaml")
```

### Custom Scripts

If you have custom scripts that reference old paths, update them:

```python
# OLD
from pathlib import Path
kb_dir = Path("kb/media")
raw_dir = Path("data/raw")

# NEW
from pathlib import Path
normalized_yaml_dir = Path("normalized_yaml")
raw_dir = Path("raw")
```

### Justfile Variables

If you have custom `justfile` recipes:

```just
# OLD
kb_dir := "kb/media"
raw_data_dir := "data/raw"

# NEW
normalized_yaml_dir := "normalized_yaml"
raw_dir := "raw"
raw_yaml_dir := "raw_yaml"
```

## Git and Version Control

### What Changed in Git

- `kb/media/` files were moved to `normalized_yaml/`
- Git history is preserved (files were moved, not deleted/recreated)
- `.gitignore` updated to use new paths

### What's Tracked

✅ **Tracked in Git**:
- `normalized_yaml/**/*.yaml` - All validated recipes
- `raw/*/README.md` - Provenance documentation
- `raw_yaml/*/README.md` - Conversion notes (if present)

❌ **Not Tracked** (in `.gitignore`):
- `raw/**/*.json`, `.tsv`, `.sql`, etc. - Raw data files
- `raw_yaml/**/*.yaml` - Unnormalized YAML (regenerable)

### After Migration

Check git status:
```bash
git status

# You should see:
# - Renamed files: kb/media/* → normalized_yaml/*
# - Modified: .gitignore, project.justfile, src/culturemech/**/*.py
# - New files: src/culturemech/convert/*, migration script
```

## Migration Procedure

The migration has already been completed using `scripts/migrate_to_three_tier.sh`. Here's what happened:

### What the Migration Script Did

1. **Created backup**: `backups/pre-migration-YYYYMMDD-HHMMSS/`
2. **Created new directories**: `raw/`, `raw_yaml/`, `normalized_yaml/`
3. **Moved raw data**: `data/raw/*` → `raw/`
4. **Moved normalized recipes**: `kb/media/*` → `normalized_yaml/`
5. **Created placeholders**: Empty `raw_yaml/<source>/` directories
6. **Verified structure**: Confirmed all moves succeeded

### Backup Location

A backup was created before migration:
```bash
ls backups/
# pre-migration-20260127-095345/
#   data/
#   kb/
```

### Rollback (if needed)

To undo the migration:

```bash
# 1. Restore from backup
BACKUP_DIR="backups/pre-migration-20260127-095345"  # Use your backup timestamp

# 2. Restore data/
rm -rf data/raw/
cp -r "$BACKUP_DIR/data/" .

# 3. Restore kb/
rm -rf kb/media/
cp -r "$BACKUP_DIR/kb/" .

# 4. Remove new directories
rm -rf raw/ raw_yaml/ normalized_yaml/

# 5. Revert code changes (if needed)
git checkout HEAD -- .gitignore project.justfile src/
```

## Post-Migration Checklist

### Verify Structure

```bash
# Check new directories exist
ls -ld raw/ raw_yaml/ normalized_yaml/

# Count files in each tier
find raw/ -name "*.json" | wc -l
find raw_yaml/ -name "*.yaml" | wc -l
find normalized_yaml/ -name "*.yaml" | wc -l
```

### Generate Raw YAML

```bash
# Populate Layer 2
just convert-to-raw-yaml all

# Verify raw_yaml populated
ls raw_yaml/mediadive/ | head -10
```

### Test Import Pipeline

```bash
# Test import on small sample
just import-mediadive 5

# Verify output
ls normalized_yaml/bacterial/
```

### Validate Recipes

```bash
# Validate all recipes
just validate-all

# Should pass with no errors
```

### Test Export

```bash
# Generate browser data
just gen-browser-data

# Verify app/data.js created
ls -lh app/data.js

# Test serve
just serve-browser
# Visit http://localhost:8000/app/
```

### Review Changes

```bash
# Check what changed in git
git diff --stat

# Review specific files
git diff .gitignore
git diff project.justfile
git diff src/culturemech/import/mediadive_importer.py
```

## Common Issues

### Issue: "No such file or directory: kb/media"

**Cause**: Old path hardcoded in custom script

**Fix**: Update to use `normalized_yaml/`

```python
# OLD
recipes_dir = Path("kb/media")

# NEW
recipes_dir = Path("normalized_yaml")
```

### Issue: "No raw data files found"

**Cause**: Forgot to fetch raw data after migration

**Fix**: Fetch raw data

```bash
just fetch-raw-data
```

### Issue: "empty raw_yaml directory"

**Cause**: Haven't run converters yet

**Fix**: Generate raw_yaml

```bash
just convert-to-raw-yaml all
```

### Issue: Import fails with "output directory not found"

**Cause**: Old importer cached or not updated

**Fix**: Reinstall package

```bash
just install
```

## FAQ

### Q: Why the new raw_yaml/ layer?

**A**: Provides human-readable intermediate format for debugging and inspection without requiring LinkML knowledge.

### Q: Do I need to regenerate raw_yaml/ every time?

**A**: No, it's optional. You can import directly from `raw/` to `normalized_yaml/`. The `raw_yaml/` layer is for inspection and debugging.

### Q: What happens to old kb/ and data/ directories?

**A**: They're backed up but can be removed after verifying migration. The backup contains everything.

### Q: Can I still use old commands?

**A**: Commands are mostly unchanged, but they now use new paths internally. Any command with explicit paths (like `just validate kb/media/...`) needs path updates.

### Q: Is git history preserved?

**A**: Yes, files were moved (not deleted), so git preserves history. Use `git log --follow` to see history across renames.

### Q: How do I update my custom scripts?

**A**: Search and replace:
- `data/raw` → `raw`
- `kb/media` → `normalized_yaml`
- Add `raw_yaml` references if needed

### Q: What if I find a bug?

**A**: The backup contains the pre-migration state. You can compare against it or restore if needed.

## Additional Resources

- **DATA_LAYERS.md** - Complete architecture documentation
- **RAW_YAML_LAYER.md** - Layer 2 details
- **QUICK_START.md** - Updated getting started guide
- **scripts/migrate_to_three_tier.sh** - Migration script source
- **backups/** - Pre-migration backups

## Summary

The three-tier migration provides:
- ✅ **Clearer naming** - `raw/`, `raw_yaml/`, `normalized_yaml/`
- ✅ **Better separation** - Three distinct data layers
- ✅ **Improved debugging** - raw_yaml/ for inspection
- ✅ **Maintained functionality** - All commands still work
- ✅ **Preserved history** - Git history intact
- ✅ **Backup safety** - Pre-migration backup created

The migration is complete and all systems are operational!
