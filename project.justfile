# CultureMech Build System
# Build recipes for validation, export, and deployment

schema_path := "src/culturemech/schema/culturemech.yaml"
oak_config := "conf/oak_config.yaml"
output_dir := "output"
pages_dir := "pages"
app_dir := "app"

# Data layer paths (see DATA_LAYERS.md)
# Four-tier system: raw/ → raw_yaml/ → normalized_yaml/ → merge_yaml/
raw_dir := "data/raw"
raw_yaml_dir := "data/raw_yaml"
normalized_yaml_dir := "data/normalized_yaml"
merge_yaml_dir := "data/merge_yaml"
processed_data_dir := "data/processed"
cmm_automation_dir := "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/cmm-ai-automation/data"
microbe_media_param_dir := "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MicrobeMediaParam/MicroMediaParam/pipeline_output/merge_mappings"
research_dir := "research"
templates_dir := "templates"

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

# ================================================================
# DEEP RESEARCH
# ================================================================

# The fleet entity-runner contract (#289): `research-entity <provider> <target>
# [focus]`. Same shape in every Mech; only target resolution and the focus table
# are domain-specific. `just research-focuses` lists the focuses and the prompt
# each one renders.
#
# The focus picks the template — it is no longer pinned to the growth prompt
# here, which is what let `--focus formulation` rank providers for formulation
# work and then research growth evidence anyway.
#
# `focus` is POSITIONAL, so flags must come after it:
#     just research-entity claude_code ko2_no3 formulation --dry-run
#     just research-entity claude_code ko2_no3 growth_evidence --dry-run
# Omitting the focus and passing a flag third would bind the flag to `focus`.
# `research-media` below takes no positional focus for exactly that reason.
[group('Research')]
research-entity provider target focus="growth_evidence" *args="":
    uv run --extra dev python scripts/research_media.py \
      --provider "{{provider}}" \
      --target "{{target}}" \
      --focus="{{focus}}" \
      --research-dir {{research_dir}} \
      {{args}}

# Compatibility alias, kept because scripts, batch files and the skills call it.
#
# Its signature is deliberately UNCHANGED — `provider target *args`, no
# positional focus. Adding one silently broke the documented form
# `just research-media claude_code ko2_no3 --dry-run`, because `--dry-run` bound
# to `focus` and the runner then saw `--focus --dry-run`. Existing callers keep
# working; pass `--focus formulation` through args, or use `research-entity`.
[group('Research')]
research-media provider target *args="":
    @just research-entity "{{provider}}" "{{target}}" growth_evidence {{args}}

[group('Research')]
research-focuses:
    uv run --extra dev python scripts/research_media.py --list-focuses

[group('Research')]
research-providers:
    uv run --extra dev python scripts/research_media.py --list-providers

[group('Research')]
research-provider provider:
    uv run --extra dev python scripts/research_media.py --provider {{provider}} --provider-info

# Edison Scientific deep research via the `edison-client` SDK. Default
# job is LITERATURE (PaperQA3). Pass `--job literature-high` etc. via
# *args. Requires EDISON_PLATFORM_API_KEY (or EDISON_API_KEY) in env
# or .env. See scripts/research_media_edison.py for details.
[group('Research')]
# Media research via the local Codex CLI (#284). Needs `codex` on PATH and
# web_search enabled in ~/.codex/config.toml; both are checked before it runs.
[group('Research')]
research-media-codex target *args="":
    uv run --extra dev python scripts/research_media_codex.py --target {{target}} {{args}}

research-media-edison target *args="":
    uv run --extra dev python scripts/research_media_edison.py \
      --target {{target}} \
      --template {{templates_dir}}/media_growth_research.md \
      --out-dir {{research_dir}}/media \
      {{args}}

# Batch variant: walk a edison_batch.json priority list and research
# the first N recipes. Default --limit is unset (run all 100); always
# pass `--limit 5` (or similar) on first runs to bound credit spend.
# Records with a completed run for the same job are skipped, so `--limit 5`
# advances 5 FRESH records per invocation rather than re-billing the first
# five. Pass `--force` to re-submit them anyway.
# Draw a stratified sample of media for Edison axis classification (#152), across
# SEMI_DEFINED / deep-research-ranked / well-known / other. Seeded, so a rerun
# researches the same records rather than a new set. Writes:
#   data/import_tracking/reports/axis_research_batch.json
[group('Research')]
sample-axis-research-batch *args="":
    uv run --extra dev python scripts/sample_axis_research_batch.py {{args}}

# Edison axis classification (#152) — nutritional_class / functional_role.
#
# Deliberately a SEPARATE recipe with a SEPARATE out-dir, not a --template flag on
# research-media-edison-batch. Both templates run under job LITERATURE and the
# output filename is <slug>-edison-literature.md, so writing axis reports into
# research/media/ would make a later growth-research run on those slugs skip
# itself as "already researched" — a silent no-op, not an error.
[group('Research')]
research-media-edison-axis batch *args="":
    uv run --extra dev python scripts/research_media_edison.py \
      --batch {{batch}} \
      --template {{templates_dir}}/media_axis_classification.md \
      --out-dir {{research_dir}}/media_axis \
      {{args}}

[group('Research')]
research-media-edison-batch batch *args="":
    uv run --extra dev python scripts/research_media_edison.py \
      --batch {{batch}} \
      --template {{templates_dir}}/media_growth_research.md \
      --out-dir {{research_dir}}/media \
      {{args}}

# Phase-2 follow-up: drill into one organism reported in phase-1
# results and extract the recipe + culture conditions + identifiers
# from the primary publication. See
# scripts/research_organism_recipe_edison.py for the full arg list
# (--strain, --identifiers, --citation-hint, --phase1-snippet,
# --organisms-batch, etc.).
# Retroactively pull verbose response + agent state + files +
# parsed citations for every research/media/*-edison-*-meta.yaml
# that has a real task_id but is missing sidecars. The fetch is
# metadata-only — Edison serves cached task results, so no compute
# is re-billed. See scripts/enrich_edison_response.py.
[group('Research')]
enrich-edison-response *args="":
    uv run --extra dev python scripts/enrich_edison_response.py {{args}}

# Rank every CultureMech media record for deep-research priority.
# Writes:
#   data/import_tracking/reports/deep_research_priority.json       (full list)
#   data/import_tracking/reports/deep_research_priority_top100.json (top 100, batch-ready)
#   data/import_tracking/reports/deep_research_priority.md          (human report)
# The top-100 JSON is compatible with `research-media-edison-batch`.
# Already-researched records are excluded via the TRACKED manifest
# data/import_tracking/researched_media.json — not by scanning the gitignored
# research/ tree — so the reports are reproducible from git alone (#121).
# If the manifest is stale, run `just refresh-researched-manifest` FIRST and
# commit that diff separately, so a report refresh never mixes the two.
[group('Research')]
prioritize-deep-research-candidates *args="":
    uv run --extra dev python scripts/prioritize_deep_research_candidates.py {{args}}

# Rank media records by how badly they need curation review — the INVERSE of
# prioritize-deep-research-candidates, which ranks by expected research yield and
# hard-filters zero-ingredient records. Signals: absent/placeholder/unparsed
# composition, ungrounded ingredients, untraceable provenance, strain-pointer
# names. Writes data/import_tracking/reports/review_need_ranking.tsv
#     just score-review-need --top 40
[group('QC')]
score-review-need *args="":
    uv run --extra dev python scripts/score_review_need.py {{args}}

# Turn the 25 NBRC records whose composition was crammed into one ingredient name
# into a structured worklist (#166). REPORT ONLY — it never writes, because a parse
# can round-trip and still be wrong: "KH2PO40.85g" splits equally well into
# KH2PO4+0.85g and KH2PO+40.85g. Writes:
#   data/import_tracking/reports/unparsed_compositions.tsv
[group('QC')]
report-unparsed-compositions *args="":
    uv run --extra dev python scripts/report_unparsed_compositions.py {{args}}

# Find records whose composition_type contradicts their own ingredient list (#158):
# `DEFINED` asserted while listing yeast extract, peptone, tryptone etc. Reports by
# default; `--apply` restamps only records carrying >= 5 g/L of undefined material,
# where SEMI_DEFINED's "a small amount" cannot apply. Writes:
#   data/import_tracking/reports/composition_type_conflicts.tsv
[group('QC')]
audit-composition-type *args="":
    uv run --extra dev python scripts/audit_composition_type.py {{args}}

# Triage recipes that share a filename across category directories (#116).
# Classifies each collision IDENTICAL / EQUIVALENT / DIFFERENT so the manual
# curation pass is tractable. Read-only — moves, renames and deletes are
# deliberately NOT automated here. Writes:
#   data/import_tracking/reports/filename_collisions.tsv
[group('QC')]
audit-filename-collisions *args="":
    uv run --extra dev python scripts/audit_filename_collisions.py {{args}}

# Flag implausible ingredient concentrations (#118): stock-solution values and
# unit slips stored as final per-litre medium concentrations. Read-only. Writes:
#   data/import_tracking/reports/concentration_plausibility.tsv            (per row)
#   data/import_tracking/reports/concentration_plausibility_by_record.tsv  (per record,
#     with a `flattened_cocktail` flag marking the actionable subset)
# Baseline history (#150): 11,540 rows across 3,914 records at the time the gate
# was added — the backlog #135's audit found and #118 never repaired. The gate
# blocks NEW implausible concentrations without demanding the backlog be cleared
# first, the same convention as `check-chebi-grounding`. LOWER the baseline as
# records are repaired; raising it to make a run pass defeats the point.
# Report media named for a selective agent their ingredient list omits (#181).
# Report-only: recovering a lost concentration needs the upstream record, and a
# plausible guess that round-trips is still false chemistry (#166).
# Triage the media that carry no usable composition (#175). Report-only: the
# obvious repair — resolving "X solution (medium N)" to medium N's composition —
# would write a whole medium's recipe into a solution record. See the docstring.
# Mark stock solutions that were imported as media records (#175). Asserts
# `record_kind: SOLUTION` — a curated claim, not derived from the name at read
# time, so it lands in a reviewable diff. Report-only without --apply.
[group('Curation')]
retype-solution-records *args="":
    uv run --extra dev python scripts/retype_solution_records.py {{args}}

# Inventory and classify every tracked derived artifact, and verify that the
# freshness-checkable ones still match a fresh run (#145). A record move leaves
# stale paths in artifacts nothing refreshes; only the indexes failed loudly.
[group('QC')]
audit-derived-artifacts *args="":
    uv run --extra dev python scripts/audit_derived_artifacts.py {{args}}

# The one follow-up step after a bulk record move: regenerate the current-view
# artifacts, then review and commit the diff.
[group('Curation')]
refresh-derived:
    uv run --extra dev python scripts/audit_derived_artifacts.py --refresh

[group('QC')]
triage-missing-compositions *args="":
    uv run --extra dev python scripts/triage_missing_compositions.py {{args}}

# Keep medium_type populated and derived from composition_type (#165). It is a
# MAINTAINED axis: kgx_export emits one edge per record from it, so a missing value
# silently drops an edge from the knowledge graph. Report-only without --apply.
[group('Curation')]
curate-medium-type *args="":
    uv run --extra dev python scripts/curate_medium_type.py {{args}}

# Backfill organism_culture_type (isolate vs community) on records that name
# target_organisms (#142). recommended:, so validate-strict never flags the gap.
# Sets `isolate` where specific strains are named; leaves community signals for a
# curator. Report-only without --apply.
[group('Curation')]
curate-organism-culture-type *args="":
    uv run --extra dev python scripts/curate_organism_culture_type.py {{args}}

# Remove the "See source for composition" placeholder ingredient (#175): a fake
# component that pollutes text scans. The incomplete_composition flag carries the
# state instead. Report-only without --apply.
[group('Curation')]
curate-placeholder-composition *args="":
    uv run --extra dev python scripts/curate_placeholder_composition.py {{args}}

# Flag media with no ingredients and no solutions as incomplete_composition (#175),
# so a silently-empty record is visible rather than reading as complete. Does not
# decide the record's fate (re-import / accept / retire). Report-only without --apply.
[group('Curation')]
curate-flag-empty-composition *args="":
    uv run --extra dev python scripts/curate_flag_empty_composition.py {{args}}

# Propose (never apply) how to nest each of the 579 flattened stock cocktails under
# a solution with an addition volume (#150). Recovers the volume from the record's
# own preparation_steps/notes where possible; marks the rest MANUAL. Emits a curator
# worklist, edits nothing — the addition volume is judgement-heavy and a wrong one
# corrupts a real recipe.
[group('QC')]
propose-cocktail-nesting *args="":
    uv run --extra dev python scripts/propose_cocktail_nesting.py {{args}}

# Fetch authoritative stock-solution ADDITION volumes from MediaDive for the
# flattened cocktails (#150). MediaDive states the volume as a structured
# solution reference ("Wolfe's mineral elixir, 1 ml"), so it is read rather than
# guessed from prose — 180 of 186 resolvable records get a real volume this way.
# Read-only; run before `propose-cocktail-nesting` so the worklist carries them.
[group('QC')]
fetch-mediadive-volumes *args="":
    uv run --extra dev python scripts/fetch_mediadive_solution_volumes.py {{args}}

# Nest flattened stock cocktails under their solution, using the MediaDive stock
# composition + addition volume (#150). Moves an ingredient ONLY when it matches the
# stock by name AND value, so a bulk salt sharing a name (NaCl 39.97 vs the stock's
# 10) is never moved. Refuses a record whose flagged rows do not all match rather
# than half-repairing it. Report-only without --apply; needs fetch-mediadive-volumes.
# Check every corpus medium id against the MediaDive catalogue by NAME (#244).
# Established that the corpus's own mediadive.medium ids are sound (3,325/3,325) and
# that the KOMODO->DSMZ mapping is what misleads (~72% land on another medium), so a
# komodo id must never be used as a MediaDive id without a name check. Read-only.
# List flattened cocktails that MediaDive cannot supply a stock+volume for, with the
# reason each is blocked (#150). Feeds Edison via
# templates/media_stock_solution_research.md. Read-only.
# Name the stock a blocked flattened cocktail came from, by exact name+value match
# against every stock MediaDive has returned (#150). Reports the stock's observed
# volume distribution as EVIDENCE and deliberately does not fill the volume in —
# see the script docstring for why the invariant-volume shortcut does not hold.
[group('QC')]
identify-cocktail-stocks *args="":
    uv run --extra dev python scripts/identify_cocktail_stocks.py {{args}}

[group('QC')]
list-cocktail-research-targets *args="":
    uv run --extra dev python scripts/list_cocktail_research_targets.py {{args}}

[group('QC')]
audit-mediadive-ids *args="":
    uv run --extra dev python scripts/audit_mediadive_ids.py {{args}}

# Resolve KOMODO-sourced cocktails to their base MediaDive medium (#150). Read-only.
[group('Curation')]
fetch-komodo-volumes *args="":
    uv run --extra dev python scripts/fetch_komodo_base_volumes.py {{args}}

# Promote KOMODO volume candidates the composition confirms (#262). Read-only by default.
[group('Curation')]
promote-komodo-candidates *args="":
    uv run --extra dev python scripts/promote_komodo_volume_candidates.py {{args}}

[group('Curation')]
apply-cocktail-nesting *args="":
    uv run --extra dev python scripts/apply_cocktail_nesting.py {{args}}

# Correct groundings that name the wrong chemical species (#256). Dry run by default.
[group('Curation')]
fix-wrong-groundings *args="":
    uv run --extra dev python scripts/fix_wrong_compound_groundings.py {{args}}

# Ingredient names the corpus grounds more than one way (#258). Read-only.
# Set term.label from the ontology (#259). Run AFTER fixing groundings, not before.
[group('Curation')]
refill-term-labels *args="":
    uv run --extra dev python scripts/refill_term_labels.py {{args}}

# Groundings whose term formula lacks an element the name demands (#276/#278).
[group('QC')]
audit-name-term-elements *args="":
    uv run --extra dev python scripts/audit_name_term_elements.py {{args}}

[group('QC')]
audit-grounding-consistency *args="":
    uv run --extra dev python scripts/audit_grounding_consistency.py {{args}}

[group('QC')]
audit-selective-agent-mismatch *args="":
    uv run --extra dev python scripts/audit_selective_agent_mismatch.py {{args}}

[group('QC')]
audit-concentration-plausibility *args="":
    uv run --extra dev python scripts/audit_concentration_plausibility.py \
        --max-allowed 9757 --max-cocktails 186 {{args}}

# Composition tables that were never parsed, plus prose sitting in name slots
# (#299, #273). Baselines are today's counts: 64 findings, none of which reach
# the KGX export. Lower them as the backlog is repaired; never raise one to make
# a run pass.
#
# Was 169/31 before `just recover-nbrc-composition` restored 58 composition
# tables from the preserved scrape and repaired 4 more surgically.
# `--max-exported 0` is now an absolute gate rather than a ratchet: no unparsed
# composition may reach the graph at all.
#
# `--max-exported` is the sharper of the two. Only UNPARSED_SOLUTION_TABLE
# reaches the KGX export -- solution ids are minted from `preferred_term` and
# need no grounding, whereas the ingredient findings are ungrounded and emit no
# edge -- so a rise there means new garbage nodes in the graph.
# Recover NBRC composition tables from the preserved source HTML (#299).
#
# Dry-run by default; `--limit 1` canaries a single record. Needs
# `data/raw/nbrc/scraped/`, which is gitignored, so this only runs on a machine
# that has the scrape -- the recovered YAML is what gets committed.
[group('Curation')]
recover-nbrc-composition *args="":
    uv run --extra dev python scripts/recover_nbrc_composition.py {{args}}

[group('QC')]
audit-unparsed-composition *args="":
    uv run --extra dev python scripts/audit_unparsed_composition.py \
        --max-allowed 64 --max-exported 0 {{args}}

# Compare our ingredient groundings against MIM's published SSSOM (#256).
#
# This has to live here rather than in MIM: kg-microbe resolves an ingredient
# with `best_primary([chebi_id, culturemech_term_id, mim_id, ...])`, so OUR
# `term.id` outranks MIM's. When MIM corrects a mapping the consumer still picks
# ours, and MIM can only fix rows we hold no opinion on.
#
# Baselines are names, not rows -- one regrounding decision fixes every row of a
# name. Today: 12 divergent, 75 internally split. Lower them as the backlog is
# curated; never raise one to make a run pass.
#
# Needs MediaIngredientMech checked out beside this repo; pass --sssom otherwise.
[group('QC')]
audit-mim-sssom *args="":
    uv run --extra dev python scripts/audit_mim_sssom_divergence.py \
        --max-divergent 12 --max-split 75 {{args}}

# Merge locally-completed Edison runs (research/media/*-meta.yaml, gitignored)
# into the tracked researched-media manifest. This is the only step that reads
# untracked research state; review and commit the resulting diff. Entries are
# merged, never dropped, so several machines can contribute safely.
#   just refresh-researched-manifest --dry-run   # preview additions
[group('Research')]
refresh-researched-manifest *args="":
    uv run --extra dev python scripts/refresh_researched_manifest.py {{args}}

# Rank MediaIngredientMech ingredients for Step 7b Edison role-research.
# Cross-repo scan of ../MediaIngredientMech/data/ingredients/**/*.yaml scored by
# (# facets missing) × log(occurrence) × mapped-mult × chebi-mult, minus records
# that already have completed Edison role research. Writes:
#   data/import_tracking/reports/role_research_priority.json  (batch-ready)
# Output is a batch payload accepted by MIM's `research-ingredient-roles-edison-batch`.
[group('Research')]
prioritize-role-research-candidates *args="":
    uv run --extra dev python scripts/prioritize_role_research_candidates.py {{args}}

# Extract structured role assignments from Edison role-research bundles.
# Consumes `-edison-literature.md` files under a directory (or single files) and
# emits two batch JSONs:
#   --out-mim  → rich shape for MIM `apply_role_research_results.py`
#   --out-cm   → scalar shape for CultureMech's future `apply_ingredient_roles`
#
# Default: scans ../MediaIngredientMech/research/ingredients/roles/
# Example: just extract-roles-from-edison
[group('Research')]
extract-roles-from-edison inputs="../MediaIngredientMech/research/ingredients/roles" *args="":
    uv run --extra dev python scripts/extract_roles_from_edison.py {{inputs}} {{args}}

# Apply the scalar-projection role batch (from `extract-roles-from-edison --out-cm`)
# across every recipe under data/normalized_yaml/. Fills empty facet slots on
# ingredient descriptors whose CHEBI id matches a batch proposal; never overwrites
# curator assignments. Adds a curation-history event per changed recipe.
[group('Research')]
apply-ingredient-roles batch *args="":
    uv run --extra dev python scripts/apply_ingredient_roles.py {{batch}} {{args}}

[group('Research')]
research-organism-recipe-edison target organism *args="":
    uv run --extra dev python scripts/research_organism_recipe_edison.py \
      --target {{target}} \
      --organism {{organism}} \
      --template {{templates_dir}}/medium_organism_recipe_extraction.md \
      --out-dir {{research_dir}}/media \
      {{args}}

# Batch variant of the phase-2 per-organism follow-up. Takes a JSON
# list (one entry per organism: {target, organism, strain?,
# identifiers?, citation_hint?, phase1_snippet?}). Always pass
# `--limit N` on first runs to bound credit spend.
[group('Research')]
research-organism-recipe-edison-batch batch *args="":
    uv run --extra dev python scripts/research_organism_recipe_edison.py \
      --organisms-batch {{batch}} \
      --template {{templates_dir}}/medium_organism_recipe_extraction.md \
      --out-dir {{research_dir}}/media \
      {{args}}

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
# MERGE (Layer 4: Recipe Deduplication)
# ================================================================

[group('Merge')]
merge-recipes dry_run="":
    #!/usr/bin/env bash
    echo "Merging duplicate recipes from normalized_yaml to merge_yaml..."
    echo "Source: {{normalized_yaml_dir}}"
    echo "Target: {{merge_yaml_dir}}/merged"
    echo ""

    if [ "{{dry_run}}" = "true" ]; then
        echo "DRY RUN MODE - no files will be written"
        echo ""
        uv run python -m culturemech.merge.merge_recipes \
            --normalized-dir {{normalized_yaml_dir}} \
            --output-dir {{merge_yaml_dir}}/merged \
            --stats-file {{merge_yaml_dir}}/merge_stats.json \
            --dry-run
    else
        uv run python -m culturemech.merge.merge_recipes \
            --normalized-dir {{normalized_yaml_dir}} \
            --output-dir {{merge_yaml_dir}}/merged \
            --stats-file {{merge_yaml_dir}}/merge_stats.json
    fi

[group('Merge')]
merge-stats:
    #!/usr/bin/env bash
    echo "Generating merge statistics (no files written)..."
    echo ""
    uv run python -m culturemech.merge.merge_recipes \
        --normalized-dir {{normalized_yaml_dir}} \
        --stats-only

# Verify merge_yaml is a current derivation of normalized_yaml (#215). Every
# corpus gate scans normalized_yaml only, on the assumption that merge_yaml is
# always regenerated from it; this tests that assumption by regenerating to a temp
# dir and diffing. Slow (~3 min) and currently DRIFTED, so it is on-demand, not a
# CI gate — see the script docstring.
[group('QC')]
audit-merge-freshness *args="":
    uv run --extra dev python scripts/audit_merge_yaml_freshness.py {{args}}

[group('Merge')]
verify-merges:
    #!/usr/bin/env bash
    echo "Verifying merged recipes..."
    echo ""

    if [ ! -d "{{merge_yaml_dir}}/merged" ]; then
        echo "✗ No merged recipes found at {{merge_yaml_dir}}/merged"
        echo "  Run: just merge-recipes"
        exit 1
    fi

    uv run python scripts/verify_merges.py \
        --normalized-dir {{normalized_yaml_dir}} \
        --merge-dir {{merge_yaml_dir}}/merged \
        --stats-file {{merge_yaml_dir}}/merge_stats.json

[group('Merge')]
count-unique-recipes:
    #!/usr/bin/env bash
    echo "Recipe Count Comparison"
    echo "======================="
    echo ""

    normalized_count=$(find {{normalized_yaml_dir}} -name "*.yaml" -type f | wc -l | xargs)
    echo "Normalized recipes: $normalized_count"

    if [ -d "{{merge_yaml_dir}}/merged" ]; then
        merged_count=$(find {{merge_yaml_dir}}/merged -name "*.yaml" -type f | wc -l | xargs)
        echo "Merged recipes:     $merged_count"
        reduction=$((normalized_count - merged_count))
        echo "Reduction:          $reduction recipes"

        if [ $normalized_count -gt 0 ]; then
            pct=$(awk "BEGIN {printf \"%.1f\", ($reduction / $normalized_count) * 100}")
            echo "Reduction %:        ${pct}%"
        fi
    else
        echo "Merged recipes:     (not yet created)"
        echo ""
        echo "Run: just merge-recipes"
    fi

    echo ""

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
    uv run linkml-term-validator validate-data {{file}} -s {{schema_path}} -t MediaRecipe --labels -c {{oak_config}}
    echo "✓ Term validation passed"

    echo ""
    echo "=== Reference validation ==="
    uv run linkml-reference-validator validate data {{file}} --schema {{schema_path}} --target-class MediaRecipe
    echo "✓ Reference validation passed"

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

# id↔label gate (Engine A): the schema binds the organism/environment/precursor/
# substrate term slots, so --labels verifies their term.label is the CANONICAL
# ontology label for term.id across all recipe files. The chemistry `term`/
# `chebi_term` slots are deliberately NOT bound (they carry curator formula/
# common-name labels; see the schema note and Engine-B's label waiver). Fails
# (non-zero) on any canonical-label drift in the bound slots.
[group('QC')]
validate-terms-all:
    #!/usr/bin/env bash
    set -uo pipefail
    shopt -s globstar nullglob
    rc=0
    # `**/*.yaml` (recursive, matching Engine B) instead of one-level `*/*.yaml`.
    for file in data/normalized_yaml/**/*.yaml; do
        [ -e "$file" ] || continue
        uv run linkml-term-validator validate-data "$file" -s {{schema_path}} -t MediaRecipe --labels -c {{oak_config}} || rc=1
    done
    exit $rc

# id↔label gate (Engine B): runs the shared OAK validator over the full
# conf/id_label_targets.yaml — this gates BOTH the recipe YAML term blocks
# (id-existence; chemistry term/chebi_term labels are waived, organism/
# environment canonical) AND the SSSOM data products (output/*.sssom.tsv,
# canonical-or-synonym). Exits non-zero on any ERROR-class verdict
# (ID_NOT_FOUND / EMPTY_LABEL / MISMATCH / MISSING_COLUMN / MISSING_GLOB).
[group('QC')]
validate-products:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml

# Baseline (non-failing): unified id↔label drift report across recipe YAMLs +
# SSSOM products to reports/label_drift.tsv. Use before enforcing.
[group('QC')]
report-label-drift:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml --report reports/label_drift.tsv

# NOTE: the id↔label validator + its shared tests are vendored byte-identical
# across the Mech repos. The old self-generated sha256 pin (verify-/refresh-
# validator-pin) was retired — it could only compare a copy to a hash from the
# SAME repo, so all four could pass while holding three different versions. Drift
# is now caught by the shared-reference check in the spokes (scripts/
# check_vendored_sync.sh, against CultureBotAI/CultureMech@<.vendored_canon_ref>)
# plus the nightly fleet audit in culturebotai-claw (fleet-audit job).
# See culturebotai-claw vendored_sync_action_plan (Phase 2).

# NOTE: the shared LinkML module (mech_shared.yaml) is vendored byte-identical
# across the Mech repos (package-namespaced path per repo). Its self-generated
# sha256 pin (verify-/refresh-schema-pin) was retired — same self-referential
# flaw as the id-label pin. mech_shared.yaml is now covered by the shared-
# reference drift check (spokes' scripts/check_vendored_sync.sh diffs their
# src/<pkg>/schema/mech_shared.yaml against this hub's copy) and the nightly
# claw's fleet-audit job. Propagation: change it in this hub → sync the
# spokes → bump their .vendored_canon_ref.
#
# The former mim-roles-pin was also retired: mim_roles.yaml is NOT a shared set —
# it is empty in MIM/CommunityMech/TraitMech (the real role facets live in MIM's
# src/mediaingredientmech/utils/role_facets.py) and has content only here, so the
# self-pin guarded a lone, dormant file. Nothing in CI referenced either pin.

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
    set -e
    echo "Running full QC pipeline..."
    just validate-all
    echo ""
    echo "Building SSSOM product + enforcing id↔label correspondence (Engine B)..."
    just generate-sssom
    just validate-products
    echo ""
    echo "✓ QC complete!"

# Strict in-process validation: walks normalized_yaml, runs linkml-validate with
# closed=True (catches unknown fields that `just validate-all` ignores), writes
# a categorized TSV, and exits non-zero if any ERROR rows are emitted.
# Pass arguments through, e.g.:
#     just validate-strict --sample 50
#     just validate-strict data/normalized_yaml/algae
[group('QC')]
validate-strict *args:
    #!/usr/bin/env bash
    uv run python scripts/validate_strict.py {{args}}

# Grounding-consistency QC (G23): flags ingredient names grounded to >1 CHEBI id
# (and CHEBI ids carrying >1 distinct compound) on the RELIABLE grounding layer,
# and reports the low-confidence kg_fallback chebi_term layer separately.
# CI gates at the current baseline so NEW inconsistencies fail without blocking
# on the existing backlog (G24/G25). Re-baseline by bumping --max-allowed.
# Baseline history: G25 Phase 1 promoting kg_fallback chebi_terms to corpus
# consensus surfaced latent salt/hydrate/isomer name->multi-CHEBI ambiguities
# (peaked at 111); the primary-term regrounding pass (483 wrong-id fixes) cut it
# to 109; the ID_NOT_FOUND remediation (re-ground absent ids + de-ground mixtures)
# cleared the last few, tightening the reliable-layer backlog to 101.
# NOTE: reports/chebi_consistency.tsv is NOT tracked (#157). It is regenerated
# from the corpus on every run and nothing reads the committed copy, so tracking it
# only produced silent rot — the gate compares against --max-allowed, never against
# the file. The chebi-consistency workflow uploads a fresh copy as an artifact
# (`if: always()`) if you need it from CI.
[group('QC')]
check-chebi-grounding *args:
    #!/usr/bin/env bash
    uv run python scripts/audit_chebi_consistency.py \
        --out reports/chebi_consistency.tsv --max-allowed 101 {{args}}

# Rebuild data/culturemech_id_registry.tsv from the corpus. A category move
# changes a record's path but not its id, so bulk recategorizations rot the
# registry silently (#144 — it reached 5,511 rows pointing at missing files).
# Never mints, retires or reassigns an id; refuses to run on duplicate ids or on
# records with no `id:` — those are `assign-ids`' job.
#     just refresh-id-registry --dry-run   # report drift only
[group('QC')]
refresh-id-registry *args="":
    uv run --extra dev python scripts/refresh_id_registry.py {{args}}

# Scan-only collision check for CultureMech:NNNNNN IDs. Exits non-zero if any
# cross-file duplicates are detected. Use as a pre-commit / CI safety net.
[group('QC')]
assign-ids-check:
    #!/usr/bin/env bash
    uv run python scripts/assign_culturemech_ids.py --check

# Mint CultureMech:NNNNNN IDs for any YAML records missing one. Refuses to run
# if cross-file collisions exist among existing IDs (run `assign-ids-check`
# first to surface them).
#     just assign-ids --dry-run   # rehearse only
#     just assign-ids             # apply
[group('QC')]
assign-ids *args:
    #!/usr/bin/env bash
    uv run python scripts/assign_culturemech_ids.py {{args}}

# ================================================================
# VALIDATION AND FIXING (Track 3)
# ================================================================

[group('Validation')]
validate-recipes report="summary":
    #!/usr/bin/env bash
    echo "Validating all recipes in normalized_yaml..."
    echo ""
    .venv/bin/python scripts/fix_validation_errors.py \
        --report-only \
        --input-dir {{normalized_yaml_dir}} \
        {{ if report == "detailed" { "--verbose" } else { "" } }}

[group('Validation')]
fix-validation-errors dry_run="" categories="all":
    #!/usr/bin/env bash
    if [ "{{dry_run}}" = "true" ]; then
        echo "DRY RUN MODE - no files will be modified"
        echo ""
        .venv/bin/python scripts/fix_validation_errors.py \
            --dry-run \
            --categories {{categories}} \
            --input-dir {{normalized_yaml_dir}} \
            --verbose
    else
        .venv/bin/python scripts/fix_validation_errors.py \
            --categories {{categories}} \
            --input-dir {{normalized_yaml_dir}} \
            --verbose
    fi

[group('Validation')]
validation-stats:
    #!/usr/bin/env bash
    echo "Generating validation statistics..."
    .venv/bin/python scripts/fix_validation_errors.py \
        --report-only \
        --input-dir {{normalized_yaml_dir}}

# Cross-check every recipe's name against NCBITaxon and report media filed under
# the wrong domain directory (e.g. an archaeon under bacterial/). Report-only;
# pass args="--apply" to move the unambiguous cases. Needs the NCBITaxon sqlite:
#   runoak -i sqlite:obo:ncbitaxon info NCBITaxon:2157
[group('Validation')]
audit-domain-categories *args="":
    #!/usr/bin/env bash
    uv run --extra dev python scripts/audit_domain_categories.py \
        --json data/import_tracking/reports/domain_category_audit.json {{args}}

# ================================================================
# ENRICHMENT (Track 2: KOMODO-DSMZ Resolution)
# ================================================================

[group('Enrichment')]
resolve-komodo-compositions dry_run="":
    #!/usr/bin/env bash
    if [ "{{dry_run}}" = "true" ]; then
        echo "DRY RUN MODE - no files will be modified"
        echo ""
        .venv/bin/python scripts/resolve_komodo_compositions.py \
            --dry-run \
            --normalized-dir {{normalized_yaml_dir}} \
            --verbose
    else
        .venv/bin/python scripts/resolve_komodo_compositions.py \
            --normalized-dir {{normalized_yaml_dir}} \
            --verbose
    fi

[group('Enrichment')]
komodo-resolution-stats:
    #!/usr/bin/env bash
    echo "KOMODO-DSMZ resolution statistics..."
    .venv/bin/python scripts/resolve_komodo_compositions.py \
        --dry-run \
        --normalized-dir {{normalized_yaml_dir}} \
        --report-unresolved

# ================================================================
# ONTOLOGY (SSSOM Mapping & EBI OLS Integration)
# ================================================================

[group('Ontology')]
extract-ingredients:
    #!/usr/bin/env bash
    echo "Extracting unique ingredient list from YAML files..."
    uv run python scripts/extract_unique_ingredients.py \
        --normalized-yaml {{normalized_yaml_dir}} \
        --output {{output_dir}}/ingredients_unique.tsv \
        --verbose

[group('Ontology')]
generate-sssom include_unmapped="":
    #!/usr/bin/env bash
    echo "Generating SSSOM mapping file from normalized_yaml..."

    cmd="uv run python scripts/generate_sssom_mappings.py \
        --normalized-dir {{normalized_yaml_dir}} \
        --output {{output_dir}}/culturemech_chebi_mappings.sssom.tsv \
        --validate"

    if [ "{{include_unmapped}}" = "true" ]; then
        echo "Including unmapped ingredients as future mapping candidates..."
        cmd="$cmd --include-unmapped"
    fi

    eval $cmd

[group('Ontology')]
enrich-sssom-with-ols:
    #!/usr/bin/env bash
    echo "Enriching SSSOM mappings using EBI OLS API..."
    uv run python scripts/enrich_sssom_with_ols.py \
        --input-sssom {{output_dir}}/culturemech_chebi_mappings.sssom.tsv \
        --input-ingredients {{output_dir}}/ingredients_unique.tsv \
        --output {{output_dir}}/culturemech_chebi_mappings_enriched.sssom.tsv \
        --rate-limit 5 \
        --verbose

[group('Ontology')]
enrich-sssom-exact:
    #!/usr/bin/env bash
    echo "Enriching SSSOM with exact matching strategies and OAK..."
    uv run python scripts/enrich_sssom_with_ols.py \
        --input-sssom {{output_dir}}/culturemech_chebi_mappings.sssom.tsv \
        --input-ingredients {{output_dir}}/ingredients_unique.tsv \
        --output {{output_dir}}/culturemech_chebi_mappings_exact.sssom.tsv \
        --use-oak \
        --exact-first \
        --rate-limit 5 \
        --verbose

[group('Ontology')]
extract-unmapped-sssom:
    #!/usr/bin/env bash
    echo "Extracting unmapped ingredients to SSSOM file..."
    uv run python scripts/extract_unmapped_sssom.py \
        --enriched-sssom {{output_dir}}/culturemech_chebi_mappings_exact.sssom.tsv \
        --ingredients {{output_dir}}/ingredients_unique.tsv \
        --output {{output_dir}}/unmapped_ingredients.sssom.tsv \
        --verbose

[group('Ontology')]
sssom-exact-pipeline: extract-ingredients (generate-sssom "true") enrich-sssom-exact extract-unmapped-sssom
    @echo ""
    @echo "✓ Exact matching SSSOM pipeline complete!"
    @echo "  - Ingredients:        {{output_dir}}/ingredients_unique.tsv"
    @echo "  - Base SSSOM:         {{output_dir}}/culturemech_chebi_mappings.sssom.tsv"
    @echo "  - Exact enriched:     {{output_dir}}/culturemech_chebi_mappings_exact.sssom.tsv"
    @echo "  - Unmapped tracking:  {{output_dir}}/unmapped_ingredients.sssom.tsv"

[group('Ontology')]
sssom-pipeline include_unmapped="": extract-ingredients (generate-sssom include_unmapped) enrich-sssom-with-ols
    @echo ""
    @echo "✓ SSSOM pipeline complete!"
    @echo "  - Ingredients extracted: {{output_dir}}/ingredients_unique.tsv"
    @echo "  - Base SSSOM:           {{output_dir}}/culturemech_chebi_mappings.sssom.tsv"
    @echo "  - Enriched SSSOM:       {{output_dir}}/culturemech_chebi_mappings_enriched.sssom.tsv"

[group('Ontology')]
sssom-with-unmapped: (sssom-pipeline "true")
    @echo ""
    @echo "✓ SSSOM pipeline with unmapped ingredients complete!"
    @echo "  Use confidence=0.0 to filter unmapped candidates for curation"

[group('Ontology')]
test-ols-client query="":
    #!/usr/bin/env bash
    if [ "{{query}}" != "" ]; then
        echo "Testing OLS client with query: {{query}}"
        uv run python -m culturemech.ontology.ols_client --search "{{query}}"
    else
        echo "Testing OLS client (verifying water CHEBI:15377)..."
        uv run python -m culturemech.ontology.ols_client --verify "CHEBI:15377"
    fi

[group('Ontology')]
enrich-with-chebi dry_run="" limit="":
    #!/usr/bin/env bash
    echo "Enriching normalized YAML recipes with CHEBI ontology terms..."

    cmd="uv run python scripts/enrich_with_chebi.py \
        --normalized-yaml {{normalized_yaml_dir}} \
        --microbe-media-param {{raw_dir}}/microbe-media-param \
        --mediadive {{raw_dir}}/mediadive"

    if [ "{{dry_run}}" = "true" ]; then
        echo "DRY RUN MODE - no files will be modified"
        cmd="$cmd --dry-run"
    fi

    if [ "{{limit}}" != "" ]; then
        echo "Limiting to {{limit}} files"
        cmd="$cmd --limit {{limit}}"
    fi

    eval $cmd

[group('Ontology')]
check-chebi-ids:
    #!/usr/bin/env bash
    echo "Checking CHEBI IDs in normalized YAML files..."
    uv run python scripts/check_chebi_ids.py

[group('Ontology')]
trace-invalid-chebi-sources:
    #!/usr/bin/env bash
    echo "Tracing invalid CHEBI IDs to source mapping files..."
    uv run python scripts/trace_invalid_chebi_sources.py

[group('Ontology')]
remove-invalid-chebi-ids dry_run="":
    #!/usr/bin/env bash
    if [ "{{dry_run}}" = "true" ]; then
        echo "DRY RUN MODE - showing what would be removed..."
        uv run python scripts/remove_invalid_chebi_ids.py --dry-run --verbose
    else
        echo "⚠️  This will modify normalized YAML files!"
        echo "Removing invalid CHEBI IDs..."
        uv run python scripts/remove_invalid_chebi_ids.py --verbose
    fi

# ================================================================
# QUALITY TAGGING (Track 1: Placeholder Transparency)
# ================================================================

[group('Quality')]
tag-placeholder-recipes dry_run="":
    #!/usr/bin/env bash
    if [ "{{dry_run}}" = "true" ]; then
        echo "DRY RUN MODE - no files will be modified"
        echo ""
        .venv/bin/python scripts/tag_placeholder_recipes.py \
            --dry-run \
            --normalized-dir {{normalized_yaml_dir}} \
            --verbose
    else
        .venv/bin/python scripts/tag_placeholder_recipes.py \
            --normalized-dir {{normalized_yaml_dir}}
    fi

[group('Quality')]
cleanup-recipe-ingredients dry_run="" report="":
    #!/usr/bin/env bash
    if [ "{{dry_run}}" = "true" ]; then
        echo "DRY RUN MODE - no files will be modified"
        echo ""
        .venv/bin/python scripts/cleanup_recipe_ingredients.py \
            --normalized-dir {{normalized_yaml_dir}} \
            --dry-run \
            --verbose
    else
        REPORT_FLAG=""
        if [ -n "{{report}}" ]; then
            REPORT_FLAG="--report {{report}}"
        fi
        .venv/bin/python scripts/cleanup_recipe_ingredients.py \
            --normalized-dir {{normalized_yaml_dir}} \
            $REPORT_FLAG
    fi

# ================================================================
# FULL PIPELINE
# ================================================================

[group('Pipeline')]
fix-all-data-quality dry_run="":
    #!/usr/bin/env bash
    echo "Running full data quality pipeline..."
    echo ""
    echo "Step 1: Track 3 - Fix YAML and schema errors"
    just fix-validation-errors {{dry_run}}
    echo ""
    echo "Step 2: Track 2 - Resolve KOMODO compositions"
    just resolve-komodo-compositions {{dry_run}}
    echo ""
    echo "Step 3: Cleanup recipe ingredients (duplicates, pH buffers)"
    just cleanup-recipe-ingredients {{dry_run}}
    echo ""
    echo "Step 4: Track 1 - Tag placeholder recipes"
    just tag-placeholder-recipes {{dry_run}}
    echo ""
    echo "Step 5: Validation report"
    just validation-stats
    echo ""
    echo "✓ Data quality pipeline complete!"

# ================================================================
# INDEXES
# ================================================================

[group('Indexes')]
generate-indexes dir="data/normalized_yaml":
    #!/usr/bin/env bash
    echo "Generating recipe indexes for {{dir}}..."
    .venv/bin/python scripts/generate_recipe_indexes.py \
        --recipe-dir {{dir}}
    echo "✓ Indexes generated!"

[group('Indexes')]
generate-all-indexes:
    #!/usr/bin/env bash
    echo "Generating indexes for all recipe collections..."
    echo ""
    echo "1. Normalized recipes"
    just generate-indexes data/normalized_yaml
    echo ""
    echo "2. Merged recipes (2026 baseline)"
    just generate-indexes data/merge_yaml/merged
    echo ""
    echo "✓ All indexes generated!"

# ================================================================
# EXPORT
# ================================================================

# Export the recipe corpus as a KGX node/edge TSV pair (#294).
#
# Driven by scripts/export_kgx.py rather than a bare `koza transform` because
# koza's CLI takes a config YAML (not a .py), does no glob expansion, and the
# 15,878-file corpus overflows ARG_MAX. The script also clears the run-scoped
# node-dedup set and fails loudly on an empty or missing output file.
#
# `--extra koza` is required: koza is an optional dependency and is in neither
# the default nor the `dev` environment.
[group('Export')]
kgx-export *args="":
    uv run --extra koza python scripts/export_kgx.py \
      --records-dir {{normalized_yaml_dir}} \
      --output-dir {{output_dir}}/kgx \
      {{args}}

# Canary the export on one category before committing to the full corpus.
# Example: just kgx-export-sample algae
[group('Export')]
kgx-export-sample category="algae":
    #!/usr/bin/env bash
    set -euo pipefail
    tmp="$(mktemp -d)"
    trap 'rm -rf "$tmp"' EXIT
    cp -r "{{normalized_yaml_dir}}/{{category}}" "$tmp/"
    uv run --extra koza python scripts/export_kgx.py \
      --records-dir "$tmp" \
      --output-dir {{output_dir}}/kgx-sample

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

# Generate per-medium HTML pages from the normalized YAML layer.
# Wraps the unified `render_media_pages` renderer (the modern Phase 2
# dismech-pattern pipeline) and points it at the raw `normalized_yaml/`
# dataset (15,827 records, pre-merge per-source view).
#
# Companion to `gen-media-pages` (in `justfile`) which targets
# `data/merge_yaml/merged/` (6,286 canonical merged records →
# `pages/media/`). Both recipes use the same renderer + template; only
# the source dir and output dir differ.
[group('Pages')]
gen-pages:
    #!/usr/bin/env bash
    echo "Generating HTML pages from {{normalized_yaml_dir}}/ → {{pages_dir}}/normalized/"
    uv run python src/culturemech/render_media_pages.py \
        --yaml-dir {{justfile_directory()}}/{{normalized_yaml_dir}} \
        --out-dir {{justfile_directory()}}/{{pages_dir}}/normalized \
        --index-dir {{justfile_directory()}}/{{pages_dir}}/normalized
    echo "✓ HTML pages generated in {{pages_dir}}/normalized/"

# Render a single recipe YAML to HTML for ad-hoc dev. The output goes
# into a tmp `pages/single/` dir so it doesn't disturb the canonical
# `pages/media/` / `pages/normalized/` trees.
[group('Pages')]
gen-page file:
    #!/usr/bin/env bash
    echo "Generating HTML page for {{file}}..."
    uv run python src/culturemech/render_media_pages.py \
        --yaml-dir {{justfile_directory()}}/$(dirname {{file}}) \
        --out-dir {{justfile_directory()}}/{{pages_dir}}/single \
        --index-dir {{justfile_directory()}}/{{pages_dir}}/single \
        --limit 1 --force
    echo "✓ HTML page generated → {{pages_dir}}/single/"

# ================================================================
# TESTING
# ================================================================

[group('Test')]
test:
    #!/usr/bin/env bash
    echo "Running test suite..."
    uv run --extra dev pytest tests/ -v

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

# Regenerate the Python dataclasses from the schema. Run this after any edit to
# culturemech.yaml — tests/test_dataclasses_current.py fails if you forget.
[group('Schema')]
gen-dataclasses:
    #!/usr/bin/env bash
    set -euo pipefail
    echo "Generating Python dataclasses from schema..."
    uv run gen-python {{schema_path}} > src/culturemech/schema/culturemech_dataclasses.py
    echo "✓ Dataclasses regenerated at src/culturemech/schema/culturemech_dataclasses.py"

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

[group('Stats')]
stats-report output_dir="output/stats":
    #!/usr/bin/env bash
    echo "Generating comprehensive statistics report..."
    uv run python scripts/generate_stats.py \
        --normalized-yaml {{normalized_yaml_dir}} \
        --microbe-media-param {{raw_dir}}/microbe-media-param \
        --mediadive {{raw_dir}}/mediadive \
        --output-dir {{output_dir}}
    echo ""
    echo "✓ Statistics report generated!"
    echo "  JSON:     {{output_dir}}/stats.json"
    echo "  Markdown: {{output_dir}}/stats.md"

[group('Stats')]
stats-json output_file="output/stats/stats.json":
    #!/usr/bin/env bash
    echo "Generating statistics JSON..."
    uv run python scripts/generate_stats.py \
        --normalized-yaml {{normalized_yaml_dir}} \
        --microbe-media-param {{raw_dir}}/microbe-media-param \
        --mediadive {{raw_dir}}/mediadive \
        --output-json {{output_file}}
    echo ""
    echo "✓ JSON generated: {{output_file}}"

[group('Stats')]
stats-markdown output_file="output/stats/stats.md":
    #!/usr/bin/env bash
    echo "Generating statistics Markdown..."
    uv run python scripts/generate_stats.py \
        --normalized-yaml {{normalized_yaml_dir}} \
        --microbe-media-param {{raw_dir}}/microbe-media-param \
        --mediadive {{raw_dir}}/mediadive \
        --output-markdown {{output_file}}
    echo ""
    echo "✓ Markdown generated: {{output_file}}"

[group('Stats')]
stats-terminal:
    #!/usr/bin/env bash
    uv run python scripts/generate_stats.py \
        --normalized-yaml {{normalized_yaml_dir}} \
        --microbe-media-param {{raw_dir}}/microbe-media-param \
        --mediadive {{raw_dir}}/mediadive \
        --terminal-only

[group('Stats')]
update-readme-stats:
    #!/usr/bin/env bash
    echo "Generating fresh statistics for README update..."
    echo ""
    just stats-report output/stats
    echo ""
    echo "Statistics generated! To update README.md:"
    echo "  1. Review output/stats/stats.md"
    echo "  2. Copy relevant sections to README.md"
    echo "  3. Update lines 56-61 with current metrics"

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

# ================================================================
# UMAP VISUALIZATION
# ================================================================

# Default path to KG-Microbe embeddings (local copy in data/embeddings/)
kg_microbe_embeddings := "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CommunityMech/CommunityMech/data/embeddings/DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_v3_2026-06-26_12_55_27.tsv.gz"

[group('Visualization')]
gen-media-umap embeddings_path=kg_microbe_embeddings:
    #!/usr/bin/env bash
    echo "Generating UMAP visualization of media embeddings..."
    echo ""
    uv run culturemech umap generate \
        --embeddings-path {{embeddings_path}} \
        --media-dir {{normalized_yaml_dir}} \
        --output app/umap.html \
        --cache-dir .umap_cache
    echo ""
    echo "✓ UMAP visualization generated!"
    echo "  Output: app/umap.html"
    echo ""
    echo "To view locally: just serve-browser"
    echo "Or open: open app/umap.html"

[group('Visualization')]
gen-media-umap-custom embeddings_path n_neighbors="15" min_dist="0.1" min_coverage="0.5":
    #!/usr/bin/env bash
    echo "Generating UMAP with custom parameters..."
    echo "  n_neighbors: {{n_neighbors}}"
    echo "  min_dist: {{min_dist}}"
    echo "  min_coverage: {{min_coverage}}"
    echo ""
    uv run culturemech umap generate \
        --embeddings-path {{embeddings_path}} \
        --media-dir {{normalized_yaml_dir}} \
        --output app/umap.html \
        --cache-dir .umap_cache \
        --n-neighbors {{n_neighbors}} \
        --min-dist {{min_dist}} \
        --min-coverage {{min_coverage}}
    echo ""
    echo "✓ UMAP visualization generated with custom parameters!"

[group('Visualization')]
gen-media-umap-force-reload embeddings_path=kg_microbe_embeddings:
    #!/usr/bin/env bash
    echo "Generating UMAP (forcing cache reload)..."
    echo ""
    uv run culturemech umap generate \
        --embeddings-path {{embeddings_path}} \
        --media-dir {{normalized_yaml_dir}} \
        --output app/umap.html \
        --cache-dir .umap_cache \
        --force-reload
    echo ""
    echo "✓ UMAP visualization regenerated!"

# Generate mapped ingredients file (ingredients with CHEBI/ontology IDs)
[group('Ingredients')]
aggregate-mapped-ingredients output="output/mapped_ingredients.yaml" min_occurrences="1":
    #!/usr/bin/env bash
    echo "Aggregating mapped ingredients from media YAML files..."
    mkdir -p $(dirname {{output}})
    uv run python scripts/aggregate_mapped_ingredients.py \
        --output {{output}} \
        --input-dir {{normalized_yaml_dir}} \
        --min-occurrences {{min_occurrences}} \
        --verbose
    echo "✓ Mapped ingredients saved to {{output}}"

# Generate unmapped ingredients file (ingredients without ontology mappings)
[group('Ingredients')]
aggregate-unmapped-ingredients output="output/unmapped_ingredients.yaml" min_occurrences="1":
    #!/usr/bin/env bash
    echo "Aggregating unmapped ingredients from media YAML files..."
    mkdir -p $(dirname {{output}})
    uv run python scripts/aggregate_unmapped_ingredients.py \
        --output {{output}} \
        --input-dir {{normalized_yaml_dir}} \
        --min-occurrences {{min_occurrences}} \
        --verbose
    echo "✓ Unmapped ingredients saved to {{output}}"

# Generate both mapped and unmapped ingredient files
[group('Ingredients')]
aggregate-all-ingredients: (aggregate-mapped-ingredients) (aggregate-unmapped-ingredients)
    @echo ""
    @echo "✓ Ingredient aggregation complete!"
    @echo "  Mapped:   output/mapped_ingredients.yaml"
    @echo "  Unmapped: output/unmapped_ingredients.yaml"

# =============================================================================
# INGREDIENT UMAP VISUALIZATION
# =============================================================================

# Generate ingredient-level UMAP (each point = one CHEBI ingredient in embedding space)
[group('Visualization')]
gen-ingredient-umap embeddings_path=kg_microbe_embeddings:
    #!/usr/bin/env bash
    echo "Generating ingredient UMAP visualization..."
    echo "  Embeddings: {{embeddings_path}}"
    echo ""
    uv run python scripts/generate_ingredient_umap.py \
        --embeddings-path {{embeddings_path}} \
        --media-dir {{normalized_yaml_dir}} \
        --output app/ingredient_umap.html \
        --cache-dir .umap_cache
    echo ""
    echo "✓ Ingredient UMAP generated: app/ingredient_umap.html"
    echo "  Open: open app/ingredient_umap.html"

# Generate ingredient UMAP dry-run (count ingredients, skip embedding)
[group('Visualization')]
gen-ingredient-umap-dry embeddings_path=kg_microbe_embeddings:
    #!/usr/bin/env bash
    echo "Ingredient UMAP dry-run (counts only)..."
    echo ""
    uv run python scripts/generate_ingredient_umap.py \
        --media-dir {{normalized_yaml_dir}} \
        --embeddings-path {{embeddings_path}} \
        --dry-run

# Generate ingredient UMAP forcing cache reload
[group('Visualization')]
gen-ingredient-umap-force-reload embeddings_path=kg_microbe_embeddings:
    #!/usr/bin/env bash
    echo "Generating ingredient UMAP (forcing cache reload)..."
    echo ""
    uv run python scripts/generate_ingredient_umap.py \
        --embeddings-path {{embeddings_path}} \
        --media-dir {{normalized_yaml_dir}} \
        --output app/ingredient_umap.html \
        --cache-dir .umap_cache \
        --force-reload
    echo ""
    echo "✓ Ingredient UMAP regenerated: app/ingredient_umap.html"
