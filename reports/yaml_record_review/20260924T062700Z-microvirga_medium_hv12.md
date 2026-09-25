# YAML Record Review: MICROVIRGA MEDIUM (HV12)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/microvirga_medium_hv12.yaml`
- Started UTC: 2026-09-24T06:27:00Z
- Finished UTC: 2026-09-24T06:27:00Z
- Verdict: pass with minor issues

## Target

- Reviewed merged record `data/merge_yaml/merged/microvirga_medium_hv12.yaml`.
- Editable normalized source: `data/normalized_yaml/bacterial/microvirga_medium_hv12.yaml`.
- DSMZ / MediaDive medium: 1547, MICROVIRGA MEDIUM (HV12).

## Validation

- LinkML open-schema validation: passed; `No issues found`.
- Strict validation: passed with 0 errors; `validate_strict.py` scanned 1 file and produced only the TSV header.
- Reference validation: passed; 1 file, 0 checks.
- Term validation: passed.
- Embedded history: Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The primary medium identity is coherent: the generated YAML, DSMZ PDF, and MediaDive medium 1547 all identify MICROVIRGA MEDIUM (HV12) at pH 7.4.
- `kg_microbe_match: mediadive.medium:74` is wrong. MediaDive medium 74 is THERMUS THERMOPHILUS MEDIUM, not Microvirga Medium (HV12).
- The normalized source has September 2026 groundings for Malt extract, Yeast extract, and Peptone; the generated YAML predates that repair and still leaves those three undefined components ungrounded.

## Evidence

- DSMZ Medium 1547 lists Malt extract 1 g, Yeast extract 2 g, Peptone 5 g, NaCl 5 g, Distilled water 1000 ml, and pH adjustment to 7.4.
- MediaDive medium 1547 reports the same four non-water ingredients and pH 7.4.
- The generated YAML carries the four non-water ingredients, correct g/L values, `ph_value: 7.4`, and the pH-adjustment step.

## Completeness

- The core four non-water ingredient recipe is complete.
- The pH adjustment is complete.
- The 1000 ml distilled-water row is absent.

## Findings

- The DSMZ source's 1000 ml distilled-water row is missing from the generated and normalized records.
- The generated record is stale relative to the normalized source's September groundings for Malt extract, Yeast extract, and Peptone.
- `kg_microbe_match` links this record to unrelated MediaDive medium 74.

## Recommended Edits

- Restore the 1000 ml distilled-water row in `data/normalized_yaml/bacterial/microvirga_medium_hv12.yaml` if explicit solvent rows are expected for generated records.
- Remove or correct `kg_microbe_match: mediadive.medium:74`.
- Regenerate `data/merge_yaml/merged/microvirga_medium_hv12.yaml` so the September exact-term groundings are published.

## Follow-up Checks

- Re-run focused open-schema, strict, reference, and term validators for `data/merge_yaml/merged/microvirga_medium_hv12.yaml`.
- Verify the non-water ingredient concentrations and pH 7.4 remain unchanged.
- Verify the generated record no longer references MediaDive 74.

## Additional Notes

- Empty optional fields were not treated as defects.
