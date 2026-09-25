# YAML Record Review: GYP-Sodium Acetate-Mineral Salts Broth

- Repository: CultureMech
- Record: `data/merge_yaml/merged/gyp_sodium_acetate_mineral_salts_broth.yaml`
- Started UTC: 2026-09-23T08:29:59Z
- Finished UTC: 2026-09-23T08:31:25Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008172`, `gyp_sodium_acetate_mineral_salts_broth`, imported from Togo `M1618` / `NBRC_M818`.

## Validation

- LinkML validation: passed.
- Strict validation: passed with 0 ERROR rows in `/private/tmp/gyp_sodium_acetate_mineral_salts_broth.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked: the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The canonical generated identity is Togo `M1618` / `NBRC_M818`. Exact ignored-file-inclusive search in `data/normalized_yaml/bacterial` and `data/merge_yaml/merged` also found a direct JCM Medium 68 parent and a Togo `M60` parent that describe the same GYP-Sodium Acetate-Mineral Salts Broth formula with pH 6.8. Those JCM-derived records should be reconciled with this NBRC import.

Glucose, MgSO4 x 7 H2O, sodium acetate, and water are grounded. MnSO4 x H2O is ungrounded in the `M1618` record, and Bacto Yeast Extract and Bacto Peptone are ungrounded complex components.

## Evidence

The Togo `M1618` payload lists 1 L Distilled water, 0.2 g MgSO4 x 7 H2O, 10 mg NaCl, 10 mg FeSO4 x 7 H2O, 10 g Sodium acetate, 10 mg MnSO4 x H2O, 10 g Glucose, 10 g Bacto Yeast Extract, and 10 g Bacto Peptone. It also records `ph: "6.8"`. The live JCM 68 page carries the same formula and explicitly lists the Mn, Fe, and NaCl quantities as 10 mg.

The generated record preserves the 10 g ingredients and 0.2 g MgSO4 x 7 H2O, but it inflates each 10 mg mineral row to 10 `G_PER_L`, drops pH 6.8, and emits the 1 L water row as 1 `G_PER_L`.

## Completeness

The ingredient names are present, but the record is incomplete for units, pH, and duplicate source grouping. It is off by 1000-fold for three mineral salts.

## Findings

- NaCl, FeSO4 x 7 H2O, and MnSO4 x H2O are misunitized. Each is 10 mg in Togo `M1618` and JCM 68, but each is stored as 10 `G_PER_L`.
- The generated record is missing pH 6.8 from Togo.
- Distilled water is misunitized as `1 G_PER_L` even though Togo records a 1 L solvent volume.
- Equivalent JCM Medium 68 and Togo `M60` source records are not grouped with this NBRC `M1618` record.
- MnSO4 x H2O is ungrounded in the `M1618` import.
- Bacto Yeast Extract and Bacto Peptone remain ungrounded. These are complex ingredients, but they should be checked against available mappings.

## Recommended Edits

- Convert source milligram values to 0.01 `G_PER_L` for NaCl, FeSO4 x 7 H2O, and MnSO4 x H2O.
- Preserve pH 6.8.
- Correct Togo liter-water handling so 1 L Distilled water is not emitted as `1 G_PER_L`.
- Group the NBRC `M1618`, JCM `M60`, and direct JCM/MediaDive `J68` records as equivalent sources after unit repair.
- Ground MnSO4 x H2O where possible and attempt complex-component groundings for Bacto Yeast Extract and Bacto Peptone.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validators after recuration.
- Recompare regenerated NBRC `M1618`, Togo `M60`, and direct JCM 68 records against the JCM 68 page to verify the three 10 mg rows.

## Additional Notes

None found.
