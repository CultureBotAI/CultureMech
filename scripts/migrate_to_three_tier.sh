#!/bin/bash
set -e

echo "=========================================="
echo "CultureMech: Migrate to Three-Tier System"
echo "=========================================="
echo ""

# Get the project root (one level up from scripts/)
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "Project root: $PROJECT_ROOT"
echo ""

# Create backup directory with timestamp
BACKUP_DIR="backups/pre-migration-$(date +%Y%m%d-%H%M%S)"
echo "Creating backup in $BACKUP_DIR..."
mkdir -p "$BACKUP_DIR"

# Backup current structure if directories exist
if [ -d "data" ]; then
    echo "  Backing up data/..."
    cp -r data/ "$BACKUP_DIR/"
fi

if [ -d "kb" ]; then
    echo "  Backing up kb/..."
    cp -r kb/ "$BACKUP_DIR/"
fi

echo "✓ Backup complete"
echo ""

# Create new directory structure
echo "Creating new directory structure..."
mkdir -p raw/
mkdir -p raw_yaml/
mkdir -p normalized_yaml/

echo "✓ New directories created"
echo ""

# Move raw data
echo "Moving raw data sources..."
if [ -d "data/raw" ]; then
    for dir in data/raw/*; do
        if [ -d "$dir" ]; then
            dirname=$(basename "$dir")
            echo "  Moving $dirname..."
            mv "$dir" raw/
        fi
    done
    echo "✓ Raw data moved to raw/"
else
    echo "  No data/raw directory found"
fi
echo ""

# Move normalized data
echo "Moving normalized YAML recipes..."
if [ -d "kb/media" ]; then
    for dir in kb/media/*; do
        if [ -d "$dir" ]; then
            dirname=$(basename "$dir")
            # Skip backup directories
            if [[ "$dirname" != *"backup"* ]]; then
                echo "  Moving $dirname..."
                mv "$dir" normalized_yaml/
            fi
        fi
    done
    echo "✓ Normalized YAML moved to normalized_yaml/"
else
    echo "  No kb/media directory found"
fi
echo ""

# Create placeholder raw_yaml directories
echo "Creating placeholder directories in raw_yaml/..."
for source_dir in raw/*; do
    if [ -d "$source_dir" ]; then
        source_name=$(basename "$source_dir")
        mkdir -p "raw_yaml/$source_name"
        echo "  Created raw_yaml/$source_name/"
    fi
done
echo "✓ Placeholder directories created"
echo ""

# Verify new structure
echo "Verifying new structure..."
echo ""
echo "Raw sources:"
ls -1 raw/ 2>/dev/null || echo "  (none)"
echo ""
echo "Raw YAML (to be populated):"
ls -1 raw_yaml/ 2>/dev/null || echo "  (none)"
echo ""
echo "Normalized YAML:"
ls -1 normalized_yaml/ 2>/dev/null || echo "  (none)"
echo ""

echo "=========================================="
echo "✓ Migration complete!"
echo "=========================================="
echo ""
echo "Backup location: $BACKUP_DIR"
echo ""
echo "Next steps:"
echo "  1. Review the new directory structure"
echo "  2. Run: just convert-to-raw-yaml all"
echo "  3. Update any custom scripts you have"
echo "  4. Test the import pipeline"
echo ""
echo "To rollback, restore from: $BACKUP_DIR"
echo ""
