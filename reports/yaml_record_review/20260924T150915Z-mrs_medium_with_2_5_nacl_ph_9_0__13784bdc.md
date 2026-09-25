# YAML Record Review: MRS MEDIUM WITH 2.5% NaCl (pH 9.0)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.yaml
- Started UTC: 2026-09-24T15:08:19Z
- Finished UTC: 2026-09-24T15:09:15Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:003279` / `mrs_medium_with_2_5_nacl_ph_9_0` at `data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.yaml`.

- Canonical generated source: `data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl_ph_9_0.yaml`
- Other merged sources: `data/normalized_yaml/bacterial/mrs_medium_with_10_nacl.yaml`, `data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl.yaml`
- Merge fingerprint: `13784bdcac51e18e3ee128152f6a2c03b9e14bae59f1f4ddda5748c04d1b9d9b`
- Category: `bacterial`
- Medium term: `mediadive.medium:J931`, label `MRS MEDIUM WITH 2.5% NaCl (pH 9.0)`
- Source: JCM GRMD 931

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.yaml` | Passed. |
| Strict validator with `scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.yaml --out /private/tmp/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator with `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were applicable. |
| Term validator with `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` events. |

## Identity and Grounding

The record claims to be MediaDive/JCM J931, the JCM MRS MEDIUM WITH 2.5% NaCl at pH 9.0. JCM GRMD 931 supports that identity and lists 55 g Lactobacilli MRS broth (BD-Difco), 25 g NaCl, 15 g Bacto agar (BD-Difco), 1 L distilled water, and pH adjustment to 9.0.

The maintained MediaDive/JCM J931 owner preserves 25 g/L NaCl, pH 9.0, and the adjust-pH step. The generated merge is wrong because it absorbed the J257 10% NaCl source and now emits NaCl at 100 `G_PER_L`.

The exact `CultureMech:003279` search across `data/normalized_yaml` and `data/merge_yaml` used `rg --no-ignore --hidden`. It found the maintained J931 owner, this generated merge, generated indexes, and the reciprocal child reference in `data/normalized_yaml/bacterial/mrs_medium_with_10_nacl.yaml`.

## Evidence

JCM GRMD 931 directly supports the 2.5% NaCl pH 9.0 formulation. The inspected TOGO M977 mirror preserves the same GRMD 931 identity, ingredients, and pH. An exact ignored-file-inclusive search for `GRMD=931` found only the JCM/MediaDive owner, the TOGO M977 owner, and their generated outputs, so these two are the direct duplicate records for GRMD 931.

The three MediaDive normalized sources merged into this generated record are distinct before merging:

| Source | Formula distinction |
|---|---|
| `mrs_medium_with_10_nacl.yaml` / J257 | 100 g/L NaCl; no pH 9.0 field. |
| `mrs_medium_with_2_5_nacl.yaml` / J596 | 25 g/L NaCl; no pH 9.0 field. |
| `mrs_medium_with_2_5_nacl_ph_9_0.yaml` / J931 | 25 g/L NaCl and pH 9.0. |

The `kg_microbe_match` on all three maintained MediaDive inputs points to `mediadive.medium:101`, which resolves to DSMZ Medium 101, NUTRIENT AGAR or BROTH WITH NaCl, a different formula.

## Completeness

The generated record has the wrong NaCl concentration for J931, omits the 1 L water row from JCM GRMD 931, and has stale cross-source merge provenance. Its pH 9.0 value and pH-adjustment step are present.

No target-organism or growth-metric block is present. JCM GRMD 931 only defines the recipe, so those empty optional slots are not defects.

## Findings

### Major

1. The merge conflates a 10% NaCl parent with 2.5% NaCl variants.
   - Evidence: J257 has 100 g/L NaCl; J596 and J931 have 25 g/L NaCl. The generated J931 record lists 100 `G_PER_L` while saying the NaCl concentration was decreased to 25 g/L.
   - Impact: the record denotes a 2.5% NaCl pH 9.0 medium but emits the 10% NaCl formula.
   - Owner: the merge/de-duplication rule for J257, J596, and J931, then regenerate `data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.yaml`.

2. The JCM/MediaDive import omits the 1 L water row.
   - Evidence: JCM GRMD 931 lists 1 L distilled water; `data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl_ph_9_0.yaml` and this generated record have no water ingredient.
   - Impact: the base solvent is absent from the J931 formula.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl_ph_9_0.yaml`, then regenerate.

3. `kg_microbe_match` points to a different medium.
   - Evidence: the maintained J257, J596, and J931 records carry `kg_microbe_match: mediadive.medium:101`; `mediadive.medium:101` is DSMZ Medium 101, NUTRIENT AGAR or BROTH WITH NaCl.
   - Impact: the NaCl MRS salinity family is linked to an unrelated DSMZ nutrient agar or broth recipe.
   - Owner: the affected MediaDive normalized NaCl MRS records.

4. JCM GRMD 931 remains split across TOGO and MediaDive imports.
   - Evidence: `data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl_ph_9_0.yaml` and `data/normalized_yaml/bacterial/TOGO_M977_MRS_Medium_With_2.5_NaCl_pH_9.0.yaml` both cite GRMD 931.
   - Impact: after the salinity merge is fixed, the same JCM pH 9.0 variant can still publish twice unless equivalent TOGO and MediaDive JCM imports are reconciled.
   - Owner: both normalized records plus the merge/de-duplication rule for equivalent TOGO and MediaDive JCM imports.

### Minor

1. BD-Difco qualifiers are not preserved on the J931 imported product rows.
   - Evidence: JCM GRMD 931 lists `Lactobacilli MRS broth (BD-Difco)` and `Bacto agar (BD-Difco)`; the MediaDive/JCM record stores only `Lactobacilli MRS broth` and `Agar`.
   - Impact: the formula amounts are correct in the maintained J931 owner, but source supplier wording is lost.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl_ph_9_0.yaml`.

### Blocker

None found.

## Recommended Edits

1. Split the J257 10% NaCl, J596 2.5% NaCl, and J931 2.5% NaCl pH 9.0 MediaDive records into distinct generated outputs; keep salinity and pH-variant relationships as metadata instead of merging their ingredient lists.
2. Add the missing 1 L distilled-water row to `data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl_ph_9_0.yaml`.
3. Remove or correct the unrelated `mediadive.medium:101` KG-Microbe match from the MediaDive NaCl MRS family.
4. Preserve the BD-Difco qualifiers on the J931 MRS broth and agar product rows.
5. Reconcile MediaDive/JCM J931 with the TOGO M977 duplicate after the merge no longer crosses distinct salinity variants.
6. Append curation-history events to changed normalized inputs and regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

After curation, run the same focused generated-record checks:

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.yaml`
- `python scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.yaml --workers 1 --quiet`
- `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`

Also rerun the merge audit and an exact ignored-file-inclusive `GRMD=931` search to verify J931 and M977 merge together without absorbing the J257 10% NaCl or J596 pH-unspecified variants.

## Additional Notes

None found.
