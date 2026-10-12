# Source-Title Prefix Follow-Up

Local issue; no GitHub issue was created. S1680 is a verified example. In the
first proposal, the [terminal reference check](cached.json) rejected the existing
title `MediaDive solution 1680: Growth-stimulating factors`. The pinned
[official source](https://mediadive.dsmz.de/rest/solution/1680) names the source
`Growth-stimulating factors`. The accession belongs in the identifier/provenance,
not in a purported literal title.

`plan-v2.json` corrects only that title and its supporting claim relative to the
first proposal, preserving all six existing acid entries and their evidence.
The [successor receipt](cached-v2.json) passes all 661 checks. The successor is
now applied with verified readback; neither the old failure nor the first plan
was overwritten.

## Broader Candidates

The pre-application [read-only inventory](next-title-prefix-candidates.json)
found 4,137 files matching a solution-title prefix and 730 matching a medium-title
prefix, or 4,867 unique exact tracked normalized paths. These are **textual
candidates**, not verified bibliography errors. Matches may occur in historical
or nested content rather than a current bibliography entry. The inventory pins
every candidate's then-current bytes and records zero edits. The ignored-inclusive
[applied-corpus inventory](next-title-prefix-candidates-applied.json) finds
4,866 candidate paths, with 4,868 structured current root-reference entries
across those same 4,866 paths. These stronger structural leads still need exact
source-title verification; only S1680 was verified and repaired in this batch.

Before changing any further record:

1. Parse the current `references` and evidence containers structurally. Do not
   treat text in an old curation event as an active bibliography claim.
2. Confirm the exact medium/solution accession and its source capture/version.
3. Compare the actual official title and source metadata. Do not remove a real
   title prefix or rewrite a journal citation merely because a regex matched.
4. Attach a literal source-title snippet and PURL to any correction, preserve
   ingredient evidence/history, and validate the resulting references.
5. Recompute candidate and applied counts. The original inventory includes
   S1680's old baseline; use the separate applied-corpus successor for current
   counts and preserve both historical receipts.

This queue supplements, and does not replace, the remaining concentration,
ingredient identity, stock-boundary and full-corpus review work.
