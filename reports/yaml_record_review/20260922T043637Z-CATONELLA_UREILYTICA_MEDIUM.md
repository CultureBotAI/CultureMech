# YAML Record Review: Catonella Ureilytica Medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/CATONELLA_UREILYTICA_MEDIUM.yaml`
- Started UTC: 2026-09-22T04:33:25Z
- Finished UTC: 2026-09-22T04:36:37Z
- Verdict: needs curation

## Target

`CATONELLA_UREILYTICA_MEDIUM.yaml` is the generated single-source `MediaRecipe` for `CultureMech:009878`, the TOGO M490 import of JCM 489 `Catonella Ureilytica Medium`.

The generated record was merged only from `data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml` on fingerprint `c7a2eae23f08d6307ca7602e6949a30e9d7d175f549d6f42daba71f0890ca276`.

## Validation

- LinkML validation against `MediaRecipe`: pass.
- `scripts/validate_strict.py`: pass with 0 strict errors.
- `linkml-reference-validator`: pass; 1 file checked, 0 reference checks.
- `linkml-term-validator`: pass.
- Embedded `curation_history`: not checked; the available `just validate-history` target validates standalone files under `history/`, not embedded history events inside merged YAML.

## Identity and Grounding

The source identity is correct: TOGO M490 points to JCM_M489 and the live JCM 489 `CATONELLA UREILYTICA MEDIUM` page. The generated record is also correctly categorized as a bacterial complex liquid.

The TOGO M490 import is not reconciled with the separate MediaDive/JCM J489 normalized owner at `data/normalized_yaml/bacterial/catonella_ureilytica_medium.yaml`. That owner has the same JCM source page, the correct JCM pH, the correct seven non-water ingredients, and the JCM preparation text.

Most defined chemicals are grounded correctly, but `MgCl2.6H2O` has only a primary `CHEBI:86345` term and is missing the matching `mediaingredientmech_chebi_term`.

## Evidence

JCM 489 lists a 1 L medium with:

- 20 g Casitone (BD-Difco)
- 5 g yeast extract
- 5 g Na2HPO4
- 1.10 g MgCl2.6H2O
- 1 g urea
- 0.75 g sodium thioglycolate
- 0.5 mg resazurin
- 1 L distilled water

The TOGO JSON preserves `unit: mg` for resazurin and `unit: L` for distilled water, but the generated YAML has `Resazurin` as `0.5 G_PER_L` and `Distilled water` as `1 G_PER_L`. MediaDive J489 correctly normalizes the 0.5 mg resazurin row to `0.0005 G_PER_L` and omits water from the direct formula.

JCM and MediaDive preserve the anaerobic handling procedure: mix all components except urea and sodium thioglycolate, boil briefly, cool under N2-CO2 4:1, add thioglycolate, dispense under the same gas, autoclave, add a filter-sterilized 10% urea solution stored under N2 after cooling, and adjust pH to 7.4.

## Completeness

The generated TOGO record drops the JCM pH 7.4 and the entire JCM preparation procedure. Instead, the N2-CO2 and N2 atmospheres from the preparation text became separate variable final ingredients, `Carbon dioxide gas` and `Nitrogen gas`.

No target organism or strain growth evidence has been curated.

## Findings

- Needs curation: the 1 L distilled-water source row was normalized as `1 G_PER_L`.
- Needs curation: the 0.5 mg resazurin source row was normalized as `0.5 G_PER_L`, 1000x too high.
- Needs curation: N2 and CO2 preparation atmospheres were promoted to variable final ingredients.
- Needs curation: pH 7.4 and the JCM anaerobic/autoclave/filter-sterilization preparation were dropped.
- Needs curation: TOGO M490 and MediaDive/JCM J489 are duplicate imports of the same JCM page but remain as separate generated recipes.
- Minor: `MgCl2.6H2O` lacks its `mediaingredientmech_chebi_term` mirror.

## Recommended Edits

- Fix the TOGO importer or normalized M490 owner so liter and milligram quantities are not treated as grams per liter.
- Remove the variable N2 and CO2 ingredient rows and keep the gas mixtures in structured or textual preparation metadata.
- Restore the JCM pH and preparation instructions from the source page.
- Reconcile `TOGO_M490_Catonella_Ureilytica_Medium.yaml` with the MediaDive/JCM J489 normalized owner once TOGO units are repaired.
- Add the missing magnesium chloride hexahydrate CHEBI mirror.

## Follow-up Checks

- Regenerate this YAML and verify that the formula contains seven non-water ingredients rather than ten rows with water and gas pseudo-ingredients.
- Compare regenerated concentrations against the JCM 489 page and MediaDive J489 JSON.
- Verify that TOGO M490 no longer remains isolated from the MediaDive/JCM J489 duplicate family for source-unit reasons.
- Run LinkML, strict, reference, and term validation after repair.

## Additional Notes

Generated `data/merge_yaml/merged` files are derived. Apply durable fixes to `data/normalized_yaml/bacterial/TOGO_M490_Catonella_Ureilytica_Medium.yaml` or the TOGO import/conversion code before regenerating this output.
