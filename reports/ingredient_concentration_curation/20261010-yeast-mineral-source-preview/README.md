# Yeast Mineral Ingredient Source Preview

Historical preview. The [applied successor](../20261010-yeast-mineral-ingredients/README.md)
now records actual recipe edits and their validation. This folder remains
excluded from canonical coverage; its receipts describe the unchanged state
at preview time.

Read-only review of four exact normalized paths, MediaDB 397-400, and all
84 stored ingredient concentrations. No recipe has been changed and no evidence
entry has been added to YAML by this preview.

The [structured preview](claim-review-preview.json) pins complete original
records, source captures, source joins, per-field decisions, snippets, locators,
bibliographic metadata and identity candidates. Each [record report](records/)
has exactly one exact-path `- Record:` line and is explicitly marked preview.

## Primary Sources

- MediaDB 397 and 398 link to Verduyn et al. (1992), DOI
  `10.1002/yea.320080703`. The captured [primary PDF](https://repository.tudelft.nl/file/File_025a63db-3c03-4a9d-b18c-d37a795e6cad)
  was inspected at printed page 502, including its page image. It describes
  carbon-limited chemostat formulations with 10 g/L glucose or 7.5 g/L ethanol.
- MediaDB 399 and 400 link to Flikweert et al. (1996), DOI
  `10.1002/(SICI)1097-0061(19960315)12:3<247::AID-YEA911>3.0.CO;2-I`.
  The captured [primary PDF](https://repository.tudelft.nl/file/File_980a303e-e5c4-40e9-ae2c-d1efee438339?preview=1)
  was inspected at printed page 250, including both columns of the page image.
  The matching batch formulations contain initial 25 g/L glucose or 7.9 g/L
  ethanol; the same paper's lower chemostat feed amounts are different contexts.

Title-page images and PubMed establish article identity, authors and publication
year. DOI resolver attempts failed, but both repository PDFs were downloaded and
hash-pinned. Initial sandbox download failed DNS; the approved network download
succeeded. Failed web screenshot attempts were replaced by inspected local PDF
renders using an existing cached renderer, without changing the tested runtime.

The ingredient snippets are short manual page-image transcriptions. Line-wrap
hyphenation is joined and chemical subscripts/unit superscripts are flattened;
printed centered decimal points are preserved. The OCR text is not treated as
a faithful chemical-formula transcript. PDF, extracted-text and rendered-page
hashes are retained in the structured preview, not invented raw web captures.

## Proposed Decisions

- **56 amount replacements** use directly stated source units, not inferred
  mass/molar conversions. This includes acid-specific para-aminobenzoic acid
  at 0.2 mg/L in all four records, replacing the database's 0.1458 mM assertion
  and conjugate-base identity together.
- **26 mineral molarities remain unsupported** as final concentrations. The
  1996 paper specifies inputs per liter of demineralized water, while its
  vitamin doses explicitly refer to final concentrations. Do not transfer the
  1992 volume wording to these records.
- **Two molybdate claims remain conflicted**. The 1992 page prints
  `NaMoO4.2H2O`; the 1996 page prints `Na2MoO4.2H2O`. No missing sodium
  subscript is silently repaired and no molybdate replacement amount or exact
  hydrate identifier is approved for the 1992 pair.
- Acid/hydrate candidates are checked against ten official ChEBI entries and
  the pinned MIM resolver. MIM is not independently sufficient recipe evidence.
  The immutable index is unchanged; molybdate's exact candidate is restricted
  to the 1996 pair.
- Silicone antifoam is omitted from all four records. The 1992 source supports
  0.025 mL/L; the 1996 source supplies a 0.05 mL per liter water-input amount,
  not a verified final concentration.
- Generic filtration-only preparation conflicts with the sources' heat
  sterilization and later filter-sterilized vitamin addition. The ethanol
  parent/child wording that only ethanol differs also needs qualification.

These decisions are now represented in the preferred
[second YAML preview](mutation-preview-v2/plan.json), with four complete YAML
proposals and diffs. It proposes 56 amount replacements, two new quantified
antifoam slots, two unquantified antifoam nodes and 218 scoped evidence entries.
None of these proposed additions is included in applied cumulative totals.
The [first preview](mutation-preview/plan.json) remains as a superseded artifact;
the second has concise history, source-specific discovery metadata and explicit
carbon-dose excerpts for the ethanol relationship explanation.

The [precision correction receipt](preview-precision-corrections.json) records
ten proposed vitamin values and four held mineral input values corrected to
preserve the 1996 paper's printed trailing zeros. It pins the original and
revised source-preview hashes; it is not a normalized-record edit.

The [guard draft](guard-draft-v1/review_yeast_mineral_ingredients.py) now implements
default-dry-run application of only this exact source-pinned snapshot. It remains
outside the maintained scripts/tests pending completion of the preceding batch's
frozen fast-tier run. No application has been performed. The [issue ledger](issues.md)
identifies the remaining installation and application work.
No organism-medium association, role, permanent ID, category or new record is
proposed by this ingredient preview.

## Validation

All [eight baseline schema/strict commands](baseline.json) pass. Independent
HTML/SQL reparsing confirms every stored amount and each accession's source
link. The full SQL join for sources 137 and 115 identifies exactly these four
accessions; the exact tracked filename-family search agrees.

The [preview validation receipt](preview-validation.json) verifies all 15,910
normalized hashes unchanged, 84 claim rows and four excluded preview reports.
Canonical follow-up coverage remains **11,930 / 15,910**, leaving **3,980** paths
outside it. No post-edit, automatic reference-validation or goal-completion
claim is made.

All [eight proposed-record schema/strict checks](mutation-preview-v2/validation.json)
also pass. An [independent semantic audit](mutation-preview-v2/semantic-audit.json)
checks all 84 claim decisions against a separately transcribed amount table,
preserves the unresolved mineral and molybdate cases, and rejects forty altered
preview cases. Those cases test read-only semantic assertions, not an application
guard. The preview builder verifies all 15,910 normalized-record hashes unchanged.

The separate [guard-draft receipt](guard-draft-v1/validation.json) records
**68 passing tests**, lint, formatting and a real-schema dry run. Tests cover
source/record drift, rehashed plan forgeries, exact git paths, symlinks/hardlinks,
preserved history, independent change counts, repeat no-op, staging failures and
rollback after replacement failures. A concurrent edit encountered during
rollback is preserved and reported as partial application, never silently
overwritten or declared successful. This does not claim crash-atomic replacement
of a multi-file batch. All tests that apply changes use isolated temporary git
repositories; all 15,910 authoritative record hashes remain unchanged.
Installation, real application/readback and post-application retention remain
pending.
