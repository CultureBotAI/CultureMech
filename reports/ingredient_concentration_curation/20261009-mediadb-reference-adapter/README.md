# MediaDB Literal Reference Adapter

This checkpoint fixes automated matching of official MediaDB compound-table
snippets. It does not edit recipes, add evidence, increase review coverage, or
approve pending formulations. The all-record ingredient review remains active.

## Scope

`src/culturemech/validation/recipe_references.py` now recognizes only exact HTTPS
`mediadb.systemsbiology.net/defined_media/media/<positive integer>/` URLs.
It verifies the page title and heading, the self-accession link, one compound
table, its reported row count, and the literal `Amount (mM)` header. Ambiguous
cells, duplicate compound IDs/names, hidden recipe content, and malformed amounts
fail closed. Cache/access/parser failures do not fall back to fuzzy matching.

Quotations must match within a single title, header, or ingredient row. Whitespace
may differ; chemical case, formula digits, signs, decimal precision, and exponent
text may not. `None` remains unknown and is never normalized to zero. Parsing a
negative source value is a literal text check, not scientific acceptance of that
concentration. Navigation, growth claims, and other page prose cannot supply a
matching concentration snippet.

Literature and other official-recipe providers retain their existing routes.
The SQL export remains on the upstream validator; its title failures are not
waived or replaced with hard-coded acceptance.

## Verified Results

- [Source checks](sources-v2.json): 469 original captures verified against their
  recorded SHA-256 values; 7,758 ingredient rows, 469 titles, and 469 unit headers
  pass the production parser and literal validator (8,696 checks).
- The recipe-only test fixture reproduces record 288's exact parsed source
  content. Login/search forms, session tokens, navigation, and unrelated page
  content are excluded. Its provenance records the original capture hash.
- [Actual-record CLI checks](references-v2.json): all 156 ingredient/root snippets
  and six MediaDB page titles now pass. Each of the six records still exits 1
  because its SQL-export reference title fails. The full reference gate is false.
- [Regressions](regression-v2.json): 686 tests pass, with two dependency warnings.
  This includes 195 new adapter cases plus other provider, MediaDB repair, and
  Kaminskyj tests. Ruff, Black, and `git diff --check` pass.
- The fresh full fast tier finished with **13,403 passed, sixteen skipped,
  3,498 deselected and two warnings** in 27:40. The command exited 0. Its detached
  recorder then raised `BrokenPipeError` while printing the saved result; that
  failure remains in `fast-v2.json`. The [final checkpoint](validation.json)
  independently verifies the terminal command result, complete log hash and
  current code/recipe hashes. It distinguishes test success from recorder failure.
  The initial `fast.json` is an interrupted run, not a pass: adversarial inspection
  found an inert-container acceptance defect, and the obsolete run was deliberately
  stopped before the fix. No full-suite pass is asserted.

## Adversarial Finding

The first adapter accepted a complete recipe wrapped in an HTML `template`.
This was reproduced through `parse_recipe` using the real recipe fixture: the
hidden ingredient text appeared in the accepted content. The fix rejects inert
ancestors and nonliteral embedded/fallback markup, with 38 added regression
cases for container and cell locations. No reference failure is suppressed.
All source and actual-record checks were repeated after this fix; the `-v2`
receipts supersede the earlier successful checks for the old code snapshot.

The six CLI checks use hash-verified raw official captures from the earlier
public-source retrieval, not a new network fetch. Historical failed reference
receipts remain unchanged. The new checks establish source-text matching only;
they do not verify original journal-article concentrations or chemical identity.

All completed phases and the independent final check verify that the 15,910-record normalized inventory
is unchanged (inventory SHA-256
`19c45017d3210c6bc2c2fde0ec7a2f2c4a4498191af394cb351249b3299f6a05`).
Curation totals remain 5,291 edited records and 36,625 added evidence entries
from prior batches. No taxa-media associations are added.

## Remaining Work

- Resolve the six SQL-export title failures without manufacturing metadata.
- Handle the separate FGSC HTML-table reference failures for Kaminskyj.
- Resolve primary-source holds before applying the remaining MediaDB draft.
  A [read-only Vogel scan follow-up](../20261009-vogel-source-followup/README.md)
  preserves stock/variant distinctions without approving a correction.
- Fix the independently reproduced MediaDB ingestion defects: source NULL
  becomes zero, the importer uses `chebi_id` as a name after the SQL column fix,
  and a truthiness check discards explicit zero. The code was inspected again
  during this checkpoint; none of these defects is fixed by the table adapter.
- Complete the remaining corpus review and resolve existing merge/freshness
  failures. This local checkpoint is not publication-ready.

To reproduce the offline adapter tests:

```bash
uv run pytest tests/test_recipe_mediadb_references.py --no-cov -q
```

The JSON receipts preserve actual commands, interpreter, log hashes, code hashes,
and source manifests used for this isolated Python 3.13 runtime.
