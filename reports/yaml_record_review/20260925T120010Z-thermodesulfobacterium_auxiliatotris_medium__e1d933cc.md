# YAML Record Review: thermodesulfobacterium_auxiliatotris_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobacterium_auxiliatotris_medium__e1d933cc.yaml
- Started UTC: 2026-09-25T12:00:10Z
- Finished UTC: 2026-09-25T12:00:10Z
- Verdict: needs curation

## Target
Reviewed the generated MediaDive/JCM J1229 record for Thermodesulfobacterium auxiliatotris medium.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with no diagnostics.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to mediadive.medium:J1229.
- MediaDive J1229 maps to JCM Thermodesulfobacterium auxiliatotris medium at pH 7.0.
- The recipe has a 1030 ml main solution, a 5 ml Mineral solution addition, a 10 ml Solution A addition, and several 1 to 2 ml post-autoclave stock additions.

## Evidence
- Main sol. J1229 lists basal salts, 5 ml Mineral solution, 1000 ml distilled water, 10 ml Solution A, 1 ml each of 1.0 M sodium acetate, 1.0 M sodium thiosulfate, and 8% NaHCO3, plus 2 ml of 5% Na2S x 9H2O.
- Solution A contributes MgSO4 x 7H2O, CaCl2 x 2H2O, and 10 ml distilled water.
- The preparation adjusts pH with NaOH, autoclaves under N2, adds filter-sterilized H2 to the headspace, and then adds the post-autoclave solutions aseptically and anaerobically.

## Completeness
- The pH 7.0 value and main preparation text are present.
- Main-solution and Solution A water rows are absent.
- Mineral solution and Solution A structure was flattened or reduced to a placeholder.

## Findings
- The 5 ml Mineral solution was flattened at full stock strength, so EDTA and trace metals appear at 1x stock concentrations rather than diluted concentrations.
- The 10 ml Solution A addition was left as an empty 10 G_PER_L solution while its MgSO4 and CaCl2 contents were also flattened into top-level ingredients.
- The 1 ml sodium acetate, 1 ml sodium thiosulfate, 1 ml NaHCO3, and 2 ml Na2S x 9H2O additions were imported as 1, 1, 1, and 2 G_PER_L solute rows.
- The Solution A label and Mineral solution KOH/stoppers comments were imported as top-level preparation steps.

## Recommended Edits
- Preserve Mineral solution, Solution A, sodium acetate, sodium thiosulfate, NaHCO3, and Na2S x 9H2O as stock additions with their source volumes and concentrations.
- Expand nested stock recipes only after applying their volume dilution.
- Keep Solution A text and Mineral solution preparation/comment text scoped to the relevant stock.
- Restore water rows if water is retained in generated records.

## Follow-up Checks
- Rebuild J1229 and verify that the four post-autoclave stock additions are not represented as gram-per-liter masses.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
