# YAML Record Review: pseudoclostridium_medium__bbe4204c

- Repository: CultureMech
- Record: data/merge_yaml/merged/pseudoclostridium_medium__bbe4204c.yaml
- Started UTC: 2026-09-24T21:58:45Z
- Finished UTC: 2026-09-24T21:58:45Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:001630`, the generated bacterial liquid `PSEUDOCLOSTRIDIUM MEDIUM` record grounded to DSMZ/MediaDive Medium 502 and merged from `pseudoclostridium_medium` plus the KOMODO synonym `clostridium_thermosuccinogenes_medium`.

## Validation

- LinkML validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `scripts/validate_strict.py` scanned one file and reported zero `ERROR` rows.
- Reference validation: Passed; `linkml-reference-validator` validated one file and reported zero reference checks.
- Term validation: Passed; `linkml-term-validator` exited 0.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The DSMZ/KOMODO merge identity is plausible: both normalized sources point to DSMZ/MediaDive Medium 502, `PSEUDOCLOSTRIDIUM MEDIUM`. An exact ignored YAML search for `mediadive.medium:502`, `DSMZ_Medium502`, `DSMZ, ID: 502`, and `pseudoclostridium_medium` found the merged DSMZ/KOMODO output and a separate TOGO `M2755` branch that references the same DSMZ Medium 502 PDF.

## Evidence

MediaDive 502 reports a 1002 ml main solution with basal salts, 1 ml Trace element solution SL-10, inulin, 0.5 ml 0.1% w/v sodium resazurin, yeast extract, Casamino acids, Na2CO3, Na2HPO4, 1 ml Wolin's vitamin solution (10x), Na2S x 9 H2O, and 1000 ml distilled water. It defines SL-10 as a 1000 ml stock with 10 ml 25% HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 990 ml water. It defines Wolin's 10x vitamin stock as a 1000 ml solution containing biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium D-(+)-pantothenate, vitamin B12, p-Aminobenzoic acid, (DL)-alpha-Lipoic acid, and water.

## Completeness

The generated record preserves most main-medium masses after MediaDive volume scaling and keeps the source pH 7.0, but it is incomplete because it omits the main and stock water rows, drops the 1 ml/L SL-10 and 1 ml/L Wolin's vitamin stock additions, and stores both stock recipes as final top-level ingredients at stock strength.

## Findings

- The 1000 ml main distilled water row, the 990 ml SL-10 water row, and the 1000 ml vitamin-stock water row are all absent.
- The 1 ml/L `Trace element solution SL-10` and 1 ml/L `Wolin's vitamin solution (10x)` additions are absent as stock additions.
- HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O are SL-10 stock components but appear as final-medium g/L ingredients.
- Biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium D-(+)-pantothenate, vitamin B12, p-Aminobenzoic acid, and (DL)-alpha-Lipoic acid are Wolin 10x vitamin-stock components but appear as final-medium g/L ingredients.
- The merged DSMZ/KOMODO output is still split from the generated TOGO `M2755` output for the same DSMZ 502 source.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/pseudoclostridium_medium.yaml` and the KOMODO synonym so SL-10 and Wolin 10x are modeled as 1 ml/L additions with nested compositions, not flattened top-level ingredients.
- Preserve the main and stock water rows, and represent the 25% HCl aliquot in SL-10 as a liquid stock component instead of pure `HCl`.
- Reconcile `data/normalized_yaml/bacterial/TOGO_M2755_Pseudoclostridium_Medium.yaml` with the repaired DSMZ/KOMODO branch so Medium 502 regenerates as one CultureMech output.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merged record.
- Repeat exact ignored YAML searches for `mediadive.medium:502`, `DSMZ_Medium502`, and `pseudoclostridium_medium` to verify that the DSMZ, KOMODO, and TOGO representations were reconciled.

## Additional Notes

None.
