# YAML Record Review: pseudoalteromonas_spiralis_medium__c1a2f91f

- Repository: CultureMech
- Record: data/merge_yaml/merged/pseudoalteromonas_spiralis_medium__c1a2f91f.yaml
- Started UTC: 2026-09-24T21:58:00Z
- Finished UTC: 2026-09-24T21:58:00Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:000504`, the generated bacterial liquid `PSEUDOALTEROMONAS SPIRALIS MEDIUM` record merged from one direct MediaDive/DSMZ normalized input, `data/normalized_yaml/bacterial/pseudoalteromonas_spiralis_medium.yaml`.

## Validation

- LinkML validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `scripts/validate_strict.py` scanned one file and reported zero `ERROR` rows.
- Reference validation: Passed; `linkml-reference-validator` validated one file and reported zero reference checks.
- Term validation: Passed; `linkml-term-validator` exited 0.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The DSMZ/MediaDive identity is correct: MediaDive Medium 1072 is `PSEUDOALTEROMONAS SPIRALIS MEDIUM` at pH 7.8. An exact ignored YAML search for `mediadive.medium:1072`, `DSMZ_Medium1072`, `DSMZ, ID: 1072`, and `pseudoalteromonas_spiralis_medium` found this direct DSMZ branch and a generated KOMODO 1072 branch that points back to the same MediaDive medium.

## Evidence

MediaDive 1072 reports a main 1000 ml solution containing KH2PO4, MgSO4 x 7 H2O, NH4Cl, KCl, CaCl2 x 2 H2O, Na-acetate, yeast extract, Casamino acids, NaCl, 2 ml Trace element solution, 2 ml Vitamin solution, and 1000 ml distilled water. The Trace element solution is a separate 1000 ml stock with MnCl2 x 4 H2O, FeSO4 x 7 H2O, and water. The Vitamin solution is a separate 1000 ml stock with biotin, thiamine-HCl x 2 H2O, nicotinic acid, vitamin B12, and water.

## Completeness

The generated direct branch preserves the main dry-salt, acetate, and complex additions, but it omits main water and both 2 ml/L stock additions. It also flattens both stock recipes into final top-level ingredients at stock strength, so trace metals and vitamins are overrepresented in the final medium.

## Findings

- The 1000 ml distilled water row from the main recipe is absent.
- The 2 ml/L `Trace element solution` and 2 ml/L `Vitamin solution` additions are absent as stock additions.
- MnCl2 x 4 H2O and FeSO4 x 7 H2O are stored as final medium ingredients at 0.3 g/L and 0.003 g/L, but those are the concentrations of the trace-element stock.
- Biotin, thiamine-HCl x 2 H2O, nicotinic acid, and vitamin B12 are stored as final medium ingredients at vitamin-stock concentrations.
- The direct DSMZ branch is split from `PSEUDOALTEROMONAS_SPIRALIS_MEDIUM.yaml`, the KOMODO 1072 representation of the same MediaDive medium.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/pseudoalteromonas_spiralis_medium.yaml` by adding the 1000 ml water row and replacing the flattened trace and vitamin ingredients with 2 ml/L solution additions.
- Move MnCl2 x 4 H2O and FeSO4 x 7 H2O into a `Trace element solution` composition, and move biotin, thiamine-HCl x 2 H2O, nicotinic acid, and vitamin B12 into a `Vitamin solution` composition.
- Reconcile the KOMODO 1072 normalized record with the direct DSMZ record so regeneration emits one `mediadive.medium:1072` output.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merged record.
- Repeat exact ignored YAML searches for `mediadive.medium:1072` and `pseudoalteromonas_spiralis_medium` to verify that the DSMZ and KOMODO branches were reconciled.

## Additional Notes

None.
