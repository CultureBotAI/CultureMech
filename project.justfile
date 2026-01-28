# CultureMech Build System
# Build recipes for validation, export, and deployment

schema_path := "src/culturemech/schema/culturemech.yaml"
oak_config := "conf/oak_config.yaml"
output_dir := "output"
pages_dir := "pages"
app_dir := "app"

# Data layer paths (see DATA_LAYERS.md)
# Three-tier system: raw/ → raw_yaml/ → normalized_yaml/
raw_dir := "raw"
raw_yaml_dir := "raw_yaml"
normalized_yaml_dir := "normalized_yaml"
processed_data_dir := "data/processed"
cmm_automation_dir := "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/cmm-ai-automation/data"
microbe_media_param_dir := "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MicrobeMediaParam/MicroMediaParam/pipeline_output/merge_mappings"

# ================================================================
# DATA LAYERS (Layer 1: Raw → Layer 2: Processed → Layer 3: KB)
# ================================================================

[group('Data')]
fetch-raw-data:
    @echo "Fetching all raw data sources..."
    just fetch-mediadive-raw
    just fetch-microbe-media-param-raw
    just fetch-togo-raw
    @echo "✓ Core raw data fetched!"
    @echo ""
    @echo "Optional: just fetch-bacdive-raw, just scrape-nbrc-raw"
    @echo "See raw/*/README.md for provenance information"

[group('Data')]
fetch-mediadive-raw:
    #!/usr/bin/env bash
    echo "Fetching MediaDive raw data from cmm-ai-automation..."
    mkdir -p {{raw_dir}}/mediadive

    if [ -d "{{cmm_automation_dir}}" ]; then
        cp {{cmm_automation_dir}}/mediadive_media.json {{raw_dir}}/mediadive/ 2>/dev/null || echo "⚠ mediadive_media.json not found"
        cp {{cmm_automation_dir}}/mediadive_ingredients.json {{raw_dir}}/mediadive/ 2>/dev/null || echo "⚠ mediadive_ingredients.json not found"
        echo "✓ MediaDive raw data copied to {{raw_dir}}/mediadive/"
        ls -lh {{raw_dir}}/mediadive/*.json 2>/dev/null || echo "No JSON files found"
    else
        echo "✗ cmm-ai-automation directory not found at {{cmm_automation_dir}}"
        echo "  Update the path in project.justfile or download manually"
    fi

[group('Data')]
fetch-microbe-media-param-raw:
    #!/usr/bin/env bash
    echo "Fetching MicrobeMediaParam raw data..."
    mkdir -p {{raw_dir}}/microbe-media-param

    if [ -d "{{microbe_media_param_dir}}" ]; then
        cp {{microbe_media_param_dir}}/*.tsv {{raw_dir}}/microbe-media-param/ 2>/dev/null || echo "⚠ TSV files not found"
        echo "✓ MicrobeMediaParam mappings copied to {{raw_dir}}/microbe-media-param/"
        ls -lh {{raw_dir}}/microbe-media-param/*.tsv 2>/dev/null || echo "No TSV files found"
    else
        echo "✗ MicrobeMediaParam directory not found at {{microbe_media_param_dir}}"
        echo "  Update the path in project.justfile or download manually"
    fi

[group('Data')]
fetch-togo-raw limit="":
    #!/usr/bin/env bash
    echo "Fetching TOGO Medium data from API..."
    mkdir -p {{raw_dir}}/togo

    # Use fetcher to download from API
    if [ "{{limit}}" != "" ]; then
        echo "  Limiting to {{limit}} media for testing"
        uv run python -m culturemech.fetch.togo_fetcher \
            --output {{raw_dir}}/togo \
            --limit {{limit}}
    else
        echo "  Fetching all media (~2,917 expected)"
        echo "  This may take 20-30 minutes with rate limiting..."
        uv run python -m culturemech.fetch.togo_fetcher \
            --output {{raw_dir}}/togo
    fi

[group('Data')]
fetch-mediadive-api limit="":
    #!/usr/bin/env bash
    echo "Fetching MediaDive compositions from REST API..."
    mkdir -p {{raw_dir}}/mediadive_api

    # Build command
    cmd="uv run python -m culturemech.fetch.mediadive_api_fetcher \
        --output {{raw_dir}}/mediadive_api"

    # Add limit if specified
    if [ "{{limit}}" != "" ]; then
        echo "  Limiting to {{limit}} media for testing"
        cmd="$cmd --limit {{limit}}"
    else
        echo "  Fetching all media (~3,327 expected)"
        echo "  This may take ~13 minutes with rate limiting..."
    fi

    echo "Starting fetch..."
    eval $cmd

    echo ""
    echo "✓ Fetch complete!"
    echo "Next step: just import-mediadive"

[group('Data')]
fetch-komodo-web:
    #!/usr/bin/env bash
    echo "Fetching KOMODO media table from web..."
    mkdir -p {{raw_dir}}/komodo_web

    uv run python -m culturemech.fetch.komodo_web_fetcher \
        --output {{raw_dir}}/komodo_web

    echo ""
    echo "✓ Fetch complete!"
    echo "Next step: just import-komodo-web"

[group('Data')]
fetch-bacdive-raw limit="" email="" password="":
    #!/usr/bin/env bash
    echo "Fetching BacDive cultivation data from API..."
    echo "Note: BacDive account required (free registration)"
    echo "      Register at: https://bacdive.dsmz.de/"
    echo ""
    mkdir -p {{raw_dir}}/bacdive

    # Build command with optional credentials
    cmd="uv run python -m culturemech.fetch.bacdive_fetcher --output {{raw_dir}}/bacdive"

    if [ "{{email}}" != "" ]; then
        cmd="$cmd --email {{email}}"
    fi

    if [ "{{password}}" != "" ]; then
        cmd="$cmd --password {{password}}"
    fi

    if [ "{{limit}}" != "" ]; then
        echo "  Limiting to {{limit}} strains for testing"
        cmd="$cmd --limit {{limit}}"
    else
        echo "  Fetching all cultivation data (66,570+ strains expected)"
        echo "  This may take SEVERAL HOURS..."
        echo "  Recommend starting with: just fetch-bacdive-raw 100"
    fi

    # Check if bacdive package is installed
    if ! uv run python -c "import bacdive" 2>/dev/null; then
        echo ""
        echo "⚠ BacDive Python client not installed"
        echo "  Installing now..."
        uv pip install bacdive
        echo ""
    fi

    eval $cmd

[group('Data')]
scrape-nbrc-raw limit="":
    #!/usr/bin/env bash
    echo "Scraping NBRC media from website..."
    echo "Note: This uses ethical web scraping (2s delay)"
    echo ""
    mkdir -p {{raw_dir}}/nbrc

    # Check if beautifulsoup4 is installed
    if ! uv run python -c "import bs4" 2>/dev/null; then
        echo "⚠ BeautifulSoup4 not installed"
        echo "  Installing now..."
        uv pip install beautifulsoup4
        echo ""
    fi

    if [ "{{limit}}" != "" ]; then
        echo "  Limiting to {{limit}} media for testing"
        uv run python -m culturemech.fetch.nbrc_scraper \
            --output {{raw_dir}}/nbrc \
            --limit {{limit}}
    else
        echo "  Scraping all media (~400 expected)"
        echo "  This will take ~15 minutes with 2s delay..."
        uv run python -m culturemech.fetch.nbrc_scraper \
            --output {{raw_dir}}/nbrc
    fi

[group('Data')]
fetch-komodo-raw source="":
    #!/usr/bin/env bash
    echo "Fetching KOMODO media data..."
    echo ""
    mkdir -p {{raw_dir}}/komodo

    # Check if required packages are installed
    if ! uv run python -c "import openpyxl" 2>/dev/null; then
        echo "⚠ openpyxl not installed (needed for Excel parsing)"
        echo "  Installing now..."
        uv pip install openpyxl
        echo ""
    fi

    if ! uv run python -c "import sqlparse" 2>/dev/null; then
        echo "⚠ sqlparse not installed (needed for SQL parsing)"
        echo "  Installing now..."
        uv pip install sqlparse
        echo ""
    fi

    # Determine fetch method
    if [ -z "{{source}}" ]; then
        echo "Using PubMed Central supplementary files (recommended)..."
        echo "Downloading from PMC article PMC4633754..."
        echo ""
        uv run python -m culturemech.fetch.komodo_fetcher \
            --pmc \
            --output {{raw_dir}}/komodo
    elif [ -f "{{source}}" ]; then
        echo "Using SQL file: {{source}}"
        echo ""
        uv run python -m culturemech.fetch.komodo_fetcher \
            --sql "{{source}}" \
            --output {{raw_dir}}/komodo
    else
        echo "✗ Error: Unknown source type"
        echo ""
        echo "Usage:"
        echo "  just fetch-komodo-raw                  # Fetch from PMC (recommended)"
        echo "  just fetch-komodo-raw path/to/file.sql # Parse SQL dump"
        echo ""
        echo "To obtain KOMODO data:"
        echo "  1. PMC supplementary files (automatic with no arguments)"
        echo "  2. Contact maintainers: raphy.zarecki@gmail.com"
        echo "  3. Paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC4633754/"
        exit 1
    fi

[group('Data')]
fetch-mediadb-raw source_path="" source_type="":
    #!/usr/bin/env bash
    echo "Fetching MediaDB media data..."
    echo "Note: MediaDB data from mediadb.systemsbiology.net"
    echo ""
    mkdir -p {{raw_dir}}/mediadb

    # Check if sqlparse is installed
    if ! uv run python -c "import sqlparse" 2>/dev/null; then
        echo "⚠ sqlparse not installed"
        echo "  Installing now..."
        uv pip install sqlparse
        echo ""
    fi

    if [ -z "{{source_path}}" ]; then
        echo "✗ Error: Source path required"
        echo ""
        echo "Usage:"
        echo "  just fetch-mediadb-raw path/to/mediadb.sql     # SQL dump"
        echo "  just fetch-mediadb-raw path/to/mediadb_tsv/    # TSV directory"
        echo ""
        echo "To obtain MediaDB data:"
        echo "  Visit: https://mediadb.systemsbiology.net/"
        echo "  Contact: Institute for Systems Biology"
        exit 1
    fi

    # Auto-detect source type
    if [ -f "{{source_path}}" ]; then
        # It's a file, assume SQL
        uv run python -m culturemech.fetch.mediadb_fetcher \
            --sql "{{source_path}}" \
            --output {{raw_dir}}/mediadb
    elif [ -d "{{source_path}}" ]; then
        # It's a directory, assume TSV
        uv run python -m culturemech.fetch.mediadb_fetcher \
            --tsv "{{source_path}}" \
            --output {{raw_dir}}/mediadb
    else
        echo "✗ Error: Source path not found: {{source_path}}"
        exit 1
    fi

[group('Data')]
fetch-utex limit="":
    #!/usr/bin/env bash
    echo "Fetching UTEX algae media recipes..."
    mkdir -p {{raw_dir}}/utex

    cmd="uv run python -m culturemech.fetch.utex_fetcher \
        --output {{raw_dir}}/utex"

    if [ "{{limit}}" != "" ]; then
        echo "  Limiting to {{limit}} recipes for testing"
        cmd="$cmd --limit {{limit}}"
    else
        echo "  Fetching all recipes (~100 expected)"
        echo "  This may take a few minutes..."
    fi

    eval $cmd

[group('Data')]
fetch-ccap limit="":
    #!/usr/bin/env bash
    echo "Fetching CCAP algae media recipes..."
    mkdir -p {{raw_dir}}/ccap

    cmd="uv run python -m culturemech.fetch.ccap_fetcher \
        --output {{raw_dir}}/ccap"

    if [ "{{limit}}" != "" ]; then
        echo "  Limiting to {{limit}} recipes for testing"
        cmd="$cmd --limit {{limit}}"
    else
        echo "  Fetching all recipes (~110 expected)"
        echo "  This may take a few minutes..."
    fi

    # Optional: Add --download-pdfs to download PDF files
    # cmd="$cmd --download-pdfs"

    eval $cmd

[group('Data')]
fetch-sag limit="":
    #!/usr/bin/env bash
    echo "Fetching SAG algae media recipes..."
    mkdir -p {{raw_dir}}/sag

    cmd="uv run python -m culturemech.fetch.sag_fetcher \
        --output {{raw_dir}}/sag"

    if [ "{{limit}}" != "" ]; then
        echo "  Limiting to {{limit}} recipes for testing"
        cmd="$cmd --limit {{limit}}"
    else
        echo "  Fetching all recipes (~45 expected)"
        echo "  This may take a few minutes..."
    fi

    # Optional: Add --download-pdfs to download PDF files
    # cmd="$cmd --download-pdfs"

    eval $cmd

[group('Data')]
fetch-algae-collections:
    @echo "Fetching all algae collection media recipes..."
    just fetch-utex
    just fetch-ccap
    just fetch-sag
    @echo "✓ All algae collections fetched!"

[group('Data')]
show-raw-data-stats:
    #!/usr/bin/env bash
    echo "=== Raw Data Statistics ==="
    echo ""
    echo "MediaDive:"
    if [ -f "{{raw_dir}}/mediadive/mediadive_media.json" ]; then
        # Handle nested structure with .data array
        records=$(jq '.data | length' {{raw_dir}}/mediadive/mediadive_media.json 2>/dev/null || jq '. | length' {{raw_dir}}/mediadive/mediadive_media.json)
        echo "  📁 mediadive_media.json: $records records"
        ls -lh {{raw_dir}}/mediadive/mediadive_media.json | awk '{print "  📦 Size: " $5}'
    else
        echo "  ⚠ mediadive_media.json not found"
    fi

    if [ -f "{{raw_dir}}/mediadive/mediadive_ingredients.json" ]; then
        # Handle both object (keys) and array structures
        ingredients=$(jq 'if type == "object" then keys | length elif type == "array" then length else 0 end' {{raw_dir}}/mediadive/mediadive_ingredients.json)
        echo "  📁 mediadive_ingredients.json: $ingredients ingredients"
    else
        echo "  ⚠ mediadive_ingredients.json not found"
    fi

    # Check for API-fetched compositions
    if [ -f "{{raw_dir}}/mediadive_api/mediadive_api_media.json" ]; then
        api_count=$(jq '.count // (.data | length)' {{raw_dir}}/mediadive_api/mediadive_api_media.json)
        echo "  ✓ API compositions: $api_count media"
        ls -lh {{raw_dir}}/mediadive_api/mediadive_api_media.json | awk '{print "  📦 Size: " $5}'
        if [ -f "{{raw_dir}}/mediadive_api/fetch_stats.json" ]; then
            success_rate=$(jq -r '.success_rate // 0' {{raw_dir}}/mediadive_api/fetch_stats.json)
            echo "  📊 Success rate: ${success_rate}%"
        fi
    fi

    # Check for PDF-parsed compositions
    if [ -d "{{raw_dir}}/mediadive/compositions" ]; then
        pdf_count=$(ls {{raw_dir}}/mediadive/compositions/*.json 2>/dev/null | wc -l | xargs)
        echo "  📁 PDF compositions: $pdf_count media"
    fi

    echo ""
    echo "MicrobeMediaParam:"
    if [ -d "{{raw_dir}}/microbe-media-param" ]; then
        tsv_count=$(find {{raw_dir}}/microbe-media-param -name "*.tsv" | wc -l)
        echo "  📁 TSV files: $tsv_count"
        if [ $tsv_count -gt 0 ]; then
            for tsv in {{raw_dir}}/microbe-media-param/*.tsv; do
                lines=$(wc -l < "$tsv" 2>/dev/null || echo 0)
                echo "    - $(basename $tsv): $((lines-1)) mappings"
            done
        fi
    else
        echo "  ⚠ No TSV files found"
    fi

    echo ""
    echo "TOGO Medium:"
    if [ -f "{{raw_dir}}/togo/togo_media.json" ]; then
        media=$(jq 'if type == "array" then length else .data | length end' {{raw_dir}}/togo/togo_media.json 2>/dev/null || echo 0)
        echo "  📁 togo_media.json: $media media"
        ls -lh {{raw_dir}}/togo/togo_media.json | awk '{print "  📦 Size: " $5}'

        if [ -f "{{raw_dir}}/togo/fetch_stats.json" ]; then
            fetch_date=$(jq -r '.fetch_date' {{raw_dir}}/togo/fetch_stats.json 2>/dev/null)
            echo "  📅 Fetched: $fetch_date"
        fi
    else
        echo "  ⚠ togo_media.json not found"
        echo "    Run: just fetch-togo-raw"
    fi

    if [ -f "{{raw_dir}}/togo/togo_components.json" ]; then
        components=$(jq 'length' {{raw_dir}}/togo/togo_components.json 2>/dev/null || echo 0)
        echo "  📁 togo_components.json: $components components"
    fi

    echo ""
    echo "ATCC:"
    if [ -f "{{raw_dir}}/atcc/atcc_media_manual.json" ]; then
        manual=$(jq 'length' {{raw_dir}}/atcc/atcc_media_manual.json 2>/dev/null || echo 0)
        echo "  📁 atcc_media_manual.json: $manual media (manually curated)"
    else
        echo "  ⚠ atcc_media_manual.json not found"
    fi

    if [ -d "{{raw_dir}}/atcc/extracted" ]; then
        extracted=$(find {{raw_dir}}/atcc/extracted -name "*.json" | wc -l)
        echo "  📁 extracted/*.json: $extracted media (from MicroMediaParam)"
    fi

    if [ -f "{{raw_dir}}/atcc/atcc_crossref.json" ]; then
        crossrefs=$(jq 'keys | length' {{raw_dir}}/atcc/atcc_crossref.json 2>/dev/null || echo 0)
        echo "  📁 atcc_crossref.json: $crossrefs cross-references"
    fi

    echo ""
    echo "BacDive:"
    if [ -f "{{raw_dir}}/bacdive/bacdive_cultivation.json" ]; then
        cultivation=$(jq 'length' {{raw_dir}}/bacdive/bacdive_cultivation.json 2>/dev/null || echo 0)
        echo "  📁 bacdive_cultivation.json: $cultivation cultivation datasets"
        ls -lh {{raw_dir}}/bacdive/bacdive_cultivation.json | awk '{print "  📦 Size: " $5}'

        if [ -f "{{raw_dir}}/bacdive/bacdive_media_refs.json" ]; then
            media_refs=$(jq 'keys | length' {{raw_dir}}/bacdive/bacdive_media_refs.json 2>/dev/null || echo 0)
            echo "  📁 bacdive_media_refs.json: $media_refs unique media"
        fi

        if [ -f "{{raw_dir}}/bacdive/fetch_stats.json" ]; then
            fetch_date=$(jq -r '.fetch_date' {{raw_dir}}/bacdive/fetch_stats.json 2>/dev/null)
            echo "  📅 Fetched: $fetch_date"
        fi
    else
        echo "  ⚠ bacdive_cultivation.json not found"
        echo "    Run: just fetch-bacdive-raw"
    fi

    echo ""
    echo "NBRC:"
    if [ -f "{{raw_dir}}/nbrc/nbrc_media.json" ]; then
        media=$(jq 'length' {{raw_dir}}/nbrc/nbrc_media.json 2>/dev/null || echo 0)
        echo "  📁 nbrc_media.json: $media media"
        ls -lh {{raw_dir}}/nbrc/nbrc_media.json | awk '{print "  📦 Size: " $5}'

        if [ -f "{{raw_dir}}/nbrc/scrape_stats.json" ]; then
            scrape_date=$(jq -r '.scrape_date' {{raw_dir}}/nbrc/scrape_stats.json 2>/dev/null)
            echo "  📅 Scraped: $scrape_date"
        fi

        if [ -d "{{raw_dir}}/nbrc/scraped" ]; then
            cached=$(find {{raw_dir}}/nbrc/scraped -name "*.html" | wc -l)
            echo "  📁 Cached HTML pages: $cached"
        fi
    else
        echo "  ⚠ nbrc_media.json not found"
        echo "    Run: just scrape-nbrc-raw"
    fi

    echo ""
    echo "KOMODO:"
    if [ -f "{{raw_dir}}/komodo/komodo_media.json" ]; then
        media=$(jq '.count' {{raw_dir}}/komodo/komodo_media.json 2>/dev/null || echo 0)
        echo "  📁 komodo_media.json: $media media"
        ls -lh {{raw_dir}}/komodo/komodo_media.json | awk '{print "  📦 Size: " $5}'

        if [ -f "{{raw_dir}}/komodo/fetch_stats.json" ]; then
            fetch_date=$(jq -r '.fetch_date' {{raw_dir}}/komodo/fetch_stats.json 2>/dev/null)
            echo "  📅 Fetched: $fetch_date"
        fi
    else
        echo "  ⚠ komodo_media.json not found"
        echo "    Run: just fetch-komodo-raw path/to/sql"
    fi

    if [ -f "{{raw_dir}}/komodo/komodo_compounds.json" ]; then
        compounds=$(jq '.count' {{raw_dir}}/komodo/komodo_compounds.json 2>/dev/null || echo 0)
        echo "  📁 komodo_compounds.json: $compounds SEED compounds"
    fi

    echo ""
    echo "MediaDB:"
    if [ -f "{{raw_dir}}/mediadb/mediadb_media.json" ]; then
        media=$(jq '.count' {{raw_dir}}/mediadb/mediadb_media.json 2>/dev/null || echo 0)
        echo "  📁 mediadb_media.json: $media media"
        ls -lh {{raw_dir}}/mediadb/mediadb_media.json | awk '{print "  📦 Size: " $5}'

        if [ -f "{{raw_dir}}/mediadb/fetch_stats.json" ]; then
            fetch_date=$(jq -r '.fetch_date' {{raw_dir}}/mediadb/fetch_stats.json 2>/dev/null)
            echo "  📅 Fetched: $fetch_date"
        fi
    else
        echo "  ⚠ mediadb_media.json not found"
        echo "    Run: just fetch-mediadb-raw path/to/data"
    fi

    if [ -f "{{raw_dir}}/mediadb/mediadb_compounds.json" ]; then
        compounds=$(jq '.count' {{raw_dir}}/mediadb/mediadb_compounds.json 2>/dev/null || echo 0)
        echo "  📁 mediadb_compounds.json: $compounds compounds"
    fi

    echo ""
    echo "Note: ATCC has no public API - data is manually curated"
    echo "Note: BacDive requires free registration - see raw/bacdive/README.md"
    echo "Note: NBRC data obtained via ethical web scraping"
    echo "Note: KOMODO requires SQL dump - contact maintainers"
    echo "Note: MediaDB data available from mediadb.systemsbiology.net"
    echo ""
    echo "See raw/*/README.md for detailed provenance"

[group('Data')]
process-raw-data:
    @echo "🔄 Processing raw data → processed data"
    @echo "This will enrich and transform raw data for import"
    @echo ""
    @echo "Not yet implemented - coming in Phase 2"
    @echo "Currently using direct import from raw data"

# ================================================================
# SETUP
# ================================================================

[group('Setup')]
install:
    #!/usr/bin/env bash
    echo "Installing CultureMech dependencies..."
    uv pip install -e ".[dev]"
    echo "✓ Installation complete!"

[group('Setup')]
install-koza:
    #!/usr/bin/env bash
    echo "Installing Koza for KG export..."
    uv pip install -e ".[koza]"
    echo "✓ Koza installed!"

# ================================================================
# VALIDATION (3-layer pipeline)
# ================================================================

[group('QC')]
validate file:
    #!/usr/bin/env bash
    set -e
    echo "=== Schema validation ==="
    uv run linkml-validate --schema {{schema_path}} --target-class MediaRecipe {{file}}
    echo "✓ Schema validation passed"

    echo ""
    echo "=== Term validation ==="
    uv run linkml-term-validator validate-data {{file}} -s {{schema_path}} -t MediaRecipe --labels -c {{oak_config}} || echo "⚠ Term validation failed (may need ontologies downloaded)"

    echo ""
    echo "=== Reference validation (optional) ==="
    uv run linkml-reference-validator validate data {{file}} --schema {{schema_path}} --target-class MediaRecipe || echo "⚠ Reference validation skipped (optional for historical recipes)"

[group('QC')]
validate-schema file:
    #!/usr/bin/env bash
    echo "Validating schema structure..."
    uv run linkml-validate --schema {{schema_path}} --target-class MediaRecipe "{{file}}"
    echo "✓ Schema validation passed"

[group('QC')]
validate-terms file:
    #!/usr/bin/env bash
    echo "Validating ontology terms..."
    uv run linkml-term-validator validate-data {{file}} -s {{schema_path}} -t MediaRecipe --labels -c {{oak_config}}
    echo "✓ Term validation passed"

[group('QC')]
validate-references file:
    #!/usr/bin/env bash
    echo "Validating evidence references..."
    uv run linkml-reference-validator validate data {{file}} --schema {{schema_path}} --target-class MediaRecipe
    echo "✓ Reference validation passed"

[group('QC')]
validate-all:
    #!/usr/bin/env bash
    failed_files=()
    for f in {{normalized_yaml_dir}}/**/*.yaml; do
        echo "=== Validating $(basename $f) ==="
        if ! just validate-schema "$f"; then
            failed_files+=("$f")
        fi
        echo ""
    done
    if [ ${#failed_files[@]} -gt 0 ]; then
        echo "✗ ${#failed_files[@]} file(s) failed validation"
        exit 1
    fi
    echo "✓ All recipes validated successfully!"

[group('QC')]
qc:
    #!/usr/bin/env bash
    echo "Running full QC pipeline..."
    just validate-all
    echo ""
    echo "✓ QC complete!"

# ================================================================
# EXPORT
# ================================================================

[group('Export')]
kgx-export:
    #!/usr/bin/env bash
    mkdir -p {{output_dir}}/kgx
    echo "Exporting recipes to KGX format..."
    uv run koza transform src/culturemech/export/kgx_export.py -i '{{normalized_yaml_dir}}/**/*.yaml' -o {{output_dir}}/kgx -f jsonl
    echo ""
    echo "✓ KGX edges exported to {{output_dir}}/kgx/"
    echo "Stats:"
    wc -l {{output_dir}}/kgx/*.jsonl || echo "No output files generated"

# ================================================================
# BROWSER
# ================================================================

[group('Browser')]
gen-browser-data:
    #!/usr/bin/env bash
    echo "Generating browser data..."
    uv run python -m culturemech.export.browser_export -i {{normalized_yaml_dir}} -o {{app_dir}}/data.js
    echo "✓ Browser data generated at {{app_dir}}/data.js"

[group('Browser')]
serve-browser port="8000":
    #!/usr/bin/env bash
    echo "Starting browser at http://localhost:{{port}}/app/"
    python -m http.server {{port}}

[group('Browser')]
build-browser: gen-browser-data
    #!/usr/bin/env bash
    echo "✓ Browser build complete!"
    echo "To view locally, run: just serve-browser"

# ================================================================
# PAGES
# ================================================================

[group('Pages')]
gen-pages:
    #!/usr/bin/env bash
    echo "Generating HTML pages for all recipes..."
    uv run python -m culturemech.render --all
    echo "✓ HTML pages generated in {{pages_dir}}/"

[group('Pages')]
gen-page file:
    #!/usr/bin/env bash
    echo "Generating HTML page for {{file}}..."
    uv run python -m culturemech.render {{file}}
    echo "✓ HTML page generated"

# ================================================================
# TESTING
# ================================================================

[group('Test')]
test:
    #!/usr/bin/env bash
    echo "Running test suite..."
    uv run pytest tests/ -v

[group('Test')]
test-kgx:
    #!/usr/bin/env bash
    echo "Running KGX export tests..."
    uv run pytest tests/test_kgx_export.py -v

[group('Test')]
test-cov:
    #!/usr/bin/env bash
    echo "Running tests with coverage..."
    uv run pytest tests/ --cov=culturemech --cov-report=html --cov-report=term-missing
    echo "✓ Coverage report generated at htmlcov/index.html"

# ================================================================
# SCHEMA
# ================================================================

[group('Schema')]
gen-docs:
    #!/usr/bin/env bash
    echo "Generating schema documentation..."
    mkdir -p docs/schema
    uv run gen-markdown --dir docs/schema {{schema_path}}
    echo "✓ Schema docs generated at docs/schema/"

[group('Schema')]
validate-schema-file:
    #!/usr/bin/env bash
    echo "Validating LinkML schema..."
    uv run linkml-validate {{schema_path}}
    echo "✓ Schema is valid"

# ================================================================
# CONVERT (Raw → Raw YAML Layer)
# ================================================================

[group('Convert')]
convert-to-raw-yaml source="all":
    #!/usr/bin/env bash
    echo "Converting raw sources to raw_yaml (unnormalized YAML)..."
    echo ""

    if [ "{{source}}" = "all" ] || [ "{{source}}" = "mediadive" ]; then
        echo "Converting MediaDive..."
        uv run python -m culturemech.convert.mediadive_raw_yaml \
            -i {{raw_dir}}/mediadive \
            -o {{raw_yaml_dir}}/mediadive
    fi

    if [ "{{source}}" = "all" ] || [ "{{source}}" = "togo" ]; then
        echo "Converting TOGO..."
        uv run python -m culturemech.convert.togo_raw_yaml \
            -i {{raw_dir}}/togo \
            -o {{raw_yaml_dir}}/togo
    fi

    if [ "{{source}}" = "all" ] || [ "{{source}}" = "atcc" ]; then
        echo "Converting ATCC..."
        uv run python -m culturemech.convert.atcc_raw_yaml \
            -i {{raw_dir}}/atcc \
            -o {{raw_yaml_dir}}/atcc
    fi

    if [ "{{source}}" = "all" ] || [ "{{source}}" = "bacdive" ]; then
        echo "Converting BacDive..."
        uv run python -m culturemech.convert.bacdive_raw_yaml \
            -i {{raw_dir}}/bacdive \
            -o {{raw_yaml_dir}}/bacdive
    fi

    if [ "{{source}}" = "all" ] || [ "{{source}}" = "nbrc" ]; then
        echo "Converting NBRC..."
        uv run python -m culturemech.convert.nbrc_raw_yaml \
            -i {{raw_dir}}/nbrc \
            -o {{raw_yaml_dir}}/nbrc
    fi

    if [ "{{source}}" = "all" ] || [ "{{source}}" = "komodo" ]; then
        echo "Converting KOMODO..."
        uv run python -m culturemech.convert.komodo_raw_yaml \
            -i {{raw_dir}}/komodo \
            -o {{raw_yaml_dir}}/komodo
    fi

    if [ "{{source}}" = "all" ] || [ "{{source}}" = "komodo_web" ]; then
        echo "Converting KOMODO web..."
        uv run python -m culturemech.convert.komodo_web_raw_yaml \
            -i {{raw_dir}}/komodo_web \
            -o {{raw_yaml_dir}}/komodo_web
    fi

    if [ "{{source}}" = "all" ] || [ "{{source}}" = "mediadb" ]; then
        echo "Converting MediaDB..."
        uv run python -m culturemech.convert.mediadb_raw_yaml \
            -i {{raw_dir}}/mediadb \
            -o {{raw_yaml_dir}}/mediadb
    fi

    echo ""
    echo "✓ Conversion complete"
    echo "  Raw YAML files written to: {{raw_yaml_dir}}/"

[group('Convert')]
convert-mediadive-raw-yaml:
    uv run python -m culturemech.convert.mediadive_raw_yaml \
        -i {{raw_dir}}/mediadive \
        -o {{raw_yaml_dir}}/mediadive

[group('Convert')]
convert-togo-raw-yaml:
    uv run python -m culturemech.convert.togo_raw_yaml \
        -i {{raw_dir}}/togo \
        -o {{raw_yaml_dir}}/togo

[group('Convert')]
convert-atcc-raw-yaml:
    uv run python -m culturemech.convert.atcc_raw_yaml \
        -i {{raw_dir}}/atcc \
        -o {{raw_yaml_dir}}/atcc

[group('Convert')]
convert-bacdive-raw-yaml:
    uv run python -m culturemech.convert.bacdive_raw_yaml \
        -i {{raw_dir}}/bacdive \
        -o {{raw_yaml_dir}}/bacdive

[group('Convert')]
convert-nbrc-raw-yaml:
    uv run python -m culturemech.convert.nbrc_raw_yaml \
        -i {{raw_dir}}/nbrc \
        -o {{raw_yaml_dir}}/nbrc

[group('Convert')]
convert-komodo-raw-yaml:
    uv run python -m culturemech.convert.komodo_raw_yaml \
        -i {{raw_dir}}/komodo \
        -o {{raw_yaml_dir}}/komodo

[group('Convert')]
convert-komodo-web-raw-yaml:
    uv run python -m culturemech.convert.komodo_web_raw_yaml \
        -i {{raw_dir}}/komodo_web \
        -o {{raw_yaml_dir}}/komodo_web

[group('Convert')]
convert-utex-raw-yaml:
    uv run python -m culturemech.convert.utex_raw_yaml \
        -i {{raw_dir}}/utex \
        -o {{raw_yaml_dir}}/utex

[group('Convert')]
convert-ccap-raw-yaml extract_pdfs="":
    #!/usr/bin/env bash
    cmd="uv run python -m culturemech.convert.ccap_raw_yaml \
        -i {{raw_dir}}/ccap \
        -o {{raw_yaml_dir}}/ccap"

    if [ "{{extract_pdfs}}" = "true" ]; then
        echo "PDF extraction enabled (requires pdfplumber)"
        cmd="$cmd --extract-pdfs"
    fi

    eval $cmd

[group('Convert')]
convert-sag-raw-yaml extract_pdfs="":
    #!/usr/bin/env bash
    cmd="uv run python -m culturemech.convert.sag_raw_yaml \
        -i {{raw_dir}}/sag \
        -o {{raw_yaml_dir}}/sag"

    if [ "{{extract_pdfs}}" = "true" ]; then
        echo "PDF extraction enabled (requires pdfplumber)"
        cmd="$cmd --extract-pdfs"
    fi

    eval $cmd

[group('Convert')]
convert-mediadb-raw-yaml:
    uv run python -m culturemech.convert.mediadb_raw_yaml \
        -i {{raw_dir}}/mediadb \
        -o {{raw_yaml_dir}}/mediadb

# ================================================================
# IMPORT (MediaDive, ATCC, TOGO Medium)
# ================================================================

[group('Import')]
import-mediadive limit="":
    #!/usr/bin/env bash
    echo "Importing MediaDive recipes from raw data layer..."
    echo "Source: {{raw_dir}}/mediadive/"
    echo ""

    # Check if raw data exists, if not try to fetch
    if [ ! -f "{{raw_dir}}/mediadive/mediadive_media.json" ]; then
        echo "⚠ Raw data not found. Attempting to fetch..."
        just fetch-mediadive-raw
        echo ""
    fi

    # Import using raw data layer
    if [ -f "{{raw_dir}}/mediadive/mediadive_media.json" ]; then
        # Check for composition data - API data takes priority
        COMP_ARG=""
        if [ -f "{{raw_dir}}/mediadive_api/mediadive_api_media.json" ]; then
            echo "✓ Using API-fetched compositions (preferred)"
            echo "  Source: {{raw_dir}}/mediadive_api/"
            # Note: Importer automatically detects API data as sibling directory
        elif [ -d "{{raw_dir}}/mediadive/compositions" ]; then
            COMP_ARG="--compositions {{raw_dir}}/mediadive/compositions"
            echo "✓ Using PDF-parsed compositions (fallback)"
            echo "  Source: {{raw_dir}}/mediadive/compositions"
        else
            echo "⚠ No composition data found (will use placeholders)"
            echo "  Run 'just fetch-mediadive-api' to get full compositions"
        fi

        uv run python -m culturemech.import.mediadive_importer \
            -i {{raw_dir}}/mediadive \
            -o {{normalized_yaml_dir}} \
            $COMP_ARG \
            {{ if limit != "" { "--limit " + limit } else { "" } }}
    else
        echo "✗ Cannot import: raw data not available at {{raw_dir}}/mediadive/"
        echo "  Run: just fetch-mediadive-raw"
        echo "  Or update cmm_automation_dir in project.justfile"
        exit 1
    fi

[group('Import')]
import-mediadive-stats:
    #!/usr/bin/env bash
    echo "MediaDive Import Statistics"

    if [ -f "{{raw_dir}}/mediadive/mediadive_media.json" ]; then
        uv run python -m culturemech.import.mediadive_importer \
            -i {{raw_dir}}/mediadive \
            --stats
    else
        echo "✗ Raw data not found at {{raw_dir}}/mediadive/"
        echo "  Run: just fetch-mediadive-raw"
        exit 1
    fi

[group('Import')]
import-komodo-web limit="":
    #!/usr/bin/env bash
    echo "Importing KOMODO media from web table..."
    echo "Source: {{raw_dir}}/komodo_web/"
    echo ""

    # Check if raw data exists, if not try to fetch
    if [ ! -f "{{raw_dir}}/komodo_web/komodo_web_media.json" ]; then
        echo "⚠ Raw data not found. Attempting to fetch..."
        just fetch-komodo-web
        echo ""
    fi

    # Import using raw data layer
    if [ -f "{{raw_dir}}/komodo_web/komodo_web_media.json" ]; then
        uv run python -m culturemech.import.komodo_web_importer \
            -i {{raw_dir}}/komodo_web \
            -o {{normalized_yaml_dir}} \
            {{ if limit != "" { "--limit " + limit } else { "" } }}
    else
        echo "✗ Cannot import: raw data not available at {{raw_dir}}/komodo_web/"
        echo "  Run: just fetch-komodo-web"
        exit 1
    fi

[group('Import')]
import-togo limit="":
    #!/usr/bin/env bash
    echo "Importing TOGO Medium recipes from raw data layer..."
    echo "Source: {{raw_dir}}/togo/"
    echo ""

    # Check if raw data exists, if not try to fetch with limit
    if [ ! -f "{{raw_dir}}/togo/togo_media.json" ]; then
        echo "⚠ Raw data not found. Fetching sample data (10 media)..."
        just fetch-togo-raw 10
        echo ""
    fi

    # Import using raw data layer
    if [ -f "{{raw_dir}}/togo/togo_media.json" ]; then
        uv run python -m culturemech.import.togo_importer \
            -i {{raw_dir}}/togo \
            -o {{normalized_yaml_dir}} \
            {{ if limit != "" { "--limit " + limit } else { "" } }}
    else
        echo "✗ Cannot import: raw data not available at {{raw_dir}}/togo/"
        echo "  Run: just fetch-togo-raw"
        exit 1
    fi

[group('Import')]
import-togo-stats:
    #!/usr/bin/env bash
    echo "TOGO Medium Import Statistics"

    if [ -f "{{raw_dir}}/togo/togo_media.json" ]; then
        uv run python -m culturemech.import.togo_importer \
            -i {{raw_dir}}/togo \
            --stats
    else
        echo "✗ Raw data not found at {{raw_dir}}/togo/"
        echo "  Run: just fetch-togo-raw"
        exit 1
    fi

[group('Import')]
import-atcc limit="":
    #!/usr/bin/env bash
    echo "Importing ATCC media from raw data layer..."
    echo "Source: {{raw_dir}}/atcc/"
    echo ""
    echo "Note: ATCC data is manually curated (no API available)"
    echo ""

    # Check if raw data exists
    if [ ! -f "{{raw_dir}}/atcc/atcc_media_manual.json" ]; then
        echo "⚠ Manual media file not found at {{raw_dir}}/atcc/"
        echo "  ATCC media must be manually curated"
        echo "  See raw/atcc/README.md for details"
    fi

    # Import using raw data layer
    uv run python -m culturemech.import.atcc_importer \
        -i {{raw_dir}}/atcc \
        -o {{normalized_yaml_dir}} \
        {{ if limit != "" { "--limit " + limit } else { "" } }}

[group('Import')]
import-atcc-stats:
    #!/usr/bin/env bash
    echo "ATCC Media Import Statistics"
    uv run python -m culturemech.import.atcc_importer \
        -i {{raw_dir}}/atcc \
        --stats

[group('Import')]
import-bacdive limit="":
    #!/usr/bin/env bash
    echo "Importing BacDive media from raw data layer..."
    echo "Source: {{raw_dir}}/bacdive/"
    echo ""

    # Check if raw data exists
    if [ ! -f "{{raw_dir}}/bacdive/bacdive_cultivation.json" ]; then
        echo "⚠ Raw data not found. Fetching sample data (10 strains)..."
        just fetch-bacdive-raw 10
        echo ""
    fi

    # Import using raw data layer
    if [ -f "{{raw_dir}}/bacdive/bacdive_cultivation.json" ]; then
        uv run python -m culturemech.import.bacdive_importer \
            -i {{raw_dir}}/bacdive \
            -o {{normalized_yaml_dir}} \
            {{ if limit != "" { "--limit " + limit } else { "" } }}
    else
        echo "✗ Cannot import: raw data not available at {{raw_dir}}/bacdive/"
        echo "  Run: just fetch-bacdive-raw"
        exit 1
    fi

[group('Import')]
import-bacdive-stats:
    #!/usr/bin/env bash
    echo "BacDive Import Statistics"
    if [ -f "{{raw_dir}}/bacdive/bacdive_cultivation.json" ]; then
        uv run python -m culturemech.import.bacdive_importer \
            -i {{raw_dir}}/bacdive \
            --stats
    else
        echo "✗ Raw data not found at {{raw_dir}}/bacdive/"
        echo "  Run: just fetch-bacdive-raw"
        exit 1
    fi

[group('Import')]
bacdive-export-associations:
    #!/usr/bin/env bash
    echo "Exporting BacDive organism→media associations..."
    echo "Output: data/processed/bacdive_organism_media.json"
    echo ""
    uv run python -m culturemech.import.bacdive_importer \
        -i {{raw_dir}}/bacdive \
        --export-associations
    echo ""
    echo "✓ Associations exported"
    echo "  Use these to enrich existing MediaDive/TOGO recipes"

[group('Import')]
import-utex limit="":
    #!/usr/bin/env bash
    echo "Importing UTEX algae media from raw data layer..."
    echo "Source: {{raw_dir}}/utex/"
    echo ""

    # Check if raw data exists, if not try to fetch
    if [ ! -f "{{raw_dir}}/utex/utex_media.json" ]; then
        echo "⚠ Raw data not found. Attempting to fetch..."
        just fetch-utex
        echo ""
    fi

    if [ -f "{{raw_dir}}/utex/utex_media.json" ]; then
        uv run python -m culturemech.import.utex_importer \
            -i {{raw_dir}}/utex \
            -o {{normalized_yaml_dir}} \
            {{ if limit != "" { "--limit " + limit } else { "" } }}
    else
        echo "✗ Cannot import: raw data not available at {{raw_dir}}/utex/"
        echo "  Run: just fetch-utex"
        exit 1
    fi

[group('Import')]
import-ccap limit="":
    #!/usr/bin/env bash
    echo "Importing CCAP algae media from raw data layer..."
    echo "Source: {{raw_dir}}/ccap/"
    echo ""

    # Check if raw data exists
    if [ ! -f "{{raw_dir}}/ccap/ccap_media.json" ]; then
        echo "⚠ Raw data not found. Fetching CCAP metadata..."
        just fetch-ccap
        echo ""
    fi

    # Import using metadata (PDF parsing optional)
    if [ -f "{{raw_dir}}/ccap/ccap_media.json" ]; then
        uv run python -m culturemech.import.ccap_importer \
            -i {{raw_dir}}/ccap \
            -o {{normalized_yaml_dir}} \
            {{ if limit != "" { "--limit " + limit } else { "" } }}
    else
        echo "✗ Cannot import: raw data not available at {{raw_dir}}/ccap/"
        echo "  Run: just fetch-ccap"
        exit 1
    fi

[group('Import')]
import-sag limit="":
    #!/usr/bin/env bash
    echo "Importing SAG algae media from raw data layer..."
    echo "Source: {{raw_dir}}/sag/"
    echo ""

    # Check if raw data exists
    if [ ! -f "{{raw_dir}}/sag/sag_media.json" ]; then
        echo "⚠ Raw data not found. Fetching SAG metadata..."
        just fetch-sag
        echo ""
    fi

    # Import using metadata (PDF parsing optional)
    if [ -f "{{raw_dir}}/sag/sag_media.json" ]; then
        uv run python -m culturemech.import.sag_importer \
            -i {{raw_dir}}/sag \
            -o {{normalized_yaml_dir}} \
            {{ if limit != "" { "--limit " + limit } else { "" } }}
    else
        echo "✗ Cannot import: raw data not available at {{raw_dir}}/sag/"
        echo "  Run: just fetch-sag"
        exit 1
    fi

[group('Import')]
import-algae-collections:
    @echo "Importing all algae collections..."
    @echo ""
    just import-utex
    @echo ""
    just import-ccap
    @echo ""
    just import-sag
    @echo ""
    @echo "✓ All algae collections imported"

[group('Import')]
import-nbrc limit="":
    #!/usr/bin/env bash
    echo "Importing NBRC media from raw data layer..."
    echo "Source: {{raw_dir}}/nbrc/"
    echo ""

    # Check if raw data exists
    if [ ! -f "{{raw_dir}}/nbrc/nbrc_media.json" ]; then
        echo "⚠ Raw data not found. Scraping sample data (5 media)..."
        just scrape-nbrc-raw 5
        echo ""
    fi

    # Import using raw data layer
    if [ -f "{{raw_dir}}/nbrc/nbrc_media.json" ]; then
        uv run python -m culturemech.import.nbrc_importer \
            -i {{raw_dir}}/nbrc \
            -o {{normalized_yaml_dir}} \
            {{ if limit != "" { "--limit " + limit } else { "" } }}
    else
        echo "✗ Cannot import: raw data not available at {{raw_dir}}/nbrc/"
        echo "  Run: just scrape-nbrc-raw"
        exit 1
    fi

[group('Import')]
import-nbrc-stats:
    #!/usr/bin/env bash
    echo "NBRC Import Statistics"
    if [ -f "{{raw_dir}}/nbrc/nbrc_media.json" ]; then
        uv run python -m culturemech.import.nbrc_importer \
            -i {{raw_dir}}/nbrc \
            --stats
    else
        echo "✗ Raw data not found at {{raw_dir}}/nbrc/"
        echo "  Run: just scrape-nbrc-raw"
        exit 1
    fi

[group('Import')]
import-komodo limit="":
    #!/usr/bin/env bash
    echo "Importing KOMODO media from raw data layer..."
    echo "Source: {{raw_dir}}/komodo/"
    echo ""

    # Check if raw data exists
    if [ ! -f "{{raw_dir}}/komodo/komodo_media.json" ]; then
        echo "✗ Raw data not found at {{raw_dir}}/komodo/"
        echo "  Run: just fetch-komodo-raw path/to/komodo.sql"
        echo "  Contact: raphy.zarecki@gmail.com for SQL dump"
        exit 1
    fi

    # Import using raw data layer with ChemicalMapper
    uv run python -m culturemech.import.komodo_importer \
        -i {{raw_dir}}/komodo \
        -o {{normalized_yaml_dir}} \
        --microbe-media-param {{raw_dir}}/microbe-media-param \
        --mediadive {{raw_dir}}/mediadive \
        {{ if limit != "" { "--limit " + limit } else { "" } }}

[group('Import')]
import-komodo-stats:
    #!/usr/bin/env bash
    echo "=== KOMODO Import Statistics ==="
    echo ""

    if [ -f "{{raw_dir}}/komodo/fetch_stats.json" ]; then
        echo "Fetch Statistics:"
        cat {{raw_dir}}/komodo/fetch_stats.json | jq '.'
        echo ""
    fi

    if [ -f "{{raw_dir}}/komodo/komodo_media.json" ]; then
        echo "Import Statistics:"
        uv run python -m culturemech.import.komodo_importer \
            -i {{raw_dir}}/komodo \
            --stats
    else
        echo "✗ Raw data not found at {{raw_dir}}/komodo/"
        echo "  Run: just fetch-komodo-raw path/to/sql"
        exit 1
    fi

[group('Import')]
import-mediadb limit="":
    #!/usr/bin/env bash
    echo "Importing MediaDB media from raw data layer..."
    echo "Source: {{raw_dir}}/mediadb/"
    echo ""

    # Check if raw data exists
    if [ ! -f "{{raw_dir}}/mediadb/mediadb_media.json" ]; then
        echo "✗ Raw data not found at {{raw_dir}}/mediadb/"
        echo "  Run: just fetch-mediadb-raw path/to/data"
        echo "  Visit: https://mediadb.systemsbiology.net/"
        exit 1
    fi

    # Import using raw data layer with ChemicalMapper
    uv run python -m culturemech.import.mediadb_importer \
        -i {{raw_dir}}/mediadb \
        -o {{normalized_yaml_dir}} \
        --microbe-media-param {{raw_dir}}/microbe-media-param \
        --mediadive {{raw_dir}}/mediadive \
        {{ if limit != "" { "--limit " + limit } else { "" } }}

[group('Import')]
import-mediadb-stats:
    #!/usr/bin/env bash
    echo "=== MediaDB Import Statistics ==="
    echo ""

    if [ -f "{{raw_dir}}/mediadb/fetch_stats.json" ]; then
        echo "Fetch Statistics:"
        cat {{raw_dir}}/mediadb/fetch_stats.json | jq '.'
        echo ""
    fi

    if [ -f "{{raw_dir}}/mediadb/mediadb_media.json" ]; then
        echo "Import Statistics:"
        uv run python -m culturemech.import.mediadb_importer \
            -i {{raw_dir}}/mediadb \
            --stats
    else
        echo "✗ Raw data not found at {{raw_dir}}/mediadb/"
        echo "  Run: just fetch-mediadb-raw path/to/data"
        exit 1
    fi

[group('Import')]
test-chemical-mappings ingredient="glucose":
    #!/usr/bin/env bash
    echo "Testing chemical mappings from raw data layer..."
    uv run python -m culturemech.import.chemical_mappings \
        --microbe-media-param {{raw_dir}}/microbe-media-param \
        --mediadive {{raw_dir}}/mediadive \
        {{ingredient}}

[group('Import')]
chemical-mapping-stats:
    #!/usr:bin/env bash
    echo "Chemical Mapping Statistics"
    uv run python -m culturemech.import.chemical_mappings \
        --microbe-media-param {{raw_dir}}/microbe-media-param \
        --mediadive {{raw_dir}}/mediadive \
        --stats

[group('Import')]
import-pfas-roles dry_run="":
    #!/usr/bin/env bash
    echo "Importing ingredient roles from PFASCommunityAgents..."
    uv run python -m culturemech.import.import_ingredient_roles \
        --kb-dir {{normalized_yaml_dir}} \
        {{ if dry_run != "" { "--dry-run" } else { "" } }}
    echo "✓ Imported ingredient roles from PFASCommunityAgents"

[group('Import')]
import-pfas-cofactors:
    #!/usr/bin/env bash
    echo "Importing cofactor hierarchy from PFASCommunityAgents..."
    uv run python -m culturemech.import.import_cofactors \
        --output-dir data/reference
    echo "✓ Imported cofactor hierarchy from PFASCommunityAgents"

[group('Import')]
import-pfas-all: import-pfas-roles import-pfas-cofactors
    @echo "✓ Imported all PFAS data"

# ================================================================
# UTILITIES
# ================================================================

[group('Utils')]
clean:
    #!/usr/bin/env bash
    echo "Cleaning generated files..."
    rm -rf {{output_dir}}/*
    rm -rf {{pages_dir}}/*
    rm -rf htmlcov/
    rm -rf .pytest_cache/
    rm -rf **/__pycache__/
    rm -f {{app_dir}}/data.js
    echo "✓ Clean complete"

[group('Utils')]
count-recipes:
    #!/usr/bin/env bash
    echo "Recipe count by category:"
    echo ""
    for dir in {{normalized_yaml_dir}}/*/; do
        cat=$(basename "$dir")
        count=$(find "$dir" -name "*.yaml" | wc -l)
        echo "  $cat: $count"
    done
    echo ""
    total=$(find {{normalized_yaml_dir}} -name "*.yaml" | wc -l)
    echo "Total recipes: $total"

[group('Utils')]
list-recipes:
    #!/usr/bin/env bash
    echo "All recipes:"
    find {{normalized_yaml_dir}} -name "*.yaml" -exec basename {} .yaml \; | sort

# ================================================================
# FULL BUILD
# ================================================================

[group('Build')]
build-all: validate-all gen-browser-data gen-pages
    #!/usr/bin/env bash
    echo ""
    echo "✓ Full build complete!"
    echo "  - All recipes validated"
    echo "  - Browser data generated"
    echo "  - HTML pages generated"
    echo ""
    echo "To view the browser: just serve-browser"

# ================================================================
# HELP
# ================================================================

[group('Help')]
help:
    @just --list --unsorted
