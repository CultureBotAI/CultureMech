---
name: audit-schema-gaps
description: Systematic gap-and-inconsistency audit for the CultureMech LinkML schema, the YAML instance corpus, and the scripts that generate them — produces a re-runnable validation harness, three audit reports, and a prioritized fix backlog. Invoke when you suspect schema drift, when records are silently failing validation, when a new bulk migration has been added, or whenever the user says "audit the schema", "find data quality issues", "what's wrong with the records", "are we silently failing validation", or similar.
version: 1.0.0
tags: [validation, linkml, schema, data-quality, audit, qc]
author: CultureMech Team
created: 2026-05-16
---

# Audit schema gaps (schema · instances · pipeline)

## Why this skill exists

CultureMech's default `just validate-all` target silently lets failures through — it runs `linkml-validate` in open-schema mode and swallows non-zero exit codes from the loop. A single use of this skill on 2026-05-16 surfaced **59,401 ERROR rows across 8,669 of 15,827 records** that nobody knew were broken. After the cleanup that the skill drives, the corpus dropped to **93 errors across 57 records** and CI gates were put in place so the regressions can't recur.

The skill is built around three orthogonal lenses:

1. **Instance-record validation** — every YAML under `data/normalized_yaml/**` is validated with `linkml-validate` in *closed* mode (unknown fields rejected). Errors are categorized into a TSV.
2. **Schema audit** — programmatic probes over `src/culturemech/schema/culturemech.yaml` for identifier policy, untyped `string` slots, divergent term-field naming, inconsistent `required:`, orphan enums, and range references to undefined types.
3. **Pipeline / writer audit** — every Python module that writes a YAML is checked for: appends to `curation_history`?, has `--dry-run`?, validates before writing?, wired into a `just` target?

Output is five reports under `reports/` plus a re-runnable validation harness at `scripts/validate_strict.py`, all version-controlled.

## When to use

Invoke when any of these conditions hold:

| Trigger | Why |
|---|---|
| User asks to "audit the schema / records / pipeline" | Direct ask. |
| User reports records "silently fail" or "validation passes but the data is wrong" | The signature symptom of open-schema validation. |
| A new bulk migration / importer is added | Run after the migration to confirm it didn't introduce drift. |
| Schema changes (`src/culturemech/schema/culturemech.yaml` modified) | Refresh the audits against the new schema. |
| A curator pass surfaces "I see lots of these errors but nobody's tracking them" | Use the harness to quantify. |
| You're picking up a CultureMech repo cold and want to know its actual health | The harness gives a single-number answer (`files with ERROR`). |

**Don't** invoke this skill for:
- Single-file validation — use `just validate FILE` directly (already wired, fast).
- Term/reference grounding only — use `just validate-terms` / `just validate-references` (term + PMID validation; complementary to this skill which covers schema layer).
- Performance regressions in the writers — out of scope.

## Required tooling

All already present in the repo; no new dependencies needed:

- `uv` (Python runner)
- `linkml-validate` CLI **and** `linkml.validator.Validator` Python API (already a dev dep)
- `just` (existing target wrapper)
- Standard `pyyaml`

If `scripts/validate_strict.py` is missing, this skill recreates it from spec (see "Step 1" below).

## Workflow

The skill is a five-step pipeline. Each step produces an artifact; later steps reuse earlier outputs. Re-run independently as needed.

### Step 1 — Strict validation harness

**File:** `scripts/validate_strict.py`  
**Just target:** `just validate-strict` (defined in `project.justfile`)

Critical implementation requirements (these are what `just validate-all` got wrong):

- Use `linkml.validator.Validator` in-process (much faster than subprocess per-file), not the CLI.
- Configure with `JsonschemaValidationPlugin(closed=True)` so unknown fields are flagged. **This is the central correctness requirement.** Without `closed=True`, ~19,400 unexpected_field errors hide.
- Parallel via `ProcessPoolExecutor` with `ncpu - 1` workers; per-worker singleton Validator (init once, validate many).
- Classify each message into a category via narrow regexes:
  - `unexpected_field`, `missing_required`, `enum_mismatch`, `type_mismatch`, `pattern_mismatch`, `format_mismatch`, `range_violation`, and a catch-all `other`.
- **Route records to the right target class**: `MediaRecipe` vs `SolutionRecipe` by inspecting `term.id` prefix. Solution records have prefix `mediadive.solution:` or `MediaIngredientMech:`; everything else is `MediaRecipe`. Mis-routing produces ~4,800 false-positive errors on standalone solutions.
- Output TSV with columns `file`, `category`, `detail`, `path`, `message`. Use `lineterminator="\n"` to avoid CRLF on macOS.
- Exit code 1 if any ERROR rows; 0 if clean. Don't ever exit 0 on errors — that's the bug `just validate-all` has.
- Flags: `--sample N`, `--out PATH`, `--workers N`, `--quiet`, `--fail-on=error|never`.

Smoke-test on `--sample 5` before any full-corpus run.

### Step 2 — Full-corpus validation

```bash
just validate-strict
```

Walks every `data/normalized_yaml/{algae,bacterial,fungal,archaea,specialized}/**/*.yaml`. ~3 min on 9 workers for 15,827 files.

**Outputs:**
- `reports/instance_validation_failures.tsv` — one row per ERROR.
- Console summary by category.

If the previous run was clean and this one isn't, the recent commits did it. `git log -- data/normalized_yaml/ src/culturemech/schema/` is your starting point.

### Step 3 — Schema probes

**File:** `scripts/audit_schema.py`  
Run: `uv run python scripts/audit_schema.py > /tmp/schema_probes.md`

Probes (all programmatic, no LLM):

| Probe | What it finds |
|---|---|
| Classes without `identifier: true` slot | Descriptors with no stable cross-reference handle. |
| Slots with `range: string` whose name suggests enum/term | E.g. `growth_phase`, `salinity`, `light_cycle`, `merge_mode`. |
| Term/ontology slot naming divergence | `term` vs `<provenance>_term` vs `<provenance>_id` vs `ontology_term`. |
| `required: true` inconsistency for analogous attributes | E.g. `concentration` required on `IngredientDescriptor` but not on `SolutionDescriptor`. |
| Orphan enums (declared but never used as `range:`) | Dead schema. |
| `range:` references to undefined classes/types/enums | Broken schema. |
| Enum casing audit | Mixed UPPER/lower/mixed values within a single enum. |

Hand-compose `reports/schema_gap_audit.md` from the probe output. The composition is the value-add — explaining *why* each finding matters and citing instance counts from Step 2.

### Step 4 — Pipeline / writer audit

**File:** `scripts/audit_writers.py`  
Run: `uv run python scripts/audit_writers.py --out reports/pipeline_writers_audit.tsv`

Walks `scripts/`, `src/culturemech/import/`, `src/culturemech/enrich/`, `src/culturemech/merge/`. For each module that writes YAML (heuristic: `yaml.safe_dump` / `yaml.dump` / `.write_text(` with a `.yaml` path hint), records:

- `appends_curation_history` — regex match on `curation_history.*append` or `record_curation_event` or `'curator':`
- `has_dry_run` — regex match on `--dry-run` or `dry_run\s*[:=]`
- `validates_before_write` — regex match on `linkml-validate` or `RecipeValidator` or `validator.validate(`
- `wired_into_just` — filename appears in `project.justfile` / `justfile`

Hand-compose `reports/pipeline_gap_audit.md` from the TSV. Highlight writers missing safeguards, especially those that touch large portions of the corpus.

### Step 5 — Prioritized fix backlog

Compose `reports/gap_fix_backlog.tsv` (machine-readable) + `reports/gap_fix_backlog.md` (narrative). One row per actionable gap:

| column | example |
|---|---|
| id | G01 |
| category | pipeline / schema / instance |
| title | Make `just validate-strict` the default validator and CI gate |
| impact | 59,401 future ERROR rows blocked at PR-time |
| effort | S / M / L |
| suggested_fix_path | `.github/workflows/validate-strict.yaml` |
| blocking | comma-separated upstream G-ids |

Rank by impact × (1/effort). Group narrative by tier so an implementer can pick the easiest big-wins first. Always lead with **G01: enable the CI/pre-commit gate** — without it, every other fix can regress on the next merge.

## Outputs (the deliverable surface)

```
scripts/
  validate_strict.py        # harness (in-process closed-schema validator)
  audit_schema.py           # schema probes
  audit_writers.py          # writer audit
reports/
  instance_validation_failures.tsv   # one row per ERROR (regenerable)
  instance_validation_summary.md     # human report; counts + drivers
  schema_gap_audit.md                # human report on schema findings
  pipeline_writers_audit.tsv         # writer/script audit (regenerable)
  pipeline_gap_audit.md              # human report on pipeline gaps
  gap_fix_backlog.tsv                # backlog rows
  gap_fix_backlog.md                 # narrative, ranked
project.justfile
  validate-strict           # new target wrapping the harness
.github/workflows/
  validate-strict.yaml      # CI gate on PRs touching schema or YAMLs
.pre-commit-config.yaml     # local gate on changed YAMLs
```

## How to follow up an audit with cleanup

The audit *finds* drift; cleanup fixes it. Typical post-audit work, in dependency order:

1. **CI gate first (G01).** Without it, the rest can regress. Add `.github/workflows/validate-strict.yaml` calling `just validate-strict`. Also add `.pre-commit-config.yaml` for the local gate.
2. **Bulk field renames.** Each is a one-file Python script that mirrors `scripts/migrate_legacy_fields.py` (idempotent, appends a `CurationEvent`, supports `--dry-run`). Patterns proven on this corpus:
   - `migrate_legacy_fields.py` — covers `date→timestamp`, `reference_id→reference`, `category` casing, concentration-unit aliases.
   - `migrate_data_quality_flags.py` — type-shape migration (dict→list).
   - `migrate_preparation_steps.py` — semantic migration with keyword-guessed enum + preserved free-text description.
3. **Schema-shape fixes.** If a finding is "schema is too narrow for real data", broaden the schema (e.g. extend `pattern:` to admit additional prefixes) rather than migrate the data — most data IDs come from upstream sources you don't control.
4. **Regenerate dataclasses after schema changes:** `uv run gen-python src/culturemech/schema/culturemech.yaml > src/culturemech/schema/culturemech_dataclasses.py`. Always commit the regenerated file in the same commit as the schema change.
5. **Routing the validator.** If a new root class is added (e.g. `SolutionRecipe`), update `infer_target_class()` in `scripts/validate_strict.py` to route by a stable signal (typically `term.id` prefix).
6. **Revalidate.** Re-run `just validate-strict`, confirm the failing count drops, update `reports/instance_validation_summary.md` with before/after numbers.

## Anti-patterns (don't do these)

- **Don't use the existing `just validate-all` to decide if the corpus is clean.** It runs in open mode and swallows exit codes; it will report success even when 50%+ of records are broken. Use `just validate-strict`.
- **Don't add `# noqa` / try/except blocks around validator results.** If a record fails, the right move is to fix the schema or migrate the data, not silence the failure.
- **Don't pile findings into a single dump.** The five-report split (instance / schema / pipeline / backlog + summary) is so a reader can scan one section at a time.
- **Don't run a full corpus pass when investigating a single regression.** Use `just validate-strict --sample 50` or pass the specific file path.
- **Don't broaden a regex pattern in the schema to "make tests pass" without understanding what the new values mean.** If `FOODON:` is showing up in `IngredientDescriptor.term`, document *why* this is correct (food ontology has things CHEBI doesn't) — bake the explanation into the schema description so future readers don't think it's a bug.
- **Don't forget to commit the regenerated `culturemech_dataclasses.py`** alongside any schema change. Drift between schema and dataclasses produces confusing errors days later.

## Cross-references

- `reports/instance_validation_summary.md` — the most recent run's full numbers and what's left.
- `reports/gap_fix_backlog.md` — the open items (G01-G20 as of the 2026-05-16 run, of which G01-G08, G15, G17 are now closed; G09-G14, G16, G18-G20 remain).
- `reports/schema_gap_audit.md` — schema findings with file:line refs.
- `reports/pipeline_gap_audit.md` — writer audit with safeguard table.
- `scripts/validate_strict.py:infer_target_class` — the routing function; the place to extend when adding new root classes.
- Existing complementary skills:
  - `review-recipes` — per-recipe QA (semantic validation, ingredient linkages, etc.). Different layer.
  - `match-kg-microbe` — term-grounding workflow. Different layer.
  - `manage-identifiers` — ID minting hygiene. Different layer.

## One-liner runbook

```bash
# Generate everything from a clean repo
just validate-strict                                       # Step 2
uv run python scripts/audit_schema.py > /tmp/probes.md     # Step 3 probes
uv run python scripts/audit_writers.py \
    --out reports/pipeline_writers_audit.tsv               # Step 4 probes

# Then hand-compose schema_gap_audit.md, pipeline_gap_audit.md,
# instance_validation_summary.md, gap_fix_backlog.{tsv,md}
# using the TSVs as evidence.
```
