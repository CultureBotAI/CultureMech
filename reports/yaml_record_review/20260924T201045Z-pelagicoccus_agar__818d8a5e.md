# YAML Record Review: pelagicoccus_agar

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/pelagicoccus_agar__818d8a5e.yaml`
- Started UTC: 2026-09-24T20:10:45Z
- Finished UTC: 2026-09-24T20:10:56Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pelagicoccus_agar__818d8a5e.yaml`, a generated `MediaRecipe` merge record.

- ID: `CultureMech:010080`
- Label: `pelagicoccus_agar`
- Category: `bacterial`
- Source term: `TOGO:M676`
- Physical state: `LIQUID`
- Maintained owner: `data/normalized_yaml/bacterial/TOGO_M676_Pelagicoccus_Agar.yaml`
- Generated from: `TOGO_M676_Pelagicoccus_Agar`

## Validation

- Passed: open LinkML validation of `data/merge_yaml/merged/pelagicoccus_agar__818d8a5e.yaml` against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`; the command exited 0 with no issues.
- Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pelagicoccus_agar__818d8a5e.yaml --out /private/tmp/pelagicoccus_agar__818d8a5e.strict.tsv --workers 1 --quiet`; the TSV contained only its header, so strict validation found 0 errors.
- Passed: focused `linkml-reference-validator validate data data/merge_yaml/merged/pelagicoccus_agar__818d8a5e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 0 references were checked.
- Passed: focused `linkml-term-validator validate-data data/merge_yaml/merged/pelagicoccus_agar__818d8a5e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
- Not checked: embedded `curation_history`; the documented `just validate-history` target validates standalone `history/` YAML rather than `MediaRecipe.curation_history` embedded in generated records.

## Identity and Grounding

`TOGO:M676` resolves to TOGO Medium M676, "Pelagicoccus Agar", with original source `JCM_M659-2` and source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=659`. JCM Medium 659 is the printed Pelagicoccus Agar recipe and includes a comment for the liquid formulation: use 37.4 g/L Marine Broth 2216 and 1.6 g/L R2A broth in the artificial seawater.

The generated record's `LIQUID` state is therefore supported even though the TOGO/JCM source title says "Agar". The generated record's TOGO identity, bacterial category, commercial broth ingredient labels, and water grounding to `CHEBI:15377` are coherent.

The current generated output is stale relative to its maintained owner. `data/normalized_yaml/bacterial/TOGO_M676_Pelagicoccus_Agar.yaml` was repaired on 2026-09-11, while this generated record still carries the 2026-08-06 merged form with imported volume-unit and solution-shape defects.

## Evidence

- TOGO M676 lists 250 ml Distilled water, 37.4 g Marine broth 2216 (BD-Difco), 1.6 g R2A broth (Daigo), and 750 ml Artificial seawater in the liquid variant.
- TOGO M676 also carries the pH comment `adjust pH to 7.5.`
- JCM Medium 659 lists the parent solid formulation with 55.1 g Marine agar 2216, 9.1 g R2A agar, 750.0 ml Artificial seawater, 250.0 ml Distilled water, and an inline Artificial seawater recipe.
- JCM Medium 659's inline Artificial seawater recipe lists 24.0 g NaCl, 7.0 g MgSO4 x 7 H2O, 5.3 g MgCl2 x 6 H2O, 0.7 g KCl, 0.1 g CaCl2 x 2 H2O, and 1.0 L Distilled water.
- The generated record preserves the 37.4 g/L Marine broth and 1.6 g/L R2A broth claims, but it changes `250 ml` Distilled water to `250 G_PER_L`, changes `750 ml` Artificial seawater to `750 G_PER_L`, drops the pH 7.5 target, and leaves Artificial seawater as an empty shell.

## Completeness

The generated record is materially incomplete because the 750 ml/L Artificial seawater addition has no salt recipe or stable CultureMech stock grounding, and the final pH is absent. The September maintained owner contains both the 750.0 ml/L Artificial seawater stock with its full composition and the pH 7.5 claim, so these are generated-output staleness gaps rather than unresolved source ambiguities.

The commercial Marine broth 2216 and R2A broth products are correctly left ungrounded in the maintained owner. Empty optional fields are not defects.

An ignored-inclusive exact search of `data`, `src`, and `scripts` for `TOGO:M676`, `JCM_M659-2`, `GRMD=659`, `CultureMech:010080`, and `TOGO_M676_Pelagicoccus_Agar` found the maintained owner, this generated record, sibling generated records for the JCM 659 solid parent and TOGO M675 source duplicate, and the September repair script.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated record encodes two source volumes as masses and leaves a required stock unresolved. | TOGO M676 lists 250 ml Distilled water and 750 ml Artificial seawater. JCM 659 prints the Artificial seawater salt composition inline. The generated record has `250 G_PER_L` water and `750 G_PER_L` `Artificial seawater (see Medium [M675])` with `composition: []`. | Future source-level edits belong in `data/normalized_yaml/bacterial/TOGO_M676_Pelagicoccus_Agar.yaml`; its 2026-09-11 repair already has `250.0 ML_PER_L` water and a 750.0 ml/L inline Artificial seawater stock. |
| Major | The generated record omits the pH 7.5 adjustment. | TOGO M676 says to adjust to pH 7.5 and JCM 659 prints the same pH. The generated record has no `ph_value` or preparation step for the pH adjustment. | `data/normalized_yaml/bacterial/TOGO_M676_Pelagicoccus_Agar.yaml`, already repaired with `ph_value: 7.5` and an `ADJUST_PH` step. |
| Minor | The generated record does not carry the repaired physical-state relationship to the JCM 659 solid agar record. | The generated record has only `merged_from: [TOGO_M676_Pelagicoccus_Agar]`; the maintained owner now links to `data/normalized_yaml/bacterial/pelagicoccus_agar.yaml` as a `PHYSICAL_STATE_VARIANT`. | `data/normalized_yaml/bacterial/TOGO_M676_Pelagicoccus_Agar.yaml`, already repaired with `parent_media` and `variant_relationship: PHYSICAL_STATE_VARIANT`. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/pelagicoccus_agar__818d8a5e.yaml` from `data/normalized_yaml/bacterial/TOGO_M676_Pelagicoccus_Agar.yaml` so the generated record carries the repaired `ML_PER_L` water and Artificial seawater volumes, the full Artificial seawater composition, pH 7.5, and the physical-state variant link.
2. If regeneration still produces an empty `Artificial seawater` solution or drops `ph_value`, fix the merge/import logic that reads maintained `solutions`, `preparation_steps`, and variant fields before rerunning the merge generator.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on the regenerated generated record.
- Diff the regenerated `pelagicoccus_agar__818d8a5e.yaml` against `data/normalized_yaml/bacterial/TOGO_M676_Pelagicoccus_Agar.yaml` and confirm it includes `250.0 ML_PER_L` Distilled water, a 750.0 ml/L Artificial seawater stock with six child components, `ph_value: 7.5`, and `variant_relationship: PHYSICAL_STATE_VARIANT`.
- Manually recheck the regenerated M676 record against TOGO M676 and JCM Medium 659 before closing the issue, because the liquid formula is derived from a comment on the solid JCM 659 source.

## Additional Notes

TOGO M675 was inspected because M676 imports `Artificial seawater (see Medium [M675])`; M675 itself is the solid Pelagicoccus Agar TOGO entry for the same JCM Medium 659 source, not a standalone Artificial seawater source. The curation repair handled this by embedding the JCM 659 Artificial seawater composition directly instead of treating M675 as the stock recipe.
