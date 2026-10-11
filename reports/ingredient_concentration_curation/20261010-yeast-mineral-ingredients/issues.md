# Yeast Mineral Ingredient Review Decisions

## Addressed

- The separate [URL-only successor](../20261010-yeast-chebi-urls/README.md)
  replaces eighty live encoded-colon ChEBI references after the original
  checkpoint was sealed. Canonical pages return HTTP 200 with matching titles
  and formula snippets. Original history and scientific claims are unchanged.
- Stale preview-only wording in the four applied reports is corrected. Their
  original and successor hashes are both retained; coverage is not incremented.
- Applied the exact source-pinned second preview after the preceding Hajjaj
  run finished and its terminal checkpoint was sealed.
- Restored source mass concentrations and corrected para-aminobenzoic acid
  identity/dose together; retained source precision, including trailing zeros.
- Added omitted antifoam with distinct medium-volume versus water-input bases.
- Repaired supplied hydrate forms and preparation sequencing; qualified both
  ends of the ethanol variant relationship without merging or renumbering them.
- Guarded application rejects source/record drift, altered plans, exact-path
  mismatches, symlinks and hardlinks before writing. Tested staging/replacement
  failures roll back known writes. A conflicting concurrent edit is preserved
  and reported as partial application, not overwritten. No crash-atomic
  multi-file guarantee is asserted.
- Applied readback and repeat no-op pass. Four canonical reports have one exact
  record line each and cover 88 original/added ingredient claim rows. Historical
  previews stay excluded from canonical coverage.

## Unresolved

- Thirteen mineral quantities in each 1996 record are specified per liter of
  demineralized water, not explicit final-medium volume. The 26 stored molarities
  remain qualified database assertions.
- The 1992 paper prints `NaMoO4.2H2O`, unlike the 1996 disodium formula. The two
  original molarities remain unresolved and the unsupported anhydrous identifiers
  are removed, not silently replaced with a guessed two-sodium hydrate.
- The 1996 antifoam amount is a water-input dose, not a verified final-medium
  concentration. The two new nodes intentionally omit fixed concentrations.
- The papers name inositol without independently establishing the imported
  myo-specific identity. Existing specificity remains database-derived.
- Generic pH-adjustment placeholders and unrelated growth/role/classification
  claims are preserved but not newly certified by this ingredient review.
- Automatic reference, corpus/merge and runtime-retention checks must retain
  their actual outcomes. Schema validity and literal numeric substring matches
  do not establish scientific concentration support.

The separate migrated-UTEX-stock preview is not part of this applied batch.
No GitHub issue or PR mutation is claimed by this local ledger.
