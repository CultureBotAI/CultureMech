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

# Knowledge-gap scan (Europe PMC, free) via shared kg_microbe_kgscan in claw.
# Dry-run by default → reports/knowledge_gap_scan.{json,md}. Pass `--apply`
# (and e.g. --limit/--min-score) to seed Discussion(kind=KNOWLEDGE_GAP).
knowledge-gap-scan *args:
    PYTHONPATH=../culturebotai-claw/src /opt/homebrew/bin/python3.13 \
      -m kg_microbe_kgscan --config conf/kgscan_config.yaml {{args}}

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

# Assess ingredient, concentration, and candidate media-variant state across
# data/normalized_yaml/**/*.yaml.
review-media-content *args:
    /opt/homebrew/bin/python3.13 scripts/build_media_content_review_manifest.py {{args}}

# Propose parent/child MediaRecipe variant links from the content review manifest.
propose-media-variant-links *args:
    /opt/homebrew/bin/python3.13 scripts/propose_media_variant_links.py {{args}}

# Validate bidirectional parent/child MediaRecipe variant links.
validate-media-variant-links *args:
    /opt/homebrew/bin/python3.13 scripts/validate_media_variant_links.py {{args}}

# Dry-run or apply proposed parent/child MediaRecipe variant links. Pass --apply
# explicitly to write YAML edits.
apply-media-variant-links *args:
    uv run python scripts/apply_media_variant_links.py {{args}}

# Render the media recipe-validation deep-research prompt for one medium (and
# its variant set) to stdout — for running validation natively in Claude Code,
# no Edison credits. Pass --template / --out to override. e.g.
#   just validate-media-recipe 1_10_r2a_medium
validate-media-recipe target *args:
    /opt/homebrew/bin/python3.13 scripts/render_media_prompt.py --target {{target}} {{args}}

# Same validation, run through the Edison deep-research API (spends credits).
# Pass --dry-run first to audit the rendered query. e.g.
#   just validate-media-recipe-edison 1_10_r2a_medium --dry-run
validate-media-recipe-edison target *args:
    uv run --extra dev python scripts/research_media_edison.py \
      --target {{target}} --template templates/media_recipe_validation.md {{args}}

# Backfill the multi-axis media-type vocabulary (composition_type /
# nutritional_class / functional_role) from the deprecated medium_type slot.
# Dry-run by default; pass --apply to write. Optionally pass specific paths. e.g.
#   just migrate-medium-type-axes            # whole corpus, dry-run
#   just migrate-medium-type-axes --apply
migrate-medium-type-axes *args:
    uv run --extra dev python scripts/migrate_medium_type_axes.py {{args}}

# Discussions / knowledge-gap browser (shared kg_microbe_discussions in claw).
gen-discussions-data:
    PYTHONPATH=../culturebotai-claw/src /opt/homebrew/bin/python3.13 \
      -m kg_microbe_discussions --config conf/discussions_config.yaml --output app/discussions
