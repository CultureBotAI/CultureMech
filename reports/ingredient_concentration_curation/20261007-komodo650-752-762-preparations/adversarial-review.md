# Adversarial Preparation Review

## Open Findings

1. **P1: related records still retain incompatible encodings.** The three DSMZ
   counterparts and standalone solutions 1378, 1538 and 1552 retain incorrect
   water units, flattened metal stocks, or flattened carbonate preparation.
   Existing evidence on these records must be preserved and explicitly rescoped
   where a stock-stage interpretation is withdrawn. The full local snapshots and
   original solution captures are in `related-record-handoff.json` and
   `related-source-handoff.json`. These six records were not edited in this batch.
2. **P1: retention does not establish formulation identity or publication safety.**
   All three repaired records retain their exact ingredient/stock/preparation and
   provenance fields in their actual merge groups. However, 752 and 762 are now
   singleton groups, and 650's group also contains an uncorrected DSMZ record and
   `medium_650_modified_for_dsm_8319.yaml`. This pass does not establish that the
   strain-specific record is an exact formulation match. Global merge verification
   still reports 1,247 name conflicts and 3,287 fingerprint issues. Freshness
   comparison reports 6,320 tracked versus 6,496 regenerated records, with 3,720
   only tracked, 3,896 only regenerated, 1,683 changed and 917 unchanged. Nothing
   generated was published or copied into tracked merge YAML.
3. **P2: automated bibliography validation remains failed.** The first CLI run
   could not resolve MediaDive in the sandbox and later stopped during snippet
   checking; its terminal failure is preserved. A network-enabled retry against
   the same public URLs completed. All 29 evidence snippets passed the installed
   matcher, but each full record still has one API URL-as-title fallback mismatch.
   The YAML titles are explicitly descriptive titles derived from the response's
   medium name; they were not replaced with URLs merely to pass a validator.
   The actual KOMODO HTML title produces no mismatch for these three records.
   This does not repair the earlier cohorts' separate mapping-title discrepancy.

## Resolved In This Batch

- Pyruvate is represented in its directly stated 20 mM unit and explicitly added
  after autoclaving. No molecular-weight or unspecified stock-dose conversion.
- The 752 metal rows denote 1 ml stock additions, not 1 g/L metal concentrations.
  Their stated stock strengths remain separate from the doses. The agar branch
  is not inserted into the liquid recipe.
- The 762 carbonate masses remain source batch inputs in a separate preparation.
  Neither 100 ml water nor a sum of water inputs is treated as final volume.
- New water nodes use the source's compound accession, not a guessed chemical
  mapping. Existing chemical identifiers, prior history and unrelated fields
  survive a complete-record inversion.
- Guard tests reject concurrent edits, untracked/case-drifted/symlink paths,
  changed source bytes, altered plans, incorrect doses/strengths, altered quotes,
  history/identity loss, and contamination from the agar preparation branch.

Baseline tests: 77 passed. Post-edit focused tests: 275 passed. Baseline and
post-edit strict schema checks scanned all 15,910 records with zero errors.
Source readback, no-op rerun, prior-cohort hash successors, IDs, cumulative diff,
and exact-path coverage checks passed. Product validation passed with 91
non-blocking warnings and 96,047 no-adapter skips; this is not proof of all
chemical identities. The final fast suite passed 7,514 tests, with 16 skipped
and 1,839 deselected. Final source readback and complete-record inversion pass
for all three records (`final-checks.json`, `final-readback.json`). These checks
used the partial locked Python 3.13 runtime; no full-CI pass is claimed.

This was a local adversarial review, not an external PR review or a claim that
GitHub issues were opened. The all-record goal remains unfinished.
