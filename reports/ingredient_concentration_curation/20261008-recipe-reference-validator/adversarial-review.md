# Adversarial Review: Official Recipe References

This is a local adversarial self-review, not an independent GitHub approval.
Issue: https://github.com/CultureBotAI/CultureMech/issues/571.

## Findings Addressed In Code

1. **Scientific notation was not preserved by the upstream matcher.** The
   recipe-specific adapter folds whitespace only, retaining bracketed
   accessions, case, hydrate notation, signs, decimal points and units. It does
   not strip bracketed text as editorial commentary or permit ellipsis matching.
   Literature and unsupported endpoints continue through the upstream plugin.
2. **The unfinished wrapper used a nonexistent `Validator.schema_view`
   attribute.** It now loads a public `SchemaView`, validates the selected class,
   and passes that schema to LinkML. Tests cover class inference, unknown classes,
   malformed YAML, nested stock evidence, variants and separate bibliography
   titles. Reported check counts include successes rather than only issues.
3. **Substring boundaries could falsely accept altered numeric meaning.**
   Direct adversarial probes initially accepted `1 g` within Unicode-minus
   `\u22121 g`, decimal-comma `0,1 g`, and superscript `1 g\u207b\u00b9`.
   Boundary handling and regression tests now reject these, along with ASCII
   signs, decimal truncation, changed units, hydrates and chemical case.
4. **A stale generic Markdown cache could hide source extraction bugs.** The
   adapter uses a separate, versioned raw cache with requested/returned URL,
   timestamp and SHA256 checks. Tests reject bad identity, malformed data,
   corrupt captures, symlinks, redirects, oversized responses and network
   failures. Official-source failures cannot fall back to generic matching or
   prefix-skipping success. Refresh is explicit.

## Data Findings

Frozen-source and fresh HTTP runs both performed 225 checks across seven
unchanged records: 206 excerpts and 19 titles. Both failed only two excerpts,
at `evidence[2].snippet` in M933 and M1390, because the excerpt ended at
`solution` inside the source word `solutions`. All 13 fresh raw captures have
the same hashes as their frozen equivalents. See `validation-offline.json` and
`validation-live.json`; these preserve the failing baseline, not an altered pass.

`excerpt-plan.json` records the narrowly scoped correction, including complete
before/after documents, source identity, raw source hashes, and old/new excerpts.
The guarded repair changes no quantity, unit, ingredient, stock structure,
scientific explanation or earlier curation event. It appends the old and new
quotation to history. Application and final gate status belong in
`post-apply.json`; a plan alone is not evidence that the edits were applied.

## Limits

- A literal occurrence is not proof that a quote supports its associated
  concentration, final volume, ingredient identity or preparation stage.
- This does not certify records without snippets or all records in the corpus.
- Other endpoint formats retain upstream behavior; this is not a replacement
  for all reference providers.
- Earlier bibliographies still contain descriptive labels such as `MediaDive
  medium J151` and `TOGO Medium M142` rather than actual source titles. They are
  not whitelisted as valid titles by this change and need evidence-backed repair.
  The read-only `earlier-cohort.json` check records 260/260 matching excerpts and
  10/12 matching titles across J261, M253, J151 and M142. It changes no data and
  does not count those records as newly reviewed.
- Full-suite results are recorded separately in `tests.json`. The runtime is
  the existing partial locked Python 3.13 environment, not a clean CI install.
- Corpus merge conflicts and freshness remain separate publication gates.

## Full-Suite Follow-Up

The broad run exposed two failures in
`tests/test_medium_concentration_batch.py`, for the historical MediaDive
2000-2500 and 2500-3000 cohorts. They reproduced without the new reference
adapter: their hand-maintained follow-up list ended before later applied JCM
stock and variant repairs, so the expected hashes were stale.

The fix shares the cumulative auditor's `review_plans()` registry and uses
`invert_chain()` to independently audit each applied repair before testing
the original claims at their original scope. It does not whitelist current
hashes or exempt moved ingredients. All ten batch tests pass after the fix,
including two new negative cases that recompute hashes after forging an
ingredient or earlier history. Those forged repairs are still rejected.

The in-flight full-suite process collected the old test module, so its two
failures remain in its historical log. The post-fix targeted run is separate
evidence and is not relabeled as a clean full-suite rerun.
