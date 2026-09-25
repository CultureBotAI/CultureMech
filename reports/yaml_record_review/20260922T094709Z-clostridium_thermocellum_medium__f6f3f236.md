# YAML Record Review: CLOSTRIDIUM THERMOCELLUM MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_thermocellum_medium__f6f3f236.yaml`
- Started UTC: `2026-09-22T09:47:09Z`
- Finished UTC: `2026-09-22T09:47:24Z`
- Verdict: pass with minor issues

## Target

Generated bacterial `MediaRecipe` record `CultureMech:002943` for JCM Medium `J595`, generated from `data/normalized_yaml/bacterial/clostridium_thermocellum_medium.yaml` on merge fingerprint `f6f3f2369baf3d5f0ba5e4c2554000c7ab0615490920475c17df87b2c27e2460`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_thermocellum_medium__f6f3f236.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The JCM identity is correct: the record links to JCM `GRMD=595`, names JCM Medium 595, and preserves the same ingredient list as the source page.

Most problematic ingredients from the TOGO import are normalized here. `Cellulose` is grounded to `CHEBI:18246`, sodium beta-glycerophosphate is grounded to `CHEBI:132089`, `FeSO4 x 7 H2O` is correctly converted from 1.1 mg to `0.0011 G_PER_L`, and `Resazurin` is correctly converted from 1.0 mg to `0.001 G_PER_L`.

`K2HPO4 x 3 H2O` is grounded to generic dipotassium hydrogen phosphate rather than a trihydrate-specific term, if one exists.

## Evidence

The JCM Medium 595 page supports all generated final ingredients: 1.3 g ammonium sulfate, 2.6 g MgCl2 x 6H2O, 1.43 g KH2PO4, 7.2 g K2HPO4 x 3H2O, 0.13 g CaCl2 x 2H2O, 6.0 g sodium beta-glycerophosphate, 1.1 mg FeSO4 x 7H2O, 0.25 g glutathione, 4.5 g yeast extract, 1.0 mg resazurin, 10.0 g cellulose, and 1.0 l distilled water.

The JCM page also supports the three preparation/source-note facts retained in `preparation_steps`: adjust pH to 7.0-7.2, use a 95% N2 / 5% CO2 gas atmosphere, and optionally replace cellulose with 5.0 g/l cellobiose from a filter-sterilized 10% w/v solution.

The ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found this direct JCM branch and the separate TOGO `M601` branch for exact JCM 595 URL tokens; ignored files were included.

## Completeness

The generated record is mostly complete for the source formula and notes.

The only source fact represented less precisely is pH: JCM gives a range of 7.0-7.2, while this record stores only `ph_value: 7.1`.

No target organism is listed.

## Findings

- Minor: pH is collapsed from source range 7.0-7.2 to midpoint value `7.1`.
- Minor: `K2HPO4 x 3 H2O` is grounded to generic dipotassium hydrogen phosphate.
- Minor: the separate TOGO `M601` branch is not merged with this direct JCM branch because that import has milligram-to-gram slips for FeSO4 and resazurin.

## Recommended Edits

- Preserve pH 7.0-7.2 as `ph_range` rather than a midpoint value.
- Use a trihydrate-specific grounding for `K2HPO4 x 3 H2O` if one exists.
- After fixing TOGO `M601` unit handling, regenerate and confirm the TOGO and direct JCM branches merge.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm FeSO4 and resazurin remain at 0.0011 and 0.001 g/l.
- Confirm the cellobiose substitution comment survives any pH or duplicate-merge regeneration.

## Additional Notes

No formula-level curation issues were found in this direct JCM branch. Empty optional fields are not defects.
