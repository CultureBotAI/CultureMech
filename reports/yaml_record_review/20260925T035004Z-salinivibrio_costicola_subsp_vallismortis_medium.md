# YAML Record Review: salinivibrio_costicola_subsp_vallismortis_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/salinivibrio_costicola_subsp_vallismortis_medium.yaml
- Started UTC: 2026-09-25T03:50:04Z
- Finished UTC: 2026-09-25T03:50:04Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:006078`, `salinivibrio_costicola_subsp_vallismortis_medium`, from `data/merge_yaml/merged/salinivibrio_costicola_subsp_vallismortis_medium.yaml`.

The generated record merges KOMODO Medium 597 with its DSMZ/MediaDive 597 source duplicate for `SALINIVIBRIO COSTICOLA SUBSP. VALLISMORTIS MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The KOMODO 597 to DSMZ 597 merge is a true source-duplicate merge: the KOMODO record states DSMZ Medium 597 provenance and the normalized KOMODO file was populated from DSMZ Medium 597.

The generated record kept that identity but inherited normalized DSMZ ingredient rows in which the Modified Wolin's mineral solution II stock had already been flattened into the parent medium.

## Evidence

DSMZ Medium 597 lists a main recipe with 1 g (NH4)Cl, 25 g NaCl, 7 g MgCl2 x 6 H2O, 9.6 g MgSO4 x 7 H2O, 0.5 g CaCl2 x 2 H2O, 3.8 g KCl, 0.4 g K2HPO4 x 3 H2O, 1 g yeast extract, 5 g glucose, 10 ml Modified Wolin's mineral solution II, and 1000 ml distilled water.

The DSMZ source says the final pH is 7.0 and 3 g/L NaHCO3 is added from a filter-sterilized stock solution after the medium has cooled.

Modified Wolin's mineral solution II is a 1 L stock containing nitrilotriacetic acid, MgSO4 x 7 H2O, MnSO4 x H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2 x 12 H2O, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, and distilled water; its pH procedure starts by dissolving nitrilotriacetic acid and adjusting to pH 6.5 with KOH, then adds minerals and adjusts final pH to 7.0 with KOH.

## Completeness

The main Salinivibrio salts, yeast extract, and glucose are present, and the KOMODO/DSMZ duplicate relationship is retained.

The main 1000 ml distilled-water row, the 3 g/L NaHCO3 addition, and all DSMZ preparation steps are absent from the generated KOMODO-canonical record.

The Modified Wolin's mineral solution II contents are present only as direct parent-medium ingredient rows at stock concentrations.

## Findings

The normalized source and generated record flatten a 10 ml/L Modified Wolin's mineral solution II aliquot into the parent medium. Most stock rows are therefore 100x too high for the final medium.

Three Modified Wolin's mineral rows were additionally summed with parent rows: NaCl became 26 g/L instead of 25 g/L plus a 10 ml/L stock aliquot, MgSO4 x 7 H2O became 12.6 g/L instead of 9.6 g/L plus a stock aliquot, and CaCl2 x 2 H2O became 0.6 g/L instead of 0.5 g/L plus a stock aliquot.

The 3 g/L NaHCO3 filter-sterilized addition from DSMZ 597 is missing entirely in the generated KOMODO-canonical record.

The DSMZ pH and stock-preparation instructions exist in the direct DSMZ normalized parent but were lost when the KOMODO source duplicate became canonical in the generated merge.

`NiCl2 x 6 H2O` is grounded to `CHEBI:34887` / `nickel dichloride`, which does not capture the hexahydrate used in Modified Wolin's mineral solution II.

## Recommended Edits

Repair the normalized DSMZ 597 record so Modified Wolin's mineral solution II remains a distinct 1 L stock with a 10 ml/L parent aliquot.

Preserve the 3 g/L NaHCO3 post-cooling filter-sterilized addition in both DSMZ and KOMODO duplicate records before regenerating the merge layer.

Keep the DSMZ preparation steps when merging KOMODO 597 into DSMZ 597; the canonical generated record should not be a less complete KOMODO copy when the richer source is available.

Reground `NiCl2 x 6 H2O` to a hydrate-specific CHEBI term if one is available in the local CHEBI snapshot; otherwise keep the hydrated source label without the anhydrous CHEBI mapping.

## Follow-up Checks

After regeneration, confirm the parent Salinivibrio record has a main recipe with a 10 ml/L Modified Wolin's mineral solution II aliquot, no stock-strength trace metals as direct parent rows, and an explicit 3 g/L NaHCO3 addition.

Validate both the normalized DSMZ file and the KOMODO source-duplicate file before regenerating `data/merge_yaml/merged/salinivibrio_costicola_subsp_vallismortis_medium.yaml`.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
