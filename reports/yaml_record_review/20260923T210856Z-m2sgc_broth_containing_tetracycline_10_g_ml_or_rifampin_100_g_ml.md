# YAML Record Review: M2SGC broth containing tetracycline (10 ug/ml) or rifampin (100 ug/ml)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/m2sgc_broth_containing_tetracycline_10_g_ml_or_rifampin_100_g_ml.yaml`
- Started UTC: 2026-09-23T21:07:42Z
- Finished UTC: 2026-09-23T21:08:56Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/m2sgc_broth_containing_tetracycline_10_g_ml_or_rifampin_100_g_ml.yaml`
- Maintained owner: `data/normalized_yaml/bacterial/m2sgc_broth_containing_tetracycline_10_g_ml_or_rifampin_100_g_ml.yaml`
- CultureMech ID: `CultureMech:009336`
- Media term: `TOGO:M2789`
- Merge fingerprint: `2133af473e424d7ceec4736c3a0c9b2342be047a430cee01716da2975fbbb98e`
- Merge sources: `m2sgc_broth_containing_tetracycline_10_g_ml_or_rifampin_100_g_ml`
- Ignored-inclusive exact searches over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the single maintained TOGO owner, the generated one-source merge, generated indexes, and archived validation rows that referenced the owner's former non-ASCII filename.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/m2sgc_broth_containing_tetracycline_10_g_ml_or_rifampin_100_g_ml.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The record represents TOGO Medium `M2789`, `M2SGC broth containing tetracycline (10 ug/ml) or rifampin (100 ug/ml)`. The inspected TOGO API confirms that identity and shows a top-level 100 ml M2SGC base under 100% CO2 with either tetracycline at 10 ug/ml or rifampin at 100 ug/ml.

The maintained owner already grounds tetracycline to `CHEBI:27902`, but the generated merge predates that August 2026 grounding. The generated and maintained records both flatten the nested M2SGC base into the final ingredient list and keep `M2SGC medium` itself as a top-level ingredient, so the ingredient list does not faithfully represent the source hierarchy.

## Evidence

- TOGO `M2789` encodes `Tetracycline` at `10 ug/ml`, `M2SGC medium` at 100 ml, and `CO2` at 100% in the top-level component.
- The same TOGO response defines the `M2SGC medium` subcomponent per 100 ml with 100 ml distilled water, 0.009 g MgSO4 x 7 H2O, 0.25 g yeast extract, 0.09 g NaCl, 0.045 g KH2PO4, 0.045 g K2HPO4, 0.1 mg resazurin, 0.4 g NaHCO3, 0.09 g ammonium sulfate, 0.009 g CaCl2, 0.2 g each cellobiose, glucose, and soluble starch, 30 ml clarified rumen fluid, 0.1 g cysteine, and 1 g Casitone.
- TOGO comment text also preserves the biological growth context: routine anaerobic 37 C growth in M2SGC broth with 10 ug/ml tetracycline or 100 ug/ml rifampin, and either Bellco tubes under 100% CO2 or an anaerobic cabinet atmosphere of 10% CO2, 10% H2, and 80% N2.

## Completeness

The generated record is incomplete for antibiotic alternatives because rifampin is present in the source name and comment but absent from the ingredient list. It is also incomplete for source hierarchy: a 100 ml M2SGC base should be represented as a base solution whose own per-100-ml recipe is scaled or scoped correctly, not as both a `100 G_PER_L` ingredient and duplicated flattened ingredients.

The generated record is stale relative to `data/normalized_yaml/bacterial/m2sgc_broth_containing_tetracycline_10_g_ml_or_rifampin_100_g_ml.yaml`, which now has a direct tetracycline CHEBI term from `apply_mim_groundings.py`.

## Findings

1. **Blocker - the tetracycline concentration is off by a factor of 1000 and the rifampin alternative is absent.** TOGO states tetracycline at 10 ug/ml, equivalent to 0.01 g/L, or rifampin at 100 ug/ml, equivalent to 0.1 g/L. The YAML stores tetracycline as `10 G_PER_L` and does not model rifampin at all.

2. **Blocker - the per-100-ml M2SGC base is flattened with unscaled quantities.** The TOGO subcomponent lists M2SGC components per 100 ml, but the YAML stores those numeric values as `G_PER_L`. That makes gram-scale base ingredients such as 1 g Casitone and 0.2 g glucose tenfold too low, while the 0.1 mg resazurin row is represented as `0.1 G_PER_L` rather than 0.001 g/L.

3. **Major - the recipe keeps a self-referential base-medium row.** The top-level source adds 100 ml M2SGC medium, then defines M2SGC as the base formula. The YAML stores `M2SGC medium` as a `100 G_PER_L` ingredient alongside the base's flattened ingredients.

4. **Major - gas and anaerobic growth context are under-modeled.** The source has 100% CO2 as a top-level gas component and notes either Bellco tubes under 100% CO2 or an anaerobic cabinet with 10% CO2, 10% H2, and 80% N2 at 37 C. The YAML defaulted CO2 to a `variable` concentration and has no preparation or incubation context.

5. **Minor - source references are not structured.** TOGO M2789 is recoverable from `media_term` and `notes`, but the inspected TOGO source is not represented as a structured `references` entry.

## Recommended Edits

- In `data/normalized_yaml/bacterial/m2sgc_broth_containing_tetracycline_10_g_ml_or_rifampin_100_g_ml.yaml`, correct tetracycline to 10 ug/ml / 0.01 g/L and represent the 100 ug/ml / 0.1 g/L rifampin alternative explicitly.
- Preserve the nested M2SGC-base boundary and scale or scope its per-100-ml ingredients correctly; remove `M2SGC medium` as a weighed final ingredient.
- Convert the M2SGC-base water, rumen fluid, and solute amounts from source per-100-ml units without treating milliliters as grams or milligrams as grams.
- Replace the default `CO2` variable concentration with source-backed atmosphere details and add anaerobic 37 C growth context where the schema permits it.
- Add a structured source reference for TOGO M2789.
- Regenerate merged YAML and rerun open schema, strict, reference, and term validation.

## Follow-up Checks

- Reinspect the TOGO M2789 API to confirm tetracycline, rifampin, CO2, M2SGC per-100-ml ingredients, and the Bellco-tube/anaerobic-cabinet atmosphere text are represented after curation.
- Rerun open schema, strict, term, and reference validation on the regenerated `m2sgc_broth_containing_tetracycline_10_g_ml_or_rifampin_100_g_ml.yaml`.

## Additional Notes

The exact search included ignored files. Archived validation rows still contain the owner's former filename with the source microgram symbol; the current maintained and generated filenames have normalized that symbol away as plain `g_ml`.
