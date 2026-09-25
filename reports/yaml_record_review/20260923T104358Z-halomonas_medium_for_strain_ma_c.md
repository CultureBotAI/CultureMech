# YAML Record Review: halomonas_medium_for_strain_ma_c

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halomonas_medium_for_strain_ma_c.yaml`
- Started UTC: 2026-09-23T10:43:58Z
- Finished UTC: 2026-09-23T10:45:07Z
- Verdict: needs curation

## Target

Generated merged YAML for MediaDive/DSMZ medium 1428, `HALOMONAS MEDIUM FOR STRAIN MA-C`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:1428` and the DSMZ 1428 PDF.
- An ignored-file-inclusive exact search for `mediadive.medium:1428`, `DSMZ_Medium1428.pdf`, and `halomonas_medium_for_strain_ma_c` found only the direct MediaDive/DSMZ import and its merged output.
- The NaCl, magnesium chloride hexahydrate, KCl, Na2SO4, and agar groundings are appropriate.
- Yeast extract and tryptone are intentionally ungrounded undefined ingredients.

## Evidence

- DSMZ 1428 lists 100 g NaCl, 10 g MgCl2 x 6 H2O, 1 g KCl, 0.5 g Na2SO4, 5 g yeast extract, 5 g tryptone, and 1000 ml distilled water.
- The DSMZ preparation text says to adjust to pH 7.0 and states that the medium may be solidified by adding 20.0 g/L agar.
- MediaDive 1428 preserves the same ingredient values, carries `min_pH: 7` and `max_pH: 7`, and represents agar as a 20 g conditional row with `condition: for solid medium`.

## Completeness

- Missing ingredient: the explicit 1000 ml distilled-water row was dropped.
- Variant handling issue: conditional agar is present as a 20 g/L ingredient in a `SOLID_AGAR` record, while the retained instruction still describes agar as optional for solidification.

## Findings

1. The generated DSMZ 1428 record omits the 1000 ml distilled-water row.
2. The conditional agar row is modeled as part of a single `SOLID_AGAR` recipe instead of as a solid variant of the base liquid medium.
3. The pH-adjustment sentence is present only as a generic `MIX` step even though its first clause is pH adjustment.

## Recommended Edits

- Add distilled water with the correct 1000 ml final-volume representation.
- Split the base liquid DSMZ 1428 recipe from the optional 20 g/L solid agar variant or otherwise scope agar with an explicit `for solid medium` condition.
- Model `Adjust to pH 7.0` as `ADJUST_PH`; keep the solidification clause on the agar variant.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:1428` and `DSMZ_Medium1428.pdf` after regeneration.
- Verify that the regenerated record retains `ph_value: 7.0` and the magnesium chloride hexahydrate grounding.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
