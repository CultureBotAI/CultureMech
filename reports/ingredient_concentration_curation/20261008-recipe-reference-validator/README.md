# Official Recipe Reference Validation

Local work for [issue #571](https://github.com/CultureBotAI/CultureMech/issues/571).
This advances, but does not complete, the all-record concentration goal.

## Implementation

`src/culturemech/validation/recipe_references.py` adds literal, accession-checked
source handling for JCM recipe HTML and TOGO/MediaDive recipe APIs. It preserves
chemical notation and uses metadata titles plus a separate integrity-checked
raw cache. Other source providers retain upstream behavior.

`scripts/validate_recipe_references.py` reuses LinkML schema traversal, infers
media versus solution records, reports successful and failed checks, and returns
nonzero for failures. The `just` reference recipes and layered strict validation
now invoke it. See `docs/validation-improvements.md` for commands and limitations.

## Evidence

- `validation-offline.json` and `validation-live.json` preserve the pre-edit
  results for seven records: 225 checks, including 206 excerpts and 19 titles.
  The 13 freshly retrieved responses exactly match the pinned raw source hashes.
- Those baseline runs fail two mid-word excerpt endings in M933 and M1390;
  the original bracket, chemical-subscript and API-title extraction failures
  no longer occur. The validator is not relaxed to accept the truncated endings.
- `excerpt-plan.json` and `repair_excerpts.py` define guarded quotation-only
  corrections. The previous quotations are retained in appended curation events.
  No quantities, units, ingredients, stock structures or earlier events change.
- `baseline.json` records passing schema/strict baselines. The two edits are
  applied and their guarded verification and no-op rerun pass. `post-apply.json`
  records passing post-edit schema/strict checks and all seven actual
  `just validate-references` commands: **206/206 excerpts and 19/19 titles pass**.
  Historical failing reports are not rewritten as passes.
- `earlier-cohort.json` checks the previous four records without edits:
  260/260 excerpts match; two of twelve bibliography titles need correction.

## Verification And Remaining Work

The fast tier passed 8,225 tests (16 skipped, 1,943 deselected). The full run
completed with 10,179 passed, 19 skipped and two stale-history test failures.
Those failures were reproduced and fixed by sharing the applied-repair registry
and independently auditing each repair before checking historical claims.
The full run is not relabeled as green: see `tests.json` and
`adversarial-review.md`. The final post-fix focused run passes **225 tests**;
lint, formatting and whitespace checks also pass. This uses the existing partial
locked Python 3.13 environment, not a clean CI installation.

`final-checks.json` proves only the two intended normalized YAML files changed
in this pass, with one canonical report per exact path. The cumulative source
audit passes: 5,134 edited records, 31,168 evidence entries, 5,496 references and
5,338 curation events. This pass adds no concentrations or evidence entries;
it corrects two existing excerpts and appends two events. Source-wide quantity
accounting is unchanged. The seven-record reference success does not establish
corpus-wide publication readiness.

See `adversarial-review.md` for findings and negative controls, and `next-work.md`
for remaining bibliographic and ingredient repairs. Reference occurrence checks
do not prove scientific entailment or complete evidence coverage. The 91-record
queue and global merge/freshness problems remain open. No commit, push, PR,
merge or branch deletion has been performed by this validator work.
