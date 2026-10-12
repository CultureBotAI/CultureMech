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

### Mutation Test Serialization

At `1e02daa498`, eight required checks passed, but full-suite job
`114654067248` exceeded its 40-minute limit and ended cancelled after 45m1s.
The fast tier passed 15,766 tests with 23 skips. The full-job log was unavailable
through both the job endpoint and the run archive; its check annotation confirms
the timeout. Issue 576 remains open. A non-fast diagnostic with coverage runs
separately against an unchanged clean checkout, not as a claimed full pass.

Profiling a Methanofollis quantity mutation attributes 0.66 of 1.18 call seconds
to rendering a forged document. A Halobacteria mutation attributes 0.40 of 0.51
seconds to its parsing/formatting helper. Six affected test modules now use the
existing JSON-as-YAML forgery pattern, retaining digest recomputation, every
mutation, independent source validation and real guarded-write tests. The two
Halobacteria mutation helpers and mock builders use the existing safe runtime
loader. A profiled late-edit guard spent 3.21 of 6.84 call seconds in the mock
builder's repeated Python YAML parses. Production writers, scientific assertions
and fixture data do not change.

Positive controls exercise every valid record through the same serialization
and independent audit. They caught S608's byte-exact no-op contract: the helper
preserves original bytes when the document is unchanged, and a dedicated test
still rejects a formatting-only rewrite of S608. No audit guard was relaxed.
The four-family regression run passes all 1,603 tests, including guarded
application/readback/no-op cases; the artifact inventory has 31 passing tests.
The two Halobacteria modules pass all 534 tests after the mock-builder change;
their guarded apply/readback/no-op calls take 3.05 and 9.03 seconds locally.
The full CI, coverage, call-budget and merge-queue requirements remain unchanged.

### Batched Elemental Metadata

The clean diagnostic also exposed repeated SQLite metadata queries in the
elemental-grounding fixture. A live process sample was dominated by SQLite
reads. A comparison using the installed, lockfile-matching OAK 0.7.4 adapter
covered all 234 requested ChEBI IDs: 229 formulas, five absent formulas, no
multiple-valued formulas, no metadata errors and no differences between the
individual and bulk answers. The original fixture took 333.44 seconds including
its corpus scan; the bulk formula query took 1.39 seconds.

Issue 586 additionally records that the old per-term exception handler silently
treated query failures as missing formulas. The fixture now uses OAK's supported
bulk metadata API with the same formula predicate and first-value semantics.
Its corpus scan, salt allowlist and scientific mismatch assertions are unchanged.
Query failures, unexpected rows, empty selection and wholly absent formula
coverage fail closed; individual missing formulas retain their previous handling.
The full module passes 12 tests in 51.92 seconds, with fixture setup at 36.89
seconds. This changes no production code, recipe, ontology pin or evidence.

### Statement Coverage Collector

Full CI at `f52f224a40` again exceeded the unchanged 40-minute limit, with
job `114671962052` cancelled after 45m1s. All eight other required checks passed;
the fast tier passed 15,789 tests with 23 skips. The full job log endpoint
returns HTTP 404, and the workflow log command reports that job log missing.
This is not a full-suite pass; issue 576 remains open.

Issue 587 records a measured collector cost. The pinned coverage.py 7.13.1
supports `sysmon` statement coverage on the maintained Python 3.13 runtime.
The project does not enable branch coverage, coverage plugins or dynamic
contexts, which would require a different compatibility assessment. See the
[versioned collector documentation](https://coverage.readthedocs.io/en/7.13.1/config.html#run-core).
The configured collector now uses `sysmon`; source/omit scope, the 17% coverage
floor, every test, the 120-second call budget and 40-minute job timeout are
unchanged. No scientific data or production behavior changes.

Sequential runs of the same 804-test Geobacter module pass under both
collectors: 371.14s with `ctrace`, 151.95s with `sysmon`. Direct CoverageData
comparison finds identical sets of 101 measured files and 333 executed lines.
These diagnostic subset runs override the coverage floor only to permit
collector comparison; they do not replace the required full-suite gate.
New subprocess controls assert exact executed-line sets and demonstrate both
a passing fully executed probe and rejection of an unexecuted body below the
unchanged configured coverage floor.

The broader fingerprint, reference-validation, renderer and KGX comparison
passes 197 tests with one optional-dependency skip under each collector. Its
coverage databases also agree exactly: 101 measured files, 1,834 executed
lines, no differing line sets. These runs overlapped, so their elapsed times
are not treated as an isolated performance comparison. The three new coverage
controls and fourteen existing merge-queue contract tests all pass.

### Bounded Parallel Execution

Full CI at `581ccd3084` again exceeded its 40-minute limit; eight other checks
passed, including 15,792 fast tests with 23 skips. The complete clean-checkout
serial diagnostic collected 19,434 tests and finished in 2,897.30s: 19,408
passed, 25 skipped, and one failure from a local `gen-linkml` pyenv shim. That
case passes when the fresh environment's bin directory is placed on PATH.
Coverage reached 33.63%; the largest call was 43.21s, below the unchanged
120-second budget. This is not described as a green full run. The diagnostic
omitted the unsupported macOS UMAP/LLVM dependency stack, but included Koza.
An earlier local attempt was invalidated by disappearing temporary-environment
files and was interrupted; its failures are not repository regressions.

Module timings show distributed cost: the largest module took 165.52s, not a
single call exceeding the budget. Issue 588 follows the explicit aggregation
requirement from issue 213. `just test` now uses exactly two pytest-xdist workers,
per-file scheduling and no worker restarts. Each worker publishes call durations;
the controller requires complete, finite, nonnegative receipts and reconciles
them against independently forwarded reports. Missing, duplicate, unexpected,
crashed or inconsistent workers fail closed. The 120-second call budget, empty
allowlist, 17% combined coverage floor and 40-minute job timeout are unchanged.
No test is excluded or moved to another tier.

The initial 47 focused tests pass, including actual multi-worker positive,
slow-call, missing-receipt, forged-receipt and crash cases. A two-worker coverage
probe requires complete coverage of both workers' executed functions. The
expanded cohort run passes 1,292 tests and explicitly reconciles all 1,292 call
receipts across two workers. These are focused checks, not a full-suite pass.
The lockfile adds only pytest-xdist 3.8.0 and execnet 2.1.2; existing pins remain.

### TSV Reader Lifecycle

The serial diagnostic also exposed repeated unraisable ResourceWarnings from
the KGX export verifier. Issue 589 tracks the row counter's unclosed TSV reader.
Two regression controls retain the opened handles and reproduce the leak on
both successful verification and empty-output rejection. The row counter now
uses a context manager; row counts, output bytes and rejection behavior are
unchanged. Actual Koza export tests run with unraisable warnings treated as
errors before publication.
Both new controls fail against the previous reader lifecycle and pass after
the fix. All 26 Koza TSV tests pass with unraisable warnings promoted to errors.

### CI Worker Capacity

The two-worker full job `114717792811` at `f449360d65` finalized cancelled after
45 minutes with an explicit 40-minute timeout annotation. The other eight
required checks passed. Issue 588's
follow-up uses four workers in CI, matching the documented four CPUs and 16 GB
RAM of this public repository's `ubuntu-latest` runner. See the
[GitHub runner specification](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories).
The local `just test` default remains two workers; CI explicitly calls
`just test 4`. File scheduling, zero worker restarts, receipt reconciliation,
all tests, combined coverage, the 17% floor, the 120-second call budget and the
40-minute job limit are unchanged. No full-suite pass is claimed here.

New contract tests check both recipe invocations, the CI worker count and the
unchanged timeout. The four-worker cohort passes all 1,295 tests in 148.91s,
with all 1,295 call receipts reconciled across four workers. This includes the
negative timing-receipt and combined-coverage subprocess controls, both large
concentration cohorts, artifact checks and workflow contracts. Full required
CI remains the merge prerequisite; local cohort timing is not a CI guarantee.
