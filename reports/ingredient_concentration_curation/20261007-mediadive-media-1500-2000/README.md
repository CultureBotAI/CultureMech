# Fourth Receiving-Medium Source Pass

This is an applied evidence-only batch, not completion of the all-record goal.
It covers frozen inventory offsets 1500-1999, with one result for every exact
tracked path, including unchanged records.

## Applied Changes

- Records reported: **500**; edited: **86**; unchanged: **414**.
- New ingredient evidence entries: **551**, each with a verified official
  MediaDive recipe URL, exact source JSON snippet, claim path, arithmetic,
  retrieval date, and response hash.
- New bibliography entries and appended curation events: **86 each**.
- Numerical, ingredient-identity, stock, variant, and growth-association changes:
  **zero**. Existing amounts were retained, not newly measured or inferred.
- Claims still unresolved in this snapshot: **11,583 unsupported** and
  **7,570 conflict** rows. These include source-only rows and preparation context;
  they are not all independent concentration claims.
- Failed records and baseline/post-edit closed-schema errors: **zero**.

Evidence supports the provider-declared main-recipe concentrations only. It
does not establish an independently measured final volume, validate secondary
ontology mappings, or authorize evidence propagation to another formulation.
Missing authors and publication years were not invented.

The [preflight](preflight.json) rebuilds all 500 proposals, pins target and source
hashes, checks ingredient identity and exact excerpts, and independently restores
the original semantic objects by removing only the appended provenance. It
proves no other fields changed. Unsupported claims remain unchanged.

## Adversarial Review

The initial preview contained 90 editable records and 574 proposed evidence
entries. Inspection of all 90 candidates' preparation text and proposed source
amounts found four records requiring separate repairs. All four original PDFs
were downloaded and visually inspected; this is not inspection of all 500 PDFs.

The [source findings](preparation-findings.md) document:

- DSMZ 1431: agar preparation replaces the liquid-table carbonate amount.
- DSMZ 1462: agar explicitly omits supplemental calcium.
- DSMZ 1624: base-table concentrations omit later molar-stock additions.
- DSMZ 1641: the original table repeats pyruvate under two names.

All **23** preliminary claims across those four records were withheld before
application. The new guards and thirteen regression cases prevent these known
automatic-endorsement errors; they do not resolve the recipes. The 419 earlier
accepted medium records were checked against the new guards, with no new hits.
The broader DSMZ 550 shared-ID finding is recorded separately, not silently
treated as duplicate chemical evidence.

This batch contains 399 DSMZ and 101 CCAP source entries. Its 157
collection/link-blocked records include those 101 CCAP entries and 56 DSMZ entries
without the established original link required by this reviewer. There are also
221 stock-topology-blocked records, seven unresolved main-solution identities,
and further inventory/preparation gaps. No collection or stock boundary was
bypassed to increase coverage.

## Verification

Applied read-back checks **500 hashes and 551 new snippets**. Reapplication
changes **zero** records. The independent preflight and preserved baseline
hashes precede the write; the all-corpus strict gate passes on **15,910** records
both before and after. Representative open-schema and stable-ID checks pass.
The focused suite passes **512 tests**. Ruff, Black, and whitespace checks pass
for the changed review code and scoped checker. Validation outcomes are recorded
in [validation.json](validation.json).

The environment is isolated Python 3.11, not the maintained Python 3.13/CI
environment. Full-suite execution stops on missing coverage support; a
no-coverage retry stops during collection on four missing modules. Product and
reference checks lack their dependencies. A separate [frozen Python 3.13 setup
attempt](runtime-attempts.json) fails while building `llvmlite==0.46.0`; no
dependency pins or existing environment were changed.

The [actual-group retention check](merge-retention.json) fails: **446 of 551**
amount/evidence pairs survive across 81 groups. Twenty records lose evidence and
nineteen lose their new bibliography entry. Global merge verification also fails,
with 1,247 name conflicts and 3,287 fingerprint issues. The [freshness gate](merge-freshness.json)
fails: 6,320 tracked versus 6,491 fresh records, with 3,718 only tracked,
3,889 only fresh, 1,549 changed, and 1,053 unchanged. All 21 sequential validation
jobs are terminal and have recorded exit codes. Schema and snippet passes do not
imply publishable merges. Generated merges are not hand-edited or copied into
the worktree. These changes remain local and uncommitted.
