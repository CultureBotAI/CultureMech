# YAML Record Review: nsy_medium_for_polynucleobacter

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/nsy_medium_for_polynucleobacter__f8203b11.yaml
- Started UTC: 2026-09-24T18:04:16Z
- Finished UTC: 2026-09-24T18:05:41Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:003885 |
| Name | nsy_medium_for_polynucleobacter |
| Original name | NSY-MEDIUM FOR POLYNUCLEOBACTER |
| Category | bacterial |
| Media term | komodo.medium:1167 / NSY-MEDIUM FOR POLYNUCLEOBACTER |
| Generated path | data/merge_yaml/merged/nsy_medium_for_polynucleobacter__f8203b11.yaml |
| Maintained sources | data/normalized_yaml/bacterial/KOMODO_1167_NSY-MEDIUM_FOR_POLYNUCLEOBACTER.yaml; data/normalized_yaml/bacterial/nsy_medium_for_polynucleobacter.yaml |
| Merge fingerprint | f8203b11819d6e880aa8d12ef4d05a3128f331156f8c8e988fa3abf584e529b5 |
| Merged from | KOMODO_1167_NSY-MEDIUM_FOR_POLYNUCLEOBACTER, nsy_medium_for_polynucleobacter |

This is a generated merge of the KOMODO 1167 import and its DSMZ Medium 1167 source duplicate. Future formula fixes belong in the maintained DSMZ/MediaDive normalized source before regenerating the KOMODO enrichment and merged YAML.

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/nsy_medium_for_polynucleobacter__f8203b11.yaml` | Passed with "No issues found". |
| Strict validation with `scripts/validate_strict.py data/merge_yaml/merged/nsy_medium_for_polynucleobacter__f8203b11.yaml --out /private/tmp/nsy_medium_for_polynucleobacter__f8203b11.strict.tsv --workers 1 --quiet` | Passed; the TSV contained only the header line. |
| Reference validation with `linkml-reference-validator validate data data/merge_yaml/merged/nsy_medium_for_polynucleobacter__f8203b11.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 total checks and no failures. |
| Term validation with `linkml-term-validator validate-data data/merge_yaml/merged/nsy_medium_for_polynucleobacter__f8203b11.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator validates standalone `history/` entries, not embedded generated `MediaRecipe.curation_history`. |

## Identity and Grounding

The record correctly denotes DSMZ Medium 1167 as mirrored through KOMODO 1167. The generated merge combines the KOMODO record and the local `mediadive.medium:1167` DSMZ source duplicate, and an ignored-file-inclusive search for `mediadive.medium:1167`, `komodo.medium:1167`, `DSMZ Medium 1167`, `NSY-MEDIUM FOR POLYNUCLEOBACTER`, and `KOMODO_1167_NSY-MEDIUM_FOR_POLYNUCLEOBACTER` across `data/normalized_yaml` and `data/merge_yaml/merged` found no additional active DSMZ 1167 mirrors outside these two normalized sources and this generated record.

This DSMZ 1167 medium should remain separate from the JCM 1230 NSY records because DSMZ 1167 is a liquid tap-water recipe with an optional inorganic substitute for tap water and Soy peptone, while JCM 1230 is a solid agar recipe with Phytone peptone.

## Evidence

The generated one-gram Nutrient broth, Soy peptone, and Yeast extract rows, pH 7.2 value, liquid state, and DSMZ/KOMODO source duplicate relationship are supported by DSMZ Medium 1167 and the KOMODO note that cites DSMZ 1167.

DSMZ 1167 does not support a single medium containing tap water, all inorganic replacement-solution salts, and all Trace element solution SL-4 components at once. The PDF lists Tap water as the base solvent, then separately says an inorganic solution with MgSO4 x 7 H2O, Ca(NO3)2 x 4 H2O, NaHCO3, KCl, K2HPO4 x 3 H2O, 0.1 ml Trace element solution SL-4, and distilled water may substitute for tap water. MediaDive expands the SL-4 recipe from DSM Medium 14, but those stock components are still part of the 0.1 ml/L SL-4 addition, not direct top-level ingredients of DSMZ 1167.

## Completeness

The generated record omits the preparation note that the inorganic solution may substitute for tap water, omits the pH-adjustment instruction as a step, and omits the SL-4 solution boundary. It also makes the KOMODO import canonical, so the generated record loses the DSMZ source URL and the DSMZ preparation details that are present in `data/normalized_yaml/bacterial/nsy_medium_for_polynucleobacter.yaml`.

Empty target-organism and citation slots are acceptable for this provider formula. No strain-specific target-organism source was present in the imported DSMZ or KOMODO sources.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Major | The DSMZ tap-water formula and inorganic replacement solution are flattened into one top-level ingredient list. | DSMZ 1167 lists Tap water in the main formula and describes the salt solution as a substitute for tap water. The generated record has Tap water plus MgSO4 x 7 H2O, Ca(NO3)2 x 4 H2O, NaHCO3, KCl, and K2HPO4 x 3 H2O as simultaneous ingredients. | MediaDive/DSMZ normalization for `data/normalized_yaml/bacterial/nsy_medium_for_polynucleobacter.yaml`, KOMODO enrichment from DSMZ 1167, then merged-record regeneration. |
| Major | The Trace element solution SL-4 stock was flattened to direct medium ingredients. | DSMZ 1167 adds 0.1 ml Trace element solution SL-4 from DSM Medium 14 to the optional inorganic solution. MediaDive has SL-4 as a nested solution, but the generated record stores Na2-EDTA, FeSO4 x 7 H2O, ZnSO4 x 7 H2O, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O directly at SL-4 stock concentrations. | MediaDive nested-solution import for DSMZ 1167 and DSM Medium 14, then downstream KOMODO and merged-record regeneration. |
| Major | DSMZ preparation semantics are lost in the generated KOMODO-canonical merge. | The maintained DSMZ source has steps for the inorganic solution substitution, pH 7.2 adjustment, and SL-4 EDTA stock preparation. The generated KOMODO-canonical record has `ph_value: 7.2` but no `preparation_steps`. | Merge precedence for DSMZ/KOMODO source duplicates. |

## Recommended Edits

1. Model Tap water as the default DSMZ 1167 solvent and the inorganic salt solution as an alternative substitute for that solvent, not as co-occurring top-level ingredients.
2. Preserve Trace element solution SL-4 as a 0.1 ml/L nested stock addition under the inorganic substitute solution.
3. Keep the DSMZ source URL and preparation semantics when merging KOMODO 1167 with its DSMZ 1167 parent.

## Follow-up Checks

1. Regenerate the DSMZ, KOMODO, and merged records, then verify the generated DSMZ 1167 NSY record separates Tap water from the inorganic substitute.
2. Verify that Trace element solution SL-4 owns the trace-metal and EDTA components instead of exposing them as top-level DSMZ 1167 ingredients.
3. Run the focused open schema, strict, reference, and term validators on `data/merge_yaml/merged/nsy_medium_for_polynucleobacter__f8203b11.yaml`.
4. Search with ignored files included for `mediadive.medium:1167`, `komodo.medium:1167`, and `DSMZ Medium 1167` to confirm only the intended DSMZ/KOMODO source pair contributes to the regenerated merge.

## Additional Notes

The generated record correctly does not merge with TOGO `M1322` / JCM `J1230`; those JCM records share the visible NSY medium name but describe a distinct agar recipe.
