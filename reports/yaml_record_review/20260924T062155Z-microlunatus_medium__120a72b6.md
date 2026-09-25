# YAML Record Review: MICROLUNATUS medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/microlunatus_medium__120a72b6.yaml`
- Started UTC: 2026-09-24T06:21:55Z
- Finished UTC: 2026-09-24T06:21:55Z
- Verdict: pass with minor issues

## Target

- Reviewed merged record `data/merge_yaml/merged/microlunatus_medium__120a72b6.yaml`.
- Editable normalized source: `data/normalized_yaml/bacterial/KOMODO_776_MICROLUNATUS_medium.yaml`.
- Canonical duplicate parent: `data/normalized_yaml/bacterial/microlunatus_medium.yaml`.
- KOMODO medium: 776, MICROLUNATUS medium.
- DSMZ / MediaDive medium: 776, MICROLUNATUS MEDIUM.

## Validation

- LinkML open-schema validation: passed; `No issues found`.
- Strict validation: passed with 0 errors; `validate_strict.py` scanned 1 file and produced only the TSV header.
- Reference validation: passed; 1 file, 0 checks.
- Term validation: passed.
- Embedded history: Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The duplicate merge is appropriate. The KOMODO source states DSMZ Medium 776 provenance, the DSMZ parent has the same seven non-water ingredients at the same concentrations, and the merged record explicitly carries `SOURCE_DUPLICATE` parent metadata.
- The MediaDive and DSMZ identities both point to MICROLUNATUS MEDIUM at pH 7.0.
- The defined salts and glucose are grounded to exact ChEBI terms.
- Peptone and yeast extract are ungrounded undefined components; that is acceptable here.

## Evidence

- DSMZ Medium 776 lists Glucose 0.5 g, Peptone 0.5 g, Yeast extract 0.5 g, Na-glutamate 0.5 g, KH2PO4 0.5 g, ammonium sulfate 0.1 g, MgSO4 x 7 H2O 0.1 g, distilled water 1000 ml, and pH adjustment to 7.0.
- MediaDive medium 776 reports the same ingredient amounts and the same pH 7.0.
- The normalized DSMZ parent contains all seven non-water ingredients, the 1000 ml water row, and an `ADJUST_PH` preparation step.
- The normalized KOMODO source contains the same seven non-water ingredient rows and has `parent_media` pointing at the DSMZ parent as a source duplicate.

## Completeness

- The core non-water ingredient recipe is complete.
- The merged record preserves pH 7.0 in `ph_value`.
- The merged record omits the DSMZ parent water row and explicit `Adjust pH to 7.0` preparation step.

## Findings

- The generated merge dropped the DSMZ parent's 1000 ml distilled-water row.
- The generated merge dropped the DSMZ parent's explicit pH-adjustment preparation step even though it retained `ph_value: 7.0`.

## Recommended Edits

- If generated records are expected to carry solvent rows, update duplicate merging so the canonical parent's 1000 ml distilled-water row is retained.
- If preparation steps should be preserved across `SOURCE_DUPLICATE` merges, update duplicate merging so the DSMZ parent's `Adjust pH to 7.0` step survives in the generated record.
- No ingredient identity or concentration edit is needed for the seven non-water ingredients.

## Follow-up Checks

- Re-run focused open-schema, strict, reference, and term validators if the merge output changes.
- Compare regenerated output against DSMZ Medium 776 to confirm the seven non-water ingredients remain unchanged.
- Verify `ph_value` stays 7.0.

## Additional Notes

- Empty optional fields were not treated as defects.
