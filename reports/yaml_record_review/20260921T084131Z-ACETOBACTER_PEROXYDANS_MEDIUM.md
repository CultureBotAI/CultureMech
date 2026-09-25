# YAML Record Review: ACETOBACTER PEROXYDANS MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETOBACTER_PEROXYDANS_MEDIUM.yaml
- Started UTC: 2026-09-21T08:40:14Z
- Finished UTC: 2026-09-21T08:41:31Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETOBACTER_PEROXYDANS_MEDIUM.yaml`.
- Stable identifier: `CultureMech:004656`.
- Source identity asserted by the canonical record: KOMODO ModelSEED `254`, copied from DSMZ Medium 254 / MediaDive `mediadive.medium:254`.
- The generated record was merged from `KOMODO_254_ACETOBACTER_PEROXYDANS_medium` and `acetobacter_peroxydans_medium` on fingerprint `5d5a1f2033a64a98948717cd80c153cc11f050418504c6d664ae3365b392e247`.
- Current authoritative source owners: `data/normalized_yaml/bacterial/KOMODO_254_ACETOBACTER_PEROXYDANS_medium.yaml` and `data/normalized_yaml/bacterial/acetobacter_peroxydans_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETOBACTER_PEROXYDANS_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETOBACTER_PEROXYDANS_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETOBACTER_PEROXYDANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETOBACTER_PEROXYDANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- DSMZ Medium 254 resolves and identifies the source as `254: ACETOBACTER PEROXYDANS MEDIUM`.
- The KOMODO/DSMZ duplicate relationship is coherent: the KOMODO owner says it copied DSMZ Medium 254, the direct owner carries `mediadive.medium:254`, and their local ingredient signatures match exactly.
- A bounded gitignore-independent exact search for `komodo.medium:254`, `mediadive.medium:254`, `DSMZ_Medium254.pdf`, `ACETOBACTER_PEROXYDANS_MEDIUM`, and `acetobacter_peroxydans_medium` found the expected normalized owners, the expected source-index rows, and the merged generated record.

## Evidence

- DSMZ Medium 254 directly lists 15.0 g malt extract, 5.0 g yeast extract, 15.0 g agar, and 940.0 ml distilled water.
- DSMZ then instructs adding `60 ml ethanol (50% v/v)`, sterilized by filtration, after the base is sterilized.
- The generated record represents that post-sterilization ethanol solution as `Ethanol` at `60 G_PER_L`, which treats a 60 ml addition of 50% v/v ethanol as 60 g/L pure ethanol.
- The direct DSMZ owner preserves the "After sterilization add 60 ml ethanol (50% v/v)" preparation step, and the KOMODO owner has copied the same `60 G_PER_L` ethanol row from DSMZ.

## Completeness

- The 940 ml distilled water row is absent.
- The post-sterilization ethanol solution is not represented as a 60 ml/L stock or solution addition, so the final record loses that the added solution is 50% v/v ethanol.
- The duplicate relationship is complete: the generated record correctly merges the KOMODO and direct DSMZ owners as source duplicates.

## Findings

- BLOCKER: the generated `60 G_PER_L` ethanol concentration misrepresents DSMZ's post-sterilization `60 ml` addition of `50% v/v` ethanol.
- MAJOR: both normalized owners carry the same ethanol conversion defect, so the incorrect concentration will remain until `data/normalized_yaml` is repaired and the merge is regenerated.
- MINOR: the canonical KOMODO owner says `Aerobic: No`, but DSMZ Medium 254 does not encode an anaerobic handling instruction.
- MINOR: `data/normalized_yaml/bacterial/KOMODO_254_ACETOBACTER_PEROXYDANS_medium.yaml` retains malformed curation history timestamp `2026-01-27T01:15:02.fZ`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/acetobacter_peroxydans_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_254_ACETOBACTER_PEROXYDANS_medium.yaml` so the post-sterilization ethanol addition preserves both the `60 ml/L` volume and the `50% v/v` solution strength.
- Keep the direct malt extract, yeast extract, and agar rows unchanged.
- Remove or verify the KOMODO `Aerobic: No` note against KOMODO's source table before carrying it into the canonical generated record.
- Regenerate `data/merge_yaml/merged/ACETOBACTER_PEROXYDANS_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium254.pdf` and verify the regenerated recipe still represents malt extract at 15 g/L, yeast extract at 5 g/L, agar at 15 g/L, and ethanol as a 60 ml/L addition of 50% v/v solution.
- Re-run ignored-file-inclusive exact searches for `komodo.medium:254`, `mediadive.medium:254`, and `ACETOBACTER_PEROXYDANS_MEDIUM` to confirm the repaired KOMODO/DSMZ source-duplicate pair remains merged.

## Additional Notes

- Optional empty fields were not treated as defects.
