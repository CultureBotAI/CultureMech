# YAML Record Review: halolamina_medium_nom_3

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halolamina_medium_nom_3.yaml`
- Started UTC: 2026-09-23T10:25:22Z
- Finished UTC: 2026-09-23T10:26:32Z
- Verdict: needs curation

## Target

Generated merged YAML for the direct MediaDive/DSMZ import of DSMZ medium 1528, `HALOLAMINA MEDIUM (NOM-3)`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:1528` and the DSMZ 1528 PDF.
- An ignored-file-inclusive exact search for `mediadive.medium:1528` and `DSMZ_Medium1528.pdf` found only the expected normalized DSMZ 1528 source and this generated merged record.
- The simple salts, short-chain organic sodium salts, and agar have reasonable ontology groundings.
- Yeast extract and Bacto peptone remain ungrounded, which is acceptable for undefined complex ingredients.

## Evidence

- The DSMZ 1528 PDF and the MediaDive 1528 REST payload list the same KCl, K2HPO4, CaCl2 x 2 H2O, NH4Cl, MgSO4 x 7 H2O, MgCl2 x 6 H2O, NaCl, Yeast extract, Bacto peptone, Sodium formate, Sodium lactate, Sodium acetate, Sodium pyruvate, Agar, and 1000 ml final-volume water rows.
- The generated concentrations match the source solute and agar masses.
- The generated `ph_value: 7.0` and `physical_state: SOLID_AGAR` match the DSMZ formula.

## Completeness

- Missing ingredient: the explicit 1000 ml distilled-water row was dropped.
- Missing qualifier: MediaDive and the DSMZ PDF identify Bacto peptone as `BD 211677`, but the generated `Bacto peptone` ingredient lost that product code.

## Findings

1. The generated recipe omits the source water row, losing the final 1000 ml volume as structured data.
2. The generated `Bacto peptone` row omits the `BD 211677` qualifier present in both DSMZ and MediaDive.

## Recommended Edits

- Add distilled water using the repository's curated final-volume representation.
- Restore the `BD 211677` qualifier on Bacto peptone.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Compare the regenerated record against the DSMZ 1528 PDF and MediaDive 1528 REST payload to verify all 15 source rows are represented.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
