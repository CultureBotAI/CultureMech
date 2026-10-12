# Scoped UTEX Integration Preview

## Applied Successor

This packet has since been applied locally. The [applied batch](../../20261010-next-utex-applied/README.md)
records eighteen verified edits, installed-code regressions, canonical reports,
source checks and remaining gates. The preview statements below are historical;
the UTEX parser remains excluded from installation.

## Frozen Preview

The [current v3 packet](validation.json) retains the corrected eighteen record
proposals and the tested KGX nested-stock fix, but **excludes installation of the
UTEX reference parser**. Existing-record compatibility issues are recorded in the
[local issue review](../../20261010-utex-reference-parser-preview/ISSUES.md).

Nine files are pinned: three guarded curation scripts and tests, the KGX fix and
test, and the cumulative-audit registry. Fresh real-schema dry runs and all three
audit dispatches pass; the combined patch passes application checking. No installed
code or authoritative YAML has changed.

The exact recipe proposals are identical to the v2 packet: soil/seawater v2,
organic-medium v3 and six-blends v1. Therefore the [eighteen reports](../v2/records/),
[render receipt](../v2/render-preview.json), source/guard checks and
[90 passing live checks with the isolated parser](../../20261010-utex-reference-parser-preview/v3/live-reference-preview-network.json)
still apply to their unchanged hashes. An isolated parser pass must not be reported
as a pass of the installed reference CLI. Its generic title/extraction failures
remain a separate gate result.

The current batch driver is `continue_applied.py`. It refuses to run before the
prior J/DAS full suite is terminal and its applied checkpoint is sealed. After
installation/application, actual readback/no-op, installed regressions, canonical
reports, cumulative accounting, indexes and corpus/derived-output checks remain
required. This packet is not applied or publication-ready.
