# CultureMech - Main Build File
# Imports project-specific recipes from project.justfile

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
