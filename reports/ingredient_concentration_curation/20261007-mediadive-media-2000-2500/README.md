# Fifth Receiving-Medium Source Pass

This is an applied local batch, not completion of the all-record objective.
Baseline commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.
The frozen medium inventory slice is `[2000:2500]`: nine CCAP and 491 JCM
records. Authoritative normalized YAML only; no generated merges were copied.

## Outcome

- 500 exact-path reports, each with one record marker and all claim rows.
- 107 edited records, 393 unchanged; zero failed or schema-blocked proposals.
- 492 new evidence entries, 107 bibliography entries, 107 append-only events.
- No numerical, unit, chemical-identity, stock, variant, or growth-claim changes.
- 151 preliminary claims withheld across 24 records after preparation review.
  Two records retain supported rows while their ambiguous rows remain unchanged.
- Remaining report rows: 6,018 conflict and 6,881 unsupported. These include
  source inventory/preparation rows and are not independent concentration counts.

[preflight.json](preflight.json) independently proves that removing the appended
provenance restores every original record, and that manual decisions only remove
support. [plan.json](plan.json) freezes source/record hashes, all proposals, and
the [source-pinned withholdings](withholdings.json). The guarded apply rebuilds
claims before writing. Reapplication made zero changes; readback verified 500
record hashes and 492 persisted literal snippets.

## Sources

Each new YAML claim cites its exact official MediaDive JSON endpoint with a
literal ingredient-row excerpt, locator, volume/arithmetic explanation, retrieval
date and response hash. JCM accession and original collection are separately
identified from DSMZ as dataset provider. Unknown individual authors and
publication years are not manufactured. These claims support provider-declared
recipe amounts, not independently measured final volumes or ontology mappings.

All 129 initially eligible candidates' main preparation text and proposed amounts
were inspected. [Preparation findings](preparation-findings.md) explain omitted
stocks, volume ambiguity, extraction inputs, and alternatives. The
[selected original-source checks](original-source-checks.json) include 13 HTML
responses and two visually inspected provider PDFs, not all 500 original recipes.
The JCM 2, 19 and 146 original endpoints are empty, despite returning a page.
Seventy-two cohort API responses have no recipe table. CCAP S77 still needs its
[original-source repair](../20261007-mediadive-media-1500-2000/ccap-s77-handoff.md).

## Verification

[validation.json](validation.json) records actual commands, exit codes and logs.
The isolated Python 3.11 focused selection passed **550 tests**. Baseline and
post-edit strict validation scanned all 15,910 normalized records with zero
errors. Representative open-schema and the canonical-ID checks passed, as did
all four earlier medium readbacks and the KOMODO 12 readback. Black and Ruff
passed for the changed reviewer, tests, withholding builder and preflight code.

The full test suite remains unavailable: the ordinary command lacks coverage
support, and its no-coverage retry stops on missing dependency modules.
Product validation lacks `oaklib`; reference validation lacks its executable.
These are not maintained Python 3.13 or CI passes. The prior maintained-runtime
installation failure is documented separately; dependency pins were not changed.

[Actual-group retention](merge-retention.json) fails: 107 records in 97 groups,
492 accepted claims, 414 retained. Twenty-four records lose evidence and 26 lose
their new reference. The normalized evidence remains intact. No evidence was
copied across unverified formulations to force a passing result.

All 22 post-apply jobs and both baseline jobs are terminal. Global merge
verification fails with 1,247 name conflicts and 3,287 fingerprint issues.
[Freshness](merge-freshness.json) also fails: 6,320 tracked versus 6,491 fresh
records, with 3,718 only tracked, 3,889 only fresh, 1,597 changed and 1,005
unchanged. Regeneration was temporary only. `git diff --check` passes.

## Remaining Work

The 24 withholding decisions require scientific repairs, not merely reruns.
[Two original-DSMZ follow-up findings](earlier-preparation-handoff.json) additionally
pin seven earlier evidence scopes for reassessment and unsupported legacy
percent-to-g/L encodings. Those earlier records were not edited here.
Historical plans and reports remain unchanged; any repair needs an explicit
successor with evidence and hash-linked readback.

The next medium inventory offset is 2500. Its [500 sources](../20261007-medium-source-fetch-2500-3000.json)
have been acquired, and a [preliminary preparation handoff](../20261007-medium-source-fetch-2500-3000-preparation-leads.md)
records newly identified volume conflicts. The temporary preview is unapplied
and not counted as another completed per-record batch. Records outside these
reports and unsupported claims within all prior reports remain in scope.
Changes are local and uncommitted; no PR or merge is asserted.
