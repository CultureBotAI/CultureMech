# YAML Record Review: thermosyntropha_l_60_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermosyntropha_l_60_medium.yaml
- Started UTC: 2026-09-25T10:52:13Z
- Finished UTC: 2026-09-25T10:52:15Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M886, Thermosyntropha L-60 Medium.
- The record was merged from `TOGO_M886_Thermosyntropha_L-60_Medium`.
- The main checked sources were TOGO M886, the live JCM 850 page, and MediaDive REST entry J850.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 after the startup line only and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- TOGO M886 correctly points to JCM_M850 and to the JCM GRMD 850 source URL.
- The live JCM 850 page is available and identifies the medium as THERMOSYNTROPHA L-60 MEDIUM.
- The generated TOGO record does not carry the JCM pH 7.0 adjustment as `ph_value`.

## Evidence

- JCM 850 defines three separately autoclaved solutions: Solution A with 760 ml water, phosphate, yeast extract, tryptone, peptone, and 1 mg resazurin; Solution B with 100 ml water, NH4Cl, NaCl, CaCl2 x 2 H2O, MgCl2 x 6 H2O, and 1 ml each of FeCl2 and trace element solutions from JCM 187; and Solution C with 100 ml water and 1.72 g crotonic acid.
- JCM 850 then adds 10 ml trace vitamins from JCM 197, 30 ml of 8% NaHCO3, and reduces the final medium with 0.025% L-cysteine x HCl x H2O plus 0.025% Na2S x 9 H2O.
- The TOGO import has the right broad structure but leaves Solution A, Solution B, Solution C, FeCl2 solution, trace element solution, 8% NaHCO3, and trace vitamins as empty placeholder `solutions`.
- A direct MediaDive/JCM J850 generated record exists as `thermosyntropha_l_60_medium__83cf0bea`.

## Completeness

- The generated TOGO record preserves the 760 ml, 100 ml, and 100 ml solution-water quantities but rolls them into a single 960 g/L water entry.
- Several source solution additions remain placeholders with `G_PER_L` concentrations equal to their source volumes.
- The pH 7.0 adjustment is present only inside `preparation_steps`.

## Findings

- The record needs curation because stock and subsolution additions are not represented as usable structured formulae. Solution A, Solution B, Solution C, FeCl2 solution, trace element solution, 8% NaHCO3 solution, and Trace vitamins are placeholders with no composition.
- The resazurin amount is imported as 1 g/L instead of the 1 mg addition listed in JCM 850.
- Reducing agents are represented only as variable `Na2S` and L-cysteine ingredients even though the JCM source gives final 0.025% target concentrations and 5% stock-solution handling.

## Recommended Edits

- Replace the TOGO placeholder import with a structured JCM 850 representation that keeps Solution A/B/C membership and JCM 187/JCM 197 stock references or expansions.
- Convert resazurin to the 1 mg source amount and preserve pH 7.0 as `ph_value`.
- Merge or retire this TOGO M886 copy once the direct MediaDive/JCM J850 record is fixed.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare the final record against the live JCM 850 page, especially the 10 ml trace vitamins and 30 ml 8% NaHCO3 solution additions.

## Additional Notes

- None found.
