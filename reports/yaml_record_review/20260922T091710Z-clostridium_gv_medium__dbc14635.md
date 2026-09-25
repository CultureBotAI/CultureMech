# YAML Record Review: CLOSTRIDIUM (GV) MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_gv_medium__dbc14635.yaml`
- Started UTC: `2026-09-22T09:17:10Z`
- Finished UTC: `2026-09-22T09:17:21Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:001628` for MediaDive medium `500`, DSMZ Medium 500 `CLOSTRIDIUM (GV) MEDIUM`. The generated record merges 10 MediaDive/KOMODO source recipes on merge fingerprint `dbc1463504d241c23d90f0d570dc5c2e6382fb85e6418fa3d84d540588725e67`, with `data/normalized_yaml/bacterial/clostridium_gv_medium.yaml` as the canonical branch.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_gv_medium__dbc14635.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The main record identity is correct: it names DSMZ Medium 500, links to `mediadive.medium:500`, and keeps the source URL for `DSMZ_Medium500.pdf`.

Ingredient grounding is mostly chemically specific. `NiCl2 x 6 H2O` remains grounded to generic nickel dichloride, and `Calcium D-(+)-pantothenate` has a primary CHEBI term but no `mediaingredientmech_chebi_term`.

The merged-source identity is too broad. KOMODO sources for `medium_500_modified_for_dsm_10612`, `medium_500_modified_for_dsm_9179`, `substrate_for_dsm_5704`, `substrate_for_dsm_6222`, and other DSMZ 500 substrates are folded into a `SOURCE_DUPLICATE` group, but DSMZ Medium 500 documents strain-specific modifications that affect glucose, carbon source, or pH. Those source identities should be reconciled against structured MediaVariant records, not only hidden in `synonyms`.

## Evidence

The DSMZ Medium 500 PDF supports the generic base formula, pH 7.0-7.2, and the anoxic preparation text copied into `preparation_steps[0]`.

The PDF also shows that Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x) are independent one-liter stock recipes. Only 1 ml of each is added to the final medium. The generated record instead lists the internals of those stocks as ordinary final `ingredients`.

The DSMZ variant notes say to replace glucose with 2 g/l sodium crotonate for DSM 5704, replace glucose with 6 g/l trisodium citrate for DSM 6222, adjust the complete medium to pH 6.5-6.7 for DSM 9179, and reduce glucose to 2 g/l for DSM 9187 and DSM 10612.

## Completeness

The record carries the source pH and the main DSMZ anaerobic autoclaving paragraph, but it is incomplete as a structured stock/variant representation:

- There is no `solutions` entry for Trace element solution SL-10.
- There is no `solutions` entry for Selenite-tungstate solution.
- There is no `solutions` entry for Wolin's vitamin solution (10x).
- The 10 merged source records collapse DSMZ-specific variants into one duplicate group.
- No `target_organisms` or strain-specific variant organism context was retained.

## Findings

- Trace element solution SL-10 internals are stored at one-liter stock concentration in the final ingredient list: `HCl` `2.5 G_PER_L`, `FeCl2 x 4 H2O` `1.5 G_PER_L`, `ZnCl2` `0.07 G_PER_L`, `MnCl2 x 4 H2O` `0.1 G_PER_L`, `CoCl2 x 6 H2O` `0.19 G_PER_L`, `CuCl2 x 2 H2O` `0.002 G_PER_L`, `NiCl2 x 6 H2O` `0.024 G_PER_L`, and `Na2MoO4 x 2 H2O` `0.036 G_PER_L`. Because the stock is dosed at only 1 ml/l final medium, these values are about 1000-fold higher than their final-medium contributions.
- Selenite-tungstate solution internals have the same stock-vs-final defect. `NaOH`, `Na2SeO3 x 5 H2O`, and `Na2WO4 x 2 H2O` are present as final ingredients at `0.5`, `0.003`, and `0.004 G_PER_L`, respectively, although DSMZ uses them to make a stock added at 1 ml/l.
- Wolin vitamin stock internals are flattened into final `ingredients`. `Biotin` and `Folic acid` at `0.02 G_PER_L`, `Pyridoxine hydrochloride` at `0.1 G_PER_L`, `Vitamin B12` at `0.001 G_PER_L`, and the other vitamin rows should be components of a 10x vitamin stock added at 1 ml/l.
- DSMZ 500 variant instructions are lost. The merged record keeps only base `D-Glucose` near 5 g/l and pH 7.0-7.2 even though its merged KOMODO sources include DSM 5704, DSM 6222, DSM 9179, and DSM 10612 variant names.
- The `parent_media` relationship points at `data/normalized_yaml/bacterial/gv_medium.yaml`, a duplicate KOMODO source, instead of using DSMZ Medium 500 as the parent for true strain variants.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/clostridium_gv_medium.yaml`, the KOMODO duplicate records, or the MediaDive/KOMODO stock import logic, then regenerate; `data/merge_yaml/merged/clostridium_gv_medium__dbc14635.yaml` is derived.
- Represent Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x) as `solutions[*]` with their stock compositions and 1 ml/l aliquots.
- Keep final-medium ingredients limited to the DSMZ base formula plus correctly diluted resazurin and FeSO4 contributions if those aliquots are intentionally flattened.
- Model DSM 5704, DSM 6222, DSM 9179, DSM 9187, and DSM 10612 modifications as explicit variants with their source changes.
- Re-ground `NiCl2 x 6 H2O` to a nickel chloride hexahydrate term and add the missing MediaIngredientMech CHEBI link for calcium pantothenate if a matching ingredient term exists.
- Reconcile this branch with the TOGO `M2475` branch so DSMZ Medium 500 is not emitted as two generic GV medium records.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm all trace, selenite-tungstate, and vitamin stock internals live only in stock solution compositions.
- Confirm `substrate_for_dsm_5704` contains sodium crotonate instead of glucose and `substrate_for_dsm_6222` contains trisodium citrate instead of glucose.
- Confirm the DSM 9179 pH 6.5-6.7 and DSM 9187 / DSM 10612 glucose 2 g/l modifications survive as structured variant data.
- Confirm the GV medium TOGO and MediaDive/KOMODO imports merge after stock and variant modeling are fixed.

## Additional Notes

Empty optional fields are not defects. The record is closer to DSMZ Medium 500 than the TOGO import because the base formula, pH, resazurin aliquot, FeSO4 aliquot, and primary anaerobic instructions are preserved, but the flattened stock recipes still make the final formula chemically misleading.
