# Paper Citation Publication Review

PR #620 publishes the citation skill, archival tooling, 392 curated normalized
records, and 34 immutable structured review bundles. The sealed curation ledger
records 517 new paper-record citations, 27 enrichments, and 162 newly cited
unique papers. These are bibliography counts, not organism-growth counts.
The publication inventory verified 15,910 normalized-record hashes and 2,157
local source-archive hashes. Original sources, Markdown conversions, and run
scratch files remain local; ignored source caches are not redistributed.

## Adversarial Self-Review

This is a curator-performed publication review, not independent scientific
approval of the full corpus. The saved record reviews retain their own scope,
source hashes, unresolved findings, and historical validation results.

- #621: invalid DOI search payloads were persisted before validation, causing
  later retries to reuse an error page. Validate structure, count and PMID
  syntax before writing the cache. Failure-then-success regression cases cover
  HTML, API errors, invalid counts, and invalid identifiers.
- #622: KGX ignored `scoped_to_variant` and could broaden growth evidence to
  the parent medium. The parent-edge helper now omits these observations with
  a warning. Tests cover direct calls and transforms, including preservation
  of unscoped parent/linked-child assertions. Variant-specific evidence remains
  in YAML; complete variant-target KGX export is not claimed.
- Black formatting of the new title-validation tests was corrected.

## Remaining Limits

- #623 tracks automatic JaLC metadata retrieval. The AF6 citation is verified
  from publisher sources, but its automatic reference check still fails.
- #624 tracks existing AF6 formulation and stock/variant ambiguities. Citation
  notes do not certify those quantities or establish parent-medium growth.
- #625 tracks trailing whitespace in canonical immutable review Markdown.
  Historical bundles are preserved rather than silently reformatted; full
  branch `git diff --check` reports this known formatting limitation.
- #396 tracks generated merge drift. This PR does not regenerate merged
  recipes or publish KGX/pages. The scheduled freshness check is not a blocking
  per-PR gate under the existing workflow policy.

Focused post-fix validation passed 96 tests; Ruff, Black, and the skill checker
passed. Required GitHub checks and the merge queue remain authoritative for
integration. Literature discovery and historical recipe reconciliation are
unfinished; this PR must not be described as corpus-wide scientific approval.
