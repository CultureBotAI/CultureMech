# YAML Record Review: MICROTETRASPORA MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/microtetraspora_medium__380d1a34.yaml`
- Started UTC: 2026-09-24T06:25:27Z
- Finished UTC: 2026-09-24T06:25:27Z
- Verdict: pass with minor issues

## Target

- Reviewed merged record `data/merge_yaml/merged/microtetraspora_medium__380d1a34.yaml`.
- Editable normalized source: `data/normalized_yaml/bacterial/microtetraspora_medium.yaml`.
- MediaDive medium: `mediadive.medium:J114`, MICROTETRASPORA MEDIUM.
- Source provider: JCM.

## Validation

- LinkML open-schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with 0 errors; `validate_strict.py` scanned 1 file and produced only the TSV header.
- Reference validation: passed; 1 file, 0 checks.
- Term validation: passed.
- Embedded history: Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The recipe identity is coherent: the generated YAML and MediaDive J114 both identify MICROTETRASPORA MEDIUM at pH 7.4.
- MediaDive preserves JCM as the source, but the current JCM `GRMD=114` page returns `Nothing found`; formula checking therefore used the MediaDive REST representation of the JCM medium.
- Defined ingredients are grounded to exact ChEBI terms where exact terms are available. `MnSO4 x n H2O` is appropriately grounded no more narrowly than generic manganese(II) sulfate.

## Evidence

- MediaDive J114 lists Glucose 2 g, L-Asparagine 1 g, K2HPO4 0.5 g, MgSO4 x 7 H2O 0.5 g, FeSO4 x 7 H2O 10 mg, MnSO4 x n H2O 1 mg, CuSO4 x 5 H2O 1 mg, ZnSO4 x 7 H2O 1 mg, Agar 15 g, distilled water 1000 ml, and pH adjustment to 7.4.
- The generated YAML carries the nine non-water rows with matching g/L values, including conversion of the 10 mg and 1 mg trace salt amounts to 0.01 and 0.001 g/L.
- The generated YAML carries `physical_state: SOLID_AGAR`, `ph_value: 7.4`, and an `ADJUST_PH` step.

## Completeness

- The core nine non-water ingredient recipe is complete.
- The pH adjustment is complete.
- The 1000 ml distilled-water row is absent.

## Findings

- The MediaDive source's 1000 ml distilled-water row is missing from the generated and normalized records.

## Recommended Edits

- Restore the 1000 ml distilled-water row in `data/normalized_yaml/bacterial/microtetraspora_medium.yaml` if explicit solvent rows are expected for generated records.
- Regenerate `data/merge_yaml/merged/microtetraspora_medium__380d1a34.yaml` after that change.

## Follow-up Checks

- Re-run focused open-schema, strict, reference, and term validators for `data/merge_yaml/merged/microtetraspora_medium__380d1a34.yaml`.
- Verify the nine non-water ingredient concentrations and pH 7.4 remain unchanged.

## Additional Notes

- Empty optional fields were not treated as defects.
