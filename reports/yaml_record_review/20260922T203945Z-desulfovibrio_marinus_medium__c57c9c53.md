# YAML Record Review: DESULFOVIBRIO MARINUS MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_marinus_medium__c57c9c53.yaml`
- Started UTC: 2026-09-22T20:39:45Z
- Finished UTC: 2026-09-22T20:40:51Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:002899` for `desulfovibrio_marinus_medium__c57c9c53`, a MediaDive import of JCM Medium J551 resolved from referenced JCM Medium J549.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `mediadive.medium:J551`, `DESULFOVIBRIO MARINUS MEDIUM`, with JCM GRMD 551 in `notes`.

MediaDive J551 is not a standalone full formula. It contains the instruction to use Medium No. 549 supplemented with final 50.0 g/L NaCl. The generated Marinus record copied `desulfovibrio_as36_medium` from JCM J549 and was then merged with J549 as an identical fingerprint, so the variant-defining NaCl supplement was not applied.

The TOGO M553 Marinus and TOGO M551 As36 provider records exist and are also merged together as `data/merge_yaml/merged/Desulfovibrio_Marinus_Medium.yaml`, so the same J551/J549 distinction likely needs repair on both provider paths.

## Evidence

MediaDive J551 exposes only `Main sol. J551` and a reference step: use Medium No. 549 with final 50.0 g/L NaCl.

MediaDive J549 has Solution A with 900 ml water, basal salts, 10 g NaCl, 1 ml Trace element solution, resazurin, and post-autoclave additions per 4.5 ml: 0.05 ml 10% yeast extract, 0.1 ml 1 M sodium lactate, 0.1 ml 15% magnesium chloride, 0.2 ml 5% sodium bicarbonate, and 0.05 ml 2% sodium sulfide.

## Completeness

The target preserves the J551 note as a preparation step, and its `parent_media` relation records that it copied composition from `desulfovibrio_as36_medium`.

The composition is incomplete for Marinus because the 50.0 g/L final NaCl supplement is absent. It is also incomplete for the inherited As36 formula because the 900 ml Solution A water row is absent, the 1 ml Trace element solution is flattened, and the five per-4.5-ml stock additions are present only as top-level `G_PER_L` rows.

## Findings

- Critical: JCM J551 Marinus and JCM J549 As36 were merged as duplicate recipes even though J551 is a salt-supplemented variant of J549. The generated target has the J551 identity but the unmodified J549 NaCl amount, 11.0865 G/L after Solution A scaling, instead of a final 50.0 G/L NaCl variant.
- High: The inherited J549 Trace element solution was flattened into HCl, iron, borate, manganese, cobalt, nickel, copper, zinc, and molybdate rows at stock-recipe strengths.
- High: The J549 completion stocks were flattened or copied from source volumes into masses. Yeast extract, sodium lactate, magnesium chloride, sodium bicarbonate, and sodium sulfide should be modeled as 0.05/0.1/0.1/0.2/0.05 ml additions per 4.5 ml medium.
- Medium: The 900 ml Solution A water row from JCM J549 is absent.
- Medium: The TOGO M553/M551 provider records have the same JCM source distinction and remain split from the MediaDive J551/J549 path in a separate generated record.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfovibrio_marinus_medium.yaml` so it expands JCM J551 as J549 plus the final 50.0 g/L NaCl supplement rather than a raw copy of J549.
- Remove the `SOURCE_DUPLICATE` relation between `desulfovibrio_marinus_medium` and `desulfovibrio_as36_medium`; it should be a salinity variant relation after the supplement is applied.
- Repair the referenced `data/normalized_yaml/bacterial/desulfovibrio_as36_medium.yaml` Solution A model so water, the Trace element stock, and the five per-4.5-ml additions are structured before J551 copies from it.
- Apply the same distinction and stock-solution repair to `TOGO_M553_Desulfovibrio_Marinus_Medium.yaml` and `TOGO_M551_Desulfovibrio_As36_Medium.yaml`.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and confirm J551 and J549 no longer collapse to the same `c57c9c5331b803afee8fcd32321645dfde53ce0de04486f44f5599576a0aa782` fingerprint.
- Confirm the regenerated Marinus composition has the J549 stock structure and the final 50.0 g/L NaCl variant amount.

## Additional Notes

None found.
