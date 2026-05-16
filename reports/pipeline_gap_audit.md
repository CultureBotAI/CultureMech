# Pipeline / generation-process gap audit

Probe: `scripts/audit_writers.py` (re-runnable, output at `reports/pipeline_writers_audit.tsv`).

The audit looks for every Python module under `scripts/`, `src/culturemech/import/`, `src/culturemech/enrich/`, and `src/culturemech/merge/` that writes a YAML, then checks four attributes:

1. Does it append to `curation_history` (audit trail)?
2. Does it offer a `--dry-run` flag (safe rehearsal)?
3. Does it call `linkml-validate` / `RecipeValidator` *before* writing (write-time gate)?
4. Is it referenced anywhere in `justfile` / `project.justfile` (i.e. discoverable / orchestrated)?

## Headline numbers

65 YAML-writing scripts identified.

| Property | Yes | No |
|---|---:|---:|
| Appends to `curation_history` | **34** | **31** |
| Has `--dry-run` flag | 33 | 32 |
| **Validates before writing** | **3** | **62** |
| Wired into a `just` target | 29 | 36 |

The standout finding: **62 of 65 writers do not validate the YAML they're about to write**. The three that do are `scripts/fix_validation_errors.py` (uses `RecipeValidator` because validation *is* its purpose), `scripts/validate_hierarchy_integration.py` (also a validator, not an enricher), and the audit script itself (false positive — it imports nothing). In effect, **zero enrichment / import / merge writers gate on validation**. Bad records can land in `data/normalized_yaml/` and persist; the only safety net is post-hoc runs of `just validate-all`.

This is the root cause of the 8,669 invalid records in the corpus today. The migrations that produced `date`/`instruction`/`reference_id` (8,688 + 846 + 497 records) all ran without write-time validation; if they had, every script run would have aborted on the first record where the new schema was violated.

## CI / pre-commit gate state

- `.pre-commit-config.yaml` — **does not exist**. No commit-time validation.
- `.github/workflows/`:
  - `generate-pages.yaml` — renders per-medium HTML to GitHub Pages. Runs only on push to specific paths. **No validation step.**
  - `weekly-compliance.yaml` — Sunday 04:13 UTC cron, builds a QC dashboard via `kg_microbe_qc`. Does not block merges. Runs after-the-fact.

Validation never runs as a gate.

## 31 writers that do not append to `curation_history`

Scripts that mutate YAMLs without recording a curation event break the audit trail. Many of these are diagnostic / cleanup utilities, but several are clearly content-producing:

| Script | Purpose (inferred) | Why it matters |
|---|---|---|
| `scripts/apply_media_variant_links.py` | Adds `variant_children` to YAMLs in bulk | This is the script that produced the variant_children annotations on 2010 YAMLs (PR #6). No audit trail. |
| `scripts/cleanup_recipe_ingredients.py` | Dedupes pH buffers in ingredient lists | Modifies ingredients without recording why. |
| `scripts/enrich_genome_ids.py` | Adds genome assembly IDs to OrganismDescriptors | Enrichment without provenance. |
| `scripts/enrich_solutions_with_chebi.py` | Adds CHEBI grounding to solutions | Enrichment without provenance. |
| `scripts/fix_schema_inconsistencies.py` | Mass schema-shape fixes | The most dangerous: silently mutates schema-affecting fields. |
| `scripts/migrate_growth_metrics_v2.py` | Migrates growth_metrics to v2 shape | Schema migration without provenance. |
| `src/culturemech/enrich/fix_unnamed_and_physical_state.py` | Fills missing physical_state | Operates at scale. |
| `src/culturemech/enrich/normalize_enums.py` | Normalizes enum casing | Touches every record's enum fields. |
| `src/culturemech/merge/merge_recipes.py` | Merges duplicate recipes | Merge events absolutely need provenance. |

Full list under `reports/pipeline_writers_audit.tsv` (column `appends_curation_history == "no"`).

## 32 writers that lack a `--dry-run` flag

Mass-mutation scripts without dry-run are rehearsal-hostile — you can't preview the change before committing. Worst offenders are the bulk importers, which often replay against the entire corpus:

- `src/culturemech/import/{atcc,bacdive,ccap,komodo,mediadb,mediadive,nbrc,sag,togo,utex}_importer.py` (10 importers) — none has `--dry-run` according to the regex. (Some may use `dry_run=False` keyword args in classes; the audit only catches CLI flags.)
- `scripts/apply_growth_evidence.py`, `scripts/apply_media_variant_links.py` — both run mutations across thousands of records.
- `scripts/cleanup_media_quality.py`, `scripts/migrate_growth_metrics_v2.py`, `scripts/resolve_unit_conflicts.py` — schema-touching utilities.

## 36 writers not wired into a `just` target

These exist but aren't part of the documented pipeline. Subset where this matters most:

- `scripts/assign_culturemech_ids.py` — mints `CultureMech:NNNNNN` IDs. **Not wired into any orchestration target.** Anyone running it manually is on the honor system not to introduce ID collisions.
- `scripts/fix_schema_inconsistencies.py` — schema-touching utility, not wired.
- `scripts/migrate_growth_metrics_v2.py` — schema migration, not wired.
- `scripts/cleanup_media_quality.py`, `scripts/cleanup_recipe_ingredients.py` — bulk cleanup, not wired.
- `src/culturemech/import/*_importer.py` — most of the importers are invoked by `just fetch-*` and `just import-*` targets, but several of the cleanup/normalize modules under `src/culturemech/enrich/` are not exposed as just targets.

(The audit's "wired_into_just" check is heuristic — a `just` target that calls the script via a helper module may go undetected. Cross-check before deleting any "orphan".)

## What the validation TSV says about pipeline drift

The instance-level errors trace back to specific writer behaviors:

| Validation drift | Most likely producing writer(s) | Why it persists |
|---|---|---|
| `curation_history.date` → `timestamp` (8,688 records) | Old importers / migrations that ran before the schema rename. None re-ran with validation. | Future importers don't validate post-write either. |
| `preparation_steps.instruction` → `action`+`description` (846 records) | Pre-`PreparationStep`-rename importers (likely MediaDive). | Same as above. |
| `references.reference_id` → `reference` (497 records) | Pre-rename importers. | Same. |
| `category` casing (610 uppercase records) | Importers likely write category as the source name (uppercase) without normalizing. | `src/culturemech/enrich/normalize_enums.py` exists, but isn't a gate. |
| 1,872 `FOODON:`/`UBERON:` in `term.id` | Ingredient-mapping pipeline accepts upstream ontology choices when no CHEBI is found. | Schema's narrow CHEBI pattern is too strict; pipeline is right, schema is wrong. |
| 273 dict-shaped `data_quality_flags` | Diagnostic enrichment scripts emit dicts because they want structure. | Schema has the wrong type; pipeline is right, schema is wrong. |

## Specific recommendations

The pipeline-side fixes that move the needle most:

1. **Add `validate-strict` as a default CI gate.** A new `.github/workflows/validate-strict.yaml` running `just validate-strict` on PRs would have caught every schema migration regression before merge. Roughly:
   ```yaml
   on: { pull_request: { paths: ['data/normalized_yaml/**', 'src/culturemech/schema/**'] } }
   jobs:
     validate:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - uses: astral-sh/setup-uv@v3
         - run: just validate-strict
   ```
2. **Pre-commit hook** that runs `just validate-strict` on changed YAMLs only (much faster than a full corpus pass).
3. **Add a write-time validator helper** (`src/culturemech/validation/write_validated.py`) that wraps `yaml.safe_dump` with an in-process `Validator(closed=True)` check; refactor the top-volume writers (`apply_growth_evidence.py`, `enrich_with_chebi.py`, the 10 importers, `merge_recipes.py`) to use it.
4. **Standardize curation_history append** across all mutating scripts — likely a single `record_curation_event(recipe, curator, action, notes)` helper that every writer must call.
5. **Wire orphan scripts into `just` targets** so the supported pipeline is discoverable (or remove unused ones).

## Re-run

```bash
uv run python scripts/audit_writers.py --out reports/pipeline_writers_audit.tsv
```
