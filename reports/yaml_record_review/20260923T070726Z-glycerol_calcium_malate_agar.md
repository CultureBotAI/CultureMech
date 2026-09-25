# YAML Record Review: glycerol_calcium_malate_agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glycerol_calcium_malate_agar.yaml
- Started UTC: 2026-09-23T07:05:16Z
- Finished UTC: 2026-09-23T07:07:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:009943` |
| Name | `glycerol_calcium_malate_agar` |
| Original name | `Glycerol-Calcium Malate Agar` |
| Category | `bacterial` |
| Canonical media term | `TOGO:M54` |
| Merged sources | `TOGO_M54_Glycerol-Calcium_Malate_Agar` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glycerol_calcium_malate_agar.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glycerol_calcium_malate_agar.yaml --out /private/tmp/glycerol_calcium_malate_agar.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glycerol_calcium_malate_agar.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glycerol_calcium_malate_agar.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record is canonicalized to Togo M54 and traces to JCM Medium 62. The same JCM page is also imported through MediaDive as `mediadive.medium:J62`, and those two JCM 62 imports currently regenerate as separate `glycerol_calcium_malate_agar` records.

A gitignore-independent exact search for `TOGO:M54`, `JCM_M62`, `TOGO_M54_Glycerol-Calcium_Malate_Agar`, `Glycerol-Calcium_Malate_Agar`, and `glycerol_calcium_malate_agar` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found the Togo M54 parent, the MediaDive J62 parent, both generated records, and the expected source indexes.

The generated ingredient identities for ammonium chloride, dipotassium hydrogen phosphate, glycerol, and agar match the upstream JCM 62 formula. Calcium malate remains ungrounded.

## Evidence

JCM Medium 62 lists 10 g glycerol, 10 g calcium malate, 0.5 g NH4Cl, 0.5 g K2HPO4, 15 g agar, and 1 L distilled water, followed by the instruction `pH unadjusted.` Togo M54 and MediaDive J62 carry the same values.

The Togo branch retains the five non-water amounts, but represents `Distilled water` as `1 G_PER_L` and drops the JCM pH instruction. The MediaDive branch for the same JCM medium encodes water as a 1000 ml source amount and keeps `pH unadjusted.` as a preparation step.

The two JCM 62 imports are split in generated output: `glycerol_calcium_malate_agar.yaml` from Togo M54 and `glycerol_calcium_malate_agar__95b71d74.yaml` from MediaDive J62.

## Completeness

The record has a complete required ingredient table for the Togo import, but it is not a complete representation of JCM 62 until the source water unit and pH instruction are repaired and the duplicate JCM imports converge. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The JCM 62 formula is duplicated as separate Togo M54 and MediaDive J62 generated records. | Both imports point to `GRMD=62`; the formula values match, but their generated fingerprints differ and produce `glycerol_calcium_malate_agar.yaml` plus `glycerol_calcium_malate_agar__95b71d74.yaml`. | Togo/MediaDive normalization and merge fingerprint generation. |
| Major | The Togo M54 parent converts 1 L distilled water into `1 G_PER_L`. | JCM and Togo list `Distilled water` at 1 L; the generated Togo record has `value: '1'`, `unit: G_PER_L`. | Togo importer or water-unit migration for liter source rows. |
| Minor | The Togo branch drops the source `pH unadjusted.` instruction. | JCM 62 and the Togo API both include `pH unadjusted.`; the MediaDive J62 parent keeps it as a `MIX` preparation step, while the Togo M54 parent has no `preparation_steps`. | Togo importer comment-to-step migration. |
| Minor | Calcium malate is still ungrounded. | Both generated JCM 62 records leave `Calcium malate` without a `term` or `mediaingredientmech_chebi_term`. | Ingredient grounding curation. |

## Recommended Edits

1. Correct the Togo M54 water row to match the JCM/Togo source volume.
2. Preserve the Togo `pH unadjusted.` comment as a preparation step or an equivalent structured pH status.
3. Regenerate merged records and confirm Togo M54 and MediaDive J62 collapse to one generated JCM 62 recipe.
4. Add a calcium malate grounding if an appropriately specific CHEBI term is available.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the repaired generated record.
- Compare the regenerated ingredient table against JCM `GRMD=62`, Togo M54, and MediaDive J62.
- Re-run the exact gitignore-independent search for `TOGO:M54`, `JCM_M62`, `TOGO_M54_Glycerol-Calcium_Malate_Agar`, `Glycerol-Calcium_Malate_Agar`, and `glycerol_calcium_malate_agar` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify that only intentional JCM 62 generated records remain.

## Additional Notes

None found.
