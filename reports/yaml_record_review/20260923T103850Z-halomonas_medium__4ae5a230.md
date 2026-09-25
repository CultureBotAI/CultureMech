# YAML Record Review: halomonas_medium__4ae5a230

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halomonas_medium__4ae5a230.yaml`
- Started UTC: 2026-09-23T10:38:50Z
- Finished UTC: 2026-09-23T10:39:21Z
- Verdict: needs curation

## Target

Generated merged YAML for direct MediaDive/DSMZ medium 276, `HALOMONAS MEDIUM`, merged with the KOMODO DSM 11845 copy.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:276` and the DSMZ 276 PDF.
- An ignored-file-inclusive exact search for `mediadive.medium:276`, `komodo.medium:276`, and `DSMZ_Medium276.pdf` found the direct DSMZ record, the KOMODO 276 copy, and a KOMODO DSM 11845 copy.
- The KOMODO DSM 11845 copy has the same ingredient signature as DSMZ 276 and is plausibly a source duplicate after preparation is reconciled.
- The source salt and agar groundings are appropriate.

## Evidence

- MediaDive 276 lists the same 1 L formula as the generated record plus an explicit 1000 ml Distilled water row.
- MediaDive carries `attribute: with vitamins` on Casamino acids.
- DSMZ 276 states that the pH should be adjusted to 7.5 with NaOH before autoclaving.

## Completeness

- Missing ingredient: the explicit 1000 ml distilled-water row was dropped.
- Missing qualifier: Casamino acids lost the `with vitamins` qualifier.
- Missing post-adjustment sterilization semantics: the record captures pH adjustment before autoclaving but does not separately represent autoclaving.

## Findings

1. The generated DSMZ 276 record omits the 1000 ml distilled-water row.
2. Casamino acids lost the `with vitamins` source qualifier.
3. Agar is modelled as an ingredient on a `SOLID_AGAR` recipe but still carries the source condition `if necessary`, so the base liquid and solid agar states are not cleanly separated.

## Recommended Edits

- Add distilled water with the correct 1000 ml final-volume representation.
- Restore `with vitamins` on Casamino acids.
- Split the conditional 15 g agar row into an explicit solid variant or otherwise scope its `if necessary` condition without forcing all DSMZ 276 records to be `SOLID_AGAR`.
- Preserve pH adjustment and autoclaving as separate preparation semantics.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Verify that the direct DSMZ 276, KOMODO 276, and KOMODO 276_11845 copies reconcile without the spurious KOH row from the KOMODO 276 import.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:276`, `komodo.medium:276`, and `komodo.medium:276_11845` after regeneration.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
