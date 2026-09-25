# YAML Record Review: methanosarcina_subterranea_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanosarcina_subterranea_medium__93c68d34.yaml
- Started UTC: 2026-09-24T05:06:09Z
- Finished UTC: 2026-09-24T05:06:09Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:007713` for TOGO medium `M1187`, "Methanosarcina Subterranea Medium", merged with TOGO medium `M223`, "Methanosarcina Medium".

## Validation

- LinkML open schema validation: Passed with "No issues found".
- Strict recipe validation: Passed; `/private/tmp/methanosarcina_subterranea_medium_93c68d34.strict.tsv` contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

- TOGO `M1187` correctly points to JCM GRMD 1110, "METHANOSARCINA SUBTERRANEA MEDIUM".
- The live JCM 1110 page defines the medium as JCM 230 supplemented with a final 6.0 g/L NaCl concentration.
- TOGO `M223` points to JCM GRMD 230, "METHANOSARCINA MEDIUM", whose live source has 2.25 g NaCl in the base formula.
- The merged record collapses those two distinct media into one fingerprint and keeps `M223` as a synonym even though the final NaCl target differs.

## Evidence

- JCM 230 lists KH2PO4, K2HPO4, NH4Cl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, 2.25 g NaCl, 2 mg FeSO4 x 7 H2O, yeast extract, Casitone, 10 ml trace vitamins from Medium 197, 1 ml FeCl2 solution from Medium 187, 1 ml trace element solution from Medium 187, NaHCO3, 10 ml methanol, L-Cysteine HCl H2O, Na2S x 9 H2O, 1 mg resazurin, and 980 ml distilled water.
- JCM 1110 changes only the NaCl endpoint, instructing use of Medium 230 supplemented with final 6.0 g/L NaCl.
- The generated `solutions` stubs correspond to TOGO/JCM cross-references, but their 10 ml, 1 ml, and 1 ml source additions are stored as `10 G_PER_L`, `1 G_PER_L`, and `1 G_PER_L` on empty `Unknown solution` records.
- The live JCM 230 page and both TOGO payloads include the same anaerobic boil, N2-CO2 cool-down, bicarbonate and methanol addition, serum-bottle dispensing, overnight standing, and separately autoclaved cysteine/sulfide-stock instructions. The generated record has no `preparation_steps`; an exact `rg --no-ignore --hidden` top-level-key check returned no matches.

## Completeness

- The high-salt JCM 1110 parent formula is mostly present.
- The lower-salt JCM 230 identity is incorrectly folded into this record as a synonym.
- JCM 230's cross-referenced trace vitamins, FeCl2 solution, and trace element solution are not linked to structured child records.
- Anaerobic preparation instructions are absent.

## Findings

1. Major - The merge collapsed a base recipe into its salt-supplemented derivative. JCM 1110/M1187 has final 6.0 g/L NaCl, while JCM 230/M223 has 2.25 g NaCl; keeping `TOGO_M223_Methanosarcina_Medium` in `merged_from` makes the record claim two non-identical source recipes are the same recipe.
2. Major - Source mg and ml rows were serialized as `G_PER_L`. The 2 mg FeSO4 x 7 H2O row became `2 G_PER_L`, the 1 mg resazurin row became `1 G_PER_L`, and the 10 ml methanol row became `10 G_PER_L`.
3. Major - The JCM cross-media stock additions were converted to empty gram-per-liter solutions. The 10 ml trace-vitamin addition from JCM 197 and the two 1 ml additions from JCM 187 should remain stock volumes with structured references, not `G_PER_L` stubs named `Unknown solution`.
4. Major - The executable preparation text was dropped. The sources explain which components are excluded before boiling, how to cool under 80:20 N2-CO2, when to add NaHCO3 and methanol, how to dispense under gas, when to stand overnight, and how to add separately autoclaved cysteine and sulfide stocks before inoculation.
5. Minor - Some source chemical labels need cleanup after import. `L--Cysteine-HCl-H2O` has a doubled hyphen, and several source hydrate names still carry punctuation artifacts in `preferred_term`.

## Recommended Edits

- Split JCM 230/TOGO M223 back out as a separate 2.25 g NaCl parent record and keep JCM 1110/TOGO M1187 as the 6.0 g/L NaCl derivative.
- Store FeSO4 and resazurin as milligram source amounts and methanol as a milliliter addition, or convert them with explicit unit-aware logic.
- Resolve the Medium 197 and Medium 187 stock references as linked solution additions with milliliter volumes.
- Restore the anaerobic boiling, gas cool-down, bottle dispensing, overnight standing, and reducing-stock addition instructions.
- Normalize displayed hydrate and cysteine labels to ASCII spellings such as `MgSO4 x 7 H2O` and `L-Cysteine HCl H2O`.

## Follow-up Checks

- Re-run focused schema, strict, reference, and term validators on the regenerated merged YAML.
- Confirm that JCM 230 and JCM 1110 no longer share a merge fingerprint.
- Confirm that the regenerated JCM 1110 record keeps exactly the JCM 230 recipe with only the documented final NaCl change.

## Additional Notes

The variable N2 and CO2 default ingredients are not the primary defect because the preparation text genuinely uses an 80:20 N2-CO2 atmosphere. They should be tied to that preparation context rather than left as independent variable ingredients.
