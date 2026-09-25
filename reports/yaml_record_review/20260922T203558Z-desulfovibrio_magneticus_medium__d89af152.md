# YAML Record Review: DESULFOVIBRIO MAGNETICUS MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_magneticus_medium__d89af152.yaml`
- Started UTC: 2026-09-22T20:35:58Z
- Finished UTC: 2026-09-22T20:36:58Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:002755` for `desulfovibrio_magneticus_medium__d89af152`, a MediaDive import of JCM Medium J399.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The reviewed record is grounded to `mediadive.medium:J399`, `DESULFOVIBRIO MAGNETICUS MEDIUM`, with JCM GRMD 399 preserved in `notes`.

TOGO M395 is the same JCM_M399 recipe and remains split as `data/merge_yaml/merged/DESULFOVIBRIO_MAGNETICUS_MEDIUM.yaml`. A KOMODO/DSMZ 896 record with the same medium title also exists, but it uses DSMZ provenance rather than the JCM M399 identifier reviewed here.

## Evidence

MediaDive J399 represents the recipe as `Main sol. J399`, volume 1014 ml, with 0.2 g `K2HPO4`, 0.06 g `NH4Cl`, 2 ml Fe(III) quinate solution, 4 ml Trace minerals, 8 ml Trace vitamins, 0.58 g sodium fumarate, 0.44 g sodium pyruvate, 0.05 g cysteine hydrochloride hydrate, and 1000 ml distilled water.

The Fe(III) quinate stock is a 100 ml solution containing ferric chloride hexahydrate, quinic acid, and water. The Trace minerals and Trace vitamins stocks are 1000 ml solutions with their own water rows and preparation context.

## Completeness

The target preserves the JCM pH 7.0 and both preparation instructions: anaerobic preparation under nitrogen, and the nitrilotriacetic-acid trace-mineral pH adjustment.

It does not preserve the three stock additions or the 1000 ml main water row structurally. All Fe(III) quinate, Trace minerals, and Trace vitamins components are promoted into final ingredients at their stock recipe strengths.

## Findings

- High: The 2 ml Fe(III) quinate solution addition was flattened into final `FeCl3 x 6 H2O` 4.5 G/L and quinic acid 1.9 G/L ingredient rows instead of a 2 ml stock addition.
- High: The 4 ml Trace minerals addition was flattened. Nitrilotriacetic acid, magnesium sulfate, manganese sulfate, sodium chloride, ferrous sulfate, cobalt sulfate, calcium chloride, zinc sulfate, copper sulfate, potassium aluminum sulfate, boric acid, and sodium molybdate are listed at their 1000 ml stock concentrations as if they were final J399 concentrations.
- High: The 8 ml Trace vitamins addition was flattened. Biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid should be nested in the Trace vitamins stock.
- Medium: The 1000 ml distilled-water row in `Main sol. J399` is absent from the generated MediaDive record.
- Medium: The exact TOGO M395 provider duplicate remains split and stores Fe(III) quinate, Trace minerals, and Trace vitamins as empty `Unknown solution` stubs with 2/4/8 values coerced to `G_PER_L`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfovibrio_magneticus_medium.yaml` so JCM J399 has a main solution with 1000 ml water and 2 ml, 4 ml, and 8 ml stock additions for Fe(III) quinate, Trace minerals, and Trace vitamins.
- Move the Fe(III) quinate, Trace minerals, and Trace vitamins stock recipes into subordinate `solutions` entries with their source water rows and preparation text.
- Repair `data/normalized_yaml/bacterial/TOGO_M395_Desulfovibrio_Magneticus_Medium.yaml` so the same three stock rows are real additions rather than empty stubs.
- Reconcile the repaired MediaDive and TOGO JCM M399 records as exact source duplicates during merge.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and confirm there is a single JCM M399 record, or a documented exact-duplicate relation if the MediaDive and TOGO provider imports intentionally remain separate.
- Confirm the regenerated composition has only the five direct main solutes plus 1000 ml water at the top level, with the three stock recipes nested below the 2/4/8 ml additions.

## Additional Notes

None found.
