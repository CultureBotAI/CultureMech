# YAML Record Review: MRS Medium With 10% Tomato Juice

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml
- Started UTC: 2026-09-24T14:59:37Z
- Finished UTC: 2026-09-24T15:01:01Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:010252` / `mrs_medium_with_10_tomato_juice` at `data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml`.

- Generated source: `data/normalized_yaml/bacterial/TOGO_M838_MRS_Medium_With_10_Tomato_Juice.yaml`
- Merge source: `TOGO_M838_MRS_Medium_With_10_Tomato_Juice`
- Merge fingerprint: `687115f81611281dbd5875d21a88d556804bb388a3d70d83ab875c72a99dbe0d`
- Category: `bacterial`
- Medium term: `TOGO:M838`, label `MRS Medium With 10% Tomato Juice`
- Original source: JCM `JCM_M803`, GRMD 803

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml` | Passed. |
| Strict validator with `scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml --out /private/tmp/mrs_medium_with_10_tomato_juice.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator with `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were applicable. |
| Term validator with `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` events. |

## Identity and Grounding

The record identifies TOGO M838, a TOGO import of JCM Medium 803, MRS Medium With 10% Tomato Juice. TOGO reports `gm` `http://togomedium.org/medium/M838`, original media ID `JCM_M803`, source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=803`, and pH `5.2`.

The powder rows are supported:

| TOGO row | YAML row | Review |
|---|---|---|
| MRS broth (BD-Difco), 55 g | `MRS broth (BD-Difco)`, 55 `G_PER_L` | Supported. |
| L-Cysteine HCl H2O, 0.5 g | `L--Cysteine...`, 0.5 `G_PER_L`, `CHEBI:91248` | Supported despite the preserved source punctuation. |

The two volume rows are not supported as mass concentrations:

- TOGO lists `Distilled water`, 900 ml; YAML has 900 `G_PER_L`.
- TOGO lists filtered tomato juice, 100 ml; YAML has 100 `G_PER_L`.

The exact `CultureMech:010252` search across `data/normalized_yaml` and `data/merge_yaml` used `rg --no-ignore --hidden`. It found one maintained YAML owner, this generated merge, and generated indexes only.

## Evidence

The inspected TOGO API record for M838 supports the four ingredient rows, pH 5.2, and the JCM GRMD 803 source identity. The live JCM GRMD 803 page currently returns `Nothing found`, so TOGO is the only inspected source that preserves the original JCM formula.

An exact ignored-file-inclusive search for `GRMD=803` using a negative lookahead for following digits also found `data/normalized_yaml/bacterial/mrs_medium_with_10_tomato_juice.yaml`, the MediaDive/JCM `J803` import of the same source, and its generated copy at `data/merge_yaml/merged/mrs_medium_with_10_tomato_juice__250c9614.yaml`. The MediaDive/JCM record has the same label and pH and is the same JCM variant, not a distinct recipe.

## Completeness

The record is incomplete because pH 5.2 and an adjust-pH preparation step are absent. The water and tomato-juice volumes are present but use wrong mass units.

No target-organism or growth-metric claims are present. TOGO M838 only exposes the old JCM formula, so those empty optional slots are not defects.

## Findings

### Major

1. The distilled-water volume was cast to grams per liter.
   - Evidence: TOGO M838 lists `Distilled water`, 900 ml; the maintained and generated YAML store 900 `G_PER_L`.
   - Impact: the water addition is dimensionally wrong.
   - Owner: `data/normalized_yaml/bacterial/TOGO_M838_MRS_Medium_With_10_Tomato_Juice.yaml`, then regenerate `data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml`.

2. The tomato-juice volume was cast to grams per liter.
   - Evidence: TOGO M838 lists filtered tomato juice, 100 ml; the maintained and generated YAML store 100 `G_PER_L`.
   - Impact: the 10% tomato juice supplement is dimensionally wrong.
   - Owner: `data/normalized_yaml/bacterial/TOGO_M838_MRS_Medium_With_10_Tomato_Juice.yaml`, then regenerate `data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml`.

3. The source pH and pH-adjustment step are missing.
   - Evidence: TOGO M838 reports pH `5.2`; the generated and maintained YAML have no `ph_value` or `preparation_steps`.
   - Impact: the generated recipe omits the final pH target that distinguishes this JCM tomato-juice MRS formulation.
   - Owner: `data/normalized_yaml/bacterial/TOGO_M838_MRS_Medium_With_10_Tomato_Juice.yaml`, then regenerate `data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml`.

4. JCM Medium 803 remains split across TOGO and MediaDive imports.
   - Evidence: `data/normalized_yaml/bacterial/TOGO_M838_MRS_Medium_With_10_Tomato_Juice.yaml` and `data/normalized_yaml/bacterial/mrs_medium_with_10_tomato_juice.yaml` both trace to GRMD 803.
   - Impact: the same JCM tomato-juice MRS medium can be emitted as two generated records instead of one merged record.
   - Owner: both normalized records plus the merge/de-duplication rule for equivalent TOGO and MediaDive JCM imports.

### Minor

1. The original JCM source URL is stale.
   - Evidence: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=803` currently returns `Nothing found`, while TOGO M838 still preserves the old formula.
   - Impact: the note still distinguishes the original JCM source, but curation has to use TOGO or another preserved capture unless JCM restores GRMD 803.
   - Owner: `data/normalized_yaml/bacterial/TOGO_M838_MRS_Medium_With_10_Tomato_Juice.yaml`.

### Blocker

None found.

## Recommended Edits

1. Convert `Distilled water` from 900 `G_PER_L` to a supported 900 ml volume representation.
2. Convert filtered tomato juice from 100 `G_PER_L` to a supported 100 ml volume representation.
3. Add pH 5.2 and a corresponding pH-adjustment preparation step from TOGO M838.
4. Reconcile the TOGO M838 and MediaDive/JCM J803 records so GRMD 803 no longer publishes twice.
5. Add a curation-history event to every changed normalized input and regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

After curation, run the same focused generated-record checks:

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml`
- `python scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml --workers 1 --quiet`
- `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_10_tomato_juice.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`

Also rerun merge freshness and an exact ignored-file-inclusive `GRMD=803` search to verify the old JCM 803 formulation is not still duplicated through TOGO and MediaDive.

## Additional Notes

None found.
