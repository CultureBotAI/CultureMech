# CultureMech - Main Build File
# Imports project-specific recipes from project.justfile

set dotenv-load := true

import 'project.justfile'

# Default recipe: show help
default:
    @just --list --unsorted

# Quick validation shortcut
v file:
    just validate {{file}}

# Quick schema validation shortcut
vs file:
    just validate-schema {{file}}

# Render per-medium HTML pages from data/merge_yaml/merged_2026/*.yaml
# into pages/media/. Idempotent (skips fresh outputs); pass --force to
# regenerate everything. New dismech-pattern pipeline (parallel to the
# legacy `gen-pages` recipe in project.justfile, which renders from a
# different YAML source via culturemech.render). See
# ../culturebotai-claw/docs/proposals/phase2_culturemech_html_pages_and_qc_dashboard.md
gen-media-pages *args:
    /opt/homebrew/bin/python3.13 src/culturemech/render_media_pages.py {{args}}

# Generate the QC dashboard (slot coverage + matplotlib chart) into
# dashboard/. Driven by conf/qc_config.yaml.
gen-qc-dashboard:
    PYTHONPATH=../culturebotai-claw/src /opt/homebrew/bin/python3.13 \
      -m kg_microbe_qc --config conf/qc_config.yaml --output dashboard

# Composite: media pages + QC dashboard (Phase 2 outputs).
gen-phase2: gen-media-pages gen-qc-dashboard

# === Growth-evidence literature pipeline (per plan
# `now-focus-on-culturemech-piped-shell.md`) ============================

# Phase A: mine PubMed for candidate (organism, genome_id, growth_metrics,
# evidence) tuples per MediaRecipe and emit one proposal YAML per medium
# under workspace/reports/growth_evidence_proposals/. Default dry-run.
propose-growth *args:
    /opt/homebrew/bin/python3.13 scripts/propose_growth_evidence.py {{args}}

# Phase B: harvest PMIDs from data/normalized_yaml/**/*.yaml evidence blocks
# and cache abstracts as Markdown under references_cache/. Idempotent.
fetch-pubmed *args:
    /opt/homebrew/bin/python3.13 scripts/fetch_pubmed_abstracts.py {{args}}

# Phase C: read curator-vetted proposals from
# workspace/reports/growth_evidence_proposals/ and write target_organisms /
# growth_metrics / genome_assembly_id blocks into the MediaRecipe YAMLs.
apply-growth *args:
    /opt/homebrew/bin/python3.13 scripts/apply_growth_evidence.py {{args}}

# Phase D: anti-hallucination gate. Verify every evidence snippet attached
# to a target_organisms or growth_metrics block appears verbatim in the
# cached PubMed abstract for the cited PMID. Exit 2 on any mismatch.
validate-growth *args:
    /opt/homebrew/bin/python3.13 scripts/validate_evidence_references.py {{args}}

# Phase E: fill missing genome_assembly_id values for organisms with a
# resolved NCBITaxon term — local SAMN TSV first, then NCBI Datasets API
# fallback. Default dry-run.
enrich-genomes *args:
    /opt/homebrew/bin/python3.13 scripts/enrich_genome_ids.py {{args}}
