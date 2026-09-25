# YAML Record Review: GYP-Sodium Acetate-Mineral Salts Broth

- Repository: CultureMech
- Record: `data/merge_yaml/merged/gyp_sodium_acetate_mineral_salts_broth__dba7d6ec.yaml`
- Started UTC: 2026-09-23T08:33:45Z
- Finished UTC: 2026-09-23T08:34:13Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:010009`, `gyp_sodium_acetate_mineral_salts_broth`, imported from Togo `M60` / `JCM_M68`.

## Validation

- LinkML validation: passed.
- Strict validation: passed with 0 ERROR rows in `/private/tmp/gyp_sodium_acetate_mineral_salts_broth_dba7d6ec.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked: the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The source identity is coherent: Togo `M60` wraps JCM `GRMD=68` and names the same `GYP-Sodium Acetate-Mineral Salts Broth`. Exact ignored-file-inclusive search found the direct JCM/MediaDive `J68` parent and the Togo `M1618` NBRC import as two same-formula records that remain split from this Togo/JCM import.

Most simple ingredients are grounded. Yeast extract and Bacto peptone are ungrounded complex components.

## Evidence

The Togo `M60` payload and live JCM 68 page list 1 L Distilled water, 0.2 g MgSO4 x 7 H2O, 10 mg NaCl, 10 mg FeSO4 x 7 H2O, 10 g Sodium acetate, 10 mg MnSO4 x H2O, 10 g Glucose, 10 g Yeast extract, and 10 g Bacto peptone, with pH 6.8.

The generated record preserves the 10 g ingredients and 0.2 g MgSO4 x 7 H2O, but it inflates each 10 mg mineral row to 10 `G_PER_L`, drops pH 6.8, and emits the 1 L water row as 1 `G_PER_L`.

## Completeness

The ingredient names are present, but the record is incomplete for units, pH, and duplicate source grouping. It is off by 1000-fold for three mineral salts.

## Findings

- NaCl, FeSO4 x 7 H2O, and MnSO4 x H2O are misunitized. Each is 10 mg in Togo `M60` and JCM 68, but each is stored as 10 `G_PER_L`.
- The generated record is missing pH 6.8 from Togo and JCM.
- Distilled water is misunitized as `1 G_PER_L` even though Togo records a 1 L solvent volume.
- Equivalent direct JCM/MediaDive `J68` and Togo `M1618` source records are not grouped with this Togo `M60` record.
- Yeast extract and Bacto peptone remain ungrounded. These are complex ingredients, but they should be checked against available mappings.

## Recommended Edits

- Convert source milligram values to 0.01 `G_PER_L` for NaCl, FeSO4 x 7 H2O, and MnSO4 x H2O.
- Preserve pH 6.8.
- Correct Togo liter-water handling so 1 L Distilled water is not emitted as `1 G_PER_L`.
- Group Togo `M60` with the direct JCM/MediaDive `J68` record after unit repair, and reconcile the equivalent NBRC `M1618` record as well.
- Attempt complex-component groundings for Yeast extract and Bacto peptone.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validators after recuration.
- Recompare the regenerated record against the live JCM 68 page to verify the three 10 mg rows.

## Additional Notes

None found.
