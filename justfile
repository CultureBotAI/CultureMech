# CultureMech - Main Build File
# Imports project-specific recipes from project.justfile

set dotenv-load := true

# Binds recipe arguments to "$@" in shebang recipes so multi-word arguments keep
# their quoting. Needed by `new-history`, whose --summary/--details are prose;
# plain `{{args}}` interpolation splits them on whitespace. No existing recipe
# uses $1/$@, so enabling this changes nothing else.
set positional-arguments := true

# Shared tooling lives in the culturebotai-claw checkout. Override CLAW_SRC when
# claw is not the default sibling directory — CI checks it out elsewhere.
claw_src := env_var_or_default("CLAW_SRC", "../culturebotai-claw/src")
claw_root := parent_directory(claw_src)

# Fail loudly when a shared claw module is missing, rather than running on and
# producing an empty or wrong result. A skip-when-missing variant of this check
# is exactly what let a vendored-sync job pass while verifying nothing
# (CultureMech#112 lane).
_require-claw module:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ ! -d "{{claw_src}}/{{module}}" ]; then
      echo "error: shared module '{{module}}' not found under '{{claw_src}}'." >&2
      echo "Set CLAW_SRC to the src/ directory of a culturebotai-claw checkout." >&2
      exit 1
    fi

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
    uv run python src/culturemech/render_media_pages.py {{args}}

# Generate the QC dashboard (slot coverage + matplotlib chart) into
# dashboard/. Driven by conf/qc_config.yaml.
gen-qc-dashboard: (_require-claw "kg_microbe_qc")
    PYTHONPATH={{claw_src}} uv run python \
      -m kg_microbe_qc --config conf/qc_config.yaml --output dashboard

# Knowledge-gap scan (Europe PMC, free) via shared kg_microbe_kgscan in claw.
# Dry-run by default → reports/knowledge_gap_scan.{json,md}. Pass `--apply`
# (and e.g. --limit/--min-score) to seed Discussion(kind=KNOWLEDGE_GAP).
knowledge-gap-scan *args: (_require-claw "kg_microbe_kgscan")
    PYTHONPATH={{claw_src}} uv run python -m kg_microbe_kgscan \
      --config conf/kgscan_config.yaml {{args}}

# Composite: media pages + QC dashboard (Phase 2 outputs).
gen-phase2: gen-media-pages gen-qc-dashboard

# === Growth-evidence literature pipeline (per plan
# `now-focus-on-culturemech-piped-shell.md`) ============================

# Phase A: mine PubMed for candidate (organism, genome_id, growth_metrics,
# evidence) tuples per MediaRecipe and emit one proposal YAML per medium
# under workspace/reports/growth_evidence_proposals/. Default dry-run.
propose-growth *args:
    uv run python scripts/propose_growth_evidence.py {{args}}

# Phase B: harvest PMIDs from data/normalized_yaml/**/*.yaml evidence blocks
# and cache abstracts as Markdown under references_cache/. Idempotent.
fetch-pubmed *args:
    uv run python scripts/fetch_pubmed_abstracts.py {{args}}

# Phase C: read curator-vetted proposals from
# workspace/reports/growth_evidence_proposals/ and write target_organisms /
# growth_metrics / genome_assembly_id blocks into the MediaRecipe YAMLs.
apply-growth *args:
    uv run python scripts/apply_growth_evidence.py {{args}}

# Phase D: anti-hallucination gate. Verify every evidence snippet attached
# to a target_organisms or growth_metrics block appears verbatim in the
# cached PubMed abstract for the cited PMID. Exit 2 on any mismatch.
validate-growth *args:
    uv run python scripts/validate_evidence_references.py {{args}}

# Phase E: fill missing genome_assembly_id values for organisms with a
# resolved NCBITaxon term — local SAMN TSV first, then NCBI Datasets API
# fallback. Default dry-run.
enrich-genomes *args:
    uv run python scripts/enrich_genome_ids.py {{args}}

# Assess ingredient, concentration, and candidate media-variant state across
# data/normalized_yaml/**/*.yaml.
review-media-content *args:
    uv run python scripts/build_media_content_review_manifest.py {{args}}

# Propose parent/child MediaRecipe variant links from the content review manifest.
propose-media-variant-links *args:
    uv run python scripts/propose_media_variant_links.py {{args}}

# Validate bidirectional parent/child MediaRecipe variant links.
validate-media-variant-links *args:
    uv run python scripts/validate_media_variant_links.py {{args}}

# Dry-run or apply proposed parent/child MediaRecipe variant links. Pass --apply
# explicitly to write YAML edits.
apply-media-variant-links *args:
    uv run python scripts/apply_media_variant_links.py {{args}}

# Render the media recipe-validation deep-research prompt for one medium (and
# its variant set) to stdout — for running validation natively in Claude Code,
# no Edison credits. Pass --template / --out to override. e.g.
#   just validate-media-recipe 1_10_r2a_medium
validate-media-recipe target *args:
    uv run python scripts/render_media_prompt.py --target {{target}} {{args}}

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
gen-discussions-data: (_require-claw "kg_microbe_discussions")
    PYTHONPATH={{claw_src}} uv run python \
      -m kg_microbe_discussions --config conf/discussions_config.yaml --output app/discussions

# ============== Curation history ==============

# Scaffold an append-only curation-history record. See history/README.md. e.g.
#   just new-history --kind record --slug 1_10_r2a_medium \
#     --target-root data/normalized_yaml/bacterial \
#     --event EDIT --outcome changed --sections ingredients \
#     --summary "Ground two ingredients to CHEBI" \
#     --details "What was done, what evidence was used, how it was validated."
new-history *args:
    #!/usr/bin/env bash
    set -euo pipefail
    claw_src="${CLAW_SRC:-../culturebotai-claw/src}"
    if [ ! -d "$claw_src/kg_microbe_history" ]; then
      echo "new-history: kg_microbe_history not found under '$claw_src'." >&2
      echo "Set CLAW_SRC to the src/ directory of a culturebotai-claw checkout." >&2
      exit 1
    fi
    # "$@" not {{args}} — see `set positional-arguments` at the top of this file.
    # `uv run python`, not `python3`: bare python3 is whatever the machine puts
    # first on PATH, which is the same undeclared-interpreter problem that has
    # bitten other recipes here.
    PYTHONPATH="$claw_src" uv run python -m kg_microbe_history new "$@"

# Validate one history record, or a directory of them. Uses the VENDORED schema,
# so this works with no claw checkout — same as CI.
validate-history target="history":
    #!/usr/bin/env bash
    set -euo pipefail
    target="{{target}}"
    if [ -z "$target" ]; then
      echo "validate-history: empty target. Pass a record path or a directory." >&2
      exit 2
    fi
    if [ ! -e "$target" ]; then
      echo "validate-history: '$target' does not exist." >&2
      exit 2
    fi
    if [ -d "$target" ]; then
      if [ -z "$(find "$target" -name '*.yaml' -print -quit)" ]; then
        echo "No history records under '$target'."
        exit 0
      fi
      find "$target" -name '*.yaml' -print0 \
        | xargs -0 uv run linkml-validate \
            --schema src/culturemech/schema/history.yaml --target-class HistoryRecord
    else
      uv run linkml-validate \
        --schema src/culturemech/schema/history.yaml --target-class HistoryRecord "$target"
    fi
