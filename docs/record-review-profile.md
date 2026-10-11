# CultureMech Record Review Profile

Passing verdicts require positive evidence-linked assessments of the reviewed
targets. Terminal finding dispositions require those targets to have actually
been reviewed and assessed, with completion other than failed. Every
supersession must preserve all affected targets from the cited prior finding,
including multi-record findings; a narrower observation cannot silently drop
unassessed members or close their issues. Keep their remaining scope explicit.

The output contract is [Structured Record Reviews](record-reviews.md).
`conf/record_review.yaml` declares the active routes and local rubrics.

## Routes And Evidence

- `review-yaml-record`: one resolved medium or solution; `kind: record`.
- `review-yaml-category`: a coherent formulation/source/category cohort, with
  explicit lump/split/retain/defer decisions; `kind: category`.
- `review-recipes`: focused QA or an explicit batch. Preserve P1-P4 rule IDs,
  linkage counts, ingredient-instance denominators and native coverage scores.
- `review-ingredient-concentrations`: every direct, inline, nested-stock and
  stock-addition claim in scope, including unchanged and unsupported amounts.
- `curate-yaml-record`: its audit-only route saves the same review bundle.
  A report never authorizes edits or a curation-history event.
- `audit-schema-gaps` and `schema-gap-analysis`: repository/bounded-record
  assessments preserving schema / instances / process as `audit_axis`
  dimensions. Keep current error classes, counts, denominators, writer owners,
  sampling and the native impact/effort/dependency backlog. Validator TSVs,
  schema probes and writer heuristics remain diagnostic evidence, not scientific
  approval. Schema/process-only assessments use `scientific_review: false`.
  Assess exact inputs and save with the common commands below; old gap reports
  are historical only. Use the existing closed-schema harness and record-kind
  routing; do not recreate gates or repair scientific inputs during audit.

Use the recipe validation rules, linkage/duplicate guide, concentration evidence
contract, single-record checklist and `CLAUDE.md` listed in the profile.
Retain record kind, accession/version, variant, exact supplied chemical form,
field path, amount/unit, batch/final-volume basis, preparation stage, source
DOI/PURL, exact snippet and locator. Record concentration decisions
(`verified`, `add`, `correct`, `evidence_only`, `not_quantified`,
`unsupported`, `conflict`, `schema_gap`) in assessment dimensions/details,
not new scientific-record fields. Keep conversion arithmetic separate from
quoted source text; unknown density, hydrate, stock strength or final volume
blocks conversion. A formula fingerprint does not prove recipe identity.

Use findings' `rule_id` and `native_severity` for P1-P4, with an explicit
`normalization_reason`: P1 normally blocker, P2 major, P3 minor, P4 informational.
Classify the actual impact; preserve any justified exception. Coverage is a
linkage metric, never a scientific accuracy score. State each metric's definition,
scale and nonzero denominator; do not invent a denominator for an empty set.

## Input And Generated Ownership

`data/normalized_yaml/` owns maintained MediaRecipe/SolutionRecipe content.
A review of `data/merge_yaml/merged/` must label it generated and identify
its normalized source records and owning merge code under `src/culturemech/merge/`
or the actual source-specific transform. Hash those inputs as context with
`inspect --input`. Raw captures, mechanical raw YAML, app data and generated
pages are not curation owners. See `docs/DATA_LAYERS.md`.
Reference the packaged MIM label-index snapshot and its metadata when used.

## Commands And Saving

Run from the repository root in its project environment:

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
just validate-schema <record-path>
just validate-strict <record-path>
just validate-terms <record-path>
just validate-references <record-path>
uv run python scripts/record_review.py validate /tmp/completed-review.yaml
uv run python scripts/record_review.py save --content /tmp/completed-review.yaml
just check-record-reviews
just test-record-reviews
```

Use session-unique temporary filenames. Capture inputs before assessment and
save only the assessed version. The saver emits authoritative YAML and derived
Markdown in `reviews/structured/<timestamp>-<slug>/`; link both in the response.

`uv run python scripts/batch_review_recipes.py --category bacterial --limit 10
--output /tmp/recipe-diagnostics` emits deterministic TSV/Markdown/JSON scan
diagnostics. Its basic schema/enum tests are not the closed-schema gate, and a
missing MIM lookup does not validate external IDs. It does not verify primary
literature or complete all P1-P4 rules. Review its output against exact targets
and save the final assessment with the shared saver above. A diagnostic-only
assessment uses `scientific_review: false`; no provider output is automatically
promoted to completed scientific review. Filtering priorities or sampling must
remain explicit in scope and limitations.

## Retained Gates

CultureMech has no record-level REVIEWED status. Keep native schema, ID,
product, concentration and merge checks: `just assign-ids-check`,
`just validate-products`, `just verify-merges`,
`just audit-merge-freshness`, and `just check-mim-label-index` when relevant.
A new bundle neither promotes scientific status nor appends curation history.
Required unavailable checks produce partial/blocked output with stated limits.
Existing reports remain historical; none are migrated. Shared schema, helper,
contract documentation and contract test are CLAW-owned byte-identical payloads;
the profile, rubrics and skill-specific judgments are maintained here.
