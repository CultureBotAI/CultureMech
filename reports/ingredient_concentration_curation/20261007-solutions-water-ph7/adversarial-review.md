# Adversarial Review

## Findings Addressed Before Apply

- A pH-only instruction alone does not establish water's volume basis.
  Each complete source was inspected; the correction uses the explicit water
  row as a batch input, never the dataset's nominal solution volume as a
  measured final volume. Quantities of pH-adjustment reagents are not invented.
- A permissive preparation-pattern rule could authorize unseen formulations.
  This mutator accepts only the hash-pinned 52-record inspected context, exact
  membership, stable IDs, matching names/inventories, source bytes and metadata.
  The original general review guard remains unchanged and has a regression test.
- Generic already-applied handling could overlook modified plan claims.
  The wrapper recomputes and validates every proposal, including source and
  baseline/result text, before delegating either apply or verification.
- Existing evidence or notes could be silently overwritten. They block this
  water-only mutator. Complete independent inversion checks preservation of
  every unrelated field and earlier provenance entry.
- Repeated reports could inflate coverage. Supplements do not introduce new
  canonical `- Record:` markers; the 18 excluded candidates are explicit triage.
- The initial generated report named a nonexistent validation journal.
  The report generator now points to the actual baseline/post journal names.

## Remaining Limits

- Brand-qualified nutrient rows, glycerol units, the unspecified iron amount
  in solution 497, and existing chemical-form mappings are not repaired here.
  Source water evidence does not validate those unchanged claims.
- The 18 candidates with stock or local-preparation differences need their own
  evidence review; they remain byte-identical.
- This is a local self-review and targeted adversarial regression suite, not an
  independent human approval or GitHub PR review. No issue/PR was opened by this
  follow-up, and no branch was merged or deleted.
- Dataset records may share source formulations. Fifty-two evidence entries
  are not fifty-two independent experimental confirmations.
