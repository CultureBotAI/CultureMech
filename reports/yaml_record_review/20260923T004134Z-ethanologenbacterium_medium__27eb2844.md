# YAML Record Review: ETHANOLOGENBACTERIUM MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ethanologenbacterium_medium__27eb2844.yaml
- Started UTC: 2026-09-23T00:38:40Z
- Finished UTC: 2026-09-23T00:41:34Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/ethanologenbacterium_medium__27eb2844.yaml` is the generated direct JCM/MediaDive record for `mediadive.medium:J483`. The maintained owner is `data/normalized_yaml/bacterial/ethanologenbacterium_medium.yaml`.

The generated file and owner both still have the same flattened stock representation, so fixes belong in the normalized owner or in the JCM/MediaDive import logic rather than only in generated output.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/ethanologen_j483.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `mediadive.medium:J483` media term and JCM 483 source link identify ETHANOLOGENBACTERIUM MEDIUM correctly.

An ignored-file-inclusive exact local search found a second generated record, `data/merge_yaml/merged/ETHANOLOGENBACTERIUM_MEDIUM.yaml`, from TOGO M484 / JCM M483. That sibling is an older TOGO import with two empty `Unknown solution` shells, while this direct JCM record has the stock constituents but flattens them.

Most small-molecule groundings are plausible. `MnSO4 x n H2O` is intentionally grounded only to manganese(II) sulfate because the hydration state is unspecified.

## Evidence

JCM Medium 483 and MediaDive J483 describe a 1020 ml main solution with:

- 10 g glucose, 4 g tryptone, 2 g beef extract, 1 g yeast extract, 4 g NaCl, 1.5 g K2HPO4, 0.1 g FeSO4 x 7 H2O, 0.2 g MgCl2 x 6 H2O, and 0.5 g L-cysteine HCl x H2O.
- 10 ml Microelement solution.
- 10 ml Vitamin solution.
- 1 L distilled water.

The Microelement solution is a separate 1 L stock with manganese sulfate, zinc sulfate, boric acid, nitrilotriacetic acid, calcium chloride, sodium molybdate, cobalt chloride, potassium aluminium sulfate, and distilled water. The Vitamin solution is another 1 L stock with cyanocobalamin, ascorbic acid, riboflavin, citric acid, pyridoxine hydrochloride, folic acid, p-aminobenzoic acid, creatine, and distilled water.

## Completeness

The base ingredients are represented at MediaDive-normalized concentrations for a 1020 ml main solution. The two stocks are not represented as stocks, so the record cannot reconstruct the source preparation: every microelement and vitamin stock constituent appears as if it were added directly to the final medium.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | `Microelement solution` is flattened into final-medium ingredients at stock strength. | JCM adds 10 ml microelement stock to 1 L water plus base ingredients and vitamin stock; the generated file lists stock rows such as `4.5 G_PER_L` nitrilotriacetic acid and `0.2 G_PER_L` CoCl2 x 6 H2O as top-level final ingredients. | Move the eight microelement stock constituents under a `Microelement solution` nested at 10 ml per 1020 ml main solution. |
| Major | `Vitamin solution` is flattened into final-medium ingredients at stock strength. | JCM adds 10 ml vitamin stock after autoclaving; the generated file lists cyanocobalamin, ascorbic acid, riboflavin, citric acid, pyridoxine, folic acid, p-aminobenzoic acid, and creatine as top-level `G_PER_L` rows. | Move the vitamin rows under a filter-sterilized `Vitamin solution` nested at 10 ml per 1020 ml main solution. |
| Major | The direct JCM import has not been reconciled with the TOGO M484 import for the same JCM formula. | `ETHANOLOGENBACTERIUM_MEDIUM.yaml` and `ethanologenbacterium_medium__27eb2844.yaml` are both generated from JCM Medium 483 but remain separate records with different CultureMech IDs and different artifact shapes. | Merge or alias TOGO M484 and JCM J483 after repairing stock modeling. |
| Minor | BD-Difco source attributes were dropped from undefined complex ingredients. | The JCM formula specifies BD-Difco for tryptone, beef extract, and yeast extract; the generated direct record keeps only bare `Tryptone`, `Beef extract`, and `Yeast extract` labels. | Preserve these product attributes in ingredient notes or names. |
| Minor | pH is reduced to a midpoint scalar. | JCM instructs adjustment to pH 4.5-6.5; the record has `ph_value: 5.5`, although the preparation text still preserves the range. | Prefer an explicit pH range if the schema supports it, or keep the range prominently in preparation text. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/ethanologenbacterium_medium.yaml`, add a 10 ml Microelement solution and a 10 ml filter-sterilized Vitamin solution with the JCM stock formulas.
2. Remove the microelement and vitamin stock constituents from top-level `ingredients`.
3. Preserve BD-Difco attributes for tryptone, beef extract, and yeast extract.
4. De-duplicate the direct JCM and TOGO M484 records once both are represented with equivalent stock structure.
5. Regenerate the merged YAML and confirm the `27eb2844` output no longer has the stock constituents as top-level final-medium rows.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated JCM record.
- Confirm the regenerated recipe has two nested solutions, each added at 10 ml.
- Confirm cyanocobalamin, nitrilotriacetic acid, and CoCl2 x 6 H2O are nested inside their stocks rather than direct final ingredients.
- Confirm only one generated Ethanologenbacterium record remains unless there is a deliberate reason to keep TOGO M484 and MediaDive J483 separate.

## Additional Notes

None found.
