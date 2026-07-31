---
name: deep-research-medium
description: Run Edison Scientific deep research for a CultureMech medium record, then for each candidate organism returned by phase 1 run a per-organism follow-up that extracts the recipe, culture conditions, identifiers, and citation metadata from the primary publication. Produces a curation-focused report with proposed YAML changes.
category: research
requires_database: false
requires_internet: true
version: 1.0.0
---

# Deep Research for a Medium (Edison API)

## Overview

**Purpose**: For one CultureMech medium record, run a two-phase Edison
Scientific deep-research workflow:

1. **Phase 1 — medium-level literature search.** Submit the medium's
   YAML context to the Edison `LITERATURE` (PaperQA3) job and ask the
   API to find candidate organisms reported to grow on this medium or
   a recognizable formulation variant.
2. **Phase 2 — per-organism follow-up.** For each candidate organism
   returned in phase 1, submit a focused follow-up that asks the API
   to extract the recipe (ingredients + concentrations), culture
   conditions, growth metrics, organism identifiers, and citation
   metadata from the primary publication(s).

The output is a single curation-focused Markdown report with proposed
YAML changes ready for a curator to review and apply via
`scripts/apply_edison_results.py`.

**When NOT to use**: skip this skill if you only need to enrich a
single field (use phase-1 alone via `just research-media-edison`).
Skip if a research output already exists for the target medium and is
recent — re-running spends API credits.

## Prerequisites

- `EDISON_PLATFORM_API_KEY` (or legacy `EDISON_API_KEY`) set in repo
  root `.env` or environment.
- `edison-client` SDK installed (already in `pyproject.toml`
  dev-extras).
- Phase-1 template: `templates/media_growth_research.md`
- Phase-2 template: `templates/medium_organism_recipe_extraction.md`
- Recipe-validation template: `templates/media_recipe_validation.md`

## Recipe-validation mode (single phase, no organism discovery)

Separate from the two-phase organism flow above. Use this to **audit the
formulation** of one medium and **each of its modeled variants** against
authoritative sources, returning curator-ready corrections rather than new
organisms.

### Native Claude Code path (default — no Edison credits)

Run the validation with this harness's own web tools (or the `deep-research`
skill) instead of the Edison API. Render the filled prompt, then research
it yourself:

```bash
# print the validation prompt for one medium + its variant set:
just validate-media-recipe <SLUG-OR-PATH>
# or with a different template / write to a file:
just validate-media-recipe <SLUG-OR-PATH> --template <tpl> --out prompt.md
```

`render_media_prompt.py` is render-only — it makes **no** external calls and
does not need the `edison-client` SDK. Take the rendered Markdown as your
research brief: do the web searches / source fetches, verify each claim
against a cited source line, and write the report to
`research/media/<slug>-recipe-validation.md` in the output format the
template specifies (verdict table → findings → proposed YAML → gaps).

### Edison API path (spends credits)

Reuses the phase-1 wrapper with the validation template — swap `--template`:

```bash
just validate-media-recipe-edison <SLUG-OR-PATH>            # via just, or:
uv run --extra dev python scripts/research_media_edison.py \
    --target <SLUG-OR-PATH> \
    --job literature \
    --template templates/media_recipe_validation.md \
    --out-dir research/media
# audit the rendered query first without spending credits:
... --dry-run
```

The template validates the base recipe (ingredient identity, amounts/units
with unit normalization + hydrate handling, pH/conditions, solutions) and
then validates **each variant set separately**:

- inline `variants[]` — via the `{variants}` template var, and
- cross-record variants (`parent_media` / `variant_children` / this
  record's `variant_relationship` + `variant_modifications`) — via the
  `{variant_records}` template var added to `scripts/research_media.py`'s
  `template_vars` (`summarize_variant_records`).

When `{variant_records}` names a linked parent/child YAML by path, run the
validation against that record too — each linked record is its own
validation unit, and the relationship is checked in both directions.

Output is a single Markdown report: a verdict table (one row per
validation unit, `CONFIRMED | DISCREPANCY | UNVERIFIABLE`), findings with
P1/P2/P3 severity and a cited source line, proposed YAML fragments, and
unresolved gaps. Hand off to `review-recipes` before applying any change.

## Inputs

The skill expects either:
- A medium **slug** (YAML file stem, e.g.
  `dehalospirillum_medium`),
- A **CultureMech ID** (e.g. `CultureMech:009034`),
- A **YAML path** under `data/normalized_yaml/`, or
- A medium **name** / **original name** as it appears in the YAML.

Optional:
- `--job` for phase 1 (default `literature`; alternatives:
  `literature-high`, `precedent`, `phoenix`).
- `--organism-job` for phase 2 (default `literature`).
- `--limit-organisms` to cap how many phase-2 follow-ups run (default:
  all organisms found, capped at 10 for first-pass safety).
- `--dry-run` to render queries + write meta yaml without burning
  credits.

## Workflow

### Step 1 — Resolve the medium

Resolve the user's input to a single YAML file under
`data/normalized_yaml/`. Reuse the existing resolver:

```bash
uv run --extra dev python -c "
import sys; sys.path.insert(0, 'scripts')
import research_media as rm
print(rm.resolve_media_file('<TARGET>'))
"
```

If the input is ambiguous (multiple matches, e.g. when several
importer-flavor variants share a slug), surface the candidate paths to
the user and ask which one to research.

### Step 2 — Check for existing research output

Before submitting, look for prior outputs in `research/media/`:

```bash
ls research/media/<slug>-edison-*.md 2>/dev/null
ls research/media/<slug>-organism-*-edison-*.md 2>/dev/null
```

If recent outputs exist (`meta.yaml` shows a real `task_id` and
`submitted_at`), tell the user and ask whether to re-run or use the
existing results. **Do not silently re-spend credits.**

### Step 3 — Phase 1: medium-level literature search

Run the existing single-record Edison wrapper:

```bash
just research-media-edison <SLUG-OR-PATH>
# or with overrides:
uv run --extra dev python scripts/research_media_edison.py \
    --target <SLUG-OR-PATH> \
    --job literature \
    --template templates/media_growth_research.md \
    --out-dir research/media
```

Outputs (per task; `<stem>` is `<slug>-edison-literature`):
- `<stem>.md` — primary Markdown answer
  (`formatted_answer` preferred over `answer`).
- `<stem>-meta.yaml` — task_id, cost, status, `query_sha256`,
  full rendered query, template_vars, char counts, sidecar
  inventory.
- `<stem>-response.json` — full
  `response.model_dump(mode="json")` plus the verbose-fetch dump.
  Every SDK-exposed field, future-proof against new ones.
- `<stem>-citations.md` — parsed reference list from the answer
  (numbered entries with PMID / DOI / URL extracted).
- `<stem>-agent-state.json` — PaperQA's `agent_state` (tool-call
  trace), `environment_frame`, and verbose `metadata`. Only
  written when the verbose fetch returns any of those.
- `<stem>-files.json` — `client.list_files(trajectory_id)` —
  inventory of any artifacts Edison produced during the run.

In `--dry-run` mode, only the meta yaml is written and no API call is
made. The meta still carries `query_sha256` so dry-run prompts can
be diffed against prior runs.

**Retroactive enrichment**: if a meta yaml has a `task_id` but is
missing sidecars (e.g. captured by an older script version), run
`just enrich-edison-response` to pull verbose + files + parse
citations without re-billing the underlying job.

### Step 4 — Parse phase-1 candidate organisms

Read the phase-1 Markdown and pull out each candidate organism row.
The phase-1 template asks the API for a table with columns:
`organism, strain, identifiers, genome/BioSample IDs, source medium
name, growth evidence, culture conditions, citation, confidence`.

For each row, capture:
- `organism_name` (required)
- `strain` (if listed)
- `identifiers` — NCBITaxon, GTDB, GCF_/GCA_/SAMN, DSM/ATCC/JCM, etc.
  Concatenate everything the row mentions; the phase-2 template just
  treats this as a hint string.
- `citation_hint` — the first PMID/DOI/URL in the row's citation cell.
- `phase1_snippet` — the row's growth-evidence cell, used as anchor
  text so the phase-2 PaperQA hits the correct paper.
- `confidence` — used for ordering and to flag low-confidence rows.

Filter:
- **Drop** rows the phase-1 report itself marks as uncertain/unsupported
  unless the user opts in.
- **De-duplicate** by `(organism_name, strain)`.
- **Cap** at `--limit-organisms` (default 10) and prefer high-confidence
  rows. Tell the user how many candidates were dropped.

Write the filtered list to
`research/media/<slug>-organisms.json` — this is the batch input for
phase 2 (one entry per organism: `{target, organism, strain,
identifiers, citation_hint, phase1_snippet}`).

### Step 5 — Phase 2: per-organism recipe extraction

Run the new batch wrapper, with `--dry-run` first so the user can
review the planned queries and credit footprint before spending:

```bash
just research-organism-recipe-edison-batch \
    research/media/<slug>-organisms.json --dry-run
```

Once the user confirms (or if `--dry-run` was not requested), run for
real:

```bash
just research-organism-recipe-edison-batch \
    research/media/<slug>-organisms.json --limit 10
```

For a single one-off organism (e.g. the user already knows which
organism to drill into), the single-target form is fine:

```bash
just research-organism-recipe-edison \
    <SLUG-OR-PATH> "Dehalospirillum multivorans" \
    --strain "DSM 12446" --citation-hint PMID:8482969
```

Each per-organism task writes:
- `research/media/<slug>-organism-<organism-slug>-edison-literature.md`
- `research/media/<slug>-organism-<organism-slug>-edison-literature-meta.yaml`

Total cost = sum of all per-organism meta `total_cost` values plus
the phase-1 cost. Surface this to the user at the end.

### Step 6 — Aggregate findings into a curation report

After both phases finish, write a single roll-up at
`research/media/<slug>-deep-research-summary.md` that combines:

1. **Phase-1 verdict.** Strongest organism-medium relationships,
   recipe-identity verdict (parent vs variant vs new record).
2. **Per-organism table** with columns:
   - Organism, strain, NCBI/GTDB/assembly IDs (from phase 2)
   - Primary citation (PMID/DOI)
   - Recipe diff vs parent (none / variant / new record)
   - Proposed action (add `target_organisms` entry, add `MediaVariant`,
     propose new record, evidence only)
   - Confidence
   - Per-organism research file path
3. **Proposed YAML changes**, one fenced ```yaml``` block per change,
   each ready to merge into `<record_path>` (or a new path). Pull the
   actual YAML fragments from the phase-2 outputs' "Proposed YAML
   changes" section.
4. **Identifier resolution status** — which IDs were verified, which
   were asserted only.
5. **Unresolved gaps & warnings** — claims to NOT curate, paywalled
   sources, ID conflicts, conflicting recipes across papers.
6. **Cost ledger** — phase-1 cost, per-organism costs, total.

The summary is the curator's hand-off artifact; the individual
phase-1 / phase-2 markdown + meta files remain the audit trail.

### Step 7 — Hand off

Tell the user:
- Where the summary report is (`research/media/<slug>-deep-research-summary.md`)
- How many organisms were researched and the total cost
- That `scripts/apply_edison_results.py --dry-run --results <json>`
  can apply structured changes once the proposed YAML is converted
  into the JSON format that script expects
- That the per-organism markdown files are the source of truth for
  citations and snippets if anything in the summary is unclear

Do NOT mutate `data/normalized_yaml/` files in this skill — that's
the curator's call after reading the summary.

## File outputs at a glance

Every Edison task (phase 1 or phase 2) writes the same 5-file
bundle. The provenance sidecars are not optional — they let you
re-derive everything from a single git-checked-in directory
without re-querying the API.

```
research/media/
├── <slug>-edison-literature.md                  # phase 1 answer
├── <slug>-edison-literature-meta.yaml           # phase 1 audit
├── <slug>-edison-literature-response.json       # full SDK response
├── <slug>-edison-literature-citations.md        # parsed refs
├── <slug>-edison-literature-agent-state.json    # tool-call trace
├── <slug>-edison-literature-files.json          # artifact inventory
├── <slug>-organisms.json                        # phase 2 batch input
├── <slug>-organism-<org1>-edison-literature.md  # phase 2, organism 1
├── <slug>-organism-<org1>-edison-literature-meta.yaml
├── <slug>-organism-<org1>-edison-literature-response.json
├── <slug>-organism-<org1>-edison-literature-citations.md
├── <slug>-organism-<org1>-edison-literature-agent-state.json
├── <slug>-organism-<org1>-edison-literature-files.json
├── ... (one bundle per organism)
└── <slug>-deep-research-summary.md              # roll-up for curator
```

## Cost & safety

- Phase 1 with `LITERATURE` typically costs a few cents per medium;
  `LITERATURE_HIGH` is several times more expensive.
- Phase 2 multiplies cost by the number of organisms researched.
  **Always default to `--limit-organisms 10` (or less) on first
  pass.** Re-run on a wider set only after the user reviews quality.
- Run with `--dry-run` first for new media so the user can audit the
  rendered queries (saved to the meta yaml) before spending credits.
- The phase-1 batch flow (`research-media-edison-batch`) is separate
  from this skill — this skill is for going *deep* on one medium, not
  *wide* across many.

## Heuristics for parsing phase-1 outputs

The phase-1 template asks for a Markdown table, but PaperQA may also
emit bullet lists when the answer space is narrow. Be flexible:

- **Tables**: parse columns by header text (`organism`, `strain`,
  `identifiers`, `citation`, `confidence`); column order varies.
- **Bullet lists**: each bullet is one organism; pull strain /
  identifiers / citation from inline text.
- **Mixed or prose**: fall back to extracting capitalized binomials
  followed by a strain designation; flag low-confidence and surface
  to the user before running phase 2.

If parsing returns zero organisms but the phase-1 report has prose
content, **stop and ask the user** what to do — don't silently skip
phase 2.

## Error handling

- **`edison-client` not installed**: tell the user to run
  `uv sync --extra dev`.
- **Missing API key**: tell the user to add
  `EDISON_PLATFORM_API_KEY=...` to repo-root `.env`.
- **Ambiguous target** (multiple YAML files match): list candidates
  and ask the user to pick.
- **Phase-1 API failure**: surface the error; do not auto-retry
  (avoids accidental double-billing).
- **Phase-2 per-organism failure**: log and continue with remaining
  organisms; record the failure in the summary's warnings section.
- **No organisms found in phase 1**: skip phase 2 entirely, write a
  summary explaining the negative result, and recommend either a
  different job (`literature-high`, `precedent`) or manual curator
  review.

## Related skills

- `create-recipe` — once a phase-2 result proposes a brand-new media
  record, hand off to this skill to mint the CultureMech ID and write
  the YAML.
- `review-recipes` — validate proposed YAML changes before applying.
- `match-kg-microbe` — after curation, link the medium to KG-Microbe
  if formulation matches.
- `manage-identifiers` — minting IDs for new variants or new records.

## Related scripts

- `scripts/research_media_edison.py` — phase-1 medium-level search.
- `scripts/research_organism_recipe_edison.py` — phase-2 per-organism
  follow-up (ships with this skill).
- `scripts/_edison_capture.py` — shared response-capture helpers
  (md + meta + response.json + citations.md + agent-state.json +
  files.json). Used by both phase-1 and phase-2 scripts.
- `scripts/enrich_edison_response.py` — retroactively fetch verbose
  response + files for any meta with a `task_id` but missing
  sidecars. No re-billing.
- `scripts/apply_edison_results.py` — apply structured Edison results
  to YAML records.

## Quick reference

```bash
# Phase 1 only (no per-organism follow-up):
just research-media-edison <slug>

# Phase 2 only, one organism:
just research-organism-recipe-edison <slug> "<Organism name>" \
    --strain "<strain>" --citation-hint <PMID|DOI>

# Phase 2 batch (after writing organisms.json):
just research-organism-recipe-edison-batch \
    research/media/<slug>-organisms.json --limit 10

# Dry-run anything to audit the rendered query without spending credits:
... --dry-run
```
