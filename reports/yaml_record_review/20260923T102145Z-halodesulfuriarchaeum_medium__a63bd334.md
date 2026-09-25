# YAML Record Review: halodesulfuriarchaeum_medium__a63bd334

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halodesulfuriarchaeum_medium__a63bd334.yaml`
- Started UTC: 2026-09-23T10:21:45Z
- Finished UTC: 2026-09-23T10:22:33Z
- Verdict: needs curation

## Target

Generated merged YAML for TOGO `M1149`, a JCM medium 1080 import of `Halodesulfuriarchaeum Medium`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches TOGO `M1149`, original source `JCM_M1080`, and the JCM 1080 source URL.
- A gitignore-independent exact search for `TOGO:M1149`, `JCM_M1080`, and `GRMD=1080` found the expected normalized TOGO source, this merged record, and a separate direct MediaDive/JCM 1080 import.
- JCM 1080 is an amendment of JCM 1079 that replaces sodium pyruvate with final 50 mM sodium formate and supplements final 200 mg/L yeast extract.
- The basal salt CHEBI mappings are acceptable, but the generated solution placeholders lost the identities of the actual MgCl2, NaHCO3, selenite-tungstate, trace element, and sodium sulfide solutions.

## Evidence

- The JCM 1079 base medium lists 240 g NaCl, 2.5 g K2HPO4, 0.5 g NH4Cl, and 7.0 g HEPES brought to 1.0 L with distilled water.
- The TOGO M1149 API carries the same basal components, plus the JCM 1080 change from pyruvate to 50 mM sodium formate and 200 mg/L yeast extract.
- JCM adds 1 ml/L 1 M MgCl2, 1 ml/L selenite-tungstate, 1 ml/L trace element solution, 10 ml/L 1 M NaHCO3, approximately 1.0 g/L sulfur in the culture vessel, and 5 ml/L 5% Na2S x 9 H2O solution, with anaerobic argon handling.

## Completeness

- The basal 1.0 L distilled-water row is present as `1 G_PER_L`, which is a unit artifact rather than a final-volume solvent.
- Sulfur is absent even though JCM completes the medium in vessels containing approximately 1.0 g/L steam-sterilized sulfur.
- Five referenced additions were moved into `solutions` entries with empty `composition: []`, `name: Unknown solution`, and default mass-like `G_PER_L` amounts.
- All JCM comments describing autoclaving, separate filter sterilization, argon gas distribution, sulfur sterilization, and trace-solution pH were dropped from `preparation_steps`.

## Findings

1. The generated record is missing the sulfur addition required to complete the JCM 1079/1080 medium.
2. The post-autoclave solution additions are corrupt placeholders. `1 M MgCl2`, `1 M NaHCO3`, selenite-tungstate, trace element solution, and `5% Na2S x 9 H2O` should be volume-per-liter stock additions, but the generated record has empty solution records with default `G_PER_L` concentrations.
3. Sodium formate is a `VARIABLE` ingredient. The source requires final 50 mM sodium formate as the JCM 1080 replacement for sodium pyruvate.
4. Distilled water is encoded as `1 G_PER_L` instead of the 1.0 L final basal volume.
5. The generated record has no preparation steps, so it omits autoclaving of the basal medium, aseptic anaerobic distribution under argon, sulfur sterilization, and the instruction that added stocks are autoclaved or filter-sterilized separately.

## Recommended Edits

- Restore JCM 1080 as a curated derivative of JCM 1079 with sodium pyruvate replaced by final 50 mM sodium formate and final 200 mg/L yeast extract retained.
- Convert 1 ml/L MgCl2, 1 ml/L selenite-tungstate, 1 ml/L trace element solution, 10 ml/L NaHCO3, and 5 ml/L Na2S x 9 H2O into structured stock additions instead of empty solution placeholders.
- Add approximately 1.0 g/L steam-sterilized sulfur as a required vessel component.
- Represent distilled water as a final-volume solvent, not as `1 G_PER_L`.
- Recreate the JCM preparation instructions for autoclaving, sterile stock handling, argon distribution, sulfur sterilization, and trace-solution pH.
- Reconcile this TOGO record with the direct JCM 1080 record without copying the existing direct record's inflated stock concentrations.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Compare the curated record against both JCM 1080 and the referenced JCM 1079 base page.
- Verify that no default `Unknown solution` stubs remain after regeneration.

## Additional Notes

- Empty optional fields were not treated as defects; empty migrated solution compositions were treated as evidence of failed curation because they stand in for required source additions.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
