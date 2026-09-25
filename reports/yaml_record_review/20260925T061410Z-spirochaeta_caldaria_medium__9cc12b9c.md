# YAML Record Review: spirochaeta_caldaria_medium__9cc12b9c

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirochaeta_caldaria_medium__9cc12b9c.yaml
- Started UTC: 2026-09-25T06:13:07Z
- Finished UTC: 2026-09-25T06:14:11Z
- Verdict: needs curation

## Target

Generated merged YAML for TOGO M689, Spirochaeta Caldaria Medium, derived from JCM 670.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/spirochaeta_caldaria_medium__9cc12b9c.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The record is grounded to TOGO M689 and correctly carries its original JCM_M670 source identity.

The generated YAML is materially stale relative to both TOGO M689 and JCM 670: it drops the pH, converts source volume and milligram rows to `G_PER_L`, and leaves all four referenced solution additions as empty `Unknown solution` stubs.

## Evidence

TOGO M689 identifies the recipe as Spirochaeta Caldaria Medium with original media ID JCM_M670, original URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=670`, and pH 7.0.

The TOGO API lists a first solution with 1 L distilled water, 0.5 mg resazurin, 2 g glucose, 2 g Tryptone (BD-Difco), 0.25 g L-cysteine HCl H2O, and N2. It then lists a second solution with 10 ml FeCl2 solution referencing M180, 10 ml trace element solution referencing M180, 25 ml trace minerals referencing M142, 10 ml trace vitamins referencing M190, and NaOH.

The JCM 670 source confirms the same 1 L base recipe, the four post-autoclave milliliter additions under N2, and adjustment to pH 7.0 with sterile NaOH if necessary.

## Completeness

The generated record has no `ph_value`, no preparation steps, no modeling of the four named solution additions as milliliter additions, and no resolved composition for any of the referenced stock solutions.

## Findings

- Major: pH 7.0 from TOGO M689 and JCM 670 is absent from the generated record.
- Major: source volume and mass-unit rows were converted to `G_PER_L`; distilled water is `1` `G_PER_L` instead of 1 L, resazurin is `0.5` `G_PER_L` instead of 0.5 mg, and the 10/10/25/10 ml solution additions were imported as `G_PER_L`.
- Major: the four referenced additions are empty `Unknown solution` stubs instead of populated FeCl2 solution, trace element solution, trace minerals, and trace vitamins records.
- Major: the generated record omits the JCM 670 preparation instructions to mix under N2, autoclave the base medium, sterilize the added solutions separately under N2, and adjust to pH 7.0 with sterile NaOH.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M689_Spirochaeta_Caldaria_Medium.yaml` to carry `ph_value: 7.0`.
- Convert the JCM 670 base recipe and the four stock additions with their source units intact: 1 L distilled water, 0.5 mg resazurin, 10 ml FeCl2 solution, 10 ml trace element solution, 25 ml trace minerals, and 10 ml trace vitamins.
- Resolve the M180, M142, and M190 references into named solution compositions, or keep exact cross-reference metadata without `Unknown solution` placeholders if those compositions cannot be inlined.
- Add preparation steps for the N2 atmosphere, autoclaving, separate stock sterilization, and sterile NaOH pH adjustment.
- Regenerate `data/merge_yaml/merged/spirochaeta_caldaria_medium__9cc12b9c.yaml` from the repaired normalized record.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm pH 7.0 is present.
- Confirm no liter, milliliter, or milligram source rows are represented as grams per liter.
- Confirm the four referenced solution additions are no longer empty `Unknown solution` stubs.

## Additional Notes

None found.
