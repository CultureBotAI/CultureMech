# YAML Record Review: Hypnocyclicus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hypnocyclicus_medium__6678e3cd.yaml
- Started UTC: 2026-09-23T14:16:45Z
- Finished UTC: 2026-09-23T14:17:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:001151 |
| Name | hypnocyclicus_medium |
| Original name | HYPNOCYCLICUS MEDIUM |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| pH | 6.8-7.2 |
| Source identity | MediaDive / DSMZ Medium 1667 |
| Generated path reviewed | data/merge_yaml/merged/hypnocyclicus_medium__6678e3cd.yaml |
| Maintained owner | data/normalized_yaml/bacterial/hypnocyclicus_medium.yaml |

The reviewed file is a generated merge from the maintained MediaDive import
above. Future fixes should update `data/normalized_yaml/bacterial/hypnocyclicus_medium.yaml`
or the MediaDive stock-nesting/import logic and then regenerate
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hypnocyclicus_medium__6678e3cd.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hypnocyclicus_medium__6678e3cd.yaml --out /private/tmp/hypnocyclicus_medium__6678e3cd.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hypnocyclicus_medium__6678e3cd.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hypnocyclicus_medium__6678e3cd.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is coherent for DSMZ Medium 1667: the stable ID,
  `hypnocyclicus_medium` slug, HYPNOCYCLICUS MEDIUM label, bacterial category,
  and `mediadive.medium:1667` grounding all describe the same MediaDive/DSMZ
  source recipe.
- A gitignore-independent exact search for `CultureMech:001151` over this
  maintained YAML, this generated YAML, the ID registry, MediaDive/bacterial
  indexes, and the media content-review manifest found this record and its
  generated index or manifest entries.
- A gitignore-independent exact search for `mediadive.medium:1667` over
  maintained bacterial records, generated merged records, and the MediaDive and
  bacterial indexes found only this DSMZ 1667 import.
- The CHEBI groundings for the direct final-medium salts and the visible stock
  components mostly match the source chemical forms; yeast extract remains an
  explicit unresolved complex material, which is acceptable.
- `NaNO3` carries an old `mediaingredientmech_term`, but its primary term is
  already the exact CHEBI sodium nitrate identifier.

## Evidence

- The direct final-medium rows for Na2SO4, KH2PO4, NH4Cl, NaCl, MgCl2 x 6 H2O,
  KCl, CaCl2 x 2 H2O, NaNO3, yeast extract, sodium resazurin 0.1% w/v,
  Na2CO3, and Na2S x 9 H2O match the DSMZ PDF and the inspected MediaDive
  payload.
- DSMZ and MediaDive list 1 ml/L Trace element solution SL-10 and 1 ml/L Seven
  vitamins solution in the final medium. The generated YAML has no `solutions`
  block and instead keeps all Trace element solution SL-10 and Seven vitamins
  solution constituents as final-medium ingredients at stock strength.
- DSMZ and MediaDive list 1000 ml distilled water for the final medium, 990 ml
  distilled water for Trace element solution SL-10, and 1000 ml distilled
  water for Seven vitamins solution. None of those water rows appears in the
  generated YAML.
- The generated YAML includes the Trace element solution SL-10 preparation
  sentence as a top-level `DISSOLVE` step even though the generated record has
  no nested Trace element solution to own it.
- The maintained normalized YAML has an Aug 7, 2026
  `NESTED_FLATTENED_COCKTAIL` event that moved FeCl2 x 4 H2O and four
  vitamins into two stock solutions. The reviewed merged YAML was generated on
  Aug 6, 2026, so it is stale and lacks even that partial repair.
- The Aug 7 repair is still incomplete upstream: HCl, ZnCl2, MnCl2 x 4 H2O,
  H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O,
  p-Aminobenzoic acid, D-(+)-biotin, and Calcium pantothenate remain
  top-level final ingredients in the maintained YAML.

## Completeness

- Both source stock solutions need complete nested compositions at 1 ml/L
  instead of stock-strength top-level ingredients.
- The three distilled-water rows are missing from the generated record.
- The Trace element solution SL-10 preparation step should be attached to that
  stock solution, not to the final medium.
- The generated merge needs to be regenerated after the maintained normalized
  YAML is completed.
- Empty optional fields for target organisms, synonyms, variants, direct
  publication references, discussions, and quality flags are acceptable for
  this provider import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated final medium flattens both DSMZ stock solutions into top-level final ingredients at stock strength. | DSMZ/MediaDive add 1 ml/L Trace element solution SL-10 and 1 ml/L Seven vitamins solution; the generated YAML has no `solutions` block and top-level HCl, trace-metal, and vitamin ingredients instead. | `data/normalized_yaml/bacterial/hypnocyclicus_medium.yaml`; MediaDive cocktail nesting. |
| Major | The normalized stock-nesting repair is partial even upstream. | The maintained Aug 7 `NESTED_FLATTENED_COCKTAIL` event moved only FeCl2 x 4 H2O and four vitamins, leaving eight Trace element solution SL-10 rows and three Seven vitamins solution rows as final ingredients. | `data/normalized_yaml/bacterial/hypnocyclicus_medium.yaml`; `apply_cocktail_nesting.py`. |
| Major | All source water rows are omitted. | DSMZ lists 1000 ml final-medium water, 990 ml Trace element solution water, and 1000 ml Seven vitamins solution water; none is present in the generated YAML. | `data/normalized_yaml/bacterial/hypnocyclicus_medium.yaml`; MediaDive import and cocktail nesting. |
| Major | The generated merge is stale relative to the maintained normalized file. | The generated curation history ends with an Aug 6 merge event, while the maintained file has an Aug 7 stock-nesting event and `solutions` blocks that do not appear in the generated file. | Merge regeneration for `data/merge_yaml/merged/hypnocyclicus_medium__6678e3cd.yaml`. |
| Minor | The Trace element solution SL-10 preparation step is scoped to the final medium. | The `DISSOLVE` step describes preparing the 1000 ml SL-10 stock, but it appears as final-medium step 2 in a record with no nested SL-10 solution. | `data/normalized_yaml/bacterial/hypnocyclicus_medium.yaml`; MediaDive preparation-step import. |

## Recommended Edits

1. Complete the Trace element solution SL-10 and Seven vitamins solution
   nesting in `data/normalized_yaml/bacterial/hypnocyclicus_medium.yaml`.
2. Restore the final-medium, Trace element solution SL-10, and Seven vitamins
   solution distilled-water rows at their source volumes.
3. Move the SL-10 preparation note under the nested SL-10 solution and keep the
   final-medium anoxic dispensing, autoclave, stock-addition, filtration, and
   pH-adjustment instructions on the parent recipe.
4. Regenerate `data/merge_yaml/merged/` so the merged YAML reflects the
   corrected normalized recipe.
5. Refresh any MediaDive cocktail-nesting rule that caused the Aug 7 repair to
   move only 5 of the 16 stock-strength rows.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  DSMZ 1667 merged record.
- Manually compare the regenerated parent medium, Trace element solution SL-10,
  and Seven vitamins solution against the DSMZ 1667 PDF and MediaDive 1667
  REST payload.
- Verify that no source DSMZ 1667 stock-strength rows remain as top-level
  final-medium ingredients.
- Rerun the merge-freshness audit after regeneration.

## Additional Notes

- The major scientific error is stock flattening and stale generation; the
  source identity, pH range, liquid complex classification, and direct grams in
  the final medium are otherwise coherent for DSMZ 1667.
