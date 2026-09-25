# YAML Record Review: peptone_succinate_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/peptone_succinate_agar.yaml
- Started UTC: 2026-09-24T20:28:18Z
- Finished UTC: 2026-09-24T20:28:18Z
- Verdict: pass with minor issues

## Target

Generated bacterial MediaRecipe `CultureMech:006230`, `peptone_succinate_agar`, merged from `data/normalized_yaml/bacterial/KOMODO_653_Peptone-SUCCINATE_AGAR.yaml` and `data/normalized_yaml/bacterial/peptone_succinate_agar.yaml`.

The record represents KOMODO medium 653 as a source duplicate of DSMZ / MediaDive medium 653, PEPTONE-SUCCINATE AGAR. The generated recipe has 1 g/L ammonium sulfate, 1 g/L MgSO4 x 7 H2O, 0.002 g/L MnSO4 x H2O, 0.002 g/L FeCl3 x 6 H2O, 1.68 g/L succinic acid, 5 g/L peptone, and 1.5 g/L agar, with pH 7.0.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/peptone_succinate_agar.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The duplicate relationship is sound. The KOMODO owner explicitly cites DSMZ Medium 653 / `mediadive.medium:653`, the direct MediaDive owner is DSMZ medium 653, and the two maintained owners have matching local ingredient and concentration signatures.

An exact ignored-inclusive search found only these two maintained source owners and their one generated merge for `komodo.medium:653`, `mediadive.medium:653`, `DSMZ_Medium653`, and the two relevant CultureMech IDs.

## Evidence

MediaDive medium 653 supports the DSMZ source identity, pH 7.0, the two 2 mg trace salts normalized to 0.002 g/L, 1.68 g/L succinic acid, 5 g/L peptone, 1.5 g/L agar, and a 1000 ml distilled water row.

The linked DSMZ medium 653 PDF agrees on 1 g sulfate salt, 1 g MgSO4 x 7 H2O, 2 mg MnSO4 x H2O, 2 mg FeCl3 x 6 H2O, 1.68 g succinic acid, 5 g peptone, 1.50 g agar, 1000 ml distilled water, and pH adjustment to 7.0.

The ingredient grounding is appropriate. Ammonium sulfate, magnesium sulfate heptahydrate, manganese(II) sulfate monohydrate, iron trichloride hexahydrate, succinic acid, and agar all have chemically specific CHEBI terms, while peptone remains ungrounded as an undefined component.

## Completeness

The merge preserves both source owners, the non-water ingredients, pH 7.0, and the expected source-duplicate relationship.

Both maintained inputs omit the 1000 ml distilled water row, and the generated merge uses the KOMODO owner as canonical, so it drops the direct DSMZ owner's `Adjust pH to 7.0` preparation step even though the scalar `ph_value` is present.

## Findings

1. Minor issue: both maintained owners and the generated record omit the 1000 ml `Distilled water` row from DSMZ / MediaDive medium 653.
2. Minor issue: the generated merge drops the direct DSMZ owner's `Adjust pH to 7.0` preparation step; `ph_value: 7.0` is still preserved.

## Recommended Edits

1. Add the 1000 ml distilled water row to both maintained owners.
2. Preserve the DSMZ pH-adjustment preparation step when regenerating the KOMODO / DSMZ source-duplicate merge.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owners and regenerated merged record.
2. Repeat an exact ignored-inclusive search for `komodo.medium:653`, `mediadive.medium:653`, `DSMZ_Medium653`, and the CultureMech IDs to confirm no additional duplicate medium 653 owner appears.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `komodo.medium:653`, `mediadive.medium:653`, `DSMZ Medium: 653`, `DSMZ_Medium653`, `CultureMech:006230`, and `CultureMech:001791`.
