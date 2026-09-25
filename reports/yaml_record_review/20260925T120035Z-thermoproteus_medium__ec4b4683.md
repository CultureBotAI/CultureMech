# YAML Record Review: thermoproteus_medium__ec4b4683

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoproteus_medium__ec4b4683.yaml
- Started UTC: 2026-09-25T12:00:35Z
- Finished UTC: 2026-09-25T12:00:35Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:001275`, `thermoproteus_medium`, generated from DSMZ Medium 185 / MediaDive `mediadive.medium:185`.

## Validation

- LinkML schema: Passed with `linkml-validate`; no issues found.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermoproteus_medium__ec4b4683.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The record is correctly grounded to DSMZ Medium 185, "THERMOPROTEUS MEDIUM". DSMZ 185 also appears in a TOGO M2676 duplicate and a KOMODO/DSMZ 185 generated record, but this direct MediaDive record is the cleanest anchor for the DSMZ recipe.

## Evidence

- DSMZ 185 lists (NH4)2SO4 0.264 g, FeSO4 x 7 H2O 0.556 g, MgSO4 x 7 H2O 0.492 g, CaSO4 x 2 H2O 0.344 g, KH2PO4 0.014 g, resazurin 1 mg, 1 ml Trace elements solution, yeast extract 0.200 g, soluble starch 5.000 g, powdered sulfur 10.000 g, Na2S x 9 H2O 0.500 g, and 1000 ml distilled water.
- DSMZ 185 defines a 1 L Trace elements solution with NaF, MnCl2 x 4 H2O, Na2B4O7 x 10 H2O, ZnSO4 x 7 H2O, CuCl2 x 2 H2O, Na2MoO4 x 2 H2O, CoSO4 x 7 H2O, and water.
- DSMZ 185 prepares the medium without starch, sodium sulfide, and sulfur under N2, adjusts pH to 5.5 with H2SO4 before sterilization, tyndallises sulfur-containing tubes, and adds starch and sodium sulfide before use.

## Completeness

The direct DSMZ import correctly converts the milligram main and trace rows. It still omits both distilled-water rows and flattens the 1 ml Trace elements stock into direct top-level ingredients at full 1 L stock strength.

## Findings

- The main 1000 ml distilled-water row and Trace elements 1000 ml distilled-water row are absent.
- The Trace elements stock is flattened; NaF, MnCl2 x 4 H2O, Na2B4O7 x 10 H2O, ZnSO4 x 7 H2O, CuCl2 x 2 H2O, Na2MoO4 x 2 H2O, and CoSO4 x 7 H2O are each 1000-fold too high if read as final concentrations.
- Soluble starch loses the "soluble" attribute by normalizing to `Starch`.
- `Sulfur` is grounded to CHEBI:26833, `sulfur atom`, which is less specific than powdered elemental sulfur.

## Recommended Edits

- Restore the Trace elements stock and its 1 ml/L addition.
- Add both distilled-water rows under the right solution scopes.
- Preserve `soluble` and `powdered` source attributes for starch and sulfur.
- Reconcile this repaired direct import with the TOGO M2676 and KOMODO/DSMZ 185 duplicates.

## Follow-up Checks

- Confirm whether starch and sodium sulfide should remain final ingredient rows with delayed-addition preparation semantics, or be moved to stock/addition structures.
- Review sulfur modeling across Thermoproteus and Thermoplasma records for consistent solid-phase handling.

## Additional Notes

No target-organism evidence was reviewed. The exact source search included ignored and hidden files and found the direct DSMZ 185 import, its TOGO M2676 duplicate, and a KOMODO/DSMZ 185 generated record.
