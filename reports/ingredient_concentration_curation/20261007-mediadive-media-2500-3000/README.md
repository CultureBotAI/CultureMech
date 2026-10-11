# Sixth Receiving-Medium Source Pass

This is an applied local batch, not completion of the all-record objective.
Baseline commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.
The frozen inventory slice `[2500:3000]` contains 500 JCM records.
Only authoritative normalized YAML was changed; no generated merges were copied.

## Outcome

- 500 exact-path reports with one record marker and all scoped claim rows.
- 50 edited records, 450 unchanged; zero failed or schema-blocked proposals.
- 223 new evidence entries, 50 bibliography entries, 50 append-only events.
- No numerical, unit, chemical-identity, stock, variant, or growth-claim changes.
- 135 preliminary claims withheld across 18 whole records after source review.
- Remaining report rows: 8,320 conflict and 9,592 unsupported. These include
  source inventory/preparation rows and are not independent concentration counts.

[preflight.json](preflight.json) independently verifies provenance-only changes,
unchanged unsupported quantities, and downgrade-only manual decisions.
[plan.json](plan.json) freezes the record/source hashes and all proposals,
including the [source-pinned withholdings](withholdings.json). Guarded apply
rebuilt the claims before writing. Readback verified all 500 record hashes and
223 persisted snippets. Reapplication changed zero records.

## Source Scope

All 68 preliminary candidates' complete main ingredient tables, preparation
steps, and proposed amounts were inspected. [Preparation findings](preparation-findings.md)
record omitted stocks, fractional-volume rounding, extraction boundaries, and
variants. Selected original JCM pages were also inspected, not all 500 original
recipes. Eighty-one API responses have no recipe table and remain unresolved.

Each added YAML entry cites its exact official MediaDive endpoint, literal row
excerpt, locator, arithmetic/basis explanation, retrieval date, and response
hash. JCM is identified as original collection and DSMZ as dataset provider.
Unknown authors and publication years are not manufactured. These entries
support provider-declared main-recipe rates, not independently measured final
volumes, downstream assay dilutions, or chemical ontology mappings.

The [J896 original-source repair handoff](jcm896-repair-handoff.md) documents its
584 ml final volume versus the API's 40 ml denominator. Its ten mass amounts,
serum unit, product name, and corrupted filtration text still require an
explicit successor correction. This batch leaves them unchanged and unsupported.

## Verification

[validation.json](validation.json) records actual commands, exit codes, and logs.
The isolated Python 3.11 focused selection passed **553 tests**. Baseline and
post-edit strict validation scanned all 15,910 normalized records with zero
errors. Representative open-schema and canonical-ID checks passed. All five
earlier medium readbacks and the KOMODO 12 readback passed, as did independent
semantic-diff and exact-path coverage checks.

[Actual-group retention](merge-retention.json) fails: 50 records in 50 groups,
223 accepted claims, 187 retained. Nine records lose evidence and ten lose the
new reference. All new evidence remains intact in authoritative normalized YAML.
No generated merge was published or manually patched.

The full suite cannot run in this environment: the ordinary command lacks
coverage support and its no-coverage retry fails during dependency imports.
Product validation lacks `oaklib`; reference validation lacks its executable.
These are not maintained Python 3.13 or CI passes. Dependency pins were not
changed. Black and Ruff passed for the changed reviewer, tests, withholding
builder, preflight checker, and validation driver. `git diff --check` passed.

All 23 post-apply jobs and both baseline jobs are terminal. Global merge
verification fails with 1,247 name conflicts and 3,287 fingerprint issues.
[Freshness](merge-freshness.json) also fails: 6,320 tracked versus 6,491 fresh
records, with 3,718 only tracked, 3,889 only fresh, 1,624 changed, and 978
unchanged. Regeneration was temporary only. No gate failure is treated as a pass.

## Remaining Work

The 18 withholding decisions need source-specific repairs, not merely another
mechanical run. J896 has a verified original-source basis ready for guarded
curation. Historical plans and reports must remain unchanged; a successor must
be explicitly hash-linked into readback, coverage, and semantic-diff checks.

The next receiving-medium offset is 3000, with 329 targets left in that frozen
source inventory. Other source collections and unresolved claims within all
previous reports remain in scope. Changes are local and uncommitted; no PR,
merge, or completion of the all-record objective is asserted.
