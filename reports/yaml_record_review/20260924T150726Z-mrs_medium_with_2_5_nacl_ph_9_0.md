# YAML Record Review: MRS Medium With 2.5% NaCl (pH 9.0)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0.yaml
- Started UTC: 2026-09-24T15:04:55Z
- Finished UTC: 2026-09-24T15:07:26Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:010403` / `mrs_medium_with_2_5_nacl_ph_9_0` at `data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0.yaml`.

- Canonical generated source: `data/normalized_yaml/bacterial/TOGO_M977_MRS_Medium_With_2.5_NaCl_pH_9.0.yaml`
- Other merged sources: `data/normalized_yaml/bacterial/TOGO_M249_MRS_Medium_With_10_NaCl.yaml`, `data/normalized_yaml/bacterial/TOGO_M602_MRS_Medium_With_2.5_NaCl.yaml`
- Merge fingerprint: `8527b26e09d54b728f00cb5cce2d246716e114972bd48eb385e1d28bcd430462`
- Category: `bacterial`
- Medium term: `TOGO:M977`, label `MRS Medium With 2.5% NaCl (pH 9.0)`
- Original source: JCM `JCM_M931`, GRMD 931

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0.yaml` | Passed. |
| Strict validator with `scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0.yaml --out /private/tmp/mrs_medium_with_2_5_nacl_ph_9_0.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator with `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were applicable. |
| Term validator with `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` events. |

## Identity and Grounding

The generated record claims to be TOGO M977 / JCM GRMD 931, MRS Medium With 2.5% NaCl at pH 9.0, but its NaCl ingredient came from a different 10% NaCl source.

TOGO and JCM support these identities:

| Source | Formula distinction |
|---|---|
| TOGO M249 / JCM 257 | 100 g NaCl; no pH 9.0 claim. |
| TOGO M602 / JCM 596 | 25 g NaCl; no pH 9.0 claim. |
| TOGO M977 / JCM 931 | 25 g NaCl and pH 9.0. |

The exact `CultureMech:010403` search across `data/normalized_yaml` and `data/merge_yaml` used `rg --no-ignore --hidden`. It found the canonical maintained M977 owner, this generated merge, generated indexes, and the reciprocal child reference in the 10% NaCl parent.

## Evidence

The inspected TOGO M977 and JCM GRMD 931 sources both list 55 g Lactobacilli MRS broth (BD-Difco), 25 g NaCl, 15 g Bacto agar (BD-Difco), 1 L distilled water, and an instruction to adjust pH to 9.0.

The generated record was merged from TOGO M249, M602, and M977, and it now has the 100 g/L NaCl row from the 10% M249 parent while retaining the M977 label and M977 `media_term`. Its `variant_modifications` text says NaCl was decreased from 100 g/L to 25 g/L, contradicting the emitted 100 `G_PER_L` ingredient.

An exact ignored-file-inclusive search for `GRMD=931` using a negative lookahead for following digits found this TOGO M977 record and `data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl_ph_9_0.yaml`, the MediaDive/JCM J931 import of the same JCM source. That MediaDive sibling should be reconciled with M977 but not with the 10% M249 or pH-unspecified M602 variants.

## Completeness

The generated record has the wrong NaCl concentration for its own identity, lacks the pH 9.0 source field and preparation step, and keeps the 1 L water row as 1 `G_PER_L`.

No target-organism or growth-metric block is present. TOGO M977 and JCM GRMD 931 only define the medium, so those empty optional slots are not defects.

## Findings

### Major

1. The merge conflates a 10% NaCl parent with 2.5% NaCl variants.
   - Evidence: TOGO M249 has 100 g NaCl; TOGO M602 and M977 have 25 g NaCl. The generated M977 record lists 100 `G_PER_L` while saying the NaCl concentration was decreased to 25 g/L.
   - Impact: the record denotes a 2.5% NaCl pH 9.0 medium but emits the 10% NaCl formula.
   - Owner: the merge/de-duplication rule for M249, M602, and M977, then regenerate `data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0.yaml`.

2. The M977 pH and pH-adjustment step are missing.
   - Evidence: TOGO M977 has `ph: 9.0`, and both TOGO M977 and JCM GRMD 931 say to adjust pH to 9.0; neither the maintained M977 YAML nor the generated record has `ph_value` or a preparation step.
   - Impact: the pH 9.0 claim is present only in free-text labels and variant notes.
   - Owner: `data/normalized_yaml/bacterial/TOGO_M977_MRS_Medium_With_2.5_NaCl_pH_9.0.yaml`, then regenerate.

3. The 1 L water row uses a mass unit.
   - Evidence: TOGO M977 and JCM GRMD 931 both list 1 L distilled water; the maintained M977 YAML and generated record store 1 `G_PER_L`.
   - Impact: the final-volume solvent is dimensionally wrong.
   - Owner: `data/normalized_yaml/bacterial/TOGO_M977_MRS_Medium_With_2.5_NaCl_pH_9.0.yaml`, then regenerate.

4. The JCM GRMD 931 source is duplicated through TOGO and MediaDive imports.
   - Evidence: `data/normalized_yaml/bacterial/TOGO_M977_MRS_Medium_With_2.5_NaCl_pH_9.0.yaml` and `data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl_ph_9_0.yaml` both cite GRMD 931.
   - Impact: after the salinity merge is fixed, the same JCM pH 9.0 variant can still publish twice unless equivalent TOGO and MediaDive JCM imports are reconciled.
   - Owner: both normalized records plus the merge/de-duplication rule for equivalent TOGO and MediaDive JCM imports.

### Minor

None found.

### Blocker

None found.

## Recommended Edits

1. Split the M249 10% NaCl, M602 2.5% NaCl, and M977 2.5% NaCl pH 9.0 records into distinct generated outputs; keep salinity and pH-variant relationships as metadata instead of merging their ingredient lists.
2. Add pH 9.0 and a pH-adjustment step to `data/normalized_yaml/bacterial/TOGO_M977_MRS_Medium_With_2.5_NaCl_pH_9.0.yaml`.
3. Convert distilled water from 1 `G_PER_L` to a supported 1 L volume representation in the maintained TOGO inputs.
4. Reconcile TOGO M977 with the MediaDive/JCM J931 duplicate once the merge no longer crosses distinct salinity variants.
5. Append curation-history events to changed normalized inputs and regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

After curation, run the same focused generated-record checks:

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0.yaml`
- `python scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0.yaml --workers 1 --quiet`
- `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`

Also rerun the merge audit and an exact ignored-file-inclusive `GRMD=931` search to verify M977 and J931 merge together without absorbing the M249 10% NaCl or M602 pH-unspecified variants.

## Additional Notes

None found.
