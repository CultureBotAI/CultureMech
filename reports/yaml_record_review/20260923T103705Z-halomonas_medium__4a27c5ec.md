# YAML Record Review: halomonas_medium__4a27c5ec

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halomonas_medium__4a27c5ec.yaml`
- Started UTC: 2026-09-23T10:37:05Z
- Finished UTC: 2026-09-23T10:37:49Z
- Verdict: needs curation

## Target

Generated merged YAML for KOMODO medium 276, a KOMODO copy of DSMZ medium 276 `HALOMONAS MEDIUM`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches KOMODO `komodo.medium:276`, which declares DSMZ Medium 276 provenance.
- A gitignore-independent exact search for `komodo.medium:276`, `mediadive.medium:276`, and the DSMZ 276 PDF found this KOMODO record, the direct DSMZ 276 parent, and a KOMODO DSM-specific variant.
- The salts and agar are grounded appropriately.
- The generated variable `KOH` pH-adjustment ingredient is not supported by DSMZ 276, which adjusts pH with NaOH.

## Evidence

- DSMZ 276 lists 80 g NaCl, 7.5 g Casamino acids with vitamins, 5 g Proteose peptone no. 3, 1 g Yeast extract, 3 g Na3-citrate, 20 g MgSO4 x 7 H2O, 0.5 g K2HPO4, 0.05 g Fe(NH4)2(SO4)2 x 6 H2O, 15 g Agar if necessary, and 1000 ml Distilled water.
- DSMZ and MediaDive both state that pH is adjusted to 7.5 with NaOH before autoclaving.
- The direct DSMZ normalized record keeps that `ADJUST_PH` preparation step; the KOMODO copy does not.

## Completeness

- Missing ingredient: distilled water is absent from the generated KOMODO record.
- Missing preparation: the pH-adjustment step before autoclaving was dropped.
- Missing source qualifier: Casamino acids lost the `with vitamins` source qualifier.

## Findings

1. The generated record has a spurious `KOH` variable ingredient derived from a `pH buffer: KOH` note, but the DSMZ source says to adjust pH to 7.5 with NaOH.
2. The DSMZ pH-adjustment step is absent from `preparation_steps`, so the bad KOH row is the only structured pH adjustment left in the KOMODO copy.
3. The recipe omits the 1000 ml distilled-water row.
4. The Casamino acids row lost the `with vitamins` qualifier present in the DSMZ source.

## Recommended Edits

- Remove the unsupported variable `KOH` ingredient.
- Restore the pH 7.5 NaOH adjustment step from DSMZ 276.
- Add distilled water with the correct final-volume representation.
- Restore the `with vitamins` qualifier on Casamino acids.
- Merge or link this KOMODO copy as a source duplicate of the direct DSMZ 276 record only after the preparation and ingredient rows match.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Verify that `komodo.medium:276` and `mediadive.medium:276` reconcile to the same DSMZ 276 formula without a KOH ingredient.
- Re-run exact ignored-file-inclusive searches for `komodo.medium:276` and `mediadive.medium:276` after regeneration.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
