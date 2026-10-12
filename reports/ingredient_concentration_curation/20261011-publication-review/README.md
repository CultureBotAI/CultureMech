# Concentration Publication Review

Publication: [draft PR 577](https://github.com/CultureBotAI/CultureMech/pull/577).
Initial curation commit: `06b8c3856f`; main integration: `0c73c10a86`.

Review date: 2026-10-11. Worktree baseline:
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.
Fetched main: `0e409dd9aecf0f51586d0dd418ba9713dd99d0cb`.

This is a publication and adversarial code review, not a new scientific review
of every concentration. Prior batch receipts remain historical observations of
their pinned inputs, not validation of subsequent code changes.

## Findings

1. **P1, reproducibility: ignored PDF dependencies.** Ten curation guards read
   original PDFs from ignored `references_cache` paths. Reproduced by pointing
   `repair_linked_middlebrook.ROOT` at an empty temporary directory: source
   loading fails at `DSMZ_Medium645.pdf`. Tracked in
   [issue 575](https://github.com/CultureBotAI/CultureMech/issues/575).
   The fix adds twenty digest-addressed source fixtures (2,171,322 JSON bytes)
   and an exact provenance/byte-checking reader. No historical context, snippet
   or normalized record changes. Twenty-three tests pass, including all ten
   affected source readers with reference-cache reads forbidden.
2. **P1, generated corpus: merge output is stale.** The preceding terminal
   checkpoint reports failing merge verification and freshness. Its 15,056
   derivation differences are not a fresh result for this publication revision.
   The formulation-aware merger changes grouping semantics; publishing only
   normalized inputs does not repair stored merges or their rendered pages.
   Existing [issue 396](https://github.com/CultureBotAI/CultureMech/issues/396)
   covers the artifact-policy and freshness problem. Do not hand-patch merges.
3. **P1, validation: no full-suite pass for this revision.** The recorded
   earlier full run passed assertions but exited nonzero on four 120-second
   test budgets. It predates the final curation batches and this fixture fix.
   Budgets and allowlists must not be relaxed to claim a pass.
   Tracked in [issue 576](https://github.com/CultureBotAI/CultureMech/issues/576).
4. **P2, references: unresolved parser/title limits.** Existing
   [issue 571](https://github.com/CultureBotAI/CultureMech/issues/571) tracks
   recipe evidence validation. The isolated strict UTEX parser was not installed;
   four earlier UTEX title checks reject HTML-encoded apostrophes. The latest
   three-record live-reference receipt does not clear those earlier failures.
5. **P2, CI scope: large diffs can evade path-filtered workflows.** This packet
   exceeds 300 files. Existing
   [issue 277](https://github.com/CultureBotAI/CultureMech/issues/277) must be
   considered when inspecting checks; absent checks are not passing checks.
6. **P1, packaging: transitive review inputs were omitted.** A clean committed
   checkout collected 19,269 tests, but a focused run had 339 passes and two
   failures. The OTEB guard follows a context path stored in JSON; the rumen
   guard adds `.json` to receipt names stored without the suffix. The first
   publication selection missed those dependencies, despite passing locally.
   [Issue 578](https://github.com/CultureBotAI/CultureMech/issues/578) records the
   exact reproduction. The follow-up selection includes transitive report-local
   paths and receipt names without changing their pinned contents. Clean runtime
   verification is required; collection alone is insufficient.

## Publication Scope

The publication manifest selects the modified authoritative records and shared
code, curation tools and tests, saved Markdown reviews, and named reproducibility
inputs required by those tools/tests. Unselected previews, raw reference caches,
generated pages, logs and temporary exports remain local. No blanket `git add .`
or forced cache addition is used. Dependency selection is conservative and must
be verified from the published tree, not just from this populated workstation.
The manifest's dependency-closure parent identifies the integration revision;
its selected-file hashes are refreshed after schema generation and packaging
corrections. Historical batch checkpoints remain unchanged.

The PR must remain draft while substantive findings or required validation are
unresolved. The all-record scientific curation objective is still incomplete.
This review does not authorize calling that objective finished or treating
report presence as verification of every quantity.

## CI Remediation Follow-up

At `30f17ae793`, all nine required checks ran: seven passed, the fast tier
failed three subprocess import tests, and the full suite timed out after its
derived-artifact manifest comparison failed. These are actual CI results from
run `38127779552`, not inferred passes from local artifact presence.

[Issue 581](https://github.com/CultureBotAI/CultureMech/issues/581) records the
new reproducibility findings. The guard subprocesses now run from the scripts
directory with `PYTHONPATH` explicitly absent. Dated curation packets are
classified as historical snapshots, without attributing generic receipt names
to unrelated live writers. Undated outputs remain visible. The inventory reads
candidate scripts once per scan, including ignored/hidden Python files; it does
not cache across invocations. Its manifest is regenerated, not hand-edited.

The runtime fix for issue 576 reuses the existing session-scoped corpus fixture
in ranking tests. Middlebrook source validation and parsing now run once per
operation, with fresh context and PDF integrity checks on each operation and
unchanged record/schema/concurrent-edit guards. Exact small HTML cell parsing
has a bounded pure-text cache; altered source bytes have different keys, large
documents bypass it, and validation decisions are never cached by this helper.

Verification before publication: 78 artifact/ranking tests and 96 reference
tests pass without the workstation YAML-loader shim. The three optimized-Python
guard subprocess tests pass with no ambient `PYTHONPATH`. All changed Python
passes Ruff and Black. The required full CI suite remains the merge gate;
budgets, coverage thresholds, tier markers and exception lists are unchanged.

### PDF Extraction Follow-up

The clean full run at `998b09ec7f` was deliberately interrupted after 1,632
passes to investigate a measured remaining cost. It is not a full-suite pass.
Profiling the Desulfurobacterium source loader attributed 20.6 of 22.7 seconds
to decoding the same five PDFs, chiefly their font maps. Reusing KOMODO parses
did not improve a separate benchmark, so that proposed cache was not added.

PDF extraction now reuses at most eight immutable `(text, page_count)` results
for inputs up to 256 KiB. Keys include exact PDF bytes, reader identity and all
extraction limits. Larger files bypass the cache. Source readers still reopen
their captures and check provenance, digest and expected text. Changed bytes,
stricter limits, reader changes, cache bounds and the large-input bypass have
explicit tests. A two-load benchmark returned identical output in 8.8 seconds
cold and 0.7 seconds warm. A new complete run is required at the successor head.

### Portable Historical Receipts

Issue 583 records an additional dependency missed by same-workstation clean
checkouts: Halobacteria guards opened historical absolute log and validation
paths. Nineteen digest-addressed fixtures preserve the exact bytes for 111
receipt references. The resolver checks the registered repository-relative
source name, original digest, strict encoding and symlink boundaries, and never
falls back to the historical workstation path. Frozen receipts are unchanged.

All 526 focused receipt and Halobacteria tests pass with historical workstation
reads explicitly forbidden, including deterministic replay, independent
projection, tamper rejection, concurrent edits and guarded no-op application.
The full CI gate is still pending. The latest fast tier separately exposed
issue 584: main refreshed the MIM index in PR 537 while this PR was under review.
That compatibility finding is not repaired by portable receipt fixtures.

### Refreshed Index And Native Safe Parsing

Main's PR 537 changes the MIM pin from `9f09e4fb` to `6643131b`. Issue 584 is
addressed by a separate, hash-pinned compatibility assessment: the exact
nickel-hexahydrate candidate and REJECTED status are unchanged; ambiguity changes
from resolved:owned to unique. The runtime checks current bytes, metadata and
the exact resolution against that assessment. Unknown bytes or changed resolver
semantics still fail. Historical review bytes, hashes and chemical assertions
are unchanged. Four dedicated drift/preservation tests pass.

The local full run at `27baf7d899` was interrupted after 1,898 passes to integrate
current main and the receipt repairs. It is not a full pass. Profiling a
remaining slow guarded application attributes 64.7 of 100.3 call seconds to
pure-Python YAML span parsing. The curation span-preserver and 42 active audit
modules now use PyYAML's existing CSafeLoader, without changing the dumper.
AST comparison confirms that those audit changes alter only safe-loader
selection, not assertions or control flow. Archived preview code is unchanged.
The guarded application passes in 17.7 unprofiled call seconds. Regression tests
compare parsed data and output source spans against the Python safe parser for
large frozen records, multiline text, Unicode, aliases and scalar types, and
verify rejection of Python object tags. No loader is globally monkeypatched in
the application or full-suite environment. Runtime limits remain unchanged.

### Independent Audit Dependency Closure

The cancelled `27baf7d899` CI log also exposed an ignored PDF read through the
KOMODO successor-chain audit. A clean checkout at `a9fe45da12` reproduced it.
Issue 585 covers this and the same dependency in the resazurin identity audit.
Those readers now use the exact PDF fixture resolver; one additional PDF is
needed. Their historical MIM assertions replay against the original CSV and
metadata capture, with both whole-capture and CSV digest checks. This snapshot
is not substituted for the current ingredient resolver or called current
evidence. The resazurin historical builder uses the same original pin.

Issue 584 also covers a second live-index guard in the Halobacteria family.
All 24 inspected lookups were compared with the refreshed index: identities,
chemical forms and statuses are unchanged; only Casamino acids ambiguity
changes from resolved:owned to unique. A separate pinned assessment verifies
every current answer. Unknown bytes, altered assessments and semantic drift
remain failures. The first Syntrophomonas compatibility fix alone was not
sufficient. The expanded tests prohibit ignored-cache reads, alongside the
existing prohibition on workstation-only receipt reads.
