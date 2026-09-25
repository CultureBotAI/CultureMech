# YAML Record Review: neutral_oligotrophic_haloarchaeal_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium__09168dc0.yaml
- Started UTC: 2026-09-24T17:09:56Z
- Finished UTC: 2026-09-24T17:11:09Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium__09168dc0.yaml` as a generated `MediaRecipe` for the direct JCM/MediaDive `J1138` import, `CultureMech:002311`, label `neutral_oligotrophic_haloarchaeal_medium`, category `archaea`, and physical state `LIQUID`.

The generated record was merged from `data/normalized_yaml/archaea/neutral_oligotrophic_haloarchaeal_medium.yaml`; it is derived and should be regenerated after normalized curation fixes.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium__09168dc0.yaml` | Passed; `No issues found`. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium__09168dc0.yaml --out /private/tmp/neutral_oligotrophic_haloarchaeal_medium__09168dc0.strict.tsv --workers 1 --quiet` | Passed; TSV had the header only, 1 line and 0 errors. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium__09168dc0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were available. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium__09168dc0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: `just validate-history` validates the standalone `history/` tree, not embedded `MediaRecipe.curation_history` entries inside a single merged YAML file. |

## Identity and Grounding

- The target denotes JCM/MediaDive `J1138`, Neutral Oligotrophic Haloarchaeal Medium, with pH 7.0.
- Live JCM GRMD 1138 was checked and returned `Nothing found`, so direct current JCM page text was unavailable.
- MediaDive REST for `J1138` resolves to one medium with a `Main sol. J1138` solution containing 767 ml MDS salt water, 0.25 g NH4Cl, 0.3 g K2HPO4, 0.05 g yeast extract, 0.25 g peptone, 1 g sodium pyruvate, and 233 ml distilled water. TOGO M1218 reports the same liquid formulation from `JCM_M1138`, and TOGO M1219 reports the same formulation plus 20 g/L agar for original ID `JCM_M1138-2`.
- A gitignore-independent hidden-file search for `J1138`, `J1139`, `GRMD=1138`, `GRMD=1139`, and `neutral_oligotrophic_haloarchaeal_medium` across `data/normalized_yaml` and `data/merge_yaml` found separate direct and TOGO owners for this medium, including `TOGO_M1218_Neutral_Oligotrophic_Haloarchaeal_Medium.yaml` and `TOGO_M1219_Neutral_Oligotrophic_Haloarchaeal_Medium.yaml`, plus their generated records.

## Evidence

The inspected MediaDive and TOGO provider records agree that the liquid J1138 medium should be made from a 767 ml aliquot of MDS salt water plus 233 ml distilled water and small NH4Cl, K2HPO4, yeast extract, peptone, and sodium pyruvate additions. MDS salt water is a separate solution that contains NaCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, KCl, and 1 M CaCl2 solution per liter, with its own instruction to adjust pH to 7.5 using 1 M Tris base.

The generated direct-JCM record does not preserve that boundary. It copies the full per-liter composition of MDS salt water into the final medium instead of using a 767 ml MDS salt water addition or scaling those salts by 0.767. It also adds the MDS salt water preparation step, pH 7.5 with Tris base, after the main-medium pH 7.0 preparation step, so following the record would change the final pH target.

## Completeness

- Consequential gap: MDS salt water is not represented as a 767 ml solution addition.
- Consequential error: MDS salt water salts are present at full stock strength in the final medium.
- Consequential duplicate gap: the direct JCM `J1138` record is separate from the TOGO M1218 liquid import for the same JCM source and separate from the related M1219 agar variant.
- Empty optional fields are not defects. The inspected MediaDive and TOGO records do not provide a target organism or incubation temperature.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | MDS salt water was flattened into final ingredients without applying the 767 ml/L dilution. | MediaDive `J1138` and TOGO M1218 list `MDS salt water` at 767 ml in a 1 L main solution. The generated record lists full MDS salt water stock concentrations, including 240 g/L NaCl, 30 g/L MgCl2 x 6 H2O, 35 g/L MgSO4 x 7 H2O, and 7 g/L KCl, directly in the final medium. | Recurate `data/normalized_yaml/archaea/neutral_oligotrophic_haloarchaeal_medium.yaml` to keep `MDS salt water` as a solution reference or scale the MDS salts to their 0.767 final fraction with provenance. |
| major | The record conflates MDS salt water preparation with final medium preparation. | The source main medium is adjusted to pH 7.0; the pH 7.5 with 1 M Tris base step belongs to the referenced MDS salt water solution, not to the final J1138 recipe. | Move the pH 7.5 Tris-base instruction to the MDS salt water solution owner and leave only the pH 7.0 final-medium instruction on J1138. |
| major | Same-source JCM 1138 imports are not reconciled. | Exact hidden-file search found direct `J1138`, TOGO M1218 liquid, and TOGO M1219 agar records for the JCM 1138 source family, with separate generated outputs and no explicit variant relationship among these active records. | Resolve `data/normalized_yaml/archaea/neutral_oligotrophic_haloarchaeal_medium.yaml`, `TOGO_M1218_Neutral_Oligotrophic_Haloarchaeal_Medium.yaml`, and `TOGO_M1219_Neutral_Oligotrophic_Haloarchaeal_Medium.yaml` into one source family with a liquid parent and agar variant. |

## Recommended Edits

1. Recurate the direct JCM `J1138` owner so MDS salt water remains a 767 ml/L referenced solution and its internal salts are not copied at full strength into the final medium.
2. Keep the final medium's pH at 7.0 and move the pH 7.5 Tris adjustment to the maintained MDS salt water solution recipe.
3. Link or merge the direct JCM liquid import with TOGO M1218, and model TOGO M1219 as the 20 g/L agar variant rather than as an unrelated active recipe.
4. Regenerate the merged YAML after the normalized records and relationships are corrected.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the repaired normalized records and regenerated merged outputs.
- Re-run a gitignore-independent hidden-file search for `J1138`, `JCM_M1138`, `JCM_M1138-2`, and `GRMD=1138` under `data/normalized_yaml` and `data/merge_yaml` to confirm the liquid and agar forms resolve to a single source family.
- Manually compare the regenerated J1138 record against MediaDive `J1138`, TOGO M1218, and TOGO M1219, and retry live JCM GRMD 1138 in case the retired page returns.

## Additional Notes

The inspected live JCM GRMD 1138 page returned no medium body at review time. MediaDive REST for `J1138` and the TOGO M1218/M1219 API records were still available and agreed on the main 767 ml MDS salt water formulation.
