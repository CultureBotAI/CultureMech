# YAML Record Review: Clostridium Thermocellum Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_thermocellum_medium__d9fc1f82.yaml`
- Started UTC: `2026-09-22T09:43:36Z`
- Finished UTC: `2026-09-22T09:43:47Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:010000` for TOGO Medium `M601`, generated from `data/normalized_yaml/bacterial/TOGO_M601_Clostridium_Thermocellum_Medium.yaml` on merge fingerprint `d9fc1f82db6e336c0b124668b16aa3cd8feb140080a8d099003969620cfd4119`.

The stated source is JCM Medium 595, `CLOSTRIDIUM THERMOCELLUM MEDIUM`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_thermocellum_medium__d9fc1f82.strict.tsv`.
- LinkML reference validation: passed.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The TOGO identity and JCM 595 source URL are recognizable, but this TOGO branch is not merged with the direct JCM branch `data/merge_yaml/merged/clostridium_thermocellum_medium__f6f3f236.yaml`, which points at the same JCM page and keeps the correct milligram conversions.

`Cellulose (Avicel or MN 300)` is unresolved even though the direct JCM branch grounds the normalized cellulose row to `CHEBI:18246`. Sodium beta-glycerophosphate is unresolved on the TOGO branch but grounded on the direct branch. `K2HPO4 x 3H2O` is grounded to generic dipotassium hydrogen phosphate rather than a trihydrate-specific term, if one exists.

## Evidence

The JCM Medium 595 page lists 1.3 g ammonium sulfate, 2.6 g MgCl2 x 6H2O, 1.43 g KH2PO4, 7.2 g K2HPO4 x 3H2O, 0.13 g CaCl2 x 2H2O, 6.0 g sodium beta-glycerophosphate, 1.1 mg FeSO4 x 7H2O, 0.25 g glutathione, 4.5 g yeast extract, 1.0 mg resazurin, 10.0 g cellulose, and 1.0 l water. It instructs pH adjustment to 7.0-7.2 and a 95% N2 / 5% CO2 gas atmosphere, and comments that cellulose can be replaced with 5 g/l cellobiose added from a filter-sterilized 10% w/v stock.

The TOGO API confirms that `M601` points to JCM `GRMD=595` and carries pH `7.0-7.2`.

The ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found both this TOGO branch and the direct JCM generated branch for exact JCM 595 URL tokens; ignored files were included.

## Completeness

The record misses several JCM facts:

- pH 7.0-7.2 is absent from `ph_range`.
- The 95% N2 / 5% CO2 atmosphere is flattened into variable `Carbon dioxide gas` and `Nitrogen gas` ingredients.
- The cellobiose-for-cellulose replacement comment is absent.
- Water is stored as `1 G_PER_L` rather than omitted or represented as 1 liter of solvent.

## Findings

- Milligram source rows were converted as if they were grams. JCM lists `FeSO4 x 7H2O` at 1.1 mg and `Resazurin` at 1.0 mg, but the TOGO record stores `FeSO4 x 7H2O` as `1.1 G_PER_L` and `Resazurin` as `1 G_PER_L`.
- `Distilled water` is stored as `1 G_PER_L`, carrying the numeric value from the source `1.0 L` water row with the wrong unit semantics.
- JCM pH and gas atmosphere instructions are missing from structured preparation fields.
- `Carbon dioxide gas` and `Nitrogen gas` were defaulted to variable-concentration ingredients even though the source only describes a gas atmosphere.
- The direct JCM branch is unmerged solely because it normalizes the same source more correctly, including `0.0011 G_PER_L` FeSO4 and `0.001 G_PER_L` resazurin.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/TOGO_M601_Clostridium_Thermocellum_Medium.yaml` or the TOGO import unit handling, then regenerate; `data/merge_yaml/merged/clostridium_thermocellum_medium__d9fc1f82.yaml` is derived.
- Convert JCM milligram rows to grams per liter instead of preserving source mg magnitudes as grams.
- Add pH 7.0-7.2 and the 95% N2 / 5% CO2 gas atmosphere as preparation metadata rather than gas ingredients.
- Ground cellulose and sodium beta-glycerophosphate consistently with the direct JCM branch.
- Merge this TOGO branch with the direct JCM branch after the two imports agree on units.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm FeSO4 and resazurin match the direct JCM branch at 0.0011 and 0.001 g/l.
- Confirm no water row remains as `1 G_PER_L`.
- Confirm the cellobiose replacement comment is preserved either as a variant or as a source note.

## Additional Notes

Empty optional fields are not defects. This record is a compact example of a TOGO unit slip: gram rows are mostly correct, while milligram and liter rows carry the right source numbers with the wrong unit semantics.
