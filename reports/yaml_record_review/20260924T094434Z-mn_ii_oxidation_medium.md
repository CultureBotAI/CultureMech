# YAML Record Review: mn_ii_oxidation_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/mn_ii_oxidation_medium.yaml
- Started UTC: 2026-09-24T09:43:48Z
- Finished UTC: 2026-09-24T09:44:34Z
- Verdict: needs curation

## Target

Generated bacterial recipe for `CultureMech:008735`, `mn_ii_oxidation_medium`, from `TOGO:M2140` / `NBRC_M1481`.

The generated file contains one source recipe, `mn_ii_oxidation_medium`, merged from `data/normalized_yaml/bacterial/mn_ii_oxidation_medium.yaml`.

## Validation

Open LinkML validation passed with `No issues found`.

Strict schema-layer validation passed with 0 error rows; `/private/tmp/mn_ii_oxidation_medium.strict.tsv` contained only the header line.

Reference validation passed, but performed 0 checks.

Term validation passed. The run emitted the expected `eutils` / `pkg_resources` deprecation warning before `Validation passed`.

Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries inside generated YAML.

## Identity and Grounding

The medium identity is correct: TOGO `M2140` imports NBRC medium 1481 as `Mn(II) oxidation medium`.

The manganese chloride tetrahydrate grounding to `CHEBI:86368` matches the NBRC and TOGO ingredient string.

The generated record is stale relative to its normalized owner. `data/normalized_yaml/bacterial/mn_ii_oxidation_medium.yaml` has already corrected the source units, pH, references, and missing ingredient terms, but the generated file still reflects the older August merge output.

## Evidence

TOGO `M2140` and the NBRC medium 1481 HTML agree on the full formula: 1 g peptone, 0.5 g yeast extract, 36 mg `MnCl2 x 4H2O`, 1 L distilled water, 15 g agar if needed, and pH 7.0.

The normalized owner file now stores that evidence directly. It records `ph_value: 7.0`, distilled water as `1.0 L`, manganese chloride tetrahydrate as `36.0 MG_PER_L`, agar as `15.0 G_PER_L`, and peptone as `1.0 G_PER_L`, with TOGO and NBRC references.

The generated file has merge metadata from 2026-08-06, while the normalized owner has a 2026-09-12 `RESOLVED_TOGO_M2140_SCORE15` repair noting the corrected water and manganese chloride hydrate units, source pH, and ingredient groundings.

## Completeness

The generated record has all five source ingredients but the water and manganese units are wrong.

The source pH is missing from the generated record despite being present in TOGO, NBRC, and the repaired normalized YAML.

The generated record also omits the repaired owner-file references, `ingredients_curated` / `has_ontology_mappings` flags, and exact terms for yeast extract, agar, and peptone.

No target organism, incubation temperature, atmosphere, or growth evidence is present in TOGO M2140 or NBRC medium 1481, so those absences are not defects for this source-only import.

## Findings

1. Needs curation: the generated record overstates `MnCl2 x 4H2O` by 1000-fold. NBRC and TOGO list 36 mg in 1 L, and the repaired normalized owner stores `36.0 MG_PER_L`, but `data/merge_yaml/merged/mn_ii_oxidation_medium.yaml` stores `36 G_PER_L`.

2. Needs curation: the generated record is stale after a normalized-record repair. It was merged on 2026-08-06 and has not picked up the 2026-09-12 `repair_togo_m2140_mn_ii_score15.py` corrections.

3. Minor: the generated water row stores `1 G_PER_L`; the source row is 1 L and the normalized owner now stores `1.0 L`.

4. Minor: pH 7.0 is absent from the generated record.

5. Minor: agar, peptone, and yeast extract groundings present in the normalized owner are absent from the generated output.

## Recommended Edits

Regenerate `data/merge_yaml/merged/mn_ii_oxidation_medium.yaml` from the current normalized record so the September unit, pH, reference, and grounding repair is reflected in generated YAML.

Keep `MnCl2 x 4H2O` at `36.0 MG_PER_L`, distilled water at `1.0 L`, agar at `15.0 G_PER_L`, peptone at `1.0 G_PER_L`, and yeast extract at `0.5 G_PER_L`.

Preserve pH 7.0 and the TOGO/NBRC source references during the merge.

## Follow-up Checks

Re-run open LinkML, strict, reference, and term validation after regeneration.

Diff the regenerated file against `data/normalized_yaml/bacterial/mn_ii_oxidation_medium.yaml` before accepting it; for this single-source record, differences should be limited to merge metadata.

## Additional Notes

No GitHub issues or PR comments were created by this record review.

All searches used to locate the source and generated records included ignored files via `find` or `rg --no-ignore --hidden`.
