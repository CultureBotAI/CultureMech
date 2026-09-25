# YAML Record Review: halopiger_medium_sg

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halopiger_medium_sg.yaml`
- Started UTC: 2026-09-23T11:04:18Z
- Finished UTC: 2026-09-23T11:05:12Z
- Verdict: needs curation

## Target

Generated merged YAML for MediaDive/DSMZ medium 1520, `HALOPIGER MEDIUM (SG)`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:1520` and the DSMZ 1520 PDF.
- An ignored-file-inclusive exact search for `mediadive.medium:1520`, `DSMZ_Medium1520.pdf`, and `halopiger_medium_sg` found only the direct DSMZ 1520 import and its merged output.
- The NaCl, KCl, trisodium citrate, MgSO4 x 7 H2O, and agar groundings are appropriate.
- Yeast extract and Casamino acids are intentionally ungrounded undefined ingredients but lost their `Difco` qualifiers.

## Evidence

- DSMZ 1520 lists 250 g NaCl, 3 g KCl, 3 g trisodium citrate, 20 g MgSO4 x 7 H2O, 1 g Yeast extract (Difco), 7.5 g Casamino acids (Difco), 20 g agar if necessary, and distilled water to 1000 ml.
- DSMZ 1520 instructs adjustment to pH 8.0 before autoclaving.
- DSMZ 1520 also says that, if solid medium is prepared, agar and sodium chloride should be autoclaved separately.
- MediaDive 1520 preserves the two `Difco` attributes, the conditional agar row, the 1000 ml distilled-water row, and both preparation sentences.

## Completeness

- Missing final volume: the 1000 ml distilled-water row was dropped.
- Missing qualifiers: Yeast extract and Casamino acids lost `Difco`.
- Variant handling issue: a conditional agar row is represented in a single `SOLID_AGAR` record instead of a base recipe plus solid variant.

## Findings

1. The generated DSMZ 1520 record omits the 1000 ml distilled-water row.
2. Yeast extract and Casamino acids lost the source `Difco` qualifier.
3. The conditional 20 g agar row is modeled as part of a single `SOLID_AGAR` recipe instead of as a solid variant of the base medium.

## Recommended Edits

- Add distilled water with the correct 1000 ml final-volume representation.
- Restore `Difco` on Yeast extract and Casamino acids.
- Split the 20 g agar row into an explicit solid variant or otherwise scope its `if necessary` condition.
- Preserve the requirement that agar and sodium chloride are autoclaved separately for the solid form.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:1520` and `DSMZ_Medium1520.pdf` after regeneration.
- Verify that `ph_value: 8.0` and the MgSO4 x 7 H2O grounding are retained.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
