# YAML Record Review: ppes_ii_agar_medium__f3f6f93b

- Repository: CultureMech
- Record: data/merge_yaml/merged/ppes_ii_agar_medium__f3f6f93b.yaml
- Started UTC: 2026-09-24T21:43:15Z
- Finished UTC: 2026-09-24T21:43:15Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:008120
- Name: ppes_ii_agar_medium
- Source import: TOGO M1571 / NBRC_M374
- Primary external ID: TOGO:M1571
- Maintained input: data/normalized_yaml/bacterial/TOGO_M1571_PPES-II_Agar_Medium.yaml

This generated record represents the TOGO import of PPES-II Agar Medium from NBRC 374.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/ppes_ii_agar_medium__f3f6f93b.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

TOGO M1571 imports NBRC_M374, and the TOGO API and NBRC 374 page agree on the PPES-II Agar Medium formula: 2 g peptone, 1 g Bacto Proteose Peptone No.3 (Difco), 1 g Soytone, 1 g yeast extract, 0.1 g Fe(III)-EDTA, 15 g agar, 1 L artificial sea water, pH 7.8, and an artificial-sea-water subrecipe containing NaCl, KCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and 1 L distilled water.

The generated record is grounded to the right NBRC source but has a stale solution migration. It leaves the artificial-sea-water salts and 1 L distilled water flattened in `ingredients` while also adding an empty `solutions` entry named `Unknown solution` for 1 L `Artificial sea water*`, and that solution row is typed as `1 G_PER_L`.

Exact ignored-file searches across `data/normalized_yaml` and `data/merge_yaml` for `TOGO:M1571`, `NBRC_M374`, `NO=374`, `TOGO_M1571_PPES-II_Agar_Medium`, and `ppes_ii_agar_medium__f3f6f93b` found one normalized YAML and this generated record for the NBRC 374 import.

## Evidence

- TOGO M1571 has a main solution with 1 L `Artificial sea water*` and six non-seawater rows: peptone, Bacto Proteose Peptone No.3, Soytone, yeast extract, Fe(III)-EDTA, and agar.
- NBRC 374 lists the same main solution, pH 7.8, and an `Artificial sea water` subrecipe with NaCl, KCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and 1 L distilled water.
- The source-equivalent JCM 246 and DSMZ 1075 imports are emitted in a separate `ppes_ii_agar_medium` duplicate cluster rather than reconciled with this NBRC branch.

## Completeness

The generated record is incomplete and structurally incorrect against NBRC 374. It loses the artificial-sea-water boundary, duplicates the artificial-sea-water signal as both an empty solution and flattened salts, misstates the 1 L distilled-water row as 1 G_PER_L, misstates the 1 L artificial sea water solution as 1 G_PER_L, omits pH 7.8, and remains split from the related JCM / DSMZ PPES-II Agar records.

## Findings

1. Major: The 1 L `Artificial sea water*` row is migrated to an empty `solutions` entry with `1 G_PER_L`, while the same subrecipe's salts remain flattened into top-level ingredients.
2. Major: The artificial-sea-water subrecipe's 1 L distilled-water row remains flattened as a top-level `1 G_PER_L` water ingredient.
3. Major: The pH 7.8 source assertion is absent from the generated record.
4. Major: The NBRC 374 PPES-II Agar import is isolated from the related JCM 246 and DSMZ 1075 PPES-II Agar records instead of being deduplicated or deliberately variant-linked.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M1571_PPES-II_Agar_Medium.yaml` so the 1 L artificial sea water row is a real nested solution with the five salts and a 1 L distilled-water carrier, not both an empty solution and flattened top-level ingredients.
- Add the pH 7.8 assertion from TOGO M1571 / NBRC 374.
- Reconcile the NBRC 374 import with the JCM 246 and DSMZ 1075 PPES-II Agar branches before regeneration.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after normalized curation and regeneration.
- Run exact ignored-file searches for `TOGO:M1571`, `NBRC_M374`, `NO=374`, `JCM_M246`, and `mediadive.medium:1075` after regeneration.
- Spot-check regenerated output for a single 1 L artificial-sea-water ingredient, one nested artificial-sea-water recipe with 1 L distilled water, and pH 7.8.

## Additional Notes

None found.
