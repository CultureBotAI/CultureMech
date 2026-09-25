# YAML Record Review: sphaerotilus_sp_fb_5_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/sphaerotilus_sp_fb_5_medium.yaml
- Started UTC: 2026-09-25T06:07:25Z
- Finished UTC: 2026-09-25T06:09:03Z
- Verdict: needs curation

## Target

Generated merged YAML for JCM Medium 1379, SPHAEROTILUS SP. FB-5 MEDIUM.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/sphaerotilus_sp_fb_5_medium.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The JCM identity is correct: JCM GRMD 1379 is SPHAEROTILUS SP. FB-5 MEDIUM.

Glucose, MgSO4 x 7H2O, and water are grounded to reasonable CHEBI terms. Proteose peptone No. 3 and Yeast extract are ungrounded complex ingredients, which is acceptable if no exact product grounding is available.

## Evidence

JCM Medium 1379 lists 0.4 g glucose, 0.2 g Proteose peptone No. 3 (BD-Difco), 0.04 g Yeast extract (BD-Difco), 0.02 g MgSO4 x 7H2O, and 1.0 L distilled water. The JCM page gives the default JCM instruction to autoclave media at 121 C for 15 minutes unless otherwise stated.

## Completeness

All source ingredients are present, but the source water volume is imported as 1.0 ml/L rather than 1.0 L. The generated record also omits JCM's default autoclave metadata.

## Findings

- Critical: `Distilled water` is modeled as `1.0` `ML_PER_L`; JCM specifies 1.0 L.
- Major: the generated record omits the JCM default autoclaving instruction at 121 C for 15 minutes.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/JCM_J1379_SPHAEROTILUS_SP_FB_5_MEDIUM.yaml` so `Distilled water` is represented as 1.0 L or 1000 ml/L, not 1.0 ml/L.
- Add sterilization metadata for JCM's default 121 C for 15 minutes autoclave instruction.
- Regenerate `data/merge_yaml/merged/sphaerotilus_sp_fb_5_medium.yaml` from the repaired normalized record.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm `Distilled water` no longer appears as `1.0` `ML_PER_L`.

## Additional Notes

None found.
