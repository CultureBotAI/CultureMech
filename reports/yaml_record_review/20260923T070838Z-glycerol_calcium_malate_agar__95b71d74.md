# YAML Record Review: glycerol_calcium_malate_agar__95b71d74

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glycerol_calcium_malate_agar__95b71d74.yaml
- Started UTC: 2026-09-23T07:08:06Z
- Finished UTC: 2026-09-23T07:08:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:002976` |
| Name | `glycerol_calcium_malate_agar` |
| Original name | `GLYCEROL-CALCIUM MALATE AGAR` |
| Category | `bacterial` |
| Canonical media term | `mediadive.medium:J62` |
| Merged sources | `glycerol_calcium_malate_agar` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glycerol_calcium_malate_agar__95b71d74.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glycerol_calcium_malate_agar__95b71d74.yaml --out /private/tmp/glycerol_calcium_malate_agar__95b71d74.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glycerol_calcium_malate_agar__95b71d74.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glycerol_calcium_malate_agar__95b71d74.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record is canonicalized to MediaDive J62 and traces to JCM Medium 62. The same JCM page is also imported through Togo M54, and those two JCM 62 imports currently regenerate as separate `glycerol_calcium_malate_agar` records.

A gitignore-independent exact search for `TOGO:M54`, `JCM_M62`, `TOGO_M54_Glycerol-Calcium_Malate_Agar`, `Glycerol-Calcium_Malate_Agar`, and `glycerol_calcium_malate_agar` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found the MediaDive J62 parent, the Togo M54 parent, both generated records, and the expected source indexes.

The generated ingredient identities for glycerol, ammonium chloride, dipotassium hydrogen phosphate, and agar match the JCM 62 and MediaDive formulas. Calcium malate remains ungrounded.

## Evidence

JCM Medium 62 lists 10 g glycerol, 10 g calcium malate, 0.5 g NH4Cl, 0.5 g K2HPO4, 15 g agar, and 1 L distilled water, followed by the instruction `pH unadjusted.` MediaDive J62 exposes the same five dry ingredients at the same final g/l values and carries the same pH instruction.

The generated MediaDive record preserves the five final g/l values and its `pH unadjusted.` step, so it is more faithful than the split Togo M54 record. The defect is that it is still a separate generated recipe for the same JCM formula because the Togo branch carries a malformed `1 G_PER_L` water row and lacks the pH step.

## Completeness

The record represents the MediaDive J62 final-concentration table and pH instruction, but the generated corpus is incomplete while the same JCM medium is split into a separate Togo M54 record. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | JCM 62 is duplicated as separate MediaDive J62 and Togo M54 generated records. | Both imports point to `GRMD=62`; the formula values match, but their generated fingerprints differ and produce `glycerol_calcium_malate_agar__95b71d74.yaml` plus `glycerol_calcium_malate_agar.yaml`. | Togo/MediaDive normalization and merge fingerprint generation. |
| Minor | Calcium malate is still ungrounded. | The MediaDive and Togo generated records both leave `Calcium malate` without a `term` or `mediaingredientmech_chebi_term`. | Ingredient grounding curation. |

## Recommended Edits

1. Repair the Togo M54 source row for water and its missing `pH unadjusted.` step so it can be compared fairly against MediaDive J62.
2. Regenerate merged records and confirm JCM 62 collapses to one generated `glycerol_calcium_malate_agar` recipe.
3. Add a calcium malate grounding if an appropriately specific CHEBI term is available.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated JCM 62 record.
- Compare the final ingredient table against JCM `GRMD=62`, Togo M54, and MediaDive J62.
- Re-run the exact gitignore-independent search for `TOGO:M54`, `JCM_M62`, `TOGO_M54_Glycerol-Calcium_Malate_Agar`, `Glycerol-Calcium_Malate_Agar`, and `glycerol_calcium_malate_agar` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify that only intentional JCM 62 generated records remain.

## Additional Notes

None found.
