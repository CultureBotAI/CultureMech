# Batch079 review-helper provenance

These one-run artifacts document the record07, record08 and record10 scientific
reviews prepared on 2026-11-15, tracked in [issue752](https://github.com/CultureBotAI/CultureMech/issues/752).
They describe review assembly and checking, not recipe repairs or whole-batch
completion.

[manifest.json](manifest.json) identifies each version's exact SHA-256, original
runtime path, recovery method, purpose, input/output scope and available execution
evidence. The `argv_display` fields normalize the historical executable and
checkout to `$UV` and `$CHECKOUT`; the separately pinned original receipts retain
the exact raw argv. Metadata paths are repository-relative. Paths under `.temp/` identify
ignored local evidence, which is not shipped with a clean checkout.

## Exact historical source data

The `history/*.py.txt` files are exact historical bytes, including superseded and
failed-attempt sources. **Do not execute, lint or reformat these archival copies.**
Current executable helpers remain separately in `scripts/batch079*.py`; their
formatting does not rewrite history. The first runner's workstation PATH literal
is preserved only because it is part of the exact original source.

Three early sources were recovered literally from recorded creation commands.
Two intermediate runner sources were reconstructed with the recorded Ruff import
fix and Black settings. Exact successor comparisons reproduce the preserved
post-edit sources, including the record07 NoAlias fix. The initial alias-producing
draft and failed native validation remain preserved in ignored evidence. Recovery
parsed sources and transformed strings; it did not execute recovered helpers.
The manifest distinguishes retained bytes, literal recovery and deterministic
reconstruction, and states remaining evidence limits. The first record08 builder
was retained without author execution; the distinct v2 source was executed.

The archive also includes the two executed record10 metadata amendments and
eighteen literal chemical-audit heredocs: six core capture/assessment bodies plus
their scoped probes, inventories and scientific projection readers. Each has
call/output event hashes. Some older outputs contain completed child text without
a serialized process exit; these remain null rather than being reported as exit0.
No full transcript is published, and no recovered source was rerun.

## Helper roles and replay limits

- The runners capture one explicitly supplied command; v2 also records launch
  errors and preserves dotted receipt labels.
- The record07 inventory associates fields with source locations without making
  a scientific judgment.
- Builders assemble manually reviewed findings from frozen local captures,
  inventories, chemical assessments and native diagnostics. They contain
  task-specific assumptions and fixed evidence hashes.
- Chemical capture and assessment snippets record exact ontology queries, local
  ingredient slots, MIM rows and manually reviewed chemical-form interpretations.
  They can fetch public responses or write audit evidence if executed; the archives
  are preserved as data only.
- The record08 metadata helper preserves and amends an unsaved draft after exact
  field checks. Native validation, saving and persisted-bundle checking are
  separate recorded operations.

These helpers are not public APIs or generic curation commands. Replay requires
the exact ignored evidence, runtime and file state; a fresh checkout alone is
insufficient. Builders can write drafts or invoke native inspection, and a runner
can execute its explicit argument. Archiving code does not authorize rerunning it.

The user-requested publication scope includes this provenance and a current
checkpoint alongside the three immutable review pairs. Earlier bundle-only plans
remain historical. Saved review YAML/Markdown and prior receipts are preserved;
the current checkpoint owns final validation status. Full transcripts, credentials
and unrelated session context are not published here.

## Current record10 portability successor

The current executable `scripts/batch079_build_record10_review.py` now requires
`--original-native-dir`, parsed as a `Path`, to select its historical native
inspection and diagnostic inputs. This replaces the machine-specific receipt
directory identified by [issue754](https://github.com/CultureBotAI/CultureMech/issues/754).
It is a **functional CLI repair**, separate from publication formatting. Callers
must provide the exact retained evidence directory; there is no implicit
workstation-path fallback, and existing input-hash checks still apply.

The original executed builder remains unchanged in
[its source-data archive](history/batch079_build_record10_review.retained-pre-format.py.txt)
(SHA-256 `508a865dec7a184b0d7ba8facfd1d7b0233e805d40aa29d2ae4f7f1f3b08090e`).
The later formatted pre-repair copy is retained locally at
`.temp/batch079-scientific-20261114/helpers-pre-machine-path-fix-record10.py`
(SHA-256 `a1d5a2c148f0626c30d009224bb10304043528dbb9ecaf3deedf8a860ba00728`).
The immutable saved review pair is unchanged; this CLI repair does not authorize
rerunning its author or restamping the review. The checkpoint records the actual
failing full-suite run and subsequent targeted/full validation outcomes separately.

## Documentation-only header successors

All nine current executable helpers now have module headers stating purpose,
required inputs, outputs, task date and related issues. These documentation-only
successors followed the successful full `just test-fast` run (16,111 passed).
Independent AST comparison found only module-docstring changes; executable
statements were unchanged. Ruff, Black and the existing portability module
(1,017 passed) were checked afterward. The full suite was not repeated for these
header changes. The checkpoint keeps these validation boundaries explicit.

Pre-header executable copies remain in the ignored
`.temp/batch079-scientific-20261114/helpers-pre-provenance-headers/` archive.
The 33 historical source-data archives and immutable review pairs were unchanged.
