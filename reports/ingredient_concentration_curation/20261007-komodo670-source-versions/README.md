# KOMODO 670 Strain Formulations And Source Versions

Five normalized records are corrected locally: the existing DSM 9463, 9466,
9467 and 9468 children and the KOMODO 670 parent's reciprocal links. This is a
follow-up repair, not completion of the all-record objective.

## Scientific Changes

The [source inspection](source-inspection.md) verifies the BacDive archive
version, DOI metadata, PDF text and rendered recipe pages. The curated children
explicitly use the archive's 2017 named-strain formulations. Their agreement
with KOMODO's pH profiles is not proof of the exact version originally imported.
Four inline alternatives preserve current DSMZ instructions without blending
them into the historical ingredients or preparation.

- Preserve four batch salt masses per child in notes; withdraw their unsupported
  final-medium g/L encodings. Add the archived 1 L water input, not a final volume.
- DSM 9463: omit copied iron and restore 5 g/L sterile powdered sulfur.
- DSM 9466: omit copied iron, restore 5 g/L sulfur and 0.2 g/L yeast extract from
  an autoclaved stock of unspecified strength/dose. Retain archived pH 3.5;
  current-source pH 3.0 is a separate alternative.
- DSM 9467: omit copied iron, restore a filtered 10% w/v glucose stock and the
  separately autoclaved yeast stock. The latter's 1% basis and both receiving
  targets' percent bases remain unspecified; no g/L or stock dose is guessed.
- DSM 9468: restore 40% w/v iron stock in 0.2 N acid. Its dose is 0.25 ml per
  5 ml prepared receiving base, normalized to 50 ml/L of that base, not of final
  medium. Retain the filtration/autoclaving alternative; keep 4 N pH acid separate.
- Correct the two yeast-containing recipes' defined-medium classification and
  the four reciprocal strain-variant relationships. Preserve all previous
  history; replace unjustified `ingredients_curated` flags with `pending_curation`.

The [applied independent audit](diff-audit.json) verifies **55 new evidence
entries, 19 references and five append-only curation events**. There are **nine
new quantity slots**, **22 withdrawn quantity slots** (16 unsupported final-volume
encodings, three inherited acid placeholders and three copied iron amounts),
and one stock concentration rebase. These categories are not interchangeable
counts of added concentrations or unique scientific confirmations. The two
unquantified-carrier counter entries comprise one carrier and one pH reagent.
No new organism-growth association is asserted.

## Verification

The [frozen plan](plan.json) binds exact git-tracked paths, full before/after
records, sources, hashes and 113 scoped claims. Five `*-followup.md` files
supplement existing per-path reports without creating duplicate `- Record:`
entries. Baseline validation passed 258 focused tests, five open-schema checks,
captured source-byte checks and strict validation of all 15,910 normalized records.

Application, readback, no-op reapplication, independent whole-record inversion,
post-edit open-schema/strict checks, IDs and the affected historical 500-record
KOMODO cohort readback pass. The cumulative audit now inverts successive
hash-linked edits rather than dropping the earlier repair of the parent. Its
delta matches this batch's audit exactly, with four newly edited paths.

Post-edit focused tests pass **259 cases**. `just test-fast` passes **7,638 tests**,
with 16 skipped and 1,839 deselected. Product validation passes with 91
non-blocking warnings and 96,057 no-adapter skips; that does not independently
validate every chemical mapping. Variant-link validation scans all 15,910
records and finds 2,986 reciprocal links in each direction, zero errors and zero
warnings. The validator's ignored `--reports-dir` argument was fixed separately;
104 final focused tests and a routed corpus rerun verify it no longer overwrites
the default report paths. Final readback, source-byte checks, cumulative-delta
comparison, Black, Ruff and `git diff --check` pass. The five live result hashes
and the three unchanged 673 handoff hashes are checked. All jobs are terminal.

The [actual-group retention check](merge-retention.json) passes three of five
records. DSM 9463, 9466 and 9467 survive intact; the parent and DSM 9468 do not
retain their distinct version/link/provenance fields in their shared group.
Global merge verification still fails with **1,247 name conflicts and 3,287
fingerprint issues**. [Freshness](merge-freshness.json) fails with 6,320 tracked
versus 6,498 fresh files: 3,720 only tracked, 3,898 only fresh, 1,684 changed and
916 unchanged. Regeneration was temporary only; no tracked merged output or
page was edited.

All five [full citation checks](reference-validation.json) fail. The installed
matcher passes 14 of 65 evidence entries and fails 51 PDF entries (44 archive,
seven current-DSMZ). Inspection of the installed URL fetcher and its caches
confirms it stores decoded PDF bytes as text without PDF extraction. It also
uses URLs as fallback titles, producing eleven title mismatches, including the
parent's existing API-title mismatch. Valid source titles and exact PDF snippets
were not replaced to force a pass. The captured PDF bytes, extracted text,
additional excerpts, DOI metadata and formulation scope are independently
verified by the source check, page inspection and full-record audit. This is
not an automated reference-validation pass.

Checks are journaled in [validation.json](validation.json) and
[final-checks-recheck.json](final-checks-recheck.json). The initial final-check
journal retains the report-label helper's subsequently corrected lint finding.
The working runtime is the partial locked
Python 3.13 environment, not full CI. Inspect terminal flags and exit codes;
scientific limitations and failing publication gates remain open.

## Remaining Work

Exact historical KOMODO source-version attribution is unresolved. Batch-mass
and normality units, unspecified percent bases, stock doses, new ingredient
ontology mappings and inherited aerobic notes remain explicitly limited.
The three inherited 673/266 records from the preceding handoff remain unchanged
and still require conflict-aware curation. The next uncovered KOMODO cohort is
offset 2500. Existing report presence is not scientific completion.

The [cumulative audit](../20261007-diff-audit-after-komodo670-versions.json)
verifies 5,024 edited paths and 29,722 new evidence entries. [Coverage](../20261007-followup-coverage-after-komodo670-versions.json)
remains 10,610 of 15,910 normalized paths, with 5,300 outside these reports.
No generated merged records or pages are hand-edited. No commit, push, PR,
merge, branch deletion or publication is claimed for this batch.
