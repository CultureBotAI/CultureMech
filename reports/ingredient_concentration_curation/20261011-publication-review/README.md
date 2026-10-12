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
