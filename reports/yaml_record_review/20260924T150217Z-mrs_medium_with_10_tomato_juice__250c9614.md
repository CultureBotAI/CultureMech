# YAML Record Review: MRS MEDIUM WITH 10% TOMATO JUICE

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml
- Started UTC: 2026-09-24T15:01:46Z
- Finished UTC: 2026-09-24T15:02:17Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:003148` / `mrs_medium_with_10_tomato_juice` at `data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml`.

- Generated source: `data/normalized_yaml/bacterial/mrs_medium_with_10_tomato_juice.yaml`
- Merge source: `mrs_medium_with_10_tomato_juice`
- Merge fingerprint: `250c9614a656ee51066d9d538bb2ed78388ce83a18bfa894bae3621ad141049e`
- Category: `bacterial`
- Medium term: `mediadive.medium:J803`, label `MRS MEDIUM WITH 10% TOMATO JUICE`
- Source: JCM GRMD 803

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml` | Passed. |
| Strict validator with `scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml --out /private/tmp/mrs_medium_with_10_tomato_juice__250c9614.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator with `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were applicable. |
| Term validator with `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` events. |

## Identity and Grounding

The record identifies the MediaDive/JCM J803 import of MRS MEDIUM WITH 10% TOMATO JUICE. Its direct JCM source URL, `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=803`, currently returns `Nothing found`, but TOGO M838 preserves JCM_M803 as MRS Medium With 10% Tomato Juice.

The record preserves pH 5.2, MRS broth 55 g/L, and cysteine hydrochloride hydrate 0.5 g/L. Against the TOGO mirror of GRMD 803, two formulation rows are wrong or absent:

- TOGO lists `Distilled water`, 900 ml; the MediaDive/JCM YAML has no water row.
- TOGO lists filtered tomato juice, 100 ml; the MediaDive/JCM YAML has 100 `G_PER_L`.

The exact `CultureMech:003148` search across `data/normalized_yaml` and `data/merge_yaml` used `rg --no-ignore --hidden`. It found one maintained YAML owner, this generated merge, and generated indexes only.

## Evidence

The inspected TOGO M838 record reports original media ID `JCM_M803`, source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=803`, pH 5.2, 900 ml distilled water, 100 ml filtered tomato juice, 0.5 g L-cysteine hydrochloride hydrate, and 55 g MRS broth (BD-Difco). The live JCM GRMD 803 page currently has no formula.

The same exact `GRMD=803` search that found this MediaDive/JCM owner also found `data/normalized_yaml/bacterial/TOGO_M838_MRS_Medium_With_10_Tomato_Juice.yaml`, which is the TOGO import of the same JCM source. The two records should not remain separate generated media after normalization and merging.

## Completeness

The generated record is missing the 900 ml water row and has a dimensionally wrong tomato-juice row. It is also stale relative to the 2026-09-13 maintained source because `data/normalized_yaml/bacterial/mrs_medium_with_10_tomato_juice.yaml` now grounds tomato juice to `FOODON:03301454`, while this generated merge still leaves that row ungrounded.

No target-organism or growth-metric blocks are present. The inspected TOGO mirror only preserves the old JCM formula, so those empty optional slots are not defects.

## Findings

### Major

1. The JCM/MediaDive import omits the water volume.
   - Evidence: TOGO M838 mirrors GRMD 803 with `Distilled water`, 900 ml; the maintained MediaDive/JCM owner and generated merge have no water row.
   - Impact: the formula loses the final-volume solvent from the JCM tomato-juice medium.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_10_tomato_juice.yaml`, then regenerate `data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml`.

2. The tomato-juice volume is represented as a mass concentration.
   - Evidence: TOGO M838 mirrors GRMD 803 with filtered tomato juice, 100 ml; the maintained MediaDive/JCM owner and generated merge store 100 `G_PER_L`.
   - Impact: the 10% tomato-juice supplement is dimensionally wrong.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_10_tomato_juice.yaml`, then regenerate `data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml`.

3. JCM Medium 803 remains split across TOGO and MediaDive imports.
   - Evidence: `data/normalized_yaml/bacterial/mrs_medium_with_10_tomato_juice.yaml` and `data/normalized_yaml/bacterial/TOGO_M838_MRS_Medium_With_10_Tomato_Juice.yaml` both trace to GRMD 803.
   - Impact: the same JCM tomato-juice MRS medium can be emitted as two generated records instead of one merged record.
   - Owner: both normalized records plus the merge/de-duplication rule for equivalent TOGO and MediaDive JCM imports.

4. The generated record is stale relative to the maintained tomato-juice grounding.
   - Evidence: the normalized owner has a 2026-09-13 `repair_bacterial_score10_exact_terms_batch5.py` event that grounds `Tomato juice`; the generated merge still ends at 2026-08-06 and has no tomato-juice term.
   - Impact: even after the volume bug is fixed in normalized YAML, this generated record will remain under-grounded until it is regenerated.
   - Owner: regenerate `data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml`.

### Minor

1. The exact MRS broth source label is weakened.
   - Evidence: TOGO M838 reports `MRS broth (BD-Difco)`, while this MediaDive/JCM record stores only `MRS broth`.
   - Impact: the row amount is correct, but the source supplier attribute is not preserved.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_10_tomato_juice.yaml`, then regenerate the merge.

2. The original JCM source URL is stale.
   - Evidence: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=803` currently returns `Nothing found`, while TOGO M838 still preserves the old formula.
   - Impact: curation has to rely on TOGO or another preserved capture unless JCM restores GRMD 803.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_10_tomato_juice.yaml`.

### Blocker

None found.

## Recommended Edits

1. Restore the 900 ml distilled-water row in `data/normalized_yaml/bacterial/mrs_medium_with_10_tomato_juice.yaml`.
2. Convert filtered tomato juice from 100 `G_PER_L` to a supported 100 ml volume representation.
3. Preserve the BD-Difco source attribute on the MRS broth row.
4. Reconcile the MediaDive/JCM J803 and TOGO M838 records so GRMD 803 no longer publishes twice.
5. Append curation-history events to changed normalized inputs and regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

After curation, run the same focused generated-record checks:

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml`
- `python scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml --workers 1 --quiet`
- `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`

Also rerun merge freshness and an exact ignored-file-inclusive `GRMD=803` search to verify JCM 803 is not still duplicated through TOGO and MediaDive.

## Additional Notes

None found.
