# YAML Record Review: CLOSTRIDIUM KN MEDIUM (HYDROXYBENZOATE)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_kn_medium_hydroxybenzoate.yaml`
- Started UTC: `2026-09-22T09:22:31Z`
- Finished UTC: `2026-09-22T09:22:42Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:001624` for MediaDive medium `497`, DSMZ Medium 497 `CLOSTRIDIUM KN MEDIUM (HYDROXYBENZOATE)`. The generated record merges five MediaDive/KOMODO source recipes on merge fingerprint `7b03f21669da57893235d69b31a4f6d42474d0591333cc4cd592451bad60fce6`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_kn_medium_hydroxybenzoate.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The main MediaDive identity is correct for DSMZ Medium 497, and the record preserves the DSMZ pH range 7.1-7.4.

The merged KOMODO duplicate set is too coarse. DSMZ Medium 497 documents strain-level modifications for DSM 5672 and DSM 5673, but `for_dsm_5672_strain_wo021` and `for_dsm_5673_strain_kn032` were merged into the base hydroxybenzoate medium as `SOURCE_DUPLICATE` synonyms. The generated `parent_media` also points to `data/normalized_yaml/bacterial/hydroxybenzoate_medium.yaml`, a duplicate KOMODO source whose pH is 7.2-7.5 and whose notes say `Aerobic: Yes`.

`2,4-Dihydroxybenzoic acid` is unresolved in the ingredient list. `NiCl2 x 6 H2O` remains grounded to generic nickel dichloride, and `Calcium D-(+)-pantothenate` has a primary CHEBI term but no `mediaingredientmech_chebi_term`.

## Evidence

The DSMZ Medium 497 PDF defines the final medium as 952 ml Solution A, 30 ml Solution B, 1 ml Solution C, 10 ml Solution D, and 10 ml Solution E. It then defines Solution A with salts, Trace element solution SL-10, Selenite-tungstate solution, resazurin, and water; Solution B with 1.5 g Na2CO3 in 30 ml water; Solution C as 1 ml Wolin's vitamin solution; Solution D with 0.40 g 2,4-Dihydroxybenzoic acid in 10 ml water; and Solution E with 0.40 g Na2S x 9 H2O in 10 ml water.

The PDF also shows DSMZ variants: DSM 5672 replaces 2,4-dihydroxybenzoic acid with 0.15 g/l salicylic acid and DSM 5673 replaces it with 0.75 g/l 3-hydroxybenzoic acid.

The ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found only this generated DSMZ/KOMODO branch for exact DSMZ Medium 497 identifiers and source URLs; ignored files were included.

## Completeness

The record is missing the source solution hierarchy:

- There is no Solution A/B/C/D/E structure even though the preparation step references B through E by name.
- Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution are flattened rather than represented as nested stock solutions.
- DSM 5672 and DSM 5673 variant substitutions are not retained as structured MediaVariant records.
- No target organism entries connect the DSM 5671, DSM 5672, or DSM 5673 strain-specific KOMODO sources to the source variants.

## Findings

- Solution B, D, and E stock concentrations are stored as final concentrations: `Na2CO3` is `50 G_PER_L`, `2,4-Dihydroxybenzoic acid` is `40 G_PER_L`, and `Na2S x 9 H2O` is `40 G_PER_L`, exactly matching 1.5 g/30 ml, 0.40 g/10 ml, and 0.40 g/10 ml stocks instead of their final-medium contributions.
- Solution A salt concentrations are stored at their concentration within the 952 ml Solution A aliquot, not in the completed 1003 ml final medium. For example, DSMZ lists 1.50 g Na2SO4 in Solution A, and the record stores `1.57563 G_PER_L`, corresponding to 1.50 g divided by 0.952 l.
- Trace element solution SL-10 internals are flattened at stock strength into the final formula, including `FeCl2 x 4 H2O` `1.5 G_PER_L`, `ZnCl2` `0.07 G_PER_L`, `MnCl2 x 4 H2O` `0.1 G_PER_L`, `CoCl2 x 6 H2O` `0.19 G_PER_L`, and `NiCl2 x 6 H2O` `0.024 G_PER_L`.
- Selenite-tungstate and Wolin vitamin stock internals are also flattened; examples include `Na2SeO3 x 5 H2O` `0.003 G_PER_L`, `Na2WO4 x 2 H2O` `0.004 G_PER_L`, `Biotin` `0.02 G_PER_L`, `Pyridoxine hydrochloride` `0.1 G_PER_L`, and `Vitamin B12` `0.001 G_PER_L`.
- KOMODO DSM 5672 and DSM 5673 variant sources were merged without the DSMZ salicylic-acid and 3-hydroxybenzoic-acid substitutions, leaving every synonym with the base 2,4-dihydroxybenzoate signature.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/clostridium_kn_medium_hydroxybenzoate.yaml`, the KOMODO duplicates, or the import logic for DSMZ solution assemblies, then regenerate; `data/merge_yaml/merged/clostridium_kn_medium_hydroxybenzoate.yaml` is derived.
- Represent Solution A through Solution E explicitly with their source aliquot volumes.
- Preserve Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution as stock recipes under the appropriate parent solution or final-medium aliquot.
- Correct the final formula so stock concentrations from Solutions A through E are not misread as final grams per liter.
- Resolve `2,4-Dihydroxybenzoic acid`, re-ground `NiCl2 x 6 H2O` to nickel chloride hexahydrate, and add the missing CHEBI-keyed MediaIngredientMech link for calcium pantothenate if available.
- Model DSM 5672 and DSM 5673 as variants with the salicylic-acid and 3-hydroxybenzoic-acid substitutions from DSMZ.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the generated record has an explicit A/B/C/D/E assembly or equivalent aliquot representation.
- Confirm no SL-10, selenite-tungstate, or Wolin vitamin internal is present as a top-level final-medium ingredient.
- Confirm DSM 5672 and DSM 5673 no longer collapse onto the base 2,4-dihydroxybenzoate fingerprint.
- Confirm the KOMODO `Aerobic: Yes` duplicate does not override DSMZ's anoxic preparation semantics.

## Additional Notes

Empty optional fields are not defects. This is a defined medium, so the unresolved hydroxybenzoate ingredient and the concentration errors are especially important: downstream chemical consumers will otherwise treat concentrated stocks and alternate substrates as the actual final formula.
