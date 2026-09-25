# YAML Record Review: pae_i_medium_0_1_w_v_urea

- Repository: CultureMech
- Record: data/merge_yaml/merged/pae_i_medium_0_1_w_v_urea.yaml
- Started UTC: 2026-09-24T19:41:45Z
- Finished UTC: 2026-09-24T19:41:45Z
- Verdict: needs curation

## Target

Reviewed generated MediaRecipe `CultureMech:008401`, `pae_i_medium_0_1_w_v_urea`, generated from `data/normalized_yaml/bacterial/pae_i_medium_0_1_w_v_urea.yaml` for TOGO M1829 / NBRC Medium 1062.

## Validation

- Open LinkML validation: Passed; exited 0 with `No issues found`.
- Strict validation: Passed; scanned 1 file with 0 ERROR rows. `/private/tmp/pae_i_medium_0_1_w_v_urea.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The generated identity matches TOGO M1829, which imports NBRC Medium 1062 / Pae I Medium + 0.1% (w/v) Urea. An ignored-inclusive exact search for `TOGO:M1829`, `NBRC_M1062`, `NO=1062`, `Pae I Medium`, and `pae_i_medium_0_1_w_v_urea` across `data/merge_yaml` and `data/normalized_yaml` found this TOGO source and a direct `NBRC_1063.yaml` source that also points to NBRC Medium 1062.

## Evidence

TOGO M1829 and the NBRC Medium 1062 page list 5 g Tryptone, 3 g Yeast extract, 10 g NaCl, 1 g Urea, 1 L Distilled water, 15 g Agar if needed, and the instruction to adjust pH to 8.5 with 50 mM Tris-HCl buffer. The direct NBRC normalized source has already been re-parsed and curated to this same formula with `ph_value: 8.5`, `Distilled water` as 1 `L`, sourced ingredients, an explicit 50 mM Tris-HCl pH-adjustment note, and an NBRC Medium 1062 term.

## Completeness

The generated TOGO record preserves the main masses but omits pH 8.5, omits the 50 mM Tris-HCl buffer concentration, regresses 1 L Distilled water to 1 `G_PER_L`, treats `Agar (if needed)` as required by setting `physical_state: SOLID_AGAR`, and remains split from the direct NBRC source for the same official medium.

## Findings

1. pH and buffer concentration were lost.

   The source says to adjust the medium to pH 8.5 with 50 mM Tris-HCl buffer. The generated record has no pH field and represents `Tris-HCl buffer` as `VARIABLE` rather than preserving the 50 mM source concentration.

2. Distilled water has the wrong unit.

   TOGO and NBRC both list Distilled water as 1 L. The generated record stores `Distilled water` as 1 `G_PER_L`.

3. Conditional agar is treated as the fixed physical state.

   NBRC lists 15 g Agar only "if needed", but the generated record sets the whole recipe to `SOLID_AGAR`. The record needs to preserve the conditional solidifier rather than making the optional agar determine a single physical state.

4. NBRC Medium 1062 is split into two generated records.

   `data/normalized_yaml/bacterial/NBRC_1063.yaml` is a repaired direct import for the same NBRC Medium 1062 source, but the TOGO generated record is a singleton and `data/merge_yaml/merged/1063.yaml` was separately generated from stale pre-repair parsing output.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/pae_i_medium_0_1_w_v_urea.yaml` to match the cured NBRC 1062 representation: 1 L water, pH 8.5, 50 mM Tris-HCl buffer, explicit preparation steps, and grounded tryptone, yeast extract, agar, and buffer.
- Link TOGO M1829 and the direct NBRC Medium 1062 record as source duplicates before regenerating.
- Keep the optional agar as a conditional solidifier and choose a physical-state representation that does not imply agar is always required.

## Follow-up Checks

- Re-run an ignored-inclusive exact search for `NO=1062`, `TOGO:M1829`, and `nbrc.medium:1062` after regeneration and confirm NBRC Medium 1062 emits as one generated source-duplicate record.
- Confirm the regenerated record includes `ph_value: 8.5`, a pH-adjustment step with 50 mM Tris-HCl, and Distilled water as a volume.
- Re-run open, strict, reference, and term validation on the regenerated YAML.

## Additional Notes

None found.
